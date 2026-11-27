---
title: Finiteness of the translations
nodes: []
sources: [CJS20, Kuh10, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Finiteness of the translations

This section reports the eighteenth research result of the milestone S7, from the milestone S7.18. It continues Section 3.17 on the corner runs in three variables with free translations. For each clean $g \in K[[y, z]][x]$, each such run has only a finite number of nonzero translations. After the last one, Volume 7, Theorem 3.13.20 gives the corner curves, so Volume 7, Question 3.13.18 has a positive answer for each such run. The key step is an inequality of Kaplansky type, which shows that the tie set of the limit data contains only $1$ and powers of $p$. Volume 7, Section 3.16, gives the same results with all the details.

### The problem

Section 3.17 proves the finiteness of the translations for $\deg_x g < p$ and for the points $\mu x + B_0$. For a general $g$ with $g_x \ne 0$, the normal form of Volume 7, Corollary 3.15.11, reduces the problem to the points $\mu x + Q(x^p, y, z)$, where $Q$ depends on $x$. For these points the coefficients of the powers $x_m^{p i}$ change with $m$, and the proof of Section 3.17 stops. The question of this section is whether the finiteness holds for each clean $g$.

### The result

We use the setting of Section 3.17. Let $g = \mu x + F(x^p)$ with $F(Y) = \sum_k B_k Y^k$ and $B_k \in K[[y, z]]$. If the run has an infinite number of nonzero translations, let $\varphi_\infty$ be the limit of the $\varphi_m$ in the Hahn field, and put $\beta_1 = v(\mu)$, $\beta_{p i} = v(F^{[i]}(\varphi_\infty^p))$, $W_k = \beta_k + k (1 + \theta)$, $W = \min_k W_k$ and $\mathcal{T} = \{k : W_k = W\}$.

**Lemma 3.18.1.** Let $G(Y)$ be a power series that is not constant, with a constant term in $K(y_N, z_N)$ and the other coefficients in $K[[y_N, z_N]]$, and assume that the run has an infinite number of nonzero translations. Then the values $\beta^G_i$ of $G^{[i]}(\varphi_m^p)$ are constant for $m$ large, and for $m$ large and each $i \ge 1$, $$\beta^G_0 < v(G^{[i]}(\varphi_m^p)) + p i \, v(M_m).$$

**Lemma 3.18.2.** Assume that the run has an infinite number of nonzero translations. If $i = p^a s$ with $s > 1$, $p \nmid s$ and $F^{[i]} \ne 0$, then $W_{p^{a+1}} < W_{p i}$. So $\mathcal{T} \setminus \{1\} \subseteq \{p, p^2, p^3, \dots\}$.

**Proposition 3.18.3.** Let $V_m$ be the cleaning of $g(\varphi_m)$, and let $\delta_m = \varphi_\infty - \varphi_m$. Then for $m$ large, $$(V_m)_{< W} = -[1 \in \mathcal{T}] \, \mu \, \delta_m^{\mathrm{tw}} + \sum_{k \in \mathcal{T}, \, k \ge p} e_k (-\delta_m)^k,$$ where $\delta_m^{\mathrm{tw}}$ is the sum of the terms $t_j M_{j+1}$ of $\delta_m$ with $\mu M_{j+1}$ not a $p$-th power, and $e_k$ is the leading term of $g^{[k]}(\varphi_\infty)$. The left side is a finite sum.

**Theorem 3.18.4.** Let $g = \mu x + F(x^p, y, z)$ be clean, with $\mu$ zero or a monomial times a unit. Then each corner run with free translations of $g$ has only a finite number of nonzero translations. The proof treats the three cases $\mathcal{T} = \{1\}$, $1 \notin \mathcal{T}$, and $1 \in \mathcal{T} \ne \{1\}$.

**Lemma 3.18.5.** If a run has an infinite number of nonzero translations, then it has an infinite number of nonzero translations in each free coordinate at each of its points.

**Theorem 3.18.6.** Let $g \in K[[y, z]][x]$ be clean. Then each corner run with free translations has only a finite number of nonzero translations. After the last one, Volume 7, Theorem 3.13.20 applies, so the corner curves have $\nu^G = d_m \ge \rho$, and Question 3.13.18 has a positive answer for the run.

**Example 3.18.7.** For the run that takes the two charts in turn, with $\theta = (1 + \sqrt 5) / 2$, the exponents $n_{j+1}$ of the monomials $M_{j+1} / (y_N z_N)$ satisfy $n_{N+1} + n_{N+5} = 3 n_{N+3}$. So for $p = 3$, if $6$ and $9$ were in $\mathcal{T}$, a cross term of $\delta_m^6$ could cancel a top term of $\delta_m^9$. Lemma 3.18.2 shows that this never occurs.

### The proof in short

For Lemma 3.18.1, a scaling puts the translations on the unit circle, and the Weierstrass preparation theorem in the Tate algebra (Bosch, Güntzer and Remmert, Non-Archimedean Analysis, Section 5.2.2, Theorem 1) writes $G$ as a polynomial times a unit. The transcendental type of Section 3.17, Proposition 3.17.2, then gives the constant values. The inequality follows from the Taylor expansion of $G$ between two late translations: the difference has the value of its least term, and both ends have the value $\beta^G_0$. The sums in the Hahn field are defined by the lemma of Neumann (On ordered division rings, Trans. Amer. Math. Soc. 66 (1949)).

For Lemma 3.18.2, put $G = F^{[p^a]}$. By Lucas's theorem, $G^{[i - p^a]} = s F^{[i]}$. Lemma 3.18.1 for $G$ gives the inequality between the lines of $p^{a+1}$ and $p i$ at the points $v(M_m) < 1 + \theta$, and the line of $p i$ is steeper. So it holds also at $1 + \theta$.

Proposition 3.18.3 is the Taylor expansion of $g$ at $\varphi_\infty$, together with the fact that the criterion (★) of Section 3.17 fails at each point. For Theorem 3.18.4, the case $\mathcal{T} = \{1\}$ uses the identity to show that only a finite number of translations are twisted, and then the dominance lemma at one base point gives $\rho = 0$. The case $1 \notin \mathcal{T}$ follows from Lemma 3.18.1: the constant term is below the other coefficients, and (★) fails only if it is above the linear term, which is too large. In the case $1 \in \mathcal{T} \ne \{1\}$, Lemma 3.18.2 removes the cross terms, and each term of the right side is a constant times $E N_{j+1}^k$. The exponent of $N_{j+1}$ is the sum of a basis of $\mathbb{Z}^2$, so it is primitive, and distinct pairs $(j, k)$ give distinct monomials. So the right side has an infinite number of terms below $W$, which is a contradiction.

For Lemma 3.18.5, write the new coordinate as a unit times $x - \zeta$. If the new run had only a finite number of translations, then $\varphi_b + M_b \zeta$ would be a limit of the translations in the completion, and Proposition 3.17.2 excludes this. Theorem 3.18.6 follows from Theorem 3.18.4 with $\mu = 0$ if $g_x = 0$, and from the normal form of Section 3.17, Proposition 3.17.3, and Lemma 3.18.5 if $g_x \ne 0$.

### The test data

Two independent sets of scripts tested the results over $\mathbb{F}_2$, $\mathbb{F}_3$, $\mathbb{F}_5$ and $\mathbb{F}_7$, with no shared code.

1. A depth first search over the translations that keep $\rho$ in the class $\mu x + F(x^p)$ did $152500$ runs with $28272$ branches of the depth $40$ or $60$. No branch had more than $3$ nonzero translations, and none had a late nonzero translation.
2. The closed form of the transform agreed with the charts in $24000$ checks in the first set of scripts, and in $1176$, $1188$, $2340$, $2400$, $2400$ and $2400$ checks in the second set. A version without the cleaning gave $278$ mismatches of $500$, so the test can see errors.
3. Lemma 3.18.1 had no failure in $4216$ checks, and Lemma 3.18.2 had no failure in $4440$ checks of the weak form and $1878$ checks of the strong form.
4. Starts with a tie of the start data took the designed translations and then no more: $13500$ and $4400$ starts in the first set, and $112971$ runs with $3269796$ nodes and $47968$ deep branches in the second set.
5. The Lucas lemma of the second proof of Lemma 3.18.2 agreed in $61100$ sets in the first set and in $2625$, $19650$, $7875$, $7875$, $31930$ and $222050$ cases in the second set.

The translations of the tests are in $\mathbb{F}_p$, the words are periodic and the searches have a cap. A test sees only a finite part of a run and cannot see the limit data. So the tests are not a proof.

### What the result means

For the corner runs in three variables with free translations, the finiteness of the translations now holds for each clean $g \in K[[y, z]][x]$, and Question 3.13.18 has a positive answer for each such run. This closes the gap that Section 3.17 left for the points $\mu x + Q(x^p, y, z)$. The result does not say that $\rho$ drops, and Example 3.17.7 is a run with $\rho = 1$ at each point. The conjecture V of note 28, that the last polynomial $\varphi_{J+1}$ has no negative exponent in $y_N, z_N$, is still open. The other regimes of the runs, and the runs in four or more variables, are not treated.

### Status

The map has the node SG00000069 for the extension of the closed form to power series in $x$, SG0000006A for Lemma 3.18.1, SG0000006B for Lemma 3.18.2, SG0000006C, SG0000006D and SG0000006E for the three cases of Theorem 3.18.4, SG0000006F for Lemma 3.18.5, SG0000006G for Theorem 3.18.4 and SG0000006H for Theorem 3.18.6. All of them have proofs in the text of Volume 7, Section 3.16, and none has a Lean proof yet. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The results of this section are from notes 34 and 36 of the research notes, with the corrected statements of the referee reports in notes 35 and 37, and they are a result of the milestone S7.18 of this project (tamnd/singularity#245). The strong form of Lemma 3.18.2 is from note 35, and note 36 gives a second proof of its consequence on $\mathcal{T}$ by the transcendence of $\varphi_\infty$. The proof of the case $1 \in \mathcal{T} \ne \{1\}$ by the primitive vectors is new in Volume 7, Section 3.16, and replaces the chain argument of note 34. The pseudo Cauchy sequences are from the paper of Kaplansky, Maximal fields with valuations, Duke Math. J. 9 (1942). The generalized stability theorem is [Kuh10, Theorem 1.1], and the facts on the henselization are in [Kuh-book]. The use of the history of the divisor is from [CJS20].
