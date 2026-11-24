---
title: The theorems
nodes: [SG0000001D, SG0000001V, SG0000001F, SG0000001C]
sources: [Abh56s, Abh66, Cut09, CP08, CP09, CP19, Zar40, Zar44, Lip78, CJS20, Kol20, BMP20, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorems

In this section we state the theorems on the resolution of threefolds in characteristic $p > 0$, in the order in which they were proved. We prove nothing here. The proofs are long. The proof of Abhyankar fills a book and several papers, and each of the papers of Cossart and Piltant is long too. The later sections of this volume explain the main ideas of the proofs, and they prove the steps that fit in a textbook.

### Resolution

We use the definition of a resolution of Volume 0, Definition 2.1.5. A *resolution* of a scheme $X$ is a proper morphism $\pi \colon Y \to X$ with $Y$ regular, which is an isomorphism over the regular locus $\operatorname{Reg}(X)$, such that $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$. For a prime $p$ and $n \ge 0$, the statement $\mathrm{Res}(p, n)$ of Volume 0, Definition 2.2.1, says that each variety of dimension at most $n$ over a field of characteristic $p$ has a resolution. A *threefold* is a variety of dimension 3.

The resolution of curves is classical: the normalization of a curve is regular (Volume 1, Theorem 2.5.6). The resolution of surfaces is Theorem 2.2.1 of Volume 4, the theorem of Lipman [Lip78]. Before Lipman, Abhyankar had proved the resolution of algebraic surfaces in characteristic $p$, through the local uniformization of surfaces [Abh56s]. In dimension 3 the first result is again due to Abhyankar.

### The theorem of Abhyankar

**Theorem 1.1.1 (Abhyankar).** Let $k$ be an algebraically closed field of characteristic $p$ with $p \ne 2, 3, 5$, and let $V$ be a projective variety of dimension 3 over $k$. Then there are a nonsingular projective variety $W$ and a birational morphism $\varphi \colon W \to V$ that is an isomorphism over the nonsingular locus of $V$.

Lean: none yet

The proof is in the book [Abh66] on the embedded resolution of surfaces and in several papers of Abhyankar [Cut09]. We state the theorem in the form of [Cut09, Theorem 1.1], which keeps the hypotheses of Abhyankar. Cutkosky writes that the proof of Abhyankar has 508 pages. The hardest part is the embedded resolution of surfaces in a nonsingular threefold, which Section 1.2 states as Theorem 1.2.2.

Cutkosky gave a new proof of Theorem 1.1.1 in [Cut09]. His proof is short and self-contained. Cutkosky writes that it could have been written in 1967, as it uses only methods known at that time. For the embedded resolution of surfaces it follows the algorithm of Levi, with the invariant of Hironaka and the weak transform of an ideal instead of the strict transform. Section 1.2 gives the plan.

### The theorems of Cossart and Piltant

Cossart and Piltant removed the conditions on $p$ and on the field. Their first two papers [CP08, CP09] treat threefolds over a field $k$ of characteristic $p > 0$ with $[k : k^p] < \infty$. A perfect field has this property, and so does a finitely generated extension of a perfect field. For such a field they prove the resolution of each threefold [CP09]. Their third paper [CP19] removes the condition on the field, and it also treats the arithmetic case.

**Theorem 1.1.2 (Cossart-Piltant).** Let $p$ be a prime. Each variety of dimension at most 3 over a field of characteristic $p$ has a resolution. That is, $\mathrm{Res}(p, 3)$ holds for each $p$.

Node: SG0000001D · Lean: `Singularity.ResolutionInDim` (the statement only)

For a field $k$ with $[k : k^p] < \infty$, the theorem is the main result of [CP08, CP09]. For an arbitrary field of characteristic $p$, it is a case of the next theorem, since a variety is quasi-excellent.

**Theorem 1.1.3 (Cossart-Piltant).** Let $X$ be a reduced separated Noetherian scheme that is quasi-excellent and has dimension at most 3. Then there is a proper birational morphism $\pi \colon X' \to X$ with these properties.

1. $X'$ is regular.
2. $\pi$ induces an isomorphism $\pi^{-1}(\operatorname{Reg} X) \to \operatorname{Reg} X$.
3. $\pi^{-1}(\operatorname{Sing} X)$ is a strict normal crossings divisor on $X'$.

If a finite affine cover $X = U_1 \cup \dots \cup U_n$ is given, then one can choose $\pi$ such that each $\pi^{-1}(U_i) \to U_i$ is projective.

Node: SG0000001V · Lean: `Singularity.resolution_quasiExcellent_three` (planned, no Lean statement yet)

This is [CP19, Theorem 1.1]. The theorem makes no hypothesis on the characteristic. It covers varieties over each field, and also schemes of mixed characteristic, for example schemes of finite type over $\mathbb{Z}$ or over an excellent discrete valuation ring of mixed characteristic. A morphism with properties 1 and 2 is a resolution in the sense of Volume 0, because $\pi$ is birational and $X$ is reduced. Two consequences are stated in [CP19].

**Corollary 1.1.4.** Let $A$ be a reduced complete Noetherian local ring of dimension 3. Then $\operatorname{Spec} A$ has a projective resolution $\pi$ such that $\pi^{-1}(\operatorname{Sing} \operatorname{Spec} A)$ is a strict normal crossings divisor.

Lean: none yet

**Corollary 1.1.5.** Let $\mathcal{O}$ be an excellent Dedekind domain with fraction field $F$, and let $\Sigma$ be a regular projective surface over $F$. Then there is a proper flat $\mathcal{O}$-scheme $\mathcal{X}$ with generic fiber $\Sigma$ such that $\mathcal{X}$ is regular.

Lean: none yet

These are [CP19, Corollary 1.2] and [CP19, Corollary 1.3]. Corollary 1.1.4 follows because a complete local ring is excellent. Corollary 1.1.5 follows because a projective model of $\Sigma$ over $\mathcal{O}$ is quasi-excellent of dimension 3.

### The method of Zariski

The proof of Cossart and Piltant follows the method that Zariski used in characteristic 0 for surfaces and threefolds [Zar40, Zar44]. First one proves local uniformization along each valuation. Then one patches the local solutions. Volume 3, Chapter 4 defines local uniformization and explains the first part of the patching.

**Theorem 1.1.6 (Cossart-Piltant).** Let $K$ be a function field of transcendence degree 3 over a field $k$ of characteristic $p > 0$. Each valuation of $K$ over $k$ has local uniformization.

Node: SG0000001F · Lean: `Singularity.localUniformization_three` (the statement only)

This is Theorem 4.1.5 of Volume 3 and Theorem 2.1.5 of Volume 9. Chapter 2 of this volume explains how Cossart and Piltant reduce it to two kinds of equations of degree $p$, and Chapter 3 gives the invariants that they use for these equations.

### What is not in these theorems

Theorem 1.1.3 is not an embedded resolution. The morphism $\pi$ is not built as a sequence of blowups in regular centers along which the strict transforms are normally flat [CP19, Remark 1.4]. The embedded resolution of a threefold in a regular fourfold by such a sequence is open in characteristic $p$. Cutkosky calls it the most fundamental problem of resolution in positive characteristic [Cut09]. Kollár [Kol20] and Bhatt, Ma, Patakfalvi, Schwede, Tucker, Waldron and Witaszek [BMP20] state the existence of projective log resolutions for quasi-excellent schemes of dimension at most 3, with these theorems as the base. They note that their results do not give a resolution by a sequence of blowups in regular centers [BMP20]. Volume 9, Section 2.1 states these facts, and Chapter 4 of this volume explains why the methods stop in dimension 3.

For surfaces the embedded problem is solved: the theorem of Cossart, Jannsen and Saito gives a canonical embedded resolution of each excellent surface in a regular excellent scheme (Theorem 3.1.4 of Volume 4).

Node: SG0000001C · Lean: `Singularity.EmbeddedResolutionSurface` (the statement only)

The proof in [CP19] uses the embedded resolution of surfaces of [CJS20] at several places.

### Notes and references

The survey of Hauser [Hau10] explains the problem in characteristic $p$ and gives the history up to 2010. The book [Abh66] has a second edition of 1998. The introduction of [Cut09] compares the proof of Abhyankar with the methods of characteristic 0. The introduction of [CP19] explains the three papers of Cossart and Piltant and their relation to the work of Hironaka.
