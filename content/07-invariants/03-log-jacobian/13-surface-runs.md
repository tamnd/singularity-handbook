---
title: Runs that follow no curve
nodes: [SG0000005K, SG0000005M, SG0000005N, SG0000005P, SG0000005Q, SG0000005R, SG0000005S, SG0000005T, SG0000005V, SG0000005W]
sources: [CP19, CJS20, Hir64, Chr79]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs that follow no curve

Hypothesis 3.12.5 says that each infinite run follows a formal curve along which the order of $G$ is at least $\rho$. In this section we prove the hypothesis in two variables, and we prove its second half in each dimension: if an infinite run follows a regular formal curve, then the order of $G$ along the curve is $\rho$ or $\rho + 1$. Then we show that the first half is false in three variables. An infinite run can take the corner of two components of the divisor at each step, and such a run follows no formal curve. It lies on a surface. Last, we give the example of Cossart and Piltant in our setting. There the run follows a formal curve, but the curve is transcendental, and its Zariski closure is a plane. So in each form of the hypothesis that can give the centers of a resolution, the curve must be replaced by a subvariety of positive dimension, and the centers of the resolution can be surfaces. We state this form as Hypothesis 3.13.12, and we isolate the open step as Question 3.13.13. Last, we show that the answer to the question is no, also in the first case with $\tau_\rho = 1$. A run can take the corner at each step and stay on no subvariety along which the order of $G$ is at least $\rho$. So Hypothesis 3.13.12 is false, and the centers must also come from subvarieties that the run does not follow. We state the corrected form as Question 3.13.18. Theorem 3.13.20 gives a positive answer for $n = 3$ when the run takes only two charts, each at the origin, and Example 3.13.21 shows that the corner curves alone do not resolve the singularity. Theorem 3.13.27 shows that for $g = B_1 x^p + B_0$ such a run has only a finite number of nonzero translations in the free coordinate, so Corollary 3.13.28 answers the question for these runs.

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

Node: SG0000005N · Lean: `Singularity.SurfaceRuns.surfaceRun_of_charts` (the runs, not the claim on curves)

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

Node: SG0000005P · Lean: `Singularity.SurfaceRuns.cpRun` (part 2 for $p = 2$)

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

Examples 3.12.2, 3.12.4, 3.13.10 and 3.13.11 satisfy the hypothesis, with $Z$ the $y$-axis, the $x$-axis, the plane $V(x)$ and the plane $W$. Theorem 3.13.8 proves it for $n = 2$, with $N = 0$ and a curve. By Lemma 3.13.5 and Theorem 3.13.6, a run with a finite number of corner steps satisfies it with a curve. So the hypothesis can fail only for the runs with an infinite number of corner steps. Example 3.13.15 shows that it does fail for such a run.

**Question 3.13.13.** Let $n \ge 3$, and let $P_0, P_1, \dots$ be an infinite run with $\rho \ge 1$ and an infinite number of corner steps. Are there an $N$ and a regular formal subvariety $Z$ of dimension at least $2$ at $P_N$ such that $P_k$ is on the strict transform of $Z$ for each $k \ge N$, and $\nu^G_Z(P_N) \ge \rho$?

A positive answer to Question 3.13.13 proves Hypothesis 3.13.12. The answer is no, by Example 3.13.15 below. We first give the facts that a proof could use, and we show where they stop. Two parts of the proof for $n = 2$ hold in each dimension. For $k \ge 1$, the restriction of $J_k$ to $E_k$ has the order $\rho$, by the proof of part 1 of Lemma 3.13.7 with Theorem 3.7.1. At a corner step in the chart $y_2$, the restriction of $J_{k+1}$ to the strict transform of $E_k$ is $y_2^{\alpha - \sigma_k} A'$, where $A$ is the restriction of $J^0_k$ to $E_k$, $\alpha \le \rho + 1$ is its order, and $A'$ is the weak transform of $A$ under the blowup of $E_k$ at $P_k$. So a corner step gives a blowup in dimension $n - 1$, and the order goes down by at most $1$. For $n = 2$ the ideal $A'$ is the unit ideal, and this gives Step 1 of the proof of Theorem 3.13.8. For $n \ge 3$ the order need not go down, as in Example 3.13.10, so the descent does not end the run. A strong form of a positive answer for $\tau_\rho = 1$ is a hypersurface $Z$ with the tangent space $T_\rho$ at $P_N$. In Example 3.13.10 this is $V(x)$. This strong form is a statement of maximal contact along the run, and in characteristic $p$ hypersurfaces of maximal contact need not exist (Volume 2, Section 2.4). The proof of Theorem 3.13.6 also does not give the bound $\nu^G_Z \ge \rho$ for a subvariety $Z$ of dimension at least $2$, since in Step 4 the points of the run can move inside $Z$, as in Example 3.13.10.

### Corner runs that lie on no subvariety

The next lemma bounds the order of $G$ along $Z$ by the order of the whole ideal $J$ along $Z$, and not only of its initial form.

**Lemma 3.13.14.** Let $Z$ be a regular formal subvariety at $P$, not the whole space. Then $\nu^G_Z(P) \le \operatorname{ord}_Z(J) + 1$. So if $\nu^G_Z(P) \ge \rho(P)$, then $J \subseteq I_Z^{\rho - 1}$.

*Proof.* Let $\nu = \nu^G_Z(P)$ and let $s$ be the sum of the $r_i$ for the components $D_i$ of $\Delta$ that contain $Z$. By Definition 3.13.2 there is an $h$ with $g + h^p \in I_Z^{\nu + s}$. A derivation or a logarithmic derivation lowers the order along $Z$ by at most $1$, and it kills $h^p$. The logarithmic derivations of $\Delta$ and the derivations in the other variables generate $\Theta(g + h^p) = \Theta(g) = x^r J$. So $x^r J \subseteq I_Z^{\nu + s - 1}$. Since $Z$ is regular, $\operatorname{ord}_Z$ is a valuation. If $D_i$ contains $Z$, then $x_i$ is a regular parameter of $Z$ and $\operatorname{ord}_Z(x_i) = 1$. If not, $x_i \notin I_Z$, and $\operatorname{ord}_Z(x_i) = 0$. So $\operatorname{ord}_Z(x^r) = s$ and $\operatorname{ord}_Z(J) \ge \nu - 1$. $\square$

The Lean library proves the lemma for a coordinate subvariety $Z$, the zero set of the $x_i$ with $i$ in a set $S$, over a field of characteristic $p$, with $h$ a polynomial. There the order of $f$ along $Z$ is the least value of $\sum_{i \in S} e_i$ on the monomials $x^e$ of $f$, and the library proves that it is the largest $m$ with $f \in I_Z^m$. The lemma for formal subvarieties and formal series $h$ is not in Lean.

Node: SG0000005T · Lean: `Singularity.orderGAlong_le_idealOrdAlong_add_one` (coordinate $Z$, polynomial $h$)

**Example 3.13.15.** Let $n = 3$ with the variables $x, y, z$, let $p$ be a prime, $\Delta = \{y, z\}$ and
$$g = x^p y z + y^{p + 2} z^{p + 1}.$$
Let $P_0$ be the origin, and let $P_0, P_1, \dots$ be a sequence of the $y$-chart and the $z$-chart at the origin that uses each chart an infinite number of times, for example the sequence that takes the two charts in turn. Then:

1. Each $P_k$ has $\rho = d = \sigma = p$ and $\tau_\rho = 1$. So the sequence is an infinite run in the first case, and it has an infinite number of corner steps.
2. For each $N$ and each regular formal subvariety $Z$ of positive dimension at $P_N$ such that $P_k$ is on the strict transform of $Z$ for each $k \ge N$, we have $\nu^G_Z(P_N) < \rho$.
3. Each regular formal surface at each $P_N$ has $\nu^G \le 1$. The surface $V(x)$ contains each $P_k$, and $\nu^G_{V(x)} = 0$.
4. For $n \ge 4$, parts 1 and 2 hold for the same $g$ with more variables that are not in $\Delta$.

So Hypothesis 3.13.12 is false, and the answer to Question 3.13.13 is no.

Node: SG0000005M

*Proof.* At each point of the sequence we use coordinates $(x, y, z)$ with $\Delta = \{y, z\}$ and write
$$g = y^a z^b (x^p + y^m z^l), \qquad M = y^m z^l.$$
At $P_0$ we have $(a, b, m, l) = (1, 1, p + 1, p)$. In the $y$-chart at the origin, $\pi(x) = y x$ and $\pi(z) = y z$, and the transform $y^{-p} \pi(g)$ has the data $(a + b, b, m + l - p, l)$. In the $z$-chart the new data are $(a, a + b, m, m + l - p)$. Let $\mu = m - p$ and $\lambda = l - p$. The $y$-chart sends $(\mu, \lambda)$ to $(\mu + \lambda, \lambda)$, and the $z$-chart sends it to $(\mu, \mu + \lambda)$. The start is $(1, 0)$. So $\mu$ and $\lambda$ are never negative, and $m + l \ge 2p + 1$ at each point. Along a sequence that uses each chart an infinite number of times, $m + l$ goes to infinity.

The $y$-chart changes $a l - b m$ by $b p$, and the $z$-chart changes it by $-a p$. So $a l - b m \equiv -1 \pmod p$ at each point, since $p - (p + 1) = -1$ at $P_0$. In particular $a$ and $b$ are not both divisible by $p$, so the monomial $x^p y^a z^b$ is not a $p$-th power. If $(a + m, b + l) \equiv (0, 0) \pmod p$, then $a l - b m \equiv -m l + l m = 0$, which is false. So the monomial $y^{a + m} z^{b + l}$ is not a $p$-th power either. Thus $g$ is clean at each point, no cleaning is needed after a chart, $r = (0, a, b)$ and $G = x^p + M$.

Part 1. The generators of $J$ are $\partial_x G = 0$, $a G + y \partial_y G = a x^p + (a + m) M$ and $b G + z \partial_z G = b x^p + (b + l) M$. The determinant of the coefficients is $a l - b m \not\equiv 0$, so $J = (x^p, M)$. Since $M$ has order at least $2p + 1$, we get $\rho = p$, and $d = p$. The ideal $J^0$ contains $\mathfrak{m} J$ and the same two generators, so $\sigma = p$, and the elements of order $p$ have the initial forms $c x^p$. So $T_\rho = V(x)$ and $\tau_\rho = 1$. A step is a corner step exactly when the chart changes. The strict transform of the old exceptional divisor passes through the origin of the other chart, and it does not meet the origin of the same chart.

Part 2. Assume $\nu^G_Z(P_N) \ge \rho = p \ge 2$. By Lemma 3.13.14, $x^p \in I_Z$ and $M \in I_Z$. The ideal $I_Z$ is prime, so $x \in I_Z$, and $y \in I_Z$ or $z \in I_Z$. Assume $y \in I_Z$, so $Z \subseteq V(y)$. A $z$-step sends $V(y)$ to the plane $y = 0$ of the new coordinates, and this plane passes through the new point. But the strict transform of $V(y)$ does not meet the origin of the $y$-chart, since there $y$ is the equation of the exceptional divisor. The sequence takes the $y$-chart at some step after $P_N$, so from that step on the points are not on the strict transform of $Z$. The case $z \in I_Z$ is the same.

Part 3. Let $Z = V(h)$ be a regular surface. If $\nu^G_Z \ge 2$, then $h$ divides $x^p$ and $M$ by Lemma 3.13.14. These two series have no common factor, so this is false. The surface $V(x)$ is not in $\Delta$, so $s = 0$. The term $y^{a + m} z^{b + l}$ of $g$ is not in $(x)$, and it is not a $p$-th power, so no $h^p$ removes it and $\bar\nu_{V(x)}(g) = 0$. The chart maps keep $V(x)$, so each $P_k$ is on its strict transform.

Part 4. A new variable $w$ not in $\Delta$ gives $\partial_w G = 0$, so $J$ does not change. The proof of part 2 uses only that $I_Z$ is prime. $\square$

A computer test checked the data of part 1 for $p = 2, 3, 5, 7$: along the sequence that takes the charts in turn and along the Fibonacci sequence for $40$ steps, along $200$ random sequences of length $30$, and for $n = 4$ with a free variable.

The Lean library proves part 1, the congruence $a l - b m \equiv -1$, the claim that $g$ is clean, the equality $J = (x^p, M)$ and the claim that $x$ does not divide $g + h^p$ for each $h$, over $\mathbb{Z}/p$ for each prime $p$. The library also proves part 2 for the coordinate subvarieties, with $h$ a polynomial: the order of $G$ along such a $Z$ is at most $1$ unless $I_Z$ contains $x$ and $y$ or $z$ (`Singularity.CornerRuns.cornerRun_orderGAlong_lt`). Part 2 for the other formal subvarieties and the first claim of part 3 are not in Lean.

Node: SG0000005Q · Lean: `Singularity.CornerRuns.cornerRun_of_charts` (part 1)

The example is a small change of Example 3.13.10, and the change shows where a proof by the data of the run must stop. At each $P_k$ the initial form of $G$ is $x^p$, and the initial form of $J$ is $(x^p)$, the same as in Example 3.13.10. The run does not see the term $M$, because its order goes to infinity. But Lemma 3.13.14 needs a divisibility of the whole ideal $J$, and $M$ is never divisible by $x$. In particular, the hypersurface with the tangent space $T_\rho$ that the strong form above asks for is $V(x)$, and its order is $0$.

**Remark 3.13.16.** The same method gives a run in the second case. Let $g = x^{p + 1} y z + y^{p + 3} z^{p + 2}$ with $\Delta = \{y, z\}$, and write $g = y^a z^b (x^{p + 1} + M)$. The charts act on $(\mu, \lambda) = (m - p - 1, l - p - 1)$ as in the example, with the start $(1, 0)$. Now $\partial_x G = x^p$, and the residues $(u, v) = (a + m, b + l)$ modulo $p$ move by $(u, v) \mapsto (u + v, v)$ and $(u, v) \mapsto (u, u + v)$. These maps are invertible, and the start $(3, 2)$ is not $(0, 0)$ modulo $p$ for any $p$. So $J = (x^p, M)$ at each point, with $\rho = p$, $d = \sigma = p + 1$ and $\tau_\rho = 1$. The proof of part 2 applies without change. A computer test checked this for $p = 2, 3, 5, 7$.

**Remark 3.13.17.** In Example 3.13.15 the point $P_N$ is not isolated in the locus of the order of $G$. The curves $V(x, y)$ and $V(x, z)$ lie in components of $\Delta$, and $\nu^G = p$ along each of them, because $G \in (x, y)^p$ and $G \in (x, z)^p$. The run follows neither curve. A computer test blew up $V(x, y)$ and then the strict transform of $V(x, z)$, for $p = 2, 3, 5$, and found that $\rho$ goes down at each point over the origin. The test covers only the points over the origin.

The remark suggests the corrected form of the question. It asks for a subvariety in the locus at a point of the run, but not for a subvariety that the run follows.

**Question 3.13.18.** Let $n \ge 3$, and let $P_0, P_1, \dots$ be an infinite run with $\rho \ge 1$ and an infinite number of corner steps. Are there an $N$ and a regular formal curve $C$ at $P_N$, in a component of $\Delta$, with $\nu^G_C(P_N) \ge \rho$?

For $n = 3$ the answer is yes for the runs where each step is at the origin of a chart and only two charts occur. We prove this now. In the rest of this part, $n = 3$, and from $P_N$ on each step is at the origin of the $y$-chart or of the $z$-chart, and each chart occurs an infinite number of times. After the first step of each type, $V(y)$ and $V(z)$ are in $\Delta$. The component $V(x)$ can be in $\Delta$ or not, and we write $r_x$ for its exponent, with $r_x = 0$ if $V(x)$ is not in $\Delta$. No step uses the chart of $x$, so $r_x$ does not change.

*The matrices.* At $P_m$ write $y = y_m^{a_1} z_m^{a_2}$ and $z = y_m^{b_1} z_m^{b_2}$, and let $c_1 = (a_1, b_1)$ and $c_2 = (a_2, b_2)$. At $P_N$ these are the unit vectors. A $y$-step replaces $c_1$ by $c_1 + c_2$, and a $z$-step replaces $c_2$ by $c_1 + c_2$. So the determinant stays $\pm 1$, and after one step of each type all entries are at least $1$ and go to infinity. The cones spanned by $c_1$ and $c_2$ are nested, and the sine of the angle between $c_1$ and $c_2$ is $1 / (|c_1| \, |c_2|)$. So the cones shrink to one ray $\mathbb{R}_{\ge 0} (1, \theta)$ with $0 < \theta < \infty$. The number $\theta$ is irrational: a primitive integer vector $q$ on the ray is in each cone, so $q = u c_1 + w c_2$ with integers $u, w \ge 0$, and then $|q| \ge \min(|c_1|, |c_2|)$, which goes to infinity.

*The monomials.* Each step divides $x$ by the chart variable, so $x = M_m x_m$ with $M_m = y z / (y_m z_m)$. The monomial $x^i y^j z^k$ of $g_N$ becomes $x_m^i y_m^{E_1} z_m^{E_2}$ with
$$E_s = (i + j, \, i + k) \cdot c_s - i, \qquad s = 1, 2.$$
The map $(i, j, k) \mapsto (i, E_1 + i, E_2 + i)$ is linear with the determinant $\pm 1$. So no two monomials cancel, a monomial is a $p$-th power after a step if and only if it was one before, and no cleaning is needed. Let $\lambda(i, j, k) = (i + j) + \theta (i + k)$. Since $\theta$ is irrational, the least value of $\lambda$ on the support of $g_N$ is taken at one pair $(A, B) = (i + j, i + k)$. Let $F$ be the set of the monomials of $g_N$ with this pair, let $i_0$ be the largest exponent of $x$ on $F$, and let $T$ be the monomial of $F$ with this exponent. For a monomial $\mu = x^i y^j z^k$ put $\delta(\mu) = (i + j - A, \, i + k - B)$. Then $E_s(\mu) - E_s(T) = \delta(\mu) \cdot c_s - (i - i_0)$.

**Lemma 3.13.19.** There is an $m_0$ such that for each $m \ge m_0$, each monomial $\mu$ of $g_N$ that is not in $F$ and $s = 1, 2$, we have $\delta(\mu) \cdot c_s > 0$ and $\delta(\mu) \cdot c_s \ge i - i_0$.

*Proof.* Choose $m_1$ such that for $m \ge m_1$ all the entries of $c_1$ and $c_2$ are at least $A + B + 1$, and each column $c = (c', c'')$ satisfies $c'' \le (\theta + 1) c'$ and $c' \le (1/\theta + 1) c''$. This is possible since $c_s / |c_s|$ goes to the direction of $(1, \theta)$. Write $\delta = (\delta_1, \delta_2)$.

If $i \ge A + B$, then $\delta_1 \ge i - A \ge 0$ and $\delta_2 \ge i - B \ge 0$, so $\delta \cdot c \ge \delta_1 + \delta_2 \ge 2i - A - B \ge i$. This is positive unless $i = A = B = 0$, and then $\mu$ is the constant term, which is in $F$.

If $i < A + B$ and $j \ge A + B(\theta + 1) + 1$, then $\delta_1 \ge j - A$ and $\delta_2 \ge -B$, so $\delta \cdot c \ge (j - A) c' - B c'' \ge c' (j - A - B(\theta + 1)) \ge c' > i$. The case $k \ge B + A(1/\theta + 1) + 1$ is the same with $y$ and $z$ exchanged.

The other monomials with $i < A + B$ are a finite set. For such a $\mu$ not in $F$, $\lambda(\mu) > \lambda(T)$, so $\delta_1 + \theta \delta_2 > 0$. Since $c_s / |c_s|$ goes to the direction of $(1, \theta)$ and $|c_s|$ goes to infinity, $\delta \cdot c_s$ goes to infinity. The number $i - i_0$ is bounded on this finite set, so there is an $m_2$ for these monomials. Take $m_0 = \max(m_1, m_2)$. $\square$

**Theorem 3.13.20.** Let $n = 3$, and let $P_N, P_{N+1}, \dots$ be an infinite run where each step is at the origin of the $y$-chart or of the $z$-chart and each chart occurs an infinite number of times. Then for $m \ge m_0$:

1. The initial form of $G_m$ is $c \, x_m^{d_m}$ with $c \ne 0$ and $d_m = i_0 - r_x$. So $d_m \in \{\rho, \rho + 1\}$.
2. The corner curves $C = V(x_m, y_m)$ and $C = V(x_m, z_m)$ have $\nu^G_C(P_m) = d_m \ge \rho$.
3. If $p \nmid d_m$ and $\rho = d_m - 1$, then the forms of degree $\rho$ of $J$ at $P_m$ are the multiples of $x_m^{\rho}$.

So Question 3.13.18 has a positive answer for these runs.

Node: SG0000005R

*Proof.* By Lemma 3.13.19, $E_s(\mu) \ge E_s(T)$ for $\mu$ not in $F$. For $\mu$ in $F$, $\delta(\mu) = 0$ and $E_s(\mu) - E_s(T) = i_0 - i \ge 0$. So $T$ has the least exponent of $y_m$ and the least exponent of $z_m$, and $r = (r_x, E_1(T), E_2(T))$ at $P_m$. Thus $G_m$ is the sum of the terms $x_m^{i - r_x} y_m^{E_1(\mu) - E_1(T)} z_m^{E_2(\mu) - E_2(T)}$, with the coefficients of $g_N$.

Part 1. The term of $\mu$ has the degree $(i - r_x) + \delta \cdot c_1 + \delta \cdot c_2 - 2(i - i_0)$. If $\mu$ is not in $F$ and $i > i_0$, the lemma gives a degree of at least $i - r_x > i_0 - r_x$. If $\mu$ is not in $F$ and $i \le i_0$, the degree is at least $(i - r_x) + 2 + 2(i_0 - i) > i_0 - r_x$. If $\mu$ is in $F$ and $i < i_0$, the degree is $(i - r_x) + 2(i_0 - i) > i_0 - r_x$. So $T$ gives the only term of the least degree, and $d_m = i_0 - r_x$. The run keeps $\rho$, and $d_m \in \{\rho, \rho + 1\}$ by Theorem 3.1.4.

Part 2. Let $C = V(x_m, y_m)$. The term of $\mu$ in $g_m$ has the order $i + E_1(\mu)$ along $C$, and $i + E_1(\mu) - (i_0 + E_1(T))$ is $\delta(\mu) \cdot c_1 > 0$ for $\mu$ not in $F$ and $0$ for $\mu$ in $F$. So the order of $g_m$ along $C$ is $i_0 + E_1(T)$. The point $g_m$ is clean, the coordinates are adapted to $C$, and the components of $\Delta$ that contain $C$ are $V(y_m)$ and, if it is in $\Delta$, $V(x_m)$. By Lemma 3.13.1, $\nu^G_C = i_0 + E_1(T) - E_1(T) - r_x = d_m$. The curve $V(x_m, z_m)$ is the same.

Part 3. The generator $\partial_x G_m$ has the initial form $d_m c \, x_m^{d_m - 1}$, which is not $0$. The other generators of $J$ have the order at least $d_m > \rho$. $\square$

If $p \mid d_m$ or $\rho = d_m$, other terms of $G_m$ can give forms of degree $\rho$, and part 3 can fail. Part 3 gives that the directrix is $V(x_m)$, so by Theorem 3.7.1 no later step with the same $\rho$ has a translation in $x$. Theorem 3.13.20 also holds for Example 3.13.15: there $V(x)$ has $\nu^G = 0$, and both corner curves have $\nu^G = p$.

A run of the general type is more complex. A step at a point that is not a chart origin is a step at the origin after a linear change of the coordinates. If the translations from $P_N$ on are only in the free coordinate $x$ and only a finite number of them are not $0$, let $J$ be the last index with a nonzero translation. Then $P_{J+1}, P_{J+2}, \dots$ is a run of the type of Theorem 3.13.20 in the coordinates of $P_{J+1}$. A computer test over $\mathbb{F}_2$ and $\mathbb{F}_3$ found a coordinate curve in a component of $\Delta$ with $\nu^G \ge \rho$ at the last point of $2802$ of $2805$ random branches with many corner steps, of the depth at most $20$, and at an earlier point of the other $3$. All $72$ branches with translations in the tail had such a curve. The runs with an infinite number of nonzero translations in $x$ are the subject of Theorem 3.13.27 below. The runs that leave a component of $\Delta$ an infinite number of times and the case $n \ge 4$ are open.

The corner curves alone do not resolve the singularity, as the next example shows.

**Example 3.13.21.** Let $n = 3$, $\Delta = \{y, z\}$ and $g = x^a y^b z^c$ with $a \ge 2$, $p \nmid a$ and $a + b \ge p$. Then $\rho = a - 1$ and $d = a$. The corner curve $C = V(x, y)$ has $\nu^G_C = a \ge \rho$, and it satisfies (H1) and (H2) of Section 3.4. After its blowup, the only point over the origin with the same $\rho$ is the origin of the $y$-chart, where $g' = x'^a y^{a + b - p} z^c$. The same holds for $V(x, z)$. So no blowup of a corner curve makes $\rho$ smaller. If $a > p$, the sequence of blowups of corner curves can go on for ever. If $a < p$, it stops after a finite number of steps at a point where no corner curve is a center of Theorem 3.4.5, and $\rho = a - 1$ there.

*Proof.* Here $G = x^a$, and $J$ has the generators $b x^a$, $c x^a$ and $a x^{a - 1}$, so $\rho = a - 1$. The order of $g$ along $C$ is $a + b \ge p$, and $\nu^G_C = a + b - b = a$. (H1) holds, since $x^{a - 1}$ has the order $a - 1 = \rho$ along $C$. The ideal $\widetilde\Theta_C(G)$ has the generators $b x^a$, $c x^a$ and $a y x^{a - 1}$, of the order $a$ along $C$, so (H2) holds. In the $y$-chart with the translation $t$, $x = y (x' + t)$ and $g' = (x' + t)^a y^{a + b - p} z^c$. If $t \ne 0$, then $\partial_{x'} G' = a (x' + t)^{a - 1}$ is a unit, so $\rho = 0$. In the $x$-chart, $y = x y'$, $\Delta' = \{x, y, z\}$ and $G' = 1$. If $p \nmid b$, then $r_y G'$ is a unit. If $p \mid b$, then $a + b - p \equiv a \not\equiv 0$, and $r_x G'$ is a unit. So $\rho = 0$ there. The curve $V(x, z)$ is the same with $y$ and $z$ exchanged.

At the origin of the $y$-chart, $g'$ has the same form with $b' = a + b - p$ in place of $b$, and $c$ does not change. If $a > p$, then $b' > b$, so $a + b' \ge p$ and $a + c' \ge p$ hold again, and we can blow up a corner curve again. If $a < p$, then $b' = b - (p - a) < b$. Each step makes $b$ or $c$ smaller by $p - a$, so after a finite number of steps $a + b < p$ and $a + c < p$. Then the order of $g$ along each corner curve is less than $p$, so $g \notin I_C^p$, and Theorem 3.4.5 does not apply to $C$. The function $g$ keeps the form $x^a y^b z^c$, so $\rho = a - 1$ there. $\square$

The case $a < p$ is the case of the most interest. For example, $p = 5$, $a = 2$ and $b = c = 4$ give the exponents $(b, c) = (4, 4), (1, 4), (1, 1)$ after two blowups, and then the corner curves have the order $3 < 5$.

*Lean.* The file `Singularity/Invariant/LogJacobianCornerCurves.lean` proves $\rho = a - 1$ (`Singularity.CornerCurves.logJacobianOrder_curvePoly`), the value $\nu^G_C = a$ along the two corner curves (`orderGAlong_curvePoly_xy` and `orderGAlong_curvePoly_xz`), the form of $g'$ at the origin of the $y$-chart and the $z$-chart (`centerRhoStep_curvePoint_y` and `centerRhoStep_curvePoint_z`), and the value $\rho = 0$ at the other points over the origin. For $a > p$ it proves that the run goes on for ever (`curveRun_of_charts`). The conditions (H1) and (H2) and the end of the run for $a < p$ have proofs in the text only.

Node: SG0000005S

In this example the surface $V(x)$ has $\nu^G = a \ge \rho$, and its blowup gives $\rho = 0$. In Example 3.13.15 the corner curves work, and no surface works. So a center must be chosen from the whole locus where $\nu^G \ge \rho$, with curves and surfaces in it, and neither type is sufficient alone. A computer test of the corner curves at random points found that $1873$ of $1925$ satisfy (H1) and (H2), and $\rho$ never went up after such a blowup.

**Remark 3.13.22.** A run can have no surface with $\nu^G \ge \rho$ at many of its points and still meet a curve in a component of $\Delta$ with $\nu^G \ge \rho$. Let $p = 2$, $\Delta = \{x, y\}$ and $g = y^2 z^3 + x^3 y^2 z$. Then $r = (0, 2, 0)$ and $G = z^3 + x^3 z$. The generators of $J$ are $x^3 z$ from $x$, $0$ from $y$, since $r_y = 2 = 0$ in $K$, and $\partial_z G = z^2 + x^3$. So $\rho = 2$. If a regular surface $V(h)$ has $\nu^G \ge 2$, then $J \subseteq (h)$ by Lemma 3.13.14. Then $h$ divides the monomial $x^3 z$, so $h$ is $x$ or $z$ up to a unit, and neither divides $z^2 + x^3$. So no regular surface has $\nu^G \ge \rho$ at $P_0$. The curve $V(x, z)$ lies in the component $V(x)$ of $\Delta$, the order of $g$ along it is $\min(3, 4) = 3$, and $r_x = 0$, so $\nu^G \ge 3 > \rho$ for this curve. A computer test follows a branch of nine chart steps and then the two corner charts of $x$ and $y$ in turn. It finds $\rho = 2$ at $P_0, \dots, P_{29}$ and the same obstruction to surfaces at $P_0, \dots, P_{49}$, but it does not prove that the run is infinite. In a larger test over $\mathbb{F}_2$ and $\mathbb{F}_3$ with $n = 3$ and $n = 4$, on branches of the depth $9$ with at least $2$ corner steps in their last $6$ or $8$ steps, each branch that the test could decide had a surface or a curve in a component of $\Delta$ with $\nu^G \ge \rho$ at some point, and $1735$ branches for $n = 3$ had no regular surface with $\nu^G \ge \rho$ at any point.

The proof of Theorem 3.13.20 uses Lemma 3.13.19 only through its two inequalities at $P_m$, and parts 1 and 2 do not need the run to be infinite. So the proof gives a result for a finite stretch of a run.

**Corollary 3.13.23.** Let $n = 3$, and let $P_N, \dots, P_m$ be a stretch of a run where each step is at the origin of the $y$-chart or of the $z$-chart, with $V(y)$ and $V(z)$ in $\Delta$ at $P_N$. Let $c_1$ and $c_2$ be the columns of the exponents from $P_N$ to $P_m$. Choose a $\theta'$ in the cone of $c_1$ and $c_2$ such that the least value of $(i + j) + \theta' (i + k)$ on the support of $g_N$ is taken at one pair, and define $F$, $i_0$ and $\delta$ as before Lemma 3.13.19 with $\theta'$ in place of $\theta$. Assume that each monomial $\mu$ of $g_N$ that is not in $F$ satisfies $\delta(\mu) \cdot c_s > 0$ and $\delta(\mu) \cdot c_s \ge i - i_0$ for $s = 1, 2$. Then at $P_m$ the initial form of $G_m$ is $c \, x_m^{d_m}$ with $c \ne 0$ and $d_m = i_0 - r_x$, and the corner curves $V(x_m, y_m)$ and $V(x_m, z_m)$ have $\nu^G = d_m \ge \rho$.

*Proof.* The proof of parts 1 and 2 of Theorem 3.13.20 uses only the two inequalities, the formula for the exponents $E_s$, and the fact that the steps need no cleaning. These hold for each stretch at the origin. The bound $d_m \ge \rho$ is Theorem 3.1.4. $\square$

Node: SG0000005V

By Lemma 3.13.19, the inequalities hold for each long enough stretch where both charts occur often enough, and the needed length depends on $g_N$. So the corollary answers Question 3.13.18 at the end of each such stretch, also if the run has translations before the stretch. A run where the stretches between the translations stay too short for the points at their starts is not covered. A computer test over $\mathbb{F}_2$ and $\mathbb{F}_3$ from $2430$ random starts found no branch that kept $\rho$ along more than $3$ nonzero translations with a change of chart between them. Of the $759$ branches with such translations, $754$ have a curve $V(y, z)$, $V(y, x - \varphi(z))$ or $V(z, x - \varphi(y))$ with $\nu^G \ge \rho$ at some point, and the other $5$ have no continuation that keeps $\rho$ for more than one step.

### Corner runs with free translations

We now allow translations in the free coordinate. In this part $n = 3$, and from $P_N$ on, $V(y_m)$ and $V(z_m)$ are in $\Delta$ and $V(x_m)$ is not. Step $m$ is the $y$-chart or the $z$-chart, followed by a translation $t_m \in K$ in $x$. Let $L_m$ be the chart variable at $P_{m+1}$, that is, $L_m = y_{m+1}$ for the $y$-chart and $L_m = z_{m+1}$ for the $z$-chart. Then $x_m = L_m (x_{m+1} + t_m)$. Each chart occurs an infinite number of times, and $\rho \ge 1$ is the same at each point. We call such a run a *corner run with free translations*. Corollary 3.13.23 covers the runs that have long stretches with $t_m = 0$. Here we show that for a large class of $g$ the case of an infinite number of nonzero $t_m$ does not occur.

The translations do not change $y$ and $z$. So the matrices and the irrational number $\theta$ of the proof of Theorem 3.13.20 are defined as before. Put $v(y_N^a z_N^b) = a + \theta b$ for $a, b \in \mathbb{Z}$. Since $\theta$ is irrational, distinct Laurent monomials have distinct values. By the matrices, $y_m$ and $z_m$ are Laurent monomials in $y_N, z_N$, so $v$ is defined on the monomials at each $P_m$. Let $R_m = K[[y_m, z_m]][1/(y_m z_m)]$. For $f \ne 0$ in $R_m$ let $v(f)$ be the least value of a monomial of $f$, and let $\operatorname{in}(f)$ be the term of $f$ with this value. Put $M_N = 1$ and $M_{m+1} = M_m L_m$, and put $\varphi_N = 0$ and $\varphi_{m+1} = \varphi_m + t_m M_{m+1}$.

**Lemma 3.13.24.**

1. $v(y_m) > 0$, $v(z_m) > 0$ and $v(y_m) + v(z_m) \to 0$.
2. Each $f \ne 0$ in $R_m$ has a unique term $\operatorname{in}(f)$, only a finite number of the monomials of $f$ have a value less than a given number, and $\operatorname{in}(f h) = \operatorname{in}(f) \operatorname{in}(h)$.
3. $x_N = \varphi_m + M_m x_m$. For $j < m$, $M_{j+1}$ and $M_m / M_{j+1}$ are monomials in $y_m, z_m$ with nonnegative exponents, $v(M_{j+1}) < v(M_m) < 1 + \theta$, and $v(M_m) \to 1 + \theta$. So $\varphi_m$ is a polynomial in $y_m, z_m$.

*Proof.* Part 1. With the columns $c_1, c_2$ from $P_N$ to $P_m$, $(1, \theta) = v(y_m) c_1 + v(z_m) c_2$. The ray of $(1, \theta)$ is in the cone of $c_1$ and $c_2$, and it is not on an edge, since $\theta$ is irrational. So both coefficients are positive. Also $1 = a_1 v(y_m) + a_2 v(z_m) \ge \min(a_1, a_2) (v(y_m) + v(z_m))$, and $\min(a_1, a_2) \to \infty$.

Part 2. The exponents of $f$ are in $(-k, -k) + \mathbb{N}^2$ for some $k$. By part 1 only a finite number of them have a value less than a given number, so a least value is taken, and it is taken at one monomial. In $f h$ the product of two terms has the value $v(f) + v(h)$ only if both are the least terms.

Part 3. A $y$-step gives $y_m z_m = y_{m+1} \cdot y_{m+1} z_{m+1}$, so $M_m = y_N z_N / (y_m z_m)$ by induction, and the $z$-step is the same. Then $v(M_m) = 1 + \theta - v(y_m) - v(z_m)$, and part 1 gives the claims on $v(M_m)$. The chart maps send the monomials in $y_m, z_m$ to monomials in $y_{m'}, z_{m'}$ with nonnegative exponents for $m' > m$, so $M_m / M_{j+1} = L_{j+1} \cdots L_{m-1}$ has nonnegative exponents and a positive value. The formula for $x_N$ follows from $x_m = L_m (x_{m+1} + t_m)$ by induction. $\square$

**Lemma 3.13.25.** Let $g = B_1 x^p + B_0$ with $B_0, B_1 \in K[[y, z]]$ be clean at $P_N$. Then for each $m$,
$$g_m = U_m x_m^p + V_m, \qquad U_m = B_1 M_m^p, \qquad V_m = B_1 \varphi_m^p + B_0,$$
where $B_0$ and $B_1$ are written in $y_m, z_m$. Here $U_m$ and $V_m$ are in $K[[y_m, z_m]]$, and no monomial of $U_m$ or of $V_m$ is a $p$-th power. So no step of the run needs a cleaning.

*Proof.* By Lemma 3.13.24, part 3, $x_N^p = \varphi_m^p + M_m^p x_m^p$, and this gives the formula. A monomial of $B_1 \varphi_m^p$ is a monomial of $B_1$ times the $p$-th power of a Laurent monomial, so it has the same class modulo $p$ as a monomial of $B_1$. Since $g$ is clean, the monomials of $B_0$ and of $B_1$ are not $p$-th powers. The monomial maps between the points have the determinant $\pm 1$, so they keep the property of being a $p$-th power. The same holds for $U_m$. $\square$

**Proposition 3.13.26.** In the setting of Lemma 3.13.25, assume that $V_m \ne 0$ and $v(V_m) < v(U_m)$ at a point $P_m$, with $v(0) = \infty$. Then there is an $m_0$ such that for each $m' \ge m_0$ and each choice of the later translations, $G_{m'}$ is a unit. So $\rho = 0$ at $P_{m'}$.

*Proof.* Let $S$ be the union of the supports of $U_m$ and $V_m$ in the exponents of $y_m, z_m$. The exponent $q_*$ of $\operatorname{in}(V_m)$ is the unique point of $S$ with the least value, and it is not in the support of $U_m$. The values of the monomials at $P_m$ are $v(y_m) (q_1 + \theta_m q_2)$ with $\theta_m = v(z_m) / v(y_m)$, and by Lemma 3.13.24, part 1, the cones of the later columns shrink to the ray of $(1, \theta_m)$. So the proof of Lemma 3.13.19, with the exponents $q \in \mathbb{N}^2$ in place of the pairs $(i + j, i + k)$, gives an $m_0$ such that $(q - q_*) \cdot c_s > 0$ for $s = 1, 2$, each $q \in S$ with $q \ne q_*$ and the columns $c_1, c_2$ from $P_m$ to each $P_{m'}$ with $m' \ge m_0$.

Write $x_m = \psi + M' x_{m'}$ with $M' = M_{m'} / M_m$ and $\psi = \sum_{m \le j < m'} t_j M_{j+1} / M_m$, by Lemma 3.13.24, part 3. Then $g_{m'} = U_m M'^p x_{m'}^p + U_m \psi^p + V_m$, in the coordinates of $P_{m'}$. Each monomial of $g_{m'}$ is the image of a $q \in S$ times a monomial with nonnegative exponents. For $q \ne q_*$ both exponents of $y_{m'}$ and $z_{m'}$ in the image of $q$ are larger than in the image of $q_*$. The monomial of $q_*$ comes only from $V_m$, so its coefficient is not $0$. Thus the image $\mu_0$ of $\operatorname{in}(V_m)$ is a term of $g_{m'}$, and each monomial of $g_{m'}$ is a multiple of $\mu_0$. By Theorem 3.1.4, $x^r$ is the monomial of $\mu_0$, since $\mu_0$ has no $x_{m'}$. So $G_{m'}$ has a nonzero constant term, $d = 0$, and $\rho = 0$. $\square$

**Theorem 3.13.27.** Let $g = B_1 x^p + B_0$ with $B_0, B_1 \in K[[y, z]]$ be clean at $P_N$, and let $P_N, P_{N+1}, \dots$ be a corner run with free translations. Then only a finite number of the $t_m$ are not $0$.

*Proof.* If $B_1 = 0$, Proposition 3.13.26 at $P_N$ gives $\rho = 0$ later, which is false. So $B_1 \ne 0$. Let $\mu = \operatorname{in}(B_1)$ and $u = 1 - B_1 / \mu$. Each monomial of $u$ has a positive value, so $\varepsilon = v(u) > 0$, with $\varepsilon = \infty$ if $u = 0$. Choose $k$ with $k \varepsilon > p (1 + \theta)$, and put $S_k = \sum_{i < k} u^i$ and $\zeta = S_k B_0 / \mu$ in $R_N$. Since $(1 - u) S_k = 1 - u^k$, we have
$$S_k V_m / \mu = \varphi_m^p + \zeta - u^k \varphi_m^p.$$

Assume that an infinite number of the $t_m$ are not $0$. The monomials $M_{j+1}$ are distinct, so the formal sum $\Phi = \sum_j t_j^p M_{j+1}^p$ is defined monomial by monomial. It has an infinite number of terms with a value less than $p (1 + \theta)$, and $\zeta$ has only a finite number. So there is a least value $\gamma < p (1 + \theta)$ of an exponent where the coefficients of $\Phi$ and $-\zeta$ differ. This least value exists, since the values $p \, v(M_{j+1})$ increase with $j$ and $\zeta$ has only a finite number of monomials below $p(1 + \theta)$. Choose $m$ with $p \, v(M_m) > \gamma$. The terms of $\Phi$ that are not in $\varphi_m^p$ have the values $p \, v(M_{j+1}) > \gamma$ for $j \ge m$. So $\varphi_m^p + \zeta$ has its least term at the value $\gamma$. The term $u^k \varphi_m^p$ has a value greater than $p(1 + \theta) > \gamma$. So $v(S_k V_m / \mu) = \gamma$. Since $\operatorname{in}(S_k) = 1$, this gives $V_m \ne 0$ and $v(V_m) = v(B_1) + \gamma$. Also $v(U_m) = v(B_1) + p \, v(M_m) > v(V_m)$. Proposition 3.13.26 gives $\rho = 0$ at a later point, which contradicts $\rho \ge 1$. $\square$

The proof shows where the cleaning could stop the argument for a general $g$. In this class $V_m$ is $g$ at $x = \varphi_m$, and the products of $\varphi_m^p$ with the monomials of $B_1$ are never $p$-th powers. So the least term of $V_m$ stays in $g_m$. For a general $g$ the terms of $g(\varphi_m + M_m x_m)$ that are $p$-th powers are removed by the cleaning, and the least term can be one of them.

**Corollary 3.13.28.** Let $g$ and the run be as in Theorem 3.13.27, let $J$ be the last index with $t_J \ne 0$, and let $J = N - 1$ if all $t_m$ are $0$. Then $P_{J+1}, P_{J+2}, \dots$ is a run of Theorem 3.13.20 in the coordinates of the run. So for $m$ large both corner curves at $P_m$ have $\nu^G = d_m \ge \rho$, and Question 3.13.18 has a positive answer for this run.

*Proof.* From $P_{J+1}$ on, each step is at the origin of the $y$-chart or of the $z$-chart, and each chart occurs an infinite number of times. The point $g_{J+1}$ is clean, $V(x_{J+1})$ is not in $\Delta$, and the run keeps $\rho$. These are the hypotheses of Theorem 3.13.20. $\square$

The polynomial $\varphi_{J+1}$ is a polynomial in $y_{J+1}, z_{J+1}$, but it need not be a polynomial in $y_N, z_N$, since some $M_{j+1}$ can have a negative exponent of $y_N$ or $z_N$. For this reason the corollary uses the coordinates of $P_{J+1}$ and not the coordinates $(x_N - \varphi_{J+1}, y_N, z_N)$ at $P_N$. A computer test over $\mathbb{F}_2$ and $\mathbb{F}_3$ from $500$ random clean starts of the form $B_1 x^p + B_0$ checked Lemma 3.13.25 at $26901$ points, Proposition 3.13.26 in $17274$ trials and the identity of the proof of Theorem 3.13.27 in $53764$ cases, with no failure.

Node: SG0000005W

A weaker form of Question 3.13.18 asks for regular $Z_k$ at $P_k$ with $G_k \in I_{Z_k}^\rho + \mathfrak{m}_{P_k}^{M_k}$ and $M_k \to \infty$. In Example 3.13.15 this holds with $Z_k = V(x_k)$, and this form may be what a proof by the data of the run can give.

### What this means for the centers

The results of this section change the plan of Section 3.12 in four ways.

1. The centers come from the locus of $\rho$ or of the order of $G$, and not from $d$ or $\tau_\rho$. These two functions are data at the closed points only, by part 4 of Example 3.13.11.
2. If a run follows a formal curve, the center is the component of the locus that contains the curve, and it can have dimension $2$ or more. A formal curve is not sufficient, since it can be transcendental.
3. If a run takes an infinite number of corner steps, no subvariety that the run follows need be in the locus, by Example 3.13.15. Then the center must come from a part of the locus that the run does not follow, such as the corner curves of Remark 3.13.17. So the centers cannot be found by a study of one run at a time.
4. The next question is the step at such a center: for a regular center $Z$ in the locus, with normal crossings with $\Delta$, does $\rho$ go down at each point over $Z$ after the blowups of the components in a good order? Example 3.13.11 shows that the order of the blowups is important, since only the order with $V(x_1, x_2)$ first satisfies (H2) at each step.

### Notes and references

Example 3.13.11 is Example 3.18 of [CP19], in the coordinates of this chapter. The transcendence argument uses the theorem of Christol [Chr79]. The use of the history of the divisor is from [CJS20], and maximal contact is from [Hir64]. Lemma 3.13.1, Theorems 3.13.6 and 3.13.8, Example 3.13.10, Hypothesis 3.13.12, Question 3.13.13, Lemma 3.13.14, Example 3.13.15, Remarks 3.13.16 and 3.13.17, Question 3.13.18, Lemma 3.13.19, Theorem 3.13.20 and Example 3.13.21 are a result of the milestone S7.18 of this project (tamnd/singularity#245).
