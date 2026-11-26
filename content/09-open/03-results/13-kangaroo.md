---
title: The kangaroo path
nodes: [SG0000005B, SG0000005C, SG0000005D]
sources: [Hir67, Hau10, CJS20]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The kangaroo path

This section reports the thirteenth research result of the milestone S7. It studies the sequences of steps that leave the first case at a kangaroo point and come back to the first case. It proves that $\tau_\rho$ does not go down along the points of the second case, it gives an example where $\tau_\rho$ goes down at the step back to the first case, and it states a conjecture for the whole path. Volume 7, Section 3.11, gives the same result with all the details.

### The problem

By Section 3.12, at the points where $\rho$ stays, the triple $(\rho, d, \tau_\rho)$ can get worse only at a step with a leaving component, from a point of the first case where $p$ divides $|r| + d$. At such a step the new point can be in the second case, with $d$ one larger. This is a kangaroo point of Hauser. The sequence of points after it can stay in the second case for some steps, and then come back to the first case, with $d$ one smaller. A reader can ask if the triple at the point of return is at least as good as the triple at the start.

### The result

We use the setting of Volume 7, Sections 3.8 to 3.10. So $g = x^r G$ is clean, $d = \operatorname{ord} G$, and $\rho = \rho(g)$. The first case is $d = \rho$, and the second case is $d = \rho + 1$. A *kangaroo path* is a sequence of points $P_0, P_1, \dots, P_m$ with $m \ge 2$, where each $P_{i+1}$ is a point of a chart of the blowup of $P_i$ with $\rho(P_{i+1}) = \rho(P_i)$, where $P_0$ and $P_m$ are in the first case, and where $P_1, \dots, P_{m-1}$ are in the second case.

**Proposition 3.13.1.** Let $P_0, P_1, \dots, P_m$ be a sequence of points as in a kangaroo path, but with no hypothesis on the case of $P_0$ and of $P_m$. Then
$$\tau_\rho(P_0) \le \tau_\rho(P_1) \le \dots \le \tau_\rho(P_{m-1}) \le \widetilde\tau(P_m).$$

Node: SG0000005B · Lean: `Singularity.logJacobianDirectrixCodim_le_fullDirectrixCodim_of_reflTransGen` (for polynomials)

**Example 3.13.2.** Let $p = 2$, $\Delta = \{x, z\}$ and $g = x^3 z + x z^3 + x^4 y z$, as in Volume 7, Example 3.11.2. Then $P_0$ is in the first case with $\rho = 2$ and $\tau_\rho = 1$. A chart in the direction $x$ with $t_y = t_z = 1$ gives a point $P_1$ of the second case with $\tau_\rho = 2$, and the component $z = 0$ leaves. The chart in the direction $y$ at the origin gives a point $P_2$ of the first case with $\tau_\rho = 1$. So $\tau_\rho$ goes $1, 2, 1$, and $\widetilde\tau(P_2) = 2$. The directrices $T_\rho(P_0) = \{a_x = a_z\}$ and $T_\rho(P_2) = \{a_x = 0\}$ are different planes.

Node: SG0000005C

**Conjecture 3.13.3.** Let $P_0, P_1, \dots, P_m$ be a kangaroo path. Then $\tau_\rho(P_m) \ge \tau_\rho(P_0)$.

Node: SG0000005D · Lean: `Singularity.KangarooPathConjecture` (the statement only)

### The proof in short

The proof of Volume 7, Proposition 3.8.2, transports each element of $H(g)$ to the new point. It uses two hypotheses: $\rho$ stays, and the new point is in the second case. It does not use the case of the old point, and it does not use the hypothesis that no component leaves, since the new divisor is the divisor of the chart in each case. So it applies at each step from $P_i$ to $P_{i+1}$ with $i + 1 \le m - 1$, and an induction gives the first $m - 1$ inequalities. At the last step, the transport lands in $\widetilde\Theta(G')$, and the full directrix $\widetilde T$ is made from all of $\widetilde\Theta(G')$. So the same dimension argument gives $\widetilde\tau(P_m) \ge \tau_\rho(P_{m-1})$.

The conjecture does not follow, since $\tau_\rho(P_m) \le \widetilde\tau(P_m)$ and the two numbers can be different at a point of the first case. In Example 3.13.2, the old form $(x + z)^2$ of $P_0$ is still at $P_2$. It is the initial form of the free derivative $\partial_z G_2$, so it is in $\widetilde\Theta(G_2)$ but not in $\widetilde\Theta_0(G_2)$. So a proof of the conjecture cannot transport the forms of $P_0$ into $H(P_m)$, as the proofs of Volume 7, Proposition 3.8.2 and Theorem 3.9.11, do.

### The test data

Random tests followed sequences of point blowups at the points where $\rho$ stays, from random clean $g$ with random divisors.

1. A test compared $\tau_\rho$ at consecutive points of the first case in one sequence, in 3,250 sequences with $(p, n) = (2, 3), (2, 4), (3, 3)$ and $(5, 3)$. There were 7,092 comparisons, and 249 of them were on a kangaroo path. In none of them did $\tau_\rho$ go down.
2. A test recorded the last step of each kangaroo path, in 1,500 sequences with $(p, n) = (2, 3)$ and 1,000 sequences with $(p, n) = (3, 3)$. There were 158 such steps. At 26 of them $\tau_\rho$ went down at the last step, and at each of these 26 steps it went down to exactly $\tau_\rho(P_0)$.
3. A test transported the generators of order $\rho$ of $\widetilde\Theta_0(G)$ at $P_0$ along the path. Their parts of degree $\rho$ at $P_m$ were in the span of the forms of $H(P_m)$ on 149 of 152 kangaroo paths. On the other 3 paths the transport failed as in Example 3.13.2, but the conjecture held all the same.

### What the result means

If the conjecture holds, then a kangaroo path does not make the triple worse from $P_0$ to $P_m$. The value of $\rho$ is the same, $d(P_m) = \rho = d(P_0)$, and $\tau_\rho$ does not go down. So the last row of the table of Section 3.12 can be replaced by a whole kangaroo path, and the triple does not get worse along it. The only remaining steps where the triple can get worse are the steps of the row before it: both points are in the first case, a component leaves, and $\tau_\rho$ goes down, as in Volume 7, Examples 3.9.5 and 3.9.6. The hypothesis $m \ge 2$ is necessary for this reason.

The tests show a pattern that a proof can use. At each drop at the last step, $\tau_\rho$ goes back to exactly its value at $P_0$, and the gain along the points of the second case is lost. This suggests that the dimension of $T_\rho(P_m)$ is controlled by the forms of $P_0$, and not by the forms of $P_{m-1}$, even when the forms of $P_0$ do not transport into $H(P_m)$.

### Status

The map gives SG0000005B the status "proved" and SG0000005D the status "open". The map gives SG0000005C the status "planned", since the example is checked by hand and by a test, but not yet by a Lean computation. The Lean library proves Proposition 3.13.1 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianKangaroo.lean`, and it states Conjecture 3.13.3 as `Singularity.KangarooPathConjecture`. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The kangaroo points are from [Hau10]. The order of the invariant of Hironaka is from [Hir67]. The use of the history of the components of the divisor is from [CJS20]. Proposition 3.13.1, Example 3.13.2 and Conjecture 3.13.3 are a result of the milestone S7.17 of this project.
