---
title: Runs with free translations
nodes: [SG00000062, SG00000063, SG00000064, SG00000065, SG00000066, SG00000067, SG00000068]
sources: [CJS20, Kuh10, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs with free translations

This section continues the part "Corner runs with free translations" of Section 3.13. There, Theorem 3.13.27 shows that a corner run of $g = B_1 x^p + B_0$ has only a finite number of nonzero translations. Its proof ends where the cleaning can remove the least term of $g$ at $x = \varphi_m$. Here we treat a general $g \in K[[y, z]][x]$. There are four results. First, the sequence of the translations is a pseudo Cauchy sequence of transcendental type in the sense of Kaplansky (Proposition 3.15.7). This holds for each run, and it gives the values of $g$ and of its Hasse derivatives along the run. Second, if a run has an infinite number of nonzero translations, then from some point on $\partial_x g_m$ is a monomial times a unit (Proposition 3.15.10), so $g_m = \mu_m x'' + Q(x''^p, y_m, z_m)$ in a new free coordinate. Third, no corner run with free translations of $\mu x + B_0$ keeps $\rho \ge 1$ (Theorem 3.15.16). Fourth, if $\deg_x g < p$, then a corner run with free translations has only a finite number of nonzero translations (Theorem 3.15.17), and Question 3.13.18 has a positive answer for it.

The fourth result does not say that $\rho$ drops. The point $x^2 y z$ for $p = 3$ has a corner run with $\rho = 1$ at each point (Example 3.15.18). We also show that $\rho$ does not depend on the choice of the free coordinate (Lemma 3.15.2), and we prove a tame form of the finiteness for a general $g$ (Theorem 3.15.12).

### The setting

We use the setting and the notation of the part "Corner runs with free translations" of Section 3.13. So $K$ is an algebraically closed field of characteristic $p$, $n = 3$, and from $P_N$ on, $V(y_m)$ and $V(z_m)$ are in $\Delta$ and $V(x_m)$ is not. Step $m$ is the $y$-chart or the $z$-chart, followed by a translation $t_m \in K$ in $x$, so that $x_m = L_m (x_{m+1} + t_m)$. Each chart occurs an infinite number of times. A *corner run with free translations* also has the same $\rho \ge 1$ at each point. We have $M_N = 1$, $M_{m+1} = M_m L_m$, $\varphi_N = 0$ and $\varphi_{m+1} = \varphi_m + t_m M_{m+1}$, and the valuation $v(y_N^a z_N^b) = a + \theta b$ with $\theta$ irrational. By Lemma 3.13.24, $x_N = \varphi_m + M_m x_m$, $\varphi_m$ and $M_m$ are polynomials in $y_m, z_m$, $v(M_m) < 1 + \theta$, and $v(M_m)$ increases to $1 + \theta$.

In this section $g \in K[[y, z]][x]$, that is, $g$ is a polynomial in $x$ with coefficients in $K[[y, z]]$, in the coordinates of $P_N$. For a series $f$ we write $\operatorname{cl}(f)$ for $f$ without its monomials $c\, y^a z^b x^e$ with $a$, $b$ and $e$ all divisible by $p$. Since $K$ is perfect, these monomials are the $p$-th powers. For a polynomial $f = \sum_k f_k X^k$ the $k$-th Hasse derivative in $X$ is $f^{[k]} = \sum_l \binom{l}{k} f_l X^{l - k}$, and Taylor's formula $f(a + b) = \sum_k f^{[k]}(a) b^k$ holds over each commutative ring. A Laurent monomial in $y_N, z_N$ is a *$p$-th power* if both exponents are divisible by $p$. The monomial maps between the points have the determinant $\pm 1$, so this does not depend on the point where we write the monomial.

**Lemma 3.15.1.** For each $m \ge N$, put
$$g_m = \operatorname{cl}\bigl(g(\varphi_m + M_m x_m)\bigr), \qquad P_m(X) = g(\varphi_m + M_m X) = \sum_k A_k X^k, \qquad A_k = M_m^k \, g^{[k]}(\varphi_m),$$
with $y_N, z_N$ written in $y_m, z_m$. Then:

1. The function of the point $P_m$ is $M_m^{-p} g_m$. So $g_m$ and the point $P_m$ have the same $G$, the same $d$ and the same $\rho$.
2. $g_m = \sum_{p \nmid k} A_k x_m^k + \sum_{p \mid k} \operatorname{cl}(A_k) \, x_m^k$, and each $A_k$ is in $K[[y_m, z_m]]$.
3. $\partial_{x_m} g_m = M_m \, g_x(\varphi_m + M_m x_m)$.

*Proof.* Part 1. We use induction on $m$. For $m = N$ the claim holds, since $g$ is clean. Let $\pi$ be the map of step $m$, with $x_m = L_m (x_{m+1} + t_m)$ and the monomial map in $y_m, z_m$. The function of $P_{m+1}$ is the cleaning of $L_m^{-p} \pi(M_m^{-p} g_m)$. If $h^p$ is a $p$-th power, then $\pi(h^p) = \pi(h)^p$, and each monomial of $\pi(h)^p$ is a $p$-th power. So $\operatorname{cl}(\pi(\operatorname{cl} f)) = \operatorname{cl}(\pi(f))$ for each $f$. The product of a series with the $p$-th power of a Laurent monomial has the same monomials up to this factor, and the factor does not change which monomials are $p$-th powers. So the function of $P_{m+1}$ is
$$M_{m+1}^{-p} \operatorname{cl}\bigl( g(\varphi_m + M_m L_m (x_{m+1} + t_m)) \bigr) = M_{m+1}^{-p} \operatorname{cl}\bigl( g(\varphi_{m+1} + M_{m+1} x_{m+1}) \bigr).$$
The factor $M_m^{-p}$ is the $p$-th power of a Laurent monomial in $y_m, z_m$. It multiplies $x^r$ by $M_m^{-p}$ and does not change $G$. So $G$, $d$ and $\rho$ are the same.

Part 2. Taylor's formula gives $A_k = M_m^k g^{[k]}(\varphi_m)$. Since $y_N$, $z_N$, $\varphi_m$ and $M_m$ are polynomials in $y_m, z_m$, each $A_k$ is in $K[[y_m, z_m]]$. A monomial of $A_k x_m^k$ with $p \nmid k$ is not a $p$-th power. If $p \mid k$, then $\operatorname{cl}(A_k x_m^k) = \operatorname{cl}(A_k) x_m^k$.

Part 3. The chain rule gives $\partial_{x_m} P_m(x_m) = M_m g_x(\varphi_m + M_m x_m)$, and $\partial_{x_m}$ kills the $p$-th powers that the cleaning removes. $\square$

So we can work with $g_m$ in place of the function of $P_m$, as in Lemma 3.13.25. The terms $\operatorname{cl}(A_k)$ for $p \mid k$ are the place where the cleaning acts.

### The residual order does not depend on the free coordinate

A *free coordinate* at $P_m$ is a series $x''$ such that $(x'', y_m, z_m)$ is a regular system of parameters. The next lemma shows that the run and $\rho$ do not depend on this choice.

**Lemma 3.15.2.** Let $P$ be a point with $\Delta = \{V(y), V(z)\}$, let $g$ be clean, and let $\Theta(g) = (g_x, y g_y, z g_z) = x^r \widetilde\Theta(G)$.

1. $\Theta(g + h^p) = \Theta(g)$ for each series $h$.
2. $x^r$ is the largest monomial in $y, z$ that divides each element of $\Theta(g)$, and $\rho = \operatorname{ord} \widetilde\Theta(G)$.
3. Let $x''$ be a free coordinate, and let $g''$ be the cleaning of $g$ in the coordinates $(x'', y, z)$. Then $\Theta(g'') = \Theta(g)$, and $g''$ has the same $x^r$ and the same $\rho$ as $g$.
4. Let $\varepsilon$ be a unit of $K[[x, y, z]]$. Then $\varepsilon^p g$ is clean, $\Theta(\varepsilon^p g) = \varepsilon^p \Theta(g)$, and $\varepsilon^p g$ has the same $x^r$ and the same $\rho$ as $g$. After each chart with a translation, the transform of $\varepsilon^p g$ is $\varepsilon_1^p$ times the transform of $g$, with $\varepsilon_1$ a unit.
5. Let $P_m, P_{m+1}, \dots$ be a corner run with free translations, and let $x''$ be a free coordinate at $P_m$. Then $P_m, P_{m+1}, \dots$ is a corner run with free translations in the coordinates $(x'', y_m, z_m)$, with the same points, the same charts and the same $\rho$ at each point. The translations $t''_j$ in these coordinates can differ from the $t_j$.

Node: SG00000063

*Proof.* Parts 1 and 2 are Lemma 3.1.2 and Theorem 3.1.4, part 1.

Part 3. The logarithmic derivations are the derivations $D$ with $D(y) \in (y)$ and $D(z) \in (z)$. This module does not depend on the free coordinate. It has the basis $\partial_x, y \partial_y, z \partial_z$ in the coordinates $(x, y, z)$, and the basis $\partial_{x''}, y \partial_y, z \partial_z$ in the coordinates $(x'', y, z)$, where now the partial derivatives keep $x''$ fixed. So $\Theta(g)$ is the image of $g$ under this module in both coordinates. The cleaning in the new coordinates changes $g$ by a $p$-th power, so $\Theta(g'') = \Theta(g)$ by part 1. By part 2 in both coordinates, $x^r$ is the largest monomial in $y, z$ that divides this ideal, and $\rho$ is the order of the ideal divided by $x^r$. Neither depends on the free coordinate.

Part 4. Each monomial of $\varepsilon^p$ is a $p$-th power. So the exponents of each monomial of $\varepsilon^p g$ are congruent modulo $p$ to the exponents of a monomial of $g$, and $\varepsilon^p g$ is clean. Each derivation kills $\varepsilon^p$, so $\Theta(\varepsilon^p g) = \varepsilon^p \Theta(g)$, and part 2 gives the same $x^r$ and $\rho$. A chart with a translation sends the origin of the chart to the origin, so it sends $\varepsilon$ to a unit $\varepsilon_1$. If $f = \operatorname{cl}(f) + h^p$, then $\varepsilon_1^p f = \varepsilon_1^p \operatorname{cl}(f) + (\varepsilon_1 h)^p$, and $\varepsilon_1^p \operatorname{cl}(f)$ is clean by the argument above. So $\operatorname{cl}(\varepsilon_1^p f) = \varepsilon_1^p \operatorname{cl}(f)$, and the cleaning commutes with the factor.

Part 5. It is sufficient to treat one step, from $P_m$ to $P_{m+1}$, since then we can use induction. Write $x''$ as a series in $x, y, z$, and write $x'' = x u + f(y, z)$, where $f = x''(0, y, z)$. Since $x''$ is a free coordinate, $u$ is a unit, and $f(0, 0) = 0$. Let $L$ be the chart variable of the step, so $L = y_{m+1}$ or $L = z_{m+1}$. In both charts $y$ and $z$ are in the ideal $(L)$, so $f / L$ is a series in $y_{m+1}, z_{m+1}$. Thus
$$\frac{x''}{L} = (x_{m+1} + t_m) \, \pi(u) + \frac{f}{L},$$
and this is a series at $P_{m+1}$. Let $t''$ be its value at $P_{m+1}$, and put $x''_{m+1} = x'' / L - t''$. The derivative of $\pi(u)$ in $x_{m+1}$ has the factor $L$, so $\partial x''_{m+1} / \partial x_{m+1}$ is $u(0) \ne 0$ at $P_{m+1}$. So $x''_{m+1}$ is a free coordinate at $P_{m+1}$.

In the coordinates $(x'', y, z)$ the same chart has the variables $y_{m+1}, z_{m+1}$, since the formulas for $y$ and $z$ do not use $x$, and the free variable $x'' / L$. The point $P_{m+1}$ is the point of this chart with $x'' / L = t''$ and $y_{m+1} = z_{m+1} = 0$. So in the new coordinates the step is the same chart followed by the translation $t''$, and the new free coordinate is $x''_{m+1}$. The chart is the same, since it is fixed by the component of $\Delta$ whose strict transform does not pass through $P_{m+1}$, and $\Delta$ does not depend on $x''$. The function of $P_{m+1}$ is the same function, up to a $p$-th power, since it is the strict transform of the same hypersurface. By part 3, $\rho$ is the same at each point. So each condition of a corner run with free translations holds in the new coordinates. $\square$

**Remark 3.15.3.** In part 5 the class of the coordinates $x'' = x u$ is not kept by the steps. Let $u = 1 + y$, $t_m = 1$ and the $y$-chart, so $y = y_{m+1}$. Then $x'' = y_{m+1} (x_{m+1} + 1)(1 + y_{m+1})$, $t'' = 1$ and $x''_{m+1} = x_{m+1} + y_{m+1} + x_{m+1} y_{m+1}$. This is not divisible by $x_{m+1}$. For this reason part 5 allows each free coordinate.

### The dominance lemma and a criterion for the drop

The next lemma is the argument of Lemma 3.13.19 in the form that the proof of Proposition 3.13.26 uses. We state it for a base point $P_m$. Let $\theta_m = v(z_m) / v(y_m)$. For $m' > m$ write $y_m = y_{m'}^{a_1} z_{m'}^{a_2}$ and $z_m = y_{m'}^{b_1} z_{m'}^{b_2}$, and let $c_1 = (a_1, b_1)$ and $c_2 = (a_2, b_2)$ be the columns from $P_m$ to $P_{m'}$. Then the monomial $y_m^{q_1} z_m^{q_2}$ is $y_{m'}^{q \cdot c_1} z_{m'}^{q \cdot c_2}$. Put $\lambda(q) = q_1 + \theta_m q_2$, so that $v(y_m^{q_1} z_m^{q_2}) = v(y_m) \lambda(q)$.

**Lemma 3.15.4.** The number $\theta_m$ is irrational. Let $S \subseteq \mathbb{N}^2$ be a set, finite or infinite, with one point $q_*$ where $\lambda$ takes its least value on $S$. Then there is an $m_0$ such that for each $m' \ge m_0$, each $q \in S$ with $q \ne q_*$ and $s = 1, 2$, we have $(q - q_*) \cdot c_s > 0$.

*Proof.* If $\theta_m = a / b$ with integers $a$ and $b > 0$, then the Laurent monomial $z_m^b y_m^{-a}$ has the value $0$. It is not $1$, and it is a Laurent monomial in $y_N, z_N$, since the matrices have the determinant $\pm 1$. This is not possible, since $\theta$ is irrational.

From $v(y_m) = a_1 v(y_{m'}) + a_2 v(z_{m'})$ and $v(z_m) = b_1 v(y_{m'}) + b_2 v(z_{m'})$ we get $(v(y_m), v(z_m)) = v(y_{m'}) c_1 + v(z_{m'}) c_2$. So the ray of $(1, \theta_m)$ is in the cone of $c_1$ and $c_2$. A $y$-step replaces $c_1$ by $c_1 + c_2$ and a $z$-step replaces $c_2$ by $c_1 + c_2$, as in the proof of Theorem 3.13.20. Both charts occur an infinite number of times, so the entries of $c_1$ and $c_2$ go to infinity, and $c_s / |c_s|$ goes to the direction of $(1, \theta_m)$.

Write $q_* = (A, B)$ and $\delta = q - q_*$. Choose $m_1$ such that for $m' \ge m_1$ the entries of $c_1$ and $c_2$ are positive, and each column $c = (c', c'')$ satisfies $c'' \le (\theta_m + 1) c'$ and $c' \le (1 / \theta_m + 1) c''$. If $q_1 \ge A + B (\theta_m + 1) + 1$, then $\delta_2 \ge -B$, since $q_2 \ge 0$, and
$$\delta \cdot c \ge (q_1 - A) c' - B c'' \ge \bigl(q_1 - A - B (\theta_m + 1)\bigr) c' \ge c' > 0.$$
The case $q_2 \ge B + A (1 / \theta_m + 1) + 1$ is the same, with the two coordinates exchanged. The other points of $S$ are a finite set. For such a $q \ne q_*$ we have $\delta_1 + \theta_m \delta_2 > 0$, since $\lambda(q) > \lambda(q_*)$. Since $c_s / |c_s|$ goes to the direction of $(1, \theta_m)$ and $|c_s|$ goes to infinity, $\delta \cdot c_s$ goes to infinity. So there is an $m_2$ for this finite set. Take $m_0 = \max(m_1, m_2)$. $\square$

In the notation of Lemma 3.15.1 put $w_k = v(A_k)$ if $p \nmid k$ and $w_k = v(\operatorname{cl} A_k)$ if $p \mid k$, with $v(0) = \infty$. Consider the condition

(★) $\operatorname{cl} A_0 \ne 0$, and $v(\operatorname{cl} A_0) < w_k$ for each $k \ge 1$.

**Proposition 3.15.5.** If (★) holds at a point $P_m$ of the run, then there is an $m_0$ such that for each $m' \ge m_0$ and each choice of the later translations, $G_{m'}$ is a unit. So $\rho = 0$ at $P_{m'}$. In particular (★) fails at each point of a corner run with free translations.

*Proof.* Let $\mu_0$ be the term of $\operatorname{cl} A_0$ with the least value. It is unique, since distinct monomials have distinct values. Write $P_m(x_m) = P^{\mathrm{cl}} + P^{\mathrm{pow}}$, where $P^{\mathrm{pow}}$ is the sum of the terms of $P_m(x_m)$ that are $p$-th powers. So $P^{\mathrm{cl}} = g_m$ by Lemma 3.15.1, part 2. Let $m' > m$ and let $\pi$ be the map from $P_m$ to $P_{m'}$. By Lemma 3.13.24, part 3, $x_m = \psi + M' x_{m'}$ with $M' = M_{m'} / M_m$ and $\psi = \sum_{m \le j < m'} t_j M_{j+1} / M_m$, and $\psi$ and $M'$ are polynomials in $y_{m'}, z_{m'}$. As in the proof of Lemma 3.15.1, $g_{m'} = \operatorname{cl}(\pi(P^{\mathrm{cl}}))$, since $\operatorname{cl}(\pi(P^{\mathrm{pow}})) = 0$.

Let $S \subseteq \mathbb{N}^2$ be the set of the exponents in $y_m, z_m$ of the terms of $P^{\mathrm{cl}}$, with each power of $x_m$. A term of $P^{\mathrm{cl}}$ with a positive power $x_m^k$ is a term of $A_k$ or of $\operatorname{cl} A_k$, so its value is at least $w_k > v(\mu_0)$. A term of $\operatorname{cl} A_0$ other than $\mu_0$ has a value larger than $v(\mu_0)$. So the exponent $q_*$ of $\mu_0$ is the only point of $S$ with the least value of $\lambda$, and only the term $\mu_0$ of $P^{\mathrm{cl}}$ has the exponent $q_*$. Lemma 3.15.4 gives an $m_0$. Let $m' \ge m_0$.

A term $Y x_m^k$ of $P^{\mathrm{cl}}$ goes to $\pi(Y) (\psi + M' x_{m'})^k$, which is a sum of terms $\pi(Y) \eta \, x_{m'}^l$, where $\eta$ is a monomial with nonnegative exponents. If the exponent $q$ of $Y$ is not $q_*$, then both exponents of $\pi(Y)$ are larger than those of $\mu_0' = \pi(\mu_0)$, by Lemma 3.15.4. So $\pi(P^{\mathrm{cl}}) = \mu_0' (1 + f)$, with $f$ in the maximal ideal. The monomial $\mu_0'$ is not a $p$-th power, since $\mu_0$ is not one. So the cleaning keeps it, and $g_{m'} = \mu_0' \varepsilon$ with a unit $\varepsilon$. Since $V(x_{m'})$ is not in $\Delta$, $x^r$ is the monomial of $\mu_0'$, and $G_{m'}$ is a unit. Then $d = 0$, and $\rho = 0$ by Theorem 3.1.4, part 2. $\square$

Proposition 3.13.26 is the case $g = B_1 x^p + B_0$ of this proposition, where no cleaning is needed. The term $\operatorname{cl} A_0$ is $g$ at $x = \varphi_m$ without its $p$-th powers. So (★) can fail because the cleaning removes the least term of $g(\varphi_m)$, and this is the reason why the next results are needed.

### The sequence of the translations

Assume that an infinite number of the $t_j$ are not $0$. Let $j_1 < j_2 < \cdots$ be the indices with $t_j \ne 0$, and put $a_i = \varphi_{j_i + 1}$. Since $t_j = 0$ for $j_i < j < j_{i+1}$, we have $\varphi_m = a_i$ for $j_i < m \le j_{i+1}$. Put $\gamma_i = v(M_{j_{i+1} + 1})$ for $i \ge 0$. By Lemma 3.13.24, part 3, the $\gamma_i$ increase strictly, $\gamma_i < 1 + \theta$, and $\gamma_i \to 1 + \theta$. For $k > i \ge 1$, $a_k - a_i = \sum_{i < s \le k} t_{j_s} M_{j_s + 1}$ is a sum of distinct monomials with nonzero coefficients, so
$$v(a_k - a_i) = \gamma_i.$$
Let $F$ be a field with a valuation $v$. Kaplansky calls a sequence $(a_i)$ in $F$ *pseudo Cauchy* if $v(a_k - a_j) > v(a_j - a_i)$ for $i < j < k$ from some index on. An element $\xi$ is a *limit* of the sequence if $v(\xi - a_i) = \gamma_i$ for $i$ large. The sequence is of *algebraic type* over $F$ if there is a polynomial $f \in F[X]$ such that $v(f(a_i))$ increases strictly for $i$ large. It is of *transcendental type* over $F$ if for each $f \in F[X]$ the value $v(f(a_i))$ is constant for $i$ large. So our sequence is pseudo Cauchy.

Let $H = K(y_N, z_N)$ with the valuation $v$, and let $\hat H$ be its completion. We use the Hahn field $\mathbb{K} = K((t^\Gamma))$ with $\Gamma = \mathbb{Z} + \theta \mathbb{Z} \subseteq \mathbb{R}$. Its elements are the formal sums $\sum_\gamma c_\gamma t^\gamma$ with a well ordered support, and $v$ is the least exponent. Since $\theta$ is irrational, $y_N^a z_N^b \mapsto t^{a + \theta b}$ is a bijection from the Laurent monomials onto the powers of $t$. So we call the terms of an element of $\mathbb{K}$ monomials in $y_N, z_N$, and $\operatorname{cl}$ is defined on $\mathbb{K}$: it removes the terms whose monomial is a $p$-th power. It is additive, and $v(\operatorname{cl} f) \ge v(f)$.

**Lemma 3.15.6.**

1. The map of the monomials extends to an embedding of valued fields $\hat H \to \mathbb{K}$. For each $m$ it maps $K[[y_m, z_m]]$ into the image, with each series going to the sum of its terms, and it commutes with $\operatorname{cl}$.
2. For each $\xi \in \hat H$ and each $c \in \mathbb{R}$, the element $\xi$ has only a finite number of terms with a value less than $c$.
3. The sum $\varphi_\infty = \sum_j t_j M_{j+1}$ is an element of $\mathbb{K}$, and $v(\varphi_\infty - \varphi_m) \ge v(M_{m+1})$. If an infinite number of the $t_j$ are not $0$, then $v(\varphi_\infty - a_i) = \gamma_i$, and $\varphi_\infty$ is not in $\hat H$.

*Proof.* Part 1. A polynomial in $y_N, z_N$ goes to the sum of its terms. Distinct monomials go to distinct powers of $t$, so the value of the image is the least value of a monomial. So the map is an injective ring map that keeps $v$, and it extends to the field $H$. A Cauchy sequence in $\mathbb{K}$ has, below each value, terms that are the same from some index on, and the sum of these terms is in $\mathbb{K}$ and is the limit. So $\mathbb{K}$ is complete, and the map extends to $\hat H$ by continuity. It keeps $v$, so it is injective. A series in $K[[y_m, z_m]]$ has only a finite number of monomials below each value, by Lemma 3.13.24, part 2. So the sums of its terms below the values $1, 2, 3, \dots$ form a Cauchy sequence in $H$, and the limit in $\hat H$ goes to the sum of all its terms. The monomials of $y_m, z_m$ are $p$-th powers in the same cases as in $y_N, z_N$, so the map commutes with $\operatorname{cl}$.

Part 2. Let $f = u / w$ with polynomials $u, w$ in $y_N, z_N$ and $w \ne 0$. Write $w = c \mu (1 + h)$, where $c \mu$ is the term of $w$ with the least value. Then $h$ is a Laurent polynomial, and $\delta = v(h) > 0$. In $\mathbb{K}$ we have $1 / (1 + h) = \sum_{n \ge 0} (-h)^n$. The terms of $h^n$ have values at least $n \delta$, so only the $n < c / \delta$ give terms below $c$, and each $h^n$ has a finite number of terms. So $1 / (1 + h)$ has only a finite number of terms below each value. The same holds for a product of two such elements, since the values of their terms are bounded below. So it holds for $f$. Let $\xi \in \hat H$ and $c \in \mathbb{R}$. Choose $f \in H$ with $v(\xi - f) > c$. Then $\xi$ and $f$ have the same terms below $c$.

Part 3. The support of $\varphi_\infty$ is the set of the values $v(M_{j+1})$ with $t_j \ne 0$. These values increase strictly, so the support is well ordered. The terms of $\varphi_\infty - \varphi_m$ have the values $v(M_{j+1})$ with $j \ge m$, and these are at least $v(M_{m+1})$. In the same way $\varphi_\infty - a_i = \sum_{s > i} t_{j_s} M_{j_s + 1}$ has the value $\gamma_i$. The element $\varphi_\infty$ has an infinite number of terms with values less than $1 + \theta$. By part 2 it is not in $\hat H$. $\square$

**Proposition 3.15.7.** If an infinite number of the $t_j$ are not $0$, then $(a_i)$ is a pseudo Cauchy sequence of transcendental type over $\hat H$. So for each $f \in \hat H[X]$ the value $v(f(a_i))$ is constant for $i$ large.

Node: SG00000062

*Proof.* Step 1: the sequence has no limit in $\hat H$. Let $\xi \in \hat H$ with $v(\xi - a_i) = \gamma_i$ for $i$ large. Then $\xi$ and $a_i$ have the same terms below $\gamma_i$. The terms of $a_i$ are the $t_{j_s} M_{j_s + 1}$ for $s \le i$, with the values $\gamma_{s-1} < \gamma_i$. So $\xi$ has all the terms $t_{j_s} M_{j_s + 1}$, and there are an infinite number of them with values less than $1 + \theta$. This contradicts Lemma 3.15.6, part 2.

Step 2: the values at an algebraic element. Let $\bar F$ be an algebraic closure of $\hat H$, with an extension of $v$. Let $\alpha \in \bar F$ and put $\delta_i = v(a_i - \alpha)$. If $\delta_i < \gamma_i$ for some $i$, then for each $k > i$, $\delta_k = v((a_k - a_i) + (a_i - \alpha)) = \delta_i$, since $v(a_k - a_i) = \gamma_i > \delta_i$. If $\delta_i > \gamma_i$ for some $i$, then in the same way $\delta_k = \gamma_i < \gamma_k$ for each $k > i$, and we are in the first case. Otherwise $\delta_i = \gamma_i$ for each $i$. So $\delta_i$ is constant for $i$ large, or $\delta_i = \gamma_i$ for each $i$. Now let $f \in \hat H[X]$, $f \ne 0$, and write $f = c \prod_l (X - \alpha_l)$ in $\bar F[X]$. Let $s_f$ be the number of the $\alpha_l$ with $v(a_i - \alpha_l) = \gamma_i$ for each $i$. Then for $i$ large
$$v(f(a_i)) = C_f + s_f \gamma_i$$
with a constant $C_f$. So $v(f(a_i))$ is constant for $i$ large if $s_f = 0$, and it increases strictly if $s_f > 0$. In both cases $v(f(a_i)) < B_f = C_f + s_f (1 + \theta)$ for $i$ large.

Step 3: density. Assume that $s_f > 0$ for some $f = \sum_k c_k X^k \in \hat H[X]$. Since $H$ is dense in $\hat H$, there is $f' = \sum_k c'_k X^k \in H[X]$ of the same degree with $v(c_k - c'_k) > B_f$ for each $k$. Each $a_i$ has a positive value. So $v(f(a_i) - f'(a_i)) > B_f > v(f(a_i))$ for $i$ large, and $v(f'(a_i)) = v(f(a_i))$. So $v(f'(a_i))$ increases strictly for $i$ large, and $(a_i)$ is of algebraic type over $H$. Let $H^h$ be the henselization of $H$. Since $f' \in H^h[X]$, the sequence is also of algebraic type over $H^h$.

Step 4: the henselization is algebraically maximal. A valued field is *algebraically maximal* if it has no proper immediate algebraic extension. The valuation $v$ on $H$ has the value group $\mathbb{Z} + \theta \mathbb{Z}$ of rational rank $2$ and the residue field $K$, and $2 + 0 = \operatorname{trdeg}(H / K)$. So it is an Abhyankar valuation, and $(H / K, v)$ has no transcendence defect. The field $K$ with the trivial valuation is defectless. By the generalized stability theorem of Kuhlmann [Kuh10, Theorem 1.1], which is Volume 5, Theorem 2.2.2, the field $(H, v)$ is defectless. With the definition of Volume 5, Section 2.2, this says that each finite extension of $H^h$ has the defect $1$. Kuhlmann defines a defectless field by the fundamental equality for each finite extension. The two definitions agree by a standard fact on the henselization, which [Kuh10] uses in its Section 2. Let $L$ be a finite immediate extension of $H^h$. Since $H^h$ is henselian, $v$ has one extension to $L$, and the defect $1$ gives $[L : H^h] = e f = 1$. So $H^h$ is algebraically maximal.

Step 5. A theorem of Kaplansky (Maximal fields with valuations, Duke Math. J. 9 (1942)) says that a pseudo Cauchy sequence of algebraic type over a field $F$ with no limit in $F$ gives a proper immediate algebraic extension of $F$. By Steps 3 and 4, the sequence $(a_i)$ has a limit in $H^h$. Since $v$ has rank $1$, $H^h$ is contained in $\hat H$ [Kuh-book]. This contradicts Step 1. So $s_f = 0$ for each $f$, and by Step 2 the sequence is of transcendental type over $\hat H$. $\square$

The type is a property of the sequence and the field. It does not depend on $g$. The coefficients of the polynomials that we use below are in $K[[y_N, z_N]]$, and a power series is in general not in $H^h$. For this reason we need the transcendental type over $\hat H$, and not only over $H$.

**Lemma 3.15.8.** Assume that an infinite number of the $t_j$ are not $0$. Let $f \in \hat H[X]$ with $\deg f \ge 1$.

1. For each $k \ge 0$, $v(f^{[k]}(a_i))$ is constant for $i$ large. Call this value $\beta_k$, with $\beta_k = \infty$ if $f^{[k]} = 0$. Also $\beta_0 < \infty$.
2. There is an index $h \ge 1$ such that for $i$ large, $\beta_h + h \gamma_i < \beta_k + k \gamma_i$ for each $k \ge 1$ with $k \ne h$.
3. For $i$ large, $\beta_0 < \beta_k + k \gamma_{i-1}$ for each $k \ge 1$.
4. $v(f^{[k]}(\varphi_\infty)) = \beta_k$ for each $k \ge 0$.

We call $h$ the *dominant index* of $f$ and $(a_i)$. Kaplansky shows that $h$ is a power of $p$. Since $h \le \deg f$, we have $h = 1$ if $\deg f < p$.

*Proof.* Part 1. Apply Proposition 3.15.7 to $f^{[k]}$. The polynomial $f$ has only a finite number of roots, and the $a_i$ are distinct, so $f(a_i) \ne 0$ for $i$ large and $\beta_0 < \infty$.

Part 2. The functions $\ell_k(\gamma) = \beta_k + k \gamma$ with $\beta_k < \infty$ and $k \ge 1$ are a finite set of lines with distinct slopes, and the set is not empty, since $f^{[\deg f]} \ne 0$. Two of them meet at most once. So there is a $c < 1 + \theta$ such that no two of them meet in the interval $(c, 1 + \theta)$. On this interval one line is below all the others, since two lines that change places would meet. Let $h$ be its index. For $i$ large, $\gamma_i$ is in the interval.

Part 3. For $l > i$, Taylor's formula gives
$$f(a_l) - f(a_i) = \sum_{k \ge 1} f^{[k]}(a_i) (a_l - a_i)^k,$$
and the term $k$ has the value $\beta_k + k \gamma_i$ for $i$ large. By part 2 one term has the least value, so $v(f(a_l) - f(a_i)) = \beta_h + h \gamma_i$. Both $f(a_l)$ and $f(a_i)$ have the value $\beta_0$, so $\beta_h + h \gamma_i \ge \beta_0$ for $i \ge i_1$. The $\gamma_i$ increase strictly. So for $i - 1 > i_1$, $\beta_k + k \gamma_{i-1} \ge \beta_h + h \gamma_{i-1} > \beta_h + h \gamma_{i_1} \ge \beta_0$.

Part 4. By Lemma 3.15.6, part 3, $v(\varphi_\infty - a_i) = \gamma_i$. So Taylor's formula at $a_i$ and part 3 give $v(f(\varphi_\infty) - f(a_i)) \ge \min_{k \ge 1} (\beta_k + k \gamma_i) > \beta_0$ for $i$ large, and $v(f(\varphi_\infty)) = \beta_0$. For $k \ge 1$ with $f^{[k]} \ne 0$, apply this to $f^{[k]}$. If $\deg f^{[k]} = 0$, then $f^{[k]}$ is a constant and the claim is clear. $\square$

**Lemma 3.15.9.** Let $g \in K[[y, z]][x]$ be clean at $P_N$, and let $P_N, P_{N+1}, \dots$ be a corner run with free translations with an infinite number of nonzero translations. Let $\beta_k$ be the values of Lemma 3.15.8 for $f = g$, and put $W = \min_{k \ge 1} (\beta_k + k (1 + \theta))$. Then:

1. At $m = j_i + 1$ with $i$ large, $v(A_0) < v(A_k)$ for each $k \ge 1$.
2. Each term of $g(\varphi_\infty)$ with a value less than $W$ is a $p$-th power. That is, $\operatorname{cl}(g(\varphi_\infty))$ has no term with a value less than $W$.

*Proof.* Part 1. At $m = j_i + 1$ we have $\varphi_m = a_i$ and $v(M_m) = \gamma_{i-1}$. So $v(A_k) = \beta_k + k \gamma_{i-1}$ for $i$ large, and Lemma 3.15.8, part 3, gives the claim.

Part 2. Put $W_i = \min_{k \ge 1} (\beta_k + k \gamma_i)$. By Proposition 3.15.5, (★) fails at $P_m$. Since $w_k \ge v(A_k)$, this gives $v(\operatorname{cl} A_0) \ge \min_{k \ge 1} v(A_k) = W_{i-1}$. Here $A_0 = g(a_i)$. By Taylor's formula at $a_i$, $v(g(\varphi_\infty) - g(a_i)) \ge W_i > W_{i-1}$. Since $\operatorname{cl}$ is additive and does not lower the value, $\operatorname{cl}(g(\varphi_\infty))$ has no term with a value less than $W_{i-1}$. As $i \to \infty$, $W_{i-1} \to W$. $\square$

### The derivative in x

**Proposition 3.15.10.** Let $g \in K[[y, z]][x]$ be clean at $P_N$, and let $P_N, P_{N+1}, \dots$ be a corner run with free translations with an infinite number of nonzero translations. If $g_x \ne 0$, then there is an $m_0$ such that for each $m \ge m_0$,
$$\partial_{x_m} g_m = \mu_m \varepsilon_m,$$
with $\mu_m$ a nonzero constant times a monomial in $y_m, z_m$ and $\varepsilon_m$ a unit of $K[[x_m, y_m, z_m]]$.

Node: SG00000064

*Proof.* Put $f = g_x$. It is in $K[[y_N, z_N]][X] \subseteq \hat H[X]$. If $\deg f = 0$, then $f$ is a nonzero series in $y_N, z_N$, and $\partial_{x_m} g_m = M_m f$ by Lemma 3.15.1, part 3. Then the claim holds for each $m$, with $\varepsilon_m$ the quotient of $f$ by its term of the least value, by the argument below with $S$ the support of $f$. So let $\deg f \ge 1$, and let $\beta_k$ be the values of Lemma 3.15.8 for $f$. Choose $m = j_i + 1$ with $i$ large, so that $\varphi_m = a_i$ and $v(M_m) = \gamma_{i-1}$. Put
$$F_m(X) = f(\varphi_m + M_m X) = \sum_k M_m^k f^{[k]}(\varphi_m) X^k.$$
The coefficients are in $K[[y_m, z_m]]$, as in Lemma 3.15.1. The constant term $f(\varphi_m)$ has the value $\beta_0$, and by Lemma 3.15.8, part 3, the coefficient of $X^k$ for $k \ge 1$ has the value $\beta_k + k \gamma_{i-1} > \beta_0$. Let $q_*$ be the exponent in $y_m, z_m$ of the term $\nu_0$ of $f(\varphi_m)$ with the least value, and let $S \subseteq \mathbb{N}^2$ be the union of the supports in $y_m, z_m$ of all the coefficients of $F_m$. Then $q_*$ is the only point of $S$ with the least value, and only the term $\nu_0$ of $F_m$ has the exponent $q_*$.

Lemma 3.15.4 at the base point $P_m$ gives an $m_0$. Let $m' \ge m_0$. As in the proof of Proposition 3.15.5, $x_m = \psi + M' x_{m'}$, $\varphi_{m'} = \varphi_m + M_m \psi$ and $M_{m'} = M_m M'$, so $f(\varphi_{m'} + M_{m'} x_{m'}) = F_m(\psi + M' x_{m'})$. Each term of this series is $\pi(Y) \eta \, x_{m'}^l$, where $Y$ is a term of a coefficient of $F_m$ and $\eta$ has nonnegative exponents. If the exponent of $Y$ is not $q_*$, then both exponents of $\pi(Y)$ are larger than those of $\pi(\nu_0)$. So $f(\varphi_{m'} + M_{m'} x_{m'}) = \pi(\nu_0) \varepsilon$ with a unit $\varepsilon$. By Lemma 3.15.1, part 3, $\partial_{x_{m'}} g_{m'} = M_{m'} \pi(\nu_0) \varepsilon$. This holds for each choice of the later translations. $\square$

No cleaning occurs in this proof, since $\partial_x$ kills the terms that the cleaning removes. The next corollary gives the normal form of $g_m$.

**Corollary 3.15.11.** In the setting of Proposition 3.15.10, let $m \ge m_0$ and write $g_m = \sum_k a_k x_m^k$ with $a_k \in K[[y_m, z_m]]$.

1. $\mu_m$ divides $a_k$ for each $k$ with $p \nmid k$, and $a_1 = \mu_m \varepsilon_m(0, y_m, z_m)$.
2. The monomial $x^r$ of $g_m$ divides $\mu_m$, and $\rho \le \operatorname{ord}(\mu_m / x^r)$.
3. Put $x'' = \sum_{p \nmid k} (a_k / \mu_m) x_m^k$. Then $x''$ is a free coordinate at $P_m$, and $g_m = \mu_m x'' + Q(x''^p, y_m, z_m)$ for a series $Q$.

*Proof.* Part 1. $\partial_{x_m} g_m = \sum_k k a_k x_m^{k-1} = \mu_m \varepsilon_m$, so $\mu_m$ divides $k a_k$ for each $k$. Put $x_m = 0$ for $a_1$.

Part 2. The element $\partial_{x_m} g_m = \mu_m \varepsilon_m$ is in $\Theta(g_m) = x^r \widetilde\Theta(G_m)$. So $x^r$ divides $\mu_m$, and $(\mu_m / x^r) \varepsilon_m$ is in $\widetilde\Theta(G_m)$.

Part 3. By part 1, $x'' = x_m w$ with $w = a_1 / \mu_m + \cdots$, and $w(0) = \varepsilon_m(0) \ne 0$. So $x''$ is a free coordinate, and $x_m = x'' w'$ with a unit $w'$ in $x'', y_m, z_m$. The series $g_m - \mu_m x'' = \sum_{p \mid k} a_k x_m^k$ is a series in $x_m^p, y_m, z_m$. Since $x_m^p = x''^p w'^p$ and $w'^p$ is a series in $x''^p, y_m^p, z_m^p$, it is a series in $x''^p, y_m, z_m$. $\square$

By Lemma 3.15.2, part 5, the run from $P_m$ is a corner run with free translations in the coordinates $(x'', y_m, z_m)$. So the case of an infinite number of nonzero translations with $g_x \ne 0$ is reduced to the points $\mu x + Q(x^p, y, z)$, with $\mu$ a constant times a monomial. The case $g_x = 0$ is the class $K[[y, z]][x^p]$.

### The tame case

Let $g \in K[[y, z]][x]$ and let $h$ be the dominant index of $g$ and $(a_i)$, as in Lemma 3.15.8. By part 4 of that lemma, $g_x(\varphi_\infty) \ne 0$ has the value $\beta_1$ if $\beta_1 < \infty$. Its term with the least value is $c_b y^b$, where $y^b$ is a Laurent monomial in $y_N, z_N$ and $c_b \in K$ is not $0$. For a sum of terms, $(\cdot)^\natural$ keeps the terms that are not $p$-th powers.

**Theorem 3.15.12.** Let $g \in K[[y, z]][x]$ be clean at $P_N$, and let $P_N, P_{N+1}, \dots$ be a corner run with free translations with an infinite number of nonzero translations. Assume that the dominant index of $g$ and $(a_i)$ is $h = 1$. This holds, for example, if $\deg_x g < p$. Let $y^b$ be the leading monomial of $g_x(\varphi_\infty)$, with the coefficient $c_b$. Then:

1. $W = \beta_1 + 1 + \theta$, and $\beta_k + k (1 + \theta) > W$ for each $k \ge 2$.
2. For $m$ large,
$$\operatorname{cl}(g(\varphi_m)) \equiv -c_b \sum_{j \ge m} t_j \, (y^b M_{j+1})^\natural$$
modulo terms with a value at least $W$.
3. Only a finite number of the $t_j \ne 0$ have $y^b M_{j+1}$ not a $p$-th power.

Node: SG00000065

*Proof.* Part 1. Since $h = 1$, for $i$ large and $k \ge 2$ we have $\beta_1 + \gamma_i < \beta_k + k \gamma_i$, so $\beta_1 - \beta_k < (k - 1) \gamma_i < (k - 1)(1 + \theta)$. This gives $\beta_1 + (1 + \theta) < \beta_k + k (1 + \theta)$, and the minimum $W$ is taken at $k = 1$.

Part 2. We work in $\mathbb{K}$. Put $\delta_m = \varphi_\infty - \varphi_m$. By Lemma 3.15.6, part 3, $v(\delta_m) \ge v(M_{m+1})$, so $v(\delta_m) \to 1 + \theta$. Taylor's formula at $\varphi_\infty$ gives
$$g(\varphi_m) = g(\varphi_\infty) - g_x(\varphi_\infty) \, \delta_m + \sum_{k \ge 2} g^{[k]}(\varphi_\infty) (-\delta_m)^k.$$
We treat the three parts of the right side.

The terms with $k \ge 2$. By Lemma 3.15.8, part 4, the term $k$ has a value at least $\beta_k + k \, v(\delta_m)$. This is at least $W$ if $v(\delta_m) \ge (\beta_1 - \beta_k + 1 + \theta) / k$. By part 1 the right side is less than $1 + \theta$. There are only a finite number of $k$, so all these terms have values at least $W$ for $m$ large.

The linear term. The support of $g_x(\varphi_\infty)$ is well ordered, so $g_x(\varphi_\infty) = c_b y^b + R$ with $v(R) \ge \beta_1 + \varepsilon_1$ for some $\varepsilon_1 > 0$. Then $v(R \delta_m) \ge \beta_1 + \varepsilon_1 + v(\delta_m) \ge W$ for $m$ large. So $g_x(\varphi_\infty) \delta_m \equiv c_b \sum_{j \ge m} t_j y^b M_{j+1}$ modulo terms with a value at least $W$.

The constant term. By Lemma 3.15.9, part 2, $\operatorname{cl}(g(\varphi_\infty))$ has no term with a value less than $W$.

Now apply $\operatorname{cl}$, which is additive, does not lower the value and acts term by term. This gives part 2.

Part 3. Fix one $m$ as in part 2. The left side $\operatorname{cl}(g(\varphi_m))$ is an element of $K[[y_m, z_m]]$, so it has only a finite number of monomials with a value less than $W$, by Lemma 3.13.24, part 2. On the right side there is one term for each $j \ge m$ with $t_j \ne 0$ and $y^b M_{j+1}$ not a $p$-th power. These monomials are distinct, since the values $v(M_{j+1})$ are distinct, and they have the values $\beta_1 + v(M_{j+1}) < \beta_1 + 1 + \theta = W$. So there are only a finite number of such $j$. $\square$

The theorem does not exclude an infinite number of translations with $y^b M_{j+1}$ a $p$-th power. For $\deg_x g < p$ Theorem 3.15.17 below excludes them by another argument.

**Remark 3.15.13 (the dominant index $h > 1$).** Let $h = p^e > 1$ be the dominant index, put $W = \beta_h + h (1 + \theta)$, and assume that $\beta_k + k (1 + \theta) \ne W$ for each $k < h$. Let $y^{b_h}$ be the leading monomial of $g^{[h]}(\varphi_\infty)$. If the run has an infinite number of nonzero translations, then $y^{b_h}$ is a $p$-th power. The proof is the same. For $k > h$ the argument of part 1 gives $\beta_k + k (1 + \theta) > W$. For $k < h$ the limit of the inequality of Lemma 3.15.8, part 2, gives $\ge$, and the assumption gives $>$. So the terms of Taylor's formula with $k \ne h$ have values at least $W$ for $m$ large. In characteristic $p$, $\delta_m^h = \sum_{j \ge m} t_j^h M_{j+1}^h$. So the argument of parts 2 and 3 shows that only a finite number of $j$ have $t_j \ne 0$ and $y^{b_h} M_{j+1}^h$ not a $p$-th power. Since $M_{j+1}^h$ is a $p$-th power, this means that $y^{b_h}$ is a $p$-th power. The case where $\beta_k + k (1 + \theta) = W$ for some $k < h$ is not treated here. For the class $\mu x + F(x^p)$, Lemma 3.16.4 shows that the tie set contains only $1$ and powers of $p$, and Section 3.16 proves the finiteness of the translations without this remark.

### The class $\mu x + B_0$

In this part $g = \mu x + B_0$, where $\mu$ is a nonzero constant times a monomial in $y, z$ and $B_0 \in K[[y, z]]$, in the coordinates of $P_N$, and $g$ is clean. Put $\xi = -B_0 / \mu$. It is a Laurent series in $y_N, z_N$ with exponents in a translate of $\mathbb{N}^2$, so it has only a finite number of terms below each value. For a Laurent series $w$ let $w^\natural$ keep the terms $c \, y^a z^b$ of $w$ such that $\mu y^a z^b$ is not a $p$-th power.

**Lemma 3.15.14.** At each $P_m$,
$$g_m = \mu M_m x_m + C_m, \qquad C_m = \operatorname{cl}(\mu \varphi_m + B_0) = \mu (\varphi_m - \xi)^\natural.$$
A translation $t_j$ with $\mu M_{j+1}$ a $p$-th power does not change $C$, that is, $C_{j+1} = C_j$ as Laurent series in $y_N, z_N$.

*Proof.* By Lemma 3.15.1, $A_1 = \mu M_m$, $A_0 = \mu \varphi_m + B_0$ and $A_k = 0$ for $k \ge 2$. The term $\mu M_m x_m$ has the degree $1$ in $x_m$, so it is not a $p$-th power. So $g_m = \mu M_m x_m + \operatorname{cl}(A_0)$, and $A_0 = \mu (\varphi_m - \xi)$. The step adds $\operatorname{cl}(\mu t_j M_{j+1})$ to $C$, and this is $0$ if $\mu M_{j+1}$ is a $p$-th power. $\square$

**Lemma 3.15.15.** In a corner run with free translations of $g$, only a finite number of the $t_j \ne 0$ have $\mu M_{j+1}$ not a $p$-th power. If $J$ is the last such index, or $J = N - 1$ if there is none, then $C_m = C_{J+1}$ for each $m > J$.

*Proof.* Assume that an infinite number of the $t_j \ne 0$ have $\mu M_{j+1}$ not a $p$-th power. Then $\varphi_\infty^\natural$ has an infinite number of terms with values less than $1 + \theta$, and $\xi^\natural$ has only a finite number. So $(\varphi_\infty - \xi)^\natural$ has a term with a value less than $1 + \theta$. Let $w$ be the term with the least value, and choose $m$ with $v(M_m) > v(w)$. The terms of $\varphi_\infty$ that are not terms of $\varphi_m$ have the values $v(M_{j+1}) > v(M_m)$ with $j \ge m$. So $w$ is also the term of $(\varphi_m - \xi)^\natural$ with the least value, and
$$v(\operatorname{cl} A_0) = v(C_m) = v(\mu) + v(w) < v(\mu) + v(M_m) = v(A_1) = w_1.$$
Also $w_k = \infty$ for $k \ge 2$. So (★) holds at $P_m$, and Proposition 3.15.5 gives $\rho = 0$ at a later point. This is a contradiction. The second claim follows from Lemma 3.15.14. $\square$

**Theorem 3.15.16.** Let $n = 3$ and let $g = \mu x + B_0$ be clean at $P_N$, with $\mu$ a nonzero constant times a monomial in $y, z$ and $B_0 \in K[[y, z]]$. Then no corner run with free translations from $P_N$ keeps $\rho \ge 1$. The same holds for $g = \mu \varepsilon^p x + B_0$ with $\varepsilon \in K[[y, z]]$ a unit.

Node: SG00000066

*Proof.* Assume that such a run exists. Let $J$ be as in Lemma 3.15.15, and put $C = C_{J+1}$. Since $\varphi_{J+1}$ is a polynomial in $y_{J+1}, z_{J+1}$, $C$ is in $K[[y_{J+1}, z_{J+1}]]$. For $m > J$, $C_m = C$, and $C$ is the same series written in $y_m, z_m$.

Case 1: $C \ne 0$ and $v(C) < v(\mu) + 1 + \theta$. For $m$ large, $v(M_m) > v(C) - v(\mu)$, so $v(\operatorname{cl} A_0) = v(C) < v(\mu M_m) = w_1$, and $w_k = \infty$ for $k \ge 2$. So (★) holds, and Proposition 3.15.5 gives $\rho = 0$ later.

Case 2: $C = 0$ or $v(C) \ge v(\mu) + 1 + \theta$. By Lemma 3.13.24, part 3, $\mu y_N z_N = \mu M_{J+1} y_{J+1} z_{J+1}$, and this is a monomial in $y_{J+1}, z_{J+1}$ with nonnegative exponents. Let $q_*$ be its exponent, and let $S$ be the union of the support of $C$ and $\{q_*\}$. Each monomial of $C$ has a value at least $v(\mu y_N z_N) = v(\mu) + 1 + \theta$, and only the monomial with the exponent $q_*$ has this value. So $q_*$ is the only point of $S$ with the least value, and Lemma 3.15.4 at the base point $P_{J+1}$ applies. For $m$ large, both exponents of each monomial of $C$ other than $q_*$, written in $y_m, z_m$, are larger than those of the image of $q_*$, which is $\mu M_m y_m z_m$. So $\mu M_m$ divides $C$ in $K[[y_m, z_m]]$, and
$$g_m = \mu M_m (x_m + D), \qquad D = C / (\mu M_m) \in (y_m z_m).$$
Since $x_m + D$ is not divisible by $y_m$ or by $z_m$, the monomial $x^r$ is the monomial of $\mu M_m$ and $G_m$ is a constant times $x_m + D$. Then $\partial_x G_m$ is a unit, and $\rho = 0$.

In both cases $\rho$ drops, which is a contradiction. For the second claim, write $\mu \varepsilon^p x + B_0 = \varepsilon^p (\mu x + \varepsilon^{-p} B_0)$. Each monomial of $\varepsilon^{-p}$ is a $p$-th power, so $\varepsilon^{-p} B_0 \in K[[y, z]]$ is clean. By Lemma 3.15.2, part 4, the two points have the same runs, with the same $\rho$ at each point. $\square$

The theorem also covers the runs with no translations and the runs with an infinite number of translations with $\mu M_{j+1}$ a $p$-th power. In the second claim $\varepsilon$ must be a series in $y, z$. If $\varepsilon = 1 + x$, then $\mu \varepsilon^p x + B_0 = \mu x + \mu x^{p+1} + B_0$, and this point is not in the class, since $\varepsilon^{-p} B_0$ depends on $x^p$.

### The class $\deg_x g < p$

**Theorem 3.15.17.** Let $n = 3$ and let $g \in K[[y, z]][x]$ be clean at $P_N$ with $\deg_x g < p$. Then each corner run with free translations from $P_N$ has only a finite number of nonzero translations. Let $J$ be the last index with $t_J \ne 0$, and let $J = N - 1$ if all $t_m$ are $0$. Then $P_{J+1}, P_{J+2}, \dots$ is a run of Theorem 3.13.20 in the coordinates of $P_{J+1}$. So for $m$ large both corner curves at $P_m$ have $\nu^G = d_m \ge \rho$, and Question 3.13.18 has a positive answer for this run.

Node: SG00000067

*Proof.* Assume that the run has an infinite number of nonzero translations. If $g_x = 0$, then $g$ has no term $a_k x^k$ with $1 \le k < p$, so $g = B_0 \in K[[y, z]]$. This is the case $B_1 = 0$ of Theorem 3.13.27, and Proposition 3.13.26 at $P_N$ gives $\rho = 0$ later, which is false. So $g_x \ne 0$.

The charts, the translations and the cleaning keep $\deg_x g_m \le \deg_x g < p$, by Lemma 3.15.1. By Proposition 3.15.10 there is an $m$ with $\partial_{x_m} g_m = \mu_m \varepsilon_m$. In Corollary 3.15.11, part 3, the series $Q$ is $\sum_{p \mid k} a_k x_m^k = a_0$, since $a_k = 0$ for $k \ge p$. So
$$g_m = \mu_m x'' + a_0(y_m, z_m),$$
with $x''$ a free coordinate at $P_m$. The series $a_0$ is the part of the clean series $g_m$ without $x_m$, so it is clean, and $g_m$ is clean in the coordinates $(x'', y_m, z_m)$. The function of $P_m$ is $M_m^{-p} g_m$ by Lemma 3.15.1. It is a power series, and so are its value at $x'' = 0$, which is $M_m^{-p} a_0$, and the coefficient $M_m^{-p} \mu_m$, which is a constant times a monomial. By Lemma 3.15.2, part 5, the run from $P_m$ is a corner run with free translations in the coordinates $(x'', y_m, z_m)$, with $\rho \ge 1$ at each point. This contradicts Theorem 3.15.16, which allows all translations.

So only a finite number of the $t_m$ are not $0$. From $P_{J+1}$ on, each step is at the origin of the $y$-chart or of the $z$-chart, and each chart occurs an infinite number of times. The point $g_{J+1}$ is clean, $V(x_{J+1})$ is not in $\Delta$, and the run keeps $\rho$. These are the hypotheses of Theorem 3.13.20. $\square$

The theorem says nothing about the drop of $\rho$. The next example shows that $\rho$ need not drop.

**Example 3.15.18.** Let $p \ge 3$, $n = 3$, $\Delta = \{y, z\}$ and
$$g = x^2 y^{p-2} z^{p-2},$$
so $g = x^2 y z$ for $p = 3$. The origin of the $y$-chart and the origin of the $z$-chart send $g$ to $g$, and $\rho = 1$ at each point. So each sequence of the two charts at the origin in which both charts occur an infinite number of times is a corner run with free translations, with all translations $0$, $\rho = 1$ and $\deg_x g = 2 < p$.

Node: SG00000068

*Proof.* The exponents of $g$ are $(2, p - 2, p - 2)$, and $2$ is not divisible by $p$, so $g$ is clean. Also $\operatorname{ord} g = 2p - 2 \ge p$. Here $r = (0, p - 2, p - 2)$ and $G = x^2$. The generators of $\widetilde\Theta(G)$ are $\partial_x G = 2x$ and $(p - 2) G + y \partial_y G = (p - 2) G + z \partial_z G = (p - 2) x^2$. Since $2 \ne 0$ in $K$, $\rho = 1$, and $d = 2$. The $y$-chart at the origin sends $g$ to
$$y^{-p} (y x)^2 y^{p-2} (y z)^{p-2} = x^2 y^{p-2} z^{p-2},$$
and the $z$-chart is the same with $y$ and $z$ exchanged. The new divisor is $\{y, z\}$ in both charts, and $V(x)$ is not in it. $\square$

The example is close to Example 3.13.10, with $x^2$ in place of $x^p$. In the run that takes the two charts in turn, Theorem 3.13.20 gives $d_m = 2 \ge \rho$ and the corner curves $V(x, y)$ and $V(x, z)$ with $\nu^G = 2$. So in the class of Theorem 3.15.17 runs with $\rho \ge 1$ exist, and the theorem gives the finiteness of the translations and not the end of the run.

### Remarks

**Remark 3.15.19.** Computer tests over $\mathbb{F}_2$, $\mathbb{F}_3$, $\mathbb{F}_5$ and $\mathbb{F}_7$ agree with the results of this section. Two independent sets of scripts did the tests, with no shared code. The translations of the tests are in $\mathbb{F}_p$ and not in $K$, the words of charts are periodic, and the searches have a cap on the depth or on the time. So the tests are not a proof.

1. Lemma 3.15.14. The formula for $g_m$ agrees with the charts in $2253$ of $2253$ cases for $p = 2$, $2093$ of $2093$ for $p = 3$ and $2005$ of $2005$ for $p = 5$. A translation with $\mu M_{j+1}$ a $p$-th power left $g$ unchanged in $192$ of $192$, $98$ of $98$ and $46$ of $46$ cases.
2. Proposition 3.15.10 and Corollary 3.15.11. At the points reached by a nonzero translation, from $150$ random starts with $\deg_x g < p$ for $p = 3, 5, 7$ and $150$ starts of degree up to $2p$ for $p = 3$, the bound of part 2 of the corollary had no failure at $19954$, $7135$, $4363$ and $7457$ points. At the points where the last $6$ letters contain each of $y$ and $z$ at least twice, $\partial_x g_m$ was a monomial times a unit at $546$ of $553$, $36$ of $36$, $12$ of $12$ and $76$ of $76$ points. The $7$ exceptions are at the first translation, and the proposition holds only for $m$ large. This test is weak, since by Theorem 3.15.17 the hypothesis of the proposition is never met in the class $\deg_x g < p$.
3. Theorem 3.15.16. From random starts $c \, y^a z^b x + B_0$ with $\rho \ge 1$, along five periodic words in the two charts, a search over all translations that keep $\rho$ found no branch that keeps $\rho$ for more than $4$ steps: $150$ starts, $750$ runs and $1368$ nodes for $p = 2$, $150$ starts, $750$ runs and $2001$ nodes for $p = 3$, and $100$ starts, $500$ runs and $2045$ nodes for $p = 5$.
4. Example 3.15.18 and Theorem 3.15.17. Along the run that takes the two charts in turn for $40$ steps, $\rho$ stayed constant for $x^2 y z$ with $p = 3$ and $p = 5$, for $x^3 y z^2$ with $p = 5$ and for two small changes of these points. Random clean starts with $\deg_x g < p$ along the five periodic words at the origin, for $60$ steps, kept $\rho$ in $225$ of $1500$ runs for $p = 3$, in $269$ of $1500$ for $p = 5$, and in $281$ of $1500$ for $p = 5$ with tilted starts. These tests use the total transform, without the factor $L^{-p}$ of the strict transform, and this factor does not change $G$ or $\rho$.
5. Theorem 3.15.17 and the open question below. A search to the depth $30$ in the class $\deg_x g < p$ tested each nonzero translation $t_j$ of each branch that keeps $\rho$ against each base point $P_m$ with $m \le j$. For the random starts it found $218$ branches at the depth $30$ for $p = 3$ and $160$ for $p = 5$, none with a nonzero translation. For the tilted starts $(x + l y)^d y^a z^b$ plus random terms, with $d < p$, it found $979$, $629$ and $465$ branches for $p = 3, 5, 7$, of which $643$, $493$ and $425$ have a nonzero translation, and none has a translation with $M_{j+1} / M_m \notin \mathbb{N}^2$. A first search of $1200$ runs for $p = 3, 5, 7$ to the depth $30$ found at most one nonzero translation on each branch, and none after the step $15$.
6. The open question below. Depth first searches in eleven classes of starts for $p = 2, 3, 5, 7$, to the depths $10$ to $14$, with about $2.63$ million nodes in total, found no branch where both charts occur, with $\rho$ kept, after a translation $t_j$ with $M_{j+1} / M_m \notin \mathbb{N}^2$ at some base point $P_m$. Long runs with many translations exist at a finite depth, also in the class of Theorem 3.15.16. This does not contradict the theorem, which is about infinite runs.

### Notes and references

The results of this section are a result of the milestone S7.18 of this project (tamnd/singularity#245). They come from note 30 of the research notes, with the corrections and the proofs of the referee report in note 33. The criterion (★) and the dominance argument are from notes 27, 28 and 29. Note 30 stated that no corner run with free translations keeps $\rho \ge 1$ when $\deg_x g < p$, and Example 3.15.18 shows that this is false. Theorem 3.15.17 is the corrected statement. Note 33 also replaced a step of the proof of Proposition 3.15.7, on the completion, by the density argument of Step 3, corrected part 5 of Lemma 3.15.2 (Remark 3.15.3), and gave a new proof of part 3 of Theorem 3.15.12. The pseudo Cauchy sequences, the two types and the dominant index are from the paper of Kaplansky, Maximal fields with valuations, Duke Math. J. 9 (1942). The generalized stability theorem is [Kuh10, Theorem 1.1], and the facts on the henselization are in [Kuh-book]. The use of the history of the divisor is from [CJS20]. None of the results has a Lean proof yet.

Several questions are open. Call a translation $t_j \ne 0$ with $j \ge m$ *violating* at the base point $P_m$ if $M_{j+1} / M_m$ has a negative exponent in $y_m, z_m$. The conjecture V of note 28 says that a corner run with free translations has no violating translation at any base point. It implies the finiteness of the translations. It is open, also in the class $\deg_x g < p$, where Theorem 3.15.17 gives only the finiteness, and for a general $g$, where Theorem 3.16.14 gives only the finiteness. In the class of Theorem 3.15.16 it holds, since there is no such run. By Proposition 3.15.10, Corollary 3.15.11 and Lemma 3.15.2, the finiteness of the translations for a general $g$ with $g_x \ne 0$ reduces to the points $\mu x + Q(x^p, y, z)$ with $\mu$ a constant times a monomial and $Q$ depending on $x$. For them the proof of Theorem 3.15.16 does not apply, since the coefficients of the powers of $x_m^p$ change with $m$ and Lemma 3.15.4 needs a fixed set of exponents. Section 3.16 proves the finiteness for these points, and so for each clean $g$ (Theorem 3.16.14). The conjecture V is open for them. Theorem 3.15.12 is proved only for the dominant index $h = 1$. For $h > 1$ there is only the partial result of Remark 3.15.13, but Section 3.16 does not need it. Last, a run with only a finite number of translations need not end, as Example 3.15.18 shows, and its centers must come from the corner curves of Theorem 3.13.20.
