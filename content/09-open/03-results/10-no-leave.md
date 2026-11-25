---
title: The first case is stable if no component leaves
nodes: [SG00000055, SG00000056]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The first case is stable if no component leaves

This section reports the tenth research result of the milestone S7. It explains the leaving components of Section 3.9, and it removes the hypothesis on $|r| + d$ from Proposition 3.8.1 and Corollary 3.8.2 when no component of the divisor leaves. Volume 7, Section 3.9, gives the same result with all the details.

### The problem

Section 3.9 gives a step from the first case with $p \mid |r| + d$ to the second case. In the example and at each such step of a random test, a component of the divisor leaves. A component $i \in \Delta$ with $i \ne 1$ *leaves* in the chart if $t_i \ne 0$, that is, if the strict transform of $x_i = 0$ does not pass through the new point. A reader can ask if a leaving component is necessary for this step, and also for the drops of $\tau_\rho$ of Section 3.7.

### The result

We use the setting of Volume 7, Section 3.9. For $i \in \Delta$ let $e_i = r_i G + x_i \partial_i G$ and let $\Phi_i$ be its homogeneous part of degree $d$. Let $R$ be the set of the $i \in \Delta$ with $\Phi_i \ne 0$.

**Theorem 3.10.1.** Assume that $\rho' = \rho$ and that $g$ is in the first case. Assume that $R$ contains an index $i \ne 1$ that does not leave, or that $R = \{1\}$. Then $g'_c$ is in the first case. In particular, this holds if no component of $\Delta$ leaves.

Node: SG00000055 · Lean: `Singularity.idealOrd_logJacobianTangent_cleanPart_of_forall_eq_zero`

**Theorem 3.10.2.** Assume that $\rho' = \rho$, that $g$ is in the first case, and that no component of $\Delta$ leaves. Then $\tau_\rho(g'_c) \ge \tau_\rho(g)$.

Node: SG00000056 · Lean: `Singularity.logJacobianDirectrixCodim_le_cleanPart_of_forall_eq_zero`

The two theorems have no hypothesis on $p$.

### The proof in short

In the first case $\rho = \sigma = d$, also when $p$ divides $|r| + d$, since $\sigma \ge d \ge \rho$. So the set $R$ is not empty. The proof of Proposition 3.8.1 needs one element $h$ of $\widetilde\Theta_0(G)$ of order $d$ whose transport is exact, that is, $\pi(x^r h) = x_1^p \, D g'$ for a derivation $D$ of $\Theta'_0$. If $i \in R$, $i \ne 1$ and $i$ does not leave, the element $h = e_i$ has this property with $D = x_i \partial_i$. If $R = \{1\}$, the Euler element has the homogeneous part $\Phi_1 \ne 0$ of degree $d$, and it has this property with $D = x_1 \partial_1$. This gives Theorem 3.10.1.

For Theorem 3.10.2 we can assume that $p$ divides $|r| + d$, by Corollary 3.8.2. Then both points are in the first case, and the proof of Volume 7, Theorem 3.9.1 applies to each $\Phi_i$ with $i \ne 1$, since $e_i$ has an exact transport. For $i = 1$, the Euler identity gives $\sum_{k \in R} \Phi_k = (|r| + d) F = 0$. So $\Phi_1$ is a linear combination of the other forms $\Phi_k$, and each vector of the directrix of $g'_c$ with $w_1 = 0$ is also in $T(\Phi_1)$.

### The test data

A random test took points in the first case and each chart where $\rho$ stays. For $(p, n) = (2, 3)$ and $(3, 3)$ it found 3,456 and 870 steps that satisfy the hypothesis of Theorem 3.10.1, and at each of them the new point is in the first case. It found 270 and 64 steps to the second case. At each of these $p$ divides $|r| + d$, the set $R$ has two elements, and the hypothesis of Theorem 3.10.1 fails. A second test took the steps where no component leaves. For $(p, n) = (2, 3), (2, 4), (3, 3)$ and $(5, 3)$ it found 3,176, 745, 698 and 175 steps. At each of them the new point is in the first case, and $\tau_\rho$ does not go down.

### What the result means

With Volume 7, Proposition 3.8.2, the result gives a short list of the steps where $\tau_\rho$ can go down when $\rho$ stays. There are two kinds.

1. The old point is in the second case, and the new point is in the first case. Volume 7, Example 3.8.3, is of this kind.
2. Both points are in the first case, $p$ divides $|r| + d$, and a component of the divisor leaves. Volume 7, Examples 3.9.5 and 3.9.6, are of this kind.

A leaving component is a component of the old divisor that does not pass through the new point. So at a step of the second kind, the new divisor has fewer components through the point than the old one, apart from the exceptional divisor. This suggests a secondary invariant for route R1 that also counts the components of the divisor, in the style of the invariants of Villamayor and of Bierstone and Milman in characteristic $0$. For the drops of the first kind, the test of Section 3.8 shows that the form of $\tau$ with $\widetilde\Theta(G)$ never went down from the second case. A candidate invariant must handle both kinds, and this is the next step of the search.

### Status

The map gives SG00000055 and SG00000056 the status "proved". The Lean library proves Theorems 3.10.1 and 3.10.2 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianNoLeave.lean`. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The codimension of the directrix is from [Hir67]. Theorems 3.10.1 and 3.10.2 are a result of the milestone S7.14 of this project.
