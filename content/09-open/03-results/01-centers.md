---
title: The log-Jacobian ideal under a blowup in a regular center
nodes: [SG0000004Q, SG0000004R, SG0000004P]
sources: [Cos87, Pos24, Hau10, HP19a]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The log-Jacobian ideal under a blowup in a regular center

This section reports the first research result of the milestone S7. It is about the equations $z^p + g = 0$ of Conjecture 2.3.7, and it is a step on the route of the purely inseparable equations in Section 2.3. Volume 7, Section 3.4, gives the same result with all the details. Here we state the result in geometric terms, we give the proof in a short form, and we explain the Lean proof and what the result does not give.

### The problem

Let $K$ be an algebraically closed field of characteristic $p$, and let $X \subseteq \mathbb{A}^{n+1}$ be the hypersurface $z^p + g(x_1, \dots, x_n) = 0$. A resolution algorithm for $X$ blows up regular centers, and after each blowup it must show that an invariant goes down. Away from a divisor, the change $z \mapsto z + h$ replaces $g$ by $g + h^p$, so the invariant must not depend on the class of $g$ modulo $p$-th powers. The residual order of Volume 7, Chapter 1, depends on this class, and it can go up under a point blowup. Moh's bound says that it goes up by at most one. The kangaroo points of Hauser are the points where it goes up [Hau10].

Volume 7, Chapter 3, replaces $g$ by its log-Jacobian ideal $\Theta(g)$. This ideal does not change when a $p$-th power is added to $g$. Its residual order $\rho$ differs from the residual order $d$ of $g$ by at most one, and $\rho$ does not go up under a point blowup (Volume 7, Theorem 3.2.4). The Lean library proves these facts.

A resolution algorithm also blows up centers of positive dimension. The question of this section is: does $\rho$ go up under the blowup of a regular center $C$ of positive dimension? For a base of dimension $3$, Cossart gives a condition of permissibility for such centers in his thesis [Cos87]. We do not know a statement for each dimension in the literature.

### The result

Let $E = V(\prod_{i \in \Delta} x_i)$ be the divisor of the earlier blowups, and let $C = V(x_1, \dots, x_c)$ with $2 \le c \le n$, a regular center that has normal crossings with $E$. Assume that $g \in I_C^p$, so that $X$ has order $p$ along the center $V(z, x_1, \dots, x_c)$. Write $g = x^r G$, where $x^r$ is the largest monomial in the variables of $\Delta$ that divides $g$, and let
$$\widetilde\Theta(G) = x^{-r} \Theta(g), \qquad \widetilde\Theta_C(G) = x^{-r} \Theta_C(g), \qquad \rho = \operatorname{ord}_0 \widetilde\Theta(G).$$
Here $\Theta_C(g)$ is the image of $g$ under the logarithmic derivations that are tangent to $C$ (Volume 7, Definition 3.4.1). The two conditions on the center are:

- (H1) $\operatorname{ord}_C \widetilde\Theta(G) = \rho$;
- (H2) $\operatorname{ord}_C \widetilde\Theta_C(G) = \rho + 1$, or $\operatorname{ord}_0 \widetilde\Theta_C(G) = \rho$.

Condition (H1) says that $\widetilde\Theta(G)$ is equimultiple along $C$ at the origin. Condition (H2) says the same for $\widetilde\Theta_C(G)$ when its order along $C$ is $\rho$.

**Theorem 3.1.1.** Let $g \ne 0$ be clean for $\Delta$ with $g \in I_C^p$, and assume (H1) and (H2). Let $\pi$ be a chart of the blowup of $C$ at a point of the exceptional divisor over the origin, with $\pi(g) = x_1^p g'$, and let $g'_c$ be the clean part of $g'$ for the new divisor $\Delta'$. Then $g'_c \ne 0$ and $\rho(g'_c) \le \rho$.

Node: SG0000004Q · Lean: `Singularity.logJacobianOrder_cleanPart_le_center` (for polynomials, with (H1) and (H2) in the form of Volume 7, Section 3.4)

The theorem holds in each number of variables. For $c = n$ the center is the origin, both conditions hold, and the theorem is Volume 7, Theorem 3.2.4.

*Proof.* We use three results of Volume 7, Section 3.4. The first is the transformation law: $\Theta'(g') = x_1^{-p} \pi(\Theta_C(g)) K[[x]]$ (Theorem 3.4.3). The second is the inclusions $I_C \widetilde\Theta(G) \subseteq \widetilde\Theta_C(G) \subseteq \widetilde\Theta(G)$. The third is the bound for the weak transform: if $h \in I_C^s$ and $\operatorname{ord}_0 h = s$, then $x_1^{-s} \pi(h)$ has order at most $s$ at the new point (Lemma 3.4.4).

Since $\Theta(g) \ne 0$ and $\pi$ is injective, the law gives $\Theta'(g') \ne 0$. If $g'_c = 0$, then $g'$ is a $p$-th power and $\Theta'(g') = 0$. So $g'_c \ne 0$.

Let $\sigma = \operatorname{ord}_C \widetilde\Theta_C(G)$. By (H1) and the inclusions, $\sigma$ is $\rho$ or $\rho + 1$. We find an element $h \in \widetilde\Theta_C(G)$ with $x_1^{-\sigma} \pi(h)$ of order at most $\rho$. If $\sigma = \rho + 1$, take $h_1 \in \widetilde\Theta(G)$ of order $\rho$. By (H1), $h_1 \in I_C^\rho$, so Lemma 3.4.4 applies to $h_1$, and $h = x_1 h_1$ is in $\widetilde\Theta_C(G)$ with $x_1^{-\rho - 1} \pi(h) = x_1^{-\rho} \pi(h_1)$. If $\sigma = \rho$, then (H2) gives $h \in \widetilde\Theta_C(G)$ of order $\rho$, and $h \in I_C^\rho$, so Lemma 3.4.4 applies to $h$.

By the law, $\Theta'(g')$ is $x^b$ times the ideal $W$ generated by the elements $x_1^{-\sigma} \pi(h)$, up to a unit, where $x^b$ is a monomial in the variables of $\Delta'$. The exponent of $x_1$ in $x^b$ is $r_1 + \dots + r_c + \sigma - p$. It is not negative, because $\sigma \ge \operatorname{ord}_C G$ and $g \in I_C^p$. The ideal $W$ has an element of order at most $\rho$. By part 1 of the dichotomy (Volume 7, Theorem 3.1.4) at the new point, $\rho(g'_c)$ is the order of $W$ after the division by the largest monomial in the variables of $\Delta'$ that divides it. This order is at most $\operatorname{ord} W \le \rho$. $\square$

### Condition (H2) cannot be omitted

**Example 3.1.2.** Let $p = 2$, $n = 3$ with the coordinates $(x, y, w)$, $E = V(w)$, $g = y^2 w + y^3$ and $C = V(x, y)$. Then $\widetilde\Theta(G) = (y^2)$, so $\rho = 2$, and (H1) holds. The ideal $\widetilde\Theta_C(G) = (y^2 w, x y^2, y^3)$ has order $2$ along $C$ and order $3$ at the origin, so (H2) fails. In the $x$-chart, $g' = y^2 w + x y^3$ is clean, $\Theta'(g') = (y^2 w, x y^2)$ and $\rho(g'_c) = 3$. So $\rho$ goes up from $2$ to $3$.

Node: SG0000004R · Lean: `Singularity.centerExample_logJacobianOrder_cleanPart` ($\rho(g'_c) = 3$, over $\mathbb{F}_2$)

Volume 7, Example 3.4.6, gives the computation. The origin is a special point of $C$: the order of $\widetilde\Theta_C(G)$ is $2$ at the generic point of $C$ and $3$ at the origin. A rule for the choice of the centers must avoid such a center.

### The Lean proof

The Lean library proves Theorem 3.1.1 and Example 3.1.2 for polynomials over a field of characteristic $p$, with the standard axioms only. The proofs are in three files.

1. `Singularity/Invariant/LogJacobianCenter.lean` defines the chart `centerChart S j t` for the center $V(x_i : i \in S)$ and the ideal `logJacobianCenter Δ S g`. It proves the transformation law as two inclusions in $K[x]$, and the bound for the equimultiple weak transform. In $K[x]$ the factors $x_i + t_i$ are not units, so the law has a factor $u$, the product of these elements (`Singularity.centerUnit`).
2. `Singularity/Invariant/LogJacobianCenterNonincrease.lean` proves the theorem. It states (H1) and (H2) with the factor $x^r$ in place of $G$: each element of $\Theta(g)$ is $x^r q$ with $q \in I_C^\rho$, and so on. The proof does not use the ideal $W$. It shows that a monomial $x^b$ divides each element of $\Theta'(g')$, where the factor $u$ cancels because its constant term is not $0$. Then it finds one element of order at most $|b| + \rho$, and it uses part 1 of the dichotomy.
3. The same file computes Example 3.1.2 over $\mathbb{F}_2$, with the theorems `Singularity.centerExample_logJacobianOrder` ($\rho = 2$), `Singularity.centerExample_H1` and `Singularity.centerExample_not_H2`.

The Lean statement of the theorem does not assume that $g$ is clean. It assumes only that $\rho$ is finite, and this is true for a clean $g \ne 0$ (`Singularity.exists_logJacobianOrder_eq`).

### What the result does not give

The result is one step. It does not prove Conjecture 2.3.7 in four variables, and it does not prove a case of $\mathrm{Res}(p, 4)$.

1. It says that $\rho$ does not go up. It does not say that $\rho$ goes down. At the points where $\rho$ stays the same, a resolution algorithm needs a second invariant. The cycles of Hauser and Perlega [HP19a] are for $z^q + F$ with $q = p^3$. They test a candidate once it is extended to $z^q + g$ (item 3).
2. It is local and in coordinates. A center rule must choose centers that satisfy (H1) and (H2) at each point, and the rule must be independent of the coordinates. A natural candidate is the locus where the pair $(\rho, \operatorname{ord}_0 \widetilde\Theta_C(G))$ is maximal. We do not know whether this locus is regular, or whether a sequence of such blowups ends.
3. It is for the equations $z^p + g$. The case $z^q + g$ with $q = p^e$ and $e \ge 2$ needs the operators $\partial^{(\beta)}$ of Volume 1, Section 6.3, in place of the derivations (Volume 7, Remark 3.1.8).
4. The Lean proof is in $K[x]$, not in $K[[x]]$.

### Status

The map gives SG0000004Q the status of a node with a Lean proof. An outside expert has not yet read the result, and the milestone S7 asks for this. Until then the result is a claim of the project with a complete proof and a Lean proof, but without an outside review.

### Notes and references

Cossart proves the transformation law for a point blowup and gives conditions of permissibility for centers of positive dimension, for a base of dimension $3$ [Cos87]. Posva gives a modern account of the transformation law [Pos24, Appendix A]. The kangaroo points are from [Hau10], and the cycles are from [HP19a].
