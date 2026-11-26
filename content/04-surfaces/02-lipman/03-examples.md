---
title: Examples in characteristic p
nodes: []
sources: [Har, Mat, AM69, Lip78]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Examples in characteristic p

In this section we run the process of Theorem 2.2.1 on some surfaces in $\mathbb{A}^3_k$. All computations are in the charts of Lemma 1.1.6. The first family works over each field. The second example is a purely inseparable equation in characteristic $p$, and its first blowup produces $p + 1$ singular points. The third example shows that the normalization step is necessary, and it gives a singularity that is not rational. The last example computes the cohomology of the resolution of $xy = z^2$ and compares it with the third.

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

Lean: none yet

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

Lean: none yet

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

Lean: none yet

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

Lean: none yet

*Proof.* 1. By Proposition 2.3.2 with $n = 2$, the $x$-chart of $\tilde{X}$ is $V(y_1 - z_1^2) \subseteq \operatorname{Spec} k[x, y_1, z_1]$, with $y = xy_1$ and $z = xz_1$. It is the graph of $y_1 = z_1^2$, so it is $U = \operatorname{Spec} k[x, z_1]$, with $y = xz_1^2$. In the same way the $y$-chart is $V = \operatorname{Spec} k[y, z_2]$ with $z = yz_2$ and $x = yz_2^2$. The $z$-chart is $V(x_1y_1 - 1)$ with $x = zx_1$. On it $x_1 = x/z$ is a unit, so $x$ generates $\mathfrak{m}\mathcal{O}_{\tilde{X}}$ there. By the remark after the proof of Theorem 1.1.2, the $z$-chart lies in the $x$-chart. Thus $U$ and $V$ cover $\tilde{X}$. By $(\ast)$ in Section 1.1, $U \cap V$ is the open set of $U$ where $y/x = z_1^2$ is a unit, that is, $\operatorname{Spec} k[x, z_1, z_1^{-1}]$. On it $z_2 = z/y = xz_1/(xz_1^2) = z_1^{-1}$. Both charts are planes, so $\tilde{X}$ is regular.

2. On $U$ the ideal $\mathfrak{m}\mathcal{O}_{\tilde{X}}$ is $(x, xz_1^2, xz_1) = (x)$, and on $V$ it is $(y)$. Thus $E \cap U = \operatorname{Spec} k[z_1]$ and $E \cap V = \operatorname{Spec} k[z_2]$, glued by $z_2 = z_1^{-1}$. This is $\mathbb{P}^1_k$ with $z_1 = X_1/X_0$. The conormal sheaf is generated by the class $e_0$ of $x$ on $E \cap U$ and by the class $e_1$ of $y$ on $E \cap V$. On the overlap $y = z_1^2x$, so $e_1 = (X_1/X_0)^2 e_0$. The sheaf $\mathcal{O}(2)$ is generated by $X_0^2$ and $X_1^2$, and $X_1^2 = (X_1/X_0)^2X_0^2$. Thus $e_0 \mapsto X_0^2$ and $e_1 \mapsto X_1^2$ give an isomorphism with $\mathcal{O}(2)$, as in Step 4 of the proof of Theorem 1.1.7. The dual $\mathcal{O}_{\tilde{X}}(E)|_E$ is $\mathcal{O}(-2)$.

3. The scheme $\tilde{X}$ is separated, since $\pi$ is projective. So the Čech complex of the cover $\{U, V\}$ computes the cohomology of $\mathcal{O}_{\tilde{X}}$ [Har, Theorem III.4.5]. Inside $\mathcal{O}(U \cap V) = k[x, z_1, z_1^{-1}]$, with its basis of monomials $x^az_1^b$ for $a \ge 0$ and $b \in \mathbb{Z}$, the ring $\mathcal{O}(U)$ is spanned by the monomials with $b \ge 0$. The ring $\mathcal{O}(V) = k[xz_1^2, z_1^{-1}]$ is spanned by the monomials $x^az_1^{2a - c}$ with $c \ge 0$, that is, by the monomials with $b \le 2a$. Each monomial has $b \ge 0$ or $b < 0 \le 2a$, so $\mathcal{O}(U) + \mathcal{O}(V) = \mathcal{O}(U \cap V)$, and $H^1 = 0$. The ring $H^0 = \mathcal{O}(U) \cap \mathcal{O}(V)$ is spanned by the monomials with $0 \le b \le 2a$. Such a monomial is $x^iy^jz^l = x^{i+j+l}z_1^{2j+l}$ with $j = \lfloor b/2 \rfloor$, $l = b - 2j$ and $i = a - j - l \ge 0$. Thus $H^0$ is the image of $k[x, y, z]$, which is $k[x, y, z]/(xy - z^2)$. $\square$

Part 3 checks Lemma 2.1.2, part 1, in this case. In the language of Remark 2.1.4, the resolution $\tilde{X}$ has $H^1(\tilde{X}, \mathcal{O}_{\tilde{X}}) = 0$, while the resolution of Example 2.3.6 has $H^1 \ne 0$. Definition 2.1.3 asks for the vanishing on every normal modification, and Example 2.3.7 does not prove it. If we admit the fact of Remark 2.1.4, the example shows that the origin of $xy = z^2$ is a rational singularity. The curve $E$ is a projective line with $E \cdot E = -2$. In Example 2.3.6 the exceptional curve has genus 1, and this is the source of the nonzero $H^1$.

### Notes and references

The surfaces $xy = z^n$ are the singularities $A_{n-1}$. Their resolution by blowups is the same in every characteristic, as Proposition 2.3.2 shows. In Example 2.3.5, one blowup turns one singular point into $p + 1$ singular points, and the number grows with $p$. Example 2.3.6 shows that the blowup of a normal surface need not be normal, so the normalization step of [Lip78] is necessary. Example 2.3.6 computes $H^1$ of the exceptional curve, and Example 2.3.7 computes $H^1$ of the resolution, in both cases by the Čech complex of two affine charts. Example 2.3.7 is the case $n = 2$ of the surfaces $xy = z^n$, whose resolution in Proposition 2.3.2 has $n - 1$ exceptional curves. For more examples of resolutions in charts see [Har, Section V.3].
