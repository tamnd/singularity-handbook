---
title: Why characteristic p is different
nodes: [SG00000018, SG00000016, SG00000017, SG0000000C]
sources: [Hau10, Nar83, Hau08, HP19a, Moh87]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Why characteristic $p$ is different

In characteristic 0 the proof of resolution is an induction on the dimension. At a point of maximal order $d$ of a hypersurface $f = 0$, the derivative $\partial^{d-1} f / \partial z^{d-1}$ defines a regular hypersurface $H$. The singularities of order $d$ stay in $H$ after each permissible blowup, so the problem goes down to an ideal on $H$, which has dimension one less. $H$ is a *hypersurface of maximal contact*.

In characteristic $p$ this fails for three reasons.

1. **No maximal contact.** Take $f = z^p + g(x)$. The Hasse-Schmidt derivative of order $j$ in $z$ sends $z^p$ to $\binom{p}{j} z^{p-j}$, which is zero for $0 < j < p$. So no derivative of $f$ in $z$ gives a hypersurface of maximal contact. Narasimhan gave a hypersurface in $\mathbb{A}^4$ over a field of characteristic 2 whose locus of maximal order is not contained in any regular hypersurface near the origin.
2. **The invariants can go up.** For $f = z^p + g(x)$, the natural invariant is the *residual order*: the order of $g$ after all coordinate changes $z \mapsto z + h(x)$ that remove $p$-th powers from $g$. Under a permissible blowup this order can go up. Hauser calls such a point a *kangaroo point*. Moh proved a bound on how much the residual order can go up in one step.
3. **Stability fails.** Moh also claimed that after a bounded number of steps the residual order cannot go up again. Hauser and Perlega found a cycle of blowups for which this claim is false.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

Node: SG00000016 · Lean: `Singularity.Examples.kangaroo`

Node: SG00000017 · Lean: `Singularity.Examples.hauserPerlegaCycle`

A fourth difference is about the field. Over an imperfect field, such as $\mathbb{F}_p(t)$, a regular variety need not be smooth. For example, the curve $y^2 = x^p - t$ over $\mathbb{F}_p(t)$ with $p$ odd is regular, and it is not smooth at the point $x^p = t$, $y = 0$. So the statement "each variety has a resolution by a smooth variety" is false over imperfect fields, and the project uses "regular".

Node: SG0000000C · Lean: `Singularity.exists_regular_not_smooth`
