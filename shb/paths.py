"""The root of the repository: the folder with tex/, filters/, EDITION and content/.

The package sits in that folder. When it is installed elsewhere, the root is the current folder.
"""

from __future__ import annotations

import os

_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE if os.path.exists(os.path.join(_HERE, "tex", "handbook.sty")) else os.getcwd()
