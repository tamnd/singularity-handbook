---
title: Monomial valuations
nodes: [SG0000000Y]
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

Lean: none yet

*Proof.* The map is a surjective homomorphism onto $\bigoplus \mathbb{Z}\gamma_i$, and it is injective because the $\gamma_i$ are independent. Each polynomial has a value of the form $\alpha \cdot \gamma$, so $\Gamma_v = \bigoplus \mathbb{Z}\gamma_i$. Since distinct monomials have distinct values, the initial form of a polynomial $f$ in the sense of Volume 3, Lemma 1.6.1, is one term $c_\alpha x^\alpha$. By the residue formula there, the residue of $f/g$ with $v(f) = v(g)$ is the residue of $c_\alpha x^\alpha/(d_\alpha x^\alpha) = c_\alpha/d_\alpha \in k$. So $Kv = k$. Then $\operatorname{rr}\Gamma_v + \operatorname{trdeg}_k Kv = r = \operatorname{trdeg}_k K$. $\square$

### Cones in ordered groups

Let $\Gamma$ be an ordered abelian group of finite rational rank, and let $V = \Gamma \otimes \mathbb{Q}$. The order of $\Gamma$ extends to a unique order of $V$: for $w \in V$ choose $n \ge 1$ with $nw \in \Gamma$, and put $w > 0$ if $nw > 0$. For elements $m_1, \dots, m_s$ of $V$, the *rational cone* is the set of $\sum q_im_i$ with $q_i \in \mathbb{Q}_{\ge 0}$. A *positive basis* is a basis of $V$ over $\mathbb{Q}$ whose elements are positive.

**Lemma 2.1.3 (cone lemma).** Let $V$ be an ordered $\mathbb{Q}$-vector space of finite dimension $r$, and let $E \subseteq V$ be a finite set of elements $\ge 0$. Then there is a positive basis $m_1, \dots, m_r$ of $V$ such that $E$ lies in its rational cone.

Lean: none yet

*Proof.* We use induction on $r$. For $r = 0$ there is nothing to prove. Let $r \ge 1$.

Convex subspaces. A convex subgroup $C$ of $V$ is a $\mathbb{Q}$-subspace: if $c \in C$ and $n \ge 1$, then $c/n$ lies between $0$ and $c$, so $c/n \in C$. The convex subgroups are totally ordered by inclusion (Volume 3, Lemma 1.2.2), so there are at most $r + 1$ of them. Let $H$ be the largest proper one, and let $W = V/H$, with the induced order. The order is well defined, because $H$ is convex. A convex subgroup of $W$ has a convex preimage in $V$ that contains $H$. So $W$ has no convex subgroups other than $0$ and $W$. Then $W$ is archimedean: for $a > 0$ in $W$, the set of $w$ with $|w| \le na$ for some $n$ is a convex subgroup, and it is not 0, so it is $W$. By the theorem of Hölder [ZS2, Chapter VI, Section 10], there is an injective homomorphism of ordered groups $\psi : W \to \mathbb{R}$. It is $\mathbb{Q}$-linear, because it is additive.

The archimedean case. Let $s = \dim W \ge 1$, let $W_\mathbb{R} = W \otimes \mathbb{R} \cong \mathbb{R}^s$, and let $\psi_\mathbb{R}$ be the $\mathbb{R}$-linear extension of $\psi$. Let $E_W$ be the set of nonzero images of elements of $E$ in $W$. They are positive, so $\psi(e) > 0$ for $e \in E_W$. The points $e/\psi(e)$ lie in the affine hyperplane $\Sigma = \{\psi_\mathbb{R} = 1\}$. Choose points $p_1, \dots, p_s \in \Sigma$, affinely independent, such that each point $e/\psi(e)$ lies in the interior of their convex hull relative to $\Sigma$. This is possible because a finite set lies in the interior of a large simplex. Since $0 \notin \Sigma$, the vectors $p_i$ are linearly independent, and each $e \in E_W$ is $\sum_i \lambda_i(e)p_i$ with all $\lambda_i(e) > 0$. The coefficients of $e$ in a basis $q_1, \dots, q_s$ depend continuously on $(q_1, \dots, q_s)$ near $(p_1, \dots, p_s)$, by Cramer's rule. Since $W$ is dense in $W_\mathbb{R}$, we can choose $q_i \in W$ near $p_i$ such that the $q_i$ are a basis, $\psi(q_i) > 0$, and each $e \in E_W$ has positive coefficients in the basis $q_i$. The coefficients are rational, because $e$ and the $q_i$ lie in $W$. Since $\psi$ is an embedding of ordered groups, $q_i > 0$ in $W$.

The lift. Choose $\tilde{q}_i \in V$ with image $q_i$. An element of $V$ whose image in $W$ is positive is larger than each element of $H$, by convexity. So $\tilde{q}_i > 0$. The elements of $E \cap H$ are $\ge 0$. By induction there is a positive basis $m_1, \dots, m_h$ of $H$ such that $E \cap H$ lies in its rational cone. For $e \in E \setminus H$ write the image of $e$ as $\sum_i \lambda_i(e)q_i$ with $\lambda_i(e) \ge 0$ rational and $\sum_i \lambda_i(e) > 0$, and write
$$e - \sum_i \lambda_i(e)\tilde{q}_i = \sum_j c_j(e)m_j \in H$$
with $c_j(e) \in \mathbb{Q}$. For an integer $N \ge 0$ let $q_i^N = \tilde{q}_i - N\sum_j m_j$. Its image in $W$ is $q_i$, so $q_i^N > 0$. Then
$$e = \sum_i \lambda_i(e)q_i^N + \sum_j \Big(c_j(e) + N\sum_i \lambda_i(e)\Big)m_j.$$
For $N$ large all coefficients are $\ge 0$, for each of the finitely many $e \in E \setminus H$. So $m_1, \dots, m_h, q_1^N, \dots, q_s^N$ is the required basis. $\square$

**Lemma 2.1.4 (lattice lemma).** Let $\Gamma \cong \mathbb{Z}^r$ be an ordered group, and let $D \subseteq \Gamma$ be a finite set of elements $\ge 0$. Then there is a basis $m_1, \dots, m_r$ of $\Gamma$ over $\mathbb{Z}$ such that each $m_i$ is positive and each $d \in D$ is a combination $\sum n_im_i$ with $n_i \in \mathbb{N}$.

Lean: none yet

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

### Local uniformization of monomial valuations

**Theorem 2.1.5 (monomial case).** Let $k$ be a field of any characteristic, and let $v$ be a monomial valuation of $K = k(x_1, \dots, x_r)$. Then $v$ has local uniformization. More precisely, for each finite subset $S$ of $\mathcal{O}_v$ there are Laurent monomials $u_1, \dots, u_r$ that form a basis of the group $M$, with $v(u_i) > 0$, such that $S \subseteq A_{(u_1, \dots, u_r)}$, where $A = k[u_1, \dots, u_r]$ is a polynomial ring.

Lean: none yet

*Proof.* Let $S \subseteq \mathcal{O}_v$ be finite. Write each $s \in S$ as $s = f_s/g_s$ with polynomials $f_s, g_s \ne 0$. Write $f_s = c\,x^\alpha(1 + F_s)$, where $c\,x^\alpha$ is the term of least value and $F_s$ is a sum of terms $c'x^\varepsilon$ with $v(x^\varepsilon) > 0$. Write $g_s = d\,x^\beta(1 + G_s)$ in the same way. Then
$$s = \frac{c}{d}\, x^{\alpha - \beta}\, \frac{1 + F_s}{1 + G_s}, \qquad v(x^{\alpha - \beta}) = v(s) \ge 0.$$
Let $D \subseteq \Gamma_v$ be the finite set of the values of $x^{\alpha - \beta}$ and of the Laurent monomials that occur in the $F_s$ and $G_s$, for $s \in S$. Its elements are $\ge 0$. By Lemma 2.1.4 there is a basis $m_1, \dots, m_r$ of $\Gamma_v$ of positive elements whose $\mathbb{N}$-span contains $D$. By Lemma 2.1.2, $m_i = v(u_i)$ for a basis $u_1, \dots, u_r$ of $M$, and each Laurent monomial whose value is in $D$ is a monomial in $u_1, \dots, u_r$ with exponents in $\mathbb{N}$.

Since $u_1, \dots, u_r$ is a basis of $M$, the $k$-algebra $k[M]$ of Laurent polynomials is $k[u_1^{\pm 1}, \dots, u_r^{\pm 1}]$. So the $u_i$ are algebraically independent over $k$, $K = k(u_1, \dots, u_r)$, and $v$ is the monomial valuation of $k(u_1, \dots, u_r)$ with weights $m_1, \dots, m_r$. Let $A = k[u_1, \dots, u_r]$. It is an affine model of $K/k$, and $A \subseteq \mathcal{O}_v$. Since the $m_i$ are positive, the center of $v$ on $A$ is $\mathfrak{p} = (u_1, \dots, u_r)$ (Volume 3, Lemma 1.6.1). The ring $A_\mathfrak{p}$ is regular of dimension $r$. The elements $x^{\alpha - \beta}$, $F_s$ and $G_s$ lie in $A$, and $F_s, G_s \in \mathfrak{p}$. So $1 + G_s \in A \setminus \mathfrak{p}$, and $s \in A_\mathfrak{p}$.

Let $A' = A[S]$. Then $S \subseteq A' \subseteq A_\mathfrak{p} \subseteq \mathcal{O}_v$, and $A'$ is an affine model of $K/k$. By Lemma 1.1.1, the local ring of $A'$ at the center of $v$ is $A_\mathfrak{p}$, which is regular. Proposition 4.1.6 of Volume 3 ends the proof. $\square$

**Corollary 2.1.6.** Let $k$ be a field of any characteristic, let $K = k(y_1, \dots, y_t, x_1, \dots, x_r)$ be a field of rational functions, and let $v$ be a valuation of $K/k$ that is trivial on $k(y_1, \dots, y_t)$ and is a monomial valuation of $K = k(y)(x_1, \dots, x_r)$ over the field $k(y)$. Then $v$ has local uniformization, and $v$ is an Abhyankar valuation of $K/k$ with residue field $k(y_1, \dots, y_t)$.

Lean: none yet

*Proof.* By Lemma 2.1.2 over the field $k(y)$, the residue field is $k(y)$ and $\Gamma_v \cong \mathbb{Z}^r$. So $\operatorname{rr}\Gamma_v + \operatorname{trdeg}_k Kv = r + t$. The residues of $y_1, \dots, y_t$ are $y_1, \dots, y_t$, which are algebraically independent over $k$. By Theorem 2.1.5 over $k(y)$ and Lemma 1.4.2, $v$ has local uniformization over $k$. $\square$

**Example 2.1.7.** Let $K = k(x, y)$ with the monomial valuation $v(x) = 1$, $v(y) = \sqrt{2}$ of Example 1.1.7. Let $S = \{y/x, x^3/y^2\}$. The values are $\sqrt{2} - 1 \approx 0.414$ and $3 - 2\sqrt{2} \approx 0.172$, so $S \subseteq \mathcal{O}_v$. The exponent vectors $(-1, 1)$ and $(3, -2)$ have determinant $-1$, so $u_1 = y/x$ and $u_2 = x^3/y^2$ form a basis of $M$, and both have positive value. In this case the lattice lemma is not needed. We have $x = u_1^2u_2$ and $y = u_1^3u_2$. So $A = k[u_1, u_2]$ contains $k[x, y]$, the center of $v$ on $A$ is the origin, and $S \subseteq A$. The local ring $A_{(u_1, u_2)}$ is the ring $R_3$ of the quadratic sequence of Example 1.2.9, since $x_3 = u_2$ and $y_3 = u_1$. Thus for this valuation the lattice lemma replaces three quadratic transforms by one monomial change of variables. The lattice lemma works in the same way in each dimension.

### Notes and references

The ring $A = k[u_1, \dots, u_r]$ is the coordinate ring of a smooth affine toric chart, and the lattice lemma says that the toric charts with a positive basis exhaust the valuation ring of a monomial valuation. Toric varieties and their resolution by regular subdivisions are in [Ful93], and in Volume 9, Section 2.4. Another combinatorial problem of resolution, the polyhedra game of Hironaka, is solved in [Spi83]. The Lean library has the one-variable step of a monomial valuation, `Singularity.monomialValuation`, which extends a valuation of $K$ to $K[X]$ with a given value of $X$. It does not have Lemmas 2.1.3 and 2.1.4 or Theorem 2.1.5.
