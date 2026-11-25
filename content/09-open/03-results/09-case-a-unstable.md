---
title: The first case is not stable when p divides the sum
nodes: [SG00000054]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The first case is not stable when p divides the sum

This section reports the ninth research result of the milestone S7. It shows that the hypothesis on $|r| + d$ in Proposition 3.8.1 is necessary. Volume 7, Example 3.9.9, gives the same example with all the details.

### The problem

Proposition 3.8.1 says that the new point is in the first case, if $\rho$ stays, the old point is in the first case and $p$ does not divide $|r| + d$. The proof uses the Euler element, and its initial form is $(|r| + d) F$. If $p$ divides $|r| + d$, this initial form is $0$, and the proof fails. A reader can ask if the result is still true in this situation.

### The result

The answer is no. We use the setting of Volume 7, Section 3.9.

**Example 3.9.1.** Let $p = 3$, $n = 3$ with the variables $x, y, z$, $\Delta = \{x, z\}$ and
$$g = x^3 y^2 z^3 + 2 x^2 y^3 z.$$
Then $r = (2, 0, 1)$, $G = x y^2 z^2 + 2 y^3$ and $d = 3$, so $|r| + d = 6$ is $0$ in $K$. The point is in the first case, with $\rho = 3$ and $\tau_\rho(g) = 1$. Take the $x$-chart at the point with $t_y = 0$ and $t_z = 1$. Then $g'_c = x^3 (x^2 y^2 (z^3 + 1) + 2 y^3 z)$ and $\Delta' = \{x\}$. The new point has $\rho' = 3$ and $\sigma' = 4$, so it is in the second case, and $\tau_\rho(g'_c) = 2$.

Node: SG00000054 · Lean: `Singularity.caseAToCaseBExample_cases`

### The example in short

At the old point the forms of the elements $e_x = r_x G + x \partial_x G$ and $e_z = r_z G + z \partial_z G$ are $y^3$ and $2 y^3$. Their sum is $(|r| + d) F = 0$, so the Euler element has order $5$ and it does not give the form $F$. The component $z = 0$ leaves the divisor, since $t_z \ne 0$. At the new point the form $y^3$ comes from $\partial_z G' = 2 y^3$. This is the derivative in the direction that left the divisor, so it is an element of $\widetilde\Theta(G')$ and not of $\widetilde\Theta_0(G')$. All the generators of $\widetilde\Theta_0(G')$ have order $4$, so $\sigma' = \rho' + 1$.

### The test data

A random test of sequences of at most four point blowups for $(p, n) = (2, 3), (2, 4)$ and $(3, 3)$ found 501, 123 and 63 steps from the first case with $p \mid |r| + d$ to the second case, with $\rho$ the same. A second test for $(p, n) = (2, 3), (2, 4), (3, 3)$ and $(5, 3)$ recorded the divisor at each of these steps. At each step a component of the divisor leaves, that is, there is an $i \in \Delta$ with $i \ne 1$ and $t_i \ne 0$.

### What the result means

The table of Section 3.8 has the row "first case, $p \mid |r| + d$, to the second case". The example shows that this row occurs, and Volume 7, Proposition 3.8.2, shows that $\tau_\rho$ does not go down in it. So the table is correct, and the row is not empty.

The test data also suggests a new hypothesis. In the example and in all the steps of the test, a component of the divisor leaves. Section 3.10 proves that this is necessary. If no component leaves, the new point is in the first case, also when $p$ divides $|r| + d$.

### Status

The map gives SG00000054 the status "proved". The Lean library proves the example over $\mathbb{F}_3$, with the polynomials written out and the standard axioms only, in `Singularity/Invariant/LogJacobianCaseAUnstable.lean`. The main result is `Singularity.caseAToCaseBExample_cases`, and `Singularity.caseAToCaseBExample_codim` gives the two values of $\tau_\rho$. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The codimension of the directrix is from [Hir67]. Example 3.9.1 is a result of the milestone S7.13 of this project.
