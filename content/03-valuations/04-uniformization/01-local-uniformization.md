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

A trivial valuation has local uniformization, because its center is the generic point, and the local ring there is the field $K$. If $\dim X = 1$, then the normalization of $X$ is regular (Volume 1, Chapter 2), so each valuation has local uniformization. The definition asks for a regular center on one model. It does not ask that the model be regular elsewhere.

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

This is the main theorem of [Zar40]. In characteristic 0 it is now also a consequence of the theorem of Hironaka, because a resolution of a model gives a regular center for each valuation.

**Theorem 4.1.4 (Abhyankar).** Let $k$ be an algebraically closed field of characteristic $p > 0$, and let $K/k$ be a function field of transcendence degree 2. Then each valuation of $K/k$ has local uniformization.

Lean: none yet

Abhyankar proved this in [Abh56s], and he deduced resolution of surfaces from it. Volume 4 proves resolution of surfaces by the method of Lipman, which does not use valuations. For threefolds over an algebraically closed field of characteristic $p > 5$, Abhyankar proved local uniformization and resolution [Abh66], and Cutkosky gives a shorter proof of resolution in this case [Cut09].

**Theorem 4.1.5 (Cossart and Piltant).** Let $K/k$ be a function field of transcendence degree 3 over a field $k$ of characteristic $p > 0$. Then each valuation of $K/k$ has local uniformization.

Node: SG0000001F · Lean: `Singularity.localUniformization_three` (planned, no Lean statement yet)

This is [CP08, CP09]. It is Theorem 2.1.5 of Volume 9, which explains the method and the patching step. We state the theorem as Volume 9 does. The two papers give the exact hypotheses on the field $k$.
