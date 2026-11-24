---
title: The Newton criterion for z^p + g
nodes: [SG0000003G, SG0000003H]
sources: [Newt, Hau10, Cos87]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Newton criterion for $z^p + g$

In characteristic $0$, a hypersurface whose equation is Newton nondegenerate has an embedded resolution by one toric modification. This is the theorem of Varchenko and Khovanskii. In this section we find out exactly when the equation $f = z^p + g(x)$ is Newton nondegenerate in characteristic $p$. The answer is a statement about the critical points of the initial forms of $g$, not about their zero sets. The reason is simple: the derivative of $z^p$ in $z$ is $0$, so the variable $z$ does not help to make a point smooth, and $z$ can take each value that $g$ takes.

We use the notation of Section 1.2. Let $K$ be an algebraically closed field of characteristic $p > 0$, and let $g \in K[x_1, \dots, x_n]$ with $g(0) = 0$. For a weight $\omega \in \mathbb{R}_{>0}^n$, the minimum of $\langle \omega, \cdot \rangle$ on $N(g)$ is attained on a compact face $\sigma$ of $N(g)$, and each compact face comes from some weight. The initial form $g_\sigma = \operatorname{in}_\omega(g)$ is the sum of the terms of $g$ whose exponents lie on $\sigma$. The *torus* is $T = (K^*)^n$, the set of points with no coordinate equal to $0$. A *torus critical point* of a polynomial $h$ is a point $v \in T$ with $\partial_1 h(v) = \cdots = \partial_n h(v) = 0$.

**Definition 3.3.1.** A polynomial $F$ in $m$ variables is *Newton nondegenerate* if, for each compact face $\tau$ of $N(F)$, the hypersurface $F_\tau = 0$ has no singular point in the torus $(K^*)^m$. That is, the equations $F_\tau = \partial_1 F_\tau = \cdots = \partial_m F_\tau = 0$ have no common solution in the torus.

This is the condition for toric resolution. A stronger condition asks that $F_\tau$ have no torus critical point at all, and it is the condition for Milnor numbers. In characteristic $0$ the two conditions agree, because the Euler identity $D \cdot F_\tau = \sum_i \omega_i x_i \partial_i F_\tau$ puts each critical point on the zero set. In characteristic $p$ the integer $D$ can be $0$ in $K$, and the two conditions differ.

### The faces of $N(z^p + g)$

Let $f = z^p + g$, a polynomial in the $n + 1$ variables $(x, z)$.

**Lemma 3.3.2.** The compact faces of $N(f)$ are of three kinds:

1. the vertex $p e_z$, with the initial form $z^p$;
2. the faces $\sigma \times \{0\}$, with the initial form $g_\sigma$, for each compact face $\sigma$ of $N(g)$;
3. the faces $\operatorname{conv}(\sigma \times \{0\}, p e_z)$, with the initial form $z^p + g_\sigma$, for each compact face $\sigma$ of $N(g)$.

*Proof.* A compact face of $N(f)$ comes from a weight $(\omega, \omega_z)$ with $\omega \in \mathbb{R}_{>0}^n$ and $\omega_z > 0$. The monomial $z^p$ has the weight $p \omega_z$. The terms of $g$ have the smallest weight $m = \min_{N(g)} \langle \omega, \cdot \rangle$ exactly on the face $\sigma$ of $N(g)$ for $\omega$. If $p \omega_z < m$, the initial form is $z^p$. If $p \omega_z > m$, it is $g_\sigma$. If $p \omega_z = m$, it is $z^p + g_\sigma$. For a given $\sigma$ we can choose $\omega_z$ freely, so each case occurs for each $\sigma$. $\square$

### The criterion

**Theorem 3.3.3.** The polynomial $f = z^p + g$ is Newton nondegenerate if and only if, for each compact face $\sigma$ of $N(g)$, the initial form $g_\sigma$ has no critical point in the torus $T$.

Node: SG0000003G · Lean: `Singularity.isSingularPoint_purelyInseparable_iff`, `Singularity.exists_torus_isCriticalPoint_iff` (for one face)

*Proof.* We examine the three kinds of faces of Lemma 3.3.2.

The vertex $z^p$ does not vanish on the torus of $(x, z)$, so it gives no condition.

On a face of the second kind, the initial form $g_\sigma$ does not contain $z$. A singular point of $g_\sigma = 0$ in the torus is a point $(v, c)$ with $v \in T$, $c \ne 0$, $g_\sigma(v) = 0$ and $\nabla g_\sigma(v) = 0$. So this kind of face asks that $g_\sigma$ have no torus critical point on its zero set.

On a face of the third kind, the initial form is $F = z^p + g_\sigma$. Its partial derivatives are $\partial_i F = \partial_i g_\sigma$ and $\partial_z F = p z^{p-1} = 0$. So a singular point of $F = 0$ in the torus is a point $(v, c)$ with $v \in T$, $c \ne 0$, $\nabla g_\sigma(v) = 0$ and $c^p = -g_\sigma(v)$. Let $v$ be a torus critical point of $g_\sigma$ with $g_\sigma(v) \ne 0$. Since $K$ is algebraically closed, $-g_\sigma(v)$ has a $p$-th root $c$, and $c \ne 0$. So $(v, c)$ is a singular point. Conversely, a singular point $(v, c)$ gives a torus critical point $v$ with $g_\sigma(v) = -c^p \ne 0$. So this kind of face asks that $g_\sigma$ have no torus critical point off its zero set.

The faces of the second and third kinds together ask that $g_\sigma$ have no torus critical point. $\square$

The heart of the proof is the third kind of face. It is the statement: $z^p + h$ is singular at a point $(v, c)$ of the torus if and only if $v$ is a critical point of $h$ and $c^p = -h(v)$. In this form the statement holds for each polynomial $h$, and the Lean library proves it in this form.

Compare the equation $z^m + g$ with $m$ invertible in $K$, for example in characteristic $0$. There $\partial_z F = m z^{m-1}$ does not vanish on the torus, so the faces of the third kind give no condition, and the criterion is the classical one: each $g_\sigma = 0$ is smooth in the torus. In characteristic $p$ the zero set of $g_\sigma$ has no special role. The variable $z$ absorbs each critical value.

**Corollary 3.3.4.** Let $\Theta_{\mathrm{all}}(h) = (x_1 \partial_1 h, \dots, x_n \partial_n h)$ be the log-Jacobian ideal of Section 3.1 for $\Delta = \{1, \dots, n\}$. Then $z^p + g$ is Newton nondegenerate if and only if $V(\Theta_{\mathrm{all}}(g_\sigma)) \cap T = \emptyset$ for each compact face $\sigma$ of $N(g)$.

*Proof.* On the torus each $x_i$ is a unit, so $x_i \partial_i h(v) = 0$ if and only if $\partial_i h(v) = 0$. Apply Theorem 3.3.3. $\square$

So the Newton nondegeneracy of $z^p + g$ is a statement about the ideal $\Theta$, face by face. Newton theory treats each coordinate hyperplane as a part of the boundary. This is why the ideal for the full set $\Delta = \{1, \dots, n\}$ appears.

**Corollary 3.3.5.** If a vertex $a$ of $N(g)$ lies in $p \mathbb{N}^n$, then $z^p + g$ is Newton degenerate.

Node: SG0000003G · Lean: `Singularity.isCriticalPoint_monomial_of_dvd`, `Singularity.exists_torus_isSingularPoint_purelyInseparable_initialForm`

*Proof.* The vertex is a compact face, with the initial form $c_a x^a$. Each partial derivative of $x^a$ is $0$, because each exponent is divisible by $p$. So each point of $T$ is a critical point of $c_a x^a$. $\square$

The change of variable $z \mapsto z + h$ replaces $g$ by $g + h^p$. It can remove the monomials that are $p$-th powers, and so it changes $N(g)$. The corollary says that this cleaning (Lemma 1.3.2) must come before each Newton test.

### A mod $p$ Euler identity

Since $K$ is perfect, each polynomial $h$ has exactly one decomposition
$$h = \sum_{c \in \{0, \dots, p-1\}^n} x^c u_c^p, \qquad u_c \in K[x].$$
The term $x^c u_c^p$ collects the monomials of $h$ whose exponent is congruent to $c$ modulo $p$. Let $S(h) = \{ c : u_c \ne 0 \}$ be the set of *residue classes* of $h$. If $h$ is clean, then $0 \notin S(h)$. Each $\partial_i$ is $K[x^p]$-linear, and $x_i \partial_i x^c = c_i x^c$, so
$$x_i \partial_i h = \sum_c c_i \, x^c u_c^p.$$
The generators of $\Theta_{\mathrm{all}}(h)$ are thus $n$ linear combinations of the pieces $x^c u_c^p$, with coefficients in $\mathbb{F}_p$.

**Proposition 3.3.6.** Let $h$ be a polynomial. Assume that there is $w \in \mathbb{F}_p^n$ such that $\langle w, c \rangle = 1$ in $\mathbb{F}_p$ for each $c \in S(h)$. Then
$$h = \sum_{i=1}^n w_i \, x_i \partial_i h.$$
In particular, $h \in \Theta_{\mathrm{all}}(h)$, and each torus critical point of $h$ lies on the zero set of $h$.

Node: SG0000003H · Lean: `Singularity.eq_sum_smul_X_mul_pderiv`, `Singularity.eval_eq_zero_of_isCriticalPoint_of_eq_sum`

*Proof.* By the formula above, $\sum_i w_i x_i \partial_i h = \sum_c \langle w, c \rangle x^c u_c^p = \sum_c x^c u_c^p = h$. At a torus critical point each $x_i \partial_i h$ is $0$, so $h$ is $0$. $\square$

The hypothesis excludes $0 \in S(h)$, because $\langle w, 0 \rangle = 0$. The proposition needs no homogeneity. The Lean library states it monomial by monomial: if $\sum_i w_i a_i = 1$ in $K$ for each exponent $a$ of $h$, then $h = \sum_i w_i x_i \partial_i h$.

**Corollary 3.3.7.** Let $\sigma$ be a compact face of $N(g)$, and let $\omega \in \mathbb{Z}_{>0}^n$ be an integral weight for $\sigma$, with the value $D = \min_{N(g)} \langle \omega, \cdot \rangle$. If $p \nmid D$, then each torus critical point of $g_\sigma$ lies on the zero set of $g_\sigma$. For this face, the condition of Theorem 3.3.3 is then the classical condition that $g_\sigma = 0$ is smooth in $T$.

Node: SG0000003H · Lean: `Singularity.eq_inv_smul_sum_X_mul_pderiv`, `Singularity.eval_eq_zero_of_isCriticalPoint_of_isWeightedHomogeneous`

*Proof.* Each exponent $a$ of $g_\sigma$ has $\langle \omega, a \rangle = D$. Reduce modulo $p$ and multiply by the inverse of $D$ in $\mathbb{F}_p$. The vector $w = D^{-1} \omega \bmod p$ satisfies $\langle w, a \rangle = 1$ for each exponent $a$ of $g_\sigma$, so it satisfies the hypothesis of Proposition 3.3.6. $\square$

**Definition 3.3.8.** A compact face $\sigma$ of $N(g)$ is *resonant* if there is no $w \in \mathbb{F}_p^n$ with $\langle w, c \rangle = 1$ for each $c \in S(g_\sigma)$.

Node: SG0000003H · Lean: `Singularity.IsResonant`, `Singularity.eval_eq_zero_of_isCriticalPoint_of_not_isResonant`

Resonance is a question of linear algebra over $\mathbb{F}_p$, so a computer can decide it. By Corollary 3.3.7, a resonant face has $p \mid D$ for each integral weight of the face. The converse is false. For $p = 2$ and the edge $x^3 y + x y^3$, the value is $D = 4$ for the weight $(1, 1)$, but $S = \{(1, 1)\}$ and $w = (1, 0)$ satisfies the condition. So this face is not resonant. By Proposition 3.3.6, the failures of nondegeneracy that are special to characteristic $p$, the torus critical points off the zero set, occur only on resonant faces.

### Examples

**Example 3.3.9.** Let $p = 3$ and $g = x^2 y + x y^2 = x y (x + y)$. The zero set of $g$ is three distinct lines, so it is smooth in the torus, and the classical condition holds. The residue classes are $S = \{(2, 1), (1, 2)\}$. The equations $2 w_1 + w_2 = 1$ and $w_1 + 2 w_2 = 1$ give $w_1 = w_2$ and $3 w_1 = 1$. The second equation has no solution in $\mathbb{F}_3$, so the edge is resonant. The partial derivatives are $\partial_x g = y (2x + y) = y (y - x)$ and $\partial_y g = x (x - y)$. They vanish together on the line $x = y$, where $g(s, s) = 2 s^3 \ne 0$. By Theorem 3.3.3, $z^3 + g$ is Newton degenerate. In fact, it is singular along the curve $(s, s, s)$: the value is $s^3 + s^3 + s^3 = 0$, and the gradient $(3 s^2, 3 s^2, 3 s^2)$ is $0$.

**Example 3.3.10.** Let $p = 2$ and $g = w x + w y + x y$ in three variables $w, x, y$. The face is the triangle with the vertices $(1, 1, 0)$, $(1, 0, 1)$ and $(0, 1, 1)$. A vector $v \in \mathbb{F}_2^3$ for Definition 3.3.8 must satisfy $v_1 + v_2 = v_1 + v_3 = v_2 + v_3 = 1$. The sum of the three equations gives $0 = 1$ in $\mathbb{F}_2$, so the triangle is resonant. The partial derivatives are $x + y$, $w + y$ and $w + x$. They vanish together on the line $w = x = y$, where $g = 3 s^2 = s^2 \ne 0$. So $z^2 + g$ is singular along the curve $(s, s, s, s)$.

**Example 3.3.11.** Let $p = 2$ and $g = x^3 y + x y^3 = x y (x + y)^2$. This is the example of Hauser that produces a kangaroo point [Hau10]. The face is not resonant: $S = \{(1, 1)\}$ and $w = (1, 0)$ works, and indeed $x \partial_x g = x^3 y + x y^3 = g$. So each torus critical point lies on $g = 0$. The partial derivatives are $\partial_x g = y (x + y)^2$ and $\partial_y g = x (x + y)^2$, so the torus critical points form the line $x = y$, where $g$ has the double factor $(x + y)^2$. Here the degeneracy is the classical one: the zero set of $g$ is not reduced along $x = y$. The line $x = y$ is also the direction of the translation that produces the kangaroo point.

### Notes and references

The toric resolution of Newton nondegenerate hypersurfaces is due to Varchenko and Khovanskii in characteristic $0$. Its proof uses only toric geometry, so it works for the nondegeneracy of Definition 3.3.1 in each characteristic. So an equation $z^p + g$ that satisfies Theorem 3.3.3 after a change of coordinates and a cleaning has an embedded resolution by one toric modification, in each dimension. The examples show that a change of the coordinates $x$ can be necessary. It is not known which resonant faces a change of coordinates can remove. A precise form of this question is in the research notes of the project. For the kangaroo phenomenon, see [Hau10].
