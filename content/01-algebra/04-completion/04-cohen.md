---
title: The Cohen structure theorem
nodes: [SG0000000P]
sources: [Coh46, Mat, Eis95, AM69]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Cohen structure theorem

Let $(R, \mathfrak{m}, \kappa)$ be a complete Noetherian local ring. The ring $k[[x_1, \dots, x_n]]$ of formal power series over a field is the simplest example. The theorem of Cohen says that, when $R$ contains a field, every such ring is a quotient of a ring of power series over $\kappa$, and a regular one is a ring of power series over $\kappa$. The key step is to find a field inside $R$ that maps onto $\kappa$. This section proves the existence of such a field in two cases: when $\kappa$ has characteristic $0$, and when $\kappa$ is perfect. It states the general case and the case of mixed characteristic with references.

### Coefficient fields

**Definition 4.4.1.** Let $(R, \mathfrak{m}, \kappa)$ be a local ring. A *coefficient field* of $R$ is a subring $K \subseteq R$ that is a field and that the projection $R \to \kappa$ maps onto $\kappa$. Then $K \to \kappa$ is an isomorphism, and $R = K + \mathfrak{m}$ as groups.

The map $K \to \kappa$ is injective because a field has no ideals other than $0$ and itself. A local ring $R$ is *equicharacteristic* if $\operatorname{char} R = \operatorname{char} \kappa$. Otherwise it has *mixed characteristic*. Then $\operatorname{char} \kappa = p > 0$ and $\operatorname{char} R$ is $0$ or a power $p^k$ with $k \ge 2$.

**Lemma 4.4.2.** A local ring $(R, \mathfrak{m}, \kappa)$ contains a field if and only if it is equicharacteristic.

Lean: `Singularity.Algebra.exists_isField_subring_iff_ringChar_eq`

*Proof.* If $R$ contains a field $k$, then $k \to \kappa$ is injective, so $\operatorname{char} R = \operatorname{char} k = \operatorname{char} \kappa$. Conversely, assume that $\operatorname{char} R = \operatorname{char} \kappa$. If this characteristic is a prime $p$, then $R$ contains the field $\mathbb{F}_p$. If it is $0$, then each nonzero integer $n$ has a nonzero image in $\kappa$. So $n \notin \mathfrak{m}$, and $n$ is a unit of $R$. Thus $R$ contains $\mathbb{Q}$. $\square$

A coefficient field is a field in $R$, so a local ring with a coefficient field is equicharacteristic. For a complete Noetherian local ring the converse is true (Theorem 4.4.4). The proof uses the lemma of Hensel.

**Lemma 4.4.3 (Hensel).** Let $(R, \mathfrak{m})$ be a complete Noetherian local ring, let $g \in R[T]$ and let $a_0 \in R$. Assume that $g(a_0) \in \mathfrak{m}$ and that $g'(a_0)$ is a unit. Then there is exactly one $a \in R$ with $g(a) = 0$ and $a - a_0 \in \mathfrak{m}$.

Lean: `Singularity.Algebra.existsUnique_root_of_isAdicComplete`

*Proof.* For $b, h \in R$ the Taylor formula gives $g(b + h) = g(b) + g'(b) h + h^2 c$ for some $c \in R$. We define $a_{k+1} = a_k - g(a_k)/g'(a_k)$, and we prove by induction that $a_k - a_0 \in \mathfrak{m}$ and $g(a_k) \in \mathfrak{m}^{2^k}$. This is true for $k = 0$. Assume it for $k$. Then $g'(a_k) \equiv g'(a_0)$ modulo $\mathfrak{m}$, so $g'(a_k)$ is a unit and $a_{k+1}$ is defined. Let $h = -g(a_k)/g'(a_k)$. Then $h \in \mathfrak{m}^{2^k}$, so $a_{k+1} - a_0 \in \mathfrak{m}$, and the Taylor formula gives $g(a_{k+1}) = h^2 c \in \mathfrak{m}^{2^{k+1}}$.

Since $a_{k+1} - a_k \in \mathfrak{m}^{2^k}$, the class of $a_k$ in $R/\mathfrak{m}^n$ is constant for $2^k \ge n$. These classes are compatible, so they define an element $a$ of $\hat{R} = R$, and $a - a_k \in \mathfrak{m}^{2^k}$ for each $k$. Then $a - a_0 \in \mathfrak{m}$ and $g(a) \equiv g(a_k)$ modulo $\mathfrak{m}^{2^k}$, so $g(a) \in \bigcap_n \mathfrak{m}^n = 0$ by Corollary 4.1.8. For the uniqueness, let $b$ be another root with $b - a_0 \in \mathfrak{m}$. The Taylor formula gives $0 = g(b) - g(a) = (b - a)(g'(a) + (b - a) c)$ for some $c \in R$. The second factor is a unit, because $g'(a)$ is a unit and $b - a \in \mathfrak{m}$. Thus $b = a$. $\square$

**Theorem 4.4.4 (Cohen).** Let $(R, \mathfrak{m}, \kappa)$ be a complete Noetherian local ring that contains a field. Then $R$ has a coefficient field. If $\operatorname{char} \kappa = p > 0$ and $\kappa$ is perfect, then the coefficient field is unique.

Lean: none yet

*Proof.* We give the proof in two cases: when $\operatorname{char} \kappa = 0$, and when $\kappa$ is perfect. For the general case we refer to [Coh46] and [Mat, Section 28].

First let $\operatorname{char} \kappa = 0$. By Lemma 4.4.2, $\mathbb{Q} \subseteq R$. The subfields of $R$ that contain $\mathbb{Q}$, ordered by inclusion, satisfy the hypothesis of the lemma of Zorn, because the union of a chain of subfields is a subfield. Let $K$ be a maximal subfield, and let $\bar{K} \subseteq \kappa$ be its image. We claim that $\bar{K} = \kappa$. Assume that there is $\bar{\alpha} \in \kappa \setminus \bar{K}$.

If $\bar{\alpha}$ is transcendental over $\bar{K}$, let $\alpha \in R$ be any lift of $\bar{\alpha}$. For each nonzero $h \in K[T]$, the image of $h(\alpha)$ in $\kappa$ is $\bar{h}(\bar{\alpha}) \ne 0$, so $h(\alpha)$ is a unit of $R$. Thus $K[\alpha] \cong K[T]$, and the field of fractions $K(\alpha)$ is a subfield of $R$. It is larger than $K$, and this contradicts the maximality of $K$.

If $\bar{\alpha}$ is algebraic over $\bar{K}$, let $g \in K[T]$ be the monic polynomial whose image $\bar{g}$ is the minimal polynomial of $\bar{\alpha}$ over $\bar{K}$. Then $g$ is irreducible over $K$. Since $\operatorname{char} \kappa = 0$, the polynomial $\bar{g}$ is separable, so $\bar{g}'(\bar{\alpha}) \ne 0$. Let $\alpha_0$ be a lift of $\bar{\alpha}$. Then $g(\alpha_0) \in \mathfrak{m}$ and $g'(\alpha_0)$ is a unit. By Lemma 4.4.3 there is $\alpha \in R$ with $g(\alpha) = 0$. The ring $K[\alpha]$ is a quotient of the field $K[T]/(g)$, so it is a field. It is larger than $K$, because $\alpha$ maps to $\bar{\alpha} \notin \bar{K}$. This again contradicts the maximality of $K$. Thus $K$ is a coefficient field.

Now let $\operatorname{char} \kappa = p > 0$ with $\kappa$ perfect. Then $\operatorname{char} R = p$, so $(a + b)^{p^n} = a^{p^n} + b^{p^n}$ in $R$. In particular, if $a - b \in \mathfrak{m}$, then $a^{p^n} - b^{p^n} = (a - b)^{p^n} \in \mathfrak{m}^{p^n}$. Let $\bar{x} \in \kappa$. Since $\kappa$ is perfect, $\bar{x}$ has a unique $p^n$-th root $\bar{x}^{1/p^n}$ for each $n$. Choose $y_n \in R$ that lifts $\bar{x}^{1/p^n}$, and let $z_n = y_n^{p^n}$. The elements $y_{n+1}^p$ and $y_n$ both lift $\bar{x}^{1/p^n}$, so
$$z_{n+1} - z_n = (y_{n+1}^p)^{p^n} - y_n^{p^n} = (y_{n+1}^p - y_n)^{p^n} \in \mathfrak{m}^{p^n}.$$
As in the proof of Lemma 4.4.3, the sequence $(z_n)$ defines an element $\tau(\bar{x}) \in R$ with $\tau(\bar{x}) - z_n \in \mathfrak{m}^{p^n}$ for each $n$. It does not depend on the choice of the $y_n$: for other lifts $y'_n$, we have $y_n^{p^n} - y_n'^{p^n} = (y_n - y'_n)^{p^n} \in \mathfrak{m}^{p^n}$. The element $\tau(\bar{x})$ lifts $\bar{x}$, because each $z_n$ lifts $\bar{x}$.

The map $\tau : \kappa \to R$ is a ring homomorphism. Let $\bar{x}, \bar{x}' \in \kappa$ with lifts $y_n, y'_n$ of their $p^n$-th roots. Then $y_n y'_n$ lifts $(\bar{x}\bar{x}')^{1/p^n}$, and $y_n + y'_n$ lifts $\bar{x}^{1/p^n} + \bar{x}'^{1/p^n} = (\bar{x} + \bar{x}')^{1/p^n}$. Also $(y_n y'_n)^{p^n} = z_n z'_n$ and $(y_n + y'_n)^{p^n} = z_n + z'_n$. Thus $\tau(\bar{x}\bar{x}') \equiv \tau(\bar{x})\tau(\bar{x}')$ and $\tau(\bar{x} + \bar{x}') \equiv \tau(\bar{x}) + \tau(\bar{x}')$ modulo $\mathfrak{m}^{p^n}$ for each $n$, and Corollary 4.1.8 gives equality. Clearly $\tau(1) = 1$. So the image of $\tau$ is a coefficient field.

For the uniqueness, let $K$ be any coefficient field. It is isomorphic to $\kappa$, so it is perfect. For $x \in K$ with image $\bar{x}$, the element $x^{1/p^n}$ of $K$ lifts $\bar{x}^{1/p^n}$. With $y_n = x^{1/p^n}$ we get $z_n = x$ for each $n$, so $\tau(\bar{x}) = x$. Thus $K = \tau(\kappa)$. $\square$

The element $\tau(\bar{x})$ is the *Teichmüller lift* of $\bar{x}$. A coefficient field need not be unique when $\kappa$ is not perfect. It also need not be unique in characteristic $0$, where each field is perfect. Example 4.4.5 shows both cases: take $F$ of characteristic $p$ for the first case, and $F = \mathbb{Q}$ for the second case.

**Example 4.4.5.** Let $F$ be a field, let $k = F(s)$ be the field of rational functions in one variable $s$ and let $R = k[[t]]$. The field $k$ is a coefficient field of $R$. The element $s + t$ of $R$ is transcendental over $F$: for each nonzero $h \in F[T]$, the constant term of $h(s + t)$ is $h(s) \ne 0$, so $h(s + t)$ is a unit of $R$. Thus $F(s + t)$ is a subfield of $R$. It maps onto $F(s) = \kappa$, because $s + t$ maps to $s$. So $F(s + t)$ is another coefficient field. It is not $k$, because $s + t \notin k$.

### The structure theorem

**Theorem 4.4.6.** Let $(R, \mathfrak{m}, \kappa)$ be a complete Noetherian local ring with a coefficient field $K$, and let $x_1, \dots, x_n \in \mathfrak{m}$. Then there is a homomorphism of $K$-algebras $\varphi : K[[X_1, \dots, X_n]] \to R$ with $\varphi(X_i) = x_i$ and $\varphi((X_1, \dots, X_n)^j) \subseteq \mathfrak{m}^j$ for each $j$. If $x_1, \dots, x_n$ generate $\mathfrak{m}$, then $\varphi$ is surjective.

Lean: none yet

*Proof.* Let $S = K[X_1, \dots, X_n]$ and $J = (X_1, \dots, X_n)$. The map of $K$-algebras $S \to R$ with $X_i \mapsto x_i$ maps $J^j$ into $\mathfrak{m}^j$. So it gives compatible maps $S/J^j \to R/\mathfrak{m}^j$, and a map of the inverse limits. By Example 4.2.2 the first limit is $K[[X_1, \dots, X_n]]$, and the second is $\hat{R} = R$. This is $\varphi$.

Assume that $x_1, \dots, x_n$ generate $\mathfrak{m}$, and let $a \in R$. The ideal $\mathfrak{m}^j$ is generated by the monomials $x^\alpha$ with $|\alpha| = j$. Since $R = K + \mathfrak{m}$, we get $x^\alpha R \subseteq x^\alpha K + \mathfrak{m}^{j+1}$, so
$$\mathfrak{m}^j = \sum_{|\alpha| = j} K x^\alpha + \mathfrak{m}^{j+1}.$$
By induction on $j$, we find homogeneous polynomials $h_j \in S$ of degree $j$ such that $a - \varphi(h_0 + \dots + h_j) \in \mathfrak{m}^{j+1}$. For $j = 0$ this is $R = K + \mathfrak{m}$. If it holds for $j$, the formula above for $\mathfrak{m}^{j+1}$ gives $h_{j+1}$. Let $f = \sum_j h_j \in K[[X_1, \dots, X_n]]$. Then $f - (h_0 + \dots + h_j) \in J^{j+1} K[[X_1, \dots, X_n]]$, so $a - \varphi(f) \in \mathfrak{m}^{j+1}$ for each $j$. By Corollary 4.1.8, $\varphi(f) = a$. $\square$

**Theorem 4.4.7 (Cohen structure theorem).** Let $(R, \mathfrak{m}, \kappa)$ be a complete regular local ring of dimension $n$ that contains a field. Then $R \cong \kappa[[X_1, \dots, X_n]]$.

Node: SG0000000P · Lean: `Singularity.cohen_structure` (planned, no Lean statement yet)

*Proof.* By Theorem 4.4.4, $R$ has a coefficient field $K \cong \kappa$. Since $R$ is regular, $\mathfrak{m}$ is generated by $n$ elements $x_1, \dots, x_n$. By Theorem 4.4.6 there is a surjection $\varphi : S = K[[X_1, \dots, X_n]] \to R$. By Corollary 4.3.4, $S$ is a regular local ring of dimension $n$ and a domain. Let $P = \ker \varphi$, and assume $P \ne 0$. Each chain of prime ideals of $S$ that contain $P$ can be extended by the prime ideal $0 \subsetneq P$. So $\dim S/P \le \dim S - 1 = n - 1$. This contradicts $\dim R = n$. Thus $P = 0$ and $R \cong K[[X_1, \dots, X_n]] \cong \kappa[[X_1, \dots, X_n]]$. $\square$

The proof is complete when $\operatorname{char} \kappa = 0$ or $\kappa$ is perfect. In general it uses Theorem 4.4.4 in the form of [Coh46]. For resolution in characteristic $0$, the first case is the important one.

**Corollary 4.4.8.** Let $(R, \mathfrak{m}, \kappa)$ be a complete Noetherian local ring that contains a field, and let $e = \operatorname{edim} R$. Then $R$ is a quotient of $\kappa[[X_1, \dots, X_e]]$. In particular, $R$ is a quotient of a complete regular local ring.

Lean: none yet

*Proof.* Take a coefficient field by Theorem 4.4.4 and $e$ generators of $\mathfrak{m}$ by Lemma 1.1.1, and apply Theorem 4.4.6. The ring $\kappa[[X_1, \dots, X_e]]$ is complete and regular by Example 4.2.2 and Corollary 4.3.4. $\square$

### Mixed characteristic

In mixed characteristic a field in $R$ does not exist, by Lemma 4.4.2. The role of the field is taken by a complete discrete valuation ring whose maximal ideal is generated by $p$. Such a ring $C$ with residue field $\kappa$ is a *Cohen ring* for $\kappa$. For $\kappa = \mathbb{F}_p$ it is $\mathbb{Z}_p$.

**Theorem 4.4.9 (Cohen).** Let $\kappa$ be a field of characteristic $p > 0$.

1. There is a Cohen ring $C$ for $\kappa$, and it is unique up to isomorphism.
2. Let $(R, \mathfrak{m}, \kappa)$ be a complete Noetherian local ring with residue field $\kappa$. Then there is a local homomorphism $C \to R$ that induces the identity of $\kappa$. Thus $R$ is a quotient of $C[[X_1, \dots, X_n]]$ for some $n$.
3. Let $R$ be as in 2, and assume that $R$ is regular of dimension $d$ and has mixed characteristic. If $p \notin \mathfrak{m}^2$, then $R \cong C[[X_1, \dots, X_{d-1}]]$. If $p \in \mathfrak{m}^2$, then $R \cong C[[X_1, \dots, X_d]]/(p - g)$ for some $g$ in the square of the maximal ideal of $C[[X_1, \dots, X_d]]$.

Lean: none yet

We do not prove Theorem 4.4.9. Part 3 follows from part 2 by the arguments of Theorem 4.4.6 and Theorem 4.4.7. For example, let $p \in \mathfrak{m}^2$, and let $x_1, \dots, x_d$ generate $\mathfrak{m}$. Then the map $\varphi : S = C[[X_1, \dots, X_d]] \to R$ with $X_i \mapsto x_i$ is surjective. The ring $S$ is regular of dimension $d + 1$, and $p, X_1, \dots, X_d$ generate its maximal ideal $\mathfrak{m}_S$. Since $p \in \mathfrak{m}^2$ and $\varphi(\mathfrak{m}_S^2) = \mathfrak{m}^2$, there is $g \in \mathfrak{m}_S^2$ with $\varphi(g) = p$. Then $p - g \in \ker \varphi$ and $p - g \notin \mathfrak{m}_S^2$. By Proposition 1.2.6, $S/(p - g)$ is regular of dimension $d$, so it is a domain by Theorem 1.3.3. It maps onto $R$, which also has dimension $d$. The argument of Theorem 4.4.7 shows that this map is injective. A ring of the form in part 3 with $p \in \mathfrak{m}^2$ is *ramified*, and the other case is *unramified*.

### Notes and references

The structure theorem is due to Cohen [Coh46], who proved the existence of coefficient fields, of Cohen rings and of coefficient rings in all cases. Matsumura proves the existence of coefficient fields with formal smoothness, and treats the structure theorems in [Mat, Sections 28 and 29]. Lemma 4.4.3 is one form of the lemma of Hensel; see [Eis95, Chapter 7] for other forms and the proof by Newton's method. The construction of the Teichmüller lift for a perfect residue field is the classical one. When $\kappa$ is not perfect, one proof of Theorem 4.4.4 in characteristic $p$ chooses a $p$-basis of $\kappa$ (Section 6.2) and lifts it; the choice of the lifts is the source of the non-uniqueness. In Example 4.4.5 the two coefficient fields come from two lifts of the transcendental element $s$.
