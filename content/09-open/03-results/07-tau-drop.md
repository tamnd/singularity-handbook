---
title: The codimension can go down from the first case to the first case
nodes: [SG00000051]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The codimension can go down from the first case to the first case

This section reports the seventh research result of the milestone S7. It answers the question that Section 3.6 left open, and the answer is negative. Volume 7, Section 3.9, gives the same result with all the details.

### The problem

Theorem 3.6.1 proves that the codimension $\tau_\rho$ of the directrix of the log-Jacobian order does not go down at a point where $\rho$ stays and both points are in the first case, if $p$ does not divide $|r| + d$. The proof uses the Euler element $|r| G + \sum_k x_k \partial_k G$, which has the initial form $(|r| + d) F$. If $p$ divides $|r| + d$, the proof has no element with the initial form $F$ and an exact weak transform. The question was if the theorem is true also in this case.

### The result

We use the setting of Volume 7, Section 3.9.

**Example 3.7.1.** Let $p = 2$, $n = 5$ with the variables $x, y, z, w, u$, $\Delta = \{x, y, z, w\}$ and
$$g = x z^2 w u^2 + x y z w u^2.$$
Then $\rho = 3$, $|r| + d = 6$, the point is in the first case, and $\tau_\rho(g) = 3$. In the $w$-chart at the point with $t_x = 1$, the value of $\rho$ stays, the new point is in the first case, and $\tau_\rho(g'_c) = 2$.

Node: SG00000051 · Lean: `Singularity.tauRhoDropExample_codim`

So the hypothesis that $p$ does not divide $|r| + d$ in Theorem 3.6.1 is necessary. Example 3.9.6 of Volume 7 gives a second example, with $n = 4$ and three monomials.

### The example

Here $x^r = x z w$, $G = (y + z) u^2$, and $d = 3$. In characteristic $2$ the elements $r_i G + x_i \partial_i G$ are $G$ for $i = x, w$ and $y u^2$ for $i = y, z$, and $\partial_u G = 0$. So the forms of the first case are $(y + z) u^2$ and $y u^2$, and $T_\rho(g) = \{a_y = a_z = a_u = 0\}$. The Euler element is $6 G = 0$.

The chart is $\pi(x) = w (x + 1)$ and $\pi(x_k) = w x_k$ for the other variables. Then $g' = w^4 (x + 1)(z^2 + y z) u^2$. The clean part drops the square monomial $w^4 z^2 u^2$, so
$$G' = x z u^2 + (x + 1) y u^2, \qquad \Delta' = \{y, z, w\}.$$
The elements of the new point are $(x + 1) y u^2$ for $i = y, z$ and $0$ for $i = w$. The derivative $\partial_x G' = (y + z) u^2$ has order $3$, so $\rho' = 3$, but it is in $\widetilde\Theta(G')$ and not in $\widetilde\Theta_0(G')$. So the new point is in the first case with the only form $y u^2$, and $T_\rho(g'_c) = \{a_y = a_u = 0\}$.

### What the result means

The form $F = (y + z) u^2$ of the old point comes only from the indices $x$ and $w$, with $v_x = v_w = 1$. Theorem 3.6.1 handles these indices with the Euler element, and here the Euler element is $0$. At the new point the form $F$ is still there, as the initial form of $\partial_x G'$. But the direction $x$ left the divisor, and in the first case the definition of $T_\rho$ uses only $\widetilde\Theta_0(G')$, so it does not see this form.

1. The pair $(\rho, -\tau_\rho)$ is not a resolution invariant, also when both points are in the first case. Section 3.5 shows the same from the second case to the first case.
2. A definition of $T_\rho$ with $\widetilde\Theta(G)$ also in the first case does not help. A random test for $p = 2, 3$ and $n = 3, 4, 5$ found many points where this form of $\tau$ goes down from the first case to the first case, also when $p$ does not divide $|r| + d$.
3. The drop is rare. For $p = 2$ and $n = 3$, a test found no drop at 6,290 points of this kind. We do not know if there is an example with $n = 3$.

So route R1 needs a secondary invariant that sees the forms of the derivatives $\partial_l G$ in the directions that leave the divisor, but that does not go down when these derivatives have no exact transport. We do not know such an invariant.

### Status

The map gives SG00000051 the status of a counterexample with a Lean proof. The Lean library proves Example 3.7.1 over $\mathbb{F}_2$ with the standard axioms only, in `Singularity/Invariant/LogJacobianDirectrixDrop.lean`. The data are `Singularity.tauRhoDropExample_hyp`, the two cases are `Singularity.tauRhoDropExample_cases`, and the two values of $\tau_\rho$ are `Singularity.tauRhoDropExample_codim`. An outside expert has not yet read the result, and the milestone S7 asks for this. We do not know a published statement of it.

### Notes and references

The codimension of the directrix and the theorem that it does not go down at the points where the order stays are from [Hir67]. Example 3.7.1 is a result of the milestone S7.11 of this project.
