---
title: Completion
nodes: []
sources: [AM69, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Completion

In this section $R$ is a ring and $I$ is an ideal of $R$. The completion of $R$ with respect to $I$ is the ring of the compatible systems of residues modulo the powers of $I$. For $R = k[x]$ and $I = (x)$ it is the ring $k[[x]]$ of formal power series, and for $R = \mathbb{Z}$ and $I = (p)$ it is the ring $\mathbb{Z}_p$ of $p$-adic integers. The main results are that, for a Noetherian ring, completion is exact on finitely generated modules (Proposition 4.2.5), the completion is flat (Theorem 4.2.7), and the completion is Noetherian (Theorem 4.2.9).

### Inverse limits

An *inverse system* of abelian groups is a sequence of groups $A_1, A_2, \dots$ with homomorphisms $\theta_n : A_{n+1} \to A_n$. Its *inverse limit* is the group
$$\varprojlim A_n = \{(a_n) \in \textstyle\prod_n A_n : \theta_n(a_{n+1}) = a_n \text{ for each } n\}.$$
A map of inverse systems $(A_n) \to (B_n)$ is a sequence of homomorphisms $A_n \to B_n$ that commute with the maps $\theta_n$. It gives a homomorphism of the inverse limits. If the groups are rings or modules and the maps respect this structure, then the limit is a ring or a module.

**Definition 4.2.1.** Let $M$ be an $R$-module. The *$I$-adic completion* of $M$ is
$$\hat{M} = \varprojlim M / I^n M,$$
for the natural maps $M/I^{n+1} M \to M/I^n M$. The map $M \to \hat{M}$ sends $x$ to the system of its classes. Its kernel is $\bigcap_n I^n M$. The module $M$ is *complete* if this map is bijective. The completion $\hat{R}$ is a ring, and $\hat{M}$ is an $\hat{R}$-module.

In topological terms, the sets $x + I^n M$ are a basis of a topology on $M$, the $I$-adic topology. The map $M \to \hat{M}$ is injective if and only if this topology is Hausdorff, and $\hat{M}$ is the completion of $M$ for this topology in the sense of Cauchy sequences [AM69, Chapter 10]. We use only the algebraic definition.

**Example 4.2.2 (power series).** Let $S = R[X_1, \dots, X_r]$ and $J = (X_1, \dots, X_r)$. The ideal $J^n$ is spanned over $R$ by the monomials of degree at least $n$, so $S/J^n$ is the free $R$-module on the monomials of degree less than $n$. An element of $\varprojlim S/J^n$ is a sequence of polynomials $f_n$ of degree less than $n$ such that $f_{n+1}$ and $f_n$ have the same terms of degree less than $n$. This is the same as a formal power series. The product of the limit is the product of power series. Thus $\hat{S} = R[[X_1, \dots, X_r]]$. In the same way, the kernel of $R[[X_1, \dots, X_r]] \to S/J^n$ is the set of the power series with no term of degree less than $n$. Such a series is a sum $\sum_{|\alpha| = n} X^\alpha g_\alpha$ over the finitely many monomials of degree $n$, so the kernel is $J^n R[[X_1, \dots, X_r]]$. Thus $R[[X_1, \dots, X_r]]$ is complete for its $J$-adic topology. For $R = \mathbb{Z}$ and $I = (p)$, the completion is the ring $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$ of $p$-adic integers.

### Two lemmas on limits

**Lemma 4.2.3.** Let $0 \to (A_n) \to (B_n) \to (C_n) \to 0$ be maps of inverse systems such that each sequence $0 \to A_n \to B_n \to C_n \to 0$ is exact. Assume that each map $A_{n+1} \to A_n$ is surjective. Then the sequence $0 \to \varprojlim A_n \to \varprojlim B_n \to \varprojlim C_n \to 0$ is exact.

Lean: `Singularity.Algebra.injOn_invLimMap`, `Singularity.Algebra.exists_invLim_of_invLimMap_eq_zero`, `Singularity.Algebra.surjOn_invLimMap` (the limit is the set of the compatible families)

*Proof.* Exactness at the first two places follows from the definition of the limit as a subgroup of a product. We prove that $\varprojlim B_n \to \varprojlim C_n$ is surjective. Let $(c_n)$ be in $\varprojlim C_n$. We choose $b_n \in B_n$ with image $c_n$ and $\theta_n(b_{n+1}) = b_n$, by induction on $n$. Choose any $b_1$ over $c_1$. Assume that $b_n$ is chosen, and choose any $b' \in B_{n+1}$ over $c_{n+1}$. Then $\theta_n(b') - b_n$ maps to $\theta_n(c_{n+1}) - c_n = 0$ in $C_n$, so it is the image of some $a \in A_n$. Since $A_{n+1} \to A_n$ is surjective, $a$ is the image of some $a' \in A_{n+1}$. Let $b_{n+1} = b' - a'$, where we view $a'$ in $B_{n+1}$. Then $b_{n+1}$ maps to $c_{n+1}$, and $\theta_n(b_{n+1}) = \theta_n(b') - a = b_n$. $\square$

**Lemma 4.2.4.** Let $M$ be an $R$-module, and let $(M_n)$ and $(M'_n)$ be descending chains of submodules of $M$. Assume that $M'_n \subseteq M_n$ for each $n$, and that there is $c$ with $M_{n+c} \subseteq M'_n$ for each $n$. Then the natural map $\varprojlim M/M'_n \to \varprojlim M/M_n$ is bijective.

Lean: `Singularity.Algebra.bijOn_chainLimitMap` (the limit is the set of the compatible families)

*Proof.* Let $(x_n)$ be in $\varprojlim M/M'_n$ with image $0$. Fix $n$. The element $x_{n+c}$ has a representative $y \in M$, and the image of $x_{n+c}$ in $M/M_{n+c}$ is $0$, so $y \in M_{n+c} \subseteq M'_n$. Since $x_n$ is the class of $y$ in $M/M'_n$, we get $x_n = 0$. Thus the map is injective. Let $(y_n)$ be in $\varprojlim M/M_n$. Since $M_{n+c} \subseteq M'_n$, there is a natural map $M/M_{n+c} \to M/M'_n$. Let $x_n$ be the image of $y_{n+c}$. The elements $x_n$ are compatible, because the elements $y_n$ are. The composite map $M/M_{n+c} \to M/M'_n \to M/M_n$ is the natural map, so $x_n$ maps to $y_n$. Thus the map is surjective. $\square$

### Exactness

**Proposition 4.2.5.** Let $R$ be a Noetherian ring, let $I$ be an ideal and let $0 \to N \to M \to P \to 0$ be an exact sequence of finitely generated $R$-modules. Then the sequence of $I$-adic completions $0 \to \hat{N} \to \hat{M} \to \hat{P} \to 0$ is exact.

Lean: `Singularity.Algebra.adicCompletion_shortExact`

*Proof.* We view $N$ as a submodule of $M$, so that $P = M/N$. For each $n$ the sequence
$$0 \to N/(I^n M \cap N) \to M/I^n M \to P/I^n P \to 0$$
is exact, because $I^n P$ is the image of $I^n M$ in $P$. The maps $N/(I^{n+1}M \cap N) \to N/(I^n M \cap N)$ are surjective. By Lemma 4.2.3, the sequence of limits is exact. It remains to identify $\varprojlim N/(I^n M \cap N)$ with $\hat{N}$. By Corollary 4.1.6 there is $c$ with $I^{n+c} M \cap N \subseteq I^n N \subseteq I^n M \cap N$ for each $n$. Apply Lemma 4.2.4 to the chains $M'_n = I^n N$ and $M_n = I^n M \cap N$ of $N$. It gives that the natural map $\hat{N} \to \varprojlim N/(I^n M \cap N)$ is bijective. $\square$

The proof uses the Artin-Rees lemma in an essential way. In general the filtration $(I^n M \cap N)$ of $N$ is not the $I$-adic filtration of $N$, and the proof needs that both filtrations give the same limit.

**Theorem 4.2.6.** Let $R$ be a Noetherian ring, let $I$ be an ideal and let $M$ be a finitely generated $R$-module. Then the natural map $\hat{R} \otimes_R M \to \hat{M}$ is an isomorphism of $\hat{R}$-modules.

Lean: `Singularity.Algebra.exists_tensorProduct_equiv_adicCompletion`

*Proof.* For each $R$-module $M$, the map $\hat{R} \otimes_R M \to \hat{M}$ sends $a \otimes x$ to $a \cdot \hat{x}$, where $\hat{x}$ is the image of $x$ in $\hat{M}$. It is natural in $M$. For $M = R^n$ it is an isomorphism, because the completion of a finite direct sum is the direct sum of the completions. Now let $M$ be finitely generated, and take an exact sequence $0 \to K \to R^n \to M \to 0$. The module $K$ is finitely generated, because $R$ is Noetherian. Take a surjection $R^m \to K$. By Proposition 4.2.5, applied to the two short exact sequences, the sequence $\hat{R}^m \to \hat{R}^n \to \hat{M} \to 0$ is exact. The tensor product is right exact, so the sequence $\hat{R}^m \to \hat{R}^n \to \hat{R} \otimes_R M \to 0$ is exact. The natural maps give a map between the two sequences, and it is an isomorphism on the first two terms. Thus it is an isomorphism on the cokernels. $\square$

**Theorem 4.2.7.** Let $R$ be a Noetherian ring and let $I$ be an ideal. Then $\hat{R}$ is a flat $R$-module.

Lean: `Singularity.Algebra.flat_adicCompletion`

*Proof.* By [AM69, Proposition 2.19], it is sufficient to show that for each injective map $N \to M$ of finitely generated $R$-modules, the map $\hat{R} \otimes_R N \to \hat{R} \otimes_R M$ is injective. By Theorem 4.2.6 this map is the map $\hat{N} \to \hat{M}$, and it is injective by Proposition 4.2.5. $\square$

### The completion as a ring

**Proposition 4.2.8.** Let $R$ be a Noetherian ring, let $I$ be an ideal and let $\hat{R}$ be the $I$-adic completion. Then:

1. For each $n$, the kernel of the projection $\hat{R} \to R/I^n$ is $I^n \hat{R}$, so $\hat{R}/I^n \hat{R} \cong R/I^n$.
2. $(I\hat{R})^n = I^n \hat{R}$, and $\hat{R}$ is complete for its $I\hat{R}$-adic topology.
3. The ideal $I\hat{R}$ is contained in the Jacobson radical of $\hat{R}$.

Lean: `Singularity.Algebra.ker_evalₐ_eq_map_pow`, `Singularity.Algebra.adicCompletionQuotientPowAlgEquiv`, `Singularity.Algebra.map_pow_adicCompletion`, `Singularity.Algebra.isAdicComplete_map_adicCompletion`, `Singularity.Algebra.map_le_jacobson_adicCompletion` (for a finitely generated ideal, which covers the Noetherian case).

*Proof.* For 1, apply Proposition 4.2.5 to the sequence $0 \to I^n \to R \to R/I^n \to 0$. The module $R/I^n$ is killed by $I^k$ for $k \ge n$, so its completion is $R/I^n$, and the map $\hat{R} \to R/I^n$ is the projection to the $n$-th term. Its kernel is the image of the completion of $I^n$. By Theorem 4.2.6, this image is the image of $\hat{R} \otimes_R I^n \to \hat{R}$, and this is $I^n \hat{R}$.

For 2, the ideal $(I\hat{R})^n$ is generated by the products of $n$ elements of $I$, so it is $I^n \hat{R}$. By 1, the map $\hat{R} \to \varprojlim \hat{R}/I^n\hat{R} = \varprojlim R/I^n$ is the identity of $\hat{R}$, so $\hat{R}$ is complete.

For 3, let $x \in I\hat{R}$. We show that $1 - x$ is a unit. Let $s_n$ be the class of $1 + x + \dots + x^{n-1}$ in $\hat{R}/I^n\hat{R}$. Since $x^n \in I^n \hat{R}$, the classes $s_n$ are compatible, and by 2 they define an element $s \in \hat{R}$. For each $n$, $(1 - x)s \equiv 1 - x^n \equiv 1$ modulo $I^n \hat{R}$. By 2, $\bigcap_n I^n \hat{R} = 0$, so $(1 - x)s = 1$. Since $1 - xy$ is a unit for each $y \in \hat{R}$, the element $x$ is in the Jacobson radical [AM69, Proposition 1.9]. $\square$

**Theorem 4.2.9.** Let $R$ be a Noetherian ring and let $I$ be an ideal. Then the $I$-adic completion $\hat{R}$ is Noetherian. More exactly, if $a_1, \dots, a_r$ generate $I$, then $\hat{R}$ is a quotient of the ring of power series $R[[X_1, \dots, X_r]]$.

Lean: none yet

*Proof.* Let $S = R[X_1, \dots, X_r]$, let $J = (X_1, \dots, X_r)$, and let $\psi : S \to R$ be the map of $R$-algebras with $\psi(X_i) = a_i$. Then $\psi(J^n) = I^n$. So $\psi$ gives surjective maps $S/J^n \to R/I^n$, and the kernel of $S/J^n \to R/I^n$ is $\psi^{-1}(I^n)/J^n$. Since $\psi(J^n) = I^n$, we have $\psi^{-1}(I^n) = \ker \psi + J^n$. Thus the kernel is $K_n = (\ker \psi + J^n)/J^n$, and the map $K_{n+1} \to K_n$ is surjective, because the image of $\ker \psi$ in $K_n$ is all of $K_n$. By Lemma 4.2.3, the map $\hat{S} \to \hat{R}$ is surjective. By Example 4.2.2, $\hat{S} = R[[X_1, \dots, X_r]]$. This ring is Noetherian by the basis theorem of Hilbert for power series [Mat, Section 3]. Thus $\hat{R}$ is Noetherian. $\square$

### Notes and references

Our treatment follows [AM69, Chapter 10]. Lemma 4.2.3 is [AM69, Proposition 10.2], Proposition 4.2.5 is [AM69, Proposition 10.12], Theorem 4.2.6 is [AM69, Proposition 10.13], Theorem 4.2.7 is [AM69, Proposition 10.14], and Proposition 4.2.8 is part of [AM69, Proposition 10.15]. Atiyah and Macdonald prove Theorem 4.2.9 with the associated graded ring [AM69, Theorem 10.26]. Matsumura gives the proof with power series in [Mat, Section 8]. The completion of a ring that is not Noetherian need not be complete, and completion need not be exact for modules that are not finitely generated. We use the results only for Noetherian rings and finitely generated modules.
