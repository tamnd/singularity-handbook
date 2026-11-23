"""The volumes of the handbook and the Markdown of each.

A volume is content/<NN-slug>/. Its Markdown is the volume intro.md (if any), then each chapter: a # heading with
the number of the chapter, a Draft mark when the chapter is not reviewed, the chapter intro.md, its sections with
numbered headings and statements, and the list of the papers that its sections cite.
"""

from __future__ import annotations

import re

from . import content
from .content import Chapter, Volume
from .map import Map
from .md import Converter


class Book:
    def __init__(self, content_dir: str, map_dir: str, pin: str = ""):
        self.content = content_dir
        self.map = Map.load(map_dir)
        self.volumes = content.load(content_dir)
        self.map_commit = self.map.commit() or pin or "unknown"

    def volume(self, n: int) -> Volume:
        return next(v for v in self.volumes if v.number == n)

    def markdown(self, v: Volume) -> tuple[str, dict]:
        conv = Converter(self.map)
        out = []
        pre = f"v{v.number}"
        if v.intro.strip():
            out.append(f"# Introduction {{#{pre}-intro}}\n")
            out.append(conv.page(v.intro, shift=0, prefix=f"{pre}-intro"))
        for ch in v.chapters:
            out.append(self._chapter(v, ch, conv))
        md = "\n\n".join(out)
        stats = {"words": len(re.findall(r"\b\w+\b", md)), "nodes": len(conv.nodes),
                 "chapters": len(v.chapters), "drafts": sum(1 for c in v.chapters if c.draft)}
        return md, stats

    def _chapter(self, v: Volume, ch: Chapter, conv: Converter) -> str:
        n = str(ch.num)
        prefix = f"v{v.number}-c{ch.num}"
        out = [f"# {conv.inline(ch.title)} {{#{prefix} num=\"{n}\"}}\n"]
        if ch.draft:
            out.append(draft_mark(ch.status))
        if ch.intro.strip():
            out.append(conv.page(ch.intro, shift=0, prefix=prefix))
        if ch.sections:
            out.append(conv.page(ch.text, shift=0, prefix=prefix, numbering=n))
        refs = self._references(ch)
        if refs:
            out.append(f"## References {{#{prefix}-references}}\n")
            out.append("\n".join(refs) + "\n")
        return "\n\n".join(out)

    def _references(self, ch: Chapter) -> list[str]:
        keys: list[str] = []
        for s in ch.sections:
            for k in s.fm.get("sources") or []:
                if str(k) not in keys:
                    keys.append(str(k))
        out = []
        for k in keys:
            p = self.map.papers.get(k)
            out.append(f"- **{k}**. {p.cite()}" if p else f"- **{k}**.")
        return out


def draft_mark(status: str) -> str:
    """The mark at the start of a chapter that is not reviewed: a box in the PDF (with DRAFT across the first
    page) and a box in the EPUB."""
    return (f"::: {{.draft latex-env=\"hbdraft\"}}\n**Draft.** The status of this chapter is {status}. "
            "No reviewer has signed it yet, and it can contain errors.\n:::\n")


def out_name(v: Volume, version: str) -> str:
    return f"singularity-handbook-{v.dirname}-{version}"
