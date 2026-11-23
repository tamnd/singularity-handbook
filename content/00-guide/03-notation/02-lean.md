---
title: Lean names
nodes: []
sources: []
status: drafted
drafted_by: writer
reviewed_by: []
---
## Lean names

The Lean code of the project is in the namespace `Singularity`. The statements of the problem are in `Singularity.Statements`, but their names have no second namespace, for example `Singularity.IsResolution`. The fidelity checks are in `Singularity.Fidelity`. Worked examples and counterexamples are in `Singularity.Examples`.

The project uses Mathlib names for Mathlib notions. The table gives the Mathlib names that the statements use.

| Notion | Mathlib |
|---|---|
| scheme | `AlgebraicGeometry.Scheme` |
| local ring of $X$ at $x$ | `X.presheaf.stalk x` |
| regular local ring | `IsRegularLocalRing` |
| proper morphism | `AlgebraicGeometry.IsProper` |
| restriction of $\pi$ over an open set $U$ | `π ∣_ U` |
| reduced scheme | `AlgebraicGeometry.IsReduced` |
| locally of finite type | `AlgebraicGeometry.LocallyOfFiniteType` |
| dimension | `topologicalKrullDim` |
| characteristic $p$ | `CharP k p` |
