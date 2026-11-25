---
title: The first case is stable
nodes: [SG00000052, SG00000053]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The first case is stable

This section reports the eighth research result of the milestone S7. It removes the hypothesis on the new point from Theorem 3.6.1, and it gives a map of the combinations of the cases where $\tau_\rho$ can go down. Volume 7, Section 3.9, gives the same result with all the details.

### The problem

Theorem 3.6.1 proves that $\tau_\rho$ does not go down at a point where $\rho$ stays, if both points are in the first case and $p$ does not divide $|r| + d$. A reader can ask if the new point can be in the second case in this situation. If yes, then Theorem 3.6.1 does not cover all the steps from the first case.

### The result

We use the setting of Volume 7, Section 3.9.

**Proposition 3.8.1.** Assume that $\rho' = \rho$, that $g$ is in the first case, and that $|r| + d$ is not $0$ in $K$. Then $g'_c$ is in the first case.

Node: SG00000052 · Lean: `Singularity.idealOrd_logJacobianTangent_cleanPart_of_caseA`

**Corollary 3.8.2.** Assume that $\rho' = \rho$, that $g$ is in the first case, and that $|r| + d$ is not $0$ in $K$. Then $\tau_\rho(g'_c) \ge \tau_\rho(g)$.

Node: SG00000053 · Lean: `Singularity.logJacobianDirectrixCodim_le_cleanPart_of_ne_zero`

### The proof in short

The Euler element $e = |r| G + \sum_k x_k \partial_k G$ has order $d$, since its initial form is $(|r| + d) F$. The chart sends $x^r e$ to $x_1^p \, x_1 \partial_1 g'$, and the derivation $x_1 \partial_1$ is logarithmic for the new divisor. So $x_1 \partial_1 g'$ is an element of $\Theta'_0(g'_c)$. It is equal to $u \, x^b e'$, with a unit $u$, the weak transform $e'$ of order at most $d$, and a monomial $x^b$ with $b \le r'$. So $\Theta'_0(g'_c)$ has an element of order at most $|r'| + d$, and $\sigma' \le d = \rho'$. The corollary follows from Theorem 3.6.1.

### The map of the combinations

At a point where $\rho$ stays, the old point and the new point are each in the first or the second case. In the first case we also ask if $p$ divides $|r| + d$. The table gives the answer for each combination. The word "stays" means that $\tau_\rho$ does not go down.

| Old point | New point | $\tau_\rho$ | Reference |
|---|---|---|---|
| second case | second case | stays | Volume 7, Proposition 3.8.2 |
| first case, $p \mid \lvert r \rvert + d$ | second case | stays | Volume 7, Proposition 3.8.2 |
| first case, $p \nmid \lvert r \rvert + d$ | second case | no such step | Proposition 3.8.1 |
| first case, $p \nmid \lvert r \rvert + d$ | first case | stays | Corollary 3.8.2 |
| second case | first case | can go down | Section 3.5 |
| first case, $p \mid \lvert r \rvert + d$ | first case | can go down | Section 3.7 |

A random test of sequences of at most four point blowups for $(p, n) = (2, 3), (2, 4)$ and $(3, 3)$ agrees with the table. It found 5,961, 1,403 and 2,288 steps from the first case with $p \nmid |r| + d$, and each one goes to the first case with no drop of $\tau_\rho$. It found 93, 49 and 43 drops from the second case to the first case, and 2 drops from the first case to the first case with $p \mid |r| + d$, both for $(p, n) = (2, 4)$.

### What the result means

The drops of $\tau_\rho$ occur in two combinations only, and both have a new point in the first case. In both, a form of the old point comes from the direction of the chart, and the new point does not see it, because the definition of the first case uses only $\widetilde\Theta_0(G')$.

The test also computed the form of $\tau$ with $\widetilde\Theta(G)$ in both cases. This form never went down from the second case. It went down at 502, 149 and 179 steps from the first case to the first case, also when $p$ does not divide $|r| + d$. So each of the two forms of $\tau$ goes down in a combination where the other form does not. So neither form of $\tau$ is a secondary invariant for route R1. A candidate is defined at one point, and it must not go down in any of the combinations of the table. The data of the test shows the steps that a candidate must handle, and this is the starting point of the search for it.

### Status

The map gives SG00000052 and SG00000053 the status "proved". The Lean library proves Proposition 3.8.1 and Corollary 3.8.2 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianCaseAStable.lean`. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The codimension of the directrix is from [Hir67]. Proposition 3.8.1 and Corollary 3.8.2 are a result of the milestone S7.12 of this project.
