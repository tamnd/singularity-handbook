"""shb: build The Singularity Handbook from content/ and the map of tamnd/singularity.

    python -m shb check   [--volume N|all]
    python -m shb number  [--write]
    python -m shb build   [--volume N|all] [--formats tex,pdf,epub] [--out build]

Each command takes --map PATH (default ../singularity, or the environment variable SHB_MAP) and --content PATH
(default content/).
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import shutil
import sys

from .book import Book, out_name
from .paths import ROOT


def edition() -> dict:
    """The file EDITION: 'version 0.1.0' and 'singularity <commit>'."""
    out = {"version": "0.1.0", "singularity": ""}
    p = os.path.join(ROOT, "EDITION")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            k, _, v = line.strip().partition(" ")
            if k:
                out[k] = v.strip()
    return out


def load(args) -> Book:
    book = Book(os.path.abspath(args.content), os.path.abspath(args.map), edition().get("singularity", ""))
    m = book.map
    print(f"map {m.root}: {len(m.nodes)} nodes, {len(m.papers)} papers, "
          f"{'no records/lean.json' if m.records is None else f'{len(m.records)} Lean records'}; "
          f"{len(book.volumes)} volumes", file=sys.stderr)
    return book


def pick(book: Book, which: str):
    if which == "all":
        return list(book.volumes)
    nums = {int(x) for x in which.split(",")}
    out = [v for v in book.volumes if v.number in nums]
    missing = nums - {v.number for v in out}
    if missing:
        raise SystemExit(f"no volume {', '.join(map(str, sorted(missing)))} in {book.content}")
    return out


def cmd_check(args):
    from .check import check
    book = load(args)
    faults, warns = check(pick(book, args.volume), book.map, os.path.dirname(book.content))
    for w in warns:
        print(f"warning: {w}")
    for f in faults:
        print(f)
    print(f"{len(faults)} faults, {len(warns)} warnings", file=sys.stderr)
    return 1 if faults else 0


def cmd_number(args):
    from . import number
    book = load(args)
    number.run(book.volumes, args.write)
    return 0


def cmd_build(args):
    from . import epub, latex
    book = load(args)
    version = edition()["version"]
    date = args.date or datetime.date.today().isoformat()
    fmts = set(args.formats.split(","))
    os.makedirs(args.out, exist_ok=True)
    report = {}
    for v in pick(book, args.volume):
        md, st = book.markdown(v)
        d = os.path.join(args.out, v.dirname)
        os.makedirs(d, exist_ok=True)
        info = dict(st)
        if fmts & {"tex", "pdf"}:
            info.update(latex.build(book, v, md, d, version, date, pdf="pdf" in fmts))
        if "epub" in fmts:
            info.update(epub.build(book, v, md, d, version, date))
        name = out_name(v, version)
        for ext in ("pdf", "epub"):
            src = os.path.join(d, f"main.{ext}")
            if ext in fmts and os.path.exists(src):
                dst = os.path.join(args.out, f"{name}.{ext}")
                shutil.copy(src, dst)
                info[ext] = dst
        err = info.pop("error", None)
        report[v.number] = info
        print(f"volume {v.number} {v.title}: " + json.dumps(info), file=sys.stderr)
        if err:
            print(err, file=sys.stderr)
    json.dump(report, open(os.path.join(args.out, "report.json"), "w"), indent=1)
    bad = [n for n, i in report.items() if i.get("ok") is False or i.get("epub_ok") is False]
    return 1 if bad else 0


def main(argv=None):
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--map", default=argparse.SUPPRESS,
                        help="the checkout of tamnd/singularity (default ../singularity or $SHB_MAP)")
    common.add_argument("--content", default=argparse.SUPPRESS, help="the content folder (default content/)")
    ap = argparse.ArgumentParser(prog="shb", parents=[common])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", parents=[common])
    c.add_argument("--volume", default="all")
    nb = sub.add_parser("number", parents=[common])
    nb.add_argument("--write", action="store_true")
    b = sub.add_parser("build", parents=[common])
    b.add_argument("--volume", default="all")
    b.add_argument("--formats", default="pdf,epub")
    b.add_argument("--out", default=os.path.join(ROOT, "build"))
    b.add_argument("--date", default="")
    args = ap.parse_args(argv)
    if not hasattr(args, "map"):
        args.map = os.environ.get("SHB_MAP") or os.path.join(ROOT, "..", "singularity")
    if not hasattr(args, "content"):
        args.content = os.path.join(ROOT, "content")
    return {"check": cmd_check, "build": cmd_build, "number": cmd_number}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main() or 0)
