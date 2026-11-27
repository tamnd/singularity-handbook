---
title: Toric branches with positive residual slope
nodes: [SG000000BE, SG000000BF, SG000000BG, SG000000BH]
sources: [Hir67, CP19, Spi83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Toric branches with positive residual slope

Section 4.4 proves that Rule 61.9' terminates at the points with $\omega = 0$ (Theorem 4.4.13). The case $\omega > 0$ is open (Conjecture 4.4.6). The natural plan for that case is a lexicographic invariant: first $\omega$, and then a secondary quantity that drops on each run where $\omega$ stays the same. On the period-5 runs of Proposition 4.4.14 such a quantity exists. It is the gap $\frac{e-2}5$, but it is hidden in the exponents, and the proof in Section 4.4 does not explain where it comes from. This section finds the general form of this quantity in a model case, and it shows where the plan stops.

The model case is the *toric model*. It is the part of the rule where the boundary is full, $E = \{0, 1, 2\}$, each new point is the origin of its chart, and the coordinate $z$ stays prepared. Then the rule acts on a finite set of points of $\mathbb Q^3$ by fixed affine maps. The main result is that $\omega$ never goes up in the toric model, and that each run with $\omega$ constant is finite (Theorem 4.5.9). So each toric branch is finite. Let $\ell$ be the length of the longest continuation with $\omega$ constant. Then the pair $(\omega, \ell)$ drops at each step (Corollary 4.5.10). The proof has stages, and each stage has its own explicit quantity that drops. For the family of Proposition 4.4.14, the quantity of the last stage is the hidden gap (Proposition 4.5.11).

The plan stops in two places. First, no lexicographic pair that starts with $\omega$ can drop at each step of the rule, because $\omega$ goes up at the steps of Theorems 4.4.7 and 4.4.8 (Proposition 4.5.14). Second, the computer finds steps of the rule that keep $\omega$ and are not toric. At these steps, none of the quantities of this section is defined (Example 4.5.15).

### The toric model

We keep the setting of Section 4.4. So $p$ is an odd prime, $k$ is a perfect field of characteristic $p$, $R = k[[x_0, x_1, x_2]]$, and $f = z^{2p} + a_1 z^{2p-1} + \dots + a_{2p}$ with $\operatorname{ord} a_i \ge i$. Let $B = \operatorname{lcm}(1, \dots, 2p)$. In this section the boundary is $E = \{0, 1, 2\}$, except in Example 4.5.15. Then all base coordinates are adapted to $E$, each $x_k$ is fixed up to a unit, and the coordinate center $V(z, x_S)$ depends only on $S$. For a nonempty $S \subseteq \{0, 1, 2\}$ we write $\delta_S = \delta(\mathbb 1_S)$. So $\delta_{\{k\}} = \mu_k$ and $\delta_{\{0,1,2\}} = \delta$.

For $u \in \mathbb Q^3$ we write $|u| = u_0 + u_1 + u_2$ and $u_S = \sum_{k \in S} u_k$. For a finite set $U \subset \mathbb Q^3_{\ge 0}$ we put
$$\delta_S(U) = \min_{u \in U} u_S, \qquad \mu_k(U) = \delta_{\{k\}}(U), \qquad \delta(U) = \delta_{\{0,1,2\}}(U), \qquad \omega(U) = \delta(U) - \sum_{k=0}^2 \mu_k(U).$$
For a coordinate $z$ let $U(f, z)$ be the set of the points $\alpha / i$, where $1 \le i \le 2p$ and $x^\alpha$ is a monomial of $a_i$. Since $v_{\mathbb 1_S}(a_i) = \min \alpha_S$ over the monomials $x^\alpha$ of $a_i$, we have $\delta_z(\mathbb 1_S) = \delta_S(U(f, z))$. So if $z$ is simultaneously prepared, then $\delta_S = \delta_S(U(f, z))$ for each $S$, and the invariants of the point are the invariants of the set $U(f, z)$.

**Definition 4.5.1 (the toric model and the toric branches).** Let $U \subset \mathbb Q^3_{\ge 0}$ be finite. A *step* of $U$ has a center $S \subseteq \{0, 1, 2\}$ and a chart $j \in S$, as follows.

1. *Divisorial step.* If $\mu_k(U) \ge 1$ for some $k$, then $S = \{k\} = \{j\}$, with $k$ chosen as in Definition 4.4.5 (1).
2. *Main step.* If $\mu_k(U) < 1$ for all $k$ and $\omega(U) > 0$, then $S$ is a curve $\{k, l\}$ with $\delta_S(U) \ge 1$ and $\delta_S(U) - \mu_k(U) - \mu_l(U) = \omega(U)$, if such a curve exists, and $S = \{0, 1, 2\}$ if no such curve exists. Any $j \in S$ is allowed.

The step replaces each $u \in U$ by the point $u'$ with
$$u'_j = u_S - 1, \qquad u'_k = u_k \quad (k \ne j).$$
The step is *allowed* if the new set $U'$ has $\delta(U') \ge 1$. A *run* of the toric model is a sequence $U_0, U_1, \dots$ in which $U_{n+1}$ comes from $U_n$ by an allowed step. A run stops at $U_n$ if $\omega(U_n) = 0$ or if no step of $U_n$ is allowed.

A *toric branch* of Rule 61.9' is a sequence $\xi_0, \xi_1, \dots$ of the rule (Definition 4.4.5), for any choice among tied centers, with $E = \{0, 1, 2\}$ at $\xi_0$, such that the following holds. If $V(z_n, x_S)$ is the center at $\xi_n$, then $\xi_{n+1}$ is the origin of the chart of some $x_j$ with $j \in S$, and the coordinate $z_{n+1} = z_n / x_j$ is simultaneously prepared at $\xi_{n+1}$. Here $z_0$ is a simultaneously prepared coordinate at $\xi_0$.

At the origin of a chart the boundary is again $\{0, 1, 2\}$: it consists of the exceptional divisor $V(x_j)$, the strict transforms $V(x'_k)$ for $k \in S \setminus \{j\}$, and the $V(x_l)$ for $l \notin S$, and all of them pass through the origin. The moves of the toric model are the moves of the polyhedra game of Hironaka. In that game, Rule 61.9' is one fixed strategy for the player who chooses $S$. Spivakovsky proved that this player has a winning strategy [Spi83]. That result does not say that a given strategy wins, so it does not apply here.

**Lemma 4.5.2 (rigid germs follow the toric model).**

1. Along a toric branch, the sets $U_n = U(f_n, z_n)$ form a run of the toric model. The invariants $\delta$, $\mu_k$, $\delta_S$ and $\omega$ at $\xi_n$ are those of $U_n$, the center of the rule at $\xi_n$ is the center of a step of $U_n$, and $U_{n+1}$ is the image of $U_n$ under that step.
2. If $a_p = a_{2p} = 0$ and $E = \{0, 1, 2\}$, then each sequence of the rule in which each point is the origin of a chart is a toric branch.

*Proof.* (1) Let $V(z, x_S)$ be the center at $\xi_n$ and $j \in S$. At the origin of the chart of $x_j$ the substitution is $x_k = x_j x'_k$ for $k \in S \setminus \{j\}$ and $z = x_j z'$, and $a'_i = a_i / x_j^i$ by Remark 4.4.2 (6). So a monomial $x^\alpha$ of $a_i$ becomes the monomial $x^{\alpha'}$ with
$$\alpha'_j = \alpha_S - i, \qquad \alpha'_k = \alpha_k \quad (k \ne j).$$
Divided by $i$, this is the map of Definition 4.5.1. For a fixed $i$ the map $\alpha \mapsto \alpha'$ is injective. So two monomials of $a_i$ never go to the same monomial, there is no cancellation, and the support of $a'_i$ is the image of the support of $a_i$. Hence $U_{n+1}$ is the image of $U_n$.

Since $z_n$ is simultaneously prepared, the invariants at $\xi_n$ are those of $U_n$, as shown before Definition 4.5.1. The center of Definition 4.4.5 depends only on these invariants. Indeed, the divisorial step depends on the $\mu_k$, and the monomial step is taken when $\omega = 0$. For the main step, $V(z, x_S)$ is permissible if and only if $\delta_S \ge 1$ (Remark 4.4.2 (4)), and since $E$ is full, $\omega(\eta_S) = \delta_S - \sum_{k \in S} \mu_k$. A surface $V(z, x_k)$ is permissible only if $\mu_k \ge 1$, and then the rule takes the divisorial step. So the main step blows up a permissible curve with $\omega(\eta_S) = \omega$ if there is one, since the rule takes the center of largest dimension, and the point otherwise. These are the centers of Definition 4.5.1. Finally, $\xi_{n+1}$ has multiplicity $2p$ if and only if $\operatorname{ord} a'_i \ge i$ for each $i$, that is, if and only if $|u| \ge 1$ for each $u \in U_{n+1}$, that is, $\delta(U_{n+1}) \ge 1$. So the step is allowed.

(2) The substitution $a'_i = a_i / x_j^i$ keeps $a_p = 0$ and $a_{2p} = 0$. Let $w$ be one of the seven weights, and suppose that the vertex of $z_n$ for $w$ is solvable with the form $C$. Then $\operatorname{in}_w a_{2p} = C^{2p} \ne 0$, which is false since $a_{2p} = 0$. So no vertex is solvable, and $\delta(w) = \delta_{z_n}(w)$ by Remark 4.4.2 (1). So $z_n$ is simultaneously prepared at each point, and the sequence is a toric branch. $\square$

A germ with $a_{2p} = 0$ has the factor $z$, so $V(f)$ contains the component $V(z)$. It is reduced if $a_{2p-1} \ne 0$ and $f / z$ is reduced, as in Example 4.5.13 below.

### The normalised polyhedron and one step

Each point of $U(f, z)$ has the form $\alpha / i$ with $i \le 2p$, so it lies in $\frac1B \mathbb Z^3$. The maps of Definition 4.5.1 keep $\frac1B \mathbb Z^3$. So along a run all points lie in $\frac1B \mathbb Z^3$, and so do $\delta$, $\mu_k$, $\delta_S$ and $\omega$.

**Definition 4.5.3 (normalised points and the bottom face).** Let $U$ be as in Definition 4.5.1 and $\mu = (\mu_0, \mu_1, \mu_2)$, with $\mu_k = \mu_k(U)$. The *normalised points* are the points $v = u - \mu$ with $u \in U$, and $V$ is the set of them. So $V \subset \mathbb Q^3_{\ge 0}$, $\min_{v \in V} v_k = 0$ for each $k$, and $\omega = \min_{v \in V} |v|$. Let $N$ be the convex hull of $V$ plus $\mathbb R^3_{\ge 0}$. The *bottom face* is
$$\mathcal F = N \cap \{|v| = \omega\}.$$
For $S \subseteq \{0, 1, 2\}$ put $\omega_S = \min_{v \in V} v_S$.

So $\delta_S = \omega_S + \sum_{k \in S} \mu_k$, and a curve $S$ has $\omega(\eta_S) = \omega$ if and only if $\omega_S = \omega$. The face $\mathcal F$ is a polytope, since $N \subset \mathbb R^3_{\ge 0}$, and its vertices are points of $V$. The point $\mu$ lies in $N + \mu$ if and only if $0 \in N$, that is, if and only if $\omega = 0$. So $\omega = 0$ means that the polyhedron is the orthant $\mu + \mathbb R^3_{\ge 0}$, as in Theorem 4.4.13.

A map $T \colon \mathbb R^3 \to \mathbb R^3$ is *monotone* if each coordinate of $T(v)$ is an affine function of $v$ with nonnegative coefficients. A monotone map sends the convex hull of a set to the convex hull of its image, and it sends $x + \mathbb R^3_{\ge 0}$ into $T(x) + \mathbb R^3_{\ge 0}$.

**Lemma 4.5.4 (one step).** Let $U'$ come from $U$ by a main step with center $S$ and chart $j \in S$. Then $\omega_S = \omega$: for a curve by Definition 4.5.1 (2), and for the point because $\omega_{\{0,1,2\}} = \omega$.

1. The new normalised points are $V' = T(V)$, where $T(v)_j = v_S - \omega$ and $T(v)_k = v_k$ for $k \ne j$. The map $T$ is monotone. The new boundary slopes are $\mu'_j = \delta_S - 1$ and $\mu'_k = \mu_k$ for $k \ne j$. A divisorial step at $k$ does not change $V$, and it lowers $\mu_k$ and $\delta$ by $1$. So it does not change $\omega$ and $\mathcal F$.
2. The new residual slope is $\omega' = \min_{v \in V}(|v| + v_{S \setminus \{j\}}) - \omega$. So $\omega' \le \omega$, with equality if and only if $|v| + v_{S \setminus \{j\}} \ge 2\omega$ for each $v \in V$.
3. If $\omega' = \omega$, then each point of $\mathcal F$ has its support in $S \setminus \{j\}$, the map $T$ fixes each point of $\mathcal F$, and $\mathcal F \subseteq \mathcal F'$. If $S = \{j, l\}$ is a curve, then $\mathcal F = \{\omega e_l\}$.
4. Along a run on which $\omega$ is constant, $\mathcal F' \ne \mathcal F$ happens at most $\frac12(B\omega + 1)(B\omega + 2)$ times.

*Proof.* (1) For $u \in U$ with $v = u - \mu$ we have $u'_j = u_S - 1 = v_S + \sum_{k \in S} \mu_k - 1$. The minimum over $U$ is $\omega_S + \sum_{k \in S} \mu_k - 1 = \delta_S - 1$. So $\mu'_j = \delta_S - 1$ and $v'_j = u'_j - \mu'_j = v_S - \omega_S = v_S - \omega$. The other coordinates do not change. A divisorial step at $k$ has $S = \{k\}$, so it replaces $u_k$ by $u_k - 1$ for each $u$. So $\mu_k$ and $\delta$ drop by $1$, and $V$ does not change.

(2) We have $|T(v)| = |v| - v_j + v_S - \omega = |v| + v_{S \setminus \{j\}} - \omega$, and $\omega' = \min_{v \in V} |T(v)|$. Take $v \in V$ with $|v| = \omega$. Since $v \ge 0$, we have $v_{S \setminus \{j\}} \le |v| = \omega$, so $|T(v)| \le \omega$. This gives $\omega' \le \omega$, and the condition for equality.

(3) The function $v \mapsto |v| + v_{S \setminus \{j\}}$ is linear with nonnegative coefficients. So if it is at least $2\omega$ on $V$, it is at least $2\omega$ on $N$. For $v \in \mathcal F$ this reads $v_{S \setminus \{j\}} \ge \omega = |v|$. Since $v \ge 0$, the support of $v$ is in $S \setminus \{j\}$. Then $v_j = 0$ and $v_S = |v| = \omega$, so $T(v)_j = 0 = v_j$ and $T(v) = v$. Since $T$ is monotone, $T(N) \subseteq N'$, where $N'$ is the convex hull of $V'$ plus $\mathbb R^3_{\ge 0}$. So $\mathcal F = T(\mathcal F) \subseteq N' \cap \{|v| = \omega'\} = \mathcal F'$. If $S = \{j, l\}$, a point $v \ge 0$ with support in $\{l\}$ and $|v| = \omega$ is $\omega e_l$.

(4) Let $\Lambda$ be the set of the points of $\frac1B \mathbb Z^3_{\ge 0}$ with $|v| = \omega$. It has $\frac12(B\omega + 1)(B\omega + 2)$ elements. The vertices of $\mathcal F$ lie in $\Lambda$. By (1) and (3), $\mathcal F$ does not get smaller along the run. If $\mathcal F' \ne \mathcal F$, then $\mathcal F'$ has a vertex outside $\mathcal F$, so $\mathcal F' \cap \Lambda$ is strictly larger than $\mathcal F \cap \Lambda$. Since $\mathcal F \cap \Lambda$ is not empty, this happens at most $|\Lambda| - 1$ times. $\square$

So along a run on which $\omega$ is constant, $\mathcal F$ is constant after finitely many steps. There are two cases: $\mathcal F$ is the vertex $\omega e_b$ on an axis, or it is not.

### The bottom face is not an axis vertex

**Proposition 4.5.5 (the face is not an axis vertex).** Let $U_0, U_1, \dots$ be a run of the toric model on which $\omega$ and $\mathcal F$ are constant. If $\mathcal F \ne \{\omega e_b\}$ for each $b$, then the run is finite.

*Proof.* Each divisorial step lowers $\delta$ by $1$, and $\delta \ge 1$ along the run. So it is enough to bound the number of main steps. By Lemma 4.5.4 (3), a curve step that keeps $\omega$ needs $\mathcal F = \{\omega e_l\}$. So each main step of the run is a point blowup, in a chart $j$ with $\mathcal F \subseteq \{v_j = 0\}$. If $\mathcal F \subseteq \{v_j = 0\}$ for no $j$, the run has no main step. If $\mathcal F \subseteq \{v_j = 0\} \cap \{v_{j'} = 0\}$ with $j \ne j'$, then $\mathcal F = \{\omega e_b\}$ for the third index $b$, which is excluded. So $j$ is unique. Let $a$ and $c$ be the other two indices.

Follow each point $g \in V_0$ through the run, and put
$$\kappa(g) = g_a + g_c - \omega.$$
A point step in the chart $j$ gives $T(g)_j = |g| - \omega$, $T(g)_a = g_a$ and $T(g)_c = g_c$. So $\kappa(g)$ does not change, and $|T(g)| = |g| + \kappa(g)$. Divisorial steps change nothing.

*Case 1: $\kappa(g) < 0$ for some $g$.* Then each point step lowers $|g|$ by $|\kappa(g)|$. But $|g| \ge \omega$ along the run. So there are at most $(|g| - \omega) / |\kappa(g)|$ point steps.

*Case 2: $\kappa(g) \ge 0$ for each $g$.* Let $T = \{a, c\}$. Then $\omega_T = \omega + \min_g \kappa(g) \ge \omega$. A vertex $v$ of $\mathcal F$ is a point of $V$ with $v_j = 0$ and $|v| = \omega$, so $v_a + v_c = \omega$. Hence $\omega_T = \omega$, and the curve $T$ has $\omega(\eta_T) = \omega$. If $\delta_T = \omega + \mu_a + \mu_c \ge 1$, the curve $T$ is a candidate of Definition 4.5.1 (2). Then the main step is a curve step, and it lowers $\omega$ by Lemma 4.5.4 (3), so this is the last step of the run. If $\omega + \mu_a + \mu_c < 1$, a point step in the chart $j$ gives $\mu'_j = \delta - 1$ by Lemma 4.5.4 (1), and so
$$\delta' = \omega + \mu_a + \mu_c + \mu'_j = \delta - (1 - \omega - \mu_a - \mu_c).$$
The number $1 - \omega - \mu_a - \mu_c$ is positive and lies in $\frac1B \mathbb Z$, so $\delta$ drops by at least $\frac1B$. Point steps in the chart $j$ do not change $\mu_a$ and $\mu_c$, and divisorial steps do not raise them. So $\omega + \mu_a + \mu_c < 1$ stays true, and each point step lowers $\delta$ by at least $\frac1B$. Since $\delta \ge 1$, the run is finite. $\square$

### The bottom face is an axis vertex: the projection to the plane

Now let $\mathcal F = \{A\}$ with $A = \omega e_b$, and let $a$ and $c$ be the other two indices. By Lemma 4.5.4 (3), a main step that keeps $\omega$ is one of the following.

- $P_a$ and $P_c$: the point blowup in the chart of $x_a$ or $x_c$.
- $C_a$ and $C_c$: the curve $\{a, b\}$ in the chart of $x_a$, or the curve $\{c, b\}$ in the chart of $x_c$.

A step in the chart of $x_b$ lowers $\omega$, since the support $\{b\}$ of $A$ is not contained in $S \setminus \{b\}$. The curve $\{a, c\}$ is never a candidate, since $\omega_{\{a,c\}} \le A_a + A_c = 0 < \omega$.

Let $g \in V$ with $g \ne A$ and $g_b \ge \omega$. Then $g \ge A$ in each coordinate. Each step of the list above is monotone and fixes $A$, so the image of $g$ is again at least the image of $A$ in each coordinate. Each invariant of the model is a minimum of a linear function with nonnegative coefficients. So we can omit these points. The other points have
$$w(g) = \omega - g_b > 0.$$
There is at least one of them: some point of $V$ has $g_b = 0 < \omega$, since $\min_V v_b = 0$. For these points put
$$q(g) = (s, t) = \Big(\frac{g_a}{w(g)}, \frac{g_c}{w(g)}\Big).$$
Let $Q$ be the convex hull of the points $q(g)$ plus $\mathbb R^2_{\ge 0}$. Put $m_s = \min_Q s$, $m_t = \min_Q t$, $h = \min_Q(s + t)$ and $\omega_2 = h - m_s - m_t \ge 0$. These minima are reached at the points $q(g)$.

**Lemma 4.5.6 (the projection).** Let $\mathcal F = \{\omega e_b\}$.

1. The steps $P_a$, $P_c$, $C_a$ and $C_c$ do not change $w(g)$, and they act on $q$ by
$$P_a \colon s \mapsto s + t - 1, \qquad P_c \colon t \mapsto s + t - 1, \qquad C_a \colon s \mapsto s - 1, \qquad C_c \colon t \mapsto t - 1,$$
with the other coordinate fixed. Divisorial steps do not change $q$.
2. $Q \subset \{s + t > 1\}$. After one of the four steps, $\omega' = \omega$ if and only if the new set $Q'$ lies in $\{s + t \ge 1\}$, and then $\mathcal F' = \mathcal F$ if and only if $Q' \subset \{s + t > 1\}$.
3. Put $\beta = \mu_b + \omega$. The step $C_a$ is a candidate of Definition 4.5.1 (2) if and only if $m_s \ge 1$ and $\mu_a + \beta \ge 1$, and the same holds for $C_c$ with $m_t$ and $\mu_c$. If $C_a$ or $C_c$ is a candidate, then the main step is a curve step.
4. $q(g) \in \frac1L \mathbb Z^2$, with $L = \operatorname{lcm}(1, \dots, B\omega)$.

*Proof.* (1) For $P_a$ we get $g'_a = |g| - \omega = g_a + g_c - w(g)$, and for $C_a$ we get $g'_a = g_a + g_b - \omega = g_a - w(g)$. In both cases $g_b$ and $g_c$ do not change, so $w(g)$ does not change. Divide by $w(g)$. The steps in the chart of $x_c$ are the same with $a$ and $c$ exchanged.

(2) We have $|g| - \omega = g_a + g_c - w(g) = w(g)(s + t - 1)$. So $|g| > \omega$ if and only if $s + t > 1$. Since $\mathcal F = \{A\}$, each point $g \ne A$ of $V$ has $|g| > \omega$, and so $Q \subset \{s + t > 1\}$. After the step, $\omega' = \min |g'|$, where $A$ and the omitted points do not matter. The face $\mathcal F'$ contains a point $g' \ne A$ exactly when $|g'| = \omega$. A half plane contains $Q'$ if and only if it contains the points $q(g')$.

(3) For a point $g$ with $w(g) > 0$ we have $g_a + g_b = \omega + w(g)(s - 1)$. The point $A$ gives $A_a + A_b = \omega$, and the omitted points give at least $\omega$. So $\omega_{\{a,b\}} = \omega$ if and only if $s \ge 1$ at each $q(g)$, that is, $m_s \ge 1$. Also $\delta_{\{a,b\}} = \omega + \mu_a + \mu_b = \mu_a + \beta$. The rule takes a curve when there is a candidate curve.

(4) We have $w(g) \in \frac1B \mathbb Z$ and $0 < w(g) \le \omega$, so $w(g) = n / B$ with $1 \le n \le B\omega$. Then $g_a / w(g) = B g_a / n \in \frac1n \mathbb Z$, since $B g_a$ is an integer. $\square$

The moves of Lemma 4.5.6 are again moves of a polyhedra game, now in the plane. Put $Q^\circ = Q - (m_s, m_t)$ and $q^\circ = q - (m_s, m_t)$. Then $\min_{Q^\circ} (s + t) = \omega_2$, so $\omega_2$ is the residual slope of the planar game. The moves $C_a$, $C_c$ and the divisorial steps only translate $Q$, so they do not change $Q^\circ$. The move $P_a$ gives $m'_s = h - 1$ and $m'_t = m_t$, so it acts on $q^\circ$ by $s^\circ \mapsto s^\circ + t^\circ - \omega_2$. This is the map $T$ of Lemma 4.5.4 (1) in the plane.

**Proposition 4.5.7 (the stage $\omega_2 > 0$).** Along a run of the toric model on which $\omega$ is constant and $\mathcal F = \{\omega e_b\}$, the planar residual slope $\omega_2$ never goes up, and only finitely many steps of the run have $\omega_2 > 0$.

*Proof.* Only $P_a$ and $P_c$ change $Q^\circ$. Consider $P_a$. The new set $Q'$ is the convex hull of the new points plus $\mathbb R^2_{\ge 0}$, so $h' = \min_q(s + 2t) - 1$ over the points $q = q(g)$. Hence
$$\omega'_2 = h' - m'_s - m'_t = \min_q(s + 2t) - h - m_t = \min_q(s^\circ + 2t^\circ) - \omega_2.$$
Take $q$ with $s^\circ + t^\circ = \omega_2$. Then $s^\circ + 2t^\circ \le 2\omega_2$, because $s^\circ \ge 0$. So $\omega'_2 \le \omega_2$. The same holds for $P_c$.

Now suppose that $\omega_2 > 0$ is constant on a part of the run. Let $\mathcal F_2 = Q^\circ \cap \{s + t = \omega_2\}$ be the planar bottom face. If $P_a$ keeps $\omega_2$, then $s^\circ + 2t^\circ \ge 2\omega_2$ on $Q^\circ$, and on $\mathcal F_2$ this gives $t^\circ \ge \omega_2$, so $\mathcal F_2 = \{(0, \omega_2)\}$. The point $(0, \omega_2)$ is fixed by the planar map of $P_a$, so it stays in $\mathcal F_2$, as in Lemma 4.5.4 (3). A move $P_c$ that keeps $\omega_2$ needs $\mathcal F_2 = \{(\omega_2, 0)\}$, and this set does not contain $(0, \omega_2)$. So after the first $P$ move of this part of the run, all $P$ moves are of the same kind, say $P_a$.

Let $g$ be a point with $t(g) = m_t$. The moves $P_a$ and $C_a$ change neither $t(g)$ nor $m_t$, and $C_c$ lowers both by $1$. So $t(g) = m_t$ stays true. At each move $P_a$,
$$s'(g) - m'_s = s(g) + m_t - 1 - (h - 1) = (s(g) - m_s) - \omega_2,$$
and the moves $C_a$ and $C_c$ do not change $s(g) - m_s$. Since $s(g) - m_s \ge 0$, there are at most $(s(g) - m_s) / \omega_2$ moves $P_a$ in this part of the run. Between two $P$ moves, each $C$ move lowers $m_s$ or $m_t$ by $1$, and by Lemma 4.5.6 (3) it needs this value to be at least $1$. So there are at most $m_s + m_t$ moves $C$ between two $P$ moves. Between two main steps there are finitely many divisorial steps, since each lowers $\delta$ by $1$. So this part of the run is finite. The values of $\omega_2$ lie in $\frac1L \mathbb Z_{\ge 0}$ by Lemma 4.5.6 (4), and they never go up. So $\omega_2$ takes only finitely many positive values, and the stage $\omega_2 > 0$ is finite. $\square$

### The orthant regime

Let $\omega_2 = 0$. Take a point $q$ with $s + t = h$. Since $s \ge m_s$, $t \ge m_t$ and $h = m_s + m_t$, we get $q = (m_s, m_t)$. So $Q = c + \mathbb R^2_{\ge 0}$ with $c = (c_a, c_c) = (m_s, m_t)$, and this stays true, since $\omega_2$ does not go up. We call this the *orthant regime*. Put $h = c_a + c_c$, so $h > 1$, and $\sigma = \mu_a + \mu_c$. At each main step $\mu_a, \mu_c, \mu_b < 1$, since otherwise the rule takes a divisorial step. The steps of the list do not change $\mu_b$, so $\beta = \mu_b + \omega$ is constant, and $\delta = \sigma + \beta$. By Lemmas 4.5.4 and 4.5.6, the run is the following system.

- $C_k$, for $k \in \{a, c\}$, is a candidate if and only if $c_k \ge 1$ and $\mu_k + \beta \ge 1$. It gives $\mu_k \mapsto \mu_k + \beta - 1$ and $c_k \mapsto c_k - 1$.
- $P_k$ is taken only if no $C$ move is a candidate. It gives $\mu_k \mapsto \sigma + \beta - 1$ and $c_k \mapsto h - 1$.
- After each main step in the chart $k$, divisorial steps lower $\mu_k$ by $1$ until $\mu_k < 1$. They do not change $c$.
- The run continues while $h > 1$ and $\delta = \sigma + \beta \ge 1$.

**Proposition 4.5.8 (the orthant regime is finite).** A run of the toric model on which $\omega$ is constant, $\mathcal F = \{\omega e_b\}$ and $\omega_2 = 0$ is finite.

*Proof.* Put $\varepsilon = 1 - \beta$ and $H = \max(c_a, c_c)$. A state is *doubly stuck* if $c_a, c_c \ge 1$ and $\mu_a, \mu_c < \varepsilon$. This needs $\beta < 1$.

*Step 1: a doubly stuck state reaches the end of the run within $B$ steps.* In a doubly stuck state no $C$ move is a candidate, so the move is $P_a$ or $P_c$, say $P_a$. The new value $\mu'_a = \sigma + \beta - 1 = \sigma - \varepsilon$ is less than $\varepsilon \le 1$, since $\sigma < 2\varepsilon$. So no divisorial step follows, and $\mu'_a < \varepsilon$. The new $c'_a = c_a + c_c - 1 \ge 1$. So the new state is again doubly stuck. The new $\sigma' = \sigma - \varepsilon + \mu_c$ is less than $\sigma$ by $\varepsilon - \mu_c > 0$, and this difference lies in $\frac1B \mathbb Z$, so it is at least $\frac1B$. Along the run $\delta \ge 1$, that is, $\sigma \ge \varepsilon$. Since $\sigma < 2\varepsilon \le \varepsilon + 1$, there are fewer than $B$ such moves.

*Step 2: outside the doubly stuck states, $H$ does not go up.* A move $C_k$ lowers $c_k$. Let $P_a$ be the move. If $c_c < 1$, then $c'_a = c_a + c_c - 1 < c_a$. Let $c_c \ge 1$. Then $C_c$ is not a candidate, so $\mu_c + \beta < 1$, that is, $\mu_c < \varepsilon$. If also $c_a \ge 1$, then $C_a$ is not a candidate either, so $\mu_a < \varepsilon$, and the state is doubly stuck. So $c_a < 1$ and $c'_a = c_a + c_c - 1 < c_c \le H$. The move $P_c$ is the same with $a$ and $c$ exchanged.

*Step 3: $H$ stays constant only for finitely many steps.* Suppose first that $c_a < c_c = H$ on a part of the run where $H$ is constant and no state is doubly stuck. A move $C_c$ lowers $H$. A move $P_c$ gives $c'_c = c_a + c_c - 1$. Here $c_a < 1$: if $c_a \ge 1$, then $c_c > 1$, and $P_c$ is taken only if both $C$ moves are blocked, so the state is doubly stuck. So $c'_c < c_c$, and $P_c$ lowers $H$ too. So only $C_a$, $P_a$ and divisorial steps occur, and $c_c$ and $\mu_c$ do not change. There are three cases.

- If $c_c \ge 1$ and $\mu_c \ge \varepsilon$, then $C_c$ is a candidate, so each main step is a curve step. It is not $C_c$, so it is $C_a$, and it lowers $c_a$ by $1$. Since $c_a \ge 0$, this happens finitely often.
- If $c_c \ge 1$ and $\mu_c < \varepsilon$, then $\varepsilon > 0$. A move $P_a$ gives $\mu'_a = \mu_a + \mu_c - \varepsilon < \mu_a$, with no divisorial step since $\mu'_a < 1$. A move $C_a$ needs $\mu_a + \beta \ge 1$ and gives $\mu'_a = \mu_a - \varepsilon < \mu_a$, again with no divisorial step. So $\mu_a \in \frac1B \mathbb Z_{\ge 0}$ drops at each main step, and this happens finitely often.
- If $c_c < 1$, then $c_a < 1$, no $C$ move is a candidate, and $P_a$ lowers $c_a$ by $1 - c_c \ge \frac1L$. Since $c_a \ge 0$, this happens finitely often.

Also $c_a$ never reaches $H$ again, since $c'_a = c_a + c_c - 1 < c_c$ after $P_a$ and $C_a$ lowers $c_a$. If $c_a = c_c = H$, a step that does not start at a doubly stuck state is a move $C_k$, or a move $P_k$ with $H < 1$, since for $H \ge 1$ a move $P_k$ needs both $C$ moves to be blocked. In both cases the two coordinates become different, and $H$ does not change. Then the first case applies.

*Conclusion.* Since $h > 1$, we have $H > \frac12$, and $H \in \frac1L \mathbb Z$ by Lemma 4.5.6 (4). By Step 2, $H$ does not go up until the run reaches a doubly stuck state, and by Step 3 it drops after finitely many steps. So it drops only finitely often, and after finitely many steps the run reaches a doubly stuck state or ends. By Step 1 it then ends within $B$ steps. Between two main steps there are finitely many divisorial steps. $\square$

If $\beta \ge 1$, there are no doubly stuck states, and the proof gives more. A move $C_k$ lowers $h$ by $1$. If $P_a$ is taken, then $C_c$ is not a candidate, and since $\mu_c + \beta \ge 1$ this means $c_c < 1$. So $P_a$ lowers $h$ by $1 - c_c \ge \frac1L$. So each main step lowers $h$ by at least $\frac1L$, and the orthant regime has at most $L(h - 1)$ main steps. This is the case of the family of Proposition 4.4.14, where $\beta = \frac53$.

### Termination along toric branches

**Theorem 4.5.9 (toric branches are finite).** In the toric model, $\omega$ never goes up, and each run on which $\omega$ is constant is finite. So each toric branch of Rule 61.9' is finite. It reaches a point with $\omega = 0$, after which Theorem 4.4.13 applies, or it reaches a center over which no chart origin has multiplicity $2p$. In particular, for each germ with $a_p = a_{2p} = 0$ and $E = \{0, 1, 2\}$, each sequence of the rule through chart origins is finite.

Node: SG000000BE

*Proof.* By Lemma 4.5.4 (2), a main step does not raise $\omega$, and by Lemma 4.5.4 (1) a divisorial step does not change it. Since $\omega \in \frac1B \mathbb Z_{\ge 0}$, it drops only finitely often. So it is enough to show that each run on which $\omega$ is constant is finite.

Take such a run. By Lemma 4.5.4 (4), the face $\mathcal F$ changes only finitely often, so the run is a union of finitely many parts on which $\mathcal F$ is constant. Take such a part. If $\mathcal F$ is not an axis vertex, it is finite by Proposition 4.5.5. If $\mathcal F = \{\omega e_b\}$, its steps with $\omega_2 > 0$ are finitely many by Proposition 4.5.7, and the rest of it is in the orthant regime and is finite by Proposition 4.5.8. So the run is finite.

By Lemma 4.5.2 (1), a toric branch is a run of the toric model. So it reaches $\omega = 0$, or a set $U_n$ with no allowed step, that is, a center over which no chart origin has multiplicity $2p$. In the first case Theorem 4.4.13 bounds the rest of the sequence, for each choice of points. The last claim follows from Lemma 4.5.2 (2). $\square$

**Corollary 4.5.10 (a lexicographic invariant on toric branches).** For a state $U$ of the toric model with $\omega(U) > 0$, let $\ell(U)$ be the supremum of the lengths of the runs from $U$ on which $\omega$ stays equal to $\omega(U)$, over all choices of centers and charts. Then $\ell(U) < \infty$. At each step $U \to U'$ of a run with $\omega(U) > 0$, either $\omega(U') < \omega(U)$, or $\omega(U') = \omega(U)$ and $\ell(U') < \ell(U)$. So the pair $(\omega, \ell)$ decreases strictly in the lexicographic order along each toric branch until $\omega = 0$. Hence Conjecture 4.4.6 holds for the toric branches, for each choice among tied centers. In particular it holds for the sequences through chart origins of each germ with $a_p = a_{2p} = 0$ and $E = \{0, 1, 2\}$.

Node: SG000000BF

*Proof.* A state has finitely many successors, since there are finitely many centers and charts. The runs from $U$ on which $\omega$ is constant form a rooted tree in which each vertex has finitely many children. By Theorem 4.5.9 this tree has no infinite branch, so it is finite by the lemma of König, and $\ell(U)$ is its height. If a step $U \to U'$ keeps $\omega$, each run from $U'$ on which $\omega$ is constant gives a run from $U$ that is one step longer. So $\ell(U) \ge \ell(U') + 1$. $\square$

The function $\ell$ is computable, but it is defined by the search itself. The useful content is the list of the quantities in the proofs, stage by stage: the number of points of $\Lambda$ in the bottom face $\mathcal F$, then $\omega_2$, then $s(g) - m_s$ and $m_s + m_t$, then the larger coordinate $H$ of the corner, then $\mu_a$ or $c_a$, and $\delta$ for the divisorial steps and for the doubly stuck phase. Together they give an explicit lexicographic invariant for each stage.

### The hidden quantity of Section 4.4

**Proposition 4.5.11 (the hidden quantity).** Let $p = 3$, $E = \{0, 1, 2\}$ and $f_{e,g}$ as in Proposition 4.4.14, with $e \ge 3$.

1. The normalised points are $A = (0, 0, \frac{22}{15})$ from $a_3$ and $F^2$, $(\frac75, \frac{3e-5}{15}, 0)$ from $a_5$, and $(\frac76, \frac{g-2}6, \frac45)$ from $a_6$. So $\mathcal F = \{A\}$, with $b = 2$, and the projection sends the last two points to
$$\Big(\frac{21}{22}, \frac{3e - 5}{22}\Big) \qquad \text{and} \qquad \Big(\frac74, \frac{g - 2}4\Big).$$
2. If $11g \ge 6e + 12$, the second point lies in the orthant of the first. Then $Q$ is the orthant at $c = (\frac{21}{22}, \frac{3e-5}{22})$, $\beta = \frac53$, and
$$h - 1 = \frac{3(e - 2)}{22}.$$
3. Along the period of Proposition 4.4.14, each point blowup lowers $h$ by exactly $\frac1{22}$, and the divisorial steps do not change $h$. So $h$ drops by $\frac3{22}$ in each period, as $e \mapsto e - 1$ needs. The gap $\frac{e-2}5$ of Section 4.4 is $\omega(h - 1)$, and the run ends when $h$ reaches $1$, that is, at $e = 2$.

Node: SG000000BH

*Proof.* (1) By Proposition 4.4.14 (1), $\mu = (0, \frac13, \frac15)$ and $\omega = \frac{22}{15}$. The monomial $2x_1x_2^5$ of $a_3$ gives $u = (0, \frac13, \frac53)$, and the monomial $x_1^2x_2^{10}$ of $a_6$ gives the same point. So $v = u - \mu = (0, 0, \frac{22}{15}) = \omega e_2$. The monomial $x_0^7x_1^ex_2$ of $a_5$ gives $u = (\frac75, \frac e5, \frac15)$ and $v = (\frac75, \frac{3e-5}{15}, 0)$. The monomial $x_0^7x_1^gx_2^6$ of $a_6$ gives $u = (\frac76, \frac g6, 1)$ and $v = (\frac76, \frac{g-2}6, \frac45)$. The second point has $|v| = \frac{3e + 16}{15} > \frac{22}{15}$, since $e > 2$, and the third has $|v| = \frac{5g + 49}{30} > \frac{22}{15}$. So $\mathcal F = \{A\}$. The second point has $w = \frac{22}{15}$, and the third has $w = \frac{22}{15} - \frac45 = \frac23$. Divide $(v_0, v_1)$ by $w$.

(2) The condition $\frac{3e-5}{22} \le \frac{g-2}4$ is $11g \ge 6e + 12$, and $\frac{21}{22} < \frac74$. So $Q = c + \mathbb R^2_{\ge 0}$. Then $h = \frac{21}{22} + \frac{3e - 5}{22} = \frac{3e + 16}{22}$, and $\beta = \mu_2 + \omega = \frac15 + \frac{22}{15} = \frac53$.

(3) The point blowups of the period are in the chart of $x_1$, so they are moves $P_c$ with $a = 0$ and $c = 1$. By Lemma 4.5.6 (1), $P_c$ sends $c_1$ to $c_0 + c_1 - 1 = c_1 - \frac1{22}$, and $c_0 = \frac{21}{22}$ does not change, since the period has no step in the chart of $x_0$. By Lemma 4.5.6 (1), divisorial steps do not change $q$. The period has three point blowups, so $h$ drops by $\frac3{22}$, and $\frac{3(e-3)}{22}$ is the value for $e - 1$. The point of $a_6$ goes from $t$ to $t + \frac34$ at each move, so from $\frac{g-2}4$ to $\frac{g+7}4$ in a period, as $g \mapsto g + 9$ needs. Finally $\omega(h - 1) = \frac{22}{15} \cdot \frac{3(e-2)}{22} = \frac{e - 2}5$. At $e = 2$ we have $h = 1$, so by Lemma 4.5.6 (2) the run with $\mathcal F$ constant ends there. $\square$

The proposition explains part (3) of Proposition 4.4.14 in the terms of this section. Since $\beta \ge 1$, the move $C_1$, which blows up the curve $V(z, x_1, x_2)$, is a candidate if and only if $c_1 \ge 1$, that is, $e \ge 9$. So for $3 \le e \le 8$ no curve is a candidate, and the rule blows up the point. The move $C_0$ is never a candidate, since $c_0 = \frac{21}{22} < 1$.

**Example 4.5.12 (germ 57).** Germ $57$ is $f_{9,5}$ (Example 4.4.15). Here $11g = 55 < 6e + 12 = 66$, so the condition of Proposition 4.5.11 (2) fails. The two projected points are $(\frac{21}{22}, 1)$ and $(\frac74, \frac34)$. So $m_s = \frac{21}{22}$, $m_t = \frac34$, $h = \frac{43}{22}$, and
$$\omega_2 = \frac{43}{22} - \frac{21}{22} - \frac34 = \frac14.$$
So the branch starts in the stage $\omega_2 > 0$ of Proposition 4.5.7. Since $m_t = \frac34 < 1$, the move $C_1$ is not a candidate. This agrees with Example 4.4.15, where the value of the curve $V(z, x_1, x_2)$ is $\omega_{\{1,2\}} = \frac{g-2}6 + \frac45 = \frac{13}{10} < \frac{22}{15}$. The first point blowup in the chart of $x_1$ sends the two points to $(\frac{21}{22}, \frac{21}{22})$ and $(\frac74, \frac32)$. Then $m_s = m_t = \frac{21}{22}$ and $h = \frac{21}{11}$, so $\omega_2 = 0$, and the branch is in the orthant regime after one step. After the first period the points are $(\frac{21}{22}, \frac{19}{22})$ and $(\frac74, 3)$, which are the points of $f_{8,14}$, and $h = \frac{20}{11}$. Along the next period $h$ takes the values $\frac{20}{11}, \frac{39}{22}, \frac{19}{11}$ at the point blowups. In the toric model, with all choices of centers and charts, the computer finds $\ell(f_{9,5}) = 41$ and $\ell(f_{8,14}) = 30 = 5(8 - 2)$ [C]. The value $41$ is the branch of Example 4.4.15 that keeps $\omega = \frac{22}{15}$ up to depth $41$.

**Example 4.5.13 (a germ with $a_p = a_{2p} = 0$).** Let $p = 3$, $E = \{0, 1, 2\}$ and
$$f = z^6 + x_0^4 z^5 + x_2^2 z^4 + x_0^5x_1^5x_2^5 z.$$
So $a_1 = x_0^4$, $a_2 = x_2^2$, $a_5 = x_0^5x_1^5x_2^5$, and $a_3 = a_6 = 0$. By Lemma 4.5.2 (2), each sequence of the rule through chart origins is a toric branch. The germ is reduced. Indeed $f = zg$ with $g = z^5 + x_0^4z^4 + x_2^2z^3 + x_0^5x_1^5x_2^5$, and $z$ does not divide $g$. Modulo $3$, $\partial g / \partial z = z^3(2z + x_0^4)$. A common factor of $g$ and $\partial g / \partial z$ would divide $2z + x_0^4$, but $g(x_0^4) = 2x_0^{20} + x_0^{12}x_2^2 + x_0^5x_1^5x_2^5 \ne 0$ in characteristic $3$. So $g$ has no square factor.

The points are $U = \{(4, 0, 0), (0, 0, 1), (1, 1, 1)\}$, and $(1, 1, 1) \ge (0, 0, 1)$, so the last point does not matter. So $\mu = (0, 0, 0)$, $\delta = 1$ and $\omega = 1$. The bottom face is $\mathcal F = \{e_2\}$, so $b = 2$, $a = 0$ and $c = 1$. The point $(4, 0, 0)$ has $w = 1$ and $q = (4, 0)$. So $Q$ is the orthant at $c = (4, 0)$, $\omega_2 = 0$, $h = 4$ and $\beta = \mu_2 + \omega = 1$.

The curve $\{0, 2\}$ has $\delta_{\{0,2\}} = \min(4, 1) = 1$ and $\omega_{\{0,2\}} = 1 = \omega$, and the other two curves have $\delta_S = 0$. So the rule blows up the curve $V(z, x_0, x_2)$. This is the move $C_0$, which is a candidate since $c_0 = 4 \ge 1$ and $\mu_0 + \beta = 1$. In the chart of $x_2$ the point $(0, 0, 1)$ goes to $(0, 0, 0)$, so the origin has multiplicity less than $6$. In the chart of $x_0$ the coefficient $a_1$ becomes $x_0^3$, and $a_2$ and $a_5$ do not change. At the other points over the center in this chart, $x'_2 = \lambda \ne 0$, the coefficient $a'_2 = x_2'^2$ is a unit, so the multiplicity is less than $6$. So the sequence is unique, and it is
$$a_1 = x_0^4 \to x_0^3 \to x_0^2 \to x_0, \qquad c = (4, 0) \to (3, 0) \to (2, 0) \to (1, 0),$$
with $\omega = 1$ and $h = 4, 3, 2, 1$ at the four points. At the last point $h = 1$, so the face $\mathcal F$ grows to the segment from $e_0$ to $e_2$, as in Lemma 4.5.6 (2). Now $\mathcal F$ is not an axis vertex, and in the notation of Proposition 4.5.5 we have $j = 1$ and $\kappa = 0$ at both points. The curve $\{0, 2\}$ is a candidate, since $\delta_{\{0,2\}} = 1$, so the rule blows it up again. In the chart of $x_0$, $a_1 = x_0$ becomes the unit $1$, and in the chart of $x_2$, $a_2$ becomes a unit. So no point of multiplicity $6$ lies over this center, and the sequence ends. The values of $\ell$ at the four points are $3, 2, 1, 0$.

### No lexicographic pair for the rule

**Proposition 4.5.14 (no lexicographic pair that starts with $\omega$).** For each odd prime $p$ there is no function $s$ of the point, with values in a totally ordered set, such that $(\omega, s)$ decreases strictly in the lexicographic order at each step of Rule 61.9' from a point of multiplicity $2p$ to a point of multiplicity $2p$ over the chosen center.

Node: SG000000BG

*Proof.* By Theorem 4.4.8 there is a point $\xi$ at which the rule blows up the point, for each choice of base coordinates and each tie-break, and a point $\xi'$ of multiplicity $2p$ over it with $\omega(\xi) = 1$ and $\omega(\xi') = \frac{p+1}p > 1$. At this step $(\omega, s)$ goes up in the lexicographic order, for each value of $s(\xi)$ and $s(\xi')$. $\square$

Theorem 4.4.7 gives a second family, with $\omega$ from $\frac{p+3}{2(p+1)}$ to $\frac{p+2}{2p}$. In both families the new point is not the origin of its chart, and $z$ must be prepared again there. This agrees with Theorem 4.5.9, where $\omega$ never goes up. So a proof of Conjecture 4.4.6 for $\omega > 0$ must bound the rises of $\omega$, or use an invariant in which $\omega$ is not the first entry. On the toric branches the pair of Corollary 4.5.10 works.

The second limit is that the maps of the toric model describe only chart origins. At a point with $x'_k = \lambda_k \ne 0$, the substitution $x_k = x_j(\lambda_k + y_k)$ mixes the monomials, $E$ loses the component $V(x_k)$, and $\omega = \delta - \sum_{k \in E} \mu_k$ has fewer terms.

**Example 4.5.15 (a step that keeps $\omega$ and is not toric).** The search of research note 72 on germ $57$ has the following step at depth $28$ of a cut branch [C]. At the point, $E = \{0, 1, 2\}$, $\delta = \frac75$ and $\mu = (0, \frac23, \frac35)$, so $\omega = \frac75 - \frac23 - \frac35 = \frac2{15}$. The rule blows up the point. In the chart of $x_0$, at the two points with $(x'_1, x'_2) = (0, 1)$ and $(0, 2)$, the new values are $E = \{0, 1\}$, $\delta = \frac65$ and $\mu = (\frac25, \frac23, 0)$. So $\omega = \frac65 - \frac25 - \frac23 = \frac2{15}$, and the step keeps $\omega$. The new point is not a chart origin, and the boundary has lost $V(x_2)$. So the polyhedron does not move by the maps of Definition 4.5.1, and the quantities $\mathcal F$, $\omega_2$ and $H$ are not defined for this step.

### What the computer shows

The results of this subsection are exact computations with rational numbers. They are evidence, not proofs, and they carry the tag [C] of the research notes. They come from research note 81, and they use the cut nodes of research note 72 (see Section 4.4).

*The model and the family.* In the toric model, the longest runs with $\omega = \frac{22}{15}$ from $f_{e,g}$ have the lengths of research note 72: $41$ for $(e, g) = (9, 5)$, $30$ for $(8, 200)$, $0$ for $(9, 200)$, $15$ for $(12, 200)$, $5$ for $(3, 10)$, $20$ for $(20, 200)$ and $15$ for $(40, 200)$.

*The cut nodes.* Of the $81$ cut nodes of Section 4.4 with $\omega > 0$, $53$ have $E = \{0, 1, 2\}$. For each of the $53$, the toric model built from the stored germ gives the recorded values of $\omega$ and $\delta$. The other $28$ are outside the model. Of the $53$, $17$ have a face $\mathcal F$ that is not an axis vertex, and $36$ have $\mathcal F = \{\omega e_b\}$ with $\omega_2 = 0$, with $\beta$ between $\frac13$ and $\frac53$. The computer followed all centers and charts from the $53$ nodes. This gave $2084$ nodes and $1027$ steps that keep $\omega$. All branches end, and the longest run with $\omega$ constant has $8$ steps. No step raises $\omega$, each step that keeps $\omega$ has $\mathcal F \subseteq \mathcal F'$, and $\omega_2$ never goes up. In the orthant regime, $h$ drops at each of the $105$ main steps with $\beta \ge 1$, and the $675$ steps with $\beta < 1$ all lie on finite branches.

*The histories.* The stored histories of the $81$ cut nodes have $2430$ steps. Of these, $2384$ are at chart origins and $46$ are at points with some $\lambda_k \ne 0$. No step raises $\omega$, and $20$ of the $46$ steps that are not at chart origins keep $\omega$.

*The open subtree of Section 4.4.* The subtree of germ $57$ with $\omega = \frac8{15}$ has finished: $446$ nodes, $268$ resolved leaves, $11$ revisits, no node at the depth limit, and least value of $\omega$ equal to $0$, in $604.6$ s. So all $81$ subtrees of research note 72 are finite.

*The orthant system.* The computer enumerated all states of the system of Proposition 4.5.8 with $\mu_k \in \frac1M \mathbb Z \cap [0, 1)$, $c_k \in \frac1M \mathbb Z \cap [0, 4]$ and $\beta \in \frac1M \mathbb Z \cap (0, 3)$. For $M = 6$ there are $471014$ transitions, and for $M = 12$ there are $15120568$. There is no step outside a doubly stuck state that raises $H$, no doubly stuck state with a successor that is not doubly stuck, and no doubly stuck step where $\sigma$ does not drop. This agrees with Steps 1 and 2 of the proof. The enumeration uses one denominator $M$ for $\mu$ and $c$, which is a simplification. There is no cycle for $M = 6, 12, 20$.

*Random polyhedra.* A search on $300$ random sets $U$ (seed $1$) found no cycle. The longest run with $\omega$ constant had $151$ steps.

### What is open

1. Conjecture 4.4.6 for $\omega > 0$ on general branches. No counterexample is known.
2. The steps of the rule that keep $\omega$ and are not toric. The histories of the $81$ cut nodes have $20$ such steps. All of them are point blowups, seen in the chart of $x_0$, at points that are not chart origins, and they are four distinct steps, recorded in several histories. Two records come from germ $57$ at depth $28$, at the points $\lambda = (\lambda_1, \lambda_2) = (0, 1)$ and $(0, 2)$ of Example 4.5.15, with $\omega = \frac2{15}$. Eighteen records come from germ $63$ at depth $23$, at the points $\lambda = (1, 0)$ and $(2, 0)$. There $\omega = \frac23$ before and after the step, $\delta$ goes from $2$ to $\frac{13}6$, $\mu$ goes from $(\frac13, \frac12, \frac12)$ to $(1, 0, \frac12)$, and $E$ goes from $\{0, 1, 2\}$ to $\{0, 2\}$. Is there a quantity that drops at these steps and on the toric runs?
3. An extension of Theorem 4.5.9 to the chart origins with $E \ne \{0, 1, 2\}$. There the free coordinates are not normalised, the maps are the same, and $\omega$ omits some $\mu_k$.
4. A bound on the rises of $\omega$ under the rule. For example, each rise could come with a drop of $\delta$, or of a flag that cannot come back infinitely often. The lexicographic plan needs this outside the toric model.
5. An explicit bound for $\ell$ in terms of $p$ and $\delta$. The proof gives one, through the size of $\Lambda$ and the bounds of Propositions 4.5.5, 4.5.7 and 4.5.8, but it is much larger than the values that the computer finds: $41$ on germ $57$, $8$ on the cut nodes and $151$ on random sets.

### Exercises

1. Prove the statement of Lemma 4.5.4 (1) on divisorial steps, and show that a divisorial step can be followed by another divisorial step at the same index.
2. Show that the number of points of $\frac1B \mathbb Z^3_{\ge 0}$ with $|v| = \omega$ is $\frac12(B\omega + 1)(B\omega + 2)$.
3. Let $\mathcal F = \{\omega e_b\}$. Show that each main step in the chart of $x_b$ lowers $\omega$, and that the curve $\{a, c\}$ is never a candidate.
4. Show that the proof of Lemma 4.5.2 (2) uses only $a_{2p} = 0$, and not $a_p = 0$.
5. In the system of Proposition 4.5.8, let $\beta = \frac12$, $\mu_a = \mu_c = \frac13$ and $c = (1, 1)$. Show that the state is doubly stuck, and that each run from it has exactly two point steps, where the second one gives $\delta < 1$.
6. For $f_{9,200}$, show that the corner is $c = (\frac{21}{22}, 1)$ and that the rule blows up the curve $V(z, x_1, x_2)$. Show that $\omega$ drops at each chart origin over it, so $\ell(f_{9,200}) = 0$.
7. In Example 4.5.13, replace $a_1 = x_0^4$ by $x_0^n$ with $n \ge 1$. Find $\ell$ at the first point as a function of $n$.
8. In the orthant regime with $\beta \ge 1$, show that the number of main steps is at most $L(h - 1)$. Compare this bound with the number of main steps in Example 4.5.13.
9. (Open.) Find a quantity that drops at the step of Example 4.5.15 and along each toric run on which $\omega$ is constant.

### Notes and references

The toric model, Theorem 4.5.9, Corollary 4.5.10, Proposition 4.5.11 and Proposition 4.5.14 are from research note 81, which answers the question of a secondary invariant of research note 72 for the toric branches. Note 81 has no referee report yet, and its last section asks for one, in particular for Proposition 4.5.8 and for the claim of Lemma 4.5.2 that the center depends only on the points. Rule 61.9' and the residual slope are from research note 61, Theorems 4.4.7 and 4.4.8 are from research notes 65 and 66, and Proposition 4.4.14 and the cut nodes are from research note 72.

The slopes are those of the characteristic polyhedron of Hironaka [Hir67], computed at a prepared coordinate. The moves of Definition 4.5.1 are the moves of the polyhedra game of Hironaka, which Spivakovsky solved [Spi83]. For $m = p$ the analogous invariant $\epsilon$ of Cossart and Piltant [CP19, Definition 2.25] is $p$ times the residual slope. Section 4.4 compares the rises of $\omega$ with the conditions of [CP19, Theorem 3.13] for the rises of $\epsilon$.

The nodes of this section are SG000000BE (Theorem 4.5.9, with Lemma 4.5.2), SG000000BF (Corollary 4.5.10), SG000000BH (Proposition 4.5.11) and SG000000BG (Proposition 4.5.14). None of them is in Lean.
