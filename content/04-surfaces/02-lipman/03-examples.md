---
title: Examples in characteristic p
nodes: []
sources: [Har, Mat, AM69, Lip78]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Examples in characteristic p

In this section we run the process of Theorem 2.2.1 on some surfaces in $\mathbb{A}^3_k$. All computations are in the charts of Lemma 1.1.6. The first family works over each field. The second example is a purely inseparable equation in characteristic $p$, and its first blowup produces $p + 1$ singular points. The third example shows that the normalization step is necessary, and it gives a singularity that is not rational. The last example computes the cohomology of the resolution of $xy = z^2$ and compares it with the third. The second half of the section computes complete resolutions with their dual graphs: the chain $A_{m-1}$, the singularities $D_4$ and $E_6$, the equation $z^2 + x^3 + y^5$ in characteristics 2, 3 and 5, and the cone over a plane cubic. For $D_4$ and $E_6$ we also show an equation that behaves differently in a small characteristic.

### Singular points of a surface in affine space

**Lemma 2.3.1.** Let $k$ be a field, let $F \in k[x, y, z]$ be nonzero, let $X = V(F)$, and let $P \in X$ be a closed point with maximal ideal $\mathfrak{m}_P \subseteq k[x, y, z]$. Then $\dim \mathcal{O}_{X,P} = 2$, and $\mathcal{O}_{X,P}$ is regular if and only if $F \notin \mathfrak{m}_P^2$. If $P = (a, b, c)$ is a rational point, then $F \notin \mathfrak{m}_P^2$ if and only if one of the partial derivatives of $F$ is nonzero at $P$.

Lean: `Singularity.mem_pointIdeal_sq_iff` (the claim for a rational point)

*Proof.* Let $R = k[x, y, z]_{\mathfrak{m}_P}$. It is a regular local ring of dimension 3 [Har, Theorem I.1.8A], and $\mathcal{O}_{X,P} = R/(F)$. Since $F$ is a nonzerodivisor of $R$, we get $\dim R/(F) = 2$ [AM69, Corollary 11.18]. If $F \notin \mathfrak{m}_P^2$, then $R/(F)$ is regular by Proposition 1.2.6 of Volume 1. If $F \in \mathfrak{m}_P^2$, then the maximal ideal $\mathfrak{n}$ of $R/(F)$ has $\mathfrak{n}/\mathfrak{n}^2 \cong \mathfrak{m}_P/\mathfrak{m}_P^2$, of dimension 3 over $\kappa(P)$, so $R/(F)$ is not regular. For a rational point, the Taylor expansion of $F$ at $P$ has the partial derivatives at $P$ as its linear coefficients, in every characteristic. Since $F(P) = 0$, we get $F \in \mathfrak{m}_P^2$ if and only if these coefficients vanish. $\square$

The Lean proof of the last claim is for a polynomial ring over a commutative ring, in any number of variables. The claim on $\dim \mathcal{O}_{X,P}$ and the claim on regularity are not in Lean.

Let $X = V(F)$ with $F$ nonconstant. By the Jacobian criterion (Corollary 1.8.3 of Volume 1), each point of $X$ outside the common zeros of the three partial derivatives is regular. Thus, if these common zeros on $X$ are finitely many closed points, then $\operatorname{Sing}(X)$ is a finite set of closed points, and $X$ is normal by Lemma 1.2.6.

### The surfaces $xy = z^n$

**Proposition 2.3.2.** Let $k$ be a field of any characteristic, let $n \ge 1$, and let $X_n = V(xy - z^n) \subseteq \mathbb{A}^3_k$.

1. The scheme $X_n$ is integral and normal. It is regular for $n = 1$, and for $n \ge 2$ its only singular point is the origin.
2. Let $n \ge 2$ and let $X'$ be the blowup of $X_n$ at the origin. Then $X'$ is covered by three charts. The $x$-chart and the $y$-chart are isomorphic to $\mathbb{A}^2_k$. The $z$-chart is isomorphic to $V(x_1 y_1 - 1)$ for $n = 2$ and to $X_{n-2}$ for $n \ge 3$.
3. For $n \ge 4$, the scheme $X'$ is normal, and its only singular point is the origin $Q$ of the $z$-chart. Near $Q$ it is isomorphic to $X_{n-2}$ near the origin. For $n = 2$ and $n = 3$, the scheme $X'$ is regular.
4. In the process of Theorem 2.2.1 for $X_n$, each normalization is the identity, and the process stops after $\lfloor n/2 \rfloor$ blowups.

Lean: `Singularity.an_xChart`, `Singularity.an_yChart`, `Singularity.an_zChart`, `Singularity.an_not_X_dvd_xChart` (part 2, the chart equations)

*Proof.* 1. Let $F = xy - z^n$. As a polynomial in $x$ over $k[y, z]$, it has degree 1, and its coefficients $y$ and $-z^n$ have no common factor. Thus $F$ is irreducible, and $X_n$ is integral. The partial derivatives are $F_x = y$, $F_y = x$ and $F_z = -n z^{n-1}$. A point of $X_n$ with $x = y = 0$ has $z^n = 0$, so it is the origin. By the remark after Lemma 2.3.1, $X_n$ is regular outside the origin and $X_n$ is normal. At the origin, $xy \in \mathfrak{m}^2$, and $z^n \in \mathfrak{m}^2$ if and only if $n \ge 2$. Lemma 2.3.1 gives part 1.

2. By Proposition 1.1.5, $X'$ is the strict transform of $X_n$ in the blowup of $\mathbb{A}^3_k$ at the origin. The least degree of a monomial of $F$ is 2, since $n \ge 2$. We use Lemma 1.1.6 in each chart, and we check each substitution twice.

In the $x$-chart, $y = x y_1$ and $z = x z_1$. Then $F = x \cdot x y_1 - x^n z_1^n = x^2 (y_1 - x^{n-2} z_1^n)$. The strict transform is $V(y_1 - x^{n-2} z_1^n)$. It is the graph of a function of $(x, z_1)$, so it is isomorphic to $\mathbb{A}^2_k$ with coordinates $x, z_1$. Check: $x^2 y_1 = x \cdot (x y_1) = xy$ and $x^2 \cdot x^{n-2} z_1^n = (x z_1)^n = z^n$.

In the $y$-chart, $x = y x_1$ and $z = y z_1$. Then $F = y x_1 \cdot y - y^n z_1^n = y^2 (x_1 - y^{n-2} z_1^n)$. The strict transform is isomorphic to $\mathbb{A}^2_k$ with coordinates $y, z_1$. Check: $y^2 x_1 = (y x_1) y = xy$ and $y^2 \cdot y^{n-2} z_1^n = (y z_1)^n = z^n$.

In the $z$-chart, $x = z x_1$ and $y = z y_1$. Then $F = z^2 x_1 y_1 - z^n = z^2 (x_1 y_1 - z^{n-2})$. The strict transform is $V(x_1 y_1 - z^{n-2})$ in the coordinates $x_1, y_1, z$. For $n \ge 3$ this is $X_{n-2}$, and for $n = 2$ it is $V(x_1 y_1 - 1)$. Check: $z^2 x_1 y_1 = (z x_1)(z y_1) = xy$ and $z^2 \cdot z^{n-2} = z^n$.

3. The surface $V(x_1 y_1 - 1)$ is regular, because the partial derivatives $y_1$ and $x_1$ do not both vanish on it. The surface $X_1$ is regular by part 1. Thus $X'$ is regular for $n = 2$ and $n = 3$. Let $n \ge 4$. By part 1 for $X_{n-2}$, the only singular point of the $z$-chart is $Q = (x_1, y_1, z) = (0, 0, 0)$. The $x$-chart meets the $z$-chart in the open set where $x_1 = x/z$ is a unit, and $x_1 = 0$ at $Q$. Thus $Q$ is not in the $x$-chart, and in the same way it is not in the $y$-chart. Thus $Q$ is the only singular point of $X'$. Each chart is normal by part 1, so $X'$ is normal.

4. The scheme $X_n$ is normal, so $X_0 = X_n$. For $n = 1$ no blowup is needed. For $n = 2, 3$ one blowup gives a regular scheme. For $n \ge 4$, the scheme $X_1 = X'$ is normal with one singular point $Q$. The blowup at $Q$ only changes the $z$-chart, which is $X_{n-2}$ with $Q$ at the origin. Thus the number $r(n)$ of blowups satisfies $r(1) = 0$, $r(2) = r(3) = 1$ and $r(n) = 1 + r(n - 2)$. This gives $r(n) = \lfloor n/2 \rfloor$. $\square$

The exceptional curve of the first blowup is the fibre over the origin. For $n \ge 3$, in the $z$-chart it is $V(z, x_1 y_1)$, the union of the two lines $x_1 = 0$ and $y_1 = 0$, which meet at $Q$. In the $x$-chart it is $V(x, y_1)$, and in the $y$-chart it is $V(y, x_1)$. Thus it is the union of two projective lines that meet at $Q$. For $n = 2$ it is the conic $xy = z^2$ in $\mathbb{P}^2_k$, which is regular in every characteristic, and it is isomorphic to $\mathbb{P}^1_k$. By induction, the exceptional locus of the resolution $X_{r(n)} \to X_n$ has $n - 1$ irreducible components: the conic for $n = 2$, two lines for $n = 3$, and for $n \ge 4$ the strict transforms of the two lines together with the $n - 3$ components for $X_{n-2}$.

**Remark 2.3.3.** Let $k$ have characteristic $p$ and let $p$ divide $n$. Then $F_z = -n z^{n-1} = 0$, but the computation above does not change. For $n = p$, the projection $(x, y, z) \mapsto (x, y)$ makes the function field $k(x, y)(z)$ of $X_p$ a purely inseparable extension of $k(x, y)$ of degree $p$, since $z^p = xy$ and $xy$ is not a $p$-th power in $k(x, y)$. Thus a purely inseparable cover of the plane can have a singularity that the process resolves as in characteristic 0.

Lean: none yet

### Purely inseparable equations

**Lemma 2.3.4.** Let $k$ be a field of characteristic $p > 0$, let $G \in k[s, t]$, and let $X = V(w^p - G(s, t)) \subseteq \mathbb{A}^3_k$. Let $P = (a, b, c)$ be a rational point of $X$. Then $P$ is a singular point of $X$ if and only if $G_s(a, b) = G_t(a, b) = 0$.

Lean: `Singularity.purelyInseparable_mem_pointIdeal_sq_iff_fin_two` (the claim that $F \in \mathfrak{m}_P^2$ if and only if $G_s(a, b) = G_t(a, b) = 0$)

*Proof.* Let $F = w^p - G$. Since $c^p = G(a, b)$, we have $F = (w - c)^p - (G - G(a, b))$. The first term is in $\mathfrak{m}_P^2$, because $p \ge 2$. The ideal $\mathfrak{m}_P^2$ is spanned by the monomials of degree at least 2 in $s - a$, $t - b$ and $w - c$. Thus $F \in \mathfrak{m}_P^2$ if and only if $G - G(a, b)$ has no linear term in $s - a$ and $t - b$, that is, $G_s(a, b) = G_t(a, b) = 0$. Lemma 2.3.1 gives the result. $\square$

The Lean proof of the claim on $\mathfrak{m}_P^2$ holds for each commutative ring $k$ of characteristic $p$. It uses the last claim of Lemma 2.3.1. The step from this claim to the singular point uses the first claims of Lemma 2.3.1, which are not in Lean. In Lean the variables $s, t, w$ are indexed by `Option (Fin 2)`, with `none` for $w$.

**Example 2.3.5.** Let $k$ be an algebraically closed field of characteristic $p > 0$, and let $X = V(z^p - x^{p+1} - y^{p+1}) \subseteq \mathbb{A}^3_k$. Then $X$ is normal with one singular point at the origin. The blowup $X'$ of $X$ at the origin is normal, and it has exactly $p + 1$ singular points $P_1, \dots, P_{p+1}$, all on the exceptional curve. Near each $P_i$, the surface $X'$ is isomorphic to $X_p = V(ab - c^p)$ near the origin. The process of Theorem 2.2.1 stops after $1 + \lfloor p/2 \rfloor$ blowups.

Lean: `Singularity.separable_one_add_X_pow_succ`, `Singularity.card_roots_one_add_X_pow_succ` (the chart equations and the $p + 1$ roots, not the claim on the singular points)

*Proof.* *The surface.* Let $g = x^{p+1} + y^{p+1}$ and $f = z^p - g$. Then $g_x = (p+1) x^p = x^p$ and $g_y = y^p$. By Lemma 2.3.4, a singular point has $x = y = 0$, and then $z^p = 0$, so $z = 0$. The origin is singular, since $f \in \mathfrak{m}^2$. Next, $f$ is irreducible. The derivative $g_x$ is not zero, so $g$ is not a $p$-th power in $k(x, y)$. Over an algebraic closure of $k(x, y)$ we have $z^p - g = (z - \gamma)^p$ with $\gamma^p = g$. A monic factor of degree $m$ with $0 < m < p$ is $(z - \gamma)^m$, and its coefficient of $z^{m-1}$ is $-m \gamma$. This is not in $k(x, y)$, since $\gamma \notin k(x, y)$. Thus $f$ is irreducible over $k(x, y)$, and since $f$ is monic in $z$, it is irreducible in $k[x, y, z]$. By Lemma 1.2.6, $X$ is normal.

*The $x$-chart.* The least degree of a monomial of $f$ is $p$. Put $y = x y_1$ and $z = x z_1$. Then $f = x^p z_1^p - x^{p+1} - x^{p+1} y_1^{p+1} = x^p (z_1^p - x h(y_1))$ with $h = 1 + y_1^{p+1}$. Check: $x^p z_1^p = z^p$, $x^p \cdot x = x^{p+1}$ and $x^p \cdot x y_1^{p+1} = (x y_1)^{p+1} = y^{p+1}$. The strict transform is $V(z_1^p - x h(y_1))$. Apply Lemma 2.3.4 with $w = z_1$ and $G = x h(y_1)$. Then $G_x = h(y_1)$ and $G_{y_1} = x h'(y_1) = x y_1^p$. A singular point has $h(y_1) = 0$. Then $y_1 \ne 0$, since $h(0) = 1$, so $x = 0$, and then $z_1 = 0$. The polynomial $h$ has $p + 1$ distinct roots $c_1, \dots, c_{p+1}$, because $h' = y_1^p$ has only the root 0 and $h(0) \ne 0$. Thus the singular points in the $x$-chart are $P_i = (0, c_i, 0)$. They lie on the exceptional curve $V(x)$.

*The $y$-chart.* Put $x = y x_1$ and $z = y z_1$. Then $f = y^p (z_1^p - y (1 + x_1^{p+1}))$, by the symmetry $x \leftrightarrow y$. The singular points are $(x_1, y, z_1) = (c, 0, 0)$ with $c^{p+1} = -1$. The point with $x_1 = 0$ is regular, since $1 + 0 \ne 0$. On the overlap of the two charts $x_1 = 1/y_1$, and $(1/c_i)^{p+1} = -1$. Thus the $y$-chart gives the same $p + 1$ points.

*The $z$-chart.* Put $x = z x_1$ and $y = z y_1$. Then $f = z^p - z^{p+1}(x_1^{p+1} + y_1^{p+1}) = z^p (1 - z g(x_1, y_1))$. On the strict transform $V(1 - z g(x_1, y_1))$ we have $z g = 1$, so $g \ne 0$, and the partial derivative $-g$ in $z$ does not vanish. Thus this chart is regular. It does not meet the exceptional curve, since $z = 0$ gives $1 = 0$.

*Normality.* The strict transforms in the $x$-chart and the $y$-chart are surfaces in $\mathbb{A}^3_k$ with finitely many singular points. By Lemma 1.2.6 they are normal. Thus $X'$ is normal, and the normalization step does nothing.

*The local form at $P_i$.* Let $u = \prod_{j \ne i} (y_1 - c_j)$. Then $h = (y_1 - c_i) u$, and $u(c_i) \ne 0$. Let $D(u) \subseteq \mathbb{A}^3_k$ be the open set where $u \ne 0$, and let $\tilde u(b) = u(b + c_i)$. The map $(x, y_1, z_1) \mapsto (a, b, c) = (x u(y_1), y_1 - c_i, z_1)$ is an isomorphism from $D(u)$ onto $D(\tilde u)$, with inverse $(a, b, c) \mapsto (a/\tilde u(b), b + c_i, c)$. It maps $V(z_1^p - x h(y_1)) \cap D(u)$ onto $V(c^p - ab) \cap D(\tilde u)$, and it maps $P_i$ to the origin. Check: $x h(y_1) = x u(y_1) (y_1 - c_i) = ab$. Thus $X'$ near $P_i$ is isomorphic to $X_p$ near the origin.

*The count.* The points $P_i$ are distinct, and the blowup at a finite set of closed points is computed near each point separately. By Proposition 2.3.2, each $P_i$ needs $\lfloor p/2 \rfloor$ more blowups, and the process does all of them at the same time. Thus the process stops after $1 + \lfloor p/2 \rfloor$ blowups. $\square$

The exceptional curve of the first blowup is $V(x, z_1^p)$ in the $x$-chart. As a scheme it is not reduced, and its reduced curve is a projective line. This reflects the tangent cone $z^p = 0$, which is the plane $z = 0$ with multiplicity $p$. The same computation works in characteristic 0 for $z^n = x^{n+1} + y^{n+1}$ with $n \ge 2$. There the Jacobian criterion replaces Lemma 2.3.4, and it gives the same $n + 1$ points. Thus the example does not show a difference between the characteristics. It shows that the process of Lipman treats a purely inseparable equation like any other equation. In higher dimension, the equations $z^p = g$ are a main source of difficulty in characteristic $p$ (Volume 9).

### The normalization step

**Example 2.3.6.** Let $k$ be an algebraically closed field of characteristic $\ne 2$, and let $X = V(z^2 - x^4 - y^4) \subseteq \mathbb{A}^3_k$. Then $X$ is normal with one singular point at the origin. The blowup of $X$ at the origin is not normal. Its normalization $\tilde X$ is regular, so the process stops after one round. The exceptional curve $\tilde E$ of $\tilde X \to X$ is a regular projective curve with $\dim_k H^1(\tilde E, \mathcal{O}_{\tilde E}) = 1$, and the local ring $\mathcal{O}_{X,0}$ does not have a rational singularity.

Lean: `Singularity.quartic_xChart`, `Singularity.quartic_yChart`, `Singularity.quartic_zChart`, `Singularity.quarticNormHom_equation`, `Singularity.quartic_normalization_regular`, `Singularity.card_roots_one_add_X_pow_four`, `Singularity.quartic_charTwo` (the charts and the regularity of $C$, not the integral closure or $H^1$)

*Proof.* *The surface.* Let $g = x^4 + y^4$ and $f = z^2 - g$. The partial derivatives are $-4x^3$, $-4y^3$ and $2z$. Since $2 \ne 0$ in $k$, their only common zero is the origin, and $f \in \mathfrak{m}^2$ there. The polynomial $g$ is the product of the four distinct factors $x - \zeta y$ with $\zeta^4 = -1$. They are distinct, since the derivative $4t^3$ of $t^4 + 1$ has no common root with it. Thus $g$ is not a square in $k(x, y)$, and $f$ is irreducible. By Lemma 1.2.6, $X$ is normal.

*The $x$-chart.* The least degree of a monomial of $f$ is 2. Put $y = x y_1$ and $z = x z_1$. Then $f = x^2 z_1^2 - x^4 - x^4 y_1^4 = x^2 (z_1^2 - x^2 h)$ with $h = 1 + y_1^4$. Check: $x^2 z_1^2 = z^2$ and $x^2 \cdot x^2 y_1^4 = (x y_1)^4 = y^4$. The strict transform is $\operatorname{Spec} B$ with $B = k[x, y_1, z_1]/(z_1^2 - x^2 h)$. The element $x^2 h$ is not a square in $k(x, y_1)$, so $B$ is a domain. Its equation lies in $(x, z_1)^2$. Thus each point of the line $V(x, z_1)$ is singular by Lemma 2.3.1, and $\operatorname{Spec} B$ is not normal by Theorem 1.2.4.

*The normalization of the $x$-chart.* Let $w = z_1/x$ in the field of fractions of $B$. Then $w^2 = z_1^2/x^2 = h$. Let $C = k[x, y_1, w]/(w^2 - h)$. The map $B \to C$ with $x \mapsto x$, $y_1 \mapsto y_1$, $z_1 \mapsto x w$ is well defined, since $z_1^2 - x^2 h \mapsto x^2 (w^2 - h) = 0$. The ring $C$ is regular: the partial derivatives of $w^2 - h$ are $0$, $-4 y_1^3$ and $2w$, and if $y_1 = w = 0$ then $w^2 - h = -1 \ne 0$. The polynomial $h$ has four distinct roots, so it is not a square in $k(y_1)$, and $C$ is a domain. The ring $C$ is generated as a $B$-module by $1$ and $w$, so it is finite over $B$. The kernel of $B \to C$ is a prime $\mathfrak{q}$, and $C$ is integral over $B/\mathfrak{q}$. Thus $\dim B/\mathfrak{q} = \dim C = 2 = \dim B$, and $\mathfrak{q} = 0$, because $B$ is a domain of finite type over $k$. Thus $B \subseteq C \subseteq \operatorname{Frac}(B)$. The ring $C$ is normal, since it is regular (Proposition 2.1.4 of Volume 1 and [Mat, Section 20]), and it is integral over $B$. Thus $C$ is the integral closure of $B$.

*The other charts.* In the $y$-chart, $x = y x_1$ and $z = y z_1$, and $f = y^2 (z_1^2 - y^2 (1 + x_1^4))$. In the same way its normalization is $C' = k[y, x_1, w']/(w'^2 - 1 - x_1^4)$ with $w' = z_1/y = z/y^2$. On the overlap, $x_1 = 1/y_1$ and $w' = z/y^2 = (z/x^2)(x/y)^2 = w/y_1^2$, since $w = z_1/x = z/x^2$. In the $z$-chart, $x = z x_1$ and $y = z y_1$, and $f = z^2 (1 - z^2 (x_1^4 + y_1^4))$. On the strict transform $V(1 - z^2 g(x_1, y_1))$ we have $z \ne 0$ and $g \ne 0$, so the partial derivative $-2 z g$ in $z$ does not vanish. Thus the $z$-chart is regular, and it does not meet the exceptional curve. Thus $\tilde X$ is covered by $\operatorname{Spec} C$, $\operatorname{Spec} C'$ and the $z$-chart, and it is regular.

*The exceptional curve.* In $C$ the ideal of the origin becomes $(x, x y_1, x^2 w) = xC$. Thus $\tilde E \cap \operatorname{Spec} C = \operatorname{Spec} k[y_1, w]/(w^2 - 1 - y_1^4) = U_1$. In the same way $\tilde E \cap \operatorname{Spec} C' = U_2 = \operatorname{Spec} k[x_1, w']/(w'^2 - 1 - x_1^4)$. Both are regular affine curves, and $\tilde E = U_1 \cup U_2$ is a closed subscheme of the separated scheme $\tilde X$, proper over $k$. Since $\tilde E$ is separated, the Čech complex of the affine cover $\{U_1, U_2\}$ computes its cohomology [Har, Theorem III.4.5]. Thus $H^1(\tilde E, \mathcal{O}_{\tilde E}) = \mathcal{O}(U_{12})/(\mathcal{O}(U_1) + \mathcal{O}(U_2))$ with $U_{12} = U_1 \cap U_2$. The ring $\mathcal{O}(U_{12}) = k[y_1, y_1^{-1}, w]/(w^2 - h)$ has the $k$-basis $y_1^i$ and $y_1^i w$ for $i \in \mathbb{Z}$. The ring $\mathcal{O}(U_1)$ is spanned by $y_1^i$ and $y_1^i w$ with $i \ge 0$. The ring $\mathcal{O}(U_2)$ is spanned by $x_1^j = y_1^{-j}$ and $x_1^j w' = y_1^{-j-2} w$ with $j \ge 0$. The only basis element in neither span is $y_1^{-1} w$. Thus $H^1(\tilde E, \mathcal{O}_{\tilde E})$ is the line $k \cdot (w/y_1)$.

*The singularity is not rational.* Let $\pi : \tilde X \to X$ and let $\mathcal{I} = \mathfrak{m}\mathcal{O}_{\tilde X}$ be the ideal of $\tilde E$. The exact sequence $0 \to \mathcal{I} \to \mathcal{O}_{\tilde X} \to \mathcal{O}_{\tilde E} \to 0$ gives the exact sequence $H^1(\tilde X, \mathcal{O}_{\tilde X}) \to H^1(\tilde E, \mathcal{O}_{\tilde E}) \to H^2(\tilde X, \mathcal{I})$. The morphism $\pi$ is a normal modification, and $X$ is affine, so $H^2(\tilde X, \mathcal{I}) = 0$ by Lemma 2.1.2. Thus $H^1(\tilde X, \mathcal{O}_{\tilde X}) \ne 0$, and $R^1 \pi_* \mathcal{O}_{\tilde X} \ne 0$ by [Har, Proposition III.8.5]. This sheaf is supported at the origin, since $\pi$ is an isomorphism elsewhere. By flat base change [Har, Proposition III.9.3], the base change of $\pi$ to $\operatorname{Spec} \mathcal{O}_{X,0}$ is a normal modification with nonzero $R^1$. Thus $\mathcal{O}_{X,0}$ does not have a rational singularity. $\square$

In characteristic 2 the example degenerates: $z^2 - x^4 - y^4 = (z + x^2 + y^2)^2$, so $X$ is not reduced. In characteristic $\ne 2$, the curve $\tilde E$ is the curve $w^2 = 1 + y_1^4$ of genus 1. The example shows that the process of Theorem 2.2.1 can resolve a singularity that is not rational in one round. The reduction to rational singularities in Step 2 of Section 2.2 is a step of the proof, and not a step of the process.

### The cohomology of the resolution of $xy = z^2$

We compare Example 2.3.6 with the simplest singularity of Proposition 2.3.2. Here the exceptional curve is a projective line, and $H^1$ vanishes.

**Example 2.3.7.** Let $k$ be a field of any characteristic, let $X = V(xy - z^2) \subseteq \mathbb{A}^3_k$, and let $\pi : \tilde{X} \to X$ be the blowup at the origin. Let $E = \pi^{-1}(0)$ with the ideal $\mathfrak{m}\mathcal{O}_{\tilde{X}}$.

1. The scheme $\tilde{X}$ is regular, and it is covered by two open sets $U \cong \operatorname{Spec} k[x, z_1]$ and $V \cong \operatorname{Spec} k[y, z_2]$, glued along $z_1 \ne 0$ by $z_2 = z_1^{-1}$ and $y = xz_1^2$.
2. The divisor $E$ is isomorphic to $\mathbb{P}^1_k$, and its conormal sheaf is $\mathcal{O}_{\mathbb{P}^1}(2)$. Thus $E \cdot E = -2$, with $E \cdot E$ defined as in Definition 1.1.8.
3. $H^0(\tilde{X}, \mathcal{O}_{\tilde{X}}) = k[x, y, z]/(xy - z^2)$ and $H^1(\tilde{X}, \mathcal{O}_{\tilde{X}}) = 0$.

Lean: `Singularity.map_chartU_span_X`, `Singularity.map_chartV_span_X`, `Singularity.quadricConeGlue_exceptional_generator` (parts 1 and 2 for the rings of the charts; the scheme, the sheaf $\mathcal{O}(2)$ and part 3 are not in Lean)

*Proof.* 1. By Proposition 2.3.2 with $n = 2$, the $x$-chart of $\tilde{X}$ is $V(y_1 - z_1^2) \subseteq \operatorname{Spec} k[x, y_1, z_1]$, with $y = xy_1$ and $z = xz_1$. It is the graph of $y_1 = z_1^2$, so it is $U = \operatorname{Spec} k[x, z_1]$, with $y = xz_1^2$. In the same way the $y$-chart is $V = \operatorname{Spec} k[y, z_2]$ with $z = yz_2$ and $x = yz_2^2$. The $z$-chart is $V(x_1y_1 - 1)$ with $x = zx_1$. On it $x_1 = x/z$ is a unit, so $x$ generates $\mathfrak{m}\mathcal{O}_{\tilde{X}}$ there. By the remark after the proof of Theorem 1.1.2, the $z$-chart lies in the $x$-chart. Thus $U$ and $V$ cover $\tilde{X}$. By $(\ast)$ in Section 1.1, $U \cap V$ is the open set of $U$ where $y/x = z_1^2$ is a unit, that is, $\operatorname{Spec} k[x, z_1, z_1^{-1}]$. On it $z_2 = z/y = xz_1/(xz_1^2) = z_1^{-1}$. Both charts are planes, so $\tilde{X}$ is regular.

2. On $U$ the ideal $\mathfrak{m}\mathcal{O}_{\tilde{X}}$ is $(x, xz_1^2, xz_1) = (x)$, and on $V$ it is $(y)$. Thus $E \cap U = \operatorname{Spec} k[z_1]$ and $E \cap V = \operatorname{Spec} k[z_2]$, glued by $z_2 = z_1^{-1}$. This is $\mathbb{P}^1_k$ with $z_1 = X_1/X_0$. The conormal sheaf is generated by the class $e_0$ of $x$ on $E \cap U$ and by the class $e_1$ of $y$ on $E \cap V$. On the overlap $y = z_1^2x$, so $e_1 = (X_1/X_0)^2 e_0$. The sheaf $\mathcal{O}(2)$ is generated by $X_0^2$ and $X_1^2$, and $X_1^2 = (X_1/X_0)^2X_0^2$. Thus $e_0 \mapsto X_0^2$ and $e_1 \mapsto X_1^2$ give an isomorphism with $\mathcal{O}(2)$, as in Step 4 of the proof of Theorem 1.1.7. The dual $\mathcal{O}_{\tilde{X}}(E)|_E$ is $\mathcal{O}(-2)$.

3. The scheme $\tilde{X}$ is separated, since $\pi$ is projective. So the Čech complex of the cover $\{U, V\}$ computes the cohomology of $\mathcal{O}_{\tilde{X}}$ [Har, Theorem III.4.5]. Inside $\mathcal{O}(U \cap V) = k[x, z_1, z_1^{-1}]$, with its basis of monomials $x^az_1^b$ for $a \ge 0$ and $b \in \mathbb{Z}$, the ring $\mathcal{O}(U)$ is spanned by the monomials with $b \ge 0$. The ring $\mathcal{O}(V) = k[xz_1^2, z_1^{-1}]$ is spanned by the monomials $x^az_1^{2a - c}$ with $c \ge 0$, that is, by the monomials with $b \le 2a$. Each monomial has $b \ge 0$ or $b < 0 \le 2a$, so $\mathcal{O}(U) + \mathcal{O}(V) = \mathcal{O}(U \cap V)$, and $H^1 = 0$. The ring $H^0 = \mathcal{O}(U) \cap \mathcal{O}(V)$ is spanned by the monomials with $0 \le b \le 2a$. Such a monomial is $x^iy^jz^l = x^{i+j+l}z_1^{2j+l}$ with $j = \lfloor b/2 \rfloor$, $l = b - 2j$ and $i = a - j - l \ge 0$. Thus $H^0$ is the image of $k[x, y, z]$, which is $k[x, y, z]/(xy - z^2)$. $\square$

Part 3 checks Lemma 2.1.2, part 1, in this case. In the language of Remark 2.1.4, the resolution $\tilde{X}$ has $H^1(\tilde{X}, \mathcal{O}_{\tilde{X}}) = 0$, while the resolution of Example 2.3.6 has $H^1 \ne 0$. Definition 2.1.3 asks for the vanishing on every normal modification, and Example 2.3.7 does not prove it. If we admit the fact of Remark 2.1.4, the example shows that the origin of $xy = z^2$ is a rational singularity. The curve $E$ is a projective line with $E \cdot E = -2$. In Example 2.3.6 the exceptional curve has genus 1, and this is the source of the nonzero $H^1$.

### Intersection numbers with a projective line

To compute the dual graphs of the resolutions below we need intersection numbers on a regular surface that need not be projective. We only need them for a curve isomorphic to a projective line. This extends Definition 1.1.8.

Let $Y$ be a regular integral separated Noetherian scheme. Each local ring of $Y$ is factorial [Mat, Theorem 20.3]. Thus each integral closed subscheme $\Gamma$ of codimension 1 is an effective Cartier divisor, and the Weil divisors and the Cartier divisors of $Y$ are the same [Har, Proposition II.6.11]. We write $\Gamma$ also for this Cartier divisor. For a nonzero rational function $g$ on $Y$, let $\operatorname{div}(g) = \sum_\Gamma v_\Gamma(g) \Gamma$, where $v_\Gamma$ is the valuation of the discrete valuation ring $\mathcal{O}_{Y,\Gamma}$ at the generic point of $\Gamma$.

**Definition 2.3.8.** Let $Y$ be as above, let $\kappa$ be a field, and let $C \subseteq Y$ be an integral closed subscheme with $C \cong \mathbb{P}^1_\kappa$. For a Cartier divisor $D$ on an open set $V \supseteq C$, the *intersection number* of $D$ and $C$ is $D \cdot C = \deg \mathcal{O}_V(D)|_C$.

Lean: none yet

For $D = E$ in the situation of Theorem 1.1.7, this is Definition 1.1.8. The number only depends on $D$ near $C$.

**Lemma 2.3.9.** Let $Y$ and $C \cong \mathbb{P}^1_\kappa$ be as in Definition 2.3.8, and let $V \supseteq C$ be open.

1. For Cartier divisors $D, D'$ on $V$, we have $(D + D') \cdot C = D \cdot C + D' \cdot C$.
2. Let $D$ be an effective Cartier divisor on $V$ with $C \not\subseteq D$. Let $D \cap C$ be the closed subscheme of $C$ whose ideal is generated by the local equations of $D$. Then $D \cdot C = \dim_\kappa H^0(D \cap C, \mathcal{O}_{D \cap C})$. In particular, if $D \cap C$ consists of $r$ points with residue field $\kappa$, and $D$ and $C$ have local equations that form a regular system of parameters at each of them, then $D \cdot C = r$.
3. Let $g$ be a nonzero element of $\Gamma(V, \mathcal{O}_Y)$. Then $\operatorname{div}(g) \cdot C = 0$.

Lean: none yet

*Proof.* 1. We have $\mathcal{O}(D + D') \cong \mathcal{O}(D) \otimes \mathcal{O}(D')$, the restriction to $C$ commutes with the tensor product, and $\mathcal{O}(a) \otimes \mathcal{O}(b) \cong \mathcal{O}(a + b)$ on $\mathbb{P}^1_\kappa$.

2. The sheaf $\mathcal{O}(D) = \mathcal{I}_D^{-1}$ contains $\mathcal{O}_V$, so it has the section $1$. Near a point with local equation $a$ of $D$, this section is $a \cdot a^{-1}$, and its restriction to $C$ vanishes exactly on the subscheme defined by $a$. Thus the restriction $\sigma$ of $1$ to $C$ is a section of $\mathcal{L} = \mathcal{O}(D)|_C$ with zero scheme $D \cap C$. Since $C$ is integral and $C \not\subseteq D$, the section $\sigma$ is not 0. Let $\mathcal{L} \cong \mathcal{O}(n)$. Then $\sigma$ is a nonzero form $G$ of degree $n$ in the homogeneous coordinates $X_0, X_1$, and $n \ge 0$. Write $G = X_0^e G_1$ with $X_0 \nmid G_1$. The zero scheme of $G$ is $\operatorname{Spec} \kappa[T]/(G(1, T))$ on $X_0 \ne 0$, with $T = X_1/X_0$, and $G(1, T) = G_1(1, T)$ has degree $n - e$. At the point $X_0 = 0$ the zero scheme is $\operatorname{Spec} \kappa[S]_{(S)}/(S^e)$, with $S = X_0/X_1$. Thus the total dimension is $(n - e) + e = n$. For the last claim, a point where the two local equations form a regular system of parameters contributes $\dim_\kappa \kappa = 1$.

3. Multiplication by $g$ is an isomorphism $\mathcal{O}_V(\operatorname{div}(g)) \to \mathcal{O}_V$, so the restriction to $C$ is $\mathcal{O}_C$, of degree 0. $\square$

Part 3 is the tool for all the self-intersections below. Let $g$ be a regular function near the exceptional curves $C_1, \dots, C_r$ of a resolution, and write $\operatorname{div}(g) = \sum_j a_j C_j + G$, where $G$ has no exceptional component. Then for each $i$,

$$a_i \, C_i \cdot C_i + \sum_{j \ne i} a_j \, C_j \cdot C_i + G \cdot C_i = 0.$$

If we know the orders $a_j$ and the points where the curves meet, this gives $C_i \cdot C_i$. We also use the next fact twice. Let $\Gamma$ be a regular curve on a surface $Y$, and let $Y' \to Y$ be the blowup of $Y$ at a finite set of closed points. Then the strict transform of $\Gamma$ is isomorphic to $\Gamma$. Indeed, by Proposition 1.1.5 it is the blowup of $\Gamma$ along a closed subscheme of dimension 0, and the ideal of such a subscheme of a regular curve is invertible, since the local rings are discrete valuation rings. The blowup along an effective Cartier divisor is an isomorphism (Corollary 1.1.12 and its proof).

### The chain of the surfaces $xy = z^m$

We now describe the whole resolution of Proposition 2.3.2. The result is the chain $A_{m-1}$ of projective lines, in every characteristic.

**Proposition 2.3.10.** Let $k$ be a field of any characteristic, let $m \ge 1$, let $X_m = V(xy - z^m) \subseteq \mathbb{A}^3_k$, and let $\tilde X \to X_m$ be the end result of the process of Theorem 2.2.1 (Proposition 2.3.2).

1. The scheme $\tilde X$ is covered by $m$ open sets $U_0, \dots, U_{m-1}$ with $U_i = \operatorname{Spec} k[s_i, t_i]$, and on $U_i$ the morphism to $X_m$ is

$$x = s_i^{m-i} t_i^{m-1-i}, \qquad y = s_i^i t_i^{i+1}, \qquad z = s_i t_i.$$

As rational functions, $s_i = z^{i+1}/y$ and $t_i = y/z^i$. For $1 \le i \le m - 1$, the open sets $\{t_i \ne 0\} \subseteq U_i$ and $\{s_{i-1} \ne 0\} \subseteq U_{i-1}$ are glued by $s_{i-1} = t_i^{-1}$ and $t_{i-1} = s_i t_i^2$.
2. The fibre over the origin is the union of $m - 1$ curves $E_1, \dots, E_{m-1}$. The curve $E_i$ is $\{s_i = 0\}$ in $U_i$ and $\{t_{i-1} = 0\}$ in $U_{i-1}$, and $E_i \cong \mathbb{P}^1_k$.
3. We have $E_i \cdot E_i = -2$. The curves $E_i$ and $E_{i+1}$ meet in one point, the origin of $U_i$, and there $s_i, t_i$ are local equations of them. The curves $E_i$ and $E_j$ are disjoint for $|i - j| \ge 2$.
4. The strict transform of the line $\{x = z = 0\}$ is $\{s_0 = 0\} \subseteq U_0$, and it meets $E_1$ transversally at the origin of $U_0$. The strict transform of the line $\{y = z = 0\}$ is $\{t_{m-1} = 0\} \subseteq U_{m-1}$, and it meets $E_{m-1}$ transversally at the origin of $U_{m-1}$.
5. The orders of the coordinates along $E_i$ are $v_{E_i}(x) = m - i$, $v_{E_i}(y) = i$ and $v_{E_i}(z) = 1$.

Parts 2 to 5 are empty for $m = 1$.

Lean: `Singularity.aChain_chart_mul`, `Singularity.aChain_glue_x`, `Singularity.aChainChart_equation` (part 1, the chart equations and the gluing)

*Proof.* 1. We use induction on $m$ with the recursion of Proposition 2.3.2. For $m = 1$, the surface $X_1$ is regular and $\tilde X = X_1 \cong \operatorname{Spec} k[x, y]$, with $z = xy$. This is $U_0$ with $s_0 = x$ and $t_0 = y$. For $m = 2$, Example 2.3.7 gives the two charts. The chart $\operatorname{Spec} k[y, z_2]$ with $x = y z_2^2$ and $z = y z_2$ is $U_0$ with $s_0 = z_2$ and $t_0 = y$. The chart $\operatorname{Spec} k[x, z_1]$ with $y = x z_1^2$ and $z = x z_1$ is $U_1$ with $s_1 = x$ and $t_1 = z_1$. The gluing $z_2 = z_1^{-1}$, $y = x z_1^2$ of Example 2.3.7 is the gluing of part 1.

Let $m \ge 3$. By the proof of Proposition 2.3.2, the first blowup has three charts. The $y$-chart is $\operatorname{Spec} k[y, z_1]$ with $x = y^{m-1} z_1^m$ and $z = y z_1$. This is $U_0$ with $s_0 = z_1$ and $t_0 = y$. The $x$-chart is $\operatorname{Spec} k[x, z_1]$ with $y = x^{m-1} z_1^m$ and $z = x z_1$. This is $U_{m-1}$ with $s_{m-1} = x$ and $t_{m-1} = z_1$. These charts are regular, and the later steps of the process do not change them (Lemma 2.2.5). The $z$-chart is $X_{m-2}$ in the coordinates $x_1, y_1, z$, with $x = z x_1$ and $y = z y_1$. By induction, the process for $X_{m-2}$ ends with charts $U'_0, \dots, U'_{m-3}$, where $x_1 = s^{m-2-j} t^{m-3-j}$, $y_1 = s^j t^{j+1}$ and $z = st$ on $U'_j$. Then

$$x = z x_1 = s^{m-1-j} t^{m-2-j}, \qquad y = z y_1 = s^{j+1} t^{j+2},$$

and these are the formulas of $U_{j+1}$. Thus $\tilde X$ is covered by $U_0, \dots, U_{m-1}$, by Lemma 2.2.5 applied to the open cover by the three charts. From $z = s_i t_i$ and $y = s_i^i t_i^{i+1}$ we get $t_i = y/z^i$ and $s_i = z/t_i = z^{i+1}/y$. Then $s_{i-1} = z^i/y = t_i^{-1}$ and $s_i t_i^2 = (z^{i+1}/y)(y^2/z^{2i}) = y/z^{i-1} = t_{i-1}$. The open sets in part 1 have the same ring $k[s_i, t_i, t_i^{-1}] = k[s_{i-1}, s_{i-1}^{-1}, t_{i-1}]$ in the function field. They are the overlaps of the charts of the blowups in the recursion, and the gluing is given by these relations.

2. On $U_i$ the fibre over the origin is $V(x, y, z) = V(s_i t_i)$ for $1 \le i \le m - 2$. For $i = 0$ it is $V(t_0)$, because $y = t_0$. For $i = m - 1$ it is $V(s_{m-1})$, because $x = s_{m-1}$. On the overlap of $U_{i-1}$ and $U_i$ we have $t_{i-1} = s_i t_i^2$ with $t_i$ a unit, so $\{t_{i-1} = 0\}$ and $\{s_i = 0\}$ agree there. Thus the axes glue to $m - 1$ curves $E_1, \dots, E_{m-1}$. The curve $E_i$ is glued from $\operatorname{Spec} k[t_i]$ and $\operatorname{Spec} k[s_{i-1}]$ along $s_{i-1} = t_i^{-1}$, so $E_i \cong \mathbb{P}^1_k$.

3. The conormal sheaf of $E_i$ is generated by the class of $s_i$ on $U_i$ and by the class of $t_{i-1}$ on $U_{i-1}$. On the overlap $t_{i-1} = t_i^2 s_i$. As in the proof of Example 2.3.7, part 2, the conormal sheaf is $\mathcal{O}(2)$, so $E_i \cdot E_i = -2$. In $U_i$ the curve $E_{i+1}$ is $\{t_i = 0\}$, and it meets $E_i = \{s_i = 0\}$ only at the origin, where $s_i, t_i$ is a regular system of parameters. In the chart $U_j$ only $E_j$ and $E_{j+1}$ appear, so $E_i \cap E_j = \emptyset$ for $|i - j| \ge 2$.

4. On $U_0$ we have $x = s_0^m t_0^{m-1}$, $y = t_0$ and $z = s_0 t_0$. Off the fibre, $t_0 \ne 0$, and $x = z = 0$ means $s_0 = 0$. Thus the strict transform is $\{s_0 = 0\}$, and it meets $E_1 = \{t_0 = 0\}$ at the origin of $U_0$, transversally. The other line is the same with $U_{m-1}$, by the symmetry $x \leftrightarrow y$.

5. At the generic point of $E_i$ in $U_i$, the element $s_i$ is a uniformizer and $t_i$ is a unit. The formulas of part 1 give the orders. $\square$

As a check of part 3, apply Lemma 2.3.9, part 3, to $g = z$. Its divisor is $\sum_{i} E_i + L_x + L_y$, where $L_x$ and $L_y$ are the strict transforms of the two lines of part 4. For $2 \le i \le m - 2$ we get $E_i \cdot E_i + 2 = 0$. For $i = 1$ and $m \ge 3$ we get $E_1 \cdot E_1 + E_2 \cdot E_1 + L_x \cdot E_1 = E_1 \cdot E_1 + 2 = 0$. The case $i = m - 1$ is the same, and for $m = 2$ we get $E_1 \cdot E_1 + L_x \cdot E_1 + L_y \cdot E_1 = 0$. This agrees with part 3. The dual graph is the chain

$$E_1 \;\; E_2 \;\; \cdots \;\; E_{m-1},$$

with an edge between $E_i$ and $E_{i+1}$ and the weight $-2$ at each vertex. This is the Dynkin diagram $A_{m-1}$. Nothing in the proof uses the characteristic, so the dual graph is the same in every characteristic. In characteristic $p$ with $p \mid m$, the projection to the $(x, y)$-plane is inseparable, as in Remark 2.3.3, but the resolution does not change.

### The singularity $D_4$

The usual equation $z^2 + x^2 y + y^3$ of $D_4$ has a bad reduction in characteristic 2. The equation $z^2 + xy(x + y)$ gives the dual graph $D_4$ in every characteristic.

**Example 2.3.11.** Let $k$ be an algebraically closed field of any characteristic, let $F = z^2 + xy(x + y)$, and let $X = V(F) \subseteq \mathbb{A}^3_k$.

1. The scheme $X$ is normal, and its only singular point is the origin.
2. The blowup $X'$ of $X$ at the origin is normal. It has exactly three singular points $P_1, P_2, P_3$, all on the exceptional curve $E_0$, and $E_0 \cong \mathbb{P}^1_k$ with its reduced structure. Near each $P_j$, the surface $X'$ is isomorphic to $X_2 = V(ab - c^2)$ near the origin.
3. The process stops after two blowups. The exceptional curves of the resolution $\tilde X \to X$ are $E_0$ and the curves $E_1, E_2, E_3$ over $P_1, P_2, P_3$. All four are projective lines with self-intersection $-2$. The curve $E_0$ meets each $E_j$ transversally in one point, and the $E_j$ with $j \ge 1$ are disjoint.

Lean: `Singularity.dFour_singular_origin`, `Singularity.dFour_xChart`, `Singularity.dFour_yChart`, `Singularity.dFour_zChart`, `Singularity.dFour_xChart_singular_iff`, `Singularity.dFour_order_z` (the charts and the singular points, not normality or part 3)

*Proof.* 1. The partial derivatives are $F_x = y(2x + y)$, $F_y = x(x + 2y)$ and $F_z = 2z$. In characteristic 2 they are $y^2$, $x^2$ and $0$. A common zero on $X$ has $x = y = 0$, and then $z^2 = 0$. In characteristic $\ne 2$, a common zero has $z = 0$, so $xy(x + y) = 0$. If $x = 0$, then $F_x = y^2$ gives $y = 0$. If $y = 0$, then $F_y = x^2$ gives $x = 0$. If $y = -x$, then $F_x = -x^2$ gives $x = 0$. In each case the point is the origin, and $F \in \mathfrak{m}^2$ there. By Lemma 1.2.6, $X$ is normal.

2. The least degree of a monomial of $F$ is 2. In the $x$-chart, $y = x y_1$ and $z = x z_1$, and $F = x^2 (z_1^2 + x y_1 (1 + y_1))$. Check: $x^2 \cdot x y_1 (1 + y_1) = x \cdot x y_1 (x + x y_1) = xy(x + y)$. Let $G = z_1^2 + x y_1 (1 + y_1)$. Then $G_x = y_1(1 + y_1)$, $G_{y_1} = x(1 + 2 y_1)$ and $G_{z_1} = 2 z_1$. A singular point has $y_1(1 + y_1) = 0$ and $G = 0$, so $z_1^2 = 0$. If $y_1 = 0$, then $G_{y_1} = x = 0$. If $y_1 = -1$, then $G_{y_1} = -x = 0$. Conversely the points $(0, 0, 0)$ and $(0, -1, 0)$ are singular, since $G$ lies in the square of their maximal ideals. In the $y$-chart, $x = y x_1$ and $z = y z_1$, and $F = y^2 (z_1^2 + y x_1 (1 + x_1))$, by the symmetry $x \leftrightarrow y$. Its singular points are $x_1 = 0$ and $x_1 = -1$ on $V(y, z_1)$. The point $x_1 = -1$ is the point $y_1 = -1$ of the $x$-chart, and the point $x_1 = 0$ is new. In the $z$-chart, $F = z^2 (1 + z x_1 y_1 (x_1 + y_1))$, and the strict transform does not meet $V(z)$. Thus $X'$ has the three singular points $P_1 = \{y_1 = 0\}$, $P_2 = \{y_1 = -1\}$ and $P_3 = \{x_1 = 0\}$. They are distinct in every characteristic, since $-1 \ne 0$. By Lemma 1.2.6 the charts are normal.

The exceptional curve is $V(x, z_1^2)$ in the $x$-chart and $V(y, z_1^2)$ in the $y$-chart. Its reduced curve $E_0$ is $V(x, z_1) \cong \operatorname{Spec} k[y_1]$ and $V(y, z_1) \cong \operatorname{Spec} k[x_1]$, glued by $x_1 = y_1^{-1}$. Thus $E_0 \cong \mathbb{P}^1_k$.

Near $P_1$, let $a = x(1 + y_1)$, $b = y_1$ and $c = z_1$. On the open set $D(1 + y_1)$ the map $(x, y_1, z_1) \mapsto (a, b, c)$ is an isomorphism onto $D(1 + b)$, with inverse $x = a/(1 + b)$. It maps $V(G)$ onto $V(c^2 + ab)$, and $c^2 + ab = 0$ is $X_2$ after the change $a \mapsto -a$. The points $P_2$ and $P_3$ are the same, with $a = x y_1$, $b = 1 + y_1$, and with the $y$-chart.

3. By Proposition 2.3.2 for $n = 2$ and Lemma 2.2.5, one blowup at each $P_j$ makes the surface regular. Thus the process stops after two blowups. By Proposition 2.3.10 with $m = 2$, the curve $E_j$ over $P_j$ is a projective line with $E_j \cdot E_j = -2$. The $E_j$ lie over distinct points, so they are disjoint. Near $P_1$, the curve $E_0 = V(x, z_1)$ is $V(a, c)$, which is a line $\{x = z = 0\}$ of $X_2$ in the coordinates of Proposition 2.3.10. By part 4 of that proposition, its strict transform meets $E_1$ transversally in one point. The same holds at $P_2$ and $P_3$. The strict transform of $E_0$ is isomorphic to $E_0$, by the remark after Lemma 2.3.9.

It remains to compute $E_0 \cdot E_0$. We use $g = z$. On $X$ the divisor of $z$ is the sum of the three lines $L_1 = \{z = y = 0\}$, $L_2 = \{z = x + y = 0\}$ and $L_3 = \{z = x = 0\}$, since $F = z^2 + xy(x + y)$. At the generic point of $E_0$ in the $x$-chart, $y_1(1 + y_1)$ is a unit, so $x = -z_1^2/(y_1(1 + y_1))$, and $z_1$ is a uniformizer. Thus $v_{E_0}(z) = v_{E_0}(x z_1) = 2 + 1 = 3$. Near $P_1$ we have $z = x z_1 = a c/(1 + b)$, and $v_{E_1}(a) = v_{E_1}(c) = 1$ by Proposition 2.3.10, part 5, for $m = 2$. Thus $v_{E_j}(z) = 2$ for $j = 1, 2, 3$. The strict transform of $L_1$ is $V(b, c)$ near $P_1$. It is the other line of $X_2$, so it meets $E_1$ and not $E_0$. In the same way $L_2$ and $L_3$ meet $E_2$ and $E_3$ and not $E_0$. Thus

$$\operatorname{div}(z) = 3 E_0 + 2 (E_1 + E_2 + E_3) + L_1 + L_2 + L_3,$$

and Lemma 2.3.9 gives $3 E_0 \cdot E_0 + 2 \cdot 3 = 0$, so $E_0 \cdot E_0 = -2$. $\square$

As a check, $\operatorname{div}(z) \cdot E_1 = 3 + 2(-2) + 1 = 0$. The dual graph has $E_0$ in the center and $E_1, E_2, E_3$ around it, with weight $-2$ at each vertex. This is the Dynkin diagram $D_4$, in every characteristic.

The other equation behaves differently. Let $k$ have characteristic 2 and let $F' = z^2 + x^2 y + y^3$. Then $F' = z^2 + y(x + y)^2$, because $(x + y)^2 = x^2 + y^2$. With $w = z$ and $G = y(x + y)^2$ as in Lemma 2.3.4, we get $G_x = 0$ and $G_y = (x + y)^2$. Thus $V(F')$ is singular along the whole line $x = y$, $z = 0$, and it is not normal. In the coordinates $u = x + y$ it is $z^2 = y u^2$, which is the Whitney umbrella of Example 1.2.7. The process starts with the normalization, which is the plane, and it stops there (Example 2.2.4). So in characteristic 2 the two equations are not equivalent, and of the two only $z^2 + xy(x + y)$ gives $D_4$. In characteristic 2 there is one more form of $D_4$, the equation $z^2 + x^2 y + x y^2 + xyz$, which is not equivalent to $z^2 + xy(x + y)$. In the classification of Artin ("Coverings of the rational double points in characteristic $p$", 1977) the two forms are $D_4^0$ and $D_4^1$. That paper has no key in the map. We do not use it, and we do not treat $D_4^1$.

### The singularity $E_6$

**Example 2.3.12.** Let $k$ be an algebraically closed field of characteristic $\ne 2$, let $F = z^2 + x^3 + y^4$, and let $X = V(F) \subseteq \mathbb{A}^3_k$.

1. The scheme $X$ is normal with one singular point at the origin. In characteristic 3 this follows from Lemma 2.3.4.
2. The blowup $X'$ of $X$ at the origin is normal, with one singular point $Q$ on the exceptional curve $E_0 \cong \mathbb{P}^1_k$. Near $Q$ the surface $X'$ is isomorphic to $X_6 = V(ab - c^6)$ near the origin, and the curve $E_0$ corresponds to the curve $a = b = c^3$.
3. The process stops after four blowups. The exceptional curves are $E_0$ and the chain $E_1, \dots, E_5$ of Proposition 2.3.10 for $m = 6$. All are projective lines with self-intersection $-2$, and $E_0$ meets $E_3$ transversally in one point and no other $E_i$. The dual graph is $E_6$.

Lean: `Singularity.eSix_xChart`, `Singularity.eSix_yChart`, `Singularity.eSix_zChart`, `Singularity.eSix_xChart_regular`, `Singularity.eSix_yChart_exceptional`, `Singularity.eSix_complete_square`, `Singularity.eSix_exceptional_curve` (the charts and the change of coordinates, not normality or part 3)

*Proof.* 1. The partial derivatives are $3x^2$, $4y^3$ and $2z$. If the characteristic is not 3, a common zero has $x = y = z = 0$. In characteristic 3, write $x^3 = -z^2 - y^4$ and apply Lemma 2.3.4 with $w = x$ and $G = -z^2 - y^4$. Then $G_z = -2z$ and $G_y = -4y^3$, so a singular point has $y = z = 0$, and then $x^3 = 0$. In both cases the origin is the only singular point, and $X$ is normal by Lemma 1.2.6.

2. The least degree of a monomial of $F$ is 2. In the $x$-chart, $F = x^2 (z_1^2 + x + x^2 y_1^4)$. The derivative of $z_1^2 + x + x^2 y_1^4$ in $z_1$ is $2 z_1$ and in $x$ is $1 + 2x y_1^4$. If both vanish, then $z_1 = 0$ and $x y_1^4 = -1/2$, and the equation gives $0 = x + x^2 y_1^4 = x/2$, so $x = 0$, which contradicts $x y_1^4 = -1/2$. Thus the $x$-chart is regular. In the $z$-chart, $F = z^2 (1 + z x_1^3 + z^2 y_1^4)$, and the strict transform does not meet $V(z)$. In the $y$-chart, $x = y x_1$ and $z = y z_1$, and

$$F = y^2 (z_1^2 + y^2 + y x_1^3).$$

Check: $y^2 \cdot y x_1^3 = (y x_1)^3$ and $y^2 \cdot y^2 = y^4$. Let $H = z_1^2 + y^2 + y x_1^3$. On $V(y)$ the equation gives $z_1 = 0$, and $H_y = 2y + x_1^3 = x_1^3$ there. Thus the only singular point on the exceptional curve is $Q = (0, 0, 0)$. Away from $V(y)$ the chart is isomorphic to an open set of $X \setminus \{0\}$, which is regular. By Lemma 1.2.6 all charts are normal. The exceptional curve is $V(y, z_1^2)$ in the $y$-chart and $V(x, z_1^2)$ in the $x$-chart, so its reduced curve $E_0$ is a projective line with the coordinates $x_1$ and $y_1 = x_1^{-1}$.

Now complete the square. Let $Y = y + x_1^3/2$. Then $y^2 + y x_1^3 = Y^2 - x_1^6/4$. Let $\iota \in k$ with $\iota^2 = -1$ and $\zeta \in k$ with $\zeta^3 = 2$, so that $\zeta^6 = 4$. Let

$$a = Y + \iota z_1, \qquad b = Y - \iota z_1, \qquad c = x_1/\zeta.$$

Then $ab = Y^2 + z_1^2$ and $c^6 = x_1^6/4$, so $H = ab - c^6$. The map $(x_1, y, z_1) \mapsto (a, b, c)$ is an automorphism of $\mathbb{A}^3_k$, with inverse $x_1 = \zeta c$, $z_1 = (a - b)/(2\iota)$ and $y = (a + b)/2 - \zeta^3 c^3/2$. It maps $Q$ to the origin. On $E_0$ we have $y = z_1 = 0$, so $a = b = x_1^3/2 = \zeta^3 c^3/2 = c^3$.

3. By Lemma 2.2.5 and Proposition 2.3.2 for $n = 6$, the process needs three more blowups at $Q$, so four in total. By Proposition 2.3.10 for $m = 6$, the curves over $Q$ form the chain $E_1, \dots, E_5$ of projective lines with self-intersection $-2$. On the chart $U_3$ of Proposition 2.3.10 we have $a = s^3 t^2$, $b = s^3 t^4$ and $c^3 = s^3 t^3$, with $s = s_3$ and $t = t_3$. Off the fibre, $s t \ne 0$, and $a = b = c^3$ gives $t^2 = t^3 = t^4$, so $t = 1$. Thus the strict transform of $E_0$ contains the curve $\{t_3 = 1\}$ of $U_3$. By the remark after Lemma 2.3.9 it is isomorphic to $E_0$, so it has exactly one point over $Q$. That point is $(s_3, t_3) = (0, 1)$. It lies on $E_3 = \{s_3 = 0\}$ and not on $E_4 = \{t_3 = 0\}$. At this point $s_3$ and $t_3 - 1$ are local equations of $E_3$ and $E_0$, so they meet transversally.

For $E_0 \cdot E_0$ we use $g = x = y x_1$. At the generic point of $E_0$ in the $y$-chart, $y + x_1^3$ is a unit, so $y = -z_1^2/(y + x_1^3)$, and $v_{E_0}(x) = 2$. Along $E_i$ with $1 \le i \le 5$, we have $x_1 = \zeta c$ with $v_{E_i}(c) = 1$, and $y = (a + b - 2c^3)/2$. In $U_i$ with $m = 6$ this is

$$y = \tfrac12 \left( s^{6-i} t^{5-i} + s^i t^{i+1} - 2 s^3 t^3 \right).$$

Its order in $s$ is $\min(6 - i, i, 3)$ for $i \ne 3$, and for $i = 3$ it is $s^3 t^2 (1 - t)^2/2$, of order 3. Thus $v_{E_i}(y) = 1, 2, 3, 2, 1$ and $v_{E_i}(x) = 2, 3, 4, 3, 2$ for $i = 1, \dots, 5$. The other components of $\operatorname{div}(x)$ are the strict transforms $M_\pm$ of the curves $\{x = 0, z = \pm \iota y^2\}$ of $X$. In the coordinates $a, b, c$ they are the lines $\{a = c = 0\}$ and $\{b = c = 0\}$. By Proposition 2.3.10, part 4, the first one meets $E_1$, the second one meets $E_5$, and neither meets $E_0$. Thus Lemma 2.3.9 gives $\operatorname{div}(x) \cdot E_0 = 2 E_0 \cdot E_0 + 4 = 0$, and $E_0 \cdot E_0 = -2$. $\square$

As a check, $\operatorname{div}(x) \cdot E_3 = 4(-2) + 3 + 3 + 2 = 0$ and $\operatorname{div}(x) \cdot E_1 = 2(-2) + 3 + 1 = 0$. The dual graph is the chain $E_1, \dots, E_5$ with the vertex $E_0$ attached to the middle vertex $E_3$, and the weight $-2$ everywhere. This is the Dynkin diagram $E_6$.

The computation fails in characteristic 2, and the singularity is of another kind. There $F = (z + y^2)^2 + x^3$. With $w = z + y^2$ the surface is $V(w^2 + x^3) \times \mathbb{A}^1_y$, the product of a cusp and a line. It is singular along the curve $x = 0$, $z = y^2$, and it is not normal. Its normalization is the plane with the coordinates $t$ and $y$, where $x = t^2$ and $w = t^3$, and the process stops there. In characteristic 3 the proof above works without change, although the projection to the $(y, z)$-plane is purely inseparable. But in characteristic 3 the equation $z^2 + x^3 + y^4$ is only one of two forms of $E_6$. Artin's list (1977) has $E_6^0 = z^2 + x^3 + y^4$ and $E_6^1 = z^2 + x^3 + y^4 + x^2 y^2$, and these are not equivalent. Example 2.3.12 treats $E_6^0$ only. In characteristic 2 the list also has two forms, $z^2 + x^3 + y^2 z$ and $z^2 + x^3 + y^2 z + xyz$. We cite these facts and we do not use them.

### The equation $z^2 + x^3 + y^5$ in small characteristic

The equation $z^2 + x^3 + y^5$ is the equation of $E_8$ in characteristic 0. In characteristics 2, 3 and 5 it is purely inseparable over a plane, in three different ways, and Lemma 2.3.4 finds its singular points.

**Example 2.3.13.** Let $k$ be an algebraically closed field of characteristic $p \in \{2, 3, 5\}$, let $F = z^2 + x^3 + y^5$, and let $X = V(F)$.

1. The scheme $X$ is normal with one singular point at the origin.
2. The blowup of $X$ at the origin is normal. It has one singular point $Q$, the origin of the $y$-chart, and near $Q$ it is $V(z_1^2 + y^3 + y x_1^3)$.

Lean: `Singularity.eEight_xChart`, `Singularity.eEight_yChart`, `Singularity.eEight_zChart`, `Singularity.eEight_xChart_regular`, `Singularity.eEight_yChart_exceptional` (the charts, not part 1 or normality)

*Proof.* 1. We apply Lemma 2.3.4 with a different variable in each case. For $p = 2$, take $w = z$ and $G = x^3 + y^5$, since $-1 = 1$. Then $G_x = x^2$ and $G_y = y^4$. For $p = 3$, take $w = x$ and $G = -z^2 - y^5$. Then $G_z = -2z = z$ and $G_y = -5y^4 = y^4$. For $p = 5$, take $w = y$ and $G = -z^2 - x^3$. Then $G_z = -2z = 3z$ and $G_x = -3x^2 = 2x^2$. In each case the two derivatives vanish only where both variables of $G$ are 0, and then $w^p = 0$. Thus the origin is the only singular point, and $X$ is normal by Lemma 1.2.6.

2. In the $x$-chart, $F = x^2 (z_1^2 + x + x^3 y_1^5)$. Let $H = z_1^2 + x + x^3 y_1^5$, with $H_x = 1 + 3x^2 y_1^5$, $H_{y_1} = 5x^3 y_1^4$ and $H_{z_1} = 2 z_1$. For $p = 3$ we have $H_x = 1$. For $p = 2$ we have $H_x = 1 + x^2 y_1^5$ and $H_{y_1} = x^3 y_1^4$. If $H_x = 0$, then $x \ne 0$ and $y_1 \ne 0$, so $H_{y_1} \ne 0$. For $p = 5$, $H_x = H_{z_1} = 0$ gives $z_1 = 0$ and $x^2 y_1^5 = -1/3$. Then $H = x(1 + x^2 y_1^5) = 2x/3$, so $x = 0$, which contradicts $x^2 y_1^5 = -1/3$. Thus the $x$-chart is regular. In the $z$-chart, $F = z^2(1 + z x_1^3 + z^3 y_1^5)$, and the strict transform does not meet $V(z)$. In the $y$-chart, $F = y^2 (z_1^2 + y x_1^3 + y^3)$. On $V(y)$ we get $z_1 = 0$, and the derivative in $y$ of $z_1^2 + y x_1^3 + y^3$ is $x_1^3 + 3y^2 = x_1^3$ there. So the only singular point on the exceptional curve is $Q = (0, 0, 0)$. Away from the exceptional curve the blowup is isomorphic to $X \setminus \{0\}$, which is regular. Lemma 1.2.6 gives the normality. $\square$

In characteristic 0, the same computation gives the same chart, and the equation $z_1^2 + y^3 + y x_1^3$ is the equation of $E_7$, with the roles of the variables exchanged. The end result is a tree of eight projective lines with self-intersection $-2$ in the shape of the Dynkin diagram $E_8$. We do not carry out the remaining blowups here. In characteristics 2, 3 and 5 the equation $z^2 + x^3 + y^5$ still defines a rational double point of type $E_8$. It is the form $E_8^0$ in the list of Artin (1977), and in each of these characteristics the list has other forms of $E_8$ that are not equivalent to it. We cite these facts from Artin's paper, which has no key in the map, and we do not prove them.

### The cone over a plane cubic

The last example is a singularity that is not rational and that one blowup resolves, without a normalization step. It works in every characteristic.

**Example 2.3.14.** Let $k$ be an algebraically closed field. If the characteristic of $k$ is not 3, let $F = x^3 + y^3 + z^3$. If the characteristic is 3, let $F = y^2 z - x^3 - x z^2$. Let $C = V_+(F) \subseteq \mathbb{P}^2_k$ and let $X = V(F) \subseteq \mathbb{A}^3_k$ be the affine cone over $C$.

1. The curve $C$ is regular, and $\dim_k H^1(C, \mathcal{O}_C) = 1$.
2. The scheme $X$ is normal, with one singular point at the origin.
3. The blowup $X'$ of $X$ at the origin is regular, and the exceptional curve $E$ with its reduced structure is isomorphic to $C$. The conormal sheaf of $E$ is $\mathcal{O}_C(1)$, of degree 3.
4. The local ring $\mathcal{O}_{X,0}$ does not have a rational singularity.

Lean: `Singularity.cubicCone_fermat_xChart`, `Singularity.cubicCone_fermat_chart_regular`, `Singularity.cubicCone_three_xChart_regular`, `Singularity.cubicCone_fermat_finrank` (the charts, their regularity and the degree 3, in parts 1 and 3). The cohomology and part 4 are not in Lean yet.

*Proof.* 1. Let $P \in C$ be a point with all three partial derivatives of $F$ equal to 0 at $P$. For $F = x^3 + y^3 + z^3$ they are $3x^2$, $3y^2$ and $3z^2$, so $P = 0$, which is not a point of $\mathbb{P}^2_k$. For the second $F$ in characteristic 3, the derivatives are $-3x^2 - z^2 = -z^2$, $2yz$ and $y^2 - 2xz = y^2 + xz$. They give $z = 0$, then $y = 0$, and then $F = -x^3 = 0$ gives $x = 0$. Thus in both cases the partial derivatives have no common zero on $C$. On the chart $z \ne 0$ with $f(x, y) = F(x, y, 1)$ we have $f_x = F_x$ and $f_y = F_y$ at $z = 1$. If $f_x = f_y = 0$ at a point of $C$, then the Euler relation $x F_x + y F_y + z F_z = 3F = 0$ gives $F_z = 0$ there. Thus $f_x$ or $f_y$ is nonzero at each point of $C$ in this chart, and $C$ is regular there by the Jacobian criterion (Corollary 1.8.3 of Volume 1). The other charts are the same. For the cohomology, the exact sequence $0 \to \mathcal{O}(-3) \to \mathcal{O}_{\mathbb{P}^2} \to \mathcal{O}_C \to 0$ and [Har, Theorem III.5.1] give $H^1(\mathcal{O}_{\mathbb{P}^2}) = H^2(\mathcal{O}_{\mathbb{P}^2}) = 0$ and $\dim_k H^2(\mathcal{O}(-3)) = 1$. Thus $H^1(C, \mathcal{O}_C) \cong H^2(\mathbb{P}^2, \mathcal{O}(-3))$ has dimension 1.

2. A point $P \ne 0$ of $X$ with all partial derivatives 0 would give a point of $C$ with the same property. Thus $X \setminus \{0\}$ is regular, and the origin is singular, since $F \in \mathfrak{m}^3$. By Lemma 1.2.6, $X$ is normal.

3. The least degree of a monomial of $F$ is 3, and $F$ is homogeneous. In the $x$-chart, $y = x y_1$ and $z = x z_1$, so $F = x^3 F(1, y_1, z_1)$. The strict transform is $V(F(1, y_1, z_1)) \subseteq \operatorname{Spec} k[x, y_1, z_1]$. This is the product of the affine curve $C \cap \{X_0 \ne 0\}$ with the line $\operatorname{Spec} k[x]$, so it is regular. The ideal of the exceptional curve is $(x, x y_1, x z_1) = (x)$ there, and $E$ is $V(x) = C \cap \{X_0 \ne 0\}$, a reduced curve. The other two charts are the same. Thus $X'$ is regular and $E \cong C$. The conormal sheaf is generated by the class of $x$, $y$ or $z$ on the three charts, and $y = (Y/X) x$ on the overlap. As in Step 4 of the proof of Theorem 1.1.7, this is $\mathcal{O}_C(1)$. The section $X_0$ of $\mathcal{O}_C(1)$ vanishes on $C \cap V_+(X_0) = V_+(X_0, F(0, Y, Z))$, a scheme of length 3, so $\mathcal{O}_C(1)$ has degree 3 [Har, Section II.6].

4. The blowup $\pi : X' \to X$ is a normal modification, since $X'$ is regular, hence normal, and $\pi$ is an isomorphism over $X \setminus \{0\}$. By Proposition 2.1.9, part 1, the map $H^1(X', \mathcal{O}_{X'}) \to H^1(E, \mathcal{O}_E)$ is onto, and $H^1(E, \mathcal{O}_E) \ne 0$ by part 1. The end of the proof of Example 2.3.6 then shows that $\mathcal{O}_{X,0}$ does not have a rational singularity. $\square$

The process of Theorem 2.2.1 for $X$ stops after one blowup. The dual graph has one vertex, a curve of genus 1, and $\mathcal{O}_{X'}(E)|_E \cong \mathcal{O}_C(-1)$ has degree $-3$. In characteristic 3 the cubic $x^3 + y^3 + z^3$ is $(x + y + z)^3$, and its cone is not reduced. This is why the example uses another cubic there. The curve $y^2 z = x^3 + x z^2$ is regular in characteristic 3, but it is singular in characteristic 2, since the derivatives $x^2 + z^2$, $0$ and $y^2$ vanish at the point $(1 : 0 : 1)$ of the curve. In characteristic 2 the Fermat cubic is regular, so each characteristic has a regular cubic among the two.

### Notes and references

The surfaces $xy = z^n$ are the singularities $A_{n-1}$. Their resolution by blowups is the same in every characteristic, as Proposition 2.3.2 shows. In Example 2.3.5, one blowup turns one singular point into $p + 1$ singular points, and the number grows with $p$. Example 2.3.6 shows that the blowup of a normal surface need not be normal, so the normalization step of [Lip78] is necessary. Example 2.3.6 computes $H^1$ of the exceptional curve, and Example 2.3.7 computes $H^1$ of the resolution, in both cases by the Čech complex of two affine charts. Proposition 2.3.10 and Examples 2.3.11 and 2.3.12 give the dual graphs $A_{m-1}$, $D_4$ and $E_6$. We compute the self-intersections with Lemma 2.3.9, part 3, and we do not need a projective surface. The singularities of Proposition 2.3.10, Example 2.3.11 and Example 2.3.12 are rational double points, but we do not prove their rationality here. Example 2.3.14 is the classical cone over an elliptic curve, and it is not rational by Proposition 2.1.9. For more examples of resolutions in charts see [Har, Section V.3].
