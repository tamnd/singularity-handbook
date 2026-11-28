---
title: The log Jacobian criterion for a step of degree $p$
nodes: []
sources: [Tem13, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The log Jacobian criterion for a step of degree $p$

Section 4.3 reduced the step of degree $p$ to an equation $\theta^p = f$ where $f$ is monomial modulo $p$-th powers (Definition 4.3.4), and it stated weak log monomialization as a hypothesis (Definition 4.3.15). The condition on $f$ depends on the choice of an element $h$ with $f - h^p$ of a special form. At the end of Section 4.3 we saw that along a valuation with a defect the values of $f - h^p$ have no maximum. In this section we replace the condition by a condition on an ideal that does not depend on such a choice. Let $D$ be a normal crossings divisor at the center, given by a part of a regular system of parameters. The *log Jacobian ideal* $J_D(f)$ is the ideal of the values $\delta(f)$ of the derivations $\delta$ that are tangent to $D$. It does not change when we add a $p$-th power to $f$. We prove that $J_D(f)$ is principal for some $D$ if and only if $f$ lies in the field $E^p(t)$ for an element $t$ of monomial type (Proposition 4.4.15, Theorem 4.4.16 and Corollary 4.4.17). We call such an $f$ *foliated monomial*. This weaker form is sufficient for the step of degree $p$, because $E(f^{1/p}) = E(t^{1/p})$ (Proposition 4.4.8 and Theorem 4.4.11). Then we compute the log Jacobian ideal after a blow-up (Lemma 4.4.18). This section does not prove that a model with a principal log Jacobian ideal exists along a valuation. This existence is open in transcendence degree 4 and more. So the open case of local uniformization stays open.

### Coordinates and log derivations

In this section $k$ is a perfect field of characteristic $p > 0$, except in Definitions 4.4.6 and 4.4.9, Propositions 4.4.7, 4.4.8 and 4.4.10, Theorem 4.4.11 and Lemmas 4.4.13 and 4.4.14, which state their own hypotheses. Let $R$ be a regular local ring that is essentially of finite type over $k$, that is, a localization of a finitely generated $k$-algebra at a prime ideal. Let $\mathfrak{m}$ be its maximal ideal, $\kappa$ its residue field and $E$ its fraction field. Let $d = \dim R$ and $\tau = \operatorname{trdeg}_k \kappa$. The dimension formula [Mat, Section 15] gives $\operatorname{trdeg}_k E = d + \tau$. We write $n = d + \tau$.

We use these facts on differentials of fields [Mat, Section 26]. Let $K$ be a field that is finitely generated over $k$, of transcendence degree $m$. Since $k$ is perfect, $k$ lies in the subfield $K^p$ of $p$-th powers. A family $B \subseteq K$ is *$p$-independent* if the monomials $\prod_{b} b^{c_b}$ with $0 \le c_b < p$ and finitely many $c_b \ne 0$ are linearly independent over $K^p$. It is a *$p$-basis* if it is $p$-independent and these monomials also span $K$ over $K^p$.

- (F1) The family $B$ is $p$-independent if and only if the elements $db$, $b \in B$, are linearly independent in $\Omega_{K/k}$. It is a $p$-basis if and only if the $db$ are a basis of $\Omega_{K/k}$.
- (F2) Each $p$-independent family is contained in a $p$-basis.
- (F3) The field $K$ has a separating transcendence basis $b_1, \dots, b_m$ over $k$, and $db_1, \dots, db_m$ is a basis of $\Omega_{K/k}$. So $\dim_K \Omega_{K/k} = m$.

For one element $x \in K$, the family $\{x\}$ is $p$-independent if and only if $x \notin K^p$. So (F1) gives: $dx = 0$ if and only if $x \in K^p$.

**Lemma 4.4.1 (coordinates).** Let $z_1, \dots, z_d$ be a regular system of parameters of $R$, and let $w_1, \dots, w_\tau \in R$ be elements whose classes are a separating transcendence basis of $\kappa/k$. Then:

1. $\Omega_{R/k}$ is a free $R$-module with the basis $dz_1, \dots, dz_d, dw_1, \dots, dw_\tau$;
2. $\operatorname{Der}_k(R)$ is a free $R$-module with the dual basis $\partial_{z_1}, \dots, \partial_{z_d}, \partial_{w_1}, \dots, \partial_{w_\tau}$, and each $\delta \in \operatorname{Der}_k(R)$ is $\sum_i \delta(z_i)\partial_{z_i} + \sum_j \delta(w_j)\partial_{w_j}$;
3. the derivations $\partial_{z_i}$, $\partial_{w_j}$ commute, and the $p$-th power of each of them is $0$;
4. each $\delta \in \operatorname{Der}_k(R)$ extends in a unique way to a derivation of $E$, and $\operatorname{Der}_k(E)$ is an $E$-vector space with the same basis. An element of $\operatorname{Der}_k(E)$ is determined by its values on the $z_i$ and the $w_j$.

Lean: none yet

We call such a family a *family of coordinates* of $R$. It exists, because $\kappa$ is finitely generated over $k$ and (F3) applies to $\kappa$.

*Proof.* The module $\Omega_{R/k}$ is finitely generated, because $R$ is essentially of finite type over $k$. The sequence
$$\mathfrak{m}/\mathfrak{m}^2 \to \Omega_{R/k} \otimes_R \kappa \to \Omega_{\kappa/k} \to 0,$$
where the first map sends the class of $g$ to $dg \otimes 1$, is exact [Mat, Section 25]. The classes of the $z_i$ generate $\mathfrak{m}/\mathfrak{m}^2$, and the elements $d\bar{w}_j$ are a basis of $\Omega_{\kappa/k}$ by (F3). So the $n$ elements $dz_i \otimes 1$ and $dw_j \otimes 1$ generate $\Omega_{R/k} \otimes_R \kappa$. By Nakayama's lemma, the $dz_i$ and $dw_j$ generate $\Omega_{R/k}$. Let $\varphi \colon R^n \to \Omega_{R/k}$ be the surjective map that sends the standard basis to these elements, and let $N$ be its kernel. The field $E$ is a localization of $R$, so $\Omega_{R/k} \otimes_R E = \Omega_{E/k}$, and this space has dimension $\operatorname{trdeg}_k E = n$ by (F3). Localization is exact, so $E^n \to \Omega_{E/k}$ is a surjective map of $E$-vector spaces of the same dimension $n$. It is injective, so $N \otimes_R E = 0$. Each element of $N$ is then killed by a nonzero element of $R$. But $N \subseteq R^n$ and $R$ is a domain, so $N = 0$. This proves part 1. Part 2 follows, because $\operatorname{Der}_k(R) = \operatorname{Hom}_R(\Omega_{R/k}, R)$, with $\delta(g) = dg(\delta)$.

Part 3. The bracket $[\delta, \delta'] = \delta\delta' - \delta'\delta$ of two $k$-derivations is a $k$-derivation. In characteristic $p$ the $p$-th power of a derivation is a derivation, because $\delta^p(ab) = \sum_i \binom{p}{i}\delta^i(a)\delta^{p-i}(b) = a\delta^p(b) + b\delta^p(a)$. By part 2 a derivation that is zero on all the coordinates is zero. Each $\partial$ of the basis sends each coordinate to $0$ or $1$, and it sends $0$ and $1$ to $0$. So each bracket $[\partial, \partial']$ is zero on the coordinates, and $\partial^p(v) = \partial^{p-1}(\partial v) = 0$ for each coordinate $v$, since $p \ge 2$. Thus the brackets and the $p$-th powers are zero.

Part 4. The derivations of $E$ are the $E$-linear maps $\Omega_{E/k} = \Omega_{R/k} \otimes_R E \to E$. Such a map is given by its values on the basis of part 1. So the $R$-linear map $\Omega_{R/k} \to R$ of $\delta$ extends in a unique way, and the claims follow. $\square$

For $\omega \in \Omega_{E/k}$ and $\delta \in \operatorname{Der}_k(E)$ we write $\omega(\delta) \in E$ for the value of the linear map of $\delta$ at $\omega$. So $dg(\delta) = \delta(g)$.

**Definition 4.4.2 (log derivations and the log Jacobian ideal).** Let $B$ be a domain that contains $k$, and let $G \subseteq B$ be a finite set. The module of derivations *tangent to $G$* is
$$T_G(B) = \{\delta \in \operatorname{Der}_k(B) : \delta(gB) \subseteq gB \text{ for each } g \in G\}.$$
For $f \in B$, the set $J_G(f) = \{\delta(f) : \delta \in T_G(B)\}$ is an ideal of $B$, because $T_G(B)$ is a $B$-module. A *normal crossings divisor* of $R$ is a set $D = \{x_1, \dots, x_r\}$ of distinct elements of a regular system of parameters of $R$. For such $D$ we call $T_D = T_D(R)$ the module of *log derivations*, and $J_D(f)$ the *log Jacobian ideal* of $f$. A family of coordinates is *adapted to $D$* if its regular system of parameters contains $x_1, \dots, x_r$. Then we write $y_1, \dots, y_s$ for the other coordinates, with $r + s = n$. Some $y_j$ are regular parameters and the others are the units $w_j$. Let $\Omega_R(\log D)$ be the $R$-submodule of $\Omega_{E/k}$ generated by the elements $d\log x_i = dx_i/x_i$ and $dy_j$.

Lean: none yet

**Lemma 4.4.3 (log derivations in coordinates).** Let $D = \{x_1, \dots, x_r\}$ be a normal crossings divisor of $R$, with an adapted family of coordinates.

1. $T_D$ is a free $R$-module with the basis $x_1\partial_{x_1}, \dots, x_r\partial_{x_r}, \partial_{y_1}, \dots, \partial_{y_s}$.
2. $T_D$ is closed under the bracket and under $\delta \mapsto \delta^p$.
3. $\Omega_R(\log D)$ is a free $R$-module with the basis $d\log x_i$, $dy_j$, and this basis is dual to the basis of part 1. It contains $\Omega_{R/k}$. An element $\omega \in \Omega_{E/k}$ lies in $\Omega_R(\log D)$ if and only if $\omega(\delta) \in R$ for each $\delta \in T_D$.
4. For $f \in R$ we have
$$df = \sum_i x_i\partial_{x_i}(f)\, d\log x_i + \sum_j \partial_{y_j}(f)\, dy_j,$$
and $J_D(f)$ is the ideal generated by the coefficients of $df$ in this basis.

Lean: none yet

*Proof.* Part 1. Let $\delta \in \operatorname{Der}_k(R)$. By Lemma 4.4.1, $\delta = \sum_i \delta(x_i)\partial_{x_i} + \sum_j \delta(y_j)\partial_{y_j}$. If $\delta \in T_D$, then $\delta(x_i) = x_i g_i$ with $g_i \in R$, and $\delta = \sum_i g_i\, x_i\partial_{x_i} + \sum_j \delta(y_j)\partial_{y_j}$. Conversely each such combination sends $x_i$ into $x_iR$, and then $\delta(x_i h) = x_i(g_i h + \delta h) \in x_iR$. The family is linearly independent, because the $\partial$ are, and $R$ is a domain.

Part 2. Let $\delta, \delta' \in T_D$ with $\delta(x_i) = x_i g_i$ and $\delta'(x_i) = x_i g'_i$. Then $[\delta, \delta'](x_i) = \delta(x_i g'_i) - \delta'(x_i g_i) = x_i(g_i g'_i + \delta g'_i - g'_i g_i - \delta' g_i) \in x_iR$. Each $\delta \in T_D$ maps $x_iR$ into $x_iR$, so $\delta^p(x_i) \in x_iR$. The $p$-th power is a derivation by the proof of Lemma 4.4.1.

Part 3. In $\Omega_{E/k}$ the elements $d\log x_i$ and $dy_j$ are a basis over $E$, because they differ from the basis $dx_i$, $dy_j$ by the nonzero factors $1/x_i$. We have $d\log x_i(x_l\partial_{x_l}) = x_l\partial_{x_l}(x_i)/x_i$, which is $1$ for $l = i$ and $0$ otherwise, and $d\log x_i(\partial_{y_j}) = 0$. In the same way $dy_j(x_l\partial_{x_l}) = 0$ and $dy_j(\partial_{y_l})$ is $1$ for $l = j$ and $0$ otherwise. So the two bases are dual. An element $\omega$ of $\Omega_{E/k}$ has the coefficients $\omega(x_i\partial_{x_i})$ and $\omega(\partial_{y_j})$ in the basis, so $\omega \in \Omega_R(\log D)$ if and only if these values are in $R$, and then $\omega(\delta) \in R$ for each $\delta \in T_D$ by part 1. Since $dx_i = x_i\, d\log x_i$, the module $\Omega_{R/k}$ lies in $\Omega_R(\log D)$.

Part 4. The coefficients of $df$ are $df(x_i\partial_{x_i}) = x_i\partial_{x_i}(f)$ and $df(\partial_{y_j}) = \partial_{y_j}(f)$. By part 1, $J_D(f)$ is generated by the values of $f$ under the basis of $T_D$, and these are the coefficients. $\square$

The definition of $T_D$ uses only the ideals $x_iR$. So $T_D$ and $J_D(f)$ do not change when we multiply an $x_i$ by a unit, and they do not depend on the family of coordinates. The module $\Omega_R(\log D)$ is the module of logarithmic differentials of the log structure on $\operatorname{Spec} R$ that the divisor $D$ defines, in the sense of K. Kato, Logarithmic structures of Fontaine-Illusie (1989). We do not use log structures in this section.

**Lemma 4.4.4 (first properties).** Let $D$ be a normal crossings divisor of $R$, and let $f \in R$.

1. $J_D(f + h^p) = J_D(f)$ for each $h \in R$.
2. $J_D(f) = 0$ if and only if $f \in E^p$.
3. If $D \subseteq D_1$ for a normal crossings divisor $D_1$, then $J_{D_1}(f) \subseteq J_D(f)$.

Lean: none yet

*Proof.* Part 1. For each derivation $\delta$ we have $\delta(h^p) = p h^{p-1}\delta(h) = 0$. Part 2. If $f = g^p$ with $g \in E$, then $\delta(f) = 0$ for the extension of each $\delta \in T_D$ to $E$. Conversely, if $J_D(f) = 0$, then all the coefficients of $df$ in Lemma 4.4.3, part 4, are zero, so $df = 0$ in $\Omega_{E/k}$, and $f \in E^p$ by (F1). Part 3. Each $\delta \in T_{D_1}$ preserves the ideals $xR$ for $x \in D_1$, so in particular for $x \in D$. Thus $T_{D_1} \subseteq T_D$. $\square$

Part 1 is the main point of the log Jacobian ideal. The condition of Definition 4.3.4 asks for a good choice of $h$. The ideal $J_D(f)$ sees only the class of $f$ modulo $p$-th powers.

**Lemma 4.4.5 (first integrals).** Let $t \in E$ with $t \notin E^p$, and let $f \in E$. Then the following are equivalent:

1. $f \in E^p(t)$;
2. $f = \sum_{i=0}^{p-1} c_i^p t^i$ with $c_0, \dots, c_{p-1} \in E$;
3. $df \in E\, dt$ in $\Omega_{E/k}$.

Lean: none yet

*Proof.* The element $t^p$ lies in $E^p$, and it is not a $p$-th power of an element of $E^p$: if $t^p = c^p$ with $c \in E^p$, then $t = c$ by the injectivity of $c \mapsto c^p$. By the fact on fields before Theorem 4.3.2, the polynomial $X^p - t^p$ is irreducible over $E^p$. So $E^p(t) = E^p[t]$ has the basis $1, t, \dots, t^{p-1}$ over $E^p$, and parts 1 and 2 are equivalent. If part 2 holds, then $df = \big(\sum_i i c_i^p t^{i-1}\big)\, dt$, because $d(c_i^p) = 0$. Conversely, assume part 3. By (F1) the family $\{t\}$ is $p$-independent. By (F2) and (F1) it is contained in a $p$-basis $t = b_1, b_2, \dots, b_n$ of $E$, with $n = \dim_E \Omega_{E/k}$ elements. The monomials $b^c = b_1^{c_1} \cdots b_n^{c_n}$ with $0 \le c_l < p$ are a basis of $E$ over $E^p$. Write $f = \sum_c a_c^p b^c$ with $a_c \in E$. Then
$$df = \sum_{l=1}^n \Big(\sum_{c : c_l \ge 1} c_l\, a_c^p\, b^{c - e_l}\Big)\, db_l,$$
where $e_l$ is the $l$-th unit vector. The $db_l$ are a basis of $\Omega_{E/k}$ by (F1), and $df \in E\, db_1$. So for $l \ge 2$ the coefficient of $db_l$ is zero. In this coefficient the monomials $b^{c - e_l}$ for the different $c$ with $c_l \ge 1$ are different elements of the basis of $E$ over $E^p$, and the coefficients $c_l a_c^p$ are in $E^p$. So $c_l a_c^p = 0$ for each $c$ with $c_l \ge 1$. Since $1 \le c_l \le p - 1$, the integer $c_l$ is a unit, and $a_c = 0$. Thus $a_c = 0$ unless $c = j e_1$ for some $j < p$, and $f = \sum_{j < p} a_{je_1}^p t^j$. This is part 2. $\square$

An element $t$ with $df \in E\,dt$ is a *first integral* of the derivations that kill $f$: if $\delta(f) = 0$ and $df = c\,dt$, then $c\,\delta(t) = 0$. The derivations that kill $f$ form a foliation of corank one, and this is the origin of the name in the next definition.

### Elements of monomial type and foliated monomial elements

**Definition 4.4.6 (monomial type and foliated monomial elements).** Let $R$ be a regular local ring of characteristic $p$, with maximal ideal $\mathfrak{m}$, residue field $\kappa$ and fraction field $E$. An element $t \in R$ has *monomial type* if one of these two conditions holds:

1. (the ramified type) $t = u \prod_{x \in s} x^{a_x}$ for a regular system of parameters $s$ of $R$, a unit $u$ and integers $a_x \ge 0$, with $p \nmid a_x$ for some $x \in s$;
2. (the residual type) $t$ is a unit of $R$, and its class in $\kappa$ is not a $p$-th power in $\kappa$.

An element $f \in R$ is *foliated monomial in $R$* if there are an element $t \in R$ of monomial type and elements $c_0, \dots, c_{p-1} \in E$ with
$$f = \sum_{i=0}^{p-1} c_i^p\, t^i.$$

Lean: `Singularity.IsMonomialType`, `Singularity.IsFoliatedMonomial`

In Lean the residual type is written as $t = u\prod_{x \in s} x^{a_x}$ with all $a_x = 0$. In a regular local ring this is the same condition (`Singularity.IsMonomialType.of_isUnit`, `Singularity.IsMonomialType.isUnit_of_residual`). If $t \notin E^p$, the condition on $f$ is $f \in E^p(t)$, by the proof of Lemma 4.4.5.

**Proposition 4.4.7 (monomial modulo $p$-th powers).** Let $R$ be a regular local ring of characteristic $p$, with fraction field $E$.

1. An element $t$ of monomial type is monomial modulo $p$-th powers in $R$, with $h = 0$ and $g = 1$.
2. An element $f$ that is monomial modulo $p$-th powers in $R$ is foliated monomial in $R$.

Lean: `Singularity.IsMonomialType.isMonomialModPow` (part 1), `Singularity.IsMonomialModPow.isFoliatedMonomial` (part 2)

*Proof.* Part 1. In the ramified type, $t = 0^p + 1^p \cdot u\prod_{x \in s} x^{a_x}$ is of the ramified type of Definition 4.3.4. In the residual type, choose a regular system of parameters $s$ and all exponents $0$. Then $t = 0^p + 1^p \cdot t$ is of the residual type of Definition 4.3.4. Part 2. Let $f = h^p + g^p u x_1^{a_1} \cdots x_d^{a_d}$ as in Definition 4.3.4, and let $t = u x_1^{a_1} \cdots x_d^{a_d}$. In the ramified type of Definition 4.3.4, $t$ is of the ramified type. In the residual type, all $a_i = 0$, so $t = u$ is a unit whose class is not a $p$-th power. So $t$ has monomial type. Since $p \ge 2$, we can take $c_0 = h$, $c_1 = g$ and $c_i = 0$ for $2 \le i \le p - 1$. $\square$

The converse of part 2 is false. Example 4.4.20 gives a foliated monomial element that is not monomial modulo $p$-th powers in $R$. For the step of degree $p$ the weaker form is sufficient, by the next proposition.

**Proposition 4.4.8 (the same extension).** Let $E$ be a field of characteristic $p$, and let $f, t \in E$ with $f = \sum_{i < p} c_i^p t^i$ for some $c_i \in E$. Assume that $f \notin E^p$. Then:

1. $t \notin E^p$;
2. there are $d_0, \dots, d_{p-1} \in E$ with $t = \sum_{i < p} d_i^p f^i$;
3. let $E'$ be a field extension of $E$, and let $\theta, \theta' \in E'$ with $\theta^p = f$ and $\theta'^p = t$. Then $E(\theta) = E(\theta')$.

In words, $E(f^{1/p}) = E(t^{1/p})$.

Lean: `Singularity.not_exists_pow_eq_of_eq_sum` (part 1), `Singularity.exists_eq_sum_of_eq_sum` (part 2), `Singularity.adjoin_eq_adjoin_of_eq_sum` (part 3)

*Proof.* Part 1. If $t = s^p$ with $s \in E$, then $f = \sum_i c_i^p s^{pi} = \big(\sum_i c_i s^i\big)^p$, which is false.

Part 2. Let $F = E^p$, a subfield of $E$. Let $x \in E$ with $x \notin F$. As in the proof of Lemma 4.4.5, the polynomial $X^p - x^p$ is irreducible over $F$, so $[F(x) : F] = p$ and $F(x) = F[x]$. We apply this to $x = f$ and to $x = t$, which is possible by part 1. The formula for $f$ shows $f \in F[t]$, so $F(f) \subseteq F(t)$. Both fields have degree $p$ over $F$, so $F(f) = F(t)$. Thus $t \in F[f]$, and $t = q(f)$ for a polynomial $q \in F[X]$. Let $q_0$ be the remainder of $q$ on division by $X^p - f^p \in F[X]$. Then $q_0(f) = q(f) = t$, and $q_0$ has degree less than $p$. Its coefficients are in $F = E^p$, so they have the form $d_i^p$.

Part 3. By part 2, $\big(\sum_i d_i\theta^i\big)^p = \sum_i d_i^p f^i = t = \theta'^p$. In characteristic $p$ the map $y \mapsto y^p$ of $E'$ is injective, so $\theta' = \sum_i d_i\theta^i \in E(\theta)$. In the same way $\big(\sum_i c_i\theta'^i\big)^p = f = \theta^p$, so $\theta = \sum_i c_i\theta'^i \in E(\theta')$. $\square$

Now we state the hypothesis of Section 4.3 with the weaker form. The setting is that of Definition 4.3.15.

**Definition 4.4.9 (foliated log monomialization).** Let $k$ be a field of characteristic $p > 0$, and let $n \ge 0$. *Foliated log monomialization along a valuation holds in transcendence degree $n$ over $k$*, and we write $\mathrm{FLM}(n, k)$, if the following is true. Let $E$ be a field extension of $k$ with $\operatorname{trdeg}_k E = n$, let $v$ be a valuation of $E$, and let $A$ be an affine model of $E/k$ with $A \subseteq \mathcal{O}_v$ whose local ring at the center of $v$ is regular. Let $f \in A$ be an element that is not a $p$-th power in $E$. Then there is an affine model $A'$ of $E/k$ with $A \subseteq A' \subseteq \mathcal{O}_v$ whose local ring $R'$ at the center of $v$ is regular, such that $f$ is foliated monomial in $R'$.

Lean: `Singularity.FoliatedLogMonomialization`

**Proposition 4.4.10 (weak log monomialization gives the foliated form).** Let $k$ be a field of characteristic $p > 0$, and let $n \ge 0$. Then $\mathrm{WLM}(n, k)$ implies $\mathrm{FLM}(n, k)$.

Lean: `Singularity.foliatedLogMonomialization_of_weakLogMonomialization`

*Proof.* The model $A'$ of $\mathrm{WLM}(n, k)$ has the properties of $\mathrm{FLM}(n, k)$, by Proposition 4.4.7, part 2. $\square$

**Theorem 4.4.11 (the step from foliated log monomialization).** Let $k$ be a field of characteristic $p > 0$, let $n \ge 0$, and assume $\mathrm{FLM}(n, k)$. Then the step of degree $p$ holds in transcendence degree $n$ over $k$.

Lean: `Singularity.regularCenterInseparableStep_of_foliatedLogMonomialization` (the Lean theorem takes the monomial step `Singularity.MonomialInseparableStep` as a second hypothesis)

*Proof.* Let $E$, $E'$, $w$, $v$ and $S$ be as in Definition 4.3.1, and assume that $v$ has a regular center on an affine model $A_0$ of $E/k$ that contains $S$. By Lemma 4.3.3 there is $\theta \in E' \setminus E$ with $f = \theta^p \in A_0$, and $f$ is not a $p$-th power in $E$. By $\mathrm{FLM}(n, k)$ there is an affine model $A'$ of $E/k$ with $A_0 \subseteq A' \subseteq \mathcal{O}_v$ whose local ring $R'$ at the center of $v$ is regular, an element $t \in R'$ of monomial type and elements $c_i \in E$ with $f = \sum_{i < p} c_i^p t^i$. By Proposition 4.4.8 there is $\theta' \in E'$ with $\theta'^p = t$, namely $\theta' = \sum_i d_i \theta^i$. By Proposition 4.4.8, part 1, $t$ is not a $p$-th power in $E$, so $\theta' \notin E$. By Proposition 4.4.7, part 1, $t$ is monomial modulo $p$-th powers in $R'$. Theorem 4.3.14, applied to $A'$ and $\theta'$, gives a regular center of $w$ on an affine model of $E'/k$ that contains $A'$. This model contains $S$. $\square$

**Corollary 4.4.12.** Let $k$ be a perfect field of characteristic $p > 0$, let $n \ge 0$, and assume $\mathrm{FLM}(n, k)$. Then for each function field $K/k$ of transcendence degree $n$, each valuation of $K/k$ has local uniformization.

Lean: `Singularity.hasLocalUniformization_of_foliatedLogMonomialization` (the Lean theorem takes the theorem of Temkin `Singularity.localUniformization_inseparable` and the monomial step `Singularity.MonomialInseparableStep` as hypotheses)

*Proof.* Theorem 4.4.11 and Theorem 4.3.2. $\square$

### Two lemmas on derivations in characteristic $p$

The proof of the criterion uses two kinds of derivations: derivations $\delta$ with $\delta^p = 0$, which behave like partial derivatives, and derivations $\delta$ with $\delta^p = \delta$, which behave like the Euler derivation $x\partial_x$. The next two lemmas describe them. In both lemmas the rings are commutative and contain $\mathbb{F}_p$, and a derivation of a ring $A$ is an additive map $\delta \colon A \to A$ with $\delta(ab) = a\delta(b) + b\delta(a)$. The integers $1, \dots, p - 1$ are units in $A$, so $c!$ is a unit for $c < p$.

**Lemma 4.4.13 (Taylor).** Let $A$ be a ring of characteristic $p$, let $\delta_1, \dots, \delta_s$ be commuting derivations of $A$ with $\delta_j^p = 0$, and let $y_1, \dots, y_s \in A$ with $\delta_j(y_l) = 1$ if $j = l$ and $\delta_j(y_l) = 0$ if $j \ne l$. Let $A' = \bigcap_j \ker \delta_j$, a subring of $A$. Then $A$ is a free $A'$-module with the basis of the monomials $y^c = y_1^{c_1} \cdots y_s^{c_s}$, $0 \le c_j < p$.

Lean: `Singularity.taylorBasis`; the case of one derivation is `Singularity.exists_taylor` (existence) and `Singularity.taylor_coeff_unique` (uniqueness)

*Proof.* The kernel of a derivation is a subring, so $A'$ is a subring. For $g \in A'$ and $a \in A$ we have $\delta_j(ga) = g\delta_j(a)$.

The case $s = 1$. Write $\delta = \delta_1$ and $y = y_1$. For $g \in A$ let
$$P(g) = \sum_{c=0}^{p-1} \frac{(-y)^c}{c!}\, \delta^c(g).$$
We have $\delta((-y)^c) = -c(-y)^{c-1}$. So
$$\delta P(g) = -\sum_{c=1}^{p-1} \frac{(-y)^{c-1}}{(c-1)!}\delta^c(g) + \sum_{c=0}^{p-1} \frac{(-y)^c}{c!}\delta^{c+1}(g) = \frac{(-y)^{p-1}}{(p-1)!}\delta^p(g) = 0,$$
since the first sum is the second sum without its last term. So $P(g) \in A'$. Next,
$$\sum_{c=0}^{p-1} \frac{y^c}{c!} P(\delta^c g) = \sum_{c=0}^{p-1}\sum_{e=0}^{p-1} \frac{y^c(-y)^e}{c!\,e!}\, \delta^{c+e}(g).$$
The terms with $c + e \ge p$ are zero, because $\delta^p = 0$. For $N = c + e < p$ the coefficient of $y^N\delta^N(g)$ is $\sum_{c+e=N} (-1)^e/(c!\,e!) = (1/N!)\sum_{e=0}^N \binom{N}{e}(-1)^e = (1 - 1)^N/N!$. This is $1$ for $N = 0$ and $0$ for $N \ge 1$. So the sum is $g$, and $g$ is a combination of $1, y, \dots, y^{p-1}$ with the coefficients $P(\delta^c g)/c! \in A'$. For the independence, let $\sum_{c < p} g_c y^c = 0$ with $g_c \in A'$, not all zero, and let $c_0$ be the largest index with $g_{c_0} \ne 0$. We have $\delta^{c_0}(y^c) = 0$ for $c < c_0$ and $\delta^{c_0}(y^{c_0}) = c_0!$. We apply $\delta^{c_0}$ and get $c_0!\, g_{c_0} = 0$. Since $c_0!$ is a unit, $g_{c_0} = 0$, which is false.

The general case, by induction on $s$. The case $s = 0$ is clear. Let $s \ge 1$ and let $A_1 = \ker\delta_s$. For $j < s$ and $g \in A_1$ we have $\delta_s(\delta_j g) = \delta_j(\delta_s g) = 0$, so $\delta_j$ maps $A_1$ into $A_1$. The restrictions of $\delta_1, \dots, \delta_{s-1}$ to $A_1$ are commuting derivations with $p$-th power $0$, the elements $y_1, \dots, y_{s-1}$ lie in $A_1$, and the common kernel of the restrictions is $A'$. By induction, $A_1$ is free over $A'$ with the basis $y_1^{c_1} \cdots y_{s-1}^{c_{s-1}}$, $c_j < p$. By the case $s = 1$, $A$ is free over $A_1$ with the basis $1, y_s, \dots, y_s^{p-1}$. So the products $y^c$ span $A$ over $A'$. If $\sum_c a_c y^c = 0$ with $a_c \in A'$, then for each $e < p$ the coefficient $\sum_{c : c_s = e} a_c y_1^{c_1} \cdots y_{s-1}^{c_{s-1}}$ of $y_s^e$ is an element of $A_1$, and it is zero by the independence over $A_1$. Then all $a_c = 0$ by the independence over $A'$. $\square$

**Lemma 4.4.14 (gradings).** Let $R$ be a ring of characteristic $p$, and let $\delta_1, \dots, \delta_q$ be commuting derivations of $R$ with $\delta_i^p = \delta_i$. For $\chi = (\chi_1, \dots, \chi_q) \in \mathbb{F}_p^q$ let
$$R_\chi = \{g \in R : \delta_i(g) = \chi_i g \text{ for } 1 \le i \le q\}.$$
The elements of $R_\chi$ are *homogeneous of weight $\chi$*.

1. $R = \bigoplus_\chi R_\chi$: each $g \in R$ is a sum $g = \sum_\chi g_\chi$ with $g_\chi \in R_\chi$, and the components $g_\chi$ are unique.
2. $R_\chi R_\psi \subseteq R_{\chi + \psi}$, and $1 \in R_0$.
3. An ideal $I$ of $R$ is stable under all $\delta_i$ if and only if it is graded, that is, $g_\chi \in I$ for each $g \in I$ and each $\chi$.
4. Let $R$ be local with maximal ideal $\mathfrak{m}$, and assume $\delta_i(R) \subseteq \mathfrak{m}$ for all $i$. Then $R_\chi \subseteq \mathfrak{m}$ for $\chi \ne 0$, and the component $u_0$ of weight $0$ of a unit $u$ is a unit.
5. Let $R$ be local. Then each principal ideal of $R$ that is stable under all $\delta_i$ has a homogeneous generator.

Lean: `Singularity.gradingProj` and `Singularity.sum_gradingProj_apply` (one derivation); `Singularity.exists_sum_commonWeightSpace` and `Singularity.eq_of_sum_commonWeightSpace` (part 1); `Singularity.mul_mem_commonWeightSpace` and `Singularity.one_mem_commonWeightSpace_zero` (part 2); `Singularity.forall_derivation_mem_iff` (part 3); `Singularity.mem_maximalIdeal_of_mem_commonWeightSpace` and `Singularity.exists_isUnit_zero_component` (part 4); `Singularity.exists_mem_commonWeightSpace_span_eq` (part 5)

*Proof.* Part 1, one derivation. Let $\delta$ be a derivation with $\delta^p = \delta$. For $\lambda \in \mathbb{F}_p$ let $\pi_\lambda = 1 - (\delta - \lambda)^{p-1}$, an additive map of $R$. The maps $\delta$ and $\lambda$ commute, so $(\delta - \lambda)^p = \delta^p - \lambda^p = \delta - \lambda$ in characteristic $p$. Thus $(\delta - \lambda)\pi_\lambda = (\delta - \lambda) - (\delta - \lambda)^p = 0$, and $\pi_\lambda(g)$ lies in the eigenspace $\{h : \delta h = \lambda h\}$. The polynomial $Q = \sum_{\lambda \in \mathbb{F}_p}\big(1 - (X - \lambda)^{p-1}\big) \in \mathbb{F}_p[X]$ has degree at most $p - 1$. At $\mu \in \mathbb{F}_p$, the term for $\lambda$ is $1$ if $\lambda = \mu$ and $0$ otherwise, since $(\mu - \lambda)^{p-1} = 1$ for $\mu \ne \lambda$. So $Q - 1$ has the $p$ roots $\mu \in \mathbb{F}_p$ and degree less than $p$, and $Q = 1$. We put $X = \delta$ and get $\sum_\lambda \pi_\lambda = 1$, so $g = \sum_\lambda \pi_\lambda(g)$. On the eigenspace of $\mu$, the map $\delta - \lambda$ is multiplication by $\mu - \lambda$, so $\pi_\lambda$ is multiplication by $1$ if $\lambda = \mu$ and by $0$ otherwise. So if $\sum_\mu g_\mu = 0$ with $g_\mu$ in the eigenspace of $\mu$, then $\pi_\lambda$ gives $g_\lambda = 0$.

Part 1, several derivations. Let $\pi_{i,\lambda}$ be the maps of $\delta_i$. They are polynomials in the $\delta_i$, so they commute with each other and with all $\delta_l$. Let $\pi_\chi = \prod_i \pi_{i,\chi_i}$. Then $\sum_\chi \pi_\chi = \prod_i \sum_\lambda \pi_{i,\lambda} = 1$. For each $i$ we can write $\pi_\chi = \pi_{i,\chi_i} \circ \rho$ with $\rho$ the product of the other factors, so $\pi_\chi(g)$ is in the eigenspace of $\chi_i$ for $\delta_i$. Thus $\pi_\chi(g) \in R_\chi$ and $g = \sum_\chi \pi_\chi(g)$. On $R_\psi$ the map $\pi_\chi$ is multiplication by $\prod_i [\chi_i = \psi_i]$, which is $1$ if $\chi = \psi$ and $0$ otherwise. As before, this gives the uniqueness, and $g_\chi = \pi_\chi(g)$.

Part 2. If $g \in R_\chi$ and $h \in R_\psi$, then $\delta_i(gh) = g\,\psi_i h + h\,\chi_i g = (\chi_i + \psi_i) gh$. Also $\delta_i(1) = 0$.

Part 3. If $I$ is stable under all $\delta_i$, it is stable under the maps $\pi_\chi$, which are sums of products of the $\delta_i$ and of integers. So $g_\chi = \pi_\chi(g) \in I$ for $g \in I$. Conversely, if $I$ is graded and $g \in I$, then $\delta_i(g) = \sum_\chi \chi_i g_\chi \in I$.

Part 4. Let $g \in R_\chi$ with $\chi_i \ne 0$. Then $g = \chi_i^{-1}\delta_i(g) \in \mathfrak{m}$. Let $u$ be a unit. Then $u_0 = u - \sum_{\chi \ne 0} u_\chi$ is a unit minus an element of $\mathfrak{m}$, so it is a unit.

Part 5. Let $I = gR$ be stable under all $\delta_i$. If $g = 0$, then $g$ is homogeneous. Let $g \ne 0$. By part 3, $g_\chi \in I$ for each $\chi$, so $g_\chi = h_\chi g$ with $h_\chi \in R$. Then $g = \sum_\chi h_\chi g$, that is,
$$\Big(1 - \sum_\chi h_\chi\Big)\, g = 0.$$
If $1 - \sum_\chi h_\chi$ were a unit, then $g = 0$, which is false. So $1 - \sum_\chi h_\chi \in \mathfrak{m}$, and $\sum_\chi h_\chi \notin \mathfrak{m}$, since otherwise $1 \in \mathfrak{m}$. So some $h_\chi$ is not in $\mathfrak{m}$, that is, $h_\chi$ is a unit. Then $g_\chi = h_\chi g$ is a homogeneous generator of $I$. $\square$

In part 5 we cannot conclude $\sum_\chi h_\chi = 1$ in general: this needs that $g$ is not a zero divisor. In a domain it holds. Part 5 does not need the hypothesis of part 4.

### A first integral of monomial type gives a principal ideal

From now on, $k$ is perfect and $R$ is as at the start of the section.

**Proposition 4.4.15 (a first integral of monomial type gives a principal ideal).** Let $t \in R$ have monomial type, and let $f \in R$ with $f = \sum_{i < p} c_i^p t^i$ for some $c_i \in E$ and $f \notin E^p$. Let $c = \sum_{i < p} i c_i^p t^{i-1} \in E$, so that $df = c\,dt$.

1. If $t = u\prod_{x \in s} x^{a_x}$ is of the ramified type, let $D \subseteq s$ be a set that contains each $x \in s$ with $p \nmid a_x$. Then $J_D(f) = ctR$, and $ct \in R$.
2. If $t$ is of the residual type, then $J_\emptyset(f) = cR$, and $c \in R$.

In both cases the ideal is principal and not zero.

Lean: none yet

*Proof.* We have $df = c\,dt$ by the proof of Lemma 4.4.5, and $df \ne 0$ by (F1), since $f \notin E^p$.

Part 1. The set $D$ is a normal crossings divisor. Choose a family of coordinates adapted to $D$ whose regular system of parameters is $s$. Let
$$\omega_t = \frac{dt}{t} = \sum_{x \in s} a_x \frac{dx}{x} + \frac{du}{u}.$$
For $x \in s \setminus D$ we have $p \mid a_x$, so $a_x = 0$ in $k$ and the term of $x$ is zero. The element $du$ lies in $\Omega_{R/k} \subseteq \Omega_R(\log D)$, and $u$ is a unit, so $du/u \in \Omega_R(\log D)$. Thus $\omega_t = \sum_{x \in D} a_x\, d\log x + du/u$ lies in $\Omega_R(\log D)$. Choose $x_1 \in D$ with $p \nmid a_{x_1}$. The coefficient of $d\log x_1$ in $\omega_t$ is $a_{x_1} + x_1\partial_{x_1}(u)/u$. Here $a_{x_1}$ is a nonzero element of $\mathbb{F}_p$, so it is a unit, and $x_1\partial_{x_1}(u)/u \in \mathfrak{m}$. So the coefficient is a unit. Thus $\omega_t$ and the basis elements of Lemma 4.4.3, part 3, other than $d\log x_1$ are again a basis of $\Omega_R(\log D)$: the matrix of the change of basis is triangular with units on the diagonal. Now $df = ct\,\omega_t$, and $df \in \Omega_{R/k} \subseteq \Omega_R(\log D)$. The coefficients of an element of $\Omega_{E/k}$ in a basis over $E$ are unique, so $ct \in R$. Let $\delta_1 \in T_D$ be the element of the dual basis with $\omega_t(\delta_1) = 1$. Then $J_D(f) = \{ct\,\omega_t(\delta) : \delta \in T_D\}$, and the values $\omega_t(\delta)$ are the elements of $R$, because $\omega_t(g\delta_1) = g$ and $\omega_t(\delta) \in R$ for all $\delta \in T_D$. So $J_D(f) = ctR$.

Part 2. The class $\bar{t}$ is not a $p$-th power in $\kappa$, so $d\bar{t} \ne 0$ in $\Omega_{\kappa/k}$ by (F1). By the exact sequence in the proof of Lemma 4.4.1, $dt \otimes 1 \ne 0$ in $\Omega_{R/k} \otimes_R \kappa$, so $dt \notin \mathfrak{m}\Omega_{R/k}$. By Nakayama's lemma $dt$ is part of a basis of the free module $\Omega_{R/k} = \Omega_R(\log\emptyset)$. As in part 1, $df = c\,dt$ gives $c \in R$ and $J_\emptyset(f) = cR$. $\square$

### A principal ideal gives a first integral of monomial type

**Theorem 4.4.16 (a principal log Jacobian ideal gives a first integral of monomial type).** Let $f \in R$ with $f \notin E^p$, and let $D = \{x_1, \dots, x_r\}$ be a normal crossings divisor of $R$ such that $J_D(f)$ is a principal ideal. Then there is $t \in R$ with $t \notin E^p$ and $f \in E^p(t)$, such that $\delta(t) = 0$ for each $\delta \in T_D$ with $\delta(f) = 0$, and $t$ has one of these forms:

1. after a change of the order of the $x_i$, $t = u\, x_1 \prod_{i \ge 2} x_i^{a_i}$ with $u$ a unit and $0 \le a_i < p$;
2. $t = u\,\zeta\prod_i x_i^{b_i}$ with $u$ a unit and $0 \le b_i < p$, where $\zeta$ is an element such that $x_1, \dots, x_r, \zeta$ is a part of a regular system of parameters;
3. $t$ is a regular parameter, that is, $t \in \mathfrak{m} \setminus \mathfrak{m}^2$;
4. $t$ is of the residual type.

In each case $t$ has monomial type, so $f$ is foliated monomial in $R$.

Lean: none yet

*Proof.* Fix a family of coordinates adapted to $D$. Let $J_D(f) = mR$. By Lemma 4.4.4, part 2, $m \ne 0$. By Lemma 4.4.3, part 4, the coefficients $x_i\partial_{x_i}(f)$ and $\partial_{y_j}(f)$ of $df$ lie in $mR$. Write them as $m c_i$ and $m d_j$. Then $df = m\,\omega$ with
$$\omega = \sum_i c_i\, d\log x_i + \sum_j d_j\, dy_j \in \Omega_R(\log D).$$
The elements $mc_i$, $md_j$ generate $mR$, so $m = me$ with $e$ in the ideal $(c_i, d_j)$. Since $R$ is a domain and $m \ne 0$, $e = 1$. So the ideal $(c_i, d_j)$ is $R$, and since $R$ is local, one of the $c_i$, $d_j$ is a unit. Let
$$\mathfrak{F} = \{\delta \in T_D : \delta(f) = 0\} = \{\delta \in T_D : \omega(\delta) = 0\},$$
where the equality holds because $\delta(f) = m\,\omega(\delta)$ and $m \ne 0$. It is an $R$-submodule of $T_D$. It is closed under the bracket, because $[\delta, \delta'](f) = \delta(0) - \delta'(0) = 0$, and under $\delta \mapsto \delta^p$, because $\delta^p(f) = \delta^{p-1}(0) = 0$, by Lemma 4.4.3, part 2.

We first show how to finish the proof from an element $t$ with the following properties: $t \in R$, $t \notin E^p$, and $\delta(t) = 0$ for each $\delta \in \mathfrak{F}$. Let $\delta \in \operatorname{Der}_k(E)$ with $\omega(\delta) = 0$. The coefficients of $\delta$ in the basis $x_i\partial_{x_i}$, $\partial_{y_j}$ are in $E$, so $b\delta \in T_D$ for a nonzero $b \in R$. Then $b\delta \in \mathfrak{F}$, so $b\,dt(\delta) = 0$ and $dt(\delta) = 0$. Thus the linear form $dt$ on the finite dimensional $E$-vector space $\operatorname{Der}_k(E)$ vanishes on the kernel of the nonzero linear form $\omega$. So $dt = \lambda\omega$ with $\lambda \in E$. We have $dt \ne 0$ by (F1), so $\lambda \ne 0$, and $df = m\omega = (m/\lambda)\,dt$. By Lemma 4.4.5, $f \in E^p(t)$. So it remains to find $t$ of one of the four forms with these properties. We treat two cases.

*Case 1: some $c_i$ is a unit.* After a change of the order, $c_1$ is a unit. We replace $\omega$ by $\omega/c_1$ and $m$ by $mc_1$. Now $c_1 = 1$. Let
$$D_i = x_i\partial_{x_i} - c_i\, x_1\partial_{x_1} \quad (2 \le i \le r), \qquad D'_j = \partial_{y_j} - d_j\, x_1\partial_{x_1} \quad (1 \le j \le s).$$
Then $\omega(D_i) = c_i - c_i = 0$ and $\omega(D'_j) = d_j - d_j = 0$, so these elements lie in $\mathfrak{F}$. They are a basis of $\mathfrak{F}$. Indeed, let $\delta = \sum_i a_i\, x_i\partial_{x_i} + \sum_j b_j\partial_{y_j} \in \mathfrak{F}$. Then $\delta - \sum_{i \ge 2} a_i D_i - \sum_j b_j D'_j = \big(a_1 + \sum_{i \ge 2} a_i c_i + \sum_j b_j d_j\big)\, x_1\partial_{x_1} = \omega(\delta)\, x_1\partial_{x_1} = 0$. The elements are independent, because their coefficients on $x_i\partial_{x_i}$ for $i \ge 2$ and on $\partial_{y_j}$ form a unit matrix.

Step 1. If $g\,x_1\partial_{x_1} \in \mathfrak{F}$ with $g \in R$, then $g = \omega(g\,x_1\partial_{x_1}) = 0$.

Step 2. The derivations $D_i$ and $D'_j$ commute, $D_i^p = D_i$ and $D'^p_j = 0$. Let $\Delta$ be one of the brackets $[D_i, D_l]$, $[D_i, D'_j]$, $[D'_j, D'_l]$, or one of $D_i^p - D_i$, $D'^p_j$. Then $\Delta \in \mathfrak{F}$, because $\mathfrak{F}$ is closed under brackets, $p$-th powers and differences. We compute $\Delta$ on the coordinates other than $x_1$. For $l \ge 2$ we have $D_i(x_l) = x_l$ if $i = l$ and $0$ otherwise, $D_i(y_l) = 0$, $D'_j(x_l) = 0$, and $D'_j(y_l) = 1$ if $j = l$ and $0$ otherwise. So each of these derivations maps $x_l$ to $\varepsilon x_l$ with $\varepsilon \in \{0, 1\}$, and $y_l$ to $0$ or $1$. For two such derivations $P$ and $Q$, $PQ(x_l) = \varepsilon_P\varepsilon_Q x_l = QP(x_l)$ and $PQ(y_l) = 0 = QP(y_l)$. So each bracket is zero on these coordinates. Also $D_i^p(x_l) = \varepsilon x_l = D_i(x_l)$, $D_i^p(y_l) = 0 = D_i(y_l)$, $D'^p_j(x_l) = 0$ and $D'^p_j(y_l) = D'^{p-1}_j(D'_j y_l) = 0$. So $\Delta$ is zero on all coordinates other than $x_1$. By Lemma 4.4.1, part 2, $\Delta = \Delta(x_1)\partial_{x_1}$, and $\Delta(x_1) = g x_1$ with $g \in R$, because $\Delta \in T_D$. So $\Delta = g\,x_1\partial_{x_1}$, and $\Delta = 0$ by Step 1.

Step 3. The residues of the $c_i$. By Step 2, Lemma 4.4.14 applies to $D_2, \dots, D_r$ on $R$, with weights in $\mathbb{F}_p^{\{2, \dots, r\}}$. We have $D_i(R) \subseteq (x_1, x_i) \subseteq \mathfrak{m}$, so part 4 of the lemma applies. For $l \ge 2$ the element $x_l$ is homogeneous of weight $e_l$, the unit vector of $l$. The ideal $x_1R$ is stable under the $D_i$, because $D_i \in T_D$. By Lemma 4.4.14, part 5, it has a homogeneous generator $\xi = gx_1$ with $g$ a unit. Let $\chi$ be its weight. Then
$$\chi_i\, g x_1 = D_i(gx_1) = D_i(g)\,x_1 + g\,D_i(x_1) = (D_i(g) - c_i g)\,x_1.$$
We cancel $x_1$ and get $c_i = D_i(g)/g - \chi_i \equiv -\chi_i$ modulo $\mathfrak{m}$. For $2 \le i \le r$ let $a_i$ be the integer with $0 \le a_i < p$ whose class in $\mathbb{F}_p$ is $-\chi_i$.

Step 4. The ring of constants. Let $R' = \bigcap_j \ker D'_j$. By Step 2 and $D'_j(y_l) = 1$ if $j = l$ and $0$ otherwise, Lemma 4.4.13 applies: $R$ is a free $R'$-module with the basis of the monomials $y^c$, $0 \le c_j < p$. The basis contains $y^0 = 1$. So for each ideal $I$ of $R'$ we have $IR = \bigoplus_c I y^c$, and $IR \cap R' = I$. An increasing chain of ideals of $R'$ gives an increasing chain of ideals of $R$, which is stationary, and we get the first chain back by intersection with $R'$. So $R'$ is Noetherian. Let $\mathfrak{m}' = \mathfrak{m} \cap R'$. An element $g \in R' \setminus \mathfrak{m}'$ is a unit of $R$, and $D'_j(g^{-1}) = -D'_j(g)/g^2 = 0$, so $g^{-1} \in R'$. Thus $R'$ is a local ring with maximal ideal $\mathfrak{m}'$. The map $R' \to R$ is flat, because $R$ is free over $R'$, and it is local. Since $R$ is regular, $R'$ is regular [Mat, Section 23]. So $R'$ is a domain and a unique factorization domain [Mat, Section 20]. The $D_i$ commute with the $D'_j$, so $D_i(R') \subseteq R'$, and $D_i(R') \subseteq \mathfrak{m} \cap R' = \mathfrak{m}'$. So Lemma 4.4.14 applies to the restrictions of the $D_i$ to $R'$, and the components of an element of $R'$ are in $R'$, because $\pi_\chi$ is a polynomial in the $D_i$.

Step 5. Let $x$ be one of $\xi, x_2, \dots, x_r$, and let $\mathfrak{q} = xR \cap R'$. The element $x$ is a regular parameter, so $R/xR$ is a regular local ring (Volume 1, Proposition 1.2.6), and $xR$ is a prime ideal (Volume 1, Theorem 1.3.3). By Krull's principal ideal theorem it has height $1$. The ideal $\mathfrak{q}$ is prime, and it is not zero, because $x^p \in \mathfrak{q}$: indeed $D'_j(x^p) = 0$. A flat extension has the going down property [Mat, Section 9]. So a chain of primes $\mathfrak{q}_0 \subsetneq \mathfrak{q}$ of $R'$ gives a chain $Q_0 \subsetneq xR$ of primes of $R$ with $Q_0 \cap R' = \mathfrak{q}_0$. Thus the height of $\mathfrak{q}$ is at most $1$, and it is $1$. In a unique factorization domain a prime of height $1$ is principal [Mat, Section 20], so $\mathfrak{q} = \eta R'$. We claim that $\eta R = xR$. Since $\eta \in xR$, we have $\eta R \subseteq xR$. The ring $R/\eta R$ is free over $R'/\eta R'$ with the basis of the classes of the $y^c$, because $\eta R = \bigoplus_c \eta R' y^c$. The $D'_j$ map $\eta R$ into $\eta R$, because $D'_j(\eta) = 0$, so they act on $R/\eta R$. They map $xR$ into $xR$, because $D'_j \in T_D$ and $xR$ is $x_lR$ or $x_1R$. So the ideal $N = xR/\eta R$ of $R/\eta R$ is stable under the $D'_j$. Assume that $N \ne 0$, and let $g = \sum_c \bar{g}_c y^c \in N$ with $g \ne 0$ and $\bar{g}_c \in R'/\eta R'$. Choose $c$ with $\bar{g}_c \ne 0$ that is maximal for the order $c \le c'$ if $c_j \le c'_j$ for all $j$. The derivations $D'_j$ kill the coefficients and satisfy $D'_j(y_l) = 0$ for $l \ne j$, so $\prod_j D'^{c_j}_j(y^{c'}) = \prod_j D'^{c_j}_j(y_j^{c'_j})$. This is $0$ unless $c'_j \ge c_j$ for all $j$, and it is $c! = \prod_j c_j!$ for $c' = c$. By the maximality of $c$, we get $\prod_j D'^{c_j}_j(g) = c!\,\bar{g}_c$. This element lies in $N$, and it is the class of an element $r \in R'$ with $r \notin \eta R'$, since $c!$ is a unit and $\bar{g}_c \ne 0$. But the class of $r$ lies in $N$, so $r \in xR$, and $r \in xR \cap R' = \eta R'$. This is a contradiction. So $N = 0$ and $\eta R = xR$.

Step 6. The ideal $\mathfrak{q} = \eta R'$ of $R'$ is stable under the $D_i$, because $D_i$ maps $xR$ and $R'$ into themselves. By Lemma 4.4.14, part 5, applied in $R'$, we can choose $\eta$ homogeneous. Write $\eta = vx$. Since $\eta R = xR$ and $R$ is a domain, $v$ is a unit of $R$. Let $\varphi$ be the weight of $x$ and $\psi$ the weight of $\eta$. Write $v = \sum_\rho v_\rho$ with $v_\rho \in R_\rho$. Then $\eta = \sum_\rho v_\rho x$ with $v_\rho x \in R_{\rho + \varphi}$, by Lemma 4.4.14, part 2. By the uniqueness of the components, $v_\rho x = 0$ for $\rho + \varphi \ne \psi$, so $v_\rho = 0$ for these $\rho$. So $v$ is homogeneous. A homogeneous unit has weight $0$ by Lemma 4.4.14, part 4. Thus $\psi = \varphi$: the element $\eta$ has the weight of $x$. Let $\eta_1$ be this element for $x = \xi$, and $\eta_l$ for $x = x_l$ with $l \ge 2$. So $\eta_1 = v_1 g x_1$ and $\eta_l = v_l x_l$ with units $v_1, v_l$, and $\eta_1$ has weight $\chi$ and $\eta_l$ has weight $e_l$.

Step 7. Let $t = \eta_1\prod_{i \ge 2}\eta_i^{a_i}$. It lies in $R'$, and by Lemma 4.4.14, part 2, its weight is $\chi + \sum_{i \ge 2} a_i e_i$. Its $i$-th component is $\chi_i + a_i = 0$ in $\mathbb{F}_p$. So $D_i(t) = 0$ for all $i$ and $D'_j(t) = 0$ for all $j$, and thus $\delta(t) = 0$ for each $\delta \in \mathfrak{F}$. We have $t = u\, x_1\prod_{i \ge 2} x_i^{a_i}$ with the unit $u = v_1 g\prod_{i \ge 2} v_i^{a_i}$. This is form (1). The order of $t$ along $x_1 = 0$ (defined in the proof of Lemma 4.3.7) is $1$, and it is not divisible by $p$, so $t \notin E^p$. This finishes Case 1.

*Case 2: no $c_i$ is a unit.* Then all $c_i \in \mathfrak{m}$, and some $d_j$ is a unit. After a change of the order, $d_1$ is a unit. We replace $\omega$ by $\omega/d_1$ and $m$ by $md_1$, and we write $y = y_1$. Then
$$\omega = dy + \sum_{i=1}^r c_i\, d\log x_i + \sum_{j \ge 2} d_j\, dy_j, \qquad c_i \in \mathfrak{m}.$$
Let $D_i = x_i\partial_{x_i} - c_i\partial_y$ for $1 \le i \le r$ and $D'_j = \partial_{y_j} - d_j\partial_y$ for $2 \le j \le s$. As in Case 1, these elements are a basis of $\mathfrak{F}$: for $\delta = \sum_i a_i\, x_i\partial_{x_i} + b\,\partial_y + \sum_{j \ge 2} b_j\partial_{y_j}$ we get $\delta - \sum_i a_i D_i - \sum_j b_j D'_j = \omega(\delta)\,\partial_y$. If $g\,\partial_y \in \mathfrak{F}$, then $g = \omega(g\,\partial_y) = 0$. On the coordinates other than $y$, that is, the $x_l$ and the $y_l$ with $l \ge 2$, the values of the $D_i$ and $D'_j$ are as in Step 2 of Case 1: $D_i(x_l) = x_l$ if $i = l$ and $0$ otherwise, $D_i(y_l) = 0$, $D'_j(x_l) = 0$, and $D'_j(y_l) = 1$ if $j = l$ and $0$ otherwise. A derivation that is zero on these coordinates is $g\,\partial_y$ with $g \in R$. So the argument of Step 2 shows that the $D_i$ and $D'_j$ commute, $D_i^p = D_i$ and $D'^p_j = 0$. Lemma 4.4.14 applies to $D_1, \dots, D_r$, and $D_i(R) \subseteq (x_i, c_i) \subseteq \mathfrak{m}$, so part 4 applies. The element $x_l$ is homogeneous of weight $e_l$. Let $R' = \bigcap_{j \ge 2}\ker D'_j$. Steps 4 to 6 of Case 1 apply with no change, with $y_2, \dots, y_s$ in place of $y_1, \dots, y_s$ and $x = x_l$ for $1 \le l \le r$. They show that $R'$ is a regular local ring, that $R$ is free over $R'$ with the basis $y_2^{c_2} \cdots y_s^{c_s}$, $c_j < p$, that the $D_i$ define a grading of $R'$ as in Lemma 4.4.14, and that there are homogeneous $\eta_l \in R'$ of weight $e_l$ with $\eta_l = v_l x_l$ for units $v_l$.

Step 8. A parameter of contact. Let $\tilde{\omega} = dy + \sum_{j \ge 2} d_j\, dy_j$. An element $\alpha = \sum_i \alpha_i\, dx_i + \beta\, dy + \sum_{j \ge 2}\gamma_j\, dy_j$ of $\Omega_{R/k}$ has $\alpha(D'_j) = \gamma_j - d_j\beta$. So the submodule $\mathcal{A} = \{\alpha \in \Omega_{R/k} : \alpha(D'_j) = 0 \text{ for } j \ge 2\}$ is free with the basis $dx_1, \dots, dx_r, \tilde{\omega}$, and $\Omega_{R/k} = \mathcal{A} \oplus \bigoplus_{j \ge 2} R\, dy_j$, since $\alpha = \sum_i \alpha_i\, dx_i + \beta\tilde{\omega} + \sum_{j \ge 2}(\gamma_j - d_j\beta)\, dy_j$. Each $g \in R$ is a combination of the monomials $y_2^{c_2} \cdots y_s^{c_s}$ with coefficients in $R'$, so $\Omega_{R/k}$ is generated by the elements $dg$, $g \in R'$, and the $dy_j$, $j \ge 2$. For $g \in R'$ we have $dg(D'_j) = D'_j(g) = 0$, so $dg \in \mathcal{A}$. The projection of $\Omega_{R/k}$ onto $\mathcal{A}$ along $\bigoplus_{j \ge 2} R\,dy_j$ maps $dg$ to $dg$ and $dy_j$ to $0$. So $\mathcal{A}$ is generated by the $dg$, $g \in R'$. If the coefficient of $\tilde{\omega}$ of each $dg$, $g \in R'$, were in $\mathfrak{m}$, then the classes of the $dg$ in $\mathcal{A}/\mathfrak{m}\mathcal{A}$ would lie in the span of the classes of the $dx_i$, and they would not span $\mathcal{A}/\mathfrak{m}\mathcal{A}$. So there is $\tilde{y} \in R'$ with $d\tilde{y} = \lambda\tilde{\omega} + \sum_i \mu_i\, dx_i$ and $\lambda$ a unit. Then $\partial_y(\tilde{y}) = d\tilde{y}(\partial_y) = \lambda$, a unit.

Step 9. Write $\tilde{y} = \sum_\chi \tilde{y}_\chi$ with $\tilde{y}_\chi \in R'_\chi = R' \cap R_\chi$. Then $\sum_\chi \partial_y(\tilde{y}_\chi) = \lambda \notin \mathfrak{m}$, so there is $\chi$ with $\partial_y(\tilde{y}_\chi) \notin \mathfrak{m}$. Let $\zeta = \tilde{y}_\chi$. It lies in $R'$ and is homogeneous of weight $\chi$, and $\partial_y(\zeta)$ is a unit. Thus $d\zeta \notin \mathfrak{m}\Omega_{R/k}$, because its coefficient on $dy$ is $\partial_y(\zeta)$.

Step 10. The weight $\chi = 0$. Then $D_i(\zeta) = 0$ and $D'_j(\zeta) = 0$, so $\zeta$ is killed by $\mathfrak{F}$. If the class $\bar{\zeta}$ of $\zeta$ in $\kappa$ is not a $p$-th power, then $\bar{\zeta} \ne 0$, so $\zeta$ is a unit of the residual type. Let $t = \zeta$. This is form (4). If $\bar{\zeta} = \bar{e}^p$ with $e \in R$, let $t = \zeta - e^p$. Then $t \in \mathfrak{m}$, $\delta(t) = \delta(\zeta) = 0$ for $\delta \in \mathfrak{F}$, and $dt = d\zeta \notin \mathfrak{m}\Omega_{R/k}$. If $t$ were in $\mathfrak{m}^2$, say $t = \sum_l a_l b_l$ with $a_l, b_l \in \mathfrak{m}$, then $dt = \sum_l(a_l\, db_l + b_l\, da_l) \in \mathfrak{m}\Omega_{R/k}$. So $t \in \mathfrak{m} \setminus \mathfrak{m}^2$, and $t$ is a regular parameter. This is form (3), and $t = 1 \cdot t^1$ is of the ramified type in a regular system of parameters that contains $t$. In both forms $dt = d\zeta \ne 0$, so $t \notin E^p$ by (F1).

Step 11. The weight $\chi \ne 0$. Then $\zeta \in \mathfrak{m}' \subseteq \mathfrak{m}$ by Lemma 4.4.14, part 4, applied in $R'$. Let $z_1, \dots, z_d$ be the regular parameters among the coordinates, and write $\zeta = \sum_q z_q g_q$ with $g_q \in R$. If $y$ is not one of the $z_q$, then $\partial_y(z_q) = 0$ for all $q$, and $\partial_y(\zeta) = \sum_q z_q\,\partial_y(g_q) \in \mathfrak{m}$, which is false. So $y = z_{q_0}$ for some $q_0$, and $\partial_y(\zeta) \equiv g_{q_0}$ modulo $\mathfrak{m}$. So $g_{q_0}$ is a unit. In $\mathfrak{m}/\mathfrak{m}^2$ the class of $\zeta$ is $\sum_q \bar{g}_q[z_q]$ with $\bar{g}_{q_0} \ne 0$. So if we replace $z_{q_0} = y$ by $\zeta$, we get a basis of $\mathfrak{m}/\mathfrak{m}^2$, and a regular system of parameters (Volume 1, Lemma 1.1.1). It contains $x_1, \dots, x_r$ and $\zeta$. For $1 \le i \le r$ let $b_i$ be the integer with $0 \le b_i < p$ whose class is $-\chi_i$, and let $t = \zeta\prod_i\eta_i^{b_i}$. It lies in $R'$ and has weight $\chi + \sum_i b_i e_i = 0$. So $\delta(t) = 0$ for $\delta \in \mathfrak{F}$. We have $t = u\,\zeta\prod_i x_i^{b_i}$ with the unit $u = \prod_i v_i^{b_i}$. This is form (2), of the ramified type with the exponent $1$ at $\zeta$. The order of $t$ along $\zeta = 0$ is $1$, so $t \notin E^p$.

In all cases we have found $t$ with the properties of the paragraph before Case 1. $\square$

**Corollary 4.4.17 (the log Jacobian criterion).** Let $f \in R$ with $f \notin E^p$. Then $f$ is foliated monomial in $R$ if and only if there is a normal crossings divisor $D$ of $R$ such that $J_D(f)$ is principal.

Lean: none yet

*Proof.* If $f$ is foliated monomial, Proposition 4.4.15 gives $D$. If $J_D(f)$ is principal, Theorem 4.4.16 gives $t$. $\square$

The proof of Theorem 4.4.16 says more than the statement. In Case 1 the residues of the coefficients $c_i$ of $\omega$ are in $\mathbb{F}_p$, and the Euler type derivations $D_i$ of the foliation $\mathfrak{F}$ give the exponents of the first integral. In Case 2 the element $\zeta$ plays the role of a hypersurface of maximal contact: it is homogeneous for the Euler type derivations, and in form (2) it becomes a new component of the divisor.

### The log Jacobian ideal after a blow-up

Let $D = \{x_1, \dots, x_r\}$ be a normal crossings divisor of $R$, with an adapted family of coordinates. A center $Z$ *has normal crossings with $D$* if its ideal is $I_Z = (z_1, \dots, z_c)$, with $c \ge 1$, where $z_1, \dots, z_c$ are distinct coordinates and each $z_a$ is one of the $x_i$ or one of the $y_j$ that are regular parameters. Let
$$T_{D,Z} = \{\delta \in T_D : \delta(I_Z) \subseteq I_Z\}, \qquad J_{D,Z}(f) = \{\delta(f) : \delta \in T_{D,Z}\}.$$
The derivations in $T_{D,Z}$ are the log derivations that are *tangent to the center*. For $1 \le b \le c$ the *chart* $C_b$ of the blow-up of $Z$ is the subring $R[z_a/z_b : a \ne b]$ of $E$. The blow-up $X'$ of $\operatorname{Spec} R$ along $Z$ is covered by the spectra of the charts $C_1, \dots, C_c$; for the blow-up of a point see Volume 1, Definition 1.10.3. On the chart $C_b$ the exceptional divisor is $z_b = 0$, since $I_ZC_b = z_bC_b$. The strict transform of $x_i = 0$ is $z_a/z_b = 0$ if $x_i = z_a$ with $a \ne b$, it is $x_i = 0$ if $x_i$ is not one of the $z_a$, and it does not meet the chart if $x_i = z_b$. So we let
$$D'_b = \{z_b\} \cup \{z_a/z_b : a \ne b,\ z_a \in D\} \cup \{x \in D : x \notin \{z_1, \dots, z_c\}\}.$$
At a point of $X'$ in the chart $C_b$, with local ring $R_1 = (C_b)_P$, the divisor $D'$ is given by $D'_b$, and we use the module $T_{D'_b}(R_1)$ of Definition 4.4.2. The elements of $D'_b$ that are not in $P$ are units of $R_1$, and for them the condition of Definition 4.4.2 is empty.

**Lemma 4.4.18 (the transformation law).** In this situation:

1. $T_{D,Z}$ is generated by the elements $x\partial_x$ for $x \in D$, the elements $\partial_v$ for the coordinates $v$ that are not in $D$ and not among the $z_a$, and the elements $z_a\partial_{z_b}$ for the $z_b$ that are not in $D$ and $1 \le a \le c$.
2. For each $b$ and each prime $P$ of $C_b$, with $R_1 = (C_b)_P$, we have $T_{D'_b}(R_1) = R_1 \cdot T_{D,Z}$ in $\operatorname{Der}_k(E)$. Thus for $f \in R$,
$$J_{D'_b}(f) = J_{D,Z}(f)\, R_1.$$

In words, the log Jacobian ideal after the blow-up is generated by the values of the log derivations that are tangent to the center.

Lean: none yet

*Proof.* Part 1. Let $\delta = \sum_i a_i\, x_i\partial_{x_i} + \sum_j b_j\partial_{y_j} \in T_D$. For $z_a = x_i$ we have $\delta(z_a) = a_i x_i \in I_Z$. For $z_a = y_j$ we have $\delta(z_a) = b_j$. So $\delta \in T_{D,Z}$ if and only if $b_j \in I_Z$ for each $y_j$ that is one of the $z_a$. These $\delta$ are the combinations of the listed elements.

Part 2. After a change of the order of the $z_a$, we have $b = 1$. Let $C = C_1$ and $z'_a = z_a/z_1$ for $2 \le a \le c$, so that $z_a = z_1z'_a$. Let $V$ be the set of the coordinates that are not among the $z_a$. We claim that $\Omega_{C/k}$ is free with the basis $dz_1$, $dz'_a$ ($2 \le a \le c$), $dv$ ($v \in V$). The module $\Omega_{C/k}$ is generated by $d(R)$ and the $dz'_a$, because $C = R[z'_2, \dots, z'_c]$. By Lemma 4.4.1, $d(R)$ is generated by the $dz_a$ and $dv$, and $dz_a = z'_a\, dz_1 + z_1\, dz'_a$. So the $n$ elements generate $\Omega_{C/k}$. The fraction field of $C$ is $E$, and $\Omega_{C/k} \otimes_C E = \Omega_{E/k}$ has dimension $n$. As in the proof of Lemma 4.4.1, the module is free with this basis. Let $\partial'_{z_1}$, $\partial'_{z'_a}$, $\partial'_v$ be the dual basis of $\operatorname{Der}_k(C)$, extended to $E$. We compute them on the coordinates of $R$, which determine a derivation of $E$ by Lemma 4.4.1, part 4. We have $\partial'_{z_1}(z_1) = 1$, $\partial'_{z_1}(z_a) = \partial'_{z_1}(z_1z'_a) = z'_a$ and $\partial'_{z_1}(v) = 0$. Next $\partial'_{z'_a}(z_1) = 0$, $\partial'_{z'_a}(z_l) = z_1$ if $l = a$ and $0$ for the other $l \ge 2$, and $\partial'_{z'_a}(v) = 0$. Last, $\partial'_v$ is $1$ at $v$ and $0$ at the other coordinates. So
$$z_1\partial'_{z_1} = \sum_{a=1}^c z_a\partial_{z_a}, \qquad \partial'_{z'_a} = z_1\partial_{z_a} \ (a \ge 2), \qquad \partial'_v = \partial_v.$$
As in Lemma 4.4.3, part 1, the module $T_{D'_1}(C)$ of the derivations of $C$ that preserve $gC$ for each $g \in D'_1$ is free with the basis of the elements $g\partial'_g$ for $g \in D'_1$ and $\partial'_h$ for the other elements $h$ of the basis. In terms of the old derivations, this basis is:

- $z_1\partial'_{z_1} = \sum_a z_a\partial_{z_a}$;
- for $a \ge 2$: $z'_a\partial'_{z'_a} = z_a\partial_{z_a}$ if $z_a \in D$, and $\partial'_{z'_a} = z_1\partial_{z_a}$ if $z_a \notin D$;
- for $v \in V$: $v\partial_v$ if $v \in D$, and $\partial_v$ if $v \notin D$.

Each of these elements is a sum of generators of $T_{D,Z}$ of part 1. For the first one, $z_a\partial_{z_a}$ is $x\partial_x$ with $x = z_a$ if $z_a \in D$, and it is a generator $z_a\partial_{z_b}$ with $b = a$ if $z_a \notin D$. So $T_{D'_1}(C) \subseteq C \cdot T_{D,Z}$. Conversely, we write the generators of part 1 in the new basis:

- $x\partial_x$ for $x \in D$ with $x \in V$ is a basis element;
- $z_a\partial_{z_a}$ for $z_a \in D$ and $a \ge 2$ is $z'_a\partial'_{z'_a}$;
- $z_1\partial_{z_1}$ for $z_1 \in D$ is $z_1\partial'_{z_1} - \sum_{a \ge 2} z_a\partial_{z_a} = z_1\partial'_{z_1} - \sum_{a \ge 2} z'_a\partial'_{z'_a}$;
- $\partial_v$ for $v \in V$, $v \notin D$, is a basis element;
- $z_a\partial_{z_l}$ for $z_l \notin D$ and $l \ge 2$ is $z'_a\, z_1\partial_{z_l} = z'_a\partial'_{z'_l}$, with $z'_1 = 1$, and $\partial'_{z'_l}$ is a basis element because $z'_l \notin D'_1$;
- $z_a\partial_{z_1}$ for $z_1 \notin D$ is $z'_a\, z_1\partial_{z_1} = z'_a\big(z_1\partial'_{z_1} - \sum_{l \ge 2} z'_l\partial'_{z'_l}\big)$.

In the third and last lines, each $z'_l\partial'_{z'_l}$ lies in $T_{D'_1}(C)$: it is a basis element if $z_l \in D$, and $z'_l$ times a basis element if not. So $T_{D,Z} \subseteq T_{D'_1}(C)$, and $T_{D'_1}(C) = C \cdot T_{D,Z}$.

Now let $P$ be a prime of $C$ and $R_1 = C_P$. Then $\Omega_{R_1/k} = \Omega_{C/k} \otimes_C R_1$, so $\operatorname{Der}_k(R_1)$ is free over $R_1$ with the basis $\partial'$. A derivation $\delta = \sum_h \alpha_h\partial'_h$ of $R_1$ maps $gR_1$ into $gR_1$, for $g \in D'_1$, if and only if $\alpha_g = \delta(g) \in gR_1$, by the computation of Lemma 4.4.3, part 1. If $g \notin P$, this condition is empty, and $\partial'_g = g^{-1}\cdot g\partial'_g$. So $T_{D'_1}(R_1) = R_1 \cdot T_{D'_1}(C) = R_1 \cdot T_{D,Z}$. The values at $f$ give the formula for the ideals. $\square$

**Corollary 4.4.19 (the ideal under blow-ups).** In the situation of Lemma 4.4.18, at each point of $X'$ with local ring $R_1$:

1. $J_{D'}(f) \subseteq J_D(f)\, R_1$;
2. if $Z$ is a stratum of $D$, that is, all $z_a$ lie in $D$, then $T_{D,Z} = T_D$ and $J_{D'}(f) = J_D(f)\, R_1$. In particular, if $J_D(f)$ is principal, then $J_{D'}(f)$ is principal.

Lean: none yet

*Proof.* Part 1 follows from $T_{D,Z} \subseteq T_D$ and Lemma 4.4.18. Part 2. If all $z_a$ lie in $D$, the generators of part 1 of Lemma 4.4.18 are the $x\partial_x$ for $x \in D$ and the $\partial_v$ for $v \notin D$. This is the basis of $T_D$ of Lemma 4.4.3. If $J_D(f) = mR$, then $J_{D'}(f) = mR_1$. $\square$

So the blow-ups of strata of $D$, the toroidal blow-ups, do not change the log Jacobian ideal. A blow-up of a center that has normal crossings with $D$ and is not a stratum can make it smaller, and it can make a principal ideal not principal (Example 4.4.22). At the points of $X'$, the elements of $D'$ in the maximal ideal are a part of a regular system of parameters of $R_1$. This is a standard fact on the blow-up of a regular center that has normal crossings with $D$. We do not use it in the proof of Lemma 4.4.18, but we need it to apply Theorem 4.4.16 at $R_1$.

### Examples

**Example 4.4.20 (a foliated monomial element that is not monomial modulo $p$-th powers).** Let $p$ be odd, let $k$ be a perfect field of characteristic $p$, and let $R = k[t, y_2, y_3]_{(t, y_2, y_3)}$, a regular local ring of dimension 3 with residue field $k$. Let
$$f = y_2^p\, t + y_3^p\, t^2.$$
Since $p \ge 3$, this has the form of Definition 4.4.6 with $c_1 = y_2$, $c_2 = y_3$ and all other $c_i = 0$. The element $t$ is a regular parameter, so it has monomial type. So $f$ is foliated monomial in $R$, and $E(f^{1/p}) = E(t^{1/p})$ by Proposition 4.4.8. We have
$$df = (y_2^p + 2t\,y_3^p)\, dt, \qquad J_\emptyset(f) = qR \text{ with } q = y_2^p + 2t\,y_3^p.$$
So $f \notin E^p$, and the ideal is principal, as Proposition 4.4.15 says. We show that $f$ is not monomial modulo $p$-th powers in $R$. First, $q$ is a prime element of $R$. As a polynomial in $t$ over the unique factorization domain $k[y_2, y_3]$ it has degree 1, and its coefficients $2y_3^p$ and $y_2^p$ have no common prime factor, because $2 \ne 0$ in $k$. By Gauss's lemma $q$ is irreducible in $k[y_2, y_3, t]$, so it is a prime element there, and it stays prime in the localization $R$, because $q$ lies in the maximal ideal. Also $q \in \mathfrak{m}^p \subseteq \mathfrak{m}^2$. Now assume that $f = h^p + g^p\,t'$ with $g \ne 0$ and $t' = u\,x_1^{a_1}x_2^{a_2}x_3^{a_3}$ as in Definition 4.3.4. The residual type is impossible, because each element of the residue field $k$ is a $p$-th power. So $t'$ is of the ramified type, with $p \nmid a_i$ for some $i$, and then $a_i \ge 1$. By Lemma 4.4.4, part 1, and $d(g^p) = 0$ we get $qR = J_\emptyset(f) = J_\emptyset(g^pt') = g^p J_\emptyset(t')$. Take the coordinates $x_1, x_2, x_3$. Then
$$\partial_{x_i}(t') = x^{a - e_i}\big(a_i u + x_i\partial_{x_i}(u)\big),$$
and the factor $a_iu + x_i\partial_{x_i}(u)$ is a unit. So $g^p x^{a - e_i}$ lies in $qR$, and $q$ divides $g^p x^{a - e_i}$. Since $q$ is prime, $q$ divides $g$ or $q$ divides some $x_l$. If $q \mid x_l$, then $q$ and $x_l$ are associated, because $x_l$ is a prime element, and this is false, since $x_l \notin \mathfrak{m}^2$ and $q \in \mathfrak{m}^2$. If $q \mid g$, then $q^p \mid g^p$, and $g^p$ divides $q$, because $q \in g^pJ_\emptyset(t')$. So $q = q^p s$ for some $s \in R$, and $1 = q^{p-1}s$, which is false, since $q$ is not a unit. So $f$ is not monomial modulo $p$-th powers in $R$. Theorem 4.3.14 does not apply to $f$ in $R$. But it applies to $t$, and by Proposition 4.4.8 the step of degree $p$ for $f$ is the step for $t$, with no change of the model.

**Example 4.4.21 (Case 2 of Theorem 4.4.16).** Let $R = k[x, y]_{(x, y)}$, $D = \{x\}$ and $f = xy$. Then $df = y\,dx + x\,dy = x\,(dy + y\,d\log x)$, and $J_D(f) = (x\partial_x f, \partial_y f) = (xy, x) = xR$. So $m = x$ and $\omega = dy + y\,d\log x$, with $c_1 = y \in \mathfrak{m}$ and $d_1 = 1$. We are in Case 2, with $\mathfrak{F} = R\,D_1$ and $D_1 = x\partial_x - y\partial_y$. Here $R' = R$, because there are no $D'_j$. The element $\tilde{y} = y$ has $\partial_y(\tilde{y}) = 1$, and it is homogeneous of weight $\chi = -1$, since $D_1(y) = -y$. So $\zeta = y$, and Step 11 gives $b_1 = 1$, $\eta_1 = x$ and $t = yx = f$. This is form (2). The divisor of the monomial $t$ is $\{x, y\}$, which is larger than $D$. The Euler type derivation $D_1$ of $\mathfrak{F}$ finds the new component $y = 0$.

**Example 4.4.22 (a blow-up that is not toroidal).** Let $R = k[y, u, v, w]_{(y, u, v, w)}$, $D = \emptyset$, $f = y + vw$ and $Z = (y, u)$. The center $Z$ has normal crossings with $D$, and it is not a stratum of $D$. We have $J_\emptyset(f) = (\partial_y f, \partial_u f, \partial_v f, \partial_w f) = (1, 0, w, v) = R$. By Lemma 4.4.18, part 1, $T_{\emptyset,Z}$ is generated by $y\partial_y$, $u\partial_y$, $y\partial_u$, $u\partial_u$, $\partial_v$ and $\partial_w$. Their values at $f$ are $y$, $u$, $0$, $0$, $w$, $v$. So $J_{\emptyset,Z}(f) = (y, u, v, w) = \mathfrak{m}$. Let $P$ be a point of $X'$ over the closed point of $\operatorname{Spec} R$, in the chart $C_u = R[y']$ with $y' = y/u$, and let $R_1 = (C_u)_P$. Then $y, u, v, w \in P$. By Lemma 4.4.18, $J_{D'}(f) = \mathfrak{m}R_1 = (u, v, w)R_1$, since $y = uy'$. This ideal is not principal. Indeed, let $S = k[u, y', v, w]$, a polynomial ring in four variables, because $k(y, u, v, w) = k(u, y', v, w)$. Then $C_u$ is the localization of $S$ at the set of the polynomials in $y = uy', u, v, w$ that are not in $(y, u, v, w)$, so $R_1$ is a localization of $S$ at a prime that contains $(u, v, w)$. In $S$ the ideal $(u, v, w)$ is a prime of height 3: the quotient $k[y']$ is a domain, the chain $0 \subsetneq (u) \subsetneq (u, v) \subsetneq (u, v, w)$ shows that the height is at least 3, and Krull's height theorem shows that it is at most 3. So $(u, v, w)R_1$ is a prime of height 3. A principal prime ideal has height at most 1 by Krull's principal ideal theorem. In the chart $C_y$ the same argument applies to $(y, v, w)$. So at each point of $X'$ over the closed point, the principal ideal $J_\emptyset(f) = R$ becomes the ideal $J_{D'}(f)$, which is not principal. The element $t = f$ is a first integral, and $f$ is a regular parameter, so $J_{\{f\}}(f) = fR$. But $Z$ does not have normal crossings with the divisor $\{f\}$: the ring $R/(y, u, f) = k[v, w]_{(v, w)}/(vw)$ is not a domain, while for a center with normal crossings with $\{f\}$ this ring would be a regular local ring.

### What stays open

Corollary 4.4.17 turns the hypothesis $\mathrm{FLM}(n, k)$ of Definition 4.4.9 into a statement on ideals. Over a perfect field $k$, $\mathrm{FLM}(n, k)$ is equivalent to the following statement. Let $E/k$ be a function field of transcendence degree $n$, let $v$ be a valuation of $E/k$, let $A \subseteq \mathcal{O}_v$ be an affine model whose local ring at the center of $v$ is regular, and let $f \in A$ be an element that is not a $p$-th power in $E$. Then there are an affine model $A'$ with $A \subseteq A' \subseteq \mathcal{O}_v$ whose local ring $R'$ at the center of $v$ is regular, and a normal crossings divisor $D$ of $R'$, such that $J_D(f)$ is a principal ideal of $R'$.

This existence statement is open for $n \ge 4$. We do not prove it. This section does not prove local uniformization in transcendence degree 4 or more, and it does not prove resolution of singularities in dimension 4 or more. The open case of local uniformization, Volume 9, Conjecture 2.3.1, stays open. What this section proves is: over a perfect field the existence statement for $n$ implies local uniformization in transcendence degree $n$ (Corollaries 4.4.12 and 4.4.17), and it is weaker than weak log monomialization (Proposition 4.4.10 and Example 4.4.20). For $n = 1$ the remark on discrete valuation rings in Section 4.3 gives $\mathrm{WLM}(1, k)$, but that remark has only a sketch of proof. For $n = 2$ and $n = 3$ this section does not prove the statement.

We state the status of the parts of this section in plain words.

- Lemmas 4.4.13 and 4.4.14 are proved in full here and in Lean.
- Proposition 4.4.15, Theorem 4.4.16, Corollary 4.4.17, Lemma 4.4.18 and Corollary 4.4.19 are proved here in full. They are not in Lean.
- Propositions 4.4.7, 4.4.8 and 4.4.10, Theorem 4.4.11 and Corollary 4.4.12 are proved here and in Lean. In Lean, Theorem 4.4.11 takes the monomial step, Theorem 4.3.14, as a hypothesis, and Corollary 4.4.12 takes also the theorem of Temkin as a hypothesis.
- $\mathrm{FLM}(n, k)$ is a hypothesis. It is open for $n \ge 4$.

The log Jacobian ideal removes one difficulty and not the main one. It does not depend on the choice of $h$ in $f - h^p$, so the problem of the maximum of the values of $f - h^p$ at the end of Section 4.3 does not appear in its definition. But a proof of the existence statement must choose the models, and Corollary 4.4.19 and Example 4.4.22 show what can happen. The toroidal blow-ups do not change $J_D(f)$. Other blow-ups with normal crossings make it smaller, and they can make a principal ideal not principal. If we add a component to $D$, the ideal becomes smaller (Lemma 4.4.4, part 3), and if we remove one, it becomes larger. We do not know a choice of centers and divisors that makes $J_D(f)$ principal along each valuation in transcendence degree 4. Along a valuation with a defect, Section 4.3 showed that the values of $f - h^p$ increase without a maximum. We do not know if, along such a valuation, the ideal $J_D(f)$ becomes principal on some model.

### References and remarks

The theorem of Temkin and the reduction to steps of degree $p$ are [Tem13]; see Sections 4.1 to 4.3. The facts on $p$-bases and differentials of fields are in [Mat, Section 26], and the exact sequence of the proof of Lemma 4.4.1 is in [Mat, Section 25]. The regularity of $R'$ in Step 4 of the proof of Theorem 4.4.16 uses the descent of regularity along flat local maps [Mat, Section 23], the unique factorization in regular local rings [Mat, Section 20], and the going down property of flat extensions [Mat, Section 9]. The module $\Omega_R(\log D)$ is the module of logarithmic differentials of the log structure of $D$ in the sense of K. Kato, Logarithmic structures of Fontaine-Illusie (1989). The proof of Theorem 4.4.16 uses only commuting derivations of the two kinds of Lemmas 4.4.13 and 4.4.14. We do not know if Theorem 4.4.16 holds for a log regular ring in the sense of Kato in place of a regular local ring with a normal crossings divisor. The Lean names of this section are in the Lean library. Proposition 4.4.15, Theorem 4.4.16, Corollary 4.4.17, Lemma 4.4.18 and Corollary 4.4.19 have no Lean proof.
