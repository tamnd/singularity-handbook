---
title: The increase of the residual order
nodes: [SG00000015, SG00000016, SG00000017, SG00000039]
sources: [Moh87, HP19a, HP19b, Hau08, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The increase of the residual order

In characteristic $0$, the residual order does not increase under a permissible blowup at the points where the order stays the same. This is the step that makes the induction of the proofs of resolution work. In characteristic $p$ the residual order can increase. In this section we prove Moh's bound for one point blowup, we compute an increase in a short example, we describe the cycle of Hauser and Perlega, along which the residual order tends to infinity, and we report the computations of the lab of the project. We keep the notation of Section 1.3: $K$ is a perfect field of characteristic $p$, $q = p^e$, and $f = z^q + F(x)$.

### Moh's bound

**Theorem 1.4.1 (Moh, for a point blowup).** Let $K$ be a field of characteristic $p$, let $q = p^e$, and let $F \in K[x_1, \dots, x_n]$ be a clean polynomial with $F \ne 0$ and $\operatorname{ord} F \ge q$. Let $E = V(\prod_{i \in \Delta} x_i)$, and let $d$ be the residual order of $f = z^q + F$ for $E$. Take the $x_j$-chart of the point blowup with the translations $t_i$, so that $\pi(F) = x_j^q F'$ and $f' = z^q + F'$ (Lemma 1.3.7), and let $E'$ be the new divisor of Section 1.3. Let $d'$ be the residual order of $f'$ for $E'$, in the coordinates of the chart and after cleaning. Then
$$d' \le d + p^{e-1}.$$
If $q$ does not divide $\operatorname{ord} F$, then $d' \le d$.

Node: SG00000015 · Lean: `Singularity.residualOrderAlong_pointChart_le`, `Singularity.residualOrderAlong_pointChart_le_of_not_dvd`, `Singularity.moh_bound_holds`

The theorem is from [Moh87], and [HP19a, Section 3] states it in this form. The papers measure the residual order in coordinates that the resolution chooses. Theorem 1.4.1 measures it after cleaning in the given coordinates, and it needs no hypothesis on them. By Proposition 1.3.5 this number does not depend on the choice of the coordinates $x$ that keep $E$. It does not need the hypothesis $\operatorname{ord} F' \ge q$, and $K$ need not be perfect or algebraically closed. The Lean proposition `Singularity.moh_bound` is the statement with these extra hypotheses, and `Singularity.moh_bound_holds` proves it. The Lean theorems are for polynomials and for point blowups. A blowup with a larger permissible center is not treated here.

The proof uses linear operators that are diagonal in the basis of the monomials. We write $|\beta| = \beta_1 + \dots + \beta_n$ for $\beta \in \mathbb{N}^n$, and $e_i$ for the unit vectors. An operator $S$ on $K[x]$ is *diagonal* with the weight $w$ if $S(x^\beta) = w(\beta) x^\beta$ for each $\beta$. A diagonal operator does not lower the order, and it keeps the monomials of $P$ with $w(\beta) \ne 0$. We use three such operators, for $h \ge 1$ and an index $i$:

* the operator $\Theta^{(h)}$ with the weight $\binom{|\beta|}{h}$;
* the operator $\theta_j^{(h)}$ with the weight $\binom{\beta_j}{h}$;
* the operator $x_i^h D_i^{(h)}$ with the weight $\binom{\beta_i}{h}$, where $D_i^{(h)}(x^\beta) = \binom{\beta_i}{h} x^{\beta - h e_i}$ is the Hasse derivative.

We also use two facts on binomial coefficients in characteristic $p$. Since $(1 + s)^{p^v b} = (1 + s^{p^v})^b$, the coefficient $\binom{p^v b}{h}$ is $0$ in $K$ if $p^v \nmid h$. So if $q \mid a$ and $0 < h < q$, then $\binom{a}{h} = 0$ in $K$. And if $q \nmid a$, write $a = p^v b$ with $p \nmid b$. Then $v < e$ and $\binom{a}{p^v} = b \ne 0$ in $K$.

*Proof.* Let $m = \operatorname{ord} F$, and let $x^\alpha$ be a monomial of $F$ with $|\alpha| = m$. Write $F = x^r G$ as in Definition 1.3.3, with $r_i = 0$ for $i \notin \Delta$. Then $\operatorname{ord} G = d$ and $m = |r| + d$.

*Step 1: the monomial factor of $F'$.* For $i \ne j$, $\pi(x_i) = x_j (x_i + t_i)$. So $\pi(x^r) = x_j^{|r|} x^{N'} U$, where $N'_i = r_i$ for $i \ne j$ with $t_i = 0$, $N'_i = 0$ for the other $i$, and $U = \prod_{i \ne j, t_i \ne 0} (x_i + t_i)^{r_i}$. Each monomial of $G$ has degree at least $d$, so $\pi(G) = x_j^d G_1$ for a polynomial $G_1$. Thus
$$F' = x^N U G_1, \qquad N = (m - q) e_j + N'.$$
So $x^N$ divides each monomial of $F'$, and also each monomial of the clean part $C$ of $F'$. The vector $N$ is $0$ outside $\{j\} \cup \{ i \in \Delta : i \ne j, t_i = 0 \}$, and this set is the set of the components of $E'$. So the exponents $r'$ of Definition 1.3.3 for $C$ and $E'$ satisfy $r' \ge N$. If $C \ne 0$, this gives $d' = \operatorname{ord} C - |r'|$, and thus
$$d' + |N| \le \operatorname{ord} C. \tag{1}$$

*Step 2: a diagonal operator on $F$.* Let $S$ be diagonal with a weight $w$ such that $w(\alpha) \ne 0$. Then $\operatorname{ord} S(F) = m$, since $S$ does not lower the order and keeps $x^\alpha$. The support of $S(F)$ is in the support of $F$, so $S(F) = x^r H$ with $\operatorname{ord} H = m - |r| = d$. As in Step 1, $\pi(S(F)) = x_j^{|r|} x^{N'} U \pi(H)$. By Theorem 2.2.2, the weak transform $x_j^{-d} \pi(H)$ has order at most $d$, so $\operatorname{ord} \pi(H) \le 2d$. The orders of $x^{N'}$ and $U$ are $|N'|$ and $0$, so
$$\operatorname{ord} \pi(S(F)) \le |r| + |N'| + 2d = m + |N'| + d. \tag{2}$$

*Step 3: the case $q \nmid m$.* Take $h = p^v$ with $v < e$ and $\binom{m}{h} \ne 0$ in $K$. Apply (2) with $S = \Theta^{(h)}$. The $x_j$-exponent of each monomial of $\pi(x^\beta) = x_j^{|\beta|} \prod_{i \ne j} (x_i + t_i)^{\beta_i}$ is $|\beta|$, so $\theta_j^{(h)} \pi(P) = \pi(\Theta^{(h)} P)$ for each $P$. Since $h < q$, $\binom{\beta_j + q}{h} = \binom{\beta_j}{h}$ in $K$, so $\theta_j^{(h)}(x_j^q P) = x_j^q \theta_j^{(h)} P$. The operator $\theta_j^{(h)}$ kills the monomials in $q \mathbb{N}^n$, so $\theta_j^{(h)} F' = \theta_j^{(h)} C$. Thus
$$\pi(\Theta^{(h)} F) = \theta_j^{(h)}(x_j^q F') = x_j^q \theta_j^{(h)} C.$$
The operator $\theta_j^{(h)}$ does not lower the order. With (2), $q + \operatorname{ord} C \le m + |N'| + d$. In particular $C \ne 0$. Since $|N| = m - q + |N'|$, (1) gives $d' \le d$.

*Step 4: the case $q \mid m$.* Since $F$ is clean, $\alpha \notin q \mathbb{N}^n$. If $q \mid \alpha_i$ for each $i \ne j$, then $q \mid m - \sum_{i \ne j} \alpha_i = \alpha_j$, a contradiction. So there is an $i \ne j$ with $q \nmid \alpha_i$. Take $h = p^v$ with $v < e$ and $\binom{\alpha_i}{h} \ne 0$ in $K$, and apply (2) with $S = x_i^h D_i^{(h)}$. The operator $D_i^{(h)}$ is the coefficient of $s^h$ of the substitution $x_i \mapsto x_i + s$. The chart sends $x_i + s$ to $x_j (x_i + t_i) + x_j s$, so $D_i^{(h)} \pi(P) = x_j^h \pi(D_i^{(h)} P)$. Also $D_i^{(h)}$ commutes with the multiplication by $x_j^q$, and it kills the monomials in $q \mathbb{N}^n$, so $D_i^{(h)} F' = D_i^{(h)} C$. Thus
$$\pi(x_i^h D_i^{(h)} F) = (x_i + t_i)^h x_j^h \pi(D_i^{(h)} F) = (x_i + t_i)^h D_i^{(h)} \pi(F) = (x_i + t_i)^h x_j^q D_i^{(h)} C.$$
The operator $x_i^h D_i^{(h)}$ does not lower the order, so $\operatorname{ord} C \le h + \operatorname{ord} D_i^{(h)} C$. With (2), $q + \operatorname{ord} C \le h + m + |N'| + d$. In particular $C \ne 0$. Then (1) gives $d' \le d + h \le d + p^{e-1}$. $\square$

The Lean proof follows these steps. It defines the operators as the coefficients of $s^h$ of the substitutions $x_i \mapsto x_i + s$, $x_j \mapsto x_j (1 + s)$ and $x_l \mapsto x_l (1 + s)$ for each $l$, from $K[x]$ to $K[x][s]$. It proves the two chain rules of Steps 3 and 4 as identities of ring maps. The main theorems use only the axioms `propext`, `Classical.choice` and `Quot.sound`. Hauser gives a further analysis of the increase and necessary conditions on $F$ for an increase in [Hau10], and Hauser and Perlega characterize the increase in [HP19b]. Hauser studies the points where the invariant increases, the *kangaroo points*, in [Hau08].

Moh also claimed a stronger result, the *stability theorem*: along a sequence of permissible blowups under which the order of the strict transforms of $f$ stays $q$, the residual order never exceeds $d + p^{e-1}$ [Moh87]. If it were true, the residual order could not increase without bound, and a refined invariant might drop in the long run. The rest of this section shows that the claim is false.

### An increase in one blowup

Moh's proof of the stability theorem uses this step [HP19a, Section 3]. Let $r$ be the largest integer such that the initial form of $F$ is a $p^r$-th power. Moh assumes, without loss of generality, that $p^r$ divides $d$, and concludes that $d' \le \lfloor d/p^r \rfloor p^r + p^r$ after one blowup. The next example, from [HP19a, Section 3], shows that this bound is false.

**Example 1.4.2.** Let $p = 2$ and $q = 4$, and let
$$f = z^4 + x^2 y^2 w^3 \bigl(w (x + y)^4 + x^{13}\bigr), \qquad E = V(xyw).$$
By Example 1.3.4, $F$ is clean, $G = w (x + y)^4 + x^{13}$, and the residual order is $d = 5$. The initial form of $F$ is
$$x^2 y^2 w^3 \cdot w (x + y)^4 = x^6 y^2 w^4 + x^2 y^6 w^4 = (x^3 y w^2 + x y^3 w^2)^2.$$
It is a square, and it is not a fourth power, because the exponent $6$ is not divisible by $4$. So $p^r = 2$, and Moh's bound is $\lfloor 5/2 \rfloor \cdot 2 + 2 = 6$.

Now take the point blowup in the $x$-chart with the translation $y \mapsto y + 1$. That is, $\pi(z) = xz$, $\pi(x) = x$, $\pi(y) = x(y + 1)$ and $\pi(w) = xw$. In characteristic $2$,
$$\pi(x + y) = x + x(y + 1) = xy, \qquad \pi\bigl(w (x + y)^4\bigr) = x^5 w y^4.$$
Thus
$$\pi(F) = x^2 \cdot x^2 (y + 1)^2 \cdot x^3 w^3 \cdot \bigl(x^5 w y^4 + x^{13}\bigr) = x^{12} (y + 1)^2 w^3 \bigl(w y^4 + x^8\bigr),$$
and by Lemma 1.3.7, with $(y + 1)^2 = y^2 + 1$,
$$F' = x^{-4} \pi(F) = x^8 w^3 \bigl(w y^4 + w y^6 + x^8 + x^8 y^2\bigr).$$
The monomial $x^8 w^4 y^4 = (x^2 w y)^4$ is a fourth power, and it is the only one, since the other exponents of $w$ are $3$. Cleaning removes it:
$$F'^{\mathrm{cl}} = x^8 w^3 \bigl(w y^6 + x^8 + x^8 y^2\bigr).$$
The translation of $y$ is not $0$, so $B = \{x, y\}$ and the new divisor is $E' = V(xw)$. The power series $w y^6 + x^8 + x^8 y^2$ is not divisible by $x$ or by $w$. So $G' = w y^6 + x^8 + x^8 y^2$ and the residual order is $d' = 7$. The order of $f'$ is still $4$.

Thus $d' = 7$ exceeds Moh's bound $6$ for this step. It agrees with Theorem 1.4.1, since $d + p^{e-1} = 5 + 2 = 7$. The Lean theorem `Singularity.Examples.kangaroo` checks by computation in the polynomial ring that $F$ is clean, that $d = 5$, that $\pi(F) = x^4 F'$ with $\operatorname{ord} F' \ge 4$, that $E' = V(xw)$ and that $d' = 7$. The value $p^r = 2$ is not checked in Lean.

Node: SG00000016 · Lean: Singularity.Examples.kangaroo, Singularity.Examples.kangaroo_increase

The mechanism is visible in the computation. The term $w (x + y)^4$ of $G$ has a large order along the line $x = y$, and the translation $y \mapsto y + 1$ moves this line to the new origin. After the blowup, the term $w y^4$ is a fourth power times the exceptional factor $x^8 w^3$, and cleaning removes it. The remaining terms of $G'$ have larger order.

### The cycle of Hauser and Perlega

**Theorem 1.4.3 (Hauser and Perlega).** Let $K$ be an algebraically closed field of characteristic $p$. There is a purely inseparable equation $f = z^{p^3} + F(x_1, \dots, x_n)$ and an infinite sequence of point blowups such that the order of the strict transforms of $f$ stays $p^3$ and their residual orders tend to infinity. For $p = 2$ one can take $n = 5$, and for $p \ge 3$ one can take $n = 4$.

Node: SG00000017 · Lean: none yet (one cycle is certified, Example 1.4.5)

We do not reproduce the proof, which is a long explicit computation [HP19a, Section 4]. We describe the case $p = 2$, with the variables $x, y, u, v, w$. Let $d$ be an even positive integer. The starting equation is
$$f = z^8 + x^{8a+4} y^{8b+4} u^{8r} w^{8s-d} \bigl(w^d (\lambda + u^{2d+6} Q) + x^{d+1} u^{2d+6} A\bigr),$$
where $\lambda \in K^*$, $A$ is a unit, $Q$ is a power series, and $a, b, r, s$ are nonnegative integers with $8s \ge d$. Its residual order is $d$. The first blowup is in the $x$-chart with the translations $y \mapsto y + 1$ and $u \mapsto u + 1$. As in Example 1.4.2, the translation produces a term that cleaning removes, and the residual order increases from $d$ to $d + 4$. This agrees with Theorem 1.4.1, since $p^{e-1} = 4$. A further sequence of point blowups lowers the residual order to $d + 2$ and gives an equation of the same shape as the starting equation, with $d$ replaced by $d + 2$ and with the roles of $y$ and $u$, and of $b$ and $r$, exchanged. The residual order increases only at the first blowup, and the other blowups rebuild the shape of the equation. Thus the cycle can be repeated, and the residual order increases without bound.

Theorem 1.4.3 disproves Moh's stability theorem for $e \ge 3$. For $e = 1$ the stability theorem is known to hold [HP19a, Section 3].

**Remark 1.4.4.** Theorem 1.4.3 is not a counterexample to resolution in characteristic $p$. At several steps of the cycle, a center larger than a point is permissible, and a different sequence of blowups with a larger center need not make the residual order tend to infinity [HP19a, Section 3]. The examples show that, under point blowups in characteristic $p$, the pair (order, residual order) need not decrease in the long run. Thus a proof must choose the centers well, or it must use a secondary invariant that controls the increases.

**Example 1.4.5 (one certified cycle).** Let $K$ be a field of characteristic 2, let $d = 2$, $a = b = r = 0$, $s = 1$, $\lambda = 1$, $A = 1$ and $Q = 0$. Then the starting equation of Theorem 1.4.3 is
$$f_0 = z^8 + F_0, \qquad F_0 = x^4 y^4 w^6 (w^2 + x^3 u^{10}),$$
and the divisor is $xyuw = 0$. The equation is clean, and its residual order along the divisor is $2$. The cycle has seven steps and 20 point blowups. In each chart the total transform of $F$ is $x_j^8 F'$, where $x_j$ is the variable of the chart, and $\operatorname{ord} F' \ge 8$. Thus the order of the strict transform stays 8 at each step. The table gives the blowups and the residual order along the new divisor.

| Step | Blowup | Divisor after | Residual order |
|---|---|---|---|
| start | | $x, y, u, w$ | 2 |
| 1 | $x$-chart, $y \mapsto y + 1$, $u \mapsto u + 1$, then $z \mapsto z + xw$ | $x, w$ | 6 |
| 2 | $x$-chart | $x, w$ | 5 |
| 3 | $u$-chart | $x, u, w$ | 5 |
| 4 | $v$-chart | $x, u, v, w$ | 5 |
| 5 | $w$-chart, $y \mapsto y + 1$, $v \mapsto v + 1$ | $x, u, w$ | 5 |
| 6 | $u$-chart | $x, u, w$ | 4 |
| 7 | $y$-chart, 14 times | $x, y, u, w$ | 4 |

Only step 1 needs cleaning. After the translations, $F$ contains the monomial $x^8 w^8$, which is an eighth power, and the coordinate change $z \mapsto z + xw$ removes it. This is the increase from $d = 2$ to $d + 4 = 6$, the largest increase that Theorem 1.4.1 allows. After step 7 the equation is
$$z^8 + x^{12} y^{2128} u^{84} w^{60} \bigl(w^4 (1 + y^{14} Q') + x^5 y^{14} A'\bigr)$$
for polynomials $Q'$ and $A'$ with $A'(0) = 1$. This is the starting shape with $d + 2 = 4$ in place of $d$, and with $y$ and $u$ exchanged. In the general statement, the units that come from the translations are put into $A$ and $Q$. In the example they stay as explicit polynomials, so $Q'$ and $A'$ are not $0$ and $1$.

Node: SG00000039 · Lean: `Singularity.Examples.hauserPerlegaCycle`, `Singularity.Examples.cycleF7_shape`

The Lean proof checks each chart equation, each weak transform, each bound on the order and each residual order by computation in $K[x, y, u, v, w]$ over an arbitrary field of characteristic 2. It does not treat the other values of the parameters. It does not prove that the residual order tends to infinity when the cycle is repeated, because the next cycle starts from the shape with $Q' \neq 0$ and $A' \neq 1$, and the Lean proof covers only $Q = 0$ and $A = 1$. Thus Theorem 1.4.3 is still without a Lean proof.

### Computations

The lab of the project computes point blowups of purely inseparable equations over $\mathbb{F}_p$. Its experiment E1 makes random walks of point blowups and records the change of the residual order at each step. The engine follows the conventions of Section 1.3, with the residual order taken in the given coordinates after cleaning. The walks start from random clean polynomials $F$ in $n = 2, 3, 4$ variables with $\operatorname{ord} F \ge q + 1$, for $p = 2, 3, 5, 7$ and $q = p$ or $q = p^2$, and also $q = 8$ for $p = 2$. The divisor at the start is $V(x_1 \cdots x_n)$. Each step blows up the origin, chooses a chart and a point over $\mathbb{F}_p$ of the exceptional divisor, and stops when the order of $f'$ drops below $q$ or when the residual order becomes $0$.

The runs of E1 have about $1.0 \cdot 10^7$ walks and $2.6 \cdot 10^7$ steps. They have these results.

1. No step exceeds the bound of Theorem 1.4.1. That is, at each step $d' \le d + p^{e-1}$, with $d$ and $d'$ in the given coordinates.
2. No walk exceeds the bound of the stability theorem. That is, at each step of a walk the residual order is at most $d_0 + p^{e-1}$, where $d_0$ is the residual order at the start. A walk has at most 12 blowups, so this does not contradict Theorem 1.4.3.
3. For $p = 2$ and $p = 3$, in each case, some step has the increase $d' - d = p^{e-1}$, so the bound of Theorem 1.4.1 is sharp on these walks. For $q = 25$ the largest increase is $4$, and for $q = 49$ it is $6$. For $q = 49$ with $n = 3$ or $n = 4$, and for $q = 25$ with $n = 4$, no walk has an increase.
4. The increases are rare. For $p = 2$, $n = 2$ and $q = 2$, the walks have $580121$ steps and $6770$ increases. For $p = 7$, $n = 2$ and $q = 49$, they have $1055815$ steps and $68$ increases.

The runs of the lab are in the directory `lab/runs` of tamnd/singularity. Each run has its spec, its seed and its outputs, and a computation of the same spec gives the same outputs. The data are examples. They prove no statement. Theorem 1.4.1 proves the bound of result 1 for a point blowup in the given coordinates, so the data are a check of the engine and not of the theorem.

The walks also give new instances of the failure in Example 1.4.2. The next one has $p = 3$.

**Example 1.4.6.** Let $p = 3$ and $q = 9$, and let
$$F = 2 x_1^9 x_2^3 x_3^6 + 2 x_1^7 x_2^5 x_3^{10} + 2 x_1^{31} x_2^{15} x_3^{18}, \qquad E = V(x_1 x_2 x_3).$$
No exponent of $F$ is in $9 \mathbb{N}^3$, so $F$ is clean. The exponents of $x_1, x_2, x_3$ that divide $F$ are $7, 3, 6$. So $G = 2 x_1^2 + 2 x_2^2 x_3^4 + 2 x_1^{24} x_2^{12} x_3^{12}$ and $d = 2$. The initial form of $F$ is $2 x_1^9 x_2^3 x_3^6 = (2 x_1^3 x_2 x_3^2)^3$, since $2^3 = 2$ in $\mathbb{F}_3$. It is a cube and it is not a ninth power. So $p^r = 3$, and the bound of the proof of Moh is $\lfloor 2/3 \rfloor \cdot 3 + 3 = 3$.

Take the $x_3$-chart with the translation $x_2 \mapsto x_2 + 2$. That is, $\pi(x_1) = x_1 x_3$, $\pi(x_2) = x_3 (x_2 + 2)$ and $\pi(x_3) = x_3$. Then
$$F' = x_3^{-9} \pi(F) = 2 x_1^9 (x_2 + 2)^3 x_3^9 + 2 x_1^7 (x_2 + 2)^5 x_3^{13} + 2 x_1^{31} (x_2 + 2)^{15} x_3^{55}.$$
In characteristic $3$, $(x_2 + 2)^3 = x_2^3 + 2$. So the first term is $2 x_1^9 x_2^3 x_3^9 + x_1^9 x_3^9$, and the monomial $x_1^9 x_3^9$ is a ninth power. It is the only one, because the other monomials have the exponent $7$ or $31$ in $x_1$. Cleaning removes it. The translation of $x_2$ is not $0$, so the new divisor is $E' = V(x_1 x_3)$. The cleaned $F'$ is divisible by $x_1^7 x_3^9$ and by no higher power of $x_1$ or of $x_3$, so
$$G' = 2 x_1^2 x_2^3 + 2 (x_2 + 2)^5 x_3^4 + 2 x_1^{24} (x_2 + 2)^{15} x_3^{46}.$$
The constant term of $2 (x_2 + 2)^5$ is $2 \cdot 2^5 = 1$ in $\mathbb{F}_3$. So the initial form of $G'$ is $x_3^4$, and $d' = 4$. The order of $F'$ is $20 \ge 9$, so the order of $f'$ is still $9$.

Thus $d' = 4$ exceeds the bound $3$ of the proof of Moh, and it agrees with Theorem 1.4.1, since $d + p^{e-1} = 2 + 3 = 5$. The mechanism is the same as in Example 1.4.2: a translation makes a $q$-th power appear in the term of the smallest order, and cleaning removes it. The walk of Example 1.4.6 is walk 7316 of the case $n = 3$, $q = 9$ in the run `2026-11-24-e1-p3-08768f1a`. The computation above checks it by hand. It has no Lean proof.

**Remark 1.4.7.** A proof by induction needs an invariant that drops at each step, or at least in the long run. The experiment E2 tests four simple candidates on the walks of E1: the pair $(d, N)$ in the lexicographic order, with $N$ the number of terms of the initial form of $G$; the quotient $d/q$; the difference $d - p^r$, with $r$ as in Example 1.4.2; and the pair $(d, -r)$. For each $p$, each of them goes up at some step. For $d/q$ this is clear, since it goes up exactly at the increases of $d$. The bound of the proof of Moh fails on $111$ steps for $p = 2$ and on $30$ steps for $p = 3$, and on no step for $p = 5$ and $p = 7$. This does not show that the bound holds for $p \ge 5$, since the walks for $q = 25$ and $q = 49$ are short and they have few increases.

### Notes and references

Moh's paper is [Moh87]. The counterexample to the stability theorem and the cycles are [HP19a]. Hauser and Perlega characterize the increase of the residual order in [HP19b]. Hauser introduced the term kangaroo point in [Hau08], and [Hau10] surveys the problem. The Lean file `Singularity/Example/HauserPerlegaCycle.lean` certifies Example 1.4.5. The lab of the project computes the example of [HP19a, Section 3] and one cycle of [HP19a, Section 4] again, and its results agree with the paper. The runs of E1 and E2 that this section describes are in `lab/runs` of tamnd/singularity, with the page https://singularity.tamnd.com/lab/.
