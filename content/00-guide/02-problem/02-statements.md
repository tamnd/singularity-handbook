---
title: The statements
nodes: [SG00000006, SG00000007, SG00000008, SG00000009]
sources: [Hir64, Lip78, CP08, CP09, Abh66, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The statements

Let $p$ be $0$ or a prime, and let $n$ be a natural number.

**Definition 2.2.1.** $\mathrm{Res}(p, n)$ is the statement that each variety $X$ of dimension at most $n$ over a field $k$ of characteristic $p$ has a resolution.

Node: SG00000006 · Lean: `Singularity.ResolutionInDim`

The field $k$ can be any field of characteristic $p$. It need not be perfect and it need not be algebraically closed. The dimension is the Krull dimension of the topological space of $X$.

**Conjecture 2.2.2 (resolution in dimension 4).** For each prime $p$, $\mathrm{Res}(p, 4)$ holds.

Node: SG00000007 · Lean: `Singularity.ResolutionDimFourCharP`

**Conjecture 2.2.3 (resolution of singularities).** For each $p$ and each $n$, $\mathrm{Res}(p, n)$ holds.

Node: SG00000008 · Lean: `Singularity.ResolutionOfSingularities`

The project also states a special case that is open and that has a simple form. Let $k$ be a field of characteristic $p$ and let $g \in k[x_1, \dots, x_n]$. The hypersurface
$$X_g = \operatorname{Spec} k[z, x_1, \dots, x_n]/(z^p + g)$$
has dimension $n$. It is purely inseparable over the affine space $\mathbb{A}^n_k$, by the projection to the coordinates $x$.

**Conjecture 2.2.4 (purely inseparable hypersurfaces).** If $X_g$ is reduced, then $X_g$ has a resolution.

Node: SG00000009 · Lean: `Singularity.PurelyInseparableHypersurfaceResolution`

We call Conjecture 2.2.4 the core problem P1. For $n \le 3$ this is a case of the theorem on threefolds. For $n \ge 4$ the conjecture is open. For $n = 4$, $X_g$ is a fourfold. Many of the known difficulties of characteristic $p$ already show in this family. Hauser studies it in detail in his survey of 2010 [Hau10].
