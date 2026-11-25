---
title: Generic regularity
nodes: [SG0000002R, SG0000002S, SG0000002T, SG0000002V, SG00000035, SG00000036, SG0000000K]
sources: [Mat, AM69, Nag62, EGA4-7, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Generic regularity

Section 1.7 reduced the openness of the regular locus of a variety to one property: each domain $D$ of finite type over the field $k$ must have a nonempty open set of regular points. In this section we prove this property when $k$ has characteristic $0$, and then when $k$ is perfect. The method is classical. We write $D$, up to a localization, as a hypersurface $A[X]/(F)$ over a polynomial ring $A$, and then we use the Jacobian criterion for a hypersurface. As a corollary, the regular locus of an algebra of finite type over a field of characteristic $0$ is open (Theorem 1.8.10). The same method works over a perfect field, with a separating transcendence basis in place of the normalization lemma (Theorems 1.8.16 and 1.8.17).

A ring $A$ is *regular* when it is Noetherian and $A_\mathfrak{p}$ is a regular local ring for each prime $\mathfrak{p}$ of $A$. By Corollary 1.6.9, it is sufficient to examine the maximal ideals. A *derivation* of $A$ is an additive map $\partial : A \to A$ with $\partial(ab) = a \, \partial b + b \, \partial a$ for all $a, b \in A$.

### The Jacobian criterion for a hypersurface

**Lemma 1.8.1.** Let $\partial$ be a derivation of $A$ and let $I$ be an ideal of $A$. If $x \in I^2$, then $\partial x \in I$.

Lean: `Singularity.Algebra.derivation_mem_of_mem_sq`

*Proof.* The ideal $I^2$ is generated as an additive group by the products $ab$ with $a \in I$ and $b \in I$, and their multiples by elements of $A$. For $a, b \in I$ and $r \in A$ we have $\partial(rab) = ra \, \partial b + rb \, \partial a + ab \, \partial r$, and each term is in $I$. Since $\partial$ is additive, the claim follows. $\square$

**Proposition 1.8.2.** Let $A$ be a Noetherian ring, let $\mathfrak{q}$ be a prime ideal of $A$ such that $A_\mathfrak{q}$ is regular, and let $F \in \mathfrak{q}$. Let $\partial$ be a derivation of $A$ with $\partial F \notin \mathfrak{q}$. Then $A_\mathfrak{q}/F A_\mathfrak{q}$ is a regular local ring.

Lean: `Singularity.Algebra.isRegularLocalRing_quotient_of_derivation`

*Proof.* Let $\mathfrak{m} = \mathfrak{q} A_\mathfrak{q}$. By Proposition 1.2.6, it is sufficient to show that $F/1 \notin \mathfrak{m}^2$. Assume that $F/1 \in \mathfrak{m}^2 = \mathfrak{q}^2 A_\mathfrak{q}$. Then there is $s \notin \mathfrak{q}$ with $sF \in \mathfrak{q}^2$. By Lemma 1.8.1, $\partial(sF) = s \, \partial F + F \, \partial s$ is in $\mathfrak{q}$. Since $F \in \mathfrak{q}$, we get $s \, \partial F \in \mathfrak{q}$. This is a contradiction, because $s \notin \mathfrak{q}$, $\partial F \notin \mathfrak{q}$ and $\mathfrak{q}$ is prime. $\square$

**Corollary 1.8.3.** Let $A$ be a regular ring, let $F \in A$ and let $\partial$ be a derivation of $A$. Then the open set $D(\overline{\partial F})$ of $\operatorname{Spec} A/(F)$ is in $\operatorname{Reg}(A/(F))$.

Node: SG0000002R · Lean: `Singularity.Algebra.regularLocus_quotient_of_derivation`

*Proof.* A prime of $A/(F)$ has the form $\mathfrak{q}/(F)$ for a prime $\mathfrak{q} \supseteq (F)$ of $A$. If $\overline{\partial F} \notin \mathfrak{q}/(F)$, then $\partial F \notin \mathfrak{q}$. The proof of Lemma 1.7.6 does not use that $\mathfrak{p}$ is prime, so it gives $(A/(F))_{\mathfrak{q}/(F)} \cong A_\mathfrak{q}/F A_\mathfrak{q}$. This ring is regular by Proposition 1.8.2. $\square$

We use Corollary 1.8.3 in one case. Let $B$ be a regular ring and let $F \in B[X]$. The ring $B[X]$ is regular [Mat, Section 19], and $\partial = d/dX$ is a derivation of $B[X]$. Thus $D(\overline{F'})$ is in $\operatorname{Reg}(B[X]/(F))$, where $F'$ is the derivative of $F$. In Lean this is `Singularity.Algebra.regularLocus_adjoinRoot`.

### A conductor

**Lemma 1.8.4.** Let $R \subseteq S$ be rings and let $c \in R$ with $cS \subseteq R$. Let $P$ be a prime of $S$ with $c \notin P$, and let $\mathfrak{p} = P \cap R$. Then the natural map $R_\mathfrak{p} \to S_P$ is an isomorphism. In particular, if $\mathfrak{p} \in \operatorname{Reg}(R)$, then $P \in \operatorname{Reg}(S)$.

Lean: `Singularity.Algebra.isLocalization_atPrime_of_conductor`, `Singularity.Algebra.mem_regularLocus_of_conductor`

*Proof.* An element of $R \setminus \mathfrak{p}$ is not in $P$, so its image in $S_P$ is a unit. Thus the map exists. Let $s/t \in S_P$ with $t \notin P$. Then $cs$ and $ct$ are in $R$, and $ct \notin P$ because $P$ is prime. Thus $ct \notin \mathfrak{p}$, and $s/t = cs/ct$ is in the image. Let $r/u \in R_\mathfrak{p}$ map to $0$. Then $vr = 0$ in $S$ for some $v \notin P$. The element $cv$ is in $R \setminus \mathfrak{p}$, and $(cv) r = 0$. Thus $r/u = 0$ in $R_\mathfrak{p}$. $\square$

In the rest of the section, $A \subseteq D$ is an extension of domains, $D$ is a finite $A$-module and $A$ is integrally closed. We write $L$ for the fraction field of $A$ and $K$ for the fraction field of $D$. The extension $K/L$ is finite, because a set of generators of $D$ over $A$ spans $K$ over $L$.

**Lemma 1.8.5.** Assume that $K/L$ is separable. Then there is $z \in D$ with $K = L(z)$.

Lean: a step in the proof of `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus`

*Proof.* By the theorem of the primitive element, $K = L(\alpha)$ for some $\alpha \in K$. Write $\alpha = y/t$ with $y, t \in D$ and $t \neq 0$. The element $t$ is integral over $A$. Take an equation $t^m + a_{m-1} t^{m-1} + \dots + a_0 = 0$ with $a_i \in A$ and $m$ as small as possible. Then $a_0 \neq 0$, because $D$ is a domain and $m$ is minimal. Thus $a = a_0$ is a nonzero element of $A$ of the form $a = ut$ with $u \in D$. Let $z = uy$. Then $z = a\alpha$, and $a$ is a nonzero element of $L$, so $L(z) = L(\alpha) = K$. $\square$

**Lemma 1.8.6.** Let $z \in D$ with $K = L(z)$. Then there is $c \neq 0$ in $A$ with $cD \subseteq A[z]$.

Lean: `Singularity.Algebra.exists_conductor`

*Proof.* Let $d \in D$. Since $z$ is algebraic over $L$, we have $L(z) = L[z]$. Thus $d = p(z)$ for a polynomial $p \in L[X]$. Take $b \neq 0$ in $A$ such that $bp$ has coefficients in $A$. Then $bd = (bp)(z)$ is in $A[z]$. Let $d_1, \dots, d_n$ generate $D$ as an $A$-module, and take $b_i \neq 0$ with $b_i d_i \in A[z]$. Let $c = b_1 \cdots b_n$. Then $c \neq 0$ and $c d_i \in A[z]$ for each $i$. Since $A[z]$ is an $A$-module, $cD \subseteq A[z]$. $\square$

**Lemma 1.8.7.** Let $z \in D$ with $K = L(z)$, and let $F$ be the minimal polynomial of $z$ over $L$. Then $F$ has coefficients in $A$, and $A[X]/(F) \cong A[z]$ by $X \mapsto z$. If $K/L$ is separable, then $F'(z) \neq 0$.

Lean: a step in the proof of `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus`

*Proof.* Since $A$ is integrally closed and $z$ is integral over $A$, the polynomial $F$ has coefficients in $A$ [AM69, Proposition 5.15]. The map $A[X] \to A[z]$ is surjective. Let $g \in A[X]$ with $g(z) = 0$. Since $F$ is monic, we can divide in $A[X]$: $g = qF + r$ with $\deg r < \deg F$. Then $r(z) = 0$, and $r = 0$ by the minimality of $F$ over $L$. Thus the kernel is $(F)$. If $K/L$ is separable, then $F$ is separable, so $F$ and $F'$ have no common root and $F'(z) \neq 0$. $\square$

### Generic regularity

**Theorem 1.8.8.** Let $A \subseteq D$ be as above. Assume that $A$ is a regular ring and that $L$ has characteristic $0$. Then there is $f \neq 0$ in $D$ with $D(f) \subseteq \operatorname{Reg}(D)$.

Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus`

*Proof.* Since $L$ has characteristic $0$, the extension $K/L$ is separable. Take $z$ as in Lemma 1.8.5, $c$ as in Lemma 1.8.6 and $F$ as in Lemma 1.8.7. Let $f = c F'(z)$. Then $f \neq 0$, because $D$ is a domain.

Let $P$ be a prime of $D$ with $f \notin P$. Then $c \notin P$ and $F'(z) \notin P$. By Lemma 1.8.4 with $R = A[z]$ and $S = D$, it is sufficient to show that $P \cap A[z]$ is in $\operatorname{Reg}(A[z])$. Under the isomorphism $A[z] \cong A[X]/(F)$ of Lemma 1.8.7, the prime $P \cap A[z]$ does not contain the image of $F'$. By Corollary 1.8.3, applied to the regular ring $A[X]$ and the derivation $d/dX$, this prime is in the regular locus. $\square$

**Theorem 1.8.9.** Let $k$ be a field of characteristic $0$ and let $D$ be a domain of finite type over $k$. Then there is $f \neq 0$ in $D$ with $D(f) \subseteq \operatorname{Reg}(D)$.

Node: SG0000002S · Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus_of_field`

*Proof.* By the normalization lemma of Noether [AM69, Chapter 5, Exercise 16], there are elements $x_1, \dots, x_s$ of $D$ that are algebraically independent over $k$ such that $D$ is a finite module over $A = k[x_1, \dots, x_s]$. The ring $A$ is a polynomial ring over a field. Thus it is regular [Mat, Section 19], and it is integrally closed, because it is a unique factorization domain. Its fraction field contains $k$, so it has characteristic $0$. Theorem 1.8.8 completes the proof. $\square$

**Theorem 1.8.10.** Let $k$ be a field of characteristic $0$ and let $R$ be an algebra of finite type over $k$. Then $\operatorname{Reg}(R)$ is open in $\operatorname{Spec} R$.

Node: SG0000002T · Lean: `Singularity.Algebra.isOpen_regularLocus_of_charZero`

*Proof.* The ring $R$ is Noetherian by the basis theorem of Hilbert. Let $\mathfrak{p}$ be a prime of $R$. Then $R/\mathfrak{p}$ is a domain of finite type over $k$. By Theorem 1.8.9, there is $f \neq 0$ in $R/\mathfrak{p}$ with $D(f) \subseteq \operatorname{Reg}(R/\mathfrak{p})$. The set $D(f)$ is open, and it contains the zero ideal because $f \neq 0$. Thus Theorem 1.7.7 applies. $\square$

**Example 1.8.11.** We use the method on the cuspidal cubic $D = k[x, y]/(y^2 - x^3)$ of Example 1.7.8, with $k$ of characteristic $0$. Let $A = k[x]$. Then $D = A[y]$, so we can take $z = y$ and $c = 1$. The minimal polynomial of $y$ is $F = Y^2 - x^3$, and $F'(y) = 2y$. Thus $f = 2y$. Since $2$ is a unit, $D(f) = D(y)$. A prime contains $y$ if and only if it contains $x$, because $y^2 = x^3$. Thus $D(f) = D(x)$, and this is the full regular locus, by Example 1.7.8. If $k$ has characteristic $2$, then $F' = 2Y = 0$ and the method gives nothing. In this case the extension $k(x, y)/k(x)$ is not separable, because $y/x$ is a square root of $x$.

### The regular locus of a scheme

**Theorem 1.8.12.** Let $k$ be a field of characteristic $0$ and let $X$ be a scheme that is locally of finite type over $k$. Then the regular locus of $X$ is open in $X$.

Node: SG0000002V · Lean: `Singularity.regularLocus_isOpen_of_charZero`

*Proof.* Let $x$ be a regular point of $X$, and let $U$ be an affine open set that contains $x$. Let $R = \Gamma(U, \mathcal{O}_X)$. Then $R$ is of finite type over $k$, and $U \cong \operatorname{Spec} R$. For $y \in U$ with prime $\mathfrak{p}_y$ of $R$, the local ring $\mathcal{O}_{X, y}$ is isomorphic to $R_{\mathfrak{p}_y}$. Thus $y$ is a regular point of $X$ if and only if $\mathfrak{p}_y \in \operatorname{Reg}(R)$. By Theorem 1.8.10, $\operatorname{Reg}(R)$ is open, so the set of the regular points of $U$ is open in $U$. Since $U$ is open in $X$, this set is an open neighbourhood of $x$ in the regular locus. $\square$

In Lean, the isomorphism $\mathcal{O}_{X, y} \cong R_{\mathfrak{p}_y}$ is `AlgebraicGeometry.IsAffineOpen.isLocalization_stalk`, and the comparison of the two regular loci is `Singularity.mem_regularLocus_iff_of_isAffineOpen`.

### Perfect fields

The proof of Theorem 1.8.8 uses only one property of characteristic $0$: the extension $K/L$ is separable. So the proof gives the next result with no change.

**Theorem 1.8.13.** Let $A \subseteq D$ be as above, with $A$ a regular ring, and assume that $K/L$ is separable. Then there is $f \neq 0$ in $D$ with $D(f) \subseteq \operatorname{Reg}(D)$.

Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus_of_isSeparable`

Over a perfect field of characteristic $p$, the normalization lemma does not always give a separable extension $K/L$. We use a separating transcendence basis in its place, and for this we must first localize $D$. The next two lemmas let us do this.

**Lemma 1.8.14.** Let $A$ be a regular ring and let $S$ be a multiplicative subset of $A$. Then $S^{-1}A$ is a regular ring.

Lean: `Singularity.Algebra.isRegularRing_of_isLocalization`

*Proof.* The ring $S^{-1}A$ is Noetherian [AM69, Proposition 7.3]. Each prime of $S^{-1}A$ is $S^{-1}\mathfrak{p}$ for a prime $\mathfrak{p}$ of $A$ with $\mathfrak{p} \cap S = \emptyset$ [AM69, Proposition 3.11], and the local ring of $S^{-1}A$ at $S^{-1}\mathfrak{p}$ is isomorphic to $A_\mathfrak{p}$. This ring is regular, because $A$ is regular. $\square$

**Lemma 1.8.15.** Let $D$ be a domain, let $h \neq 0$ in $D$, and assume that there is $g \neq 0$ in $D_h$ with $D(g) \subseteq \operatorname{Reg}(D_h)$. Then there is $f \neq 0$ in $D$ with $D(f) \subseteq \operatorname{Reg}(D)$.

Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus_of_away`

*Proof.* Write $g = a/h^m$ with $a \in D$. Then $a \neq 0$, and we let $f = ah$. Then $f \neq 0$, because $D$ is a domain. Let $P$ be a prime of $D$ with $f \notin P$. Then $h \notin P$, so $PD_h$ is a prime of $D_h$, and $D_P$ is isomorphic to the local ring of $D_h$ at $PD_h$. Also $a \notin P$, so $g \notin PD_h$. Thus $PD_h \in \operatorname{Reg}(D_h)$, and $D_P$ is regular. $\square$

**Theorem 1.8.16.** Let $k$ be a perfect field and let $D$ be a domain of finite type over $k$. Then there is $f \neq 0$ in $D$ with $D(f) \subseteq \operatorname{Reg}(D)$.

Node: SG00000035 · Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus_of_perfectField`

*Proof.* The fraction field $K$ of $D$ is a finitely generated extension of $k$. Since $k$ is perfect, $K$ has a separating transcendence basis $t_1, \dots, t_s$ over $k$: the $t_i$ are algebraically independent over $k$, and $K$ is a finite separable extension of $k(t_1, \dots, t_s)$ [Mat, Section 26], [Stacks, Tag 030W]. Write $t_i = a_i/b$ with $a_i, b \in D$ and $b \neq 0$. By Lemma 1.8.15 it is sufficient to prove the theorem for $D_b$, which has the same fraction field and contains the $t_i$. So we can assume that $t_i \in D$.

Let $A_0 = k[t_1, \dots, t_s] \subseteq D$. It is a polynomial ring, because the $t_i$ are algebraically independent. Let $d_1, \dots, d_m$ generate $D$ as an algebra over $k$. Each $d_j$ is algebraic over $k(t_1, \dots, t_s)$, so after we clear the denominators, it satisfies an equation $c_j d_j^{n_j} + (\text{lower terms}) = 0$ with coefficients in $A_0$ and $c_j \neq 0$. Let $c = c_1 \cdots c_m$ and $A = (A_0)_c$. Then each $d_j$ is integral over $A$, so $D_c = A[d_1, \dots, d_m]$ is a finite $A$-module [AM69, Corollary 5.2]. The ring $A$ is regular by Lemma 1.8.14, because $A_0$ is regular [Mat, Section 19]. It is integrally closed, because it is a localization of a unique factorization domain [AM69, Proposition 5.12]. The fraction field of $A$ is $L = k(t_1, \dots, t_s)$, and the fraction field of $D_c$ is $K$, so $K/L$ is separable. Theorem 1.8.13 gives $g \neq 0$ in $D_c$ with $D(g) \subseteq \operatorname{Reg}(D_c)$, and Lemma 1.8.15 completes the proof. $\square$

**Theorem 1.8.17.** Let $k$ be a perfect field.

1. Let $R$ be an algebra of finite type over $k$. Then $\operatorname{Reg}(R)$ is open in $\operatorname{Spec} R$.
2. Let $X$ be a scheme that is locally of finite type over $k$. Then the regular locus of $X$ is open in $X$.

Node: SG00000036 · Lean: `Singularity.regularLocus_isOpen_of_perfectField`, `Singularity.Algebra.isOpen_regularLocus_of_perfectField`

*Proof.* The proofs of Theorems 1.8.10 and 1.8.12 apply with no change, with Theorem 1.8.16 in place of Theorem 1.8.9. $\square$

A field of characteristic $0$ is perfect, so Theorem 1.8.17 contains Theorems 1.8.10 and 1.8.12. In the Lean library, `Singularity.regularLocus_isOpen_of_charZero` and `Singularity.regularLocus_isOpen_of_perfectField` are now corollaries of `Singularity.regularLocus_isOpen_of_field`, the case of an arbitrary field (Theorem 1.9.5).

**Remark 1.8.18 (imperfect fields).** Let $k$ be an imperfect field of characteristic $p$, and let $t \in k$ have no $p$-th root in $k$. The ring $D = k[x]/(x^p - t)$ is a field, so it is regular. But the extension $D/k$ is not separable, and the derivative of $x^p - t$ is $0$. So the method of this section gives nothing for $D$, even though $D$ is regular. Example 6.2.7 gives a regular curve over such a field that is not smooth. The regular locus of an algebra of finite type over an imperfect field is still open, because such an algebra is excellent [EGA4-7, Section 7.8], [Mat, Section 32]. Section 1.9 gives a proof that does not use the theory of excellent rings. It uses the descent of regularity along flat local homomorphisms [Mat, Theorem 23.7] and a finite purely inseparable extension of $k$, and it is in the Lean library.

### The Lean proof

The results of this section are in `Singularity/Algebra/Jacobian.lean`, `Singularity/Algebra/GenericRegular.lean`, `Singularity/Algebra/GenericRegularPerfect.lean` and `Singularity/Scheme/RegularLocus.lean`. In Lean, $D$ is a ring with an algebra structure over $A$, and the condition $A \subseteq D$ is the class `FaithfulSMul A D`. The fraction fields are `FractionRing A` and `FractionRing D`, with the algebra structure `FractionRing.liftAlgebra`.

The proof of Theorem 1.8.8 uses these Mathlib results: `Field.exists_primitive_element` for the primitive element, `Ideal.under_ne_bot_of_algebraic_mem` for the element $a$ of Lemma 1.8.5, `IsLocalization.integerNormalization_spec` to clear the denominators in Lemma 1.8.6, `minpoly.isIntegrallyClosed_eq_field_fractions` for Lemma 1.8.7 and `minpoly.equivAdjoin` for the isomorphism $A[X]/(F) \cong A[z]$. Theorem 1.8.9 uses `exists_finite_inj_algHom_of_fg` for the normalization lemma and `MvPolynomial.isRegularRing_of_isRegularRing` for the regularity of $A$. The derivation $d/dX$ is `Polynomial.derivative'`. The proof of Theorem 1.8.16 uses `exists_isTranscendenceBasis_and_isSeparable_of_perfectField` of Mathlib for the separating transcendence basis. All the theorems of this section use only the three standard axioms of Lean.

### Notes and references

The Jacobian criterion in the form of Proposition 1.8.2 is in [Mat, Section 30], where Matsumura uses derivations to give criteria for regularity. The reduction to a hypersurface by a primitive element and a conductor is the classical proof that a variety in characteristic $0$ is smooth on a dense open set. Nagata used the criterion of Section 1.7 to prove that the regular locus is open for many rings [Nag62], and Grothendieck proved it for each algebra of finite type over a field, over $\mathbb{Z}$ or over a complete Noetherian local ring, because these rings are excellent [EGA4-7].
