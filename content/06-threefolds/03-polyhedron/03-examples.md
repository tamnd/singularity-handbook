---
title: Examples computed by hand
nodes: [SG00000013, SG00000015]
sources: [CP19, Moh87, HP19a]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Examples computed by hand

This section computes the invariants of Section 3.2 in two examples. The first example is a point blowup at which $\epsilon$ increases and $\omega$ does not. The second example is [CP19, Remark 2.70]: two equations with the same polyhedron and different values of $\omega$. We checked each computation with a short computer program, but each step below can be done by hand.

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

Lean: none yet

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

Lean: none yet

The term $c \, u_1^3 u_2 u_3$ does not change the polyhedron, because $w$ is not a vertex. It changes $\omega$, because the derivative in the direction $u_3$, which is not in $E$, sees each monomial of the initial form. Thus $\omega$ uses more information than the polyhedron. We compute only the invariants at the origin, and we do not check condition (E) for this example.

### Notes and references

The table of Example 3.3.1 also shows the pattern of Volume 7, Section 1.4: the increase of $\epsilon$ happens at a point where a translation $u_2 \mapsto u_2 + 1$ produces a square that cleaning removes. Example 3.3.1 is our own example. Example 3.3.2 is from [CP19]. For the increase of the residual order see [Moh87] and [HP19a].
