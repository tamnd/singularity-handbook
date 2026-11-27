---
title: The residual slope at multiplicity 2p
nodes: [SG0000009K, SG0000009M, SG0000009N, SG0000009P, SG0000009Q, SG0000009R, SG0000009S, SG0000009T]
sources: [Hir67, CP19, Hau10, HP19b]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The residual slope at multiplicity 2p

Chapter 3 controls a point of multiplicity $p$ of $z^p + F$ with the residual order $\rho$ of the log-Jacobian ideal. The order $\rho$ does not go up under the permissible blowups of that chapter (Sections 3.2 and 3.4). But $\rho$ often stays the same for many steps, and the runs where $\rho$ stays need more entries in the invariant (Sections 3.12 to 3.18). This section starts the same program for the first mixed multiplicity $m = 2p$, and here a second problem comes first. At $m = 2p$ the coefficients $a_1, \dots, a_{p-1}$ form a rigid layer (Section 4.1), so there is no Tschirnhausen step and no hypersurface of maximal contact. The equation is also not of the form $z^p + F$, so the log-Jacobian ideal of Chapter 3 is not available. To show that a resolution sequence makes progress while the multiplicity stays $2p$, we need an invariant that is intrinsic and that we can compute from the equation. The candidate of this section is the *residual slope* $\omega$: the slope of Hironaka's characteristic polyhedron [Hir67] minus the part that the boundary explains.

The results are of two kinds. The negative results show that $\omega$ can go up under the center of the natural rule (Theorems 4.4.7 and 4.4.8), and that a correction of $\omega$ by a constant times a natural flag does not repair this (Proposition 4.4.12). The positive result is the termination of the rule at the points with $\omega = 0$ (Theorem 4.4.13). A period-5 mechanism explains the long runs with $\omega > 0$ that the computer finds (Proposition 4.4.14). The termination for $\omega > 0$ is open (Conjecture 4.4.6).

*A warning on the letter.* The $\omega$ of this section is not the invariant $\omega$ of Cossart and Piltant of Section 3.6. That one is a differential invariant at multiplicity $p$, and Section 3.6 shows that it is $\rho$. The $\omega$ here is the slope $\delta$ minus the boundary slopes. For $m = p$ it is $\epsilon / p$, where $\epsilon$ is the invariant of [CP19, Definition 2.25]. We keep the letter because the research notes use it.

### Setting and the slopes

Throughout, $p$ is an odd prime, $k$ is a perfect field of characteristic $p$, $R = k[[x_0, x_1, x_2]]$, $m = 2p$, and
$$f = z^{2p} + a_1 z^{2p-1} + \dots + a_{2p}, \qquad a_i \in R, \quad \operatorname{ord} a_i \ge i.$$
So the origin $\xi$ is a point of multiplicity $2p$ of $V(f)$. We put $a_0 = 1$. A set $E \subseteq \{0, 1, 2\}$ gives the boundary: the components $V(x_k)$, $k \in E$, of a normal crossings divisor through $\xi$. The coordinates $x_t$ with $t \notin E$ are *free*. Base coordinates are *adapted to $E$* if each $V(x_k)$, $k \in E$, is a coordinate hyperplane. Then $x_k$ for $k \in E$ is fixed up to a unit, and a free coordinate can be replaced by any element that completes a regular system of parameters. An index $i$ is *rigid* if $p \nmid i$. For $c \in \mathfrak m_R$ we write $a_i^{(c)}$ for the coefficients of $f(z + c)$, as in Lemma 4.1.2.

A *weight* is a vector $w \in \{0, 1\}^3$. It gives the monomial valuation $v_w(\sum g_\alpha x^\alpha) = \min\{w \cdot \alpha : g_\alpha \ne 0\}$ and the initial form $\operatorname{in}_w g$, the sum of the terms where the minimum is reached. We use seven weights: $(1, 1, 1)$, which gives $\operatorname{ord}$; the unit vectors $e_k$, where $v_{e_k}$ is the order along $V(x_k)$; and $\mathbb 1_S$ for $|S| = 2$, where $v_{\mathbb 1_S}$ is the order along the curve $V(x_S)$. For the last two kinds, $v_w$ is the order along a prime $P$ with $R/P$ regular, so it is a valuation, and it depends only on $P$.

**Definition 4.4.1 (slopes and the residual slope).** For a coordinate $z + c$, $c \in \mathfrak m_R$, and a weight $w$, put
$$\delta_{z+c}(w) = \min_{1 \le i \le 2p} \frac{v_w(a_i^{(c)})}{i}, \qquad \delta(w) = \sup_{c \in \mathfrak m_R} \delta_{z+c}(w).$$
Write $\delta = \delta(\xi) = \delta(1, 1, 1)$ and $\mu_k = \delta(e_k)$. The *residual slope* is
$$\omega = \omega(\xi) = \delta - \sum_{k \in E} \mu_k.$$
For $S \subseteq \{0, 1, 2\}$ with $|S| = 2$, the value along the curve $V(x_S)$ is $\omega(\eta_S) = \delta(\mathbb 1_S) - \sum_{k \in E \cap S} \mu_k$. The vertex of $z$ for $w$ is *solvable* if $\operatorname{in}_{w,z,t} f = (Z + C)^{2p}$ for a nonzero form $C$ of weight $t = \delta_z(w)$, where $\operatorname{in}_{w,z,t} f = \sum_{v_w(a_i) = it} \operatorname{in}_w(a_i) Z^{2p-i}$. The coordinate $z$ is *prepared* if $\delta_z(1,1,1) = \delta$, and *simultaneously prepared* if $\delta_z(w) = \delta(w)$ for all seven weights.

Since $(Z + C)^{2p} = (Z^p + C^p)^2 = Z^{2p} + 2C^pZ^p + C^{2p}$ (Lemma 4.1.1), a solvable vertex has three properties: $t$ is an integer, since $C$ is a nonzero form of weight $t$; no rigid $a_i$ has $v_w(a_i) = it$; and $\operatorname{in}_w a_p = 2C^p$ and $\operatorname{in}_w a_{2p} = C^{2p}$. We use the negation of this many times: if $t$ is not an integer, or a rigid coefficient reaches the slope, or $\operatorname{in}_w a_p$ is not $2$ times a $p$-th power, then the vertex is not solvable.

The next facts are the theory of the characteristic polyhedron for this equation [Hir67]. Research note 61 proves them in this form, and research note 65 checked the proofs. We use them without proof.

**Remark 4.4.2 (facts from the theory of the polyhedron).** Let $w$ be one of the seven weights, and assume that $f$ is not a unit times $(z - \varphi)^{2p}$.

1. *Vertex criterion.* If the vertex of $z$ for $w$ is not solvable, then $\delta(w) = \delta_z(w)$. If it is solvable with the form $C$, then $\delta_{z + C}(w) > \delta_z(w)$. The supremum over all regular parameters $z'$ with $(x, z')$ a regular system of parameters gives the same $\delta(w)$ as the supremum over the translates $z + c$.
2. *Simultaneous preparation.* Finitely many solving translations give a simultaneously prepared coordinate.
3. *Invariance.* The numbers $\delta$, $\mu_k$ and $\omega$ do not depend on $z$, and they do not change under a change of base coordinates adapted to $E$.
4. *Preparation and centers.* Two prepared coordinates differ by $z \mapsto z + c$ with $\operatorname{ord} c \ge \delta$. The regime of Definition 4.4.4 below does not depend on the prepared coordinate. At a simultaneously prepared $z$, the subvariety $V(z, x_S)$ is permissible for the blowup of $V(f)$ if and only if $\delta(\mathbb 1_S) \ge 1$, where $\mathbb 1_S = e_k$ for $S = \{k\}$.
5. *Upper semicontinuity.* If $V(z, x_S)$ is permissible, then $\delta(\mathbb 1_S) \le \delta$ and $\omega(\eta_S) \le \omega(\xi)$.
6. *Points over a center.* Let $z$ be simultaneously prepared, and assume $\delta > 1$ or $\mu_k > 0$ for some $k \in E$. Let $V(z, x_S)$ be permissible and $j \in S$. In the chart of $x_j$ put $x_k = x_j x_k'$ for $k \in S \setminus \{j\}$ and $z = x_j z'$. Then the strict transform is $z'^{2p} + \sum a_i' z'^{2p-i}$ with $a_i' = a_i / x_j^i$, and each point of multiplicity $2p$ over $\xi$ in this chart lies on $z' = 0$.

The proofs are in research note 61 (Lemma 61.3, Theorem 61.4, Lemma 61.7, Propositions 61.6, 61.9 and 61.10) and in research note 51 (Lemmas 3.2 and 3.3).

**Remark 4.4.3 ($\omega \ge 0$, and the denominators).** Let $B = \operatorname{lcm}(1, \dots, 2p)$. Then $\omega \ge 0$, and $\delta$, each $\delta(w)$ and $\omega$ lie in $\frac1B \mathbb Z$.

*Proof.* Let $z$ be simultaneously prepared. For a monomial $x^\alpha$ of $a_i$ and $k \in E$ we have $\alpha_k \ge v_{e_k}(a_i) \ge i \mu_k$. So $|\alpha| / i \ge \sum_{k \in E} \alpha_k / i \ge \sum_{k \in E} \mu_k$. The minimum of $|\alpha| / i$ over all monomials of all $a_i$ is $\delta_z(1,1,1) = \delta$. So $\delta \ge \sum_{k \in E} \mu_k$. For the second claim, $\delta(w) = \delta_z(w) = \min_i v_w(a_i)/i$, and $v_w(a_i)$ is an integer, so $\delta(w) \in \frac1i \mathbb Z \subseteq \frac1B \mathbb Z$ for some $i \le 2p$. $\square$

### The two parts of the equation

Since $(z^p + F)^2 = z^{2p} + 2F z^p + F^2$, the equation splits into a square and the rest.

**Definition 4.4.4 (the q-part, the rigid part and the regimes).** Put $F = a_p / 2$ and $G = a_{2p} - F^2$, so that
$$f = (z^p + F)^2 + G + \sum_{p \nmid i} a_i z^{2p - i}.$$
The *q-part* is $\{a_p, a_{2p}\}$ and the *rigid part* is $\{a_i : p \nmid i\}$. At a prepared coordinate let $D = \min(\operatorname{ord} a_p / p, \operatorname{ord} a_{2p} / 2p)$ and $\sigma^* = \min_{p \nmid i} \operatorname{ord} a_i / i$, with $\sigma^* = \infty$ when the rigid part is $0$. The point is in the *regime* R1 if $\sigma^* > D$, in R2 if $\sigma^* = 1$, and in R3 if $1 < \sigma^* \le D$.

Since $\delta = \min(D, \sigma^*)$ at a prepared coordinate, $\delta = D < \sigma^*$ in R1. By Lemma 4.1.2 and Lemma 4.1.1, a translation changes the q-part as
$$F^{(c)} = F + c^p + \tfrac12 \sum_{0 < i < p} \tbinom{2p - i}{p - i} a_i c^{p - i},$$
because $\binom{2p}{p} \equiv 2 \pmod p$. If $a_1 = 0$, then $a_2^{(c)} = a_2$ for each $c$ (Theorem 4.1.3).

The rule below is Rule 61.9' of research note 61, with the tie-break of research note 65. A *coordinate center* is $V(z, x_S)$ with $S \ne \emptyset$; it is a surface, a curve or the point for $|S| = 1, 2, 3$. It is *$\omega$-constant* if it is the point, or if $\omega(\eta_S) = \omega(\xi)$, where $\omega(\eta_S) = \mu_k - \mu_k = 0$ for a surface $V(z, x_k)$ with $k \in E$ and $\omega(\eta_S) = \mu_t$ for a free $t$.

**Definition 4.4.5 (Rule 61.9').** At $\xi$, choose base coordinates adapted to $E$ and a simultaneously prepared $z$. Then:

1. *Divisorial step.* If $\mu_k \ge 1$ for some $k$, blow up $V(z, x_k)$, for the largest $\mu_k$ with $k \in E$ first, then for the smallest index.
2. *Monomial step.* Otherwise, if $\omega = 0$, blow up the permissible coordinate center of smallest codimension.
3. *Main step.* Otherwise, blow up the permissible $\omega$-constant coordinate center of largest dimension. Among several, take the one with the larger $\sum_{k \in E \cap S} \mu_k$, then the smaller $S$.

A *sequence of the rule* is a sequence of points $\xi_0, \xi_1, \dots$ where $\xi_{n+1}$ is a point of multiplicity $2p$ over the center that the rule chooses at $\xi_n$. The new boundary $E'$ at $\xi'$ consists of the exceptional divisor and the strict transforms of the components of $E$ through $\xi'$.

By Remark 4.4.2 (3) and (4), the rule does not depend on $z$. It depends on the choice of the free coordinates, because a center $V(z, x_S)$ with $S \not\subseteq E$ does, and in step 2 and step 3 it can depend on the tie-break.

**Conjecture 4.4.6 (termination of Rule 61.9').** In its *strong form*: for each germ $(f, E)$ as above, each choice of base coordinates adapted to $E$ at each step, each choice among tied centers, and each choice of points, every sequence of the rule is finite. The *weak form* fixes the tie-break of Definition 4.4.5 (3) and the convention for the free coordinates of the code of research note 61.

Node: SG0000009T

Theorem 4.4.13 proves the strong form for germs with $\omega(\xi_0) = 0$. Since it applies again at each point of a sequence where $\omega = 0$, the open case is a sequence with $\omega(\xi_n) > 0$ for every $n$. This is part (b) of Problem 10.2 of the research notes for $m = 2p$, and it is open. The evidence is in the subsection "What the computer shows" below.

### The residual slope goes up

In characteristic $0$ and for $m = p$, the invariants of this kind do not go up under the centers of a good rule. The first natural hope was the same for $\omega$ at $m = 2p$ (Conjecture 61.18 (a) of the research notes). It is false, for every odd $p$, and no choice is involved.

**Theorem 4.4.7 ($\omega$ goes up under the rule).** Let $E = \{0, 1, 2\}$ and
$$F = x_0 x_1^p x_2^{p-1}, \qquad f = (z^p + F)^2 + x_0 x_1^{2p} x_2^{p-1} z^{p-1} + x_0^2 x_1^p x_2^{4p}.$$
So $a_p = 2F$, $a_{p+1} = x_0 x_1^{2p} x_2^{p-1}$, $a_{2p} = F^2 + G$ with $G = x_0^2 x_1^p x_2^{4p}$, and the other $a_i$ are $0$.

1. $f$ is reduced, $\xi$ has multiplicity $2p$ and is in R1, $\delta = 2$, $\mu = (\frac1{p+1}, \frac12, \frac{p-1}{p+1})$, and $\omega(\xi) = \frac{p+3}{2(p+1)}$.
2. Rule 61.9' blows up the point $\xi$, for each choice of base coordinates and each tie-break.
3. Let $\lambda \in k^\times$ and let $\xi'$ be the point $x_1' = 0$, $x_2' = \lambda$, $z' = 0$ of the chart of $x_0$. Then $\xi'$ has multiplicity $2p$, it is in R1 with $\sigma^* = \frac{6p-5}{2p-1}$, $E' = \{0, 1\}$, and $\omega(\xi') = \frac{p+2}{2p}$.

So $\omega$ goes up by $\frac{p+2}{2p} - \frac{p+3}{2(p+1)} = \frac1{p(p+1)}$. For $p = 3, 5, 7$ the values are $\frac34 \to \frac56$, $\frac23 \to \frac7{10}$ and $\frac58 \to \frac9{14}$.

Node: SG0000009K

*Proof.* (1) The terms $z^{2p}$, $a_p z^p$ and $a_{2p}$ have derivative $0$ in $z$, so $\partial f / \partial z = (p - 1) a_{p+1} z^{p-2} = -a_{p+1} z^{p-2} \ne 0$. A repeated factor of $f$ divides $\partial f / \partial z$, so it is $z$ or some $x_k$ up to a unit. It is not $z$, since $f(0) = F^2 + G \ne 0$, and it is not $x_k$, since $f$ is monic in $z$. So $f$ is reduced. The orders of $a_p$, $a_{p+1}$, $a_{2p}$ are $2p$, $3p$, $4p$, so $\xi$ has multiplicity $2p$.

The slopes $v_w(a_i)/i$ of $a_p$, $a_{p+1}$ and $a_{2p}$ are as follows, where for $a_{2p}$ we take the smaller of the values of $F^2$ and $G$, which are different monomials.

| $w$ | $a_p$ | $a_{p+1}$ | $a_{2p}$ | minimum |
|---|---|---|---|---|
| $(1,1,1)$ | $2$ | $\frac{3p}{p+1}$ | $2$ | $2$ |
| $e_0$ | $\frac1p$ | $\frac1{p+1}$ | $\frac1p$ | $\frac1{p+1}$ |
| $e_1$ | $1$ | $\frac{2p}{p+1}$ | $\frac12$ | $\frac12$ |
| $e_2$ | $\frac{p-1}p$ | $\frac{p-1}{p+1}$ | $\frac{p-1}p$ | $\frac{p-1}{p+1}$ |
| $\mathbb 1_{01}$ | $\frac{p+1}p$ | $\frac{2p+1}{p+1}$ | $\frac{p+2}{2p}$ | $\frac{p+2}{2p}$ |
| $\mathbb 1_{02}$ | $1$ | $\frac p{p+1}$ | $1$ | $\frac p{p+1}$ |
| $\mathbb 1_{12}$ | $\frac{2p-1}p$ | $\frac{3p-1}{p+1}$ | $\frac{2p-1}p$ | $\frac{2p-1}p$ |

In the last row, $(3p-1)p - (2p-1)(p+1) = (p-1)^2 > 0$. Only the first minimum is an integer, and there $\operatorname{in}(a_p) = 2X_0X_1^pX_2^{p-1}$ is not $2C^p$. So no vertex is solvable, $z$ is simultaneously prepared, and the minima are the values $\delta(w)$ by Remark 4.4.2 (1). This gives $\delta$ and $\mu$, and
$$\omega(\xi) = 2 - \tfrac1{p+1} - \tfrac12 - \tfrac{p-1}{p+1} = \tfrac32 - \tfrac p{p+1} = \tfrac{p+3}{2(p+1)}.$$
The only rigid coefficient is $a_{p+1}$, so $\sigma^* = \frac{3p}{p+1} > 2 = D$, and $\xi$ is in R1.

(2) Since $E = \{0, 1, 2\}$, base coordinates adapted to $E$ are $u_kx_k$ with units $u_k$, so the coordinate centers do not depend on any choice. All $\mu_k$ are less than $1$, so there is no divisorial step, and $\omega \ne 0$, so there is no monomial step. No surface $V(z, x_k)$ is permissible, since $\mu_k < 1$. The curves $V(z, x_0, x_1)$ and $V(z, x_0, x_2)$ are not permissible, since $\frac{p+2}{2p} < 1$ and $\frac p{p+1} < 1$. The curve $V(z, x_1, x_2)$ is permissible, but
$$\omega(\xi) - \omega(\eta_{12}) = \Bigl(2 - \tfrac1{p+1}\Bigr) - \tfrac{2p-1}{p} = \tfrac1p - \tfrac1{p+1} > 0.$$
So the main step blows up the point, and there is one candidate only.

(3) In the chart of $x_0$ put $x_1 = x_0 x_1'$, $x_2 = x_0 u$ with $u = \lambda + y$, and $z = x_0 z'$. Then $a_i' = a_i / x_0^i$ gives
$$F_1 = x_0^p x_1'^p u^{p-1}, \qquad a_{p+1}' = x_0^{2p-1} x_1'^{2p} u^{p-1}, \qquad G' = x_0^{3p+2} x_1'^p u^{4p},$$
with $a_p' = 2F_1$ and $a_{2p}' = F_1^2 + G'$. The exceptional divisor $V(x_0)$ and the strict transform $V(x_1')$ of $V(x_1)$ pass through $\xi'$, and the strict transform $V(u)$ of $V(x_2)$ does not, since $\lambda \ne 0$. So $E' = \{0, 1\}$. The vertex of $z'$ for $(1,1,1)$ is solvable: $a_p'$ and $a_{2p}'$ have slope $2$, the rigid $a_{p+1}'$ has order $4p - 1 > 2(p+1)$, and $\operatorname{in}(F_1) = \lambda^{p-1} X_0^p X_1'^p$ is a $p$-th power, since $k$ is perfect. Put $\gamma = -\lambda^{(p-1)/p} x_0 x_1'$ and $z' = Z + \gamma$. Then $z'^p + F_1 = Z^p + H$ with
$$H = x_0^p x_1'^p \bigl(u^{p-1} - \lambda^{p-1}\bigr), \qquad \operatorname{in}(H) = -\lambda^{p-2} X_0^p X_1'^p Y,$$
of order $2p + 1$, since $u^{p-1} - \lambda^{p-1} = (p-1)\lambda^{p-2} y + \dots$. Thus
$$f' = (Z^p + H)^2 + a_{p+1}' \sum_{j=0}^{p-1} \tbinom{p-1}{j} \gamma^j Z^{p-1-j} + G'.$$
The coefficients are $b_p = 2H$, the rigid $b_{p+1+j} = \binom{p-1}{j} \gamma^j a_{p+1}'$ for $0 \le j \le p - 2$, and $b_{2p} = H^2 + \gamma^{p-1} a_{p+1}' + G'$. Here $\binom{p-1}{j} \equiv (-1)^j \not\equiv 0$, and $\gamma$ has order $2$, so $\operatorname{ord} b_{p+1+j} = 4p - 1 + 2j$. The term $\gamma^{p-1} a_{p+1}'$ has order $6p - 3 > 4p + 2$, and $H^2$ and $G'$ have order $4p + 2$ with the different initial monomials $\lambda^{2p-4} X_0^{2p} X_1'^{2p} Y^2$ and $\lambda^{4p} X_0^{3p+2} X_1'^p$. So $\operatorname{ord} b_{2p} = 4p + 2$. Each order is at least the index, so $\xi'$ has multiplicity $2p$.

For $(1,1,1)$, $b_p$ and $b_{2p}$ have slope $\frac{2p+1}p$. The rigid slopes are $\frac{4p-1+2j}{p+1+j} = 2 + \frac{2p-3}{p+1+j}$. They decrease in $j$, so
$$\sigma^* = \frac{6p-5}{2p-1} > \frac{2p+1}{p}, \quad\text{since}\quad (6p-5)p - (2p+1)(2p-1) = 2p^2 - 5p + 1 > 0.$$
So $\delta_Z = \frac{2p+1}p$. It is not an integer, so $\delta(\xi') = \frac{2p+1}p$, and $\xi'$ is in R1. For $e_0$, the terms $2H$ and $H^2$ give $1$, the term $G'$ gives $\frac{3p+2}{2p}$, the term $\gamma^{p-1} a_{p+1}'$ gives $\frac{3p-2}{2p}$, and the rigid ones give $\frac{2p-1+j}{p+1+j} > 1$. So $\delta_Z(e_0) = 1$. This vertex is not solvable: its p-part is $2x_0^p x_1'^p (u^{p-1} - \lambda^{p-1})$, and $x_1'^p(u^{p-1} - \lambda^{p-1})$ has the monomial $x_1'^p y$, so it is not a $p$-th power in $k[[x_1', y]]$. Hence $\mu_0' = 1$. For $e_1$, the term $G'$ gives $\frac12$, and all other terms give at least $1$. So $\mu_1' = \frac12$, which is not an integer. Therefore $\omega(\xi') = \frac{2p+1}p - 1 - \frac12 = \frac{p+2}{2p}$. $\square$

Research note 65 has $4p - 1 + j$ for the orders of the rigid $b_{p+1+j}$, and so the value $\frac{5p-3}{2p-1}$ for $\sigma^*$ ($\frac{12}5$ for $p = 3$). The correct value is $\frac{6p-5}{2p-1}$ ($\frac{13}5$ for $p = 3$), because $\gamma$ has order $2$. The regime and the conclusion are the same. Research notes 66 and 72 found and checked the fix, and note 72 recomputed the theorem exactly for $p = 3, 5, 7$.

The mechanism is the classical one [Hau10, Sections D, F and G]: after the blowup, the leading part of $F$ becomes a $p$-th power, the translation that removes it raises the order of $F$, and the new initial form is linear in a new free variable. The next family gives a larger jump with the same mechanism.

**Theorem 4.4.8 (a jump of $\frac1p$).** Let $E = \{0, 2\}$ and
$$F = x_0 x_1^p x_2^{p-1}, \qquad f = (z^p + F)^2 + x_0^{2p} x_1 x_2^2 z^{2p-2} + x_0^2 x_1^{p+1} x_2^{4p+2}.$$
So $a_2 = x_0^{2p} x_1 x_2^2$, $a_p = 2F$, $a_{2p} = F^2 + G$ with $G = x_0^2 x_1^{p+1} x_2^{4p+2}$, and the other $a_i$ are $0$.

1. $f$ is reduced, $\xi$ has multiplicity $2p$ and is in R1, $\delta = 2$, $\mu = (\frac1p, \frac12, \frac{p-1}p)$, and $\omega(\xi) = 1$.
2. Rule 61.9' blows up the point $\xi$, for each choice of base coordinates adapted to $E$ and each tie-break.
3. Let $\lambda \in k^\times$ and let $\xi'$ be the point $x_1' = 0$, $x_2' = \lambda$, $z' = 0$ of the chart of $x_0$. Then $\xi'$ has multiplicity $2p$, it is in R1, $E' = \{0\}$, and $\omega(\xi') = \frac{p+1}p$.

Node: SG0000009M

*Proof.* (1) As in Theorem 4.4.7, $\partial f / \partial z = -2 a_2 z^{2p-3} \ne 0$, and $f$ is reduced. The orders of $a_2$, $a_p$, $a_{2p}$ are $2p + 3$, $2p$, $4p$, so $\xi$ has multiplicity $2p$. The slopes are:

| $w$ | $a_2$ | $a_p$ | $a_{2p}$ | minimum |
|---|---|---|---|---|
| $(1,1,1)$ | $\frac{2p+3}2$ | $2$ | $2$ | $2$ |
| $e_0$ | $p$ | $\frac1p$ | $\frac1p$ | $\frac1p$ |
| $e_1$ | $\frac12$ | $1$ | $\frac{p+1}{2p}$ | $\frac12$ |
| $e_2$ | $1$ | $\frac{p-1}p$ | $\frac{p-1}p$ | $\frac{p-1}p$ |
| $\mathbb 1_{01}$ | $\frac{2p+1}2$ | $\frac{p+1}p$ | $\frac{p+3}{2p}$ | $\frac{p+3}{2p}$ |
| $\mathbb 1_{02}$ | $p+1$ | $1$ | $1$ | $1$ |
| $\mathbb 1_{12}$ | $\frac32$ | $\frac{2p-1}p$ | $\frac{2p-1}p$ | $\frac32$ |

For $(1,1,1)$ and $\mathbb 1_{02}$ the minimum is an integer reached by $a_p$, and $\operatorname{in}_w(a_p)$ is $2x_0x_1^px_2^{p-1}$, which is not $2C^p$ because of the exponent $1$ of $x_0$. For $\mathbb 1_{01}$ the minimum is an integer only for $p = 3$. Then $t = 1$, the part of $a_3$ of weight $3$ is $0$, so $C = 0$, but $G$ gives a nonzero part of $a_6$ of weight $6$. The other minima are not integers. So $z$ is simultaneously prepared, $\delta = 2$, and $\omega = 2 - \frac1p - \frac{p-1}p = 1$. The rigid slope is $\frac{2p+3}{2} > 2$, so $\xi$ is in R1.

(2) The coordinates $x_0, x_2$ are fixed up to units, and a free coordinate is $x_1' = v x_1 + h(x_0, x_2)$ with a unit $v$. We use two facts. First, $a_2$ does not depend on $z$, since $a_1 = 0$ (Theorem 4.1.3). So $\delta(\mathbb 1_S) \le \frac12 v_{\mathbb 1_S}(a_2)$ for each $S$ and in each base coordinates. Second, $f(z + c) = (z^p + c^p + F)^2 + a_2 (z + c)^{2p-2} + G$, so with $K = \binom{2p-2}{p-2} c^{p-2}$,
$$F^{(c)} = c^p + F + \tfrac12 a_2 K, \qquad G^{(c)} = G + a_2\bigl(c^{2p-2} - (c^p + F)K\bigr) - \tfrac14 a_2^2 K^2.$$

- Divisorial step. We have $\mu_0, \mu_2 < 1$. For the free $V(x_1')$, the order of $a_2$ along $V(x_1')$ is the order of $x_1$, which is at most $1$, so $\mu_1 \le \frac12$. There is no divisorial step.
- Monomial step. It needs $\omega = 0$.
- Surfaces. None is permissible, by the values above.
- The curve $V(x_0, x_2)$. It does not depend on $x_1'$, and $\omega(\eta) = 1 - \mu_0 - \mu_2 = 0 < 1$.
- The curve $V(x_1', x_2)$. The order of $a_2$ along it is at most $3$, since $x_0$ is a unit at its generic point and $x_1, x_2$ have order at most $1$. So $\delta(\mathbb 1_S) \le \frac32$ and $\omega(\eta) \le \frac32 - \frac{p-1}p = \frac{p+2}{2p} < 1$.
- The curve $C = V(x_0, x_1')$. Let $c \in \mathfrak m_R$ and $d = \delta_{z+c}(\mathbb 1_C)$. If $c \notin (x_0, x_1')$, then $F^{(c)} \notin (x_0, x_1')$, because $F$ and $a_2$ lie in $(x_0)$, so $d = 0$. Otherwise each term of $G^{(c)} - G$ has order greater than $2p$ along $C$, since $a_2$ has order at least $2p$ there and each term also has a factor $a_2$, $c$ or $F$ (note $p - 2 \ge 1$). The order of $G$ along $C$ is $2 + (p+1)\operatorname{ord}_C x_1 \le p + 3 \le 2p$, so $\operatorname{ord}_C G^{(c)} = \operatorname{ord}_C G \le p + 3$. Since $\operatorname{ord}_C a_p^{(c)} \ge pd$ and $\operatorname{ord}_C a_{2p}^{(c)} \ge 2pd$, also $\operatorname{ord}_C G^{(c)} \ge 2pd$. So $d \le \frac{p+3}{2p}$, and $\omega(\eta) \le \frac{p+3}{2p} - \frac1p = \frac{p+1}{2p} < 1$.

No surface or curve is permissible and $\omega$-constant, so the rule blows up the point, and no tie-break enters.

(3) In the chart of $x_0$ put $x_1 = x_0 x_1'$, $x_2 = x_0 u$ with $u = \lambda + y$, and $z = x_0 z'$. Then
$$a_2' = x_0^{2p+1} x_1' u^2, \qquad F_1 = x_0^p x_1'^p u^{p-1}, \qquad G' = x_0^{3p+5} x_1'^{p+1} u^{4p+2},$$
and $E' = \{0\}$, since $x_1$ is free and the strict transform of $V(x_2)$ does not pass through $\xi'$. As in Theorem 4.4.7 the vertex for $(1,1,1)$ is solvable, and with $\gamma = -\lambda^{(p-1)/p} x_0 x_1'$ and $z' = Z + \gamma$ we get $z'^p + F_1 = Z^p + H$, with the same $H$ of order $2p + 1$, and
$$f' = (Z^p + H)^2 + a_2' \sum_{j=0}^{2p-2} \tbinom{2p-2}{j} \gamma^j Z^{2p-2-j} + G'.$$
The coefficient of $Z^{2p-2-j}$ from the middle sum is $\binom{2p-2}{j} \gamma^j a_2'$. By the theorem of Lucas, with $2p - 2 = 1 \cdot p + (p - 2)$, this binomial vanishes modulo $p$ exactly for $j = p - 1$, so $b_{p+1} = 0$. The other rigid $b_{2+j}$ have order $2p + 2 + 2j$ and slope $2 + \frac{2p-2}{2+j}$, which decreases in $j$. The least rigid slope is at $j = 2p - 3$, where $\binom{2p-2}{2p-3} = 2p - 2 \not\equiv 0$, and it is $\frac{6p-4}{2p-1}$. Next, $b_p = 2H + \binom{2p-2}{p-2} \gamma^{p-2} a_2'$, where the second term has order $4p - 2 > 2p + 1$, and $b_{2p} = H^2 + \gamma^{2p-2} a_2' + G'$, with terms of orders $4p + 2$, $6p - 2$ and $4p + 6$. Each order is at least the index, so $\xi'$ has multiplicity $2p$.

For $(1,1,1)$ the least slope is $\frac{2p+1}p$, from $b_p$ and $H^2$. Since $(6p-4)p - (2p+1)(2p-1) = 2p^2 - 4p + 1 > 0$, the rigid slopes are larger, and $\xi'$ is in R1. The value is not an integer, so $\delta(\xi') = \frac{2p+1}p$. For $e_0$, the terms $2H$ and $H^2$ give $1$, the second term of $b_p$ gives $\frac{3p-1}p$, the other terms of $b_{2p}$ give $\frac{4p-1}{2p}$ and $\frac{3p+5}{2p}$, and the rigid ones give $\frac{2p+1+j}{2+j} > 1$. The vertex is not solvable, as in Theorem 4.4.7. So $\mu_0' = 1$ and $\omega(\xi') = \frac{2p+1}p - 1 = \frac{p+1}p$. $\square$

Research note 72 checked the theorem by hand for $p = 3$ and with exact code for $p = 3, 5, 7$. The values at $\xi'$ are $\frac43$, $\frac65$, $\frac87$, and every other point of multiplicity $2p$ over $\xi$ has $\omega \le 1$. Here the jump comes with a jump of $\mu_0$ to $1$, so that $\omega(\xi') = \delta(\xi') - 1$.

### A flag does not repair the jumps

In both theorems the jump happens at a point where $F$ must be prepared again, and the new initial form of $F$ is not a $p$-th power in the free variables. For $m = p$, Cossart and Piltant repair the jumps of $\epsilon$ with a differential refinement that looks at exactly this property [CP19, Definition 2.68 and Theorem 3.13]. This suggests a flag.

**Definition 4.4.9 (the low flag).** Let $z$ be prepared at $\xi$, and put $q = \frac{\operatorname{ord} F}{p} - \sum_{k \in E} \mu_k$. Since $\operatorname{ord} a_p \ge p\delta$, we have $q \ge \omega$. In $\operatorname{gr} R = k[X_0, X_1, X_2]$ let $A_E = k[X_E, X_{\mathrm{free}}^p]$ be the subring generated by the $X_k$ with $k \in E$ and the $p$-th powers of the free $X_t$. The point is *low* if $q = \omega$ and $\operatorname{in}(F) \notin A_E$, that is, if $\partial \operatorname{in}(F) / \partial X_t \ne 0$ for some free $t$. Put $\lambda = 1$ if the point is low and $\lambda = 0$ otherwise, and $\lambda_{R1} = 1$ if the point is low and in R1, and $\lambda_{R1} = 0$ otherwise.

Note that $A_E = k[X_E, (\operatorname{gr}_1 R)^p]$, since $(\sum_s c_s X_s)^p = \sum_s c_s^p X_s^p$.

**Lemma 4.4.10 (the flag is intrinsic in R1).** At a point in R1 the flag $\lambda$ does not depend on the prepared coordinate $z$, nor on the base coordinates adapted to $E$.

Node: SG0000009N

*Proof.* Let $F_{p\delta}$ be the homogeneous part of degree $p\delta$ of $F$, with $F_{p\delta} = 0$ if $p\delta$ is not an integer. Since $\operatorname{ord} F \ge p\delta$, the point is low if and only if $F_{p\delta} \notin A_E$: if $\operatorname{ord} F > p\delta$ then $F_{p\delta} = 0 \in A_E$ and $q > \omega$, and if $\operatorname{ord} F = p\delta$ then $F_{p\delta} = \operatorname{in}(F)$ and $q = \omega$.

By Remark 4.4.2 (4), a second prepared coordinate is $z + c$ with $\operatorname{ord} c \ge \delta$. By the formula after Definition 4.4.4, $F^{(c)} = F + c^p + \frac12\sum_{0<i<p} \binom{2p-i}{p-i} a_i c^{p-i}$. In R1 each rigid $a_i$ has order at least $i\sigma^* > i\delta$, so each term of the sum has order greater than $i\delta + (p-i)\delta = p\delta$. Hence $F^{(c)}_{p\delta} = F_{p\delta} + c_\delta^p$, where $c_\delta$ is the part of degree $\delta$ of $c$ (or $0$). Since $c_\delta^p \in k[X^p] \subseteq A_E$ and $A_E$ is a ring, $F^{(c)}_{p\delta} \in A_E$ if and only if $F_{p\delta} \in A_E$. This also covers the case $q > \omega$.

A change of base coordinates adapted to $E$ does not change $F \in R$. On $\operatorname{gr}_1 R$ it sends $X_k$ to a nonzero multiple of $X_k$ for $k \in E$ and each free $X_t$ to a linear form. So it maps $A_E = k[X_E, (\operatorname{gr}_1R)^p]$ onto itself. The numbers $\delta$, $\mu_k$ and $\omega$ do not change by Remark 4.4.2 (3). $\square$

Outside R1 a rigid term of $F^{(c)}$ can have degree $p\delta$, and the flag can then depend on $z$. This is why we restrict the flag to R1. The candidate $V_6 = \omega - \frac1{2p}\lambda_{R1}$ absorbs the jump of Theorem 4.4.7: by the computations of research note 66, it goes from $\frac34$ to at most $\frac23$ for $p = 3$. But Theorem 4.4.8 already breaks it: the point $\xi$ there is not low, since $\operatorname{in}(F) = X_0X_1^pX_2^{p-1} \in k[X_0, X_2, X_1^p]$, and $\xi'$ is low, since its $F$ is $b_p/2$ of order $2p + 1$, so $q = \omega(\xi')$, and $\operatorname{in}(H)$ is linear in the free $Y$. So $V_6$ goes from $1$ to $\frac{2p+1}{2p}$. The next example shows that the flag can also switch off with $\omega$ constant.

**Example 4.4.11 (the flag is lost from R1 to R2).** Let $p = 3$, $E = \{0, 2\}$, and
$$a_2 = x_0^2 x_2, \quad a_3 = x_1^2 x_2 + x_0^4 x_1^2 x_2^3, \quad a_6 = x_1^4 x_2^2 + x_0^4 x_1^2 x_2^4 + 2 x_0^4 x_1^4 x_2^4 + x_0^8 x_1^4 x_2^6,$$
with the other $a_i = 0$. Then $F = a_3/2 = 2a_3$, $F^2 = a_3^2$, and $G = a_6 - a_3^2 = x_0^4 x_1^2 x_2^4$. Rule 61.9' blows up the point in every choice of base coordinates adapted to $E$, and at the origin $\xi'$ of the chart of $x_0$ the value of $\omega$ stays $\frac23$, while the regime goes from R1 to R2. So $V_6$ goes from $\frac12$ to $\frac23$.

Node: SG0000009P

*Proof.* For $(1,1,1)$ the slopes of $a_2$, $a_3$, $a_6$ are $\frac32$, $1$, $1$, and $\operatorname{in}(a_3) = X_1^2X_2$ is not $2C^3$, so $\delta = 1$. For $e_0$ the slope $0$ comes from $x_1^2x_2$ in $a_3$, which is not $2C^3$, so $\mu_0 = 0$. For $e_2$ the least slope is $\frac13$, from $a_3$ and $x_1^4x_2^2$, so $\mu_2 = \frac13$. Hence $\omega = \frac23$. The rigid slope is $\frac32 > 1 = D$, so $\xi$ is in R1. Also $q = 1 - \frac13 = \omega$, and $\operatorname{in}(F) = 2X_1^2X_2$ has degree $2$ in the free $X_1$. So $\xi$ is low, and $V_6(\xi) = \frac23 - \frac16 = \frac12$.

The coordinates $x_0, x_2$ are fixed up to units, and the free one is any $x_1' = vx_1 + h(x_0, x_2)$. Since $a_1 = 0$, the coefficient $a_2 = x_0^2x_2$ does not depend on $z$ (Theorem 4.1.3). No $\mu_k$ with $k \in E$ reaches $1$, and the free $V(x_1')$ has $\mu_1 \le \frac12 v_{e_1}(a_2) = 0$, since $x_0^2x_2 \notin (x_1')$. As $\omega \ne 0$, the rule takes the main step. No surface is permissible. The curve $V(z, x_0, x_2)$ does not depend on $x_1'$, and $\delta(\mathbb 1_{02}) = \frac13$ (from $a_3$ and $x_1^4x_2^2$, not an integer), so it is not permissible. The curve $V(z, x_1', x_2)$ is not permissible, since $a_2$ has order $1$ along $V(x_1', x_2)$, so $\delta(\mathbb 1_S) \le \frac12$. If the curve $V(z, x_0, x_1')$ were permissible, its value would be $\delta(\mathbb 1_S) - \mu_0 = \delta(\mathbb 1_S) \ge 1 \ne \frac23$. So the rule blows up the point.

At the origin of the chart of $x_0$,
$$a_2' = x_0 x_2', \qquad a_3' = x_1'^2 x_2' + x_0^6 x_1'^2 x_2'^3, \qquad G' = x_0^4 x_1'^2 x_2'^4,$$
with $a_6' = a_3'^2 + G'$ and $E' = \{0, 2\}$. All three coefficients have slope $1$ for $(1,1,1)$, and the rigid $a_2'$ reaches it, so the vertex is not solvable and $\delta' = 1$. As before $\mu_0' = 0$ (from $a_3'$) and $\mu_2' = \frac13$. So $\omega' = \frac23$, and $\sigma^* = 1$, so $\xi'$ is in R2 and $\lambda_{R1} = 0$. $\square$

Research note 72 found that the same transition happens for $p = 5$ in the computer runs. Together with Theorem 4.4.8, the example excludes all corrections of the form $\omega - c\lambda$.

**Proposition 4.4.12 (no flag correction is monotone).** Let $p = 3$ and $c \in \mathbb R$. Neither $\omega - c\lambda$ nor $\omega - c\lambda_{R1}$ is non-increasing under Rule 61.9'.

Node: SG0000009Q

*Proof.* For $\lambda_{R1}$: in Example 4.4.11, $\omega$ is constant and $\lambda_{R1}$ goes from $1$ to $0$, so non-increase needs $\frac23 \le \frac23 - c$, that is $c \le 0$. In Theorem 4.4.8 for $p = 3$, $\omega$ goes from $1$ to $\frac43$ and $\lambda_{R1}$ goes from $0$ to $1$, so non-increase needs $\frac43 - c \le 1$, that is $c \ge \frac13$.

For $\lambda$: both points of Theorem 4.4.8 are in R1, so again $c \ge \frac13$. Now let $E = \{1, 2\}$ and
$$a_3 = 2x_0x_1^2x_2^3 + x_0^2x_2^2, \qquad a_6 = x_0^2x_1^4x_2^6 + x_0^3x_1^2x_2^5 + 2x_0^3x_1^5x_2^2 + x_0^4x_2^4,$$
with the other $a_i = 0$. Then $F = x_0x_1^2x_2^3 + 2x_0^2x_2^2$ and $G = 2x_0^3x_1^5x_2^2$. There is no rigid part, so the point is in R1. For $(1,1,1)$ the slopes of $a_3$ and $a_6$ are $\frac43$, which is not an integer, so $\delta = \frac43$. The coefficient $a_3$ has the term $x_0^2x_2^2$, which gives $\mu_1 = 0$ (this vertex is not solvable, since $x_0^2x_2^2$ is not $2C^3$), and $G$ gives $\mu_2 = \frac13$. So $\omega = 1$ and $q = \frac43 - \frac13 = \omega$. Since $\operatorname{in}(F) = 2X_0^2X_2^2$ has degree $2$ in the free $X_0$, the point is low. In these base coordinates, which the strong form of Conjecture 4.4.6 allows, the rule blows up the point: $\mu_0 = \frac13$, $\mu_1 = 0$, $\mu_2 = \frac13$, $\omega \ne 0$, and the values $\delta(\mathbb 1_{01}) = \frac23$, $\delta(\mathbb 1_{02}) = \frac56$, $\delta(\mathbb 1_{12}) = \frac23$ are not integers and are less than $1$. At the origin of the chart of $x_1$, with $E' = \{1, 2\}$,
$$F' = x_1^3x_0'x_2'^3 + 2x_1x_0'^2x_2'^2, \qquad G' = 2x_1^4x_0'^3x_2'^2.$$
For $(1,1,1)$ the slopes are $\frac53$ for $F'$ and $\frac32$ for $G'$, so $\delta' = \frac32$, which is not an integer. The least slopes are $\mu_1' = \frac13$ (from $x_1x_0'^2x_2'^2$) and $\mu_2' = \frac13$ (from $G'$). So $\omega' = \frac32 - \frac23 = \frac56$, and $q' = \frac53 - \frac23 = 1 > \omega'$, so $\xi'$ is not low. Then $\omega - c\lambda$ goes from $1 - c$ to $\frac56$, and non-increase needs $c \le \frac16$. This contradicts $c \ge \frac13$. $\square$

The proof shows the size of the problem. The drop of $\omega$ that $G$ causes in the second example ($\frac16$) is smaller than the jump that the new preparation causes in Theorem 4.4.8 ($\frac13$). A replacement for $\omega$ must carry a second number, for example a measure of how far the prepared $F$ is from a $p$-th power in the free variables, or the rule must change.

### Termination when $\omega = 0$

If $\omega = 0$, then all of $\delta$ is explained by the boundary. The next theorem shows that this case is monomial in the sense of the polyhedron: the polyhedron is an orthant, it stays an orthant, and $\delta$ drops at each step.

**Theorem 4.4.13 (termination at $\omega = 0$).** Let $\xi_0$ be a point of multiplicity $2p$ of $(f, E)$ with $\omega(\xi_0) = 0$. Let $\xi_0, \xi_1, \dots$ be a sequence in which $\xi_{n+1}$ is a point of multiplicity $2p$ over the center chosen at $\xi_n$ by Rule 61.9', for any base coordinates adapted to $E$ and any tie-break. Then $\omega(\xi_n) = 0$ for all $n$, and
$$\delta(\xi_{n+1}) \le \delta(\xi_n) - \tfrac1B, \qquad B = \operatorname{lcm}(1, \dots, 2p).$$
So the sequence has at most $B(\delta(\xi_0) - 1) + 1$ points, and Conjecture 4.4.6 holds in its strong form for the germs with $\omega = 0$.

Node: SG0000009R

*Proof.* By induction it is enough to treat one step. Write $\xi = \xi_n$, $\delta = \delta(\xi)$ and $\mu_k = \mu_k(\xi)$, and let $z$ be simultaneously prepared. Put $\hat\mu = \sum_{k \in E} \mu_k e_k \in \mathbb R^3$.

*Step 1: the orthant.* As in Remark 4.4.3, each monomial $x^\alpha$ of each $a_i$ has $\alpha / i \in \hat\mu + \mathbb R_{\ge 0}^3$. On this orthant $|\cdot| \ge |\hat\mu| = \sum_{k \in E} \mu_k = \delta$, with equality only at $\hat\mu$. Since $\delta = \delta_z(1,1,1)$ is the minimum of $|\alpha|/i$, some $a_{i_0}$ has a monomial $c_0 x^{i_0 \hat\mu}$ with $c_0 \ne 0$. Hence $\delta_z(w) = w \cdot \hat\mu$ for each weight $w$, because the minimum of $w \cdot \beta$ on the orthant is at its corner. Since $z$ is simultaneously prepared, $\delta(\mathbb 1_S) = \sum_{k \in S \cap E} \mu_k$ for each $S$, and $\mu_t = 0$ for each free $t$.

*Step 2: the center.* Since $\delta \ge 1$ and $\omega = 0$, some $\mu_k$ with $k \in E$ is positive, so Remark 4.4.2 (6) applies. If some $\mu_k \ge 1$, the rule takes the divisorial step, and $k \in E$ since $\mu_t = 0$ for $t$ free. Otherwise the rule takes the monomial step and blows up $V(z, x_S)$ with $|S|$ least among the $S$ with $\delta(\mathbb 1_S) \ge 1$. The set $S \cap E$ has the same value $\sum_{k \in S \cap E} \mu_k$, so it also qualifies, and by the choice of $S$ we get $S \subseteq E$. In both cases the center is $V(z, x_S)$ with $S \subseteq E$, so it does not depend on the free coordinates, and it is minimal: $\sum_{k \in S'} \mu_k < 1$ for each proper subset $S' \subset S$. For $|S| = 1$ this is clear, and for $|S| \ge 2$ it holds because a smaller $S'$ with sum at least $1$ would be a permissible center of smaller codimension.

*Step 3: the transform.* Let $\xi'$ be a point of multiplicity $2p$ in the chart of $x_j$, $j \in S$. By Remark 4.4.2 (6), $z' = z/x_j$ vanishes at $\xi'$ and $a_i' = a_i / x_j^i$. First let $\xi'$ be rational, and let $\lambda_k$, $k \in S \setminus \{j\}$, be the values of $x_k'$ at $\xi'$. Put $T = \{k \in S \setminus \{j\} : \lambda_k \ne 0\}$. Local coordinates at $\xi'$ are $x_j$, the $x_k'$ with $k \in S \setminus (T \cup \{j\})$, the $x_l$ with $l \notin S$, and $y_k = x_k' - \lambda_k$ for $k \in T$. A monomial $x^\alpha$ of $a_i$ becomes
$$x_j^{\alpha_j'} \prod_{k \in S \setminus (T \cup \{j\})} x_k'^{\alpha_k} \prod_{l \notin S} x_l^{\alpha_l} \prod_{k \in T} (\lambda_k + y_k)^{\alpha_k}, \qquad \alpha_j' = \sum_{k \in S} \alpha_k - i.$$
Define $\mu''$ in the new coordinates by $\mu_j'' = \sum_{k \in S} \mu_k - 1$, $\mu_k'' = 0$ at the coordinates $y_k$, $k \in T$, and $\mu''_l = \hat\mu_l$ at the other coordinates. Since $S \subseteq E$, we have $\alpha_k \ge i\mu_k$ for $k \in S$, so $\alpha_j' \ge i\mu_j''$, and each monomial of each $a_i'$ has exponent at least $i\mu''$ in each coordinate. A monomial $x^\alpha$ of $a_{i_0}$ contributes to the monomial $x^{i_0\mu''}$ with $y$-exponent $0$ only if $\alpha_l = i_0 \hat\mu_l$ for $l \notin T \cup \{j\}$ and $\alpha_j + \sum_{k \in T} \alpha_k = i_0(\mu_j + \sum_{k \in T} \mu_k)$. Since $\alpha_k \ge i_0 \mu_k$ for each $k \in E$, this forces $\alpha = i_0 \hat\mu$. So that monomial of $a_{i_0}'$ has the coefficient $c_0 \prod_{k \in T} \lambda_k^{i_0\mu_k} \ne 0$, and there is no cancellation. Hence $\delta_{z'}(w) = w \cdot \mu''$ for each weight $w$ at $\xi'$.

If $\xi'$ is not rational, its residue field $k'$ is a finite extension of $k$, so it is perfect. Choose a coefficient field $k'$ of the completed local ring at $\xi'$. The $x_k'$ with $k \in T$ are units, with nonzero values in $k'$, and a regular system of parameters of the fiber at $\xi'$ replaces the $y_k$. The computation is the same, over $k'$.

*Step 4: the vertex of $z'$ is not solvable.* For $(1,1,1)$, the degree $i|\mu''|$ part of $a_i'$ is a multiple of $X^{i\mu''}$. If the vertex were solvable with the form $C$, then $C^{2p} = \operatorname{in}(a_{2p}')$ would be a nonzero multiple of $X^{2p\mu''}$, so $C$ would be a multiple of $X^{\mu''}$ and $\mu''$ would be integral. We exclude this case by case.

- Divisorial step, $S = \{j\}$. Here $\mu'' = \hat\mu - e_j$, and the initial form at $\xi'$ is $\Phi'(Z') = X_j^{-2p}\Phi(X_jZ')$, where $\Phi(Z) = \operatorname{in}_{(1,1,1),z,\delta} f$. If $\Phi' = (Z' + C')^{2p}$, then $\Phi = (Z + X_jC')^{2p}$, and the vertex of $z$ at $\xi$ would be solvable. This contradicts the preparation of $z$.
- Monomial step, $S = \{j, b\}$. Here $\mu_j, \mu_b < 1 \le \mu_j + \mu_b$, so $\mu_j'' \in [0, 1)$, and integrality gives $\mu_j + \mu_b = 1$. If $b \notin T$, then $\mu_b'' = \mu_b \in (0, 1)$, which is not an integer. If $b \in T$, then $\mu''_b = 0$. The third entry is $\hat\mu_l \in [0, 1)$, so it is $0$. So $\mu'' = 0$.
- Monomial step, $S = \{0, 1, 2\}$. By minimality all sums $\mu_k + \mu_l$ of two entries are less than $1$, so $\sum_k \mu_k < \frac32$ and $\mu_j'' \in [0, \frac12)$. So $\mu_j'' = 0$, and the other entries are $0$ or $\mu_k \in [0, 1)$, hence $0$. So $\mu'' = 0$.

But $\mu'' = 0$ means that $a_{i_0}'$ has a nonzero constant term, against the multiplicity $2p$ of $\xi'$. So the vertex is not solvable, and $\delta(\xi') = |\mu''|$ by Remark 4.4.2 (1).

*Step 5: conclusion.* The new boundary is $E' = E \setminus T$: the exceptional divisor $V(x_j)$, the strict transforms $V(x_k')$ for $k \in S \setminus (T \cup \{j\})$, and the $V(x_l)$ for $l \in E \setminus S$. The vector $\mu''$ is $0$ outside $E'$, and $\mu_k' \ge \delta_{z'}(e_k) = \mu_k''$ for $k \in E'$. So
$$0 \le \omega(\xi') = |\mu''| - \sum_{k \in E'} \mu_k' \le |\mu''| - \sum_{k \in E'} \mu_k'' = 0.$$
Finally
$$\delta(\xi) - \delta(\xi') = |\hat\mu| - |\mu''| = 1 - \sum_{k \in S \setminus (T \cup \{j\})} \mu_k > 0,$$
by the minimality of $S$, since $S \setminus (T \cup \{j\})$ is a proper subset of $S$. Both values lie in $\frac1B\mathbb Z$ by Remark 4.4.3, so the difference is at least $\frac1B$. Since $\delta \ge 1$ at each point of multiplicity $2p$, there are at most $B(\delta(\xi_0) - 1)$ steps. No step of the argument uses the tie-break or the free coordinates. $\square$

The proof gives more. At $\omega = 0$ the polyhedron has one vertex, on the boundary, and $z' = z/x_j$ needs no new preparation. This is the analogue for $m = 2p$ of the monomial case of the classical proofs, where the polyhedron is an orthant and a combinatorial invariant drops. Research note 72 checked each step of the proof with independent code (see the table below).

### A long run with $\omega$ constant

The computer searches find long runs with $\omega > 0$ constant. The longest one found comes from a family where the mechanism can be proved.

**Proposition 4.4.14 (a period-5 mechanism).** Let $p = 3$, $E = \{0, 1, 2\}$ and, for integers $e, g \ge 2$,
$$f_{e,g} = (z^3 + x_1x_2^5)^2 + x_0^7x_1^ex_2\, z + x_0^7x_1^gx_2^6.$$
1. At the origin, $\delta = 2$, $\mu = (0, \frac13, \frac15)$ and $\omega = \frac{22}{15}$.
2. If $e \ge 3$, the five blowups "point, $V(z, x_1)$, point, point, $V(z, x_1)$", each followed by the origin of the chart of $x_1$, take $f_{e,g}$ to $f_{e-1, g+9}$, and $\omega = \frac{22}{15}$ at each of the five points.
3. If $3 \le e \le 8$, these five centers are the centers of Rule 61.9' at each step, for every choice of base coordinates. If $e = 2$, the rule blows up the point, and at the origin of the chart of $x_1$ one has $\delta = \frac{13}5$, $\mu = (0, 1, \frac15)$ and $\omega = \frac75$.

So from $f_{e,g}$ with $3 \le e \le 8$ the rule has a branch of length $5(e - 2)$ with $\omega = \frac{22}{15}$ constant, on which the germ never repeats, and which ends with a drop of $\omega$.

Node: SG0000009S

*Proof.* (1) Here $a_3 = 2x_1x_2^5$, $a_5 = x_0^7x_1^ex_2$, $a_6 = x_1^2x_2^{10} + x_0^7x_1^gx_2^6$. For $(1,1,1)$ the slopes are $2$, $\frac{8+e}5$, $2$ and $\frac{13+g}6$, so $\delta_z = 2$. For $e_0$ the least slope is $0$, from $a_3$. For $e_1$ the slopes are $\frac13$, $\frac e5$, $\frac13$ and $\frac g6$, so the least is $\frac13$. For $e_2$ the least is $\frac15$, from $a_5$. The values $\frac13$ and $\frac15$ are not integers. For $(1,1,1)$ and $e_0$ the initial part of $a_3$ is $2x_1x_2^5$, which is not $2C^3$, since $5 \not\equiv 0 \pmod 3$. So no vertex for these weights is solvable, and $\omega = 2 - \frac13 - \frac15 = \frac{22}{15}$.

(2) Since $E = \{0, 1, 2\}$, all centers are coordinate centers and the coordinates are fixed up to units. At the origin of the chart of $x_1$ of a point blowup, a monomial $x^\alpha$ of $a_i$ becomes $x^{(\alpha_0, |\alpha| - i, \alpha_2)}$, and for $V(z, x_1)$ it becomes $x^{(\alpha_0, \alpha_1 - i, \alpha_2)}$. The square stays a square, since $F$ becomes $F/x_1^3$. The $x_1$-exponents of the four monomials $x_1x_2^5$ (in $a_3$), $x_0^7x_1^ex_2$ (in $a_5$), $x_1^2x_2^{10}$ and $x_0^7x_1^gx_2^6$ (in $a_6$) change through the five steps as
$$1 \to 3 \to 0 \to 2 \to 4 \to 1, \qquad e \to e+3 \to e-2 \to e+1 \to e+4 \to e-1,$$
$$2 \to 6 \to 0 \to 4 \to 8 \to 2, \qquad g \to g+7 \to g+1 \to g+8 \to g+15 \to g+9,$$
and the exponents of $x_0$ and $x_2$ do not change. At the five new points the monomial of $a_3$ is $2x_1^ax_2^5$ with $a = 3, 0, 2, 4, 1$, so $a_3$ and $F^2$ give the slope $\frac{a+5}3 = \frac83, \frac53, \frac73, 3, 2$. The slopes of the monomial of $a_5$ are $\frac{e+11}5, \frac{e+6}5, \frac{e+9}5, \frac{e+12}5, \frac{e+7}5$, and they are at least these values when $e \ge 3$. The slopes of $G$ are larger. For $e_1$ the least values are $\frac a3 = 1, 0, \frac23, \frac43, \frac13$, again for $e \ge 3$. For $e_0$ and $e_2$ the values stay $0$ and $\frac15$. When a value is an integer, the vertex is not solvable by the argument of (1): $\operatorname{in}(a_3)$ is a multiple of $X_1^aX_2^5$, and for $e_1$ at $t = 1$ and $t = 0$ the initial part of $a_3$ in $x_1^{3t} k[[x_0, x_2]]$ is $2x_1^{3t}x_2^5$, which is not $2C^3$. So $\delta - \mu_1 = \frac53$ and $\omega = \frac53 - \frac15 = \frac{22}{15}$ at all five points. Each point is the origin of a chart, so $E$ stays $\{0, 1, 2\}$, and each exponent stays nonnegative because $e - 2 \ge 1$.

(3) First, $a_5$ does not depend on $z$: by Lemma 4.1.2, $a_5^{(c)} = a_5 + \sum_{j < 5} \binom{6-j}{5-j} a_j c^{5-j}$, and here $a_1 = a_2 = a_4 = 0$ along the branch, $\binom32 = 3$ and $\binom65 = 6$. So $\delta(\mathbb 1_S) \le \frac15 v_{\mathbb 1_S}(a_5)$ for each $S$. Also $a_3^{(c)} = a_3 + 2c^3$.

The rule takes a main step at the points with $a = 1, 0, 2$, where $e$ is replaced by $e' = e, e-2, e+1$, since there all $\mu_k < 1$. No surface is permissible. The curve $V(z, x_0, x_1)$ is not permissible. Indeed, put $P = (x_0, x_1)$. If $c \in P$, then $a_3 + 2c^3$ has order $a \le 2$ along $V(P)$, since $v_P(2c^3) \ge 3$. If $c \notin P$, the image of $a_3 + 2c^3$ in $R/P = k[[x_2]]$ is $2\bar c^3 \ne 0$ when $a \ge 1$, and $2(x_2^5 + \bar c^3) \ne 0$ when $a = 0$. In both cases $\delta_{z+c}(\mathbb 1_{01}) < 1$. The curve $V(z, x_0, x_2)$ has $\delta(\mathbb 1_{02}) \le \frac85$ from $a_5$, so its value is at most $\frac85 - \frac15 = \frac75 < \frac{22}{15}$. The curve $V(z, x_1, x_2)$ has $\delta(\mathbb 1_{12}) \le \frac{e'+1}5$, so its value is at most $\frac{e+1}5 - \frac13 - \frac15$, $\frac{e-1}5 - \frac15$ and $\frac{e+2}5 - \frac23 - \frac15$ at the three points. All three are less than $\frac{22}{15}$ when $e \le 8$. So no curve is $\omega$-constant, and the rule blows up the point. At the two other points $\mu_1 = 1$ or $\frac43$ is the largest $\mu_k$, and $\mu_0 = 0$, $\mu_2 = \frac15$, so the rule takes the divisorial step along $V(z, x_1)$.

For $e = 2$ the same bounds show that the rule blows up the point. At the origin of the chart of $x_1$ the monomial of $a_5$ is $x_0^7x_1^5x_2$, of slope $\frac{13}5 < \frac83$. So $\delta = \frac{13}5$, not an integer. For $e_1$ the coefficients $a_3$, $a_5$ and $F^2$ give $1$, and the rigid $a_5$ reaches it, so the vertex is not solvable and $\mu_1 = 1$. With $\mu_0 = 0$ and $\mu_2 = \frac15$ we get $\omega = \frac{13}5 - \frac65 = \frac75$. The conclusion follows by $e - 2$ applications of (2) and (3), since $e$ drops by $1$ in each period. $\square$

The quantity that decreases on the run is hidden: it is the gap between the slope $\frac{e+7}5$ of the monomial of $a_5$ and $\delta = 2$ at the start of each period, which is $\frac{e-2}5$. The invariants $(\delta, \mu)$ repeat with period $5$, but the germ does not.

**Example 4.4.15 (germ 57).** The search of research note 66 on the random family `pert651` for $p = 3$ cut a branch at depth $30$ with $\omega = \frac{22}{15}$. Its germ is $f_{9,5}$ of Proposition 4.4.14. The value $e = 9$ is outside part (3). At the first point, $G$ gives $\delta(\mathbb 1_{12}) = \frac{11}6$ at the prepared $z$, so the value of the curve $V(z, x_1, x_2)$ is $\frac{11}6 - \frac8{15} = \frac{13}{10} < \frac{22}{15}$. The computer checks that $z$ is prepared for $\mathbb 1_{12}$ [C]. At the other two main steps of the first period, the bounds of the proof give $\frac75$ and $\frac43$. So after one period the germ is $f_{8,14}$, and Proposition 4.4.14 applies. The result is $\omega = \frac{22}{15}$ from depth $0$ to depth $35$, with $a_5 = x_0^7x_1^5x_2$ at depth $20$ and $a_5 = x_0^7x_1^3x_2$ at depth $30$, and the drop to $\frac75$ at depth $36$. This is what the computer saw. The fact that the other points over each center have a smaller $\omega$ is a computation, not a proof. Another branch of the same germ keeps $\omega = \frac{22}{15}$ up to depth $41$. It ends at depth $43$, where the rule blows up the curve $V(z, x_0, x_2)$ and no point of multiplicity $6$ lies over it.

### What the computer shows

The results of this subsection are computations over $\mathbb F_p$, at rational points only, to a finite depth. They are evidence, not proofs, and they carry the tag [C] of the research notes. They come from research notes 66 and 72. "All ties" means that at each step each tied center of the rule is followed.

*The case $\omega = 0$.* Research note 72 checked Theorem 4.4.13 on random germs with $\omega = 0$, with all ties, and with random changes of the base coordinates adapted to $E$ at half of the nodes. At each node it checked that $\omega = 0$, that a vertex monomial exists, that $\mu_t = 0$ for $t$ free, that $S \subseteq E$, the exact drop of $\delta$, and the bound on the depth. There was no failure.

| $p$ | base changes | germs | nodes | maximal depth | least drop of $\delta$ |
|---|---|---|---|---|---|
| $3$ | no | $285$ | $9102$ | $8$ | $\frac16$ |
| $3$ | yes | $289$ | $1986$ | $7$ | $\frac16$ |
| $3$ | yes | $968$ | $11557$ | $10$ | $\frac16$ |
| $5$ | no | $199$ | $1996$ | $9$ | $\frac1{10}$ |
| $5$ | yes | $200$ | $2143$ | $10$ | $\frac1{10}$ |

*The cut nodes with $\omega > 0$.* Research note 66 ran a search with all branches under the rule on the family `pert651` for $p = 3$, which imitates Theorem 4.4.7, with depth limit $30$. Research note 72 reproduced it: $15386$ nodes, $7$ germs at the time limit, and $220$ nodes cut at depth $30$. Of these, $139$ have $\omega = 0$, so their branches end by Theorem 4.4.13, and $81$ have $\omega > 0$. The $81$ come from three germs: $56$ from germ $57$, $24$ from germ $63$ and $1$ from germ $42$. Their values of $\omega$ are $\frac{22}{15}$ (once), $\frac35$, $\frac25$ and $\frac8{15}$ (twice each), $\frac7{15}$ ($3$), $\frac4{15}$ (once), $\frac15$ ($5$), $\frac2{15}$ ($12$), $\frac1{15}$ ($15$), $\frac13$ ($21$), $\frac16$ ($3$) and $\frac12$ ($14$).

Research note 72 followed every branch from each of the $81$ cut nodes, with all ties, for up to $80$ more steps.

- From $80$ of the $81$ cut nodes, every branch ends. There is no cycle and no node at the new depth limit. These subtrees have $2653$ nodes in total, and $1496$ branches end at a center over which no point of multiplicity $6$ lies.
- For $44$ cut nodes the subtree has at most $3$ nodes.
- In $38$ subtrees some branch reaches $\omega = 0$. In the other $43$, every branch ends while $\omega > 0$, with least values $\frac13$ ($18$ subtrees), $\frac16$ ($6$), $\frac2{15}$ ($10$), $\frac1{15}$ ($7$), $\frac25$ and $\frac7{15}$ (one each). So most branches end by a drop of the multiplicity, not by $\omega = 0$.
- The longest run at the starting value of $\omega$ has $7$ nodes.

*The open subtree.* One subtree is not finished. It starts at a cut node of germ $57$ with $\omega = \frac8{15}$ and $\delta = \frac{12}5$. It hit the time limit of $400$ s after $110$ nodes, with no cycle and no node at the depth limit in those nodes. A run of this subtree with a limit of $2$ hours had not finished when research note 72 was written. Until it is finished, this subtree is open.

*Wider searches.* A search of research note 72 that also follows every permissible curve of smallest codimension in the monomial step saw $74212$ nodes for $p = 3$, with $2409$ cut nodes, $1765$ of them with $\omega = 0$, and no cycle. On each branch, $\omega = 0$ was never followed by $\omega > 0$, as Theorem 4.4.13 says. For $p = 5$ (depth $25$) it saw $18488$ nodes, with no cycle and $65$ cut nodes, $55$ with $\omega = 0$ and $10$ with $\omega \in \{\frac3{35}, \frac3{70}\}$. In the family of Proposition 4.4.14, the longest $\omega$-constant branch from $f_{e,200}$ has length $5(e - 2)$ for $2 \le e \le 8$ and $5(e - 9)$ for $9 \le e \le 15$, and it is at most $35$ for $e \le 40$.

### What is open

1. Conjecture 4.4.6 when $\omega(\xi_n) > 0$ for every $n$, in its weak or strong form. This is part (b) of Problem 10.2 of the research notes for $m = 2p$. No counterexample is known, and the computations above found no cycle. One subtree of the search is still open.
2. A secondary invariant for the runs with $\omega$ constant. On the run of Proposition 4.4.14 the gap $\frac{e-2}5$ decreases. Is there an intrinsic form of this gap, for example an order of the part of the polyhedron away from its vertex, that drops on each $\omega$-constant step of the rule, or at least once in a bounded number of steps?
3. Is the length of an $\omega$-constant run bounded in terms of $p$ and $\delta(\xi_0)$? Is the jump of $\omega$ under the rule bounded? Theorems 4.4.7 and 4.4.8 give the jumps $\frac1{p(p+1)}$ and $\frac1p$.
4. A replacement for $\omega$. By Proposition 4.4.12 it cannot be $\omega$ minus a constant times a flag. It must measure how far the new $F$ is from a $p$-th power in the free variables, and it must survive the step from R1 to R2 of Example 4.4.11.
5. Points that are not rational. All searches follow only the $\mathbb F_p$-rational points of the exceptional fibers.

### Exercises

1. Show that $\binom{2p}{p} \equiv 2$, $\binom{2p}{2} \equiv 0$ and $\binom{2p-2}{p-1} \equiv 0$ modulo $p$. Deduce the formula for $F^{(c)}$ after Definition 4.4.4, and find all $j$ with $0 \le j \le 2p - 2$ such that $\binom{2p-2}{j} \equiv 0 \pmod p$.
2. In Theorem 4.4.7 for $p = 3$, write the coefficients $b_3, b_4, b_5, b_6$ at $\xi'$ and their orders. Check that $\sigma^* = \frac{13}5$ and $\omega(\xi') = \frac56$, and find the error that gives $\frac{12}5$.
3. In Theorem 4.4.7, find the points of multiplicity $2p$ in the chart of $x_0$ with $x_2' = 0$, and compute $\omega$ at them. Compare with $\omega(\xi)$.
4. Find the step in the proof of Lemma 4.4.10 that uses R1. Give a germ in R3 and a translation $z \mapsto z + c$ with $\operatorname{ord} c = \delta$ for which a rigid term of $F^{(c)}$ has degree $p\delta$.
5. Let $p = 3$, $E = \{0, 1, 2\}$ and $f = z^6 + x_0^3x_1^3x_2^3z^2 + x_0^4x_1^4x_2^4$. Show that $\omega = 0$. Find the centers that Rule 61.9' can choose at the origin, the boundary and $\delta$ at each point of multiplicity $6$ over them, and compare the length of the longest sequence with the bound of Theorem 4.4.13.
6. In Step 4 of the proof of Theorem 4.4.13, show by an example that $\mu'' = \hat\mu - e_j$ can be integral after a divisorial step. So the argument for the divisorial step cannot use integrality alone.
7. Check the four exponent sequences in the proof of Proposition 4.4.14. For $e = 9$ and $g \ge 6$, show that the bound of part (3) does not exclude the curve $V(z, x_1, x_2)$ at the first step.
8. (Open.) Find an invariant that is intrinsic, drops on the run of Proposition 4.4.14, and does not go up under the centers of Theorems 4.4.7 and 4.4.8.

### Notes and references

The slope $\delta$ is the first slope of the characteristic polyhedron of Hironaka [Hir67], computed for monomial valuations, and the vertex criterion is his test for a solvable vertex. The residual slope $\omega$ and Rule 61.9' are from research note 61. Research note 65 is the referee report on note 61. It proves Theorem 4.4.7, which shows that part (a) of Conjecture 61.18 of note 61 is false, and it states Conjecture 4.4.6. Research note 66 proves Theorem 4.4.8, Lemma 4.4.10, Example 4.4.11, Proposition 4.4.12 and Theorem 4.4.13, and it finds the slip in the proof of Theorem 4.4.7. Research note 72 is the referee report on note 66. It checks these results, proves that the center of Example 4.4.11 is forced in all base coordinates, corrects the order of $b_{p+1}$ in Theorem 4.4.8, proves Proposition 4.4.14, and makes the computations of the subsection "What the computer shows".

For $m = p$, the invariant $\epsilon$ of Cossart and Piltant is $p$ times the residual slope, and their differential invariant $\omega$ has values in $\{\epsilon, \epsilon - 1\}$ [CP19, Definitions 2.25 and 2.68]. Their Theorem 3.13 says when $\epsilon$ can go up, and the conditions are the ones of Theorems 4.4.7 and 4.4.8: an integer slope, and a leading form that becomes a $p$-th power. Hauser attributes the first examples of such increases to Abhyankar, Cossart, Moh and Seidenberg [Hau10, Sections D, F and G]. Hauser and Perlega characterise the increases of the residual order [HP19b]. One of their necessary conditions is the loss of two boundary components, as in Theorem 4.4.7, where $E = \{0, 1, 2\}$ becomes $E' = \{0, 1\}$ and the exceptional divisor replaces $V(x_0)$.

The nodes of this section are SG0000009K (Theorem 4.4.7), SG0000009M (Theorem 4.4.8), SG0000009N (Lemma 4.4.10), SG0000009P (Example 4.4.11), SG0000009Q (Proposition 4.4.12), SG0000009R (Theorem 4.4.13), SG0000009S (Proposition 4.4.14) and SG0000009T (Conjecture 4.4.6). None of them is in Lean.
