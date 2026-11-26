---
title: Runs along a curve
nodes: []
sources: [Hir64, CJS20, Nar83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs along a curve

Example 3.11.6 shows that the triple $(\rho, d, \tau_\rho)$ can get worse along a kangaroo path, and that the full form $\widetilde\tau$ does not repair it. So the data at the point do not give an invariant that does not get worse at each step where $\rho$ stays. In this section we ask a weaker question, and it is the question that a resolution needs: does each run of point blowups where $\rho$ stays end? An invariant that gets worse at some steps can still give a resolution if each such run ends. We give an example of a run that does not end. The run follows a curve along which the order is $\rho$, so the example is not a defect of the invariant: a point blowup does not separate the curve from the locus where the order is $\rho$. A second example shows that the right order along the curve is the order of $G$, and not the order of $\widetilde\Theta(G)$. It is an infinite run that starts at an isolated point of the locus where $\rho$ is at least its value at the start. We state the hypothesis that each run that does not end follows a curve along which the order of $G$ is at least $\rho$, and we report the computer tests.

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

### A run at an isolated point of the locus of $\rho$

In Example 3.12.2 the ideal $\widetilde\Theta(G_k)$ has the order $\rho$ along the curve $C$, and $\rho = 4$ at each point of $C$. So the point $P_k$ is not an isolated point of the locus where $\rho$ is $4$. The next example shows that an infinite run can also start at an isolated point of this locus. Along the curve of the run the order of $G$ is $\rho$, but the order of $\widetilde\Theta(G)$ is smaller.

**Example 3.12.4.** Let $p = 2$, $n = 3$ with the variables $x, y, z$, $\Delta = \{x, z\}$, and for $k \ge 0$ let
$$g_k = x^{5 + 3k} y^2 z^3 + x^{10 + 3k} y^3 z^2.$$
Let $P_k$ be the point $(\{x, z\}, g_k)$, let $G = y^2 z + x^5 y^3$, and let $\gamma = V(y, z)$ be the $x$-axis, with $I_\gamma = (y, z)$. Then:

1. $g_k$ is clean, $r = (5 + 3k, 0, 2)$, $G_k = G$, and $\widetilde\Theta(G) = (y^2 z, x^5 y^2)$. So $P_k$ is in the first case with $\rho = d = 3$.
2. The origin of the $x$-chart of the blowup of $P_k$ is the point $P_{k+1}$, and it is the point of the strict transform of $\gamma$ over the origin.
3. $G \in I_\gamma^3$, but $\widetilde\Theta(G) \subseteq I_\gamma^2$ and $\widetilde\Theta(G) \not\subseteq I_\gamma^3$.
4. Let $Q = (a, b, c) \in K^3$ be a point with $Q \ne 0$. Then $\rho(Q) \le 2$, and $\rho(Q) = 2$ if $Q$ is a point of $\gamma$. So the origin is an isolated point of the locus where $\rho \ge 3$.

So $P_0, P_1, P_2, \dots$ is an infinite run, and it starts at an isolated point of the locus where $\rho \ge 3$.

*Proof.* Part 1. The monomial $x^{5 + 3k} y^2 z^3$ has an odd exponent of $z$, and the monomial $x^{10 + 3k} y^3 z^2$ has an odd exponent of $y$. So no monomial of $g_k$ is a square, and $g_k$ is clean. The largest power of $x$ that divides $g_k$ is $x^{5 + 3k}$, and the largest power of $z$ is $z^2$. The variable $y$ is not in $\Delta$, so $r_y = 0$. Thus $r = (5 + 3k, 0, 2)$, and $g_k = x^{5 + 3k} z^2 G$ with $G = y^2 z + x^5 y^3$. The term $y^2 z$ is not divisible by $x$, and the term $x^5 y^3$ is not divisible by $z$. Both terms have degree at least $3$, and $y^2 z$ has degree $3$, so $d = \operatorname{ord} G = 3$. The generators of $\widetilde\Theta(G)$ are the two elements $r_i G + x_i \partial_i G$ for $i = x, z$ and the free derivative $\partial_y G$. With $r_x = 5 + 3k$ and $r_z = 2$, and with the coefficients modulo $2$, we get
$$e_x = (5 + 3k) y^2 z + (10 + 3k) x^5 y^3 = (k + 1) y^2 z + k x^5 y^3,$$
$$e_z = 2 G + z \partial_z G = y^2 z, \qquad \partial_y G = 2 y z + 3 x^5 y^2 = x^5 y^2.$$
Here $e_x$ is a combination of $y^2 z = e_z$ and $x^5 y^3 = y \partial_y G$. So $\widetilde\Theta(G) = (y^2 z, x^5 y^2)$. The element $y^2 z$ has order $3$ and $x^5 y^2$ has order $7$, so $\rho = 3 = d$, and $P_k$ is in the first case.

Part 2. The $x$-chart at the origin is $\pi(x) = x$, $\pi(y) = x y$, $\pi(z) = x z$. The new divisor is $\{x, z\}$: the chart variable is $x$, and the component $z = 0$ of $\Delta$ passes through the origin of the chart, since $t_z = 0$. We have
$$\pi(g_k) = x^{5 + 3k} \cdot x^2 y^2 \cdot x^3 z^3 + x^{10 + 3k} \cdot x^3 y^3 \cdot x^2 z^2 = x^{10 + 3k} y^2 z^3 + x^{15 + 3k} y^3 z^2.$$
We divide by $x^p = x^2$ and we get $x^{8 + 3k} y^2 z^3 + x^{13 + 3k} y^3 z^2 = g_{k+1}$. By part 1 this is clean, so no cleaning is necessary, and the new point is $P_{k+1}$. By part 1 for $k + 1$, $\rho(P_{k+1}) = 3 = \rho(P_k)$, so the step is a step of a run. The inverse image of $\gamma$ in the chart is given by $x y = x z = 0$. Away from the exceptional divisor $x = 0$ it is the set $y = z = 0$, so the strict transform of $\gamma$ is the $x$-axis $V(y, z)$ of the chart. It meets the exceptional divisor only at the origin, that is, at $P_{k+1}$.

Part 3. We have $G = y^2 (z + x^5 y)$, and $y^2 \in I_\gamma^2$ and $z + x^5 y \in I_\gamma$, so $G \in I_\gamma^3$. The generators $y^2 z$ and $x^5 y^2$ of $\widetilde\Theta(G)$ are in $I_\gamma^2$. Assume that $\widetilde\Theta(G) \subseteq I_\gamma^3$. The ideal $I_\gamma^3$ is generated by monomials in $y$ and $z$ of degree $3$, so a monomial is in $I_\gamma^3$ if and only if the sum of its exponents of $y$ and $z$ is at least $3$. The monomial $x^5 y^2$ has the sum $2$. This is a contradiction. So the order of $\widetilde\Theta(G)$ along $\gamma$ is $2 < \rho$.

Part 4. The component $x_i = 0$ of $\Delta$ passes through $Q$ if and only if the coordinate $i$ of $Q$ is $0$. Let $\Delta_Q$ be the set of the components through $Q$, and let $u = (x - a, y - b, z - c)$ be the coordinates at $Q$. The log-Jacobian ideal at $Q$ is generated by $u_i \partial_i g_0$ for $i \in \Delta_Q$ and by $\partial_j g_0$ for $j \notin \Delta_Q$. If $i \in \Delta$ and $i \notin \Delta_Q$, then $x_i$ is a unit at $Q$, so $\partial_i g_0$ and $x_i \partial_i g_0$ generate the same ideal of $K[[u]]$. Thus the log-Jacobian ideal at $Q$ is $\Theta(g_0) K[[u]]$, where $\Theta(g_0)$ is the ideal for $\Delta$. The clean part $g_Q$ of $g_0$ at $Q$ differs from $g_0$ by a $p$-th power, so by Lemma 3.1.2 it has the same ideal. Write $g_Q = u^{r'} G'$ for $\Delta_Q$. Then $\Theta(g_Q) = u^{r'} \widetilde\Theta(G')$, and by Theorem 3.1.4, part 1, $u^{r'}$ is the largest monomial in the variables of $\Delta_Q$ that divides each element of $\Theta(g_Q)$. So $\rho(Q)$ is the order at $Q$ of the ideal that we get when we divide $\Theta(g_0) K[[u]]$ by its largest monomial factor in the variables of $\Delta_Q$. By part 1, $\Theta(g_0) = x^5 z^2 \widetilde\Theta(G) = x^5 y^2 z^2 (z, x^5)$. There are four cases.

- If $a = c = 0$ and $b \ne 0$, then $\Delta_Q = \{x, z\}$ and $y$ is a unit. The ideal is $x^5 z^2 (z, x^5)$, and $(z, x^5)$ is not contained in $(x)$ or in $(z)$. So $\rho(Q) = \operatorname{ord}_Q (z, x^5) = 1$.
- If $a = 0$ and $c \ne 0$, then $\Delta_Q = \{x\}$ and $z$ is a unit, so $(z, x^5) = K[[u]]$. The ideal is $x^5 (y^2)$, and $\rho(Q) = \operatorname{ord}_Q y^2$. This is $2$ if $b = 0$, and $0$ if $b \ne 0$.
- If $a \ne 0$ and $c = 0$, then $\Delta_Q = \{z\}$ and $x$ is a unit, so $(z, x^5) = K[[u]]$. The ideal is $z^2 (y^2)$, and $\rho(Q) = \operatorname{ord}_Q y^2$. This is $2$ if $b = 0$, and $0$ if $b \ne 0$.
- If $a \ne 0$ and $c \ne 0$, then $\Delta_Q = \emptyset$, and $x$ and $z$ are units. The ideal is $(y^2)$, and $\rho(Q) \le 2$ in the same way.

So $\rho(Q) \le 2$ for each $Q \ne 0$. The points of $\gamma$ with $Q \ne 0$ are the points $(a, 0, 0)$ with $a \ne 0$, and they are in the third case, so $\rho(Q) = 2$ there.

By part 2, $P_{k+1}$ is a point of the blowup of $P_k$ with the same $\rho$, for each $k \ge 0$. So the sequence $P_0, P_1, P_2, \dots$ is an infinite run. By part 4, $P_0$ is an isolated point of the locus where $\rho \ge 3$. $\square$

Part 4 holds for each $P_k$ with the same proof, since $\Theta(g_k) = x^{5 + 3k} y^2 z^2 (z, x^5)$. So each point of the run is an isolated point of the locus where $\rho \ge 3$, and the point blowup at $P_k$ is the blowup that the locus of $\rho$ asks for. All the same, the run does not end. The curve $\gamma$ is not in the locus of $\rho$, but it is in the locus where the order of $G$ is at least $3$: at a point $(a, 0, 0)$ of $\gamma$, the series $G$ has the term $a^5 y^3$ of degree $3$ in $u$, and $G \in I_\gamma^3$. Note also that $\gamma$ lies in the component $z = 0$ of $\Delta$.

The blowup of $\gamma$ ends the run. Here $g_0 \in I_\gamma^5 \subseteq I_\gamma^p$, but by part 3 condition (H1) of Section 3.4 fails, so Theorem 3.4.5 does not apply. We compute the points over the origin directly. In the $y$-chart $\pi(y) = y$, $\pi(z) = y (z + t)$, $\pi(x) = x$, the transform is $g' = x^5 y^3 (z + t)^3 + x^{10} y^3 (z + t)^2$. Each monomial has the exponent $3$ of $y$, so $g'$ is clean. If $t \ne 0$, the divisor is $\{x, y\}$, $G' = (z + t)^3 + x^5 (z + t)^2$ is a unit, and $\rho' = 0$. If $t = 0$, the divisor is $\{x, y, z\}$, $r' = (5, 3, 2)$ and $G' = z + x^5$. The generators of $\widetilde\Theta(G')$ are $5 G' + 5 x^5 = z$, $3 G' = z + x^5$ and $2 G' + z = z$, so $\rho' = 1$. In the $z$-chart at the origin, $\pi(z) = z$, $\pi(y) = z y$, $\pi(x) = x$, the transform is $g' = x^5 y^2 z^3 + x^{10} y^3 z^3$ with the divisor $\{x, z\}$. It is clean, $r' = (5, 0, 3)$ and $G' = y^2 + x^5 y^3$, and the generator $5 G' + x \partial_x G' = y^2 + 10 x^5 y^3 = y^2$ gives $\rho' \le 2$. So $\rho' < 3$ at each point over the origin.

### The hypothesis

Examples 3.12.2 and 3.12.4 show that the question "does each run end" has the answer no for a reason that each resolution must handle. The right question is whether each run that does not end is of this kind. Let $\gamma$ be a formal curve through $P_0$, that is, a regular formal curve given by a prime ideal $I_\gamma$ of $K[[x]]$ with $K[[x]] / I_\gamma \cong K[[s]]$. We say that a run $P_0, P_1, \dots$ *follows* $\gamma$ if, for each $i$, the point $P_{i+1}$ is the point of the strict transform of $\gamma_i$ over $P_i$, where $\gamma_0 = \gamma$ and $\gamma_{i+1}$ is the strict transform of $\gamma_i$.

**Hypothesis 3.12.5 (H4).** Let $P_0, P_1, P_2, \dots$ be an infinite run, and let $g = x^r G$ and $\rho$ be the data of $P_0$. Then the run follows a formal curve $\gamma$ through $P_0$, and the order of $G$ along $\gamma$ is at least $\rho$, that is, $G \in I_\gamma^\rho$.

This is an open question. We do not know a proof or a counterexample. Example 3.12.2 and Remark 3.12.3 are infinite runs that satisfy the conclusion, with $\gamma = C$ and with the curve $x = 0$. Example 3.12.4 satisfies it with the $x$-axis $\gamma$, by part 3.

**Remark 3.12.6.** The first form of H4 in this section asked for $\widetilde\Theta(G) \subseteq I_\gamma^\rho$ in place of $G \in I_\gamma^\rho$. This form is false, by Example 3.12.4. There $\rho = 3$, and no formal curve $\gamma'$ through the origin has $\widetilde\Theta(G) \subseteq I_{\gamma'}^3$. For a proof, let $v$ be the order along $\gamma'$, that is, $v(h)$ is the largest $m$ with $h \in I_{\gamma'}^m$. Since $K[[x]] / I_{\gamma'}$ is regular, the graded ring of $I_{\gamma'}$ is a polynomial ring over $K[[s]]$, so $v(h h') = v(h) + v(h')$. Also $I_{\gamma'}^2 \subseteq \mathfrak{m}^2$, so $v(x), v(y), v(z) \le 1$. If $\widetilde\Theta(G) \subseteq I_{\gamma'}^3$, then $2 v(y) + v(z) = v(y^2 z) \ge 3$, so $v(y) = v(z) = 1$, and $I_{\gamma'}$ contains the prime ideal $(y, z)$ of height $2$. Both ideals have height $2$, so $I_{\gamma'} = (y, z)$ and $v(x) = 0$. Then $v(x^5 y^2) = 2 < 3$, which is a contradiction. In Example 3.12.2 the two forms agree, since there $\widetilde\Theta(G_k) \subseteq I_C^4$ and $G_k \in I_C^4$.

**What H4 gives.** Assume that H4 holds. The locus where the order of $G$ is at least $\rho$ is closed. If $G \in I_\gamma^\rho$, then the generic point of $\gamma$ is in this locus, so the locus has dimension at least one at $P_0$, and $P_0$ is not an isolated point of the locus. So two things follow.

1. A run that starts at an isolated point of the locus where the order of $G$ is at least $\rho$ is finite. For such a run the point blowups are sufficient, and the invariant can get worse at some steps without harm.
2. A run that does not end gives a formal curve $\gamma$ of this locus. If $\gamma$ is algebraic and it is a permissible center, then its blowup is a step of a different type. Theorem 3.4.5 controls $\rho$ at this step under the conditions (H1) and (H2). Condition (H1) asks for the order $\rho$ of $\widetilde\Theta(G)$ along $\gamma$, and Example 3.12.4 shows that it can fail. So this step needs a form of Theorem 3.4.5 with a condition on $G$. In Example 3.12.4, $\rho$ goes down at each point over the origin.

So a resolution with this invariant must take its centers in the locus of the order of $G$, that is, the locus where the multiplicity of $G$ is at least $\rho$, and $\rho$ is a second entry of the invariant. The locus of $\rho$ alone is not sufficient. A choice of centers needs that the value of the invariant at the point is also its value at the generic point of the curve that the run follows, so that the curve is in the locus. The function $\rho$ does not have this property: in Example 3.12.4 it is $3$ at the origin and $2$ at the other points of $\gamma$, and the locus where $\rho \ge 3$ is the origin only. The other way is a form of $\rho$ that sees the curve.

This is the shape of the classical argument for surfaces: blow up the isolated points of the locus of maximal order, and the curves of the locus when the point blowups do not separate them.

**Characteristic zero.** In characteristic $0$ the analogue of H4 for the order of an ideal comes from a hypersurface of maximal contact (Volume 2, Theorem 2.3.3). The points where the order stays lie on the strict transforms of this hypersurface, so an infinite sequence of such points is a sequence on a space of dimension one less, and the induction on the dimension reduces the question to a curve. In characteristic $p$ a hypersurface of maximal contact need not exist, also not in the formal neighbourhood of the point [Nar83] (Volume 2, Section 2.4). So in characteristic $p$, H4 does not follow from this argument, and it is the point to test.

### The computer tests

A test explored the full tree of a point to a depth limit: all the charts, all the translations over $\mathbb{F}_p$, and the cleaning at each step. The runs had $(p, n) = (2, 3)$, and they started at points of the first case with $p \mid |r| + d$ and $\tau_\rho \ge 2$. The script `inv38` used the depth limit $10$ on $600$ starts. At $446$ starts all the branches ended, $153$ starts reached the depth limit, and $1$ start reached the time limit. The script `inv38b` used the depth limit $12$ on $800$ starts, with the results $621$, $178$ and $1$. The maximal depth of a start where all the branches end was $11$, at a start with $(\rho, d, \tau_\rho) = (4, 4, 2)$. All the starts with $\tau_\rho = 3$ ended at depth $0$. The script `inv38b` also extended each deep branch along the same chart at the origin for $40$ more steps. Of the deep nodes, $238$ were axis tails, that is, the last four steps or more were in the same chart at the origin. For $236$ of them, $\rho$ stayed for the $40$ extra steps, and for $2$ of them $\rho$ went from $4$ to $2$. Only $40$ deep nodes were not axis tails. A chain of the test shows the mechanism of Example 3.12.2: at each step $G$ contains the term $x^4$ and $\Delta = \{y\}$, so the order is $4$ along the curve $x = z = 0$, and the chart at the origin is the point of the strict transform of this curve.

The script `inv39` computed the formal curve of each deep branch of the trees of `inv38b`, and it checked two forms of H4 along the curve: $\widetilde\Theta(G) \subseteq I_\gamma^\rho$ (the first form) and $G \in I_\gamma^\rho$ (the form of Hypothesis 3.12.5). For the $238$ axis tails of $(p, n) = (2, 3)$, the first form held for $216$ and failed for $22$. The form of Hypothesis 3.12.5 held for $234$ and failed for $4$. The $4$ failures are artifacts of the test. At the start $738$ they come from the cleaning in later charts, and at the start $788$ from a branch that is finite. There are $18$ distinct starts with $(p, n) = (2, 3)$ that contradict the first form. The start $49$ of them is Example 3.12.4. No start contradicts the form of Hypothesis 3.12.5. For $(p, n) = (3, 3)$ there were $30$ axis tails. The form of Hypothesis 3.12.5 held for all $30$, and the first form held for $28$. It failed at the starts $44$ and $170$. At the start $44$ the order of $G$ along the curve is $6$, and the order of $\widetilde\Theta(G)$ is $5$.

A second test repeated the tree test with the rule that each center is an isolated point of a locus: the locus where the order of $\widetilde\Theta(G)$ is at least $\rho$, or the locus where the order of $G$ is at least $\rho$. The table gives the number of starts where all the branches ended, the number of starts that reached the depth limit, and the maximal depth of a start where all the branches ended.

| $(p, n)$ | locus | all branches end | depth limit | maximal depth |
|---|---|---|---|---|
| $(2, 3)$ | $\rho$ | $780$ | $20$ | $11$ |
| $(2, 3)$ | order of $G$ | $799$ | $1$ | $11$ |
| $(3, 3)$ | $\rho$ | $398$ | $2$ | $6$ |
| $(3, 3)$ | order of $G$ | $400$ | $0$ | $6$ |
| $(2, 4)$, $300$ starts | order of $G$ | $298$ | $2$ | $2$ |

The tests have limits. The test checks that a point is isolated in the locus only against the lines and the quadrics over $\mathbb{F}_p$. So a start that passes the test can be a point of a curve of higher degree in the locus. The start of $(2, 3)$ that reached the depth limit with the locus of the order of $G$ is the start $788$. There $G = (x (x + y + z + z^3))^2$, and the locus contains the cubic $x = 0$, $y = z + z^3$. The start $112$ of $(2, 4)$ follows the curve $z = 0$, $w = y$, $y = x + x^3 y^2$. The deep nodes that are not axis tails are at the starts $777$ and $788$, and they follow curves too: the line $x = 0$, $y = z$ at the start $777$, and the cubic at the start $788$. So the deep starts of the tests with the locus of the order of $G$ follow curves of higher degree, which the test does not see. Two things are not tested: the isolation against curves of higher degree, and the cleaning at the generic point of the curve, where the residue field is not perfect.

### Notes and references

The use of the history of the components of the divisor is from [CJS20]. Maximal contact is from [Hir64], and the example of Narasimhan that shows its failure in characteristic $2$ is [Nar83]. Examples 3.12.2 and 3.12.4, Remarks 3.12.3 and 3.12.6 and Hypothesis 3.12.5 are a result of the milestone S7.18 of this project (tamnd/singularity#245).
