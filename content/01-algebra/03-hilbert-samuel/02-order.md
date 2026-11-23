---
title: The order of an element
nodes: [SG0000002E, SG0000002F]
sources: [AM69, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The order of an element

In this section $R$ is a commutative ring and $I$ is an ideal of $R$. The order of an element measures how deep the element is in the filtration $R = I^0 \supseteq I \supseteq I^2 \supseteq \dots$. For a local ring and its maximal ideal it is the classical order of vanishing at the closed point.

### The definition

**Definition 3.2.1.** The *order* of an element $f \in R$ with respect to $I$ is
$$\operatorname{ord}_I(f) = \sup \{ n \in \mathbb{N} : f \in I^n \} \in \mathbb{N} \cup \{\infty\}.$$
The set is not empty, because $f \in I^0 = R$.

Node: SG0000002E · Lean: `Singularity.Algebra.order`

**Lemma 3.2.2.** Let $f \in R$ and $n \in \mathbb{N}$. Then $n \le \operatorname{ord}_I(f)$ if and only if $f \in I^n$.

Lean: `Singularity.Algebra.le_order_iff`

*Proof.* If $f \in I^n$, then $n$ is in the set of Definition 3.2.1, so $n \le \operatorname{ord}_I(f)$. Conversely, assume that $n \le \operatorname{ord}_I(f)$. If $n = 0$, then $f \in I^0 = R$. If $n \ge 1$, then $n - 1 < \operatorname{ord}_I(f)$, so by the definition of the supremum there is an $m$ with $f \in I^m$ and $n - 1 < m$. Thus $m \ge n$, and $f \in I^m \subseteq I^n$. $\square$

Thus the set of Definition 3.2.1 is the set of all $n \le \operatorname{ord}_I(f)$. If $\operatorname{ord}_I(f) = d$ is finite, then $f \in I^d$ and $f \notin I^{d+1}$. If $\operatorname{ord}_I(f) = \infty$, then $f$ is in each power of $I$.

### The laws of the order

**Proposition 3.2.3.** Let $f, g \in R$. Then:

1. $\operatorname{ord}_I(0) = \infty$.
2. $\operatorname{ord}_I(-f) = \operatorname{ord}_I(f)$.
3. $\operatorname{ord}_I(f + g) \ge \min(\operatorname{ord}_I(f), \operatorname{ord}_I(g))$.
4. $\operatorname{ord}_I(fg) \ge \operatorname{ord}_I(f) + \operatorname{ord}_I(g)$.
5. If $I \ne R$, then $\operatorname{ord}_I(1) = 0$.
6. If $I \subseteq J$, then $\operatorname{ord}_I(f) \le \operatorname{ord}_J(f)$.

Lean: `Singularity.Algebra.order_zero`, `Singularity.Algebra.order_neg`, `Singularity.Algebra.order_add`, `Singularity.Algebra.order_mul`, `Singularity.Algebra.order_one`, `Singularity.Algebra.order_mono`

*Proof.* Each statement follows from Lemma 3.2.2. For 1, $0$ is in each ideal $I^n$. For 2, $I^n$ is closed under negation, so $f \in I^n$ if and only if $-f \in I^n$. For 3, let $n \le \min(\operatorname{ord}_I(f), \operatorname{ord}_I(g))$. Then $f, g \in I^n$, so $f + g \in I^n$ and $n \le \operatorname{ord}_I(f+g)$. Since this is true for each such $n$, statement 3 follows.

For 4, if $\operatorname{ord}_I(f) = \infty$, then $f$ is in each $I^n$, so $fg$ is in each $I^n$, and $\operatorname{ord}_I(fg) = \infty$. The case $\operatorname{ord}_I(g) = \infty$ is the same. If $a = \operatorname{ord}_I(f)$ and $b = \operatorname{ord}_I(g)$ are finite, then $f \in I^a$ and $g \in I^b$, so $fg \in I^a I^b = I^{a+b}$ and $a + b \le \operatorname{ord}_I(fg)$.

For 5, if $1 \le \operatorname{ord}_I(1)$, then $1 \in I$, so $I = R$. For 6, $I^n \subseteq J^n$ for each $n$. $\square$

Statement 4 is an inequality. Let $R = k[x, y]/(xy)$ and $I = (x, y)$. Then $\operatorname{ord}_I(x) = \operatorname{ord}_I(y) = 1$ and $xy = 0$, so $\operatorname{ord}_I(xy) = \infty$. When $(R, \mathfrak{m})$ is a regular local ring, the ring $\bigoplus_n \mathfrak{m}^n / \mathfrak{m}^{n+1}$ is a polynomial ring over the residue field [AM69, Theorem 11.22]. Thus it is a domain, and statement 4 is an equality for $I = \mathfrak{m}$. This edition does not prove this, and it has no Lean proof yet.

**Theorem 3.2.4.** Let $(R, \mathfrak{m})$ be a Noetherian local ring and let $I \ne R$ be an ideal. Then $\operatorname{ord}_I(f) = \infty$ if and only if $f = 0$.

Node: SG0000002F · Lean: `Singularity.Algebra.order_eq_top_iff`

*Proof.* By Proposition 3.2.3, $\operatorname{ord}_I(0) = \infty$. Conversely, if $\operatorname{ord}_I(f) = \infty$, then by Lemma 3.2.2 the element $f$ is in $\bigcap_n I^n$. Since $I \subseteq \mathfrak{m}$, this intersection is in $\bigcap_n \mathfrak{m}^n$, and $\bigcap_n \mathfrak{m}^n = 0$ by the intersection theorem of Krull [AM69, Corollary 10.20]. $\square$

The theorem is false without the hypothesis that $R$ is Noetherian. Let $R$ be the ring of germs at $0$ of smooth functions $\mathbb{R} \to \mathbb{R}$, with the maximal ideal $\mathfrak{m}$ of the germs that vanish at $0$. The germ of $e^{-1/x^2}$ (extended by $0$ at $0$) is not $0$, but it is in each $\mathfrak{m}^n$.

**Proposition 3.2.5.** Let $(R, \mathfrak{m})$ be a local ring and let $f \in R$. Then $\operatorname{ord}_\mathfrak{m}(f) = 0$ if and only if $f$ is a unit.

Lean: `Singularity.Algebra.order_eq_zero_iff`

*Proof.* By Lemma 3.2.2, $\operatorname{ord}_\mathfrak{m}(f) \ge 1$ if and only if $f \in \mathfrak{m}$. In a local ring, $f \in \mathfrak{m}$ if and only if $f$ is not a unit. $\square$

### The order of a hypersurface

**Example 3.2.6.** Let $k$ be a field, let $A = k[x, y]$, let $\mathfrak{n} = (x, y)$ and let $R = A_\mathfrak{n}$ with maximal ideal $\mathfrak{m} = \mathfrak{n} R$. Let $f = y^2 - x^3$, the equation of the cusp of Example 1.2.4. Then $f \in \mathfrak{m}^2$. Also $f \notin \mathfrak{m}^3$. Indeed, the ideal $\mathfrak{n}^3$ is $\mathfrak{n}$-primary, so it is the inverse image of $\mathfrak{m}^3 = \mathfrak{n}^3 R$ in $A$ [AM69, Proposition 4.8]. The polynomial $f$ has the monomial $y^2$ of degree 2, so $f \notin \mathfrak{n}^3$. Thus $\operatorname{ord}_\mathfrak{m}(f) = 2$.

The same argument shows the general rule. For a polynomial $f \in A$ with $f(0) = 0$, the order $\operatorname{ord}_\mathfrak{m}(f)$ is the smallest degree of a monomial of $f$. A point of the hypersurface $f = 0$ is regular if and only if the order of $f$ there is $1$ (Section 1.2). The order is the multiplicity of the hypersurface at the point, and the proofs of resolution in characteristic 0 make it smaller by blowups. In characteristic $p$ the order alone does not give a proof. Let $f = z^p + g$ with $g \in k[x_1, \dots, x_4]$. Then $\operatorname{ord}_\mathfrak{m}(f) = \min(p, \operatorname{ord}_\mathfrak{m}(g)) \le p$ for each $g$, and the methods for this case use the residual order of $g$ after the coordinate changes that remove $p$-th powers (node SG00000013).

Lean: none yet
