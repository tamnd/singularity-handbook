---
title: Origin runs in all dimensions
nodes: []
sources: [CJS20]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Origin runs in all dimensions

This section reports the sixteenth research result of the milestone S7, from the milestone S7.18. It treats the runs of point blowups where each step is at the origin of a chart, in each dimension. A run of this type that uses all the charts an infinite number of times reaches $\rho = 0$. A run that uses $k$ charts an infinite number of times, with $2 \le k \le n - 1$, has $k$ corner curves along which the order of $G$ is at least $\rho$. So Volume 7, Question 3.13.18 has a positive answer for each such run, in each dimension $n \ge 3$. An example in four variables shows that three charts can occur for ever and that the surfaces do not work there. Volume 7, Section 3.14, gives the same result with all the details.

### The problem

Volume 7, Theorem 3.13.20 proves Question 3.13.18 for $n = 3$ and the runs where each step is at the origin of the $y$-chart or of the $z$-chart. The question of this section is what happens when the run uses all three charts, and what happens for $n \ge 4$. The proof of Theorem 3.13.20 uses the angle between two columns of exponents and a primitive vector on a ray. For three or more charts these arguments do not exclude a limit in a rational plane, so a new tool is necessary.

### The result

We use the setting of Volume 7, Sections 3.13 and 3.14. An *origin run* is a sequence of point blowups where each step is at the origin of the $x_j$-chart, in the coordinates of the start, and $j$ is the *letter* of the step. By Volume 7, Lemma 3.14.1, an origin step needs no cleaning, and it sends the exponent vector $e$ to the vector with $e_j$ replaced by $|e| - p$. A *window* is a stretch of consecutive steps.

**Lemma 3.16.1.** Let $\delta \in \mathbb{Z}^k$, and let $\Phi(\delta)$ be the smaller of the sum of the positive entries and the sum of the absolute values of the negative entries. A step with the letter $j$ replaces $\delta_j$ by the sum of the entries. Then $\Phi$ does not go up, a vector $\delta \ge 0$ or $\delta \le 0$ stays so, and if $\delta$ has a negative entry and a positive entry after $w$ disjoint windows, each with all $k$ letters, then $w \le \Phi(\delta_0) - 1$.

**Theorem 3.16.2.** Let $P_N, P_{N+1}, \dots$ be an origin run in $n \ge 2$ variables, and let $P_M$ be a point such that each letter occurs among the steps from $P_N$ to $P_M$. Let $W$ be the largest value of $\Phi(e - f) - 1$ for two minimal exponent vectors $e, f$ of $g_M$ with $e - f$ not $\ge 0$ and not $\le 0$, or $0$ if there is no such pair. If $G$ is a unit at a point after $P_M$, then $\rho = 0$ there and at each later point. After $W + 1$ disjoint windows with all $n$ letters, $\rho = 0$. So an origin run with $\rho \ge 1$ at each point does not use all $n$ letters an infinite number of times.

**Theorem 3.16.3.** Let $P_N, P_{N+1}, \dots$ be an origin run, and let $L$ be a set of $k$ letters with $2 \le k \le n - 1$. Assume that each step has a letter in $L$, that each letter of $L$ occurs an infinite number of times, and that $L \subseteq \Delta_N$, and let $U$ be the other coordinates. Then the cones of the exponent columns shrink to one ray $\omega$ with positive and rationally independent entries. For $m$ large, the initial form of $G_m$ is a nonzero form $h$ in the variables of $U$ of a degree $d_m \in \{\rho, \rho + 1\}$, and for each $t \in L$ the corner curve $C_t$, which is the $x_t$-axis, lies in a component of the divisor and has $\nu^G_{C_t} = d_m \ge \rho$. If $U$ has one element $u$ and $\rho = d_m - 1$, then the forms of degree $\rho$ of $\widetilde\Theta(G_m)$ are the multiples of $x_u^\rho$. The coordinate strata between the curves and $V(x_U)$ have an explicit order of $G$, and it is less than $d_m$ unless the monomials of the least value have one value of the degree in $x_U$.

**Corollary 3.16.4.** Let $n \ge 3$, and let an infinite origin run have $\rho \ge 1$ at each point and an infinite number of corner steps. Then the set $L$ of the letters that occur an infinite number of times has $2 \le |L| \le n - 1$, and for $m$ large there are $|L|$ regular coordinate curves at $P_m$ in components of the divisor with $\nu^G = d_m \ge \rho$. So Volume 7, Question 3.13.18 has a positive answer for each origin run. For $n = 3$ this is Volume 7, Theorem 3.13.20.

**Example 3.16.5.** Let $n = 4$, $\Delta = \{1, 2, 3\}$ and $g = x_1 x_4^p + x_1^2 x_2 x_3 x_4^{p-2}$. Each word in the letters $1, 2, 3$ is an origin run with $\rho = d = p$ at each point and $G_m = x_4^p + x_1 x_2 x_3 x_4^{p-2}$. The three corner curves have $\nu^G = p$, the surfaces $V(x_4, x_s)$ have $\nu^G = p - 1$, $V(x_4)$ has $\nu^G = p - 2$, and no regular formal subvariety of dimension $2$ or $3$ has $\nu^G \ge \rho$.

### The proof in short

For Lemma 3.16.1, if the sum $S$ of the entries is positive, then $\Phi$ is the sum $Q$ of the absolute values of the negative entries. A step at a negative entry makes $Q$ smaller, and a step at another entry keeps it. In a window where $\Phi$ does not change, no step is at an entry that is negative at the start, so a window with all the letters makes $\Phi$ smaller. The case $S \le 0$ is the same.

For Theorem 3.16.2, the step map is injective and keeps the componentwise order of the exponent vectors. So the minimal vectors at a later point are images of minimal vectors of $g_M$, which are a finite set by Dickson's lemma. When the divisor has all the coordinates, $G$ is a unit exactly when there is one minimal vector, and two minimal vectors are incomparable exactly when their difference has a negative entry and a positive entry. Lemma 3.16.1 bounds the number of windows for each such pair.

For Theorem 3.16.3, the exponent of $x_s$ at $P_m$ is a linear function of the exponent columns $c_s$, after a shift. Lemma 3.16.1 applied to the vectors with the entries $\delta \cdot c_s$ shows that no nonzero integer vector is orthogonal to a vector of the limit cone, so the cone is one ray. The monomials of $g$ with the least value along the ray and the largest degree in $x_U$ give the initial form $h$ and the order of $G$ along the corner curves, once the columns are long enough. The proof uses Dickson's lemma in place of the box argument of Volume 7, Lemma 3.13.19. Corollary 3.16.4 follows from Theorems 3.16.2 and 3.16.3, since a run has an infinite number of corner steps exactly when at least two letters occur an infinite number of times.

For Example 3.16.5, the difference of the two exponent vectors is $(1, 1, 1, -2)$, with the sum $1$, so no step with a letter in $\{1, 2, 3\}$ changes it, and $G_m$ is the same at each point. By Volume 7, Lemma 3.13.14, a subvariety with $\nu^G \ge \rho$ has $J$ in the power $p - 1$ of its ideal. For $p \ge 3$ this puts $x_4$ and two of $x_1, x_2, x_3$ in its ideal, so it is a curve. For $p = 2$ a direct check gives the same conclusion.

### The test data

1. Lemma 3.16.1. An exhaustive test on all vectors in a box found no failure in $882$, $6591$ and $9604$ transitions for $k = 2, 3, 4$. A full search of the words to the depth $10$ for $k = 3$ and $9$ for $k = 4$ found no violation of the bound on the windows, and the bound is reached for $\Phi(\delta_0) = 1, 2, 3$.
2. The formula for the exponents agrees with the charts in $60079$ random cases.
3. Theorem 3.16.2. A full search of the words found no violation of the bound for $n = 3$ to the depth $9$ and for $n = 4$ to the depths $7$ and $6$. A search of all origin branches that keep $\rho$ for $n = 3$ to the depth $14$, with $3754057$, $3318393$ and $2271974$ nodes for $p = 2, 3, 5$, found no branch that uses all three letters after $P_M$. The same holds for $n = 4$ to the depth $10$ with all four letters.
4. Theorem 3.16.3. In $14530$ random runs for $(n, k) = (3, 2)$, $(4, 2)$, $(4, 3)$, $(5, 3)$ and $(5, 4)$ and $p = 2, 3, 5$, all claims held, also in $3003$ runs built with a spread of the degree in $x_U$ on the monomials of the least value. Random runs rarely show the failure of the surfaces: for $(n, k) = (4, 3)$ it occurred in $3$ of $858$ cases for $p = 2$ and in no case for $p = 3, 5$.
5. Example 3.16.5. For $p = 2, 3, 5, 7$, all $3280$ words of the length at most $7$ and $300$ random words of the length $300$, with $114904$ points for each $p$, gave no failure.

### What the result means

For origin runs the corrected question of Section 3.15 is answered in each dimension, and the answer is curves. In three variables the case of three charts is empty when $\rho \ge 1$. In four variables three charts can occur for ever, and then the corner surfaces can fail, as Example 3.16.5 shows, while the corner curves always work. The analogue of the irrational slope of Volume 7, Theorem 3.13.20 is a monomial valuation of real rank $1$ and rational rank $k$, and the run is the sequence of its centers (Volume 7, Remark 3.14.10). The open cases are the runs with translations, in particular for $n = 4$ and $k = 2$, where the initial form is a binary form, the runs that leave a component of the divisor an infinite number of times, the directrix when $U$ has two or more elements, and a bound on the windows that does not depend on the coordinates. The corner curves need not resolve the point, by Volume 7, Example 3.13.21.

### Status

The map has the node SG0000005X for Lemma 3.16.1, SG0000005Y for Theorem 3.16.2, SG0000005Z for Theorem 3.16.3, SG00000060 for Corollary 3.16.4 and SG00000061 for Example 3.16.5. All of them have proofs in the text of Volume 7, Section 3.14, and none of them has a Lean proof yet. Volume 7, Section 3.13 now has the corrected formula for the exponents before Lemma 3.13.19. The old formula gave the exponents in the total transform and not in the strict transform. The correction does not change Theorem 3.13.20 or its proof, except that the line on the vector $r$ is now right. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The results of this section are from notes 31 and 32 of the research notes, with the corrections of the second note, and they are a result of the milestone S7.18 of this project (tamnd/singularity#245). The use of the history of the divisor is from [CJS20].
