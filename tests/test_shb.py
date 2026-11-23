"""Tests of shb on the small volume in tests/fixture. They do not need Tectonic. One test needs pandoc and is
skipped without it.

    python -m unittest discover -s tests
    python -m pytest tests
"""

from __future__ import annotations

import io
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from shb import number  # noqa: E402
from shb.__main__ import main  # noqa: E402
from shb.book import Book, out_name  # noqa: E402
from shb.check import check  # noqa: E402
from shb.content import load, read  # noqa: E402
from shb.map import Map  # noqa: E402

FIXTURE = os.path.join(HERE, "fixture")
CONTENT = os.path.join(FIXTURE, "content")
MAP = os.path.join(FIXTURE, "map")


class Tmp(unittest.TestCase):
    """A copy of the fixture that a test can change."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        shutil.copytree(FIXTURE, os.path.join(self.tmp, "fixture"))
        self.content = os.path.join(self.tmp, "fixture", "content")
        self.map = os.path.join(self.tmp, "fixture", "map")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str):
        p = os.path.join(self.content, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)


class TestParse(unittest.TestCase):
    def test_volume(self):
        (v,) = load(CONTENT)
        self.assertEqual((v.number, v.dirname, v.title, v.subtitle), (0, "00-test", "Test", "A small volume for the tests"))
        self.assertEqual([c.num for c in v.chapters], [1, 2])
        first, second = v.chapters
        self.assertEqual(first.title, "The first chapter")
        self.assertEqual(second.title, "Second")
        self.assertEqual(len(first.sections), 2)
        self.assertEqual(first.sections[0].fm["nodes"], ["SG0000000A"])
        self.assertEqual((first.status, first.draft), ("reviewed", False))
        self.assertEqual((second.status, second.draft), ("drafted", True))

    def test_out_name(self):
        (v,) = load(CONTENT)
        self.assertEqual(out_name(v, "0.1.0"), "singularity-handbook-00-test-0.1.0")


class TestStatus(unittest.TestCase):
    def test_with_records(self):
        m = Map.load(MAP)
        self.assertEqual(m.status("SG0000000A"), "proved")
        self.assertEqual(m.status("SG0000000B"), "open")
        self.assertEqual(m.status("SG0000000C"), "planned")

    def test_decls_and_hypotheses(self):
        # The form that tamnd/singularity-lean writes has the key "decls". A node with hypotheses is proved-mod.
        with tempfile.TemporaryDirectory() as d:
            root = os.path.join(d, "map")
            shutil.copytree(MAP, root)
            with open(os.path.join(root, "records", "lean.json"), "w") as f:
                f.write('{"commit": "x", "decls": {"Singularity.isResolution_id": {"axioms": []}}}')
            with open(os.path.join(root, "blueprint", "nodes", "SG0000000A.yaml"), "a") as f:
                f.write("hypotheses:\n- SG0000000B\n")
            m = Map.load(root)
            self.assertEqual(set(m.records), {"Singularity.isResolution_id"})
            self.assertEqual(m.status("SG0000000A"), "proved-mod")

    def test_without_records(self):
        with tempfile.TemporaryDirectory() as d:
            shutil.copytree(MAP, os.path.join(d, "map"), ignore=shutil.ignore_patterns("records"))
            m = Map.load(os.path.join(d, "map"))
            self.assertIsNone(m.records)
            self.assertEqual({m.status(t) for t in m.nodes}, {"planned"})


class TestMarkdown(unittest.TestCase):
    def setUp(self):
        self.book = Book(CONTENT, MAP)
        self.md, self.stats = self.book.markdown(self.book.volume(0))

    def test_numbers(self):
        self.assertIn('# The first chapter {#v0-c1 num="1"}', self.md)
        self.assertIn('## The start {#v0-c1-the-start num="1.1"}', self.md)
        self.assertIn('## More {#v0-c1-more num="1.2"}', self.md)
        self.assertIn("[Theorem 1.1.1 (identity).]", self.md)
        self.assertIn("[Definition 1.1.2.]", self.md)
        self.assertIn("[Conjecture 1.2.1 (dimension 4).]", self.md)
        self.assertIn("[Lemma 2.1.1.]", self.md)

    def test_node_lines(self):
        self.assertIn("[Node: [SG0000000A](https://singularity.tamnd.com/node/SG0000000A/) · Lean: "
                      "`Singularity.isResolution_id` (status: proved)]{.node latex-cmd=\"hblean\"}", self.md)
        # a status written in the source is replaced by the computed one
        self.assertIn("`Singularity.ResolutionDimFourCharP` (status: open)]", self.md)
        self.assertNotIn("(status: proved) (status", self.md)
        self.assertIn("[Node: [SG0000000C](https://singularity.tamnd.com/node/SG0000000C/) (status: planned)]", self.md)
        self.assertEqual(self.stats["nodes"], 3)

    def test_draft_mark(self):
        self.assertEqual(self.md.count('::: {.draft latex-env="hbdraft"}'), 1)
        self.assertLess(self.md.index("# Second"), self.md.index(".draft"))

    def test_references(self):
        self.assertIn("- **Hir64**. Heisuke Hironaka. Resolution of singularities", self.md)
        self.assertIn("<https://arxiv.org/abs/2503.17321>", self.md)


class TestNumber(Tmp):
    def test_write(self):
        with redirect_stdout(io.StringIO()):
            changed = number.run(load(self.content), write=True)
        self.assertEqual(len(changed), 3)
        t = read(os.path.join(self.content, "00-test", "01-first", "01-start.md"))
        self.assertIn("**Theorem 1.1.1 (identity).**", t)
        self.assertIn("**Definition 1.1.2.**", t)
        self.assertTrue(t.startswith("---\ntitle: The start\n"))
        t = read(os.path.join(self.content, "00-test", "01-first", "02-more.md"))
        self.assertIn("**Conjecture 1.2.1 (dimension 4).**", t)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(number.run(load(self.content), write=True), [])   # a second run changes nothing

    def test_dry_run(self):
        with redirect_stdout(io.StringIO()):
            changed = number.run(load(self.content), write=False)
        self.assertEqual(len(changed), 3)
        self.assertIn("**Theorem (identity).**", read(changed[0]))


class TestCheck(Tmp):
    def faults(self):
        return check(load(self.content), Map.load(self.map), self.tmp)

    def test_clean(self):
        faults, warns = self.faults()
        self.assertEqual(faults, [])
        self.assertEqual(warns, [])

    def test_faults(self):
        self.write("00-test/02-second/02-bad.md", "---\ntitle: Bad\nnodes: [SG0000000Y]\nsources: [Nope99]\n"
                   "status: done\ndrafted_by: writer\n---\n## Bad\n\n**Theorem.** A claim.\n\n"
                   "Node: SG0000000Z · Lean: `Singularity.nothing`\n\nNode:\n")
        faults, _ = self.faults()
        text = "\n".join(faults)
        self.assertIn("02-bad.md:12: the node SG0000000Z is not in the map", text)
        self.assertIn("the node SG0000000Y of the front matter is not in the map", text)
        self.assertIn("the source Nope99 is not a paper of the map", text)
        self.assertIn("the status 'done' is not one of drafted, checked, reviewed", text)
        self.assertIn("02-bad.md:14: a Node line without a tag", text)

    def test_section_rules(self):
        self.write("00-test/02-second/02-bad.md", "---\ntitle: Bad\nstatus: reviewed\ndrafted_by: writer\n"
                   "reviewed_by: []\n---\nNo heading here, and a dash \u2014 here.\n")
        faults, _ = self.faults()
        text = "\n".join(faults)
        self.assertIn("a section must open with a ## heading", text)
        self.assertIn("the status is reviewed and reviewed_by is empty", text)
        self.assertIn("an en dash or an em dash", text)

    def test_warnings(self):
        self.write("00-test/02-second/02-warn.md", "---\ntitle: Warn\nnodes: []\nstatus: drafted\ndrafted_by: writer\n"
                   "---\n## Warn\n\n**Theorem.** A claim.\n\n**Lemma.** Another claim.\n\n"
                   "Node: SG0000000A · Lean: `Singularity.other`\n")
        faults, warns = self.faults()
        self.assertEqual(faults, [])
        text = "\n".join(warns)
        self.assertIn("02-warn.md:9: Theorem with no Node line", text)
        self.assertIn("the node SG0000000A is not in the nodes of the front matter", text)
        self.assertIn("the Lean name Singularity.other is not the Lean name of SG0000000A", text)

    def test_no_map(self):
        faults, _ = check(load(self.content), Map.load(os.path.join(self.tmp, "nowhere")), self.tmp)
        self.assertTrue(faults[0].startswith("the map is not found"))


class TestCli(unittest.TestCase):
    def run_cli(self, argv):
        with redirect_stdout(io.StringIO()) as out, redirect_stderr(io.StringIO()):
            code = main(argv)
        return code, out.getvalue()

    def test_check(self):
        self.assertEqual(self.run_cli(["--map", MAP, "--content", CONTENT, "check"])[0], 0)
        self.assertEqual(self.run_cli(["check", "--map", MAP, "--content", CONTENT, "--volume", "0"])[0], 0)

    def test_check_bad_map(self):
        code, out = self.run_cli(["check", "--map", os.path.join(HERE, "nowhere"), "--content", CONTENT])
        self.assertEqual(code, 1)
        self.assertIn("the map is not found", out)


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is not installed")
class TestLatex(unittest.TestCase):
    def test_pandoc(self):
        from shb.latex import pandoc_latex
        book = Book(CONTENT, MAP)
        md, _ = book.markdown(book.volume(0))
        tex = pandoc_latex(md)
        self.assertIn(r"\hbchapter{1}{The first chapter}{v0-c1}", tex)
        self.assertIn(r"\hbsection{1.1}{The start}{v0-c1-the-start}", tex)
        self.assertIn(r"\href{https://singularity.tamnd.com/node/SG0000000A/}{SG0000000A}", tex)
        self.assertIn(r"\hblean{", tex)
        self.assertEqual(tex.count(r"\begin{hbdraft}"), 1)


if __name__ == "__main__":
    unittest.main()
