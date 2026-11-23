# The Singularity Handbook

The Singularity Handbook explains the theory of resolution of singularities. It starts with curves and ends with the open case in characteristic $p > 0$. It is for graduate students and for mathematicians, and it comes as a set of books in PDF and EPUB.

Each chapter follows the published proofs. Each chapter defines its objects, states its results with numbers (Theorem 2.3.1), proves them, and gives its references. Where a result has a Lean form in the project [tamnd/singularity](https://github.com/tamnd/singularity), a line under the statement gives the node of the map, the Lean name and the status of the Lean proof. The web version of the map is at [singularity.tamnd.com](https://singularity.tamnd.com).

## The status of the open case

Resolution of singularities is known in characteristic 0 in every dimension (Hironaka, 1964). In characteristic $p > 0$ it is known in dimension at most 3. In dimension 4 and higher in characteristic $p > 0$ it is an open problem.

The open case is not proved. The handbook does not claim a proof of it. Volume 9 reports the work on the open case and says which results are new, which are checked in Lean, and which are only conjectures. The builder writes the status of each node from the records of the map at build time. No status in the books is written by hand.

## The volumes

| | Volume |
|---|---|
| 0 | Guide |
| 1 | Commutative algebra for resolution |
| 2 | Resolution in characteristic 0 |
| 3 | Valuations |
| 4 | Curves and surfaces in every characteristic |
| 5 | Local uniformization |
| 6 | Threefolds in positive characteristic |
| 7 | Invariants in positive characteristic |
| 8 | Alterations |
| 9 | The open problem |

A volume has a release when all its chapters have the status `reviewed`. Volume 9 is the exception: it has a release at each milestone of the project, as a research report. The books are in the [releases](https://github.com/tamnd/singularity-handbook/releases).

## The content format

A volume is a folder `content/<NN-slug>/`, for example `content/00-guide/`. It has a file `volume.yaml` with `number`, `title` and `subtitle`. It can have an `intro.md`.

A chapter is a folder `content/<NN-volume>/<NN-chapter>/`. It has an optional `intro.md`, whose `#` heading is the title of the chapter, and one file `NN-<slug>.md` for each section. The number of the chapter is the `NN` of its folder.

A section file starts with YAML front matter:

```markdown
---
title: Moh's bound
nodes: [SG0000000A]
sources: [Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Moh's bound

**Theorem (Moh).** Let $f = z^{p^e} + \dots$ ...

Node: SG0000000A · Lean: `Singularity.Residual.moh_bound`

*Proof.* ... $\square$
```

- `nodes` lists the tags of the nodes of the map that the section uses. Each tag must be a file `blueprint/nodes/<TAG>.yaml` of the map.
- `sources` lists the keys of the papers that the section cites. Each key must be a file `papers/<Key>.yaml` of the map. The build lists these papers at the end of the chapter.
- `status` is `drafted`, `checked` or `reviewed`. The status of a chapter is the lowest status of its sections. A chapter that is not `reviewed` is a draft: the PDF has a Draft mark on its first page, and the EPUB has a Draft mark at its start.
- `reviewed_by` lists the people who have read the section. A section at status `reviewed` must have at least one name.

The text of a section starts with a `##` heading. A statement starts with a bold head: `**Definition.**`, `**Theorem (Name).**`, and so on. The build numbers each `##` heading (2.3) and each statement (Theorem 2.3.1). `shb number --write` writes the same numbers into the source files, so that the source on GitHub reads as the book does.

A statement that has a node has a line ``Node: <TAG> · Lean: `<Name>` `` under it. At build time `shb` reads the status of the node and adds it to the line, for example "(status: proved)". The tag becomes a link to `https://singularity.tamnd.com/node/<TAG>/` in the PDF and in the EPUB. A status that is written in the source is replaced.

## The status of a node

`shb` reads the map from a checkout of tamnd/singularity. If the map has a file `records/lean.json` that contains the Lean name of the statement of the node, the status comes from that record: "proved" when the record of the proof exists and has no `sorry`, "open" for a conjecture, and "stated" in the other cases. A record can also give the status itself. If there is no such record, the status is "planned".

## Build

You need Python 3.11 or later, [pandoc](https://pandoc.org) 3.8 or later and [Tectonic](https://tectonic-typesetting.github.io). Put a checkout of [tamnd/singularity](https://github.com/tamnd/singularity) next to this repository, at `../singularity`, or give its path with `--map PATH` or the environment variable `SHB_MAP`.

```sh
pip install .
python scripts/style.py
python -m shb check
python -m shb number --write
python -m shb build --volume 0,9 --formats pdf,epub
python -m unittest discover -s tests
```

`shb check` reports a section with a bad front matter, a `Node:` line or a `nodes` tag that is not in the map, a source key that is not in the map, and an en dash or an em dash. It also gives warnings that do not fail the check, for example a theorem with no `Node:` line.

The books go to `build/singularity-handbook-<NN-slug>-<version>.pdf` and `.epub`. The version is in the first line of `EDITION`, and the second line gives the commit of tamnd/singularity that the edition describes. The pipeline is that of [The Riemann Handbook](https://github.com/tamnd/riemann-handbook): Markdown, then pandoc with `filters/shb.lua`, then LaTeX with `tex/handbook.sty`, then Tectonic. The EPUB is EPUB 3 with MathML.

## Licence

The text is licensed under [CC BY 4.0](LICENSE-CONTENT). The builder `shb`, the filter and the style files are licensed under the [MIT licence](LICENSE).

Please report errors at [issues](https://github.com/tamnd/singularity-handbook/issues). [CONTRIBUTING.md](CONTRIBUTING.md) tells how to send a change.
