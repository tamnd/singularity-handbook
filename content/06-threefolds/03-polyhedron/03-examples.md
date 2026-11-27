---
title: Examples computed by hand
nodes: [SG00000013, SG00000015]
sources: [CP19, Hir67, Moh87, HP19a, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Examples computed by hand

The theorems of Cossart and Piltant that Section 3.2 cites are long, and we do not prove them. Examples are the best way to see what they say. An example shows which invariant moves under a blowup, and why. It also tests the statements: Examples 3.3.1, 3.3.4, 3.3.5 and 3.3.6 check a conclusion of Theorem 3.2.6 or Theorem 3.2.7 in one case. The polyhedron itself is due to Hironaka [Hir67], and Cossart and Piltant give examples of their invariants in [CP19, Section 1, Remark 2.70 and Example 3.6].

This section computes the invariants of Section 3.2 in six examples. The first example is a point blowup at which $\epsilon$ increases and $\omega$ does not. The second example is [CP19, Remark 2.70]: two equations with the same polyhedron and different values of $\omega$. The third example computes a characteristic polyhedron over $\mathbb{F}_3$ by vertex preparation, in two steps. The fourth example is a point blowup at which $\iota$ drops, followed by the blowup of a curve that resolves the singularity. The fifth example is the analogue of the first one for $p = 3$, with a table of all the points of the exceptional plane over $\mathbb{F}_3$. The sixth example carries out the step of Theorem 3.2.7 in the case $\epsilon = 1$, with a center that is not a coordinate curve in the given coordinates. We checked each computation with a short computer program in SymPy, but each step below can be done by hand.

We use these conventions. Let $k$ be a perfect field of characteristic $p$, let $S = k[[u_1, u_2, u_3]]$, and let $h = Z^p + f$ with $f$ clean (Volume 7, Definition 1.3.1). By Proposition 3.2.4, $(u; Z)$ is well adapted, and the invariants are read off from $f$. Let $\operatorname{ord} f \ge p$, so that $m(x) = p$ at the origin $x$. The blowup of the origin in the $u_j$-chart at the point with coordinates $t = (t_i)_{i \ne j}$ is
$$u_i = u_j (u'_i + t_i) \text{ for } i \ne j, \qquad Z = u_j Z', \qquad h' = Z'^p + u_j^{-p} f.$$
We write $u_i$ for $u'_i$ when no confusion is possible. The new divisor $E'$ is $\operatorname{div}(u_j)$ plus $\operatorname{div}(u'_i)$ for each $i \ne j$ with $\operatorname{div}(u_i) \subseteq E$ and $t_i = 0$. The series $u_j^{-p} f$ need not be clean, so we clean it before we read off the invariants.

### A point blowup at which epsilon increases

**Example 3.3.1.** Let $p = 2$, let
$$f = u_1 u_2^3 u_3^2 + u_1^3 u_2 u_3^2 + u_1^8 u_2 u_3,$$
and let $E = \operatorname{div}(u_1 u_2 u_3)$. Each monomial of $f$ has an odd exponent, so $f$ is clean, and $h$ is reduced.

*The point $x$.* We have $\operatorname{ord} f = 6$, so $\delta(x) = 3$ and $m(x) = 2$. The smallest exponents are $r = (1, 1, 1)$, so $f = u_1 u_2 u_3 G$ with $G = u_2^2 u_3 + u_1^2 u_3 + u_1^7$ and $\epsilon(x) = \operatorname{ord} G = 3$. All three variables belong to $E$, so $\omega(x) = \epsilon(x) = 3$. Thus $\iota(x) = (2, 3, \ge 2)$.

*Condition (E).* Modulo 2 we have $\partial f/\partial u_3 = u_1^8 u_2$. So $V(\partial f/\partial u_1, \partial f/\partial u_2, \partial f/\partial u_3) \subseteq V(u_1 u_2) \subseteq E$, and Lemma 2.3.3 shows that $(S, h, E)$ satisfies condition (E). So Theorems 3.2.6 and 3.2.7 apply to the blowup of the point $x$, which is permissible of the first kind.

*The point $t_2 = 1$, $t_3 = 0$ of the $u_1$-chart.* Here $u_2 = u_1(u_2 + 1)$ and $u_3 = u_1 u_3$. The three monomials of $f$ become $u_1^6 (u_2 + 1)^3 u_3^2$, $u_1^6 (u_2 + 1) u_3^2$ and $u_1^{10} (u_2 + 1) u_3$. In characteristic 2, $(u_2 + 1)^3 + (u_2 + 1) = u_2^3 + u_2^2$. So
$$u_1^{-2} f = u_1^4 u_2^3 u_3^2 + u_1^4 u_2^2 u_3^2 + u_1^8 u_2 u_3 + u_1^8 u_3.$$
The monomial $u_1^4 u_2^2 u_3^2 = (u_1^2 u_2 u_3)^2$ is a square. The translation $Z' \mapsto Z' + u_1^2 u_2 u_3$ removes it, and the clean part is
$$f' = u_1^4 u_2^3 u_3^2 + u_1^8 u_2 u_3 + u_1^8 u_3.$$
Its order is $9$. The new divisor is $E' = \operatorname{div}(u_1 u_3)$, since $t_2 = 1$. The smallest exponents of $u_1$ and $u_3$ are $4$ and $1$, so $\epsilon(x') = 9 - 5 = 4$. The initial form is $F' = U_1^4 U_2^3 U_3^2 + U_1^8 U_3$. The variable $U_2$ is not in $E'$, and $\partial F'/\partial U_2 = U_1^4 U_2^2 U_3^2 \ne 0$. So $\omega(x') = \epsilon(x') - 1 = 3$.

Thus $\epsilon$ increases from $3$ to $4$, while $\omega$ stays $3$ and $\iota(x') = \iota(x)$. The increase of $\epsilon$ is $1 = p^0$, the largest increase that Moh's bound allows (Volume 7, Theorem 1.4.1). The conclusions of Theorem 3.2.6 hold: $\epsilon(x) = \omega(x) = 3$ and $\delta(x) = 3 \in \mathbb{N}$. Here the center is $Y = \{x\}$, so $y = x$.

*The other points.* The table lists the seven points of the exceptional plane with coordinates $0$ or $1$ in the charts, each point in the first chart that contains it. The column "ord" is the order of the clean part of $u_j^{-2} f$.

| Chart | $t$ | $E'$ | ord | smallest exponents | $\epsilon(x')$ | $\omega(x')$ |
|---|---|---|---|---|---|---|
| $u_1$ | $(0, 0)$ | $u_1, u_2, u_3$ | 7 | $(4, 1, 1)$ | 1 | 1 |
| $u_1$ | $(0, 1)$ | $u_1, u_2$ | 5 | $(4, 1)$ | 0 | 0 |
| $u_1$ | $(1, 0)$ | $u_1, u_3$ | 9 | $(4, 1)$ | 4 | 3 |
| $u_1$ | $(1, 1)$ | $u_1$ | 7 | $(4)$ | 3 | 2 |
| $u_2$ | $(0, 0)$ | $u_1, u_2, u_3$ | 7 | $(1, 4, 1)$ | 1 | 1 |
| $u_2$ | $(0, 1)$ | $u_1, u_2$ | 5 | $(1, 4)$ | 0 | 0 |
| $u_3$ | $(0, 0)$ | $u_1, u_2, u_3$ | 8 | $(1, 1, 4)$ | 2 | 2 |

In the column $t$ the entries are $(t_2, t_3)$ in the $u_1$-chart, $(t_1, t_3)$ in the $u_2$-chart and $(t_1, t_2)$ in the $u_3$-chart, and the third row is the point that we computed above. At each point $m(x') = 2$, because the order is at least 2, and $\omega(x') \le 3$, as Theorem 3.2.6 says. At the two points with $\omega(x') = 0$, Theorem 3.2.7 applies. For example, at $t = (0, 1)$ in the $u_1$-chart, $u_1^{-2} f = u_1^4 u_2^3 (u_3 + 1)^2 + u_1^4 u_2 (u_3 + 1)^2 + u_1^8 u_2 (u_3 + 1)$. After expansion, each monomial has an odd exponent of $u_2$, so this series is clean, and its initial form is $U_1^4 U_2$, a monomial in the variables of $E'$. We do not compute the points of the exceptional plane that are not on this list.

Lean: `Singularity.Examples.example_3_3_1_chart` (the chart substitution)

### The polyhedron does not determine omega

**Example 3.3.2.** Let $p = 3$, let $c \in k$, let
$$f_c = u_1 u_2 u_3^3 + u_1^5 + u_2^5 + c \, u_1^3 u_2 u_3,$$
and let $E = \operatorname{div}(u_1 u_2)$. This is the example of [CP19, Remark 2.70] for $p = 3$, where $h$ is equal to its initial form. Each monomial of $f_c$ has an exponent prime to 3, so $f_c$ is clean, and $(u; Z)$ is well adapted by Proposition 3.2.4.

*The polyhedron.* The exponents divided by 3 are
$$v_1 = (\tfrac53, 0, 0), \quad v_2 = (0, \tfrac53, 0), \quad v_3 = (\tfrac13, \tfrac13, 1), \quad w = (1, \tfrac13, \tfrac13),$$
where $w$ comes from the term with $c$. All four points lie in the plane $x_1 + x_2 + x_3 = \frac53$, and
$$w = \tfrac{8}{15} v_1 + \tfrac{2}{15} v_2 + \tfrac{1}{3} v_3, \qquad \tfrac{8}{15} + \tfrac{2}{15} + \tfrac{1}{3} = 1.$$
So $w$ lies in the triangle with vertices $v_1, v_2, v_3$, and $\Delta(h; u; Z) = \operatorname{Conv}\{v_1, v_2, v_3\} + \mathbb{R}_{\ge 0}^3$ for each $c$. In particular $\delta(x) = \frac53 = 1 + \frac2p$ and $m(x) = 3$.

*The invariants.* The exponents of $u_1$ and of $u_2$ are $0$ in $u_2^5$ and in $u_1^5$, so $d_1 = d_2 = 0$ and $\epsilon(x) = 5 = p + 2$. The variable $U_3$ is not in $E$. For $F = f_c$ we have
$$\frac{\partial F}{\partial U_3} = 3 U_1 U_2 U_3^2 + c \, U_1^3 U_2 = c \, U_1^3 U_2.$$
So $\omega(x) = 5 = p + 2$ for $c = 0$, and $\omega(x) = 4 = p + 1$ for $c \ne 0$, as [CP19, Remark 2.70] says.

Lean: `Singularity.Examples.example_3_3_2_combination` (the convex combination)

The term $c \, u_1^3 u_2 u_3$ does not change the polyhedron, because $w$ is not a vertex. It changes $\omega$, because the derivative in the direction $u_3$, which is not in $E$, sees each monomial of the initial form. Thus $\omega$ uses more information than the polyhedron. We compute only the invariants at the origin, and we do not check condition (E) for this example.

### Vertex preparation over the prime field

**Example 3.3.3.** Let $p = 3$, $k = \mathbb{F}_3$, $S = k[[u_1, u_2, u_3]]$ and
$$h = X^3 + f, \qquad f = u_1^3 + u_1^3 u_2^3 + u_2^4 + u_3^5.$$
The series $f$ is not clean. We compute the characteristic polyhedron by vertex preparation (Lemma 3.1.10), and then we compare with cleaning.

*The first polyhedron.* By Lemma 3.1.10(1), $\Delta(h; u; X) = \frac13 N(f)$. The points $a/3$ for $a \in \operatorname{supp} f$ are $(1, 0, 0)$, $(1, 1, 0)$, $(0, \frac43, 0)$ and $(0, 0, \frac53)$. The point $(1, 1, 0)$ lies in $(1, 0, 0) + \mathbb{R}_{\ge 0}^3$, so it is not a vertex. The vertices are $(1, 0, 0)$, $(0, \frac43, 0)$ and $(0, 0, \frac53)$, and $\delta_{\mathbf 1}(h; u; X) = 1$. The vertex $(1, 0, 0)$ lies in $\mathbb{N}^3$, and the coefficient of $u_1^3$ is $1 \in k^3$. So it is solvable by Lemma 3.1.10(2). Indeed $\operatorname{in}_{(1, 0, 0)} h = X^3 + U_1^3 = (X + U_1)^3$.

*The first step.* Let $Z_1 = X + u_1$. By Lemma 3.1.10(3), with $\lambda = -1$,
$$h = Z_1^3 + f_1, \qquad f_1 = u_1^3 u_2^3 + u_2^4 + u_3^5.$$
Now $(1, 1, 0)$ is a vertex of $\frac13 N(f_1)$. For the weight $\alpha = (\frac1{10}, 1, 1)$ its value is $\frac{11}{10}$, while $(0, \frac43, 0)$ and $(0, 0, \frac53)$ have the values $\frac43$ and $\frac53$. So $(1, 1, 0)$ is the only point where $|\cdot|_\alpha$ is minimal. The vertex was hidden behind $(1, 0, 0)$ before the first step. It lies in $\mathbb{N}^3$, and its coefficient is $1$, so it is solvable.

*The second step.* Let $Z = Z_1 + u_1 u_2 = X + u_1 + u_1 u_2$. Then
$$h = Z^3 + f^{\mathrm{cl}}, \qquad f^{\mathrm{cl}} = u_2^4 + u_3^5.$$
The vertices $(0, \frac43, 0)$ and $(0, 0, \frac53)$ are not in $\mathbb{N}^3$. Since $\mathbb{F}_3$ is perfect, Lemma 3.1.10(4) shows that
$$\Delta(h; u) = \operatorname{Conv}\{(0, \tfrac43, 0), (0, 0, \tfrac53)\} + \mathbb{R}_{\ge 0}^3.$$
So $\delta(x) = \frac43$ and $m(x) = 3$ by Proposition 3.2.2(3). The value $\delta_{\mathbf 1}(h; u; X) = 1$ of the first polyhedron is only a lower bound.

*Cleaning.* The monomials of $f$ in $3 \mathbb{N}^3$ are $u_1^3$ and $u_1^3 u_2^3$. Let $g = -u_1 - u_1 u_2$. Then $g^3 = -u_1^3 - u_1^3 u_2^3$, and $g^3 + f = f^{\mathrm{cl}}$. So $X - g = Z$, and cleaning gives the two steps at once, as Proposition 3.2.4 says.

*The invariants.* Let $E = \operatorname{div}(u_1 u_2)$. The monomial $u_2^4$ is not divisible by $u_1$, and $u_3^5$ is not divisible by $u_2$. So $r_1 = r_2 = 0$, $d_1 = d_2 = 0$, and $\epsilon(x) = \operatorname{ord} f^{\mathrm{cl}} = 4$ by Proposition 3.2.4. The initial form is $F = U_2^4$, and $\partial F / \partial U_3 = 0$. So $\omega(x) = \epsilon(x) = 4$, and $\kappa(x) \ge 2$. For $E = \operatorname{div}(u_1)$ instead, $\epsilon(x) = 4$ again, but now $U_2$ is not a variable of $E$, and $\partial F / \partial U_2 = 4 U_2^3 = U_2^3 \ne 0$. So $\omega(x) = 3$. In the coordinates $(u; X)$ one would read off the wrong values $\operatorname{ord} f / 3 = 1$ and $\operatorname{ord} f = 3$ for $\delta(x)$ and $\epsilon(x)$.

Lean: `Singularity.Examples.taylor_example_3_3_3` (the translation)

### A point blowup at which the invariant drops

**Example 3.3.4.** Let $p = 2$, let $k$ be algebraically closed of characteristic 2, let
$$f = u_1^3 + u_2^3 + u_3^3,$$
and let $E = \operatorname{div}(u_1 u_2 u_3)$. Each monomial of $f$ has an odd exponent, so $f$ is clean, and $h = Z^2 + f$ is reduced.

*The point $x$.* We have $\operatorname{ord} f = 3$, so $\delta(x) = \frac32$ and $m(x) = 2$. No $u_j$ divides $f$, so $r = (0, 0, 0)$ and $\epsilon(x) = 3$. All three variables belong to $E$, so $\omega(x) = \epsilon(x) = 3$. Since $e = n = 3$, the vector space $\operatorname{Vdir}(x)$ lies in $\langle U_1, U_2, U_3 \rangle$, and $\kappa(x) = 4$ by [CP19, Definition 5.1]. So $\iota(x) = (2, 3, 4)$.

*Condition (E).* We have $\partial f / \partial u_i = 3 u_i^2 = u_i^2$. So $V(\partial f/\partial u_1, \partial f/\partial u_2, \partial f/\partial u_3)$ is the closed point, which lies in $E$, and $(S, h, E)$ satisfies condition (E) by Lemma 2.3.3. The blowup of $x$ is permissible of the first kind, so Theorem 3.2.6 applies.

*The blowup of $x$.* In the $u_1$-chart at the point $t = (t_2, t_3)$, the identity $(u + t)^3 = u^3 + t u^2 + t^2 u + t^3$ in characteristic 2 gives
$$u_1^{-2} f = u_1 g, \qquad g = (1 + t_2^3 + t_3^3) + t_2^2 u_2 + t_2 u_2^2 + u_2^3 + t_3^2 u_3 + t_3 u_3^2 + u_3^3.$$
Each monomial of $u_1 g$ has the exponent $1$ in $u_1$, so $f' = u_1 g$ is clean. If $1 + t_2^3 + t_3^3 \ne 0$, then $\operatorname{ord} f' = 1$, and $x'$ is a regular point. So the points of multiplicity 2 in this chart are the points of the curve
$$C = \{ U_1^3 + U_2^3 + U_3^3 = 0 \} \subset \mathbb{P}^2_k$$
of the exceptional plane. The curve $C$ is smooth in characteristic 2, since the partial derivatives $U_i^2$ have no common zero in $\mathbb{P}^2_k$. The equation $f$ is symmetric, so the other charts give the same result for the points of $C$ with $U_1 = 0$.

*The invariant at the points of $C$.* Let $x'$ lie over a point of $C$ in the $u_1$-chart. Then $t_2$ and $t_3$ are not both $0$, so the linear part $t_2^2 u_2 + t_3^2 u_3$ of $g$ is not $0$. So $\operatorname{ord} f' = 2$, $\delta(x') = 1$ and $m(x') = 2$. The initial form is $F' = U_1 (t_2^2 U_2 + t_3^2 U_3)$. The exponent of $u_1$ is $r_1 = 1$, and $g$ is not divisible by $u_2$ or $u_3$. So $\epsilon(x') = 2 - 1 = 1$. If $t_2 t_3 \ne 0$, then $E' = \operatorname{div}(u_1)$ and $\partial F' / \partial U_2 = t_2^2 U_1 \ne 0$. If $t_2 = 0$, then $E' = \operatorname{div}(u_1 u_2)$, $t_3 \ne 0$ and $\partial F' / \partial U_3 = t_3^2 U_1 \ne 0$. The case $t_3 = 0$ is the same. In each case $\omega(x') = \epsilon(x') - 1 = 0$, so $\kappa(x') = 1$ and
$$\iota(x') = (2, 0, 1) < (2, 3, 4) = \iota(x).$$
So one point blowup makes $\omega$ drop from $3$ to $0$. Condition (E) holds at $x'$ by [CP19, Proposition 2.34]. One can also see it directly with Lemma 2.3.3. We have $\partial f' / \partial u_2 = u_1 (u_2 + t_2)^2$ and $\partial f' / \partial u_3 = u_1 (u_3 + t_3)^2$. Since $t_2$ and $t_3$ are not both $0$, one of $u_2 + t_2$ and $u_3 + t_3$ is a unit of $k[[u_1, u_2, u_3]]$. So the common zeros of the derivatives lie in $V(u_1) \subseteq E'$.

*The second blowup.* Theorem 3.2.7 applies at $x'$, and here one more blowup suffices. The series $g$ has a nonzero linear part, so we can take $v = g$ as a coordinate. If $t_2 = 0$, then $(u_1, u_2, v)$ is a regular system of parameters, since the linear part of $g$ contains $t_3^2 u_3$. If $t_2 t_3 \ne 0$, then $(u_1, u_2, v)$ is one as well. The case $t_3 = 0$ is the same, with $u_2$ and $u_3$ exchanged. In these coordinates $f' = u_1 v$ is clean, and $E'$ is $\operatorname{div}(u_1)$ or $\operatorname{div}(u_1 u_2)$. The center $Y' = V(Z', u_1, v)$ is Hironaka-permissible with respect to $E'$, because $f' \in (u_1, v)^2$ and $V(u_1, v)$ has normal crossings with $E'$. This is the center of Case 2 of the proof of [CP19, Theorem 2.81], with $\delta(x') = 1$: the coordinate $u_1$ is the one with $d_1 > 0$, and $v$ plays the role of $u_{e + 1}$ there. In the $u_1$-chart at the point $v = u_1 (v'' + a)$, with $Z' = u_1 Z''$, the strict transform is $Z''^2 + v'' + a$. Let $b \in k$ with $b^2 = a$. Then $Z''^2 + v'' + a = (Z'' + b)^2 + v''$, which has order 1 at the point $Z'' = b$. In the $v$-chart at the origin, $u_1 = v u''_1$ and the strict transform is $Z''^2 + u''_1$, of order 1. So all the points over $x'$ are regular.

*The resolution.* Let $X_1$ be the blowup of $X$ at $x$. The ring $S[Z]/(h)$ is finite over $S$, so $X$ has only the closed point $x$, and each closed point of $X_1$ lies over $x$. Let $\Gamma \subset X_1$ be the reduced curve over $C$. In the $u_1$-chart it is $V(Z', u_1, 1 + s_2^3 + s_3^3)$ with $s_j = u_j/u_1$, and at each of its closed points it is the center $Y'$ above. So $\Gamma$ is a regular curve, and it is Hironaka-permissible with respect to $E_1$. Let $X_2$ be the blowup of $X_1$ along $\Gamma$. The closed points of $X_2$ over $\Gamma$ are regular by the chart computation, and the other closed points of $X_2$ map isomorphically to closed points of $X_1$ of multiplicity 1. So each closed point of $X_2$ is regular. The morphism $X_2 \to X$ is proper, so each point of $X_2$ specializes to a closed point, and a localization of a regular local ring is regular [Mat]. Thus $X_2$ is regular, and two Hironaka-permissible blowups resolve $X$.

Lean: `Singularity.Examples.example_3_3_4_chart` (the chart substitution)

For the first blowup, Theorem 3.2.6 gives only $\iota(x') \le \iota(x)$. The invariant drops because $C$ is smooth. At each point of $C$ the linear part $t_2^2 u_2 + t_3^2 u_3$ of $g$ is an equation of the tangent line of $C$, and it contains a variable that is not in $E'$. In Example 3.3.1, by contrast, one point has $\iota(x') = \iota(x)$.

### An increase of epsilon for p = 3

Example 3.3.1 has $p = 2$. The next example shows the same effect for $p = 3$, and it shows where the cube that cleaning removes comes from.

**Example 3.3.5.** Let $p = 3$, let $k$ be a perfect field of characteristic 3, let
$$f = u_1^2 u_2^4 - u_1^5 u_2 + u_1^2 u_2 u_3^4,$$
and let $E = \operatorname{div}(u_1 u_2 u_3)$. The exponents $(2, 4, 0)$, $(5, 1, 0)$ and $(2, 1, 4)$ are not in $3 \mathbb{N}^3$, so $f$ is clean, and $h = Z^3 + f$ is reduced.

*The point $x$.* The first two monomials have degree 6 and the third has degree 7, so $\operatorname{ord} f = 6$, $\delta(x) = 2$ and $m(x) = 3$. We have $f = u_1^2 u_2 G$ with
$$G = u_2^3 - u_1^3 + u_3^4, \qquad \operatorname{in}(G) = U_2^3 - U_1^3 = (U_2 - U_1)^3,$$
where the last equality holds in characteristic 3. So $r = (2, 1, 0)$ and $\epsilon(x) = \operatorname{ord} G = 3$. All three coordinates belong to $E$, so $\omega(x) = \epsilon(x) = 3$ by Lemma 3.2.14(3), and $\iota(x) = (3, 3, \ge 2)$.

*Condition (E).* Modulo 3 we have $\partial f/\partial u_3 = 4 u_1^2 u_2 u_3^3 = u_1^2 u_2 u_3^3$. So the common zero set of the three derivatives lies in $V(u_1 u_2 u_3) = E$, and $(S, h, E)$ satisfies condition (E) by Lemma 2.3.3. The blowup of the point $x$ is permissible of the first kind, and Theorem 3.2.6 applies, since $\omega(x) > 0$.

*The point $t_2 = 1$, $t_3 = 0$ of the $u_1$-chart.* Here $u_2 = u_1 (u_2 + 1)$ and $u_3 = u_1 u_3$. After division by $u_1^3$ the three monomials of $f$ become $u_1^3 (u_2 + 1)^4$, $-u_1^3 (u_2 + 1)$ and $u_1^4 (u_2 + 1) u_3^4$. In characteristic 3,
$$(u_2 + 1)^4 - (u_2 + 1) = (u_2 + 1) \bigl( (u_2 + 1)^3 - 1 \bigr) = (u_2 + 1) u_2^3 = u_2^4 + u_2^3.$$
So
$$u_1^{-3} f = u_1^3 u_2^4 + u_1^3 u_2^3 + u_1^4 u_2 u_3^4 + u_1^4 u_3^4.$$
The monomial $u_1^3 u_2^3 = (u_1 u_2)^3$ is a cube, and the translation $Z' \mapsto Z' - u_1 u_2$ removes it, since $(Z' + u_1 u_2)^3 = Z'^3 + u_1^3 u_2^3$. The clean part is
$$f' = u_1^3 u_2^4 + u_1^4 u_2 u_3^4 + u_1^4 u_3^4.$$
Its order is $7 \ge 3$, so $m(x') = 3$ and $\delta(x') = \frac73$. The new divisor is $E' = \operatorname{div}(u_1 u_3)$, since $t_2 \ne 0$ and $t_3 = 0$. The smallest exponents of $u_1$ and $u_3$ are $3$ and $0$, so $\epsilon(x') = 7 - 3 = 4$. The initial form is $F' = U_1^3 U_2^4$. The variable $U_2$ is not in $E'$, and its exponent $4$ is prime to 3. So $\omega(x') = \epsilon(x') - 1 = 3$.

Thus $\epsilon$ goes up from $3$ to $4$, by $1 = p^0$, the largest increase that Moh's bound allows (Volume 7, Theorem 1.4.1). The invariant $\omega$ stays $3$. The conclusions of Theorem 3.2.6 hold: $\epsilon(x) = \omega(x) = 3$ and $\delta(x) = 2 \in \mathbb{N}$.

*Where the cube comes from.* The point $(1 : 1 : 0)$ of the exceptional plane lies on the line $U_2 = U_1$, and $\operatorname{in}(G)$ is the cube of $U_2 - U_1$. After the translation $u_2 \mapsto u_2 + 1$ of the chart, this cube becomes the cube $u_1^3 u_2^3$, and cleaning removes it. So the part of $f$ of degree 6 loses a term, and the order goes up. The third monomial of $f$ does not spoil this, because $t_3 = 0$ keeps its image $u_1^4 (u_2 + 1) u_3^4$ of order at least 8. At the points $t = (1, 1)$ and $t = (1, 2)$ the same monomial contains $u_1^4$, and the order is only 4.

*All the points over $\mathbb{F}_3$.* The table lists the 13 points of the exceptional plane with coordinates in $\mathbb{F}_3$, each in the first chart that contains it, with the conventions of the table of Example 3.3.1.

| Chart | $t$ | $E'$ | ord | smallest exponents | $\epsilon(x')$ | $\omega(x')$ |
|---|---|---|---|---|---|---|
| $u_1$ | $(0, 0)$ | $u_1, u_2, u_3$ | 4 | $(3, 1, 0)$ | 0 | 0 |
| $u_1$ | $(0, 1)$, $(0, 2)$ | $u_1, u_2$ | 4 | $(3, 1)$ | 0 | 0 |
| $u_1$ | $(1, 0)$ | $u_1, u_3$ | 7 | $(3, 0)$ | 4 | 3 |
| $u_1$ | $(1, 1)$, $(1, 2)$ | $u_1$ | 4 | $(3)$ | 1 | 1 |
| $u_1$ | $(2, 0)$ | $u_1, u_3$ | 4 | $(3, 0)$ | 1 | 0 |
| $u_1$ | $(2, 1)$, $(2, 2)$ | $u_1$ | 4 | $(3)$ | 1 | 0 |
| $u_2$ | $(0, 0)$ | $u_1, u_2, u_3$ | 5 | $(2, 3, 0)$ | 0 | 0 |
| $u_2$ | $(0, 1)$, $(0, 2)$ | $u_1, u_2$ | 5 | $(2, 3)$ | 0 | 0 |
| $u_3$ | $(0, 0)$ | $u_1, u_2, u_3$ | 7 | $(2, 1, 3)$ | 1 | 1 |

At each of the 13 points $m(x') = 3$, and $\omega(x') \le 3$, as Theorem 3.2.6 says. Only one point has $\epsilon(x') > \epsilon(x)$. Lemma 3.2.14(2) explains the two values of $\omega$ in the rows with $\epsilon(x') = 1$. At $t = (1, 1)$ the initial form is $U_1^4$, so $\operatorname{in}(G') = U_1$ lies in the span of the variables of $E'$, and $\omega(x') = 1$. At $t = (2, 0)$ we have $(u_2 - 1)^4 - (u_2 - 1) = u_2^4 + 2 u_2^3 + u_2 + 2$ modulo 3. The constant $2 = (-1)^3$ and the monomial $2 u_2^3$ give cubes, and after cleaning the initial form is $U_1^3 U_2$. So $\operatorname{in}(G') = U_2$ is transverse to $E'$, and $\omega(x') = 0$.

Lean: none yet

### A curve center when epsilon is one

The step of Theorem 3.2.7 in the case $\epsilon(x) = 1$ and $\delta(x) = 1$ blows up a curve that one may have to find after a change of coordinates [CP19, proof of Theorem 2.81, Case 2]. The next example shows this step, and it shows that the point blowup does not help.

**Example 3.3.6.** Let $p = 3$, let $k$ be algebraically closed of characteristic 3, let
$$f = u_1^2 u_2 + u_1^2 u_3^2 = u_1^2 (u_2 + u_3^2),$$
and let $E = \operatorname{div}(u_1)$. The exponents $(2, 1, 0)$ and $(2, 0, 2)$ are not in $3 \mathbb{N}^3$, so $f$ is clean.

*The point $x$.* We have $\operatorname{ord} f = 3$, so $\delta(x) = 1$ and $m(x) = 3$. Further $r_1 = 2$ and $G = u_2 + u_3^2$, so $\epsilon(x) = 1$ and $\operatorname{in}(G) = U_2$. This form is not in the span of $U_1$, so $\omega(x) = 0$ by Lemma 3.2.14(2), and $\iota(x) = (3, 0, 1)$. The derivatives of $f$ modulo 3 are $-u_1 (u_2 + u_3^2)$, $u_1^2$ and $-u_1^2 u_3$, and their common zero set is $V(u_1) = E$. So condition (E) holds by Lemma 2.3.3.

*The point blowup.* At the origin of the $u_3$-chart, $u_1 = u_3 u_1'$ and $u_2 = u_3 u_2'$, and
$$u_3^{-3} f = u_1'^2 u_2' + u_1'^2 u_3 = u_1'^2 (u_2' + u_3).$$
This series is clean, of order 3, and the new divisor is $\operatorname{div}(u_1' u_3)$. So $\delta(x') = 1$, $r = (2, 0)$, $\epsilon(x') = 1$ and $\operatorname{in}(G') = U_2 + U_3$. Since $U_2$ is not in $E'$, $\omega(x') = 0$. So $\iota(x') = \iota(x)$, and $\delta$ does not drop at this point.

*The coordinate $u_{e + 1}$.* Let $v = u_2 + u_3^2$. Since $v \equiv u_2$ modulo $\mathfrak{m}_S^2$, the family $(u_1, v, u_3)$ is a regular system of parameters of $S$, and $E = \operatorname{div}(u_1)$ is still a coordinate hyperplane. In these coordinates $f = u_1^2 v$. This is the form $H^{-1} f = (u_{e + 1})$ of Section 3.2, with $H = u_1^2$ and $u_{e + 1} = v$.

*The center.* Let $Y = V(Z, u_1, v)$. In the given coordinates $Y = V(Z, u_1, u_2 + u_3^2)$, a curve that is not a coordinate curve. We have $f \in (u_1, v)^3$, so $h \in (Z, u_1, v)^3$, and the image of $h$ modulo $(u_1, v)$ is $Z^3$. So $m(y) = 3$. The curve $W = V(u_1, v)$ is regular and has normal crossings with $E$. So $Y$ is Hironaka-permissible with respect to $E$. The coordinate curve $V(Z, u_1, u_2)$ is not permissible: $f$ has the term $u_1^2 u_3^2$, which is not in $(u_1, u_2)^3$, so the multiplicity at its generic point is less than 3.

*The blowup of $Y$.* In the $u_1$-chart at the point $v = u_1 (v' + a)$, with $a \in k$ and $Z = u_1 Z'$, the strict transform is
$$h' = Z'^3 + u_1^{-3} u_1^2 \cdot u_1 (v' + a) = Z'^3 + v' + a.$$
Let $b \in k$ with $b^3 = a$. Then $h' = (Z' + b)^3 + v'$, which has order 1 at the point $Z' = -b$. So this point is regular. In the $v$-chart at the origin, $u_1 = v u_1'$ and $Z = v Z'$, and the strict transform is $Z'^3 + u_1'^2$, of order 2. So each point $x'$ over $x$ has $m(x') \le 2 < p$, as [CP19, Proposition 2.79] says for this center.

Lean: none yet

The two blowups of this example have the same invariant at the start, and they behave in a different way. The point blowup keeps $\iota$ at the origin of one chart, while the blowup of $Y$ ends the case $m = p$ at once. The center $Y$ is visible only in the coordinates $(u_1, v, u_3)$, in which $f$ is a monomial times the transverse coordinate. This is the reason why Cossart and Piltant choose the coordinates with $H^{-1} f = (u_{e + 1})$ before they choose the center.

### Notes and references

The table of Example 3.3.1 also shows the pattern of Volume 7, Section 1.4: the increase of $\epsilon$ happens at a point where a translation $u_2 \mapsto u_2 + 1$ produces a square that cleaning removes. Examples 3.3.1, 3.3.3, 3.3.4, 3.3.5 and 3.3.6 are our own examples. Example 3.3.2 is from [CP19]. Example 3.3.6 follows Case 2 of [CP19, proof of Theorem 2.81], and Example 3.3.5 is the pattern of Example 3.3.1 for $p = 3$. We computed the table of Example 3.3.5 with SymPy, and we checked the rows with an increase or with $\omega(x') = 0$ by hand. For the increase of the residual order see [Moh87] and [HP19a].
