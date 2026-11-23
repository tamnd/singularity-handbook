"""Write the numbers of the build into the Markdown of the section files.

A statement head **Theorem (Name).** becomes **Theorem 3.2.4 (Name).**: chapter 3 of its volume (the NN of the
chapter folder), section 2 of the chapter (the second ## heading, counted over the section files in order),
statement 4 of the section. So the source on GitHub reads as the book does.

    python -m shb number           # list the files that would change
    python -m shb number --write   # change them
"""

from __future__ import annotations

import re

from .content import read
from .md import _FENCE, _STMT, KINDS

_HEAD = re.compile(r"^(\*\*(?:" + KINDS + r")(?: [a-z]+)?)(?: [0-9]+(?:\.[0-9]+)*)?")


def stamp(text: str, ci: int, sec: int) -> tuple[str, int]:
    """Number the statement heads of one section file. `sec` is the number of ## headings before it in the
    chapter; the new count is returned."""
    out, fence = [], None
    stmt = 0
    for ln in text.split("\n"):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
        elif not fence:
            if re.match(r"^## ", ln):
                sec += 1
                stmt = 0
            elif _STMT.match(ln):
                stmt += 1
                ln = _HEAD.sub(lambda m: f"{m.group(1)} {ci}.{sec}.{stmt}", ln, count=1)
        out.append(ln)
    return "\n".join(out), sec


def run(volumes, write: bool) -> list[str]:
    changed = []
    for v in volumes:
        for ch in v.chapters:
            sec = 0
            for s in ch.sections:
                src = read(s.path)
                fm_end = 0
                if src.startswith("---\n"):
                    fm_end = src.index("\n---\n", 4) + 5
                body, sec = stamp(src[fm_end:], ch.num, sec)
                new = src[:fm_end] + body
                if new != src:
                    changed.append(s.path)
                    if write:
                        with open(s.path, "w", encoding="utf-8") as f:
                            f.write(new)
    for p in changed:
        print(("numbered " if write else "would number ") + p)
    print(f"{len(changed)} files")
    return changed
