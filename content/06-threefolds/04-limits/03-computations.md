---
title: Computations in dimensions three and four
nodes: [SG00000013, SG00000014, SG00000015]
sources: [CP19, HP19a, Moh87]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Computations in dimensions three and four

Section 4.1 lists the results of Chapter 3 that hold in each dimension. Theorem 3.2.6 is one of them: under its hypotheses the invariant $\iota$ does not go up. Its proof in [CP19] does not use $n = 3$. In this section we report an experiment of the lab of the project, the experiment E4. It computes the invariants of Section 3.2 at each step of many random point blowups, for $n = 3$ and for $n = 4$. The question is this.

*Question.* Let $f = z^p + F(x_1, \dots, x_n)$ over $\mathbb{F}_p$ with $F$ clean. Under random point blowups that keep the multiplicity $p$, does $\omega$ or $\iota$ ever go up, and does each increase of $\epsilon$ have the form that Theorem 3.2.6 predicts? Do the answers for $n = 4$ differ from those for $n = 3$?

The answer on the data is no to the first part, yes to the second, and no to the third. The data are examples and prove no statement. The last part of the section says what they do not show.

### The setting

Let $k = \mathbb{F}_p$, let $S = k[[x_1, \dots, x_n]]$, and let $h = Z^p + F$ with $F \in k[x_1, \dots, x_n]$ clean (Volume 7, Definition 1.3.1) and $\operatorname{ord} F \ge p$. The ring $S$ is complete, so it is excellent, and $k$ is perfect. Case 1 of Theorem 1.2.6 holds, since $h$ has no terms in $Z^1, \dots, Z^{p-1}$. The polynomial $h$ is reduced, since a clean $F \ne 0$ is not a $p$-th power. Let $E$ be the divisor of a product of some of the $x_j$. By Proposition 3.2.4 the coordinates $(x; Z)$ are well adapted, and the invariants are read off from $F$:
$$m(x) = p, \qquad \delta(x) = \frac{\operatorname{ord} F}{p}, \qquad \epsilon(x) = \operatorname{ord} F - \sum_{j \in E} r_j,$$
where $r_j$ is the largest integer with $x_j^{r_j} \mid F$. The number $\epsilon(x)$ is the residual order of Volume 7, by Proposition 3.2.4(4). The invariants $\omega(x)$, $\kappa(x)$ and $\iota(x)$ are those of Definition 3.2.5. The engine computes $\omega$ with the next lemma.

**Lemma 4.3.1.** Let $k$ be a field of characteristic $p$, let $F \in k[U_1, \dots, U_n]$, and let $j \in \{1, \dots, n\}$. Then $\partial F/\partial U_j \ne 0$ if and only if $F$ has a monomial $c U^a$ with $c \ne 0$ and $p \nmid a_j$.

Lean: `Singularity.pderiv_ne_zero_iff`

*Proof.* Write $F = \sum_a c_a U^a$. Then $\partial F/\partial U_j = \sum_{a_j \ge 1} a_j c_a U^{a - e_j}$, where $e_j$ is the $j$-th unit vector. The map $a \mapsto a - e_j$ is injective, so distinct monomials of $F$ give distinct monomials, and no two terms cancel. The coefficient $a_j c_a$ is zero exactly when $p \mid a_j$, since $c_a \ne 0$. So $\partial F/\partial U_j \ne 0$ if and only if some $a$ with $c_a \ne 0$ has $p \nmid a_j$. If $a_j = 0$, then $p \mid a_j$, so the condition $a_j \ge 1$ needs no separate mention. $\square$

Apply Lemma 4.3.1 to the initial form of $F$. Then $\omega(x) = \epsilon(x) - 1$ if the initial form of $F$ has a monomial in which some $x_j$ with $\operatorname{div}(x_j) \not\subseteq E$ has an exponent prime to $p$, and $\omega(x) = \epsilon(x)$ otherwise. In particular $\omega(x) = \epsilon(x)$ if $E$ contains all the $\operatorname{div}(x_j)$. The engine computes $\kappa$ only as $1$ or $\ge 2$, as Definition 3.2.5 does. It does not compute the values $2, 3, 4$ of [CP19, Definition 5.1], because they need the coordinate $v = u_3 - \varphi_2$ of the projection (Section 4.1), and the engine cannot choose it.

The blowups are those of Section 3.3: the blowup of the origin, in the $x_j$-chart, at the point with coordinates $t \in \mathbb{F}_p^{n-1}$, with the new divisor $E'$ of Section 3.3. The point $\{x\}$ is permissible of the first kind (Section 3.2). For this center Theorem 3.2.6 says the following.

**Corollary 4.3.2.** Let $(S, h, E)$ be as above, and assume that it satisfies condition (E) and that $\omega(x) > 0$. Let $x'$ be a point over $x$ of the blowup of the closed point. Then $\iota(x') \le \iota(x)$. If also $\epsilon(x') > \epsilon(x)$, then $\epsilon(x) = \omega(x)$ and $\delta(x) \in \mathbb{N}$.

Lean: none yet

*Proof.* The hypotheses of Theorem 3.2.6 hold, as we showed above. Apply it with $Y = \{x\}$. Then the generic point $y$ of $Y$ is $x$, so $\epsilon(y) = \epsilon(x)$ and $\delta(y) = \delta(x)$, and the theorem gives both claims. $\square$

Corollary 4.3.2 rests on Theorem 3.2.6, which we cite and do not prove. If $m(x') = p$, then $\iota(x') \le \iota(x)$ means $\omega(x') \le \omega(x)$, because the value $\kappa \ge 2$ is not split. So on the walks the test of $\iota$ is a test of $\omega$ at the steps with $\omega(x) > 0$.

### The experiment

The experiment E4 uses the random walks of the experiment E1 (Volume 7, Section 1.4) with $q = p$, for $p = 2, 3, 5$ and $n = 3, 4$. A walk starts from a random clean $F$ in $n$ variables with $E = \operatorname{div}(x_1 \cdots x_n)$. At each step it blows up the origin, takes a random point over $\mathbb{F}_p$ of the exceptional divisor at which the order stays $p$, translates it to the origin and cleans. It stops after 12 blowups, when no such point exists, when $\epsilon = 0$, or at a cap on the size of the polynomials. At each step the engine computes $\delta$, $\epsilon$, $\omega$ and $\kappa$ before and after the blowup, and it counts three kinds of failure.

1. *Omega.* $\omega(x') > \omega(x)$, at any step.
2. *Iota.* $\iota(x') > \iota(x)$, at a step with $\omega(x) > 0$.
3. *The jump of epsilon.* $\epsilon(x') > \epsilon(x)$ at a step with $\omega(x) > 0$, and $\epsilon(x) \ne \omega(x)$ or $\delta(x) \notin \mathbb{N}$.

By Corollary 4.3.2, failures of kind 2 or 3 can occur only at a point where condition (E) fails. Theorem 3.2.6 does not cover the steps with $\omega(x) = 0$, so the test of kind 1 also counts steps outside the theorem.

### The data

The next table gives the counts for each $p$ and $n$. The column "$\omega(x) > 0$" is the number of steps from a point with $\omega(x) > 0$. The column "$\omega$ drops" is the share of the steps at which $\omega(x') < \omega(x)$. The column "$\epsilon$ goes up" is the number of steps with $\epsilon(x') = \epsilon(x) + 1$. No step has a larger increase, as Volume 7, Theorem 1.4.1 with $q = p$ predicts.

| $p$ | $n$ | walks | steps | $\omega(x) > 0$ | $\omega$ drops | $\epsilon$ goes up | failures |
|---|---|---|---|---|---|---|---|
| 2 | 3 | 489000 | 2360914 | 1188490 | 22.9% | 4516 | 0 |
| 2 | 4 | 58000 | 264994 | 167073 | 27.8% | 472 | 0 |
| 3 | 3 | 1000000 | 4716878 | 3979140 | 25.8% | 1541 | 0 |
| 3 | 4 | 267000 | 1322391 | 1191556 | 26.4% | 354 | 0 |
| 5 | 3 | 122000 | 554376 | 531702 | 27.3% | 18 | 0 |
| 5 | 4 | 22000 | 113833 | 111414 | 25.1% | 3 | 0 |

The table shows these facts.

1. No step of the six cases is a failure of kind 1, 2 or 3. In particular $\omega$ never goes up, also at the steps with $\omega(x) = 0$.
2. Each increase of $\epsilon$ starts at a point with $\omega(x) > 0$. Indeed a walk stops when $\epsilon = 0$, so $\epsilon(x) \ge 1$ at each step. If $\omega(x) = 0$, then $\epsilon(x) = 1$, and an increase would give $\epsilon(x') = 2$ and $\omega(x') \ge 1 > \omega(x)$, a failure of kind 1. So each of the increases of $\epsilon$ in the table satisfies $\epsilon(x) = \omega(x)$ and $\delta(x) \in \mathbb{N}$, as Corollary 4.3.2 predicts.
3. At each increase of $\epsilon$ the value of $\omega$ stays the same. Indeed $\omega(x') \ge \epsilon(x') - 1 = \epsilon(x) = \omega(x)$, and $\omega(x') \le \omega(x)$ by fact 1.
4. The counts for $n = 4$ are close to those for $n = 3$. For each $p$ the share of the steps at which $\omega$ drops differs by at most 5 percentage points between $n = 3$ and $n = 4$, and the share of the steps at which $\epsilon$ goes up is about the same: $0.19\%$ and $0.18\%$ for $p = 2$, $0.033\%$ and $0.027\%$ for $p = 3$, and $0.003\%$ for $p = 5$. The steps from a point with $\omega(x) = 0$ are fewer for $n = 4$: $50\%$ and $37\%$ of the steps for $p = 2$, $16\%$ and $10\%$ for $p = 3$, and $4\%$ and $2\%$ for $p = 5$. At these steps $\omega$ stays $0$, by fact 1.

The next example is the first increase of $\epsilon$ in the case $p = 2$, $n = 4$. We check it by hand.

**Example 4.3.3.** Let $p = 2$, $n = 4$, $E = \operatorname{div}(x_1 x_2 x_3 x_4)$ and
$$F = x_1 x_2^2 x_3 + x_1^2 x_3^3 + x_1^2 x_3 x_4^2.$$
Each monomial has an odd exponent, so $F$ is clean. We have $\operatorname{ord} F = 4$, so $\delta(x) = 2$, and $r = (1, 0, 1, 0)$, so $\epsilon(x) = 2$. All four variables are in $E$, so $\omega(x) = \epsilon(x) = 2$ and $\iota(x) = (2, 2, \ge 2)$.

*Condition (E).* Modulo 2 we have $\partial F/\partial x_1 = x_2^2 x_3$. So $V(\partial F/\partial x_1, \dots, \partial F/\partial x_4) \subseteq V(x_2 x_3) \subseteq E$, and Lemma 2.3.3 shows that $(S, h, E)$ satisfies condition (E).

*The blowup.* Take the $x_4$-chart at the point $t_1 = 1$, $t_2 = 0$, $t_3 = 1$. That is, $x_1 = x_4 (x_1 + 1)$, $x_2 = x_4 x_2$ and $x_3 = x_4 (x_3 + 1)$. The three monomials become $x_4^4 (x_1 + 1) x_2^2 (x_3 + 1)$, $x_4^5 (x_1 + 1)^2 (x_3 + 1)^3$ and $x_4^5 (x_1 + 1)^2 (x_3 + 1)$. In characteristic 2, $(x_3 + 1)^3 + (x_3 + 1) = (x_3 + 1)(x_3^2 + 1 + 1) = x_3^3 + x_3^2$. So
$$x_4^{-2} F = x_2^2 x_4^2 (x_1 + 1)(x_3 + 1) + x_4^3 (x_1^2 + 1)(x_3^3 + x_3^2).$$
The first product contains the square $x_2^2 x_4^2$, and the translation $Z' \mapsto Z' + x_2 x_4$ removes it. The clean part is
$$F' = x_1 x_2^2 x_3 x_4^2 + x_1 x_2^2 x_4^2 + x_2^2 x_3 x_4^2 + x_1^2 x_3^3 x_4^3 + x_1^2 x_3^2 x_4^3 + x_3^3 x_4^3 + x_3^2 x_4^3.$$
Its order is $5 \ge 2$, so the point $x'$ has $m(x') = 2$, and $\delta(x') = 5/2$. The new divisor is $E' = \operatorname{div}(x_2 x_4)$, since $t_2 = 0$ and $t_1, t_3 \ne 0$. The smallest exponents of $x_2$ and $x_4$ are $0$ and $2$, so $\epsilon(x') = 5 - 2 = 3 = \epsilon(x) + 1$. The initial form is $x_1 x_2^2 x_4^2 + x_2^2 x_3 x_4^2 + x_3^2 x_4^3$. The variable $x_1$ is not in $E'$, and it has the exponent 1 in the first monomial. By Lemma 4.3.1, $\omega(x') = \epsilon(x') - 1 = 2$. So $\iota(x') = \iota(x)$, while $\epsilon$ goes up. The point $x$ satisfies $\epsilon(x) = \omega(x) = 2$ and $\delta(x) = 2 \in \mathbb{N}$, as Corollary 4.3.2 says it must.

Lean: none yet

Example 4.3.3 is the dimension 4 analogue of Example 3.3.1. The mechanism is the same: a translation makes a square appear in the term of smallest order, and cleaning removes it. The example is walk 207, step 1, of the case $n = 4$ in the run `2026-11-25-e4-p2-b049ce95` of the lab. The engine gives the same values.

### What the data does not show

The data are examples. They prove no statement, and they do not prove Corollary 4.3.2 in any case that it does not already cover. We list the limits of the experiment.

1. The walks use only point centers, and only the points over $\mathbb{F}_p$ of the exceptional divisor, in the given coordinates after cleaning. Theorem 3.2.6 is about each point over $x$ and each permissible center, also curves and surfaces, and about residue fields that need not be perfect.
2. The engine does not check condition (E) at the points of a walk. Example 4.3.3 checks it by hand at one point. A failure at a point where condition (E) fails would not contradict Theorem 3.2.6. The data have no failure, so this question does not arise.
3. The values of $\epsilon$ and $\omega$ do not depend on the choice of well adapted coordinates (Proposition 3.2.4(5) and [CP19, Remark 2.69]). So, unlike the steps over the bound of Moh in Volume 7, Section 1.4, a failure in E4 would not be a matter of coordinates. It would have to be checked by hand.
4. The engine computes $\kappa$ only as $1$ or $\ge 2$. It does not compute the projected polygon or its invariants [CP19, (1.5) and Definition 5.1]. So the experiment does not test the Projection Theorem [CP19, Theorem 5.5], and it says nothing about the missing step of Section 4.2, the decrease of the invariant in dimension 4.
5. A walk has at most 12 blowups, and it stops at caps on the size of the polynomials. So the data do not show that $\iota$ goes down in the long run, for $n = 3$ or for $n = 4$.

The agreement of the cases $n = 3$ and $n = 4$ is what Section 4.1 leads one to expect: Theorem 3.2.6 holds in each dimension. The experiment confirms that the engine computes the invariants of Section 3.2 in a way that is consistent with that theorem. It gives no evidence for or against an analogue of the Projection Theorem in dimension 4.

### Notes and references

The invariants and Theorem 3.2.6 are from [CP19, Sections 2.7 and 3]. The walks and the residual order follow Hauser and Perlega [HP19a, Section 2], and Volume 7, Section 1.4, reports the experiments E1 and E2 on the same walks. Moh's bound is from [Moh87]. The specs of E4 are `lab/specs/e4-p2.yaml`, `lab/specs/e4-p3.yaml` and `lab/specs/e4-p5.yaml` of tamnd/singularity, and the runs `2026-11-25-e4-p2-b049ce95`, `2026-11-25-e4-p3-5fdbdc69` and `2026-11-25-e4-p5-1ebbb9f0` are in `lab/runs`. Each run has its seed, and a computation of the same spec gives the same outputs. Lemma 4.3.1 and Example 4.3.3 are ours.

Node: SG00000014 · Lean: `Singularity.charPolyhedron` (the definition of the characteristic polyhedron; the invariants of this section have no Lean definition yet)
