---
title: The regular locus over an imperfect field
nodes: [SG00000038, SG0000000K]
sources: [Mat, AM69, Stacks, EGA4-7]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The regular locus over an imperfect field

Section 1.8 proved that the regular locus is open over a perfect field. Remark 1.8.18 explained why its method fails over an imperfect field: the fraction field of a domain need not be separably generated, and then the Jacobian criterion gives nothing. In this section we remove the hypothesis. We go up to a finite extension of the base field over which the fraction field is separably generated, and then we come down again with the flat descent of regularity. The method is classical [Mat, Sections 23 and 26], [Stacks, Tag 07PJ]. In this section $k$ is a field of characteristic $p > 0$. Characteristic 0 is covered by Section 1.8, because a field of characteristic 0 is perfect.

### Flat descent

**Theorem 1.9.1.** Let $(A, \mathfrak{m}, \kappa) \to (B, \mathfrak{n})$ be a flat local homomorphism of Noetherian local rings. If $B$ is regular, then $A$ is regular.

Node: SG00000038 · Lean: `Singularity.Algebra.isRegularLocalRing_of_flat`

*Proof.* By the theorem of Serre (Theorem 1.6.8), it is sufficient to prove that $\operatorname{pd}_A \kappa < \infty$. Let $d = \dim B$. Choose an exact sequence
$$0 \to K \to F_{d-1} \to \cdots \to F_0 \to \kappa \to 0$$
of finitely generated $A$-modules, with each $F_i$ free. This is possible because $A$ is Noetherian. Since $B$ is flat over $A$, the sequence stays exact after the tensor product with $B$. So $B \otimes_A K$ is a $d$-th syzygy of the $B$-module $B \otimes_A \kappa = B/\mathfrak{m}B$. By Theorem 1.6.3, $\operatorname{pd}_B (B/\mathfrak{m}B) \le d$. So $B \otimes_A K$ is projective, and it is free, because $B$ is local.

We show that $K$ is flat over $A$. Let $N$ be an $A$-module. Since $B$ is flat over $A$,
$$B \otimes_A \operatorname{Tor}_1^A(K, N) \cong \operatorname{Tor}_1^B(B \otimes_A K, B \otimes_A N) = 0.$$
By Proposition 6.4.1, $B$ is faithfully flat over $A$. Thus $\operatorname{Tor}_1^A(K, N) = 0$, and $K$ is flat. A finitely generated flat module over a Noetherian local ring is free [Mat, Theorem 7.10]. So the sequence above is a free resolution of $\kappa$ of length $d$, and $\operatorname{pd}_A \kappa \le d$. $\square$

### Descent along a finite map

We say that a domain $D$ is *generically regular* if there is $f \neq 0$ in $D$ with $D(f) \subseteq \operatorname{Reg}(D)$.

**Lemma 1.9.2.** Let $D \subseteq S$ be domains, with $D$ Noetherian and $S$ a finitely generated $D$-module. If $S$ is generically regular, then $D$ is generically regular.

Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus_of_finite`

*Proof.* Let $g \neq 0$ in $S$ with $D(g) \subseteq \operatorname{Reg}(S)$.

Step 1. We find $c \neq 0$ in $D$ with $c \in gS$. The element $g$ is integral over $D$. Choose an equation $g^m + a_{m-1} g^{m-1} + \cdots + a_0 = 0$ with $a_i \in D$ and $m$ minimal. Then $a_0 \neq 0$. Otherwise we could divide by $g$, because $S$ is a domain, and get an equation of a smaller degree. Let $c = a_0 = -g(g^{m-1} + \cdots + a_1)$.

Step 2. We find $r \neq 0$ in $D$ such that $S_r$ is a free $D_r$-module. Let $L$ be the fraction field of $D$. The $L$-vector space $L \otimes_D S$ is finite. Choose $s_1, \dots, s_n \in S$ that give a basis of it. The map $D^n \to S$ that they define is injective, because it is injective after the tensor product with $L$ and $D^n$ has no torsion. Its cokernel is a finitely generated $D$-module $Q$ with $L \otimes_D Q = 0$. So some $r \neq 0$ in $D$ has $rQ = 0$, and then $D_r^n \cong S_r$.

Step 3. Let $f = rc$, and let $\mathfrak{p} \in D(f)$. Since $S$ is integral over $D$, there is a prime $P$ of $S$ with $P \cap D = \mathfrak{p}$ [AM69, Theorem 5.10]. Then $c \notin P$, and $g \notin P$ because $g$ divides $c$. So $S_P$ is regular. The map $D_\mathfrak{p} \to S_P$ is local. It is flat, because $S_\mathfrak{p}$ is free over $D_\mathfrak{p}$ by Step 2 and $S_P$ is a localization of $S_\mathfrak{p}$. The ring $S_P$ is Noetherian, because $S$ is finite over $D$. By Theorem 1.9.1, $D_\mathfrak{p}$ is regular. Thus $D(f) \subseteq \operatorname{Reg}(D)$. $\square$

### Generic regularity over an arbitrary field

The proof of Theorem 1.8.16 uses only one property of the perfect field $k$: the fraction field of $D$ has a separating transcendence basis over $k$. So the proof gives the next result with no change.

**Proposition 1.9.3.** Let $D$ be a domain of finite type over a field $k$, and assume that the fraction field of $D$ is separably generated over $k$. Then $D$ is generically regular.

Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus_of_isSeparablyGenerated`

**Theorem 1.9.4.** Let $k$ be a field and let $D$ be a domain of finite type over $k$. Then $D$ is generically regular.

Lean: `Singularity.Algebra.exists_ne_zero_basicOpen_subset_regularLocus_of_finiteType`

*Proof.* Let $x_1, \dots, x_m$ generate $D$ over $k$. Let $\Omega$ be an algebraic closure of the fraction field of $D$, and let $P \subseteq \Omega$ be the perfect closure of $k$, the set of the elements $a$ with $a^{p^n} \in k$ for some $n$. Let $F = P(x_1, \dots, x_m) \subseteq \Omega$.

Step 1. The field $F$ is finitely generated over the perfect field $P$. So it has a separating transcendence basis $s_1, \dots, s_t$ over $P$ [Mat, Section 26]: the $s_i$ are algebraically independent over $P$, and each $x_j$ is separable over $P(s_1, \dots, s_t)$.

Step 2. We go down to a finite extension of $k$. Each $s_i$ is a quotient of two polynomials in the $x_j$ with coefficients in $P$. Each $x_j$ has a minimal polynomial over $P(s_1, \dots, s_t)$, and its coefficients are quotients of polynomials in the $s_i$ with coefficients in $P$. Let $E \subseteq P$ be the finite set of all these coefficients, and let $L = k(E)$. Each element of $E$ is algebraic over $k$, so $L$ is a finite extension of $k$. Now $s_i \in L(x_1, \dots, x_m)$, and the $s_i$ are algebraically independent over $L$, because they are independent over $P \supseteq L$. The minimal polynomial of $x_j$ over $P(s)$ has coefficients in $L(s)$, and it is separable. So $x_j$ is separable over $L(s)$. Thus $L(x_1, \dots, x_m)$ is a finite separable extension of $L(s_1, \dots, s_t)$, and it is separably generated over $L$.

Step 3. Let $S = L[x_1, \dots, x_m] \subseteq \Omega$. It is a domain of finite type over $L$, and its fraction field is $L(x_1, \dots, x_m)$. By Proposition 1.9.3, $S$ is generically regular. Also $D \subseteq S$, and $S = D[E]$. Each element of $E$ is integral over $k \subseteq D$, so $S$ is a finitely generated $D$-module. By Lemma 1.9.2, $D$ is generically regular. $\square$

The proof does not use the ring $D \otimes_k L$. This ring can be not reduced, as Remark 1.8.18 shows for $L = k(t^{1/p})$, and its regular locus does not determine that of $D$. The subring $S$ of $\Omega$ avoids this problem.

### The regular locus is open

**Theorem 1.9.5.** Let $k$ be a field.

1. Let $R$ be an algebra of finite type over $k$. Then $\operatorname{Reg}(R)$ is open in $\operatorname{Spec} R$.
2. Let $X$ be a scheme that is locally of finite type over $k$. Then the regular locus of $X$ is open in $X$.

Node: SG0000000K · Lean: `Singularity.regularLocus_isOpen_of_field`, `Singularity.Algebra.isOpen_regularLocus_of_field`

*Proof.* The proofs of Theorems 1.8.10 and 1.8.12 apply with no change, with Theorem 1.9.4 in place of Theorem 1.8.9. Each quotient $R/\mathfrak{p}$ is a domain of finite type over $k$, so it is generically regular, and the criterion of Nagata (Theorem 1.7.7) applies. $\square$

Theorem 1.9.5 contains Theorem 1.8.17, and thus Theorems 1.8.10 and 1.8.12. In the Lean library, `Singularity.regularLocus_isOpen_of_perfectField` and `Singularity.regularLocus_isOpen_of_charZero` are now corollaries of `Singularity.regularLocus_isOpen_of_field`. Thus condition 3 of the definition of a resolution, that the regular locus is open, holds for each variety over each field. Over an imperfect field, the regular locus and the smooth locus are different (Example 6.2.7), and the definition of resolution in this handbook uses the regular locus.

### The Lean proof

The results of this section are in `Singularity/Algebra/FlatDescent.lean`, `Singularity/Algebra/RegularLocusField.lean` and `Singularity/Scheme/RegularLocus.lean`. The Lean proof of Theorem 1.9.1 uses the converse of the theorem of Serre from Section 1.6. The proof of Lemma 1.9.2 uses the generic freeness of Mathlib in place of Step 2. In the proof of Theorem 1.9.4, the Lean proof takes the perfect closure inside an algebraic closure, and it collects the finite set $E$ with the lemma `exists_finset_mem_adjoin_union`. The main theorems use only the axioms `propext`, `Classical.choice` and `Quot.sound`.

### Notes and references

Theorem 1.9.1 is [Mat, Theorem 23.7 (i)]. The openness of the regular locus of an algebra of finite type over a field is a special case of the openness for excellent rings [EGA4-7, Section 7.8], [Mat, Section 32]. The proof of this section avoids the theory of excellent rings, and it is close to the proof of [Stacks, Tag 07PJ].
