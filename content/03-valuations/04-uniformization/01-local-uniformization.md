---
title: Local uniformization
nodes: [SG0000001F]
sources: [Zar40, Zar44, Har, Pil, Abh56s, Abh66, Cut09, CP08, CP09]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Local uniformization

In this section $K/k$ is a function field. A *model* of $K/k$ is an integral variety $X$ over $k$ with function field $K$, in the sense of Definition 2.1.4 of Volume 0. For a valuation $v$ of $K/k$, Proposition 1.4.3 shows that $v$ has at most one center on a model.

### The definition

**Definition 4.1.1 (local uniformization).** A valuation $v$ of $K/k$ has *local uniformization* if for each model $X$ of $K/k$ on which $v$ has a center, there are a model $X'$ and a proper birational morphism $X' \to X$ such that the center of $v$ on $X'$ is a regular point of $X'$.

The center of $v$ on $X'$ exists. Let $x$ be the center of $v$ on $X$. The inclusion $\mathcal{O}_{X,x} \subseteq \mathcal{O}_v$ gives a morphism $\operatorname{Spec} \mathcal{O}_v \to X$, and the valuative criterion of properness [Har, Chapter II, Theorem 4.7] lifts it to $X'$. The image $x'$ of the closed point is a center of $v$ on $X'$. This is the definition of Volume 9, Section 2.3.

A trivial valuation has local uniformization, because its center is the generic point, and the local ring there is the field $K$. If $\dim X = 1$, then the normalization of $X$ is regular, and the normalization morphism is finite and birational, so it is proper (Volume 1, Theorem 2.5.6). Thus each valuation has local uniformization. Proposition 4.1.7 below gives a proof in the affine form. The definition asks for a regular center on one model. It does not ask that the model be regular elsewhere.

### The method of Zariski

Zariski proved resolution in characteristic 0 up to dimension 3 in two steps [Zar40, Zar44]. First he proved local uniformization for each valuation. Then he patched the local solutions. Quasi-compactness of the Zariski-Riemann space makes the first step finite.

**Proposition 4.1.2.** Let $X$ be a model of $K/k$ that is proper over $k$, and assume that each valuation of $K/k$ has local uniformization. Then there are finitely many models $X_1, \dots, X_m$ and proper birational morphisms $X_i \to X$ with this property: each valuation of $K/k$ has a regular center on at least one $X_i$.

Lean: none yet

*Proof.* Let $v$ be a valuation of $K/k$. By Proposition 1.4.4, $v$ has a center on $X$. By local uniformization there is a proper birational morphism $X_v \to X$ from a model $X_v$ such that the center $x_v$ of $v$ on $X_v$ is regular. Let $\operatorname{Spec} B_v$ be an affine open subset of $X_v$ that contains $x_v$. Then $B_v$ is a finitely generated $k$-algebra and a domain with $\operatorname{Frac} B_v = K$. Also $B_v \subseteq \mathcal{O}_{X_v, x_v} \subseteq \mathcal{O}_v$. Let $G_v$ be the regular locus of $\operatorname{Spec} B_v$. It is open by Theorem 5.3.3 of Volume 1, and it contains $x_v$.

By Corollary 1.5.4 there are $v_1, \dots, v_m$ such that each valuation $w$ of $K/k$ has a center on some $\operatorname{Spec} B_{v_i}$, and this center lies in $G_{v_i}$. A center on the open subset $\operatorname{Spec} B_{v_i}$ is a center on $X_{v_i}$, and it is a regular point. Let $X_i = X_{v_i}$. $\square$

Each $X_i$ is proper over $k$, because $X_i \to X$ and $X \to \operatorname{Spec} k$ are proper. A proper model of $K/k$ exists: take a projective closure of an affine model. So Proposition 4.1.2 always applies once local uniformization is known.

The second step, *patching*, builds one regular model from $X_1, \dots, X_m$. A first idea is the join, the closure of the image of $\operatorname{Spec} K$ in $X_1 \times_k \dots \times_k X_m$. Each valuation has a center on the join, and the center maps to its centers on the $X_i$. But the center on the join need not be regular, even if one of its images is regular. Zariski solved this problem in characteristic 0 for dimension at most 3 [Zar44]. Piltant gives an axiomatic form of the patching theorem [Pil]. In dimension 4 patching is open, also when local uniformization is known; see Conjecture 2.3.2 of Volume 9.

### Known cases

**Theorem 4.1.3 (Zariski).** Let $k$ be a field of characteristic 0. Then each valuation of a function field $K/k$ has local uniformization.

Lean: none yet

This is the main theorem of [Zar40]. Zariski proves it for function fields over each ground field of characteristic 0. In characteristic 0 it is now also a consequence of the theorem of Hironaka, because a resolution of a model gives a regular center for each valuation.

**Theorem 4.1.4 (Abhyankar).** Let $k$ be an algebraically closed field of characteristic $p > 0$, and let $K/k$ be a function field of transcendence degree 2. Then each valuation of $K/k$ has local uniformization.

Lean: none yet

Abhyankar proved this in [Abh56s], and he deduced resolution of surfaces from it. Volume 4 proves resolution of surfaces by the method of Lipman, which does not use valuations. For threefolds over an algebraically closed field of characteristic $p > 5$, Abhyankar proved local uniformization and resolution [Abh66], and Cutkosky gives a shorter proof of resolution in this case [Cut09].

**Theorem 4.1.5 (Cossart-Piltant).** Let $K/k$ be a function field of transcendence degree 3 over a field $k$ of characteristic $p > 0$. Then each valuation of $K/k$ has local uniformization.

Node: SG0000001F · Lean: `Singularity.localUniformization_three` (the statement only)

The papers [CP08, CP09] prove this theorem, and resolution of threefolds, when $k$ is differentially finite over a perfect subfield $k_0$, that is, when $\Omega_{k/k_0}$ has finite dimension over $k$. For example, each function field $k_0(\lambda_1, \dots, \lambda_s)$ over a perfect field $k_0$ is of this kind. For an arbitrary field $k$ of characteristic $p$, the theorem follows from the resolution of quasi-excellent schemes of dimension 3 [CP19]. Indeed, a model $X$ of $K/k$ is quasi-excellent, so there is a proper birational morphism $X' \to X$ with $X'$ regular, and the center of $v$ on $X'$ is a regular point. The theorem is Theorem 2.1.5 of Volume 9, which explains the method and the patching step.

### The affine form

Definition 4.1.1 uses all models. The next proposition gives an equivalent form with affine models only. This form is the form of [KK05], and it is the form of the Lean statement. Let $v$ be a valuation of $K/k$ with valuation ring $\mathcal{O}_v$ and maximal ideal $\mathfrak{m}_v$. An *affine model* of $K/k$ is a $k$-subalgebra $A$ of $K$ that is finitely generated over $k$ and has fraction field $K$. If $A \subseteq \mathcal{O}_v$, then $\mathfrak{m}_v \cap A$ is the center of $v$ on $\operatorname{Spec} A$.

**Proposition 4.1.6 (the affine form).** A valuation $v$ of $K/k$ has local uniformization if and only if this condition holds: for each finite subset $S$ of $\mathcal{O}_v$ there is an affine model $A$ of $K/k$ with $S \subseteq A \subseteq \mathcal{O}_v$ such that the local ring $A_{\mathfrak{m}_v \cap A}$ is regular.

Lean: `Singularity.HasLocalUniformization`

*Proof.* Assume that $v$ has local uniformization, and let $S \subseteq \mathcal{O}_v$ be finite. Choose $t_1, \dots, t_n$ that generate $K$ as a field over $k$. If $t_i \notin \mathcal{O}_v$, then $t_i^{-1} \in \mathcal{O}_v$, and we replace $t_i$ by $t_i^{-1}$. Let $A_0 = k[S, t_1, \dots, t_n]$. Then $A_0$ is an affine model, and $A_0 \subseteq \mathcal{O}_v$, so $v$ has a center on $\operatorname{Spec} A_0$. By Definition 4.1.1 there is a proper birational morphism $X' \to \operatorname{Spec} A_0$ such that the center $x'$ of $v$ on $X'$ is regular. Let $\operatorname{Spec} A$ be an affine open subset of $X'$ that contains $x'$. Then $A$ is an affine model, and $A \subseteq \mathcal{O}_{X',x'} \subseteq \mathcal{O}_v$. The morphism to $\operatorname{Spec} A_0$ gives $A_0 \subseteq A$, so $S \subseteq A$. The point $x'$ is the prime $\mathfrak{m}_v \cap A$, so $A_{\mathfrak{m}_v \cap A} = \mathcal{O}_{X',x'}$ is regular.

Conversely, assume the condition, and let $X$ be a model on which $v$ has a center $x$. Let $\operatorname{Spec} A_0$ be an affine open subset of $X$ that contains $x$, and let $S$ be a finite set of generators of $A_0$ over $k$. Then $S \subseteq \mathcal{O}_{X,x} \subseteq \mathcal{O}_v$. Choose $A$ as in the condition, and let $Y$ be a projective closure of $\operatorname{Spec} A$. Let $X'$ be the closure of the image of $\operatorname{Spec} K$ in $X \times_k Y$. The projection $X' \to X$ is proper, because $Y$ is proper over $k$, and it is birational. The center $x'$ of $v$ on $X'$ maps to $x$ and to the center of $v$ on $Y$, which is the point $\mathfrak{m}_v \cap A$ of $\operatorname{Spec} A$. Near $x'$, the scheme $X'$ is the closed subscheme of $\operatorname{Spec} A_0 \times_k \operatorname{Spec} A$ given by the image of $A_0 \otimes_k A \to K$. This image is $A$, because $A_0 \subseteq A$. Thus $\mathcal{O}_{X',x'} = A_{\mathfrak{m}_v \cap A}$, and it is regular. $\square$

The condition with one affine model, without the finite set $S$, follows from the condition of Proposition 4.1.6. The converse is not known in general, and the definition of local uniformization must ask for each finite set.

### Transcendence degree at most 1

The affine form gives a direct proof of the case of curves. It uses no blowup and no condition on the characteristic.

**Proposition 4.1.7.** Let $k$ be a field of any characteristic, and let $K/k$ be a function field with $\operatorname{trdeg}_k K \le 1$. Then each valuation of $K/k$ has local uniformization.

Lean: `Singularity.hasLocalUniformization_of_trdeg_le_one`

*Proof.* We use Proposition 4.1.6. Let $v$ be a valuation of $K/k$, and let $S \subseteq \mathcal{O}_v$ be finite. As in the proof of Proposition 4.1.6, choose $t_1, \dots, t_n \in \mathcal{O}_v$ that generate $K$ as a field over $k$, and let $A_0 = k[S, t_1, \dots, t_n]$. Then $A_0$ is an affine model with $S \subseteq A_0 \subseteq \mathcal{O}_v$. Let $A$ be the integral closure of $A_0$ in $K$. A valuation ring is integrally closed, so $A \subseteq \mathcal{O}_v$. By the theorem of E. Noether (Volume 1, Theorem 2.4.7), $A$ is a finite $A_0$-module. Thus $A$ is a finitely generated $k$-algebra, and $A$ is an affine model.

We show that $\dim A \le 1$. By Noether normalization (Volume 1, Theorem 2.2.1) there are $y_1, \dots, y_s \in A$, algebraically independent over $k$, such that $A$ is finite over $P = k[y_1, \dots, y_s]$. The $y_i$ are algebraically independent elements of $K$, so $s \le \operatorname{trdeg}_k K \le 1$. The extension $P \subseteq A$ is integral. By incomparability, a strict chain of primes of $A$ maps to a strict chain of primes of $P$, so $\dim A \le \dim P = s$.

Let $\mathfrak{p} = \mathfrak{m}_v \cap A$, and let $R = A_\mathfrak{p}$. Then $R$ is a Noetherian local domain with $\dim R \le 1$, and $R$ is integrally closed, because $A$ is integrally closed. If $\dim R = 0$, then $R$ is a field, and it is regular. If $\dim R = 1$, then $R$ is regular by Volume 1, Theorem 1.4.2. $\square$

The proof is the proof of Theorem 2.5.6 of Volume 1 in the affine form. The model $A$ is regular at the center of $v$, and the proof gives no information at the other points of $\operatorname{Spec} A$. For $\operatorname{trdeg}_k K = 0$ the field $K$ is finite over $k$, so $A = K$, and the result is trivial.

### The Lean statements

The Lean library states the definitions of this chapter in `Singularity/Statements/LocalUniformization.lean`. A valuation of $K/k$ is a valuation subring $V$ of $K$ that contains $k$. The condition of Proposition 4.1.6 for one finite set is `Singularity.HasRegularCenter`, and local uniformization is `Singularity.HasLocalUniformization`. The regular local rings are the regular local rings of Mathlib. The library has no Lean proof of Proposition 4.1.6, because it has no Lean statement of Definition 4.1.1. Proposition 4.1.7 is proved in `Singularity/Valuation/LocalUniformizationCurves.lean`. The file also proves `Singularity.localUniformizationInDim_zero` and `Singularity.localUniformizationInDim_one`, that is, local uniformization for each function field of transcendence degree 0 or 1 over a field of characteristic $p$, for each $p$. Theorem 4.1.5 is stated as `Singularity.localUniformization_three`, for each prime $p$ and each field of characteristic $p$, and it is not proved. The file also states Theorems 4.2.1 and 4.2.2 and the two conjectures of Volume 9, Section 2.3. The file `Singularity/Fidelity/LocalUniformization.lean` proves three facts that test the definition. The trivial valuation has local uniformization. A valuation with local uniformization contains $k$. If some valuation has local uniformization, then $K$ is finitely generated over $k$. The last fact shows that the condition on the models is not empty.
