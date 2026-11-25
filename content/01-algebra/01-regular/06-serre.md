---
title: The theorem of Serre and localization
nodes: [SG0000002J, SG0000002K, SG0000002M, SG0000000H]
sources: [Mat, Ser55, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem of Serre and localization

In this section we complete the theorem of Serre: a Noetherian local ring is regular if and only if its residue field has finite projective dimension. Then we use the theorem to prove that a localization of a regular local ring at a prime ideal is regular. The condition "regular" is a condition on the number of generators of one ideal, and it is not clear that it passes from $R$ to $R_\mathfrak{p}$. The condition "the residue field has finite projective dimension" is homological, and localization respects it. This is the reason for the homological detour.

Throughout the section, $(R, \mathfrak{m}, \kappa)$ is a Noetherian local ring and all modules are modules over $R$. For a finitely generated module $M$ we use a *presentation*: an exact sequence $0 \to K \to F \to M \to 0$ with $F$ free of finite rank. Since $R$ is Noetherian, $K$ is finitely generated.

### A test for freeness

We start with a test for freeness that uses only the residue field. Over a local ring, a finitely generated module $M$ is free if and only if the map $\kappa \otimes K \to \kappa \otimes F$ is injective for one presentation of $M$. This criterion contains the theorem that a finitely generated flat module over a local ring is free [Mat, Theorem 7.10], because the map is injective when $M$ is flat. In Lean this criterion is the Mathlib theorem `Module.free_of_lTensor_residueField_injective`.

**Lemma 1.6.1 (the Ext criterion).** Let $M$ be a finitely generated $R$-module and let $n \ge 0$. Then $\operatorname{pd}_R M \le n$ if and only if $\operatorname{Ext}^{n+1}_R(M, \kappa) = 0$.

Node: SG0000002J · Lean: `Singularity.Algebra.projectiveDimension_le_iff_subsingleton_ext`

*Proof.* If $\operatorname{pd}_R M \le n$, then $\operatorname{Ext}^{n+1}_R(M, N) = 0$ for each module $N$, because we can compute Ext with a projective resolution of length $n$. We prove the converse by induction on $n$.

Let $n = 0$, and assume that $\operatorname{Ext}^1_R(M, \kappa) = 0$. Take a presentation $0 \to K \xrightarrow{i} F \to M \to 0$. The long exact sequence of $\operatorname{Hom}_R(-, \kappa)$ contains the exact part
$$\operatorname{Hom}_R(F, \kappa) \to \operatorname{Hom}_R(K, \kappa) \to \operatorname{Ext}^1_R(M, \kappa) = 0.$$
Thus each $R$-linear map $g \colon K \to \kappa$ extends to a map $g' \colon F \to \kappa$ with $g' \circ i = g$. We show that $\kappa \otimes i \colon \kappa \otimes K \to \kappa \otimes F$ is injective. Let $t \in \kappa \otimes K$ with $(\kappa \otimes i)(t) = 0$, and let $\varphi \colon \kappa \otimes K \to \kappa$ be a $\kappa$-linear form. The map $g(y) = \varphi(1 \otimes y)$ is an $R$-linear map $K \to \kappa$. Let $g'$ be an extension of $g$, and let $\psi \colon \kappa \otimes F \to \kappa$ be the map $a \otimes z \mapsto a\, g'(z)$. Then $\varphi = \psi \circ (\kappa \otimes i)$, because the two maps agree on each $a \otimes y$. Thus $\varphi(t) = \psi(0) = 0$. A vector of the $\kappa$-vector space $\kappa \otimes K$ on which each linear form is zero is $0$, so $t = 0$. By the criterion above, $M$ is free, and $\operatorname{pd}_R M \le 0$.

Let $n \ge 1$, and assume the result for $n - 1$. Take a presentation $0 \to K \to F \to M \to 0$. Since $F$ is free, $\operatorname{Ext}^j_R(F, \kappa) = 0$ for $j \ge 1$, and the long exact sequence gives an isomorphism $\operatorname{Ext}^n_R(K, \kappa) \cong \operatorname{Ext}^{n+1}_R(M, \kappa)$. Thus $\operatorname{Ext}^n_R(K, \kappa) = 0$, and by the induction hypothesis $\operatorname{pd}_R K \le n - 1$. The presentation then gives $\operatorname{pd}_R M \le n$. $\square$

Lemma 1.6.1 is in [Mat, Section 19], where it is stated with Tor. Mathlib has the same criterion with $\operatorname{Ext}^{n+1}_R(M, N) = 0$ for all finitely generated $N$. The point of the lemma is that one test module, the residue field, is sufficient.

### Regular local rings have finite global dimension

**Lemma 1.6.2.** Let $x \in R$ be a nonzerodivisor, let $\bar{R} = R/(x)$, and let $N$ be a finitely generated $\bar{R}$-module. Then $\operatorname{pd}_R N \le \operatorname{pd}_{\bar{R}} N + 1$.

Lean: `Singularity.Algebra.hasProjectiveDimensionLT_of_quotient`

*Proof.* We use induction on $n = \operatorname{pd}_{\bar{R}} N$. As an $R$-module, $\bar{R}$ has the free resolution $0 \to R \xrightarrow{x} R \to \bar{R} \to 0$, because $x$ is a nonzerodivisor. Thus $\operatorname{pd}_R \bar{R}^m \le 1$ for each $m$.

Let $n = 0$. Then $N$ is a projective $\bar{R}$-module, so $N$ is a direct summand of some $\bar{R}^m$. A direct summand of a module of projective dimension at most $1$ has projective dimension at most $1$. Thus $\operatorname{pd}_R N \le 1$.

Let $n \ge 1$. Take an exact sequence $0 \to K \to \bar{R}^m \to N \to 0$ of $\bar{R}$-modules. Then $\operatorname{pd}_{\bar{R}} K = n - 1$, and by the induction hypothesis $\operatorname{pd}_R K \le n$. The same sequence is an exact sequence of $R$-modules, with $\operatorname{pd}_R \bar{R}^m \le 1 \le n + 1$. Thus $\operatorname{pd}_R N \le n + 1$. $\square$

**Theorem 1.6.3.** Let $R$ be a regular local ring of dimension $d$. Then $\operatorname{pd}_R M \le d$ for each finitely generated $R$-module $M$.

Node: SG0000002K · Lean: `Singularity.Algebra.projectiveDimension_le_ringKrullDim`

*Proof.* We use induction on $d$. If $d = 0$, then $\mathfrak{m} = 0$ and $R$ is a field. Each module over a field is free, so $\operatorname{pd}_R M \le 0$.

Let $d \ge 1$. Lemma 1.3.2 gives $x \in \mathfrak{m} \setminus \mathfrak{m}^2$. By Proposition 1.2.6, $\bar{R} = R/(x)$ is a regular local ring of dimension $d - 1$. By Theorem 1.3.3, $R$ is a domain, so $x$ is a nonzerodivisor. Take a presentation $0 \to K \to F \to M \to 0$. Then $K$ is a submodule of the free module $F$, so $x$ is a nonzerodivisor on $K$, and the sequence $0 \to K \xrightarrow{x} K \to K/xK \to 0$ is exact. By the induction hypothesis, $\operatorname{pd}_{\bar{R}} K/xK \le d - 1$. By Lemma 1.6.2, $\operatorname{pd}_R K/xK \le d$. By Lemma 1.5.5, $\operatorname{pd}_R K/xK = \operatorname{pd}_R K + 1$, so $\operatorname{pd}_R K \le d - 1$. The presentation then gives $\operatorname{pd}_R M \le d$. $\square$

With Theorem 1.5.6, the bound is sharp: $\operatorname{pd}_R \kappa = d$. Thus the global dimension of $R$ is $d$. This is the first half of the theorem of Serre.

### The converse

The converse needs more care, because we know nothing about $R$ except that $\operatorname{pd}_R \kappa < \infty$. We first treat the case in which $\mathfrak{m}$ consists of zero divisors in a strong sense.

**Lemma 1.6.4.** Assume that there is an element $s \ne 0$ of $R$ with $\mathfrak{m} s = 0$. Then each finitely generated $R$-module of finite projective dimension is free. If also $\operatorname{pd}_R \kappa < \infty$, then $\mathfrak{m} = 0$.

Lean: `Singularity.Algebra.free_of_hasProjectiveDimensionLT_of_socle`, `Singularity.Algebra.maximalIdeal_eq_bot_of_socle`

*Proof.* The map $R \to R$, $a \mapsto as$, has kernel $\mathfrak{m}$: the kernel contains $\mathfrak{m}$, and it does not contain a unit, because $s \ne 0$. Thus the map gives an injective $R$-linear map $j \colon \kappa \to R$.

Let $\varphi \colon K \to F$ be an injective map of free modules. In the square
$$\begin{array}{ccc} \kappa \otimes K & \xrightarrow{\kappa \otimes \varphi} & \kappa \otimes F \\ \downarrow & & \downarrow \\ R \otimes K & \xrightarrow{R \otimes \varphi} & R \otimes F \end{array}$$
the vertical maps are $j \otimes K$ and $j \otimes F$. They are injective, because free modules are flat. The lower map is $\varphi$, which is injective. The square commutes, so $\kappa \otimes \varphi$ is injective.

Now let $M$ be finitely generated with $\operatorname{pd}_R M = n < \infty$. We use induction on $n$. If $n = 0$, then $M$ is projective, and a finitely generated projective module over a local ring is free. Let $n \ge 1$, and take a presentation $0 \to K \to F \to M \to 0$. Then $\operatorname{pd}_R K = n - 1$, so $K$ is free by the induction hypothesis. By the square, $\kappa \otimes K \to \kappa \otimes F$ is injective, and the criterion before Lemma 1.6.1 shows that $M$ is free.

If $\operatorname{pd}_R \kappa < \infty$, then $\kappa$ is a free $R$-module. It is not zero, so it has a basis vector $b$. For $a \in \mathfrak{m}$ we have $ab = 0$ in $\kappa$, and the coordinate of $ab$ at $b$ is $a$. Thus $a = 0$, and $\mathfrak{m} = 0$. $\square$

The proof of [Mat, Theorem 19.2] uses a minimal free resolution of $\kappa$ at this step. The argument with the map $j$ is shorter, and it is the argument in the Lean proof.

**Lemma 1.6.5.** Assume that $\mathfrak{m} \ne 0$ and that no $s \ne 0$ has $\mathfrak{m} s = 0$. Then there is a nonzerodivisor $x \in \mathfrak{m} \setminus \mathfrak{m}^2$.

Lean: `Singularity.Algebra.exists_mem_maximalIdeal_notMem_sq_mem_nonZeroDivisors`

*Proof.* The set of zero divisors of the Noetherian ring $R$ is the union of the finitely many associated primes $\mathfrak{p}_1, \dots, \mathfrak{p}_k$ of $R$ [Mat, Theorem 6.1]. Each $\mathfrak{p}_i$ has the form $\operatorname{Ann}(s_i)$ with $s_i \ne 0$. If $\mathfrak{p}_i = \mathfrak{m}$, then $\mathfrak{m} s_i = 0$, which is false. Thus $\mathfrak{m} \not\subseteq \mathfrak{p}_i$ for each $i$. Also $\mathfrak{m}^2 \ne \mathfrak{m}$, by Nakayama's lemma, because $\mathfrak{m} \ne 0$. By Lemma 1.3.1, with $I_1 = \mathfrak{m}^2$, $\mathfrak{m}$ is not a subset of $\mathfrak{m}^2 \cup \mathfrak{p}_1 \cup \dots \cup \mathfrak{p}_k$. An element $x$ of $\mathfrak{m}$ outside this union is the required element. $\square$

The next lemma is a change of rings in the other direction from Lemma 1.6.2.

**Lemma 1.6.6.** Let $x \in R$ be a nonzerodivisor on $R$ and on a finitely generated module $M$, and let $\bar{R} = R/(x)$. Then $\operatorname{pd}_{\bar{R}} M/xM \le \operatorname{pd}_R M$.

Lean: `Singularity.Algebra.hasProjectiveDimensionLT_baseChange_quotient`

*Proof.* Note that $M/xM \cong \bar{R} \otimes M$. We use induction on $n = \operatorname{pd}_R M$. If $n = 0$, then $M$ is projective, and $\bar{R} \otimes M$ is a projective $\bar{R}$-module.

Let $n \ge 1$, and take a presentation $0 \to K \to F \to M \to 0$. The element $x$ is a nonzerodivisor on the free module $F$, so also on $K$, and $\operatorname{pd}_R K = n - 1$. By the induction hypothesis, $\operatorname{pd}_{\bar{R}} \bar{R} \otimes K \le n - 1$. The functor $\bar{R} \otimes -$ is right exact, so the sequence $\bar{R} \otimes K \to \bar{R} \otimes F \to \bar{R} \otimes M \to 0$ is exact. We show that the first map is injective. Let $y \in K$ with $y = xz$ for some $z \in F$. Then $x$ times the image of $z$ in $M$ is $0$. Since $x$ is a nonzerodivisor on $M$, the image of $z$ is $0$, so $z \in K$ and $y \in xK$. Thus $K/xK \to F/xF$ is injective. The sequence $0 \to \bar{R} \otimes K \to \bar{R} \otimes F \to \bar{R} \otimes M \to 0$ is exact, with $\bar{R} \otimes F$ free over $\bar{R}$, and so $\operatorname{pd}_{\bar{R}} \bar{R} \otimes M \le n$. $\square$

**Lemma 1.6.7.** Let $x \in \mathfrak{m} \setminus \mathfrak{m}^2$ and let $\bar{R} = R/(x)$, with residue field $\kappa$. Then $\kappa$ is a direct summand of the $\bar{R}$-module $\mathfrak{m}/x\mathfrak{m}$.

Lean: part of `Singularity.Algebra.hasProjectiveDimensionLT_residueField_quotient`

*Proof.* The class of $x$ in the $\kappa$-vector space $\mathfrak{m}/\mathfrak{m}^2$ is not zero. Thus there is a $\kappa$-linear form on $\mathfrak{m}/\mathfrak{m}^2$ with value $1$ at this class. With the map $\mathfrak{m} \to \mathfrak{m}/\mathfrak{m}^2$, it gives an $R$-linear map $g \colon \mathfrak{m} \to \kappa$ with $g(x) = 1$. Since $x\mathfrak{m} \subseteq \mathfrak{m}^2$, the map $g$ is zero on $x\mathfrak{m}$, and it gives an $\bar{R}$-linear map $r \colon \mathfrak{m}/x\mathfrak{m} \to \kappa$.

Let $i \colon \kappa \to \mathfrak{m}/x\mathfrak{m}$ be the map $\bar{a} \mapsto ax$. It is well defined, because $\mathfrak{m} x \subseteq x\mathfrak{m}$. Then $r(i(\bar{a})) = g(ax) = \bar{a}\, g(x) = \bar{a}$. Thus $r \circ i$ is the identity, and $\kappa$ is a direct summand. $\square$

**Theorem 1.6.8 (Serre).** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring. Then $R$ is regular if and only if $\operatorname{pd}_R \kappa < \infty$.

Node: SG0000002M · Lean: `Singularity.Algebra.isRegularLocalRing_of_hasProjectiveDimensionLT`

*Proof.* If $R$ is regular, then $\operatorname{pd}_R \kappa = \dim R$ by Theorem 1.5.6. We prove the converse by induction on $e = \operatorname{edim} R = \mu(\mathfrak{m})$.

If $\mathfrak{m} = 0$, then $R$ is a field, and a field is regular. Assume that $\mathfrak{m} \ne 0$. By Lemma 1.6.4, no $s \ne 0$ has $\mathfrak{m} s = 0$. Lemma 1.6.5 gives a nonzerodivisor $x \in \mathfrak{m} \setminus \mathfrak{m}^2$. Let $\bar{R} = R/(x)$.

The sequence $0 \to \mathfrak{m} \to R \to \kappa \to 0$ is exact, and $R$ is free, so $\operatorname{pd}_R \mathfrak{m} < \infty$. The element $x$ is a nonzerodivisor on $R$, so also on the ideal $\mathfrak{m}$. By Lemma 1.6.6, $\operatorname{pd}_{\bar{R}} \mathfrak{m}/x\mathfrak{m} < \infty$. By Lemma 1.6.7, the residue field $\kappa$ of $\bar{R}$ is a direct summand of $\mathfrak{m}/x\mathfrak{m}$, so $\operatorname{pd}_{\bar{R}} \kappa < \infty$.

By Lemma 1.1.5, $\operatorname{edim} \bar{R} = e - 1$. By the induction hypothesis, $\bar{R}$ is regular. Since $x$ is a nonzerodivisor in $\mathfrak{m}$, Proposition 1.2.8 shows that $R$ is regular. $\square$

### Localization

**Corollary 1.6.9.** Let $R$ be a regular local ring and let $\mathfrak{p}$ be a prime ideal of $R$. Then $R_\mathfrak{p}$ is a regular local ring.

Node: SG0000000H · Lean: `Singularity.Algebra.isRegularLocalRing_localization`

*Proof.* Let $d = \dim R$. By Theorem 1.6.3, $\operatorname{pd}_R R/\mathfrak{p} \le d$. Localization is exact and it sends free $R$-modules to free $R_\mathfrak{p}$-modules, so it sends a projective resolution of $R/\mathfrak{p}$ of length $d$ to a projective resolution of $(R/\mathfrak{p})_\mathfrak{p}$ over $R_\mathfrak{p}$. Thus $\operatorname{pd}_{R_\mathfrak{p}} (R/\mathfrak{p})_\mathfrak{p} \le d$.

The module $(R/\mathfrak{p})_\mathfrak{p}$ is the residue field $\kappa(\mathfrak{p})$ of $R_\mathfrak{p}$. Indeed, $R/\mathfrak{p}$ is a domain, and the image of $R \setminus \mathfrak{p}$ in $R/\mathfrak{p}$ is the set of nonzero elements. So $(R/\mathfrak{p})_\mathfrak{p}$ is the field of fractions of $R/\mathfrak{p}$, and this field is $R_\mathfrak{p}/\mathfrak{p}R_\mathfrak{p} = \kappa(\mathfrak{p})$. Thus the residue field of the Noetherian local ring $R_\mathfrak{p}$ has finite projective dimension, and $R_\mathfrak{p}$ is regular by Theorem 1.6.8. $\square$

**Example 1.6.10.** Let $k$ be a field, let $R = k[x, y]_{(x, y)}$, and let $\mathfrak{p} = (y)$. Then $R_\mathfrak{p}$ is the local ring of the plane at the generic point of the line $y = 0$. Its maximal ideal is generated by $y$, and $\dim R_\mathfrak{p} = 1$, so $R_\mathfrak{p}$ is regular, as Corollary 1.6.9 says. In this example we can see the result directly. In general we cannot, because a regular system of parameters of $R$ does not give generators of $\mathfrak{p}R_\mathfrak{p}$.

For a scheme, Corollary 1.6.9 says that the regular points are closed under generization: if $x$ is a regular point of a locally Noetherian scheme $X$ and $y$ is a point with $x$ in the closure of $y$, then $y$ is a regular point. The reason is that $\mathcal{O}_{X,y}$ is a localization of $\mathcal{O}_{X,x}$ at a prime ideal. This is the first step to the openness of the regular locus, which is the subject of Section 1.7 and of the node SG0000000K.

### The Lean proof

The Ext criterion is in `Singularity/Algebra/ExtCriterion.lean`. The extension of the maps $K \to \kappa$ comes from the Mathlib lemma `Ext.contravariant_sequence_exact₁`, and the injectivity of $\kappa \otimes K \to \kappa \otimes F$ is the theorem `Singularity.Algebra.lTensor_residueField_injective_of_forall_extend`.

Lemma 1.6.2 and Theorem 1.6.3 are in `Singularity/Algebra/GlobalDimension.lean`. The induction in Theorem 1.6.3 quantifies over all regular local rings of dimension $d$, as in the proof of Theorem 1.3.3.

The converse is in `Singularity/Algebra/SerreConverse.lean`. The main theorem `Singularity.Algebra.isRegularLocalRing_of_spanFinrank_le` is the induction on $e$. The injectivity in Lemma 1.6.6 uses the Mathlib lemma `lTensor_injective_of_exact_of_exact_of_rTensor_injective` for the two right exact sequences $R \xrightarrow{x} R \to \bar{R} \to 0$ and $K \to F \to M \to 0$, in place of the element argument above. The direct summand of Lemma 1.6.7 is a `Retract` in the category of $\bar{R}$-modules, and the module $\mathfrak{m}/x\mathfrak{m}$ is $\bar{R} \otimes_R \mathfrak{m}$.

The two directions of Theorem 1.6.8 together are the theorem `Singularity.Algebra.isRegularLocalRing_iff_exists_hasProjectiveDimensionLT`. Corollary 1.6.9 is in `Singularity/Algebra/RegularLocalization.lean`. The localization step is the Mathlib lemma `ModuleCat.localizedModule_hasProjectiveDimensionLE`. The identification $(R/\mathfrak{p})_\mathfrak{p} \cong \kappa(\mathfrak{p})$ uses the Mathlib instance `IsFractionRing (R ⧸ I) I.ResidueField`, and the uniqueness of localizations, `IsLocalizedModule.iso`. All the theorems of this section use only the three standard axioms of Lean.

### Notes and references

The theorem of Serre is [Ser55] and [Mat, Theorem 19.2], and Corollary 1.6.9 is [Mat, Theorem 19.3]. Auslander and Buchsbaum proved the same characterization at the same time. Before this theorem, the localization of a regular local ring was known only in special cases, for example for the local rings of a variety over a perfect field, where the Jacobian criterion applies. The proof of Lemma 1.6.4 with an embedding $\kappa \to R$ follows the idea of the proof of [Mat, Theorem 19.2] but avoids minimal resolutions. Corollary 1.6.9 is not sufficient to prove that the regular locus is open. For an excellent scheme, for example a scheme of finite type over a field, the openness is a further theorem, and it is the subject of the node SG0000000K.
