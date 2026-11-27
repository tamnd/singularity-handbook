---
title: The log-Jacobian ideal and the dichotomy
nodes: [SG0000003E, SG0000003F, SG0000004N]
sources: [Cos87, Pos24, CP08, HP19a]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The log-Jacobian ideal and the dichotomy

Let $R = K[[x]]$ or $R = K[x]$. In this section the equation is $f = z^p + F$ with $F \in R$, so $q = p$. A change of the variable $z \mapsto z + h$ replaces $F$ by $F + h^p$ (Lemma 1.3.2). An invariant of the hypersurface must therefore see only the class of $F$ modulo $p$-th powers. The derivatives of $F$ have this property, because every derivation kills a $p$-th power.

### The ideal

The derivations of $R$ that are tangent to the divisor $E$ are the derivations $D$ with $D(x_i) \in (x_i)$ for each $i \in \Delta$. They form a free $R$-module with the basis
$$x_i \partial_i \ (i \in \Delta), \qquad \partial_j \ (j \notin \Delta).$$
These are the *logarithmic derivations* for $E$.

**Definition 3.1.1.** The *log-Jacobian ideal* of $F$ for $E$ is the ideal of $R$
$$\Theta(F) = \bigl( x_i \partial_i F \ (i \in \Delta), \ \partial_j F \ (j \notin \Delta) \bigr).$$

Node: SG0000003E · Lean: `Singularity.logJacobian`

The ideal is the image of $F$ under all logarithmic derivations. For $\Delta = \emptyset$ it is the Jacobian ideal $(\partial_1 F, \dots, \partial_n F)$. For $\Delta = \{1, \dots, n\}$ it is $(x_1 \partial_1 F, \dots, x_n \partial_n F)$, the ideal of Section 3.3.

**Lemma 3.1.2.** For each $h \in R$, $\Theta(F + h^p) = \Theta(F)$.

Node: SG0000003E · Lean: `Singularity.logJacobian_add_pow`

*Proof.* For each derivation $D$, the Leibniz rule gives $D(h^p) = p h^{p-1} D(h) = 0$. So each generator of $\Theta(F + h^p)$ is the generator of $\Theta(F)$ with the same index. $\square$

So $\Theta(F)$ depends only on the hypersurface $f = 0$, the divisor $E$ and the coordinates $x$, not on the choice of $z$. A change of the coordinates $x$ that keeps $E$ maps the module of logarithmic derivations to itself, so it maps $\Theta(F)$ to the log-Jacobian ideal of the new $F$. Cossart used this ideal for a base of dimension $3$ in his thesis [Cos87]. Posva gives a modern account of its transformation law [Pos24, Appendix A].

*Lean.* The file `Singularity/Invariant/LogJacobianUnitLocal.lean` proves that a unit factor $u^p$ does not change the ideal, for a polynomial $u$ with $u(0) \ne 0$. In $K[x]$ the library has $\Theta(u^p F) = (u^p) \, \Theta(F)$ (`Singularity.logJacobian_pow_mul`). Such a $u$ is a unit in the local ring of $K[x]$ at the origin (`Singularity.isUnit_algebraMap_of_constantCoeff_ne_zero`), so $\Theta(u^p F)$ and $\Theta(F)$ have the same image in this ring (`Singularity.map_logJacobian_pow_mul_of_constantCoeff_ne_zero`). The units of $K[[x]]$ that are not polynomials are not in Lean.

*Lean.* The file `Singularity/Invariant/LogJacobianCoordinates.lean` proves the claim on the change of coordinates for the changes of $K[x]$ that keep $E$. Let $\varphi$ and $\psi$ be $K$-algebra endomorphisms of $K[x]$ with $\psi \circ \varphi = \mathrm{id}$, and let $\varphi(x_l) = c_l x_l$ with $c_l \in K$ for each $l \in \Delta$. The images of the other coordinates are arbitrary. The chain rule is $\partial_i \varphi(h) = \sum_l \varphi(\partial_l h) \, \partial_i \varphi(x_l)$ (`Singularity.pderiv_algHom`). Then $\Theta(\varphi(h)) \subseteq \varphi(\Theta(h))$ (`Singularity.logJacobian_le_map_of_adapted`), and if also $\varphi \circ \psi = \mathrm{id}$, then $\varphi(\Theta(h)) = \Theta(\varphi(h))$ (`Singularity.map_logJacobian_eq_of_adapted`). The changes of $K[[x]]$ with $x'_l = u_l x_l$ for a unit $u_l$ that is not a constant are not in Lean.

### The operators on monomials

The operators $x_i \partial_i$ and $\partial_j$ act on monomials one at a time:
$$x_i \partial_i (x^\alpha) = \alpha_i x^\alpha, \qquad \partial_j (x^\alpha) = \alpha_j x^{\alpha - e_j}.$$
The first keeps the degree and multiplies by the exponent $\alpha_i$. The second lowers the degree by one. In characteristic $0$, $x_i \partial_i$ kills only the monomials with $\alpha_i = 0$. In characteristic $p$ it kills every monomial with $p \mid \alpha_i$. A monomial is killed by all the operators exactly when all its exponents are divisible by $p$, that is, when it is a $p$-th power up to a constant. Cleaning removes these monomials. This is the reason why the theorem below needs a clean $F$.

### The dichotomy

Let $F \ne 0$ be clean, and write $F = x^r G$ as in Definition 1.3.3, with $r_i = 0$ for $i \notin \Delta$. Let $d = \operatorname{ord} G$ be the residual order. The Leibniz rule gives
$$x_i \partial_i F = x^r (r_i G + x_i \partial_i G) \ (i \in \Delta), \qquad \partial_j F = x^r \partial_j G \ (j \notin \Delta).$$
So $\Theta(F) = x^r \widetilde\Theta(G)$, where
$$\widetilde\Theta(G) = \bigl( r_i G + x_i \partial_i G \ (i \in \Delta), \ \partial_j G \ (j \notin \Delta) \bigr).$$
In Lean the factorization is `Singularity.logJacobian_monomial_mul` and `Singularity.logJacobian_eq_mul`.

**Definition 3.1.3.** The *residual order of the log-Jacobian ideal* is $\rho(F) = \operatorname{ord} \widetilde\Theta(G)$, the smallest order of an element of $\widetilde\Theta(G)$.

Node: SG0000003F · Lean: `Singularity.residualLogJacobian`, `Singularity.logJacobianOrder`

**Theorem 3.1.4.** Let $F \ne 0$ be clean, with $F = x^r G$ and $d = \operatorname{ord} G$ as above, and let $\rho = \rho(F)$.

1. For each $i \in \Delta$, the ideal $\widetilde\Theta(G)$ is not contained in $(x_i)$. So $x^r$ is the largest monomial in the variables of $\Delta$ that divides every element of $\Theta(F)$.
2. $d - 1 \le \rho \le d$.
3. $\rho = d - 1$ if and only if $\partial_j \operatorname{in}(G) \ne 0$ for some $j \notin \Delta$, where $\operatorname{in}(G)$ is the homogeneous part of degree $d$ of $G$.

Node: SG0000003F · Lean: `Singularity.residualLogJacobian_not_le_span_X`, `Singularity.le_divisorExponent_of_logJacobian_le` (part 1), `Singularity.logJacobianOrder_eq_or` (part 2), `Singularity.logJacobianOrder_add_one_eq_iff` (part 3)

*Proof.* Write $G = \sum_\alpha c_\alpha x^\alpha$. The coefficient of $x^\alpha$ in $r_i G + x_i \partial_i G$ is $(r_i + \alpha_i) c_\alpha$. The coefficient of $x^{\alpha - e_j}$ in $\partial_j G$ is $\alpha_j c_\alpha$. The monomial $x^{r + \alpha}$ is a monomial of $F$ with the coefficient $c_\alpha$.

Part 1. Fix $i \in \Delta$. By the choice of $r_i$, the factor $G$ is not divisible by $x_i$, so some $\alpha$ with $c_\alpha \ne 0$ has $\alpha_i = 0$. Assume that every generator of $\widetilde\Theta(G)$ lies in $(x_i)$. Then the coefficient of $x^\alpha$ in each generator $r_k G + x_k \partial_k G$ is $0$, so $p \mid r_k + \alpha_k$ for each $k \in \Delta$. The monomial $x^{\alpha}$ is not divisible by $x_i$, so the monomial $x^{\alpha - e_j}$ of $\partial_j G$ is not divisible by $x_i$ either, and its coefficient $\alpha_j c_\alpha$ must be $0$. So $p \mid \alpha_j = r_j + \alpha_j$ for each $j \notin \Delta$. Thus every exponent of the monomial $x^{r + \alpha}$ of $F$ is divisible by $p$. This contradicts the cleanness of $F$.

Part 2. Each generator has order at least $d - 1$, so $\rho \ge d - 1$. Take $\alpha$ with $c_\alpha \ne 0$ and $|\alpha| = d$. Since $F$ is clean, some exponent $r_k + \alpha_k$ of $x^{r + \alpha}$ is not divisible by $p$. If $k \in \Delta$, the generator $r_k G + x_k \partial_k G$ contains the term $(r_k + \alpha_k) c_\alpha x^\alpha \ne 0$ of degree $d$. If $k \notin \Delta$, then $r_k = 0$, and $\partial_k G$ contains the term $\alpha_k c_\alpha x^{\alpha - e_k} \ne 0$ of degree $d - 1$. In both cases a generator has order at most $d$, so $\rho \le d$.

Part 3. The generators $r_i G + x_i \partial_i G$ have order at least $d$. An element $\sum_k u_k g_k$ of $\widetilde\Theta(G)$ has order at least the minimum of the orders of the generators $g_k$, so $\rho$ is the minimum of the orders of the generators. So $\rho = d - 1$ if and only if some $\partial_j G$ with $j \notin \Delta$ has order $d - 1$. The homogeneous part of degree $d - 1$ of $\partial_j G$ is $\partial_j \operatorname{in}(G)$. $\square$

The proof never uses the number of variables. The same argument works for each $n$, and in particular for a base of dimension $4$, where the open case lives. Part 1 says that the monomial factor of $F$ can be read from the ideal $\Theta(F)$, which does not depend on the choice of $z$. Part 2 says that the residual order $d$ of $F$ is pinned by the invariant $\rho$: $d \in \{\rho, \rho + 1\}$.

**Definition 3.1.5.** The *type* of $F$ is $\tau = d - \rho \in \{0, 1\}$.

Type $1$ means that the initial form of $G$ depends on a variable $x_j$ with $j \notin \Delta$, in a way that is not a $p$-th power in $x_j$. Type $0$ means that it does not.

*Lean.* The file `Singularity/Invariant/LogJacobianTau.lean` proves the definition and its properties for polynomials in fixed coordinates. The type is `Singularity.logJacobianType`, with $d$ the residual order `Singularity.residualOrderAlong`. For a clean $F$, $d = \rho + \tau$ (`Singularity.residualOrderAlong_eq_logJacobianOrder_add_logJacobianType`), and $\tau$ is $0$ or $1$ (`Singularity.logJacobianType_le_one`, `Singularity.logJacobianType_eq_zero_or_eq_one`). The type is $0$ if and only if $\rho = d$ (`Singularity.logJacobianType_eq_zero_iff`), and for $F \ne 0$ it is $1$ if and only if $\rho + 1 = d$ (`Singularity.logJacobianType_eq_one_iff`). The type is $1$ if and only if $\partial_j \operatorname{in}(G) \ne 0$ for some $j \notin \Delta$ (`Singularity.logJacobianType_eq_one_iff_pderiv`), and $0$ if and only if $\partial_j \operatorname{in}(G) = 0$ for each $j \notin \Delta$ (`Singularity.logJacobianType_eq_zero_iff_pderiv`). These are the two sentences above. For the changes of coordinates $\varphi$ of $K[x]$ above, the file `Singularity/Invariant/LogJacobianCoordinates.lean` proves more. Let $F \ne 0$ be clean and let $F'$ have $\Theta(F') = \varphi(\Theta(F))$, for example $F' = \varphi(F) + h^p$ (`Singularity.logJacobian_map_add_pow_eq`). Then the clean part of $F'$ is not $0$, it has the same exponents $r$ along $\Delta$ and the same $\rho$ (`Singularity.cleanPart_ne_zero_of_adapted`, `Singularity.divisorExponent_cleanPart_eq_of_adapted`, `Singularity.logJacobianOrder_cleanPart_eq_of_adapted`), and its residual order $d'$ satisfies $\rho \le d' \le \rho + 1$ (`Singularity.logJacobianOrder_le_residualOrderAlong_of_adapted`, `Singularity.residualOrderAlong_le_logJacobianOrder_add_one_of_adapted`). Lean does not prove the bound $\rho \le d^{\max} \le \rho + 1$ for the largest residual order over all coordinates of $K[[x]]$ adapted to $E$, because the changes $x'_l = u_l x_l$ with a unit $u_l$ that is not a constant are not covered.

**Example 3.1.6.** Let $p = 2$, $n = 2$, $\Delta = \emptyset$ and $F = x^2 y + x y^2$. This $F$ is clean. Here $r = 0$, $G = F$ and $d = 3$. The derivatives are $\partial_x F = y^2$ and $\partial_y F = x^2$, since $2 = 0$. So $\Theta(F) = (x^2, y^2)$, and $\rho = 2 = d - 1$. The type is $1$. Now let $\Delta = \{1, 2\}$. Then $r = (1, 1)$, $G = x + y$, $d = 1$, and
$$\widetilde\Theta(G) = \bigl( 1 \cdot G + x, \ 1 \cdot G + y \bigr) = (y, x),$$
so $\rho = 1 = d$, and the type is $0$.

**Example 3.1.7.** Let $p = 3$, $\Delta = \emptyset$ and $F = x^3 y$. Then $\partial_x F = 0$ and $\partial_y F = x^3$, so $\rho = 3$ and $d = 4$. The type is $1$. The variable $x$ appears only as a cube, and the derivative in $y$ lowers the degree by one.

The Lean library states the dichotomy for $R = K[x]$, over a field $K$ of characteristic $p$. The proofs do not use that $p$ is prime. The case $R = K[[x]]$ is not in Lean yet.

**Remark 3.1.8 (the case $q = p^e$ with $e \ge 2$).** Let the equation be $f = z^q + F$ with $q = p^e$. The change $z \mapsto z + h$ replaces $F$ by $F + h^q$, so an invariant must see the class of $F$ modulo $q$-th powers. For $e \ge 2$ the ideal $\Theta(F)$ sees less. By Lemma 3.1.2 it does not change when we add a $p$-th power, and a $p$-th power need not be a $q$-th power. For example, let $p = 2$, $q = 4$, $\Delta = \emptyset$ and $F = x^2 y^2$. Each derivation kills $F$, so $\Theta(F) = 0$, but $F$ is not a polynomial in $x^4$ and $y^4$. The Hasse-Schmidt derivative $\partial^{((2, 0))}$ of Volume 1, Section 6.3 sends $F$ to $y^2$. In general, $F$ is a polynomial in $x_1^q, \dots, x_n^q$ if and only if $\partial^{(\beta)}(F) = 0$ for each $\beta \ne 0$ with $\beta_i < q$ for each $i$ (Volume 1, Corollary 6.3.7). For $R = K[x]$ and such $\beta$, this gives $\partial^{(\beta)}(h^q) = 0$, so $\partial^{(\beta)}(F + h^q) = \partial^{(\beta)}(F)$, as in Lemma 3.1.2. So for $e \ge 2$ an invariant of this kind must use the operators $\partial^{(\beta)}$ with $\beta_i < q$ in place of the derivations.

Node: SG0000004N · Lean: `Singularity.Algebra.MvHasse.exists_expand_eq_iff_hasseDeriv`

### Notes and references

For a base of dimension $3$, the ideal $\Theta(F)$ and its order appear in the thesis of Cossart [Cos87], and Cossart and Piltant use it in their proof of resolution of threefolds [CP08]. The transformation law under blowups is in [Pos24, Appendix A]. The dichotomy of Theorem 3.1.4 holds in each dimension. Section 3.2 shows that $\rho$ does not go up under a point blowup. For a base of dimension $4$, the question whether a sequence of blowups makes $\rho$ drop is open.
