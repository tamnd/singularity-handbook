# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The versions follow the line `version` of `EDITION`.

## [Unreleased]

### Added

- Volume 1, Commutative algebra for resolution, with Chapter 1, Regular local rings. It has four sections: dimension and the cotangent space, regular local rings and the quotient by a parameter, the proof that a regular local ring is a domain, and the description of regular local rings of dimension 1. Each section gives complete proofs for a graduate student with references to Atiyah and Macdonald, Matsumura and the Stacks project, examples (the cusp, the node, the cone, the union of two axes), an explanation of the Lean proof and notes.
- The workflow `build` builds Volumes 0, 1 and 9.

### Changed

- `shb` reads the record of the Lean build in the form with the key `decls`, that tamnd/singularity-lean writes. Before this change it did not find the declarations, and each node had the status planned. A node with named hypotheses now has the status proved-mod.
- Volume 9, Section 1.3 refers to the full proof in Volume 1 and gives the Lean name of SG0000000J.
- `EDITION` points to the map after the nodes of the regular local ring API.

## [0.2.0] - 2026-11-23

### Added

- Volume 9, The open problem, Chapter 1, The proved cases and the reductions. It has five sections: dimension 0, integral varieties in characteristic 0, the reduction to integral varieties, the bridge to formal-conjectures, and the purely inseparable hypersurfaces of P1. Each section gives the statements, complete proofs for a graduate student, examples and counterexamples, an explanation of the Lean proof, and notes with references.
- Volume 0: Theorem 2.3.2 (integral varieties in characteristic 0), Hypothesis 2.3.3 (the reduction to integral varieties), Theorem 2.3.4 (characteristic 0 from the hypothesis), Proposition 2.5.4 (the bridge to formal-conjectures) and Corollary 2.5.5 (Hironaka's theorem in the form of formal-conjectures).
- The statement kind Hypothesis in `shb`.
- The workflow `build` builds Volumes 0 and 9.

### Changed

- The edition page of Volume 0 describes the milestone S1.
- `EDITION` is 0.2.0 and points to the map after the records of S1.

## [0.1.0] - 2026-11-23

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
