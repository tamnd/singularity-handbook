---
title: The kangaroo path
nodes: [SG0000005B, SG0000005C, SG0000005D]
sources: [Hir67, Hau10, CJS20]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The kangaroo path

Section 3.10 shows that at the points where $\rho$ stays, the triple $(\rho, d, \tau_\rho)$ can get worse only at a step with a leaving component, from a point of the first case where $p$ divides $|r| + d$. At such a step the new point can be in the second case, with $d$ one larger, as at the kangaroo points of Example 3.2.6. In this section we follow the sequence after a kangaroo point. It goes through points of the second case, and it can come back to the first case. We show that $\tau_\rho$ does not go down along the points of the second case, and that the full form $\widetilde\tau$ of Section 3.8 at the point of return is at least $\tau_\rho$ at the start. We state the conjecture that $\tau_\rho$ itself is at least its value at the start, we give the tests, and we give an example that shows why a simple proof does not work.

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

Node: SG0000005D · Lean: `Singularity.KangarooPathConjecture` (the statement only)

If the conjecture holds, then a kangaroo path does not make the triple worse from $P_0$ to $P_m$: the value of $\rho$ is the same, $d(P_m) = \rho = d(P_0)$, and $\tau_\rho$ does not go down. Then the only remaining steps where the triple gets worse are the steps of the second kind of Section 3.10: both points are in the first case, a component leaves, and $\tau_\rho$ goes down, as in Examples 3.9.5 and 3.9.6.

The hypothesis $m \ge 2$ is necessary. For $m = 1$ the path is one step from the first case to the first case, and Examples 3.9.5 and 3.9.6 are steps of this kind where $\tau_\rho$ goes down.

### What a random test found

Random tests followed sequences of point blowups at the points where $\rho$ stays, from random clean $g$ with random divisors.

1. A test compared $\tau_\rho$ at consecutive points of the first case in one sequence, in 3,250 sequences with $(p, n) = (2, 3), (2, 4), (3, 3)$ and $(5, 3)$. There were 7,092 comparisons, 249 of them on a kangaroo path. In none of them did $\tau_\rho$ go down.
2. A test recorded, at each step from the second case to the first case, the start of the run of points of the second case before it. In 1,500 sequences with $(p, n) = (2, 3)$ and 1,000 sequences with $(p, n) = (3, 3)$, there were 158 such steps at the end of a kangaroo path. At 26 of them $\tau_\rho$ went down at the last step, and at each of these 26 steps it went down to exactly $\tau_\rho(P_0)$. So the gain along the points of the second case was lost at the last step, but $\tau_\rho$ did not go below its value at the start. At the steps from the second case to the first case where the run of points of the second case started at the start of the sequence, $\tau_\rho$ went down 32 times, as in Example 3.8.3.
3. A test transported the generators of order $\rho$ of $\widetilde\Theta_0(G)$ at $P_0$ along the path, and checked whether their parts of degree $\rho$ at $P_m$ are in the span of the forms of $H(P_m)$. This held on 149 of the 152 kangaroo paths of the runs with $(p, n) = (2, 3)$ and $(3, 3)$, and failed on 3 of them, as in Example 3.11.2. On these 3 paths the conjecture held all the same.

### The Lean proof

The Lean library proves Proposition 3.11.1 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianKangaroo.lean`. A step of a point blowup where $\rho$ stays $m$ is `Singularity.RhoStep`, and a point of the second case is `Singularity.IsLogJacobianCaseB`. A run of steps into points of the second case is the reflexive and transitive closure of the relation "a step into a point of the second case". `Singularity.logJacobianDirectrixCodim_le_of_reflTransGen` gives $\tau_\rho(P_0) \le \tau_\rho(P_{m-1})$, and `Singularity.logJacobianDirectrixCodim_le_fullDirectrixCodim_of_reflTransGen` gives $\tau_\rho(P_0) \le \widetilde\tau(P_m)$. The Lean statements have no hypothesis on the case of $P_0$ and of $P_m$. The proofs use the Lean form of Proposition 3.8.2 in `Singularity/Invariant/LogJacobianDirectrix.lean` and the bound $\tau_\rho(g) \le \widetilde\tau(g'_c)$ in `Singularity/Invariant/LogJacobianFullDirectrix.lean`.

### Notes and references

The kangaroo points are from [Hau10]. The order of the invariant of Hironaka is from [Hir67]. The use of the history of the components of the divisor is from [CJS20], and Section 3.10 shows that its simplest form does not apply to the triple. Proposition 3.11.1, Example 3.11.2 and Conjecture 3.11.3 are a result of the milestone S7.17 of this project. Volume 9, Section 3.13 gives the result as a research report.
