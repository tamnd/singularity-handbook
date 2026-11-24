---
title: The statement and the base
nodes: [SG00000004, SG0000001P, SG0000000D, SG0000001Z, SG0000001Y, SG00000020]
sources: [HirLean, Hir64, Kol07, FC, Mathlib, Har]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The statement and the base

This section gives the Lean form of Theorem 1.1.1 and the chain of Lean theorems that proves it. Volume 9, Sections 1.2 to 1.4, has the full mathematical proofs of the steps. Here we explain how the steps fit together, and how the Lean statement relates to the theorems of Chapter 1.

### The Lean statement

The library defines a resolution in the file `Singularity/Statements/Basic.lean` and the main statement in `Singularity/Statements/Main.lean`. We copy the two definitions.

```lean
structure IsResolution {X Y : Scheme.{u}} (π : Y ⟶ X) : Prop where
  regular : IsRegularScheme Y
  proper : IsProper π
  isIso_over : ∃ U : X.Opens, (U : Set X) = regularLocus X ∧ IsIso (π ∣_ U)
  dense : Dense (π.base ⁻¹' regularLocus X)

def ResolutionInDim (p n : ℕ) : Prop :=
  ∀ (k : Type u) [Field k] [CharP k p] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsVariety X f],
    topologicalKrullDim X ≤ n → ∃ (Y : Scheme.{u}) (π : Y ⟶ X), IsResolution π
```

**Definition 4.1.1 (the Lean form of resolution).** A morphism $\pi \colon Y \to X$ satisfies `IsResolution` if $Y$ is regular, $\pi$ is proper, the regular locus of $X$ is open and $\pi$ is an isomorphism over it, and the inverse image of the regular locus is dense in $Y$.

Node: SG00000004 · Lean: `Singularity.IsResolution`

The proposition `ResolutionInDim p n` says that each variety of dimension at most $n$ over a field of characteristic $p$ has a morphism that satisfies `IsResolution`. It is the Lean statement of node SG0000001P.

The four fields are the four conditions of Volume 0, Definition 2.1.5, and the definition of a resolution in Section 1.1 is the same. The class `IsVariety X f` says that $X$ is reduced and that $f$ is locally of finite type, quasi-compact and separated. So a variety in Lean is a variety in the sense of Section 1.1, and it need not be irreducible. The regular locus is the set of points whose local ring is a regular local ring in the sense of Mathlib [Mathlib]. The field $k$ is any field of characteristic $p$. For $p = 0$ the field is perfect, so regular and smooth have the same meaning for varieties over $k$, as in Section 1.1.

A variety over a field has finite dimension. Hence the statement $\forall n, \ \mathrm{ResolutionInDim}\ 0\ n$ is Theorem 1.1.1. The Lean form has the same content as Theorem 1.1.1, but it is weaker than the strong form, Theorem 1.1.3, in four ways.

1. It gives one proper morphism, not a composite of blowups with smooth centers.
2. It does not say that $\pi$ is projective.
3. It does not say that the inverse image of the singular locus is a divisor with simple normal crossings.
4. It does not say that the resolution is functorial, as in Theorem 1.1.8.

The note of node SG0000001P records this difference. The map has no node for Theorems 1.1.3 to 1.1.8.

### The base

The base states Main Theorem I in this form: for an integral variety $X$ over a field of characteristic 0, there is an ideal sheaf $D$ on $X$ whose support is the singular locus of $X$, such that the blowup of $X$ along $D$ is regular. This is Theorem 1.2.2 of Volume 9. Its Lean name is `AlgebraicGeometry.exists_support_eq_singularLocus_isRegular_blowUp`. That name is a declaration of the base, not of the library, so it has no result line in this handbook.

Hironaka's Main Theorem I in [Hir64] gives a sequence of blowups with regular centers. The base states the theorem with one ideal sheaf. The project does not use the proof in the base. It uses only the statement, together with three facts on blowups that the base proves: the blowup is proper over a locally Noetherian scheme, it is an isomorphism off the support of the center, and the inverse image of the center is an invertible ideal sheaf. These are the three parts of Volume 9, Proposition 1.2.1.

The part of the library that imports the base is a separate Lake package, `SingularityBase`, in the folder `base` of tamnd/singularity-lean. Its file `lakefile.toml` pins the base to one commit. The main package `Singularity` does not import the base. Thus each statement of the main package, and each proof that does not use characteristic 0, builds without the base.

### From the base to the statement

The library proves Theorem 1.1.1 in four steps. Each step is a Lean theorem with a node.

**Theorem 4.1.2 (the morphism of the base is a resolution).** Let $k$ be a field of characteristic 0 and let $X$ be an integral variety over $k$. Then $X$ has a resolution in the sense of Definition 4.1.1.

Node: SG0000001Z · Lean: `Singularity.Base.integralResolutionInDim_zero`

*Proof.* This is Volume 9, Theorem 1.2.5. Let $D$ be the ideal sheaf of Main Theorem I and let $\pi$ be the blowup along $D$. Then $Y$ is regular by Main Theorem I, and $\pi$ is proper and an isomorphism over $X \setminus \operatorname{supp} D = \operatorname{Reg}(X)$ by the facts on blowups above. The inverse image of $\operatorname{Reg}(X)$ is the complement of the exceptional divisor. The exceptional divisor is locally defined by one nonzerodivisor, so its complement is dense, by Volume 9, Lemma 1.2.4. $\square$

In Lean the theorem `Singularity.Base.exists_isResolution_of_isIntegral` proves the statement for one integral variety, with the hypothesis `CharZero k` of the base on the field. The theorem `Singularity.Base.integralResolutionInDim_zero` changes the hypothesis `CharP k 0` of the statement into `CharZero k`, and it proves the integral case of `ResolutionInDim 0 n` for each $n$, the proposition `Singularity.IntegralResolutionInDim 0 n`.

**Theorem 4.1.3 (reduction to integral varieties).** Let $p$ be $0$ or a prime and let $n \ge 0$. If each integral variety of dimension at most $n$ over a field of characteristic $p$ has a resolution, then each variety of dimension at most $n$ over a field of characteristic $p$ has a resolution.

Node: SG0000001Y · Lean: `Singularity.ReductionToIntegral`, `Singularity.Reduction.reductionToIntegral`

*Proof.* This is Volume 9, Theorem 1.3.1. Let $X_1, \dots, X_r$ be the irreducible components of $X$ with the reduced structure, and let $Y_i \to X_i$ be resolutions. Then the disjoint union of the $Y_i$ is a resolution of $X$. A regular local ring is a domain, so a regular point of $X$ lies on only one component, and the map is an isomorphism over $\operatorname{Reg}(X)$. Properness follows from the valuative criterion. $\square$

The theorem holds in each characteristic, and its proof is in the main package. The file that defines `ReductionToIntegral` cannot import the file of the proof. Thus the theorem `Singularity.resolutionInDim_zero` of the package `SingularityBase` takes the proposition as an argument, and the last step supplies the proof.

**Theorem 4.1.4 (Hironaka's theorem in Lean).** For each $n$, the proposition `ResolutionInDim 0 n` holds.

Node: SG0000000D · Lean: `Singularity.resolutionInDim_charZero`

*Proof.* Theorem 4.1.2 gives the integral case, and Theorem 4.1.3 for $p = 0$ gives the general case. $\square$

The same Lean theorem is the proof of node SG0000001P, Hironaka's theorem, whose Lean statement is `Singularity.ResolutionInDim`. It takes no hypothesis.

**Theorem 4.1.5 (the form of formal-conjectures).** Let $k$ be a field of characteristic 0 and let $X$ be an integral scheme that is separated and of finite type over $k$. Then $X$ has a resolution in the sense of google-deepmind/formal-conjectures [FC].

Node: SG00000020 · Lean: `Singularity.Bridge.FCResolutionCharZero`, `Singularity.Base.fcResolutionCharZero`

*Proof.* This is Volume 9, Corollary 1.4.2. In [FC] a resolution is a proper birational morphism from an integral smooth scheme. A resolution in the sense of Definition 4.1.1 of an integral variety over a perfect field has these properties, by Volume 9, Proposition 1.4.1. Apply this to the morphism of Theorem 4.1.2. $\square$

The converse fails: the blowup of a point of $\mathbb{A}^2$ is a resolution in the sense of [FC], but it is not an isomorphism over the regular locus (Volume 9, Example 1.4.3). So the statement of [FC] is weaker than Definition 4.1.1.

### What the Lean proof shows

The four theorems show that the statement of the base implies the statement of the project. They do not check the mathematics of Chapters 2 and 3. Those chapters give the proof of principalization, Theorem 3.3.11, with some steps cited from [Kol07, Chapter 3], and Section 1.2 deduces resolution from principalization. The Lean proof of Theorem 4.1.4 uses none of this. It gives one morphism, the blowup along the ideal sheaf $D$ of the base, and it forgets the extra properties of this morphism. For example, a blowup of a coherent ideal sheaf is projective over $X$ [Har, Section II.7], but the Lean statement does not record this.

### Notes and references

The definitions of this section are in the files `Singularity/Statements/Basic.lean`, `Singularity/Statements/Main.lean` and `Singularity/Hypotheses/Integral.lean` of tamnd/singularity-lean. The proofs of Theorems 4.1.2 and 4.1.4 are in `base/SingularityBase/CharZero.lean`, the proof of Theorem 4.1.3 is in `Singularity/Scheme/Reduction.lean`, and the proof of Theorem 4.1.5 is in `base/SingularityBase/Bridge.lean`. For the base and its Main Theorem I see [HirLean]. The comparison of Hironaka's theorem in [Hir64] with the modern proofs is in [Kol07, Chapter 3].
