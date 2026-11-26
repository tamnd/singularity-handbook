---
title: Runs that follow no curve
nodes: [SG0000005K]
sources: [CP19, CJS20, Hir64, Chr79]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs that follow no curve

Hypothesis 3.12.5 says that each infinite run follows a formal curve along which the order of $G$ is at least $\rho$. In this section we prove the hypothesis in two variables, and we prove its second half in each dimension: if an infinite run follows a regular formal curve, then the order of $G$ along the curve is $\rho$ or $\rho + 1$. Then we show that the first half is false in three variables. An infinite run can take the corner of two components of the divisor at each step, and such a run follows no formal curve. It lies on a surface. Last, we give the example of Cossart and Piltant in our setting. There the run follows a formal curve, but the curve is transcendental, and its Zariski closure is a plane. So in each form of the hypothesis that can give the centers of a resolution, the curve must be replaced by a subvariety of positive dimension, and the centers of the resolution can be surfaces. We state this form as Hypothesis 3.13.10, and we isolate the open step as Question 3.13.11.

We use the setting and the notation of Sections 3.8 to 3.12. So $K$ is an algebraically closed field of characteristic $p$, $g = x^r G$ is clean for the divisor $\Delta$, $d = \operatorname{ord} G$, $\rho = \rho(g)$, and $\sigma \in \{\rho, \rho + 1\}$ is the order of $\widetilde\Theta_0(G)$. By Theorem 3.1.4, part 1, $x^r$ is the largest monomial in the variables of $\Delta$ that divides $g$, so no $x_i$ with $i \in \Delta$ divides $G$. We write $J = \widetilde\Theta(G)$ and $J^0 = \widetilde\Theta_0(G)$, and we recall that $\mathfrak{m} J \subseteq J^0 \subseteq J$. In the formal ring $K[[x]]$ the number $\rho$ does not depend on the coordinates, if the components of $\Delta$ are coordinate hyperplanes, because $\Theta(g)$ does not depend on them (Section 3.6). So we can change the coordinates at each point of a run.

### The order along a subvariety

Example 3.12.4 measures the order of $G$ along the $x$-axis, and the cleaning of $g$ is in the given coordinates. This is not intrinsic. A cleaning in other coordinates gives a different $G$, and the order along a curve can change. So we first define an order that does not depend on the coordinates.

The *class* of a monomial $x^a$ is the vector $a$ modulo $p$ in $(\mathbb{Z} / p)^n$. A series is clean if no monomial of class $0$ occurs in it. Each series $f$ is $f = F + H^p$ in a unique way with $F$ clean, since $K$ is perfect. We write $F = \operatorname{cl}(f)$. This series depends on the coordinates.

**Lemma 3.13.1.** Let $Z = V(y_1, \dots, y_c)$ in the coordinates $(w, y)$ at $P$, and let $f \in K[[w, y]]$. Then the largest value of $\operatorname{ord}_Z(f + h^p)$ for $h \in K[[w, y]]$ is $\operatorname{ord}_y \operatorname{cl}(f)$. The largest value is the same if $h$ is in the local ring of $K[[w, y]]$ at the prime ideal $I_Z$.

*Proof.* Let $F = \operatorname{cl}(f)$ and $e = \operatorname{ord}_y F$. Then $f + h^p = F + Q$ with $Q = H^p + h^p$, and $Q$ has only monomials of class $0$. The part of $F + Q$ of degree $e$ in $y$ is $F_e + Q_e$. Here $F_e \ne 0$ has no monomial of class $0$, and $Q_e$ has only monomials of class $0$. So $F_e + Q_e \ne 0$, and $\operatorname{ord}_Z(f + h^p) \le e$. The choice $h = -H$ gives the value $e$. For the second claim, let $h = a / b$ with $b \notin I_Z$. Then $\operatorname{ord}_Z(f + h^p) = \operatorname{ord}_Z(b^p f + a^p)$. The multiplication by $b^p$ keeps the class of each monomial, so $\operatorname{cl}(b^p f) = b^p F$. Also $\operatorname{ord}_y(b^p F) = e$, because $b$ is a unit in the local ring at $I_Z$. Now apply the first claim to $b^p f$. $\square$

**Definition 3.13.2.** Let $Z$ be a regular formal subvariety through $P$. The *clean order* of $g$ along $Z$ is $\bar\nu_Z(g) = \max_h \operatorname{ord}_Z(g + h^p)$. The *order of $G$ along $Z$* is
$$\nu^G_Z(P) = \bar\nu_Z(g) - \sum_{i \in \Delta,\ Z \subseteq V(x_i)} r_i,$$
where the sum is over the components of $\Delta$ that contain $Z$.

The clean order does not depend on the coordinates, by its definition. The entries $r_i$ do not depend on the coordinates, because $x^r$ is the largest monomial factor of $\Theta(g)$. So $\nu^G_Z$ is intrinsic. If the coordinates are adapted to $Z$ and $\Delta$, that is, $Z = V(y)$ and each component of $\Delta$ that contains $Z$ is some $V(y_i)$, and if $g$ is cleaned in these coordinates, then Lemma 3.13.1 gives $\nu^G_Z = \operatorname{ord}_Z G$. The second claim of the lemma says that a cleaning at the generic point of $Z$ does not give a larger order. This was a gap of the tests of Section 3.12.

In Example 3.12.4 the coordinates are adapted to the $x$-axis $\gamma$ and to $\Delta = \{x, z\}$. The clean order is $\operatorname{ord}_\gamma g_0 = 5$, and the only component of $\Delta$ that contains $\gamma$ is $z = 0$, with $r_z = 2$. So $\nu^G_\gamma = 3 = \rho$, as in part 3 of the example.

**Remark 3.13.3.** Hypothesis 3.12.5 needs two corrections.

1. *The runs with $\rho = 0$.* Let $\Delta = \{x, y\}$ and $g = x^{p+1} y^{p+1}$. Then $G = 1$ and $\rho = 0$. The $x$-chart at the origin sends $x^a y^b$ to $x^{a + b - p} y^b$, and the $y$-chart sends it to $x^a y^{a + b - p}$. Modulo $p$ both maps are invertible on the exponent vectors, so the class never becomes $0$. Thus $g$ stays clean, $G = 1$ and $\rho = 0$ at each point of each sequence of these charts. The sequence that takes the two charts in turn follows no formal curve, by Lemma 3.13.5 below. So the hypothesis must assume $\rho \ge 1$. This is not a loss, since a point with $\rho = 0$ is monomial by Section 3.5.
2. *The order of the given $G$.* Let $p = 3$, $\Delta = \{y\}$ and $g = x^5 y + 2 x^4 y^2 + x^2 y^4 + 2 x y^5$. With $X = x + y$, an expansion over $\mathbb{F}_3$ gives $g = y X^5 - y^3 X^3$. In the coordinates $(x, y)$, $g$ is clean, $r = (0, 1)$ and $G = X^3 (X^2 - y^2)$, so $d = 5$ and $\rho = 4$. In the coordinates $(X, y)$ the monomial $y^3 X^3$ is a cube, so $\operatorname{cl}(g) = y X^5$. The $y$-chart at the origin in the coordinates $(X, y)$ sends $y^a X^5$ to $y^{a + 2} X^5$, so the run of these charts has the points $y^{2k+1} X^5$ with $G_k = X^5$ and $\widetilde\Theta(G_k) = (X^4)$. Thus $\rho = 4$ at each point, and the run follows the curve $\gamma = V(X)$. Here $\nu^G_\gamma = 5 \ge \rho$. But the $G$ of the coordinates $(x, y)$ is in $I_\gamma^3$ and not in $I_\gamma^4$. So the condition $G \in I_\gamma^\rho$ of Hypothesis 3.12.5 depends on the coordinates of the cleaning, and the right condition is $\nu^G_\gamma \ge \rho$.

### Corner steps

Let $P_0, P_1, \dots$ be a run, and let $E_k$ be the exceptional divisor of the blowup that gives $P_k$, for $k \ge 1$. For $k \ge 1$ the step from $P_k$ to $P_{k+1}$ is a *corner step* if $P_{k+1}$ is on the strict transform of $E_k$. Let $\gamma$ be a formal curve at $P_N$. The run *follows* $\gamma$ from $P_N$ if $P_k$ is on the strict transform $\gamma_k$ of $\gamma$ for each $k \ge N$.

**Lemma 3.13.4.** Let $\gamma$ be a regular formal curve at $P_N$, and assume that the run follows $\gamma$ from $P_N$.

1. For $k \ge N + 1$, $\gamma_k$ is regular and transversal to $E_k$, and the step from $P_k$ to $P_{k+1}$ is not a corner step.
2. Each component $D$ of the divisor that does not contain $\gamma_k$ is not at $P_l$ for $l$ large.
3. There is an $M \ge N$ such that for each $k \ge M$, the components of the divisor at $P_k$ are $E_k$ and the strict transforms of the components that contain $\gamma$.

*Proof.* The strict transform of a regular curve under the blowup of a point of the curve is regular, and it meets the exceptional divisor transversally at one point. This gives the first claim of part 1. Let $D$ be a regular hypersurface that does not contain $\gamma_k$. The intersection number of $\gamma_k$ and $D$ at $P_k$ is finite, and it is positive if $P_k \in D$. At each step that stays on both, it goes down by the product of the multiplicities of $\gamma_k$ and of $D$ at $P_k$, that is, by $1$. This gives part 2. For $D = E_k$ the number is $1$, so $P_{k+1}$ is not on the strict transform of $E_k$. This is the second claim of part 1. Part 3 follows from part 2, because only a finite number of components pass through $P_N$, and each new component is an $E_k$, which is not at $P_{k+1}$ by part 1. $\square$

**Lemma 3.13.5.** Let $N \ge 1$, and assume that no step from $P_k$ to $P_{k+1}$ with $k \ge N$ is a corner step. Then the run follows a regular formal curve at $P_N$ that is transversal to $E_N$. So an infinite run follows a formal curve if and only if it has only a finite number of corner steps.

*Proof.* Take coordinates $(u, w_2, \dots, w_n)$ at $P_N$ with $E_N = V(u)$. The points of $E_{N+1}$ that are not on the strict transform of $E_N$ are the points of the $u$-chart $\pi(u) = u$, $\pi(w_i) = u (w_i + t_i)$, and in this chart $E_{N+1} = V(u)$ again. By induction each step is a $u$-chart with a translation $t^{(k)} \in K^{n-1}$, and the coordinates satisfy $w^{(k)} = u (w^{(k+1)} + t^{(k)})$. Let $\varphi(u) = \sum_{k \ge N} t^{(k)} u^{k - N + 1}$ and $\gamma = V(w - \varphi(u))$. This curve is regular and transversal to $V(u)$. Its strict transform at step $k$ is $V(w^{(k)} - \sum_{j \ge k} t^{(j)} u^{j - k + 1})$, and it passes through the origin of the chart, that is, through $P_k$. For the second claim, if the run follows a singular formal curve, then after a finite number of point blowups its strict transform is regular, and part 1 of Lemma 3.13.4 applies. $\square$

### The second half of the hypothesis

**Theorem 3.13.6.** Let $P_0, P_1, \dots$ be an infinite run, and assume that it follows a regular formal curve $\gamma$ from $P_N$. Then:

1. $\bar\nu_{\gamma_k}(g_k) \ge p$ for each $k \ge N$. So the generic point of $\gamma$ is in the locus where the multiplicity of $z^p + g$ is $p$.
2. The numbers $\bar\nu_{\gamma_k}(g_k)$ and $\nu^G_{\gamma_k}(P_k)$ do not depend on $k \ge N$.
3. $\nu^G_{\gamma_N}(P_N) \in \{\rho, \rho + 1\}$.

*Proof.* Step 1, one blowup. Let $k \ge N$. Take coordinates $(x, y_2, \dots, y_n)$ at $P_k$ with $\gamma_k = V(y)$. The point $P_{k+1}$ is the point of $\gamma_{k+1}$ on the exceptional divisor, that is, the origin of the $x$-chart $\pi(x) = x$, $\pi(y) = x y'$, and $\gamma_{k+1} = V(y')$. Write $g_k = F + H^p$ with $F = \operatorname{cl}(g_k)$. Then
$$x^{-p} \pi(g_k) = x^{-p} \pi(F) + \bigl(x^{-1} \pi(H)\bigr)^p.$$
The map $x^a y^\beta \mapsto x^{a + |\beta| - p} y^\beta$ sends a monomial of class $0$ to a monomial of class $0$, and a monomial of another class to a monomial of another class, since $|\beta| \equiv 0$ if $\beta \equiv 0$. So the two terms on the right have disjoint supports, and each of them is a power series. The first term is clean, so it is the clean part of $g_{k+1}$ in the coordinates $(x, y')$. The map keeps $\beta$, so $\operatorname{ord}_{y'} \operatorname{cl}(g_{k+1}) = \operatorname{ord}_y F$, and Lemma 3.13.1 gives $\bar\nu_{\gamma_{k+1}}(g_{k+1}) = \bar\nu_{\gamma_k}(g_k)$.

Step 2, part 1. Repeat Step 1 from $P_N$ in the same coordinates. After $m$ steps the monomial $x^a y^\beta$ of $F$ goes to $x^{a + m (|\beta| - p)} y^\beta$, and distinct monomials go to distinct monomials. So no two terms cancel, and the exponent $a + m (|\beta| - p)$ is not negative for each $m$. Thus $|\beta| \ge p$ for each monomial of $F$.

Step 3, part 2. For $k \ge N$ the curve $\gamma_{k+1}$ is transversal to $E_{k+1}$, by part 1 of Lemma 3.13.4, so the components of the divisor at $P_{k+1}$ that contain $\gamma_{k+1}$ are the strict transforms of the components at $P_k$ that contain $\gamma_k$. If such a component is $V(y_i)$, then $\pi(y_i^{r_i}) = x^{r_i} y_i'^{r_i}$, so the entry of $r$ for its strict transform is $r_i$ again. With Step 1 this gives part 2.

Step 4, part 3. Take $M$ as in part 3 of Lemma 3.13.4, with $M \ge N + 1$. At $P_M$ take coordinates $(x, y)$ adapted to $E_M$, $\gamma_M$ and the divisor: $E_M = V(x)$, $\gamma_M = V(y)$, and the components that contain $\gamma_M$ are the $V(y_i)$ for $i$ in a set $S$. These coordinates exist. By the normal crossings, the differentials $dx$ and $dy_i$ for $i \in S$ are independent. The $dy_i$ are zero on the tangent line of $\gamma_M$, and $dx$ is not, since $\gamma_M$ is transversal to $E_M$. So we can complete them to coordinates in which $\gamma_M = V(y)$. In these coordinates each later step is the $x$-chart at the origin, and the coordinates stay adapted. Clean $g_M$ in these coordinates, and write $g_M = x^a y_S^{r_S} G_M$. Then $x$ and the $y_i$ for $i \in S$ do not divide $G_M$, and $e = \operatorname{ord}_y G_M$ is $\nu^G_{\gamma_M}(P_M)$. By Step 1 no cleaning is necessary at the later steps, so the series $G_{M+m}$ of $P_{M+m}$ is $G_M(x, x^m y)$ divided by the largest power $x^c$ that divides it. A monomial $x^a y^\beta$ of $G_M$ goes to $x^{a + m |\beta| - c} y^\beta$. Let $a_0$ be the smallest $a$ among the monomials of $G_M$ with $|\beta| = e$. For $m > a_0$, the monomials with $|\beta| > e$ have $a + m |\beta| > a_0 + m e$, so $c = a_0 + m e$. Then the monomials with $|\beta| = e$ and $a = a_0$ go to monomials of degree $e$, and the other monomials go to monomials of degree more than $e$. So $d(P_{M+m}) = \operatorname{ord} G_{M+m} = e$. By Theorem 3.1.4, part 2, $d(P_{M+m}) \in \{\rho, \rho + 1\}$. So $e \in \{\rho, \rho + 1\}$, and part 2 gives the same value at $P_N$. $\square$

The proof shows the mechanism. The order of $G$ at the point is bounded by $\rho + 1$, and along the run it converges to the order of $G$ along the curve. So the order along the curve is at least $\rho$, and the second half of Hypothesis 3.12.5 holds in each dimension, with $\nu^G_\gamma$ in place of the order of the given $G$. Only the existence of the curve is not automatic.

### Two variables

In this subsection $n = 2$ and $\rho \ge 1$. For an ideal $I$ and a regular curve $E$ through $P$, let $i(I, E)$ be the order at $P$ of the restriction of $I$ to $E$. Then $i(I, E) \ge \operatorname{ord} I$. We write $J_k$ and $J^0_k$ for the ideals $J$ and $J^0$ at $P_k$, and $\sigma_k$ for the order of $J^0_k$.

**Lemma 3.13.7.** Let $k \ge 1$.

1. $i(J_k, E_k) = \rho$.
2. If the step from $P_k$ to $P_{k+1}$ is a corner step, then $i(J_{k+1}, E'_k) = i(J^0_k, E_k) - \sigma_k$, where $E'_k$ is the strict transform of $E_k$.

*Proof.* Part 1. Let $\sigma = \sigma_{k-1}$, and take coordinates at $P_{k-1}$ where the step is the chart $\pi(x_1) = x_1$, $\pi(x_2) = x_1 (x_2 + t)$, with the vector $v = (1, t)$. Then $E_k = V(x_1)$, and $J_k = x_1^{-\sigma} \pi(J^0_{k-1})$ by Theorem 3.2.3 and the proof of Proposition 3.8.2. For $f$ of order at least $\sigma$, the restriction of $x_1^{-\sigma} \pi(f)$ to $x_1 = 0$ is $\operatorname{in}_\sigma(f)(1, x_2 + t)$, where $\operatorname{in}_\sigma(f)$ is the part of degree $\sigma$ of $f$. In the case $\sigma = \rho$, take $h \in J^0_{k-1}$ of order $\rho$. In the case $\sigma = \rho + 1$, take $h \in J_{k-1}$ of order $\rho$. In both cases Theorem 3.7.1 gives $v \in T(\operatorname{in}(h))$. In two variables this means that $\operatorname{in}(h) = c \ell^\rho$, where $c \ne 0$ and $\ell$ is a linear form with $\ell(v) = 0$. Then $\ell(1, x_2 + t) = \lambda x_2$ with $\lambda \ne 0$, since $\ell \ne 0$. In the first case the restriction of $x_1^{-\rho} \pi(h)$ is $c \lambda^\rho x_2^\rho$. In the second case $x_1 h \in \mathfrak{m} J_{k-1} \subseteq J^0_{k-1}$, and the restriction of $x_1^{-\rho - 1} \pi(x_1 h)$ is $c \lambda^\rho x_2^\rho$ again. So $i(J_k, E_k) \le \rho$, and the other inequality holds since $\operatorname{ord} J_k = \rho$.

Part 2. Take coordinates $(u, w)$ at $P_k$ with $E_k = V(u)$. The corner point is the origin of the $w$-chart $\pi(u) = w u'$, $\pi(w) = w$, and $E'_k = V(u')$. On $u' = 0$ the map $\pi$ is the identity $w \mapsto w$ from $E'_k$ to $E_k$. So the restriction of $J_{k+1} = w^{-\sigma_k} \pi(J^0_k)$ to $E'_k$ is $w^{-\sigma_k}$ times the restriction of $J^0_k$ to $E_k$. $\square$

**Theorem 3.13.8.** Let $n = 2$, and let $P_0, P_1, \dots$ be an infinite run with $\rho \ge 1$. Then no step from $P_k$ to $P_{k+1}$ with $k \ge 1$ is a corner step. So the run follows a regular formal curve $\gamma$ from $P_0$, the curve $\gamma$ is not a component of $\Delta$, and $\nu^G_\gamma(P_0) = \bar\nu_\gamma(g_0) \in \{\rho, \rho + 1\}$.

*Proof.* Step 1. Assume that the step from $P_k$ to $P_{k+1}$ is a corner step with $k \ge 1$. Since $\mathfrak{m} J_k \subseteq J^0_k$, part 1 of Lemma 3.13.7 gives $i(J^0_k, E_k) \le \rho + 1$. By part 2,
$$\rho = \operatorname{ord} J_{k+1} \le i(J_{k+1}, E'_k) = i(J^0_k, E_k) - \sigma_k \le \rho + 1 - \sigma_k.$$
So $\sigma_k \le 1$. Since $\sigma_k \ge \rho \ge 1$, we get $\rho = \sigma_k = 1$ and $i(J^0_k, E_k) = 2$. If both coordinates are in the divisor at $P_k$, then $J^0_k = J_k$, and $i(J^0_k, E_k) = \rho = 1$ by Lemma 3.13.7. This is false, so the divisor at $P_k$ is $\{E_k\}$.

Step 2. Thus the divisor is $V(u)$, with the entry $r$, and $w$ is free. Then $J_k = (r G + u \partial_u G, \partial_w G)$ and $J^0_k = (r G + u \partial_u G) + \mathfrak{m} (\partial_w G)$. If $d = 2$, then $J^0_k$ has order at least $2$, against $\sigma_k = 1$. So $d = 1$. If the coefficient of $w$ in $G$ is not $0$, then $\partial_w G$ is a unit and $\rho = 0$. So $G = \alpha u + c_2 w^2 + G_2$, where $G_2$ has order at least $2$ and no monomial $w^2$. The linear part of $r G + u \partial_u G$ is $(r + 1) \alpha u$, and $\sigma_k = 1$ gives $\alpha \ne 0$ and $r + 1 \not\equiv 0$. On $u = 0$, the element $r G + u \partial_u G$ restricts to $r c_2 w^2 + \dots$, and the elements of $\mathfrak{m} (\partial_w G)$ restrict to multiples of $w \partial_w G|_{u = 0} = 2 c_2 w^2 + \dots$. So $i(J^0_k, E_k) = 2$ gives $c_2 \ne 0$, and $r \not\equiv 0$ or $p \ne 2$. If $p = 2$, then $r \not\equiv 0$ and $r + 1 \not\equiv 0$ modulo $2$, which is false. So $p$ is odd.

Step 3. The corner step. We have $g_{k+1} = w^{-p} (w u')^r G(w u', w)$. A monomial $u^a w^b$ of $G$ goes to $u'^a w^{a + b}$, so $G(w u', w) = w (\alpha u' + c_2 w + \dots)$, where the dots have order at least $2$. Thus $g_{k+1} = u'^r w^{r + 1 - p} G'$ with $G' = \alpha u' + c_2 w + \dots$. The two monomials of $g_{k+1}$ that come from the linear part of $G'$ are $u'^{r+1} w^{r+1-p}$ and $u'^r w^{r+2-p}$. The first is not of class $0$, since $r + 1 \not\equiv 0$. The second is not of class $0$: if $r \not\equiv 0$, its exponent of $u'$ is not $0$ modulo $p$, and if $r \equiv 0$, its exponent of $w$ is $r + 2 - p \not\equiv 0$, since $p$ is odd. So the cleaning does not change the linear part of $G'$. The divisor at $P_{k+1}$ is $\{u', w\}$ with the entries $a = r$ and $b = r + 1 - p$.

Step 4. At $P_{k+1}$ both coordinates are in the divisor, so $J_{k+1} = (a G' + u' \partial_{u'} G', b G' + w \partial_w G')$. The linear parts of the two generators are $(a + 1) \alpha u' + a c_2 w$ and $b \alpha u' + (b + 1) c_2 w$. Their determinant is $\alpha c_2 \bigl((a + 1)(b + 1) - a b\bigr) = \alpha c_2 (a + b + 1)$, and $a + b + 1 = 2 r + 2 - p \equiv 2 (r + 1) \not\equiv 0$. So $J_{k+1}$ contains two independent linear forms, $\rho(P_{k+1}) = 1$ and $T_\rho(P_{k+1}) = 0$. By Corollary 3.7.2, $\rho$ goes down at each point over $P_{k+1}$, and the run is finite. This is a contradiction.

Step 5. By Lemma 3.13.5 with $N = 1$, the run follows a regular formal curve $\gamma_1$ at $P_1$ that is transversal to $E_1$. In the chart of the first step, a curve $x_2 = \psi(x_1)$ transversal to $V(x_1)$ is the strict transform of the curve $x_2 = x_1 (\psi(x_1) + t)$, which is regular. So the run follows a regular curve $\gamma$ from $P_0$. The proof of Theorem 3.13.6 holds from $k = 0$ for this curve, since Steps 1 and 3 use only that $\gamma_k$ is regular and passes through $P_k$. So $\nu^G_\gamma(P_0) \in \{\rho, \rho + 1\}$.

Step 6. Assume that $\gamma$ is a component $V(y)$ of $\Delta$. In two variables a regular curve in $V(y)$ is $V(y)$. In the coordinates of Step 4 of the proof of Theorem 3.13.6, $\operatorname{ord}_y G_M = \nu^G \ge \rho \ge 1$, so $y$ divides $G_M$. This is false, because no equation of a component of the divisor divides $G_M$. So $\gamma$ is not in $\Delta$, and $\nu^G_\gamma = \bar\nu_\gamma$. $\square$

**Corollary 3.13.9.** Let $n = 2$ and $\rho \ge 1$ at $P_0$. Then each point has at most one point over it with the same $\rho$, so the points over $P_0$ with the same $\rho$ form one run. If no regular formal curve $\gamma$ at $P_0$ that is not in $\Delta$ has $\bar\nu_\gamma(g) \ge \rho$, then this run is finite.

*Proof.* By Theorem 3.7.1, a point over $P_k$ with the same $\rho$ is in $\mathbb{P}(T_\rho)$. Since $\rho \ge 1$, $T_\rho$ is a line or $0$, so $\mathbb{P}(T_\rho)$ has at most one point. The second claim is Theorem 3.13.8. $\square$

A computer test explored the full trees over $\mathbb{F}_p$ for $n = 2$ and $p \in \{2, 3, 5\}$, from $2259$ random clean starts with $\rho \ge 1$, to the depth $9$. In $681$ branches that reached the depth $9$, no corner step at $k \ge 1$ kept $\rho$. This agrees with Theorem 3.13.8. As a control, the same counter found $100$, $166$ and $238$ corner steps along the run of part 1 of Remark 3.13.3 for $p = 2, 3, 5$.

### Three variables: a run on a surface

**Example 3.13.10.** Let $n = 3$ with the variables $x, y, z$, let $p$ be a prime, $\Delta = \{y, z\}$ and $g = x^p y z$. Then each sequence of the $y$-chart and the $z$-chart at the origin is an infinite run with $\rho = p$, and the sequence that takes the two charts in turn follows no formal curve. Each point of each such run is on the strict transform of the surface $Z = V(x)$, and $\nu^G_Z = p = \rho$.

*Proof.* The point $x^p y^a z^b$ with $a, b \ge 1$ and $\gcd(a, b) = 1$ is clean, since $(a, b) \not\equiv (0, 0)$. Here $r = (0, a, b)$ and $G = x^p$. The generators of $\widetilde\Theta(G)$ are $a G + y \partial_y G = a x^p$, $b G + z \partial_z G = b x^p$ and $\partial_x G = p x^{p-1} = 0$. One of $a, b$ is not divisible by $p$, so $\widetilde\Theta(G) = (x^p)$ and $\rho = p = d$. Also $\widetilde\Theta_0(G) = (x^p)$, so the point is in the first case. The $y$-chart at the origin sends $x^p y^a z^b$ to $y^{-p} (y x)^p y^a (y z)^b = x^p y^{a + b} z^b$, and the $z$-chart sends it to $x^p y^a z^{a + b}$. The new divisor is $\{y, z\}$ in both charts. Both maps keep the condition $\gcd(a, b) = 1$, so each sequence of the two charts from $(a, b) = (1, 1)$ is an infinite run with $\rho = p$. In the sequence that takes the two charts in turn, each step from the second step on is a corner step, so by Lemma 3.13.4 and Lemma 3.13.5 it follows no formal curve. Both charts send $V(x)$ to its strict transform $V(x)$, and the origin is on it. The coordinates are adapted to $Z = V(x)$, no component of $\Delta$ contains $Z$, and $\operatorname{ord}_x g = p$. So $\nu^G_Z = p$. $\square$

The exponents along the run that takes the two charts in turn are the Fibonacci numbers, and the run is the sequence of the centers of the monomial valuation on $(y, z)$ with the ratio of the golden section. So the first half of Hypothesis 3.12.5 is false for $n = 3$, for each $p$, also with the correction of Remark 3.13.3. The point is in the first case, with $\tau_\rho = 1$. So the failure does not need a large codimension.

The example does not contradict the use of the hypothesis for the centers. The run lies on a surface along which the order of $G$ is $\rho$, so its start is not an isolated point of the locus where the order of $G$ is at least $\rho$. The center is the surface $Z = V(x)$. Here $g = x^p y z \in I_Z^p$, and $\widetilde\Theta(G) = (x^p) = I_Z^p$, so conditions (H1) and (H2) of Section 3.4 hold, and Theorem 3.4.5 applies. The blowup of $Z$ is the identity, and the transform is $x^{-p} g = y z$ with $\rho = 0$.

### The example of Cossart and Piltant

Example 3.18 of [CP19] is an infinite sequence of point blowups along a transcendental formal arc in four variables. We translate it into our setting.

**Example 3.13.11.** Let $n = 4$, let $p$ be a prime, $\Delta = \{1, 2\}$ and
$$g = x_2^p x_3^p x_4 + x_1^p x_3.$$
Let $c_0, c_1, c_2, \dots \in K$ with $c_k = 0$ if $p \nmid k + 1$, let $\varphi(t) = \sum_{k \ge 0} c_k t^{k + 1}$, and let $\gamma$ be the formal curve $x_1 = x_3 = 0$, $x_4 = \varphi(x_2)$. Let $W = V(x_1, x_3)$. Then:

1. $g$ is clean, $r = 0$, $G = g$, $\widetilde\Theta(G) = (x_1^p, x_2^p x_3^p)$, and $(\rho, d, \tau_\rho) = (p, p + 1, 1)$.
2. The points of the strict transforms of $\gamma$ form an infinite run with $(\rho, d, \tau_\rho) = (p, p + 1, 1)$ at each point.
3. $G \in I_W^p \subseteq I_\gamma^p$, and near the origin the locus where the order of $G$ is at least $\rho$ is $V(x_1, x_2) \cup V(x_1, x_3)$.
4. At the generic point of $W$ the residual order is $p$.

*Proof.* Part 1. Each monomial of $g$ has an exponent $1$, so $g$ is clean. The exponent of $x_1$ is $0$ in the first monomial, and the exponent of $x_2$ is $0$ in the second, so $r = 0$ and $G = g$. The generators of $\widetilde\Theta(G)$ are $x_1 \partial_1 G = 0$, $x_2 \partial_2 G = 0$, $\partial_3 G = x_1^p$ and $\partial_4 G = x_2^p x_3^p$. So $\rho = p$ and $d = p + 1$, and the point is in the second case. The elements of $\widetilde\Theta(G)$ of order $p$ have the initial forms $c x_1^p$ with $c \ne 0$, and $(x_1 + s b_1)^p = x_1^p + s^p b_1^p$. So $T_\rho = \{b_1 = 0\}$ and $\tau_\rho = 1$.

Part 2. Let $g_k = x_2^k (x_2^p x_3^p x_4 + x_1^p x_3)$ with the divisor $\{1, 2\}$. The step from $P_k$ to $P_{k+1}$ is the $x_2$-chart with the translation $c_k$ in the direction of $x_4$: $\pi(x_1) = x_2 x_1$, $\pi(x_3) = x_2 x_3$, $\pi(x_4) = x_2 (x_4 + c_k)$. Then
$$x_2^{-p} \pi(g_k) = x_2^{k+1} \bigl( x_2^p x_3^p x_4 + x_1^p x_3 \bigr) + c_k x_2^{k + 1 + p} x_3^p.$$
If $c_k \ne 0$, then $p \mid k + 1$, so the last term is a $p$-th power, and the cleaning removes it. So the clean part is $g_{k+1}$, and the new divisor is $\{1, 2\}$ since $t_1 = 0$. At $P_k$ we have $r = (0, k, 0, 0)$ and $G = g_0$. The generators of $\widetilde\Theta(G)$ are $k G$, $\partial_3 G = x_1^p$ and $\partial_4 G = x_2^p x_3^p$, and $k G$ has order $p + 1$. So the computation of part 1 holds at $P_k$, and $(\rho, d, \tau_\rho) = (p, p + 1, 1)$. The composite of the charts is $x_4 = \varphi(x_2)$ on the strict transforms, as in the proof of Lemma 3.13.5, so $P_{k+1}$ is the point of the strict transform of $\gamma$.

Part 3. Each monomial of $G$ is in $(x_1, x_3)^p$, and in $(x_1, x_2)^p$. At a point with $x_1 \ne 0$ the derivative $\partial_3 G = x_1^p$ is a unit, and at a point with $x_1 = 0$ and $x_2 x_3 \ne 0$ the derivative $\partial_4 G$ is a unit. So the order of $G$ is at most $1$ off the two planes.

Part 4. At the generic point of $W$ the parameters are $x_1$ and $x_3$, and the residue field is $K(x_2, x_4)$. This field is not perfect, and $x_2^p x_4$ is not in $K(x_2, x_4)^p$, so the term $x_2^p x_4 x_3^p$ of degree $p$ in the parameters is not part of a $p$-th power, and the cleaning cannot remove it. Thus the residual order is $p$ there. $\square$

The sequence $c_k$ can be chosen so that $\varphi$ is transcendental over $K(t)$. Then $W$ is the Zariski closure of $\gamma$, and no algebraic curve contains $\gamma$. For example, let $c_k = 1$ if $k + 1 = p m^2$ for an integer $m \ge 1$, and $c_k = 0$ otherwise. Then $\varphi = \vartheta^p$, where the coefficients of $\vartheta$ over $\mathbb{F}_p$ are $1$ at the squares and $0$ at the other exponents. This sequence is not automatic, so $\vartheta$ is transcendental over $\mathbb{F}_p(t)$ by the theorem of Christol [Chr79]. Its coefficients are in $\mathbb{F}_p$, so it is also transcendental over $K(t)$. These translations are in $\mathbb{F}_p$, so the run is in the trees of our tests for $n = 4$.

So the example satisfies the second half of Hypothesis 3.12.5 with $\gamma$, but the curve is transcendental, and the plan "blow up the curve that the run follows" cannot be done. Three facts point to the center.

- *A center of dimension at most one does not stop the runs.* A computer test blew up the line $L = V(x_1, x_2, x_3)$, where the two planes meet. At the origin of the $x_2$-chart, the transform is $G = x_2^{p-1} x_3^p x_4 + x_1^p x_3$, still in $(x_1, x_3)^p$, with $(\rho, d, \tau_\rho) = (p, p + 1, 1)$. After $20$ more point blowups along an arc in the strict transform of $W$, $\rho$ was still $p$, for $p = 2, 3$. The reason is that the strict transform of $W$ under a center of dimension at most one is a surface along which the order of $G$ is at least $p$.
- *The planes stop them.* The plane $V(x_1, x_2)$ satisfies (H1) and (H2) of Section 3.4, since $\widetilde\Theta(G) \subseteq (x_1, x_2)^p$ and $\partial_3 G = x_1^p$ has order $p$ in $\widetilde\Theta_C(G)$. So Theorem 3.4.5 applies to its blowup. Over the origin, $\rho$ goes down to $0$ except at the origin of the $x_2$-chart, where $G = x_3^p x_4 + x_1^p x_3$ with $(\rho, d, \tau_\rho) = (p, p + 1, 2)$. There the strict transform of $W$ is $V(x_1, x_3)$, and it satisfies (H1) and (H2), since $\partial_4 G = x_3^p$ has order $p$. A computer test found $\rho \le 1$ at each $\mathbb{F}_p$-point over the origin after the blowup of this plane, for $p = 2, 3$.
- *The residual order does not choose the center.* By part 4, $d$ is $p + 1$ at the closed points of $W$ and $p$ at its generic point. So $d$ is not upper semicontinuous at the points that are not closed, and the locus of the triple $(\rho, d, \tau_\rho)$ is not closed. This is the reason that [CP19] calls the support of the arc not permissible. The functions $\rho$ and the order of $G$ have the value $p$ at the generic point of $W$ too.

In each dimension, a formal curve $\gamma$ with $G \in I_\gamma^\rho$ gives an algebraic subvariety. If $G$ is a polynomial, each Hasse derivative $D^\alpha G$ with $|\alpha| < \rho$ is in $I_\gamma$, and it is a polynomial, so it is in the ideal of the Zariski closure $\overline\gamma$ of $\gamma$. Over a perfect field the theorem of Zariski and Nagata with Hasse derivatives then gives that $G$ has the order at least $\rho$ at the generic point of $\overline\gamma$. So the run lies on the strict transforms of an algebraic subvariety of the locus of the order of $G$. This subvariety can be a surface, as in Example 3.13.11, and it need not be regular.

### The hypothesis on surfaces

**Hypothesis 3.13.12 (H4').** Let $P_0, P_1, P_2, \dots$ be an infinite run with $\rho \ge 1$. Then there are an $N \ge 0$ and a regular formal subvariety $Z$ of positive dimension at $P_N$ such that $P_k$ is on the strict transform of $Z$ for each $k \ge N$, and $\nu^G_Z(P_N) \ge \rho$.

Node: SG0000005K

Examples 3.12.2, 3.12.4, 3.13.10 and 3.13.11 satisfy the hypothesis, with $Z$ the $y$-axis, the $x$-axis, the plane $V(x)$ and the plane $W$. Theorem 3.13.8 proves it for $n = 2$, with $N = 0$ and a curve. By Lemma 3.13.5 and Theorem 3.13.6, a run with a finite number of corner steps satisfies it with a curve. So the hypothesis is open only for the runs with an infinite number of corner steps.

**Question 3.13.13.** Let $n \ge 3$, and let $P_0, P_1, \dots$ be an infinite run with $\rho \ge 1$ and an infinite number of corner steps. Are there an $N$ and a regular formal subvariety $Z$ of dimension at least $2$ at $P_N$ such that $P_k$ is on the strict transform of $Z$ for each $k \ge N$, and $\nu^G_Z(P_N) \ge \rho$?

A positive answer to Question 3.13.13 proves Hypothesis 3.13.12. We do not know the answer, also not for $n = 3$ and $\tau_\rho = 1$. Two parts of the proof for $n = 2$ hold in each dimension. For $k \ge 1$, the restriction of $J_k$ to $E_k$ has the order $\rho$, by the proof of part 1 of Lemma 3.13.7 with Theorem 3.7.1. At a corner step in the chart $y_2$, the restriction of $J_{k+1}$ to the strict transform of $E_k$ is $y_2^{\alpha - \sigma_k} A'$, where $A$ is the restriction of $J^0_k$ to $E_k$, $\alpha \le \rho + 1$ is its order, and $A'$ is the weak transform of $A$ under the blowup of $E_k$ at $P_k$. So a corner step gives a blowup in dimension $n - 1$, and the order goes down by at most $1$. For $n = 2$ the ideal $A'$ is the unit ideal, and this gives Step 1 of the proof of Theorem 3.13.8. For $n \ge 3$ the order need not go down, as in Example 3.13.10, so the descent does not end the run. A strong form of a positive answer for $\tau_\rho = 1$ is a hypersurface $Z$ with the tangent space $T_\rho$ at $P_N$. In Example 3.13.10 this is $V(x)$. This strong form is a statement of maximal contact along the run, and in characteristic $p$ hypersurfaces of maximal contact need not exist (Volume 2, Section 2.4). The proof of Theorem 3.13.6 also does not give the bound $\nu^G_Z \ge \rho$ for a subvariety $Z$ of dimension at least $2$, since in Step 4 the points of the run can move inside $Z$, as in Example 3.13.10.

### What this means for the centers

The results of this section change the plan of Section 3.12 in three ways.

1. The centers come from the locus of $\rho$ or of the order of $G$, and not from $d$ or $\tau_\rho$. These two functions are data at the closed points only, by part 4 of Example 3.13.11.
2. If a run does not end, the center is the component of the locus that contains the run, and it can have dimension $2$ or more. A formal curve is not sufficient, since it can be transcendental.
3. The next question is the step at such a center: for a regular center $Z$ in the locus, with normal crossings with $\Delta$, does $\rho$ go down at each point over $Z$ after the blowups of the components in a good order? Example 3.13.11 shows that the order of the blowups is important, since only the order with $V(x_1, x_2)$ first satisfies (H2) at each step.

### Notes and references

Example 3.13.11 is Example 3.18 of [CP19], in the coordinates of this chapter. The transcendence argument uses the theorem of Christol [Chr79]. The use of the history of the divisor is from [CJS20], and maximal contact is from [Hir64]. Lemma 3.13.1, Theorems 3.13.6 and 3.13.8, Example 3.13.10, Hypothesis 3.13.12 and Question 3.13.13 are a result of the milestone S7.18 of this project (tamnd/singularity#245).
