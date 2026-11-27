---
title: Planar runs and the hypothesis H1
nodes: [SG00000089, SG0000008A, SG0000008B, SG0000008C, SG0000008D, SG0000008E, SG0000008F, SG0000008G, SG0000008H, SG0000008J, SG0000008K, SG0000008M, SG0000008N]
sources: [CJS20, Kuh10, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Planar runs and the hypothesis H1

Section 3.17 leaves three statements open for the corner runs in four variables: Conjecture L (Conjecture 3.17.18), Conjecture L° (Conjecture 3.17.24) and Hypothesis H1 (Hypothesis 3.17.32). Theorem 3.17.33 proves Conjecture L under H1 for $\deg_{x, w} g < p$, but it does not give the corner curves of Conjecture L° in its case 2. This section removes the hypothesis and proves all three statements for $\deg_{x, w} g < p$.

The corner runs are of three kinds. In the first kind all the translations are $0$ from some point on, and Theorem 3.14.7 applies. In the second kind the run is linear (Definition 3.17.5) with an infinite number of nonzero translations, so the late translations lie on one line of $K^2$. In the third kind the run is planar. The proof has two halves, one for each of the last two kinds.

For a linear run the translations of one free coordinate $x$ are $0$, so the coefficients of the powers of $x$ in $g_m$ depend on one sequence $(\psi_m)$ only, and the one-variable theory of Section 3.15 makes them monomials times units. The $w$-part of $g$ is then $\mu w$ plus a constant term, and a uniform form of the dominance lemma controls the constant term along all the later translations. The result is Theorem 3.18.6: for $m$ large, $\operatorname{in} G_m = c\, x_m^d$ with $2 \le d = \rho + 1 < p$, the corner curves have $\nu^G = d$ and the corner surfaces have $\nu^G \ge \rho$. So H1, L, L+ and L° hold for these runs.

For a planar run there is no such reduction, and Section 3.17 asks for a theory of Kaplansky type for the pair of limits $(\varphi_\infty, \psi_\infty)$ (Remark 3.17.34). We do not need it. The key point is that a linear combination $\alpha \Delta\varphi + \beta \Delta\psi$ of the tails, with coefficients in a field $\mathbb{F}$ of series of finite type, cannot cancel the infinite number of terms of a planar tail below $1 + \theta$ (Lemma 3.18.10). An induction on the degree then proves Conjecture T for the planar runs and the polynomials of degree less than $p$ (Theorem 3.18.11). From it the derivatives $\partial_x g_m$ and $\partial_w g_m$ become monomials times units, the point becomes cylindrical, and Theorem 3.15.16 gives a contradiction. So there is no planar corner run with $\deg_{x, w} g < p$ (Theorem 3.18.17).

The section proves the following.

1. For $\deg_{x, w} g < p$, each corner run in four variables is linear, and Hypothesis H1 and Conjectures L and L° hold for it, with $d = \rho + 1$ for $m$ large. For the runs with an infinite number of nonzero translations Conjecture L+ holds as well (Theorem 3.18.6 and Corollary 3.18.18). So Theorem 3.17.33 holds without its hypothesis.
2. Conjecture T holds for the planar runs and the polynomials of degree less than $p$ (Theorem 3.18.11).
3. Planarity does not depend on the free coordinates, linear or not. A corner run satisfies Conjecture L if and only if it is not planar (Theorem 3.18.19). This holds for each degree.

For $\deg_{x, w} g \ge p$ the statements stay open, and Remark 3.18.22 says where the proofs break.

### The setting

We use the setting of Section 3.17. The field $K$ is algebraically closed of characteristic $p$. From $P_N$ on, $P_m$ has the coordinates $(x_m, w_m, y_m, z_m)$, step $m$ is a $y$-chart or a $z$-chart with the chart variable $L_m$, followed by $x_m = L_m (x_{m+1} + a_m)$ and $w_m = L_m (w_{m+1} + b_m)$. We have $M_N = 1$, $M_{m+1} = M_m L_m$, $\varphi_m = \sum_{N \le j < m} a_j M_{j+1}$, $\psi_m = \sum_{N \le j < m} b_j M_{j+1}$ and $\Phi_m = (\varphi_m, \psi_m)$, with the limits $\varphi_\infty$, $\psi_\infty$ and $\Phi_\infty$ in the Hahn field $\mathbb{K}$ of Lemma 3.15.6. The field $\hat H$ is the completion of $H = K(y_N, z_N)$, embedded in $\mathbb{K}$ by Lemma 3.15.6, part 1. It contains $K[[y_m, z_m]]$ for each $m$.

The valuation is $v(y_N^a z_N^b) = a + \theta b$ with $\theta$ irrational. So two Laurent monomials with the same value are equal. By Lemma 3.13.24, $M_m = y_N z_N / (y_m z_m)$ and $v(M_m)$ increases strictly to $1 + \theta$. Put $\delta_m = v(y_m z_m)$. Then $\delta_m = 1 + \theta - v(M_m)$, and $\delta_m$ decreases strictly to $0$. For $j \le m$ the monomials $y_j$, $z_j$, $M_j$ and $M_m / M_j$ have nonnegative exponents in $y_m, z_m$, and a series in $y_m, z_m$ has only a finite number of terms below each value.

For $f \in \hat H[X, W]$ the Hasse derivatives $f^{[k, l]}$ satisfy $f(X + S, W + T) = \sum_{k, l} f^{[k, l]}(X, W) S^k T^l$. In each characteristic,
$$\partial_X f^{[k, l]} = (k + 1) f^{[k + 1, l]}, \qquad \partial_W f^{[k, l]} = (l + 1) f^{[k, l + 1]}, \tag{18.1}$$
since the coefficient of $X^i W^j$ in $f^{[k, l]}$ is $\binom{i + k}{k} \binom{j + l}{l}$ times the coefficient of $X^{i + k} W^{j + l}$ in $f$, and $(i + 1) \binom{i + 1 + k}{k} = (k + 1) \binom{i + 1 + k}{k + 1}$. If $\deg f < p$ and $f^{[k + 1, l]} \ne 0$, then $k + 1 \le \deg f < p$, so $k + 1$ is a unit of $K$. The same holds for $l + 1$.

By Lemma 3.17.1, the function of $P_m$ is $M_m^{-p} g_m$, with $g_m$ the cleaning of $\sum_{k, l} A_{kl} x_m^k w_m^l$ and $A_{kl} = M_m^{k + l} g^{[k, l]}(\Phi_m)$. If $\deg_{x, w} g < p$, then only $A_{00}$ is cleaned, since $p \mid k$ and $p \mid l$ with $k + l < p$ give $k = l = 0$. The proof of Lemma 3.17.1 uses only two facts: the cleaning commutes with the substitution, and a monomial $c\, Y x^k w^l$ with $p \nmid k$ or $p \nmid l$ is not a $p$-th power. Both facts hold for a clean series $g \in K[[x, w, y, z]]$ in each free coordinate system in which the steps have the form above, so we use the closed form in this generality. By Lemma 3.17.2, part 2, each free coordinate system gives such a form of the run.

We use the following description of $\rho$. Write $g = y^{r_y} z^{r_z} G$. The generators of $\widetilde\Theta(G)$ are $G_x$, $G_w$, $r_y G + y G_y$ and $r_z G + z G_z$. Each of them maps distinct monomials of $G$ to distinct monomials or to $0$. So $\rho$ is the least value, over the monomials $x^i w^l y^j z^k$ of $G$ of degree $e$, of $e - 1$ if $p \nmid i$ or $p \nmid l$, of $e$ if $p \mid i$, $p \mid l$ and $p \nmid r_y + j$ or $p \nmid r_z + k$, and of $\infty$ otherwise. In particular, a monomial $x^i$ of $G$ with $p \nmid i$ gives $\rho \le i - 1$, since $G_x \in \widetilde\Theta(G)$ has the monomial $x^{i - 1}$ with a nonzero coefficient. The same holds for $w$. By Theorem 3.1.4, part 2, $\rho \ge d - 1$.

We also use the following fact. Let $g$ be clean in the coordinates $(x, w, y, z)$, and let $D_0$ be the largest monomial in $y, z$ that divides $g$. Then $D_0 = y^{r_y} z^{r_z}$. Indeed, $D_0$ divides $g_x$, $g_w$, $y g_y$ and $z g_z$, so $D_0$ divides $y^{r_y} z^{r_z}$ by Theorem 3.1.4, part 1. Conversely, let $c\, x^i w^l y^j z^k$ be a monomial of $g$. It is not a $p$-th power, so one of $i, l, j, k$ is not divisible by $p$, and then one of $g_x$, $g_w$, $y g_y$, $z g_z$ has a monomial with the exponents $j, k$ of $y, z$. Since $y^{r_y} z^{r_z}$ divides that generator, $j \ge r_y$ and $k \ge r_z$. So $y^{r_y} z^{r_z}$ divides $D_0$.

### Three lemmas

**Lemma 3.18.1.** Let $Q$ be a Laurent monomial in $y_N, z_N$ with $v(Q) > 0$, and write $Q = y_m^{e_m} z_m^{f_m}$. Then $e_m \to \infty$ and $f_m \to \infty$. In particular $Q$ is a monomial in $y_m, z_m$ with nonnegative exponents for $m$ large.

*Proof.* The monomial maps have the determinant $\pm 1$, so $(e_m, f_m)$ is well defined. A $y$-step gives $y_m^e z_m^f = y_{m+1}^{e + f} z_{m+1}^f$, so $(e, f) \mapsto (e + f, f)$, and a $z$-step gives $(e, f) \mapsto (e, e + f)$. Since $v(y_m), v(z_m) > 0$ and $v(Q) > 0$, at least one exponent is positive at each level.

If $e_m, f_m \ge 0$ at some $m$, they stay nonnegative. If one of them is $0$, the first step of the other letter makes both positive. When both are positive, a $y$-step adds $f \ge 1$ to $e$ and a $z$-step adds $e \ge 1$ to $f$. Both charts occur an infinite number of times, so both exponents go to infinity.

Assume $e_m < 0 < f_m$. A $y$-step keeps $f$ and adds $f$ to $e$. A $z$-step keeps $e$ and lowers $f$ by $|e| \ge 1$. So while $e < 0$, the exponent $f$ does not increase, and it decreases at each $z$-step. It stays positive, by the value. Since there are an infinite number of $z$-steps, $e$ does not stay negative, and at the first level with $e \ge 0$ we still have $f > 0$. So we are in the first case. The case $f_m < 0 < e_m$ is the same with the letters exchanged. $\square$

**Lemma 3.18.2.** Assume that an infinite number of the $b_j$ are not $0$, and let $f \in K[[y_N, z_N]][W]$ be nonzero. Let $c \nu$ be the term of least value of $f(\psi_\infty)$. Then there is an $m_0$ such that for each $m \ge m_0$, $\nu$ is a monomial in $y_m, z_m$ with nonnegative exponents and
$$f(\psi_m + M_m W) = c\, \nu\, \varepsilon_m, \qquad \varepsilon_m \in K[[W, y_m, z_m]], \quad \varepsilon_m - 1 \in y_m z_m K[[W, y_m, z_m]].$$

*Proof.* This is the proof of Proposition 3.15.10 with $f$ in place of $g_x$ and $(\psi_m)$ in place of $(\varphi_m)$. That proof uses only the sequence $\sum_j b_j M_{j+1}$ with an infinite number of nonzero $b_j$, through Lemma 3.15.8, and the dominance lemma. It does not use $g$, the cleaning or $\rho$. It gives a base point $P_{m'}$ at which the term $\nu_0$ of least value of $f(\psi_{m'})$ is the only term of $f(\psi_{m'} + M_{m'} W)$ with its exponent in $y_{m'}, z_{m'}$, and an $m_0$ such that for $m \ge m_0$ each other term of $f(\psi_m + M_m W)$ is $\nu_0$ times a monomial in $W, y_m, z_m$ whose exponents of $y_m$ and $z_m$ are both positive. So $f(\psi_m + M_m W) = \nu_0 \varepsilon_m$ with $\varepsilon_m - 1 \in y_m z_m K[[W, y_m, z_m]]$. The value of $\nu_0$ is $\beta_0 = v(f(\psi_\infty))$, and $f(\psi_\infty) - f(\psi_{m'})$ has a value larger than $\beta_0$ by the proof of Lemma 3.15.8, part 4. So $\nu_0 = c \nu$. If $\deg f = 0$, the same argument with $S$ the support of $f$ applies. $\square$

**Lemma 3.18.3.** Let $(x, w)$ be a free coordinate system at a point $P_m$ of the run, and assume that the function of $P_m$ is a $p$-th power of a Laurent monomial times $g_m = \sum_{k, l} B_{kl} x^k w^l$, a clean series with $B_{kl} \in K[[y_m, z_m]]$. If $B_{00} \ne 0$ and $v(B_{00}) < v(B_{kl})$ for each $(k, l) \ne (0, 0)$, then $\rho = 0$ at a later point of the run.

*Proof.* This is the proof of Proposition 3.17.3 in the coordinates of Lemma 3.17.2, part 2. Let $\mu_0$ be the term of least value of $B_{00}$ and let $S$ be the set of the exponents in $y_m, z_m$ of all the terms of $g_m$. The exponent $q_*$ of $\mu_0$ is the only point of $S$ of least value. The set $S$ may be infinite, which Lemma 3.15.4 allows, and the rest of the proof does not use that $g$ is a polynomial. $\square$

### Linear runs

In this part the run is linear with an infinite number of nonzero translations. The first step is a normal form.

**Proposition 3.18.4.** Let $g \in K[[y, z]][x, w]$ be clean at $P_N$ with $\deg_{x, w} g < p$, and let $P_N, P_{N+1}, \dots$ be a linear corner run in four variables with an infinite number of nonzero translations. Then, after a linear change of $(x, w)$, there are an $m_0$ and a free coordinate system $(x, w)$ at $P_{m_0}$, with $x = x_{m_0}$ and $w$ equal to $w_{m_0}$ times a unit, such that, with $y = y_{m_0}$ and $z = z_{m_0}$,
$$g_{m_0} = \sum_{i \in I} c_i D_i (1 + h_i)\, x^i + \mu\, w + C,$$
where $I \subseteq \{1, \dots, p - 1\}$, $c_i \in K^*$, $D_i$ is a monomial in $y, z$, $h_i \in y z K[[w, y, z]]$, $\mu$ is $0$ or a nonzero constant times a monomial in $y, z$, and $C \in K[[y, z]]$ is clean. The series $g_{m_0}$ is clean in $(x, w, y, z)$. In these coordinates the run from $P_{m_0}$ has the same points, charts and $\rho$, all the translations of $x$ are $0$, and the translations of $w$ are some $b''_j \in K$.

*Proof.* Let $\lambda$ be as in Definition 3.17.5, with $t^\lambda_j = 0$ for $j \ge J$. By Lemma 3.17.2, part 3, after a linear change of $(x, w)$ we may assume $\lambda = (1, 0)$, so $a_j = 0$ for $j \ge J$. A linear change keeps $\deg_{x, w}$ and the cleanness, since a monomial $x^i w^l$ with $1 \le i + l < p$ is not a $p$-th power. The steps do not raise $\deg_{x, w}$ (proof of Theorem 3.17.33). So we may start the run at $P_J$, and we rename $J$ as $N$. Then $a_j = 0$ for each $j$, an infinite number of the $b_j$ are not $0$, $\varphi_m = 0$, and $g = \sum_{i = 0}^{p - 1} x^i g_i(w)$ with $g_i \in K[[y, z]][w]$. The valuation is normalized at the new $N$, and nothing below depends on the normalization.

Since only $A_{00}$ is cleaned,
$$g_m = \sum_{i \ge 1} M_m^i g_i(\psi_m + M_m w_m)\, x_m^i + f_m, \qquad f_m = \operatorname{cl} f(\psi_m) + \sum_{l \ge 1} M_m^l f^{[l]}(\psi_m)\, w_m^l,$$
with $f = g_0$. Let $I$ be the set of the $i \ge 1$ with $g_i \ne 0$. Apply Lemma 3.18.2 to each $g_i$ with $i \in I$, and to $f_w$ if $f_w \ne 0$, and let $m_0$ be the largest of the indices that it gives. At $m_0$ this gives $M^i g_i(\psi + M w) = c_i D_i (1 + h_i)$ with $D_i = M_{m_0}^i \nu_i$, and $\partial_w f_{m_0} = M_{m_0} f_w(\psi + M w) = \mu \varepsilon'$ with $\mu = c' M_{m_0} \nu'$ and $\varepsilon'$ a unit. Write $f_{m_0} = \sum_l e_l w^l$. As in Corollary 3.15.11, $\mu$ divides $l e_l$ for each $l$, so it divides $e_l$ for $1 \le l < p$, and $e_1 = \mu \varepsilon'(0, y, z)$. Since $\deg_w f < p$, we get $f_{m_0} = \mu w'' + e_0$ with $w'' = \sum_{l \ge 1} (e_l / \mu) w^l$, and $w''$ is $w$ times a unit. Put $C = e_0 = \operatorname{cl} f(\psi_{m_0})$. If $f_w = 0$, then $f \in K[[y, z]]$, and we put $\mu = 0$ and $w'' = w$. Now write $w = w'' u$ with a unit $u \in K[[w'', y, z]]$. This substitution keeps $h_i \in y z K[[w'', y, z]]$. We rename $w''$ as $w$.

The series is clean in the new coordinates: a monomial with $x^i$, $1 \le i < p$, or with $w^1$ and no $x$, is not a $p$-th power, and $C$ is clean. By Lemma 3.17.2, part 2, the run from $P_{m_0}$ is a corner run in the coordinates $(x, w'')$. In the proof of that lemma, the new translation of a coordinate $x'' = f(y, z) + x u_{11} + w u_{12}$ is the value of $x'' / L$ at $P_{m+1}$. For $x'' = x$ we have $f = 0$, $u_{11} = 1$ and $u_{12} = 0$, so $x'' / L = x_{m+1} + a_m$, and the new translation is $a_m = 0$. The transforms $x_m$ of $x$ are the same as before, since $w''$ depends only on $(w, y, z)$ and does not enter the recursion of $x$. $\square$

**Lemma 3.18.5.** In the setting of Proposition 3.18.4, put $Q_i = (y_{m_0} z_{m_0})^i D_i$ for $i \in I$. If $\mu \ne 0$, write $\mu = c_\mu \mu_1$ with $\mu_1$ a monomial, and put $Q_W = y_{m_0} z_{m_0} \mu_1$. These are fixed Laurent monomials, with nonnegative exponents in $y_m, z_m$ for each $m \ge m_0$. Let $T$ be the set of the $j \ge m_0$ with $b''_j \ne 0$ and $Q_W / (y_{j+1} z_{j+1})$ not a $p$-th power, with $T = \emptyset$ if $\mu = 0$. Then for $m \ge m_0$, in the coordinates $(x_m, w_m, y_m, z_m)$ of the run of Proposition 3.18.4,
$$g_m = \sum_{i \in I} c_i \frac{Q_i}{(y_m z_m)^i} (1 + h_{i, m})\, x_m^i + c_\mu \frac{Q_W}{y_m z_m}\, w_m + C_m, \qquad C_m = C + \sum_{j \in T,\ m_0 \le j < m} b''_j c_\mu \frac{Q_W}{y_{j+1} z_{j+1}},$$
with $h_{i, m} \in y_m z_m K[[w_m, y_m, z_m]]$.

*Proof.* Put $M' = M_m / M_{m_0} = y_{m_0} z_{m_0} / (y_m z_m)$. By the closed form for the clean series $g_{m_0}$, we have $x_{m_0} = M' x_m$ and $w_{m_0} = \psi''_m + M' w_m$ with $\psi''_m = \sum_{m_0 \le j < m} b''_j M_{j+1} / M_{m_0}$, and $g_m$ is the cleaning of the substitution. The term $c_i D_i (1 + h_i) x^i$ goes to $c_i D_i M'^i (1 + \pi(h_i)) x_m^i$. It is not cleaned, since $p \nmid i$, and $D_i M'^i = Q_i / (y_m z_m)^i$. Since $y_{m_0} z_{m_0} = M' y_m z_m$, we have $\pi(h_i) \in y_m z_m K[[w_m, y_m, z_m]]$. The term $\mu w$ goes to $\mu M' w_m + \mu \psi''_m$, and the first part is not cleaned. The part without $x_m$ and $w_m$ is $C + \mu \psi''_m$. The series $C$ stays clean under the monomial maps, and $\mu M_{j+1} / M_{m_0} = c_\mu Q_W / (y_{j+1} z_{j+1})$ is a constant times one monomial. So the cleaning of this part is $C_m$. $\square$

This is Lemma 3.15.14 in the free coordinate $w$. Put $\kappa_i = v(Q_i)$, $\kappa_* = \min_{i \in I} \kappa_i$, with $\kappa_* = \infty$ if $I = \emptyset$, $\kappa_W = v(Q_W)$, with $\kappa_W = \infty$ if $\mu = 0$, and $\kappa_0 = \min(\kappa_*, \kappa_W)$. If $\kappa_* < \infty$, let $i_0$ be the largest $i \in I$ with $\kappa_i = \kappa_*$. Since two monomials with the same value are equal, $\kappa_i = \kappa_*$ gives $Q_i = Q_{i_0}$. In $\mathbb{K}$ put $C_\infty = C + \sum_{j \in T} b''_j c_\mu Q_W / (y_{j+1} z_{j+1})$. Its support is well ordered, since the values $\kappa_W - \delta_{j+1}$ of the added terms increase.

**Theorem 3.18.6.** Let $g \in K[[y, z]][x, w]$ be clean at $P_N$ with $\deg_{x, w} g < p$, and let $P_N, P_{N+1}, \dots$ be a linear corner run in four variables with an infinite number of nonzero translations. Let $(x, w)$ be the free coordinate system at $P_{m_0}$ of Proposition 3.18.4 and $(x_m, w_m)$ its transforms. Then there is an integer $d$ with $2 \le d < p$ such that for $m$ large:

1. $\operatorname{in} G_m = c\, x_m^d$ with $c \in K^*$, $d_m = d$ and $\rho = d - 1$. Here $x_m$ is a linear form in the coordinates of the run from $P_N$, and $\operatorname{in} G_m = c\, x_m^d$ also in these coordinates. So Hypothesis H1 holds for the run.
2. The corner curves $V(x_m, w_m, y_m)$ and $V(x_m, w_m, z_m)$ have $\nu^G = d = \rho + 1$.
3. The corner surfaces $V(x_m, y_m)$ and $V(x_m, z_m)$ have $\nu^G \ge \rho$.

So Conjectures 3.17.18 (L), 3.17.20 (L+) and 3.17.24 (L°) hold for the run, with the free coordinate system $(x, w)$ at $P_{m_0}$, and Question 3.13.18 has a positive answer for it.

Node: SG00000089

*Proof.* We work in the coordinates of Proposition 3.18.4 and Lemma 3.18.5. In these coordinates $g_m$ is clean, since it is the cleaning of the substitution.

Step 0: $I \ne \emptyset$ or $\mu \ne 0$. Otherwise $g_m = C_m = C$ for each $m$. It is not $0$, since $\operatorname{ord} g \ge p$, and all the other coefficients are $0$, so Lemma 3.18.3 gives $\rho = 0$ at a later point. This is false. So $\kappa_0 < \infty$.

Step 1: each term of $C_\infty$ has a value at least $\kappa_0$. At $P_m$, the coefficient of $x_m^i$, for $i \in I$, is $c_i Q_i (y_m z_m)^{-i} (1 + h_{i, m})$. Its coefficients of the powers of $w_m$ have values at least $\kappa_i - i \delta_m$. The coefficient of $w_m$ is $c_\mu Q_W / (y_m z_m)$, of value $\kappa_W - \delta_m$. There are no other coefficients $B_{kl}$ with $(k, l) \ne (0, 0)$, since $h_{i, m}$ has no $x_m$. So each $B_{kl}$ with $(k, l) \ne (0, 0)$ has a value at least
$$V_m = \min\Bigl(\min_{i \in I} (\kappa_i - i \delta_m),\ \kappa_W - \delta_m\Bigr),$$
and $V_m$ increases to $\kappa_0$. By Lemma 3.18.3, $C_m = 0$ or $v(C_m) \ge V_m$, for each $m$. Assume that $C_\infty$ has a term of value less than $\kappa_0$, and let $\tau$ be its term of least value. Choose $m$ with $V_m > v(\tau)$ and, if $\mu \ne 0$, with $\kappa_W - \delta_{m+1} > v(\tau)$. The terms of $C_\infty - C_m$ are the $b''_j c_\mu Q_W / (y_{j+1} z_{j+1})$ with $j \ge m$, of values $\kappa_W - \delta_{j+1} \ge \kappa_W - \delta_{m+1} > v(\tau)$. So $\tau$ is the term of least value of $C_m$, and $v(C_m) = v(\tau) < V_m$. This is a contradiction.

Step 2: the case $\kappa_W < \kappa_*$. Then $\mu \ne 0$. The terms $b''_j c_\mu Q_W / (y_{j+1} z_{j+1})$ with $j \in T$ have distinct monomials, of values $\kappa_W - \delta_{j+1} < \kappa_W = \kappa_0$. By Step 1 none of them is a term of $C_\infty$, so each of them cancels a term of $C$. But $C$ has only a finite number of terms of value less than $\kappa_W$. So $T$ is finite. Let $J'$ be its largest element, or $J' = m_0 - 1$ if $T = \emptyset$. For $m > J'$ we have $C_m = C_\infty =: C'$. This is a series in $y_{J'+1}, z_{J'+1}$, and its terms have values at least $\kappa_W$. The only monomial of value $\kappa_W$ is $Q_W$. Apply Lemma 3.15.4 at the base point $P_{J'+1}$ with $S$ the support of $C'$ together with the exponent of $Q_W$. For $m$ large, each term of $C'$ that is not a multiple of $Q_W$ has both exponents in $y_m, z_m$ larger than those of $Q_W$. So $C' = Q_W C''$ with $C'' \in K[[y_m, z_m]]$. For $i \in I$ the monomial $Q_i / Q_W$ has a positive value, so by Lemma 3.18.1 its exponents are at least $i - 1$ for $m$ large. Then
$$g_m = c_\mu \frac{Q_W}{y_m z_m} H, \qquad H = w_m + \sum_{i \in I} \frac{c_i}{c_\mu} \frac{Q_i}{Q_W} (y_m z_m)^{1 - i} (1 + h_{i, m})\, x_m^i + \frac{y_m z_m C''}{c_\mu},$$
with $H \in K[[x_m, w_m, y_m, z_m]]$. The monomial $w_m$ occurs in $H$ with the coefficient $1$, since the other terms contain $x_m$ or are in $(y_m z_m)$. So $H$ is not divisible by $y_m$ or $z_m$. By the fact at the end of the setting, $y^{r_y} z^{r_z}$ is the monomial of $Q_W / (y_m z_m)$, and $G_m$ is a constant times $H$. The monomial $w_m$ of $G_m$ gives $\rho = 0$. This contradicts $\rho \ge 1$. So $\kappa_* \le \kappa_W$, and $I \ne \emptyset$.

Step 3: the case $\kappa_W = \kappa_*$. As in Step 2, $T$ is finite and $C_m = C'$ for $m$ large, with all terms of value at least $\kappa_W = \kappa_*$, and $Q_W = Q_{i_0}$. Lemma 3.15.4 at $P_{J'+1}$ gives $C_m = Q_{i_0} C''_m$ with $C''_m \in K[[y_m, z_m]]$ for $m$ large.

Step 4: the case $\kappa_W > \kappa_*$, which includes $\mu = 0$. Now $T$ can be infinite, and we need an argument that is uniform in the translations. Choose $m_1 \ge m_0$ with $\delta_{m_1 + 1} < \kappa_W - \kappa_*$, or any $m_1 \ge m_0$ if $\mu = 0$. For $m > m_1$,
$$C_m = C_{m_1} + \sum_{j \in T,\ m_1 \le j < m} b''_j c_\mu \frac{Q_W}{y_{j+1} z_{j+1}}.$$
First the part $C_{m_1}$. We have $C_{m_1} = C_\infty - \sum_{j \in T, j \ge m_1} b''_j c_\mu Q_W / (y_{j+1} z_{j+1})$, and the subtracted terms have values $\kappa_W - \delta_{j+1} \ge \kappa_W - \delta_{m_1+1} > \kappa_*$. With Step 1, each term of $C_{m_1}$ has a value at least $\kappa_*$, and only a multiple of $Q_{i_0}$ can have the value $\kappa_*$. The series $C_{m_1}$ is in $K[[y_{m_1}, z_{m_1}]]$, and $Q_{i_0}$ is a monomial in $y_{m_1}, z_{m_1}$ with nonnegative exponents. Lemma 3.15.4 at the base point $P_{m_1}$, with $S$ the support of $C_{m_1}$ together with the exponent of $Q_{i_0}$, gives an $m_2$ such that $Q_{i_0}$ divides $C_{m_1}$ in $K[[y_m, z_m]]$ for $m \ge m_2$.

Next the translation terms. Put $Q'' = Q_W / (Q_{i_0}\, y_{m_1+1} z_{m_1+1})$. It is a fixed Laurent monomial of value $\kappa_W - \kappa_* - \delta_{m_1+1} > 0$, so by Lemma 3.18.1 it has nonnegative exponents in $y_m, z_m$ for $m \ge m_3$. For $m_1 \le j < m$,
$$\frac{Q_W}{Q_{i_0}\, y_{j+1} z_{j+1}} = Q'' \cdot \frac{y_{m_1+1} z_{m_1+1}}{y_{j+1} z_{j+1}},$$
and the last factor is $M_{j+1} / M_{m_1+1}$, a product of chart variables $L_k$ with $m_1 + 1 \le k \le j$. So it has nonnegative exponents in $y_m, z_m$. So $Q_{i_0}$ divides each translation term in $K[[y_m, z_m]]$ for $m \ge m_3$, for all $j$ at once.

So in Steps 3 and 4, for $m$ large, $C_m = Q_{i_0} C''_m$ with $C''_m \in K[[y_m, z_m]]$.

Step 5: the form of $G_m$. Let $m$ be large. For $i \in I$ with $\kappa_i > \kappa_*$, the monomial $Q_i / Q_{i_0}$ has a positive value, and by Lemma 3.18.1 its exponents are at least $\max(i - i_0, 0) + i_0 + 1$. In Step 4 with $\mu \ne 0$, $Q_W / Q_{i_0}$ has a positive value, and its exponents are at least $i_0 + 1$. Put $D = c_{i_0} Q_{i_0} / (y_m z_m)^{i_0}$. Then $g_m = D H$ with
$$H = (1 + h_{i_0, m}) x_m^{i_0} + \sum_{\substack{i \in I,\ i < i_0 \\ \kappa_i = \kappa_*}} \frac{c_i}{c_{i_0}} (y_m z_m)^{i_0 - i} (1 + h_{i, m}) x_m^i + \sum_{\substack{i \in I \\ \kappa_i > \kappa_*}} \frac{c_i}{c_{i_0}} \frac{Q_i}{Q_{i_0}} (y_m z_m)^{i_0 - i} (1 + h_{i, m}) x_m^i + \frac{c_\mu}{c_{i_0}} \frac{Q_W}{Q_{i_0}} (y_m z_m)^{i_0 - 1} w_m + \frac{(y_m z_m)^{i_0} C''_m}{c_{i_0}},$$
and each coefficient is a series. The monomial $x_m^{i_0}$ occurs only in the first term, so $H$ is not divisible by $y_m$ or $z_m$. By the fact at the end of the setting, the monomial of $D$ is $y_m^{r_y} z_m^{r_z}$, and $G_m = c_{i_0} H$. We compare each term with $x_m^{i_0}$.

- The terms of $x_m^{i_0} h_{i_0, m}$ are in $y_m z_m x_m^{i_0} K[[w_m, y_m, z_m]]$.
- A tied term $(y_m z_m)^{i_0 - i} x_m^i$ with $i < i_0$ has the degree $2 i_0 - i > i_0$. Its exponent of $y_m$ plus $i$ is $i_0$, and the same holds for $z_m$.
- An untied term has the exponents of $y_m$ and $z_m$ at least $i_0 + 1$. So its degree is larger than $i_0$, and $i$ plus each exponent is larger than $i_0$.
- The $w_m$-term. In Step 3, $Q_W = Q_{i_0}$, and the term is $(c_\mu / c_{i_0}) (y_m z_m)^{i_0 - 1} w_m$, of degree $2 i_0 - 1$. In Step 4 it is $0$ or its exponents of $y_m$ and of $z_m$ are at least $2 i_0$.
- The last term has both exponents at least $i_0$, and its degree is at least $2 i_0$.

If $i_0 = 1$, then $G_m$ has the monomial $x_m$, so $\rho = 0$. This is a contradiction, so $i_0 \ge 2$. Then each term other than $x_m^{i_0}$ has a degree larger than $i_0$; in Step 3 this uses $2 i_0 - 1 > i_0$. So $\operatorname{in} G_m = c_{i_0} x_m^{i_0}$, and $d = i_0 < p$. We have $\rho \ge d - 1$, and the monomial $x_m^{i_0}$ with $p \nmid i_0$ gives $\rho \le i_0 - 1$. So $\rho = d - 1$.

It remains to pass to the coordinates of the run from $P_N$. These differ from ours in two ways. First, the linear change at the start of the proof of Proposition 3.18.4. Since $\deg_{x, w} g_m < p$, the cleaning removes only terms without $x_m$ and $w_m$, so it commutes with a linear change of $(x_m, w_m)$, and the initial form changes by the linear map. Second, the change from $w''_m$ to $w_m$, which fixes $x_m$, $y_m$ and $z_m$. Let $\hat g$ be $g_m$ written in the other coordinates by this substitution. The function of $P_m$ in the other coordinates is the cleaning of $\hat g$, and $\hat g = y_m^{r_y} z_m^{r_z} \hat G$ with $\operatorname{in} \hat G = c_{i_0} x_m^{i_0}$, since the change of a regular system of parameters acts on the initial form by its linear part, and this linear part fixes $x_m$. The cleaning removes monomials and adds none, and it does not remove $y_m^{r_y} z_m^{r_z} x_m^{i_0}$, since $p \nmid i_0$. So the new $G_m$ has no monomial of degree less than $i_0$, and its part of degree $i_0$ is $c_{i_0} x_m^{i_0}$. This is part 1.

Step 6: the curves and the surfaces. The coordinates $(x_m, w_m, y_m, z_m)$ are adapted to the curves and the surfaces of the theorem, and $g_m$ is clean in them. So by Lemma 3.13.1 and Definition 3.13.2, $\nu^G$ of $V(x_m, w_m, y_m)$ is the least value of $i + l + j$ over the monomials $x^i w^l y^j z^k$ of $G_m$, and $\nu^G$ of $V(x_m, y_m)$ is the least value of $i + j$. The same holds with $z$ in place of $y$. By the list in Step 5, each monomial of $G_m$ has $i + l + j \ge i_0$ and $i + l + k \ge i_0$. For the tied terms this is an equality, and for the $w_m$-term of Step 3 we have $1 + (i_0 - 1) = i_0$. So $\nu^G \ge d$ on both corner curves, and $\nu^G \le \operatorname{ord} G_m = d$. This is part 2. For the surfaces, the least value of $i + j$ is at least $i_0$ for all the terms except the $w_m$-term of Step 3, for which it is $i_0 - 1 = \rho$. This is part 3. The points lie on the strict transforms of $V(x_{m_0})$, since the translations of $x$ are $0$, by the fact on hypersurfaces in the proof of Lemma 3.17.6. $\square$

The proof shows more. In Step 3 only a finite number of the $b''_j$ have $Q_W / (y_{j+1} z_{j+1})$ not a $p$-th power. In Step 4 the argument allows all the translations of $w$, and the only obstruction to $\rho \ge 1$ is $i_0 = 1$. The corner surfaces have $\nu^G = \rho$ only in Step 3, when the coefficient of $(y_m z_m)^{i_0 - 1} w_m$ is not $0$, and $\nu^G = d$ in the other cases. Examples 3.18.20 and 3.18.21 show the two cases.

Where is the linearity used? With $a_j = 0$, the coefficient of $x^i$ is $M^i g_i(\psi_m + M w)$, a polynomial in the single sequence $(\psi_m)$, and Lemma 3.18.2 makes it a fixed Laurent monomial times $M^i$ times a unit. In a planar run the coefficient of $x^k w^l$ is $M^{k + l} g^{[k, l]}(\varphi_m, \psi_m)$, a polynomial in two sequences, and the rest of the section treats this case.

**Corollary 3.18.7.** Let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g < p$, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables that is not planar. Then Hypothesis H1 and Conjectures L and L° hold for the run, and $d = \rho + 1$ for $m$ large.

Node: SG0000008A

*Proof.* If all the translations are $0$ from some point on, the run is an origin run from some point on. Then Theorem 3.14.7, part 2, gives a binary initial form of $G_m$ for $m$ large, which is H1, and part 3 gives the corner curves with $\nu^G = d_m \ge \rho$. Conjecture L holds with $x' = x_J$ for $J$ after the last nonzero translation. The initial form is binary of degree $d < p$, since $\deg_{x, w} g_m < p$, so one of its derivatives in $x, w$ is not $0$, and Theorem 3.1.4, part 3, gives $d = \rho + 1$. Otherwise the run is linear with an infinite number of nonzero translations, and Theorem 3.18.6 applies. $\square$

So for $\deg_{x, w} g < p$ the hypothesis H1 holds for each corner run of $g$ if and only if $g$ has no planar corner run. Indeed, both cases of Theorem 3.17.33 are linear runs, and Corollary 3.18.7 gives the converse. The next part proves that there is no planar corner run.

### Planar runs and Statement D

In this part the run is planar. An element of $\mathbb{K}$ is *of finite type* if it has only a finite number of terms below each value. Let $\mathbb{F} \subseteq \mathbb{K}$ be the set of the elements of finite type.

**Lemma 3.18.8.** The set $\mathbb{F}$ is a subfield of $\mathbb{K}$. It contains $\hat H$ and, for each $f \in \hat H[X, W]$ and each $m$, the element $f(\Phi_m)$.

Node: SG0000008B

*Proof.* We have $\hat H \subseteq \mathbb{F}$ by Lemma 3.15.6, part 2. Sums are clear. Products: let $A, B \in \mathbb{F}$ be nonzero, and let $V$ be a value. A term of $A B$ of value less than $V$ comes from a term $s$ of $A$ and a term $t$ of $B$ with $v(s) + v(t) < V$, so $v(s) < V - v(B)$ and $v(t) < V - v(A)$, and there are a finite number of such pairs. Inverses: let $A \ne 0$, let $c \nu$ be its term of least value, which exists since $A$ has a finite number of terms below each value, and write $A = c \nu (1 + \varepsilon)$. Then $\varepsilon \in \mathbb{F}$, and its terms have values at least $s_0 = v(\varepsilon) > 0$. A term of $\varepsilon^n$ has a value at least $n s_0$, so only the $n < V / s_0$ give terms below $V$, and each of them gives a finite number. So $(1 + \varepsilon)^{-1} = \sum_n (-\varepsilon)^n$ is in $\mathbb{F}$, and so is $A^{-1}$. The last claim holds since $\varphi_m$ and $\psi_m$ are finite sums of terms, so they are in $H$. $\square$

If the run has an infinite number of nonzero translations, then $\varphi_\infty$ or $\psi_\infty$ is not in $\mathbb{F}$, since it has an infinite number of terms below $1 + \theta$.

**Lemma 3.18.9.** Let $\alpha, \beta, \gamma \in \hat H$ with $(\alpha, \beta) \ne (0, 0)$. Then
$$v(\alpha \varphi_\infty + \beta \psi_\infty + \gamma) < \min(v(\alpha), v(\beta)) + 1 + \theta.$$
In particular $\alpha \varphi_\infty + \beta \psi_\infty + \gamma \ne 0$, and $v(\alpha \varphi_m + \beta \psi_m + \gamma)$ is constant for $m$ large.

Node: SG0000008C

*Proof.* By symmetry we may assume $\alpha \ne 0$ and $v(\alpha) \le v(\beta)$, with $v(0) = \infty$. Put $u = \beta / \alpha \in \hat H$. Then $v(u) \ge 0$. The only Laurent monomial of value $0$ is $1$, so $u = c + u'$ with $c \in K$ the coefficient of $1$ in $u$ and $v(u') > 0$. Write
$$\frac{\alpha \varphi_\infty + \beta \psi_\infty + \gamma}{\alpha} = (\varphi_\infty + c \psi_\infty) + u' \psi_\infty + \frac{\gamma}{\alpha}.$$
The first summand is $\sum_j (a_j + c b_j) M_{j+1}$. Since the run is planar, the direction $\lambda = (1, c)$ has an infinite number of nonzero $t^\lambda_j = a_j + c b_j$. The monomials $M_{j+1}$ are distinct, with values less than $1 + \theta$. So the first summand has an infinite number of terms of value less than $1 + \theta$.

The second summand has only a finite number of terms of value less than $1 + \theta$. Indeed, let $s_0 = v(u') > 0$. A term of $u' \psi_\infty$ of value less than $1 + \theta$ comes from a term of $u'$ of value less than $1 + \theta$ and a term $b_j M_{j+1}$ of value less than $1 + \theta - s_0$. By Lemma 3.15.6, part 2, $u'$ has a finite number of terms below $1 + \theta$, and since $v(M_{j+1})$ increases strictly to $1 + \theta$, only a finite number of $j$ have $v(M_{j+1}) < 1 + \theta - s_0$. The third summand $\gamma / \alpha \in \hat H$ has a finite number of terms below $1 + \theta$ by Lemma 3.15.6, part 2.

So the sum has an infinite number of terms below $1 + \theta$. It is not $0$, and its value is less than $1 + \theta$. Multiplication by $\alpha$ gives the inequality, since $v(\alpha) = \min(v(\alpha), v(\beta))$. For the last claim, the difference of $\alpha \varphi_\infty + \beta \psi_\infty + \gamma$ and $\alpha \varphi_m + \beta \psi_m + \gamma$ has a value at least $\min(v(\alpha), v(\beta)) + v(M_{m+1})$ by Lemma 3.15.6, part 3, and $v(M_{m+1}) \to 1 + \theta$. So for $m$ large this difference has a value larger than $v(\alpha \varphi_\infty + \beta \psi_\infty + \gamma)$. $\square$

The proof uses only that $u'$ and $\gamma / \alpha$ are of finite type, so it applies to coefficients in $\mathbb{F}$ and to each tail of the run. For $m \ge N$ put
$$\Delta_m = \Phi_\infty - \Phi_m = (\Delta\varphi, \Delta\psi), \qquad \Delta\varphi = \sum_{j \ge m} a_j M_{j+1}, \quad \Delta\psi = \sum_{j \ge m} b_j M_{j+1}.$$

**Lemma 3.18.10.** Let $m \ge N$, and let $\alpha, \beta, \gamma \in \mathbb{F}$ with $(\alpha, \beta) \ne (0, 0)$. Then
$$v(\gamma + \alpha\, \Delta\varphi + \beta\, \Delta\psi) < \min(v(\alpha), v(\beta)) + 1 + \theta.$$

Node: SG0000008D

*Proof.* This is the proof of Lemma 3.18.9 with $\Delta_m$ in place of $\Phi_\infty$. Assume $v(\alpha) \le v(\beta)$, so $\alpha \ne 0$, and put $u = \beta / \alpha$, which is in $\mathbb{F}$ by Lemma 3.18.8. Then $v(u) \ge 0$, so $u = c + u'$ with $c \in K$ and $v(u') > 0$. Write
$$\frac{\gamma + \alpha \Delta\varphi + \beta \Delta\psi}{\alpha} = \sum_{j \ge m} (a_j + c b_j) M_{j+1} + u' \Delta\psi + \frac{\gamma}{\alpha}.$$
By planarity for $\lambda = (1, c)$, an infinite number of the $a_j + c b_j$ with $j \ge m$ are not $0$, and the $M_{j+1}$ are distinct with values below $1 + \theta$. So the first sum has an infinite number of terms below $1 + \theta$. The element $u' \Delta\psi$ has a finite number of terms below $1 + \theta$, since $u'$ has a finite number of terms below $1 + \theta$ and only a finite number of $j$ have $v(M_{j+1}) < 1 + \theta - v(u')$. The element $\gamma / \alpha$ is in $\mathbb{F}$. So the sum has an infinite number of terms below $1 + \theta$, its value is less than $1 + \theta$, and we multiply by $\alpha$. $\square$

For $f \in \hat H[X, W]$ with $f \ne 0$ and for $s \ge 0$ put
$$\lambda_s(f) = \min_{k + l = s} v\bigl(f^{[k, l]}(\Phi_\infty)\bigr),$$
with $v(0) = \infty$. So $\lambda_0(f) = v(f(\Phi_\infty))$ and $\lambda_1(f) = \min(v(f_X(\Phi_\infty)), v(f_W(\Phi_\infty)))$. The next theorem is the two-variable form of Lemma 3.15.8, parts 1 and 3, for $\deg f < p$. We call it Statement D.

**Theorem 3.18.11.** Let the run be planar, and let $f \in \hat H[X, W]$ be nonzero with $\deg f < p$. Then:

1. $f(\Phi_\infty) \ne 0$, and if $\deg f \ge 1$, then $v(f(\Phi_\infty)) < \lambda_1(f) + 1 + \theta$.
2. $v(f(\Phi_\infty) - f(\Phi_m)) > v(f(\Phi_\infty))$ for $m$ large. So $v(f(\Phi_m)) = v(f(\Phi_\infty))$ for $m$ large, and the term of least value of $f(\Phi_m)$ is that of $f(\Phi_\infty)$.
3. $\lambda_{s - 1}(f) < \lambda_s(f) + 1 + \theta$ for $1 \le s \le \deg f$, and $\lambda_s(f) = \infty$ if and only if $s > \deg f$. In particular, for each $(k, l) \ne (0, 0)$ with $f^{[k, l]} \ne 0$,
$$v(f(\Phi_\infty)) < v\bigl(f^{[k, l]}(\Phi_\infty)\bigr) + (k + l)(1 + \theta).$$

Node: SG0000008E

*Proof.* Induction on $D = \deg f$. If $D = 0$, then $f$ is a nonzero element of $\hat H$, and the three claims are clear. Let $D \ge 1$, assume the theorem for all nonzero $h$ with $\deg h < D$, and write $\lambda_s = \lambda_s(f)$.

Step 0: the derivatives. For $(k, l) \ne (0, 0)$ the polynomial $f^{[k, l]}$ has a degree less than $D$, so the induction hypothesis applies to it when it is not $0$. Hence $f^{[k, l]}(\Phi_\infty) \ne 0$ when $f^{[k, l]} \ne 0$, and there is an $m_0$ such that $v(f^{[k, l]}(\Phi_m)) = v(f^{[k, l]}(\Phi_\infty))$ for each $m \ge m_0$ and each of the finite number of $(k, l) \ne (0, 0)$ with $f^{[k, l]} \ne 0$. By (18.1), if $f^{[K, L]} \ne 0$ with $K + L = s \ge 1$, then $f^{[K - 1, L]} \ne 0$ when $K \ge 1$, and $f^{[K, L - 1]} \ne 0$ when $L \ge 1$. A monomial $X^i W^j$ of $f$ of degree $D$ gives $f^{[i, j]} \ne 0$. So $\lambda_s < \infty$ for $s \le D$, and $\lambda_s = \infty$ for $s > D$, since then $f^{[k, l]} = 0$.

Step 1: the chain. Let $2 \le s \le D$, and let $(K, L)$ with $K + L = s$ and $f^{[K, L]} \ne 0$. Say $K \ge 1$, else exchange the roles of $X$ and $W$, and put $h = f^{[K - 1, L]}$. By (18.1), $\partial_X h = K f^{[K, L]}$ with $K$ a unit, so $h \ne 0$ and $\deg h \ge 1$. Also $\deg h \le D - (s - 1) < D$. By part 1 for $h$,
$$\lambda_{s - 1} \le v(h(\Phi_\infty)) < \lambda_1(h) + 1 + \theta \le v(\partial_X h(\Phi_\infty)) + 1 + \theta = v\bigl(f^{[K, L]}(\Phi_\infty)\bigr) + 1 + \theta.$$
The minimum over $(K, L)$ gives $\lambda_{s - 1} < \lambda_s + 1 + \theta$. The sum of these inequalities for $2, \dots, s$ gives
$$\lambda_1 + (1 + \theta) < \lambda_s + s (1 + \theta) \qquad (2 \le s \le D). \tag{18.2}$$

Step 2: the linear part. Let $m \ge m_0$. Taylor's formula at $\Phi_m$ gives
$$f(\Phi_\infty) = B_m + H_m, \qquad B_m = f(\Phi_m) + f_X(\Phi_m)\, \Delta\varphi + f_W(\Phi_m)\, \Delta\psi, \qquad H_m = \sum_{k + l \ge 2} f^{[k, l]}(\Phi_m)\, \Delta\varphi^k \Delta\psi^l.$$
The coefficients $f(\Phi_m)$, $f_X(\Phi_m)$ and $f_W(\Phi_m)$ are in $\mathbb{F}$ by Lemma 3.18.8, and by Step 0, $\min(v(f_X(\Phi_m)), v(f_W(\Phi_m))) = \lambda_1 < \infty$. So Lemma 3.18.10 gives
$$v(B_m) < \lambda_1 + 1 + \theta.$$

Step 3: the higher terms. Since $v(\Delta\varphi), v(\Delta\psi) \ge v(M_{m+1})$, Step 0 gives $v(H_m) \ge \min_{2 \le s \le D} (\lambda_s + s\, v(M_{m+1}))$, with $H_m = 0$ if $D = 1$. Let $\delta > 0$ be the least of the differences $\lambda_s + s (1 + \theta) - \lambda_1 - (1 + \theta)$ in (18.2). Since $v(M_{m+1}) \to 1 + \theta$, for $m$ large we have $s (1 + \theta - v(M_{m+1})) < \delta$ for each $s \le D$, so $v(H_m) > \lambda_1 + 1 + \theta > v(B_m)$. So $v(f(\Phi_\infty)) = v(B_m) < \lambda_1 + 1 + \theta$, and in particular $f(\Phi_\infty) \ne 0$. This is part 1.

Step 4: parts 2 and 3. The difference $f(\Phi_\infty) - f(\Phi_m) = f_X(\Phi_m) \Delta\varphi + f_W(\Phi_m) \Delta\psi + H_m$ has a value at least $\min(\lambda_1 + v(M_{m+1}), v(H_m))$ for $m \ge m_0$. For $m$ large, $\lambda_1 + v(M_{m+1})$ is larger than $v(f(\Phi_\infty))$ by part 1, and $v(H_m) > \lambda_1 + 1 + \theta$ by Step 3. This gives part 2. Part 3 is part 1 for $s = 1$, Step 1 for $s \ge 2$, and Step 0 for the values $\infty$. The displayed inequality is the sum of the inequalities of the chain from $1$ to $k + l$. $\square$

**Remark 3.18.12.** Theorem 3.18.11 proves Conjecture T of Remark 3.17.34 for the planar runs and the polynomials $f$ with $\deg f < p$. No factorization into linear factors and no theory of Kaplansky type in two variables is used. The induction replaces the factorization of Proposition 3.15.7: the Taylor expansion at $\Phi_m$ reduces the claim to Lemma 3.18.10, applied to the tail $\Delta_m$ with the coefficients $f_X(\Phi_m)$ and $f_W(\Phi_m)$, and the chain (18.2), which is part 1 for the derivatives, makes the higher terms small. This works because Lemma 3.18.10 holds for coefficients in the field $\mathbb{F}$, which contains $f_X(\Phi_m)$ but not $\Phi_\infty$. The hypothesis $\deg f < p$ is used only through (18.1), in Steps 0 and 1. For $f = X^p - \gamma$ the derivatives $f_X$ and $f_W$ are $0$, so $\lambda_1 = \infty$, part 1 says nothing, and the chain breaks. In one variable this is the case of a dominant index $h > 1$ (Lemma 3.15.8 and Remark 3.15.13), where Section 3.15 uses the transcendental type of Proposition 3.15.7. For a pair of sequences we have no substitute, and Conjecture T stays open for $\deg f \ge p$. For a linear run the theorem is false: if $a_j = 0$ for $j \ge J$, then $f = X - \varphi_J$ has $f(\Phi_\infty) = 0$. In the proof, Lemma 3.18.10 fails for $(\alpha, \beta) = (1, 0)$.

### Dominance and the planar runs

The next two propositions turn Statement D into the form of Proposition 3.15.10: a polynomial in the translated coordinates is a fixed monomial times a unit. The first is the case of degree $1$, which already gives the case $\deg_{x, w} g = 2$. The second is the general case.

**Proposition 3.18.13.** Let the run be planar, and let
$$F_m = M_m (\alpha_1 \varphi_m + \beta_1 \psi_m + \gamma_1) + M_m^2 (\alpha_1 x_m + \beta_1 w_m)$$
with $\alpha_1, \beta_1, \gamma_1 \in K[[y_N, z_N]]$ and $(\alpha_1, \beta_1) \ne (0, 0)$. Then there are a Laurent monomial $\nu$, a constant $c \ne 0$ and an $m_0$ such that for $m \ge m_0$, $\nu$ has nonnegative exponents in $y_m, z_m$ and $F_m = c\, M_m \nu\, \varepsilon_m$ with $\varepsilon_m$ a unit of $K[[x_m, w_m, y_m, z_m]]$. The same holds if $(\alpha_1, \beta_1) = (0, 0)$ and $\gamma_1 \ne 0$, with $F_m = M_m \gamma_1$.

Node: SG0000008F

*Proof.* The last case is the dominance lemma at $P_N$ for the support of $\gamma_1$. Otherwise put $f_m = \alpha_1 \varphi_m + \beta_1 \psi_m + \gamma_1$ and $f_\infty = \alpha_1 \varphi_\infty + \beta_1 \psi_\infty + \gamma_1$, and let $c \nu$ be the term of least value of $f_\infty$. Put $v_0 = \min(v(\alpha_1), v(\beta_1))$. By Lemma 3.18.9, $v(\nu) < v_0 + 1 + \theta$.

By the dominance lemma at $P_N$, for $m$ large each nonzero one of $\alpha_1$ and $\beta_1$ is a monomial $\nu_\alpha$ or $\nu_\beta$ times a unit of $K[[y_m, z_m]]$, and $v(\nu_\alpha), v(\nu_\beta) \ge v_0$. Choose $m_1$ with $v(M_{m_1 + 1}) > v(\nu) - v_0$. This is possible, since $v(\nu) - v_0 < 1 + \theta$. For $m > m_1$,
$$f_m = f_{m_1} + \sum_{m_1 \le j < m} (\alpha_1 a_j + \beta_1 b_j) M_{j+1}.$$
The terms of $f_\infty - f_{m_1}$ have values at least $v_0 + v(M_{m_1 + 1}) > v(\nu)$, so $c \nu$ is the only term of least value of $f_{m_1} \in K[[y_{m_1}, z_{m_1}]]$. The dominance lemma at the base point $P_{m_1}$, with $S$ the support of $f_{m_1}$, gives an $m_2$ such that for $m \ge m_2$ each other term of $f_{m_1}$ has both exponents in $y_m, z_m$ larger than those of $\nu$. For the translation terms, write $\alpha_1 M_{j+1} = \nu \cdot (\nu_\alpha M_{m_1 + 1} / \nu) \cdot (M_{j+1} / M_{m_1 + 1}) \cdot \varepsilon_\alpha$ with a unit $\varepsilon_\alpha$. The middle factor is a fixed Laurent monomial of value at least $v_0 + v(M_{m_1 + 1}) - v(\nu) > 0$, so by Lemma 3.18.1 both its exponents are positive for $m$ large. The factor $M_{j+1} / M_{m_1 + 1}$ is a product of chart variables $L_k$ with $k \le j < m$, so it has nonnegative exponents at the level $m$. This holds for all $j$ at once, as in Step 4 of the proof of Theorem 3.18.6. The same holds for $\beta_1$, and for the terms $M_m^2 \alpha_1 x_m$ and $M_m^2 \beta_1 w_m$, with $M_m / M_{m_1 + 1}$ in place of $M_{j+1} / M_{m_1 + 1}$. So $F_m = c M_m \nu (1 + h)$ with $h$ in the maximal ideal. $\square$

**Proposition 3.18.14.** Let the run be planar, and let $f \in K[[y_N, z_N]][X, W]$ be nonzero with $\deg f < p$. Let $c \nu$ be the term of least value of $f(\Phi_\infty)$, which exists by Theorem 3.18.11. Then there is an $m_2$ such that for each $m \ge m_2$, $\nu$ is a monomial in $y_m, z_m$ with nonnegative exponents and
$$F_m := f(\varphi_m + M_m x_m, \psi_m + M_m w_m) = c\, \nu\, (1 + h_m), \qquad h_m \in (x_m, w_m, y_m, z_m)\, K[[y_m, z_m]][x_m, w_m].$$

Node: SG0000008G

*Proof.* If $\deg f = 0$, this is the dominance lemma at $P_N$ with $S$ the support of $f$. Let $D = \deg f \ge 1$ and $V = v(f(\Phi_\infty))$. By Theorem 3.18.11, parts 2 and 3, there is an $m_1$ with the following properties.

1. $v(f^{[k, l]}(\Phi_{m_1})) = v(f^{[k, l]}(\Phi_\infty))$ for all $(k, l)$ with $f^{[k, l]} \ne 0$.
2. $v(f(\Phi_\infty) - f(\Phi_{m_1})) > V$. So $c \nu$ is the only term of least value of $f(\Phi_{m_1})$, and $v(f(\Phi_{m_1})) = V$.
3. $\lambda_s(f) + s\, v(M_{m_1 + 1}) > V$ for $1 \le s \le D$. This is possible, since $V < \lambda_s(f) + s(1 + \theta)$ by Theorem 3.18.11, part 3.

Let $m > m_1$. Then $\varphi_m + M_m x_m = \varphi_{m_1} + E$ with $E = \sum_{m_1 \le j < m} a_j M_{j+1} + M_m x_m$, and in the same way $\psi_m + M_m w_m = \psi_{m_1} + E'$. Each monomial of $E$ and $E'$ is $M_{m_1 + 1}$ times $M_{j+1} / M_{m_1 + 1}$, or times $(M_m / M_{m_1 + 1}) x_m$ or $(M_m / M_{m_1 + 1}) w_m$, and these have nonnegative exponents at the level $m$. So by Taylor's formula
$$F_m = \sum_{k, l} \bigl(f^{[k, l]}(\Phi_{m_1}) M_{m_1 + 1}^{k + l}\bigr)\, Q_{kl}, \qquad Q_{kl} = (E / M_{m_1 + 1})^k (E' / M_{m_1 + 1})^l,$$
with $Q_{00} = 1$ and each $Q_{kl}$ a polynomial in $x_m, w_m, y_m, z_m$.

The elements $f^{[k, l]}(\Phi_{m_1}) M_{m_1 + 1}^{k + l}$ are power series in $y_{m_1 + 1}, z_{m_1 + 1}$. Let $S \subseteq \mathbb{N}^2$ be the union of their supports, in the exponents at the base point $P_{m_1 + 1}$. By property 2, the exponent $q_*$ of $\nu$ is the only point of least value in the support of $f(\Phi_{m_1})$. By properties 1 and 3, each term of $f^{[k, l]}(\Phi_{m_1}) M_{m_1 + 1}^{k + l}$ with $k + l = s \ge 1$ has a value at least $\lambda_s(f) + s\, v(M_{m_1 + 1}) > V$. So $q_*$ is the only point of least value of $S$, and it occurs only in the term $c \nu$ of $f(\Phi_{m_1})$. Lemma 3.15.4 at the base point $P_{m_1 + 1}$ gives an $m_2$ such that for $m \ge m_2$ each $q \in S$ with $q \ne q_*$ has both exponents at the level $m$ larger than those of $\nu$. So each monomial of $F_m$ other than $c \nu$ is $\nu$ times a monomial in $x_m, w_m, y_m, z_m$ with nonnegative exponents that is not $1$. This is the claim. $\square$

Proposition 3.18.13 is the case $\deg f = 1$ times $M_m$, and Lemma 3.18.2 is the case of one sequence. The next lemma is the four-variable form of the last step of the proof of Theorem 3.15.17.

**Lemma 3.18.15.** Let $P_m$ be a point of a corner run in four variables, and let $(x, w)$ be a free coordinate system at $P_m$ in which the function of $P_m$ is $M^{-p}$ times the cleaning of $\sum_{k, l} A_{kl} x^k w^l$, with $M$ a monomial, $A_{kl} \in K[[y_m, z_m]]$, $A_{kl} = 0$ for $k + l \ge p$, and only $A_{00}$ cleaned. Let $g_m = \sum_{k, l} A_{kl} x^k w^l$. Assume that $\partial_x g_m = \mu \varepsilon$ with $\mu$ a nonzero constant times a monomial in $y_m, z_m$ and $\varepsilon$ a unit, and that $\mu$ divides $\partial_w g_m$. Then the run does not keep $\rho \ge 1$. So there is no such point on a corner run in four variables.

Node: SG0000008H

*Proof.* We have $\partial_x g_m = \sum_{k \ge 1} k A_{kl} x^{k-1} w^l$ and $\partial_w g_m = \sum_{l \ge 1} l A_{kl} x^k w^{l-1}$. The monomial $\mu$ divides each coefficient of these series, and $k, l < p$ are units of $K$, so $\mu$ divides $A_{kl}$ for each $(k, l) \ne (0, 0)$. Put
$$x'' = \frac{1}{\mu} \sum_{(k, l) \ne (0, 0)} A_{kl} x^k w^l \in K[[y_m, z_m]][x, w].$$
Then $x''(0, 0, y_m, z_m) = 0$ and $\partial x'' / \partial x = \varepsilon$ is a unit, so $(x'', w, y_m, z_m)$ is a regular system of parameters and $(x'', w)$ is a free coordinate system at $P_m$. The function of $P_m$ is $f = M^{-p} (\mu x'' + \operatorname{cl} A_{00})$, and it does not contain $w$. So $P_m$ is cylindrical (Definition 3.17.10). The coefficients of $x''^1$ and $x''^0$ of a power series in $(x'', w, y_m, z_m)$ are power series, so $\mu' = M^{-p} \mu$ is a constant times a monomial with nonnegative exponents and $B'_0 = M^{-p} \operatorname{cl} A_{00} \in K[[y_m, z_m]]$. The series $f = \mu' x'' + B'_0$ is clean, since the multiplication by the $p$-th power $M^{-p}$ keeps the cleanness. By Theorem 3.17.13, part 3, the run from $P_m$ gives a corner run with free translations in three variables of the point $\mu' x'' + B'_0$, with the same $\rho \ge 1$. This contradicts Theorem 3.15.16. $\square$

If $\partial_w g_m = 0$, the condition of divisibility is empty. If $\partial_x g_m = 0 \ne \partial_w g_m$, we exchange $x$ and $w$.

**Theorem 3.18.16.** Let $p \ge 3$, and let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g = 2$. Then $g$ has no planar corner run in four variables.

Node: SG0000008J

*Proof.* Write $g = q_{20} x^2 + q_{11} x w + q_{02} w^2 + \alpha x + \beta w + \gamma$ with $q_{kl}, \alpha, \beta, \gamma \in K[[y, z]]$, and assume that the run is planar. By Lemma 3.17.1, part 4,
$$\partial_x g_m = M_m (2 q_{20} \varphi_m + q_{11} \psi_m + \alpha) + M_m^2 (2 q_{20} x_m + q_{11} w_m),$$
$$\partial_w g_m = M_m (q_{11} \varphi_m + 2 q_{02} \psi_m + \beta) + M_m^2 (q_{11} x_m + 2 q_{02} w_m).$$
Since $2 < p$, these are not both $0$. Each nonzero one has the form of Proposition 3.18.13, with $(\alpha_1, \beta_1, \gamma_1)$ equal to $(2 q_{20}, q_{11}, \alpha)$ or to $(q_{11}, 2 q_{02}, \beta)$. So for $m$ large, $\partial_x g_m = c_X M_m \nu_X \varepsilon_X$ and $\partial_w g_m = c_W M_m \nu_W \varepsilon_W$, or $0$, with fixed Laurent monomials $\nu_X$ and $\nu_W$. Exchange $x$ and $w$ if needed, so that $\partial_x g_m \ne 0$ and $v(\nu_X) \le v(\nu_W)$ if $\partial_w g_m \ne 0$. If $v(\nu_X) < v(\nu_W)$, then by Lemma 3.18.1 the monomial $\nu_W / \nu_X$ has nonnegative exponents for $m$ large. If the values are equal, then the monomials are equal. So $M_m \nu_X$ divides $\partial_w g_m$. Since $\deg_{x, w} g_m \le 2 < p$, only $A_{00}$ is cleaned, and Lemma 3.18.15 at $P_m$ gives a contradiction. $\square$

The proof needs no study of the constant term $\operatorname{cl} g(\varphi_m, \psi_m)$: Lemma 3.18.15 passes it to Theorem 3.15.16, which treats it, with the $p$-th powers that the cleaning removes. Linear runs with $\deg_{x, w} g = 2$ exist (Proposition 3.17.8). The proof shows where they escape: with $\lambda = (1, 0)$ we have $\varphi_\infty = 0$, so Lemma 3.18.9 does not apply to $2 q_{20} \varphi_m + \alpha$, and the coefficient $M_m^2 q_{20}$ of $x_m$ in $\partial_x g_m$ is not dominated by the constant term.

**Theorem 3.18.17.** Let $g \in K[[y, z]][x, w]$ be clean with $1 \le \deg_{x, w} g < p$. Then $g$ has no planar corner run in four variables.

Node: SG0000008K

*Proof.* Assume that the run is planar. Since $1 \le \deg_{x, w} g < p$, the polynomials $g_X$ and $g_W$ are not both $0$, since a monomial $x^k w^l$ with $1 \le k + l < p$ has a nonzero derivative. Apply Proposition 3.18.14 to each nonzero one of $g_X, g_W \in K[[y_N, z_N]][X, W]$. Their degrees are less than $p$. By Lemma 3.17.1, part 4, for $m$ large
$$\partial_x g_m = c_X M_m \nu_X \varepsilon_X, \qquad \partial_w g_m = c_W M_m \nu_W \varepsilon_W \quad (\text{or } 0),$$
with fixed Laurent monomials $\nu_X$ and $\nu_W$ that have nonnegative exponents at the level $m$, and units $\varepsilon_X$ and $\varepsilon_W$ of $K[[x_m, w_m, y_m, z_m]]$. Exchange $x$ and $w$ if needed, so that $\partial_x g_m \ne 0$ and $v(\nu_X) \le v(\nu_W)$ if $\partial_w g_m \ne 0$. As in the proof of Theorem 3.18.16, $\mu = c_X M_m \nu_X$ divides $\partial_w g_m$ for $m$ large, and $\partial_x g_m = \mu \varepsilon_X$. Since $\deg_{x, w} g_m \le \deg_{x, w} g < p$, only $A_{00}$ is cleaned, and Lemma 3.18.15 at $P_m$ gives a contradiction. $\square$

For $\deg_{x, w} g = 3$ and $p \ge 5$ the proof uses Theorem 3.18.11 for the quadratic polynomials $g_X$ and $g_W$. Nothing in this case depends on the degree $3$. The obstruction is $\deg \ge p$, not $\deg \ge 3$.

**Corollary 3.18.18.** Let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g < p$. Then each corner run in four variables of $g$ is linear, and Hypothesis H1 (Hypothesis 3.17.32) and Conjectures L (Conjecture 3.17.18) and L° (Conjecture 3.17.24) hold for it, with $d = \rho + 1$ for $m$ large. For the runs with an infinite number of nonzero translations, Conjecture L+ (Conjecture 3.17.20) holds as well. So Theorem 3.17.33 holds without its hypothesis.

Node: SG0000008M

*Proof.* If $\deg_{x, w} g = 0$, then $g \in K[[y, z]]$ is not $0$, since $\operatorname{ord} g \ge p$, and (★★) holds at $P_N$, so Proposition 3.17.3 gives $\rho = 0$ at a later point, and there is no run. If $\deg_{x, w} g \ge 1$, the run is not planar by Theorem 3.18.17. Corollary 3.18.7 gives H1, L, L° and $d = \rho + 1$, and Theorem 3.18.6, part 3, gives L+ for the runs with an infinite number of nonzero translations. Theorem 3.17.33 assumes H1, which holds now. $\square$

Conjecture L+ is false in general for $\deg_{x, w} g < p$: in Example 3.17.22 all the translations are $0$, and the corner surface $V(x, y)$ has $\nu^G = 1 < \rho$. So the condition on the translations in the last claim is needed. Theorem 3.17.33 does not give Conjecture L° in its case 2, but Theorem 3.18.6 does: the line $\ell$ of case 2 is the coordinate $x$ of Theorem 3.18.6 up to a constant, since $c\, x_m^d$ and $c_m \ell^d$ are the same form.

### Linearity does not depend on the free coordinates

Definition 3.17.5 uses the free coordinates of $P_N$. By Lemma 3.17.2, part 3, linearity does not depend on the linear free coordinates. The next theorem says that it does not depend on any free coordinates. It holds for each degree.

**Theorem 3.18.19.** Let $P_N, P_{N+1}, \dots$ be a corner run in four variables. The following are equivalent.

1. The run is linear in the coordinates $(x_N, w_N)$.
2. There are a $J \ge N$ and a free coordinate $x'$ at $P_J$, linear or not, whose translations are $0$ from some point on. That is, Conjecture L holds for the run.
3. For each $J \ge N$ and each free coordinate system $(x'', w'')$ at $P_J$, the run from $P_J$ is linear in $(x'', w'')$.

So a corner run is planar if and only if Conjecture L fails for it.

Node: SG0000008N

*Proof.* Part 1 gives part 2. If $\alpha a_j + \beta b_j = 0$ for $j \ge J$, then by Lemma 3.17.2, part 3, the coordinate $x' = \alpha x_J + \beta w_J$, completed to a linear free coordinate system, has these translations.

Part 2 gives part 1. This is the main point. After a change of $J$ we may assume that the translations of $x'$ are $0$ for each $j \ge J$. By the fact on hypersurfaces in the proof of Lemma 3.17.6, the points $P_j$ with $j > J$ lie on the strict transforms of $V(x')$. We write the coordinates of $P_J$ without the index, and we start the run at $P_J$. Then $M_J = 1$, $\varphi_m = \sum_{J \le j < m} a_j M_{j+1}$, and $v(M_m)$ increases to a finite limit $\Lambda > 0$. Since $(x', w', y, z)$ is a regular system for some $w'$, the linear part of $x'$ in $(x, w)$ is not $0$. Assume that $\partial x' / \partial x$ is a unit at $P_J$, else exchange $x$ and $w$. By the Weierstrass preparation theorem, $x' = \varepsilon \cdot (x - F(w, y, z))$ with a unit $\varepsilon$ and $F \in K[[w, y, z]]$ with $F(0) = 0$. So $V(x') = V(x - F)$.

We claim that for each $m \ge J$ the strict transform of $V(x - F)$ at $P_m$ is $V(x_m - F_m)$, with $F_m \in K[[w_m, y_m, z_m]]$, $F_m(0) = 0$ and
$$F(\psi_m + M_m w_m, y, z) - \varphi_m = M_m F_m(w_m, y_m, z_m). \tag{18.3}$$
For $m = J$ this holds with $F_J = F$. Assume it at $m$. In the chart, $w_m = L_m (w_{m+1} + b_m)$ and $y_m, z_m \in (L_m)$, so $F_m = L_m G$ with $G \in K[[w_{m+1}, y_{m+1}, z_{m+1}]]$, and the strict transform of $V(x_m - F_m)$ is $V(x_{m+1} + a_m - G)$. Since $P_{m+1}$ lies on it, $G(0) = a_m$. Put $F_{m+1} = G - a_m$. Then $F_{m+1}(0) = 0$, and $M_{m+1} F_{m+1} = M_m F_m - a_m M_{m+1}$. With $\varphi_{m+1} = \varphi_m + a_m M_{m+1}$ and $\psi_{m+1} + M_{m+1} w_{m+1} = \psi_m + M_m w_m$, this gives (18.3) at $m + 1$.

Put $w_m = 0$ in (18.3). Then $F(\psi_m, y, z) - \varphi_m = M_m F_m(0, y_m, z_m)$, and $F_m(0, y_m, z_m)$ has no constant term. So each term of $F(\psi_m, y, z) - \varphi_m$ has a value larger than $v(M_m)$. In $\mathbb{K}$ the sum $F(\psi_\infty, y, z) = \sum_n F_n(y, z) \psi_\infty^n$ converges, since $v(\psi_\infty) > 0$, and $F(\psi_\infty, y, z) - F(\psi_m, y, z)$ is $\psi_\infty - \psi_m$ times an element of value at least $0$. So it has a value at least $v(M_{m+1})$. Also $v(\varphi_\infty - \varphi_m) \ge v(M_{m+1})$. So each term of $F(\psi_\infty, y, z) - \varphi_\infty$ has a value at least $v(M_m)$, for each $m$, and $v(M_m) \to \Lambda$. So
$$F(\psi_\infty, y, z) - \varphi_\infty \text{ has no term of value less than } \Lambda. \tag{18.4}$$

Now write $F = c\, w + F_0(y, z) + w F_1(y, z) + w^2 F_2(w, y, z)$ with $c \in K$ and $F_0, F_1 \in (y, z)$. Assume that the run is planar. Then $\varphi_\infty - c \psi_\infty = \sum_{j \ge J} (a_j - c b_j) M_{j+1}$ has an infinite number of nonzero terms, all of value less than $\Lambda$. The other part, $F_0 + \psi_\infty F_1 + \psi_\infty^2 F_2(\psi_\infty, y, z)$, has only a finite number of terms below $\Lambda$. Indeed, $F_0$ is a power series. For $\psi_\infty F_1$ the count in the proof of Lemma 3.18.9 applies, with $v(F_1) > 0$. For $n \ge 2$, a term of $\psi_\infty^n$ of value below $\Lambda$ is a product of $n$ terms $b_j M_{j+1}$, each of value below $\Lambda - v(M_{J+1})$, and there are a finite number of these. Also $\psi_\infty^n$ has a value at least $n\, v(M_{J+1})$, so only the $n < \Lambda / v(M_{J+1})$ matter, each multiplied by a power series in $y, z$ with a finite number of terms below $\Lambda$. So $\varphi_\infty - F(\psi_\infty, y, z)$ has an infinite number of terms below $\Lambda$. This contradicts (18.4). So the run is linear. If $\partial x' / \partial w$ is a unit instead, we exchange the roles of $(x, \varphi)$ and $(w, \psi)$.

Part 1 gives part 3. By part 2 there is a free coordinate $x'$ at a point $P_{J_0}$ whose translations are $0$ from some point on. Let $J \ge N$, let $(x'', w'')$ be a free coordinate system at $P_J$, and put $J_1 = \max(J, J_0)$. By Lemma 3.17.2, part 2, the transform of $x'$ at $P_{J_1}$ is a free coordinate there, and its translations from $P_{J_1}$ on are those of $x'$, so they are $0$ from some point on. The run from $P_J$ in the coordinates $(x'', w'')$ is a corner run by Lemma 3.17.2, part 2, and we start it at $P_{J_1}$, in the transforms of $(x'', w'')$. For this run part 2 holds with the coordinate $x'$ at $P_{J_1}$, so by the implication from part 2 to part 1 it is linear in the transforms of $(x'', w'')$. A run that is linear from a later point on is linear. So the run from $P_J$ is linear in $(x'', w'')$. Part 3 with $J = N$ and $(x'', w'') = (x_N, w_N)$ is part 1. $\square$

Lemma 3.17.6, part 2, is the case $F = -(\beta_0 / \alpha_0) w - \gamma / \alpha_0$ of the implication from part 2 to part 1. Theorems 3.18.17 and 3.18.19 together give Conjecture L once more for $\deg_{x, w} g < p$.

### Examples

**Example 3.18.20.** Let $p \ge 3$, $Y = y^{p-2} z^{p-2}$ and $g = Y (x^2 + y z w)$. Then $r = (p - 2, p - 2)$, $G = x^2 + y z w$, $d = 2$ and $\rho = 1$. In the notation of Proposition 3.18.4 and Lemma 3.18.5, with $m_0 = N$, we have $I = \{2\}$, $Q_2 = (y z)^2 Y = y^p z^p$, $\mu = y^{p-1} z^{p-1}$ and $Q_W = y z \mu = y^p z^p = Q_2$. So this is the case of Step 3 in the proof of Theorem 3.18.6, with $i_0 = 2$. Both charts with the translation $(0, 0)$ send $g$ to $g$. The $y$-chart with the translation $(0, b)$, $b \ne 0$, gives $x = y' x'$, $w = y' (w' + b)$, $z = y' z'$, and after the division by $y'^p$,
$$g' = y'^{p-2} z'^{p-2} \bigl(x'^2 + y' z' w' + b\, y' z'\bigr).$$
The new term $b\, y'^{p-1} z'^{p-1}$ is not a $p$-th power. At this point $G = x^2 + y z w + b\, y z$, so $d = 2$ and $\rho = 1$. The next $y$-step sends $b\, y z$ to $b\, z$, and the next $z$-step sends it to $b\, y$. So at the next point $G$ has a monomial of degree $1$, and $d = \rho = 1$: the point has type $0$. By Theorem 3.17.27 a point of type $0$ cannot be followed by a change of the letter. Computer tests found that each such branch ends within $4$ steps. This agrees with Step 3, which says that a corner run has only a finite number of translations of $w$ with $Q_W / (y_{j+1} z_{j+1})$ not a $p$-th power: a nonzero translation of $w$ adds a term of value less than $\kappa_W$ to $C$, and Step 1 forbids such terms in the limit. Along the run with all translations $0$, the corner surfaces have $\nu^G = \rho = 1$, because of the monomial $y z w$ of $G$, and the corner curves have $\nu^G = 2 = d$.

**Example 3.18.21.** Let $p \ge 3$, $Y = y^{p-2} z^{p-2}$ and $g = x^2 Y + w y^p z^p$, the second point of Example 3.17.9. Then $I = \{2\}$, $Q_2 = (y z)^2 Y = y^p z^p$, $\mu = y^p z^p$ and $Q_W = y^{p+1} z^{p+1}$. So $\kappa_W = \kappa_* + 1 + \theta > \kappa_*$, and this is the case of Step 4 in the proof of Theorem 3.18.6. In this case the proof allows all the translations of $w$, and this agrees with Proposition 3.17.8, which gives a corner run with $\rho = 1$ for each choice of the $b_m$. Theorem 3.18.6 gives $\operatorname{in} G_m = c\, x_m^2$, $d = 2$ and $\rho = 1$ for $m$ large, and by the list in Step 5 the corner surfaces and the corner curves have $\nu^G = 2 = d$ for $m$ large.

### What stays open for degree at least p

**Remark 3.18.22.** For $\deg_{x, w} g \ge p$ the proofs of this section break in two places.

1. Statement D. The relation (18.1) does not give a nonzero derivative when $p \mid k + 1$, so the chain of Step 1 and the linear part of Step 2 in the proof of Theorem 3.18.11 need not exist. For $f = X^p + \gamma$ we have $f_X = f_W = 0$. In one variable Section 3.15 treats this case with the dominant index of Lemma 3.15.8 and the transcendental type of Proposition 3.15.7. For a pair of sequences a substitute would be a statement on $f(\Phi_\infty)$ for $f \in \hat H[X^p, W^p]$ plus terms of lower degree. We have no proof of it.
2. Lemma 3.18.15. The coefficients $A_{kl}$ with $p \mid k$, $p \mid l$ and $(k, l) \ne (0, 0)$ are cleaned, so $g_m$ is not $\mu x'' + \operatorname{cl} A_{00}$, and the reduction to Theorem 3.15.16 is not available. This is the four-variable form of the passage from Theorem 3.15.17, where $\deg_x g < p$, to the general case in Section 3.16.

Also the proof of Theorem 3.18.6 uses $\deg_{x, w} g < p$ in Proposition 3.18.4, where the divisibility of $e_l$ by $\mu$ and the form $\mu w''$ need $l < p$. So the open cases of H1, L and L° are the corner runs with $\deg_{x, w} g \ge p$, linear with a dominant index $h > 1$ or planar. The class $B_1 x^p + B_2 w^p + B_0$ of rank $2$ of Corollary 3.17.17 is the first of them. Theorem 3.18.19 holds for each degree, so in this range Conjecture L is again the statement that there is no planar run.

### Notes and references

The results of this section are a result of the track C4 of this project (tamnd/singularity#286). They come from notes 50, 52, 54 and 63 of the research notes. Note 50 gave the three lemmas, the normal form, Theorem 3.18.6 and Corollary 3.18.7, and Example 3.18.20. Note 52 is the referee report on note 50. It added the proof that the largest monomial factor of $g_m$ is $y^{r_y} z^{r_z}$ in Step 5 and the proof that the translations of $x$ stay $0$ in Proposition 3.18.4, and it proved Lemma 3.18.9, Lemma 3.18.15, Proposition 3.18.13 and Theorem 3.18.16. Note 54 checked note 52 again and gave the field $\mathbb{F}$, Lemma 3.18.10, Theorem 3.18.11, Proposition 3.18.14, Theorem 3.18.17, Corollary 3.18.18 and Theorem 3.18.19. Note 63 is the referee report on note 54. It made the identity (18.1) hold in each characteristic, limited the claims on Conjecture T and on Theorem 3.17.33 to $\deg < p$, and added the argument with $J_1$ in the proof of Theorem 3.18.19.

Computer tests with exact arithmetic over $\mathbb{F}_3$, $\mathbb{F}_9$, $\mathbb{F}_5$, $\mathbb{F}_{25}$, $\mathbb{F}_7$, $\mathbb{F}_{49}$ and $\mathbb{F}_{11}$ agree with each result. Depth first searches over all the translations along random words, for starting points with $\deg_{x, w} g = 2$ and $3$, found no planar run. Only one branch, over $\mathbb{F}_5$ with $\deg_{x, w} g = 2$, had late translations that span $K^2$, and it ends at a point with $d = \rho = 1$ from which no step keeps $\rho$. Linear walks checked the conclusions of Theorem 3.18.6, and computations in a model of the Hahn field checked Theorem 3.18.11 and Proposition 3.18.14. A control with linear translations made the dominance fail, as Remark 3.18.12 predicts, so the tests can see failures. The translations of the tests are in finite fields, the words are finite and the searches have budgets, so the tests are not a proof.

The outside results are those of Section 3.17: the pseudo Cauchy sequences of Kaplansky, the generalized stability theorem [Kuh10, Theorem 1.1] and the facts on the henselization in [Kuh-book], through Proposition 3.15.7. The use of the history of the divisor is from [CJS20]. None of the results has a Lean proof yet.

Several questions are open.

1. Hypothesis H1 and Conjectures L and L° for $\deg_{x, w} g \ge p$ (Remark 3.18.22).
2. Statement D and Conjecture T for the planar runs and $\deg f \ge p$.
3. Conjecture L° for the linear runs with a dominant index $h > 1$.
