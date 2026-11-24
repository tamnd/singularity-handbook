---
title: The inequality
nodes: [SG0000000Y]
sources: [Abh56, ZS2, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The inequality

In this section $(L/K, w)$ is an extension of valued fields, as at the end of Section 1.3. So $w$ is a valuation of $L$, its restriction to $K$ is $v$, $\Gamma_v \subseteq \Gamma_w$ and $Kv \subseteq Lw$. We prove one lemma on linear independence, and we deduce the Abhyankar inequality from it.

### Independent elements

**Definition 2.1.1 (ramification index, residue degree).** The *ramification index* of $(L/K, w)$ is the index $e = (\Gamma_w : \Gamma_v)$, and the *residue degree* is $f = [Lw : Kv]$. Each of them can be infinite.

**Lemma 2.1.2 (independence lemma).** Let $x_1, \dots, x_m \in L^\times$ be elements whose values $w(x_i)$ lie in distinct cosets of $\Gamma_v$ in $\Gamma_w$. Let $y_1, \dots, y_n \in \mathcal{O}_w$ be elements whose residues $\bar{y}_1, \dots, \bar{y}_n$ are linearly independent over $Kv$. Then for all $c_{ij} \in K$,
$$w\Big(\sum_{i,j} c_{ij}x_iy_j\Big) = \min_{i,j}\big(v(c_{ij}) + w(x_i)\big).$$
In particular the $mn$ elements $x_iy_j$ are linearly independent over $K$.

Lean: none yet

*Proof.* Fix $i$ and let $s_i = \sum_j c_{ij}y_j$. We first show that $w(s_i) = \min_j v(c_{ij})$. If all $c_{ij}$ are 0 this is clear. Otherwise choose $j_0$ with $v(c_{ij_0})$ minimal, and let $c = c_{ij_0}$. Then $s_i/c = \sum_j (c_{ij}/c)y_j$, and each $c_{ij}/c$ is in $\mathcal{O}_v$. Its residue is $\sum_j \overline{c_{ij}/c}\,\bar{y}_j$. This is not 0, because the $\bar{y}_j$ are independent and the coefficient of $\bar{y}_{j_0}$ is 1. So $w(s_i/c) = 0$ and $w(s_i) = v(c)$.

Now $\sum_{i,j} c_{ij}x_iy_j = \sum_i x_is_i$. For each $i$ with $s_i \ne 0$, the value $w(x_is_i) = w(x_i) + w(s_i)$ lies in the coset $w(x_i) + \Gamma_v$. These cosets are distinct, so the nonzero terms $x_is_i$ have distinct values. By Lemma 1.1.3 the value of the sum is the least of these values. This is the formula. If not all $c_{ij}$ are 0, the right side is finite, so the sum is not 0. $\square$

**Corollary 2.1.3.** Let $L/K$ be finite of degree $n$. Then $ef \le n$. If $L/K$ is algebraic, then $\Gamma_w/\Gamma_v$ is a torsion group and $Lw/Kv$ is algebraic.

Lean: none yet

*Proof.* If $e \ge m$ and $f \ge n'$, choose $x_1, \dots, x_m$ with values in distinct cosets and $y_1, \dots, y_{n'}$ with independent residues. Lemma 2.1.2 gives $mn'$ elements of $L$ that are independent over $K$, so $mn' \le n$. Thus $e$ and $f$ are finite and $ef \le n$. If $L/K$ is algebraic, each element of $L$ lies in a finite subextension $L'$. The value of the element is then in $\Gamma_{w|L'}$, which has finite index over $\Gamma_v$, and its residue, if it is defined, is algebraic over $Kv$. $\square$

### The relative inequality

**Theorem 2.1.4 (relative Abhyankar inequality).** Let $(L/K, w)$ be an extension of valued fields. Then
$$\operatorname{rr}(\Gamma_w/\Gamma_v) + \operatorname{trdeg}(Lw/Kv) \le \operatorname{trdeg}(L/K).$$
More precisely, let $x_1, \dots, x_r \in L^\times$ be elements whose values are linearly independent over $\mathbb{Z}$ modulo $\Gamma_v$, and let $y_1, \dots, y_s \in \mathcal{O}_w$ be elements whose residues are algebraically independent over $Kv$. Then $x_1, \dots, x_r, y_1, \dots, y_s$ are algebraically independent over $K$.

Lean: none yet

Here $\operatorname{rr}(\Gamma_w/\Gamma_v) = \dim_\mathbb{Q}((\Gamma_w/\Gamma_v) \otimes \mathbb{Q})$. It is the largest number of elements of $\Gamma_w$ that are linearly independent over $\mathbb{Z}$ modulo $\Gamma_v$. The first statement follows from the second.

*Proof.* Let $\gamma_i = w(x_i)$. For $a \in \mathbb{N}^r$ the monomial $x^a$ has value $a \cdot \gamma$. If $a \ne a'$, then $a \cdot \gamma - a' \cdot \gamma = \sum (a_i - a'_i)\gamma_i$ is not in $\Gamma_v$, by the independence modulo $\Gamma_v$. So distinct monomials $x^a$ have values in distinct cosets of $\Gamma_v$. For $b \in \mathbb{N}^s$ the monomial $y^b$ is in $\mathcal{O}_w$ with residue $\bar{y}^b$. Distinct monomials in algebraically independent elements are linearly independent, so the residues $\bar{y}^b$ are linearly independent over $Kv$. Let $F = \sum_{a,b} c_{ab}X^aY^b$ be a nonzero polynomial over $K$. Apply Lemma 2.1.2 to the finitely many $x^a$ and $y^b$ that occur in $F$. It gives $F(x, y) \ne 0$. $\square$

**Theorem 2.1.5 (Abhyankar inequality).** Let $K/k$ be a field extension and let $v$ be a valuation of $K/k$. Then
$$\operatorname{rr} \Gamma_v + \operatorname{trdeg}(Kv/k) \le \operatorname{trdeg}(K/k).$$

Node: SG0000000Y · Lean: `Singularity.abhyankar_inequality` (planned, no Lean statement yet)

*Proof.* Apply Theorem 2.1.4 to $(K/k, v)$. The restriction of $v$ to $k$ is trivial, so its value group is 0 and its residue field is $k$. $\square$

**Corollary 2.1.6.** Let $K/k$ be a function field of transcendence degree $d$, and let $v$ be a valuation of $K/k$. Then the rank of $v$, the rational rank of $v$ and the dimension of $v$ are at most $d$. The valuation ring $\mathcal{O}_v$ has dimension at most $d$.

Lean: none yet

*Proof.* Theorem 2.1.5 bounds the rational rank and the dimension. Proposition 1.2.5 bounds the rank by the rational rank, and Corollary 1.2.4 gives $\dim \mathcal{O}_v$ as the rank. $\square$

Abhyankar proved the inequality in the local form of Section 2.3 [Abh56]. The field form above, with the proof by Lemma 2.1.2, is in [ZS2, Chapter VI, Section 10] and in [Kuh-book]. The proof uses no Noetherian ring, so it works for each extension of valued fields.
