---
title: Rings, schemes and dimension
nodes: []
sources: [EGA4-7, Ser55]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Rings, schemes and dimension

A ring is commutative with $1$. A local ring is written $(R, \mathfrak{m}, \kappa)$, with maximal ideal $\mathfrak{m}$ and residue field $\kappa = R/\mathfrak{m}$. The completion of $R$ at $\mathfrak{m}$ is $\widehat{R}$.

The letter $k$ is a field, and $p$ is its characteristic, a prime or $0$. The field $k$ is not assumed perfect. When a result needs a perfect field, the statement says so.

A scheme is not assumed Noetherian or separated. For a scheme $X$ and a point $x \in X$, the local ring is $\mathcal{O}_{X,x}$, with maximal ideal $\mathfrak{m}_x$ and residue field $\kappa(x)$.

The dimension of a scheme is the Krull dimension of its topological space. The empty scheme has dimension $-\infty$. In Lean this is `topologicalKrullDim`, with values in `WithBot ℕ∞`.

The order of an element $f \neq 0$ of a Noetherian local ring $(R, \mathfrak{m})$ is the largest $d$ with $f \in \mathfrak{m}^d$. The order of an ideal is the minimum of the orders of its elements.

A blowup of $X$ along a closed subscheme $Z$ is written $\operatorname{Bl}_Z X \to X$. A blowup is *permissible* when $Z$ is regular and $X$ is normally flat along $Z$.

The disjoint union of schemes is $X \sqcup Y$. The codiagonal $X \sqcup X \to X$ is $\nabla$.
