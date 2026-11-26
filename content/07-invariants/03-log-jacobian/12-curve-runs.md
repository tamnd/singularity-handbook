---
title: Runs along a curve
nodes: []
sources: [Hir64, CJS20, Nar83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs along a curve

Example 3.11.6 shows that the triple $(\rho, d, \tau_\rho)$ can get worse along a kangaroo path, and that the full form $\widetilde\tau$ does not repair it. So the data at the point do not give an invariant that does not get worse at each step where $\rho$ stays. In this section we ask a weaker question, and it is the question that a resolution needs: does each run of point blowups where $\rho$ stays end? An invariant that gets worse at some steps can still give a resolution if each such run ends. We give an example of a run that does not end. The run follows a curve along which the order is $\rho$, so the example is not a defect of the invariant: a point blowup does not separate the curve from the locus where the order is $\rho$. We state the hypothesis that each run that does not end is of this kind, and we report the first computer tests.

We use the setting and the notation of Sections 3.8 to 3.11. So $K$ is an algebraically closed field of characteristic $p$, $g = x^r G$ is clean for the divisor $\Delta$, $d = \operatorname{ord} G$ and $\rho = \rho(g)$. The first case is $d = \rho$, and the second case is $d = \rho + 1$. We write a point as the pair $(\Delta, g)$.

### The question

The kangaroo path of Example 3.11.6 also shows that an invariant needs more data than the data of the point. A natural candidate is the history of the components of the divisor, as in [CJS20]. Give each component of $\Delta$ an age: the components at the start of a run are old, and the exceptional divisor of each step is new. A random test of the milestone S7.17 recorded the component that leaves at each step where the triple gets worse. This component can be a component of the first divisor, or an exceptional component made before or after the last step where the triple got strictly better. So the rule "only an old component can leave at a step where the triple gets worse" is false, and a count of the old components through the point does not pay for these steps.

**Definition 3.12.1.** A *run* is a finite or infinite sequence of points $P_0, P_1, P_2, \dots$ where each $P_{i+1}$ is a point of a chart of the blowup of $P_i$ at the origin, after the cleaning, with $\rho(P_{i+1}) = \rho(P_i)$. The *tree* of a point $P_0$ is the set of the runs that start at $P_0$. The runs of $P_0$ *end* if each run in the tree of $P_0$ is finite.

The charts are the charts of Section 3.2, with all the translations. In Lean, one step of a run is `Singularity.RhoStep`. By Theorem 3.2.4, $\rho$ does not go up at a point blowup, so at each point of the blowup of $P_i$ that is not the next point of a run, $\rho$ goes down. The question of this section is:

> Do the runs of each point end? That is, is each run finite?

If the answer is yes, then along each sequence of point blowups at the points where $\rho$ stays, $\rho$ goes down after a finite number of steps, and an invariant that gets worse at some steps of a run is not a problem. The next example shows that the answer is no.

### A run that does not end

**Example 3.12.2.** Let $p = 2$, $n = 3$ with the variables $x, y, z$, $\Delta = \{y\}$, and for $k \ge 0$ let
$$g_k = y^{2k+1} (x^4 + x^2 y^k z^3) = x^4 y^{2k+1} + x^2 y^{3k+1} z^3.$$
Let $P_k$ be the point $(\{y\}, g_k)$, and let $C = V(x, z)$ be the $y$-axis. Then:

1. $g_k$ is clean, and $P_k$ is in the first case with $(\rho, d, \tau_\rho) = (4, 4, 1)$.
2. The origin of the $y$-chart of the blowup of $P_k$ is the point $P_{k+1}$, and it is the point of the strict transform of $C$ over the origin.
3. The ideal $\widetilde\Theta(G_k)$ is contained in $I_C^4$, where $I_C = (x, z)$, and $\rho = 4$ at each point of $C$.

So $P_0, P_1, P_2, \dots$ is an infinite run, and the runs of $P_0$ do not end.

*Proof.* Part 1. The monomial $x^4 y^{2k+1}$ has an odd exponent of $y$, and the monomial $x^2 y^{3k+1} z^3$ has an odd exponent of $z$. So no monomial of $g_k$ is a square, and $g_k$ is clean. The largest power of $y$ that divides $g_k$ is $y^{2k+1}$, since $2k + 1 \le 3k + 1$. So $r = (0, 2k+1, 0)$ and
$$G_k = x^4 + x^2 y^k z^3.$$
The term $x^4$ is not divisible by $y$, and $d = \operatorname{ord} G_k = 4$. Also $\operatorname{ord} g_k \ge 5 \ge p$. The generators of $\widetilde\Theta(G_k)$ are $e_y = (2k + 1) G_k + y \partial_y G_k$ and the free derivatives $\partial_x G_k$ and $\partial_z G_k$. In characteristic $2$ we have $2k + 1 = 1$ and $y \partial_y (x^2 y^k z^3) = k x^2 y^k z^3$, so
$$e_y = x^4 + (k + 1) x^2 y^k z^3, \qquad \partial_x G_k = 4 x^3 + 2 x y^k z^3 = 0, \qquad \partial_z G_k = 3 x^2 y^k z^2 = x^2 y^k z^2.$$
The element $e_y$ has order $4$, and $\partial_z G_k$ has order $4 + k \ge 4$. So $\rho = 4 = d$, and $P_k$ is in the first case. By Lemma 3.11.4, $T_\rho(P_k) = T(E_y F)$, where $F = x^4$ is the part of degree $4$ of $G_k$ and $E_y F = (2k + 1) x^4 + y \partial_y x^4 = x^4$. For a vector $b$, in $K[x, y, z, s]$ we have $(x + s b_x)^4 = x^4 + s^4 b_x^4$, so $T(x^4) = \{a_x = 0\}$ and $\tau_\rho(P_k) = 1$.

Part 2. The $y$-chart at the origin is $\pi(x) = y x$, $\pi(y) = y$, $\pi(z) = y z$. The new divisor is $\{y\}$, since the chart variable is $y$ and $\Delta$ has no other component. We have
$$\pi(g_k) = y^4 x^4 \cdot y^{2k+1} + y^2 x^2 \cdot y^{3k+1} \cdot y^3 z^3 = x^4 y^{2k+5} + x^2 y^{3k+6} z^3.$$
We divide by $y^2$ and we get $x^4 y^{2(k+1)+1} + x^2 y^{3(k+1)+1} z^3 = g_{k+1}$. By part 1 this is clean, so no cleaning is necessary, and the new point is $P_{k+1}$. By part 1 for $k + 1$, $\rho(P_{k+1}) = 4 = \rho(P_k)$, so the step is a step of a run. The chart vector is $v = (0, 1, 0)$, and it is in $T_\rho(P_k) = \{a_x = 0\}$, as Theorem 3.7.1 requires. The inverse image of $C$ in the chart is given by $y x = y z = 0$. Away from the exceptional divisor $y = 0$ it is the set $x = z = 0$, so the strict transform of $C$ is the $y$-axis $V(x, z)$ of the chart. It meets the exceptional divisor only at the origin, that is, at $P_{k+1}$.

Part 3. The element $e_y = x^4 + (k + 1) x^2 y^k z^3$ is in $(x, z)^4$, and $\partial_z G_k = x^2 y^k z^2$ is in $(x, z)^4$. So $\widetilde\Theta(G_k) \subseteq I_C^4$, and $e_y \notin I_C^5$, so the order of $\widetilde\Theta(G_k)$ along $C$ is $4 = \rho$. Now let $Q = (0, c, 0)$ with $c \ne 0$ be a point of $C$. The component $y = 0$ does not pass through $Q$, so at $Q$ the divisor is empty, and the log-Jacobian ideal at $Q$ is $(\partial_x g_k, \partial_y g_k, \partial_z g_k)$ in the coordinates $x, y - c, z$. The clean part of $g_k$ at $Q$ differs from $g_k$ by a square, so by Lemma 3.1.2 it has the same ideal. With the empty divisor, $r = 0$ at $Q$, so $\rho(Q)$ is the order of this ideal at $Q$. We have $\partial_x g_k = 0$,
$$\partial_y g_k = y^{2k} \bigl( x^4 + (3k + 1) x^2 y^k z^3 \bigr), \qquad \partial_z g_k = y^{3k+1} x^2 z^2,$$
and $y$ is a unit at $Q$. Both elements are in $(x, z)^4$, and $\partial_y g_k$ has the term $c^{2k} x^4$ of degree $4$. So $\rho(Q) = 4$. At the origin, $\rho = 4$ by part 1.

By part 2, $P_{k+1}$ is a point of the blowup of $P_k$ with the same $\rho$, for each $k \ge 0$. So the sequence $P_0, P_1, P_2, \dots$ is an infinite run. $\square$

Along the run the triple $(\rho, d, \tau_\rho)$ is $(4, 4, 1)$ at each point, no component leaves, and $|r| + d = 2k + 5$ is odd. So the run agrees with Theorem 3.10.3, and none of the bad steps of Sections 3.9 to 3.11 occurs. The full form goes $\widetilde\tau(P_0) = 2$ and $\widetilde\tau(P_k) = 1$ for $k \ge 1$, since the form $x^2 z^2$ of $\partial_z G_0$ has degree $4$ at $P_0$, and the form $x^2 y^k z^2$ of $\partial_z G_k$ has degree $4 + k$ at $P_k$. The only thing that changes along the run is the exponent $2k + 1$ of $y$ and the degree $5 + k$ of the second monomial of $G_k$. Neither of them goes down. A monomial $x^a y^b z^c$ of $g$ goes to $x^a y^{a + b + c - 2} z^c$ in the $y$-chart at the origin, so the exponent of $y$ in $G$ goes up by $a + c - d$. For the monomial $x^4$ of degree $d$ this is $0$, and the monomial $x^4$ stays at each step.

**Why this is not a defect of the invariant.** By part 3, the locus where $\rho$ is $4$ contains the curve $C$ through $P_k$, and by part 2 the blowup of $P_k$ maps the strict transform of $C$ isomorphically to $C$. So after each point blowup, the locus where $\rho = 4$ contains a curve through the new point, as before. A point blowup at a point of a curve in this locus does not separate the curve from the locus, in each characteristic. No invariant with values in a well ordered set can go down at each step of this run. So a resolution must blow up the curve $C$, or a center that contains it, and not only points.

The curve is a good center. Here $g_0 = x^4 y + x^2 y z^3$ is in $I_C^2 = I_C^p$, and by part 3 the ideal $\widetilde\Theta(G_0)$ has the order $\rho$ along $C$, which is condition (H1) of Section 3.4. The ideal $\widetilde\Theta_C(G_0)$ contains $e_y$, of order $4$ at the origin, which is condition (H2). So Theorem 3.4.5 applies to the blowup of $C$. In fact $\rho$ goes down at each point over the origin. In the $x$-chart $\pi(x) = x$, $\pi(z) = x (z + t)$, $\pi(y) = y$, the transform is $g' = x^2 y + x^3 y (z + t)^3$ with the divisor $\{x, y\}$. It is clean, since the exponent of $y$ is $1$ in each monomial, and $G' = 1 + x (z + t)^3$ is a unit, so $d' = 0$ and $\rho' = 0$. In the $z$-chart at the origin, $\pi(x) = z x$, $\pi(z) = z$, $\pi(y) = y$, the transform is $g' = x^4 y z^2 + x^2 y z^3$ with the divisor $\{y, z\}$. It is clean, $r' = (0, 1, 2)$ and $G' = x^4 + x^2 z$. The generators of $\widetilde\Theta(G')$ are $e_y = G'$, $e_z = 2 G' + z \partial_z G' = x^2 z$ and $\partial_x G' = 0$, so $\rho' = 3 < 4$.

**Remark 3.12.3.** The same mechanism gives a run of length one that repeats, for each $p$. Let $n = 2$ with the variables $x, y$, $\Delta = \{y\}$ and $g = x^p y$. The exponent of $y$ is $1$, so $g$ is clean. Here $r = (0, 1)$, $G = x^p$ and $d = p$. The generators of $\widetilde\Theta(G)$ are $e_y = G + y \partial_y G = x^p$ and $\partial_x G = p x^{p-1} = 0$, so $\rho = p = d$. In the $y$-chart at the origin, $\pi(g) = y^p x^p \cdot y = x^p y^{p+1}$, and $y^{-p} \pi(g) = x^p y = g$, with the divisor $\{y\}$. So the blowup of the origin gives the same point again, and the run $g, g, g, \dots$ does not end. Here $\widetilde\Theta(G) = (x^p)$ is the $p$-th power of the ideal of the curve $x = 0$. Example 3.12.2 is of more interest because $G_k$ changes at each step, and the run is not a cycle of points.

### The hypothesis

Example 3.12.2 shows that the question "does each run end" has the answer no for a reason that each resolution must handle. The right question is whether each run that does not end is of this kind. Let $\gamma$ be a formal curve through $P_0$, that is, a regular formal curve given by a prime ideal $I_\gamma$ of $K[[x]]$ with $K[[x]] / I_\gamma \cong K[[s]]$. We say that a run $P_0, P_1, \dots$ *follows* $\gamma$ if, for each $i$, the point $P_{i+1}$ is the point of the strict transform of $\gamma_i$ over $P_i$, where $\gamma_0 = \gamma$ and $\gamma_{i+1}$ is the strict transform of $\gamma_i$.

**Hypothesis 3.12.4 (H4).** Let $P_0, P_1, P_2, \dots$ be an infinite run. Then the run follows a formal curve $\gamma$ through $P_0$, and the order of $\widetilde\Theta(G)$ along $\gamma$ is $\rho$, that is, $\widetilde\Theta(G) \subseteq I_\gamma^\rho$ at $P_0$.

This is an open question. We do not know a proof or a counterexample. Example 3.12.2 and Remark 3.12.3 are infinite runs that satisfy the conclusion, with $\gamma = C$.

**What H4 gives.** Assume that H4 holds. If $\widetilde\Theta(G) \subseteq I_\gamma^\rho$ at $P_0$, then each point of $\gamma$ is in the locus where the order of $\widetilde\Theta(G)$ is at least $\rho$, The locus is closed, so a formal curve in it through $P_0$ shows that the locus has dimension at least one at $P_0$, and $P_0$ is not an isolated point of the locus. So two things follow.

1. A run that starts at an isolated point of the locus where the order of $\widetilde\Theta(G)$ is at least $\rho$ is finite. For such a run the point blowups are sufficient, and the invariant can get worse at some steps without harm.
2. A run that does not end gives a formal curve $\gamma$ of the locus. If $\gamma$ is algebraic and it is a permissible center, then its blowup is a step of a different type, and Theorem 3.4.5 controls $\rho$ at this step under the conditions (H1) and (H2). So the infinite runs reduce to a center of dimension one.

This is the shape of the classical argument for surfaces: blow up the isolated points of the locus of maximal order, and the curves of the locus when the point blowups do not separate them.

**Characteristic zero.** In characteristic $0$ the analogue of H4 for the order of an ideal comes from a hypersurface of maximal contact (Volume 2, Theorem 2.3.3). The points where the order stays lie on the strict transforms of this hypersurface, so an infinite sequence of such points is a sequence on a space of dimension one less, and the induction on the dimension reduces the question to a curve. In characteristic $p$ a hypersurface of maximal contact need not exist, also not in the formal neighbourhood of the point [Nar83] (Volume 2, Section 2.4). So in characteristic $p$, H4 does not follow from this argument, and it is the point to test.

### The computer tests

A test explored the full tree of a point to a depth limit: all the charts, all the translations over $\mathbb{F}_p$, and the cleaning at each step. The runs had $(p, n) = (2, 3)$, and they started at points of the first case with $p \mid |r| + d$ and $\tau_\rho \ge 2$. The script `inv38` used the depth limit $10$ on $600$ starts. At $446$ starts all the branches ended, $153$ starts reached the depth limit, and $1$ start reached the time limit. The script `inv38b` used the depth limit $12$ on $800$ starts, with the results $621$, $178$ and $1$. The maximal depth of a start where all the branches end was $11$, at a start with $(\rho, d, \tau_\rho) = (4, 4, 2)$. All the starts with $\tau_\rho = 3$ ended at depth $0$. The script `inv38b` also extended each deep branch along the same chart at the origin for $40$ more steps. Of the deep nodes, $238$ were axis tails, that is, the last four steps or more were in the same chart at the origin. For $236$ of them, $\rho$ stayed for the $40$ extra steps, and for $2$ of them $\rho$ went from $4$ to $2$. Only $40$ deep nodes were not axis tails. A chain of the test shows the mechanism of Example 3.12.2: at each step $G$ contains the term $x^4$ and $\Delta = \{y\}$, so the order is $4$ along the curve $x = z = 0$, and the chart at the origin is the point of the strict transform of this curve. The tests of H4 are in progress. The planned tests compute the formal curve that the centers of each deep branch follow, as the limit of the translations, and check whether the order is $\rho$ along it. They also repeat the tree test with the rule that each center is an isolated point of the locus where the order is $\rho$.

### Notes and references

The use of the history of the components of the divisor is from [CJS20]. Maximal contact is from [Hir64], and the example of Narasimhan that shows its failure in characteristic $2$ is [Nar83]. Example 3.12.2, Remark 3.12.3 and Hypothesis 3.12.4 are a result of the milestone S7.18 of this project (tamnd/singularity#245).
