---
title: The Newton criterion for z^p + g
nodes: [SG0000003G, SG0000003H, SG0000008P, SG0000008Q, SG0000008R, SG0000008S, SG0000008T, SG0000008V, SG0000008W, SG0000008X, SG0000008Y, SG0000008Z, SG00000097, SG00000098, SG00000099, SG0000009A, SG0000009B, SG0000009C, SG0000009D, SG0000009E]
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

### The weight form over a perfect field

Theorem 3.3.3 is a statement over an algebraically closed field, and it uses the faces of $N(g)$. For a proof in Lean and for the computations over finite fields, a form with weights and with points over a smaller field is better. In this subsection $K$ is a field of characteristic $p$, not necessarily algebraically closed. For a weight $W$ with positive integer entries, let $m_W(F)$ be the smallest weight of a monomial of $F$, and let $\operatorname{in}_W F$ be the sum of the terms of $F$ of weight $m_W(F)$.

**Definition 3.3.12.** A polynomial $F$ in $m$ variables over $K$ is *Newton nondegenerate over $K$* if, for each $W \in \mathbb{Z}_{>0}^m$, the hypersurface $\operatorname{in}_W F = 0$ has no singular point in $(K^*)^m$.

Lean: `Singularity.NewtonNondegenerate`

Each positive weight selects a compact face of $N(F)$, and each compact face comes from a positive integer weight, with $\operatorname{in}_W F = F_\tau$. So for an algebraically closed $K$, Definition 3.3.12 is Definition 3.3.1. The weights avoid the convex geometry of the faces.

**Theorem 3.3.13.** Let $K$ be a perfect field of characteristic $p$, and let $g \in K[x_1, \dots, x_n]$ with $g \ne 0$ and $g(0) = 0$. Then $z^p + g$ is Newton nondegenerate over $K$ if and only if, for each $w \in \mathbb{Z}_{>0}^n$, the initial form $\operatorname{in}_w g$ has no critical point in $(K^*)^n$.

Node: SG0000008P · Lean: `Singularity.newtonNondegenerate_purelyInseparable_iff`

*Proof.* Write a weight of the $n + 1$ variables as $W = (w, c)$, with $c$ the weight of $z$, and let $m = m_w(g)$. As in the proof of Lemma 3.3.2, $\operatorname{in}_W(z^p + g)$ is $z^p$ if $pc < m$, it is $\operatorname{in}_w g$ if $pc > m$, and it is $z^p + \operatorname{in}_w g$ if $pc = m$.

Assume that no $\operatorname{in}_w g$ has a torus critical point, and let $(v, c_0)$ be a torus point. The form $z^p$ is not $0$ at $(v, c_0)$. The form $\operatorname{in}_w g$ does not contain $z$, so a singular point $(v, c_0)$ of it gives a critical point $v$ of $\operatorname{in}_w g$. The form $z^p + \operatorname{in}_w g$ has the derivative $0$ in $z$, so a singular point $(v, c_0)$ of it also gives a critical point $v$ of $\operatorname{in}_w g$. So no initial form has a singular point in the torus.

Conversely, let $v \in (K^*)^n$ be a critical point of $\operatorname{in}_w g$ for some $w > 0$. If $\operatorname{in}_w g(v) = 0$, take $W = (w, m + 1)$. Then $p(m + 1) > m$, so $\operatorname{in}_W(z^p + g) = \operatorname{in}_w g$, and $(v, 1)$ is a singular point. If $\operatorname{in}_w g(v) \ne 0$, take $W = (pw, m)$. Since $g(0) = 0$ and $w > 0$, $m \ge 1$, so $W > 0$. The weight $pw$ has the same initial form as $w$ and the value $pm$, so $\operatorname{in}_W(z^p + g) = z^p + \operatorname{in}_w g$. Since $K$ is perfect, $-\operatorname{in}_w g(v)$ has a $p$-th root $c_0 \ne 0$, and $(v, c_0)$ is a singular point. $\square$

The Lean theorem holds for each perfect reduced ring $K$ of characteristic $p$. The direction from the right side to the left side does not use that $K$ is perfect (`Singularity.newtonNondegenerate_purelyInseparable_of_forall`). The two hypotheses on $g$ are necessary. For $g = 0$ the right side fails and $z^p$ is nondegenerate. For $g = 1$ each point is critical for $\operatorname{in}_w g = 1$, but $z^p + 1$ has the initial form $1$ for each $W$. The proof uses the integer weight $(pw, m)$ in the place of the rational weight $m/p$ of $z$. The step from Definition 3.3.12 to the faces of $N(F)$ is not in Lean.

**Example 3.3.14 (the field must be perfect).** Let $K = \mathbb{F}_p(t)$, $n = 1$ and $g = t x^p$. Each initial form of $g$ is $t x^p$, and $\partial_x(t x^p) = 0$, so each point of $K^*$ is a critical point. But $z^p + t x^p$ is Newton nondegenerate over $K$. Its initial forms are $z^p$ and $t x^p$, which have no zero in $(K^*)^2$, and $z^p + t x^p$. A zero of the last one in the torus needs $(z/x)^p = -t$, and $-t$ is not a $p$-th power in $K$. So the right side of Theorem 3.3.13 fails and the left side holds. Over an algebraic closure of $K$ the polynomial is degenerate, as Theorem 3.3.3 says.

Node: SG0000008Q · Lean: `Singularity.newtonNondegenerate_ratFunc_example`

### Preparation and its obstruction

Theorem 3.3.3 is a test in fixed coordinates. Example 3.3.9 shows that the test can fail although the zero set of $g$ is smooth in the torus. The natural question is whether a change of coordinates makes the equation nondegenerate. If it does, the toric resolution of Theorem 3.3.40 below resolves the hypersurface. This would be a direct method for $z^p + g$ in each dimension. In this subsection the answer is no for a large class of $g$, and for each kind of change of coordinates when the degree of $g$ is more than $p$. The subsection on the case $D = p$ gives the same answer for many $g$ of degree $p$. Here $k$ is an algebraically closed field of characteristic $p$, and $g \in k[[x_1, \dots, x_n]]$ is a series. Definition 3.3.1 applies to a series, since the initial form of a series for a positive weight is a polynomial.

**Definition 3.3.15.** A *change $(\varphi, q)$* is an automorphism $\varphi$ of $k[[x]]$ together with a series $q \in k[[x]]$. It sends $z^p + g$ to $z^p + g \circ \varphi + q^p$, that is, $x \mapsto \varphi(x)$ and $z \mapsto z + q$. A *change of all coordinates* is an automorphism $\Psi$ of $k[[x, z]]$ together with a unit $u$ of $k[[x, z]]$. It sends $F$ to $u \cdot (F \circ \Psi)$.

The changes $(\varphi, q)$ include the linear changes of $x$ and the cleaning of Lemma 1.3.2. For a unit $u$ and a weight $W > 0$, $\operatorname{in}_W(u F) = u(0) \operatorname{in}_W F$, so a unit does not change Newton nondegeneracy. A change of all coordinates can mix $z$ into the new $x$, and then the equation does not have the form $z^p + G(x)$.

Let $D = \operatorname{ord} g$, let $h$ be the form of degree $D$ of $g$, and assume $\nabla h \ne 0$. The *projective critical set* of $h$ is $C = V(\partial_1 h, \dots, \partial_n h) \subset \mathbb{P}^{n-1}$. Since $\nabla h$ is homogeneous, each point of $C$ off the coordinate hyperplanes gives a line of torus critical points of $h$.

**Theorem 3.3.16.** Assume that $C$ is not contained in the union of $n$ hyperplanes with linearly independent equations. Then for each change $(\varphi, q)$ and each unit $u$, the series $u \cdot (z^p + g \circ \varphi + q^p)$ is Newton degenerate. Its initial form for the weight $(1, \dots, 1)$ has a torus critical point.

Node: SG0000008R · Lean: none yet

*Proof.* Let $A$ be the linear part of $\varphi$. It is invertible, so $g \circ \varphi$ has order $D$ and the form $h \circ A$ of degree $D$. Let $G = g \circ \varphi + q^p$, let $e = \operatorname{ord} q$, and let $q_e$ be the form of degree $e$ of $q$. If $pe < D$, the initial form of $G$ for $(1, \dots, 1)$ is $q_e^p$, and each point is a critical point of it. If $pe > D$, the initial form is $h \circ A$. If $pe = D$, it is $h \circ A + q_e^p$. In the last two cases its gradient is $A^t \, (\nabla h) \circ A$, and its projective critical set is $A^{-1} C$. If $A^{-1} C$ were in the union of the coordinate hyperplanes, then $C$ would be in the union of the hyperplanes $\ell_i = 0$, with $\ell_i(x) = (A^{-1} x)_i$, and these forms are linearly independent. So $A^{-1} C$ has a point off the coordinate hyperplanes, and this point gives a torus critical point of the initial form. In each case the proof of Theorem 3.3.13, applied to the weight $(1, \dots, 1)$, shows that $z^p + G$ is degenerate. The proof is the same for a series. $\square$

The theorem does not need $h$ resonant. But if $h$ is not resonant, each torus critical point lies on $h = 0$ by Corollary 3.3.7, and the degeneracy is the classical one. If $p \nmid D$, then $h$ is not resonant. So the case of interest is $p \mid D$.

**Theorem 3.3.17.** Assume $D > p$ and that $C$ is not contained in the union of $n$ hyperplanes with linearly independent equations. Let $F = z^p + g$. Then for each automorphism $\Psi$ of $k[[x, z]]$ and each unit $u$, the series $u \cdot (F \circ \Psi)$ is Newton degenerate.

Node: SG0000008S · Lean: none yet

*Proof.* We can take $u = 1$. Let $F' = F \circ \Psi = \zeta^p + g(\varphi)$, with $\zeta = \Psi^* z$ and $\varphi = \Psi^* x$, series in new variables $y_1, \dots, y_{n+1}$.

Step 1. Let $\ell \ne 0$ be the linear part of $\zeta$. The form of degree $p$ of $F'$ is $\ell^p$, because $\zeta^p - \ell^p$ has order at least $2p$ and $g(\varphi)$ has order $D > p$. If $\ell$ has two nonzero coefficients, the zero set of $\ell^p$ meets the torus, and each of its points is singular, because $\nabla(\ell^p) = 0$. So $F'$ is degenerate for the weight $(1, \dots, 1)$. Otherwise $\ell = \lambda y_j$ for one $j$. Call this variable $Z$ and the other variables $X = (X_1, \dots, X_n)$. Write $\zeta = \lambda Z + q(X, Z)$ with $\operatorname{ord} q \ge 2$, and $\varphi_i = (A X)_i + b_i Z + (\text{terms of order at least } 2)$. The linear part of $\Psi$ is block triangular with the diagonal blocks $A$ and $\lambda$, so $A$ is invertible. In characteristic $p$, $F' = \lambda^p Z^p + q(X, Z)^p + g(\varphi(X, Z))$. Let $e \ge 2$ be the order of $q(X, 0)$, possibly infinite, and let $q_e$ be its form of degree $e$.

Step 2, the case $pe < D$. Take $W_1 = (1, \dots, 1, e)$, with the weight $e$ for $Z$. A monomial $Z^j X^a$ of $q$ with $j \ge 1$ has the weight $je + |a| > e$, so $\operatorname{in}_{W_1}(q^p) = q_e^p$, of weight $pe$. Each $\varphi_i$ has the initial form $(A X)_i$, so $g(\varphi)$ has the $W_1$-order $D > pe$. So $\operatorname{in}_{W_1} F' = (\lambda Z + q_e(X))^p$. For a torus point $v$ with $q_e(v) \ne 0$ and $c = -q_e(v)/\lambda$, the torus point $(v, c)$ is a singular point of this initial form.

Step 3, the case $pe \ge D$. Take $W = (p, \dots, p, D)$. Each $\varphi_i$ has the initial form $(A X)_i$, so $\operatorname{in}_W g(\varphi) = h(A X)$, of weight $pD$. A monomial $Z^j X^a$ of $q$ with $j \ge 1$ has the weight at least $D + p$, so its $p$-th power has a weight more than $pD$. A monomial $X^a$ of $q$ has $|a| \ge e$, so its $p$-th power has the weight $p^2 |a| \ge pD$, with equality only if $pe = D$ and $|a| = e$. So $\operatorname{in}_W F' = \lambda^p Z^p + H(X)$ with $H = h \circ A + \varepsilon q_e^p$ and $\varepsilon \in \{0, 1\}$. The gradient of $H$ is $A^t \, (\nabla h) \circ A$, and as in the proof of Theorem 3.3.16 the hypothesis on $C$ gives a torus point $v$ with $\nabla H(v) = 0$. If $H(v) \ne 0$, choose $c$ with $\lambda^p c^p = -H(v)$. Then $(v, c)$ is a torus singular point of $\operatorname{in}_W F'$. If $H(v) = 0$, take $W'' = (p, \dots, p, D + 1)$. The same count gives $\operatorname{in}_{W''} F' = H(X)$, and $(v, 1)$ is a torus singular point of it. So in each case $F'$ is Newton degenerate. $\square$

The hypothesis $D > p$ is used only in Step 1, to show that the form of degree $p$ of $F'$ is a $p$-th power.

### Two variables

For $n = 2$ the hyperplanes of $\mathbb{P}^1$ are points, so the hypothesis of Theorems 3.3.16 and 3.3.17 says that $C$ has at least three points.

**Proposition 3.3.18.** Let $n = 2$, and let $h \in k[x, y]$ be a form of degree $D$ with $p \mid D$ and $\nabla h \ne 0$. Then there is a unique form $G$ of degree $D - 2$ with $\partial_x h = y G$ and $\partial_y h = -x G$, and $C = V(G) \subset \mathbb{P}^1$. The following are equivalent.

1. $G$ has at most two distinct roots in $\mathbb{P}^1$.
2. A linear change of $x, y$ and a cleaning make $\operatorname{in}_{(1,1)}$ free of torus critical points.
3. A change $(\varphi, q)$ makes $\operatorname{in}_{(1,1)}$ free of torus critical points.

Lean: none yet

*Proof.* The Euler identity gives $x \partial_x h + y \partial_y h = D h = 0$. Since $x$ and $y$ are coprime in the factorial ring $k[x, y]$, $y \mid \partial_x h$. Write $\partial_x h = y G$. Then $\partial_y h = -x G$. The common zeros in $\mathbb{P}^1$ of $y G$ and $x G$ are the zeros of $G$. If $G$ has at most two roots, an element of $\mathrm{PGL}_2$ moves them to $(1 : 0)$ and $(0 : 1)$. Then the critical set of $h \circ A$ is on $xy = 0$, and a cleaning does not change the gradient. So 1 gives 2. Clearly 2 gives 3. Theorem 3.3.16 shows that 3 gives 1. $\square$

For $D = p$ the form $G$ has degree $p - 2$. For $p = 3$ each such form satisfies 1. For $p \ge 5$ a general form $h$ does not, because the map $h \mapsto G$ is linear and onto the forms of degree $p - 2$.

**Example 3.3.19.** Let $p = 3$ and $g = x^5 y + x y^5$, of degree $D = 6$. In characteristic $3$, $\partial_x g = 5 x^4 y + y^5 = y (y^4 - x^4)$, so $G = y^4 - x^4$. Its roots are the four points $(1 : \zeta)$ with $\zeta^4 = 1$, and they are distinct because $3 \nmid 4$. At these points $g(1, \zeta) = \zeta + \zeta^5 = 2 \zeta \ne 0$. The residue classes are $(2, 1)$ and $(1, 2)$, so $g$ is resonant, as in Example 3.3.9. The zero set $xy(x^4 + y^4) = 0$ is smooth in the torus, so $g$ is nondegenerate in the classical sense. Four points of $\mathbb{P}^1$ are not in the union of two points, and $D = 6 > 3$. By Theorem 3.3.17, no change of all coordinates and no unit makes $z^3 + x^5 y + x y^5 + (\text{terms of order at least } 7)$ Newton nondegenerate. More generally, for an odd $p$, $p \mid D$ and $D \ge 2p$, the same holds for $z^p + x^{D-1} y + x y^{D-1}$, whose form $G = y^{D-2} - x^{D-2}$ has $D - 2$ roots.

For weights other than $(1, 1)$ the changes must keep the weight. Let $w = (1, m)$ with $m \ge 2$, and let $h$ be weighted homogeneous of degree $D$ for $w$, with $\nabla h \ne 0$. The changes that keep $w$ are $x \mapsto \alpha x$ and $y \mapsto \beta y + \gamma x^m$. They act on the coordinate $s = y / x^m$ by $s \mapsto (\beta s + \gamma)/\alpha^m$.

**Proposition 3.3.20.** Let $Z_0 \subset \mathbb{A}^1$ be the set of the values of $s$ at the critical points of $h$ with $x \ne 0$. Then a change that keeps $w$ makes $h$ free of torus critical points if and only if $|Z_0| \le 1$. If $p \mid D$ and $h$ is clean, then $0 \in Z_0$ if and only if $h$ has no monomial $x^{D-m} y$.

Node: SG0000008T · Lean: none yet

*Proof.* The torus critical points of $h$ are a finite union of orbits of $t \mapsto (t v_1, t^m v_2)$, and each orbit is a value $s \ne 0$. The value $s = 0$ is a critical point on the axis $y = 0$, which is not in the torus. The affine maps of $s$ fix $s = \infty$, the axis $x = 0$. A change prepares $h$ if and only if it maps $Z_0$ into $\{0\}$, and an affine map does this if and only if $|Z_0| \le 1$. Then $y \mapsto \beta y + \gamma x^m$ moves the point to $s = 0$. For the last claim, write $h = \sum_j c_j x^{D - mj} y^j$. On $y = 0$, $\partial_y h = c_1 x^{D-m}$ and $\partial_x h = D c_0 x^{D-1} = 0$. $\square$

The set $Z_0$ can contain the point $s = 0$, which is not in the torus. A change $y \mapsto \beta y + \gamma x^m$ with $\gamma \ne 0$ moves this point into the torus. So it is not sufficient that $h$ has at most one orbit of torus critical points.

**Example 3.3.21.** Let $p = 3$, $w = (1, 2)$ and $h = x^4 y^4 + x^2 y^5 = x^2 y^4 (x^2 + y)$, of degree $12$. The residue classes are $(1, 1)$ and $(2, 2)$, so $h$ is resonant. Write $h = x^{12} \phi(s)$ with $\phi(s) = s^4 + s^5$. Then $\phi'(s) = s^3 (1 + 2s)$. The torus critical points are the orbit $s = 1$, that is $y = x^2$, where $h = 2 x^{12} \ne 0$. The axis $y = 0$ is also critical, so $Z_0 = \{0, 1\}$, and no change that keeps $w$ prepares $h$. The research notes check this for all the changes that keep $w$ over $\mathbb{F}_3$, by computer.

Node: SG0000008T · Lean: none yet

### Three variables and the Fano plane

In three variables the critical set can have a rigid structure that comes from the Frobenius map. Let $p = 2$ and $n = 3$. Each clean quartic form can be written $h = x_1 x_2 L_3^2 + x_1 x_3 L_2^2 + x_2 x_3 L_1^2$ with linear forms $L_1$, $L_2$, $L_3$, because an exponent of degree $4$ that is not in $2 \mathbb{N}^3$ has exactly two odd entries. The derivatives are $\partial_1 h = x_2 L_3^2 + x_3 L_2^2$, $\partial_2 h = x_1 L_3^2 + x_3 L_1^2$ and $\partial_3 h = x_1 L_2^2 + x_2 L_1^2$. Let $\Phi(x) = (L_1(x)^2, L_2(x)^2, L_3(x)^2)$. At a fixed point of $\Phi$ each derivative is a sum of two equal terms, so each fixed point is a critical point, and there $h = 3 x_1 x_2 x_3 = x_1 x_2 x_3$.

**Theorem 3.3.22.** Assume that $L_1$, $L_2$ and $L_3$ are linearly independent. Then $C$ contains the seven points of a Fano plane, and it is not contained in the union of three lines with independent equations. So for each $g \in k[[x_1, x_2, x_3]]$ with the lowest form $h$, no automorphism of $k[[x, z]]$ and no unit makes $z^2 + g$ Newton nondegenerate. Also $h$ has a torus critical point where $h \ne 0$.

Node: SG0000008Y · Lean: none yet

*Proof.* The map $\Phi$ is the composite of the invertible linear map $x \mapsto (L_1(x), L_2(x), L_3(x))$ and the coordinatewise square. So $\Phi$ is a bijective additive map of $k^3$ with $\Phi(\lambda x) = \lambda^2 \Phi(x)$. By Lang's theorem, in the form for a bijective Frobenius semilinear map of a finite dimensional vector space over an algebraically closed field, the fixed points form an $\mathbb{F}_2$-structure $V_0$ of $k^3$, that is, $V_0 \otimes_{\mathbb{F}_2} k = k^3$. The seven nonzero vectors of $V_0$ give seven points of $\mathbb{P}^2$ in $C$. Vectors of $V_0$ that are independent over $\mathbb{F}_2$ stay independent over $k$, so three of these points are on a line of $\mathbb{P}^2(k)$ only if they are on a line of $\mathbb{P}(V_0)$. So they form a Fano plane, with seven lines of three points, and each other line of $\mathbb{P}^2$ contains at most one of them. Three lines with independent equations meet in pairs in three distinct points. Three Fano lines that do not meet in one point cover $3 + 3 + 3 - 3 = 6$ points, two Fano lines and another line cover at most $3 + 3 - 1 + 1 = 6$ points, and fewer Fano lines cover at most $5$ points. So the seven points are not covered. Theorem 3.3.16 gives the changes $(\varphi, q)$, and Theorem 3.3.17 gives all changes of coordinates, since $D = 4 > 2 = p$. The coordinate lines are three lines with independent equations, so one of the seven points is in the torus, and there $h = x_1 x_2 x_3 \ne 0$. $\square$

**Example 3.3.23.** Let $p = 2$ and $h = x y w (x + y + w) = x y \cdot w^2 + x w \cdot y^2 + y w \cdot x^2$, so $L_1 = x$, $L_2 = y$ and $L_3 = w$ are independent. Here $\Phi(x, y, w) = (x^2, y^2, w^2)$, and its fixed points are $\mathbb{F}_2^3$. The derivatives are $\partial_x h = y w (y + w)$, $\partial_y h = x w (x + w)$ and $\partial_w h = x y (x + y)$, and a direct check shows $C = \mathbb{P}^2(\mathbb{F}_2)$. At $(1, 1, 1)$, $h = 1 \ne 0$. In the torus the zero set of $h$ is $x + y + w = 0$, where $\partial_x h = x y w \ne 0$, so $h$ is nondegenerate in the classical sense. The edges such as $x^2 y w + x y^2 w$ and the vertices are nondegenerate, and only the whole triangle is degenerate. By Theorem 3.3.22, $z^2 + x y w (x + y + w) + (\text{terms of order at least } 5)$ is Newton degenerate after each change of all coordinates.

For $p = 2$ and a quadratic form, and for $p = 3$ and a cubic form in three variables, the research notes show that the critical set is always covered by three independent lines. So Theorem 3.3.16 gives no obstruction in these cases.

### The case $D = p$

When $D = p$, the form of degree $p$ of $F = z^p + g$ is $z^p + h$, which is not a $p$-th power, and Step 1 of the proof of Theorem 3.3.17 fails. Let $Q = \{z^p + h = 0\} \subset \mathbb{P}^n$ and $O = (0 : \dots : 0 : 1)$, so $O \notin Q$. Since $\partial_z (z^p + h) = 0$, the singular points of $Q$ are the points $S_v = (v : c_v)$ with $v \in C$ and $c_v^p = -h(v)$. The root $c_v$ is unique, so $v \mapsto S_v$ is a bijection from $C$ onto the singular locus of $Q$. For $n = 2$ and three points of $C$ these are three points of $\mathbb{P}^2$. If they are not on one line, a linear change of $(x, y, z)$ moves them to the coordinate points, and then the face of the weight $(1, 1, 1)$ has no torus singular point. So the argument of Theorem 3.3.16 does not apply to the changes of all coordinates. In this subsection a finer study of the singular points of $Q$ gives the answer for $n = 2$, and for $n \ge 3$ when $Q$ contains no line. Two tools are necessary. In them $F$ is a series in variables $y_1, \dots, y_N$ over $k$.

**Lemma 3.3.24 (arc lemma).** Let $F \in k[[y_1, \dots, y_N]]$ be Newton nondegenerate. Let $\gamma(t) = (\gamma_1(t), \dots, \gamma_N(t))$ with $\gamma_i \in k[[t]]$ and $\gamma(0) = 0$, and let $J = \{ i : \gamma_i \ne 0 \}$. Assume that $F(\gamma) = 0$ and $(\partial_i F)(\gamma) = 0$ for each $i \in J$. Then $F$ is in the ideal $(y_i : i \notin J)$.

Lean: none yet

*Proof.* Assume that $F$ is not in this ideal. Then $F^J = F|_{y_i = 0, \, i \notin J}$ is a nonzero series in the variables $y_J$. For $i \in J$ write $\gamma_i = c_i t^{w_i} + (\text{terms of higher order})$ with $c_i \ne 0$ and $w_i \ge 1$. Let $\Phi = \operatorname{in}_{w_J} F^J$, of $w_J$-weight $d$. Each term of $F^J$ has a weight at least $d$, and the terms of weight $d$ make $\Phi$, so $F^J(\gamma_J) = \Phi(c_J) t^d + (\text{terms of higher order})$. In the same way, for $i \in J$ each term of $\partial_i F^J$ has a weight at least $d - w_i$, and the terms of weight $d - w_i$ make $\partial_i \Phi$, so $\partial_i F^J(\gamma_J) = (\partial_i \Phi)(c_J) t^{d - w_i} + (\text{terms of higher order})$. Since $\gamma_i = 0$ for $i \notin J$, we have $F^J(\gamma_J) = F(\gamma) = 0$ and $\partial_i F^J(\gamma_J) = (\partial_i F)(\gamma) = 0$ for $i \in J$. So $\Phi(c_J) = 0$ and $\partial_i \Phi(c_J) = 0$ for $i \in J$.

Let $W$ be the weight with $W_i = w_i$ for $i \in J$ and $W_i = M$ for $i \notin J$, with $M > d$. A term of $F$ that contains some $y_i$ with $i \notin J$ has a weight at least $M > d$. So $\operatorname{in}_W F = \Phi$, a polynomial in the variables $y_J$. At the torus point with the coordinates $c_i$ for $i \in J$ and $1$ for $i \notin J$, the polynomial $\Phi$ and its partial derivatives in $y_i$, $i \in J$, are $0$, and its partial derivatives in $y_i$, $i \notin J$, are identically $0$. This contradicts the nondegeneracy of $F$. $\square$

A homogeneous polynomial $H$ is *nondegenerate on all faces* if, for each face $\tau$ of the polytope $\operatorname{conv}(\operatorname{supp} H)$, including the polytope itself, the hypersurface $H_\tau = 0$ has no singular point in the torus. The compact faces of $N(H)$ are among these faces, so such an $H$ is Newton nondegenerate.

**Proposition 3.3.25 (reduction to the leading form).** Let $F \in k[[y_1, \dots, y_N]]$ have the order $d$ and the form $F_d$ of degree $d$. Let $\Psi$ be an automorphism of $k[[y]]$ with the linear part $A$, and let $u$ be a unit. If $u \cdot (F \circ \Psi)$ is Newton nondegenerate, then $F_d \circ A$ is nondegenerate on all faces.

Lean: none yet

*Proof.* Let $G = u \cdot (F \circ \Psi)$ and $H = u(0) \, F_d \circ A$. Then $G = H + (\text{terms of order at least } d + 1)$, and $H \ne 0$ is homogeneous of degree $d$. Let $\tau$ be a face of $P = \operatorname{conv}(\operatorname{supp} H)$, and let $v \in \mathbb{R}^N$ be a vector whose minimum on $P$ is attained exactly on $\tau$. Let $W = (1, \dots, 1) + \varepsilon v$ with $\varepsilon > 0$ small, so that $W > 0$. The polytope $P$ is in the hyperplane $|a| = d$, so on $P$ the weight $W$ is $d + \varepsilon \langle v, a \rangle$, and it is a minimum exactly on $\tau$. A monomial of degree at least $d + 1$ has a $W$-weight at least $(d + 1)(1 - \varepsilon \max_i |v_i|)$, and for $\varepsilon$ small this is more than $d + \varepsilon \max_P \langle v, \cdot \rangle$. So $\operatorname{in}_W G = H_\tau$. Since $G$ is nondegenerate, $H_\tau = 0$ has no singular point in the torus. $\square$

**Theorem 3.3.26.** Let $n = 2$, let $g \in k[[x, y]]$ with $\operatorname{ord} g = p$, let $h$ be the form of degree $p$ of $g$ with $\nabla h \ne 0$, and assume $|C| \ge 3$. Let $F = z^p + g$. Then for each automorphism $\Psi$ of $k[[x, y, z]]$ and each unit $u$, the series $u \cdot (F \circ \Psi)$ is Newton degenerate.

Node: SG00000097 · Lean: none yet

*Proof.* Let $F_p = z^p + h$. By Proposition 3.3.25 it is sufficient to show that for each $A \in \mathrm{GL}_3(k)$ the form $H = F_p \circ A$ is not nondegenerate on all faces. Assume that $H$ is nondegenerate on all faces. In particular $H$ is Newton nondegenerate. Let $X, Y, Z$ be the variables of $H$.

Step 1, $H$ has no linear factor. As a polynomial in $z$ over $k(x, y)$, $z^p + h$ is irreducible, because $-h$ is not a $p$-th power in $k(x, y)$, since $\nabla h \ne 0$. So $F_p$ has no linear factor, and $H$ has no linear factor.

Step 2, the singular points of $H = 0$ are coordinate points. Let $S \in k^3 \setminus \{0\}$ represent a singular point of the curve $H = 0$ in $\mathbb{P}^2$, and let $J$ be the set of the indices $i$ with $S_i \ne 0$. The arc $\gamma(t) = t S$ satisfies $H(\gamma) = t^p H(S) = 0$ and $\nabla H(\gamma) = t^{p-1} \nabla H(S) = 0$. Lemma 3.3.24 gives $H \in (X_i : i \notin J)$. If $|J| = 3$, then $H = 0$. If $|J| = 2$, then $H$ has a linear factor. Both are false, so $|J| = 1$. The map $A^{-1}$ sends the singular points of $Q$ bijectively onto the singular points of $H = 0$, so $|C| \le 3$. So $|C| = 3$, the three points $S_v$ are not on one line, and after a scaling and a permutation of the columns, the columns of $A$ represent $S_{v_1}$, $S_{v_2}$ and $S_{v_3}$, with $C = \{v_1, v_2, v_3\}$.

Step 3, the tangent cone at $S_v$. Fix $v \in C$ and a vector $v'$ that is not a multiple of $v$. Let $\varphi(t) = h(v + t v')$ and $\psi(t) = \varphi(t) - \varphi(0)$. Then $\psi'(0) = \nabla h(v) \cdot v' = 0$, so $e = \operatorname{ord}_0 \psi \ge 2$. Also $e \le p - 1$. Indeed $\deg \psi \le p$, so $e \ge p$ gives $\psi = a t^p$, and then $h(s v + t v') = \varphi(0) s^p + a t^p$ is a $p$-th power, which contradicts $\nabla h \ne 0$. In the affine coordinates $(t, \zeta)$ near $S_v$, for the points $(v + t v' : c_v + \zeta)$, the local equation of $Q$ is $\zeta^p + c_v^p + \varphi(t) = \zeta^p + \psi(t)$. Its form of lowest degree is $\psi_e t^e$ with $\psi_e \ne 0$, because $e < p$. So the tangent cone of $Q$ at $S_v$ is the line $t = 0$ counted $e$ times. This line is the set of the points $(v : z)$, that is, the line $\overline{O S_v}$.

Step 4, a corner face. Let $S_1 = S_{v_1}$, so that $A e_1$ represents $S_1$. The local equation of $H = 0$ at $e_1$ is $H(1, Y, Z)$. The map $A$ gives an isomorphism of the germ of $H = 0$ at $e_1$ onto the germ of $Q$ at $S_1$, and it sends the lines through $e_1$ to the lines through $S_1$. So by Step 3 the form of lowest degree of $H(1, Y, Z)$ is $c L^e$, with $c \ne 0$, $e \ge 2$ and $L$ a linear form in $(Y, Z)$ such that the line $L = 0$ is $A^{-1}(\overline{O S_1})$. For the weight $W = (1, 2, 2)$ a monomial $X^{p - j} Y^a Z^b$ with $a + b = j$ has the weight $p + j$, so $\operatorname{in}_W H = c X^{p - e} L^e$. If $L$ has two nonzero coefficients, the zero set of $L$ meets the torus, and since $e \ge 2$, each of these points is a singular point of $c X^{p - e} L^e = 0$. Then $H$ is degenerate, which is false. So $L$ is a multiple of $Y$ or of $Z$. Then the line $A^{-1}(\overline{O S_1})$ is a coordinate line through $e_1$, so it contains $e_2$ or $e_3$, and $\overline{O S_1}$ contains $S_{v_2}$ or $S_{v_3}$. But the points of $\overline{O S_1}$ other than $O$ are the points $(v_1 : z)$, and $S_{v_j} = (v_j : c_{v_j})$ with $v_j \ne v_1$ in $\mathbb{P}^1$. This is a contradiction. $\square$

Step 4 explains the degenerate faces of the examples below. They are the corner faces $c X^{p - e} L^e$.

**Proposition 3.3.27.** Let $n = 2$, $D = p$ and $\nabla h \ne 0$. Then $|C| \le p - 2$. So Theorem 3.3.26 is empty for $p \le 3$, and for $p = 5$ it applies exactly when $|C| = 3$.

Node: SG00000097 · Lean: none yet

*Proof.* By Proposition 3.3.18, $C = V(G)$ with a form $G \ne 0$ of degree $p - 2$. A nonzero binary form of degree $p - 2$ has at most $p - 2$ zeros in $\mathbb{P}^1$. $\square$

**Example 3.3.28.** Let $p = 5$. For $h = x^4 y + x y^4$ we have $\partial_x h = y (4 x^3 + y^3)$ and $\partial_y h = x (x^3 + 4 y^3)$. A common zero in $\mathbb{P}^1$ has $x y \ne 0$, and then $y^3 = x^3$. So $C = \{ (1 : \zeta) : \zeta^3 = 1 \}$, three points. For $h = 2 x^2 y^2 (x + y)$ we have $\partial_x h = x y^2 (x - y)$ and $\partial_y h = x^2 y (y - x)$, so $C = \{(1 : 0), (0 : 1), (1 : 1)\}$, and $h(1, 1) = 4 \ne 0$. By Theorem 3.3.26, the series $z^5 + x^4 y + x y^4 + (\text{terms of order at least } 6)$ and $z^5 + 2 x^2 y^2 (x + y) + (\text{terms of order at least } 6)$ are Newton degenerate after each change of all coordinates and each multiplication by a unit.

The research notes check this by computer. This is numerical evidence, in the form of exact computations over finite fields, and the theorem does not depend on it. For $h = x^4 y + x y^4$ over $\mathbb{F}_{25}$, the change $A$ whose columns are the three singular points of $Q$ gives a form $F_5 \circ A$ with $12$ monomials and $13$ faces. Its top face is nondegenerate, and exactly three faces are degenerate. These are the corner faces $X^3 q_1(Y, Z)$, $Y^3 q_2(X, Z)$ and $Z^3 q_3(X, Y)$ of Step 4, with $p - e = 3$ and quadratic forms $q_i$. For $h = 2 x^2 y^2 (x + y)$ the change $x = X + Z$, $y = Y + Z$, $z = Z$ gives a form with $12$ monomials, and exactly three of its $13$ faces are degenerate, among them $2 X^3 (Y + Z)^2$. For both forms, a search over all $4495$ unordered triples of points of $\mathbb{P}^2(\mathbb{F}_5)$ as the columns of $A$ finds no nondegenerate $F_5 \circ A$.

Node: SG00000097 · Lean: none yet

**Corollary 3.3.29.** Let $h \in k[x, y]$ be a form of degree $D$ with $p \mid D$ and $\nabla h \ne 0$. The following are equivalent.

1. An automorphism of $k[[x, y, z]]$ and a unit make $z^p + h$ Newton nondegenerate.
2. A linear change of $(x, y)$ and a cleaning make $z^p + h$ Newton nondegenerate.
3. $|C| \le 2$.

Node: SG00000098 · Lean: none yet

*Proof.* Clearly 2 gives 1. Theorem 3.3.26 for $D = p$ and Theorem 3.3.17 for $D > p$ show that 1 gives 3, because in $\mathbb{P}^1$ two hyperplanes with independent equations are two distinct points. Assume 3. By Proposition 3.3.18, a linear change $A$ and a cleaning make $\operatorname{in}_{(1, 1)}$ free of torus critical points. Let $h' = (h \circ A)^{\mathrm{cl}}$. Then $h' \ne 0$, since $\nabla h' = A^t (\nabla h) \circ A \ne 0$, and $N(h')$ is the segment between the two extreme monomials of $h'$ plus the positive quadrant. Its compact faces are the segment and its two vertices. A vertex is a monomial $x^a y^b$ that is not a $p$-th power, say with $p \nmid a$, and its derivative $a x^{a-1} y^b$ has no zero in the torus. So no face of $h'$ has a torus critical point, and Theorem 3.3.3 gives 2. $\square$

In more variables the same method works when $Q$ contains no line.

**Lemma 3.3.30.** The hypersurface $Q$ contains a line if and only if there is a line $M \subset \mathbb{P}^{n-1}$ such that $h|_M$ is the $p$-th power of a linear form on $M$.

Node: SG00000099 · Lean: none yet

*Proof.* A line $\Lambda \subset Q$ does not pass through $O$, since $O \notin Q$. So the projection from $O$ maps $\Lambda$ isomorphically onto a line $M \subset \mathbb{P}^{n-1}$, and $\Lambda$ is the graph of $z = \lambda(x)$ for a linear form $\lambda$ on the plane of $k^n$ over $M$. Then $\Lambda \subset Q$ if and only if $h|_M = -\lambda^p = (-\lambda)^p$. Conversely, if $h|_M = \mu^p$ for a linear form $\mu$, the graph of $z = -\mu$ is a line in $Q$. $\square$

In the coordinates $(s, t)$ of a line, $(\alpha s + \beta t)^p = \alpha^p s^p + \beta^p t^p$. So $h|_M$ is the $p$-th power of a linear form if and only if its coefficients of $s^i t^{p - i}$ for $0 < i < p$ are $0$. This is a finite test.

**Theorem 3.3.31.** Let $n \ge 2$, let $g \in k[[x_1, \dots, x_n]]$ with $\operatorname{ord} g = p$, and let $h$ be the form of degree $p$ of $g$, with $\nabla h \ne 0$. Assume that $Q$ contains no line, and that $C$ is infinite or has at least $n + 2$ points. Then for each automorphism $\Psi$ of $k[[x, z]]$ and each unit $u$, the series $u \cdot ((z^p + g) \circ \Psi)$ is Newton degenerate.

Node: SG00000099 · Lean: none yet

*Proof.* By Proposition 3.3.25 it is sufficient to show that for each $A \in \mathrm{GL}_{n+1}(k)$ the form $H = (z^p + h) \circ A$ is not nondegenerate on all faces. Assume that it is. Let $S$ represent a singular point of $H = 0$ in $\mathbb{P}^n$, and let $J$ be the set of the indices $i$ with $S_i \ne 0$. As in Step 2 of the proof of Theorem 3.3.26, the arc $t S$ and Lemma 3.3.24 give $H \in (X_i : i \notin J)$. So the coordinate subspace $\{X_i = 0 \text{ for } i \notin J\}$, of dimension $|J| - 1$, is in the hypersurface $H = 0$, which is $A^{-1}(Q)$. Since $Q$ contains no line, $|J| = 1$, and $S$ is a coordinate point. So $H = 0$ has at most $n + 1$ singular points, and so has $Q$. But the singular points of $Q$ are in bijection with $C$. This is a contradiction. $\square$

Let $n \ge 3$. If $C$ is finite with at most $n + 1$ points, then $C$ is in the union of $n$ hyperplanes with linearly independent equations. Indeed, add points to $C$ if necessary, so that it has $n + 1$ distinct points $p_1, \dots, p_{n+1}$, and for a point $q$ let $V_q$ be the space of the linear forms that are $0$ at $q$, of dimension $n - 1$. Take $\ell_1 \ne 0$ that is $0$ at $p_1, \dots, p_{n-1}$. The space $V_{p_n}$ is not in the union of $V_{p_n} \cap V_{p_{n+1}}$ and $k \ell_1$, so there is $\ell_2 \in V_{p_n}$, independent of $\ell_1$, with $\ell_2(p_{n+1}) \ne 0$. Then $V_{p_{n+1}}$ is not in the span of $\ell_1$ and $\ell_2$, so there is $\ell_3 \in V_{p_{n+1}}$ independent of them. Complete $\ell_1, \ell_2, \ell_3$ to a basis. So for $n \ge 3$ and $Q$ without a line, Theorem 3.3.31 covers each case where Theorem 3.3.16 gives an obstruction. Conversely, if $C$ is in the union of $n$ hyperplanes with independent equations, a linear change $\varphi$ of $x$ moves these hyperplanes to the coordinate hyperplanes. By the chain rule, as in the proof of Theorem 3.3.16, the top face of $z^p + (g \circ \varphi)^{\mathrm{cl}}$ then has no torus critical point. This holds also when $Q$ contains a line. It is not known if the other faces are then nondegenerate.

**Example 3.3.32.** Let $p = 5$, $n = 3$ and $h = x^4 y + y^4 w + w^4 x$. Then $\partial_x h = 4 x^3 y + w^4$, $\partial_y h = x^4 + 4 y^3 w$ and $\partial_w h = y^4 + 4 w^3 x$. The form $h$ is invariant under the cyclic permutation $x \mapsto y \mapsto w \mapsto x$. A point of $C$ with $x = 0$ has $w = 0$ by $\partial_x h$, and then $y = 0$ by $\partial_w h$, which is not a point. So by the symmetry each point of $C$ has three nonzero coordinates. Take $x = 1$. Then $\partial_x h = 0$ gives $y = w^4$, since $-1/4 = 1$ in $\mathbb{F}_5$, and $\partial_y h = 0$ gives $y^3 w = 1$, so $w^{13} = 1$. Then $\partial_w h = w^{16} + 4 w^3 = w^3 (w^{13} + 4) = 0$. So $C = \{ (1 : w^4 : w) : w^{13} = 1 \}$, and $|C| = 13 \ge n + 2$. The research notes show by an exact computer computation that $Q$ contains no line. The computation applies the test after Lemma 3.3.30 in three charts of the dual plane, with Gröbner bases over $\mathbb{F}_5$. With this computation, Theorem 3.3.31 shows that no change of all coordinates and no unit make $z^5 + h + (\text{terms of order at least } 6)$ Newton nondegenerate.

The research notes apply Theorem 3.3.31 in the same way to six other forms of degree $5$ in three variables for $p = 5$. An earlier computer search had left five of them undecided, because the field was too big. For each of the six forms, an exact computer computation shows that $Q$ contains no line and that $C$ has at least $7$ points. So none of these forms is prepared by a change of all coordinates.

Node: SG0000009A · Lean: none yet

**Conjecture 3.3.33.** Theorem 3.3.17 holds also for $D = p$.

Node: SG0000008Z · Lean: none yet

For $n = 2$ this is Theorem 3.3.26. For $n \ge 3$ and $Q$ without a line it follows from Theorem 3.3.31 and the remark after it. It is not known if the statement is true in the other cases with $n \ge 3$, in particular when $Q$ contains a line.

### Changes that do not keep the weight

The arc lemma also gives a restriction on the singular locus of a nondegenerate germ. Here $\operatorname{Sing}\{F = 0\}$ is the singular locus of the germ of $F = 0$ at the origin.

**Corollary 3.3.34.** Let $F \in k[[x, y, z]]$ be irreducible of order at least $2$. Assume that $u \cdot (F \circ \Psi)$ is Newton nondegenerate for an automorphism $\Psi$ and a unit $u$. Then $\operatorname{Sing}\{F = 0\}$ is the image under $\Psi$ of a union of coordinate axes. So it has at most three branches of dimension $1$, each branch is smooth, and their tangent lines are linearly independent.

Lean: none yet

*Proof.* Let $G = u \cdot (F \circ \Psi)$. It is irreducible, of order at least $2$, and its singular locus is the inverse image of the singular locus of $F = 0$. Since $G$ is irreducible, its singular locus has dimension at most $1$. Let $\Gamma$ be a branch of dimension $1$ of the singular locus of $G = 0$, and let $\gamma$ be its parametrization by the normalization. Then $G(\gamma) = 0$ and $\partial_i G(\gamma) = 0$ for each $i$. Lemma 3.3.24 gives $G \in (y_i : i \notin J)$. If $|J| = 3$, then $G = 0$, which is false. If $|J| = 2$, the third coordinate divides $G$, and since $G$ is irreducible, $G$ is this coordinate times a unit, of order $1$, which is false. So $J = \{i\}$, the arc $\gamma$ is in the $y_i$-axis, and $\Gamma$ is this axis. Distinct branches give distinct axes. An automorphism sends smooth branches to smooth branches, and it acts on their tangent lines by its linear part. $\square$

**Theorem 3.3.35.** Let $p = 3$, $F_1 = z^3 + x^3 y^2 + y^4$ and $F_2 = z^3 + x^4 y^4 + x^2 y^5$. Then for each automorphism $\Psi$ of $k[[x, y, z]]$ and each unit $u$, the series $u \cdot (F_1 \circ \Psi)$ and $u \cdot (F_2 \circ \Psi)$ are Newton degenerate.

Node: SG0000009B · Lean: none yet

*Proof.* Both series have order $3$. A series $z^3 + a$ with $a \in (x, y)$ is a Weierstrass polynomial. By the Weierstrass preparation theorem and the Gauss lemma, it is irreducible in $k[[x, y, z]]$ if $-a$ is not a cube in the fraction field of the factorial ring $k[[x, y]]$, that is, not a cube in $k[[x, y]]$. Here $x^3 y^2 + y^4 = y^2 (x^3 + y^2)$ has the order $2$ in $y$, and $x^4 y^4 + x^2 y^5 = x^2 y^4 (x^2 + y)$ has the order $2$ in $x$. So neither is a cube, and $F_1$ and $F_2$ are irreducible. We apply Corollary 3.3.34.

For $F_1$, in characteristic $3$, $\partial_x F_1 = \partial_z F_1 = 0$ and $\partial_y F_1 = 2 x^3 y + y^3 = y (y^2 - x^3)$. On $y = 0$ the equation $F_1 = 0$ gives $z = 0$, so the $x$-axis is in the singular locus. On $y^2 = x^3$ we have $F_1 = z^3 + 2 x^6 = (z - x^2)^3$, so the singular locus also contains the branch $y^2 = x^3$, $z = x^2$, with the parametrization $(t^2, t^3, t^4)$. This branch has the multiplicity $2$, so it is not smooth, and Corollary 3.3.34 is contradicted.

For $F_2$, $\partial_x F_2 = x^3 y^4 + 2 x y^5 = x y^4 (x^2 - y)$, $\partial_y F_2 = x^4 y^3 + 2 x^2 y^4 = x^2 y^3 (x^2 - y)$ and $\partial_z F_2 = 0$. On $x = 0$ or $y = 0$ the equation gives $z = 0$, so the singular locus contains the $x$-axis and the $y$-axis. On $y = x^2$ we have $F_2 = z^3 + 2 x^{12} = (z - x^4)^3$, so it also contains the branch $(t, t^2, t^4)$. This branch is smooth, with the tangent line of the $x$-axis. Two branches with the same tangent line contradict Corollary 3.3.34. $\square$

So the obstruction for $F_2$ in Example 3.3.21 holds for each change of all coordinates, and also the classical example $F_1$ is not prepared by any change. The theorem is about these two polynomials. Terms of higher order can change the singular locus. For changes whose linear part respects the weights, the next result allows terms of higher weight.

**Proposition 3.3.36.** Let $W = (w_x, w_y, w_z)$ be $(2, 3, 4)$ for $F_1$ and $(1, 2, 4)$ for $F_2$, and let $F$ be $F_1$ or $F_2$ plus a series whose monomials have a $W$-weight more than $12$. Let $\Psi$ be an automorphism of $k[[x, y, z]]$ whose linear part sends each variable into the span of the variables of weight at least its own. Then $u \cdot (F \circ \Psi)$ is Newton degenerate for each unit $u$.

Node: SG0000009B · Lean: none yet

*Proof.* We can take $u = 1$, since $\operatorname{in}_V(u G) = u(0) \operatorname{in}_V G$ for each weight $V > 0$. Let $h$ be $x^3 y^2 + y^4$ or $x^4 y^4 + x^2 y^5$. It is $W$-homogeneous of weight $12$, and $F = z^3 + h + R$ where each monomial of $R$ has a $W$-weight at least $13$. Write $\Psi_x, \Psi_y, \Psi_z$ for the images of $x, y, z$. By the hypothesis the linear part of $\Psi$ is triangular: $\Psi_x$ has the linear part $\alpha x + (\text{terms in } y, z)$, $\Psi_y$ has the linear part $\beta y + (\text{a term in } z)$ for $F_1$ and for $F_2$, and $\Psi_z$ has the linear part $c z$. Since the linear part is invertible, $\alpha \beta c \ne 0$. A monomial of degree at least $2$ has a $W$-weight at least $2 w_x$, and $2 w_x \ge w_y$. So $\Psi_x$ and $\Psi_y$ have the $W$-orders $w_x$ and $w_y$, and their initial forms $\varphi_x = \operatorname{in}_W \Psi_x$ and $\varphi_y = \operatorname{in}_W \Psi_y$ do not contain $z$. They define a graded automorphism $\varphi_W = (\varphi_x, \varphi_y)$ of $k[x, y]$ for the weight $(w_x, w_y)$. Write $\Psi_z = c z + s$, where $s$ has no linear term. In characteristic $3$, $F \circ \Psi = c^3 z^3 + s^3 + h(\Psi_x, \Psi_y) + R \circ \Psi$.

Case 1, $s$ has a $W$-order $\delta < 4$. This occurs only for $F_2$, since for $F_1$ each monomial of degree at least $2$ has a weight at least $4$. Then $\delta \in \{2, 3\}$, and $s_\delta = \operatorname{in}_W s$ is a nonzero polynomial in $x, y$, because a monomial of degree at least $2$ that contains $z$ has a weight more than $4$. Let $V = (1, 2, \delta)$. A monomial of $s$ other than those of $s_\delta$ has a $V$-weight more than $\delta$, so $\operatorname{in}_V \Psi_z = c z + s_\delta$, of $V$-weight $\delta$. The components $\Psi_x$ and $\Psi_y$ have $V$-orders at least $1$ and $2$, so $h(\Psi_x, \Psi_y)$ has a $V$-order at least $12 > 3 \delta$. A monomial $x^a y^b z^e$ of $R$ has $a + 2b + 4e \ge 13$. If $e \ge 4$, its $V$-weight is at least $4 \delta > 3 \delta$. If $e \le 3$, its $V$-weight is $a + 2b + \delta e \ge 13 - (4 - \delta) e \ge 1 + 3 \delta$. So $R \circ \Psi$ has a $V$-order more than $3 \delta$, and $\operatorname{in}_V(F \circ \Psi) = (c z + s_\delta)^3$. Take a torus point $(x_0, y_0)$ with $s_\delta(x_0, y_0) \ne 0$ and $z_0 = -s_\delta(x_0, y_0)/c$. Then $(x_0, y_0, z_0)$ is in the torus, and it is a singular point of $(c z + s_\delta)^3 = 0$, since the gradient of a cube is $0$. So $F \circ \Psi$ is degenerate.

Case 2, $s$ has a $W$-order at least $4$. Let $q \in k[x, y]$ be the part of $s$ of $W$-weight $4$. A monomial of degree at least $2$ that contains $z$ has a weight more than $4$, so $\operatorname{in}_W \Psi_z = c z + q$. The map $\Psi$ does not lower the $W$-weights, so $\operatorname{in}_W(F \circ \Psi) = c^3 z^3 + G$ with $G = h \circ \varphi_W + q^3$, and $R \circ \Psi$ has a $W$-order at least $13$. If $G = 0$, then $h \circ \varphi_W = -q^3$ has the gradient $0$, and so has $h$, which is false. So $G \ne 0$, and $\nabla G = \nabla (h \circ \varphi_W)$. For $F_1$ the weight $(2, 3)$ admits only the graded automorphisms $x \mapsto a x$, $y \mapsto b y$, and $\partial_y (h \circ \varphi_W) = b^2 y (2 a^3 x^3 + b^2 y^2)$ is $0$ at the torus points with $b^2 y^2 = a^3 x^3$, while $\partial_x (h \circ \varphi_W) = 0$. For $F_2$, Example 3.3.21 and Proposition 3.3.20 show that $h \circ \varphi_W$ has a torus critical point. So in both cases $G$ has a torus critical point $(x_0, y_0)$. If $G(x_0, y_0) \ne 0$, choose $z_0$ with $c^3 z_0^3 = -G(x_0, y_0)$. Then $(x_0, y_0, z_0)$ is a torus singular point of $c^3 z^3 + G = 0$. If $G(x_0, y_0) = 0$, take the weight $W' = W + e_z$. Then $F \circ \Psi = c^3 z^3 + G + E$, where $E$ has a $W$-order more than $12$. The $W'$-weight of a monomial is at least its $W$-weight. So the monomials of $G$ have the $W'$-weight $12$, the monomial $z^3$ has the $W'$-weight $15$, and the monomials of $E$ have a $W'$-weight more than $12$. So $\operatorname{in}_{W'}(F \circ \Psi) = G$, and $(x_0, y_0, 1)$ is a torus singular point of $G = 0$, because $G$ does not contain $z$. $\square$

### Weighted forms in three variables

For a weight that is not $(1, \dots, 1)$, Theorem 3.3.16 has a version for the top face. Let $\omega \in \mathbb{Z}_{>0}^n$, and let $h$ be clean and $\omega$-homogeneous of degree $D$, with $\nabla h \ne 0$. Let $G_\omega$ be the group of the graded automorphisms of $k[x]$, that is, the automorphisms that send $x_i$ to an $\omega$-homogeneous polynomial of weight $\omega_i$. A *change that keeps $\omega$* is a change $(\varphi, q)$ such that the initial forms $\operatorname{in}_\omega \varphi_i$ have the weights $\omega_i$ and define an element $\varphi_\omega$ of $G_\omega$. Let $Z = \{\nabla h = 0\} \subset \mathbb{A}^n$. It is a closed cone for the action $\lambda \cdot x = (\lambda^{\omega_i} x_i)$.

**Proposition 3.3.37.** Let $g = h + (\text{terms of higher } \omega\text{-weight})$. A change that keeps $\omega$, followed by the cleaning, makes the $\omega$-face of $g$ free of torus critical points if and only if there is $\psi \in G_\omega$ with $\psi(Z) \subset \{x_1 \cdots x_n = 0\}$. The terms of higher weight have no effect.

Lean: none yet

*Proof.* Let $(\varphi, q)$ keep $\omega$. Then $\operatorname{in}_\omega(g \circ \varphi) = h \circ \varphi_\omega$, and the cleaning removes $q^p$ and the monomials that are $p$-th powers. The cleaning acts monomial by monomial, so the $\omega$-face of the cleaned series is $(h \circ \varphi_\omega)^{\mathrm{cl}}$, and it has the same gradient as $h \circ \varphi_\omega$, which is not $0$. The Jacobian determinant of a graded automorphism is $\omega$-homogeneous of weight $0$, so it is a nonzero constant. By the chain rule, $\{\nabla(h \circ \varphi_\omega) = 0\} = \varphi_\omega^{-1}(Z)$. So the face is free of torus critical points if and only if $\psi = \varphi_\omega^{-1}$ sends $Z$ into $\{x_1 \cdots x_n = 0\}$. Conversely, for such a $\psi$ take $\varphi = \psi^{-1}$ and $q = 0$. $\square$

Now let $n = 3$, with the variables $(x, y, w)$ and the weight $\omega$ with $\gcd 1$. For a point $P$ with $(x, y) \ne 0$ the *base* of $P$ is $(x : y) \in \mathbb{P}^1$.

**Theorem 3.3.38.** Let $n = 3$, and let $g = h + (\text{terms of higher } \omega\text{-weight})$. A change that keeps $\omega$, followed by the cleaning, makes the $\omega$-face of $g$ free of torus critical points if and only if the following condition holds.

1. For $\omega = (1, 1, 1)$: $C$ is on three lines with no common point.
2. For $\omega = (a, a, b)$ with $a, b \ge 2$ and $a \ne b$: the points of $Z$ with $w \ne 0$ and $(x, y) \ne 0$ have at most two bases.
3. For $\omega = (1, 1, m)$ with $m \ge 2$: there are a set $B \subset \mathbb{P}^1$ with $|B| \le 2$ and a binary form $c$ of degree $m$ such that each point $P \in Z$ with $(x, y) \ne 0$ and the base outside $B$ satisfies $w(P) = c(x(P), y(P))$.
4. For $\omega = (1, m, m)$ with $m \ge 2$: the set $Z \cap \{x = 1\} \subset \mathbb{A}^2$ is in the union of two lines with independent directions.
5. For $\omega = (a, b, b)$ with $2 \le a < b$: the points of $Z$ with $x \ne 0$ and $(y, w) \ne 0$ have at most two images $(y : w) \in \mathbb{P}^1$.
6. For $\omega = (1, m_1, m_2)$ with $1 < m_1 < m_2$: there are $s_0 \in k$ and a polynomial $P_1$ of degree at most $\lfloor m_2 / m_1 \rfloor$ with $Z \cap \{x = 1\} \subset \{y = s_0\} \cup \{w = P_1(y)\}$.
7. For three distinct entries, none of them a combination of the other two with coefficients in $\mathbb{N}$: $Z$ does not meet the torus.

Node: SG0000009C · Lean: none yet

*Proof.* By Proposition 3.3.37 we need $\psi \in G_\omega$ with $Z \subset \psi^{-1}\{x y w = 0\}$. A graded automorphism sends a variable of weight $\omega_i$ to a polynomial of weight $\omega_i$. Such a polynomial contains only variables of weight at most $\omega_i$, and the variables of weight $\omega_i$ only linearly. A monomial of weight $\omega_i$ in the variables of smaller weight exists only if $\omega_i$ is a combination of these weights with coefficients in $\mathbb{N}$. In each case this gives $G_\omega$.

Case 1. Here $G_\omega = \mathrm{GL}_3$, and $\psi^{-1}\{x y w = 0\}$ is the union of three planes with independent equations. The set $Z$ is the cone over $C$, and three lines in $\mathbb{P}^2$ have independent equations if and only if they have no common point.

Case 2. Since $\gcd(a, b) = 1$ and $a, b \ge 2$, neither entry divides the other, so $\psi = (L_1(x, y), L_2(x, y), e w)$ with $L_1, L_2$ independent and $e \ne 0$. Then $\psi^{-1}\{x y w = 0\} = \{L_1 = 0\} \cup \{L_2 = 0\} \cup \{w = 0\}$. A point with $w \ne 0$ is in this set if and only if $(x, y) = 0$ or its base is the zero of $L_1$ or of $L_2$. Two independent linear forms can vanish at any two given bases.

Case 3. Here $\psi = (L_1, L_2, e w + Q(x, y))$ with $Q$ a binary form of degree $m$. A point is in $\psi^{-1}\{x y w = 0\}$ if and only if $(x, y) = 0$, or its base is the zero of $L_1$ or of $L_2$, or $w = -Q(x, y)/e$. Take $B$ the set of the zeros of $L_1$ and $L_2$, and $c = -Q/e$. Conversely, $B$ and $c$ give $L_1$, $L_2$ and $Q = -c$ with $e = 1$.

Case 4. Here $\psi = (e x, \ell_1(y, w) + c_1 x^m, \ell_2(y, w) + c_2 x^m)$ with $\ell_1, \ell_2$ independent. The points with $x = 0$ are in $\psi^{-1}\{x y w = 0\}$. Each orbit with $x \ne 0$ meets $\{x = 1\}$ in exactly one point, because $x$ has the weight $1$. On $\{x = 1\}$ the set $\psi^{-1}\{x y w = 0\}$ is the union of the lines $\ell_1 = -c_1$ and $\ell_2 = -c_2$, and each pair of lines with independent directions has this form.

Case 5. Since $\gcd(a, b) = 1$ and $a \ge 2$, $a \nmid b$. So $\psi = (e x, M(y, w))$ with $M \in \mathrm{GL}_2$, and the argument of Case 2 applies with the roles of the variables exchanged. A weight $(a, a, b)$ with $a > b$ is of this type after a permutation of the variables.

Case 6. Here $\psi = (e_1 x, e_2 y + c x^{m_1}, e_3 w + P(x, y))$ with $P = \sum_{j \le \lfloor m_2 / m_1 \rfloor} c_j x^{m_2 - j m_1} y^j$. As in Case 4 it is sufficient to look at $\{x = 1\}$, where the conditions are $y = -c/e_2$ or $w = -P(1, y)/e_3$, and $P(1, y)$ is an arbitrary polynomial of degree at most $\lfloor m_2 / m_1 \rfloor$.

Case 7. No monomial other than the variable has the weight of a variable, so $G_\omega$ is the group of the diagonal matrices. It keeps the torus, so the condition is $Z \cap T = \emptyset$. $\square$

In Case 3 the condition implies that each base outside $B$ carries at most one orbit of points of $Z$, since over a base the condition fixes the value of $w$. So a necessary condition is that at most two bases carry more than one orbit. A sufficient condition is that, in addition, there are at most $m + 3$ bases. Indeed, put the bases with more than one orbit into $B$, and complete $B$ to two bases. At most $m + 1$ bases remain, each with one orbit. The evaluation of the binary forms of degree $m$ at $m + 1$ distinct points of $\mathbb{P}^1$ is a bijection onto $k^{m+1}$, because a nonzero form of degree $m$ has at most $m$ zeros. So a form $c$ with the given values exists. In two variables, Proposition 3.3.20 is the analogue of Case 6.

Theorem 3.3.38 is only about the top face. For the edges there is a direct test. A torus critical point is in the sense of the beginning of the section, $\nabla f = 0$, with no condition on $f$.

**Lemma 3.3.39.** Let $f = x^a \psi(x^u)$ be the initial form of an edge, with $a \in \mathbb{N}^n$, a primitive $u \in \mathbb{Z}^n$, and $\psi \in k[T]$ with $\psi(0) \ne 0$ and $\deg \psi \ge 1$.

1. If $a$ and $u$ are linearly independent modulo $p$, then $f$ has a torus critical point if and only if $\psi$ has a multiple root.
2. If $a \equiv \lambda u$ modulo $p$ with $\lambda \in \mathbb{F}_p$, then $f$ has a torus critical point if and only if $\lambda \psi + T \psi'$ has a nonzero root or is $0$.

For the singular points of Definition 3.3.1, the condition in part 2 becomes that $\psi$ has a multiple root.

Lean: none yet

*Proof.* On the torus, $x_i \partial_i f = x^a (a_i \psi(T) + u_i T \psi'(T))$ with $T = x^u$, and $T$ takes each value of $k^*$, since $u \ne 0$. So a torus critical point is a value $T \in k^*$ with $a_i \psi(T) + u_i T \psi'(T) = 0$ for each $i$. In part 1 the matrix with the rows $a$ and $u$ has the rank $2$ over $\mathbb{F}_p$, so the condition is $\psi(T) = T \psi'(T) = 0$. This says that $T$ is a multiple root, and a root is not $0$, since $\psi(0) \ne 0$. In part 2, some $u_i$ is not $0$ modulo $p$, since $u$ is primitive, and the condition is $\lambda \psi(T) + T \psi'(T) = 0$. At a singular point we also need $\psi(T) = 0$, and then the condition is $\psi(T) = \psi'(T) = 0$. $\square$

The research notes compare the criterion of Theorem 3.3.38 for the weights $(1, 1, m)$ and $(1, m, m)$ with exhaustive searches over $G_\omega(\mathbb{F}_q)$ for $p = 2, 3, 5$ and small $q$, and the two agree in each case. This is numerical evidence, in the form of exact computer computations over finite fields. It checks the description of the groups $G_\omega$ and a few forms, and the theorem does not depend on it. In these computations the faces below the top face were often degenerate after a preparation of the top face. So for weighted forms in three variables a preparation of the top face is weaker than nondegeneracy, unlike Corollary 3.3.29 for binary forms.

### Toric resolution without convenience

The theorem of Varchenko and Khovanskii is usually stated for a *convenient* polynomial, one whose Newton polyhedron meets each coordinate axis. An equation $z^p + g$ with a singular locus of positive dimension is not convenient in general. The next theorem removes this hypothesis near the origin.

**Theorem 3.3.40.** Let $k$ be a perfect field and let $F \in k[x_1, \dots, x_m]$ with $F \ne 0$ and $F(0) = 0$ be Newton nondegenerate over an algebraic closure of $k$. Let $\Sigma$ be a regular fan with the support $\mathbb{R}_{\ge 0}^m$ that refines the normal fan of $N(F)$, and let $\pi \colon X_\Sigma \to \mathbb{A}^m$ be the toric morphism. Then there is a Zariski open neighbourhood $U$ of $0$ such that over $U$ the total transform of $F$ has simple normal crossings. Locally $\pi^* F = y^\mu \tilde F$, where $\tilde F = 0$ is smooth and transverse to the toric boundary, and $\tilde F = 0$ is the strict transform of the closure of $\{F = 0\} \cap T$.

Node: SG0000008W · Lean: none yet

*Proof.* We can work over the algebraic closure, since smoothness and normal crossings descend. Take a maximal cone of $\Sigma$ with the primitive generators $v^1, \dots, v^m$, a basis of $\mathbb{Z}^m$. The chart has the coordinates $y_1, \dots, y_m$ and $x_i = \prod_j y_j^{v^j_i}$, so $x^a = \prod_j y_j^{\langle v^j, a \rangle}$. Let $\mu_j = m_{v^j}(F)$. Then $\pi^* F = y^\mu \tilde F$ with $\tilde F = \sum_a c_a \prod_j y_j^{\langle v^j, a \rangle - \mu_j}$. No $y_j$ divides $\tilde F$, because the face of $v^j$ has an exponent with $\langle v^j, a \rangle = \mu_j$, and distinct exponents give distinct monomials, since the matrix $(v^j_i)$ is unimodular. So $\tilde F = 0$ has no component in the boundary.

Let $P$ be a point of the chart with $\pi(P) = 0$ and $\tilde F(P) = 0$, and let $J = \{ j : y_j(P) = 0 \}$. For each $i$ some $j \in J$ has $v^j_i > 0$, since $x_i(P) = 0$. So $\sum_{j \in J} v^j$ has positive entries, and its face $\Delta$ of $N(F)$ is compact. The cone of the $v^j$ with $j \in J$ is in one cone of the normal fan, so an exponent $a$ has $\langle v^j, a \rangle = \mu_j$ for each $j \in J$ exactly when $a \in \Delta$. So $\tilde F$ restricted to $y_J = 0$ is $Q = \sum_{a \in \Delta} c_a \prod_{l \notin J} y_l^{\langle v^l, a \rangle - \mu_l}$, and the same computation gives $F_\Delta \circ \pi = y^\mu Q$, with $Q$ independent of $y_J$.

Assume that $\partial_{y_l} Q(P) = 0$ for each $l \notin J$. Let $P'$ be the torus point with $y_j(P') = 1$ for $j \in J$ and $y_l(P') = y_l(P)$ for $l \notin J$. Then $Q(P') = 0$, and each partial derivative of $Q$ is $0$ at $P'$. By the product rule, $y^\mu Q = F_\Delta \circ \pi$ and its partial derivatives are $0$ at $P'$. Since $\pi$ is an isomorphism of the tori, $\pi(P')$ is a torus singular point of $F_\Delta = 0$, which contradicts the nondegeneracy. So $\partial_{y_l} Q(P) \ne 0$ for some $l \notin J$, and $\partial_{y_l} \tilde F(P) = \partial_{y_l} Q(P)$, because $\tilde F - Q$ is in the ideal $(y_j : j \in J)$. So $\tilde F = 0$ is smooth at $P$, and the differentials $d y_j$ for $j \in J$ and $d \tilde F$ are independent at $P$.

Let $B$ be the closed set of the points of $\tilde F = 0$ where this fails. It does not meet $\pi^{-1}(0)$. The support of $\Sigma$ is the whole orthant, so $\pi$ is proper, $\pi(B)$ is closed, and $U = \mathbb{A}^m \setminus \pi(B)$ is the neighbourhood. $\square$

The components of $F = 0$ in the coordinate hyperplanes become boundary divisors. Convenience makes $\pi$ an isomorphism outside $0$ for an isolated singularity, but it is not necessary for the normal crossings near $\pi^{-1}(0)$. The proof uses only the Jacobian criterion and the properness of $\pi$, so it works in each characteristic.

### Weighted blowups

A degenerate face of the third kind of Lemma 3.3.2 can be localized by one weighted blowup. Let $f = z^p + g$, let $w > 0$, let $m = m_w(g) \ge 1$, let $\sigma$ be the face of $w$, and let $W = (p w, m)$, divided by the gcd of its entries.

**Proposition 3.3.41.** In each regular fan that contains the ray of $W$ and refines the normal fan of $N(f)$, the points of the open orbit of the divisor $E_W$ where the strict transform is singular or not transverse to $E_W$ correspond to the torus orbits of the torus critical points $v$ of $g_\sigma$ with $g_\sigma(v) \ne 0$. If $g = g_\sigma$, these points are singular points of the strict transform.

Node: SG0000008V · Lean: none yet

*Proof.* Take $J = \{j\}$ in the proof of Theorem 3.3.40, with $v^j$ the primitive vector of $W$. The face of $W$ is of the third kind, with the initial form $z^p + g_\sigma$. Write $\tilde F = Q + y_j R$. As in that proof, $\tilde F$ is not smooth and transverse to $y_j = 0$ at a point $P$ of the open orbit if and only if $Q(P) = 0$ and $\nabla Q(P) = 0$. On the torus the steps are reversible, so this holds if and only if the corresponding torus point is a singular point of $z^p + g_\sigma$. By the proof of Theorem 3.3.3 these are the points $(v, c)$ with $v$ critical and $c^p = -g_\sigma(v) \ne 0$. If $g = g_\sigma$, then $f$ is weighted homogeneous for $W$, so $R = 0$ and $\tilde F = Q$. $\square$

**Example 3.3.42.** The word "transverse" is necessary. Let $p = 3$ and $f = z^3 + x^2 y + x y^2 + y^4$. For $W = (1, 1, 1)$ the face is $z^3 + x y (x + y)$, which is degenerate along $(s, s, s)$ by Example 3.3.9. In the chart $y = x t$, $z = x z'$ of the blowup of the origin, $f = x^3 (z'^3 + t + t^2 + x t^4)$. At $P = (x, t, z') = (0, 1, 1)$ the strict transform $\tilde F = z'^3 + t + t^2 + x t^4$ has $\tilde F(P) = 0$ and $\nabla \tilde F(P) = (1, 0, 0)$. So the strict transform is smooth at $P$, but it is tangent to $E_W = \{x = 0\}$, and only its restriction $z'^3 + t + t^2$ to $E_W$ is singular.

Node: SG0000008V · Lean: none yet

In two variables one weighted blowup turns a homogeneous equation into nondegenerate singularities.

**Theorem 3.3.43.** Let $h \in k[x, y]$ be a form of degree $D$ with $p \mid D$ and $\nabla h \ne 0$, and let $f = z^p + h$. Let $\pi$ be the weighted blowup with the weights $(1, 1, D/p)$. Then the strict transform of $f = 0$ is in the $x$-chart and the $y$-chart, and at each of its singular points it is, in suitable coordinates, $\{ z^p + s^e u(s) = 0 \} \times \mathbb{A}^1$ with $u(0) \ne 0$, $p \nmid e$ and $2 \le e \le D$. These germs are Newton nondegenerate and convenient in $(s, z)$, so a toric modification resolves each of them.

Node: SG0000008X · Lean: none yet

*Proof.* In the $x$-chart, $y = x t$ and $z = x^{D/p} z'$, and $f = x^D (z'^p + \varphi(t))$ with $\varphi(t) = h(1, t)$. The strict transform $z'^p + \varphi(t)$ does not contain $x$, so it is a curve times a line. It is singular at $(t_0, z_0)$ exactly when $\varphi'(t_0) = 0$ and $z_0^p = -\varphi(t_0)$. Let $z' = z'' + z_0$ and $t = t_0 + s$. The equation becomes $z''^p + \psi(s)$ with $\psi(s) = \varphi(t_0 + s) - \varphi(t_0)$ of order at least $2$. A change $z'' \mapsto z'' + r(s)$ removes the $p$-th powers of $\psi$, and what is left is $s^e u(s)$ with $p \nmid e$. The exception is a $\psi$ that is a $p$-th power. Then $\varphi' = 0$, so $\partial_y h = 0$, since $\partial_y h = x^{D-1} \varphi'(y/x)$, and then $\partial_x h = 0$ by the Euler identity, which is excluded. The order $e$ is at least $2$ and at most $\deg \varphi \le D$. The face $z^p + u(0) s^e$ has $\partial_s \ne 0$ on the torus, so it is nondegenerate, and the vertices are not $p$-th powers. The $y$-chart is the same with the roles of $x$ and $y$ exchanged. In the $z$-chart, at the point $x = y = 0$ of the exceptional divisor the strict transform is $1 + h(\cdot) \ne 0$, so the strict transform is in the other two charts. $\square$

For $z^5 + x^4 y + x y^4$ the three critical directions give $e = 2$. So one weighted blowup and three toric modifications resolve it, while by Example 3.3.28 no change of all coordinates makes it nondegenerate.

The same blowup also works with terms of higher order, if we measure the singularity by the residual order. For $f = z^p + g$ let $\nu(f) = \operatorname{ord} g^{\mathrm{cl}}$. This is the residual order of Definition 1.3.3 for $E = \emptyset$. By part 1 of Proposition 1.3.5, $\nu(f) = \max_q \operatorname{ord}(g + q^p)$. So $\nu(f)$ does not change under $z \mapsto z + q(x)$, and it does not depend on the coordinates $x$, since a change of $x$ keeps the order and the $p$-th powers. If the form $h$ of degree $D = \operatorname{ord} g$ has $\nabla h \ne 0$, then $h$ has a monomial that is not a $p$-th power, and $\nu(f) = D$. For $v \in k^n$ let $\partial_v h = \sum_i v_i \partial_i h$.

**Theorem 3.3.44.** Let $n \ge 2$ and $g \in k[[x_1, \dots, x_n]]$ with $\operatorname{ord} g = D$ and $p \mid D$, and let $h$ be the form of degree $D$ of $g$, with $\nabla h \ne 0$. Let $f = z^p + g$, so $\nu(f) = D$. Let $\pi$ be the weighted blowup of the origin of $\mathbb{A}^{n+1}$ with the weights $(1, \dots, 1, D/p)$, and let $f'$ be the strict transform.

1. The strict transform $f' = 0$ meets the exceptional divisor $E$ only in the $x_i$-charts.
2. In the $x_1$-chart, with $x_1 = t$, $x_j = t y_j$ for $j \ge 2$ and $z = t^{D/p} z'$, we have $f' = z'^p + \varphi(y) + t R(t, y)$ with $\varphi(y) = h(1, y)$. At a point $P = (0, y_0, z_0)$ of $f' = 0$, the strict transform is smooth unless $v = (1 : y_0) \in C$. Then $z_0^p = -\varphi(y_0)$, and we call the point $P_v$.
3. At $P_v$, with $s = y - y_0$ and $\zeta = z' - z_0$, we have $f' = \zeta^p + g_v$ with $g_v = \psi(s) + t R(t, y_0 + s)$ and $\psi(s) = \varphi(y_0 + s) - \varphi(y_0)$. Then $\nu(P_v) = \operatorname{ord} g_v^{\mathrm{cl}} \le D - 1$, unless $\partial_v h$ is identically $0$.
4. If $n = 2$, the exception in part 3 does not occur. So the residual order goes down at each point of the strict transform over the origin. At the smooth points it is $1$.

Node: SG0000009D · Lean: none yet

*Proof.* Part 1. In the $z$-chart, $x = z' x'$ and $z = z'^{D/p}$, and $f = z'^D (1 + h(x') + z' (\cdots))$. At the point $x' = 0$ of $E$ the strict transform has the value $1$. Each other point of $E$ in this chart has some $x'_i \ne 0$, and it is in the $x_i$-chart.

Part 2. We have $g(t, t y) = t^D (\varphi(y) + t R(t, y))$ and $z^p = t^D z'^p$. On $E = \{t = 0\}$, $\partial_{y_j} f' = \partial_j \varphi(y_0)$. If this is not $0$ for some $j$, then $f'$ is smooth at $P$. Assume $\nabla \varphi(y_0) = 0$. Then $\partial_j h(1, y_0) = 0$ for $j \ge 2$, and the Euler identity $\sum_i x_i \partial_i h = D h = 0$ gives $\partial_1 h(1, y_0) = 0$. So $v \in C$. Since $P$ is on $f' = 0$, $z_0^p = -\varphi(y_0)$.

Part 3. The equation follows from $(z_0 + \zeta)^p = z_0^p + \zeta^p$. The monomials of $\psi$ do not contain $t$, and the monomials of $t R$ all contain $t$. So a monomial of $\psi$ that is not a $p$-th power stays in $g_v^{\mathrm{cl}}$, and $\nu(P_v)$ is at most its degree. Assume that $\psi$ has no such monomial of degree at most $D - 1$. After the linear change $x \mapsto (x_1, x' + x_1 y_0)$ we can assume $y_0 = 0$ and $v = e_1$. Write $h(x_1, y) = \sum_j x_1^{D - j} h_j(y)$ with forms $h_j$ of degree $j$. Then $\psi(s) = \sum_{j \ge 1} h_j(s)$, and by the assumption $h_j$ is a $p$-th power for $1 \le j \le D - 1$, so $h_j = 0$ unless $p \mid j$. Since $p \mid D$, each $x_1^{D - j} h_j$ with $j < D$ is a $p$-th power, and $h(x_1, y) = h(0, y) + (\text{a } p\text{-th power})$. So $\partial_{x_1} h = 0$, that is, $\partial_v h = 0$.

Part 4. For $n = 2$ and $v = e_1$, $\partial_x h = 0$ gives $h = \sum_j c_j x^{p j} y^{D - p j}$. Since $p \mid D$, $h$ is then a $p$-th power, which contradicts $\nabla h \ne 0$. At a smooth point of $f' = 0$ the equation after the translation has a linear term, which is in the part without $z$ and is not a $p$-th power, so $\nu = 1$. $\square$

The theorem does not say that $f'$ is Newton nondegenerate at $P_v$, and it does not say that a defect is a singular point and not a tangency, as in Example 3.3.42.

**Example 3.3.45 (the exception occurs).** Let $p = 5$, $n = 3$ and $g = h = y^4 w + y w^4 + x^5$. Then $\partial_x h = 0$ identically, and $\nabla h \ne 0$. For $v = e_1$ we have $y_0 = 0$, $\psi(y, w) = y^4 w + y w^4$ and $R = 0$, so $\nu(P_v) = 5 = D$. This is a trivial case, since $z \mapsto z - x$ removes $x^5$. For $g = y^4 w + y w^4 + x^5 + x^3 y^3$ we get $t R = t y^3$, so $g_v = y^4 w + y w^4 + t y^3$ and $\nu(P_v) = 4$. If $\partial_v h = 0$, then $v \in C$. It is not known if the set of the forms $h$ with $\partial_v h = 0$ for some $v$ has a high codimension.

To apply Theorem 3.3.44 to a general $f = z^p + g$, first make the change $z \mapsto z + q(x)$ that replaces $g$ by $g^{\mathrm{cl}}$. Then $\operatorname{ord} g = \nu$, the leading form has no monomial that is a $p$-th power, so $\nabla h \ne 0$. If $p \mid \nu$, one weighted blowup with the weights $(1, \dots, 1, \nu/p)$ lowers $\nu$ at each point over the origin, outside the points $P_v$ with $\partial_v h = 0$. For $n = 2$ this gives the step of an induction. For $n \ge 3$ the expected statement is the following.

**Conjecture 3.3.46.** Let $n \ge 3$, and let $f = z^p + g$ with $g \in k[[x_1, \dots, x_n]]$ and $\nu(f) \ge 2$. Then there is a finite sequence of weighted blowups such that at each step the largest residual order at the points of the strict transform over the origin goes down. In particular, after a finite number of steps the strict transform is smooth at each point over the origin.

Node: SG0000009E · Lean: none yet

It is not known if this is true. The missing parts are the case $p \nmid \nu$, the exceptional points of Theorem 3.3.44, and the termination.

### What is open

1. Conjecture 3.3.33 for $n \ge 3$ when $Q$ contains a line and $C$ is not in the union of $n$ hyperplanes with independent equations. For $n = 3$ the open case is that $Q$ contains a line and $C$ is infinite or not on three lines with no common point.
2. The nondegeneracy of all the faces after a preparation of the top face. This is open for $D = p$ and $n = 3$ when $C$ is on three lines with no common point, in particular when $|C| \le 4$, and for the weighted forms of Theorem 3.3.38. The computer searches of the research notes found degenerate lower faces after the preparation of the top face, which is numerical evidence that the preparation of the top face is not sufficient.
3. Theorem 3.3.35 with terms of higher order and a change of all coordinates whose linear part does not respect the weights. Proposition 3.3.36 gives the case where it does.
4. Theorem 3.3.38 for the weights that have no entry $1$ and an entry that is a combination of the other two, for example $(2, 3, 4)$, and a version for $n \ge 4$.
5. Conjecture 3.3.46. A part of it is the nondegeneracy of $f'$ at the points $P_v$ of Theorem 3.3.44, which Example 3.3.42 shows can fail by a tangency.

The result for the method is negative: preparation to a Newton nondegenerate form is not a general method for $z^p + g$, also when changes of all coordinates are allowed. Theorem 3.3.13 and Example 3.3.14 have Lean proofs. The other results of the last subsections are in the research notes, with referee reports, and they have no Lean proof yet. The examples marked as computer computations are numerical evidence, and no proof in this section depends on them, except the absence of lines in Example 3.3.32.

### Notes and references

The toric resolution of Newton nondegenerate hypersurfaces is due to Varchenko and Khovanskii in characteristic $0$. Its proof uses only toric geometry, so it works for the nondegeneracy of Definition 3.3.1 in each characteristic. So an equation $z^p + g$ that satisfies Theorem 3.3.3 after a change of coordinates and a cleaning has an embedded resolution by one toric modification near the origin, in each dimension, and Theorem 3.3.40 shows that convenience is not necessary. A version of Theorem 3.3.40 is standard in characteristic $0$ (Varchenko, Oka), and for characteristic $p$ there is work of Aroca, Gómez-Morales and Mourtada. The examples show that a change of the coordinates $x$ can be necessary. Theorems 3.3.16, 3.3.17, 3.3.22, 3.3.26, 3.3.31 and 3.3.35 show that for many resonant faces no change of coordinates helps. The results of the subsections on preparation, two variables, three variables and weighted blowups up to Theorem 3.3.43 are from research note 55 of the project, with the corrections of research note 60, which is a referee report on note 55. Note 60 found Theorem 3.3.17, the correct scope of Theorem 3.3.16, the set $Z_0$ of Proposition 3.3.20 and the word "transverse" in Proposition 3.3.41. The arc lemma, Proposition 3.3.25, Theorems 3.3.26, 3.3.31, 3.3.35, 3.3.38 and 3.3.44 and their corollaries are from research note 68, with the corrections of research note 70, which is a referee report on note 68. Note 70 found the bound of Proposition 3.3.27 and the statement and proof of Proposition 3.3.36. The case of the terms of low weight in the third component of $\Psi$ in that proof, Case 1, is added here. Lang's theorem on Frobenius semilinear maps is in the form of Katz. For the kangaroo phenomenon, see [Hau10].
