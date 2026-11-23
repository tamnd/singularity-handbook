"""Small helpers shared by the writers."""

from __future__ import annotations

import colorsys
import re

_TEX_SPECIAL = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$", "&": r"\&",
                "#": r"\#", "^": r"\textasciicircum{}", "_": r"\_", "%": r"\%", "~": r"\textasciitilde{}"}


def tex(s: str) -> str:
    """Escape plain text for LaTeX; $…$ stays mathematics."""
    out = []
    for i, part in enumerate(re.split(r"(\$[^$]+\$)", s)):
        if i % 2:
            out.append(r"\(" + part[1:-1] + r"\)")
        else:
            out.append("".join(_TEX_SPECIAL.get(c, c) for c in part))
    return "".join(out)


def volume_hue(n: int) -> str:
    """One hue per volume, spread round the wheel with the golden angle, at an even darkness."""
    if n == 0:
        return "34495E"
    h = ((n * 137.508 + 200) % 360) / 360
    r, g, b = colorsys.hls_to_rgb(h, 0.38, 0.55)
    return "%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))
