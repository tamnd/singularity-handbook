---
title: The case of equality
nodes: []
sources: [ZS2, Kuh-book, KK05, Kuh10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The case of equality

When the Abhyankar inequality is an equality, the value group and the residue field are as simple as possible. In this section we prove this, and we define Abhyankar valuations. The notation is that of Section 2.1.

**Lemma 2.2.1.** Let $(L/K, w)$ be an extension of valued fields, and let $x_1, \dots, x_r$ and $y_1, \dots, y_s$ be as in Theorem 2.1.4, with $\gamma_i = w(x_i)$. Let $K_0 = K(x_1, \dots, x_r, y_1, \dots, y_s) \subseteq L$ and let $w_0$ be the restriction of $w$ to $K_0$. Then
$$\Gamma_{w_0} = \Gamma_v \oplus \mathbb{Z}\gamma_1 \oplus \dots \oplus \mathbb{Z}\gamma_r, \qquad K_0w_0 = Kv(\bar{y}_1, \dots, \bar{y}_s).$$

Lean: none yet

*Proof.* The sum $\Gamma_v + \sum \mathbb{Z}\gamma_i$ is direct, because the $\gamma_i$ are independent modulo $\Gamma_v$. Each nonzero element of $K[x, y]$ has the form $F = \sum_a x^ap_a$, where $a$ runs over a finite subset of $\mathbb{N}^r$ and each $p_a$ is a nonzero polynomial in $y$ with coefficients in $K$. By Lemma 2.1.2, $w(p_a) = \min v(\text{coefficients of } p_a) \in \Gamma_v$, and $w(F) = \min_a (a \cdot \gamma + w(p_a))$. So $w(F) \in \Gamma_v + \sum \mathbb{Z}\gamma_i$. Since $K_0$ is the field of fractions of $K[x, y]$, the value group $\Gamma_{w_0}$ is in this sum. The other inclusion is clear.

For the residue field, the values $a \cdot \gamma + w(p_a)$ lie in distinct cosets of $\Gamma_v$, so the minimum is attained at exactly one $a = a_0$. Choose a coefficient $c$ of $p_{a_0}$ of least value. Then
$$\frac{F}{cx^{a_0}} = \frac{p_{a_0}}{c} + \sum_{a \ne a_0} \frac{x^ap_a}{cx^{a_0}},$$
and each term of the sum has positive value. So $F/(cx^{a_0})$ has value 0, and its residue is the residue of $p_{a_0}/c$. This is a polynomial in $\bar{y}_1, \dots, \bar{y}_s$ with coefficients in $Kv$. Now let $F, G \in K[x, y]$ be nonzero with $w(F) = w(G)$, and write $F = cx^{a_0}F'$ and $G = c'x^{b_0}G'$ as above, with $w(F') = w(G') = 0$. Then $w(cx^{a_0}) = w(c'x^{b_0})$, so $a_0 \cdot \gamma - b_0 \cdot \gamma \in \Gamma_v$. Thus $a_0 = b_0$ and $v(c) = v(c')$. So $F/G = (c/c')(F'/G')$ has residue $\overline{c/c'} \cdot \overline{F'}/\overline{G'} \in Kv(\bar{y})$. Each element of $K_0$ of value 0 is such a quotient $F/G$. $\square$

**Theorem 2.2.2.** Let $(L/K, w)$ be an extension of valued fields with $L/K$ finitely generated, and assume that
$$\operatorname{rr}(\Gamma_w/\Gamma_v) + \operatorname{trdeg}(Lw/Kv) = \operatorname{trdeg}(L/K).$$
Then $\Gamma_w/\Gamma_v$ is a finitely generated abelian group, and $Lw$ is a finitely generated field extension of $Kv$.

Lean: none yet

*Proof.* Let $r = \operatorname{rr}(\Gamma_w/\Gamma_v)$ and $s = \operatorname{trdeg}(Lw/Kv)$. Choose $x_1, \dots, x_r$ and $y_1, \dots, y_s$ as in Theorem 2.1.4, with $r$ values independent modulo $\Gamma_v$ and $s$ residues that form a transcendence basis of $Lw/Kv$. Let $K_0$ be as in Lemma 2.2.1. By Theorem 2.1.4 the $r + s$ elements are algebraically independent over $K$. Since $r + s = \operatorname{trdeg}(L/K)$, the extension $L/K_0$ is algebraic, and it is finite because $L/K$ is finitely generated. By Corollary 2.1.3, $\Gamma_w/\Gamma_{w_0}$ is finite and $Lw$ is a finite extension of $K_0w_0$. By Lemma 2.2.1, $\Gamma_{w_0}/\Gamma_v \cong \mathbb{Z}^r$, so $\Gamma_w/\Gamma_v$ is an extension of a finite group by $\mathbb{Z}^r$, which is finitely generated. Also by Lemma 2.2.1, $K_0w_0 = Kv(\bar{y})$ is finitely generated over $Kv$, so $Lw$ is finitely generated over $Kv$. $\square$

### Abhyankar valuations

**Definition 2.2.3 (Abhyankar valuation).** Let $K/k$ be a function field. A valuation $v$ of $K/k$ is an *Abhyankar valuation* if
$$\operatorname{rr} \Gamma_v + \operatorname{trdeg}(Kv/k) = \operatorname{trdeg}(K/k).$$
An Abhyankar valuation with $\operatorname{rr} \Gamma_v = 1$ is a *divisorial valuation*.

**Corollary 2.2.4.** Let $v$ be an Abhyankar valuation of a function field $K/k$, with rational rank $r$. Then $\Gamma_v \cong \mathbb{Z}^r$ as a group, and $Kv$ is a finitely generated extension of $k$. A divisorial valuation is discrete of rank 1.

Lean: `Singularity.IsAbhyankarValuation.free_valueGroup`, `Singularity.IsAbhyankarValuation.exists_basis_valueGroup` (the claim $\Gamma_v \cong \mathbb{Z}^r$), `Singularity.IsAbhyankarValuation.fg_residueField` (the claim on $Kv$), `Singularity.IsAbhyankarValuation.nonempty_orderMonoidIso_units_valueGroup` (the claim on divisorial valuations)

*Proof.* Apply Theorem 2.2.2 to $(K/k, v)$. The group $\Gamma_v$ is finitely generated, and it is torsion free because it is ordered (Section 1.1), so $\Gamma_v \cong \mathbb{Z}^r$. If $r = 1$, then $\Gamma_v \cong \mathbb{Z}$ as a group. An ordered group isomorphic to $\mathbb{Z}$ is isomorphic to $\mathbb{Z}$ as an ordered group: map a generator that is positive to 1. $\square$

The Lean proof of the claim on $\Gamma_v$ does not use Theorem 2.2.2 in full. It uses the subfield $K_0 = k(x_1, \dots, x_r, y_1, \dots, y_s)$ of Volume 5, Section 2.2. The values of the nonzero elements of $K_0$ are in the group $\Gamma_0$ that $v(x_1), \dots, v(x_r)$ generate, because the restriction of $v$ to $K_0$ is monomial. The degree $[K : K_0]$ is finite. Nonzero elements of $K$ with values in different cosets of $\Gamma_0$ are linearly independent over $K_0$, by the argument of Lemma 2.1.2, so $\Gamma_v/\Gamma_0$ is finite (`Singularity.finite_quotient_of_valuation_mem`). The generators of $\Gamma_0$ and one element of each coset generate $\Gamma_v$. The Lean proof of the claim on $Kv$ uses the same subfield $K_0$. Each element of $K_0$ with value $0$ is $c\,(1 + m)$ with $c \in k(y_1, \dots, y_s)$ and $v(m) > 0$, because the restriction of $v$ to $K_0$ is monomial over $k(y)$. So the residues of $K_0$ are in $k(\bar y_1, \dots, \bar y_s)$ (`Singularity.residue_mem_adjoin_of_mem_adjoin_sumElim`). Elements of $\mathcal{O}_v$ with residues that are linearly independent over $k(\bar y)$ are linearly independent over $K_0$, by the argument of Lemma 2.1.2. Thus $[Kv : k(\bar y)] \le [K : K_0]$ (`Singularity.IsAbhyankarValuation.finiteDimensional_residueField`), and $Kv$ is generated over $k$ by the $\bar y_j$ and a basis over $k(\bar y)$. The Lean proof of the last claim follows the proof above. A group isomorphism from $\Gamma_v$ to $\mathbb{Z}$ that maps a positive generator to $1$ preserves the order (`Singularity.nonempty_orderMonoidIso_multiplicativeInt`).

The order on $\mathbb{Z}^r$ is not determined by $r$. Examples 1.6.3 and 1.6.4 give two Abhyankar valuations of $k(x, y)$ with $\Gamma_v \cong \mathbb{Z}^2$. In the first the order comes from an embedding in $\mathbb{R}$, and the rank is 1. In the second the order is lexicographic, and the rank is 2.

A divisorial valuation of $K/k$ has $\operatorname{trdeg}(Kv/k) = \operatorname{trdeg}(K/k) - 1$. On a suitable normal model its center is the generic point of a prime divisor, and the valuation is the order of vanishing along this divisor [ZS2, Chapter VI, Section 14]. We do not prove this here. Local uniformization is known for Abhyankar valuations in each characteristic and in each dimension (Chapter 4). One reason is the generalized stability theorem of Kuhlmann. A special case states: if $v$ is an Abhyankar valuation of $K/k$, then $(K, v)$ is a *defectless* valued field. Kuhlmann proves this theorem in [Kuh10]. Section 3.2 defines the defect, and Section 4.2 explains why it is the obstruction. Knaf and Kuhlmann use the theorem in [KK05].
