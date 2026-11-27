---
title: The Frobenius
nodes: []
sources: [Mat, AM69]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Frobenius

Let $R$ be a ring of characteristic $p$. For $0 < i < p$, the prime $p$ divides the binomial coefficient $\binom{p}{i}$, so $(a + b)^p = a^p + b^p$ in $R$. This simple fact gives a ring homomorphism from $R$ to itself. This section defines it and proves its first properties.

**Definition 6.1.1.** Let $R$ be a ring of characteristic $p$. The *Frobenius* of $R$ is the ring homomorphism $F : R \to R$, $F(a) = a^p$. For $e \ge 1$ we write $q = p^e$ and $F^e(a) = a^q$. We write $F^e_* R$ for the $R$-module whose group is $R$ and whose scalar multiplication is $r \cdot s = r^q s$. The ring $R$ is *perfect* if $F$ is bijective. A field $K$ of characteristic $p$ is perfect if $K = K^p$.

The Frobenius is a homomorphism because $(ab)^p = a^p b^p$, $(a + b)^p = a^p + b^p$ and $1^p = 1$. By induction, $(a + b)^q = a^q + b^q$. The Frobenius of a field is injective, so a field is perfect in the sense of rings if and only if $K = K^p$. Each homomorphism $\varphi : R \to S$ of rings of characteristic $p$ commutes with the Frobenius: $\varphi \circ F_R = F_S \circ \varphi$.

**Lemma 6.1.2.** Let $R$ be a ring of characteristic $p$ and let $\mathfrak{p}$ be a prime ideal. Then $F^{-1}(\mathfrak{p}) = \mathfrak{p}$. So the map $\operatorname{Spec} R \to \operatorname{Spec} R$ that $F$ gives is the identity.

Lean: `Singularity.Algebra.comap_frobenius_eq`, `Singularity.Algebra.primeSpectrum_comap_frobenius`

*Proof.* For $a \in R$ we have $a^p \in \mathfrak{p}$ if and only if $a \in \mathfrak{p}$, because $\mathfrak{p}$ is prime. $\square$

**Proposition 6.1.3.** Let $R$ be a ring of characteristic $p$. Then $F$ is injective if and only if $R$ is reduced.

Lean: `Singularity.Algebra.injective_frobenius_iff_isReduced`

*Proof.* The kernel of $F$ is the set of the elements $a$ with $a^p = 0$. If $R$ is reduced, this set is $0$. Conversely, assume that $F$ is injective, and let $a$ be nilpotent. Take $e$ with $a^{p^e} = 0$. Then $F^e(a) = 0$. The map $F^e$ is injective, because it is a composite of injective maps. Thus $a = 0$. $\square$

**Example 6.1.4.** A finite field is perfect, because its Frobenius is an injective map from a finite set to itself. An algebraically closed field is perfect. The field $\mathbb{F}_p(t)$ is not perfect: if $t = (a/b)^p$ with polynomials $a, b$, then $t b^p = a^p$. The degree of the left side is $1$ modulo $p$, and the degree of the right side is $0$ modulo $p$. This is not possible.

Lean: `Singularity.Example.perfectRing_of_finite`, `Singularity.Example.perfectRing_of_isAlgClosed`, `Singularity.Example.not_perfectRing_ratFunc`

### The Frobenius of a ring of power series

**Proposition 6.1.5.** Let $K$ be a field of characteristic $p$, let $q = p^e$, let $S = K[[x_1, \dots, x_n]]$ and let $S_e = K[[x_1^q, \dots, x_n^q]]$ be the subring of the power series in $x_1^q, \dots, x_n^q$. Then $S$ is a free $S_e$-module, with basis the monomials $x^\alpha$ with $0 \le \alpha_i < q$ for each $i$. The same holds for the polynomial ring $K[x_1, \dots, x_n]$ over its subring $K[x_1^q, \dots, x_n^q]$.

Lean: `Singularity.Algebra.boxBasis`, `Singularity.Algebra.finrank_powSubalgebra`, `Singularity.Algebra.boxBasisPoly`, `Singularity.Algebra.finrank_powSubalgebraPoly` (with $S_e$ taken as the series or the polynomials supported on $q\mathbb{N}^n$)

*Proof.* Each exponent $\beta \in \mathbb{N}^n$ can be written in exactly one way as $\beta = q\gamma + \alpha$ with $\gamma \in \mathbb{N}^n$ and $0 \le \alpha_i < q$. Let $f = \sum_\beta c_\beta x^\beta$ be in $S$. For each $\alpha$ in the box $0 \le \alpha_i < q$, let $f_\alpha = \sum_\gamma c_{q\gamma + \alpha} x^{q\gamma}$. This is an element of $S_e$, and $f = \sum_\alpha x^\alpha f_\alpha$. The coefficients of $f$ determine the series $f_\alpha$, and conversely. So the expression is unique. For polynomials the same proof works with finite sums. $\square$

**Corollary 6.1.6.** Let $K$ be a perfect field of characteristic $p$ and let $S = K[[x_1, \dots, x_n]]$. Then $F^e_* S$ is a free $S$-module of rank $q^n$, where $q = p^e$. In particular, the Frobenius of $S$ is flat.

Lean: `Singularity.Algebra.iterateFrobenius_finite_and_flat` (the map $F^e$ is finite and flat; the rank $q^n$ is not stated in Lean)

*Proof.* The image of $F^e$ is the ring $K^q[[x_1^q, \dots, x_n^q]]$, and $K^q = K$ because $K$ is perfect. So $F^e$ is an isomorphism from $S$ onto $S_e$. Under this isomorphism, the $S$-module $F^e_* S$ is the ring $S$ as an $S_e$-module. By Proposition 6.1.5 it is free of rank $q^n$. A free module is flat. $\square$

The same proof shows that $F_* K[x_1, \dots, x_n]$ is a free module of rank $p^n$ over $K[x_1, \dots, x_n]$ when $K$ is perfect. When $K$ is not perfect, the image of $F$ is $K^p[[x_1^p, \dots, x_n^p]]$, and $K$ is an extension of $K^p$ that can be infinite. Section 6.4 proves that the Frobenius of $K[[x_1, \dots, x_n]]$ is still flat. With Lemma 6.1.2, this gives a first view of the theorem of Kunz: the Frobenius of a regular ring is flat, and it does not change the points of the spectrum.

### Notes and references

The Frobenius is the basic tool of commutative algebra in positive characteristic. Matsumura uses it in [Mat, Section 26] for the theory of separability and $p$-bases, which is the subject of Section 6.2. The notation $F_* R$ comes from algebraic geometry: it is the direct image of the structure sheaf under the morphism $\operatorname{Spec} R \to \operatorname{Spec} R$ that $F$ gives. A Noetherian ring $R$ of characteristic $p$ is *F-finite* if $F_* R$ is a finitely generated $R$-module. By Corollary 6.1.6, $K[[x_1, \dots, x_n]]$ is F-finite when $K$ is perfect.
