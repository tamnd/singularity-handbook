"""The checks of `shb check`.

A fault fails the check:
- the map (tamnd/singularity) is not found;
- a volume has no volume.yaml, or the file has no title;
- a section has no title, no status, a status that is not drafted, checked or reviewed, no drafted_by, or the
  status reviewed with an empty reviewed_by;
- a section does not open with a ## heading;
- a tag in `nodes` or on a Node line is not a node of the map;
- a key in `sources` is not a paper of the map;
- a line starts with "Node:" and does not have the form of a Node line;
- a Node line marks a Lean name as "the statement only", and records/lean.json exists and does not have
  the name;
- an en dash, an em dash or a word of the banned list in the prose.

A warning does not fail the check:
- a tag on a Node line is not in the `nodes` of its section;
- the Lean name on a Node line is not the lean.statement or lean.proof of the node;
- a theorem, proposition, lemma or corollary has no Node line and no Lean line under it.
"""

from __future__ import annotations

import os
import re

from .content import STATUSES, Volume, front, read
from .map import Map
from .md import _FENCE, _STMT, NODE

BANNED = (r"\b(leverag(?:e|es|ed|ing)|showcas(?:e|es|ed|ing)|powerful|elegant(?:ly)?|seamless(?:ly)?|crucial(?:ly)?|"
          r"delv(?:e|es|ed|ing)|journey|landscape|tapestry|realm|intricate|pivotal|robust|underscores?|"
          r"notably|furthermore|moreover)\b")
_ANY_NODE = re.compile(r"^(?:>\s*)?Node:\s*([^\s·,;]+)")


def _prose(t: str) -> str:
    p = re.sub(r"```.*?```|\$\$.*?\$\$|\$[^$\n]*\$|`[^`\n]*`", " ", t, flags=re.S)
    return re.sub(r"\]\([^)]*\)", "]", p)


def _style(rel: str, text: str, faults: list[str]):
    prose = _prose(text)
    for w in sorted(set(re.findall(BANNED, prose, flags=re.I))):
        faults.append(f"{rel}: style: the word '{w}'")
    if re.search("[\u2013\u2014]", prose):
        faults.append(f"{rel}: style: an en dash or an em dash")


def _body(rel: str, body: str, offset: int, fm_nodes: set, smap: Map, faults: list[str], warns: list[str]):
    fence = None
    open_stmt = None     # (line, kind) of a theorem-like statement with no Node line yet
    for i, ln in enumerate(body.split("\n"), offset):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
            continue
        if fence:
            continue
        sm = _STMT.match(ln)
        if sm or ln.startswith("#"):
            if open_stmt:
                warns.append(f"{rel}:{open_stmt[0]}: {open_stmt[1]} with no Node line")
            open_stmt = (i, sm.group(1)) if sm and sm.group(1) in ("Theorem", "Proposition", "Lemma",
                                                                    "Corollary") else None
            continue
        if re.match(r"^\*?Lean:", ln):
            open_stmt = None
            continue
        a = _ANY_NODE.match(ln)
        if not a and re.match(r"^(?:>\s*)?Node:", ln):
            faults.append(f"{rel}:{i}: a Node line without a tag")
            continue
        if not a:
            continue
        tag = a.group(1)
        quoted = ln.startswith(">")
        if not quoted:
            open_stmt = None
            if not NODE.match(ln):
                faults.append(f"{rel}:{i}: a Node line not of the form 'Node: TAG · Lean: `Name`'")
        node = smap.nodes.get(tag)
        if node is None:
            faults.append(f"{rel}:{i}: the node {tag} is not in the map")
            continue
        if quoted:
            continue
        if tag not in fm_nodes:
            warns.append(f"{rel}:{i}: the node {tag} is not in the nodes of the front matter")
        names = re.findall(r"`([^`]+)`", ln)
        known = {n for n in (node.statement, node.proof) if n}
        for nm in names:
            if known and nm not in known:
                warns.append(f"{rel}:{i}: the Lean name {nm} is not the Lean name of {tag} in the map "
                             f"({', '.join(sorted(known))})")
        if smap.records is not None and "statement only" in ln:
            for nm in names:
                if nm not in smap.records:
                    faults.append(f"{rel}:{i}: the Lean name {nm} is marked as a statement, but it is not in "
                                  f"records/lean.json")
    if open_stmt:
        warns.append(f"{rel}:{open_stmt[0]}: {open_stmt[1]} with no Node line")


def check(volumes: list[Volume], smap: Map, root: str) -> tuple[list[str], list[str]]:
    faults: list[str] = []
    warns: list[str] = []
    if not smap.exists:
        faults.append(f"the map is not found at {smap.root} (give it with --map PATH)")
    for v in volumes:
        vrel = os.path.relpath(v.dir, root)
        vy = os.path.join(v.dir, "volume.yaml")
        if not os.path.exists(vy):
            faults.append(f"{vrel}: no volume.yaml")
        p = os.path.join(v.dir, "intro.md")
        if os.path.exists(p):
            _style(os.path.relpath(p, root), read(p), faults)
        for ch in v.chapters:
            ip = os.path.join(ch.dir, "intro.md")
            if os.path.exists(ip):
                _style(os.path.relpath(ip, root), read(ip), faults)
            for s in ch.sections:
                rel = os.path.relpath(s.path, root)
                text = read(s.path)
                fm, body = front(text)
                offset = text[:len(text) - len(body)].count("\n") + 1
                _style(rel, text, faults)
                for k in ("title", "status", "drafted_by"):
                    if not fm.get(k):
                        faults.append(f"{rel}: the front matter has no {k}")
                st = fm.get("status")
                if st and st not in STATUSES:
                    faults.append(f"{rel}: the status '{st}' is not one of {', '.join(STATUSES)}")
                if st == "reviewed" and not fm.get("reviewed_by"):
                    faults.append(f"{rel}: the status is reviewed and reviewed_by is empty")
                if not re.match(r"\s*## ", body):
                    faults.append(f"{rel}: a section must open with a ## heading")
                fm_nodes = {str(t) for t in fm.get("nodes") or []}
                for t in sorted(fm_nodes):
                    if smap.exists and t not in smap.nodes:
                        faults.append(f"{rel}: the node {t} of the front matter is not in the map")
                for k in fm.get("sources") or []:
                    if smap.exists and str(k) not in smap.papers:
                        faults.append(f"{rel}: the source {k} is not a paper of the map")
                if smap.exists:
                    _body(rel, body, offset, fm_nodes, smap, faults, warns)
    return faults, warns
