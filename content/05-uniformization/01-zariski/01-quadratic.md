---
title: Quadratic transforms
nodes: [SG0000003C, SG00000023]
sources: [Abh56, Zar39, Mat, Cut04]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Quadratic transforms

Local uniformization asks for one thing: given a valuation $v$ and a model on which $v$ has a center, find a new model on which the center of $v$ is a regular point. On a surface the simplest way to change a model is to blow up the center of $v$ when it is a closed point. If we follow $v$ through this blowup, we get a new local ring, again of dimension 2 or else a valuation ring. This section sets up that one step in algebraic form. The next section iterates it. The main point here is that the step is explicit: it uses one chart $R[y/x]$, a choice of the parameter of least value, and the residue of $y/x$. All later arguments in this chapter reduce to these three data.

In this section $R$ is a regular local ring of dimension 2 with maximal ideal $\mathfrak{m}$ and residue field $\kappa$, and $K$ is the fraction field of $R$. We assume that $R$ is essentially of finite type over a field $k$, in the sense of Volume 3, Section 4.1. A valuation $v$ of $K$ *dominates* $R$ if $R \subseteq \mathcal{O}_v$ and $\mathfrak{m}_v \cap R = \mathfrak{m}$. Then $v$ is trivial on $k$, because the elements of $k^\times$ are units of $R$.

We first record a remark on local rings of affine models that we use many times. In the rest of the volume, the *center* of $v$ on an affine model $A \subseteq \mathcal{O}_v$ is the prime $\mathfrak{m}_v \cap A$ (Volume 3, Lemma 1.4.2).

**Lemma 1.1.1.** Let $v$ be a valuation of $K/k$, let $A \subseteq A'$ be affine models of $K/k$ contained in $\mathcal{O}_v$, with centers $\mathfrak{p}$ and $\mathfrak{p}'$. If $A' \subseteq A_\mathfrak{p}$, then $A'_{\mathfrak{p}'} = A_\mathfrak{p}$.

Lean: `Singularity.centerLocalization_eq_of_le`

*Proof.* The elements of $A \setminus \mathfrak{p}$ are units of $\mathcal{O}_v$, so they lie in $A' \setminus \mathfrak{p}'$. Thus $A_\mathfrak{p} \subseteq A'_{\mathfrak{p}'}$. Conversely, $A' \subseteq A_\mathfrak{p} \subseteq \mathcal{O}_v$, and the maximal ideal of $A_\mathfrak{p}$ is $\mathfrak{m}_v \cap A_\mathfrak{p}$. An element of $A' \setminus \mathfrak{p}'$ lies in $A_\mathfrak{p}$ and is a unit of $\mathcal{O}_v$, so it is a unit of $A_\mathfrak{p}$. Thus $A'_{\mathfrak{p}'} \subseteq A_\mathfrak{p}$. $\square$

### The quadratic transform

Let $x, y$ be a regular system of parameters of $R$. We use the chart $B = R[\mathfrak{m}/x]$ of Volume 1, Definition 1.10.3. Since $\mathfrak{m} = (x, y)$, we have $B = R[y/x]$. By Volume 1, Proposition 1.10.4, there is an isomorphism
$$B/xB \cong \kappa[Y]$$
onto a polynomial ring in one variable, which maps the class of $y/x$ to $Y$. By Volume 1, Theorem 1.10.6, $B$ is a Noetherian regular domain. Since $B/xB$ is a domain, $xB$ is a prime ideal. Also $\mathfrak{m}B = xB$, because $y = x \cdot (y/x)$, and so $\mathfrak{m}^aB = x^aB$ for each $a \ge 0$.

**Definition 1.1.2 (quadratic transform).** Let $v$ be a valuation of $K$ that dominates $R$. Choose the regular system of parameters $x, y$ with $v(x) \le v(y)$, and let $B = R[y/x]$. Then $B \subseteq \mathcal{O}_v$. Let $\mathfrak{n} = \mathfrak{m}_v \cap B$ be the center of $v$ on $\operatorname{Spec} B$. The *quadratic transform* of $R$ along $v$ is the local ring $R_1 = B_\mathfrak{n}$.

Geometrically, $\operatorname{Spec} R_1$ is the local scheme of the blowup of $\operatorname{Spec} R$ at the closed point, at the center of $v$. The ring $R_1$ depends on the choice of $x$ and $y$ only through this center. We do not need this fact, and we fix a choice. The ring $R_1$ is essentially of finite type over $k$, it contains $R$, and $v$ dominates $R_1$.

*Remark (the choice of parameters).* For the reader who wants the fact anyway, here is the short proof. Let $x', y'$ be a second regular system of parameters with $v(x') \le v(y')$, let $B' = R[y'/x']$, and let $\mathfrak{n}' = \mathfrak{m}_v \cap B'$. Each element of $\mathfrak{m}$ is a combination of $x$ and $y$ with coefficients in $R$, so the least value of $v$ on $\mathfrak{m}$ is $v(x)$. For the same reason it is $v(x')$. So $v(x') = v(x)$. Since $x' \in \mathfrak{m} \subseteq xB$, the quotient $x'/x$ lies in $B$, and it is a unit of $\mathcal{O}_v$. So $x'/x \notin \mathfrak{n}$, and $x'/x$ is a unit of $B_\mathfrak{n}$. Then $\mathfrak{m}/x' = (x/x')(\mathfrak{m}/x) \subseteq B_\mathfrak{n}$, and thus $B' \subseteq B_\mathfrak{n}$. The elements of $B' \setminus \mathfrak{n}'$ are units of $\mathcal{O}_v$ that lie in $B_\mathfrak{n}$. The maximal ideal of $B_\mathfrak{n}$ is $\mathfrak{m}_v \cap B_\mathfrak{n}$, so these elements are units of $B_\mathfrak{n}$. Thus $B'_{\mathfrak{n}'} \subseteq B_\mathfrak{n}$. By symmetry the two rings are equal. This is the argument of Lemma 1.1.1, applied to two models that need not be contained in each other. The remark covers in particular the case $v(x) = v(y)$, where both $x$ and $y$ can serve as the denominator.

**Proposition 1.1.3.** In Definition 1.1.2 exactly one of these cases holds.

1. $\mathfrak{n} = xB$. Then $R_1$ is a discrete valuation ring, and $R_1 = \mathcal{O}_v$.
2. $\mathfrak{n} = xB + \tilde{h}B$, where $\tilde{h} \in B$ maps to a monic irreducible polynomial $h \in \kappa[Y]$. Then $R_1$ is a regular local ring of dimension 2, the elements $x, \tilde{h}$ form a regular system of parameters of $R_1$, and the residue field of $R_1$ is $\kappa[Y]/(h)$, a finite extension of $\kappa$.

Lean: none yet

*Proof.* The ideal $\mathfrak{n}$ contains $x$, because $x \in \mathfrak{m} \subseteq \mathfrak{m}_v$. So $\mathfrak{n}/xB$ is a prime ideal of $\kappa[Y]$. It is either 0 or generated by one monic irreducible polynomial $h$.

In the first case $\mathfrak{n} = xB$. A nonzero principal prime of a Noetherian domain has height 1, by the principal ideal theorem. So $R_1 = B_{xB}$ is a regular local ring of dimension 1, that is, a discrete valuation ring (Volume 1, Theorem 1.4.2). The valuation ring $\mathcal{O}_v$ dominates $R_1$, and a valuation ring is maximal for domination (Volume 3, Theorem 1.3.2). So $\mathcal{O}_v = R_1$.

In the second case choose $\tilde{h} \in B$ that maps to $h$. Then $\mathfrak{n} = xB + \tilde{h}B$. The chain $0 \subsetneq xB \subsetneq \mathfrak{n}$ of primes shows that $\mathfrak{n}$ has height at least 2. By the principal ideal theorem, an ideal with two generators has height at most 2. So $R_1$ is a local ring of dimension 2 whose maximal ideal has two generators. It is regular. Its residue field is $B/\mathfrak{n} = \kappa[Y]/(h)$. $\square$

The first case happens when the residue of $y/x$ in $\kappa_v$ is transcendental over $\kappa$. Then $v$ is the order of vanishing along the exceptional curve. In the second case the residue of $y/x$ is algebraic over $\kappa$, with minimal polynomial $h$.

### Strict transforms

For $f \in R$ with $f \ne 0$ let $\operatorname{ord}(f)$ be the largest $a$ with $f \in \mathfrak{m}^a$. By Volume 1, Proposition 1.10.1, the graded ring $\operatorname{gr}_\mathfrak{m}(R)$ is the polynomial ring $\kappa[X, Y]$, where $X$ and $Y$ are the classes of $x$ and $y$. The *initial form* of $f$ is the class $F$ of $f$ in $\mathfrak{m}^a/\mathfrak{m}^{a+1}$, with $a = \operatorname{ord}(f)$. It is a nonzero homogeneous polynomial of degree $a$ in $X$ and $Y$. Since $\kappa[X, Y]$ is a domain, $\operatorname{ord}(fg) = \operatorname{ord}(f) + \operatorname{ord}(g)$, and the initial form of $fg$ is the product of the initial forms.

**Definition 1.1.4 (strict transform).** Let $f \in R$ with $f \ne 0$ and $a = \operatorname{ord}(f)$. Since $f \in \mathfrak{m}^a$ and $\mathfrak{m}^aB = x^aB$, there is a unique $f' \in B$ with $f = x^af'$. We call $f'$, and its image in $R_1$, the *strict transform* of $f$.

**Lemma 1.1.5.** Let $f, g \in R$ be nonzero, with $a = \operatorname{ord}(f)$ and initial form $F$.

1. The image of $f'$ in $B/xB = \kappa[Y]$ is $F(1, Y)$. In particular $f' \notin xB$, and $f'$ is not divisible by $x$ in $R_1$.
2. $(fg)' = f'g'$.
3. In case 2 of Proposition 1.1.3, the length of $R_1/(x, f')$ is the order of $h$ in $F(1, Y)$. It is at most $a$. Also $\operatorname{ord}_{R_1}(f') \le a$.

Lean: none yet

*Proof.* Part 1. Write $f = \sum_{i + j = a} c_{ij}x^iy^j + r$ with $c_{ij} \in R$ and $r \in \mathfrak{m}^{a+1}$. Then $F = \sum \bar{c}_{ij}X^iY^j$. Since $r \in \mathfrak{m}^{a+1}B = x^{a+1}B$, we get $f' = \sum c_{ij}(y/x)^j + x b$ for some $b \in B$. So the image of $f'$ in $\kappa[Y]$ is $\sum \bar{c}_{ij}Y^j = F(1, Y)$. This polynomial is not 0, because $F = X^aF(1, Y/X)$ in $\kappa(X, Y)$ and $F \ne 0$. Thus $f' \notin xB$. The ring $R_1/xR_1$ is a localization of the domain $\kappa[Y]$, so the image of $f'$ in it is not 0 either.

Part 2. We have $fg = x^{a+b}f'g'$ with $b = \operatorname{ord}(g)$, and $\operatorname{ord}(fg) = a + b$. Since $B$ is a domain, $(fg)' = f'g'$.

Part 3. The ring $R_1/xR_1 = \kappa[Y]_{(h)}$ is a discrete valuation ring with uniformizer $h$. So the length of $R_1/(x, f')$ is the order $e$ of $h$ in $F(1, Y)$, and $e \deg h \le \deg F(1, Y) \le a$. If $f' \in \mathfrak{m}_{R_1}^n$, then its image in $\kappa[Y]_{(h)}$ lies in $(h^n)$, so $n \le e \le a$. $\square$

**Lemma 1.1.6.** Assume case 2 of Proposition 1.1.3. If $f, g \in R$ are nonzero and have no common prime factor in $R$, then $f'$ and $g'$ have no common prime factor in $R_1$.

Lean: none yet

*Proof.* A regular local ring is a unique factorization domain [Mat, Theorem 20.3]. This is node SG00000023 of the map. So $R$ and $R_1$ are unique factorization domains, and their height 1 primes are principal. Assume that a height 1 prime $\mathfrak{q}$ of $R_1$ contains $f'$ and $g'$. By Lemma 1.1.5, $f' \notin xR_1$. The ideal $xR_1$ is a prime of height 1, so $x \notin \mathfrak{q}$. Let $Q = \mathfrak{q} \cap B$. Then $x \notin Q$, and $Q$ has height 1, because $R_1$ is a localization of $B$. Now $B_x = R_x$, because $y/x \in R_x$. So $QB_x$ is a height 1 prime of $R_x$, and $P = Q \cap R$ is a height 1 prime of $R$. It contains $f = x^af'$ and $g = x^bg'$. So the generator of $P$ is a common prime factor of $f$ and $g$, a contradiction. $\square$

**Example 1.1.7.** Let $R = k[x, y]_{(x, y)}$, and let $v$ be the monomial valuation of Volume 3, Lemma 1.6.1, with $v(x) = 1$ and $v(y) = \sqrt{2}$, with values in $\mathbb{R}$. Then $v(x) < v(y)$, and $B = R[y_1]$ with $y_1 = y/x$. Since $v(y_1) = \sqrt{2} - 1 > 0$, the center of $v$ on $B$ is the ideal $(x, y_1)$, so $h = Y$ and $R_1 = k[x, y_1]_{(x, y_1)}$. Let $f = y^2 - x^3$. Then $\operatorname{ord}(f) = 2$, the initial form is $Y^2$, and $f = x^2(y_1^2 - x)$. So $f' = y_1^2 - x$, and $\operatorname{ord}_{R_1}(f') = 1$. The curve $f = 0$ is the cusp, and its strict transform is a regular curve that is tangent to the exceptional curve $x = 0$. The length of $R_1/(x, f')$ is 2, the order of $Y$ in $F(1, Y) = Y^2$.

Example 1.1.7 has $h = Y$, so the residue field does not change. The two examples below show the other possibilities of Proposition 1.1.3. In the first one the center is the exceptional curve. In the second one the residue field of $R_1$ is a proper extension of $\kappa$. Both cases come back in the proof of Theorem 1.2.6.

**Example 1.1.8.** Let $R = k[x, y]_{(x, y)}$.

1. Let $v = \operatorname{ord}_\mathfrak{m}$ be the order valuation, so that $v(f) = \operatorname{ord}(f)$ for $f \in R$ (Volume 3, Example 1.6.2 with $a = b = 1$). Then $v(x) = v(y) = 1$, and $y/x$ is a unit of $\mathcal{O}_v$. Its residue is transcendental over $k$, because for a nonzero polynomial $q \in k[Y]$ of degree $d$ the element $x^dq(y/x)$ is a homogeneous form of degree $d$, so $v(q(y/x)) = 0$. So case 1 of Proposition 1.1.3 holds, and $R_1 = B_{xB} = \mathcal{O}_v$. One quadratic transform makes the center a curve, and the sequence stops.
2. Let $k = \mathbb{Q}$. Consider the arc $x \mapsto t$, $y \mapsto \psi = \sqrt{2}\,t + \sum_{i \ge 2} t^{i!}$ in $\mathbb{Q}(\sqrt{2})[[t]]$. By Volume 3, Lemma 1.6.5, applied over the field $\mathbb{Q}(\sqrt{2})$, the series $\varphi = \sum_{i \ge 1} t^{i!}$ is transcendental over $\mathbb{Q}(\sqrt{2})(t)$. Since $\psi - \varphi = (\sqrt{2} - 1)t$ lies in $\mathbb{Q}(\sqrt{2})(t)$, the series $\psi$ is also transcendental over this field. So $f \mapsto f(t, \psi)$ is injective on $\mathbb{Q}[x, y]$, and $v(f) = \operatorname{ord}_t f(t, \psi)$ defines a valuation of $\mathbb{Q}(x, y)$ that dominates $R$. Then $v(x) = v(y) = 1$, and $y/x$ maps to $\sqrt{2} + \sum_{i \ge 2} t^{i! - 1}$, so its residue is $\sqrt{2}$. Thus $h = Y^2 - 2$, and $R_1$ is the localization of $B = R[y_1]$ at $(x, y_1^2 - 2)$, with $y_1 = y/x$. The residue field of $R_1$ is $\mathbb{Q}(\sqrt{2})$, of degree 2 over $\kappa = \mathbb{Q}$. The center of $v$ on $\operatorname{Spec} B$ is a closed point that is not rational over $\mathbb{Q}$.

*Example (strict transform at a point of degree 2).* We continue Example 1.1.8.2 and test Lemma 1.1.5.3 when $\deg h = 2$. Let $f = y^2 - 2x^2 + y^3$ in $R = \mathbb{Q}[x, y]_{(x, y)}$. Then $\operatorname{ord}(f) = 2$, and the initial form is $F = Y^2 - 2X^2$. With $y = xy_1$ we get $f = x^2(y_1^2 - 2 + xy_1^3)$, so $f' = y_1^2 - 2 + xy_1^3$. Its image in $\kappa[Y] = \mathbb{Q}[Y]$ is $Y^2 - 2 = F(1, Y)$, as part 1 says. The order of $h = Y^2 - 2$ in $F(1, Y)$ is $e = 1$. So the length of $R_1/(x, f')$ is 1, and indeed $R_1/(x, f') = \mathbb{Q}[Y]_{(h)}/(h) = \mathbb{Q}(\sqrt{2})$ is a field. The bound of part 3 reads $e \deg h = 2 \le 2 = a$, with equality. Over $\mathbb{Q}(\sqrt{2})$ the same curve has two branches, with tangents $y = \pm\sqrt{2}x$, and each meets the exceptional curve in a rational point with length 1. Over $\mathbb{Q}$ the two branches are conjugate, and the strict transform meets the exceptional curve in one point of degree 2. A length counts points with their residue degree only after we multiply by $\deg h$. This is the reason for the weights in the Noether inequality below.

*Remark (the characteristic).* Nothing in this section uses the characteristic of $k$. The chart $B$, the dichotomy of Proposition 1.1.3, the strict transform and Lemmas 1.1.5 and 1.1.6 hold over any field. Their proofs use only that $R$ is a regular local ring of dimension 2. The polynomial $h$ can be inseparable over $\kappa$ when $\kappa$ is not perfect. For example, if $\kappa = \mathbb{F}_p(s)$ and the residue of $y/x$ is $s^{1/p}$, then $h = Y^p - s$. This does not affect the proofs here. It matters later, in Section 1.3, where the existence of an étale generator needs a separable residue extension.

### Notes and references

The quadratic transforms of a regular local ring of dimension 2 are studied in [Abh56], and they are the main tool of Zariski for surfaces [Zar39]. The book [Cut04] gives an account of the resolution of surfaces with these tools. Volume 4, Chapter 1, treats the blowup of a point on a surface as a scheme. The Lean library proves the facts on the chart $B$ that we use: `Singularity.Algebra.blowupChartQuotientEquiv` is the isomorphism $B/xB \cong \kappa[Y]$, and `Singularity.Algebra.isRegularRing_blowupChart` is the regularity of $B$. The quadratic transform along a valuation and the strict transform are not in the library.
