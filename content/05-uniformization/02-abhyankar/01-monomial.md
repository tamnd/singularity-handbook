---
title: Monomial valuations
nodes: [SG0000000Y, SG0000004D]
sources: [ZS2, Ful93, Spi83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Monomial valuations

Let $k$ be a field of any characteristic, and let $K = k(x_1, \dots, x_r)$ be a field of rational functions. Let $\Gamma$ be an ordered abelian group, and let $\gamma_1, \dots, \gamma_r \in \Gamma$ be linearly independent over $\mathbb{Z}$. By Volume 3, Lemma 1.6.1, the formula
$$v\Big(\sum_\alpha c_\alpha x^\alpha\Big) = \min\{\alpha \cdot \gamma : c_\alpha \ne 0\}$$
for polynomials defines a valuation $v$ of $K/k$, where $\alpha \cdot \gamma = \sum \alpha_i\gamma_i$.

**Definition 2.1.1 (monomial valuation).** The valuation $v$ is the *monomial valuation* of $K = k(x_1, \dots, x_r)$ with *weights* $\gamma_1, \dots, \gamma_r$.

For $\varepsilon \in \mathbb{Z}^r$ we write $x^\varepsilon = \prod x_i^{\varepsilon_i}$, a *Laurent monomial*. The Laurent monomials form a group $M \cong \mathbb{Z}^r$ under multiplication.

**Lemma 2.1.2.** Let $v$ be a monomial valuation as above.

1. The map $x^\varepsilon \mapsto v(x^\varepsilon) = \varepsilon \cdot \gamma$ is an isomorphism of $M$ onto $\Gamma_v = \bigoplus_i \mathbb{Z}\gamma_i$.
2. The residue field of $v$ is $k$.
3. $v$ is an Abhyankar valuation with $\operatorname{rr}\Gamma_v = r$.

Lean: `Singularity.IsMonomialValuation.existsUnique_valuation_eq`, `Singularity.IsMonomialValuation.valueGroupBasis` (part 1), `Singularity.IsMonomialValuation.algebraMap_residueField_bijective` (part 2), `Singularity.IsMonomialValuation.isAbhyankarValuation` (part 3)

*Proof.* The map is a surjective homomorphism onto $\bigoplus \mathbb{Z}\gamma_i$, and it is injective because the $\gamma_i$ are independent. Each polynomial has a value of the form $\alpha \cdot \gamma$, so $\Gamma_v = \bigoplus \mathbb{Z}\gamma_i$. Since distinct monomials have distinct values, the initial form of a polynomial $f$ in the sense of Volume 3, Lemma 1.6.1, is one term $c_\alpha x^\alpha$. By the residue formula there, the residue of $f/g$ with $v(f) = v(g)$ is the residue of $c_\alpha x^\alpha/(d_\alpha x^\alpha) = c_\alpha/d_\alpha \in k$. So $Kv = k$. Then $\operatorname{rr}\Gamma_v + \operatorname{trdeg}_k Kv = r = \operatorname{trdeg}_k K$. $\square$

The Lean proof of part 3 does not use part 2. In Lean, a monomial valuation is a valuation $v$ of $K/k$ and elements $x_1, \dots, x_r \in K^\times$ that generate $K$ as a field over $k$, such that the values $v(x_i)$ are linearly independent over $\mathbb{Z}$. Then $\operatorname{rr}\Gamma_v \ge r$. The field $K$ is algebraic over $k(x_1, \dots, x_r)$, so $\operatorname{trdeg}_k K \le r$. The Abhyankar inequality (Volume 3, Theorem 2.1.5) gives $\operatorname{rr}\Gamma_v + \operatorname{trdeg}_k Kv \le \operatorname{trdeg}_k K \le r \le \operatorname{rr}\Gamma_v$. So all these numbers are equal, $\operatorname{trdeg}_k Kv = 0$, and $v$ is an Abhyankar valuation.

The Lean proofs of parts 1 and 2 do not use the residue formula of Volume 3. Let $z \ne 0$, and write $z = f/g$ with polynomials $f, g$ in $x$. The leading term of $f$ gives $f = c_\alpha x^\alpha(1 + F)$ with $c_\alpha \in k^\times$ and $v(F) > 0$, and in the same way $g = d_\beta x^\beta(1 + G)$ with $v(G) > 0$. So $z(1 + G) = c\,x^\varepsilon(1 + F)$ with $c = c_\alpha/d_\beta$ and $\varepsilon = \alpha - \beta$. Thus $v(z) = v(x^\varepsilon)$, and the map of part 1 is surjective. If $v(z) = 0$, then $v(x^\varepsilon) = 0$, so $\varepsilon = 0$, and the residue of $z$ is the residue of $c$. This is part 2.

### Cones in ordered groups

Let $\Gamma$ be an ordered abelian group of finite rational rank, and let $V = \Gamma \otimes \mathbb{Q}$. The order of $\Gamma$ extends to a unique order of $V$: for $w \in V$ choose $n \ge 1$ with $nw \in \Gamma$, and put $w > 0$ if $nw > 0$. For elements $m_1, \dots, m_s$ of $V$, the *rational cone* is the set of $\sum q_im_i$ with $q_i \in \mathbb{Q}_{\ge 0}$. A *positive basis* is a basis of $V$ over $\mathbb{Q}$ whose elements are positive.

**Lemma 2.1.3 (cone lemma).** Let $V$ be an ordered $\mathbb{Q}$-vector space of finite dimension $r$, and let $E \subseteq V$ be a finite set of elements $\ge 0$. Then there is a positive basis $m_1, \dots, m_r$ of $V$ such that $E$ lies in its rational cone.

Lean: `Singularity.coneLemma`

*Proof.* We use induction on $r$. For $r = 0$ there is nothing to prove. Let $r \ge 1$.

Convex subspaces. A convex subgroup $C$ of $V$ is a $\mathbb{Q}$-subspace: if $c \in C$ and $n \ge 1$, then $c/n$ lies between $0$ and $c$, so $c/n \in C$. The convex subgroups are totally ordered by inclusion (Volume 3, Lemma 1.2.2), so there are at most $r + 1$ of them. Let $H$ be the largest proper one, and let $W = V/H$, with the induced order. The order is well defined, because $H$ is convex. A convex subgroup of $W$ has a convex preimage in $V$ that contains $H$. So $W$ has no convex subgroups other than $0$ and $W$. Then $W$ is archimedean: for $a > 0$ in $W$, the set of $w$ with $|w| \le na$ for some $n$ is a convex subgroup, and it is not 0, so it is $W$. By the theorem of Hölder [ZS2, Chapter VI], there is an injective homomorphism of ordered groups $\psi : W \to \mathbb{R}$. It is $\mathbb{Q}$-linear, because it is additive.

The archimedean case. Let $s = \dim W \ge 1$, let $W_\mathbb{R} = W \otimes \mathbb{R} \cong \mathbb{R}^s$, and let $\psi_\mathbb{R}$ be the $\mathbb{R}$-linear extension of $\psi$. Let $E_W$ be the set of nonzero images of elements of $E$ in $W$. They are positive, so $\psi(e) > 0$ for $e \in E_W$. The points $e/\psi(e)$ lie in the affine hyperplane $\Sigma = \{\psi_\mathbb{R} = 1\}$. Choose points $p_1, \dots, p_s \in \Sigma$, affinely independent, such that each point $e/\psi(e)$ lies in the interior of their convex hull relative to $\Sigma$. This is possible because a finite set lies in the interior of a large simplex. Since $0 \notin \Sigma$, the vectors $p_i$ are linearly independent, and each $e \in E_W$ is $\sum_i \lambda_i(e)p_i$ with all $\lambda_i(e) > 0$. The coefficients of $e$ in a basis $q_1, \dots, q_s$ depend continuously on $(q_1, \dots, q_s)$ near $(p_1, \dots, p_s)$, by Cramer's rule. Since $W$ is dense in $W_\mathbb{R}$, we can choose $q_i \in W$ near $p_i$ such that the $q_i$ are a basis, $\psi(q_i) > 0$, and each $e \in E_W$ has positive coefficients in the basis $q_i$. The coefficients are rational, because $e$ and the $q_i$ lie in $W$. Since $\psi$ is an embedding of ordered groups, $q_i > 0$ in $W$.

The lift. Choose $\tilde{q}_i \in V$ with image $q_i$. An element of $V$ whose image in $W$ is positive is larger than each element of $H$, by convexity. So $\tilde{q}_i > 0$. The elements of $E \cap H$ are $\ge 0$. By induction there is a positive basis $m_1, \dots, m_h$ of $H$ such that $E \cap H$ lies in its rational cone. For $e \in E \setminus H$ write the image of $e$ as $\sum_i \lambda_i(e)q_i$ with $\lambda_i(e) \ge 0$ rational and $\sum_i \lambda_i(e) > 0$, and write
$$e - \sum_i \lambda_i(e)\tilde{q}_i = \sum_j c_j(e)m_j \in H$$
with $c_j(e) \in \mathbb{Q}$. For an integer $N \ge 0$ let $q_i^N = \tilde{q}_i - N\sum_j m_j$. Its image in $W$ is $q_i$, so $q_i^N > 0$. Then
$$e = \sum_i \lambda_i(e)q_i^N + \sum_j \Big(c_j(e) + N\sum_i \lambda_i(e)\Big)m_j.$$
For $N$ large all coefficients are $\ge 0$, for each of the finitely many $e \in E \setminus H$. So $m_1, \dots, m_h, q_1^N, \dots, q_s^N$ is the required basis. $\square$

The Lean proof goes the other way. It does not use the induction above. It multiplies a basis of $V$ by a common denominator, so that the lattice the basis generates contains $E$. Then it applies the lattice lemma (Lemma 2.1.4) to this lattice. The Lean statement also gives a little more: each $e \in E$ has coordinates in $\mathbb{N}$.

**Lemma 2.1.4 (lattice lemma).** Let $\Gamma \cong \mathbb{Z}^r$ be an ordered group, and let $D \subseteq \Gamma$ be a finite set of elements $\ge 0$. Then there is a basis $m_1, \dots, m_r$ of $\Gamma$ over $\mathbb{Z}$ such that each $m_i$ is positive and each $d \in D$ is a combination $\sum n_im_i$ with $n_i \in \mathbb{N}$.

Node: SG0000004D · Lean: `Singularity.latticeLemma`, `Singularity.latticeLemma_of_injective` (the form with matrices of Lemma 2.1.8)

*Proof.* Let $V = \Gamma \otimes \mathbb{Q}$, which contains $\Gamma$. By Lemma 2.1.3 there is a positive basis $m_1, \dots, m_r$ of $V$ whose rational cone contains $D$. Each element of a basis of $\Gamma$ is a rational combination of the $m_i$. Let $N \ge 1$ be a common denominator of these coefficients, and replace each $m_i$ by $m_i/N$. Then the lattice $L = \bigoplus \mathbb{Z}m_i$ contains $\Gamma$, the $m_i$ are positive, and the rational cone is the same.

Thus we have a positive basis $m$ of $V$ with $\Gamma \subseteq L$ and $D$ in the rational cone. Let $\Delta = (L : \Gamma)$, a positive integer. If $\Delta = 1$, then $L = \Gamma$, and each $d \in D$ is $\sum q_im_i$ with $q_i \ge 0$ rational and integral, so $q_i \in \mathbb{N}$. We are done. Assume $\Delta > 1$. We construct another positive basis $m'$ with the same properties and with $(L' : \Gamma) < \Delta$. Then induction on $\Delta$ ends the proof.

Let $\Lambda \subseteq \mathbb{Z}^r$ be the group of coefficient vectors $c$ with $\sum c_im_i \in \Gamma$. It has index $\Delta$ in $\mathbb{Z}^r$. Its dual group $\Lambda^* = \{t \in \mathbb{Q}^r : c \cdot t \in \mathbb{Z} \text{ for all } c \in \Lambda\}$ contains $\mathbb{Z}^r$ with index $\Delta$, so it contains some $t \notin \mathbb{Z}^r$. After we subtract an integer vector, $0 \le t_i < 1$ for each $i$, and $t \ne 0$. Among the indices $i$ with $t_i > 0$, choose $l$ such that $m_l/t_l$ is the smallest of the elements $m_i/t_i$ in the order of $V$. Put
$$m'_l = \frac{m_l}{t_l}, \qquad m'_j = m_j - \frac{t_j}{t_l}m_l \quad (j \ne l).$$

The new basis is positive. Clearly $m'_l > 0$. If $t_j = 0$, then $m'_j = m_j > 0$. If $t_j > 0$, then $m_l/t_l \le m_j/t_j$, so $m'_j = t_j(m_j/t_j - m_l/t_l) \ge 0$, and $m'_j \ne 0$ because the $m_i$ are linearly independent.

The cone grows. We have $m_l = t_lm'_l$ and $m_j = m'_j + t_jm'_l$ for $j \ne l$. So each $m_i$ is in the rational cone of $m'$, and so is $D$.

The lattice. Let $L' = \bigoplus \mathbb{Z}m'_i$. An element $\gamma = \sum c_im_i$ of $\Gamma$ has $c \in \Lambda$, and
$$\gamma = \sum_{j \ne l} c_jm'_j + (c \cdot t)\, m'_l.$$
Since $t \in \Lambda^*$, the coefficient $c \cdot t$ is an integer. So $\Gamma \subseteq L'$. The matrix that expresses $m'$ in terms of $m$ has determinant $1/t_l$, so the covolume of $L'$ is $1/t_l$ times the covolume of $L$, and $(L' : \Gamma) = t_l\Delta < \Delta$. $\square$

The proof is an algorithm. It needs to compare elements of $V$, which is possible for an explicit ordered group such as a subgroup of $\mathbb{R}$ with an explicit basis.

The Lean proof of Lemma 2.1.4 does not use Lemma 2.1.3 or the group $V$. It uses the same induction as the proof of Lemma 2.1.3, but on $\Gamma$ itself, and Lemma 2.1.8 for the archimedean step. We give it here.

*Second proof.* We use induction on $r$. For $r = 0$ there is nothing to prove. Let $r \ge 1$, let $b_1, \dots, b_r$ be a basis of $\Gamma$, and let $t = \sum_i |b_i| > 0$.

The subgroup $H$. Let $H$ be the set of $a \in \Gamma$ with $n|a| < t$ for each $n \in \mathbb{N}$. Since $n|a + b| \le 2n\max(|a|, |b|)$, the set $H$ is a subgroup. It is convex: if $0 \le a \le c$ and $c \in H$, then $n|a| \le n|c| < t$. Also $t \notin H$. For each $a \in \Gamma$ we have $a = \sum_i c_ib_i$ with $c_i \in \mathbb{Z}$, so $|a| \le Nt$ with $N = \sum_i |c_i|$. If $a \notin H$, then $t \le n|a|$ for some $n \ge 1$.

The splitting. If $na \in H$ with $n \ge 1$, then $|a| \le |na|$, so $a \in H$. Thus $\Gamma/H$ is torsion free. It is finitely generated, so it is free. So there is a subgroup $W$ with $\Gamma = H \oplus W$. The groups $H$ and $W$ are free of ranks $h$ and $s$ with $h + s = r$, and $s \ge 1$ because $t \notin H$. Write $a = a_H + a_W$ for the decomposition of $a \in \Gamma$. If $w \in W$ is not zero, then $w \notin H$.

Positivity. Let $a \ge 0$ in $\Gamma$. We show that $a_W \ge 0$. If $a_W < 0$, then $0 < -a_W \le a_H$, and convexity gives $-a_W \in H$. This is false, because $a_W \ne 0$. Similarly, if $w \in W$ is positive and $c \in H$, then $w + c > 0$. Otherwise $0 < w \le -c$, and convexity gives $w \in H$.

The archimedean step. The order of $\Gamma$ restricts to $W$, and $W$ is archimedean. Let $0 < a, b$ in $W$. Then $a \notin H$, so $t \le n a$ for some $n \ge 1$, and $b \le N t \le Nn a$ for some $N$. By the theorem of Hölder [ZS2, Chapter VI], there is an injective homomorphism of ordered groups $\psi : W \to \mathbb{R}$. Let $w_1, \dots, w_s$ be a basis of $W$ and let $\gamma = (\psi(w_1), \dots, \psi(w_s)) \in \mathbb{R}^s$. Then $a \cdot \gamma = \psi(\sum_i a_iw_i) \ne 0$ for each nonzero $a \in \mathbb{Z}^s$. The elements $d_W$ with $d \in D$ are $\ge 0$, so their coefficient vectors $a$ have $a \cdot \gamma \ge 0$. Lemma 2.1.8 gives a basis $q_1, \dots, q_s$ of $W$ with $\psi(q_i) > 0$, so $q_i > 0$, such that $d_W = \sum_i \lambda_i(d)q_i$ with $\lambda_i(d) \in \mathbb{N}$ for each $d \in D$.

The induction. The elements of $D \cap H$ are $\ge 0$. Since $h < r$, the induction hypothesis gives a basis $m_1, \dots, m_h$ of $H$ of positive elements such that each element of $D \cap H$ has coefficients in $\mathbb{N}$. For $d \in D$ write $d_H = \sum_j c_j(d)m_j$ with $c_j(d) \in \mathbb{Z}$.

The shear. Let $m = \sum_j m_j \in H$, and for $N \in \mathbb{N}$ let $q_i^N = q_i - Nm$. Then $q_i^N > 0$ by the positivity step, and $m_1, \dots, m_h, q_1^N, \dots, q_s^N$ is a basis of $\Gamma$. For $d \in D$ we have
$$d = \sum_i \lambda_i(d)q_i^N + \sum_j \Big(c_j(d) + N\sum_i \lambda_i(d)\Big)m_j.$$
If $d_W = 0$, then $d \in D \cap H$, and all coefficients are in $\mathbb{N}$. If $d_W \ne 0$, then $\sum_i \lambda_i(d) \ge 1$, and the coefficients are in $\mathbb{N}$ for $N$ large. Since $D$ is finite, one $N$ works for all $d \in D$. $\square$

### Local uniformization of monomial valuations

**Theorem 2.1.5 (monomial case).** Let $k$ be a field of any characteristic, and let $v$ be a monomial valuation of $K = k(x_1, \dots, x_r)$. Then $v$ has local uniformization. More precisely, for each finite subset $S$ of $\mathcal{O}_v$ there are Laurent monomials $u_1, \dots, u_r$ that form a basis of the group $M$, with $v(u_i) > 0$, such that $S \subseteq A_{(u_1, \dots, u_r)}$, where $A = k[u_1, \dots, u_r]$ is a polynomial ring.

Node: SG0000004D · Lean: `Singularity.hasLocalUniformization_of_isMonomialValuation`

*Proof.* Let $S \subseteq \mathcal{O}_v$ be finite. Write each $s \in S$ as $s = f_s/g_s$ with polynomials $f_s, g_s \ne 0$. Write $f_s = c\,x^\alpha(1 + F_s)$, where $c\,x^\alpha$ is the term of least value and $F_s$ is a sum of terms $c'x^\varepsilon$ with $v(x^\varepsilon) > 0$. Write $g_s = d\,x^\beta(1 + G_s)$ in the same way. Then
$$s = \frac{c}{d}\, x^{\alpha - \beta}\, \frac{1 + F_s}{1 + G_s}, \qquad v(x^{\alpha - \beta}) = v(s) \ge 0.$$
Let $D \subseteq \Gamma_v$ be the finite set of the values of $x^{\alpha - \beta}$ and of the Laurent monomials that occur in the $F_s$ and $G_s$, for $s \in S$. Its elements are $\ge 0$. By Lemma 2.1.4 there is a basis $m_1, \dots, m_r$ of $\Gamma_v$ of positive elements whose $\mathbb{N}$-span contains $D$. By Lemma 2.1.2, $m_i = v(u_i)$ for a basis $u_1, \dots, u_r$ of $M$, and each Laurent monomial whose value is in $D$ is a monomial in $u_1, \dots, u_r$ with exponents in $\mathbb{N}$.

Since $u_1, \dots, u_r$ is a basis of $M$, the $k$-algebra $k[M]$ of Laurent polynomials is $k[u_1^{\pm 1}, \dots, u_r^{\pm 1}]$. So the $u_i$ are algebraically independent over $k$, $K = k(u_1, \dots, u_r)$, and $v$ is the monomial valuation of $k(u_1, \dots, u_r)$ with weights $m_1, \dots, m_r$. Let $A = k[u_1, \dots, u_r]$. It is an affine model of $K/k$, and $A \subseteq \mathcal{O}_v$. Since the $m_i$ are positive, the center of $v$ on $A$ is $\mathfrak{p} = (u_1, \dots, u_r)$ (Volume 3, Lemma 1.6.1). The ring $A_\mathfrak{p}$ is regular of dimension $r$. The elements $x^{\alpha - \beta}$, $F_s$ and $G_s$ lie in $A$, and $F_s, G_s \in \mathfrak{p}$. So $1 + G_s \in A \setminus \mathfrak{p}$, and $s \in A_\mathfrak{p}$.

Let $A' = A[S]$. Then $S \subseteq A' \subseteq A_\mathfrak{p} \subseteq \mathcal{O}_v$, and $A'$ is an affine model of $K/k$. By Lemma 1.1.1, the local ring of $A'$ at the center of $v$ is $A_\mathfrak{p}$, which is regular. Proposition 4.1.6 of Volume 3 ends the proof. $\square$

**Corollary 2.1.6.** Let $k$ be a field of any characteristic, let $K = k(y_1, \dots, y_t, x_1, \dots, x_r)$ be a field of rational functions, and let $v$ be a valuation of $K/k$ that is trivial on $k(y_1, \dots, y_t)$ and is a monomial valuation of $K = k(y)(x_1, \dots, x_r)$ over the field $k(y)$. Then $v$ has local uniformization, and $v$ is an Abhyankar valuation of $K/k$ with residue field $k(y_1, \dots, y_t)$.

Node: SG0000004D · Lean: `Singularity.hasLocalUniformization_of_isMonomialValuation_adjoin`, `Singularity.IsMonomialValuation.isAbhyankarValuation_adjoin`, `Singularity.IsMonomialValuation.adjoin_residue_eq_top`, `Singularity.algebraicIndependent_residue`

*Proof.* By Lemma 2.1.2 over the field $k(y)$, the residue field is $k(y)$ and $\Gamma_v \cong \mathbb{Z}^r$. So $\operatorname{rr}\Gamma_v + \operatorname{trdeg}_k Kv = r + t$. The residues of $y_1, \dots, y_t$ are $y_1, \dots, y_t$, which are algebraically independent over $k$. By Theorem 2.1.5 over $k(y)$ and Lemma 1.4.2, $v$ has local uniformization over $k$. $\square$

In this corollary, local uniformization means local uniformization over $k$: the affine models are of finite type over $k$. An affine model of $K/k(y)$ is of finite type over $k(y)$, and it is not of finite type over $k$ if $t \ge 1$. Theorem 2.1.5 over $k(y)$ gives local uniformization over $k(y)$ only. The step from $k(y)$ to $k$ is the second part of Lemma 1.4.2, which holds for each subfield $k' \subseteq \mathcal{O}_v$ that contains $k$ and is finitely generated over $k$. The proof of Theorem 2.2.1 needs the form over $k$, because Theorem 1.3.4 takes local uniformization of $K_0/k$ as its hypothesis. In Lean the step from $k'$ to $k$ is `Singularity.HasLocalUniformization.of_intermediateField`. The Lean proof that $v$ is an Abhyankar valuation does not use that $Kv = k(y)$. By Lemma 2.1.2 over $k(y)$, $\operatorname{rr}\Gamma_v = r$. The residues of the $y_i$ are algebraically independent over $k$, so $\operatorname{trdeg}_k Kv \ge t$. Also $\operatorname{trdeg}_k K \le r + t$, and the Abhyankar inequality gives equality.

**Example 2.1.7.** Let $K = k(x, y)$ with the monomial valuation $v(x) = 1$, $v(y) = \sqrt{2}$ of Example 1.1.7. Let $S = \{y/x, x^3/y^2\}$. The values are $\sqrt{2} - 1 \approx 0.414$ and $3 - 2\sqrt{2} \approx 0.172$, so $S \subseteq \mathcal{O}_v$. The exponent vectors $(-1, 1)$ and $(3, -2)$ have determinant $-1$, so $u_1 = y/x$ and $u_2 = x^3/y^2$ form a basis of $M$, and both have positive value. In this case the lattice lemma is not needed. We have $x = u_1^2u_2$ and $y = u_1^3u_2$. So $A = k[u_1, u_2]$ contains $k[x, y]$, the center of $v$ on $A$ is the origin, and $S \subseteq A$. The local ring $A_{(u_1, u_2)}$ is the ring $R_3$ of the quadratic sequence of Example 1.2.9, since $x_3 = u_2$ and $y_3 = u_1$. Thus for this valuation the lattice lemma replaces three quadratic transforms by one monomial change of variables. The lattice lemma works in the same way in each dimension.

### The case of rank 1

When $\Gamma_v$ has rank 1, the lattice lemma has a shorter proof that does not use Lemma 2.1.3. We give it in the dual form that the Lean library uses. A vector $\varepsilon \in \mathbb{Z}^r$ is the exponent of the Laurent monomial $x^\varepsilon$, and a vector $\gamma \in \mathbb{R}^r$ gives the value $\varepsilon \cdot \gamma = \sum_i \varepsilon_i\gamma_i$. We write $aC$ for the product of a row vector $a$ and a matrix $C$, and $C\mu$ for the product of $C$ and a column vector $\mu$.

**Lemma 2.1.8 (lattice lemma in rank 1).** Let $\gamma \in \mathbb{R}^r$ be such that $a \cdot \gamma \ne 0$ for each nonzero $a \in \mathbb{Z}^r$. Let $E \subseteq \mathbb{Z}^r$ be a finite set with $a \cdot \gamma \ge 0$ for each $a \in E$. Then there are integer matrices $B$ and $C$ with $BC = CB = 1$ such that each row $b_l$ of $B$ has $b_l \cdot \gamma > 0$ and each $a \in E$ has $aC \in \mathbb{N}^r$. Then $b_1, \dots, b_r$ is a basis of $\mathbb{Z}^r$, and each $a \in E$ is $a = \sum_l (aC)_l\, b_l$.

Node: SG0000004D · Lean: `Singularity.latticeLemma_real`

*Proof.* The last claim holds because $a = (aC)B$. If $r = 0$, there is nothing to prove, so let $r \ge 1$. For a matrix $C$ with columns $c_1, \dots, c_r$ we have $(aC)_l = a \cdot c_l$. We call an integer matrix $C$ a *good cone* if $\det C \ne 0$, if $\gamma = C\mu$ for a vector $\mu \in \mathbb{R}^r$ with $\mu_l > 0$ for each $l$, and if $a \cdot c_l \ge 0$ for each $a \in E$ and each $l$. Thus $\gamma$ is in the interior of the cone of the columns of $C$, and $E$ is in the dual cone.

Independence. Let $C$ be an integer matrix with $\det C \ne 0$, and let $\gamma = C\mu$. Then $\mu = (\det C)^{-1}\operatorname{adj}(C)\gamma$. Each row of $\operatorname{adj}(C)$ is a nonzero integer vector, because $\operatorname{adj}(C)$ is invertible over $\mathbb{Q}$. So $\mu_l \ne 0$ for each $l$, by the hypothesis on $\gamma$. For $C = 1$ this gives $\gamma_i \ne 0$ for each $i$.

Reduction to $\gamma_i > 0$. Let $\sigma_i = 1$ if $\gamma_i > 0$ and $\sigma_i = -1$ if $\gamma_i < 0$, and let $D$ be the diagonal matrix with the entries $\sigma_i$. Then $D^2 = 1$. The vector $\gamma' = D\gamma$ has positive coordinates, it has the property of the hypothesis, and $(aD) \cdot \gamma' = a \cdot \gamma$. Apply the case of positive coordinates to $\gamma'$ and $E' = \{aD : a \in E\}$, and get $B'$ and $C'$. Then $B = B'D$ and $C = DC'$ have the required properties: $BC = B'C' = 1$, $CB = DC'B'D = 1$, $b_l \cdot \gamma = b'_l \cdot \gamma' > 0$, and $aC = (aD)C'$. From now on, $\gamma_i > 0$ for each $i$.

A first good cone. Let $Q = r + 1$. Choose an integer $M > 0$ such that $M(a \cdot \gamma) \ge (Q + 1)\sum_i |a_i|$ for each nonzero $a \in E$. This is possible, because $a \cdot \gamma > 0$ for these $a$. Let $t = M\gamma$, let $R = \lfloor t \rfloor$ coordinatewise, and let $f = t - R$. Then $R_i \ge 0$ and $0 \le f_i < 1$. Let $C$ be the matrix with the columns $c_l = R + Qe_l$, where $e_l$ is the $l$-th unit vector. Then $C = Q \cdot 1 + R\,(1, \dots, 1)$, and $\det C = Q^{r-1}(Q + \sum_i R_i) > 0$. For a nonzero $a \in E$,
$$a \cdot c_l = M(a \cdot \gamma) - a \cdot f + Qa_l \ge M(a \cdot \gamma) - (Q + 1)\sum_i |a_i| \ge 0,$$
and $a \cdot c_l = 0$ for $a = 0$. Let $\Sigma = \sum_i t_i/(Q + \sum_i R_i)$ and $\mu_l = (t_l - \Sigma R_l)/Q$. Then $\sum_l \mu_l = (\sum_l t_l - \Sigma\sum_l R_l)/Q = \Sigma$, so $C\mu = \Sigma R + Q\mu = t$. Since $0 \le R_l \le t_l$ and $\sum_i f_i < r$,
$$t_l\Big(Q + \sum_i R_i\Big) - R_l\sum_i t_i = Qt_l + f_l\sum_i R_i - R_l\sum_i f_i > Qt_l - rt_l = t_l > 0.$$
So $\mu_l > 0$ for each $l$, and $\gamma = C(\mu/M)$. Thus $C$ is a good cone.

The index decreases. Let $C$ be a good cone with $|\det C| > 1$, and let $\gamma = C\mu$ with $\mu_l > 0$. If $C^{-1}$ had integer entries, then $\det C \cdot \det C^{-1} = 1$ would give $|\det C| = 1$. So some column $t = C^{-1}e_j$ of $C^{-1}$ is not in $\mathbb{Z}^r$. Let $t'$ be the vector of the fractional parts of the $t_i$. Then $0 \le t'_i < 1$, $t' \ne 0$, and $u = Ct' = e_j - C\lfloor t \rfloor$ is an integer vector. Among the indices $i$ with $t'_i > 0$, choose $l$ such that $\mu_l/t'_l$ is the smallest. Let $C'$ be the matrix $C$ with the column $c_l$ replaced by $u$. Since $u = \sum_i t'_ic_i$, we have $\det C' = t'_l\det C$, so $0 < |\det C'| < |\det C|$. For $a \in E$ we have $a \cdot u = \sum_i t'_i(a \cdot c_i) \ge 0$. Since $c_l = (u - \sum_{i \ne l} t'_ic_i)/t'_l$,
$$\gamma = \frac{\mu_l}{t'_l}\,u + \sum_{i \ne l}\Big(\mu_i - t'_i\frac{\mu_l}{t'_l}\Big)c_i.$$
The coefficient $\mu_l/t'_l$ is positive. For $i \ne l$ the coefficient is $\mu_i > 0$ if $t'_i = 0$, and $t'_i(\mu_i/t'_i - \mu_l/t'_l) \ge 0$ if $t'_i > 0$, by the choice of $l$. By the independence step, no coefficient is zero. So $C'$ is a good cone with $|\det C'| < |\det C|$.

The end. By induction on $|\det C|$, there is a good cone $C$ with $|\det C| = 1$. Then $B = C^{-1} = (\det C)\operatorname{adj}(C)$ is an integer matrix, and $BC = CB = 1$. If $\gamma = C\mu$, then $B\gamma = \mu$, so $b_l \cdot \gamma = \mu_l > 0$. Each $a \in E$ has $(aC)_l = a \cdot c_l \ge 0$. $\square$

**Proposition 2.1.9.** Let $k$ be a field of any characteristic, let $v$ be a valuation of $K/k$, and let $x_1, \dots, x_r \in K^\times$ generate $K$ as a field over $k$. Assume that $v(x^\varepsilon) \ne 0$ for each nonzero $\varepsilon \in \mathbb{Z}^r$. Assume also the conclusion of the lattice lemma for $v$: for each finite set $E \subseteq \mathbb{Z}^r$ with $v(x^a) \ge 0$ for each $a \in E$, there are integer matrices $B$ and $C$ with $BC = CB = 1$ such that the rows $b_l$ of $B$ have $v(x^{b_l}) > 0$ and each $a \in E$ has $aC \in \mathbb{N}^r$. Then $v$ has local uniformization.

Lean: `Singularity.hasLocalUniformization_of_isMonomialValuation_of_lattice`

*Proof.* First, $v$ is a monomial valuation. Let $f = \sum_\alpha c_\alpha x^\alpha$ be a polynomial in the $x_i$ with a nonzero coefficient. Two distinct monomials $x^\alpha$ and $x^\beta$ have distinct values, because $v(x^\alpha) = v(x^\beta)$ gives $v(x^{\alpha - \beta}) = 0$, so $\alpha = \beta$. So $f$ has exactly one term $c\,x^\alpha$ of least value, and $v(f) = v(x^\alpha) < \infty$. Thus $f \ne 0$ in $K$, the $x_i$ are algebraically independent over $k$, $K = k(x_1, \dots, x_r)$, and $v$ is the monomial valuation with the weights $v(x_i)$. Also $f = c\,x^\alpha(1 + F)$, where $F$ is a $k$-linear combination of Laurent monomials $x^\varepsilon$ with $v(x^\varepsilon) > 0$.

Now we follow the proof of Theorem 2.1.5. Let $S \subseteq \mathcal{O}_v$ be finite, write $s = f_s/g_s$ as there, and let $E$ be the finite set of the exponents of the Laurent monomials $x^{\alpha - \beta}$ and of the Laurent monomials in $F_s$ and $G_s$, for $s \in S$. Their values are $\ge 0$. The hypothesis gives $B$ and $C$. Let $u_l = x^{b_l}$. Then $v(u_l) > 0$. Each $a \in E$ is $\sum_l (aC)_l\,b_l$ with $(aC)_l \in \mathbb{N}$, so $x^a = \prod_l u_l^{(aC)_l}$ is a monomial in the $u_l$. The rows of $B$ are a basis of $\mathbb{Z}^r$, so $u_1, \dots, u_r$ is a basis of the group $M$ of Laurent monomials. The rest of the proof of Theorem 2.1.5 applies without change: $A = k[u_1, \dots, u_r]$ is a polynomial ring, $S$ lies in the localization $A_\mathfrak{p}$ at the center $\mathfrak{p}$ of $v$ on $A$, and the local ring of $A' = A[S]$ at the center of $v$ is $A_\mathfrak{p}$, which is regular. $\square$

The Lean proof does not use that $\mathfrak{p} = (u_1, \dots, u_r)$. It uses that $A_\mathfrak{p}$ is the localization of a polynomial ring over a field at a prime ideal, so it is a regular local ring.

**Corollary 2.1.10 (monomial case in rank 1).** Let $k$ be a field of any characteristic, and let $v$ and $x_1, \dots, x_r$ be as in the first two sentences of Proposition 2.1.9, so that $v$ is the monomial valuation of $K = k(x_1, \dots, x_r)$ with the weights $v(x_i)$. Assume that there is an injective homomorphism of ordered groups $\varphi : \Gamma_v \to \mathbb{R}$. By the theorem of Hölder [ZS2, Chapter VI], this holds if and only if $\Gamma_v$ has rank at most 1. Then $v$ has local uniformization.

Node: SG0000004D · Lean: `Singularity.hasLocalUniformization_of_isMonomialValuation_of_rankOne`

*Proof.* Let $\gamma_i = \varphi(v(x_i))$. Then $\varphi(v(x^a)) = a \cdot \gamma$ for each $a \in \mathbb{Z}^r$. Since $\varphi$ is injective and preserves the order, $v(x^a) \ge 0$ if and only if $a \cdot \gamma \ge 0$, and $v(x^a) > 0$ if and only if $a \cdot \gamma > 0$. Also $a \cdot \gamma = 0$ gives $v(x^a) = 0$, so $a = 0$. Thus Lemma 2.1.8 applies to $\gamma$, and it gives the hypothesis of Proposition 2.1.9. $\square$

In Lean the valuation is multiplicative, and $\varphi$ maps the value group to $\mathbb{R}_{\ge 0}$. The weights are $\gamma_i = -\log\varphi(v(x_i))$. The Lean statement does not say that $v$ is an Abhyankar valuation. This is part 3 of Lemma 2.1.2, which is `Singularity.IsMonomialValuation.isAbhyankarValuation`. The Lean proof of Theorem 2.1.5 for each rank, `Singularity.hasLocalUniformization_of_isMonomialValuation`, is Proposition 2.1.9 together with Lemma 2.1.4 in the form with matrices. It applies the lemma to the map $\varepsilon \mapsto v(x^\varepsilon)$ from $\mathbb{Z}^r$ to $\Gamma_v$, which is injective.

In Example 2.1.7 the elements of $S$ are themselves Laurent monomials, and their exponent vectors form a basis. In general the chart must be adapted to all the monomials in the proof of Theorem 2.1.5, and a chart that is good for one finite set can fail for a larger set. The next example carries out the proof for a quotient of two polynomials.

**Example 2.1.11.** Keep $v(x) = 1$ and $v(y) = \sqrt{2}$ on $K = k(x, y)$, and let
$$s = \frac{y^3 + x^5}{x^4 + y^4}.$$
The terms of the numerator have values $3\sqrt{2} \approx 4.243$ and $5$, and the terms of the denominator have values $4$ and $4\sqrt{2} \approx 5.657$. So the terms of least value are $y^3$ and $x^4$, and
$$s = \frac{y^3}{x^4} \cdot \frac{1 + x^5/y^3}{1 + y^4/x^4}.$$
The Laurent monomials $y^3/x^4$, $x^5/y^3$ and $y^4/x^4$ have the exponent vectors $(-4, 3)$, $(5, -3)$ and $(-4, 4)$, with the values $3\sqrt{2} - 4 \approx 0.243$, $5 - 3\sqrt{2} \approx 0.757$ and $4\sqrt{2} - 4 \approx 1.657$. So $v(s) = 3\sqrt{2} - 4 > 0$.

1. The chart of Example 2.1.7 fails. With $u_1 = y/x$ and $u_2 = x^3/y^2$ we get $y^3/x^4 = u_1/u_2$, $x^5/y^3 = u_1u_2^2$ and $y^4/x^4 = u_1^4$. So $s\,u_2(1 + u_1^4) = u_1(1 + u_1u_2^2)$. Let $A = k[u_1, u_2]$. If $s = a/b$ with $a, b \in A$ and $b \notin (u_1, u_2)$, then $u_2$ divides $u_1(1 + u_1u_2^2)\,b$ in the factorial ring $A$. It does not divide $u_1$ or $1 + u_1u_2^2$, so it divides $b$, a contradiction. Thus $s \notin A_{(u_1, u_2)}$, although $v(s) > 0$.
2. A good chart. Let $w_1 = y^3/x^4$ and $w_2 = x^3/y^2$, with exponent vectors $(-4, 3)$ and $(3, -2)$. The determinant is $8 - 9 = -1$, so $w_1, w_2$ is a basis of $M$. Both values are positive. We have
$$\frac{x^5}{y^3} = w_1w_2^3, \qquad \frac{y^4}{x^4} = w_1^4w_2^4, \qquad x = w_1^2w_2^3, \qquad y = w_1^3w_2^4.$$
Let $A = k[w_1, w_2]$. Then $k[x, y] \subseteq A$, the center of $v$ on $A$ is $\mathfrak{p} = (w_1, w_2)$, and
$$s = w_1\, \frac{1 + w_1w_2^3}{1 + w_1^4w_2^4} \in A_\mathfrak{p}.$$
Let $A' = A[s]$. By Lemma 1.1.1 the local ring of $A'$ at the center of $v$ is $A_\mathfrak{p}$, which is regular. This is local uniformization for $S = \{s\}$.
3. The good chart is one more quadratic transform. In Example 1.2.9 we have $x_3 = u_2$ and $y_3 = u_1$, with $v(x_3) = 3 - 2\sqrt{2} < \sqrt{2} - 1 = v(y_3)$. So the next transform has $x_4 = x_3 = w_2$ and $y_4 = y_3/x_3 = w_1$, and $A_\mathfrak{p} = R_4$. Theorem 1.2.6 says that $s$ lies in some $R_n$. The lattice lemma finds the right $n$ in one step: it asks for a basis of positive Laurent monomials whose exponent vectors span, over $\mathbb{N}$, the vectors $(-4, 3)$, $(5, -3)$ and $(-4, 4)$.

### Notes and references

The ring $A = k[u_1, \dots, u_r]$ is the coordinate ring of a smooth affine toric chart, and the lattice lemma says that the toric charts with a positive basis exhaust the valuation ring of a monomial valuation. Toric varieties and their resolution by regular subdivisions are in [Ful93], and in Volume 9, Section 2.4. Another combinatorial problem of resolution, the polyhedra game of Hironaka, is solved in [Spi83]. The Lean library has the one-variable step of a monomial valuation, `Singularity.monomialValuation`, which extends a valuation of $K$ to $K[X]$ with a given value of $X$. It proves Lemma 2.1.8, Proposition 2.1.9, Corollary 2.1.10, the lattice lemma (Lemma 2.1.4) by the second proof, and Theorem 2.1.5 for value groups of each rank. It proves Lemma 2.1.2 and Corollary 2.1.6. It does not have Lemma 2.1.3.
