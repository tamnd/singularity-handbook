---
title: The codimension from the first case to the first case
nodes: [SG00000050]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The codimension from the first case to the first case

This section reports the sixth research result of the milestone S7. It is the third step toward the open step of the route of the purely inseparable equations in Section 2.3, after Sections 3.4 and 3.5. Volume 7, Section 3.9, gives the same result with all the details.

### The problem

Section 3.5 proves that the codimension $\tau_\rho$ of the directrix of the log-Jacobian order does not go down at a point where $\rho$ stays, if the new point is in the second case. It also shows that $\tau_\rho$ can go down from the second case to the first case. This leaves the combination from the first case to the first case. Section 3.5 transports each element of the definition of $T_\rho(g)$ to the new point. In the first case at the new point, the weak transform of an element need not be an element of the new definition, so the method of Section 3.5 does not apply.

### The result

We use the setting of Volume 7, Section 3.9. So $g = x^r G$, $d = \operatorname{ord} G$, $F = \operatorname{in}(G)$, and $v = (1, t_2, \dots, t_n)$ is the vector of the chart.

**Theorem 3.6.1.** Assume that $\rho(g'_c) = \rho(g)$, that the old point and the new point are both in the first case, and that $p$ does not divide $|r| + d$. Then $\tau_\rho(g'_c) \ge \tau_\rho(g)$.

Node: SG00000050 · Lean: `Singularity.logJacobianDirectrixCodim_le_cleanPart_of_caseA` (for polynomials)

### The proof

In the first case, and when $p$ does not divide $|r| + d$, the value of $\rho$ is $d$. The initial forms of the elements of order $\rho$ of $\widetilde\Theta_0(G)$ are the nonzero linear combinations of the forms $\Phi_i = r_i F + x_i \partial_i F$ for $i \in \Delta$. So $T_\rho(g)$ is the intersection of the directrices of the nonzero $\Phi_i$.

The proof divides the indices $i \in \Delta$ in two groups.

1. If $v_i = 0$, the derivation $x_i \partial_i$ of the old point gives the derivation $x_i \partial_i$ of the new point. So the weak transform of $r_i G + x_i \partial_i G$ is an element of $\widetilde\Theta_0(G')$, and the argument of Section 3.5 applies to it.
2. If $v_i \ne 0$, the weak transform is not exact. But the vector $v$ is in the directrix of $F$ and of $\Phi_i$, so the derivative of $F$ and of $\Phi_i$ along $v$ is $0$. A short computation then gives $\partial_i F = 0$ and $\Phi_i = r_i F$. The Euler element $|r| G + \sum_k x_k \partial_k G$ has the initial form $(|r| + d) F$, and the Euler derivation of the old point gives the derivation $x_1 \partial_1$ of the new point. So its weak transform is exact, and the argument of Section 3.5 applies to $F$, so also to $\Phi_i$.

So each vector of $T_\rho(g'_c)$ with first coordinate $0$ is in $T_\rho(g)$, and the count of dimensions of Section 3.5 gives the theorem.

### An example

For $p = 2$, $g = x z^2 + x^2 y^3$ and $\Delta = \{x\}$, the point is in the first case with $\rho = 2$ and $T_\rho(g) = T(z^2)$. In the $y$-chart at the point with $t_x = 1$, the value of $\rho$ stays, the new point is in the first case, and $T_\rho(g'_c) = T((z + y)^2)$. The weak transform of $G + x \partial_x G = z^2$ is $z^2$, and it is not an element of the new definition. So the method of Section 3.5 does not apply. The Euler element is $G$, and its weak transform gives the new form $(z + y)^2$. Both values of $\tau_\rho$ are $1$.

### The Lean proof

The Lean library proves the theorem and the example for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianDirectrixCaseA.lean`. The theorem is `Singularity.logJacobianDirectrixCodim_le_cleanPart_of_caseA`, and the example is `Singularity.tauRhoCaseAExample_hyp` and `Singularity.tauRhoCaseAExample_not_mem`. The Lean theorem assumes $\rho = d$ in the place of the first case at the old point. If $p$ does not divide $|r| + d$, the Euler element shows that the two hypotheses are equivalent.

### What the result does not give

1. It does not cover the case where $p$ divides $|r| + d$. Then the proof has no element with the initial form $F$, and Section 3.7 shows that the theorem is then false.
2. It does not say that $\rho$ goes down. Since $\tau_\rho$ can go down from the second case to the first case, the pair $(\rho, -\tau_\rho)$ is still not a resolution invariant.
3. It is for point blowups only, as the results of Sections 3.4 and 3.5.

### Status

The map gives SG00000050 the status of a node with a Lean proof. An outside expert has not yet read the result, and the milestone S7 asks for this. The proof uses only Sections 3.4 and 3.5 and the Euler identity. We do not know a published statement of it.

### Notes and references

The codimension of the directrix and the theorem that it does not go down at the points where the order stays are from [Hir67].
