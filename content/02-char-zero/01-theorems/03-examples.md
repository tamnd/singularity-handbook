---
title: Three examples
nodes: [SG0000002C, SG0000001A]
sources: [Kol07, Hau03, Har, Cut04]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Three examples

The examples of this section are small enough to be done by hand. They show the three things that a resolution algorithm must handle: the singular variety itself, the divisor that the blowups create, and centers of positive dimension. In each case we only verify the claims that we state; we do not claim that a given canonical algorithm makes the same choices.

### Curves

For curves there is nothing to blow up in the abstract sense: normalization resolves.

**Theorem 1.3.1 (resolution of curves).** Let $X$ be an integral variety of dimension at most 1 over a field of any characteristic. Then the normalization $X' \to X$ is a resolution of $X$.

Node: SG0000002C · Lean: `Singularity.Curves.integralResolutionInDim_one`

This is Volume 1, Theorem 2.5.6, with a complete proof there. The normalization is finite, so it is proper, and a normal Noetherian domain of dimension 1 is regular. With the reduction to integral varieties of Volume 9, Section 1.3, it gives $\mathrm{Res}(p, 1)$ for each $p$, which is the node SG0000001A and the Lean theorem `Singularity.Curves.resolutionInDim_one`. Normalization is not a sequence of blowups of the ambient space, and it does not give an embedded resolution. For a plane curve, the embedded resolution needs point blowups, as the next example shows.

### The cusp

**Example 1.3.2 (the cusp).** Let $C \subseteq \mathbb{A}^2$ be the curve $y^2 = x^3$ and $I = (y^2 - x^3)$. We give a sequence of three point blowups $\Pi \colon Y_3 \to \mathbb{A}^2$ after which $\Pi^* I$ is the ideal of the divisor
$$C_3 + 2 E_1 + 3 E_2 + 6 E_3$$
with simple normal crossings, where $C_3$ is the strict transform of $C$ and $E_i$ is the strict transform of the $i$th exceptional curve.

Lean: `Singularity.Example.cusp_chart_x`, `Singularity.Example.cusp_chart_y`, `Singularity.CharZeroExamples.cusp_step_two`, `Singularity.CharZeroExamples.cusp_step_three`, `Singularity.CharZeroExamples.cusp_total_u`, `Singularity.CharZeroExamples.cusp_total_v`, `Singularity.CharZeroExamples.cusp_step_three_disjoint` (the chart equations and the multiplicities, not the normal crossings)

*Step 1.* Blow up the origin. In the chart $y = x y_1$ the pullback of $f = y^2 - x^3$ is $x^2 (y_1^2 - x)$. The exceptional curve is $E_1 = (x = 0)$, with multiplicity 2, and the strict transform is $C_1 = (x = y_1^2)$, a smooth curve. In the other chart $x = x_1 y$ the pullback is $y^2 (1 - x_1^3 y)$, and the strict transform $1 = x_1^3 y$ does not meet $E_1 = (y = 0)$. So $C_1$ is smooth, and $C_1 \to C$ is the normalization. But $C_1$ meets $E_1$ only at the point $p_1 = (x, y_1) = (0, 0)$, and there it is tangent to $E_1$: the restriction of $x - y_1^2$ to $E_1 = (x = 0)$ is $-y_1^2$, which vanishes to order 2. So $C_1 + 2E_1$ does not have normal crossings at $p_1$.

*Step 2.* Blow up $p_1$, with coordinates $(x, y_1)$. In the chart $x = x_2 y_1$ the pullback of $x^2 (y_1^2 - x)$ is
$$x_2^2 y_1^2 \cdot y_1 (y_1 - x_2) = x_2^2 \, y_1^3 \, (y_1 - x_2).$$
The new exceptional curve is $E_2 = (y_1 = 0)$ with multiplicity 3, the strict transform of $E_1$ is $(x_2 = 0)$ with multiplicity 2, and the strict transform of $C$ is $C_2 = (y_1 = x_2)$. In the other chart $y_1 = y_2 x$ the pullback is $x^3 (y_2^2 x - 1)$, and neither the strict transform of $E_1$ nor $C_2$ meets $E_2 = (x = 0)$ there. So the three smooth curves $E_1$, $E_2$, $C_2$ pass through the origin $p_2$ of the first chart, with three distinct tangent lines. Each two of them meet transversally, but three components through one point of a surface is not a normal crossing.

*Step 3.* Blow up $p_2$, with coordinates $(x_2, y_1)$. In the chart $y_1 = u x_2$ the pullback is
$$x_2^2 \cdot u^3 x_2^3 \cdot x_2 (u - 1) = x_2^6 \, u^3 \, (u - 1),$$
so $E_3 = (x_2 = 0)$ has multiplicity 6, the strict transform of $E_2$ is $(u = 0)$, and $C_3 = (u = 1)$. In the chart $x_2 = v y_1$ the pullback is $v^2 y_1^6 (1 - v)$, so the strict transform of $E_1$ is $(v = 0)$ and $C_3 = (v = 1)$. On $E_3 \cong \mathbb{P}^1$ the three curves $E_1$, $E_2$, $C_3$ meet $E_3$ at the three distinct points $v = 0$, $u = 0$ and $u = v = 1$, each transversally, and no two of $E_1$, $E_2$, $C_3$ meet. Away from $E_3$ nothing changed, and Steps 1 and 2 show that there are no other bad points. Thus $\Pi^* I$ is the ideal of $C_3 + 2E_1 + 3E_2 + 6E_3$, and this divisor has simple normal crossings. $\square$

The example shows the difference between the resolution of $C$, which is reached after one blowup, and the monomialization of $I$ in the sense of Theorem 1.1.7, which needs two more. The two extra blowups have centers on the exceptional divisor, at points where the strict transform $C_1$ is already smooth. They are needed because the divisor created by the first blowup is part of the problem. This is the reason why the algorithm carries a divisor $E$ with it.

### The Whitney umbrella

**Example 1.3.3 (the Whitney umbrella).** Let $X \subseteq \mathbb{A}^3$ be the surface $x^2 = y^2 z$, with $f = x^2 - y^2 z$. Then:

1. The singular locus of $X$ is the $z$-axis $L = (x = y = 0)$, and $f$ has order 2 at each point of $L$.
2. The tangent cone of $X$ at the origin is the double plane $x^2 = 0$, and at a point $(0, 0, c)$ with $c \ne 0$ it is $x^2 - c y^2 = 0$, a pair of planes over an algebraic closure of $k$.
3. The blowup of $\mathbb{A}^3$ along $L$ resolves $X$: the strict transform $X_1$ is smooth, and $X_1$ and the exceptional divisor $F$ have simple normal crossings.
4. The blowup of $\mathbb{A}^3$ at the origin does not improve the singularity: in one chart the strict transform is again a Whitney umbrella.

Lean: `Singularity.CharZeroExamples.whitneyEq_singular_iff`, `Singularity.CharZeroExamples.ord_whitneyEq`, `Singularity.CharZeroExamples.ord_whitneyEq_translate`, `Singularity.whitney_lineChart_x`, `Singularity.whitney_lineChart_y`, `Singularity.whitney_pointChart_z` (the singular locus, the order and the chart equations)

*Proof.* (1) The partial derivatives are $\partial_x f = 2x$, $\partial_y f = -2yz$ and $\partial_z f = -y^2$. They vanish together exactly when $x = 0$ and $y = 0$, and then $f = 0$. A point of $X$ is singular if and only if all partials vanish there, so $\operatorname{Sing}(X) = L$. At a point of $L$ all partials vanish, so the order is at least 2, and the second derivative $\partial_x^2 f = 2$ is a unit, so it is exactly 2.

(2) At the origin the homogeneous part of degree 2 of $f$ is $x^2$. At $(0, 0, c)$, write $z = c + t$. Then $f = x^2 - c y^2 - y^2 t$, and the part of degree 2 in $(x, y, t)$ is $x^2 - c y^2$.

(3) The blowup along $L = (x = y = 0)$ has two charts. In the chart $x = x_1 y$ the pullback of $f$ is $y^2 (x_1^2 - z)$. The exceptional divisor is $F = (y = 0)$ and the strict transform is $X_1 = (z = x_1^2)$, a graph, hence smooth. The differentials $dy$ and $dz - 2 x_1 dx_1$ are independent everywhere, so $X_1$ and $F$ meet transversally along the smooth curve $(y = 0, z = x_1^2)$. In the chart $y = y_1 x$ the pullback is $x^2 (1 - y_1^2 z)$. The strict transform $X_1 = (y_1^2 z = 1)$ is smooth, because on it $y_1 \ne 0$ and $z \ne 0$, so the partial derivative $2 y_1 z$ in $y_1$ is not zero. Its equation does not involve $x$, so it meets $F = (x = 0)$ transversally. Thus $X_1$ is smooth and $X_1 + F$ has simple normal crossings in the sense of Definition 1.1.2.

(4) Blow up the origin and take the chart $x = x_1 z$, $y = y_1 z$. The pullback of $f$ is $x_1^2 z^2 - y_1^2 z^3 = z^2 (x_1^2 - y_1^2 z)$. The strict transform is $(x_1^2 = y_1^2 z)$, the same equation as $X$. $\square$

The order of $f$ is 2 at every point of $L$, so the order alone does not see that the origin is a worse point than the others. Part (2) shows that the tangent cone does. A resolution algorithm that blows up the locus of maximal order would blow up $L$ here, which by part (3) is a good choice. An algorithm that uses the tangent cone to find the worst point would blow up the origin, and by part (4) it would return to the same singularity. Here the rough invariant gives the right center and the finer invariant gives the wrong one. Kollár concludes that we should not look at the singularities too carefully [Kol07, Chapter 3], Section "What is a good resolution algorithm?". In Chapter 3 the invariant is computed on a hypersurface of maximal contact. For the umbrella, Example 3.2.6 computes the coefficient ideal on $H = (x = 0)$ and finds its cosupport, which is again $L$.

### A principalization by hand

The cusp is a curve, and its ideal is already principal. Principalization is a statement about ideals that are not principal, and the simplest such ideals are generated by monomials. We principalize the ideal $I = (x^2, y^3)$ on $\mathbb{A}^2$ by hand, and we record at each step the data that the algorithm of Chapter 3 uses. Section 3.3 runs the algorithm on the same ideal and finds the same three point blowups.

*Example (the ideal $(x^2, y^3)$).* Let $I = (x^2, y^3)$ on $X_0 = \mathbb{A}^2$, with $E = \emptyset$. Its cosupport is the origin, and its order there is 2. We claim that three point blowups $\Pi \colon X_3 \to X_0$ give
$$\Pi^* I = \mathcal{O}_{X_3}(-2E_1 - 3E_2 - 6E_3),$$
where $E_i$ is the birational transform in $X_3$ of the $i$th exceptional curve, and that $E_1 + E_2 + E_3$ has simple normal crossings.

*Step 1.* Blow up the origin. In the chart $y = x y_1$ the pullback is $(x^2, x^3 y_1^3) = (x^2)$, since $x^2$ divides $x^3 y_1^3$. In the chart $x = x_1 y$ the pullback is $(x_1^2 y^2, y^3) = y^2 \cdot (x_1^2, y)$. The exceptional curve $E_1$ is $(x = 0)$ in the first chart and $(y = 0)$ in the second. So $\Pi_1^* I = \mathcal{O}(-2E_1) \cdot N_1$ with $N_1 = (x_1^2, y)$ in the second chart and $N_1 = \mathcal{O}$ in the first. The factor $N_1$ is not principal at the point $P = (x_1 = y = 0)$. This is the point of $E_1$ that corresponds to the tangent direction of the $y$-axis, and it lies on the birational transform $(x_1 = 0)$ of the $y$-axis. At $P$ the ideal $N_1$ has order 1, because it contains $y$.

*Step 2.* Blow up $P$, with the coordinates $(x_1, y)$. In the chart $x_1 = u$, $y = u v$ the pullback of $N_1$ is $(u^2, u v) = u \cdot (u, v)$, so the total pullback of $I$ is
$$x = u^2 v, \quad y = u v, \qquad \Pi_2^* I = (u^4 v^2, u^3 v^3) = u^3 v^2 \cdot (u, v).$$
Here $E_2 = (u = 0)$ and the birational transform of $E_1$ is $(v = 0)$. In the chart $y = w$, $x_1 = t w$ we have $x = t w^2$ and $\Pi_2^* I = (t^2 w^4, w^3) = (w^3)$, with $E_2 = (w = 0)$; the transform of $E_1$ does not meet this chart. So $\Pi_2^* I = \mathcal{O}(-2E_1 - 3E_2) \cdot N_2$ with $N_2 = (u, v)$, the ideal of the point $P' = E_1 \cap E_2$.

*Step 3.* Blow up $P'$. The ideal $N_2$ is the ideal of a point, so by the example of the maximal ideal in Section 1.1 its pullback is $\mathcal{O}(-E_3)$. We check this together with the coefficients. In the chart $u = a$, $v = a b$ we have $x = a^3 b$ and $y = a^2 b$, so
$$\Pi_3^* I = (a^6 b^2, a^6 b^3) = (a^6 b^2),$$
with $E_3 = (a = 0)$ and $E_1 = (b = 0)$. In the chart $v = c$, $u = c d$ we have $x = c^3 d^2$ and $y = c^2 d$, so
$$\Pi_3^* I = (c^6 d^4, c^6 d^3) = (c^6 d^3),$$
with $E_3 = (c = 0)$ and $E_2 = (d = 0)$. Away from $E_3$ nothing changed. So $\Pi_3^* I = \mathcal{O}(-2E_1 - 3E_2 - 6E_3)$. In each chart the divisors are coordinate lines, $E_1$ and $E_2$ meet $E_3$ at two distinct points, and they do not meet each other. So $E_1 + E_2 + E_3$ has simple normal crossings. $\square$

We checked the chart computations of the three steps with a computer algebra system. The data of the steps fit in a table. The column $N_i$ gives the factor that is not yet monomial, and the column "order" gives its order at the next center.

| step | center | $\Pi_i^* I$ | $N_i$ near the center | order of $N_i$ |
|---|---|---|---|---|
| 0 | origin | $(x^2, y^3)$ | $(x^2, y^3)$ | 2 |
| 1 | $P \in E_1$ | $\mathcal{O}(-2E_1) N_1$ | $(x_1^2, y)$ | 1 |
| 2 | $P' = E_1 \cap E_2$ | $\mathcal{O}(-2E_1 - 3E_2) N_2$ | $(u, v)$ | 1 |
| 3 | none | $\mathcal{O}(-2E_1 - 3E_2 - 6E_3)$ | $\mathcal{O}$ | 0 |

Three features of this table appear in the algorithm. First, the order alone does not decide when to stop. After Step 1 the order of $N_1$ is 1, but $N_1$ is still not principal, and two more blowups are needed. Second, after Step 1 the ideal $N_1 = (x_1^2, y)$ is the ideal of a point with a double structure along $E_1$: its restriction to $E_1 = (y = 0)$ is $(x_1^2)$. The second and third centers are chosen by this restriction, a problem in one dimension less. Section 3.3 shows that this is the going-up step, Lemma 3.3.4, applied to $E_1$. Third, the last center $P'$ is the intersection of two exceptional curves. The ideal $N_2 = (u, v)$ is generated by the equations of $E_2$ and $E_1$, so it is already monomial as an ideal, but not principal.

*Remark (comparison with the cusp).* Exchange $x$ and $y$ in the example. Then the ideal is $(y^2, x^3)$, the ideal generated by the two terms of the equation $y^2 - x^3$ of the cusp, and the three centers become the centers of Example 1.3.2: the origin, the point of $E_1$ in the direction of the $x$-axis, and the point $E_1 \cap E_2$. The coefficients $2, 3, 6$ of the exceptional curves are the same in both examples. Here is the reason. Each $E_i$ defines a valuation $v_i$ of $k(x, y)$, the order of vanishing along $E_i$. The charts show that $v_i$ is a monomial valuation: $v_i(x) = \alpha_i$ and $v_i(y) = \beta_i$ with $(\alpha_i, \beta_i) = (1, 1), (1, 2), (2, 3)$ for $i = 1, 2, 3$, and $v_i$ of a polynomial is the minimum of $\alpha_i a + \beta_i b$ over its monomials $x^a y^b$. So
$$v_i(y^2 - x^3) = \min(2 \beta_i, 3 \alpha_i) = v_i\big((y^2, x^3)\big),$$
and the values are $2$, $3$ and $6$. The difference between the two problems is the factor that is left. For the ideal it is the unit ideal. For the cusp it is the ideal of the strict transform $C_3$, which meets $E_3$ at a point that lies on neither $E_1$ nor $E_2$. At this point the two terms of $y^2 - x^3$ have the same value of $v_3$, and they cancel. Volume 7 studies the Newton polyhedron, which is the general form of this remark.

*Remark (principal ideals).* For the principal ideal $I = (y^2 - x^3)$, Theorem 1.1.6 holds with the empty sequence, and Theorem 1.1.7 needs the three blowups of Example 1.3.2. Theorem 3.3.11 asks for more: the divisor $G$ with $\Pi^* I = \mathcal{O}(-G)$ is supported on exceptional divisors. A blowup with a center of codimension 1 is allowed in a blowup sequence, and its center becomes a new exceptional divisor. So the algorithm can end with the blowup of the smooth curve $C_3$, which is the identity of the surface and which moves $C_3$ into the divisor. In this sense the curve itself is part of the exceptional divisor at the end.

*Remark (positive characteristic).* The computations of this section use only the coefficients $\pm 1$ and the binomial formula for squares and cubes. They hold over every field, with one exception: in part (2) of Example 1.3.3 the pair of planes $x^2 - c y^2$ is a double plane in characteristic 2. For plane curves the embedded resolution by point blowups works in every characteristic [Har, Section V.3]. What fails in characteristic $p$ is not the resolution of these examples but the method of Chapter 2 for choosing the centers. In characteristic 2 the derivative of $y^2 - x^3$ with respect to $y$ is $0$, so the derivative ideal is $(y^2 - x^3, x^2)$ and it contains no element of order 1 at the origin. The curve $(y = 0)$, which is the curve of maximal contact in characteristic 0, is not visible in the derivative ideal. Section 2.4 gives the general form of this failure.

### Notes and references

The umbrella is an example of [Kol07, Chapter 3], Section "What is a good resolution algorithm?", where it shows that blowing up the worst singular point does not work. The cusp is a classical example; see also the survey [Hau03]. The resolution of plane curves by point blowups is classical; see [Har, Section V.3] and [Cut04]. For the failure of maximal contact in positive characteristic, see Section 2.4 and Volume 9, Section 2.2.
