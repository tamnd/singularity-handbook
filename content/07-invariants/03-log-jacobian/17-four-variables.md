---
title: Corner runs in four variables
nodes: [SG0000006J, SG0000006K, SG0000006M, SG0000006N, SG0000006P, SG0000006Q, SG0000006R, SG0000006S, SG0000006T, SG0000006V, SG0000006W, SG0000006X, SG0000006Y, SG0000006Z, SG00000070, SG00000071, SG00000072, SG00000073, SG00000074, SG00000075, SG00000076, SG00000077, SG00000078, SG00000079, SG0000007A, SG0000007B, SG0000007C, SG0000007D, SG0000007E]
sources: [CJS20, Kuh10, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Corner runs in four variables

Sections 3.15 and 3.16 treat the corner runs in three variables. There the point moves along the corner $V(y) \cap V(z)$, each step is a chart followed by a translation $t_m$ of the one free coordinate $x$, and the main result says that only a finite number of the $t_m$ are nonzero (Theorem 3.16.14). After the last one, the corner curves of Theorem 3.13.20 have $\nu^G \ge \rho$, so Question 3.13.18 has a positive answer. The Notes of Section 3.14 ask what happens in four variables with two letters, that is, for $n = 4$ and $k = 2$. Now there are two free coordinates $x$ and $w$, and each step has a translation vector $(a_m, b_m) \in K^2$. In this section we answer the question and look at what can replace the finiteness.

The answer to the question of Section 3.14 is negative. The points $x^2 y^{p-2} z^{p-2} + F$ with $F$ divisible by $y^p z^p$ keep $\rho = 1$ for each choice of the translations in $w$ (Proposition 3.17.8), so a corner run in four variables can have an infinite number of nonzero translations (Corollary 3.17.12). This does not depend on the choice of the free coordinates (Lemma 3.17.6), and it occurs also at points that are not a product of a point in three variables with a line (Lemma 3.17.11). But all these runs lie on the strict transforms of the hypersurface $V(x)$, and Question 3.13.18 has a positive answer for them. So what fails is the route through the finiteness, and not the question.

This leads to three forms of the statement that could replace the finiteness. Conjecture L asks that the run lies eventually on a regular hypersurface. Conjecture L+ asks in addition for corner surfaces with $\nu^G \ge \rho$ in this hypersurface, and it is false (Theorem 3.17.21 and Example 3.17.22). It is false also for the linear runs with an infinite number of nonzero translations (Theorem 3.19.17). Conjecture L° asks for corner curves with $\nu^G \ge \rho$, and it implies a positive answer to Question 3.13.18. The section proves the following.

1. Proved without a hypothesis: the tools of Sections 3.15 and 3.16 for two free coordinates (Lemmas 3.17.1 and 3.17.2, Propositions 3.17.3 and 3.17.4), the family with an infinite number of translations (Proposition 3.17.8 and Corollary 3.17.12), the reduction to three variables (Theorem 3.17.13 and Corollary 3.17.14), the class of one linear form (Theorem 3.17.15 and Corollary 3.17.17), the counterexamples to L+ (Theorem 3.17.21 and Example 3.17.22), the results on the points of type $0$ (Theorems 3.17.27 and 3.17.29), and the result on the binary initial forms (Proposition 3.17.30).
2. If $\deg_{x, w} g < p$, then each corner run is linear and Conjecture L holds for it (Theorem 3.17.33). The proof here uses the hypothesis H1 (Hypothesis 3.17.32), and Section 3.18 proves H1 for $\deg_{x, w} g < p$ (Corollary 3.18.18).
3. Conjectures: L (Conjecture 3.17.18) and L° (Conjecture 3.17.24). They hold in all the examples and tests. Section 3.18 proves both of them for $\deg_{x, w} g < p$, and Section 3.19 proves Conjecture L for each clean $g$ (Corollary 3.19.7). So Conjecture L° is open only for $\deg_{x, w} g \ge p$ outside $K[[y, z]][x^p, w^p]$.

In each example that we know, Question 3.13.18 has a positive answer.

### The setting

Let $K$ be an algebraically closed field of characteristic $p$. From $P_N$ on we have $n = 4$ and the coordinates $(x_m, w_m, y_m, z_m)$ at $P_m$, with $V(y_m)$ and $V(z_m)$ in $\Delta$ and $V(x_m)$, $V(w_m)$ not in $\Delta$. Step $m$ blows up $P_m$ and takes the $y$-chart or the $z$-chart, followed by a translation $(a_m, b_m) \in K^2$:
$$\text{$y$-chart: } y_m = y_{m+1}, \ z_m = y_{m+1} z_{m+1}; \qquad \text{$z$-chart: } z_m = z_{m+1}, \ y_m = z_{m+1} y_{m+1};$$
$$x_m = L_m (x_{m+1} + a_m), \qquad w_m = L_m (w_{m+1} + b_m),$$
with $L_m = y_{m+1}$ in the $y$-chart and $L_m = z_{m+1}$ in the $z$-chart. In the $y$-chart, the points of the exceptional divisor on the strict transform of $V(z_m)$ form the plane $y_{m+1} = z_{m+1} = 0$ with the coordinates $(x_{m+1}, w_{m+1})$. So the vectors $(a_m, b_m)$ are exactly the points of this plane, and a corner step has two parameters, not one. A *corner run in four variables* is a sequence of such steps in which each chart occurs an infinite number of times and $\rho \ge 1$ is the same at each point. The function of a point is the strict transform with the factor $L_m^{-p}$, followed by the cleaning, as in Section 3.15. We assume that $g \in K[[y, z]][x, w]$ is clean in the coordinates of $P_N$, and, as in Sections 3.12 to 3.16, that the points have $\operatorname{ord} g \ge p$.

The translations do not change $y$ and $z$. So the monomials $M_N = 1$ and $M_{m+1} = M_m L_m$, the irrational number $\theta$, the valuation $v(y_N^a z_N^b) = a + \theta b$ and Lemma 3.13.24 are the same as for $n = 3$. In particular $M_m = y_N z_N / (y_m z_m)$, $v(M_m)$ increases to $1 + \theta$, and for $j < m$ both $M_{j+1}$ and $M_m / M_{j+1}$ are monomials in $y_m, z_m$ with nonnegative exponents. The dominance lemma 3.15.4 uses only the letters and the word, so it holds without change. Put
$$\varphi_N = \psi_N = 0, \qquad \varphi_{m+1} = \varphi_m + a_m M_{m+1}, \qquad \psi_{m+1} = \psi_m + b_m M_{m+1}.$$
For a polynomial $f(X, W)$ the Hasse derivatives are $f^{[k, l]} = \sum_{i, j} \binom{i}{k} \binom{j}{l} f_{ij} X^{i - k} W^{j - l}$, and Taylor's formula $f(\varphi + X, \psi + W) = \sum_{k, l} f^{[k, l]}(\varphi, \psi) X^k W^l$ holds over each commutative ring.

The first lemma is Lemma 3.15.1 with two free coordinates. Both coordinates are multiplied by the same $L_m$ at each step, so the proof does not change.

**Lemma 3.17.1.** For each $m \ge N$:

1. $x_N = \varphi_m + M_m x_m$ and $w_N = \psi_m + M_m w_m$, and $\varphi_m, \psi_m$ are polynomials in $y_m, z_m$ with no constant term.
2. The function of $P_m$ is $M_m^{-p} g_m$, where $g_m = \operatorname{cl} g(\varphi_m + M_m x_m, \psi_m + M_m w_m)$, with $y_N, z_N$ written in $y_m, z_m$. So $g_m$ and $P_m$ have the same $G$, $d$ and $\rho$.
3. $g(\varphi_m + M_m X, \psi_m + M_m W) = \sum_{k, l} A_{kl} X^k W^l$ with $A_{kl} = M_m^{k + l} g^{[k, l]}(\varphi_m, \psi_m) \in K[[y_m, z_m]]$, and $g_m$ is the sum of the terms $A_{kl} x_m^k w_m^l$ over the $(k, l)$ with $k$ or $l$ not divisible by $p$, plus the sum of the terms $\operatorname{cl}(A_{kl}) x_m^k w_m^l$ over the $(k, l)$ with $p \mid k$ and $p \mid l$.
4. $\partial_{x_m} g_m = M_m g_x(\varphi_m + M_m x_m, \psi_m + M_m w_m)$, and the same holds for $w$.

Node: SG0000006J

*Proof.* Part 1 is the induction of Lemma 3.13.24, part 3, for each of the two free coordinates: from $x_N = \varphi_m + M_m x_m$ and $x_m = L_m (x_{m+1} + a_m)$ we get $x_N = \varphi_m + a_m M_m L_m + M_m L_m x_{m+1} = \varphi_{m+1} + M_{m+1} x_{m+1}$, and the same for $w$. The other parts are the proof of Lemma 3.15.1. It uses only two facts. First, the cleaning commutes with the substitution, since $\pi(h^p) = \pi(h)^p$ and the monomial maps have the determinant $\pm 1$. Second, a monomial $c\, Y x^k w^l$ with $k$ or $l$ not divisible by $p$ is not a $p$-th power. Both hold with two free coordinates. Part 4 is the chain rule. $\square$

A *free coordinate system* at $P_m$ is a pair $(x'', w'')$ of series such that $(x'', w'', y_m, z_m)$ is a regular system of parameters. The next lemma says that $\rho$ and the run do not depend on this choice. Only the translations change.

**Lemma 3.17.2.**

1. The logarithmic derivations at $P_m$ have the basis $\partial_{x''}, \partial_{w''}, y \partial_y, z \partial_z$ in each free coordinate system. So $\Theta(g) = (g_x, g_w, y g_y, z g_z)$, its monomial $x^r$ and $\rho$ do not depend on the free coordinates. They do not change if we add a $p$-th power to $g$, or if we multiply $g$ by $\varepsilon^p$ with $\varepsilon$ a unit.
2. Let $(x'', w'')$ be a free coordinate system at $P_m$. Then the run from $P_m$ is a corner run in four variables in the coordinates $(x'', w'', y_m, z_m)$, with the same points, charts and $\rho$, and with other translations $(a''_j, b''_j) \in K^2$.
3. If $(x'', w'') = (x_m, w_m) A^T$ with $A \in \mathrm{GL}_2(K)$, then the coordinates $(x_j, w_j) A^T$ at $P_j$, $j \ge m$, have the translations $(a_j, b_j) A^T$.

Node: SG0000006K

*Proof.* Part 1 is the proof of Lemma 3.15.2, parts 1 to 4, with one more free coordinate. Part 3 follows from $\alpha x_m + \beta w_m = L_m (\alpha x_{m+1} + \beta w_{m+1} + \alpha a_m + \beta b_m)$. Part 2. As in the proof of Lemma 3.15.2, part 5, it is sufficient to treat one step. Write $x'' = f(y, z) + x u_{11} + w u_{12}$ and $w'' = f'(y, z) + x u_{21} + w u_{22}$ with series $u_{ij}$. Since $(x'', w'', y, z)$ is a regular system, the matrix $(u_{ij}(0))$ is invertible. In the chart, $x'' / L = (x_{m+1} + a_m) \pi(u_{11}) + (w_{m+1} + b_m) \pi(u_{12}) + f / L$, and $f / L$ is a series, since $y, z \in (L)$. Let $a''$ be its value at $P_{m+1}$ and put $x''_{m+1} = x'' / L - a''$, and the same for $w''$. Each derivative of $\pi(u_{ij})$ in $x_{m+1}$ or $w_{m+1}$ has the factor $L$. So the Jacobian matrix of $(x''_{m+1}, w''_{m+1})$ in $(x_{m+1}, w_{m+1})$ at $P_{m+1}$ is $(u_{ij}(0))$, and $(x''_{m+1}, w''_{m+1})$ is a free coordinate system at $P_{m+1}$. The rest is the proof of Lemma 3.15.2, part 5. $\square$

As in Remark 3.15.3, the linear changes of part 3 are the only free changes that the steps keep in an obvious way. A change such as $x'' = x + y w$ gives translations that depend on the word.

For a point $P_m$ put $w_{kl} = v(A_{kl})$ if $k$ or $l$ is not divisible by $p$, and $w_{kl} = v(\operatorname{cl} A_{kl})$ otherwise, with $v(0) = \infty$. The criterion (★) of Section 3.15 becomes:

(★★) $\operatorname{cl} A_{00} \ne 0$, and $v(\operatorname{cl} A_{00}) < w_{kl}$ for each $(k, l) \ne (0, 0)$.

**Proposition 3.17.3.** If (★★) holds at a point $P_m$, then there is an $m_0$ such that for each $m' \ge m_0$ and each choice of the later translations, $G_{m'}$ is a unit, so $\rho = 0$ at $P_{m'}$. So (★★) fails at each point of a corner run in four variables.

Node: SG0000006M

*Proof.* This is the proof of Proposition 3.15.5. Let $\mu_0$ be the term of $\operatorname{cl} A_{00}$ with the least value, and let $S \subseteq \mathbb{N}^2$ be the set of the exponents in $y_m, z_m$ of the terms of $g_m$. A term with $x_m^k w_m^l$, $(k, l) \ne (0, 0)$, has a value at least $w_{kl} > v(\mu_0)$, so the exponent $q_*$ of $\mu_0$ is the only point of $S$ with the least value. The set $S$ is a finite union of supports, since $g$ is a polynomial in $x, w$. Lemma 3.15.4 gives an $m_0$. For $m' \ge m_0$ write $x_m = \psi' + M' x_{m'}$ and $w_m = \psi'' + M' w_{m'}$, with $M' = M_{m'} / M_m$ and $\psi', \psi''$ polynomials in $y_{m'}, z_{m'}$. Each term $Y x_m^k w_m^l$ of $g_m$ with an exponent other than $q_*$ goes to a sum of terms $\pi(Y) \eta\, x_{m'}^i w_{m'}^j$ with $\eta$ a monomial with nonnegative exponents, and both exponents of $\pi(Y)$ are larger than those of $\pi(\mu_0)$. So $\pi(g_m) = \pi(\mu_0)(1 + f)$ with $f$ in the maximal ideal, the cleaning keeps $\pi(\mu_0)$, and $G_{m'}$ is a unit. $\square$

### Directions of the translations

For $\lambda = (\alpha, \beta) \in K^2 \setminus \{0\}$ put $t^\lambda_j = \alpha a_j + \beta b_j$ and $\varphi^\lambda_m = \alpha \varphi_m + \beta \psi_m = \sum_{j < m} t^\lambda_j M_{j+1}$. By Lemma 3.17.2, part 3, $t^\lambda_j$ is the translation of the free coordinate $\alpha x + \beta w$. So each direction $\lambda$ gives a sequence of the kind of Section 3.15. Let $H = K(y_N, z_N)$ with the valuation $v$, let $\hat H$ be its completion, and let $\mathbb{K}$ be the Hahn field of Lemma 3.15.6. Put $\varphi_\infty = \sum_j a_j M_{j+1}$ and $\psi_\infty = \sum_j b_j M_{j+1}$ in $\mathbb{K}$.

**Proposition 3.17.4.** Let $\lambda \ne 0$, and assume that an infinite number of the $t^\lambda_j$ are not $0$. Then the values of $\varphi^\lambda$ at the points just after these translations form a pseudo Cauchy sequence of transcendental type over $\hat H$, and $\alpha \varphi_\infty + \beta \psi_\infty$ is transcendental over $\hat H$.

Node: SG0000006N

*Proof.* The proofs of Lemma 3.15.6, part 3, and Proposition 3.15.7 use only that the sequence is $\sum_j t_j M_{j+1}$ with $t_j \in K$ and with the monomials of the run. They do not use $g$. The field $H$, the value group $\mathbb{Z} + \theta \mathbb{Z}$ and the Hahn field are the same as for $n = 3$, since the run has the two letters $y, z$. So the proofs apply to the $t^\lambda_j$. The transcendence is the first step of Remark 3.16.15, which uses only the transcendental type. $\square$

For $k = 2$ letters the value group has the rational rank $2$ for each $n$, so Proposition 3.17.4 is enough for one direction. For $k \ge 3$ letters the valuation of Proposition 3.14.4 has the rational rank $k$, and Lemma 3.15.6 and Proposition 3.15.7 must be proved again.

**Definition 3.17.5.** A corner run in four variables is *linear* if there is a $\lambda \ne 0$ with $t^\lambda_j = 0$ for $j$ large, and *planar* if not.

In a planar run each $\lambda \ne 0$ has an infinite number of $t^\lambda_j \ne 0$, so by Proposition 3.17.4 no nonzero combination $\alpha \varphi_\infty + \beta \psi_\infty$ with $\alpha, \beta \in K$ is in $\hat H$. We do not have the transcendental type for the pair $(\varphi_\infty, \psi_\infty)$. Remark 3.17.34 says more about this.

Can a change of the free coordinates remove an infinite number of translations? The next lemma says no. It is the reason why the examples of the next part are real counterexamples, and not an effect of a bad choice of coordinates.

**Lemma 3.17.6.** Let $P_N, P_{N+1}, \dots$ be a corner run in four variables, and let $J \ge N$.

1. If there is a free coordinate system $(x', w')$ at $P_J$ whose translations are $0$ from some point on, then only a finite number of the $(a_j, b_j)$ are nonzero.
2. If the translations of a free coordinate $x' = \alpha_0 x_J + \beta_0 w_J + \gamma(y_J, z_J)$, with $(\alpha_0, \beta_0) \ne 0$ and $\gamma(0) = 0$, are $0$ from some point on, then $\alpha_0 a_j + \beta_0 b_j = 0$ for $j$ large.

Node: SG0000006P

*Proof.* We first note a fact on hypersurfaces. Let $x'_j$ be a free coordinate at $P_j$, and put $x'_{j+1} = x'_j / L_j - t'_j$ as in the proof of Lemma 3.17.2, part 2. The strict transform of $V(x'_j)$ is $V(x'_j / L_j)$, so $P_{j+1}$ lies on it if and only if $t'_j = 0$, and then $x'_{j+1}$ is its equation. So if the translations of $x'$ and $w'$ are $0$ for $j > J'$, then the points $P_j$, $j > J'$, lie on the strict transforms of the regular surface $V(x'_{J'+1}, w'_{J'+1})$. We change $J$ to $J' + 1$, and we write the coordinates of $P_J$ without the index.

Part 1. The surface is a graph $x = \alpha(y, z)$, $w = \beta(y, z)$ with $\alpha, \beta \in K[[y, z]]$ in the coordinates of $P_J$, by the implicit function theorem. We show by induction that the strict transform at $P_m$ is the graph $x_m = \alpha_m$ with $\alpha_m = (\alpha - \varphi^{(J)}_m) / M^{(J)}_m$, where $\varphi^{(J)}_m$ and $M^{(J)}_m$ are $\varphi_m$ and $M_m$ for the run from $P_J$, and that $\alpha_m \in K[[y_m, z_m]]$ with $\alpha_m(0) = 0$. If this holds at $P_m$, then $\alpha_m$ is divisible by $L_m$ in the chart, since $y_m, z_m \in (L_m)$, so the strict transform is $x_{m+1} = \alpha_m / L_m - a_m$, and $P_{m+1}$ lies on it if and only if $(\alpha_m / L_m)(0) = a_m$. This gives the claim at $P_{m+1}$. So each term of $\alpha - \varphi^{(J)}_m$ has a value larger than $v(M^{(J)}_m)$. Now $\varphi^{(J)}_m = \sum_{J \le i < m} a_i M^{(J)}_{i+1}$ is a sum of distinct monomials, and $v(M^{(J)}_{i+1}) < v(M^{(J)}_m)$ for $i + 1 < m$. So $\alpha$ has the term $a_i M^{(J)}_{i+1}$ for each $i \ge J$. The values $v(M^{(J)}_{i+1})$ are bounded by the limit of $v(M^{(J)}_m)$, which is finite. If an infinite number of the $a_i$ are not $0$, then $\alpha$ has an infinite number of terms below a fixed value. This is not possible by Lemma 3.13.24, part 2. The same argument applies to $\beta$ and the $b_i$.

Part 2. By Lemma 3.17.2, part 3, the free coordinate $x'' = \alpha_0 x_J + \beta_0 w_J$, completed to a linear free coordinate system, has the translations $\alpha_0 a_j + \beta_0 b_j$. The points lie on the strict transforms of $V(x') = V(x'' + \gamma)$, which is the graph $x'' = -\gamma(y, z)$ over the coordinates $(w, y, z)$ with the equation independent of the second free coordinate. The argument of part 1 with $x''$ in place of $x$ and $-\gamma$ in place of $\alpha$ gives the claim. $\square$

So the property "only a finite number of the translations are nonzero" does not depend on the free coordinates, and neither does the property "the translations of one direction are $0$ from some point on".

### Runs with an infinite number of nonzero translations

The Notes of Section 3.14 ask the following question.

**Question 3.17.7.** Let $g \in K[[y, z]][x, w]$ be clean. Does each corner run in four variables from $P_N$ have only a finite number of nonzero translations?

Node: SG0000006Q

For $n = 3$ the answer is positive (Theorem 3.16.14). The reason is that $\rho \ge 1$ forces $g$ to depend strongly on the only free coordinate $x$, so each translation in $x$ is seen by $g$. For $n = 4$ there can be a direction in which $g$ depends only on terms of a large value. Then the translations in this direction are not seen, and the answer is negative. The simplest example is $g = x^2 y^{p-2} z^{p-2}$, which does not depend on $w$ at all. The next result gives examples that depend on $w$.

**Proposition 3.17.8.** Let $p \ge 3$ and $Y = y^{p-2} z^{p-2}$. Let $F \in K[[y, z]][x, w]$ be a polynomial in $x, w$ such that each monomial of $F$ is divisible by $y^p z^p$ and $g = x^2 Y + F$ is clean. Then a sequence of steps from $P_N$ in which each chart occurs an infinite number of times is a corner run in four variables if and only if $a_m = 0$ for each $m$. In this case $\rho = 1$ at each point, for each choice of the $b_m \in K$. The function of $P_m$ is $y_m^{p-2} z_m^{p-2} (x_m^2 + R)$ up to a $p$-th power monomial factor, with $R \in (y_m z_m)$, and $\nu^G \ge 1$ along $V(x_m, y_m)$ and $V(x_m, z_m)$.

Node: SG0000006R

Before the proof we do one step by hand. Take $F = w y^p z^p$ and the $y$-chart with the translation $(0, b)$, so $x = y x'$, $w = y (w' + b)$ and $z = y z'$. Then
$$x^2 Y = y^{2p - 2} z'^{p - 2} x'^2, \qquad w y^p z^p = y^{2p + 1} z'^p (w' + b),$$
and after the division by $y^p$ the function is
$$y^{p-2} z'^{p-2} \bigl( x'^2 + y^3 z'^2 (w' + b) \bigr).$$
No monomial is a $p$-th power, since the exponent of $y$ in $b\, y^{p+1} z'^p$ is $p + 1$. So the new point has the same form, with $R = y^3 z'^2 (w' + b)$, for each $b$. The proof shows that this happens at each step.

*Proof.* Let $E_m$ be the linear map that sends the exponent $q$ of a monomial $y_N^{q_1} z_N^{q_2}$ to its exponent in $y_m, z_m$. It maps $\mathbb{N}^2$ into $\mathbb{N}^2$, and the exponent of $M_m = y_N z_N / (y_m z_m)$ is $e_m = E_m(1, 1) - (1, 1)$.

First let $a_j = 0$ for each $j$. Then $\varphi_m = 0$, and Lemma 3.17.1 gives $g_m = \operatorname{cl}(M_m^2 Y x^2 + F(M_m x, \psi_m + M_m w))$. A term $c\, x^i w^l y^A z^B$ of $F$, with $A, B \ge p$, gives the terms
$$c \binom{l}{s} M_m^{i + s} \psi_m^{l - s} y_N^A z_N^B \, x^i w^s, \qquad 0 \le s \le l.$$
Each monomial of $\psi_m^{l - s}$ is a product of $l - s$ monomials $M_{j+1}$ with $j < m$, and these have nonnegative exponents in $y_m, z_m$. Put $A' = A - p + 2 \ge 2$ and $B' = B - p + 2 \ge 2$. A monomial of this term, divided by $M_m^2 Y$, is $Q x^i w^s$, where the exponent of $Q$ is at least
$$E_m(A', B') + (i + s - 2) e_m .$$
If $i + s \ge 2$, this is at least $E_m(2, 2) = 2 e_m + (2, 2)$. If $i + s = 1$, it is $E_m(A' - 1, B' - 1) + (1, 1) \ge (1, 1)$. If $i + s = 0$, it is $E_m(A' - 2, B' - 2) + (2, 2) \ge (2, 2)$. So $Q$ is divisible by $y_m z_m$. The term $M_m^2 Y x^2$ is not a $p$-th power, since $p \nmid 2$, and the cleaning only removes terms. So
$$g_m = M_m^2 Y (x^2 + R), \qquad R \in (y_m z_m).$$
All the generators of $\Theta(g_m)$ are divisible by $M_m^2 Y$, and $\partial_x g_m = M_m^2 Y (2x + \partial_x R)$ with $2x + \partial_x R$ not divisible by $y_m$ or $z_m$. So $x^r = M_m^2 Y$ and $G_m = x^2 + R$. The generator $\partial_x G_m = 2 x + \partial_x R$ has the order $1$. The other generators $\partial_w G_m = \partial_w R$, $r_y G_m + y \partial_y G_m$ and $r_z G_m + z \partial_z G_m$ are in the maximal ideal, since $G_m$ is. So $\rho = 1$. Also $\operatorname{ord} g_m \ge 2p - 2 \ge p$. Along $Z = V(x_m, z_m)$ we have $\operatorname{ord}_Z g_m \ge r_z + \operatorname{ord}_Z G_m \ge r_z + 1$, since $G_m \in (x, z)$, so $\nu^G_Z \ge 1$. The same holds for $V(x_m, y_m)$.

Now let $j$ be the first index with $a_j \ne 0$. Then $\varphi_{j+1} = a_j M_{j+1}$, and $x_N = M_{j+1} (x_{j+1} + a_j)$. The computation above, with $(x + a_j)$ in place of $x$, gives $g_{j+1} = M_{j+1}^2 Y ((x + a_j)^2 + R)$ with $R \in (y z)$, up to the removal of $p$-th power terms. The generators of $\Theta(g_{j+1})$ are divisible by $M_{j+1}^2 Y$, and $\partial_x g_{j+1} = M_{j+1}^2 Y (2 x + 2 a_j + \partial_x R)$ is this monomial times a unit. So $\rho = 0$ at $P_{j+1}$, and the sequence is not a corner run. $\square$

**Example 3.17.9.** Three members of the family.

1. $F = 0$, that is, $g = x^2 y^{p-2} z^{p-2}$. This is Example 3.15.18 with a fourth variable. The point is a product of a point in three variables with the $w$-line, and the translations in $w$ are not seen at all.
2. $F = w y^p z^p$. This is clean, since $w$ has the exponent $1$. The step by hand above shows how $w$ enters $R$.
3. $F = x w y^p z^p$. This is also clean.

By Proposition 3.17.8 the points 2 and 3 keep $\rho = 1$ for each choice of the $b_m$. The next lemma shows that they are not products with a line at any point of the run.

**Definition 3.17.10.** A point $P_m$ of a corner run in four variables is *cylindrical* if there is a free coordinate system $(x', w')$ at $P_m$ such that the function of $P_m$ is congruent, modulo $p$-th powers, to a series $f \in K[[x', y_m, z_m]]$.

We can take $f$ clean in $(x', y_m, z_m)$. A cylindrical point is a point in three variables times a line, and Theorem 3.17.13 below reduces it to Sections 3.15 and 3.16.

**Lemma 3.17.11.** Let $p \ge 3$, $Y = y^{p-2} z^{p-2}$, and let $g = x^2 Y + w y^p z^p$ or $g = x^2 Y + x w y^p z^p$. At each point $P_m$ of a corner run in four variables of $g$ there is no free coordinate system $(x'', w'')$ such that the function of $P_m$ is, up to a $p$-th power and a factor $\varepsilon^p$ with $\varepsilon$ a unit, a series in $x'', y_m, z_m$. So no point of the run is cylindrical.

Node: SG0000006S

*Proof.* The idea is that a function of $x'', y, z$ is killed by the derivation $\partial / \partial w''$, and we show that no derivation of this kind kills $g_m$. Assume that there is such a system, and let $D = \partial / \partial w''$ in the system $(x'', w'', y_m, z_m)$. Then $D(y_m) = D(z_m) = 0$, so $D = \alpha \partial_x + \beta \partial_w$ with $\alpha = D(x_m)$ and $\beta = D(w_m)$. From $\alpha\, \partial_x w'' + \beta\, \partial_w w'' = D(w'') = 1$ we see that $\alpha(0)$ and $\beta(0)$ are not both $0$. The derivation kills the $p$-th powers, and $D(\varepsilon^p f) = \varepsilon^p D(f)$. So $D$ kills the function of $P_m$, and then $D(g_m) = 0$. By the proof of Proposition 3.17.8, $a_j = 0$ for each $j$ and $g_m = M_m^2 Y (x^2 + R)$. The derivation kills $M_m^2 Y$, so $D(x^2 + R) = 0$.

For $F = w y^p z^p$ we have $R = Q_0 + Q w$, with $Q = y_N^p z_N^p / (M_m Y)$ a monomial divisible by $y_m z_m$ and $Q_0 \in K[[y_m, z_m]]$. Then $0 = D(x^2 + R) = 2 \alpha x + \beta Q$. So $x$ divides $\beta Q$, hence $x$ divides $\beta$. Also $y_m$ divides $2 \alpha x$, hence $y_m$ divides $\alpha$. So $\alpha(0) = \beta(0) = 0$, which is a contradiction.

For $F = x w y^p z^p$ we have $R = Q_1 x + Q_2 x w$, with $Q_1 = y_N^p z_N^p \psi_m / (M_m Y) \in (y_m z_m)$ and $Q_2 = y_N^2 z_N^2$, a monomial divisible by $y_m^2 z_m^2$. Then $0 = \alpha \pi + \beta Q_2 x$ with $\pi = 2x + Q_1 + Q_2 w$. The series $\pi$ has the linear part $2x$, so it is a regular parameter and a prime element. It is not associate to $x$, since $Q_1 + Q_2 w$ is not divisible by $x$, and it is not associate to $y_m$ or $z_m$. So $\pi$ divides $\beta$, and $\beta(0) = 0$. Also $y_m$ divides $\alpha \pi$, and $y_m$ does not divide $\pi$, so $y_m$ divides $\alpha$ and $\alpha(0) = 0$. This is a contradiction. $\square$

The lemma keeps the letters $y_m, z_m$ fixed. A change of the letters by units, such as $y_m \mapsto u y_m$, is not treated.

**Corollary 3.17.12.**

1. Let $p \ge 3$ and $g = x^2 y^{p-2} z^{p-2} + w y^p z^p$. Each word in the two charts with each chart an infinite number of times, with $a_m = 0$ and any $b_m \in K$, is a corner run in four variables with $\rho = 1$ at each point. If an infinite number of the $b_m$ are not $0$, then the run has an infinite number of nonzero translations in each free coordinate system, and no point of the run is cylindrical. So the answer to Question 3.17.7 is negative, also for points with $\deg_{x, w} g = 2 < p$, and the analogue of Theorem 3.15.17 is false for $n = 4$.
2. Let $g = x^2 y^{p-2} z^{p-2} + x w y^p z^p$ and take an infinite number of $b_m \ne 0$. Then at each point of the run, in the coordinates of the run, neither $\partial_x g_m$ nor $\partial_w g_m$ is a monomial times a unit. So the analogue of Proposition 3.15.10 is false.

Node: SG0000006T

*Proof.* Part 1 is Proposition 3.17.8, Lemma 3.17.6, part 1, and Lemma 3.17.11. Part 2. In the notation of the proof of Lemma 3.17.11, $\partial_w g_m = M_m^2 Y Q_2 x$ and $\partial_x g_m = M_m^2 Y \pi$, and $x$ and $\pi$ are not units. $\square$

Part 2 is a statement in the coordinates of the run. We do not claim that no derivation $\alpha \partial_x + \beta \partial_w$ of $g_m$ is a monomial times a unit in other free coordinates.

The runs of Proposition 3.17.8 are linear, with $\lambda = (1, 0)$, and they lie on the strict transforms of $V(x)$. Question 3.13.18 has a positive answer for them: the corner curves $V(x_m, w_m, y_m)$ and $V(x_m, w_m, z_m)$ lie in the corner surfaces $V(x_m, y_m)$ and $V(x_m, z_m)$, so they have $\nu^G \ge 1 = \rho$. So the counterexample is to the finiteness, and not to Question 3.13.18.

### Reduction to three variables

At a cylindrical point the second free coordinate is not seen by the function. So the run is a run in three variables, and the results of Sections 3.15 and 3.16 apply.

**Theorem 3.17.13.** Let $P_m$ be a point of a corner run in four variables, and let $(x', w')$ be a free coordinate system at $P_m$ such that the function of $P_m$ is congruent, modulo $p$-th powers, to a series $f \in K[[x', y_m, z_m]]$. Put $x'_m = x'$, $w'_m = w'$, $x'_{j+1} = x'_j / L_j - t'_j$ and $w'_{j+1} = w'_j / L_j - s'_j$, where $t'_j, s'_j \in K$ are the values of $x'_j / L_j$ and $w'_j / L_j$ at $P_{j+1}$. Then for each $j \ge m$:

1. $x'_j = L_j (x'_{j+1} + t'_j)$ and $w'_j = L_j (w'_{j+1} + s'_j)$, and $(x'_j, w'_j)$ is a free coordinate system at $P_j$.
2. The function of $P_j$ is congruent, modulo $p$-th powers, to a series $f_j \in K[[x'_j, y_j, z_j]]$, and $f_j$ is the function of the point $Q_j$ of the run in three variables of $f$ with the same charts and the translations $t'_j$.
3. $\rho(P_j) = \rho(Q_j)$. So $Q_m, Q_{m+1}, \dots$ is a corner run with free translations in the sense of Section 3.15, in the coordinates $(x'_j, y_j, z_j)$.
4. The $t'_j$ are $0$ for $j > J$ if and only if the points $P_j$, $j > J$, lie on the strict transforms of the regular hypersurface $V(x'_{J+1})$.

The translations $s'_j$ are arbitrary.

Node: SG0000006V

*Proof.* Part 1 is the definition and Lemma 3.17.2, part 2. Part 2. Assume that the function of $P_j$ is $f_j + h^p$ with $f_j \in K[[x'_j, y_j, z_j]]$. The function of $P_{j+1}$ is the cleaning of $L_j^{-p} \pi(f_j + h^p)$, and $\pi(h^p) = \pi(h)^p$. In the chart, $x'_j = L_j (x'_{j+1} + t'_j)$, and $y_j, z_j$ are monomials in $y_{j+1}, z_{j+1}$. So $L_j^{-p} \pi(f_j)$ is a series in $x'_{j+1}, y_{j+1}, z_{j+1}$ with no $w'_{j+1}$, after the removal of its Laurent $p$-th powers as in Lemma 3.15.1. This series is the transform of $f_j$ by the same chart in three variables with the translation $t'_j$. A Laurent series that is a $p$-th power and a power series is the $p$-th power of a power series. Induction on $j$ gives part 2.

Part 3. By Lemma 3.17.2, part 1, $\rho(P_j)$ and $x^r$ can be computed from $f_j$ in the coordinates $(x'_j, w'_j, y_j, z_j)$. Since $\partial_{w'} f_j = 0$, the ideal $\Theta(f_j)$ is generated by $\partial_{x'} f_j$, $y \partial_y f_j$ and $z \partial_z f_j$, which are the generators of the ideal $\Theta$ of $Q_j$ in three variables. The monomial $x^r$ is the largest monomial in $y, z$ that divides these three series, and this does not depend on the ring. The order of an ideal generated by series in $x', y, z$ is the least order of a generator, in both rings. So $\rho(P_j) = \rho(Q_j)$. The charts are the same, so both charts occur an infinite number of times, and $V(x'_j)$ is not in $\Delta$.

Part 4. As in the proof of Lemma 3.17.6, $P_{j+1}$ lies on the strict transform of $V(x'_j)$ if and only if $t'_j = 0$, and then $x'_{j+1}$ is an equation of this strict transform. Induction on $j$. $\square$

The results of Sections 3.15 and 3.16 are for points in $K[[y, z]][x]$, that is, for polynomials in $x$. The series $f$ of the theorem is a power series in $x'$. So the next corollary needs $f$ to be a polynomial in $x'$.

**Corollary 3.17.14.** Let $P_m$ be a cylindrical point as in Theorem 3.17.13, with $f \in K[[y_m, z_m]][x']$. Then only a finite number of the $t'_j$ are nonzero. For $j$ large, the corner surfaces $V(x'_j, y_j)$ and $V(x'_j, z_j)$ and the corner curves $V(x'_j, w'_j, y_j)$ and $V(x'_j, w'_j, z_j)$ have $\nu^G = d_j \ge \rho$. So Conjectures 3.17.18, 3.17.20 and 3.17.24 below hold for the run, and Question 3.13.18 has a positive answer for it.

Node: SG0000006W

*Proof.* By Theorem 3.17.13, part 3, the points $Q_j$ form a corner run with free translations of the point $f \in K[[y_m, z_m]][x']$. By Theorem 3.16.14, only a finite number of the $t'_j$ are nonzero, and after the last one, the corner curves $V(x'_j, y_j)$ and $V(x'_j, z_j)$ in three variables have $\nu^G = d_j \ge \rho$. The function of $P_j$ does not depend on $w'_j$, modulo $p$-th powers. So in the coordinates $(x'_j, w'_j, y_j, z_j)$, which are adapted to the four subvarieties, Lemma 3.13.1 gives the same order along $V(x'_j, y_j)$ in four variables as along $V(x'_j, y_j)$ in three variables, and the same order along $V(x'_j, w'_j, y_j)$, since the function does not contain $w'_j$. Definition 3.13.2 subtracts the same exponent $r_z$ or $r_y$ in each case. By Theorem 3.17.13, part 4, the points lie on the strict transforms of $V(x'_{J+1})$, with $J$ the last index with $t'_J \ne 0$. $\square$

### The class of one linear form

The simplest points that depend on both free coordinates are the functions of one linear form $\gamma_1 x + \gamma_2 w$. The idea is that after a finite number of steps the linear form is a monomial times a free coordinate, and then the point is cylindrical.

**Theorem 3.17.15.** Let $(\gamma_1, \gamma_2) \ne 0$ in $K[[y, z]]^2$, let $\Phi \in K[[y, z]][T]$, and let $g = \operatorname{cl} \Phi(\gamma_1 x + \gamma_2 w, y, z)$ be clean at $P_N$. Let $P_N, P_{N+1}, \dots$ be a corner run in four variables.

1. There is an $m_0$ such that each $P_m$ with $m \ge m_0$ is cylindrical, with $x' = u_1 x_m + u_2 w_m$ for some $u_1, u_2 \in K[[y_m, z_m]]$, at least one of them a unit, and the function of $P_m$ is congruent modulo $p$-th powers to a polynomial in $x'$ with coefficients in $K[[y_m, z_m]]$.
2. If $\Phi = c\, T + B_0$ with $c \ne 0$, that is, $g = \mu x + \nu w + B_0$ with $(\mu, \nu) \ne 0$ and $\mu, \nu, B_0 \in K[[y, z]]$, then no corner run in four variables from $P_N$ keeps $\rho \ge 1$.
3. There is a $J$ such that the points $P_j$, $j > J$, lie on the strict transforms of a regular hypersurface $V(x'_{J+1})$, with $x'_{J+1}$ a free coordinate. For $j$ large the corner surfaces and the corner curves of Corollary 3.17.14 have $\nu^G = d_j \ge \rho$.

Node: SG0000006X

*Proof.* Part 1. Let $S = \operatorname{supp} \gamma_1 \cup \operatorname{supp} \gamma_2 \subseteq \mathbb{N}^2$, in the exponents at $P_N$. Distinct points of $S$ have distinct values, so $S$ has one point $q_*$ of least value. Lemma 3.15.4 at the base point $P_N$ gives an $m_0$ such that, for $m \ge m_0$, each $q \in S \setminus \{q_*\}$ has an image $E_m(q)$ larger than $E_m(q_*)$ in both coordinates. So at $P_m$ we have $\gamma_i = \nu_m u_i$ with $\nu_m$ the monomial of exponent $E_m(q_*)$ and $u_i \in K[[y_m, z_m]]$, and $u_i(0)$ is the coefficient of $y^{q_*}$ in $\gamma_i$. At least one $u_i(0)$ is not $0$. Say $u_1(0) \ne 0$, else exchange $x$ and $w$, and put $x' = u_1 x_m + u_2 w_m$ and $w' = w_m$. This is a free coordinate system. By Lemma 3.17.1, part 1,
$$\gamma_1 x_N + \gamma_2 w_N = \sigma_m + \mu_m x', \qquad \sigma_m = \gamma_1 \varphi_m + \gamma_2 \psi_m \in K[[y_m, z_m]], \quad \mu_m = M_m \nu_m .$$
So $g(x_N, w_N) \equiv \Phi(\sigma_m + \mu_m x', y_N, z_N) =: \Phi_m(x')$ modulo $p$-th powers, and $\Phi_m$ is a polynomial in $x'$ with coefficients in $K[[y_m, z_m]]$. By Lemma 3.17.1, part 2, the function of $P_m$ is $M_m^{-p} g_m \equiv M_m^{-p} \Phi_m(x')$ modulo $p$-th powers of Laurent series. Let $\operatorname{cl}'$ be the cleaning in the coordinates $(x', w', y_m, z_m)$. Then $\operatorname{cl}'(M_m^{-p} g_m)$ is a power series, since $M_m^{-p} g_m$ is one, and it is equal to $\operatorname{cl}'(M_m^{-p} \Phi_m(x'))$, which is a polynomial in $x'$ with Laurent coefficients and no $w'$. So its coefficients are power series, and $P_m$ is cylindrical.

Part 2. By part 1 and Theorem 3.17.13, the run from $P_{m_0}$ gives a corner run with free translations in three variables of the point
$$f = M^{-p} \mu_m x' + \operatorname{cl}'\bigl(M^{-p} (\sigma_m + B_0)\bigr), \qquad M = M_{m_0}, \ m = m_0,$$
with $\rho \ge 1$ at each point. The coefficient $M^{-p} \mu_m$ is a Laurent monomial, and it is a monomial with nonnegative exponents, since it is the coefficient of $x'$ in the power series $f$. So $f$ has the form $\mu' x' + B'_0$ of Theorem 3.15.16, with $\mu'$ a constant times a monomial. That theorem says that no corner run with free translations from this point keeps $\rho \ge 1$. This is a contradiction.

Part 3. By part 1 the points $P_m$, $m \ge m_0$, are cylindrical with $f$ a polynomial in $x'$. Corollary 3.17.14 gives the claim, and Theorem 3.17.13, part 4, gives the hypersurface. $\square$

For $\deg_T \Phi < p$, part 3 also follows from Theorem 3.15.17, and for $\Phi = B_1 T^p + B_0$ it also follows from Theorem 3.13.27, since then $\Phi_m(x') = B_1 \mu_m^p x'^p + B_1 \sigma_m^p + B_0$. If $\Phi$ has no term with $T$, then $g = B_0$, and Proposition 3.17.3 at $P_N$ gives $\rho = 0$ later, so there is no run.

**Remark 3.17.16.** Part 2 extends Theorem 3.15.16 in two ways: there are two free coordinates, and $\mu, \nu$ are any series, not monomials. The second extension gives a new statement also for $n = 3$: for $g = \mu x + B_0$ with any nonzero $\mu \in K[[y, z]]$, no corner run with free translations keeps $\rho \ge 1$. The proof is the case $\gamma_2 = 0$, where the dominance at $P_{m_0}$ makes $\mu$ a monomial times a unit, and the unit goes into the free coordinate. Part 1 is where $n = 4$ differs from $n = 3$ in this class. For a form of degree $2$ or more in $x, w$ there is no such statement, by Example 3.17.9.

**Corollary 3.17.17.** Let $g = B_1 x^p + B_2 w^p + B_0$ be clean, with $B_i \in K[[y, z]]$. Write $B_i = \sum_c y^{c_1} z^{c_2} \beta_{i, c}^p$ over $c \in \{0, \dots, p - 1\}^2$, with $\beta_{i, c} \in K[[y, z]]$. If the vectors $(\beta_{1, c}, \beta_{2, c})$ span a space of dimension at most $1$ over the field of fractions of $K[[y, z]]$, then the conclusion of Theorem 3.17.15, part 3, holds for each corner run in four variables from $P_N$.

Node: SG0000006Y

*Proof.* If all the vectors are $0$, then $g = B_0$, and Proposition 3.17.3 at $P_N$ gives $\rho = 0$ later, so there is no run. If not, then since $K[[y, z]]$ is factorial there is a vector $(\gamma_1, \gamma_2)$ with coprime entries such that $(\beta_{1, c}, \beta_{2, c}) = \lambda_c (\gamma_1, \gamma_2)$ for each $c$, with $\lambda_c \in K[[y, z]]$, since a denominator of $\lambda_c$ would divide both $\gamma_i$. Then $B_i = \gamma_i^p B$ with $B = \sum_c y^{c_1} z^{c_2} \lambda_c^p$, and $g = B (\gamma_1 x + \gamma_2 w)^p + B_0$. This is the case $\Phi = B T^p + B_0$ of Theorem 3.17.15. $\square$

If the rank is $2$, for example for $g = y x^p + z w^p + B_0$, the proof of Theorem 3.13.27 does not apply, since it compares the value of $g$ at the translations with one coefficient. Theorem 3.17.29 below treats this example by another method.

### Corner surfaces and corner curves

The runs of Proposition 3.17.8 have an infinite number of nonzero translations, but they lie on the strict transforms of a hypersurface. This suggests the following form of the finiteness.

**Conjecture 3.17.18 (L).** Let $g \in K[[y, z]][x, w]$ be clean, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables. Then there are a $J$ and a free coordinate system $(x', w')$ at $P_J$ such that the translations of $x'$ are $0$ after $J$. Equivalently, the points $P_j$, $j > J$, lie on the strict transforms of the regular hypersurface $V(x')$.

Node: SG0000006Z

The two forms are equivalent by the fact on hypersurfaces in the proof of Lemma 3.17.6. Conjecture L holds for the runs of Proposition 3.17.8 with $x' = x$, in the class of Theorem 3.17.15, at the cylindrical points of Corollary 3.17.14, and for $\deg_{x, w} g < p$ (Theorem 3.17.33 and Corollary 3.18.18). For $n = 3$ it is the finiteness itself, since then the hypersurface $V(x')$ is a surface that contains the corner run.

Conjecture L alone does not give Question 3.13.18. Take Example 3.13.15 with a fourth variable, $g = x^p y z + y^{p+2} z^{p+1}$ with the translations in $w$. The run lies on $V(x)$, but $\nu^G_{V(x)} = 0$. So a hypersurface that contains the run gives no bound for $\nu^G$ along it. What can give the bound are the surfaces $V(x', y)$ and $V(x', z)$ in the components of $\Delta$, and the curves in them. In this example the corner surfaces $V(x, y)$ and $V(x, z)$ have $\nu^G \ge p = \rho$.

The next lemma bounds $\nu^G$ along the corner surfaces through the initial form of $G$. It is the key to the counterexamples to Conjecture L+.

**Lemma 3.17.19.** Let $g = y^{r_y} z^{r_z} G$, and let $(X, W, y, z)$ be a regular system of parameters at the point.

1. Let $D$ be a derivation of $K[[x, w, y, z]]$ with $D(y) = D(z) = 0$. Then $\nu^G_{V(X, z)} \le 1 + \operatorname{ord}_{V(X, z)}(D G)$.
2. Assume that $\operatorname{in} G = h(x, w)$ is a nonzero binary form of degree $d$ with $1 \le d < p$. Let $\ell(x, w)$ be the part in $x, w$ of the linear part of $X$, and let $\operatorname{mult}_\ell h$ be the largest $m$ with $\ell^m \mid h$. Then $\nu^G_{V(X, z)} \le \max(1, \operatorname{mult}_\ell h)$.

The same holds for $V(X, y)$.

Node: SG00000070

*Proof.* Part 1 is the proof of Lemma 3.13.14 with one derivation. Let $Z = V(X, z)$. Only the component $V(z)$ of $\Delta$ contains $Z$, so the number subtracted in Definition 3.13.2 is $r_z$. Let $\nu = \nu^G_Z$ and take $h$ with $\operatorname{ord}_Z(g + h^p) = \nu + r_z$. The derivation lowers $\operatorname{ord}_Z$ by at most $1$, by the Leibniz rule, and $D(h^p) = 0$. So $\operatorname{ord}_Z D(g) \ge \nu + r_z - 1$. Since $D(y) = D(z) = 0$, $D(g) = y^{r_y} z^{r_z} D(G)$. The ideal of $Z$ is prime and $Z$ is regular, so $\operatorname{ord}_Z$ is a valuation, with $\operatorname{ord}_Z(z) = 1$ and $\operatorname{ord}_Z(y) = 0$. So $r_z + \operatorname{ord}_Z D(G) \ge \nu + r_z - 1$.

Part 2. Since $(X, W, y, z)$ is a regular system, $\ell \ne 0$. We first show: if a series $f$ has a binary initial form $\operatorname{in} f = q(x, w)$, then $\operatorname{ord}_Z f \le \operatorname{mult}_\ell q$. Let $N = \operatorname{ord}_Z f$, so $f \in (X, z)^N$. Put $y = z = 0$. Then $f(x, w, 0, 0) \in (\bar X)^N$ in $K[[x, w]]$, with $\bar X = X(x, w, 0, 0) = \ell + $ terms of higher degree. The initial form of $f(x, w, 0, 0)$ is $q$, since $q$ has no $y$ and $z$, and the initial form of an element of $(\bar X)^N$ is divisible by $\ell^N$. So $\ell^N \mid q$.

Let $m = \operatorname{mult}_\ell h$, and write $h = \ell^m q$ with $\ell \nmid q$. If $m \ge 1$, take a constant derivation $D = \alpha \partial_x + \beta \partial_w$ with $D(\ell) = 1$. Then $D h = \ell^{m-1} (m q + \ell D q)$, and $p \nmid m$ since $m \le d < p$. So $D h \ne 0$, $\operatorname{mult}_\ell D h = m - 1$, and $\operatorname{in}(D G) = D h$ is binary. Part 1 and the claim give $\nu^G_Z \le 1 + (m - 1) = m$. If $m = 0$, the Euler identity $x h_x + w h_w = d h$ with $p \nmid d$ shows that $\ell$ does not divide both $h_x$ and $h_w$. Take $D \in \{\partial_x, \partial_w\}$ with $\ell \nmid D h$. Then $\operatorname{in}(D G) = D h$, $\operatorname{ord}_Z D G = 0$ by the claim, and part 1 gives $\nu^G_Z \le 1$. The case $V(X, y)$ is the same with $y$ and $z$ exchanged. $\square$

So if the initial form $h$ has no linear factor of a high multiplicity, then no corner surface can have a large $\nu^G$. This is a restriction on the surfaces, and it does not depend on the translations. The next conjecture was proposed as the form of Conjecture L that gives Question 3.13.18.

**Conjecture 3.17.20 (L+).** Let $g \in K[[y, z]][x, w]$ be clean, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables. Then there are a $J$ and a free coordinate system $(x', w')$ at $P_J$ such that the translations of $x'$ are $0$ after $J$, and for $m$ large the corner surfaces $V(x'_m, y_m)$ and $V(x'_m, z_m)$ have $\nu^G(P_m) \ge \rho$.

Node: SG00000071

The conjecture is false. In the counterexample, the initial form is a product of three distinct lines, so by Lemma 3.17.19 each corner surface has $\nu^G \le 1$, and $\rho = 2$.

**Theorem 3.17.21.** Let $p \ge 5$ and $g = x w (x + w)\, y^{p-3} z^{p-3}$.

1. The point is clean, $r = (p - 3, p - 3)$, $G = x w (x + w)$, $d = 3$ and $\rho = 2$, and the point has type $1$.
2. The $y$-chart and the $z$-chart with the translation $(0, 0)$ send $g$ to $g$, and no other translation keeps $\rho$. So each word in the two charts with each chart an infinite number of times is a corner run in four variables with $\rho = 2$, and all its translations are $0$.
3. At each point of the run, each free coordinate $X$ has $\nu^G \le 1$ on $V(X, y)$ and on $V(X, z)$, whatever its translations. So Conjecture L+ is false.
4. The corner curves $V(x, w, y)$ and $V(x, w, z)$ and the surface $V(x, w)$ have $\nu^G = 3 \ge \rho$ at each point of the run.

Node: SG00000072

*Proof.* Part 1. The monomials $x^2 w y^{p-3} z^{p-3}$ and $x w^2 y^{p-3} z^{p-3}$ have an exponent $1$ in $w$ or in $x$, so $g$ is clean. Also $\operatorname{ord} g = 2p - 3 \ge p$. The derivatives $G_x = 2 x w + w^2$ and $G_w = x^2 + 2 x w$ have the order $2$, and $r_y G + y G_y = (p - 3) G$ has the order $3$, so $\rho = 2 = d - 1$, and the type is $1$.

Part 2. In the $y$-chart with the translation $(0, 0)$ we have $x = y x'$, $w = y w'$ and $z = y z'$, so
$$\pi(g) = y^3 x' w' (x' + w') \cdot y^{p-3} \cdot y^{p-3} z'^{p-3}, \qquad y^{-p} \pi(g) = x' w' (x' + w')\, y^{p-3} z'^{p-3}.$$
This is $g$ in the new coordinates. The $z$-chart is the same with $y$ and $z$ exchanged. The initial form $h = x w (x + w)$ is binary of degree $3 < p$ and it is not a power of a line, so by Proposition 3.17.30 below no nonzero translation keeps $\rho$.

Part 3. At each point of the run the function is $g$ in the coordinates of the run. A linear form $\ell$ that divides $h$ is proportional to $x$, $w$ or $x + w$, and it has the multiplicity $1$. Each other $\ell$ has the multiplicity $0$. So Lemma 3.17.19 gives $\nu^G \le 1 < 2 = \rho$ on each corner surface through the point. In this run all translations are $0$, so each free coordinate has translations $0$ from some point on, and each choice fails.

Part 4. The curve $C = V(x, w, z)$ lies only in the component $V(z)$ of $\Delta$, so the number subtracted is $r_z = p - 3$. In the coordinates $(x, w, y, z)$, which are adapted to $C$ and $\Delta$, the point $g$ is clean, so Lemma 3.13.1 gives $\nu^G_C = \operatorname{ord}_{(x, w, z)} g - (p - 3) = 3$. The curve $V(x, w, y)$ is the same. The surface $V(x, w)$ is in no component of $\Delta$, and $\operatorname{ord}_{(x, w)} g = 3$. $\square$

The run of Theorem 3.17.21 is an origin run, and a cycle of the kind of Remark 3.12.3. It lies on the strict transforms of the surface $V(x, w)$ with $\nu^G = 3 \ge \rho$. So Question 3.13.18 and Question 3.13.13 both have a positive answer for it. A second counterexample shows that a power of a line in the initial form is not enough for Conjecture L+.

**Example 3.17.22.** Let $p \ge 5$ and $g = y^{p-4} z^{p-4} (x^4 + y z w^3)$. Then $G = x^4 + y z w^3$, $d = 4$ and $\rho = 3$. Both charts with the translation $(0, 0)$ send $g$ to $g$, so each word in the two charts with each chart an infinite number of times is a corner run in four variables. Each corner surface $V(X, y)$ or $V(X, z)$ through a point of the run has $\nu^G \le 2 < \rho$, although $\operatorname{in} G = x^4$. The corner curves $V(x, w, y)$ and $V(x, w, z)$ have $\nu^G = 4 \ge \rho$.

Node: SG00000073

*Proof.* The point is clean, since $x^4$ has the exponent $4$ and $w^3$ has the exponent $3$, and $\operatorname{ord} g = 2p - 4 \ge p$. We have $G_x = 4 x^3$, $G_w = 3 y z w^2$ and $r_y G + y G_y = -4 G + y z w^3 = -4 x^4 - 3 y z w^3$, and the same for $z$. So $\rho = 3$. In the $y$-chart, $x^4 \mapsto y^4 x'^4$ and $y z w^3 \mapsto y^5 z' w'^3$, so $G \mapsto y^4 (x'^4 + y z' w'^3)$, and with the factor $y^{p-4} \cdot y^{p-4} z'^{p-4}$ and the division by $y^p$ we get $g$ again. The $z$-chart is the same.

Let $X$ be a free coordinate with the linear part $\ell$ in $x, w$. If $\ell$ is not proportional to $x$, then $\operatorname{mult}_\ell x^4 = 0$, and Lemma 3.17.19 gives $\nu^G \le 1$. If $\ell$ is proportional to $x$, take $D = \partial_w$ in Lemma 3.17.19, part 1. Then $D G = 3 y z w^2$. On $Z = V(X, z)$ we have $\operatorname{ord}_Z z = 1$, $\operatorname{ord}_Z y = 0$ and $\operatorname{ord}_Z w = 0$, since the linear part of $w$ is not in the span of the linear parts of $X$ and $z$. So $\operatorname{ord}_Z D G = 1$ and $\nu^G_Z \le 2$. The case $V(X, y)$ is the same. The curve $C = V(x, w, y)$ has $\operatorname{ord}_C g = (p - 4) + 4$, and the number subtracted is $r_y = p - 4$, so $\nu^G_C = 4$ by Lemma 3.13.1. $\square$

Lemma 3.17.19 gives a necessary condition for Conjecture L+ in the origin runs.

**Corollary 3.17.23.** Let $P_N, P_{N+1}, \dots$ be an origin run of a clean $g \in K[[y, z]][x, w]$ in which both charts occur an infinite number of times. Let $h$ be the initial form of $G_m$ for $m$ large, which is a binary form by Theorem 3.14.7, part 2, and assume that $h$ has the degree $d$ with $3 \le d < p$ and that the type is $1$. If a free coordinate $X$ gives corner surfaces $V(X_m, y_m)$ and $V(X_m, z_m)$ with $\nu^G \ge \rho$ for $m$ large, then $h = c \ell^d$ or $h = c \ell^{d-1} \ell'$ for some linear forms $\ell, \ell'$.

Node: SG00000074

*Proof.* Here $\rho = d - 1 \ge 2$. Lemma 3.17.19 gives $\max(1, \operatorname{mult}_\ell h) \ge d - 1 \ge 2$ for the linear part $\ell$ of $X_m$, so $\operatorname{mult}_\ell h \ge d - 1$. $\square$

The converse is false, by Example 3.17.22. In the two counterexamples the corner curves have $\nu^G \ge \rho$. For the origin runs this is Theorem 3.14.7, part 3: the curves $C_y = V(x, w, z)$ and $C_z = V(x, w, y)$ have $\nu^G = d_m \ge \rho$. This gives the following form.

**Conjecture 3.17.24 (L°).** Let $g \in K[[y, z]][x, w]$ be clean, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables. Then there are a $J$ and a free coordinate system $(x', w')$ at $P_J$ such that the translations of $x'$ are $0$ after $J$, and for $m$ large the corner curves $V(x'_m, w'_m, y_m)$ and $V(x'_m, w'_m, z_m)$ have $\nu^G(P_m) \ge \rho$.

Node: SG00000075

The curves $V(x'_m, w'_m, y_m)$ and $V(x'_m, w'_m, z_m)$ are regular and lie in the components $V(y_m)$ and $V(z_m)$ of $\Delta$. So Conjecture L° implies a positive answer to Question 3.13.18 for the corner runs in four variables. It holds for the origin runs (Theorem 3.14.7), at the cylindrical points of Corollary 3.17.14, for the runs of Proposition 3.17.8, for Theorem 3.17.21 and for Example 3.17.22. By Corollary 3.18.18 it holds for each corner run with $\deg_{x, w} g < p$.

### Points of type 0 and the change of letters

A corner run uses each letter an infinite number of times, so it changes the letter an infinite number of times. Here we show that a point of type $0$ with $\rho < p$ cannot be the point before a change of the letter. The tool is the directrix condition of Theorem 3.7.1. By Lemma 3.10.1, $\sigma = d$ for a clean point, so part 1 of that theorem is the case of type $0$ ($\rho = d$), and part 2 is the case of type $1$ ($\rho = d - 1$). The chart vector of a $y$-step with the translation $(a, b)$ is $v = (a, b, 1, 0)$, and for a $z$-step it is $v = (a, b, 0, 1)$. We write $H_y = r_y G + y G_y$ and $H_z = r_z G + z G_z$. They are in $\widetilde\Theta_0(G)$.

**Lemma 3.17.25.** Let $g = y^{r_y} z^{r_z} G$ be clean with $\operatorname{ord} g \ge p$, and assume that the point has type $0$ with $1 \le \rho = d < p$. If a $y$-step with any translation keeps $\rho$, then $\operatorname{in} G = c z^d$ with $c \ne 0$. If a $z$-step keeps $\rho$, then $\operatorname{in} G = c y^d$.

Node: SG00000076

*Proof.* By Theorem 3.1.4, part 3, type $0$ means $\partial_x \operatorname{in} G = \partial_w \operatorname{in} G = 0$, so each exponent of $x$ and $w$ in $\operatorname{in} G$ is divisible by $p$. Since $d < p$, these exponents are $0$, and $\operatorname{in} G = \sum c_{\alpha\beta} y^\alpha z^\beta$ over $\alpha + \beta = d$. The parts of degree $d$ of $H_y$ and $H_z$ are
$$\textstyle\sum (r_y + \alpha) c_{\alpha\beta}\, y^\alpha z^\beta, \qquad \sum (r_z + \beta) c_{\alpha\beta}\, y^\alpha z^\beta.$$
If one of them is not $0$, then the element has the order $d = \rho$, and Theorem 3.7.1, part 1, gives $v = (a, b, 1, 0) \in T(f)$ for this part $f$. A form $f \in K[y, z]$ with $f(y + s, z) = f(y, z)$ has $\partial_y f = 0$, so its exponents of $y$ are divisible by $p$, and since its degree is $d < p$, $f \in K z^d$. So in both cases, $(r_y + \alpha) c_{\alpha\beta} = 0$ and $(r_z + \beta) c_{\alpha\beta} = 0$ for each $\alpha \ge 1$. If $c_{\alpha\beta} \ne 0$ with $\alpha \ge 1$, then $p \mid r_y + \alpha$ and $p \mid r_z + \beta$, so the monomial $y^{r_y + \alpha} z^{r_z + \beta}$ of $g$ is a $p$-th power. This is not possible, since $g$ is clean. So $\operatorname{in} G = c_{0d} z^d$, and $c_{0d} \ne 0$. $\square$

**Lemma 3.17.26.** Let $g \in K[[y, z]][x^p, w^p]$ be clean with $\rho \ge 1$. If a $y$-step keeps $\rho$, then each monomial of $\operatorname{in} G$ has its exponent of $y$ divisible by $p$. The same holds for $z$ and a $z$-step.

Node: SG00000077

*Proof.* Here $G_x = G_w = 0$, so the type is $0$. Let $H$ be $H_y$ or $H_z$, and let $f$ be its part of degree $d$. Its monomials are the monomials $c\, x^{pi} w^{pl} y^\alpha z^\beta$ of $\operatorname{in} G$, with the coefficients $(r_y + \alpha) c$ or $(r_z + \beta) c$. If $f \ne 0$, Theorem 3.7.1, part 1, gives $f(x + s a, w + s b, y + s, z) = f$. The coefficient of $s$ is $a f_x + b f_w + f_y = f_y$, since $f_x = f_w = 0$. So $\alpha (r_y + \alpha) c = 0$ and $\alpha (r_z + \beta) c = 0$ for each monomial, and this also holds if $f = 0$. If a monomial of $\operatorname{in} G$ has $p \nmid \alpha$, then $p \mid r_y + \alpha$ and $p \mid r_z + \beta$, and the monomial $x^{pi} w^{pl} y^{r_y + \alpha} z^{r_z + \beta}$ of $g$ is a $p$-th power. This is not possible. $\square$

**Theorem 3.17.27.** Let $g$ be clean with $\operatorname{ord} g \ge p$ at a point $P$ of type $0$ with $1 \le \rho = d < p$. Then a $y$-step from $P$ to $P'$ followed by a $z$-step from $P'$, both keeping $\rho$, is not possible. The same holds with $y$ and $z$ exchanged.

Node: SG00000078

The idea is that Lemma 3.17.25 at $P$ gives $\operatorname{in} G = c z^d$, and this form survives the $y$-step. At $P'$ the same lemma for the $z$-step needs $\operatorname{in} G' = c'' y^d$, and the two forms are not compatible.

*Proof.* By Lemma 3.17.25, $\operatorname{in} G = c z^d$. In the chart, a monomial of degree $e$ in $(x, w, y, z)$ becomes $y^e$ times a series, so
$$\pi(G) = y^d (c z'^d + y U), \qquad g' = y^{-p} \pi(g) = y^{s} z'^{r_z} (c z'^d + y U), \quad s = r_y + r_z + d - p \ge 0.$$
The only monomial of $g'$ with the exponent $s$ of $y$ is $c\, y^s z'^{r_z + d}$. It is not a $p$-th power: if $p \mid s$ and $p \mid r_z + d$, then $p \mid r_y$, and the monomial $y^{r_y} z^{r_z + d}$ of $g$ would be a $p$-th power. So it survives the cleaning, and the clean part $g'_c$ has the monomial factor $y^s z'^{r_z + e}$ for some $0 \le e \le d$, since all monomials of $g'$ are divisible by $z'^{r_z}$. Then $G'_c \equiv c\, z'^{d - e}$ modulo $y$. So $d' = \operatorname{ord} G'_c \le d - e$. The step keeps $\rho$, so $d' \ge \rho = d$ by Theorem 3.1.4. Hence $e = 0$ and $d' = d = \rho$, the point $P'$ has type $0$ with $\rho < p$, and the part of degree $d$ of $G'_c$ is congruent to $c z'^d$ modulo $y$. Lemma 3.17.25 at $P'$ for the $z$-step gives $\operatorname{in} G'_c = c'' y^d$, which is $0$ modulo $y$. This contradicts $c \ne 0$. $\square$

**Corollary 3.17.28.** Let $P_N, P_{N+1}, \dots$ be a corner run in four variables with $1 \le \rho < p$. If the step out of $P_m$ and the step out of $P_{m+1}$ use different letters, then $P_m$ has type $1$, so $d = \rho + 1 \le p$ at $P_m$.

Node: SG00000079

*Proof.* If $P_m$ has type $0$, then $d = \rho < p$ at $P_m$, and Theorem 3.17.27 applies to the two steps. $\square$

The point $P_{m+1}$ reached by the step can have type $0$. The tests found such points in several classes.

**Theorem 3.17.29.**

1. Let $g \in K[[y, z]][x^p, w^p]$ be clean with $\operatorname{ord} g \ge p$ and $1 \le \rho < p$. Then no step that changes the letter keeps $\rho$, so no corner run in four variables from $g$ exists.
2. Let $g = y^{pA} z^{pB} (y x^p + z w^p + B_0)$ be clean with $\operatorname{ord} g \ge p$, $A, B \ge 0$ and $B_0 \in K[[y, z]]$. Then no corner run in four variables from $g$ exists.

Node: SG0000007A

*Proof.* Part 1. The class is kept by the steps: $\pi(x^p) = L^p (x' + a)^p = L^p (x'^p + a^p)$, $\pi(w^p)$ is the same, the coefficients go to $K[[y', z']]$, and the cleaning and the division by $L^p$ keep the class. Each point of the class has type $0$, since $G_x = G_w = 0$. So $d = \rho < p$ at each point, and Theorem 3.17.27 applies at the first change of the letter.

Part 2. Here $r = (pA, pB)$ and $G = y x^p + z w^p + B_0$, since $z w^p$ has no $y$ and $y x^p$ has no $z$. By symmetry the first step is a $y$-step. If $\operatorname{ord} B_0 \ge p + 1$, then $\operatorname{in} G$ contains $y x^p$, with the exponent $1$ of $y$, and Lemma 3.17.26 says that the step does not keep $\rho$. If $\operatorname{ord} B_0 = p$, then $\operatorname{in} G$ is the part of degree $p$ of $B_0$, and Lemma 3.17.26 gives $\operatorname{in} G \in K y^p + K z^p$. These monomials times $y^{pA} z^{pB}$ are $p$-th powers, which is not possible for a clean $g$. If $\operatorname{ord} B_0 < p$, then $d = \operatorname{ord} B_0 < p$, the type is $0$, so $\rho = d < p$, and part 1 applies. For $A = B = 0$ this last case is outside the regime $\operatorname{ord} g \ge p$. $\square$

Part 2 is the first case of rank $2$ of Corollary 3.17.17. The class $B_1 x^p + B_2 w^p + B_0$ of rank $2$ with $\rho \ge p$ was left open here, and Corollary 3.18.38 settles it. There $d = \rho \ge p$, Lemma 3.17.25 does not apply, and the tests found deep walks.

### Binary initial forms

Now let the initial form of $G$ be a binary form $h(x, w)$ of degree less than $p$. Then the directrix condition of Theorem 3.7.1, part 2, allows a nonzero translation only along a line of $h$, and only if $h$ is a power of this line.

**Proposition 3.17.30.** Let $g = y^{r_y} z^{r_z} G$ be clean with $\operatorname{ord} g \ge p$, and let $\operatorname{in} G = h(x, w)$ be a binary form of degree $d$ with $2 \le d < p$. If a $y$-step or a $z$-step with the translation $u = (a, b) \ne 0$ keeps $\rho$, then $h = c \ell^d$ with $\ell = b x - a w$. In particular $\ell(u) = 0$.

Node: SG0000007B

*Proof.* By the Euler identity $x h_x + w h_w = d h \ne 0$, so $h_x$ or $h_w$ is not $0$. So the type is $1$ by Theorem 3.1.4, part 3, and $\rho = d - 1$. The generators $G_x$ and $G_w$ of $\widetilde\Theta(G)$ have the initial forms $h_x$ and $h_w$ if these are not $0$, of the order $\rho$. Theorem 3.7.1, part 2, gives $v \in T(h_x)$ and $v \in T(h_w)$ for the nonzero ones. Since $h_x$ and $h_w$ do not contain $y$ and $z$, this says $h_x(x + s a, w + s b) = h_x(x, w)$, and the coefficient of $s$ gives $D_u h_x = 0$, with $D_u = a \partial_x + b \partial_w$. The same holds for $h_w$. So $\partial_x(D_u h) = \partial_w(D_u h) = 0$. Now $D_u h$ is a form of degree $d - 1$ with $1 \le d - 1 < p$, so the Euler identity gives $D_u h = 0$. Choose a linear form $m$ with $D_u m = 1$. Since $D_u \ell = a b - b a = 0$, the forms $(\ell, m)$ are coordinates and $D_u = \partial_m$ in them. So $\partial_m h = 0$ with $\deg h < p$, and $h \in K[\ell]$. $\square$

The proposition does not extend to $d = p + 1$. For $p = 2$ the form $h = x^2 w$ has $D_u h = b x^2$ for $u = (0, b)$, whose two derivatives are $0$, and a step with $u = (0, b)$, $b \ne 0$, keeps $\rho$ at a point of a corner run with $\operatorname{in} G = x^2 w$ (Example 3.19.15 and Corollary 3.19.16). The Euler identity is the step that needs $d < p$. Proposition 3.19.19 gives the list of the forms $h$ in each degree.

The next lemma says that a power of a line stays in the initial form after a step along this line.

**Lemma 3.17.31.** In the setting of Proposition 3.17.30, let $h = c \ell^d$ and let the translation $u$ satisfy $\ell(u) = 0$, or $u = 0$. Let $P'$ be the next point. Then $G'_c \equiv c\, \ell(x', w')^d$ modulo $y$ after a $y$-step, and modulo $z$ after a $z$-step. If $\operatorname{in} G'_c$ is binary, then $\operatorname{in} G'_c = c\, \ell(x', w')^d$.

Node: SG0000007C

*Proof.* For a $y$-step, $\ell(x, w) = y (\ell(x', w') + \ell(a, b)) = y\, \ell(x', w')$, so $\pi(G) = y^d (c\, \ell(x', w')^d + y U)$ and $g' = y^s z'^{r_z} (c\, \ell(x', w')^d + y U)$ with $s = r_y + r_z + d - p$. The monomials of $y^s z'^{r_z} \ell(x', w')^d$ have an exponent of $x'$ or $w'$ between $1$ and $d$, so they are not $p$-th powers, they survive the cleaning, and they are the only monomials with the exponent $s$ of $y$. So the monomial factor of $g'_c$ is $y^s z'^{r_z}$ and $G'_c \equiv c\, \ell(x', w')^d$ modulo $y$. If $\operatorname{in} G'_c$ is binary of degree $d'$, then it is the part of degree $d'$ of $G'_c$ modulo $y$, so it is the part of degree $d'$ of $c\, \ell(x', w')^d$. This is not $0$ only for $d' = d$. The $z$-step is the same. $\square$

So along a run with binary initial forms of degree less than $p$, the line $\ell$ is fixed in the coordinates of the run after the first nonzero translation. To use this along a whole run we need the initial forms to be binary from some point on. We could not prove this, and we state it as a hypothesis.

**Hypothesis 3.17.32 (H1).** Let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g < p$, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables. Then $\operatorname{in} G_m \in K[x_m, w_m]$ for $m$ large.

Node: SG0000007D

For a run with only a finite number of nonzero translations, the hypothesis holds by Theorem 3.14.7, part 2, since the run is an origin run from some point on. So it was open only for the runs with an infinite number of nonzero translations. Corollary 3.17.28 gives a first step: the points before a change of the letter have type $1$. Corollary 3.18.18 proves the hypothesis for each corner run with $\deg_{x, w} g < p$. The form $\operatorname{in} G_m \in K[x'_m]$ in a free coordinate with the translations $0$ is false for $\deg_{x, w} g \ge p + 1$ (Corollary 3.19.16), and the binary form in each degree is Conjecture 3.19.22.

**Theorem 3.17.33.** Let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g < p$, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables. Then one of the following holds.

1. The run is an origin run from some point on. Then Conjecture 3.17.18 and Conjecture 3.17.24 hold for it, by Theorem 3.14.7.
2. There are a linear form $\ell$ and an $m_1$ such that $\operatorname{in} G_m = c_m \ell(x_m, w_m)^d$ and $\ell(a_m, b_m) = 0$ for each $m \ge m_1$. Then the points $P_m$, $m \ge m_1$, lie on the strict transforms of $V(\ell(x_{m_1}, w_{m_1}))$, so Conjecture 3.17.18 holds for the run.

In both cases the run is linear.

Node: SG0000007E

*Proof.* A step sends $x^i w^l$ to $L^{i + l} (x' + a)^i (w' + b)^l$, so $\deg_{x, w}$ does not go up, and the cleaning only removes monomials. So $\deg_{x, w} g_m < p$ for each $m$. For $m$ large, $h_m = \operatorname{in} G_m$ is binary by Hypothesis 3.17.32, which holds by Corollary 3.18.18, so its degree $d$ is less than $p$, the type is $1$ by the Euler identity, and $d = \rho + 1 \ge 2$. If all the translations after some point are $0$, we are in case 1. If not, let $m_1$ be the first index after this point with $(a_{m_1}, b_{m_1}) \ne 0$. Proposition 3.17.30 gives $h_{m_1} = c \ell^d$ with $\ell(a_{m_1}, b_{m_1}) = 0$, and Lemma 3.17.31 with induction gives $h_m = c_m \ell^d$ for each $m \ge m_1$. For a later nonzero translation, Proposition 3.17.30 gives $h_m = c' \ell'^d$ with $\ell'$ zero on it, and the unique factorization of the binary forms gives $\ell' \in K^* \ell$. So $\ell(a_m, b_m) = 0$ for each $m \ge m_1$. By Lemma 3.17.2, part 3, these are the translations of the free coordinate $\ell(x, w)$, and the proof of Lemma 3.17.6 gives the hypersurface. $\square$

The proof answers two questions for this class. The first asks whether each corner run in four variables is linear in the coordinates of $P_N$ (Question L'). A linear run satisfies Conjecture L by Lemma 3.17.2, part 3. The second asks whether, in a run with an infinite number of nonzero translations, the initial form of $G_m$ is $c\, \ell^d$ for $m$ large with the late translations in the kernel of $\ell$ (Question H). For Proposition 3.17.8, $h = x^2$ and the translations are in the kernel of $x$. Theorem 3.17.33 gives a positive answer to both questions for $\deg_{x, w} g < p$. In case 2 the corner surfaces $V(\ell, y)$ and $V(\ell, z)$ can have $\nu^G$ up to $d$ by Lemma 3.17.19, and in all the tests both they and the corner curves had $\nu^G \ge \rho$. The proof here does not give Conjecture L° in case 2. Theorem 3.18.6 and Corollary 3.18.7 prove it: the corner curves have $\nu^G = d = \rho + 1$ for $m$ large.

### Remarks

**Remark 3.17.34 (the limit change and Conjecture T).** One could try to remove the translations by the change $x \mapsto x - \varphi_\infty$, $w \mapsto w - \psi_\infty$. By Lemma 3.15.6, part 3, if an infinite number of the $a_j$ are not $0$, then $\varphi_\infty$ is not in $\hat H$, so this is not a change of coordinates over $K[[y_N, z_N]]$ or its completion. Theorem 3.17.33 uses the directrix in place of a limit. For a planar run, note 38 of the research notes states a conjecture T: for each nonzero $f \in \hat H[X, W]$ the value $v(f(\varphi_m, \psi_m))$ is constant for $m$ large, and $f(\varphi_\infty, \psi_\infty) \ne 0$. One direction at a time this is the transcendental type of Proposition 3.17.4. The proof of Proposition 3.15.7 factors $f$ into linear factors, and this has no analogue in two variables. The theory of Kaplansky (Maximal fields with valuations, Duke Math. J. 9 (1942)), the stability theorem [Kuh10, Theorem 1.1], the approximation types of F.-V. Kuhlmann (Math. Z. 301 (2022)), the results on algebraic independence of A. Blaszczok and F.-V. Kuhlmann (J. Algebra 425 (2015)) and the key polynomials of J. Novacoski and M. Spivakovsky (J. Algebra 495 (2018)) are for one variable or need an immediate extension in which the second sequence is still of transcendental type. We found no theorem of Kaplansky type for a pair of sequences. Theorem 3.18.11 proves Conjecture T for $\deg f < p$ without such a theorem, and Theorem 3.18.26 proves it for the planar runs in each degree. Conjecture T is false for the linear runs (Remark 3.18.12). So in this form it is settled for both kinds of run.

**Remark 3.17.35 (the tests).** Computer tests agree with the results of this section. Two independent sets of scripts did the tests, with no shared code.

1. The closed form of Lemma 3.17.1 agreed with the charts in $180$ of $180$ checks in the first set, and with $0$ mismatches in $120$, $180$, $100$ and $100$ checks for $p = 2, 3, 5, 7$ in the second set. A version without the cleaning gave $71$ mismatches of $150$, so the test can see errors.
2. Proposition 3.17.8 had no failure at $9000$ points in the first set and at $15200$ points in the second set, also for $\nu^G \ge 1$ along $V(x, y)$, $V(x, z)$ and $V(x, w, y)$. With $F = w y^{p-1} z^{p-1}$, which is one less than the hypothesis in each exponent, $\rho$ changed in many runs, so the hypothesis is used.
3. Random walks that keep $\rho$, in classes of low degree, along $V(x + c\, y w)$, with products of two lines, with $x^2 + c w^2$ and in the class $y x^p + z w^p + B_0$, found no run with late translations of rank $2$ over $\mathbb{F}_p$ and no planar run. Every deep walk with late translations had them in the kernel of one line, with corner surfaces of $\nu^G \ge \rho$.
4. Lemma 3.17.25, Theorem 3.17.27, Proposition 3.17.30 and Lemma 3.17.31 had no failure in the walks for $p = 3, 5, 7$ in five classes, and every deep walk ended with a binary initial form of type $1$.
5. The bound of Lemma 3.17.19 had no failure on $45000$ random pairs over $\mathbb{F}_9$, $\mathbb{F}_{25}$ and $\mathbb{F}_{49}$. Theorem 3.17.21 was checked over $\mathbb{F}_5$, $\mathbb{F}_{25}$, $\mathbb{F}_{49}$, $\mathbb{F}_{121}$ and $\mathbb{F}_{125}$, with free coordinates that are not linear.
6. In the first set, $42$ origin runs of the class $x^2 + c w^2$ had no line over $\mathbb{F}_p$ with corner surfaces of $\nu^G \ge \rho$. These are not counterexamples: $x^2 + c w^2$ has a linear factor over $\mathbb{F}_{p^2}$, and all $42$ runs pass with the lines over $\mathbb{F}_{25}$. Walks with translations over $\mathbb{F}_{p^2}$ found no failure of Conjecture L° and no planar run.

The translations of the tests are in finite fields, the words are random or periodic, and the walks have a finite depth. So the tests are not a proof.

### Notes and references

The results of this section are a result of the milestone S7.18 of this project (tamnd/singularity#245). They come from notes 38 and 40 of the research notes, with the corrected statements of the referee reports in notes 39 and 42. Note 38 gave the closed form, the family of Proposition 3.17.8, the reduction to three variables and the class of one linear form, and proposed Conjecture L. Note 39 added the converse of Proposition 3.17.8, Lemma 3.17.6, the fixes of Theorems 3.17.13 and 3.17.15, Corollary 3.17.14 and Conjecture L+. It also separated the finiteness question from Question 3.13.18. Note 40 gave the counterexample of Theorem 3.17.21, Conjecture L°, the results on the points of type $0$ and on the binary initial forms, and Theorem 3.17.33. Note 42 added Example 3.17.22, the wording of Corollary 3.17.28, the multiples $y^{pA} z^{pB}$ in Theorem 3.17.29, and the remark that Hypothesis 3.17.32 holds for the origin runs. Note 38 had Corollary 3.17.14 and Theorem 3.17.15, part 3, for a general $\Phi$ under a result of note 36. Theorem 3.16.14 is this result, so they are now proved.

The outside results are the following. The pseudo Cauchy sequences and their types are from the paper of Kaplansky cited in Remark 3.17.34, the generalized stability theorem is [Kuh10, Theorem 1.1], and the facts on the henselization are in [Kuh-book]. The use of the history of the divisor is from [CJS20]. None of the results has a Lean proof yet.

Several questions are open.

1. Conjecture L, Conjecture L° and Hypothesis H1 were open for $\deg_{x, w} g > p$ in general. Section 3.18 proves them for $\deg_{x, w} g < p$ (Corollary 3.18.18), proves Conjecture L for $\deg_{x, w} g \le p$ and under the condition (C) (Corollary 3.18.36), and proves L and L° for $g \in K[[y, z]][x^p, w^p]$ (Theorem 3.18.37). By Theorem 3.18.19 the rest of Conjecture L is Conjecture P (Conjecture 3.18.39), and Section 3.19 proves it (Theorem 3.19.6). So Conjecture L holds for each clean $g$ (Corollary 3.19.7), and Conjecture L° and the binary form of Hypothesis H1 are open for $\deg_{x, w} g \ge p$ outside $K[[y, z]][x^p, w^p]$ (Conjecture 3.19.22). The form $\operatorname{in} G_m \in K[x'_m]$ is false for $\deg_{x, w} g \ge p + 1$ (Corollary 3.19.16).
2. Conjecture L° for the linear runs with $\deg_{x, w} g \ge p$ outside $K[[y, z]][x^p, w^p]$. The class $B_1 x^p + B_2 w^p + B_0$ of rank $2$ is no longer open (Corollary 3.18.38). The rest is Conjecture 3.19.22. Conjecture L+ is false for these runs (Theorem 3.19.17).
3. Conjecture T of Remark 3.17.34 is proved for the planar runs in each degree (Theorem 3.18.26). A form of it for the runs in more than two directions is open.
4. For $k \ge 3$ letters the value group has the rational rank $k$, and Lemma 3.15.6 and Proposition 3.15.7 must be proved again. A form of Conjecture L° for $k \ge 3$ is open.
5. Lemma 3.17.11 keeps the letters fixed. Whether a change of the letters by units can make the points of Example 3.17.9 cylindrical is not treated.
6. The corner curves need not resolve the point, as Example 3.13.21 shows, so the results of this section do not give a resolution strategy.
