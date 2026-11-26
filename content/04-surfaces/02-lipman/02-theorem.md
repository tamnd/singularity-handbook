---
title: The theorem of Lipman
nodes: [SG0000001B]
sources: [Lip78, Art86, Stacks, Liu, Mat, Nag62, Har, AM69, EGA4-7]
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

### Two runs of the process

The process can stop at each of its two operations. The next example stops after the normalization. The surfaces $xy = z^n$ of Proposition 2.3.2 are normal, and for them the process consists of blowups only.

**Example 2.2.4.** Let $k$ be a field and let $X = V(x^2 - y^2z) \subseteq \mathbb{A}^3_k$ be the Whitney umbrella of Example 1.2.7. Then $X_0 = \mathbb{A}^2_k$, so the process stops with $n = 0$. The normalization $\nu : \mathbb{A}^2_k \to X$ is a resolution of $X$. It is finite, and no curve of $\mathbb{A}^2_k$ maps to a point.

Lean: none yet

*Proof.* By Example 1.2.7, the normalization of $X$ is $\nu : \mathbb{A}^2_k \to X$, and $\mathbb{A}^2_k$ is regular. By the second part of the proof of Theorem 2.2.1, with $n = 0$, the morphism $\nu$ is a resolution. A finite morphism has finite fibres, so no curve maps to a point. $\square$

The resolution of Example 2.2.4 is not an isomorphism over any point of the singular locus $L$. The fibre of $\nu$ over a point of $L$ with residue field $\kappa$ and coordinate $z = c$ is $\operatorname{Spec} \kappa[t]/(t^2 - c)$, which has degree 2 over $\kappa$, by the proof of Example 1.2.7. It is an isomorphism over $\operatorname{Reg}(X) = X \setminus L$, as condition 3 of the definition asks. For a normal surface $X_0 = X$, and the blowups do the work.

### Locality and the growth of $H^1$

The next two results are the short steps of the proof that we can give in full. The first one says that the process is local. The second one gives an invariant that does not go down along the process.

**Lemma 2.2.5.** Let $X$ be as in Theorem 2.2.1, with the sequence $X_0, X_1, \dots$. Let $\varphi : W \to X$ be either the inclusion of an open set or the morphism $\operatorname{Spec} \mathcal{O}_{X,x} \to X$ for a point $x \in X$.

1. The sequence of Theorem 2.2.1 for $W$ is $W_i = X_i \times_X W$, and $\operatorname{Sing}(W_i)$ is the inverse image of $\operatorname{Sing}(X_i)$.
2. The scheme $X_n$ is regular if and only if $X_n \times_X \operatorname{Spec} \mathcal{O}_{X,x}$ is regular for each closed point $x$ of $X$.

Lean: none yet

*Proof.* 1. The scheme $W$ is reduced and Noetherian, and it is excellent, since a localization of an excellent ring is excellent [Stacks]. Let $Y$ be a scheme over $X$ and let $Y_W = Y \times_X W$. In both cases the projection $Y_W \to Y$ is injective on points, and it induces isomorphisms of the local rings. For an open set this is clear. For $W = \operatorname{Spec} \mathcal{O}_{X,x}$, over an affine open $\operatorname{Spec} B$ of $Y$ that lies over an affine open $\operatorname{Spec} R$ of $X$, we have $Y_W \cap \operatorname{Spec} B = \operatorname{Spec} B_\Sigma$, where $\Sigma$ is the image of $R \setminus \mathfrak{p}_x$. The primes of $B_\Sigma$ are primes of $B$, with the same local rings. Thus a point of $Y_W$ is regular if and only if its image in $Y$ is regular, and $\operatorname{Sing}(Y_W)$ is the inverse image of $\operatorname{Sing}(Y)$.

We now compare the two operations with the base change. The normalization commutes with this base change, because integral closure commutes with localization [AM69, Proposition 5.12]. The blowup commutes with flat base change. Indeed, $\varphi$ is flat, so for an ideal sheaf $\mathcal{I}$ the map $\varphi^* \mathcal{I}^n \to (\mathcal{I}\mathcal{O}_W)^n$ is an isomorphism. Thus the Rees algebra of $\mathcal{I}\mathcal{O}_W$ is the pullback of the Rees algebra of $\mathcal{I}$, and $\operatorname{Proj}$ commutes with base change. A localization of a reduced ring is reduced, so the inverse image of the reduced scheme $S_i = \operatorname{Sing}(X_i)$ is $\operatorname{Sing}(W_i)$ with its reduced structure. By induction on $i$ we get $W_i = X_i \times_X W$.

2. Each point $y$ of $X_n$ maps to a point of $X$, and this point specializes to a closed point $x$, since $X$ is Noetherian. Then $y$ is in $X_n \times_X \operatorname{Spec} \mathcal{O}_{X,x}$, with the same local ring, by the proof of part 1. $\square$

Thus the process near one point does not see the other points, and we may study it for one excellent local ring at a time. Lemma 2.2.5 is Step 4 of the table below.

**Proposition 2.2.6.** Let $A$ be an excellent normal local domain of dimension 2, let $X = \operatorname{Spec} A$, and let $X_0 = X, X_1, X_2, \dots$ be the sequence of Theorem 2.2.1. Let $g_i : X_{i+1} \to X_i$ be the morphism of the process, and let $h_i = \ell_A(H^1(X_i, \mathcal{O}_{X_i}))$.

1. Each composite $X_i \to X$ is a normal modification, and each $g_i$ is a normal modification.
2. We have $h_0 = 0$ and $h_{i+1} = h_i + \ell_A(H^0(X_i, R^1 g_{i*} \mathcal{O}_{X_{i+1}}))$. In particular the sequence $h_0, h_1, \dots$ does not go down.
3. There is an $i_0$ such that $R^1 g_{i*} \mathcal{O}_{X_{i+1}} = 0$ for each $i \ge i_0$.

Lean: none yet

*Proof.* 1. By the proof of Theorem 2.2.1, each $X_i$ is a normal excellent surface, and $g_i$ is proper. The scheme $X_i$ is integral by induction. Indeed, the blowup of an integral surface in a finite set of closed points that is not the whole surface is integral with the same function field (Lemma 1.1.3), and the normalization of an integral scheme is integral. The morphism $g_i$ is an isomorphism over the dense open set $\operatorname{Reg}(X_i)$, by Corollary 1.2.5. Thus $g_i$ is a normal modification. A composite of normal modifications is a normal modification.

2. The scheme $X_0 = X$ is affine, so $h_0 = 0$. By part 1 and Lemma 2.1.2 for $X_i \to X$, we have $(g_i)_* \mathcal{O}_{X_{i+1}} = \mathcal{O}_{X_i}$ and $H^2(X_i, \mathcal{O}_{X_i}) = 0$. The Leray spectral sequence for $g_i$ gives, as in the proof of Proposition 2.1.7, the exact sequence

$$0 \to H^1(X_i, \mathcal{O}_{X_i}) \to H^1(X_{i+1}, \mathcal{O}_{X_{i+1}}) \to H^0(X_i, R^1 g_{i*} \mathcal{O}_{X_{i+1}}) \to 0.$$

All three modules have finite length, by Lemma 2.1.2, part 4. The length is additive, and this gives the formula.

3. By Theorem 2.1.6, $h_i \le N$ for each $i$. A sequence of integers that does not go down and is bounded is constant from some index $i_0$ on. For $i \ge i_0$, part 2 gives $H^0(X_i, R^1 g_{i*} \mathcal{O}_{X_{i+1}}) = 0$. The sheaf $R^1 g_{i*} \mathcal{O}_{X_{i+1}}$ is supported on finitely many closed points, by Lemma 2.1.2, part 4. As in the proof of Lemma 2.1.5, its global sections are the sum of its stalks. Thus the sheaf is 0. $\square$

Proposition 2.2.6 does not say that $X_{i_0}$ has rational singularities. Part 3 says that $R^1 g_{*} \mathcal{O} = 0$ for the one modification $g = g_i$ that the process chooses at each step $i \ge i_0$. Definition 2.1.3 asks for the vanishing for every normal modification. To close this gap is the main work of the second step of [Lip78], and we do not reproduce it. Proposition 2.1.7 closes the gap in a weaker sense: a normal modification $Y$ of $\operatorname{Spec} A$ with the largest value of $\ell_A(H^1(Y, \mathcal{O}_Y))$ has rational singularities. But this $Y$ need not be one of the $X_i$.

### The structure of the proof

The proof of the existence of $n$ in [Lip78] has three parts: the reduction to a local problem at finitely many points, the reduction to rational singularities, and the resolution of rational singularities. The table lists the steps of each part. For each step it says whether this volume proves it or cites it, and where.

| Step | Content | Here |
|---|---|---|
| 1 | The normalization of an excellent scheme is finite | Cited: Theorem 1.2.2, part 2, from [EGA4-7, Section 7.8] and [Stacks] |
| 2 | A normal excellent surface has finitely many singular points, all closed | Proved: Theorem 1.2.4 |
| 3 | One round of the process gives a normal excellent surface | Proved: Corollary 1.2.5 |
| 4 | The process is local over the points of $X$ | Proved: Lemma 2.2.5 |
| 5 | If $X_n$ is regular, then $X_n \to X$ is a resolution | Proved: Theorem 2.2.1, second part of the proof |
| 6 | The length of $H^1(Y, \mathcal{O}_Y)$ is bounded over the normal modifications $Y$ | Cited: Theorem 2.1.6, from [Lip78] |
| 7 | The length of $H^1(X_i, \mathcal{O}_{X_i})$ does not go down, so it is constant from some step on | Proved: Proposition 2.2.6, with Step 6 for the bound |
| 8 | A normal modification with the largest $H^1$ has rational singularities | Proved: Proposition 2.1.7, with Step 6 for its existence |
| 9 | The process itself reaches a surface with only rational singularities | Cited: [Lip78] |
| 10 | Rationality is stable under normal modifications, and it can be checked at the local rings | Proved: Lemma 2.1.5 and Lemma 2.1.8 |
| 11 | The curves over a rational singularity have $H^1 = 0$, and two of them with $H^0 = \kappa$ meet in at most one point | Proved: Proposition 2.1.9 and Corollary 2.1.10 |
| 12 | The process stops on a surface with only rational singularities | Cited: [Lip78], with the accounts in [Art86] and [Stacks] |

*The first part: Steps 1 to 5.* These steps make the process well defined and local. They use excellence twice: for the finiteness of the normalization in Step 1, and for the openness of the regular locus in Step 2. By Lemma 2.2.5 it suffices to treat the local ring $A = \mathcal{O}_{X_0,x}$ at one singular point $x$ of $X_0$. This is an excellent normal local domain of dimension 2. Only Step 1 is cited, and it is a theorem of commutative algebra and not of the resolution of singularities. Step 3 uses it.

*The second part: Steps 6 to 9.* Step 6 is the hard input. It is a bound that does not depend on the modification. Steps 7 and 8 are formal consequences of Step 6 and the Leray spectral sequence, and we prove them. Step 9 connects the two. Lipman shows that the process itself, and not some other modification, reaches a surface whose singularities are all rational [Lip78]. We do not reproduce this step. The remark after Proposition 2.2.6 explains why Steps 7 and 8 do not give it at once.

*The third part: Steps 10 to 12.* By Lemma 2.1.5, rational singularities stay rational in the later steps of the process. By Lemma 2.1.8, it suffices to know rationality at each point of dimension 2. Step 11 gives the first facts on the curves over a rational singularity. Lipman then makes a detailed study of rational singularities, and he shows that the process, started on a surface with only rational singularities, stops after finitely many steps [Lip78]. A main fact of the theory of rational singularities, due to Lipman, is that the blowup of a rational singularity at its singular point is normal. Thus from this stage on the normalization step does nothing. The rational double points need a separate argument. We cite Step 12. For the equations of $A_n$, $D_4$ and $E_6$ in Section 2.3 the reader can see by hand that the process stops. In characteristics 2 and 3 there are other equations of type $D_4$ or $E_6$ that are not equivalent to these, and Section 2.3 does not treat them.

The proof is free of the characteristic. No step uses a hypersurface of maximal contact. Thus the proof of [Lip78] works in every characteristic and in mixed characteristic. The examples of Section 2.3 show the process in characteristic $p$.

### Notes and references

Theorem 2.2.1 is the theorem of [Lip78]. Artin gives a shorter account of the proof in [Art86]. The chapter "Resolution of Surfaces" of [Stacks] gives a complete proof that follows Lipman. Liu states the theorem as [Liu, Theorem 8.3.44], and he discusses the desingularization of surfaces and the minimal desingularization in [Liu, Chapters 8 and 9]. For the excellence of varieties see Corollary 5.2.9 of Volume 1. The Lean library has the statement `Singularity.ResolutionInDim`, and $\mathrm{Res}(p, 2)$ is the case $n = 2$ of it. The Lean library does not prove Theorem 2.2.1 or this case. The map plans the theorem `Singularity.resolutionInDim_two` (planned, no Lean statement yet) for $\mathrm{Res}(p, 2)$ in each characteristic [Lip78]. The plan is to prove it in the project, or to get it from the Lean proof of the theorem of Lipman in the library AxiomMath/Stacks (`exists_isResolution_of_isExcellent_of_ringKrullDim_eq_two`). Models wrote that proof, and nobody has reviewed it yet. The bridge needs a human review of that proof and of its definitions, and it is not done.
