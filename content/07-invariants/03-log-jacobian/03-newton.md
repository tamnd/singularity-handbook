---
title: The Newton criterion for z^p + g
nodes: [SG0000003G, SG0000003H, SG0000008P, SG0000008Q, SG0000008R, SG0000008S, SG0000008T, SG0000008V, SG0000008W, SG0000008X, SG0000008Y, SG0000008Z]
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

Theorem 3.3.3 is a test in fixed coordinates. Example 3.3.9 shows that the test can fail although the zero set of $g$ is smooth in the torus. The natural question is whether a change of coordinates makes the equation nondegenerate. If it does, the toric resolution of Theorem 3.3.27 below resolves the hypersurface. This would be a direct method for $z^p + g$ in each dimension. In this subsection the answer is no for a large class of $g$, and for each kind of change of coordinates when the degree of $g$ is more than $p$. Here $k$ is an algebraically closed field of characteristic $p$, and $g \in k[[x_1, \dots, x_n]]$ is a series. Definition 3.3.1 applies to a series, since the initial form of a series for a positive weight is a polynomial.

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

When $D = p$, the form of degree $p$ of $F = z^p + g$ is $z^p + h$, which is not a $p$-th power, and Step 1 of the proof of Theorem 3.3.17 fails. The singular points of the cone $z^p + h = 0$ in $\mathbb{P}^n$ are the points $(v : c)$ with $v \in C$ and $c^p = -h(v)$, one over each point of $C$. For $n = 2$ and three points of $C$ these are three points of $\mathbb{P}^2$. If they are not on one line, a linear change of $(x, y, z)$ moves them to the coordinate points, and then the face of the weight $(1, 1, 1)$ has no torus singular point. So the obstruction of Theorem 3.3.16 does not apply to the changes of all coordinates.

**Conjecture 3.3.24.** Theorem 3.3.17 holds also for $D = p$.

Node: SG0000008Z · Lean: none yet

This is the expected answer, but it is not known if it is true.

**Example 3.3.25.** Let $p = 5$ and $h = 2 x^2 y^2 (x + y)$. Then $\partial_x h = x y^2 (x - y)$ and $\partial_y h = x^2 y (y - x)$, so $C = \{(1 : 0), (0 : 1), (1 : 1)\}$, and $h(1, 1) = 4 \ne 0$. By Proposition 3.3.18, no change $(\varphi, q)$ makes $z^5 + h$ nondegenerate. The change $x = X + Z$, $y = Y + Z$, $z = Z$ gives a form of degree $5$ with $12$ monomials, none of them in $k[X^5, Y^5, Z^5]$. A computation of the research notes shows that of the $13$ faces of its Newton polyhedron, the face of the weight $(1, 1, 1)$ has no torus singular point, and exactly three edges are degenerate, among them $2 X^3 (Y + Z)^2$. The same occurs for $z^5 + x^4 y + x y^4$ and the linear changes of all coordinates. It is not known if a change of all coordinates that is not linear makes these equations nondegenerate.

### Toric resolution without convenience

The theorem of Varchenko and Khovanskii is usually stated for a *convenient* polynomial, one whose Newton polyhedron meets each coordinate axis. An equation $z^p + g$ with a singular locus of positive dimension is not convenient in general. The next theorem removes this hypothesis near the origin.

**Theorem 3.3.26.** Let $k$ be a perfect field and let $F \in k[x_1, \dots, x_m]$ with $F \ne 0$ and $F(0) = 0$ be Newton nondegenerate over an algebraic closure of $k$. Let $\Sigma$ be a regular fan with the support $\mathbb{R}_{\ge 0}^m$ that refines the normal fan of $N(F)$, and let $\pi \colon X_\Sigma \to \mathbb{A}^m$ be the toric morphism. Then there is a Zariski open neighbourhood $U$ of $0$ such that over $U$ the total transform of $F$ has simple normal crossings. Locally $\pi^* F = y^\mu \tilde F$, where $\tilde F = 0$ is smooth and transverse to the toric boundary, and $\tilde F = 0$ is the strict transform of the closure of $\{F = 0\} \cap T$.

Node: SG0000008W · Lean: none yet

*Proof.* We can work over the algebraic closure, since smoothness and normal crossings descend. Take a maximal cone of $\Sigma$ with the primitive generators $v^1, \dots, v^m$, a basis of $\mathbb{Z}^m$. The chart has the coordinates $y_1, \dots, y_m$ and $x_i = \prod_j y_j^{v^j_i}$, so $x^a = \prod_j y_j^{\langle v^j, a \rangle}$. Let $\mu_j = m_{v^j}(F)$. Then $\pi^* F = y^\mu \tilde F$ with $\tilde F = \sum_a c_a \prod_j y_j^{\langle v^j, a \rangle - \mu_j}$. No $y_j$ divides $\tilde F$, because the face of $v^j$ has an exponent with $\langle v^j, a \rangle = \mu_j$, and distinct exponents give distinct monomials, since the matrix $(v^j_i)$ is unimodular. So $\tilde F = 0$ has no component in the boundary.

Let $P$ be a point of the chart with $\pi(P) = 0$ and $\tilde F(P) = 0$, and let $J = \{ j : y_j(P) = 0 \}$. For each $i$ some $j \in J$ has $v^j_i > 0$, since $x_i(P) = 0$. So $\sum_{j \in J} v^j$ has positive entries, and its face $\Delta$ of $N(F)$ is compact. The cone of the $v^j$ with $j \in J$ is in one cone of the normal fan, so an exponent $a$ has $\langle v^j, a \rangle = \mu_j$ for each $j \in J$ exactly when $a \in \Delta$. So $\tilde F$ restricted to $y_J = 0$ is $Q = \sum_{a \in \Delta} c_a \prod_{l \notin J} y_l^{\langle v^l, a \rangle - \mu_l}$, and the same computation gives $F_\Delta \circ \pi = y^\mu Q$, with $Q$ independent of $y_J$.

Assume that $\partial_{y_l} Q(P) = 0$ for each $l \notin J$. Let $P'$ be the torus point with $y_j(P') = 1$ for $j \in J$ and $y_l(P') = y_l(P)$ for $l \notin J$. Then $Q(P') = 0$, and each partial derivative of $Q$ is $0$ at $P'$. By the product rule, $y^\mu Q = F_\Delta \circ \pi$ and its partial derivatives are $0$ at $P'$. Since $\pi$ is an isomorphism of the tori, $\pi(P')$ is a torus singular point of $F_\Delta = 0$, which contradicts the nondegeneracy. So $\partial_{y_l} Q(P) \ne 0$ for some $l \notin J$, and $\partial_{y_l} \tilde F(P) = \partial_{y_l} Q(P)$, because $\tilde F - Q$ is in the ideal $(y_j : j \in J)$. So $\tilde F = 0$ is smooth at $P$, and the differentials $d y_j$ for $j \in J$ and $d \tilde F$ are independent at $P$.

Let $B$ be the closed set of the points of $\tilde F = 0$ where this fails. It does not meet $\pi^{-1}(0)$. The support of $\Sigma$ is the whole orthant, so $\pi$ is proper, $\pi(B)$ is closed, and $U = \mathbb{A}^m \setminus \pi(B)$ is the neighbourhood. $\square$

The components of $F = 0$ in the coordinate hyperplanes become boundary divisors. Convenience makes $\pi$ an isomorphism outside $0$ for an isolated singularity, but it is not necessary for the normal crossings near $\pi^{-1}(0)$. The proof uses only the Jacobian criterion and the properness of $\pi$, so it works in each characteristic.

### Weighted blowups

A degenerate face of the third kind of Lemma 3.3.2 can be localized by one weighted blowup. Let $f = z^p + g$, let $w > 0$, let $m = m_w(g) \ge 1$, let $\sigma$ be the face of $w$, and let $W = (p w, m)$, divided by the gcd of its entries.

**Proposition 3.3.27.** In each regular fan that contains the ray of $W$ and refines the normal fan of $N(f)$, the points of the open orbit of the divisor $E_W$ where the strict transform is singular or not transverse to $E_W$ correspond to the torus orbits of the torus critical points $v$ of $g_\sigma$ with $g_\sigma(v) \ne 0$. If $g = g_\sigma$, these points are singular points of the strict transform.

Node: SG0000008V · Lean: none yet

*Proof.* Take $J = \{j\}$ in the proof of Theorem 3.3.26, with $v^j$ the primitive vector of $W$. The face of $W$ is of the third kind, with the initial form $z^p + g_\sigma$. Write $\tilde F = Q + y_j R$. As in that proof, $\tilde F$ is not smooth and transverse to $y_j = 0$ at a point $P$ of the open orbit if and only if $Q(P) = 0$ and $\nabla Q(P) = 0$. On the torus the steps are reversible, so this holds if and only if the corresponding torus point is a singular point of $z^p + g_\sigma$. By the proof of Theorem 3.3.3 these are the points $(v, c)$ with $v$ critical and $c^p = -g_\sigma(v) \ne 0$. If $g = g_\sigma$, then $f$ is weighted homogeneous for $W$, so $R = 0$ and $\tilde F = Q$. $\square$

**Example 3.3.28.** The word "transverse" is necessary. Let $p = 3$ and $f = z^3 + x^2 y + x y^2 + y^4$. For $W = (1, 1, 1)$ the face is $z^3 + x y (x + y)$, which is degenerate along $(s, s, s)$ by Example 3.3.9. In the chart $y = x t$, $z = x z'$ of the blowup of the origin, $f = x^3 (z'^3 + t + t^2 + x t^4)$. At $P = (x, t, z') = (0, 1, 1)$ the strict transform $\tilde F = z'^3 + t + t^2 + x t^4$ has $\tilde F(P) = 0$ and $\nabla \tilde F(P) = (1, 0, 0)$. So the strict transform is smooth at $P$, but it is tangent to $E_W = \{x = 0\}$, and only its restriction $z'^3 + t + t^2$ to $E_W$ is singular.

Node: SG0000008V · Lean: none yet

In two variables one weighted blowup turns a homogeneous equation into nondegenerate singularities.

**Theorem 3.3.29.** Let $h \in k[x, y]$ be a form of degree $D$ with $p \mid D$ and $\nabla h \ne 0$, and let $f = z^p + h$. Let $\pi$ be the weighted blowup with the weights $(1, 1, D/p)$. Then the strict transform of $f = 0$ is in the $x$-chart and the $y$-chart, and at each of its singular points it is, in suitable coordinates, $\{ z^p + s^e u(s) = 0 \} \times \mathbb{A}^1$ with $u(0) \ne 0$, $p \nmid e$ and $2 \le e \le D$. These germs are Newton nondegenerate and convenient in $(s, z)$, so a toric modification resolves each of them.

Node: SG0000008X · Lean: none yet

*Proof.* In the $x$-chart, $y = x t$ and $z = x^{D/p} z'$, and $f = x^D (z'^p + \varphi(t))$ with $\varphi(t) = h(1, t)$. The strict transform $z'^p + \varphi(t)$ does not contain $x$, so it is a curve times a line. It is singular at $(t_0, z_0)$ exactly when $\varphi'(t_0) = 0$ and $z_0^p = -\varphi(t_0)$. Let $z' = z'' + z_0$ and $t = t_0 + s$. The equation becomes $z''^p + \psi(s)$ with $\psi(s) = \varphi(t_0 + s) - \varphi(t_0)$ of order at least $2$. A change $z'' \mapsto z'' + r(s)$ removes the $p$-th powers of $\psi$, and what is left is $s^e u(s)$ with $p \nmid e$. The exception is a $\psi$ that is a $p$-th power. Then $\varphi' = 0$, so $\partial_y h = 0$, since $\partial_y h = x^{D-1} \varphi'(y/x)$, and then $\partial_x h = 0$ by the Euler identity, which is excluded. The order $e$ is at least $2$ and at most $\deg \varphi \le D$. The face $z^p + u(0) s^e$ has $\partial_s \ne 0$ on the torus, so it is nondegenerate, and the vertices are not $p$-th powers. The $y$-chart is the same with the roles of $x$ and $y$ exchanged. In the $z$-chart, at the point $x = y = 0$ of the exceptional divisor the strict transform is $1 + h(\cdot) \ne 0$, so the strict transform is in the other two charts. $\square$

For $z^5 + x^4 y + x y^4$ the three critical directions give $e = 2$. So one weighted blowup and three toric modifications resolve it, while no change $(\varphi, q)$ makes it nondegenerate.

### What is open

1. Conjecture 3.3.24, the case $D = p$. The first test cases are $z^5 + x^4 y + x y^4$ and $z^5 + 2 x^2 y^2 (x + y)$.
2. Theorem 3.3.29 for $g = h + (\text{terms of higher order})$. Then the strict transform $z'^p + \varphi(t) + x r(x, t)$ is not a product, and Example 3.3.28 shows that the defect after one weighted blowup can be a tangency. A measure for the defect that goes down after a weighted blowup is not known for $n \ge 3$, where the critical locus of a face can have positive dimension.
3. Whether a change that does not keep the weight prepares Example 3.3.21.
4. Whether the condition of Theorem 3.3.16 is also sufficient for all the faces when $n = 3$. The lab of the research notes tested this for small $p$ and $D$, and some cases are not decided.

The result for the method is negative: preparation to a Newton nondegenerate form is not a general method for $z^p + g$. Theorem 3.3.13 and Example 3.3.14 have Lean proofs. The other results of the last subsections are in the research notes, with a referee report, and they have no Lean proof yet.

### Notes and references

The toric resolution of Newton nondegenerate hypersurfaces is due to Varchenko and Khovanskii in characteristic $0$. Its proof uses only toric geometry, so it works for the nondegeneracy of Definition 3.3.1 in each characteristic. So an equation $z^p + g$ that satisfies Theorem 3.3.3 after a change of coordinates and a cleaning has an embedded resolution by one toric modification near the origin, in each dimension, and Theorem 3.3.26 shows that convenience is not necessary. A version of Theorem 3.3.26 is standard in characteristic $0$ (Varchenko, Oka), and for characteristic $p$ there is work of Aroca, Gómez-Morales and Mourtada. The examples show that a change of the coordinates $x$ can be necessary. Theorems 3.3.16, 3.3.17 and 3.3.22 show that for many resonant faces no change of coordinates helps. The results of the last subsections are from research note 55 of the project, with the corrections of research note 60, which is a referee report on note 55. Note 60 found Theorem 3.3.17, the correct scope of Theorem 3.3.16, the set $Z_0$ of Proposition 3.3.20 and the word "transverse" in Proposition 3.3.27. Lang's theorem on Frobenius semilinear maps is in the form of Katz. For the kangaroo phenomenon, see [Hau10].
