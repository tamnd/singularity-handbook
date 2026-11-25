---
title: The theorem of Lipman
nodes: [SG0000001B]
sources: [Lip78, Art86, Stacks, Liu, Mat, Nag62, Har]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem of Lipman

In this section we state the theorem of Lipman and we prove its formal parts. Then we give the structure of the proof, and we say for each step whether we prove it here or cite it. The definition of a resolution is Definition 2.1.5 of Volume 0.

### The statement

Let $X$ be a reduced excellent Noetherian scheme of dimension at most 2. We define a sequence of schemes $X_0, X_1, \dots$ over $X$. Let $X_0 = X^\nu$ be the normalization of $X$. For $i \ge 0$, let $S_i = \operatorname{Sing}(X_i)$ with its reduced structure, and let $X_{i+1}$ be the normalization of $\operatorname{Bl}_{S_i} X_i$.

**Theorem 2.2.1 (Lipman).** Let $X$ be a reduced excellent Noetherian scheme of dimension at most 2. Then the sequence $X_0, X_1, \dots$ is well defined, and there is an $n$ such that $X_n$ is regular. For such an $n$, the morphism $X_n \to X$ is a resolution of $X$. In particular, $X$ has a resolution, and $\mathrm{Res}(p, 2)$ holds for each $p$.

Node: SG0000001B · Lean: `Singularity.ResolutionInDim` (the statement only)

The existence of $n$ is the theorem of [Lip78], and we do not prove it. We prove the other claims.

*Proof that the sequence is well defined.* By Theorem 1.2.2, $X_0$ is a normal excellent surface, and $X_0 \to X$ is finite. Assume that $X_i$ is a normal excellent surface. By Theorem 1.2.4, $S_i$ is a finite set of closed points. By Corollary 1.2.5, $X_{i+1}$ is a normal excellent surface, and $X_{i+1} \to X_i$ is proper and an isomorphism over $X_i \setminus S_i$. $\square$

*Proof that $X_n \to X$ is a resolution when $X_n$ is regular.* Let $\pi : X_n \to X$ be the composite. We check the four conditions of Definition 2.1.5 of Volume 0.

1. The scheme $X_n$ is regular by assumption.
2. The morphism $\pi$ is a composite of a finite morphism and proper morphisms, so it is proper.
3. Let $U = \operatorname{Reg}(X)$. The set $U$ is open by Proposition 5.3.2 of Volume 1, because $X$ is excellent. A regular local ring is a factorial domain [Mat, Section 20], so it is integrally closed by Proposition 2.1.4 of Volume 1. Thus $U$ is normal, and $X_0 \to X$ is an isomorphism over $U$. Assume that the preimage $U_i$ of $U$ in $X_i$ maps isomorphically to $U$. Then $U_i$ is regular, so $U_i \cap S_i = \emptyset$, and $X_{i+1} \to X_i$ is an isomorphism over $U_i$. By induction $\pi^{-1}(U) \to U$ is an isomorphism.
4. Each irreducible component of $X_n$ is integral, and its generic point maps to a generic point of $X$. Indeed, normalization maps generic points to generic points, and the blowup of an integral surface at a finite set of closed points that is not the whole surface is integral with the same function field (Lemma 1.1.3). A component of dimension 0 is regular and is never blown up. The local ring of the reduced scheme $X$ at a generic point is a field, so each generic point of $X$ is in $U$. Thus the open set $\pi^{-1}(U)$ contains all generic points of $X_n$, and it is dense. $\square$

For the last claim, recall from Definition 2.2.1 of Volume 0 that $\mathrm{Res}(p, 2)$ asks for a resolution of each variety of dimension at most 2 over a field of characteristic $p$. A variety is excellent by Corollary 5.2.9 of Volume 1, so Theorem 2.2.1 applies.

### Why excellence

The next proposition shows that the finiteness of normalization is necessary for a resolution.

**Proposition 2.2.2.** Let $X$ be an integral Noetherian scheme that has a resolution $\pi : Y \to X$. Then the normalization of $X$ is finite.

Lean: none yet

*Proof.* Let $K$ be the function field of $X$ and let $U = \operatorname{Reg}(X)$. The set $U$ is open by condition 3 of Definition 2.1.5 of Volume 0. The generic point of $X$ is in $U$, so $U$ is a nonempty open set and it is irreducible. The set $\pi^{-1}(U) \cong U$ is irreducible and dense in $Y$, so $Y$ is irreducible. The local rings of $Y$ are regular, so they are domains (Theorem 1.3.3 of Volume 1), and $Y$ is integral with function field $K$. A regular local ring is factorial [Mat, Section 20], so it is integrally closed (Proposition 2.1.4 of Volume 1). Thus $Y$ is normal.

Let $\operatorname{Spec} R \subseteq X$ be an affine open and let $B = \Gamma(\pi^{-1}(\operatorname{Spec} R), \mathcal{O}_Y)$. Since $\pi$ is proper, $B$ is a finite $R$-module [Stacks]. The ring $B$ is the intersection of the local rings $\mathcal{O}_{Y,y} \subseteq K$ for $y \in \pi^{-1}(\operatorname{Spec} R)$, and each of them is integrally closed in $K$. Thus $B$ is integrally closed in $K$. Let $R'$ be the integral closure of $R$ in $K$. Each element of $R'$ is integral over $R \subseteq B$, so $R' \subseteq B$. Since $R$ is Noetherian and $B$ is a finite $R$-module, the submodule $R'$ is a finite $R$-module. $\square$

**Remark 2.2.3.** Nagata gives Noetherian local domains whose normalization is not finite [Nag62, Appendix]. By Proposition 2.2.2, such a ring has no resolution. Thus some condition such as excellence is necessary in Theorem 2.2.1. The theorem of [Lip78] is more general than Theorem 2.2.1. It gives a condition for the existence of a resolution of a reduced Noetherian scheme of dimension 2 that is not assumed excellent. We do not state that condition here.

Lean: none yet

### The structure of the proof

The proof of the existence of $n$ in [Lip78] has three steps. The table lists them and says where each part is.

| Step | Content | Here |
|---|---|---|
| 1 | Reduction to a normal surface with finitely many singular points, each a closed point | Proved in Section 1.2 |
| 2 | Reduction to rational singularities | Partly proved in Section 2.1, the bound cited |
| 3 | The resolution of rational singularities | Cited |

*Step 1.* This is the content of Theorem 1.2.2, Theorem 1.2.4 and Corollary 1.2.5. It uses excellence twice: for the finiteness of the normalization and for the openness of the regular locus. The process is local over the singular points. Thus we may study one normal excellent local domain $A$ of dimension 2 at a time.

*Step 2.* By Theorem 2.1.6, the length of $H^1(Y, \mathcal{O}_Y)$ is bounded over the normal modifications $Y$ of $\operatorname{Spec} A$. By Proposition 2.1.7, a normal modification with the largest length has only rational singularities. We prove Proposition 2.1.7 here, and we cite Theorem 2.1.6. Lipman then shows that the sequence $X_0, X_1, \dots$ itself reaches, after finitely many steps, a scheme with only rational singularities [Lip78]. We do not reproduce this part of the argument.

*Step 3.* By Lemma 2.1.5, rational singularities stay rational in the later steps of the process. This part is formal, and we prove it here. Lipman then makes a detailed study of rational singularities, and he shows that the process stops on a surface with only rational singularities [Lip78]. The rational double points need a separate argument. We cite this step.

The proof is free of the characteristic. No step uses a hypersurface of maximal contact. Thus the proof of [Lip78] works in every characteristic and in mixed characteristic. The examples of Section 2.3 show the process in characteristic $p$.

### Notes and references

Theorem 2.2.1 is the theorem of [Lip78]. Artin gives a shorter account of the proof in [Art86]. The chapter "Resolution of Surfaces" of [Stacks] gives a complete proof that follows Lipman. Liu discusses the desingularization of surfaces and the minimal desingularization in [Liu]. For the excellence of varieties see Corollary 5.2.9 of Volume 1. The Lean library has the statement `Singularity.ResolutionInDim`, and $\mathrm{Res}(p, 2)$ is the case $n = 2$ of it. The Lean library does not prove Theorem 2.2.1 or this case.
