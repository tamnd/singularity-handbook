# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The versions follow the line `version` of `EDITION`.

## [Unreleased]

### Added

- The builder `shb`, a fork of `rhb`, the builder of The Riemann Handbook. It keeps the pipeline: Markdown, then pandoc with `filters/shb.lua`, then LaTeX with `tex/handbook.sty`, then Tectonic for the PDF, and pandoc for the EPUB 3 with MathML. It keeps the fonts, the fallback fonts and the cover.
- The content format: a volume is `content/<NN-slug>/` with a `volume.yaml`, a chapter is a folder `<NN-chapter>/` with an optional `intro.md` and one file per section. A section has the front matter `title`, `nodes`, `sources`, `status`, `drafted_by` and `reviewed_by`.
- `shb check`: checks the front matter, the `Node:` lines, the node tags and the paper keys against the map of tamnd/singularity, and the dashes and the banned words.
- `shb number --write`: writes the numbers of the statements into the section files.
- `shb build`: writes `build/singularity-handbook-<NN-slug>-<version>.pdf` and `.epub`. Each `Node:` line gets a link to the node on singularity.tamnd.com and the status of the node, computed from `records/lean.json` of the map, or "planned".
- A Draft mark on the first page of each chapter that is not `reviewed`, in the PDF and in the EPUB.
- The list of the papers that the sections of a chapter cite, at the end of the chapter.
- The option `--map PATH` and the environment variable `SHB_MAP` for the checkout of tamnd/singularity.
- Tests of `shb` on a small volume in `tests/fixture`.
- The workflows `check` (the style rules, `shb check` and the tests) and `build` (Volume 0 as PDF and EPUB, and the release on a tag `v*`), with each action pinned to a commit.
- `scripts/style.py`, the writing rules of tamnd/singularity.
- `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE` (MIT, for the builder) and `LICENSE-CONTENT` (CC BY 4.0, for the text).
- Volume 0, Section 2.3: Theorem 2.3.1, resolution in dimension 0, with its proof and its Lean name.
- Volume 0, Section 2.5: Proposition 2.5.3, the core problem P1 is a special case of the main statement, with its proof and its Lean name.

### Removed

- From `rhb`: the sources of tamnd/riemann and tamnd/riemann-lean, the ledger of declarations and its dominator tree (`corpus.py`, `ledger.py`), the links `/entry/<id>/` and their numbers, the named results, the index of Lean names, the commands `survey` and `ledger`, and the list of the riemann volumes.
