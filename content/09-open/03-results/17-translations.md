---
title: Runs with free translations
nodes: []
sources: [CJS20, Kuh10, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs with free translations

This section reports the seventeenth research result of the milestone S7, from the milestone S7.18. It treats the runs in three variables that take the corners of the divisor for ever, with translations in the free coordinate. The translations form a pseudo Cauchy sequence of transcendental type in the sense of Kaplansky. If there are an infinite number of nonzero translations, then from some point on the derivative of $g$ in the free coordinate is a monomial times a unit. For the points $\mu x + B_0$ no such run keeps $\rho \ge 1$, and for the points of degree less than $p$ in $x$ such a run has only a finite number of nonzero translations. So Volume 7, Question 3.13.18 has a positive answer for these runs. The point $x^2 y z$ for $p = 3$ shows that $\rho$ need not drop. Volume 7, Section 3.15, gives the same results with all the details.

### The problem

Volume 7, Theorem 3.13.27 shows that a corner run with free translations of $B_1 x^p + B_0$ has only a finite number of nonzero translations. After the last one, Theorem 3.13.20 applies and gives the corner curves. For a general $g$ the proof stops, since the cleaning can remove the least term of $g$ at $x = \varphi_m$. The question of this section is what happens for a general $g \in K[[y, z]][x]$.

### The result

We use the setting of Volume 7, Section 3.13. So $n = 3$, $V(y_m)$ and $V(z_m)$ are in $\Delta$, step $m$ is the $y$-chart or the $z$-chart followed by a translation $t_m$ in $x$, each chart occurs an infinite number of times, and $\rho \ge 1$ is the same at each point. Then $x_N = \varphi_m + M_m x_m$ with $\varphi_m = \sum_{j < m} t_j M_{j+1}$, and $v(y_N^a z_N^b) = a + \theta b$ with $\theta$ irrational. Let $a_i$ be the values of $\varphi_m$ after the nonzero translations.

**Lemma 3.17.1.** The residual order $\rho$ does not depend on the free coordinate, and a corner run with free translations from $P_m$ is a corner run with free translations in each free coordinate $x''$ at $P_m$, with the same points, charts and $\rho$. The same holds for $\varepsilon^p g$ with a unit $\varepsilon$.

**Proposition 3.17.2.** If an infinite number of the $t_j$ are not $0$, then $(a_i)$ is a pseudo Cauchy sequence of transcendental type over the completion of $K(y_N, z_N)$.

**Proposition 3.17.3.** Let $g \in K[[y, z]][x]$ be clean with $g_x \ne 0$, and let the run have an infinite number of nonzero translations. Then for $m$ large, $\partial_{x_m} g_m$ is a monomial $\mu_m$ times a unit, $\rho \le \operatorname{ord}(\mu_m / x^r)$, and $g_m = \mu_m x'' + Q(x''^p, y_m, z_m)$ in a free coordinate $x''$.

**Theorem 3.17.4.** In the setting of Proposition 3.17.3, assume that the dominant index of $g$ and $(a_i)$ is $1$, for example $\deg_x g < p$. Let $y^b$ be the leading monomial of $g_x(\varphi_\infty)$. Then only a finite number of the nonzero translations have $y^b M_{j+1}$ not a $p$-th power.

**Theorem 3.17.5.** Let $g = \mu x + B_0$ be clean, with $\mu$ a monomial and $B_0 \in K[[y, z]]$. Then no corner run with free translations keeps $\rho \ge 1$. The same holds for $\mu \varepsilon^p x + B_0$ with a unit $\varepsilon \in K[[y, z]]$.

**Theorem 3.17.6.** Let $g \in K[[y, z]][x]$ be clean with $\deg_x g < p$. Then each corner run with free translations has only a finite number of nonzero translations. After the last one, Volume 7, Theorem 3.13.20 applies, so the corner curves have $\nu^G = d_m \ge \rho$, and Question 3.13.18 has a positive answer for the run.

**Example 3.17.7.** For $p \ge 3$ the point $x^2 y^{p-2} z^{p-2}$ is fixed by the origins of both charts and has $\rho = 1$. So in the class of Theorem 3.17.6 there are runs with $\rho \ge 1$ in which both charts occur an infinite number of times.

### The proof in short

Lemma 3.17.1 uses the module of the logarithmic derivations, which does not depend on the free coordinate. For a free coordinate $x'' = x u + f(y, z)$, the new coordinate after a step has the derivative $u(0)$ in $x_{m+1}$, and the chart is fixed by the component of the divisor that the new point does not lie on.

For Proposition 3.17.2, the sequence has no limit in the completion, since a limit would have an infinite number of terms below the value $1 + \theta$. If it were of algebraic type over the completion, then by density it would be of algebraic type over $K(y_N, z_N)$ and over its henselization. The valuation is an Abhyankar valuation, so by the generalized stability theorem of Kuhlmann the field is defectless, and the henselization is algebraically maximal. A theorem of Kaplansky then gives a limit in the henselization, which lies in the completion. This is a contradiction.

The values of $g$ and of its Hasse derivatives along the sequence are then constant, and one index $h$ dominates the Taylor expansion. A dominance lemma on the exponents, as in Volume 7, Lemma 3.13.19, gives a criterion (★): if the least term of $g$ at $x = \varphi_m$ survives the cleaning and is below the other coefficients, then $\rho$ drops. For Proposition 3.17.3 the same lemma applied to $g_x$ gives the monomial times a unit. For Theorem 3.17.4 the Taylor expansion at $\varphi_\infty$ shows that the cleaning of $g(\varphi_m)$ is $-c_b \sum_{j \ge m} t_j (y^b M_{j+1})^\natural$ below a fixed value, and the left side has only a finite number of terms there. For Theorem 3.17.5, (★) shows that after some index $J$ the constant term $C$ of $g_m$ does not change. Then (★) or the dominance lemma with the monomial $\mu y_N z_N$ gives $\rho = 0$. For Theorem 3.17.6, the normal form of Proposition 3.17.3 is $\mu_m x'' + a_0$ when $\deg_x g < p$, and Lemma 3.17.1 and Theorem 3.17.5 give a contradiction.

### The test data

Two independent sets of scripts tested the results over $\mathbb{F}_2$, $\mathbb{F}_3$, $\mathbb{F}_5$ and $\mathbb{F}_7$, with no shared code.

1. The formula for $g_m$ in the class $\mu x + B_0$ agreed with the charts in $2253$, $2093$ and $2005$ cases for $p = 2, 3, 5$, with no failure.
2. The bound $\rho \le \operatorname{ord}(\mu_m / x^r)$ had no failure at $19954$, $7135$, $4363$ and $7457$ points for $p = 3, 5, 7$ and for $p = 3$ with the degree up to $2p$.
3. For Theorem 3.17.5, a search over all translations that keep $\rho$ found no branch that keeps $\rho$ for more than $4$ steps, with $1368$, $2001$ and $2045$ nodes for $p = 2, 3, 5$.
4. For Example 3.17.7, $\rho$ stayed constant along $40$ steps for $x^2 y z$ with $p = 3, 5$, for $x^3 y z^2$ with $p = 5$ and for two small changes of these points. Random starts with $\deg_x g < p$ kept $\rho$ for $60$ steps in $225$, $269$ and $281$ of $1500$ runs.
5. A search to the depth $30$ from tilted starts with $\deg_x g < p$ found no violating translation among $643$, $493$ and $425$ branches with a nonzero translation for $p = 3, 5, 7$. Earlier searches with about $2.63$ million nodes found none either.

The translations of the tests are in $\mathbb{F}_p$, the words are periodic and the searches have a cap. So the tests are not a proof.

### What the result means

For the corner runs in three variables with free translations, Question 3.13.18 now has a positive answer when $\deg_x g < p$ and for the points $\mu x + B_0$, in addition to the points $B_1 x^p + B_0$ of Volume 7, Theorem 3.13.27. A first form of the result said that $\rho$ drops in the class $\deg_x g < p$. This is false, and Example 3.17.7 shows it. The finiteness of the translations is what remains, and the centers must come from the corner curves. For a general $g$ with $g_x \ne 0$ the problem reduces to the points $\mu x + Q(x^p, y, z)$ with $Q$ depending on $x$. For them the finiteness and the conjecture V of note 28, that no translation has $M_{j+1} / M_m$ with a negative exponent at a base point $P_m$, are open. The conjecture V is also open in the class $\deg_x g < p$. Theorem 3.17.4 is proved only for the dominant index $1$, and the case $h > 1$ has only a partial result.

### Status

The map has the node SG00000062 for Proposition 3.17.2, SG00000063 for Lemma 3.17.1, SG00000064 for Proposition 3.17.3, SG00000065 for Theorem 3.17.4, SG00000066 for Theorem 3.17.5, SG00000067 for Theorem 3.17.6 and SG00000068 for Example 3.17.7. All of them have proofs in the text of Volume 7, Section 3.15, and none has a Lean proof yet. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The results of this section are from note 30 of the research notes, with the corrections and the proofs of the referee report in note 33, and they are a result of the milestone S7.18 of this project (tamnd/singularity#245). The pseudo Cauchy sequences are from the paper of Kaplansky, Maximal fields with valuations, Duke Math. J. 9 (1942). The generalized stability theorem is [Kuh10, Theorem 1.1], and the facts on the henselization are in [Kuh-book]. The use of the history of the divisor is from [CJS20].
