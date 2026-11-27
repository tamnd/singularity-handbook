---
title: The centers of Cossart and permissibility
nodes: []
sources: [Cos87, Pos24, Hir64, Benn70]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The centers of Cossart and permissibility

This section reports the twentieth research result, from the track Q1 (tamnd/singularity#284). It answers the question of Volume 7, Section 4.2: when does a blowup of the base in the algorithm of Cossart for $z^p + g$ come from a permissible blowup of the hypersurface? Volume 7, Section 4.3, gives the results with all the details.

### The problem

Let $B$ be a regular threefold of characteristic $p$, let $g \in \mathcal{O}(B)$ and $X = V(z^p + g)$. The algorithm of Cossart blows up regular centers $C$ of the base [Cos87]. By Volume 7, Proposition 4.3.1, the blowup of $B$ along $C$ comes from the blowup of $X$ along the center $C' = V(z - h, I_C)$, along which $X$ has order $p$, if and only if the test $g + h^p \in I_C^p$ holds for some $h$. The residue field at the generic point of a curve is not perfect, so it was not clear whether the test can fail at a center along which $X$ has multiplicity $p$, and whether the centers of the algorithm pass the test.

### The result

Proved:

1. For each irreducible regular center $C$ of a regular base, the test holds if and only if $X$ has multiplicity $p$ at the generic point of $C$, and then $X$ has multiplicity $p$ at each point of $C$ and the blowup along $C'$ is permissible (Volume 7, Theorem 4.3.6). There is a unique $b \in \mathcal{O}(C)$ with $b^p = -g|_C$, and $C' = V(z - b, I_C)$.
2. So no regular center that lies in the multiplicity $p$ locus of $X$ fails the test, whatever the algorithm chooses (Volume 7, Corollary 4.3.8).
3. At a closed point with a perfect residue field, the test holds if and only if the clean part of $g$, in coordinates adapted to $C$, has order at least $p$ along $C$. The generic multiplicity is $\min(p, \max(1, \operatorname{ord}_C g_c))$ (Volume 7, Proposition 4.3.9). The coordinates must be adapted to $C$ (Volume 7, Example 4.3.10).
4. The invariant $\nu$ of Cossart along a failing center is at most the clean order, so it is at most $p - 1$ (Volume 7, Proposition 4.3.11). A failing surface center is not a component of the boundary and has $1 \le \nu \le p - 2$, and for $p = 2$ every surface center passes (Volume 7, Corollary 4.3.12).

Examples: the centers of Cossart fail the test for every $p$. The surface $V(x)$ for $g = x^d$, $2 \le d \le p - 1$, fails for each $p \ge 3$ (Volume 7, Example 4.3.14). For $p = 2$, $g = x + y^3$ with $E = \{x\}$, a curve and its points fail, and $X$ is regular along them (Volume 7, Example 4.3.15). For $p = 2$, $g = xw + y^3$ with $E = \{x\}$, the $w$-axis is the curve that the test of a good point blows up at the origin, it fails the test, and $X$ has multiplicity $2 = p$ at the origin (Volume 7, Example 4.3.16).

### The proof in short

Membership in $J^n$, for $J = (z - h) + I R[z]$, is read from the coefficients of $z - h$, and the Frobenius gives $z^p + g = (z - h)^p + (g + h^p)$. For a regular base and a regular center, the order along $I_C$ is the order at the generic point, because the associated graded ring is a polynomial ring over a domain. At the generic point, multiplicity $p$ means that $-\bar g$ is a $p$-th power $b^p$ in the function field of $C$. The element $b$ is integral over $\mathcal{O}(C)$, and $C$ is normal, so $b \in \mathcal{O}(C)$. Equimultiplicity of a hypersurface along a regular center gives normal flatness [Hir64, Benn70]. The bound on $\nu$ comes from one derivation in $D(B, E)$ applied to a monomial of the clean part of the least order along $C$.

### The test data

A script over $\mathbb{F}_p$ drew $1500$ pairs $(g, E)$ for each of $p = 2, 3, 5$ and listed the candidate centers through the origin by type, with a proxy for the choice of the algorithm. In all $12\,381$ centers, the test agreed with the multiplicity of $X$ at random closed points of $C$ over finite extensions, the test agreed with the clean order, $\nu(C) \ge p$ implied the test, and each $h$ found satisfied $g + h^p \in I_C^p$. On $4500$ curves that are not coordinate curves, the test agreed with the generic multiplicity in all cases. The proxy ignores the history invariant and the tests for $\kappa \ge 2$, so the tests are not a proof, and the rows for surfaces count proxy centers only.

### What the result means

The test of Volume 7, Section 4.2, is generic equimultiplicity, for each regular center and each algorithm. The algorithm of Cossart is not a sequence of permissible blowups of $X$: failing centers occur for every $p$, and they can meet the multiplicity $p$ locus of $X$. For the resolution of $X$ alone this changes nothing, since a failing base blowup is still a birational step for $X$. For the embedded problem, the failing centers need other methods, also near the points of multiplicity $p$ that they pass through. Whether a rule for the centers exists that makes $\nu$ drop and keeps each center that meets the multiplicity $p$ locus inside it is open.

### Status

The results are the nodes SG0000007H to SG0000007V of the map. The order along the lifted center and the chart identity (SG0000007H and SG0000007J) have Lean proofs, with ordinary powers of ideals. The generic multiplicity, the equivalence of Theorem 4.3.6 and the comparison with the invariants of Cossart are planned for Lean. An outside expert has not yet read the result.

### Notes and references

The results are in the research notes 10, 43 and 47. Note 47 is a referee report on note 43, and it gives Example 4.3.16. The algorithm is in [Cos87], restated in [Pos24, Appendix A].
