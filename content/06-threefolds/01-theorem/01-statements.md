---
title: The theorems
nodes: [SG0000001D, SG0000001V, SG0000001F, SG0000001C]
sources: [Abh56s, Abh66, Cut09, CP08, CP09, CP19, Zar40, Zar44, Lip78, CJS20, Kol20, BMP20, Hau10, Cos87, Moh96, Hir64, Nag62, EGA4-7, dJ96, Tem13]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorems

In this section we state the theorems on the resolution of threefolds in characteristic $p > 0$, in the order in which they were proved. We prove nothing here. The proofs are long. The proof of Abhyankar fills a book and several papers, and each of the papers of Cossart and Piltant is long too. The later sections of this volume explain the main ideas of the proofs, and they prove the steps that fit in a textbook.

*Motivation.* In characteristic 0 each variety has a resolution, by the theorem of Hironaka [Hir64]. Many results use a resolution: the computation of cohomology, the definition of invariants of singularities, and the construction of regular models are examples. In characteristic $p > 0$ the proof of Hironaka does not work. The main reason is the failure of maximal contact, which Section 1.2 explains. So the dimensions in which resolution is known in characteristic $p$ are a basic limit for many methods. At present this limit is dimension 3. Resolution of varieties of dimension 4 in characteristic $p$ is open. This section states what is known in dimension 3, and it says which hypotheses each theorem needs.

The three theorems below have different strengths. The theorem of Abhyankar is the first result, with conditions on $p$ and on the variety. The theorems of Cossart and Piltant remove these conditions, and the last one also treats arithmetic schemes. The theorem on local uniformization is the local statement from which the others come. A reader who wants only the statements can read this section and Section 4.2. A reader who wants the proofs should continue with Section 1.2, which gives the plan of each proof.

### Resolution

We use the definition of a resolution of Volume 0, Definition 2.1.5. A *resolution* of a scheme $X$ is a proper morphism $\pi \colon Y \to X$ with $Y$ regular, which is an isomorphism over the regular locus $\operatorname{Reg}(X)$, such that $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$. For a prime $p$ and $n \ge 0$, the statement $\mathrm{Res}(p, n)$ of Volume 0, Definition 2.2.1, says that each variety of dimension at most $n$ over a field of characteristic $p$ has a resolution. A *threefold* is a variety of dimension 3.

The resolution of curves is classical: the normalization of a curve is regular (Volume 1, Theorem 2.5.6). The resolution of surfaces is Theorem 2.2.1 of Volume 4, the theorem of Lipman [Lip78]. Before Lipman, Abhyankar had proved the resolution of algebraic surfaces in characteristic $p$, through the local uniformization of surfaces [Abh56s]. In dimension 3 the first result is again due to Abhyankar.

### The theorem of Abhyankar

**Theorem 1.1.1 (Abhyankar).** Let $k$ be an algebraically closed field of characteristic $p$ with $p \ne 2, 3, 5$, and let $V$ be a projective variety of dimension 3 over $k$. Then there are a nonsingular projective variety $W$ and a birational morphism $\varphi \colon W \to V$ that is an isomorphism over the nonsingular locus of $V$.

Lean: none yet

The proof is in the book [Abh66] on the embedded resolution of surfaces and in several papers of Abhyankar [Cut09]. We state the theorem in the form of [Cut09, Theorem 1.1], which keeps the hypotheses of Abhyankar. Cutkosky writes that the proof of Abhyankar has 508 pages. The hardest part is the embedded resolution of surfaces in a nonsingular threefold, which Section 1.2 states as Theorem 1.2.2.

Cutkosky gave a new proof of Theorem 1.1.1 in [Cut09]. His proof is much shorter than the proof of Abhyankar. Cutkosky writes that it could have been written in 1967, as it uses only methods known at that time. For the embedded resolution of surfaces it follows the algorithm of Levi, with the invariant of Hironaka and the weak transform of an ideal instead of the strict transform. Section 1.2 gives the plan.

*Remark (the hypotheses of Theorem 1.1.1).* The proofs of [Abh66] and [Cut09] are written under these hypotheses, and each hypothesis has a visible role in the plan of Section 1.2.

1. *The condition on $p$.* The field has characteristic $p \ge 7$. Theorem 1.2.1 gives a projective model whose points have multiplicity at most $3! = 6$, and Step 3 of Section 1.2 resolves a point of multiplicity $m$ only when $m < p$. So the method needs $6 < p$. For $p \in \{2, 3, 5\}$ a point of multiplicity $m$ with $p \le m \le 6$ can remain on the model of Theorem 1.2.1. Then $m! = 0$ in $k$, and Proposition 1.2.5 does not apply. For $m = p$ Example 2.3.5 shows that no regular hypersurface can replace it.
2. *The field.* The field is algebraically closed. The constructions of Theorem 1.2.1 use projections from points and general linear subspaces of a projective space, and the local arguments of Step 3 use rational points and the Jacobian criterion over a perfect field. Theorem 1.1.2 shows that the result holds over each field, but its proof is different.
3. *Projectivity.* The variety is projective, because Theorem 1.2.1 works with an embedding in a projective space, and the patching of Step 4 works with projective models, as in the method of Zariski. For a variety that is not projective, Theorem 1.1.3 gives a resolution, and by the lemma of Chow each variety is birational to a projective one.

The conclusion of Theorem 1.1.1 does not say that $\varphi$ is a sequence of blowups in regular centers, and it does not give an embedded resolution.

### The theorems of Cossart and Piltant

Cossart and Piltant removed the conditions on $p$ and on the field. Their first two papers [CP08, CP09] treat threefolds over a field $k$ of characteristic $p > 0$ with $[k : k^p] < \infty$. A perfect field has this property, and so does a finitely generated extension of a perfect field. For such a field they prove the resolution of each quasi-projective threefold [CP09]. Their third paper [CP19] removes the condition on the field, and it also treats the arithmetic case.

**Theorem 1.1.2 (Cossart-Piltant).** Let $p$ be a prime. Each variety of dimension at most 3 over a field of characteristic $p$ has a resolution. That is, $\mathrm{Res}(p, 3)$ holds for each $p$.

Node: SG0000001D · Lean: `Singularity.ResolutionInDim` (the statement only)

For a quasi-projective variety over a field $k$ with $[k : k^p] < \infty$, the theorem is the main result of [CP08, CP09]. For an arbitrary field of characteristic $p$, it is a case of the next theorem, since a variety is quasi-excellent.

**Theorem 1.1.3 (Cossart-Piltant).** Let $X$ be a reduced separated Noetherian scheme that is quasi-excellent and has dimension at most 3. Then there is a proper birational morphism $\pi \colon X' \to X$ with these properties.

1. $X'$ is regular.
2. $\pi$ induces an isomorphism $\pi^{-1}(\operatorname{Reg} X) \to \operatorname{Reg} X$.
3. $\pi^{-1}(\operatorname{Sing} X)$ is a strict normal crossings divisor on $X'$.

If a finite affine cover $X = U_1 \cup \dots \cup U_n$ is given, then one can choose $\pi$ such that each $\pi^{-1}(U_i) \to U_i$ is projective.

Node: SG0000001V · Lean: `Singularity.resolution_quasiExcellent_three` (planned, no Lean statement yet)

This is [CP19, Theorem 1.1]. The theorem makes no hypothesis on the characteristic. It covers varieties over each field, and also schemes of mixed characteristic, for example schemes of finite type over $\mathbb{Z}$ or over an excellent discrete valuation ring of mixed characteristic. A morphism with properties 1 and 2 is a resolution in the sense of Volume 0, because $\pi$ is birational and $X$ is reduced.

*Remark (the hypotheses of Theorem 1.1.3).* We explain why each hypothesis is there.

1. *Reduced.* A regular scheme is reduced. If $X$ is not reduced, a morphism from a regular scheme factors through $X_{\mathrm{red}}$, so it cannot be an isomorphism over a dense open subset of $X$ unless $X$ is reduced there. One resolves $X_{\mathrm{red}}$ instead.
2. *Quasi-excellent.* This hypothesis is necessary in a precise sense. Let $X$ be integral, and let $\pi \colon X' \to X$ be proper and birational with $X'$ regular. Then $X'$ is normal and integral, and $\pi_* \mathcal{O}_{X'}$ is a coherent sheaf of $\mathcal{O}_X$-algebras, because $\pi$ is proper. Its sections over an affine open set $U$ are the ring $\mathcal{O}_{X'}(\pi^{-1} U)$, which is integrally closed in the function field and contains $\mathcal{O}_X(U)$. So it contains the integral closure of $\mathcal{O}_X(U)$, and the integral closure is a submodule of a finite module over a Noetherian ring. Thus the normalization of $X$ is finite over $X$. Nagata gives Noetherian local domains whose normalization is not finite [Nag62], and for them no such $\pi$ exists. Grothendieck shows more: if each integral scheme that is finite over $X$ has a resolution, then $X$ is quasi-excellent [EGA4-7, Section 7.9].
3. *Separated and Noetherian.* These are the standard finiteness conditions. The proof works with finite affine covers, and the statement on the projective morphisms $\pi^{-1}(U_i) \to U_i$ refers to such a cover.
4. *Dimension at most 3.* The proof uses dimension 3 at many places (Chapter 4). In dimension 4 the statement is open, also for varieties over an algebraically closed field.

The theorem gives more than a resolution: by property 3 the exceptional locus is a strict normal crossings divisor. This is what one needs for applications to regular models, as in Corollary 1.1.5.

Two consequences are stated in [CP19].

**Corollary 1.1.4.** Let $A$ be a reduced complete Noetherian local ring of dimension 3. Then $\operatorname{Spec} A$ has a projective resolution $\pi$ such that $\pi^{-1}(\operatorname{Sing} \operatorname{Spec} A)$ is a strict normal crossings divisor.

Lean: none yet

**Corollary 1.1.5.** Let $\mathcal{O}$ be an excellent Dedekind domain with fraction field $F$, and let $\Sigma$ be a regular projective surface over $F$. Then there is a proper flat $\mathcal{O}$-scheme $\mathcal{X}$ with generic fiber $\Sigma$ such that $\mathcal{X}$ is regular.

Lean: none yet

These are [CP19, Corollary 1.2] and [CP19, Corollary 1.3]. Corollary 1.1.4 follows because a complete local ring is excellent. Corollary 1.1.5 follows because a projective model of $\Sigma$ over $\mathcal{O}$ is quasi-excellent of dimension 3.

*Proof sketch of the corollaries.* For Corollary 1.1.4, the scheme $X = \operatorname{Spec} A$ is affine, so we may take the cover with one set $U_1 = X$. Theorem 1.1.3 gives $\pi$ with $\pi$ projective, $X'$ regular and $\pi^{-1}(\operatorname{Sing} X)$ a strict normal crossings divisor. For Corollary 1.1.5, choose a projective embedding of $\Sigma$ in $\mathbb{P}^N_F$, and let $\mathcal{X}_0$ be the closure of $\Sigma$ in $\mathbb{P}^N_{\mathcal{O}}$. It is integral, projective and flat over $\mathcal{O}$, because it has no component in a closed fiber. It has dimension $1 + 2 = 3$, and it is of finite type over the excellent ring $\mathcal{O}$, so it is excellent. Theorem 1.1.3 with a finite affine cover gives a regular $\mathcal{X}$ with a projective morphism to $\mathcal{X}_0$ over each set of the cover. Since $\Sigma$ is regular, $\pi$ is an isomorphism over $\Sigma$, so the generic fiber is $\Sigma$. A morphism $\mathcal{X} \to \mathcal{X}_0$ that is projective over each set of an affine cover is proper, so $\mathcal{X}$ is proper over $\mathcal{O}$. It is flat, since $\mathcal{X}$ is integral and dominates $\operatorname{Spec} \mathcal{O}$ and $\mathcal{O}$ is a Dedekind domain.

### The method of Zariski

The proof of Cossart and Piltant follows the method that Zariski used in characteristic 0 for surfaces and threefolds [Zar40, Zar44]. First one proves local uniformization along each valuation. Then one patches the local solutions. Volume 3, Chapter 4 defines local uniformization and explains the first part of the patching.

**Theorem 1.1.6 (Cossart-Piltant).** Let $K$ be a function field of transcendence degree 3 over a field $k$ of characteristic $p > 0$. Each valuation of $K$ over $k$ has local uniformization.

Node: SG0000001F · Lean: `Singularity.localUniformization_three` (the statement only)

This is Theorem 4.1.5 of Volume 3 and Theorem 2.1.5 of Volume 9. Chapter 2 of this volume explains how Cossart and Piltant reduce it to two kinds of equations of degree $p$, and Chapter 3 gives the invariants that they use for these equations.

### What is not in these theorems

Theorem 1.1.3 is not an embedded resolution. The morphism $\pi$ is not built as a sequence of blowups in regular centers along which the strict transforms are normally flat [CP19, Remark 1.4]. The embedded resolution of a threefold in a regular fourfold by such a sequence is open in characteristic $p$. Cossart and Piltant see the local Theorem 1.2.6, which uses only Hironaka-permissible blowups, as evidence that such a resolution may exist for threefolds, and they also point to [Cos87, Moh96] [CP19, Section 1]. Cutkosky calls it the most fundamental problem of resolution in positive characteristic [Cut09]. Kollár and Witaszek construct resolutions with an ample exceptional divisor in dimension 3 [Kol20]. Bhatt, Ma, Patakfalvi, Schwede, Tucker, Waldron and Witaszek prove the existence of projective log resolutions for reduced schemes of dimension 3 that are quasi-projective over a Noetherian quasi-excellent affine scheme [BMP20, Proposition 2.14]. Both results use the theorems of Cossart and Piltant. Neither result is an embedded resolution by a sequence of blowups in regular centers. Volume 9, Section 2.1 states these facts, and Chapter 4 of this volume explains why the methods stop in dimension 3.

For surfaces the embedded problem is solved: the theorem of Cossart, Jannsen and Saito gives a canonical embedded resolution of each excellent surface in a regular excellent scheme (Theorem 3.1.4 of Volume 4).

Node: SG0000001C · Lean: `Singularity.EmbeddedResolutionSurface` (the statement only)

The proof in [CP19] uses the embedded resolution of surfaces of [CJS20] at several places.

### Dimension four and higher

*Remark (the open problem).* None of the theorems of this section says anything about dimension 4. In characteristic $p > 0$ these problems are open in dimension at least 4: the resolution of varieties, the local uniformization of function fields of transcendence degree at least 4, and the embedded resolution of threefolds in regular schemes of dimension 4 by blowups in regular centers. Volume 9, Chapter 2, states them as conjectures. Weaker results hold in each dimension. The theorem of de Jong gives regular alterations [dJ96], and the theorem of Temkin gives local uniformization after a finite purely inseparable extension of the function field [Tem13]. Neither result gives a birational resolution. Volume 5, Chapter 5, describes the programs that aim at dimension 4, and it marks for each program what is proved and what is only announced. Chapter 4 of this volume explains where the proofs of this volume use dimension 3.

*Remark (the hypotheses of Theorem 1.1.6).* The function field $K$ is finitely generated over $k$, and the valuations are trivial on $k$. The field $k$ need not be perfect, and $[k : k^p]$ need not be finite. The papers [CP08, CP09] assume $[k : k^p] < \infty$, and [CP19] removes this assumption. The residue field of a valuation can be transcendental over $k$, and it need not be perfect even if $k$ is perfect. Imperfect residue fields cause technical problems in [CP19] (Section 4.1).

### Notes and references

The survey of Hauser [Hau10] explains the problem in characteristic $p$ and gives the history up to 2010. The book [Abh66] has a second edition of 1998. The introduction of [Cut09] compares the proof of Abhyankar with the methods of characteristic 0. The introduction of [CP19] explains the three papers of Cossart and Piltant and their relation to the work of Hironaka.
