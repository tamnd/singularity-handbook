---
title: The end case of the log-Jacobian ideal
nodes: [SG0000004S]
sources: [Cos87, CP08, Wlo22, AS22]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The end case

Sections 3.2 and 3.4 show that $\rho$ does not go up under a blowup, at least when the center satisfies (H1) and (H2). If a resolution algorithm makes $\rho$ go down, it ends at a point with $\rho = 0$. In this section we find the singularities at such a point. They are very simple: after a change of the coordinates, the equation is $z^p + x^r$ or $z^p + x^r x_j$. These are binomial equations, and binomial varieties have a resolution in each characteristic. So the end of the route is not the difficult part. The difficult part is to make $\rho$ go down.

We use the notation of Section 3.1. The equation is $z^p + F$, the divisor is $E = V(\prod_{i \in \Delta} x_i)$, and for a clean $F \ne 0$ we write $F = x^r G$ with $r_i = 0$ for $i \notin \Delta$ and $d = \operatorname{ord} G$.

### The two types

**Proposition 3.5.1.** Let $F \ne 0$ be clean. Then $\rho(F) = 0$ if and only if one of these holds:

1. (type 0) $G(0) \ne 0$, and $p \nmid r_i$ for some $i \in \Delta$;
2. (type 1) $G(0) = 0$, and $\partial_j G(0) \ne 0$ for some $j \notin \Delta$.

In type 0 we have $d = 0$, and in type 1 we have $d = 1$.

Node: SG0000004S

*Proof.* The ideal $\widetilde\Theta(G)$ has an element of order $0$ if and only if one of its generators has a constant term that is not $0$, because the elements of order at least $1$ form the ideal $(x)$, and an ideal is in $(x)$ if and only if each of its generators is in $(x)$. The constant terms of the generators are
$$(r_i G + x_i \partial_i G)(0) = r_i G(0) \ (i \in \Delta), \qquad (\partial_j G)(0) \ (j \notin \Delta).$$
Assume that $\rho(F) = 0$. If $G(0) \ne 0$, then $d = 0$. The coefficient of the monomial $x^r$ in $F = x^r G$ is $G(0) \ne 0$. Since $F$ is clean, the exponent $r$ is not in $p \mathbb{N}^n$, so $p \nmid r_i$ for some $i$. Since $r_i = 0$ for $i \notin \Delta$, this $i$ is in $\Delta$. This is type 0. If $G(0) = 0$, then the constant terms $r_i G(0)$ are $0$, so $\partial_j G(0) \ne 0$ for some $j \notin \Delta$. Then $G$ has a term $c x_j$ with $c \ne 0$, and $d = 1$. This is type 1.

Conversely, in type 0 the generator $r_i G + x_i \partial_i G$ has the constant term $r_i G(0)$, which is not $0$ because $p \nmid r_i$. In type 1 the generator $\partial_j G$ has a constant term that is not $0$. In both cases $\rho(F) = 0$. $\square$

The proposition agrees with Theorem 3.1.4. In type 0 we have $\rho = d = 0$, so the type of Definition 3.1.5 is $\tau = 0$. In type 1 we have $\rho = d - 1 = 0$, so $\tau = 1$. The proof uses the cleanness of $F$ only in type 0. There it is necessary, as the next example shows.

**Example 3.5.2.** Let $p = 2$, $n = 2$, $\Delta = \{1\}$ and $F = x_1^2 + x_1^2 x_2$. Then $r = (2, 0)$, $G = 1 + x_2$ and $G(0) = 1$, but $2 \mid r_1$. The generators of $\widetilde\Theta(G)$ are $r_1 G + x_1 \partial_1 G = 0$ and $\partial_2 G = 1$, so $\rho = 0$, but $F$ is not of type 0. This $F$ is not clean, because $x_1^2$ is a square. Its clean part is $F_c = x_1^2 x_2$, with $r = (2, 0)$ and $G = x_2$. Now $G(0) = 0$ and $\partial_2 G = 1$, so $F_c$ is of type 1. The equation is $z^2 + x_1^2 x_2$.

### The normal form

Now let $R = K[[x]]$, with $K$ algebraically closed. A change of the coordinates is *adapted to $E$* if it maps each hyperplane $V(x_i)$ with $i \in \Delta$ to itself.

**Theorem 3.5.3.** Let $F \in K[[x]]$ be clean, $F \ne 0$, with $\rho(F) = 0$. Then there is a change of the coordinates, adapted to $E$, after which:

1. in type 0, $F = x^r$, with $p \nmid r_i$ for some $i \in \Delta$;
2. in type 1, $F = x^r x_j$ for some $j \notin \Delta$.

So the hypersurface $z^p + F = 0$ is $z^p + x^r = 0$ or $z^p + x^r x_j = 0$ in the new coordinates.

Node: SG0000004S

*Proof.* Type 0. Fix $i \in \Delta$ with $p \nmid r_i$. The element $G$ is a unit of $K[[x]]$. Since $K$ is algebraically closed, $G(0)$ has an $r_i$-th root $a \in K$. Write $G = G(0)(1 + m)$ with $m \in (x)$. The polynomial $T^{r_i} - (1 + m)$ over $K[[x]]$ has the root $T = 1$ modulo $(x)$, and its derivative $r_i T^{r_i - 1}$ is a unit at $T = 1$, because $r_i$ is not $0$ in $K$. Since $K[[x]]$ is complete, Hensel's lemma gives $w \in 1 + (x)$ with $w^{r_i} = 1 + m$. So $v = a w$ is a unit with $v^{r_i} = G$. Put $x_i' = x_i v$, and keep the other coordinates. This is a change of the coordinates, because $v(0) \ne 0$. It is adapted to $E$, because $V(x_i') = V(x_i)$. Then
$$x_1^{r_1} \cdots (x_i')^{r_i} \cdots x_n^{r_n} = x^r v^{r_i} = x^r G = F.$$

Type 1. Fix $j \notin \Delta$ with $\partial_j G(0) \ne 0$. Put $x_j' = G$, and keep the other coordinates. The linear part of $G$ has the coefficient $\partial_j G(0) \ne 0$ at $x_j$, so the Jacobian matrix of the new coordinates at the origin is invertible, and the new coordinates are a regular system of parameters of $K[[x]]$. The change is adapted to $E$, because it does not change $x_i$ for $i \in \Delta$. Since $r_j = 0$, the monomial $x^r$ does not contain $x_j$, so it does not change, and $F = x^r x_j'$. $\square$

The proof of type 0 is the only place where $p \nmid r_i$ is used. If $p$ divides each $r_i$ and $G(0) \ne 0$, then the monomial $x^r$ of $F$ is a $p$-th power up to a constant, so $F$ is not clean. Example 3.5.2 shows this case.

In type 1 the divisor $V(x_j')$ is not part of $E$. A global argument must explain where this divisor comes from. On the hypersurface $z^p + x^r G = 0$ the divisor of $G$ is $p \operatorname{div}(z) - \operatorname{div}(x^r)$, and this suggests a global construction. We do not develop it here.

### Binomial equations

The equations $z^p + x^r$ and $z^p + x^r x_j$ are binomial: they have two terms. A variety that is defined locally by binomial equations is locally toric, and it has a resolution in each characteristic by combinatorial methods (Volume 9, Theorem 2.4.3). Włodarczyk proves this with cobordant blowups [Wlo22], and Abramovich and Schober prove it with weighted blowups [AS22]. In both proofs the invariant is built from the monomials, not from the derivatives.

So the points with $\rho = 0$ are not an obstacle. Two questions remain. The first is to glue the local normal forms of Theorem 3.5.3, with the extra divisor $V(x_j')$ in type 1, into a global toroidal structure. The second, and the main one, is to find a sequence of blowups that makes $\rho$ go down to $0$. Sections 3.2 and 3.4 give only that $\rho$ does not go up.

### The Lean proof

The Lean library proves Proposition 3.5.1 for polynomials over a field of characteristic $p$. It does not prove Theorem 3.5.3, because the change of the coordinates needs the ring $K[[x]]$ and the roots of units in it.

### Notes and references

In Cossart's thesis the end case for a base of dimension $3$ is the case where his invariant is $0$, and Giraud gives the form $t^p + x^a$ in the étale topology [Cos87]. Cossart and Piltant treat the case $(m, \omega) = (p, 0)$ with combinatorial methods [CP08]. The proof above does not use the number of variables.
