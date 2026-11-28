---
title: The Hilbert-Samuel function
nodes: [SG0000000Q, SG0000002D]
sources: [AM69, Nag62, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Hilbert-Samuel function

In this section $R$ is a commutative ring, $I$ is an ideal of $R$ and $M$ is an $R$-module. We write $\ell(M) = \ell_R(M)$ for the length of $M$. It is the supremum of the lengths $n$ of the chains $0 = M_0 \subsetneq M_1 \subsetneq \dots \subsetneq M_n = M$ of submodules, so it is an element of $\mathbb{N} \cup \{\infty\}$. We use two facts about length. First, for each exact sequence $0 \to N \to M \to P \to 0$ we have $\ell(M) = \ell(N) + \ell(P)$, with the rule $a + \infty = \infty$ [AM69, Proposition 6.9]. Second, a vector space over a field has length equal to its dimension [AM69, Proposition 6.10].

Lean: `Module.length` (in Mathlib)

### The definition

**Definition 3.1.1.** The *Hilbert-Samuel function* of $M$ with respect to $I$ is the function
$$\chi_{I,M} : \mathbb{N} \to \mathbb{N} \cup \{\infty\}, \qquad \chi_{I,M}(n) = \ell_R(M / I^n M).$$
When $M = R$ we write $\chi_I$, and when $(R, \mathfrak{m})$ is a local ring we write $\chi_R = \chi_{\mathfrak{m}, R}$.

Node: SG0000000Q · Lean: `Singularity.Algebra.hilbertSamuel`

Some books use the function $n \mapsto \ell(M/I^{n+1}M)$. It is $\chi_{I,M}(n+1)$ in our notation, so the two choices give the same theory. Our choice gives $\chi_{I,M}(0) = 0$, and it makes the recursion of Proposition 3.1.3 simple.

**Lemma 3.1.2.** Let $N \subseteq P$ be submodules of $M$. Then $\ell(M/N) = \ell(P/N) + \ell(M/P)$.

Lean: `Singularity.Algebra.length_quotient_eq_add`

*Proof.* The inclusion $P \to M$ gives an injective map $P/N \to M/N$, and the identity of $M$ gives a surjective map $M/N \to M/P$, because $N \subseteq P$. The kernel of the second map is the set of classes of elements of $P$, and this is the image of the first map. Thus the sequence $0 \to P/N \to M/N \to M/P \to 0$ is exact, and the formula is the additivity of length. $\square$

### The basic laws

**Proposition 3.1.3.** The function $\chi = \chi_{I,M}$ has these properties.

1. $\chi(0) = 0$.
2. $\chi(n+1) = \chi(n) + \ell(I^n M / I^{n+1} M)$ for each $n$.
3. $\chi(n) \le \chi(n+1)$ for each $n$, so $\chi$ is monotone.
4. If $I \subseteq J$, then $\chi_{J,M}(n) \le \chi_{I,M}(n)$ for each $n$.
5. If $J$ is an ideal with $J^k \subseteq I$, then $\chi_{I,M}(n) \le \chi_{J,M}(kn)$ for each $n$.

Lean: `Singularity.Algebra.hilbertSamuel_zero`, `Singularity.Algebra.hilbertSamuel_succ`, `Singularity.Algebra.hilbertSamuel_mono`, `Singularity.Algebra.hilbertSamuel_anti`, `Singularity.Algebra.hilbertSamuel_le_of_pow_le`

*Proof.* For 1, $I^0 = R$, so $I^0 M = M$ and $M/I^0M = 0$. For 2, apply Lemma 3.1.2 to $N = I^{n+1}M$ and $P = I^n M$. Here $N \subseteq P$, because $I^{n+1} \subseteq I^n$. Statement 3 follows from 2.

For 4 and 5, let $I'$ and $J'$ be ideals with $I' \subseteq J'$. Then $I'M \subseteq J'M$, so the identity of $M$ gives a surjective map $M/I'M \to M/J'M$. A quotient of a module has a smaller length, by the additivity of length. For 4, take $I' = I^n$ and $J' = J^n$. For 5, take $I' = J^{kn} = (J^k)^n$ and $J' = I^n$. $\square$

**Lemma 3.1.4.** Let $R$ be a Noetherian ring and let $\mathfrak{m}$ be a maximal ideal of $R$ with residue field $\kappa = R/\mathfrak{m}$. Let $Q$ be a finitely generated $R$-module with $\mathfrak{m} Q = 0$. Then $\ell_R(Q) = \dim_\kappa Q$, and in particular $\ell_R(Q)$ is finite.

Lean: `Singularity.Algebra.length_ne_top_of_smul_eq_bot`

*Proof.* Since $\mathfrak{m}$ annihilates $Q$, the action of $R$ on $Q$ comes from an action of $\kappa$. The $R$-submodules of $Q$ are the $\kappa$-subspaces of $Q$, so $\ell_R(Q) = \ell_\kappa(Q) = \dim_\kappa Q$. A set of generators of $Q$ over $R$ spans $Q$ over $\kappa$, so $\dim_\kappa Q$ is finite. $\square$

The hypothesis that $R$ is Noetherian is not necessary for the lemma. We use it in the next theorem, to know that each $\mathfrak{m}^n M$ is finitely generated.

**Theorem 3.1.5.** Let $R$ be a Noetherian ring, let $M$ be a finitely generated $R$-module and let $\mathfrak{m}$ be a maximal ideal of $R$. Let $I$ be an ideal of $R$ that contains a power $\mathfrak{m}^k$ of $\mathfrak{m}$. Then $\chi_{I,M}(n)$ is finite for each $n$.

Node: SG0000002D · Lean: `Singularity.Algebra.hilbertSamuel_ne_top`

*Proof.* By Proposition 3.1.3, part 5, $\chi_{I,M}(n) \le \chi_{\mathfrak{m},M}(kn)$. Thus it is sufficient to prove the theorem for $I = \mathfrak{m}$. We use induction on $n$. For $n = 0$ the value is $0$. Assume that $\chi_{\mathfrak{m},M}(n)$ is finite. By Proposition 3.1.3, part 2, it is sufficient to show that $Q = \mathfrak{m}^n M / \mathfrak{m}^{n+1} M$ has finite length. The module $M$ is Noetherian, because $R$ is Noetherian and $M$ is finitely generated [AM69, Proposition 6.5]. Thus the submodule $\mathfrak{m}^n M$ is finitely generated, and so is its quotient $Q$. For $a \in \mathfrak{m}$ and $x \in \mathfrak{m}^n M$ we have $ax \in \mathfrak{m}^{n+1} M$, so $\mathfrak{m} Q = 0$. Lemma 3.1.4 gives the result. $\square$

Let $(R, \mathfrak{m})$ be a Noetherian local ring. An ideal $I$ is $\mathfrak{m}$-primary if and only if $\mathfrak{m}^k \subseteq I \subseteq \mathfrak{m}$ for some $k$ [AM69, Corollary 7.16]. Thus Theorem 3.1.5 applies to each $\mathfrak{m}$-primary ideal, and this is the case of interest.

### Examples

**Example 3.1.6.** Let $\mathfrak{m}$ be a maximal ideal of $R$. Then $\chi_{\mathfrak{m}}(1) = \ell(R/\mathfrak{m}) = 1$, because $R/\mathfrak{m}$ is a field, and a field has no ideals other than $0$ and itself.

Lean: `Singularity.Algebra.hilbertSamuel_self_one`

Now let $k$ be a field, let $A = k[x_1, \dots, x_d]$ and let $R = A_\mathfrak{n}$ with $\mathfrak{n} = (x_1, \dots, x_d)$. We write $j$ for the index, to avoid a clash with the ideal $\mathfrak{n}$. By Lemma 3.1.4 and Proposition 3.1.3, part 2, $\chi_R(j+1) - \chi_R(j) = \dim_k \mathfrak{m}^j / \mathfrak{m}^{j+1}$. Each element $s \in A \setminus \mathfrak{n}$ is a unit modulo $\mathfrak{n}^{j+1}$, because its image in $A/\mathfrak{n}^{j+1}$ is outside the only maximal ideal. Thus $A/\mathfrak{n}^{j+1} = R/\mathfrak{m}^{j+1}$, and $\mathfrak{m}^j/\mathfrak{m}^{j+1}$ is isomorphic to $\mathfrak{n}^j/\mathfrak{n}^{j+1}$. It has a basis of the monomials of degree $j$, and there are $\binom{j+d-1}{d-1}$ of them. Thus
$$\chi_R(j) = \sum_{i=0}^{j-1} \binom{i+d-1}{d-1} = \binom{j+d-1}{d}.$$
For large $j$ this is a polynomial in $j$ of degree $d = \dim R$ with leading coefficient $1/d!$.

Lean: `Singularity.Algebra.isRegularLocalRing_affineOriginRing`, `Singularity.Algebra.hilbertSamuel_affineOriginRing_succ`, `Singularity.Algebra.length_grPiece_affineOriginRing`, `Singularity.Algebra.samuelMultiplicity_affineOriginRing` (the local ring at the origin of affine space).

**Remark 3.1.7 (the multiplicity).** Let $(R, \mathfrak{m})$ be a Noetherian local ring of dimension $d$, let $I$ be an $\mathfrak{m}$-primary ideal and let $M$ be a finitely generated $R$-module. By the theorem of Hilbert and Samuel, there is a polynomial $P$ with rational coefficients such that $\chi_{I,M}(n) = P(n)$ for large $n$. Section 3.3 proves this result (Theorem 3.3.6). The degree of $P$ is at most $d$, and for $M = R$ it is exactly $d$ [AM69, Theorem 11.14]. The *multiplicity* $e(I, M)$ is $d!$ times the coefficient of $n^d$ in $P$, and $e(R) = e(\mathfrak{m}, R)$. Section 3.3 defines it, proves its first laws and proves that $e(R) = 1$ for each regular local ring (Theorem 3.3.13). Example 3.1.6 gives $e(R) = 1$ for the local ring of affine space at the origin. A theorem of Nagata says that an unmixed local ring $R$ is regular if and only if $e(R) = 1$ [Nag62, Section 40]. This edition does not prove the theorem of Nagata or the equality of the degree with the dimension.

Lean: none yet
