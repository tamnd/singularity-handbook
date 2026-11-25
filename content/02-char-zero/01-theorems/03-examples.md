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

Lean: none yet

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

Lean: none yet

*Proof.* (1) The partial derivatives are $\partial_x f = 2x$, $\partial_y f = -2yz$ and $\partial_z f = -y^2$. They vanish together exactly when $x = 0$ and $y = 0$, and then $f = 0$. A point of $X$ is singular if and only if all partials vanish there, so $\operatorname{Sing}(X) = L$. At a point of $L$ all partials vanish, so the order is at least 2, and the second derivative $\partial_x^2 f = 2$ is a unit, so it is exactly 2.

(2) At the origin the homogeneous part of degree 2 of $f$ is $x^2$. At $(0, 0, c)$, write $z = c + t$. Then $f = x^2 - c y^2 - y^2 t$, and the part of degree 2 in $(x, y, t)$ is $x^2 - c y^2$.

(3) The blowup along $L = (x = y = 0)$ has two charts. In the chart $x = x_1 y$ the pullback of $f$ is $y^2 (x_1^2 - z)$. The exceptional divisor is $F = (y = 0)$ and the strict transform is $X_1 = (z = x_1^2)$, a graph, hence smooth. The differentials $dy$ and $dz - 2 x_1 dx_1$ are independent everywhere, so $X_1$ and $F$ meet transversally along the smooth curve $(y = 0, z = x_1^2)$. In the chart $y = y_1 x$ the pullback is $x^2 (1 - y_1^2 z)$. The strict transform $X_1 = (y_1^2 z = 1)$ is smooth, because on it $y_1 \ne 0$ and $z \ne 0$, so the partial derivative $2 y_1 z$ in $y_1$ is not zero. Its equation does not involve $x$, so it meets $F = (x = 0)$ transversally. Thus $X_1$ is smooth and $X_1 + F$ has simple normal crossings in the sense of Definition 1.1.2.

(4) Blow up the origin and take the chart $x = x_1 z$, $y = y_1 z$. The pullback of $f$ is $x_1^2 z^2 - y_1^2 z^3 = z^2 (x_1^2 - y_1^2 z)$. The strict transform is $(x_1^2 = y_1^2 z)$, the same equation as $X$. $\square$

The order of $f$ is 2 at every point of $L$, so the order alone does not see that the origin is a worse point than the others. Part (2) shows that the tangent cone does. A resolution algorithm that blows up the locus of maximal order would blow up $L$ here, which by part (3) is a good choice. If it chose the origin, it would by part (4) return to the same singularity, so the invariant that drives the algorithm must be finer than the order and must not be fooled by such a loop. In Chapter 3 the invariant is computed on a hypersurface of maximal contact. For the umbrella, Example 3.2.6 computes the coefficient ideal on $H = (x = 0)$ and finds its cosupport, which is again $L$.

### Notes and references

The cusp and the umbrella are examples of [Kol07, Chapter 3], Section "Examples of resolutions", and of [Hau03]. The resolution of plane curves by point blowups is classical; see [Har, Section V.3] and [Cut04]. For the failure of maximal contact in positive characteristic, see Section 2.4 and Volume 9, Section 2.2.
