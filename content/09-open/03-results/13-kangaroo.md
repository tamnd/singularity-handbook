---
title: The kangaroo path
nodes: [SG0000005B, SG0000005C, SG0000005D, SG0000005E, SG0000005F, SG0000005G]
sources: [Hir67, Hau10, CJS20]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The kangaroo path

This section reports the thirteenth research result of the milestone S7. It studies the sequences of steps that leave the first case at a kangaroo point and come back to the first case. It proves that $\tau_\rho$ does not go down along the points of the second case, it gives an example where $\tau_\rho$ goes down at the step back to the first case, and it states a conjecture for the whole path. It proves the conjecture if $\tau_\rho \le 1$ at the start, and it gives a counterexample with $\tau_\rho = 2$ at the start. So the conjecture is false. Volume 7, Section 3.11, gives the same result with all the details.

### The problem

By Section 3.12, at the points where $\rho$ stays, the triple $(\rho, d, \tau_\rho)$ can get worse only at a step with a leaving component, from a point of the first case where $p$ divides $|r| + d$. At such a step the new point can be in the second case, with $d$ one larger. This is a kangaroo point of Hauser. The sequence of points after it can stay in the second case for some steps, and then come back to the first case, with $d$ one smaller. A reader can ask if the triple at the point of return is at least as good as the triple at the start.

### The result

We use the setting of Volume 7, Sections 3.8 to 3.10. So $g = x^r G$ is clean, $d = \operatorname{ord} G$, and $\rho = \rho(g)$. The first case is $d = \rho$, and the second case is $d = \rho + 1$. A *kangaroo path* is a sequence of points $P_0, P_1, \dots, P_m$ with $m \ge 2$, where each $P_{i+1}$ is a point of a chart of the blowup of $P_i$ with $\rho(P_{i+1}) = \rho(P_i)$, where $P_0$ and $P_m$ are in the first case, and where $P_1, \dots, P_{m-1}$ are in the second case. We call $P_m$ the *point of return*.

**Proposition 3.13.1.** Let $P_0, P_1, \dots, P_m$ be a sequence of points as in a kangaroo path, but with no hypothesis on the case of $P_0$ and of $P_m$. Then
$$\tau_\rho(P_0) \le \tau_\rho(P_1) \le \dots \le \tau_\rho(P_{m-1}) \le \widetilde\tau(P_m).$$

Node: SG0000005B · Lean: `Singularity.logJacobianDirectrixCodim_le_fullDirectrixCodim_of_reflTransGen` (for polynomials)

**Example 3.13.2.** Let $p = 2$, $\Delta = \{x, z\}$ and $g = x^3 z + x z^3 + x^4 y z$, as in Volume 7, Example 3.11.2. Then $P_0$ is in the first case with $\rho = 2$ and $\tau_\rho = 1$. A chart in the direction $x$ with $t_y = t_z = 1$ gives a point $P_1$ of the second case with $\tau_\rho = 2$, and the component $z = 0$ leaves. The chart in the direction $y$ at the origin gives a point $P_2$ of the first case with $\tau_\rho = 1$. So $\tau_\rho$ goes $1, 2, 1$, and $\widetilde\tau(P_2) = 2$. The directrices $T_\rho(P_0) = \{a_x = a_z\}$ and $T_\rho(P_2) = \{a_x = 0\}$ are different planes.

Node: SG0000005C

**Conjecture 3.13.3.** Let $P_0, P_1, \dots, P_m$ be a kangaroo path. Then $\tau_\rho(P_m) \ge \tau_\rho(P_0)$.

Node: SG0000005D · Lean: `Singularity.KangarooPathConjecture` (the statement only)

**Lemma 3.13.4.** Let $g = x^r G$ be in the first case, and let $F$ be the part of degree $\rho$ of $G$. For $i \in \Delta$ put $E_i F = r_i F + x_i \partial_i F$. Then $T_\rho(g) = \bigcap_{i \in \Delta} T(E_i F)$.

Node: SG0000005E · Lean: `Singularity.logJacobianDirectrix_eq_iInf_caseAForm`

**Proposition 3.13.5.** If $\rho = 0$, then $\tau_\rho = 0$. If $\rho \ge 1$ and $g$ is in the first case, then $\tau_\rho(g) \ge 1$. Thus Conjecture 3.13.3 holds for each kangaroo path with $\tau_\rho(P_0) \le 1$.

Node: SG0000005F · Lean: `Singularity.kangarooPath_of_codim_le_one`

**Example 3.13.6.** Let $p = 2$, $\Delta = \{y, z\}$ and $g_0 = x^2 y^3 z + x^2 y z^3 + x^4 y z^2$, as in Volume 7, Example 3.11.6. Then $P_0$ is in the first case with $\rho = 4$, and $T_\rho(P_0) = T(x^2 (y + z)^2) = \{a_x = 0, a_y = a_z\}$, so $\tau_\rho(P_0) = 2$. The chart in the direction $y$ with $t_x = 0$ and $t_z = 1$ gives a point $P_1$ of the second case with $g_1 = y^4 (x^2 z^3 + x^4 y + x^4 y z^2)$ and $\tau_\rho(P_1) = 2$, and the component $z = 0$ leaves. The chart in the direction $y$ at the origin gives a point $P_2$ of the first case with $g_2 = y^7 (x^4 + x^2 z^3 + x^4 y^2 z^2)$ and $\tau_\rho(P_2) = 1$. So $\tau_\rho(P_2) < \tau_\rho(P_0)$, and Conjecture 3.13.3 is false.

Node: SG0000005G

### The proof in short

The proof of Volume 7, Proposition 3.8.2, transports each element of $H(g)$ to the new point. It uses two hypotheses: $\rho$ stays, and the new point is in the second case. It does not use the case of the old point, and it does not use the hypothesis that no component leaves, since the new divisor is the divisor of the chart in each case. So it applies at each step from $P_i$ to $P_{i+1}$ with $i + 1 \le m - 1$, and an induction gives the first $m - 1$ inequalities. At the last step, the transport lands in $\widetilde\Theta(G')$, and the full directrix $\widetilde T$ is made from all of $\widetilde\Theta(G')$. So the same dimension argument gives $\widetilde\tau(P_m) \ge \tau_\rho(P_{m-1})$.

The conjecture does not follow, since $\tau_\rho(P_m) \le \widetilde\tau(P_m)$ and the two numbers can be different at a point of the first case. In Example 3.13.2, the old form $(x + z)^2$ of $P_0$ is still at $P_2$. It is the initial form of the free derivative $\partial_z G_2$, so it is in $\widetilde\Theta(G_2)$ but not in $\widetilde\Theta_0(G_2)$. So a proof of the conjecture cannot transport the forms of $P_0$ into $H(P_m)$, as the proofs of Volume 7, Proposition 3.8.2 and Theorem 3.9.11, do.

Proposition 3.13.5 uses that a form $F$ of positive degree with $T(F) = K^n$ is $0$. For each $i$, the substitution $s \mapsto x_i$, $x_i \mapsto 0$ in the identity $F(x + s e_i) = F(x)$ gives $F = F|_{x_i = 0}$. This holds over each field. In the first case $\Theta_0(g)$ has an element $x^r \psi$ of order $|r| + \rho$, and then $\psi_\rho$ is such a form, with $T_\rho(g) \subseteq T(\psi_\rho)$.

In Example 3.13.6, the form of degree $4$ at $P_1$ is $x^2 z^2 = \operatorname{in}(\partial_z G_1)$, and it comes from a free derivative. The monomial $x^4 y$ of $G_1$ has degree $5$. At the blowup at the origin of the $y$-chart, the exponent of $y$ in this monomial of $g$ grows by $2$, and $r_y$ grows by $3$. So at $P_2$ the monomial is $x^4$, of degree $4$, and the point goes back to the first case. In the first case the free derivatives do not count in $T_\rho$, so the form $x^2 z^2$ is lost. It is still in $\widetilde\Theta(G_2)$, so $\widetilde\tau(P_2) = 2$, as Proposition 3.13.1 requires.

### The test data

Random tests followed sequences of point blowups at the points where $\rho$ stays, from random clean $g$ with random divisors.

1. A test compared $\tau_\rho$ at consecutive points of the first case in one sequence, in 3,250 sequences with $(p, n) = (2, 3), (2, 4), (3, 3)$ and $(5, 3)$. There were 7,092 comparisons, and 249 of them were on a kangaroo path. In none of them did $\tau_\rho$ go down.
2. A test recorded the last step of each kangaroo path, in 1,500 sequences with $(p, n) = (2, 3)$ and 1,000 sequences with $(p, n) = (3, 3)$. There were 158 such steps. At 26 of them $\tau_\rho$ went down at the last step, and at each of these 26 steps it went down to exactly $\tau_\rho(P_0)$.
3. A test transported the generators of order $\rho$ of $\widetilde\Theta_0(G)$ at $P_0$ along the path. Their parts of degree $\rho$ at $P_m$ were in the span of the forms of $H(P_m)$ on 149 of 152 kangaroo paths. On the other 3 paths the transport failed as in Example 3.13.2, but the conjecture held all the same.
4. On the 128 kangaroo paths of a run with $(p, n) = (2, 3)$, each start had $\tau_\rho(P_0) \le 1$. So by Proposition 3.13.5 the tests 1 to 3 did not test the conjecture in the case where it has content.
5. A test started only at points of the first case with $p \mid |r| + d$ and $\tau_\rho(P_0) \ge 2$. With $(p, n) = (2, 3)$ there were 337 such starts and 58 first steps into the second case, and the test found 2 kangaroo paths where $\tau_\rho$ goes down from $2$ to $1$. They start at the same point, and one is the other with the roles of $y$ and $z$ exchanged. With $(p, n) = (3, 3)$ there were 568 such starts and 16 first steps into the second case, and no path came back to the first case.

### What the result means

Conjecture 3.13.3 was the hope that a kangaroo path does not make the triple worse from $P_0$ to $P_m$. Example 3.13.6 shows that this is false. Along the path the triple $(\rho, d, \tau_\rho)$ goes from $(4, 4, 2)$ to $(4, 5, 2)$ and then to $(4, 4, 1)$. Section 3.12 gives a table of the steps where the triple can get worse, and its last row is the first step of a kangaroo path. The hope was to remove this row with a look at the whole path. The example shows that this does not work with the triple as the invariant: the triple at the end of the path is worse than at the start.

The example also shows where the triple loses information. In the first case the triple uses $T_\rho$, which is made from $\widetilde\Theta_0(G)$ only. In the second case it uses $\widetilde\Theta(G)$, which also has the free derivatives $\partial_l G$ for $l \notin \Delta$. A form of a free derivative counts at the points of the second case, and it does not count at the point of return. The full form $\widetilde\tau$ keeps it, and by Proposition 3.13.1 the full form at the point of return is at least $\tau_\rho$ at the start.

The full form does not repair the triple. In Volume 7, Example 3.11.6, the next point $P_3$ after the point of return is the only point of the blowup of $P_2$ with $\rho = 4$, and there $\tau_\rho(P_3) = \widetilde\tau(P_3) = 1$. So an invariant made only from $\rho$, $d$ and one of $\tau_\rho$ and $\widetilde\tau$ at the point gets worse from $P_0$ to $P_3$. An invariant that is good on this path must use other data. This suggests three directions for the next work.

1. Put the condition $p \mid |r| + d$ before $\tau_\rho$. The start $P_0$ has $p \mid |r| + d$, and $P_3$ has $|r| + d = 13$, which is odd. An invariant that counts a point of the first case with $p \mid |r| + d$ as worse than the other points of the first case gets better from $P_0$ to $P_2$ and to $P_3$. The open question is whether it gets worse at other steps.
2. Add the history of the path to the invariant, as in [CJS20]. At the point of return, the leaving component and the number of steps in the second case are known, and an invariant can use them.
3. Find a different second entry for the invariant, in place of $d$, that does not change at the first step of a kangaroo path. In the example the monomial $x^4 y^b$ of $g$ controls the return to the first case, and its degree in $G$ goes down by $1$ at each step from a point of the second case.

Lemma 3.13.4 stays useful for each of these directions. At a point of the first case, $T_\rho$ depends only on $F = \operatorname{in}(G)$, on $r$ and on $\Delta$. If $g$ is clean, write $F_\chi$ for the part of $F$ with the character $\chi(\alpha) = (r_i + \alpha_i \bmod p)_{i \in \Delta}$. Then $E_i F = \sum_\chi \chi_i F_\chi$, and $T_\rho(g)$ contains the joint directrix of the $F_\chi$ (Volume 7, Section 3.11).

### Status

The map gives SG0000005B the status "proved". The map gives SG0000005D the status "open", since the map has no status for a false statement, and the statement and the notes of SG0000005D say that it is false. The map gives SG0000005G the status "planned", since the counterexample is checked by hand and by a test, but not yet by a Lean computation. The map gives SG0000005C the status "planned", since the example is checked by hand and by a test, but not yet by a Lean computation. The Lean library proves Proposition 3.13.1 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianKangaroo.lean`, and it states Conjecture 3.13.3 as `Singularity.KangarooPathConjecture`, with no proof. A Lean proof of the negation for $p = 2$ and three variables is not done yet. It proves Lemma 3.13.4 in `Singularity/Invariant/LogJacobianCaseAForms.lean`, with no hypothesis on the field, and the map gives SG0000005E the status "proved". It proves Proposition 3.13.5 in `Singularity/Invariant/LogJacobianKangarooSmall.lean`, and the map gives SG0000005F the status "proved". An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The kangaroo points are from [Hau10]. The order of the invariant of Hironaka is from [Hir67]. The use of the history of the components of the divisor is from [CJS20]. Proposition 3.13.1, Example 3.13.2, Conjecture 3.13.3, Lemma 3.13.4, Proposition 3.13.5 and Example 3.13.6 are a result of the milestone S7.17 of this project.
