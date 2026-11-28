---
title: Hypersurfaces of maximal contact
nodes: [SG00000045]
sources: [Kol07, Hir64, Gir75, Hau03, EH02]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Hypersurfaces of maximal contact

Let $I$ be an ideal sheaf on $X$ with maximal order $m \ge 1$. By Corollary 2.1.5 the locus of order $m$ is the zero set of $D^{m-1}(I)$. This ideal has order 1 at each point of the locus, so it contains, locally, the equation of a smooth hypersurface. This section shows that such a hypersurface keeps containing the locus of order $m$ after each blowup sequence of order $m$.

The idea is old. For a plane curve $f(x, y) = 0$ of multiplicity $m$ at the origin, written as $y^m + a_1(x) y^{m-1} + \dots + a_m(x)$, the substitution $y \mapsto y - a_1(x)/m$ removes the term $a_1$. After it, the curve $(y = 0)$ follows the branches of $f$ as closely as a smooth curve can, and the points of multiplicity $m$ that appear after blowups lie on its transforms. This is the Tschirnhausen transformation. The maximal contact ideal $MC(I)$ is the form of this idea that needs no coordinates and no Weierstrass preparation: for $f$ as above, $D^{m-1}(f)$ contains $\partial_y^{m-1} f = m! \, y + (m-1)! \, a_1$, and its zero set is the curve $y = -a_1/m$. The division by $m$ is the place where the characteristic enters; Volume 7, Section 4.1, shows that in characteristic $p$ with $p \mid m$ no translation of $y$ changes $a_1$.

**Definition 2.3.1 (maximal contact).** Let $m = \operatorname{max\text{-}ord} I \ge 1$. The ideal $MC(I) = D^{m-1}(I)$ is the *maximal contact ideal* of $I$. A *hypersurface of maximal contact* for $I$ is a smooth hypersurface $H \subseteq X$ whose ideal sheaf $\mathcal{O}_X(-H)$ is contained in $MC(I)$.

**Lemma 2.3.2 (local existence).** Let $m = \operatorname{max\text{-}ord} I \ge 1$ and let $x$ be a closed point with $\operatorname{ord}_x I = m$. Then there are an open set $U \ni x$ and a hypersurface of maximal contact $H \subseteq U$ for $I|_U$. Each hypersurface of maximal contact $H$ contains $\operatorname{cosupp}(I, m)$.

Node: SG00000045 · Lean: `Singularity.exists_mem_derivIdeal_iterate_ord_eq_one` (the claim that $D^{m-1}(I)$ has an element of order 1 at the origin of affine space)

*Proof.* By Lemma 2.1.4, $\operatorname{ord}_x MC(I) = m - (m - 1) = 1$. So $MC(I)_x \subseteq \mathfrak{m}_x$, and there is $h \in MC(I)_x$ with $h \notin \mathfrak{m}_x^2$. The germ $h$ is a section of $MC(I)$ over some open set $U_0 \ni x$.

The class of $h$ in $\mathfrak{m}_x / \mathfrak{m}_x^2$ is not zero. This space has dimension $n$ over $K = k(x)$. Choose $x_2, \dots, x_n \in \mathfrak{m}_x$ whose classes, together with the class of $h$, form a basis. We shrink $U_0$ so that $x_2, \dots, x_n$ are regular on $U_0$. By the paragraph on coordinates at the start of Section 2.1, the map $\mathfrak{m}_x / \mathfrak{m}_x^2 \to \Omega_{X/k} \otimes k(x)$ is an isomorphism. So the values $dh(x), dx_2(x), \dots, dx_n(x)$ form a basis of the fiber of $\Omega_{X/k}$ at $x$. The sheaf $\Omega_{X/k}$ is locally free of rank $n$. By the lemma of Nakayama the $n$ sections $dh, dx_2, \dots, dx_n$ generate it on an open set $U \ni x$ with $U \subseteq U_0$, and $n$ generators of a free module of rank $n$ form a basis. Also by Nakayama, $h, x_2, \dots, x_n$ generate $\mathfrak{m}_x$. So $h, x_2, \dots, x_n$ are local coordinates at $x$ on $U$.

These functions define a morphism $\varphi \colon U \to \mathbb{A}^n_k$, and $\varphi$ is étale because it induces an isomorphism on differentials. The closed subscheme $H = (h = 0)$ of $U$ is the inverse image of the hyperplane $(t_1 = 0)$. So $H$ is étale over $\mathbb{A}^{n-1}_k$, hence smooth of pure dimension $n - 1$, and in particular reduced. It contains $x$. Its ideal sheaf is $\mathcal{O}_U(-H) = h \, \mathcal{O}_U$, and $h$ is a section of $MC(I)$ over $U$, so $\mathcal{O}_U(-H) \subseteq MC(I)|_U$. Thus $H$ is a hypersurface of maximal contact for $I|_U$.

For the last claim, let $H$ be any hypersurface of maximal contact. By Corollary 2.1.5, $\operatorname{cosupp}(I, m)$ is the zero set of $MC(I)$. Since $\mathcal{O}_X(-H) \subseteq MC(I)$, the zero set of $MC(I)$ lies in the zero set of $\mathcal{O}_X(-H)$, which is $H$. $\square$

The proof shows more. Near a point $x$ of order $m$, each section $h$ of $MC(I)$ with $h \notin \mathfrak{m}_x^2$ defines a hypersurface of maximal contact near $x$. Here is the classical form of this choice. Let $f$ be a section of $I$ near $x$, and let $x_1, \dots, x_{n-1}, z$ be local coordinates at $x$ such that $\partial_z^m f$ is a unit at $x$. Put $h = \partial_z^{m-1} f$. Then $h \in D^{m-1}(I) = MC(I)$. Also $\partial_z h = \partial_z^m f$ is a unit at $x$, and a derivation maps $\mathfrak{m}_x^2$ into $\mathfrak{m}_x$, so $h \notin \mathfrak{m}_x^2$. So $(\partial_z^{m-1} f = 0)$ is a hypersurface of maximal contact near $x$. If $f = z^m + a_1 z^{m-1} + \dots + a_m$ with $\partial_z a_i = 0$ for all $i$, then
$$\partial_z^{m-1} f = m! \, z + (m-1)! \, a_1 = m! \Big( z + \frac{a_1}{m} \Big).$$
The hypersurface $z + a_1/m = 0$ is the hypersurface of the Tschirnhausen transformation $z \mapsto z + a_1/m$. In the new coordinate $z' = z + a_1/m$ the polynomial $f$ has no term in $z'^{m-1}$. The formula divides by $m$. Section 2.4 shows what happens when $m$ is a multiple of the characteristic.

A global hypersurface of maximal contact need not exist, and the local ones are not unique. Section 3.2 deals with the choice of $H$, and Section 3.3 with the passage from local to global.

**Theorem 2.3.3 (maximal contact).** Let $m = \operatorname{max\text{-}ord} I \ge 1$, let $H \subseteq X$ be a hypersurface of maximal contact for $I$, and let $(X_r, I_r, E_r) \to \dots \to (X_0, I_0, E_0) = (X, I, E)$ be a blowup sequence of order $m$. Let $H_0 = H$ and let $H_{i+1}$ be the birational transform of $H_i$. Then for each $i$:

1. $\mathcal{O}_{X_i}(-H_i) \subseteq J^{(m-1)}_i \subseteq MC(I_i)$, with $J^{(m-1)}_i$ as in Theorem 2.2.7;
2. $\operatorname{cosupp}(I_i, m) \subseteq H_i$, and in particular the center $Z_i$ lies in $H_i$;
3. $H_{i+1}$ is smooth, and it is a hypersurface of maximal contact for $I_{i+1}$ whenever $\operatorname{max\text{-}ord} I_{i+1} = m$.

Node: SG00000045 · Lean: `Singularity.chartSubst_X_of_ne`, `Singularity.X_mem_centerChartTransformIdeal_one` (part 1 in one chart), `Singularity.eq_zero_of_X_mem_derivIdeal_iterate` (part 2 for $i = 0$). Part 3 and the statements for sequences of blowups are not in Lean yet.

*Proof.* We first compute the transform of $H_i$ near the center. Let $\pi_i \colon X_{i+1} \to X_i$ be the blowup of a smooth center $Z_i \subseteq H_i$, with exceptional divisor $F_i$. Let $x \in Z_i$ be a closed point, and let $c$ be the codimension of $Z_i$ in $X_i$ at $x$. Since $Z_i \subseteq H_i$ are both smooth, there are local coordinates $x_1, \dots, x_n$ on an open set $U \ni x$ with $H_i \cap U = (x_1 = 0)$ and $Z_i \cap U = (x_1 = \dots = x_c = 0)$. To find them, take coordinates on $H_i$ at $x$ in which $Z_i$ is a coordinate subspace, lift them to $X_i$, and add an equation $x_1$ of $H_i$. Assume $c \ge 2$, and use the charts $U_1, \dots, U_c$ of Lemma 2.2.2.

- On $U_1$ we have $\pi_i^* x_1 = y_1$, and $F_i \cap U_1 = (y_1 = 0)$. So $\pi_i^{-1}(H_i \setminus Z_i)$ does not meet $U_1$, and the birational transform $H_{i+1}$, the closure of this set, does not meet $U_1$. The function $\pi_i^* x_1$ generates $\mathcal{O}(-F_i)$ on $U_1$.
- On $U_j$ with $2 \le j \le c$ we have $\pi_i^* x_1 = y_1 y_j$, and $F_i \cap U_j = (y_j = 0)$. The set $\pi_i^{-1}(H_i \setminus Z_i) \cap U_j$ is $(y_1 = 0)$ minus $(y_1 = y_j = 0)$, and its closure is the smooth hypersurface $(y_1 = 0)$. So $H_{i+1} \cap U_j = (y_1 = 0)$, and $\pi_i^* x_1 = y_j \cdot y_1$ generates $\mathcal{O}(-F_i - H_{i+1})$ on $U_j$.

Over $X_i \setminus Z_i$ the blowup is an isomorphism and $F_i$ is empty. Thus, for $c \ge 2$,
$$\pi_i^* \mathcal{O}_{X_i}(-H_i) = \mathcal{O}_{X_{i+1}}(-H_{i+1} - F_i), \tag{2.3.1}$$
and $H_{i+1}$ is smooth. The restrictions of $y_2, \dots, y_n$ to $(y_1 = 0)$ are the chart coordinates of the blowup of $H_i$ along $Z_i$, so $H_{i+1}$ is this blowup. If $c = 1$, then $Z_i$ is a union of connected components of $H_i$, the blowup is the identity, $F_i = Z_i$, and $H_{i+1}$ is the union of the other components. Formula (2.3.1) holds also in this case, and $H_{i+1}$ is again smooth.

We prove (1) and (2) by induction on $i$. For $i = 0$, the first inclusion of (1) is the definition, since $J^{(m-1)}_0 = D^{m-1}(I)$. The second inclusion of (1) holds for each $i$ by Theorem 2.2.7. Assume the first inclusion of (1) for $i$. By Lemma 2.1.4, $\operatorname{cosupp}(I_i, m)$ lies in the zero set of $D^{m-1}(I_i)$. Since $J^{(m-1)}_i \subseteq D^{m-1}(I_i)$, the zero set of $D^{m-1}(I_i)$ lies in the zero set of $J^{(m-1)}_i$, and this lies in the zero set of $\mathcal{O}(-H_i)$, which is $H_i$. This is (2) for $i$. In particular $Z_i \subseteq H_i$, so (2.3.1) applies. By Theorem 2.2.7, $Z_i \subseteq \operatorname{cosupp}(J^{(m-1)}_i, 1)$, and the transform of $(J^{(m-1)}_i, 1)$ is $J^{(m-1)}_{i+1} = \mathcal{O}(F_i) \cdot \pi_i^* J^{(m-1)}_i$. It contains
$$\mathcal{O}(F_i) \cdot \pi_i^* \mathcal{O}(-H_i) = \mathcal{O}(F_i) \cdot \mathcal{O}(-H_{i+1} - F_i) = \mathcal{O}(-H_{i+1}).$$
This is (1) for $i + 1$.

(3) We saw that $H_{i+1}$ is smooth. By Corollary 2.2.8, $\operatorname{max\text{-}ord} I_{i+1} \le m$. If it is $m$, then $MC(I_{i+1}) = D^{m-1}(I_{i+1})$, and (1) says that $H_{i+1}$ is a hypersurface of maximal contact for $I_{i+1}$. $\square$

The computation (2.3.1) holds in every characteristic. The proof of (1) and (2) uses only Theorem 2.2.7 and the inequality $\operatorname{ord}_x D^j(I) \ge \operatorname{ord}_x I - j$. In positive characteristic the difficulty comes before the theorem: the ideal $D^{m-1}(I)$ need not contain an element of order 1, so there may be no $H$ to start with. Section 2.4 makes this precise.

The theorem has an important consequence. The whole blowup sequence of order $m$ takes place inside the hypersurfaces $H_i$. So it should be possible to describe it on $H$, a variety of dimension $n - 1$. The problem is to find the right ideal on $H$. The restriction $I|_H$ is not the right ideal, as the next example shows.

**Example 2.3.4.** Let $I = (xy - z^n)$ on $\mathbb{A}^3$ with $n \ge 2$. The order of $I$ is 2 at the origin and at most 1 elsewhere, so $m = 2$, and
$$MC(I) = D(I) = (xy - z^n, \; y, \; x, \; n z^{n-1}) = (x, \; y, \; z^{n-1}).$$
So $\operatorname{cosupp}(I, 2)$ is the origin, and $H = (x = 0)$ and $H' = (x - y = 0)$ are hypersurfaces of maximal contact. The restriction of $I$ to $H$ is $(z^n)$ in the coordinates $y, z$ of $H$. It has order at least 2 along the whole line $(z = 0)$ of $H$, which is not in $\operatorname{cosupp}(I, 2)$. The restriction of $I$ to $H'$ is $(y^2 - z^n)$ in the coordinates $y, z$, which has order 2 only at the origin. So the restriction of $I$ depends on $H$ and it does not see the locus of order $m$. The derivatives of $I$ correct this. On $H$,
$$\big( I + D(I)^2 \big)\big|_H = (z^n) + (y, z^{n-1})^2 = (y^2, \; y z^{n-1}, \; z^n),$$
because $2n - 2 \ge n$. This ideal has order at least 2 only at the origin. It is the coefficient ideal of Section 3.2 for $m = 2$.

Lean: `Singularity.DerivativeIdeals.derivIdeal_xy_sub_z_pow`, `Singularity.DerivativeIdeals.coeffIdeal_H`, `Singularity.DerivativeIdeals.coeffIdeal_H'`

The next example shows the theorem at work in the running example, and it shows that a smooth hypersurface through the points of order $m$ can lose them after one blowup.

**Example 2.3.5 (contact along a blowup sequence).** Let $I = (y^2 - x^5)$ on $\mathbb{A}^2$. By Example 2.1.8, $m = 2$, $MC(I) = (y, x^4)$, and $\operatorname{cosupp}(I, 2)$ is the origin. The curve $H = (y = 0)$ is a curve of maximal contact. The curve $H' = (y = x)$ also passes through the origin, but it is not a curve of maximal contact, because $y - x \notin (y, x^4)$.

Blow up the origin, with the charts of Example 2.2.9. In the chart with $y = y_1 x$ we have $\pi^* y = x y_1$ and $\pi^*(y - x) = x(y_1 - 1)$. So the birational transforms are $H_1 = (y_1 = 0)$ and $H'_1 = (y_1 = 1)$ in this chart. By Example 2.2.9 the other chart has no point of order 2 of $I_1$. The only point of order 2 of $I_1 = (y_1^2 - x^3)$ is $p_1 = (x = y_1 = 0)$. It lies on $H_1$ and not on $H'_1$. On the chart, $\mathcal{O}(-H_1) = (y_1)$ lies in $J^{(1)}_1 = (y_1, x^3)$, which lies in $MC(I_1) = (y_1, x^2)$, as part (1) of Theorem 2.3.3 says. So $H_1$ is a curve of maximal contact for $I_1$. After the second blowup of Example 2.2.9 the maximal order is 1, and the sequence ends.

The name comes from the order of contact. The restriction of $y^2 - x^5$ to $H$ is $x^5$, of order 5, and its restriction to $H'$ is $x^2 - x^5$, of order 2. A smooth curve germ through the origin is $(y = \varphi(x))$ or $(x = \psi(y))$ with $\varphi, \psi$ of order at least 1. The restriction of $y^2 - x^5$ is $\varphi^2 - x^5$, of order at most 5, or $y^2 - \psi^5$, of order 2. So $H$ has the highest order of contact with the curve $(y^2 = x^5)$ among all smooth curves through the origin.

Lean: `Singularity.CharZeroExamples.sub_not_mem_mc`, `Singularity.CharZeroExamples.ord_restrict_H`, `Singularity.CharZeroExamples.ord_restrict_H'`, `Singularity.CharZeroExamples.derivIdeal_transform`, `Singularity.CharZeroExamples.mc_chain_transform` (the computations, with no definition of maximal contact)

**Remark 2.3.6.** Theorem 2.3.3 needs the blowup sequence to be of order $m$, with $m$ the maximal order. For a marked ideal $(I, m)$ with $m$ less than the maximal order, the locus $\operatorname{cosupp}(I, m)$ need not lie in a smooth hypersurface. For example, $I = (xy)$ on $\mathbb{A}^2$ has maximal order 2, and $\operatorname{cosupp}(I, 1)$ is the union of the two lines $x = 0$ and $y = 0$, which is not contained in a smooth curve near the origin. This is why the induction of Chapter 3 treats ideals of maximal order $m$ and marked ideals in different steps.

*Example (tangency is not enough).* Let $f = (y - x^2)^2 - x^7$ on $\mathbb{A}^2$. Then $\partial_y f = 2(y - x^2)$ and $\partial_x f = -4x(y - x^2) - 7x^6$, so
$$D(f) = (y - x^2, \; x^6) = MC(f), \qquad \operatorname{max\text{-}ord} f = 2,$$
and $\operatorname{cosupp}(f, 2)$ is the origin. The curve $H' = (y = x^2)$ is a curve of maximal contact. The line $H = (y = 0)$ is tangent to $H'$ at the origin, and the restriction $f|_H = x^4 - x^7$ has order $4 \ge 2$. So $H$ passes the obvious tests: it contains the point of order 2, it is tangent to the right curve, and the restriction of $f$ to it has high order. But $y \notin MC(f)$, because modulo $y - x^2$ the function $y$ becomes $x^2$, and $x^2 \notin (x^6)$ in $k[x]$. So $H$ is not a curve of maximal contact. We follow both curves through two blowups. We checked the charts below with a computer algebra system.

Blow up the origin. In the chart $y = x y_1$ the pullback is $x^2 \big( (y_1 - x)^2 - x^5 \big)$, so $f_1 = (y_1 - x)^2 - x^5$. In the chart $x = x_1 y$ the pullback is $y^2 \big( (1 - x_1^2 y)^2 - x_1^7 y^5 \big)$, and the second factor is a unit near the exceptional curve. So $\operatorname{cosupp}(f_1, 2)$ is the origin of the first chart. The transforms are $H_1 = (y_1 = 0)$ and $H'_1 = (y_1 = x)$, and both pass through this point.

Blow up the origin again. In the chart $y_1 = x y_2$ the pullback is $x^2 \big( (y_2 - 1)^2 - x^3 \big)$, so $f_2 = (y_2 - 1)^2 - x^3$, and its only point of order 2 on this chart is $(x, y_2) = (0, 1)$. In the other chart, $x = x_2 y_1$, the transform is $(1 - x_2)^2 - x_2^5 y_1^3$, and its only point of order 2 on the exceptional curve is the same point, $x_2 = 1$. So $\operatorname{cosupp}(f_2, 2)$ is the point $y_2 = 1$ of the new exceptional curve. The transform $H'_2 = (y_2 = 1)$ passes through it, as Theorem 2.3.3 says. The transform $H_2 = (y_2 = 0)$ does not: at its point $(0, 0)$ on the exceptional curve the function $f_2$ takes the value 1. So after two blowups of order 2 the line $H$ has lost the point of order 2.

The example refines Example 2.3.5. There the line $(y = x)$ was transversal to the curve of maximal contact, and it lost the point after one blowup. Here $H$ has contact of order 2 with $H'$, and it loses the point after two blowups. In general a smooth curve with contact of order $e$ with $H'$ at the origin follows the points of order 2 for $e$ blowups and then loses them, as long as the points of order 2 last that long. The maximal contact ideal is the algebraic form of the condition that a hypersurface has enough contact for all the blowups at once.

### Notes and references

Maximal contact goes back to Hironaka [Hir64], and Kollár attributes the theory of maximal contact to Hironaka and Giraud [Kol07, Chapter 3]. Giraud studies what remains of it in positive characteristic in [Gir75]. Theorem 2.3.3 is in [Kol07, Chapter 3], Section "Maximal contact and going down"; see also [EH02] and [Hau03] for the same theorem in the language of their invariants.
