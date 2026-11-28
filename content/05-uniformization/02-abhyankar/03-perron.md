---
title: The Perron algorithm
nodes: []
sources: [Zar40, Ful93, Cut99, AKMW02, Kar03]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Perron algorithm

The lattice lemma (Lemma 2.1.4) gives, for each finite set of monomials of nonnegative value, one monomial chart in which all of them are monomials with exponents in $\mathbb{N}$. It does not say how to reach that chart from the original coordinates by blowups. In dimension 2 the quadratic sequence reaches it (the Remark "the quadratic sequence of a monomial valuation is toric" in Section 2.1). This section does the same in each dimension for weights in $\mathbb{R}$. We give a sequence of blowups of strata of codimension 2, each followed by localization at the center of the valuation. We give an explicit rule that chooses the next blowup, and we prove that the rule ends. The problem is classical. It goes back to the algorithm of Jacobi-Perron for continued fractions of several numbers. Zariski used an algorithm of this type in his proof of local uniformization in characteristic 0 [Zar40]. The rule and the proof of termination below are our own. We wrote them for the formalization in Lean, and we do not claim that the statement is new.

We keep the notation of Section 2.1, in rank 1. Let $x_1, \dots, x_r$ be the coordinates of a chart: Laurent monomials that form a basis of the group $M$, or a regular system of parameters at the center of the valuation $v$. Let $\gamma_i = v(x_i)$. We assume that $\gamma_i \in \mathbb{R}$, that $\gamma_i > 0$ for each $i$, and that $\gamma_1, \dots, \gamma_r$ are linearly independent over $\mathbb{Z}$. By the theorem of Hölder this covers the monomial valuations whose value group has rank 1 (Corollary 2.1.10). We call a vector $\gamma \in \mathbb{R}^r$ *positive* if each $\gamma_i > 0$, and *independent* if $a \cdot \gamma = 0$ with $a \in \mathbb{Z}^r$ implies $a = 0$. An *exponent* is a vector $D \in \mathbb{Z}^r$. It gives the Laurent monomial $x^D = \prod_l x_l^{D_l}$, and its value is $v(x^D) = \gamma \cdot D = \sum_l \gamma_l D_l$. We write $D \ge 0$ if $D_l \ge 0$ for each $l$, that is, if $x^D$ is a monomial. For $D, D' \in \mathbb{Z}^r$ we write $D \le D'$ if $D' - D \ge 0$.

### Steps and runs

**Definition 2.3.1 (step).** A *step* is an ordered pair $s = (i, j)$ of indices with $i \ne j$. The step is *valid* for a weight $\gamma$ if $\gamma_i < \gamma_j$. The step changes a weight $\gamma$ into the weight $\gamma^s$ and an exponent $D$ into the exponent $s(D)$, where
$$\gamma^s_j = \gamma_j - \gamma_i, \qquad \gamma^s_l = \gamma_l \ (l \ne j), \qquad s(D)_i = D_i + D_j, \qquad s(D)_l = D_l \ (l \ne i).$$

In Lean these are `Singularity.Perron.stepWeight` and `Singularity.Perron.stepExp`.

The geometric meaning is a blowup. Let $s = (i, j)$ be valid for $\gamma$. Blow up the stratum $V(x_i, x_j)$, the intersection of two coordinate hyperplanes. The blowup has two charts, with $x_j = x_ix_j'$ and with $x_i = x_jx_i'$. We have $v(x_j/x_i) = \gamma_j - \gamma_i > 0$, so $x_j/x_i$ lies in the maximal ideal of $\mathcal{O}_v$, and $x_i/x_j$ does not lie in $\mathcal{O}_v$. So the center of $v$ lies in the first chart. Its coordinates are $x'_j = x_j/x_i$ and $x'_l = x_l$ for $l \ne j$. They are again Laurent monomials that form a basis of $M$, and their values are $\gamma^s$. All values are positive, so the center of $v$ is the origin of the new chart. In the new coordinates,
$$x^D = x_i^{D_i}(x_ix'_j)^{D_j}\prod_{l \ne i, j} x_l^{D_l} = x'^{s(D)}.$$
So the step $s$ records the blowup of $V(x_i, x_j)$ followed by localization at the center of $v$. In dimension 2 the stratum $V(x_1, x_2)$ is the closed point, and the step is a quadratic transform.

The step has a matrix form. Let $E_{ij}$ be the matrix with the entry 1 at the place $(i, j)$ and 0 elsewhere. We write exponents and weights as column vectors. Then $s(D) = (1 + E_{ij})D$, because row $i$ of $(1 + E_{ij})D$ is $D_i + D_j$. The weights satisfy $\gamma = (1 + E_{ij})^T\gamma^s$, because $(1 + E_{ij})^T = 1 + E_{ji}$, and row $j$ of $(1 + E_{ji})\gamma^s$ is $\gamma^s_j + \gamma^s_i = \gamma_j$. For $r = 2$ and $s = (1, 2)$ this reads
$$\begin{pmatrix} D_1 + D_2 \\ D_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} D_1 \\ D_2 \end{pmatrix}, \qquad \begin{pmatrix} \gamma_1 \\ \gamma_2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} \gamma_1 \\ \gamma_2 - \gamma_1 \end{pmatrix}.$$
The two formulas together give $\gamma^s \cdot s(D) = (\gamma^s)^T(1 + E_{ij})D = \gamma \cdot D$. This is part 1 of the next lemma.

**Lemma 2.3.2 (facts on a step).** Let $\gamma \in \mathbb{R}^r$, let $D, D' \in \mathbb{Z}^r$, and let $s = (i, j)$ be a step.

1. (value) $\gamma^s \cdot s(D) = \gamma \cdot D$.
2. (positive) If $\gamma$ is positive and $s$ is valid for $\gamma$, then $\gamma^s$ is positive.
3. (independent) If $\gamma$ is independent, then $\gamma^s$ is independent.
4. (additive) $s(D + D') = s(D) + s(D')$.
5. (cone) If $D \ge 0$, then $s(D) \ge 0$.
6. (distinct) If $\gamma$ is independent and $i \ne j$, then $\gamma_i \ne \gamma_j$. So exactly one of the steps $(i, j)$ and $(j, i)$ is valid for $\gamma$.

Lean: `Singularity.Perron.sum_stepExp_mul_stepWeight` (part 1), `Singularity.Perron.stepWeight_pos` (part 2), `Singularity.Perron.stepWeight_independent` (part 3), `Singularity.Perron.stepExp_add` (part 4), `Singularity.Perron.stepExp_nonneg` (part 5), `Singularity.Perron.ne_of_independent` (part 6)

*Proof.* Only the entries $i$ and $j$ matter in part 1. They contribute $\gamma_i(D_i + D_j) + (\gamma_j - \gamma_i)D_j = \gamma_iD_i + \gamma_jD_j$ on the left, and the same on the right. For part 2, the only new entry is $\gamma_j - \gamma_i$, which is positive because $s$ is valid. For part 3, let $a \in \mathbb{Z}^r$ with $a \cdot \gamma^s = 0$. Then
$$0 = \sum_{l \ne i, j} a_l\gamma_l + a_i\gamma_i + a_j(\gamma_j - \gamma_i) = \sum_{l \ne i, j} a_l\gamma_l + (a_i - a_j)\gamma_i + a_j\gamma_j.$$
Since $\gamma$ is independent, $a_l = 0$ for $l \ne i, j$, and $a_i - a_j = 0$, and $a_j = 0$. So $a_i = 0$ and $a = 0$. Part 4 holds because $D \mapsto s(D)$ is a linear map. Part 5 holds because $D_i + D_j \ge 0$ if $D_i, D_j \ge 0$. For part 6, let $a = e_i - e_j$, where $e_l$ is the $l$-th unit vector. Then $a \ne 0$, so $a \cdot \gamma = \gamma_i - \gamma_j \ne 0$. $\square$

**Definition 2.3.3 (run).** A *run* is a finite list $l = (s_1, \dots, s_m)$ of steps. It acts on weights and exponents step by step: $\gamma^l = (\cdots(\gamma^{s_1})\cdots)^{s_m}$ and $l(D) = s_m(\cdots s_1(D)\cdots)$. The run is *valid* for $\gamma$ if each step $s_k$ is valid for the weight $\gamma^{(s_1, \dots, s_{k-1})}$ before it. For two runs $l_1$ and $l_2$, the run $l_1l_2$ is $l_1$ followed by $l_2$.

In Lean these are `Singularity.Perron.runWeight`, `Singularity.Perron.runExp` and `Singularity.Perron.IsValidRun`. The empty run is valid, and it changes nothing. A valid run is a sequence of blowups of strata of codimension 2, each followed by localization at the center of $v$.

**Lemma 2.3.4 (facts on a run).** Let $\gamma \in \mathbb{R}^r$, let $D, D' \in \mathbb{Z}^r$, and let $l$, $l_1$, $l_2$ be runs.

1. (value) $\gamma^l \cdot l(D) = \gamma \cdot D$.
2. (positive) If $\gamma$ is positive and $l$ is valid for $\gamma$, then $\gamma^l$ is positive.
3. (independent) If $\gamma$ is independent, then $\gamma^l$ is independent.
4. (additive) $l(D + D') = l(D) + l(D')$.
5. (cone) If $D \ge 0$, then $l(D) \ge 0$.
6. (concatenation) $(l_1l_2)(D) = l_2(l_1(D))$ and $\gamma^{l_1l_2} = (\gamma^{l_1})^{l_2}$. If $l_1$ is valid for $\gamma$ and $l_2$ is valid for $\gamma^{l_1}$, then $l_1l_2$ is valid for $\gamma$.

Lean: `Singularity.Perron.sum_runExp_mul_runWeight` (part 1), `Singularity.Perron.runWeight_pos` (part 2), `Singularity.Perron.runWeight_independent` (part 3), `Singularity.Perron.runExp_add` (part 4), `Singularity.Perron.runExp_nonneg` (part 5), `Singularity.Perron.runExp_append`, `Singularity.Perron.runWeight_append`, `Singularity.Perron.isValidRun_append` (part 6)

*Proof.* Parts 1 to 5 follow from the same parts of Lemma 2.3.2 by induction on the length of $l$. In part 2 the induction uses that each step is valid for the weight before it, and that this weight is positive by the induction hypothesis. Part 6 holds by the definition. The steps of $l_1l_2$ are the steps of $l_1$ and then the steps of $l_2$. The weight before a step of $l_2$ is computed from $\gamma^{l_1}$. $\square$

### The theorem

**Theorem 2.3.5 (Perron algorithm).** Let $\gamma \in \mathbb{R}^r$ be positive and independent, and let $D \in \mathbb{Z}^r$ with $\gamma \cdot D > 0$. Then there is a run $l$, valid for $\gamma$, such that $l(D) \ge 0$.

Lean: `Singularity.Perron.exists_isValidRun_runExp_nonneg`

In geometric terms: let $x^D$ be a Laurent monomial of positive value. Then after finitely many blowups of strata of codimension 2, each followed by localization at the center of $v$, the Laurent monomial $x^D$ becomes a monomial in the new coordinates. The proof is in the next subsection. It gives an explicit rule for the run. First we draw two consequences.

**Corollary 2.3.6 (finite sets).** Let $\gamma \in \mathbb{R}^r$ be positive and independent, and let $\mathcal{E} \subseteq \mathbb{Z}^r$ be a finite set with $\gamma \cdot D > 0$ for each $D \in \mathcal{E}$. Then there is one run $l$, valid for $\gamma$, such that $l(D) \ge 0$ for each $D \in \mathcal{E}$.

Lean: `Singularity.Perron.exists_isValidRun_forall_runExp_nonneg`

*Proof.* We use induction on the number of elements of $\mathcal{E}$. For $\mathcal{E}$ empty the empty run works. Let $\mathcal{E} = \mathcal{E}_0 \cup \{D\}$, and let $l_1$ be a valid run with $l_1(D') \ge 0$ for each $D' \in \mathcal{E}_0$. The weight $\gamma^{l_1}$ is positive and independent, by Lemma 2.3.4, parts 2 and 3. By part 1, $\gamma^{l_1} \cdot l_1(D) = \gamma \cdot D > 0$. Theorem 2.3.5 gives a run $l_2$, valid for $\gamma^{l_1}$, with $l_2(l_1(D)) \ge 0$. Let $l = l_1l_2$. It is valid for $\gamma$ by part 6. We have $l(D) = l_2(l_1(D)) \ge 0$. For $D' \in \mathcal{E}_0$ we have $l(D') = l_2(l_1(D')) \ge 0$ by part 5, because $l_1(D') \ge 0$. $\square$

**Corollary 2.3.7 (divisibility of monomials).** Let $\gamma \in \mathbb{R}^r$ be positive and independent.

1. Let $B, C \in \mathbb{N}^r$ with $\gamma \cdot B < \gamma \cdot C$. Then there is a run $l$, valid for $\gamma$, with $l(B) \le l(C)$.
2. Let $\mathcal{S} \subseteq \mathbb{N}^r$ be finite and not empty, and let $B \in \mathcal{S}$ be the element of least value. Then there is a run $l$, valid for $\gamma$, with $l(B) \le l(C)$ for each $C \in \mathcal{S}$.

Lean: `Singularity.Perron.exists_isValidRun_runExp_le` (part 1), `Singularity.Perron.exists_isValidRun_forall_runExp_le` (part 2)

*Proof.* The element $B$ of part 2 is unique, because distinct exponents have distinct values when $\gamma$ is independent. For part 1, let $D = C - B$. Then $\gamma \cdot D > 0$, and Theorem 2.3.5 gives a valid run $l$ with $l(D) \ge 0$. By Lemma 2.3.4, part 4, $l(C) = l(B) + l(D) \ge l(B)$. For part 2, apply Corollary 2.3.6 to the set of $C - B$ with $C \in \mathcal{S}$ and $C \ne B$, and use part 4 in the same way. $\square$

The Lean statements allow $B$ and $C$ in $\mathbb{Z}^r$, and in part 2 they ask only that $B$ has a value at most the value of each $C \in \mathcal{S}$. In geometric terms, $x^B = x'^{l(B)}$ and $x^C = x'^{l(C)}$ in the coordinates $x'$ after the run, and both exponents lie in $\mathbb{N}^r$ by Lemma 2.3.4, part 5. So $x'^{l(B)}$ divides $x'^{l(C)}$ in the polynomial ring $k[x']$. In part 2, the monomial ideal of $k[x]$ generated by the $x^C$ with $C \in \mathcal{S}$ generates in $k[x']$ the principal ideal $(x'^{l(B)})$. So a monomial ideal becomes principal after a valid run, at the center of $v$ and on the whole new chart. Proposition 2.3.10 below shows that $k[x] \subseteq k[x']$.

### The proof of Theorem 2.3.5

A state is a pair $(\gamma, D)$, with $\gamma$ positive and independent and $c = \gamma \cdot D > 0$. By Lemma 2.3.4, a valid step changes a state into a state with the same value $c$. For a state we use the following notation.

- $P = \{i : D_i > 0\}$ is the set of positive indices, and $N = \{j : D_j < 0\}$ is the set of negative indices.
- $\nu(D) = \sum_j \max(-D_j, 0)$ is a natural number. We have $\nu(D) = 0$ if and only if $D \ge 0$.
- $W = \sum_l \gamma_l$ is the total weight.

The set $P$ is not empty, because $\gamma$ is positive and $\gamma \cdot D > 0$.

A naive measure fails. The sum $\sum_l |D_l|$ does not go down along the rule. Let $D = (5, -1)$ and $\gamma_2 < \gamma_1$. The step $(2, 1)$ is valid, and it gives $D = (5, 4)$, so the sum goes from 6 to 9. Step (b2) of the rule below also makes a positive entry larger. The number $\nu(D)$ does not go up, but the steps (b1) and (b2) do not change it. The total weight $W$ goes down at each step, but by amounts that can become as small as we like. So the proof needs a measure that combines these quantities. It uses the bound $b$ on the entries and a lower bound on the largest positive weight.

The rule. If $N$ is empty, then $D \ge 0$, and we stop. Otherwise we do one of the following steps.

- **(a)** If there are $i \in P$ and $j \in N$ with $\gamma_j < \gamma_i$, do the step $(j, i)$. So $D_j$ becomes $D_j + D_i$, and $\gamma_i$ becomes $\gamma_i - \gamma_j$.
- **(b1)** Otherwise, if there are $i \in P$ and $j \in N$ with $D_i \ge -D_j$, do the step $(i, j)$. So $D_i$ becomes $D_i + D_j \ge 0$, and $\gamma_j$ becomes $\gamma_j - \gamma_i$.
- **(b2)** Otherwise, let $i_0 \in P$ be the index of least weight in $P$, and let $a \in P$ be the index of largest weight in $P$. Do the step $(i_0, a)$. So $D_{i_0}$ becomes $D_{i_0} + D_a$, and $\gamma_a$ becomes $\gamma_a - \gamma_{i_0}$.

The weights are distinct by Lemma 2.3.2, part 6, so $i_0$ and $a$ are unique. When (a) or (b1) applies to several pairs, any choice works. In the examples we take the least $i \in P$, and then the least $j \in N$.

Claim 1 (the rule is well defined). Each step of the rule is valid, and in (b2) we have $i_0 \ne a$. The step of (a) is valid by the hypothesis $\gamma_j < \gamma_i$. If (a) does not apply, then $\gamma_i \le \gamma_j$ for all $i \in P$ and $j \in N$, so $\gamma_i < \gamma_j$ by part 6. So the step of (b1) is valid. In (b2) we have $D_i < -D_j$ for all $i \in P$ and $j \in N$. Assume that $i_0 = a$. Then $P = \{i_0\}$. Choose $j \in N$. The terms of $c$ with an index in $N$ are negative, so
$$c = D_{i_0}\gamma_{i_0} + \sum_{l \in N} D_l\gamma_l \le D_{i_0}\gamma_{i_0} + D_j\gamma_j < 0,$$
because $0 < D_{i_0} < -D_j$ and $0 < \gamma_{i_0} < \gamma_j$. This contradicts $c > 0$. So $i_0 \ne a$, and $\gamma_{i_0} < \gamma_a$ by part 6. So the step of (b2) is valid.

Claim 2 (step (a) lowers $\nu$). Only the entry $j$ of $D$ changes. It goes from $D_j \le -1$ to $D_j + D_i \ge D_j + 1$. So $\max(-(D_j + D_i), 0) \le -D_j - 1$, and $\nu$ goes down by at least 1.

Claim 3 (steps (b1) and (b2) keep $\nu$ and $N$). In (b1) the entry $i$ goes from a positive number to a number $\ge 0$. In (b2) the entry $i_0$ goes from a positive number to a larger positive number. The negative entries do not change. So $N$ and $\nu$ do not change. In (b2) the set $P$ does not change. In (b1) the set $P$ stays the same or loses the index $i$.

The bound $b$. Let $b \ge 1$ be an integer. A state is *$b$-bounded* if $D_l \le b$ for each $l$ and $-2D_j \le b + 2$ for each $j \in N$. Each state is $b$-bounded for $b = 2\sum_l |D_l|$, and this $b$ is at least 2 because $D \ne 0$.

Claim 4 (steps (b1) and (b2) keep the bound). Let the state be $b$-bounded. In (b1) the entry $D_i$ goes down, and no other entry changes. In (b2) choose $j \in N$. Then $D_{i_0} \le -D_j - 1$ and $D_a \le -D_j - 1$, because (b1) does not apply. So the new entry is $D_{i_0} + D_a \le -2D_j - 2 \le b$. The negative entries do not change. So the new state is $b$-bounded.

Claim 5 (the key inequality). In a $b$-bounded state, let $U = \max_{i \in P}\gamma_i$, and let $\delta = c/(br)$. Then $U \ge \delta$. Indeed, $D_i \le b$ for $i \in P$, and $P$ has at most $r$ elements, so
$$brU \ge \sum_{i \in P} D_i\gamma_i = c - \sum_{j \in N} D_j\gamma_j \ge c.$$
Put $\kappa_0 = \delta/2$. It depends only on $b$, $c$ and $r$.

The measure. Fix $\nu_0 \ge 1$, $b$ and $c$. For a $b$-bounded state with $\nu(D) = \nu_0$ and value $c$, let $u = \min_{i \in P}\gamma_i$ and put

- $m_1 = |P|$,
- $m_2 = 1$ if $u > \kappa_0$, and $m_2 = 0$ if $u \le \kappa_0$,
- $\kappa = \min(u, \kappa_0)$ and $m_3 = \lfloor W/\kappa \rfloor$.

The measure of the state is the triple $(m_1, m_2, m_3) \in \mathbb{N}^3$. We order $\mathbb{N}^3$ lexicographically. This order is a well-order.

Claim 6 (the measure goes down). Let the state be $b$-bounded, with $\nu(D) = \nu_0$ and value $c$, and assume that (a) does not apply. Then the step (b1) or (b2) of the rule gives a $b$-bounded state with $\nu = \nu_0$, value $c$ and a smaller measure.

*Proof of Claim 6.* The new state is $b$-bounded with $\nu = \nu_0$ and value $c$, by Claims 3 and 4 and Lemma 2.3.2. We compare the measures. A primed letter denotes the quantity of the new state.

Step (b1), with the pair $(i, j)$, $i \in P$, $j \in N$. If $D_i + D_j = 0$, then $P' = P \setminus \{i\}$, and $m_1$ goes down. Otherwise $P' = P$. Only the weight $\gamma_j$ changes, and $j \notin P$. So the weights of the indices in $P$ do not change, and $u' = u$, $m'_2 = m_2$ and $\kappa' = \kappa$. The total weight goes down by $\gamma_i$, and $\gamma_i \ge u \ge \kappa$. So $W'/\kappa \le W/\kappa - 1$, and $m'_3 \le m_3 - 1$.

Step (b2), with the pair $(i_0, a)$. Here $P' = P$, so $m'_1 = m_1$. Only the weight $\gamma_a = U$ changes, and it becomes $U - u$. So $W' = W - u$. The index $i_0$ keeps the weight $u$, because $i_0 \ne a$.

- Case $u \le \kappa_0$. Then $m_2 = 0$ and $\kappa = u$. By Claim 5, $U \ge 2\kappa_0$, so $U - u \ge 2\kappa_0 - \kappa_0 = \kappa_0 \ge u$. The other weights in $P$ do not change and are $\ge u$. So $u' = u$, $m'_2 = 0$ and $\kappa' = u$. Then $W'/\kappa' = W/u - 1$, and $m'_3 = m_3 - 1$.
- Case $u > \kappa_0$. Then $m_2 = 1$ and $\kappa = \kappa_0$. If $u' \le \kappa_0$, then $m'_2 = 0 < m_2$. Otherwise $m'_2 = 1$ and $\kappa' = \kappa_0$. Then $W' = W - u < W - \kappa_0$, so $W'/\kappa_0 < W/\kappa_0 - 1$, and $m'_3 \le m_3 - 1$.

In each case the measure goes down. $\square$

*Proof of Theorem 2.3.5.* We use two inductions. The outer induction is a strong induction on $\nu(D)$. We prove the theorem for all states $(\gamma, D)$ with $\nu(D) = \nu_0$, and we assume it for all states with $\nu(D) < \nu_0$.

If $\nu_0 = 0$, then $D \ge 0$, and the empty run works. Let $\nu_0 \ge 1$. Let $(\gamma, D)$ be a state with $\nu(D) = \nu_0$ and value $c$. It is $b$-bounded for $b = 2\sum_l |D_l|$. Fix this $b$ and this $c$. The inner induction is a well-founded induction on the measure. It proves the following statement: for each $b$-bounded state $(\gamma', D')$ with $\nu(D') = \nu_0$ and value $c$, there is a run $l$, valid for $\gamma'$, with $l(D') \ge 0$.

Let $(\gamma', D')$ be such a state. Since $\nu_0 \ge 1$, the set $N$ is not empty. If (a) applies, let $s$ be its step. By Claim 1 the step is valid. The state $(\gamma'^s, s(D'))$ is a state by Lemma 2.3.2, parts 1 to 3. By Claim 2, $\nu(s(D')) < \nu_0$. The outer hypothesis gives a run $l_2$, valid for $\gamma'^s$, with $l_2(s(D')) \ge 0$. Then the run $s$ followed by $l_2$ works, by Lemma 2.3.4, part 6. If (a) does not apply, let $s$ be the step (b1) or (b2) of the rule. It is valid by Claim 1. By Claim 6 the new state is $b$-bounded, with $\nu = \nu_0$, value $c$ and a smaller measure. The inner hypothesis gives a run $l_2$ for it, and again $s$ followed by $l_2$ works. This ends the inner induction. Apply it to $(\gamma, D)$ itself. This ends the outer induction. $\square$

The run of the proof is the run of the rule, for each choice of the pairs in (a) and (b1). So the proof shows that the rule ends from each state. The Lean proof follows the two inductions above.

### Examples

**Example 2.3.8 (dimension 2).** Let $r = 2$. For $i \ne j$ only one step is valid, by Lemma 2.3.2, part 6: the step that subtracts the smaller weight from the larger one. So each valid run is an initial part of one sequence, the subtractive algorithm of Euclid on $(\gamma_1, \gamma_2)$. The stratum $V(x_1, x_2)$ is the closed point, so this sequence is the quadratic sequence of the Remark "the quadratic sequence of a monomial valuation is toric" in Section 2.1. The rule never uses (b2) for $r = 2$ (Exercise 2). Take $\gamma = (1, \sqrt{2})$ and $D = (-4, 3)$, the exponent of $y^3/x^4$ in Example 2.1.11, with $x = x_1$ and $y = x_2$. Its value is $3\sqrt{2} - 4 \approx 0.243$.

| step | kind | pair | $\gamma'_1$ | $\gamma'_2$ | $D'$ |
|---|---|---|---|---|---|
| 0 | | | $1$ | $\sqrt{2}$ | $(-4, 3)$ |
| 1 | a | $(1, 2)$ | $1$ | $\sqrt{2} - 1$ | $(-1, 3)$ |
| 2 | b1 | $(2, 1)$ | $2 - \sqrt{2}$ | $\sqrt{2} - 1$ | $(-1, 2)$ |
| 3 | b1 | $(2, 1)$ | $3 - 2\sqrt{2}$ | $\sqrt{2} - 1$ | $(-1, 1)$ |
| 4 | a | $(1, 2)$ | $3 - 2\sqrt{2}$ | $3\sqrt{2} - 4$ | $(0, 1)$ |

The weights are the rows $n = 0$ to $4$ of the table in Section 2.1. After the run, $y^3/x^4$ is the coordinate $y_4$, which is $w_1$ in Example 2.1.11, part 3. So the rule finds the good chart of that example by four quadratic transforms.

**Example 2.3.9 (dimension 3).** Let $r = 3$, $\gamma = (1, \sqrt{2}, \sqrt{3})$ and $D = (3, 3, -4)$. The value is $c = 3 + 3\sqrt{2} - 4\sqrt{3} \approx 0.314 > 0$. The weights are independent, because $1, \sqrt{2}, \sqrt{3}$ are linearly independent over $\mathbb{Q}$. We run the rule and take the least indices when there is a choice. The table gives the kind of each step, its pair, the new weights $\gamma'$, the new exponent $D'$, the number $\nu(D')$ and the value $\gamma' \cdot D'$. We computed it with exact arithmetic.

| step | kind | pair | $\gamma'_1$ | $\gamma'_2$ | $\gamma'_3$ | $D'$ | $\nu$ | $\gamma' \cdot D'$ |
|---|---|---|---|---|---|---|---|---|
| 0 | | | $1$ | $\sqrt{2}$ | $\sqrt{3}$ | $(3, 3, -4)$ | 4 | $c$ |
| 1 | b2 | $(1, 2)$ | $1$ | $\sqrt{2} - 1$ | $\sqrt{3}$ | $(6, 3, -4)$ | 4 | $c$ |
| 2 | b1 | $(1, 3)$ | $1$ | $\sqrt{2} - 1$ | $\sqrt{3} - 1$ | $(2, 3, -4)$ | 4 | $c$ |
| 3 | a | $(3, 1)$ | $2 - \sqrt{3}$ | $\sqrt{2} - 1$ | $\sqrt{3} - 1$ | $(2, 3, -2)$ | 2 | $c$ |
| 4 | b1 | $(1, 3)$ | $2 - \sqrt{3}$ | $\sqrt{2} - 1$ | $2\sqrt{3} - 3$ | $(0, 3, -2)$ | 2 | $c$ |
| 5 | b1 | $(2, 3)$ | $2 - \sqrt{3}$ | $\sqrt{2} - 1$ | $2\sqrt{3} - \sqrt{2} - 2$ | $(0, 1, -2)$ | 2 | $c$ |
| 6 | a | $(3, 2)$ | $2 - \sqrt{3}$ | $1 + 2\sqrt{2} - 2\sqrt{3}$ | $2\sqrt{3} - \sqrt{2} - 2$ | $(0, 1, -1)$ | 1 | $c$ |
| 7 | a | $(3, 2)$ | $2 - \sqrt{3}$ | $3 + 3\sqrt{2} - 4\sqrt{3}$ | $2\sqrt{3} - \sqrt{2} - 2$ | $(0, 1, 0)$ | 0 | $c$ |

The approximate weights after step 7 are $0.268$, $0.314$ and $0.050$. We explain the first steps. In the state of row 0, $P = \{1, 2\}$ and $N = \{3\}$. The weight $\sqrt{3}$ is larger than $1$ and $\sqrt{2}$, so (a) does not apply. We have $D_1 = D_2 = 3 < 4 = -D_3$, so (b1) does not apply. In (b2) the index of least weight in $P$ is $i_0 = 1$ and the index of largest weight is $a = 2$. In the state of row 1, $D_1 = 6 \ge 4$, so (b1) applies to the pair $(1, 3)$. In the state of row 2, $\gamma_3 = \sqrt{3} - 1 \approx 0.732 < 1 = \gamma_1$, so (a) applies with $i = 1$ and $j = 3$. As a check of the last column, row 5 gives $(\sqrt{2} - 1) - 2(2\sqrt{3} - \sqrt{2} - 2) = 3 + 3\sqrt{2} - 4\sqrt{3}$. The run uses all three kinds of steps. The number $\nu$ goes down exactly at the steps (a), as Claims 2 and 3 say. At the end $D' = (0, 1, 0)$, so $x^D$ is the second new coordinate, and its weight is $c$.

The matrix of the run (Proposition 2.3.10) is the product of the seven elementary matrices, the last one on the left:
$$A_l = \begin{pmatrix} 2 & 2 & 3 \\ 1 & 2 & 2 \\ 3 & 5 & 6 \end{pmatrix}, \qquad \det A_l = 1, \qquad A_lD = (0, 1, 0)^T.$$
The new coordinates are $x'_1 = x_1^2/x_3$, $x'_2 = x_1^3x_2^3/x_3^4$ and $x'_3 = x_3^2/(x_1^2x_2)$. Their exponents are the columns of $A_l^{-1}$, and their values are $2 - \sqrt{3}$, $c$ and $2\sqrt{3} - \sqrt{2} - 2$. The old coordinates are monomials in the new ones, with the columns of $A_l$ as exponents. For example $x_1 = x_1'^2x'_2x_3'^3$.

### Blowups of strata of codimension 2

We now connect Theorem 2.3.5 with the lattice lemma in rank 1 (Lemma 2.1.8) and with Theorem 2.1.5. For a step $s = (i, j)$ let $A_s = 1 + E_{ij}$. For a run $l = (s_1, \dots, s_m)$ let $A_l = A_{s_m}\cdots A_{s_1}$, the *matrix of the run*.

**Proposition 2.3.10 (matrix of a run).** Let $\gamma \in \mathbb{R}^r$ and let $l$ be a run.

1. $l(D) = A_lD$ for each $D \in \mathbb{Z}^r$, and $\gamma = A_l^T\gamma^l$.
2. The matrix $A_l$ has entries in $\mathbb{N}$ and determinant 1. So $A_l^{-1}$ is an integer matrix.
3. Let $\gamma$ be positive and independent, and let $\mathcal{E} \subseteq \mathbb{Z}^r$ be a finite set with $\gamma \cdot D \ge 0$ for each $D \in \mathcal{E}$. Then there is a run $l$, valid for $\gamma$, with the following property. The matrices $C = A_l^T$ and $B = C^{-1}$ have the properties of Lemma 2.1.8 for $\gamma$ and $\mathcal{E}$: $BC = CB = 1$, each row $b_k$ of $B$ has $b_k \cdot \gamma > 0$, and $D^TC \in \mathbb{N}^r$ for each $D \in \mathcal{E}$. The matrix $C$ is a product of elementary matrices $1 + E_{ji}$.

Lean: `Singularity.Perron.runMatrix_mulVec` and `Singularity.Perron.sum_runMatrix_mul_runWeight` (part 1), `Singularity.Perron.runMatrix_nonneg` and `Singularity.Perron.det_runMatrix` (part 2), `Singularity.Perron.exists_isValidRun_matrix` and `Singularity.Perron.latticeLemma_real_of_pos_of_perron` (part 3)

*Proof.* Part 1 follows from the matrix form of a step by induction on the length of $l$: if $l = l_0s$, then $l(D) = A_s A_{l_0} D$, and $\gamma = A_{l_0}^T\gamma^{l_0} = A_{l_0}^TA_s^T\gamma^l$. Each $A_s$ has entries in $\mathbb{N}$ and determinant 1, so the product has the same properties. This is part 2. For part 3, an element $D \in \mathcal{E}$ with $\gamma \cdot D = 0$ is 0, because $\gamma$ is independent. Apply Corollary 2.3.6 to the elements of $\mathcal{E}$ that are not 0. It gives a valid run $l$ with $l(D) \ge 0$ for each $D \in \mathcal{E}$. Then $D^TC = (A_lD)^T = l(D)^T \in \mathbb{N}^r$. The row $b_k$ of $B = (A_l^{-1})^T$ is the column $A_l^{-1}e_k$ of $A_l^{-1}$, so by part 1
$$b_k \cdot \gamma = (A_l^{-1}e_k)^TA_l^T\gamma^l = e_k \cdot \gamma^l = \gamma^l_k > 0,$$
by Lemma 2.3.4, part 2. Finally $C = A_{s_1}^T\cdots A_{s_m}^T$, and $A_s^T = 1 + E_{ji}$ for $s = (i, j)$. $\square$

So, for real independent weights, Theorem 2.3.5 gives the matrices of the lattice lemma with one more property. The matrix $C$ is a product of elementary matrices with entries in $\mathbb{N}$, in an order that the valuation chooses. The next corollary states the geometric meaning for the monomial valuation and the polynomial ring localized at the origin.

**Corollary 2.3.11 (monomial charts by blowups).** Let $k$ be a field of any characteristic, and let $v$ be the monomial valuation of $K = k(x_1, \dots, x_r)$ with weights $\gamma_1, \dots, \gamma_r \in \mathbb{R}$, positive and linearly independent over $\mathbb{Z}$. Let $R_0 = k[x_1, \dots, x_r]_{(x_1, \dots, x_r)}$. Let $l = (s_1, \dots, s_m)$ be a run, valid for $\gamma$. For $0 \le n \le m$ let $x^{(n)}$ be the coordinates after the first $n$ steps, defined as in the geometric meaning of Definition 2.3.1, and let $R_n = k[x^{(n)}]_{(x^{(n)})}$.

1. For $1 \le n \le m$, let $s_n = (i, j)$. Then $R_n$ is the local ring at the center of $v$ of the blowup of $\operatorname{Spec} R_{n-1}$ along $V(x^{(n-1)}_i, x^{(n-1)}_j)$, a regular subscheme of codimension 2. The valuation $v$ is the monomial valuation of $K = k(x^{(n)})$ with the weights $\gamma^{(s_1, \dots, s_n)}$.
2. For each finite set $S \subseteq \mathcal{O}_v$ there is a run $l$, valid for $\gamma$, such that $S \subseteq R_m$ for the rings $R_n$ of this run. The ring $R_m$ is the local ring at the origin of a chart $A = k[u_1, \dots, u_r]$ with the properties of Theorem 2.1.5 for $S$, where $u = x^{(m)}$.

Lean: `Singularity.IsMonomialValuation.runCoord` (part 1, the valuation is monomial in the new coordinates), `Singularity.Perron.exists_isValidRun_forall_mem_adjoin_runCoord` (part 2, in terms of the coordinates). The blowups as schemes are not in Lean.

*Proof.* Part 1. Write $y = x^{(n-1)}$ and $y'$ for the coordinates after the step $s_n = (i, j)$, so $y'_j = y_j/y_i$ and $y'_l = y_l$ for $l \ne j$. The Laurent monomials $y'$ form a basis of $M$, because $A_{s_n}$ has determinant 1. As in the proof of Theorem 2.1.5, they are algebraically independent, $K = k(y')$, and $v$ is the monomial valuation of $k(y')$ with the weights $v(y'_l)$. These weights are $\gamma^{(s_1, \dots, s_n)}$, by the geometric meaning of a step, and they are positive by Lemma 2.3.4, part 2. The blowup of $\operatorname{Spec} k[y]$ along $V(y_i, y_j)$ is covered by the charts $\operatorname{Spec} k[y][y_j/y_i] = \operatorname{Spec} k[y']$ and $\operatorname{Spec} k[y][y_i/y_j]$. The second ring is not contained in $\mathcal{O}_v$, because $v(y_i/y_j) < 0$. The first ring is contained in $\mathcal{O}_v$, and the center of $v$ on it is the ideal $(y'_1, \dots, y'_r)$ by Volume 3, Lemma 1.6.1, because all the weights are positive. The blowup of $\operatorname{Spec} R_{n-1}$ along $V(y_i, y_j)$ is the base change of this blowup to $\operatorname{Spec} R_{n-1}$, and the local ring at the center does not change. So the local ring at the center of $v$ is $k[y']_{(y')} = R_n$. The center $V(y_i, y_j)$ is defined by two members of a regular system of parameters of $R_{n-1}$, so it is regular of codimension 2.

Part 2. Follow the proof of Theorem 2.1.5. Write each $s \in S$ as $s = (c/d)\,x^{\alpha - \beta}(1 + F_s)/(1 + G_s)$, where $F_s$ and $G_s$ are sums of terms $c'x^D$ with $\gamma \cdot D > 0$. Let $\mathcal{E}$ be the set of the exponents $\alpha - \beta$ that are not 0, and of the exponents of the Laurent monomials in the $F_s$ and $G_s$. Each $D \in \mathcal{E}$ has $\gamma \cdot D > 0$, because $\gamma \cdot (\alpha - \beta) = v(s) \ge 0$ and $\gamma$ is independent. Corollary 2.3.6 gives a run $l$, valid for $\gamma$, with $l(D) \ge 0$ for each $D \in \mathcal{E}$. Let $u = x^{(m)}$ and $A = k[u]$. Then $x^D = u^{l(D)}$ with $l(D) \in \mathbb{N}^r$, and $l(D) \ne 0$ for $D \ne 0$, because $A_l$ is invertible. So $x^{\alpha - \beta} \in A$, and $F_s, G_s$ lie in the ideal $(u_1, \dots, u_r)$ of $A$. Thus $1 + G_s$ is a unit of $R_m$, and $s \in R_m$. The Laurent monomials $u$ form a basis of $M$ with positive values, by part 1, so $A$ has the properties of Theorem 2.1.5. $\square$

The corollary is about a monomial valuation with real independent weights. It says that the monomial chart of Theorem 2.1.5 can be reached from $R_0$ by blowups of regular centers of codimension 2, each followed by localization at the center of $v$. Each center is a stratum of the coordinate hyperplanes of the chart before it. The corollary does not say more. It does not treat value groups of rank greater than 1. It does not say that a given chart of the lattice lemma is reached in this way. It says nothing about valuations that are not monomial, and nothing about the open case of local uniformization in positive characteristic.

### The monomial form of a polynomial

The last result of the section is about polynomials. A step $s = (i, j)$ gives the substitution $x_j = x_ix_j'$ of the chart that contains the center of $v$. We write it as a homomorphism of the polynomial ring to itself. Let $k$ be a commutative ring, and let $\varphi_s \colon k[x_1, \dots, x_r] \to k[x_1, \dots, x_r]$ be the homomorphism of $k$-algebras with
$$\varphi_s(x_j) = x_ix_j, \qquad \varphi_s(x_l) = x_l \ (l \ne j).$$
For a run $l = (s_1, \dots, s_m)$ let $\varphi_l = \varphi_{s_m} \circ \dots \circ \varphi_{s_1}$. The formula $x^D = x'^{s(D)}$ of the geometric meaning of Definition 2.3.1 says that $\varphi_s(x^D) = x^{s(D)}$ for $D \in \mathbb{N}^r$. By induction on the length of the run,
$$\varphi_l(x^D) = x^{l(D)} \qquad \text{for each } D \in \mathbb{N}^r.$$
In Lean these maps are `Singularity.Perron.stepHom` and `Singularity.Perron.runHom`, and the formula is `Singularity.Perron.runHom_monomial`.

**Corollary 2.3.12 (monomial form of a polynomial).** Let $k$ be a commutative ring, and let $\gamma \in \mathbb{R}^r$ be positive and independent.

1. Let $f \in k[x_1, \dots, x_r]$ with $f \ne 0$, and let $c_Bx^B$ be the term of $f$ of least value $\gamma \cdot B$. Then there is a run $l$, valid for $\gamma$, and a polynomial $g$ such that $\varphi_l(f) = x^{l(B)}g$ and $g(0) = c_B$. In particular $g(0) \ne 0$.
2. Let $f_1, \dots, f_t$ be polynomials that are not 0. Then there is one run $l$, valid for $\gamma$, with exponents $d_1, \dots, d_t \in \mathbb{N}^r$ and polynomials $g_1, \dots, g_t$ such that $\varphi_l(f_a) = x^{d_a}g_a$ and $g_a(0) \ne 0$ for each $a$.
3. For each run $l$ whose steps $(i, j)$ have $i \ne j$, the homomorphism $\varphi_l$ is injective.

Lean: `Singularity.Perron.exists_isValidRun_runHom_eq_monomial_mul_coeff` (part 1), `Singularity.Perron.exists_isValidRun_forall_runHom_eq_monomial_mul` (part 2), `Singularity.Perron.runHom_injective` (part 3)

*Proof.* Part 3. The map $D \mapsto l(D)$ is injective on $\mathbb{Z}^r$, because the matrix $A_l$ has determinant 1 (Proposition 2.3.10). So $\varphi_l$ maps distinct monomials to distinct monomials. Let $f = \sum_C c_Cx^C$. Then $\varphi_l(f) = \sum_C c_Cx^{l(C)}$, and the coefficient of $x^{l(C)}$ in $\varphi_l(f)$ is $c_C$. So $\varphi_l(f) = 0$ gives $f = 0$.

Part 1. Let $\mathcal{S}$ be the set of the exponents $C$ with $c_C \ne 0$. It is finite, and it is not empty. The term of least value is unique, because $\gamma$ is independent. Corollary 2.3.7, part 2, gives a run $l$, valid for $\gamma$, with $l(B) \le l(C)$ for each $C \in \mathcal{S}$. The steps of a valid run have $i \ne j$. Then
$$\varphi_l(f) = \sum_{C \in \mathcal{S}} c_Cx^{l(C)} = x^{l(B)}g \qquad\text{with}\qquad g = \sum_{C \in \mathcal{S}} c_Cx^{l(C) - l(B)}.$$
The exponent $l(C) - l(B)$ is in $\mathbb{N}^r$, and it is 0 only for $C = B$, by the injectivity in part 3. So the constant term of $g$ is $c_B$.

Part 2. Let $B_a$ be the exponent of the term of least value of $f_a$, and let $\mathcal{S}_a$ be the set of the exponents of $f_a$. Apply Corollary 2.3.6 to the finite set of the differences $C - B_a$ with $C \in \mathcal{S}_a$, $C \ne B_a$ and $1 \le a \le t$. Each difference has positive value. So there is one run $l$, valid for $\gamma$, with $l(B_a) \le l(C)$ for each $a$ and each $C \in \mathcal{S}_a$. Now the proof of part 1 applies to each $f_a$ with this run. $\square$

Let $k$ be a field, and let $v$, $R_0$ and $R_m$ be as in Corollary 2.3.11. In the field $K$ we have $f(x) = \varphi_l(f)(u)$, where $u = x^{(m)}$ are the coordinates after the run. So part 1 says that $f = u^{l(B)}g(u)$ in $R_m$, and $g(u)$ is a unit of $R_m$, because $g(0) \ne 0$. The divisor of $f$ is a divisor with normal crossings at the center of $v$ on the last chart, and its components are coordinate hyperplanes. Part 2 gives the same for a finite set of polynomials at the same time. The Lean form holds for a commutative semiring $k$.

This is the model case of log monomialization along a valuation, the subject of Chapter 4. For a monomial valuation with independent weights, each polynomial becomes a monomial times a unit after blowups of strata of codimension 2. The proof needs two facts: a polynomial has only finitely many terms, and these terms have distinct values. For a valuation that is not monomial, the expansion of $f$ in a regular system of parameters can have terms of equal value, and a power series can have infinitely many terms. Then this proof does not apply.

### Remarks

*Remark (the rule uses only comparisons).* The rule compares two weights and compares two integers. It never uses the numerical values of the weights. In geometry, the comparison $\gamma_i < \gamma_j$ asks whether $x_j/x_i$ lies in the maximal ideal of $\mathcal{O}_v$, that is, which chart of the blowup contains the center of $v$. So the rule can be carried out with the valuation ring alone. The measure in the proof uses the numerical values, but only in the proof.

*Remark (the largest entry).* Let $D_i$ and $D_j$ have opposite signs. Then $|D_i + D_j| \le \max(|D_i|, |D_j|)$. So a step between two entries of opposite signs does not make $\max_l |D_l|$ larger. The steps (a) and (b1) of the rule are of this kind. The steps (b2) are the only steps of the rule between two entries of the same sign, and they can make $\max_l |D_l|$ larger, as in step 1 of Example 2.3.9.

*Remark (an open question).* Consider any sequence of valid steps, each between two entries of opposite signs. As long as $N$ is not empty, such a step exists, by Lemma 2.3.2, part 6. The entries stay bounded by $\max_l |D_l|$, by the previous remark. We do not know whether each such sequence reaches $D \ge 0$. The exponents take only finitely many values, but the weights do not, and the bound alone does not exclude an infinite sequence. For $r = 2$ the answer is yes, because then the only valid step is the step of the rule (Example 2.3.8). We tested the question by computer for the formalization. In 10 000 random cases with $r \le 5$, a random choice of such steps reached $D \ge 0$ in at most 31 steps. We also tested the rule itself, in 2 000 and in 10 000 random cases. The tests had $r$ from 2 to 5, weights of the form $q_0 + q_1\sqrt{2} + q_2\sqrt{3} + q_3\sqrt{5}$ with rational $q_i$, and entries of $D$ between $-6$ and $6$. The rule ended in all cases. This is evidence, not a proof.

*Remark (factorization).* The lattice lemma gives a chart $k[u]$ and a monomial birational map to $k[x]$. Apply Corollary 2.3.6 to the exponents of $u_1, \dots, u_r$. It gives a chart $k[x']$ with $k[u] \subseteq k[x']$, and $k[x']$ is reached from $k[x]$ by blowups alone. The question whether two such charts are related by blowups alone, or only by blowups and blowdowns, is a local form of the strong and the weak factorization problems. Weak factorization of birational maps is proved in characteristic 0 in [AKMW02], which also explains the status of the strong factorization conjecture of Oda. The local form of strong factorization for toric maps is the subject of [Kar03]. For toric geometry and blowups of torus invariant centers see [Ful93]. We do not use these results.

*Remark (the role of independence).* The hypothesis that $\gamma$ is independent is used in Lemma 2.3.2, parts 3 and 6. It makes two weights distinct, so exactly one of the two steps on a pair is valid, and $i_0$ and $a$ in (b2) are unique. It also gives $D = 0$ from $\gamma \cdot D = 0$. Without it, two weights can become equal. If $\gamma_i = \gamma_j$, then $v(x_j/x_i) = 0$. For the monomial valuation of Volume 3, Lemma 1.6.1, with such weights, the residue of $x_j/x_i$ is transcendental over $k$. Then the center of $v$ on the blowup of $V(x_i, x_j)$ is not a closed point. It is not the origin of either chart, and the method stops. The Remark "why the weights must be independent" in Section 2.1 treats the case of the order valuation.

*Remark (the characteristic).* No step of this section uses the characteristic of $k$. The theorem and its corollaries are statements on $\mathbb{Z}^r$ and $\mathbb{R}^r$, and the blowups of Corollary 2.3.11 are monomial. So they hold over a field of each characteristic.

### Exercises

1. Let $\gamma = (1, \sqrt{2})$ and $D = (5, -3)$. Check that $\gamma \cdot D > 0$, run the rule, and give the table of the run as in Example 2.3.8. Check that the rule stops after 3 steps.
2. Let $r = 2$. Show that the rule never uses (b2): if $P = \{1\}$, $N = \{2\}$ and $\gamma_1 < \gamma_2$, then $D_1\gamma_1 > -D_2\gamma_2 > -D_2\gamma_1$, so $D_1 > -D_2$. Deduce that each step except the last lowers $|D_1| + |D_2|$ by at least 1, and that the rule stops after at most $|D_1| + |D_2| - 1$ steps.
3. Let $s$ be a step. Show that $\gamma$ is independent if and only if $\gamma^s$ is independent. Use $\gamma = A_s^T\gamma^s$ for one direction. Show by an example with $r = 2$ that a step can change a positive weight into a weight that is not positive when the step is not valid.
4. Let $\gamma = (1, \sqrt{2})$ and $D = (-41, 29)$. Show that each valid run is an initial part of the sequence of the table in Section 2.1, and that the shortest valid run with $l(D) \ge 0$ has 9 steps. Hint: the cones $\{D : l(D) \ge 0\}$ grow along the sequence (Exercise 7). Show that the number of steps needed is not bounded in terms of $r$ and $\gamma$ alone. Hint: if $l(D) \ge 0$ and $D \ne 0$, then $\gamma \cdot D$ is at least the least entry of $\gamma^l$.
5. Let $\gamma$ be positive and independent, let $l_0$ be a run valid for $\gamma$, and let $\mathcal{E}$ be as in Corollary 2.3.6. Show that the run of Corollary 2.3.6 can be chosen of the form $l_0l_1$.
6. Show that the matrix $A_l$ of each run has determinant 1 and entries in $\mathbb{N}$, and that $A_l \ne 1$ if $l$ is not empty. Show that the exponents of the new coordinates $x'_k$ in terms of the old ones are the columns of $A_l^{-1}$. Compute $A_l^{-1}$ for the run of Example 2.3.9.
7. Let $\gamma$ be positive and independent. For a run $l$ valid for $\gamma$, let $\sigma_l = \{D \in \mathbb{Z}^r : l(D) \ge 0\}$. Show that $\sigma_l \subseteq \sigma_{ll'}$ for each run $l'$ that is valid for $\gamma^l$. Show that the union of the $\sigma_l$, over all valid runs $l$, is the set of $D$ with $\gamma \cdot D > 0$, together with $0$.

### Notes and references

The algorithm of Jacobi for the continued fraction of several numbers was developed by O. Perron, Grundlagen für eine Theorie des Jacobischen Kettenbruchalgorithmus, Math. Ann. 64 (1907). It is now called the algorithm of Jacobi-Perron. Zariski used an algorithm of this type in his proof of local uniformization in characteristic 0 [Zar40]. We do not follow his rule, and we have not compared the two rules in detail. Monomial transforms of the same kind appear in the work of Cutkosky on local monomialization [Cut99]. The rule (a), (b1), (b2) and the measure $(m_1, m_2, m_3)$ were written for this handbook and for the Lean library. We do not claim that the statement of Theorem 2.3.5 is new. The Lean library proves Lemma 2.3.2, Lemma 2.3.4, Theorem 2.3.5, Corollary 2.3.6, Corollary 2.3.7, Proposition 2.3.10 and Corollary 2.3.12, in the namespace `Singularity.Perron`. For Corollary 2.3.11 the library proves the statements on the coordinates and on the valuation. The statement that each step is the blowup of a regular center of a scheme is not in the library. The weak and the strong factorization problems are discussed in [AKMW02] and [Kar03], and the toric background is in [Ful93].
