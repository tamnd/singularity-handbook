---
title: Dimension 0
nodes: [SG0000001W, SG0000000A]
sources: [AM69, Mat, Har, Liu, Stacks, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Dimension 0

In dimension 0 there is nothing to resolve. A reduced scheme of dimension 0 is already regular, so its identity morphism is a resolution. The proof is short, but it uses each part of the definition of a resolution, and it shows why the definition asks for a reduced scheme and for a regular scheme, not a smooth one. This makes it a good first example.

**Theorem 1.1.1 (resolution in dimension 0).** Let $p$ be $0$ or a prime. Then $\mathrm{Res}(p, 0)$ holds. More exactly, let $X$ be a reduced scheme with $\dim X \le 0$. Then $X$ is regular, and the identity $\mathrm{id}_X : X \to X$ is a resolution of $X$.

Node: SG0000001W · Lean: `Singularity.resolutionInDim_dim_zero`

The second form of the theorem is stronger than the first. It does not ask that $X$ is of finite type over a field, and it does not use the characteristic. We prove it in four steps.

### Step 1: the local rings have dimension 0

**Lemma 1.1.2.** Let $X$ be a scheme and let $x \in X$. Then $\dim \mathcal{O}_{X,x} \le \dim X$. In particular, if $\dim X \le 0$, then each local ring of $X$ has dimension 0.

Lean: `Singularity.krullDimLE_zero_stalk`

*Proof.* Let $U = \operatorname{Spec} A$ be an affine open set that contains $x$, and let $\mathfrak{q} \subset A$ be the prime ideal of $x$. Then $\mathcal{O}_{X,x} = A_{\mathfrak{q}}$. The prime ideals of $A_{\mathfrak{q}}$ are the ideals $\mathfrak{p} A_{\mathfrak{q}}$ for the prime ideals $\mathfrak{p} \subseteq \mathfrak{q}$ of $A$ [AM69, Corollary 3.13]. Thus a chain $\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \dots \subsetneq \mathfrak{p}_d$ of prime ideals of $A_{\mathfrak{q}}$ gives a chain of prime ideals of $A$ in $\mathfrak{q}$ of the same length. The closures of the corresponding points of $U$ are irreducible closed subsets $Z_d \subsetneq \dots \subsetneq Z_0$ of $U$. Their closures in $X$ are irreducible closed subsets of $X$, and they are still distinct, because $\overline{Z_i} \cap U = Z_i$. Thus $X$ has a chain of irreducible closed subsets of length $d$, and $d \le \dim X$. $\square$

In the language of order theory, $\dim \mathcal{O}_{X,x}$ is the *coheight* of $x$ in the specialization order of $X$: the supremum of the lengths of the chains of points $x_0 \rightsquigarrow x_1 \rightsquigarrow \dots \rightsquigarrow x_d = x$ in which each point is a proper generalization of the next. The proof above shows that the coheight of a point is at most the length of the longest chain in the whole space. The Lean proof uses this form.

### Step 2: a reduced local ring of dimension 0 is a field

**Lemma 1.1.3.** Let $(R, \mathfrak{m})$ be a local ring. If $R$ is reduced and $\dim R = 0$, then $R$ is a field.

Lean: `Ring.KrullDimLE.isField_of_isReduced` (in Mathlib)

*Proof.* Since $\dim R = 0$, each prime ideal of $R$ is maximal. Since $R$ is local, it has only one maximal ideal. Thus $\mathfrak{m}$ is the only prime ideal of $R$. The nilradical of $R$ is the intersection of the prime ideals of $R$ [AM69, Proposition 1.8], so it is equal to $\mathfrak{m}$. Since $R$ is reduced, the nilradical is $0$. Thus $\mathfrak{m} = 0$. In a local ring each element outside $\mathfrak{m}$ is a unit, so each nonzero element of $R$ is a unit, and $R$ is a field. $\square$

The two hypotheses are necessary. The ring $\mathbb{Z}_{(p)}$ is a reduced local ring of dimension 1, and it is not a field. The ring $k[\varepsilon]/(\varepsilon^2)$ is a local ring of dimension 0, and it is not a field. We come back to the second ring in Example 1.1.6.

### Step 3: a field is a regular local ring

Recall that a Noetherian local ring $(R, \mathfrak{m}, \kappa)$ is *regular* when $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = \dim R$ [Mat, Section 14]. The left side is the *embedding dimension* of $R$. By Nakayama's lemma it is the least number of generators of $\mathfrak{m}$, and it is always at least $\dim R$.

**Lemma 1.1.4.** A field $K$ is a regular local ring of dimension 0.

Lean: `Singularity.isRegularLocalRing_of_isField`

*Proof.* A field is Noetherian and local, with maximal ideal $\mathfrak{m} = 0$. Its only prime ideal is $0$, so $\dim K = 0$. The quotient $\mathfrak{m}/\mathfrak{m}^2$ is $0$, so the embedding dimension is $0$. The two numbers are equal. $\square$

### Step 4: the identity is a resolution

**Proposition 1.1.5.** Let $X$ be a regular scheme. Then $\mathrm{id}_X$ is a resolution of $X$.

Node: SG0000000A · Lean: `Singularity.Fidelity.isResolution_id`

*Proof.* We examine the four conditions. The source $X$ is regular by hypothesis. An isomorphism is proper. Since $X$ is regular, $\operatorname{Reg}(X) = X$. This set is open, and $\mathrm{id}_X$ is an isomorphism over it. Its inverse image is $X$, which is dense in $X$. $\square$

*Proof of Theorem 1.1.1.* Let $x \in X$. By Lemma 1.1.2, $\dim \mathcal{O}_{X,x} = 0$. The scheme $X$ is reduced, so the local ring $\mathcal{O}_{X,x}$ is reduced. By Lemma 1.1.3 it is a field, and by Lemma 1.1.4 it is a regular local ring. Thus $X$ is regular, and Proposition 1.1.5 gives the resolution.

For the first form, let $X$ be a variety of dimension at most 0 over a field $k$ of characteristic $p$. A variety is reduced by definition, so the second form applies. $\square$

### Examples

The first example shows that the theorem is false without the hypothesis that $X$ is reduced.

**Example 1.1.6 (a fat point).** Let $k$ be a field and let $X = \operatorname{Spec} k[\varepsilon]/(\varepsilon^2)$. Then $X$ is one point, so $\dim X = 0$. Its local ring $R = k[\varepsilon]/(\varepsilon^2)$ has the maximal ideal $\mathfrak{m} = (\varepsilon)$, and $\mathfrak{m}^2 = 0$. Thus $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 1 \ne 0 = \dim R$, and $R$ is not regular. The scheme $X$ is not a variety in our sense, because it is not reduced. The problem of resolution is a problem about reduced schemes, and the statement of the project says so.

The second example shows that *regular* is the correct word in the statement, and *smooth* is not.

**Example 1.1.7 (regular, but not smooth).** Let $p$ be a prime, let $k = \mathbb{F}_p(t)$, and let $K = k[u]/(u^p - t)$. The polynomial $u^p - t$ is irreducible over $k$, because $t$ is not a $p$-th power in $k$. Thus $K$ is a field, and $X = \operatorname{Spec} K$ is a variety of dimension 0 over $k$. By Theorem 1.1.1, $X$ is regular. But $X$ is not smooth over $k$. Let $s = t^{1/p} \in K$ be the class of $u$. Then
$$K \otimes_k K \cong K[u]/(u^p - t) = K[u]/((u - s)^p),$$
and the class of $u - s$ is a nonzero nilpotent element. Thus $X \times_k X$ is not reduced, and so $X$ is not geometrically reduced. A smooth scheme over $k$ is geometrically reduced, so $X$ is not smooth [Liu, Section 4.3].

Over a perfect field the two notions agree for varieties, and over an imperfect field they do not. A statement that asks for a smooth $Y$ would ask for a resolution of the regular variety $X$ of Example 1.1.7 that does not exist: each $Y \to X$ that is an isomorphism over $X$ is $X$ itself. This is why the project uses regular schemes (Volume 0, Section 2.4).

**Example 1.1.8 (several points).** Let $k$ be a field and let $X = \operatorname{Spec}(k \times k \times k)$. Then $X$ is three points, each with the local ring $k$. It is reduced and of dimension 0, so it is regular, and $\mathrm{id}_X$ is a resolution. A variety need not be irreducible, and Theorem 1.1.1 does not ask for it.

### The Lean proof

The Lean proof is in the file `Singularity/Known/DimZero.lean` of `tamnd/singularity-lean`. It has four declarations, one for each step.

```lean
lemma isRegularLocalRing_of_isField {R : Type*} [CommRing R] (h : IsField R) :
    IsRegularLocalRing R

lemma krullDimLE_zero_stalk {X : Scheme.{u}} (h : topologicalKrullDim X ≤ 0) (x : X) :
    Ring.KrullDimLE 0 (X.presheaf.stalk x)

theorem isRegularScheme_of_topologicalKrullDim_le_zero {X : Scheme.{u}} [IsReduced X]
    (h : topologicalKrullDim X ≤ 0) : IsRegularScheme X

theorem resolutionInDim_dim_zero (p : ℕ) : ResolutionInDim.{u} p 0
```

The first lemma is Lemma 1.1.4. In Mathlib, `IsField R` is a property of a ring, and `Field` is a structure. The proof makes a `Field` structure from `h` and then finds the Mathlib instance that a field is a regular local ring.

The second lemma is Lemma 1.1.2 in the form of order theory. Mathlib has the equality $\dim \mathcal{O}_{X,x} = \operatorname{coheight}(x)$ as `ringKrullDim_stalk_eq_coheight`. The Krull dimension of a topological space in Mathlib is the length of the longest chain of irreducible closed subsets. The map $x \mapsto \overline{\{x\}}$ is an order isomorphism from the points of a sober space to its irreducible closed subsets. The proof moves the coheight along this isomorphism with `coheight_orderIso`, and it bounds the coheight by the dimension with `coheight_le_krullDim`.

The third declaration is Steps 2 and 3. For each point $x$ it takes the bound of the second lemma, uses the Mathlib lemma `Ring.KrullDimLE.isField_of_isReduced` (this is Lemma 1.1.3), and then applies the first lemma.

The theorem is the first form of Theorem 1.1.1. It takes a field, a variety and the bound on the dimension, and it gives the pair $(X, \mathrm{id}_X)$ with the proof `Fidelity.isResolution_id` of Proposition 1.1.5. The statement of `ResolutionInDim` bounds the dimension by a natural number, and Mathlib measures dimension in $\mathbb{N} \cup \{\pm\infty\}$. The tactic `exact_mod_cast` moves the bound from one to the other.

The record of the Lean build lists the axioms of each theorem. For `resolutionInDim_dim_zero` they are `propext`, `Classical.choice` and `Quot.sound`, the three standard axioms of Lean and Mathlib.

### Notes and references

Lemma 1.1.3 is a standard exercise. It is the case $\dim R = 0$ of the more general fact that a reduced Noetherian ring of dimension 0 is a finite product of fields. Example 1.1.7 is the simplest example of a regular variety that is not smooth. Such varieties exist only over imperfect fields. For the relation between regular and smooth, see [Liu, Sections 4.2 and 4.3] and [Stacks]. The main difficulty of the problem begins in dimension 1, where a local ring of positive dimension can fail to be regular, and a resolution must change the scheme. Volume 1, Chapter 2 treats curves, and Volume 4 treats surfaces.
