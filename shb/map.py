"""The map of tamnd/singularity: the nodes of the blueprint, the paper records and the Lean records.

    blueprint/nodes/SG*.yaml   tag, kind, title, lean.statement, lean.proof
    papers/<Key>.yaml          key, title, authors, year, arxiv
    records/lean.json          the Lean declarations that exist (optional)

The status of a node is computed here, in a simple form. With no records/lean.json, or with a node whose Lean
statement is not in it, the status is "planned". records/lean.json is read in one of these forms:

    {"declarations": {"Singularity.foo": {...}, ...}}
    {"decls": {"Singularity.foo": {...}, ...}}           (the form that tamnd/singularity-lean writes)
    {"Singularity.foo": {...}, ...}
    [{"name": "Singularity.foo", ...}, ...]

A record is a status string, or an object that can have "status" (used as it is) and "sorry" (true when the
proof is not finished).
"""

from __future__ import annotations

import glob
import json
import os
import subprocess
from dataclasses import dataclass, field

import yaml

from .content import read

SITE = "https://singularity.tamnd.com"


def node_url(tag: str) -> str:
    return f"{SITE}/node/{tag}/"


def commit(path: str) -> str:
    try:
        return subprocess.run(["git", "-C", path, "rev-parse", "HEAD"], capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return ""


@dataclass
class Node:
    tag: str
    kind: str
    title: str
    statement: str    # the Lean name of the statement, "" if none
    proof: str        # the Lean name of the proof, "" if none
    hypotheses: list = field(default_factory=list)   # the tags of the named hypotheses that the proof takes


@dataclass
class Paper:
    key: str
    title: str
    authors: list
    year: str
    arxiv: list

    def cite(self) -> str:
        """One line of a list of references, in Markdown."""
        bits = []
        if self.authors:
            bits.append(", ".join(str(a) for a in self.authors))
        bits.append(self.title)
        if self.year and str(self.year) not in self.title:
            bits.append(str(self.year))
        s = ". ".join(b.rstrip(".") for b in bits if b) + "."
        for a in self.arxiv:
            s += f" <https://arxiv.org/abs/{a}>"
        return s


@dataclass
class Map:
    root: str
    nodes: dict[str, Node] = field(default_factory=dict)
    papers: dict[str, Paper] = field(default_factory=dict)
    records: dict[str, object] | None = None   # None: no records/lean.json

    @property
    def exists(self) -> bool:
        return os.path.isdir(os.path.join(self.root, "blueprint", "nodes"))

    @classmethod
    def load(cls, root: str) -> "Map":
        m = cls(root)
        for p in sorted(glob.glob(os.path.join(root, "blueprint", "nodes", "SG*.yaml"))):
            y = yaml.safe_load(read(p)) or {}
            lean = y.get("lean") or {}
            tag = str(y.get("tag") or os.path.basename(p)[:-5])
            m.nodes[tag] = Node(tag, str(y.get("kind") or ""), str(y.get("title") or ""),
                                str(lean.get("statement") or ""), str(lean.get("proof") or ""),
                                [str(h) for h in y.get("hypotheses") or []])
        for p in sorted(glob.glob(os.path.join(root, "papers", "*.yaml"))):
            y = yaml.safe_load(read(p)) or {}
            key = str(y.get("key") or os.path.basename(p)[:-5])
            arxiv = y.get("arxiv") or []
            m.papers[key] = Paper(key, str(y.get("title") or key), list(y.get("authors") or []),
                                  str(y.get("year") or ""), [str(a) for a in (arxiv if isinstance(arxiv, list) else [arxiv])])
        rp = os.path.join(root, "records", "lean.json")
        if os.path.exists(rp):
            m.records = _records(json.loads(read(rp)))
        return m

    def commit(self) -> str:
        return commit(self.root)

    def status(self, tag: str) -> str:
        n = self.nodes.get(tag)
        if n is None or self.records is None or not n.statement or n.statement not in self.records:
            return "planned"
        rec = self.records[n.statement]
        if isinstance(rec, str) and rec:
            return rec
        if isinstance(rec, dict) and rec.get("status"):
            return str(rec["status"])
        if n.proof and n.proof in self.records:
            prec = self.records[n.proof]
            if not (isinstance(prec, dict) and prec.get("sorry")):
                return "proved-mod" if n.hypotheses else "proved"
        return "open" if n.kind == "conjecture" else "stated"


def _records(data) -> dict:
    for key in ("declarations", "decls"):
        if isinstance(data, dict) and isinstance(data.get(key), (dict, list)):
            data = data[key]
            break
    if isinstance(data, list):
        out = {}
        for r in data:
            if isinstance(r, str):
                out[r] = {}
            elif isinstance(r, dict) and r.get("name"):
                out[str(r["name"])] = r
        return out
    if isinstance(data, dict):
        return data
    return {}
