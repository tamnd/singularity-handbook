"""The conversion of the Markdown of a chapter into the Markdown of a volume.

Each ## heading of a chapter gets a number (2.3) and each bold statement head the number of its section and its
place there: **Theorem (Moh).** becomes Theorem 2.3.1 (Moh). A line `Node: SG... · Lean: `Name`` under a
statement gets a link to the node on the site and the status of the node: "(status: proved)". A link to a path
of the site (/node/SG.../) becomes a link to https://singularity.tamnd.com.
"""

from __future__ import annotations

import re

from .content import anchor
from .map import SITE, Map, node_url

KINDS = "Definition|Theorem|Proposition|Lemma|Corollary|Example|Counterexample|Remark|Conjecture"

_FENCE = re.compile(r"^(`{3,}|~{3,})")
_MATH = re.compile(r"\$\$.*?\$\$|(?<![\\$])\$[^$\n]+\$", re.S)
_LINK = re.compile(r"(?<!!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)")
_STMT = re.compile(r"^\*\*(" + KINDS + r")((?: [a-z]+)?)(?: [0-9]+(?:\.[0-9]+)*)?((?: \((?:[^()]|\([^()]*\))*\))?)\.\*\*")
# Node: SG0000000A · Lean: `Singularity.foo` (status: proved)
NODE = re.compile(r"^Node:\s*(\S+?)(?:\s*·\s*(.*?))?(?:\s*\(status: [a-z-]+\))?\s*$")


def label_id(*parts: str) -> str:
    return "-".join(p for p in parts if p).replace("_", "-")


class Converter:
    """Converts the Markdown of one chapter for one volume."""

    def __init__(self, smap: Map):
        self.map = smap
        self.nodes: list[str] = []     # the tags of the Node lines, in order

    def resolve(self, dest: str, text: str) -> str:
        if dest.startswith("/") and not dest.startswith("//"):
            return f"[{text}]({SITE}{dest})"
        return f"[{text}]({dest})"

    def inline(self, s: str) -> str:
        """Links in one line of prose, outside code and mathematics."""
        keep: list[str] = []

        def hold(m: re.Match) -> str:
            keep.append(m.group(0))
            return f"\x00{len(keep) - 1}\x00"

        s = re.sub(r"`[^`\n]*`", hold, s)
        s = _MATH.sub(hold, s)
        s = _LINK.sub(lambda m: self.resolve(m[2], m[1]), s)
        while "\x00" in s:
            s = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m[1])], s)
        return s

    def node_line(self, tag: str, rest: str | None) -> str:
        """The Node line as the book prints it: a link to the node, the Lean name, the computed status."""
        self.nodes.append(tag)
        parts = [f"Node: [{tag}]({node_url(tag)})"]
        if rest:
            parts.append(self.inline(rest))
        return f"[{' · '.join(parts)} (status: {self.map.status(tag)})]{{.node latex-cmd=\"hblean\"}}"

    def page(self, md: str, *, shift: int, prefix: str, numbering: str | None = None) -> str:
        """Convert a page. `shift` moves every heading down (## becomes ### for shift 1). Headings get the
        identifier `prefix-<anchor>`. With `numbering` ("3"), each ## heading gets a number 3.1, 3.2, and each
        bold statement head the number of its section and its place there: Definition 3.2.1."""
        out, fence = [], None
        sec = stmt = 0
        for ln in md.split("\n"):
            f = _FENCE.match(ln)
            if f:
                fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
                out.append(ln)
                continue
            if fence:
                out.append(ln)
                continue
            m = re.match(r"^(#{1,6}) +(.*?)\s*$", ln)
            if m:
                level = len(m.group(1))
                title = m.group(2)
                lab = label_id(prefix, anchor(title))
                head = "#" * min(6, level + shift)
                if numbering and level == 2:
                    sec += 1
                    stmt = 0
                    out.append(f"{head} {self.inline(title)} {{#{lab} num=\"{numbering}.{sec}\"}}")
                else:
                    out.append(f"{head} {self.inline(title)} {{#{lab}}}")
                continue
            m = _STMT.match(ln)
            if m and numbering:
                stmt += 1
                kind, more, name = m.group(1), m.group(2), m.group(3)
                num = f"{numbering}.{sec}.{stmt}"
                rest = ln[m.end():]
                lab = label_id(prefix, "st", str(sec), str(stmt))
                head = f"[{kind}{more} {num}{self.inline(name)}.]{{latex-cmd=\"hbsthead\"}}"
                if not out or not out[-1].strip():   # a paragraph of its own: a little space above it
                    out.append("```{=latex}\n\\hbstskip\\hbnoindentnext\n```\n")
                out.append(f"[]{{#{lab}}}{head}{self.inline(rest)}")
                continue
            nm = NODE.match(ln)
            if nm:
                out.append(self.node_line(nm.group(1), nm.group(2)))
                continue
            lm = re.match(r"^\*?Lean:\*? (.*)$", ln)
            if lm:
                out.append(f"[Lean: {self.inline(lm.group(1))}]{{.node latex-cmd=\"hblean\"}}")
                continue
            out.append(self.inline(ln))
        return "\n".join(out)
