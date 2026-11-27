---
title: Conjecture P
nodes: [SG0000009F, SG0000009G, SG00000096, SG0000006Z, SG0000009H, SG0000009J]
sources: [CJS20, Kuh10, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Conjecture P

Section 3.18 reduces Conjecture L (Conjecture 3.17.18) to Conjecture P (Conjecture 3.18.39): a clean $g \in K[[y, z]][x, w]$ has no planar corner run in four variables. It proves Conjecture P for $\deg_{x, w} g < p$, under the condition (C) on the derivatives of order $p^e$, and for $g \in K[[y, z]][x^p, w^p]$. In this section we prove Conjecture P for each prime $p$ and each clean $g \in K[[y, z]][x, w]$. So Conjecture L holds for each clean polynomial in $x, w$.

The tools are the results of Section 3.18 for degree at least $p$: Statement D in each degree (Theorem 3.18.26), the two necessary conditions on a planar run (Theorem 3.18.32) and the class of the least term of order $p^e$ (Corollary 3.18.33). At the point $P_N$ alone these conditions do not contradict each other. The new idea is to apply them again at each later point $P_m$, to the run that starts at $P_m$. Seen from $P_N$, the restart does not change the invariant of order $1$, and it changes the invariants of order $p^e$ only in their terms of class $0$. But it gives a better lower bound for these terms, and as $m$ grows the bound meets Statement D for $g_X$ or $g_W$ exactly.

The section proves the following.

1. The run from a point $P_m$ is a corner run of the function of $P_m$, with the same degree in $x, w$, and the results of Section 3.18 hold for it with $\delta_m$ in place of $1 + \theta$ (Lemma 3.19.1). Two identities compare its invariants with those of the run from $P_N$ (Lemma 3.19.2 and Corollary 3.19.3).
2. Conjecture P holds for each $p$ and each clean $g \in K[[y, z]][x, w]$ with $\deg_{x, w} g \ge 1$ (Theorem 3.19.6). So each corner run in four variables of a clean $g \in K[[y, z]][x, w]$ is linear, and Conjecture L holds for it in each free coordinate system (Corollary 3.19.7). The case $p = 2$ and $\deg_{x, w} g \le 3$ comes first, as a warm-up (Theorem 3.19.5).
3. For $p = 2$ and $\deg_{x, w} g = 3$, Hypothesis H1 and Conjecture L° hold for the linear runs whose function at the restart point has no monomial $x'^2 w'$, $w'^2$ or $w'^3$ in adapted coordinates (Theorem 3.19.11). The rest of this case is Conjecture 3.19.14.

The proof needs a finite degree in $x, w$, so it says nothing about power series in $x, w$ or about $g \in K[[x, y, z]]$. It does not give Conjecture L°, Hypothesis H1 or Conjecture L+ for the linear runs with $\deg_{x, w} g \ge p$ outside $K[[y, z]][x^p, w^p]$.

### The setting

We use the setting of Sections 3.17 and 3.18. The field $K$ is algebraically closed of characteristic $p$, any prime. Let $g \in K[[y, z]][x, w]$ be clean at $P_N$, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables of $g$. So each step is a $y$-chart or a $z$-chart followed by a translation $(a_m, b_m) \in K^2$ of $(x, w)$, each chart occurs an infinite number of times, $\rho \ge 1$ is the same at each point, and the points have $\operatorname{ord} \ge p$. The function of a point is the transform with the factor $L_m^{-p}$, followed by the cleaning. We write $D = \deg_{x, w} g$.

As in Section 3.18 we have the monomials $M_m$, the sums $\Phi_m = (\varphi_m, \psi_m)$, the limit $\Phi_\infty$ in the Hahn field $\mathbb{K}$, the valuation $v(y_N^a z_N^b) = a + \theta b$ with $\theta$ irrational, and $\delta_m = v(y_m z_m) = 1 + \theta - v(M_m)$, which decreases to $0$. Put
$$\Delta_m = \Phi_\infty - \Phi_m = (\Delta\varphi_m, \Delta\psi_m), \qquad \Delta\varphi_m = \sum_{j \ge m} a_j M_{j+1}, \qquad \Delta\psi_m = \sum_{j \ge m} b_j M_{j+1}.$$
Each term of $\Delta\varphi_m$ and of $\Delta\psi_m$ has a value at least $v(M_{m+1})$. Put
$$\tilde g_m = g(\varphi_m + M_m x_m, \psi_m + M_m w_m) = \sum_{k, l} A_{kl}\, x_m^k w_m^l, \qquad A_{kl} = M_m^{k + l} g^{[k, l]}(\Phi_m),$$
and $g_m = \operatorname{cl}(\tilde g_m)$. By Lemma 3.17.1 the function of $P_m$ is
$$g^{(m)} = M_m^{-p} g_m.$$

The *class* of a Laurent monomial in $y_N, z_N$ is its vector of exponents modulo $p$. By Lemma 3.18.23 the class does not depend on the level: a monomial has the class $0$ if and only if it is a $p$-th power of a Laurent monomial in $y_m, z_m$, for each $m$. For $A \in \mathbb{K}$, $\operatorname{cl} A$ is the sum of the terms of $A$ of nonzero class, and we put $\operatorname{cl}_0 A = A - \operatorname{cl} A$. We use three facts.

1. The maps $\operatorname{cl}$ and $\operatorname{cl}_0$ are additive, and they do not lower values.
2. If all the terms of $P \in \mathbb{K}$ have the class $0$, then $\operatorname{cl}(P A) = P \operatorname{cl}(A)$ and $\operatorname{cl}_0(P A) = P \operatorname{cl}_0(A)$, since the class of a product of two monomials is the sum of their classes.
3. A $p$-th power $Q^p$ of an element $Q \in \mathbb{K}$ has only terms of class $0$, since the Frobenius acts term by term on Hahn series: $(\sum_s c_s \omega_s)^p = \sum_s c_s^p \omega_s^p$.

For $f \in \hat H[X, W]$ we use $\beta_{kl}(f) = v(f^{[k, l]}(\Phi_\infty))$, with $v(0) = \infty$, and the invariants $\Lambda(f)$ and $\Lambda_e(f)$ of Section 3.18. For $g$ we write $\beta_{kl} = \beta_{kl}(g)$ and
$$\beta_1 = \min\bigl(v(g_X(\Phi_\infty)), v(g_W(\Phi_\infty))\bigr), \qquad \Lambda_0 = \beta_1 + 1 + \theta, \qquad \Lambda_e = \min(\beta_{p^e 0}, \beta_{0 p^e}) + p^e (1 + \theta) \quad (e \ge 1).$$
For a pair $(C, D)$ of elements of $\mathbb{K}$ we write $v(C, D) = \min(v(C), v(D))$, the least value of the pair.

### The run seen from a later point

**Lemma 3.19.1.** Let $m \ge N$. Then:

1. The function $g^{(m)}$ of $P_m$ is in $K[[y_m, z_m]][x_m, w_m]$ and is clean at $P_m$. The points $P_m, P_{m+1}, \dots$ are a corner run in four variables of $g^{(m)}$, with the same charts and translations. Its monomials are $M_n / M_m$, its sums are $(\Phi_n - \Phi_m) / M_m$ for $n \ge m$, and its limit is $\Phi^{(m)}_\infty = \Delta_m / M_m$. It is planar if and only if the run from $P_N$ is planar.
2. The irrational number of the run from $P_m$ is $\theta^{(m)} = v(z_m) / v(y_m)$, and its valuation is $v / v(y_m)$. So $v(y_m) (1 + \theta^{(m)}) = \delta_m$.
3. $\deg_{x_m, w_m} g^{(m)} = D$.
4. Theorems 3.18.26 and 3.18.32 and Corollary 3.18.33 hold for the run from $P_m$ and the function $g^{(m)}$, with the Hasse derivatives in $(x_m, w_m)$, the limit $\Phi^{(m)}_\infty$, the valuation $v$, and $\delta_m$ in place of $1 + \theta$.

Node: SG0000009F

*Proof.* Part 1. The function of a point is defined step by step from the function of the point before it. So the functions of the points $P_n$, $n \ge m$, are the same for the two runs, and so are $\rho$ and the orders. Each chart occurs an infinite number of times after $m$. The function of $P_m$ is a clean power series, and by Lemma 3.17.1, part 3, it is a polynomial in $x_m, w_m$. The recursion $M'_m = 1$, $M'_{n+1} = M'_n L_n$ gives $M'_n = M_n / M_m$, and the sums of the run from $P_m$ are $\sum_{m \le j < n} a_j M_{j+1} / M_m = (\varphi_n - \varphi_m) / M_m$, and the same for $\psi$. The limit is $\Delta_m / M_m$. Planarity depends only on the translations $(a_j, b_j)$ for $j$ large, so it is the same for the two runs.

Part 2. For $n > m$ write $y_m = y_n^{a_1} z_n^{a_2}$ and $z_m = y_n^{b_1} z_n^{b_2}$, and let $c_1 = (a_1, b_1)$ and $c_2 = (a_2, b_2)$ be the columns from $P_m$ to $P_n$, as in the proof of Theorem 3.13.20. Then $(v(y_m), v(z_m)) = v(y_n) c_1 + v(z_n) c_2$, and $v(y_n), v(z_n) > 0$ by Lemma 3.13.24, part 1. So the vector $(1, \theta_m)$ with $\theta_m = v(z_m) / v(y_m)$ is in the cone of $c_1$ and $c_2$ for each $n$. By the proof of Theorem 3.13.20 these cones shrink to the ray of $(1, \theta^{(m)})$, since each chart occurs an infinite number of times. So $\theta^{(m)} = \theta_m$, and the valuation of the run from $P_m$ is $v^{(m)}(y_m^a z_m^b) = a + \theta_m b = v(y_m^a z_m^b) / v(y_m)$. Then $v(y_m)(1 + \theta^{(m)}) = v(y_m) + v(z_m) = \delta_m$. This is also the proof of Proposition 3.13.26, where $\theta_m$ occurs.

Part 3. The part of degree $D$ of $\tilde g_m$ in $(x_m, w_m)$ is $M_m^D$ times the part of degree $D$ of $g$, since $g(\varphi_m + M_m x, \psi_m + M_m w)$ has the top part $g_D(M_m x, M_m w) = M_m^D g_D(x, w)$. The cleaning does not remove a monomial of it. Indeed, let $c_{kl}$ be the coefficient of $x^k w^l$ in $g$, with $k + l = D$. The coefficient $M_m^D c_{kl}$ is cleaned only if $p \mid k$ and $p \mid l$. Then $p \mid D$, so $M_m^D$ is a $p$-th power, and $c_{kl}$ has only terms of nonzero class, since $g$ is clean. By fact 2, $\operatorname{cl}(M_m^D c_{kl}) = M_m^D c_{kl}$. The factor $M_m^{-p}$ does not change the degree.

Part 4. The field $\hat H$ is the completion of $K(y_N, z_N) = K(y_m, z_m)$ for $v$, and $v / v(y_m)$ gives the same completion. The Laurent monomials in $y_m, z_m$ are the Laurent monomials in $y_N, z_N$, so the Hahn field of Lemma 3.15.6 is the same, with the valuation multiplied by $1 / v(y_m)$. By parts 1 to 3 the hypotheses of the three results hold for the run from $P_m$, in its own valuation $v^{(m)}$ and with its number $1 + \theta^{(m)}$. Each statement of these results is an equality or an inequality between values and multiples of $1 + \theta$, homogeneous of degree $1$. We multiply by $v(y_m)$ and use part 2. $\square$

For the run from $P_m$ we write, in the units of $v$,
$$\Lambda^{(m)}_0 = \min\bigl(v(g^{(m)}_X(\Phi^{(m)}_\infty)), v(g^{(m)}_W(\Phi^{(m)}_\infty))\bigr) + \delta_m, \qquad \Lambda^{(m)}_e = v\bigl(H^{(m)}_{e, 1}, H^{(m)}_{e, 2}\bigr) + p^e \delta_m \quad (e \ge 1),$$
with $H^{(m)}_{e, 1} = (g^{(m)})^{[p^e, 0]}(\Phi^{(m)}_\infty)$ and $H^{(m)}_{e, 2} = (g^{(m)})^{[0, p^e]}(\Phi^{(m)}_\infty)$. Let $\Lambda^{(m)}_+ = \min_{e \ge 1} \Lambda^{(m)}_e$, and let $\Lambda^{(m)}$ be the invariant $\Lambda$ of $g^{(m)}$, with $\delta_m$ in place of $1 + \theta$. These are the numbers of Theorem 3.18.32 for the run from $P_m$.

**Lemma 3.19.2.** Let $m \ge N$ and $M = M_m$. Then:

1. $g^{(m)}_X(\Phi^{(m)}_\infty) = M^{1 - p} g_X(\Phi_\infty)$ and $g^{(m)}_W(\Phi^{(m)}_\infty) = M^{1 - p} g_W(\Phi_\infty)$.
2. $\operatorname{cl} g^{(m)}(\Phi^{(m)}_\infty) = M^{-p} \operatorname{cl} g(\Phi_\infty)$.
3. For each $e \ge 1$,
$$H^{(m)}_{e, 1} = M^{p^e - p} \sum_{k, l} \binom{k}{p^e} \bigl[g^{[k, l]}(\Phi_m)\bigr]'\, \Delta\varphi_m^{k - p^e} \Delta\psi_m^l, \tag{19.1}$$
where $[A]' = \operatorname{cl} A$ if $p \mid k$ and $p \mid l$, and $[A]' = A$ otherwise. The same holds for $H^{(m)}_{e, 2}$, with $\binom{l}{p^e}$ and $\Delta\varphi_m^k \Delta\psi_m^{l - p^e}$.
4. Let $e \ge 1$. Let $S^e_1$ be the set of the $(k, l)$ with $g^{[k, l]} \ne 0$, with $k$ and $l$ not both divisible by $p$, and with $\binom{k}{p^e} \not\equiv 0 \pmod p$. Let $S^e_2$ be the same set with $\binom{l}{p^e}$. Then
$$\operatorname{cl}_0 H^{(m)}_{e, 1} = M^{p^e - p} \operatorname{cl}_0 \Bigl(\sum_{(k, l) \in S^e_1} \binom{k}{p^e} g^{[k, l]}(\Phi_m)\, \Delta\varphi_m^{k - p^e} \Delta\psi_m^l\Bigr),$$
and the same holds for $H^{(m)}_{e, 2}$ and $S^e_2$. Each $(k, l) \in S^e_1 \cup S^e_2$ has $k + l - p^e \ge 0$ and is not $(1, 0)$ or $(0, 1)$. Each term of $\operatorname{cl}_0 H^{(m)}_{e, 1}$ and of $\operatorname{cl}_0 H^{(m)}_{e, 2}$ has a value at least
$$(p^e - p)\, v(M_m) + \min_{(k, l) \in S^e_1 \cup S^e_2} \Bigl(v\bigl(g^{[k, l]}(\Phi_m)\bigr) + (k + l - p^e)\, v(M_{m+1})\Bigr),$$
with $\min \emptyset = \infty$.

Node: SG0000009G

*Proof.* Write $x, w$ for $x_m, w_m$. The substitutions below are possible in $\mathbb{K}$: $g^{(m)}$ and its derivatives are polynomials in $x, w$, and the entries of $\Delta_m / M$ have positive values, since $v(M_{m+1}) > v(M)$.

Part 1. A monomial $x^k w^l y_m^a z_m^b$ that the cleaning removes has $p \mid k$, so its derivative in $x$ is $0$. So $\partial_x g^{(m)} = M^{-p} \partial_x \tilde g_m$, and by Lemma 3.17.1, part 4, $\partial_x \tilde g_m = M\, g_X(\varphi_m + M x, \psi_m + M w)$. At $(x, w) = \Delta_m / M$ the argument is $\Phi_m + \Delta_m = \Phi_\infty$. The same holds for $w$.

Part 2. We have $M^p g^{(m)} = \tilde g_m - Q$, where $Q$ is the sum of the removed monomials $c\, Y x^k w^l$, with $Y$ a monomial of class $0$ and $p \mid k$, $p \mid l$. At $\Delta_m / M$, $\tilde g_m$ gives $g(\Phi_\infty)$. A removed monomial gives $c\, Y \bigl((\Delta\varphi_m / M)^{k/p} (\Delta\psi_m / M)^{l/p}\bigr)^p$, which has only terms of class $0$ by facts 2 and 3. So $\operatorname{cl}\bigl(M^p g^{(m)}(\Phi^{(m)}_\infty)\bigr) = \operatorname{cl} g(\Phi_\infty)$, and fact 2 for the factor $M^p$ gives part 2.

Part 3. The cleaning acts monomial by monomial, so the coefficient of $x^k w^l$ in $g_m$ is $\operatorname{cl} A_{kl}$ if $p \mid k$ and $p \mid l$, and $A_{kl}$ otherwise (Lemma 3.17.1, part 3, and Lemma 3.18.23). If $p \mid k$ and $p \mid l$, then $M^{k + l}$ is a $p$-th power, and fact 2 gives $\operatorname{cl}(M^{k + l} g^{[k, l]}(\Phi_m)) = M^{k + l} \operatorname{cl} g^{[k, l]}(\Phi_m)$. So in all cases
$$g^{(m)} = M^{-p} \sum_{k, l} M^{k + l} \bigl[g^{[k, l]}(\Phi_m)\bigr]'\, x^k w^l.$$
The Hasse derivative $[p^e, 0]$ sends $x^k w^l$ to $\binom{k}{p^e} x^{k - p^e} w^l$. At $(x, w) = \Delta_m / M$ the term of $(k, l)$ is
$$\binom{k}{p^e} M^{-p} M^{k + l} \bigl[g^{[k, l]}(\Phi_m)\bigr]'\, \frac{\Delta\varphi_m^{k - p^e} \Delta\psi_m^l}{M^{k + l - p^e}},$$
and the power of $M$ is $-p + (k + l) - (k + l - p^e) = p^e - p$. This is (19.1). The same computation with $[0, p^e]$ gives the formula for $H^{(m)}_{e, 2}$.

Part 4. Take a term of (19.1) with $p \mid k$, $p \mid l$ and $\binom{k}{p^e} \ne 0$. Then $k \ge p^e$, and $p \mid k - p^e$ since $e \ge 1$. So $\Delta\varphi_m^{k - p^e} \Delta\psi_m^l$ is a $p$-th power and has only terms of class $0$ by fact 3. The factor $\operatorname{cl} g^{[k, l]}(\Phi_m)$ has only terms of nonzero class, so by fact 2 the product has only terms of nonzero class. The factor $M^{p^e - p} = (M^{p^{e - 1} - 1})^p$ has the class $0$. By facts 1 and 2, $\operatorname{cl}_0 H^{(m)}_{e, 1}$ is $M^{p^e - p}$ times the part of class $0$ of the sum of the other terms. These are the terms with $(k, l) \in S^e_1$, and for them $[A]' = A$. For $(k, l) \in S^e_1$, $\binom{k}{p^e} \ne 0$ gives $k \ge p^e \ge p \ge 2$, so $k + l - p^e \ge 0$ and $(k, l)$ is not $(1, 0)$ or $(0, 1)$. The same holds for $S^e_2$, with $l \ge p^e$. Each term of the sum over $S^e_1$ is $g^{[k, l]}(\Phi_m)$ times a product of $k + l - p^e$ entries of $\Delta_m$, so its terms have values at least $v(g^{[k, l]}(\Phi_m)) + (k + l - p^e) v(M_{m+1})$. By fact 1, $\operatorname{cl}_0$ does not lower values. $\square$

The two powers $M^{1 - p}$ and $M^{p^e - p}$ are the whole content of the lemma. For $p = 2$ and $e = 1$ they are $M^{-1}$ and $1$.

**Corollary 3.19.3.** Let the run be planar, and put $\hat\Lambda^{(m)}_\bullet = \Lambda^{(m)}_\bullet + p\, v(M_m)$. Then for each $m \ge N$:

1. $\hat\Lambda^{(m)}_0 = \Lambda_0$.
2. For $e \ge 1$, $\hat\Lambda^{(m)}_e = v\bigl(\mathbf H^{(m)}_{e, 1}, \mathbf H^{(m)}_{e, 2}\bigr) + p^e (1 + \theta)$, where $\mathbf H^{(m)}_{e, i} = M_m^{p - p^e} H^{(m)}_{e, i}$ is the sum in (19.1). The difference $\mathbf H^{(m)}_{e, 1} - g^{[p^e, 0]}(\Phi_\infty)$ has only terms of class $0$, and the same holds for $\mathbf H^{(m)}_{e, 2} - g^{[0, p^e]}(\Phi_\infty)$.
3. $v(\operatorname{cl} g^{(m)}(\Phi^{(m)}_\infty)) + p\, v(M_m) = v(\operatorname{cl} g(\Phi_\infty))$.

*Proof.* Part 1. By Lemma 3.19.2, part 1, $\Lambda^{(m)}_0 = \beta_1 + (1 - p) v(M_m) + \delta_m$, and $v(M_m) + \delta_m = 1 + \theta$. Part 2. We have $\Lambda^{(m)}_e + p\, v(M_m) = v(\mathbf H^{(m)}_e) + (p^e - p) v(M_m) + p^e \delta_m + p\, v(M_m) = v(\mathbf H^{(m)}_e) + p^e (1 + \theta)$, with $v(\mathbf H^{(m)}_e)$ the least value of the pair. Taylor's formula at $\Phi_m$ for $g^{[p^e, 0]}$ and the identity (18.5) give
$$g^{[p^e, 0]}(\Phi_\infty) = \sum_{k, l} \binom{k}{p^e} g^{[k, l]}(\Phi_m)\, \Delta\varphi_m^{k - p^e} \Delta\psi_m^l.$$
So the difference with $\mathbf H^{(m)}_{e, 1}$ is the sum of the terms $\binom{k}{p^e} \operatorname{cl}_0(g^{[k, l]}(\Phi_m))\, \Delta\varphi_m^{k - p^e} \Delta\psi_m^l$ with $p \mid k$ and $p \mid l$, up to the sign, and it has only terms of class $0$ by facts 2 and 3. The same holds for $i = 2$. Part 3 is Lemma 3.19.2, part 2. $\square$

So, seen from $P_N$, the restart does not change the invariant of order $1$, and it does not change the part of nonzero class of the pairs of order $p^e$. It changes only their part of class $0$, and Lemma 3.19.2, part 4, gives a lower bound for this part that rises with $v(M_{m+1})$ to $1 + \theta$.

### A first case

The following example shows the mechanism in the smallest case.

**Example 3.19.4.** Let $p = 2$ and $g = Y x^3 + B_1 x^2 + \alpha x + B_0$, clean, with $Y \ne 0$. Then $g_X = \alpha + Y X^2$, since $3 = 1$ and $2 = 0$ in $K$, and $g_W = 0$. Assume that the run is planar, so an infinite number of the $a_j$ are not $0$. Statement D for $g_X$ (Theorem 3.18.26, part 1, with the index $(2, 0)$) says $v(\alpha + Y \varphi_\infty^2) < v(Y) + 2(1 + \theta)$. Here this is visible by hand: $Y \varphi_\infty^2 = \sum_j a_j^2 Y M_{j+1}^2$ has an infinite number of distinct terms of value less than $v(Y) + 2(1 + \theta)$, and $\alpha$ has only a finite number of terms there.

On the other side, (19.1) with $e = 1$ has the terms $(k, l) = (2, 0)$, which is cleaned, and $(3, 0)$, with $\binom{3}{2} = 1$ in $K$. So
$$H^{(m)}_{1, 1} = \operatorname{cl}(B_1 + Y \varphi_m) + Y \Delta\varphi_m, \qquad H^{(m)}_{1, 2} = 0,$$
and the part of class $0$ of $H^{(m)}_{1, 1}$ is $\operatorname{cl}_0(Y \Delta\varphi_m)$, with all terms of value at least $v(Y) + v(M_{m+1})$. Theorem 3.18.32, part 1, at $P_m$ says $\Lambda^{(m)}_0 \ge \Lambda^{(m)}_1$, that is, $v(\alpha + Y \varphi_\infty^2) \ge \mu_m + 1 + \theta$ with $\mu_m = v(H^{(m)}_{1, 1})$, by Corollary 3.19.3. Corollary 3.18.33 at $P_m$ says that the least term of $H^{(m)}_{1, 1}$ has the class $0$, so $\mu_m \ge v(Y) + v(M_{m+1})$. At $P_N$ alone nothing is contradicted: $v(M_{N+1})$ can be small. But the two conditions hold at each $P_m$, and $v(M_{m+1}) \to 1 + \theta$. So $v(\alpha + Y \varphi_\infty^2) \ge v(Y) + 2(1 + \theta)$, which contradicts Statement D.

**Theorem 3.19.5.** Let $p = 2$, and let $g \in K[[y, z]][x, w]$ be clean with $1 \le \deg_{x, w} g \le 3$. Then $g$ has no planar corner run in four variables.

*Proof.* For $\deg_{x, w} g \le 2 = p$ this is Theorem 3.18.34. Let $\deg_{x, w} g = 3$, let $c_{kl}$ be the coefficient of $x^k w^l$ in $g$, and let $\lambda$ be the least value of the nonzero cubic coefficients $c_{30}, c_{21}, c_{12}, c_{03}$. Assume that the run is planar.

Step 1. Let $m \ge N$. By Lemma 3.19.1 the run from $P_m$ is a planar corner run of the clean cubic $g^{(m)}$, and Theorem 3.18.32 holds for it. Since $\deg g^{(m)} = 3 < 4$, we have $\Lambda^{(m)}_e = \infty$ for $e \ge 2$, so $\Lambda^{(m)}_+ = \Lambda^{(m)}_1$. By Theorem 3.18.32, part 1, $\Lambda^{(m)}_0 \ge \Lambda^{(m)}_1$, and $\Lambda^{(m)}$ is finite by Theorem 3.18.26. Let $\mu_m$ be the least value of the pair $H^{(m)}_{1, 1}, H^{(m)}_{1, 2}$. Corollary 3.19.3 turns $\Lambda^{(m)}_0 \ge \Lambda^{(m)}_1$ into
$$\beta_1 \ge \mu_m + 1 + \theta.$$

Step 2. By Corollary 3.18.33 for the run from $P_m$ with $e = 1$, the least term of the pair has the class $0$. For $p = 2$ and $e = 1$ the sets of Lemma 3.19.2, part 4, are $S^1_1 \subseteq \{(2, 1), (3, 0)\}$ and $S^1_2 \subseteq \{(1, 2), (0, 3)\}$, since $\binom{k}{2}$ is odd only for $k \equiv 2, 3 \pmod 4$. For these $(k, l)$ we have $g^{[k, l]} = c_{kl}$ and $k + l - 2 = 1$. So $\mu_m \ge \lambda + v(M_{m+1})$, and $\beta_1 \ge \lambda + v(M_{m+1}) + 1 + \theta$ for each $m$. In the limit,
$$\beta_1 \ge \lambda + 2(1 + \theta).$$

Step 3. In characteristic $2$,
$$g_X = c_{10} + c_{11} W + c_{30} X^2 + c_{12} W^2, \qquad g_W = c_{01} + c_{11} X + c_{21} X^2 + c_{03} W^2.$$
Let $c$ be a cubic coefficient with $v(c) = \lambda$. Then $c$ is the coefficient of $X^2$ or of $W^2$ in $g_X$ or in $g_W$. Say $c = c_{30}$, the other cases being the same. Then $g_X^{[2, 0]} = c_{30}$, and Theorem 3.18.26, part 1, for $f = g_X$ and the index $(2, 0)$ gives $\beta_1 \le v(g_X(\Phi_\infty)) < \lambda + 2(1 + \theta)$. This contradicts Step 2. $\square$

### Conjecture P

The general proof has the same three ingredients: the inequality of order $1$ at each point, the class of the least term at each point, and Statement D for a first derivative. Two things change. The least term of order $p^e$ can come from each $e$ with $p^e \le D$, and the index $(k, l)$ of Lemma 3.19.2, part 4, depends on $m$. A pigeonhole on the finite set of triples $(e, k, l)$ handles both.

**Theorem 3.19.6 (Conjecture P).** Let $p$ be a prime, and let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g \ge 1$. Then $g$ has no planar corner run in four variables. So Conjecture 3.18.39 holds.

Node: SG00000096

*Proof.* Assume that $P_N, P_{N+1}, \dots$ is a planar corner run of $g$, and let $D = \deg_{x, w} g \ge 1$.

Step 1: the restarted runs. Let $m \ge N$. By Lemma 3.19.1 the run from $P_m$ is a planar corner run of the clean polynomial $g^{(m)}$ of degree $D \ge 1$, and Theorems 3.18.26 and 3.18.32 and Corollary 3.18.33 hold for it with $\delta_m$ in place of $1 + \theta$. By Theorem 3.18.32, part 1, $\Lambda^{(m)} = \Lambda^{(m)}_+ \le \Lambda^{(m)}_0$, and $\Lambda^{(m)}$ is finite by Theorem 3.18.26, since $D \ge 1$. For $p^e > D$ we have $(g^{(m)})^{[p^e, 0]} = (g^{(m)})^{[0, p^e]} = 0$, so $\Lambda^{(m)}_e = \infty$. So the minimum $\Lambda^{(m)}_+$ is attained at some $e = e(m) \ge 1$ with $p^e \le D$. Let $c_m \nu_m$ be the term of least value of the pair $H^{(m)}_{e, 1}, H^{(m)}_{e, 2}$, so that $\Lambda^{(m)}_e = v(\nu_m) + p^e \delta_m$.

Step 2: the inequality of order $1$. By Corollary 3.19.3, parts 1 and 2, the inequality $\Lambda^{(m)}_0 \ge \Lambda^{(m)}_e$ is
$$\beta_1 + 1 + \theta \ge v(\nu_m) - (p^e - p)\, v(M_m) + p^e (1 + \theta). \tag{19.2}$$

Step 3: the class of the least term. By Corollary 3.18.33 for the run from $P_m$ and the exponent $e$, the monomial $\nu_m$ has the class $0$. So $c_m \nu_m$ is a term of $\operatorname{cl}_0 H^{(m)}_{e, 1}$ or of $\operatorname{cl}_0 H^{(m)}_{e, 2}$. By Lemma 3.19.2, part 4, $S^e_1 \cup S^e_2$ is not empty, since otherwise both parts of class $0$ are $0$, and there is a $(k, l) = (k(m), l(m)) \in S^e_1 \cup S^e_2$ with
$$v(\nu_m) \ge (p^e - p)\, v(M_m) + v\bigl(g^{[k, l]}(\Phi_m)\bigr) + (k + l - p^e)\, v(M_{m+1}).$$
With (19.2) this gives
$$\beta_1 \ge v\bigl(g^{[k, l]}(\Phi_m)\bigr) + (k + l - p^e)\, v(M_{m+1}) + (p^e - 1)(1 + \theta). \tag{19.3}$$

Step 4: the limit. The triple $(e(m), k(m), l(m))$ takes a finite number of values, since $p^e \le D$ and $k + l \le D$. So one triple $(e, k, l)$ occurs for an infinite set $\Sigma$ of indices $m$. Since $g^{[k, l]} \ne 0$, Theorem 3.18.26, parts 1 and 2, gives $v(g^{[k, l]}(\Phi_m)) = \beta_{kl}$ for $m$ large, and $\beta_{kl}$ is finite. We have $k + l - p^e \ge 0$ and $v(M_{m+1}) \to 1 + \theta$. So, as $m \to \infty$ in $\Sigma$, (19.3) gives
$$\beta_1 \ge \beta_{kl} + (k + l - 1)(1 + \theta). \tag{19.4}$$

Step 5: Statement D for a first derivative. By Lemma 3.19.2, part 4, $k$ and $l$ are not both divisible by $p$, and $(k, l)$ is not $(1, 0)$ or $(0, 1)$. Assume that $p \nmid k$. Then $k \ge 1$, and by (18.5), $(g^{[1, 0]})^{[k - 1, l]} = \binom{k}{1} g^{[k, l]} = k\, g^{[k, l]}$, which is not $0$, since $k$ is a unit of $K$. So $f = g_X$ is not $0$, $f^{[k - 1, l]} \ne 0$, $(k - 1, l) \ne (0, 0)$, and $\beta_{k - 1, l}(f) = \beta_{kl}$. Theorem 3.18.26, part 1, for $f$ gives
$$\beta_1 \le v(g_X(\Phi_\infty)) < \beta_{k - 1, l}(g_X) + (k + l - 1)(1 + \theta) = \beta_{kl} + (k + l - 1)(1 + \theta),$$
which contradicts (19.4). If $p \mid k$, then $p \nmid l$, so $l \ge 1$ and $(k, l - 1) \ne (0, 0)$, and the same argument with $f = g_W$ and $(g^{[0, 1]})^{[k, l - 1]} = l\, g^{[k, l]}$ gives the contradiction. $\square$

**Corollary 3.19.7 (Conjecture L).** Let $p$ be a prime, and let $g \in K[[y, z]][x, w]$ be clean. Then each corner run in four variables of $g$ is linear, and Conjecture L (Conjecture 3.17.18) holds for it. By Theorem 3.18.19 the same holds in each free coordinate system.

Node: SG0000006Z

*Proof.* If $\deg_{x, w} g = 0$, then $g \in K[[y, z]]$ is not $0$, since $\operatorname{ord} g \ge p$, and (★★) holds at $P_N$. So Proposition 3.17.3 (or Lemma 3.18.3) gives $\rho = 0$ at a later point, and there is no run. If $\deg_{x, w} g \ge 1$, the run is not planar by Theorem 3.19.6, so it is linear (Definition 3.17.5), and Theorem 3.18.19 gives Conjecture L in each free coordinate system. $\square$

**Example 3.19.8.** Let $p = 3$ and $g = Y x^3 w + \alpha x + B_0$, clean, with $Y \ne 0$. This $g$ does not satisfy (C), since $g^{[3, 0]} = Y W$ depends on $W$, and it is not in $K[[y, z]][x^3, w^3]$. So Section 3.18 does not cover it. Here $g_X = \alpha$, since $3 Y x^2 w = 0$, and $g_W = Y X^3$, $g^{[3, 0]} = Y W$, $g^{[3, 1]} = Y$ and $g^{[0, 3]} = 0$. Only $e = 1$ occurs, since $9 > 4$. In (19.1) the terms are $(k, l) = (3, 0)$, which is cleaned, and $(3, 1)$, which is not, and $M^{p^e - p} = 1$. So
$$H^{(m)}_{1, 1} = \operatorname{cl}(Y \psi_m) + Y \Delta\psi_m, \qquad H^{(m)}_{1, 2} = 0, \qquad \operatorname{cl}_0 H^{(m)}_{1, 1} = \operatorname{cl}_0(Y \Delta\psi_m).$$
A planar run needs, at each late $P_m$, $\beta_1 \ge v(\nu_m) + 2(1 + \theta)$ by (19.2) and $v(\nu_m) \ge v(Y) + v(M_{m+1})$ by Step 3. In the limit $\beta_1 \ge v(Y) + 3(1 + \theta)$. This is (19.4) for $(k, l) = (3, 1)$. Statement D for $g_W = Y X^3$ with the index $(3, 0)$ says $v(Y \varphi_\infty^3) < v(Y) + 3(1 + \theta)$, and this is visible by hand: $Y \varphi_\infty^3 = \sum_j a_j^3 Y M_{j+1}^3$ has an infinite number of distinct terms below $v(Y) + 3(1 + \theta)$. So $\beta_1 \le v(g_W(\Phi_\infty)) < v(Y) + 3(1 + \theta)$, a contradiction. The power $M^{1 - p} = M^{-2}$ of Lemma 3.19.2, part 1, is necessary here: with $M^{-1}$ in its place the bound in the limit is only $v(Y) + 2(1 + \theta)$, and there is no contradiction.

**Remark 3.19.9.**

1. The restart is necessary. At $P_N$ alone, Steps 2 and 3 give (19.3) with $m = N$, and this is weaker than Statement D by $(k + l - p^e)(1 + \theta - v(M_{N+1}))$. So no contradiction follows, as Example 3.19.4 shows.
2. The finite degree in $x, w$ is used twice: in Step 1, where $p^e \le D$ makes the minimum $\Lambda^{(m)}_+$ attained, and in Step 4, for the pigeonhole on the triples $(e, k, l)$. For a power series in $x, w$ both fail as stated, and Theorems 3.18.26 and 3.18.32 are proved only for polynomials. So the theorem says nothing about $g \in K[[y, z]][[x, w]]$ or about $g \in K[[x, y, z]]$.
3. If $g_X = g_W = 0$, then $g \in K[[y, z]][x^p, w^p]$, each nonzero $g^{[k, l]}$ has $p \mid k$ and $p \mid l$ by the theorem of Lucas, and $S^e_1 \cup S^e_2 = \emptyset$. Then Step 3 alone gives the contradiction. This is a new proof of Theorem 3.18.35.
4. The theorem contains Theorems 3.18.17, 3.18.34 and 3.18.35 and Theorem 3.19.5 as statements. Their proofs are used only through Theorems 3.18.26 and 3.18.32 and Corollary 3.18.33. It also contains the shape $g = Y x^2 w + Y' x w^2 + B_1 x^2 + B_2 w^2 + B_0$ with $p = 2$, which was the first open case at the end of Section 3.18.
5. The proof does not give Conjecture L°, Hypothesis H1 or Conjecture L+ for the linear runs. The next part treats one case.

### Linear runs of cubics in characteristic 2

By Corollary 3.19.7 each corner run of a clean cubic is linear. Conjecture L° and Hypothesis H1 ask more: the corner curves have $\nu^G \ge \rho$, and $\operatorname{in} G_m$ is a form in the free coordinate whose translations are $0$. For an origin run from some point on both hold by Theorem 3.14.7. So let the run be linear with an infinite number of nonzero translations. In this part $p = 2$ and $\deg_{x, w} g = 3$.

*Adapted coordinates.* Let $(\alpha_0, \beta_0) \ne (0, 0)$ with $\alpha_0 a_j + \beta_0 b_j = 0$ for $j \ge J$, and complete $x' = \alpha_0 x_J + \beta_0 w_J$ to a linear free coordinate system $(x', w')$ at $P_J$. By Lemma 3.17.2, part 3, the translations of $x'$ are $0$ after $J$, and an infinite number of the translations of $w'$ are not $0$. In characteristic $2$ a linear change does not keep the cleanness in degree $2$: a monomial $x w$ with a coefficient of class $0$ can give $x'^2$ with a coefficient of class $0$. But by definition the function of a point in the coordinates $(x', w')$ is the cleaning of the function written in these coordinates (Section 3.17), and by Lemma 3.17.2, part 1, $\rho$ and the steps do not change. By Lemma 3.19.1 we may start the run at $P_J$ and rename $J$ as $N$. Then $a_j = 0$ for each $j \ge N$, $\varphi_m = 0$, an infinite number of the $b_j$ are not $0$, and
$$g = E_3 x^3 + x^2 (\alpha + \beta w) + x E_1(w) + f(w), \qquad f = f_0 + f_1 w + f_2 w^2 + f_3 w^3,$$
with $E_3, \alpha, \beta, f_i \in K[[y, z]]$ and $E_1 \in K[[y, z]][w]$ of degree at most $2$. Since $g$ is clean, $\alpha$, $f_0$ and $f_2$ have only monomials of nonzero class.

**Lemma 3.19.10.** In adapted coordinates, the function of $P_m$ is $g^{(m)} = \sum_{i, l} B^{(m)}_{il} x_m^i w_m^l$, with $M = M_m$ and:

1. $B^{(m)}_{30} = M E_3$ and $B^{(m)}_{1l} = M^{l - 1} E_1^{[l]}(\psi_m)$;
2. $B^{(m)}_{21} = M \beta$ and $B^{(m)}_{20} = \operatorname{cl}(\alpha + \beta \psi_m) = \alpha + \sum_{N \le j < m} b_j \operatorname{cl}(\beta M_{j+1})$;
3. $B^{(m)}_{03} = M f_3$, $B^{(m)}_{02} = \operatorname{cl}(f_2 + f_3 \psi_m) = f_2 + \sum_{N \le j < m} b_j \operatorname{cl}(f_3 M_{j+1})$, $B^{(m)}_{01} = M^{-1}(f_1 + f_3 \psi_m^2)$ and $B^{(m)}_{00} = M^{-2} \operatorname{cl} f(\psi_m)$.

For $m$ large, the coefficients of $x_m$ and of $x_m^3$ are $0$ or a constant times a Laurent monomial times a unit of $K[[w_m, y_m, z_m]]$.

*Proof.* Lemma 3.17.1 with $\varphi_m = 0$ gives $A_{il} = M^{i + l} E_i^{[l]}(\psi_m)$, with $E_2 = \alpha + \beta w$ and $E_0 = f$. The cleaning acts only on the $(i, l)$ with $i$ and $l$ even, that is, on $(0, 0)$, $(2, 0)$ and $(0, 2)$. In characteristic $2$, $f' = f_1 + f_3 w^2$ and $f^{[2]} = f_2 + f_3 w$. The cleaning is additive, $\operatorname{cl} \alpha = \alpha$ and $\operatorname{cl} f_2 = f_2$, and the factor $M^2$ has the class $0$, so fact 2 applies. The factor $M^{-2}$ of the function gives the powers of $M$. The coefficient of $x_m^i$ for $i$ odd is $M^{i - 2} E_i(\psi_m + M w_m)$, and nothing in it is cleaned. So the last claim is Lemma 3.18.2 for $E_1$ and for the constant $E_3$. $\square$

The pairs $(B_{20}, B_{21})$ and $(B_{02}, B_{03})$ are additive towers of the kind of Lemma 3.18.5, and the derivative $f_1 + f_3 \psi_m^2$ of the constant term is a polynomial in $\psi_m^2$. These are the obstructions in the rest of this part.

**Theorem 3.19.11.** Let $p = 2$, let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g = 3$, and let $P_N, P_{N+1}, \dots$ be a corner run in four variables of $g$ with an infinite number of nonzero translations. Let $J$ and $(x', w')$ be adapted coordinates at $P_J$ as above, and assume that the function of $P_J$, written in $(x', w', y_J, z_J)$ and cleaned, has no monomial $x'^2 w'$, $w'^2$ or $w'^3$, that is,
$$g^{(J)} = E_3 x'^3 + \alpha x'^2 + x' E_1(w') + f_0 + f_1 w'.$$
Then there are an $m_0 \ge J$ and a free coordinate system $(x'', w'')$ at $P_{m_0}$, with $x''$ the transform $x'_{m_0}$ of $x'$ and $w''$ equal to $w'_{m_0}$ times a unit, whose translations of $x''$ are $0$, such that for $m$ large:

1. $\operatorname{in} G_m = c\, x_m''^{\,d}$ with $c \in K^*$ and $d \in \{2, 3\}$, and $\rho \in \{d - 1, d\}$, with $\rho = 2$ if $d = 3$;
2. the corner curves $V(x''_m, w''_m, y_m)$ and $V(x''_m, w''_m, z_m)$ have $\nu^G = d \ge \rho$.

The same initial form $c\, x_m'^{\,d}$ holds in the coordinates $(x'_m, w'_m)$. So Hypothesis H1 in the form $\operatorname{in} G_m \in K[x'_m]$ and Conjectures L and L° hold for the run.

Node: SG0000009H

*Proof.* We start the run at $P_J$ and rename $J$ as $N$, as above. Then $\beta = f_2 = f_3 = 0$, and by Lemma 3.19.10 the function of $P_m$ is
$$g^{(m)} = M_m E_3\, x_m^3 + \alpha\, x_m^2 + M_m^{-1} E_1(\psi_m + M_m w_m)\, x_m + M_m^{-1} f_1\, w_m + M_m^{-2} \operatorname{cl}(f_0 + f_1 \psi_m).$$
At each $P_m$ only the constant term is cleaned. The coefficient of $x_m^2$ is $\alpha$ at each level, and its monomials have a nonzero class, so they are never removed. This is the situation of Proposition 3.18.4, with $I \subseteq \{1, 2, 3\}$ in place of $I \subseteq \{1, \dots, p - 1\}$ and with $f = f_0 + f_1 w$ of degree less than $p$ in $w$. We check that the proofs of Proposition 3.18.4, Lemma 3.18.5 and Theorem 3.18.6 go through.

Proposition 3.18.4 uses $\deg_{x, w} g < p$ in three places. The cleanness after the linear change is replaced by the definition of the function in the coordinates $(x', w')$. The claim that only $A_{00}$ is cleaned holds by Lemma 3.19.10, as we saw. The form $f_{m_0} = \mu w'' + e_0$ holds since $\deg_w f \le 1$. Lemma 3.18.2 applies to $E_1$, to $E_3$ and to the constant $\alpha$, and it gives the forms $c_i D_i (1 + h_i)$ for $i \in I$. For $f_1 \ne 0$ it gives $f_1 = c \nu \varepsilon$ at a late level $m_0$, with $\varepsilon$ a unit of $K[[y_{m_0}, z_{m_0}]]$, and we put $w'' = \varepsilon w'_{m_0}$. This change fixes $x'_{m_0}$, $y_{m_0}$ and $z_{m_0}$, and the series stays clean: the monomials with $x^1$ or $x^3$, or with $w''^1$ and no $x$, are not squares, the coefficient $\alpha$ of $x^2$ does not change, and the constant term is clean. Lemma 3.18.5 uses that the term $c_i D_i (1 + h_i) x^i$ is not cleaned at the later points. For $i$ odd this is $p \nmid i$. For $i = 2$ the coefficient at the level $m$ is $\alpha M'^2$, with $M' = M_m / M_{m_0}$, and its monomials have the nonzero class of the monomials of $\alpha$.

Steps 0 to 4 of the proof of Theorem 3.18.6 use only these forms, Lemma 3.18.3 and Lemma 3.18.1, and not the bound $i < p$. Step 5 gives, with $i_0$ the largest $i \in I$ with the least $\kappa_i$, the list of degrees of the terms of $G_m$, and this list uses only $i_0 \ge 2$. If $i_0 = 1$, then $G_m$ has the monomial $x_m$, so $\rho = 0$, which is false. So $d = i_0 \in \{2, 3\}$ and $\operatorname{in} G_m = c\, x_m''^{\,d}$. By Theorem 3.1.4, part 2, $\rho \ge d - 1$. If $d = 3$, the monomial $x_m^3$ of $G_m$, with $2 \nmid 3$, gives $\rho \le 2$, so $\rho = 2$. If $d = 2$, the monomial $y_m^{r_y} z_m^{r_z} x_m^2$ of $g^{(m)}$ is a term of the coefficient $\alpha M'^2$ of $x_m^2$, so its class is not $0$, and $r_y$ or $r_z$ is odd. By the description of $\rho$ in the setting of Section 3.18, the monomial $x_m^2$ of $G_m$ then gives $\rho \le 2$. So $\rho \in \{1, 2\} = \{d - 1, d\}$.

Step 6 of the proof of Theorem 3.18.6 does not change: each monomial $x^i w^l y^j z^k$ of $G_m$ has $i + l + j \ge i_0$ and $i + l + k \ge i_0$, so $\nu^G = d$ on both corner curves, and $d \ge \rho$. The change from $w''_m$ to $w'_m$ fixes $x_m$, $y_m$ and $z_m$, and its linear part fixes $x_m$. As at the end of Step 5 of the proof of Theorem 3.18.6, the function in the coordinates $(x'_m, w'_m)$ has the same $G_m$ up to terms of degree larger than $d$ and terms that the cleaning removes. The cleaning does not remove $y_m^{r_y} z_m^{r_z} x_m^d$: for $d = 3$ since $2 \nmid 3$, and for $d = 2$ since its class is not $0$. So $\operatorname{in} G_m = c\, x_m'^{\,d}$ also in these coordinates, and $x'_m$ is the transform of the linear form $x'$. $\square$

The hypothesis is made at $P_J$ and not at $P_N$. The next example shows that it does not pass from $P_N$ to $P_J$ when the translations of $x'$ are not $0$ between $N$ and $J$.

**Example 3.19.12.** Let $p = 2$ and $g = y x w^2 + y z x^2 + x^3$. It is clean, it has $\operatorname{ord} g = 3 \ge 2$, and it has no monomial $x^2 w$, $w^2$ or $w^3$. Take one $z$-chart step with the translation $(a, b) = (1, 0)$, that is, $z = z_1$, $y = z_1 y_1$, $x = z_1 (x_1 + 1)$ and $w = z_1 w_1$. The term $y x w^2$ goes to $z_1^4 y_1 (x_1 + 1) w_1^2$, and with the factor $z_1^{-2}$ it gives $y_1 z_1^2 (x_1 + 1) w_1^2$. This contains the monomial $y_1 z_1^2 w_1^2$, whose class $(1, 0)$ is not $0$. So it is not cleaned, and the function of $P_1$ has a monomial $w_1^2$. If the translations of $x$ are $0$ after this step, then $J = N + 1$ and $x' = x$, and the hypothesis of Theorem 3.19.11 holds at $P_N$ but not at $P_J$.

**Remark 3.19.13.** Theorem 3.19.11 does not claim Conjecture L+, that is, the order $\nu^G \ge \rho$ along the corner surfaces. In Step 3 of the proof of Theorem 3.18.6 the term with $w_m$ gives the order $i_0 - 1$ along the surfaces, and this is less than $\rho$ if $i_0 = 2 = \rho$. The tests of Remark 3.19.15 found Conjecture L+ at all the linear leaves, so it may still hold.

**Conjecture 3.19.14.** Let $p = 2$, and let $g \in K[[y, z]][x, w]$ be clean with $\deg_{x, w} g = 3$. For each corner run in four variables of $g$ with an infinite number of nonzero translations, and adapted coordinates $(x', w')$, we have $\operatorname{in} G_m = c\, x_m'^{\,d}$ with $c \in K^*$ and $d \in \{\rho, \rho + 1\}$ for $m$ large, and the corner curves have $\nu^G \ge \rho$.

Node: SG0000009J

By Theorem 3.19.11 the open part is the case where the function of $P_J$ has one of the monomials $x'^2 w'$, $w'^2$ or $w'^3$ in adapted coordinates. In the language of the proof of Theorem 3.18.6 one needs two things. First, a bound in the limit on the terms of the towers $B_{20} = \alpha + \sum_j b_j \operatorname{cl}(\beta M_{j+1})$ and $B_{02} = f_2 + \sum_j b_j \operatorname{cl}(f_3 M_{j+1})$ below the least $\kappa$, the analogue of Step 1. The criterion (★★) does not give it, since these are not constant terms. Second, a form of $f_m = \mu w'' + e_0$ when $\mu = M_m^{-1}(f_1 + f_3 \psi_m^2)$ does not divide $B_{02}$. This is the four-variable form, for one sequence, of the passage from Theorem 3.15.17 to Section 3.16, and the methods of Section 3.16, the set $\mathcal{T}$ of dominant indices and the identity below $W$, are the natural tools.

### The numerical evidence

**Remark 3.19.15 (the numerical evidence).** The following tests agree with the results of this section. Theorem 3.19.6 does not depend on them. The scripts use a literal blowing up step, with the cleaning and with $\rho$ computed from the four generators of $\widetilde\Theta(G)$, and not the closed form of Lemma 3.17.1.

1. Exact checks of Lemma 3.19.2, parts 1, 2 and 4, and of (19.1) for each $e \ge 1$ with $p^e \le D$, on random clean $g$ of degree $D$ and random words of $3$ to $6$ steps, for $p = 2, 3, 5, 7$ and $D$ up to $10$. No identity failed. Two controls failed as they must: a version of part 1 with $M_m^{-1}$ in place of $M_m^{1 - p}$ failed at most points with $m > N$ for odd $p$, and a version of (19.1) without the factor $M_m^{p^e - p}$ failed at most points with $e \ge 2$. An earlier check for $p = 2$ and $e = 1$ over $\mathbb{F}_2$ and $\mathbb{F}_4$ found no failure in $1000$ runs and $9224$ point checks.
2. Random dives that keep $\operatorname{ord} \ge p$ and $\rho$, from clean starts of degree $3$ over $\mathbb{F}_2$: $840$ starts and $24000$ dives gave $6321$ dives of full depth and no planar one. The control without the condition on $\rho$ gave $296$ planar dives among $518$ of full depth. A second, independent sampler gave $18000$ dives over $\mathbb{F}_2$ at depth $18$, $4000$ over $\mathbb{F}_4$ at depth $14$, and $7000$ in degrees $4$ and $5$ over $\mathbb{F}_2$, with no planar one, and its control in degree $3$ gave $447$ planar dives among $559$ of full depth. Its runs over $\mathbb{F}_3$ are not informative, since its control over $\mathbb{F}_3$ reached no dive of full depth.
3. Random dives for $p = 2, 3, 5$ from starts outside the condition (C), with top parts such as $x^3 w$, $x^3 w + x w^3$, $x^4 w$ and $x^5 w$ and degrees up to $7$, gave no planar dive with $\rho$ kept. The controls without the condition on $\rho$ gave between $80$ and $95$ percent of planar dives, for $p = 2, 3, 5$.
4. At the $3239$ linear leaves of item 2 the initial form was a power of the adapted coordinate, with $d = \rho$ at $2818$ leaves and $d = \rho + 1$ at $421$, and all the corner curves and the corner surfaces had $\nu^G \ge \rho$.

A dive of full depth counts as planar if in both of two late windows the translations span $K^2$ and both charts occur. The fields, the words and the depths are finite, so the tests are evidence only.

### Notes and references

The results of this section are a result of the track C4 of this project (tamnd/singularity#286). They come from notes 69, 71 and 74 of the research notes. Note 69 gave Lemma 3.19.1, Lemma 3.19.2 for $p = 2$, Example 3.19.4, Theorem 3.19.5, Lemma 3.19.10, Theorem 3.19.11 and Conjecture 3.19.14. Note 71 is the referee report on note 69. It found that a remark of note 69, which claimed that the method fails for odd $p$, is false, since it used the factor $M_m^{-1}$ in place of $M_m^{1 - p}$ and dropped the factor $M_m^{p^e - p}$. It proved Lemma 3.19.2 for each $p$, Theorem 3.19.6 and Corollary 3.19.7, and it gave Example 3.19.12 and the two corrections of the proof of Theorem 3.19.11 that are in the text: the hypothesis is made at $P_J$, and the bound $\rho \le d$ for $d = 2$ uses the class of $\alpha$. Note 74 is a second referee of note 71. It found no gap. It gave the proof of Theorem 3.19.6 in five steps, Corollary 3.19.3 and Example 3.19.8, and it added to Lemma 3.19.1 the proof that the top part survives the cleaning. The tests are in the directories `/tmp/bf/69`, `/tmp/bf/71` and `/tmp/bf/74` of these notes.

The outside results are those of Sections 3.17 and 3.18: the pseudo Cauchy sequences of Kaplansky, the generalized stability theorem [Kuh10, Theorem 1.1] and the facts on the henselization in [Kuh-book]. The use of the history of the divisor is from [CJS20]. None of the results has a Lean proof yet.

Several questions are open.

1. Conjecture L° and the form $\operatorname{in} G_m \in K[x'_m]$ of H1 for the linear runs with $\deg_{x, w} g \ge p$ outside $K[[y, z]][x^p, w^p]$. The first case is Conjecture 3.19.14.
2. Conjecture L+ for the linear runs with an infinite number of nonzero translations outside $K[[y, z]][x^p, w^p]$, also in the class of Theorem 3.19.11.
3. Conjecture P for a clean power series in $x, w$, and the statement for $g \in K[[x, y, z]]$. The proof of Theorem 3.19.6 needs a bound on the orders $p^e$ and on the indices $(k, l)$ that matter, for example from the Weierstrass degree of $g$ in $(x, w)$.
