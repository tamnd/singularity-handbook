---
title: The codimension of the directrix of the log-Jacobian order
nodes: [SG0000004Z]
sources: [Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The codimension of the directrix of the log-Jacobian order

Section 3.7 found a place for the points where $\rho$ stays: they lie in the projective space of a linear subspace $T_\rho(g)$. For the order of a hypersurface, Hironaka goes one step further. At a point where the order stays, the codimension of the directrix does not go down, and this second number is the next entry of his invariant. In this section we ask the same question for $\rho$. The answer depends on the two cases of Section 3.7. If the new point is in the second case, the codimension does not go down, and the proof is the proof of Hironaka with the weak transforms of Section 3.7. If the old point is in the second case and the new point is in the first case, the codimension can go down, and an example for $p = 2$ shows this.

We use the setting and the notation of Section 3.7. So $\pi = \pi_{1,t}$ is the chart at a point of the exceptional divisor, with the vector $v = (1, t_2, \dots, t_n)$, and $\sigma = \operatorname{ord} \widetilde\Theta_0(G)$. We say that $g$ is in the *first case* if $\sigma = \rho$, and in the *second case* if $\sigma = \rho + 1$. For the clean part $g'_c$ of the transform we write $g'_c = x^{r'} G'$, and we use the same words for $g'_c$, with $\sigma' = \operatorname{ord} \widetilde\Theta_0(G')$ and $\rho' = \rho(g'_c)$.

### The definition

**Definition 3.8.1.** Let $H(g)$ be the set of the elements $h \in \widetilde\Theta_0(G)$ with $\operatorname{ord} h = \rho$ if $g$ is in the first case, and the set of the elements $h \in \widetilde\Theta(G)$ with $\operatorname{ord} h = \rho$ if $g$ is in the second case. The *directrix of $\rho$* is
$$T_\rho(g) = \bigcap_{h \in H(g)} T(\operatorname{in}(h)),$$
and $\tau_\rho(g) = n - \dim T_\rho(g)$ is its codimension.

Node: SG0000004Z · Lean: `Singularity.logJacobianDirectrix`

This is the subspace of Section 3.7, and Theorem 3.7.1 says that $v \in T_\rho(g)$ when $\rho' = \rho$. The set $H(g)$ is not empty, because $\widetilde\Theta_0(G)$ has order $\rho$ in the first case and $\widetilde\Theta(G)$ has order $\rho$ in the second case. If $\rho = 0$, then $H(g)$ contains a unit, its initial form is a nonzero constant, and $T_\rho(g) = K^n$.

To compute $T_\rho(g)$ we need only finitely many elements. Let $h_1, \dots, h_m$ generate the ideal of the definition. Each $h_i$ has order at least $\rho$. An element $h = \sum_i a_i h_i$ of order $\rho$ has the initial form $\sum_i a_i(0) \, (h_i)_\rho$, where $(h_i)_\rho$ is the homogeneous part of degree $\rho$ of $h_i$. A sum of forms of degree $\rho$ has a directrix that contains the intersection of their directrices. So $T_\rho(g)$ is the intersection of the subspaces $T((h_i)_\rho)$ for the $i$ with $(h_i)_\rho \ne 0$.

### The proposition

**Proposition 3.8.2.** Assume that $\rho' = \rho$ and that $g'_c$ is in the second case. Then $\tau_\rho(g'_c) \ge \tau_\rho(g)$.

Node: SG0000004Z · Lean: `Singularity.logJacobianDirectrixCodim_le_cleanPart` (for polynomials)

*Proof.* We write $y = (x_2, \dots, x_n)$, so $x = (x_1, y)$, and $t = (t_2, \dots, t_n)$. Let $h \in H(g)$ and let $h' = x_1^{-\rho} \pi(h)$ be its weak transform in the chart. We show three facts about $h'$.

First, $h' \in H(g'_c)$. The proof of Theorem 3.7.1 shows that $h' \in W$ and $\operatorname{ord} h' = \rho$, and that $\rho = \rho' \le \operatorname{ord} W \le \rho$. The proof of Theorem 3.2.4 gives $\rho' = \operatorname{ord} W - |s|$, so $s = 0$ and $\widetilde\Theta(G') = W$. Thus $h'$ is an element of $\widetilde\Theta(G')$ of order $\rho = \rho'$. Since $g'_c$ is in the second case, this is the condition for $h' \in H(g'_c)$.

Second, the restriction of $\operatorname{in}(h')$ to $x_1 = 0$ is $\operatorname{in}(h)(0, y)$. As in the proof of Theorem 2.2.5, write $h = \sum_{k \ge 0} h_{\rho + k}$ with $h_{\rho + k}$ homogeneous of degree $\rho + k$. Then
$$h' = \sum_{k \ge 0} x_1^k \, h_{\rho + k}(1, y + t).$$
The terms with $k \ge 1$ are divisible by $x_1$. So the part of degree $\rho$ of $h'$, restricted to $x_1 = 0$, is the part of degree $\rho$ of $h_\rho(1, y + t) = \operatorname{in}(h)(v + (0, y))$. Since $v \in T(\operatorname{in}(h))$ by Theorem 3.7.1, this is $\operatorname{in}(h)(0, y)$, which is homogeneous of degree $\rho$.

Third, $\operatorname{in}(h)(x) = \operatorname{in}(h)(0, y - x_1 t)$. This is the identity $\operatorname{in}(h)(x + sv) = \operatorname{in}(h)(x)$ with $-x_1$ in the place of $s$.

Now let $w \in T_\rho(g'_c)$ with $w_1 = 0$, and write $w = (0, w')$. Let $h \in H(g)$. By the first fact, $w \in T(\operatorname{in}(h'))$, so $\operatorname{in}(h')(x + sw) = \operatorname{in}(h')(x)$. The first coordinate of $x + sw$ is $x_1$, so we can put $x_1 = 0$ on both sides, and the second fact gives
$$\operatorname{in}(h)(0, y + s w') = \operatorname{in}(h)(0, y)$$
in $K[y, s]$. With the third fact and this identity, for $y - x_1 t$ in the place of $y$,
$$\operatorname{in}(h)(x + sw) = \operatorname{in}(h)(0, y - x_1 t + s w') = \operatorname{in}(h)(0, y - x_1 t) = \operatorname{in}(h)(x).$$
So $w \in T(\operatorname{in}(h))$ for each $h \in H(g)$, that is, $w \in T_\rho(g)$.

Let $L$ be the hyperplane $w_1 = 0$. We showed that $T_\rho(g'_c) \cap L \subseteq T_\rho(g) \cap L$. Since $v \in T_\rho(g)$ and $v_1 = 1$, the subspace $T_\rho(g)$ is not contained in $L$, so $\dim (T_\rho(g) \cap L) = \dim T_\rho(g) - 1$. Hence
$$\dim T_\rho(g'_c) \le \dim (T_\rho(g'_c) \cap L) + 1 \le \dim (T_\rho(g) \cap L) + 1 = \dim T_\rho(g),$$
and $\tau_\rho(g'_c) \ge \tau_\rho(g)$. $\square$

The proof does not use the case of the old point. It uses the case of the new point only once, in the first fact, to know that the weak transforms are in $H(g'_c)$. If $g'_c$ is in the first case, then $H(g'_c)$ is a subset of $\widetilde\Theta_0(G')$, and a weak transform $h'$ can be outside $\widetilde\Theta_0(G')$. Then the forms $\operatorname{in}(h')$ do not control $T_\rho(g'_c)$, and the next example shows that the result can fail.

### The codimension can go down

**Example 3.8.3.** Let $p = 2$, $n = 3$ with the variables $x, y, z$, $\Delta = \emptyset$ and
$$g = x y z^2 + y^2 z + x z^2.$$
The exponents $(1, 1, 2)$, $(0, 2, 1)$ and $(1, 0, 2)$ are not all even, so $g$ is clean, and $\operatorname{ord} g = 3 \ge p$. Here $r = 0$ and $G = g$. In characteristic $2$ the generators of $\widetilde\Theta(G)$ are
$$\partial_x G = y z^2 + z^2, \qquad \partial_y G = x z^2, \qquad \partial_z G = y^2.$$
Their orders are $2$, $3$ and $2$, so $\rho = 2$. Since $\Delta = \emptyset$, the ideal $\widetilde\Theta_0(G)$ is generated by the elements $x_k \partial_j G$, and it has order $3$. So $g$ is in the second case. The parts of degree $2$ of the generators are $z^2$, $0$ and $y^2$. We have $T(z^2) = \{w_3 = 0\}$ and $T(y^2) = \{w_2 = 0\}$, so $T_\rho(g)$ is the line of $e_1$, and $\tau_\rho(g) = 2$.

Take the $x$-chart $\pi(x) = x$, $\pi(y) = x y$, $\pi(z) = x z$ at its origin, with the vector $v = e_1 \in T_\rho(g)$. Then $\pi(g) = x^4 y z^2 + x^3 y^2 z + x^3 z^2$, so
$$g' = x^2 y z^2 + x y^2 z + x z^2,$$
which is clean, and $\Delta' = \{1\}$. Here $r' = (1, 0, 0)$ and $G' = x y z^2 + y^2 z + z^2$. The generators of $\widetilde\Theta(G')$ are
$$r'_1 G' + x \partial_x G' = y^2 z + z^2, \qquad \partial_y G' = x z^2, \qquad \partial_z G' = y^2,$$
with the orders $2$, $3$ and $2$. So $\rho' = 2 = \rho$, and $\rho$ stays. But the first generator is also in $\widetilde\Theta_0(G')$, so $\sigma' = 2$, and $g'_c$ is in the first case. The other generators of $\widetilde\Theta_0(G')$ are the elements $x_k \partial_y G'$ and $x_k \partial_z G'$, of order at least $3$. So each element of $H(g'_c)$ has an initial form $c z^2$ with $c \ne 0$, and $T_\rho(g'_c) = \{w_3 = 0\}$. So $\tau_\rho(g'_c) = 1 < 2 = \tau_\rho(g)$.

Node: SG0000004Z · Lean: `Singularity.tauRhoExample_finrank`

In the example, the weak transform of $\partial_z G = y^2$ is $y^2 = \partial_z G'$. It is an element of $\widetilde\Theta(G')$ of order $\rho$, but it is not in $\widetilde\Theta_0(G')$, so it is not in $H(g'_c)$. This is the step of the proof that fails. The old point is in the second case and the new point is in the first case.

A random test checked the other combinations of the cases. It used random clean $g$ and random charts for $(p, n) = (2, 3), (3, 3), (2, 4)$ and $(5, 3)$, and it computed $T_\rho$ from the generators, as above, with a search over $\mathbb{F}_p^n$. It found 1,054 points where $\rho$ stays and the cases go from the first to the first, from the first to the second, or from the second to the second. At none of them does $\tau_\rho$ go down. Proposition 3.8.2 covers the last two combinations. For the cases from the first to the first, the forms $\operatorname{in}(h')$ of the weak transforms need not lie in the span of the initial forms of $H(g'_c)$, so the proof above does not apply. Example 3.9.4 shows this, and Section 3.9 gives a different proof for these cases when $p$ does not divide $|r| + d$. At 12 of 345 points with the cases from the second to the first, $\tau_\rho$ went down by $1$.

### The Lean proof

The Lean library proves Proposition 3.8.2 and Example 3.8.3 for polynomials over a field of characteristic $p$, with the standard axioms only, in the file `Singularity/Invariant/LogJacobianDirectrix.lean`. As in Section 3.7, the Lean definitions use the element $\psi = x^r h$ of $\Theta_0(g)$ or of $\Theta(g)$ in the place of $h$. The ideal of the case is `Singularity.logJacobianCaseIdeal`. It is $\Theta_0(g)$ if $\operatorname{ord} \Theta_0(g) = |r| + \rho$ and $\Theta(g)$ in the other case. The subspace $T_\rho(g)$ is `Singularity.logJacobianDirectrix`, and $\tau_\rho(g)$ is `Singularity.logJacobianDirectrixCodim`.

The remark on the generators after Definition 3.8.1 is `Singularity.homogeneousComponent_mem_span_of_mem_span`, with the form for directrices `Singularity.le_directrix_homogeneousComponent_of_mem_span`. The count of dimensions at the end of the proof of Proposition 3.8.2 is a separate lemma, `Singularity.finrank_iInf_directrix_pointChart_le`, for any family of polynomials of order at least $m$ whose weak transforms have order at least $m$. Proposition 3.8.2 is `Singularity.finrank_logJacobianDirectrix_cleanPart_le` in the form $\dim T_\rho(g'_c) \le \dim T_\rho(g)$, and `Singularity.logJacobianDirectrixCodim_le_cleanPart` in the form with $\tau_\rho$. In Example 3.8.3, `Singularity.tauRhoExample_cases` gives the two cases, and `Singularity.tauRhoExample_finrank` gives $\rho = \rho' = 2$, $\dim T_\rho(g) = 1$ and $\dim T_\rho(g'_c) = 2$.

### Notes and references

The codimension of the directrix and the theorem that it does not go down at the points where the order stays are from [Hir67]. Proposition 3.8.2 and Example 3.8.3 are a result of the milestone S7.9 of this project. Volume 9, Section 3.5 gives the result as a research report. Section 3.9 continues with the cases from the first to the first.
