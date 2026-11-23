"""The content of the handbook: content/<NN-volume>/<NN-chapter>/ with an optional intro.md and one file
NN-<slug>.md per section.

A volume folder has a volume.yaml with title, subtitle and number. A section file has YAML front matter (title,
nodes, sources, status, drafted_by, reviewed_by), and its text starts with a ## heading.
"""

from __future__ import annotations

import glob
import os
import re
from dataclasses import dataclass, field

import yaml

STATUSES = ("drafted", "checked", "reviewed")


def read(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def front(text: str) -> tuple[dict, str]:
    """Split a Markdown file into its YAML front matter and its body."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end > 0:
            return yaml.safe_load(text[4:end]) or {}, text[end + 5:]
    return {}, text


_SLUG = re.compile(r"[^a-z0-9 -]")


def anchor(heading: str) -> str:
    """The anchor of a heading: lower case, spaces become hyphens, other punctuation goes."""
    s = _SLUG.sub("", heading.strip().lower())
    return re.sub(r" +", "-", s).strip("-")


@dataclass
class Section:
    path: str
    fm: dict
    body: str

    @property
    def status(self) -> str:
        return str(self.fm.get("status") or "drafted")

    @property
    def title(self) -> str:
        return str(self.fm.get("title") or "")


@dataclass
class Chapter:
    num: int          # the NN of the folder
    slug: str
    dir: str
    title: str
    intro: str        # intro.md without its # title line
    sections: list[Section] = field(default_factory=list)

    @property
    def status(self) -> str:
        """The lowest status of its sections. A chapter with no sections is a draft."""
        if not self.sections:
            return "drafted"
        rank = min(STATUSES.index(s.status) if s.status in STATUSES else 0 for s in self.sections)
        return STATUSES[rank]

    @property
    def draft(self) -> bool:
        return self.status != "reviewed"

    @property
    def text(self) -> str:
        return "\n\n".join(s.body.strip("\n") for s in self.sections)


@dataclass
class Volume:
    number: int
    dirname: str      # 00-guide
    dir: str
    title: str
    subtitle: str
    intro: str
    chapters: list[Chapter] = field(default_factory=list)

    @property
    def slug(self) -> str:
        return self.dirname[3:]

    @property
    def squares(self) -> list[float]:
        """The cover: one square per chapter, filled by its status."""
        fill = {"drafted": 0.25, "checked": 0.6, "reviewed": 1.0}
        return [fill.get(c.status, 0.0) for c in self.chapters]


def _intro(path: str) -> tuple[str, str]:
    """The title (its # line) and the rest of an intro.md."""
    if not os.path.exists(path):
        return "", ""
    _, body = front(read(path))
    lines = body.lstrip("\n").split("\n")
    if lines and lines[0].startswith("# "):
        return lines[0][2:].strip(), "\n".join(lines[1:]).strip("\n")
    return "", body.strip("\n")


def load_volume(d: str) -> Volume:
    vy = os.path.join(d, "volume.yaml")
    v = (yaml.safe_load(read(vy)) or {}) if os.path.exists(vy) else {}
    base = os.path.basename(d)
    _, vintro = _intro(os.path.join(d, "intro.md"))
    vol = Volume(int(v.get("number", base[:2])), base, d, str(v.get("title") or base[3:].title()),
                 str(v.get("subtitle") or ""), vintro)
    for cdir in sorted(glob.glob(os.path.join(d, "[0-9][0-9]-*"))):
        if not os.path.isdir(cdir):
            continue
        cbase = os.path.basename(cdir)
        title, intro = _intro(os.path.join(cdir, "intro.md"))
        secs = []
        for sp in sorted(glob.glob(os.path.join(cdir, "[0-9][0-9]-*.md"))):
            fm, body = front(read(sp))
            secs.append(Section(sp, fm, body))
        if not secs and not intro and not title:   # a chapter of the plan with nothing written yet
            continue
        if not title:
            title = cbase[3:].replace("-", " ").capitalize()
        vol.chapters.append(Chapter(int(cbase[:2]), cbase[3:], cdir, title, intro, secs))
    return vol


def load(content: str) -> list[Volume]:
    out = []
    for d in sorted(glob.glob(os.path.join(content, "[0-9][0-9]-*"))):
        if os.path.isdir(d):
            out.append(load_volume(d))
    return sorted(out, key=lambda v: v.number)
