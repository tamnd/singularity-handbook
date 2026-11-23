---
title: Finiteness of the normalization
nodes: [SG00000025, SG00000026, SG00000027]
sources: [AM69, Mat, Har, Nag62, Stacks, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Finiteness of the normalization

Let $A$ be a domain. The normalization $\tilde{A}$ is a subring of $\operatorname{Frac} A$ that contains $A$, but in general it need not be a finite $A$-module. Nagata found a Noetherian local domain of dimension 1 whose normalization is not finite [Nag62, Appendix]. For a finitely generated domain over a field, E. Noether proved that $\tilde{A}$ is always finite. In this section we prove her theorem when a field extension is separable, and in particular in characteristic 0. The tool is the trace form of a separable field extension.

Throughout the section, $P$ is an integrally closed domain, $K = \operatorname{Frac} P$, $L$ is a finite field extension of $K$, and $B$ is the integral closure of $P$ in $L$.

### Integral elements and the trace

**Lemma 2.3.1.** For each $b \in L$ there is an element $a \in P$ with $a \ne 0$ such that $ab \in B$.

Lean: `exists_integral_multiple` (in Mathlib)

*Proof.* The element $b$ is algebraic over $K$, so
$$b^n + c_1 b^{n-1} + \dots + c_n = 0$$
for some $c_1, \dots, c_n \in K$. Choose $a \in P$ with $a \ne 0$ such that $a c_i \in P$ for each $i$, for example the product of the denominators. We multiply the equation by $a^n$ and get
$$(ab)^n + (a c_1)(ab)^{n-1} + (a^2 c_2)(ab)^{n-2} + \dots + a^n c_n = 0.$$
Each coefficient $a^i c_i = a^{i-1} (a c_i)$ is in $P$, so $ab$ is integral over $P$. $\square$

For $b \in L$, multiplication by $b$ is a $K$-linear map $L \to L$. Its trace is the *trace* $\operatorname{Tr}_{L/K}(b) \in K$. The trace is $K$-linear in $b$.

**Lemma 2.3.2.** Let $b \in B$. Then the coefficients of the minimal polynomial of $b$ over $K$ are in $P$, and $\operatorname{Tr}_{L/K}(b) \in P$.

Lean: `minpoly.isIntegrallyClosed_eq_field_fractions`, `Algebra.isIntegral_trace` (in Mathlib)

*Proof.* Let $F$ be the minimal polynomial of $b$ over $K$, and let $M$ be a field extension of $L$ in which $F$ splits, $F = \prod_{j} (T - b_j)$. The element $b$ is a root of a monic polynomial $G$ with coefficients in $P$, and $F$ divides $G$ in $K[T]$. Thus each root $b_j$ of $F$ is a root of $G$, and so it is integral over $P$. The coefficients of $F$ are polynomials in the $b_j$ with integer coefficients, so they are integral over $P$. They are also in $K$, and $P$ is integrally closed, so they are in $P$.

Let $m = [L : K(b)]$. With a basis of $L$ over $K(b)$, the matrix of multiplication by $b$ on $L$ is a block matrix with $m$ copies of the matrix of multiplication by $b$ on $K(b)$. The trace of the second matrix is $-c_1$, where $c_1$ is the second coefficient of $F$. Thus $\operatorname{Tr}_{L/K}(b) = -m c_1 \in P$. $\square$

This is [AM69, Proposition 5.15]. The next fact is from field theory. If $L$ is separable over $K$, then the *trace form* $(u, v) \mapsto \operatorname{Tr}_{L/K}(uv)$ is a nondegenerate $K$-bilinear form on $L$ [AM69, Chapter 5, Exercise 27 and the proof of Proposition 5.17]. Thus for each basis $v_1, \dots, v_n$ of $L$ over $K$ there is a *dual basis* $w_1, \dots, w_n$ with
$$\operatorname{Tr}_{L/K}(v_i w_j) = \begin{cases} 1 & \text{if } i = j, \\ 0 & \text{if } i \ne j. \end{cases}$$
The trace form of an inseparable extension is zero. For example, if $K = \mathbb{F}_p(t)$ and $L = K(t^{1/p})$, then $\operatorname{Tr}_{L/K}$ is the zero map. This is the reason why the separable case is easier.

**Theorem 2.3.3.** Assume that $P$ is Noetherian and that $L$ is separable over $K$. Then $B$ is a finite $P$-module.

Lean: `IsIntegralClosure.finite` (in Mathlib)

*Proof.* Let $u_1, \dots, u_n$ be a basis of $L$ over $K$. By Lemma 2.3.1 there are nonzero $a_i \in P$ with $a_i u_i \in B$. The elements $v_i = a_i u_i$ are also a basis of $L$ over $K$, and they are in $B$. Let $w_1, \dots, w_n$ be the dual basis for the trace form.

Let $b \in B$, and write $b = \sum_j c_j w_j$ with $c_j \in K$. For each $i$,
$$\operatorname{Tr}_{L/K}(b v_i) = \sum_j c_j \operatorname{Tr}_{L/K}(w_j v_i) = c_i.$$
The element $b v_i$ is in $B$, because $B$ is a ring. By Lemma 2.3.2, $c_i \in P$. Thus
$$B \subseteq P w_1 + \dots + P w_n.$$
The right side is a finitely generated $P$-module, and $P$ is Noetherian, so its submodule $B$ is finitely generated [AM69, Proposition 6.5]. $\square$

This is [AM69, Proposition 5.17] and the remark after it. Note that $B$ is between two free $P$-modules of rank $n$: it contains $P v_1 + \dots + P v_n$, and it is contained in $P w_1 + \dots + P w_n$.

### The finiteness theorem

**Theorem 2.3.4.** Let $P \subseteq A$ be domains such that $A$ is a finite $P$-module. Assume that $P$ is Noetherian and integrally closed, and that $\operatorname{Frac} A$ is separable over $\operatorname{Frac} P$. Then the normalization $\tilde{A}$ is a finite $A$-module.

Node: SG00000025 · Lean: `Singularity.Algebra.finite_integralClosure_of_finite`

*Proof.* Let $K = \operatorname{Frac} P$ and $L = \operatorname{Frac} A$.

*Step 1. $L$ is a finite extension of $K$.* Let $a_1, \dots, a_m$ generate $A$ as a $P$-module. Let $D \subseteq L$ be the $K$-subspace that $a_1, \dots, a_m$ span. It is the set of the fractions $a/s$ with $a \in A$ and $s \in P \setminus \{0\}$, so it is a subring of $L$ that contains $A$, and it has finite dimension over $K$. A domain that has finite dimension over a field is a field: for $d \in D$ with $d \ne 0$, the multiplication by $d$ is an injective $K$-linear map $D \to D$, so it is surjective, and $d$ has an inverse in $D$. Thus $D$ is a subfield of $L$ that contains $A$, and so $D = L$. In particular $[L : K] \le m$.

*Step 2. $\tilde{A}$ is contained in $B$.* The ring $A$ is integral over $P$, because it is a finite $P$-module. By Lemma 2.1.2, each element of $L$ that is integral over $A$ is integral over $P$. Thus $\tilde{A} \subseteq B$, where $B$ is the integral closure of $P$ in $L$.

*Step 3.* By Theorem 2.3.3, $B$ is a finite $P$-module. Since $P$ is Noetherian, $B$ is a Noetherian $P$-module, and its $P$-submodule $\tilde{A}$ is a finite $P$-module. A set of generators of $\tilde{A}$ over $P$ also generates $\tilde{A}$ over $A$, because $P \subseteq A$. Thus $\tilde{A}$ is a finite $A$-module. $\square$

**Corollary 2.3.5.** Let $k$ be a field of characteristic 0 and let $A$ be a domain that is a finitely generated $k$-algebra. Then the normalization $\tilde{A}$ is a finite $A$-module.

Node: SG00000026 · Lean: `Singularity.Algebra.finite_integralClosure_of_charZero`

*Proof.* By Theorem 2.2.1 there are elements $y_1, \dots, y_s \in A$, algebraically independent over $k$, such that $A$ is a finite module over $P = k[y_1, \dots, y_s]$. The ring $P$ is a polynomial ring. It is Noetherian by the Hilbert basis theorem [AM69, Corollary 7.6], and it is integrally closed by Example 2.1.5. The field $\operatorname{Frac} P$ has characteristic 0, so each algebraic extension of it is separable. By Step 1 of the proof of Theorem 2.3.4, $\operatorname{Frac} A$ is a finite extension of $\operatorname{Frac} P$, so it is separable. Theorem 2.3.4 gives the result. $\square$

When $k$ is perfect, one can choose the $y_i$ such that $\operatorname{Frac} A$ is separable over $k(y_1, \dots, y_s)$, because $\operatorname{Frac} A$ then has a separating transcendence basis [Mat, Theorem 26.2]. Then the same proof applies. Over a field that is not perfect, such a choice is not always possible. Section 2.4 gives a proof over each field that does not need this choice.

### The general case

E. Noether proved Corollary 2.3.5 over each field $k$. The statement is [Har, Chapter I, Theorem 3.9A], and the proof is in [Mat, Section 33] and [Stacks]. When $\operatorname{Frac} A$ is not separable over $\operatorname{Frac} P$, the trace form can be zero, and Theorem 2.3.3 does not apply. Section 2.4 proves the general case with the $q$-th roots of the coefficients and with the normal closure. It also proves Corollary 2.3.6 over each field.

### Application to curves

The finiteness theorem and Chapter 1 together resolve the singularities of an affine curve in characteristic 0.

**Corollary 2.3.6.** Let $k$ be a field of characteristic 0 and let $A$ be a domain that is a finitely generated $k$-algebra with $\dim A = 1$. Then $\tilde{A}$ is a finitely generated $k$-algebra, it is a finite $A$-module, and for each maximal ideal $\mathfrak{n}$ of $\tilde{A}$ the local ring $\tilde{A}_\mathfrak{n}$ is regular of dimension 1.

Node: SG00000027 · Lean: `Singularity.Curves.isDedekindDomain_integralClosure_of_charZero`

*Proof.* By Corollary 2.3.5, $\tilde{A}$ is a finite $A$-module. Thus it is a finitely generated $k$-algebra, and it is Noetherian by the Hilbert basis theorem. The extension $A \subseteq \tilde{A}$ is integral, so $\dim \tilde{A} = \dim A = 1$ (Section 2.1). Let $\mathfrak{n}$ be a maximal ideal of $\tilde{A}$ and let $R = \tilde{A}_\mathfrak{n}$. Then $R$ is a Noetherian local domain, and it is integrally closed because $\tilde{A}$ is integrally closed and integral closure commutes with localization (Section 2.1). Its dimension is the height of $\mathfrak{n}$, which is at most 1. The ideal $\mathfrak{n}$ is not $0$, because $\tilde{A}$ is not a field: a domain that is integral over $A$ and is a field makes $A$ a field [AM69, Proposition 5.7], and $\dim A = 1$. Thus $\dim R = 1$, and $R$ is regular by Theorem 1.4.2. $\square$

In the language of schemes, $\operatorname{Spec} \tilde{A}$ is a normal scheme of dimension 1, so it is regular by Corollary 1.4.3, and the morphism $\operatorname{Spec} \tilde{A} \to \operatorname{Spec} A$ is finite and birational. Volume 4 shows that this morphism is a resolution, and it glues the affine pieces to resolve each curve.

### The Lean proof

The Lean proof of Theorem 2.3.4 is `Singularity.Algebra.finite_integralClosure_of_finite` in the file `Singularity/Algebra/Normalization.lean` of `tamnd/singularity-lean`. The hypotheses are the Mathlib classes `Module.Finite P A`, `IsTorsionFree P A` for the injectivity of $P \to A$, and `Algebra.IsSeparable (FractionRing P) (FractionRing A)`. The proof follows the three steps above.

1. Step 1 is the Mathlib instance that makes `FractionRing A` a finite-dimensional vector space over `FractionRing P` when `A` is a finite torsion-free `P`-module.
2. Theorem 2.3.3 is `IsIntegralClosure.finite`, applied to the integral closure of `P` in `FractionRing A`. The Mathlib proof uses the trace form, as above.
3. Step 2 is `isIntegral_trans`. Step 3 is `isNoetherian_of_le` for the inclusion of submodules, and `Submodule.FG.of_restrictScalars` to go from generators over $P$ to generators over $A$.

The Lean proof of Corollary 2.3.5 is `Singularity.Algebra.finite_integralClosure_of_charZero`. It takes $P$ from `exists_finite_inj_algHom_of_fg`, makes $A$ a $P$-algebra with the map `g`, and obtains the separability from `Algebra.IsAlgebraic.isSeparable_of_perfectField`, since a field of characteristic 0 is perfect. Mathlib knows that a polynomial ring over a field is Noetherian, and that it is integrally closed because it is a unique factorization domain.

The Lean proof of Corollary 2.3.6 is `Singularity.Curves.isDedekindDomain_integralClosure_of_charZero` in the file `Singularity/Curves/Affine.lean`. It proves a slightly stronger statement: $\tilde{A}$ is a Dedekind domain, that is, a Noetherian integrally closed domain in which each nonzero prime ideal is maximal. The dimension hypothesis is the Mathlib class `Ring.DimensionLEOne A`, which says that each nonzero prime ideal of $A$ is maximal. The three parts of the proof above are `finite_integralClosure_of_charZero` with `IsNoetherianRing.of_finite`, the Mathlib theorem `integralClosure.isIntegrallyClosedOfFiniteExtension`, and the Mathlib instance that an integral extension of a ring of dimension at most 1 has dimension at most 1. Mathlib then knows that the localization of a Dedekind domain at a nonzero prime ideal is a discrete valuation ring, and so a regular local ring. The theorem `Singularity.Curves.isRegularRing_integralClosure_of_charZero` states this consequence.

### Notes and references

The finiteness of the normalization for finitely generated algebras is due to E. Noether. Rings $A$ for which the normalization of each finite extension domain is finite are the *Japanese rings* of Nagata [Nag62], and a Noetherian ring with this property for all its quotient domains is a *Nagata ring*. Fields, $\mathbb{Z}$, complete Noetherian local rings and the finitely generated algebras over them are Nagata rings [Mat, Section 32]. These rings are the right setting for the theory of excellent rings, which a later chapter of this volume treats.
