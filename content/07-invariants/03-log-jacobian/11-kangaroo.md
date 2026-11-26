---
title: The kangaroo path
nodes: [SG0000005B, SG0000005C, SG0000005D, SG0000005E, SG0000005F, SG0000005G]
sources: [Hir67, Hau10, CJS20]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The kangaroo path

Section 3.10 shows that at the points where $\rho$ stays, the triple $(\rho, d, \tau_\rho)$ can get worse only at a step with a leaving component, from a point of the first case where $p$ divides $|r| + d$. At such a step the new point can be in the second case, with $d$ one larger, as at the kangaroo points of Example 3.2.6. In this section we follow the sequence after a kangaroo point. It goes through points of the second case, and it can come back to the first case. We show that $\tau_\rho$ does not go down along the points of the second case, and that the full form $\widetilde\tau$ of Section 3.8 at the point of return is at least $\tau_\rho$ at the start. We state the conjecture that $\tau_\rho$ itself is at least its value at the start, and we give an example that shows why a simple proof does not work. We describe the forms of $H$ at a point of the first case in terms of the initial form of $G$, and we show that the conjecture holds if $\tau_\rho(P_0) \le 1$. Last, we give a counterexample with $\tau_\rho(P_0) = 2$. So the conjecture is false, and the triple $(\rho, d, \tau_\rho)$ can get worse along a kangaroo path.

We use the setting and the notation of Sections 3.8 to 3.10. So $g = x^r G$ is clean, $d = \operatorname{ord} G$, and $\rho = \rho(g)$. By Corollary 3.10.2, the first case is $d = \rho$ and the second case is $d = \rho + 1$. We write a point as the pair $(\Delta, g)$.

A *kangaroo path* is a sequence of points $P_0, P_1, \dots, P_m$ with $m \ge 2$, where each $P_{i+1}$ is a point of a chart of the blowup of $P_i$ with $\rho(P_{i+1}) = \rho(P_i)$, where $P_0$ and $P_m$ are in the first case, and where $P_1, \dots, P_{m-1}$ are in the second case.

By Section 3.10, the first step of a kangaroo path goes from a point of the first case with $p \mid |r| + d$ to the second case, and a component of $\Delta$ leaves at this step. The other components of $\Delta$ can leave at the later steps, and the exceptional divisor of each step is a new component.

### The points of the second case

**Proposition 3.11.1.** Let $P_0, P_1, \dots, P_m$ be a sequence of points as in a kangaroo path, but with no hypothesis on the case of $P_0$ and of $P_m$. Then
$$\tau_\rho(P_0) \le \tau_\rho(P_1) \le \dots \le \tau_\rho(P_{m-1}) \le \widetilde\tau(P_m).$$

Node: SG0000005B · Lean: `Singularity.logJacobianDirectrixCodim_le_fullDirectrixCodim_of_reflTransGen` (for polynomials)

*Proof.* Proposition 3.8.2 has two hypotheses: $\rho$ stays, and the new point is in the second case. It has no hypothesis on the old point. Its proof transports each element of $H(g)$, and $H(g)$ is made from $\widetilde\Theta_0(G)$ in the first case and from $\widetilde\Theta(G)$ in the second case. In both cases the transport lands in $\widetilde\Theta(G')$, and in the second case this is the ideal of $H(g'_c)$. The proof also does not use the hypothesis that no component leaves, since the new divisor is the divisor of the chart in each case. So Proposition 3.8.2 applies at each step from $P_i$ to $P_{i+1}$ with $i + 1 \le m - 1$, and it gives the first $m - 1$ inequalities. At the last step, the same transport lands in $\widetilde\Theta(G')$, and $\widetilde T$ is made from all of $\widetilde\Theta(G')$. So the dimension argument of Proposition 3.8.2 gives $\dim \widetilde T(P_m) \le \dim T_\rho(P_{m-1})$, with no hypothesis on the case of $P_m$. This is the last inequality. $\square$

At $P_m$ we have $\tau_\rho(P_m) \le \widetilde\tau(P_m)$, since $T_\rho \supseteq \widetilde T$. If $P_m$ is in the second case, the two are equal. If $P_m$ is in the first case, they can be different (Example 3.8.5). So Proposition 3.11.1 does not bound $\tau_\rho(P_m)$ from below. Indeed $\tau_\rho$ can go down at the last step, and this happens in the example below.

### An example

**Example 3.11.2.** Let $p = 2$, $n = 3$ with the variables $x, y, z$, $\Delta = \{x, z\}$ and
$$g = x z (x^2 + z^2 + x^3 y) = x^3 z + x z^3 + x^4 y z.$$
The exponent $(1, 0, 3)$ is not even, so $g$ is clean. Here $r = (1, 0, 1)$ and $G = x^2 + z^2 + x^3 y$, so $d = 2$. In characteristic $2$ the generators of $\widetilde\Theta(G)$ are
$$e_x = G + x \partial_x G = x^2 + z^2, \qquad e_z = G + z \partial_z G = G, \qquad \partial_y G = x^3.$$
So $\rho = 2$, and $\widetilde\Theta_0(G)$ also has order $2$, so $P_0$ is in the first case. Also $|r| + d = 4$ is even. The forms of $H(P_0)$ are the multiples of $(x + z)^2$, so $T_\rho(P_0) = \{a_x = a_z\}$ and $\tau_\rho(P_0) = 1$.

Take the chart $\pi(x) = x$, $\pi(y) = x (y + 1)$, $\pi(z) = x (z + 1)$. Then $t_z = 1$, so the component $z = 0$ leaves, and the new divisor is $\{x\}$. We have
$$\pi(g) = x^4 \bigl( (z + 1)^3 + (z + 1) + x^2 (y + 1)(z + 1) \bigr) = x^4 \bigl( z^3 + z^2 + x^2 (y z + y + z + 1) \bigr).$$
We divide by $x^2$ and we remove the monomials $x^2 z^2$ and $x^4$, which are squares. This gives $g_1 = x^2 G_1$ with $G_1 = z^3 + x^2 y z + x^2 y + x^2 z$, so $d_1 = 3$. The element $e_x = 2 G_1 + x \partial_x G_1$ is $0$, and the free derivatives are
$$\partial_y G_1 = x^2 z + x^2, \qquad \partial_z G_1 = z^2 + x^2 y + x^2.$$
So $\rho(P_1) = 2$, and $P_1$ is in the second case. The forms of degree $2$ are $x^2$ and $x^2 + z^2$, so $T_\rho(P_1) = \{a_x = a_z = 0\}$ and $\tau_\rho(P_1) = 2$.

Now take the chart $\pi(x) = y x$, $\pi(y) = y$, $\pi(z) = y z$ at the origin. We divide by $y^2$, and no monomial is a square, so $g_2 = x^2 y^3 G_2$ with
$$G_2 = x^2 + z^3 + x^2 z + x^2 y z,$$
and the divisor is $\{x, y\}$. Then $e_x = 2 G_2 + x \partial_x G_2 = 0$ and $e_y = 3 G_2 + y \partial_y G_2 = x^2 + z^3 + x^2 z$. So $\rho(P_2) = 2$, $d_2 = 2$, and $P_2$ is in the first case. The forms of $H(P_2)$ are the multiples of $x^2$, so $T_\rho(P_2) = \{a_x = 0\}$ and $\tau_\rho(P_2) = 1$.

So $\tau_\rho$ goes $1, 2, 1$ along the path, and $\tau_\rho(P_2) = \tau_\rho(P_0)$. But the two directrices $\{a_x = a_z\}$ and $\{a_x = 0\}$ are different planes. The old form $(x + z)^2$ is still at $P_2$. It is the initial form of the free derivative $\partial_z G_2 = z^2 + x^2 y + x^2$, so it is in $\widetilde\Theta(G_2)$ and not in $\widetilde\Theta_0(G_2)$. Thus $\widetilde T(P_2) = \{a_x = a_z = 0\}$ and $\widetilde\tau(P_2) = 2$.

Node: SG0000005C

The example shows that a proof of the conjecture below cannot transport the forms of $P_0$ into $H(P_m)$, as the proofs of Proposition 3.8.2 and Theorem 3.9.11 do. In the example the transports of $e_x$ and $e_z$ have the parts $z^2$ and $x^2 + z^2$ of degree $2$, and $z^2$ is not a multiple of $x^2$. A proof must compare the dimensions in a different way.

### The conjecture

**Conjecture 3.11.3.** Let $P_0, P_1, \dots, P_m$ be a kangaroo path. Then $\tau_\rho(P_m) \ge \tau_\rho(P_0)$.

Node: SG0000005D · Lean: `Singularity.KangarooPathConjecture` (the statement; the negation is proved)

**The conjecture is false.** Example 3.11.6 below is a counterexample with $p = 2$ and $n = 3$. We keep the statement here because the first random tests at the end of this section supported it, and because the counterexample shows which part of the argument fails.

If the conjecture were true, then a kangaroo path would not make the triple worse from $P_0$ to $P_m$: the value of $\rho$ is the same, $d(P_m) = \rho = d(P_0)$, and $\tau_\rho$ does not go down. Then the only remaining steps where the triple gets worse would be the steps of the second kind of Section 3.10: both points are in the first case, a component leaves, and $\tau_\rho$ goes down, as in Examples 3.9.5 and 3.9.6.

The hypothesis $m \ge 2$ is necessary. For $m = 1$ the path is one step from the first case to the first case, and Examples 3.9.5 and 3.9.6 are steps of this kind where $\tau_\rho$ goes down.

### The forms in the first case

At a point of the first case, the forms of $H(g)$ have a closed description in terms of the initial form of $G$ alone. So a proof of the conjecture can compare $P_0$ and $P_m$ through the initial forms, without a transport of the elements of $H(P_0)$.

**Lemma 3.11.4.** Let $g = x^r G$ be in the first case, and let $F$ be the part of degree $\rho$ of $G$. For $i \in \Delta$ put $E_i F = r_i F + x_i \partial_i F$. Then
$$T_\rho(g) = \bigcap_{i \in \Delta} T(E_i F).$$

Node: SG0000005E · Lean: `Singularity.logJacobianDirectrix_eq_iInf_caseAForm`

*Proof.* The ideal $\widetilde\Theta_0(G)$ is generated by the elements $e_i = r_i G + x_i \partial_i G$ for $i \in \Delta$ and by the elements $x_a \partial_l G$ for $l \notin \Delta$ and each $a$. Each $e_i$ and each $\partial_l G$ with $l \notin \Delta$ is in $\widetilde\Theta(G)$, and this ideal has order $\rho$. So $e_i$ has order at least $\rho$, and its part of degree $\rho$ is $E_i F$. Also $x_a \partial_l G$ has order at least $\rho + 1$, so its part of degree $\rho$ is $0$.

Let $\psi$ be an element of the definition of $T_\rho(g)$. In the first case $x^r \psi$ is in $\Theta_0(g) = x^r \widetilde\Theta_0(G)$, so $\psi$ is in $\widetilde\Theta_0(G)$. Since each generator has order at least $\rho$, the part of degree $\rho$ of $\psi$ is a linear combination of the parts of degree $\rho$ of the generators, that is, of the $E_i F$. So each vector of $\bigcap_i T(E_i F)$ is in $T(\psi_\rho)$.

Conversely, let $i \in \Delta$ with $E_i F \ne 0$. Then $e_i$ has order exactly $\rho$, and $x^r e_i = x_i \partial_i g$ is in $\Theta_0(g)$. So $e_i$ is an element of the definition of $T_\rho(g)$, and $T_\rho(g) \subseteq T(E_i F)$. If $E_i F = 0$, then $T(E_i F)$ is the full space. $\square$

The proof does not use that $g$ is clean, and it has no hypothesis on the field.

**The characters.** Now let $g$ be clean. In the first case $\rho = d$, so $F = \operatorname{in}(G)$, and $\partial_l F = 0$ for each $l \notin \Delta$ by part 3 of Theorem 3.1.4. So for each monomial $x^\alpha$ of $F$, the exponent $\alpha_l$ is divisible by $p$ for each $l \notin \Delta$. Put
$$\chi(\alpha) = (r_i + \alpha_i \bmod p)_{i \in \Delta} \in \mathbb{F}_p^\Delta.$$
The monomial $x^{r + \alpha}$ is a monomial of $g$. Since $g$ is clean, not all exponents of $x^{r + \alpha}$ are divisible by $p$, so $\chi(\alpha) \ne 0$. Let $F_\chi$ be the sum of the terms of $F$ with the character $\chi$. The coefficient of $x^\alpha$ in $E_i F$ is $(r_i + \alpha_i) c_\alpha$, so
$$E_i F = \sum_\chi \chi_i F_\chi.$$
Thus the span of the $E_i F$ is the set of the sums $\sum_\chi \lambda(\chi) F_\chi$, with $\lambda$ a linear map from $\mathbb{F}_p^\Delta$ to $K$. This span is contained in the span of the $F_\chi$, with equality if the characters that occur in $F$ are linearly independent over $\mathbb{F}_p$. In particular $T_\rho(g)$ contains the joint directrix of the $F_\chi$.

In Example 3.11.2, at $P_0$ we have $F = x^2 + z^2$ and $r = (1, 0, 1)$ on $\Delta = \{x, z\}$. Both monomials have the character $(1, 1)$, so the span of the $E_i F$ is spanned by $x^2 + z^2$. At $P_2$ we have $F = x^2$ with $r_x = 2$ and $r_y = 3$ on $\Delta = \{x, y\}$. The character is $(0, 1)$, and the span is spanned by $x^2$.

By Lemma 3.11.4, Conjecture 3.11.3 compares the joint directrices of two spans of the same kind at $P_0$ and at $P_m$. At the points of the second case between them, the forms of $H$ also include the initial forms of the free derivatives $\partial_l G$, and the decomposition by characters does not apply.

### When the start has codimension at most one

The conjecture has content only if $\tau_\rho(P_0) \ge 2$. The reason is that $\tau_\rho$ is at least $1$ at each point of the first case with $\rho \ge 1$.

**Proposition 3.11.5.** Let $g = x^r G$ be a polynomial with $\rho = \rho(g)$ finite.

1. If $\rho = 0$, then $\tau_\rho(g) = 0$.
2. If $\rho \ge 1$ and $g$ is in the first case, then $\tau_\rho(g) \ge 1$.
3. Let $P_0, P_1, \dots, P_m$ be a kangaroo path with $\tau_\rho(P_0) \le 1$. Then $\tau_\rho(P_m) \ge \tau_\rho(P_0)$.

Node: SG0000005F · Lean: `Singularity.kangarooPath_of_codim_le_one`

*Proof.* First we show that a form $F$ of degree $e \ge 1$ with $T(F) = K^n$ is $0$. Let $i$ be an index. The vector $e_i$ is in $T(F)$, so $F(x + s e_i) = F(x)$ in $K[x, s]$. Apply to this identity the homomorphism of $K$-algebras from $K[x, s]$ to $K[x]$ that sends $s$ to $x_i$, sends $x_i$ to $0$, and fixes the other variables. On the left side the variable $x_i$ becomes $x_i + s$ and then $0 + x_i$, so the left side becomes $F$. The right side becomes $F|_{x_i = 0}$. Thus $F = F|_{x_i = 0}$, and no monomial of $F$ contains $x_i$. This holds for each $i$, so $F$ is a constant, and since $e \ge 1$ we get $F = 0$. The argument uses only the identity in $K[x, s]$, so it holds also over a finite field, where a polynomial can vanish at each point without being $0$.

For part 1, let $\psi$ be an element of the definition of $T_\rho(g)$. Its part of degree $0$ is a constant, and the directrix of a constant is the full space. So $T_\rho(g) = K^n$ and $\tau_\rho(g) = 0$.

For part 2, in the first case the ideal $\Theta_0(g)$ has order $|r| + \rho$, so it has an element $f$ of this order. Since $\Theta_0(g) = x^r \widetilde\Theta_0(G)$, we can write $f = x^r \psi$ with $\operatorname{ord} \psi = \rho$. So $\psi$ is an element of the definition of $T_\rho(g)$, and its part $\psi_\rho$ of degree $\rho$ is a nonzero form of positive degree. By the first step $T(\psi_\rho) \ne K^n$, so $T_\rho(g) \ne K^n$ and $\tau_\rho(g) \ge 1$.

For part 3, the value of $\rho$ is the same at each point of the path. If $\rho = 0$, then $\tau_\rho(P_0) = 0$ by part 1. If $\rho \ge 1$, then $\tau_\rho(P_m) \ge 1 \ge \tau_\rho(P_0)$ by part 2, since $P_m$ is in the first case. $\square$

So a counterexample to Conjecture 3.11.3 must start at a point with $\tau_\rho(P_0) \ge 2$. In Example 3.11.2 we have $\tau_\rho(P_0) = 1$, so the example is in the case of Proposition 3.11.5. The example is of interest because the directrix moves, not because $\tau_\rho$ could go down.

### A counterexample

The next example starts at a point with $\tau_\rho(P_0) = 2$. The path has one point of the second case, and $\tau_\rho$ goes down from $2$ to $1$ at the last step.

**Example 3.11.6.** Let $p = 2$, $n = 3$ with the variables $x, y, z$, $\Delta = \{y, z\}$ and
$$g_0 = y z (x^2 y^2 + x^2 z^2 + x^4 z) = x^2 y^3 z + x^2 y z^3 + x^4 y z^2.$$
All coefficients are $1$, so the example works over each field $K$ of characteristic $2$. Each monomial has an odd exponent, so $g_0$ is clean. Here $r = (0, 1, 1)$ and $G_0 = x^2 y^2 + x^2 z^2 + x^4 z$, so $d_0 = 4$. In characteristic $2$ we have $\partial_x G_0 = 0$ and $\partial_y G_0 = 0$, and $\partial_z G_0 = x^4$. So
$$e_y = G_0 + y \partial_y G_0 = G_0, \qquad e_z = G_0 + z \partial_z G_0 = x^2 y^2 + x^2 z^2,$$
and the only free derivative is $\partial_x G_0 = 0$. So $\rho(P_0) = 4$, and $\widetilde\Theta_0(G_0)$ also has order $4$, so $P_0$ is in the first case. Also $|r| + d_0 = 6$ is even. The part of degree $4$ of $G_0$ is
$$F_0 = x^2 y^2 + x^2 z^2 = x^2 (y + z)^2,$$
and $E_y F_0 = E_z F_0 = F_0$. By Lemma 3.11.4, $T_\rho(P_0) = T(F_0)$. For a vector $b$, in $K[x, y, z, s]$ we have $F_0(x + s b) = (x^2 + s^2 b_x^2) \bigl( (y + z)^2 + s^2 (b_y + b_z)^2 \bigr)$, since squares are additive in characteristic $2$. This is equal to $F_0$ if and only if $b_x = 0$ and $b_y + b_z = 0$. We use the identity of polynomials, and not the values at the points, because the example must also work over $\mathbb{F}_2$. Thus $T_\rho(P_0) = \{a_x = 0, a_y = a_z\}$ and $\tau_\rho(P_0) = 2$.

Take the chart $\pi(x) = y x$, $\pi(y) = y$, $\pi(z) = y (z + 1)$. Then $t_z = 1$, so the component $z = 0$ leaves, and the new divisor is $\{y\}$. We have
$$\pi(g_0) = y^6 \bigl( x^2 (z + 1) + x^2 (z + 1)^3 + x^4 y (z + 1)^2 \bigr) = y^6 \bigl( x^2 z^3 + x^2 z^2 + x^4 y z^2 + x^4 y \bigr).$$
We divide by $y^2$ and we remove the monomial $x^2 y^4 z^2$, which is a square. This gives $g_1 = y^4 G_1$ with
$$G_1 = x^2 z^3 + x^4 y + x^4 y z^2,$$
so $d_1 = 5$. The element $e_y = 4 G_1 + y \partial_y G_1 = x^4 y + x^4 y z^2$ has order $5$, and the free derivatives are $\partial_x G_1 = 0$ and $\partial_z G_1 = x^2 z^2$. So $\rho(P_1) = 4$, and $\widetilde\Theta_0(G_1)$ has order $5$, so $P_1$ is in the second case. The only form of degree $4$ is $x^2 z^2$, so $T_\rho(P_1) = \{a_x = a_z = 0\}$ and $\tau_\rho(P_1) = 2$.

Now take the chart $\pi(x) = y x$, $\pi(y) = y$, $\pi(z) = y z$ at the origin. We divide by $y^2$, and no monomial is a square, so $g_2 = y^7 G_2$ with
$$G_2 = x^4 + x^2 z^3 + x^4 y^2 z^2,$$
and the divisor is $\{y\}$. Then $e_y = 7 G_2 + y \partial_y G_2 = G_2$, since $\partial_y G_2 = 0$. So $e_y$ has order $4$ and the initial form $x^4$. The free derivatives are $\partial_x G_2 = 0$ and $\partial_z G_2 = x^2 z^2$. So $\rho(P_2) = 4$, $d_2 = 4$, and $P_2$ is in the first case. By Lemma 3.11.4, with $F_2 = x^4$ and $E_y F_2 = x^4$, we get $T_\rho(P_2) = \{a_x = 0\}$ and $\tau_\rho(P_2) = 1$.

So $\tau_\rho$ goes $2, 2, 1$ along the kangaroo path $P_0, P_1, P_2$, and $\tau_\rho(P_2) < \tau_\rho(P_0)$. The triple $(\rho, d, \tau_\rho)$ goes from $(4, 4, 2)$ to $(4, 5, 2)$ and then to $(4, 4, 1)$. Thus Conjecture 3.11.3 is false.

Node: SG0000005G · Lean: `Singularity.KangarooCounterexample.not_kangarooPathConjecture`

The mechanism is as follows. At $P_1$ the form of degree $4$ comes only from the free derivative $\partial_z G_1$, which has the initial form $x^2 z^2$. The monomial $x^4 y$ of $G_1$ has degree $5$. At the blowup at the origin of the $y$-chart, a monomial $x^a y^b z^c$ of $g$ goes to $x^a y^{a + b + c - 2} z^c$. So the exponent $r_y$ grows by $d - 2$, and the exponent of $y$ in the monomial $x^4 y^{b - r_y}$ of $G$ changes by $4 - d$. At $P_1$ we have $d = 5$, so this monomial of $G$ loses one degree. At $P_2$ it is $x^4$, of degree $4$, so $e_y$ gets the order $4$ and the point goes back to the first case. In the first case the forms of the free derivatives do not count in $T_\rho$, so the form $x^2 z^2$ is lost, and only $x^4$ remains.

The form $x^2 z^2$ is still in $\widetilde\Theta(G_2)$, so $\widetilde T(P_2) = \{a_x = a_z = 0\}$ and $\widetilde\tau(P_2) = 2$. This agrees with Proposition 3.11.1. So the full form $\widetilde\tau$ does not go down along this path, but $\tau_\rho$ does.

The full form does not repair the triple at the next step. The only point $P_3$ of the blowup of $P_2$ with $\rho = 4$ is the origin of the $y$-chart. Indeed, by Corollary 3.7.3 the points where $\rho$ stays lie in $\mathbb{P}(T_\rho(P_2))$, so they have $a_x = 0$. At the point of the $y$-chart with $t_z = c \ne 0$, the free derivative $\partial_z G$ gets the term $c^2 x^2 y$ of degree $3$, so $\rho \le 3$. At the origin of the $z$-chart, $d = 3$. There $g_3 = y^9 G_3$ with
$$G_3 = x^4 + x^2 y z^3 + x^4 y^4 z^2,$$
and the divisor stays $\{y\}$. Then $e_y = 9 G_3 + y \partial_y G_3 = x^4 + x^4 y^4 z^2$, and the free derivative $\partial_z G_3 = x^2 y z^2$ has order $5$. So $P_3$ is in the first case with $\tau_\rho(P_3) = \widetilde\tau(P_3) = 1$. The values along $P_0, P_1, P_2, P_3$ are:

| point | case | $(\rho, d)$ | $\tau_\rho$ | $\widetilde\tau$ |
| --- | --- | --- | --- | --- |
| $P_0$ | first | $(4, 4)$ | $2$ | $2$ |
| $P_1$ | second | $(4, 5)$ | $2$ | $2$ |
| $P_2$ | first | $(4, 4)$ | $1$ | $2$ |
| $P_3$ | first | $(4, 4)$ | $1$ | $1$ |

So $\widetilde\tau$ goes down at the step from $P_2$ to $P_3$, a step from the first case to the first case with no leaving component. Thus an invariant made only from $\rho$, $d$ and one of $\tau_\rho$ and $\widetilde\tau$ at the point gets worse from $P_0$ to $P_3$. An invariant that is good on this path must use other data. For example, $P_0$ has $p \mid |r| + d$, and $P_3$ has $|r| + d = 13$, which is odd.

A random test found a longer path of the same kind. It starts at $x^2 y^3 z + x^2 y z^3 + x^4 y^3 z^2 + x^4 y^5 z^4$ with the divisor $\{y, z\}$, the first step is the same chart, and the next steps are at the origin of the $y$-chart. The path has three points of the second case, and $\tau_\rho$ goes $2, 2, 2, 2, 1$. The exponent $3$ of $y$ in $x^4 y^3 z^2$ makes the monomial $x^4 y^{b - r_y}$ of $G$ start at degree $7$, so it takes three steps to come down to degree $4$. The monomial $x^4 y^5 z^4$ is not necessary for this path.

### What a random test found

Random tests followed sequences of point blowups at the points where $\rho$ stays, from random clean $g$ with random divisors.

1. A test compared $\tau_\rho$ at consecutive points of the first case in one sequence, in 3,250 sequences with $(p, n) = (2, 3), (2, 4), (3, 3)$ and $(5, 3)$. There were 7,092 comparisons, 249 of them on a kangaroo path. In none of them did $\tau_\rho$ go down.
2. A test recorded, at each step from the second case to the first case, the start of the run of points of the second case before it. In 1,500 sequences with $(p, n) = (2, 3)$ and 1,000 sequences with $(p, n) = (3, 3)$, there were 158 such steps at the end of a kangaroo path. At 26 of them $\tau_\rho$ went down at the last step, and at each of these 26 steps it went down to exactly $\tau_\rho(P_0)$. So the gain along the points of the second case was lost at the last step, but $\tau_\rho$ did not go below its value at the start. At the steps from the second case to the first case where the run of points of the second case started at the start of the sequence, $\tau_\rho$ went down 32 times, as in Example 3.8.3.
3. A test transported the generators of order $\rho$ of $\widetilde\Theta_0(G)$ at $P_0$ along the path, and checked whether their parts of degree $\rho$ at $P_m$ are in the span of the forms of $H(P_m)$. This held on 149 of the 152 kangaroo paths of the runs with $(p, n) = (2, 3)$ and $(3, 3)$, and failed on 3 of them, as in Example 3.11.2. On these 3 paths the conjecture held all the same.
4. A test recorded the pair $(\tau_\rho(P_0), \tau_\rho(P_m))$ on the 128 kangaroo paths of a run with $(p, n) = (2, 3)$. On each of them $\tau_\rho(P_0) \le 1$. So by Proposition 3.11.5 the tests 1 to 3 did not test the conjecture in the case where it has content.
5. A test started only at points of the first case with $p \mid |r| + d$ and $\tau_\rho(P_0) \ge 2$. With $(p, n) = (2, 3)$ it had 337 such starts, and 58 of them had a first step into the second case, each with a leaving component. It found 2 kangaroo paths where $\tau_\rho$ goes down from $2$ to $1$. Both start at the start of the longer path above, and the second path is the first one with the roles of $y$ and $z$ exchanged. With $(p, n) = (3, 3)$ it had 568 such starts and 16 first steps into the second case, and it found no kangaroo path back to the first case.

### The Lean proof

The Lean library proves Proposition 3.11.1 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianKangaroo.lean`. A step of a point blowup where $\rho$ stays $m$ is `Singularity.RhoStep`, and a point of the second case is `Singularity.IsLogJacobianCaseB`. A run of steps into points of the second case is the reflexive and transitive closure of the relation "a step into a point of the second case". `Singularity.logJacobianDirectrixCodim_le_of_reflTransGen` gives $\tau_\rho(P_0) \le \tau_\rho(P_{m-1})$, and `Singularity.logJacobianDirectrixCodim_le_fullDirectrixCodim_of_reflTransGen` gives $\tau_\rho(P_0) \le \widetilde\tau(P_m)$. The Lean statements have no hypothesis on the case of $P_0$ and of $P_m$. The Lean library has Conjecture 3.11.3 as the statement `Singularity.KangarooPathConjecture`, and it proves the negation for $p = 2$ in `Singularity/Invariant/LogJacobianKangarooCounterexample.lean`. The theorem is `Singularity.KangarooCounterexample.not_kangarooPathConjecture`. It is the computation of Example 3.11.6 over $\mathbb{F}_2$, with $x, y, z$ as the indices $0, 1, 2$ of `Fin 3`. The proof computes $g_1$ and $g_2$ from the two charts and the cleaning, and it gets the cases from the orders $6$, $9$ and $11$ of the ideals $\Theta_0(g_0)$, $\Theta_0(g_1)$ and $\Theta_0(g_2)$. For the bounds on $\tau_\rho$ it uses Lemma 3.11.4: at $P_0$ the directrix lies in the line $T(E_y F_0)$, so $\tau_\rho(P_0) \ge 2$, and at $P_2$ the directrix contains the plane $a_x = 0$, so $\tau_\rho(P_2) \le 1$. The proof does not compute the exact values, since the inequalities are sufficient. The proofs use the Lean form of Proposition 3.8.2 in `Singularity/Invariant/LogJacobianDirectrix.lean` and the bound $\tau_\rho(g) \le \widetilde\tau(g'_c)$ in `Singularity/Invariant/LogJacobianFullDirectrix.lean`. Lemma 3.11.4 is `Singularity.logJacobianDirectrix_eq_iInf_caseAForm` in `Singularity/Invariant/LogJacobianCaseAForms.lean`, with `Singularity.caseAForm` for the form $E_i F$. The Lean statement has no hypothesis on the field and no hypothesis that $g$ is clean. Proposition 3.11.5 is in `Singularity/Invariant/LogJacobianKangarooSmall.lean`. The first step of the proof is `Singularity.eq_zero_of_directrix_eq_top`, part 1 is `Singularity.logJacobianDirectrixCodim_eq_zero_of_order_eq_zero`, part 2 is `Singularity.one_le_logJacobianDirectrixCodim_of_caseA`, and part 3 is `Singularity.kangarooPath_of_codim_le_one`.

### Notes and references

The kangaroo points are from [Hau10]. The order of the invariant of Hironaka is from [Hir67]. The use of the history of the components of the divisor is from [CJS20], and Section 3.10 shows that its simplest form does not apply to the triple. Proposition 3.11.1, Example 3.11.2, Conjecture 3.11.3, Lemma 3.11.4, Proposition 3.11.5 and Example 3.11.6 are a result of the milestone S7.17 of this project. Volume 9, Section 3.13 gives the result as a research report.
