---
title: The case is the type
nodes: [SG00000059, SG0000005A]
sources: [Hir67, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The case is the type

This section reports the twelfth research result of the milestone S7. It shows that the two cases of Section 3.4 are the two types $d - \rho$ of Volume 7, Definition 3.1.5, and it uses this to combine the results of Sections 3.5 to 3.11 into one statement about a triple of numbers. Volume 7, Section 3.10, gives the same result with all the details.

### The problem

The codimension $\tau_\rho$ can go down at a step from the second case to the first case, by Section 3.5. The full codimension $\widetilde\tau$ does not go down at such a step, but it can go down at a step from the first case, by Section 3.11. The two numbers do not combine into one function of the point. A reader can ask if some other number of the point goes down at the steps from the second case to the first case.

### The result

We use the setting of Volume 7, Sections 3.8 to 3.10. So $g = x^r G$ is clean, $d = \operatorname{ord} G$ is the residual order, $\rho = \operatorname{ord} \widetilde\Theta(G)$, and $\sigma = \operatorname{ord} \widetilde\Theta_0(G)$. The first case is $\sigma = \rho$, and the second case is $\sigma = \rho + 1$. At the new point we write $g'_c = x^{r'} G'$ and $d' = \operatorname{ord} G'$.

**Lemma 3.12.1.** Let $g \ne 0$ be clean. Then $\sigma = d$. So the first case is the type $0$, that is, $\rho = d$, and the second case is the type $1$, that is, $\rho = d - 1$. The point is in the second case if and only if $\partial_l \operatorname{in}(G) \ne 0$ for some $l \notin \Delta$.

Node: SG00000059 · Lean: `Singularity.idealOrd_logJacobianTangent_eq_ord` (for polynomials)

**Theorem 3.12.2.** Assume that $\rho' = \rho$ and that no component of $\Delta$ leaves. Then $d' \le d$. If $d' = d$, then $\tau_\rho(g'_c) \ge \tau_\rho(g)$. If $g$ is in the second case and $g'_c$ is in the first case, then $d' = d - 1$.

Node: SG0000005A · Lean: `Singularity.residualOrderAlong_cleanPart_le_of_forall_eq_zero` (for polynomials)

The Lean form with $\tau_\rho$ is `Singularity.logJacobianDirectrixCodim_le_cleanPart_of_residualOrderAlong_eq`.

**Example 3.12.3.** Let $p = 2$, $\Delta = \emptyset$ and $g = x y z^2 + y^2 z + x z^2$, as in Volume 7, Example 3.8.3. Then $d = 3$, $\rho = 2$ and $\tau_\rho(g) = 2$, so $g$ is in the second case. At the origin of the $x$-chart, $G' = x y z^2 + y^2 z + z^2$, so $d' = 2$, $\rho' = 2$ and $\tau_\rho(g'_c) = 1$, and $g'_c$ is in the first case. The codimension goes down, but the residual order goes down from $3$ to $2$. The triple $(\rho, d, \tau_\rho)$ goes from $(2, 3, 2)$ to $(2, 2, 1)$.

So with the order where a smaller $\rho$ is better, then a smaller $d$, and then a larger $\tau_\rho$, the triple $(\rho, d, \tau_\rho)$ does not get worse at a point where no component of the divisor leaves. This order is the lexicographic order on the triples $(\rho, d, \dim T_\rho(g))$ in $\mathbb{N}^3$, and it is a well-order.

### The proof in short

Each generator of $\widetilde\Theta_0(G)$ has order at least $d$, so $\sigma \ge d$. For the converse, take a monomial $x^\alpha$ of degree $d$ of $G$. Since $g$ is clean, some exponent $r_k + \alpha_k$ of the monomial $x^{r + \alpha}$ is prime to $p$. If $k \in \Delta$, the generator $e_k = r_k G + x_k \partial_k G$ has the term $(r_k + \alpha_k) c_\alpha x^\alpha$. If $k \notin \Delta$, the generator $x_k \partial_k G$ has the term $\alpha_k c_\alpha x^\alpha$. So $\sigma \le d$. This is the proof of the dichotomy of Volume 7, Theorem 3.1.4, with $x_k \partial_k$ in the place of $\partial_k$. With $\rho \le \sigma \le \rho + 1$ this gives the lemma, and part 3 of Theorem 3.1.4 gives the criterion with $\operatorname{in}(G)$.

By the lemma, $d = \rho$ in the first case and $d = \rho + 1$ in the second case, at both points. If $g$ is in the first case, then $g'_c$ is in the first case by Section 3.10, so $d' = \rho = d$, and $\tau_\rho$ does not go down by Section 3.10. If both points are in the second case, then $d' = \rho + 1 = d$, and $\tau_\rho$ does not go down by Section 3.5. If $g$ is in the second case and $g'_c$ is in the first case, then $d' = \rho = d - 1$. The hypothesis on the divisor is used only for the old points in the first case. In that case the hypothesis $p \nmid |r| + d$ of Section 3.8 can replace it.

In the example, the term $x z^2$ of $g$ gives the term $x z^2$ of $g'$. The component $x = 0$ of the new divisor takes the factor $x$ into $x^{r'}$, and the term $z^2$ of $G'$ has degree $2$. This is where $d$ loses one.

### The test data

A random test computed $\sigma$, $\rho$ and $d$ for 97,989 random clean $g$, with $(p, n) = (2, 3), (2, 4), (3, 3), (3, 4)$ and $(5, 3)$, and it found $\sigma = d$ for each of them, with the type $1$ for 74,523 of them and the type $0$ for 23,466 of them. A second test recorded the type at both points of each step where $\rho$ stays, in random sequences of point blowups. In a first run with $p = 2$, $n = 3$ and 800 sequences, the type was $1$ at each point of the second case and $0$ at each point of the first case, the type went up only at steps from the first case with $p \mid |r| + d$ to the second case with a leaving component, and the 18 drops of $\tau_\rho$ were all from the second case to the first case, with the type going from $1$ to $0$. The test of Section 3.11 had 447 steps from the second case to the first case where $\tau_\rho$ goes down, and by Theorem 3.12.2 the residual order goes down by one at each of them.

### What the result means

With Volume 7, Proposition 3.8.2, Corollary 3.9.8 and Theorems 3.9.10 and 3.9.11, we have this table for the steps where $\rho$ stays.

| Old point | New point | $d$ | $\tau_\rho$ | $(\rho, d, \tau_\rho)$ |
|---|---|---|---|---|
| second case | second case | stays | does not go down | not worse |
| second case | first case | goes down by one | can go down | better |
| first case, $p \nmid \lvert r \rvert + d$ | first case | stays | does not go down | not worse |
| first case, no component leaves | first case | stays | does not go down | not worse |
| first case, $p \mid \lvert r \rvert + d$, a component leaves | first case | stays | can go down | can get worse |
| first case, $p \mid \lvert r \rvert + d$, a component leaves | second case | goes up by one | does not go down | worse |

So the drops of $\tau_\rho$ from the second case to the first case, which Sections 3.5 and 3.11 could not handle with $\tau_\rho$ and $\widetilde\tau$, are steps where $d$ goes down. The full codimension $\widetilde\tau$ is not needed for them. The triple can get worse only in the last two rows, and both have a leaving component. The last row is the kangaroo points of Hauser, as in Volume 7, Examples 3.2.6 and 3.9.9, and the row before it is Volume 7, Examples 3.9.5 and 3.9.6. The next step of route R1 is an entry, built from the components of the divisor and their history, that goes down at the steps of these two rows. The result does not say that the triple goes down, and a resolution invariant must also exclude an infinite sequence of steps where the triple stays.

### Status

The map gives SG00000059 and SG0000005A the status "proved". The Lean library proves Lemma 3.12.1 and Theorem 3.12.2 for polynomials over a field of characteristic $p$, with the standard axioms only, in `Singularity/Invariant/LogJacobianType.lean`. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The order of the invariant of Hironaka, with the order first and the codimension of the directrix second, is from [Hir67]. The kangaroo points are from [Hau10]. Lemma 3.12.1 and Theorem 3.12.2 are a result of the milestone S7.16 of this project.
