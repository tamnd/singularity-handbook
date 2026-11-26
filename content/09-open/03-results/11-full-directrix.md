---
title: The full codimension does not go down from the second case
nodes: [SG00000057, SG00000058]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The full codimension does not go down from the second case

This section reports the eleventh research result of the milestone S7. It is about the first kind of drop of $\tau_\rho$ in Section 3.10, the steps from the second case to the first case. Volume 7, Section 3.8, gives the same result with all the details.

### The problem

The codimension $\tau_\rho$ of Section 3.5 uses the ideal $\widetilde\Theta_0(G)$ in the first case and the ideal $\widetilde\Theta(G)$ in the second case. So its definition changes at a step from the second case to the first case, and Volume 7, Example 3.8.3, shows that $\tau_\rho$ can go down at such a step. In that example the form that is lost is the initial form of an element of $\widetilde\Theta(G')$ that is not in $\widetilde\Theta_0(G')$. A reader can ask what happens if we keep these forms.

### The result

Let $\widetilde H(g)$ be the set of the elements of $\widetilde\Theta(G)$ of order $\rho$, in both cases. Let $\widetilde T(g)$ be the intersection of the subspaces $T(\operatorname{in}(h))$ for $h \in \widetilde H(g)$, and let $\widetilde\tau(g) = n - \dim \widetilde T(g)$ be the full codimension. In the second case $\widetilde\tau(g) = \tau_\rho(g)$, and in the first case $\widetilde\tau(g) \ge \tau_\rho(g)$.

**Theorem 3.11.1.** Assume that $\rho' = \rho$ and that $g$ is in the second case. Then $\widetilde\tau(g'_c) \ge \widetilde\tau(g) = \tau_\rho(g)$.

Node: SG00000057 · Lean: `Singularity.logJacobianFullDirectrixCodim_le_cleanPart`

**Example 3.11.2.** Let $p = 2$, $\Delta = \{x, z\}$ and $g = y z^2 + x z$. Then $g$ is in the first case, with $\tau_\rho(g) = 1$ and $\widetilde\tau(g) = 2$. At the origin of the $y$-chart, $g' = g$, $\Delta' = \{x, y, z\}$, $\rho$ stays, and the new point is in the first case with $\tau_\rho(g'_c) = 1$ and $\widetilde\tau(g'_c) = 1$.

Node: SG00000058 · Lean: `Singularity.fullDirectrixExample_codim`

### The proof in short

The proof of Theorem 3.5.1 shows that the weak transform $h'$ of each $h \in H(g)$ is an element of $\widetilde\Theta(G')$ of order $\rho$. This part of the proof does not use the case of the new point. The case of the new point is used only to put $h'$ in $H(g'_c)$, and with the full set $\widetilde H(g'_c)$ this step is not necessary. The rest of the proof is the count of dimensions of Hironaka. The proof also gives $\widetilde\tau(g'_c) \ge \tau_\rho(g)$ at each step where $\rho$ stays, in each case of the two points. The case of $g$ is used only for $\tau_\rho(g) = \widetilde\tau(g)$.

In the example, the element $\partial_y G = z$ is in $\widetilde H(g)$ because $y \notin \Delta$. At the new point $y$ is a component of the divisor, and only $y \partial_y$ is a generator. The weak transform $z$ is not in $\widetilde\Theta(G')$, and its form is lost. No component of $\Delta$ leaves at this step. The exceptional divisor is a new component, and the new component removes a derivation.

### The test data

A random test with random clean $g$ and random sequences of point blowups computed $\tau_\rho$ and $\widetilde\tau$ for $(p, n) = (2, 3), (2, 4)$ and $(3, 3)$. It found 48,399 steps from the second case where $\rho$ stays. At none of them does $\widetilde\tau$ go down. At the 447 of these steps where $\tau_\rho$ goes down, $\widetilde\tau$ stays the same or goes up. It found 2,105 steps from the first case where $\widetilde\tau$ goes down.

### What the result means

With Volume 7, Proposition 3.8.2, Corollary 3.9.8 and Theorem 3.9.11, we have this table for the steps where $\rho$ stays.

| Old point | New point | $\tau_\rho$ | $\widetilde\tau$ |
|---|---|---|---|
| second case | second case | does not go down | does not go down |
| second case | first case | can go down | does not go down |
| first case | second case | does not go down | can go down |
| first case, $p \nmid \lvert r \rvert + d$ | first case | does not go down | can go down |
| first case, no component leaves | first case | does not go down | can go down |
| first case, a component leaves | first case | can go down | can go down |

So $\tau_\rho$ does not go down from the first case, except in the last row, and $\widetilde\tau$ does not go down from the second case. But a secondary invariant must be a function of the point alone. After a step from the second case to the first case and a second step from the first case to the first case, the first step keeps $\widetilde\tau$ and the second step keeps $\tau_\rho$. At the middle point $\tau_\rho$ can be smaller than $\widetilde\tau$, so the two bounds do not combine. The simple combinations also fail on the test data. The minimum and the maximum of the two numbers are $\tau_\rho$ and $\widetilde\tau$, since $\tau_\rho \le \widetilde\tau$. The pairs $(\tau_\rho, \widetilde\tau)$ and $(\widetilde\tau, \tau_\rho)$ in the lexicographic order go down at some steps of the test. A candidate must keep some information about the history of the point, for example the forms that come from the second case, until $\rho$ goes down. Section 3.12 gives a different answer. The case is the type $d - \rho$, so the residual order $d$ goes down by one at each step from the second case to the first case where $\rho$ stays. With $d$ as the second entry, the triple $(\rho, d, \tau_\rho)$ does not get worse at a step where $\rho$ stays and no component of the divisor leaves.

### Status

The map gives SG00000057 and SG00000058 the status "proved". The Lean library proves Theorem 3.11.1 and Example 3.11.2 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianFullDirectrix.lean`. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The codimension of the directrix is from [Hir67]. Theorem 3.11.1 and Example 3.11.2 are a result of the milestone S7.15 of this project.
