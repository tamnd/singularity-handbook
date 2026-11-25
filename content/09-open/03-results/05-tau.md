---
title: The codimension of the directrix of the log-Jacobian order
nodes: [SG0000004Z]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The codimension of the directrix of the log-Jacobian order

This section reports the fifth research result of the milestone S7. It is the second step toward the open step of the route of the purely inseparable equations in Section 2.3, after Section 3.4. Volume 7, Section 3.8, gives the same result with all the details.

### The problem

Section 3.4 gives a linear subspace $T_\rho(g)$ that contains the vectors of the points where the residual order $\rho$ of the log-Jacobian ideal stays under a point blowup. In the theory of Hironaka, the next entry of the invariant after the order is the codimension $\tau$ of the directrix, and it does not go down at the points where the order stays. The question of this section is: does the codimension $\tau_\rho(g) = n - \dim T_\rho(g)$ go down at the points where $\rho$ stays?

### The result

We use the setting of Volume 7, Section 3.8. The point is in the first case if $\operatorname{ord} \widetilde\Theta_0(G) = \rho$, and in the second case if $\operatorname{ord} \widetilde\Theta_0(G) = \rho + 1$. The subspace $T_\rho(g)$ is the intersection of the directrices of the initial forms of the elements of order $\rho$ of $\widetilde\Theta_0(G)$ in the first case and of $\widetilde\Theta(G)$ in the second case.

**Theorem 3.5.1.** Assume that $\rho(g'_c) = \rho(g)$.

1. If the new point is in the second case, then $\tau_\rho(g'_c) \ge \tau_\rho(g)$.
2. If the old point is in the second case and the new point is in the first case, then $\tau_\rho(g'_c) < \tau_\rho(g)$ can occur. For $p = 2$, $g = x y z^2 + y^2 z + x z^2$ and $E = \emptyset$, the value of $\tau_\rho$ goes from $2$ to $1$ at the origin of the $x$-chart, and $\rho = 2$ stays.

Node: SG0000004Z · Lean: `Singularity.logJacobianDirectrixCodim_le_cleanPart` (part 1, for polynomials)

### The proof

Part 1. Let $h$ be an element of the definition of $T_\rho(g)$, and let $h'$ be its weak transform. The proof of Volume 7, Theorem 3.7.1, shows that $h'$ has order $\rho$ and is in $\widetilde\Theta(G')$. Since the new point is in the second case, $h'$ is an element of the definition of $T_\rho(g'_c)$. The restriction of $\operatorname{in}(h')$ to $x_1 = 0$ is $\operatorname{in}(h)(0, x_2, \dots, x_n)$, because the vector $v$ of the chart is in $T(\operatorname{in}(h))$. From this, each vector of $T_\rho(g'_c)$ with first coordinate $0$ is in $T_\rho(g)$. Since $v \in T_\rho(g)$ has first coordinate $1$, a count of dimensions gives $\dim T_\rho(g'_c) \le \dim T_\rho(g)$.

Part 2. Volume 7, Example 3.8.3, computes the generators of the two ideals. At the old point the initial forms of order $2$ are the combinations of $y^2$ and $z^2$, so $T_\rho(g)$ is a line. At the new point only $z^2$ remains, because the weak transform $y^2$ of $\partial_z G$ is not in $\widetilde\Theta_0(G')$, so $T_\rho(g'_c)$ is a plane.

### The Lean proof

The Lean library proves both parts for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianDirectrix.lean`. Part 1 is `Singularity.logJacobianDirectrixCodim_le_cleanPart`, and part 2 is `Singularity.tauRhoExample_cases` and `Singularity.tauRhoExample_finrank`.

### What the result does not give

1. It does not say that $\rho$ goes down. Since $\tau_\rho$ can go down from the second case to the first case, the pair $(\rho, -\tau_\rho)$ can go up, and it is not a resolution invariant. An invariant that compares the case before $\tau_\rho$ also fails, because at the points where $\rho$ stays the case can change in both directions.
2. It does not cover the cases from the first to the first. Section 3.6 proves that $\tau_\rho$ does not go down in these cases when $p$ does not divide $|r| + d$. The case where $p$ divides $|r| + d$ is open.
3. It is for point blowups only, as the result of Section 3.4.

### Status

The map gives SG0000004Z the status of a node with a Lean proof of both parts. An outside expert has not yet read the result, and the milestone S7 asks for this. The proof uses only the theorem of Section 3.4 and the method of Hironaka for $\tau$. We do not know a published statement of it.

### Notes and references

The codimension of the directrix and the theorem that it does not go down at the points where the order stays are from [Hir67].
