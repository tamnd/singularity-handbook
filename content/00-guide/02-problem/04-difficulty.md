---
title: Why characteristic p is different
nodes: [SG00000018, SG00000016, SG00000017, SG00000039, SG0000000C]
sources: [Hau10, Nar83, Hau08, HP19a, Moh87]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Why characteristic $p$ is different

In characteristic 0 the proof of resolution is an induction on the dimension. At a point of maximal order $d$ of a hypersurface $f = 0$, choose coordinates in which $f$ contains the monomial $z^d$. Then the derivative $\partial^{d-1} f / \partial z^{d-1}$ has order 1, and it defines a regular hypersurface $H$. The points of order $d$ lie in $H$, and after each permissible blowup the points of order $d$ lie in the strict transform of $H$, so the problem goes down to an ideal on $H$, which has dimension one less. $H$ is a *hypersurface of maximal contact*.

In characteristic $p$ this fails for three reasons.

1. **No maximal contact.** Take $f = z^p + g(x)$. The Hasse-Schmidt derivative of order $j$ in $z$ sends $z^p$ to $\binom{p}{j} z^{p-j}$, which is zero for $0 < j < p$, and the derivative of order $p$ is 1. So no derivative of $f$ in $z$ gives a hypersurface of maximal contact. Narasimhan gave a hypersurface in $\mathbb{A}^4$ over a field of characteristic 2 whose locus of maximal order is not contained in any regular hypersurface near the origin.
2. **The invariants can go up.** For $f = z^q + g(x)$ with $q$ a power of $p$, the natural invariant is the *residual order*. Over a perfect field, a coordinate change $z \mapsto z + h(x)$ removes the terms of $g$ whose exponents lie in $q\mathbb{N}^n$. The residual order is the order of the other terms, after division by the largest monomial in the exceptional variables that divides them (Volume 7, Definition 1.3.3). Under a point blowup this order can go up (Volume 7, Example 1.4.2, with $q = 4$). Hauser calls such a point a *kangaroo point*. Moh proved that under a point blowup the residual order goes up by at most $q/p$ (Volume 7, Theorem 1.4.1).
3. **Stability fails.** Moh also claimed that after a bounded number of steps the residual order cannot go up again. Hauser and Perlega found a cycle of point blowups of an equation $z^{p^3} + g$ for which this claim is false (Volume 7, Theorem 1.4.3). For $q = p$ the claim holds [HP19a, Section 3]. The library certifies one cycle for one choice of the parameters, but not the iteration of the cycle.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

Node: SG00000016 · Lean: `Singularity.Examples.kangaroo`

Node: SG00000017 · Lean: none yet (one cycle is certified, Volume 7, Example 1.4.5)

Node: SG00000039 · Lean: `Singularity.Examples.hauserPerlegaCycle`

A fourth difference is about the field. Over an imperfect field, such as $\mathbb{F}_p(t)$, a regular variety need not be smooth. For example, the curve $y^2 = x^p - t$ over $\mathbb{F}_p(t)$ with $p$ odd is regular, and it is not smooth at the point $x^p = t$, $y = 0$. So the statement "each variety has a resolution by a smooth variety" is false over imperfect fields, and the project uses "regular".

Node: SG0000000C · Lean: `Singularity.exists_regular_not_smooth` (planned, no Lean statement yet)
