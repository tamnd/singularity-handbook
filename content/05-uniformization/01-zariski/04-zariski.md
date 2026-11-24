---
title: The theorem of Zariski
nodes: [SG0000000D, SG0000000X, SG0000001J, SG0000004F, SG0000004E]
sources: [Zar40, Zar44, Hir64, Cut04, NS14, Tem13, Pil]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem of Zariski

Zariski proved local uniformization in characteristic 0 in all dimensions [Zar40]. This is Theorem 4.1.3 of Volume 3:

**Theorem 1.4.1 (Zariski).** Let $k$ be a field of characteristic 0. Then each valuation of a function field $K/k$ has local uniformization.

Lean: none yet

We do not reproduce the proof of [Zar40]. In this section we prove two reductions that hold in each characteristic, we deduce Theorem 1.4.1 from the theorem of Hironaka, and we describe the other proofs and the use of the theorem.

### Reduction to an algebraic residue field

A valuation $v$ of $K/k$ is *zero-dimensional* if its residue field $\kappa_v$ is algebraic over $k$. For a divisorial valuation the residue field has transcendence degree $\operatorname{trdeg}_k K - 1$, and Volume 3, Proposition 4.1.8, treats it directly. The next lemma shows that in general one can enlarge the ground field until the valuation is zero-dimensional.

**Lemma 1.4.2.** Let $v$ be a valuation of $K/k$, and let $y_1, \dots, y_m \in \mathcal{O}_v$ be elements whose residues are algebraically independent over $k$. Then $y_1, \dots, y_m$ are algebraically independent over $k$, the field $k' = k(y_1, \dots, y_m)$ is contained in $\mathcal{O}_v$, and $v$ is a valuation of the function field $K/k'$. If $v$ has local uniformization as a valuation of $K/k'$, then $v$ has local uniformization as a valuation of $K/k$. If the residues form a transcendence basis of $\kappa_v$ over $k$, then $v$ is zero-dimensional as a valuation of $K/k'$, and $\operatorname{trdeg}_{k'} K = \operatorname{trdeg}_k K - \operatorname{trdeg}_k \kappa_v$.

Node: SG0000004F · Lean: none yet

*Proof.* The first claims are in the proof of Volume 3, Proposition 4.1.8, part 2: for a nonzero polynomial $Q$ over $k$, the residue of $Q(y)$ is $Q(\bar{y}) \ne 0$, so $Q(y)$ is a unit of $\mathcal{O}_v$. Thus $k' \subseteq \mathcal{O}_v$, and $K$ is finitely generated over $k'$.

We use Proposition 4.1.6 of Volume 3 twice. Let $S \subseteq \mathcal{O}_v$ be finite. By assumption there is an affine model $A'$ of $K/k'$ with $S \subseteq A' \subseteq \mathcal{O}_v$ such that $A'_{\mathfrak{p}'}$ is regular, where $\mathfrak{p}' = \mathfrak{m}_v \cap A'$. Write $A' = k'[a_1, \dots, a_r]$, and let $B = k[y_1, \dots, y_m, a_1, \dots, a_r, S]$. Then $B \subseteq A' \subseteq \mathcal{O}_v$, since $S \subseteq A'$. The fraction field of $B$ contains $k'$ and the $a_i$, so it is $K$, and $B$ is an affine model of $K/k$. Let $\mathfrak{q} = \mathfrak{m}_v \cap B$.

We show $B_\mathfrak{q} = A'_{\mathfrak{p}'}$. An element of $B \setminus \mathfrak{q}$ is a unit of $\mathcal{O}_v$ that lies in $A'$, so it lies in $A' \setminus \mathfrak{p}'$. Thus $B_\mathfrak{q} \subseteq A'_{\mathfrak{p}'}$. Conversely, each element of $k'$ is $Q_1(y)/Q_2(y)$ with $Q_2 \ne 0$, and $Q_2(y) \in B \setminus \mathfrak{q}$, so $k' \subseteq B_\mathfrak{q}$ and $A' \subseteq B_\mathfrak{q}$. The maximal ideal of $B_\mathfrak{q}$ is $\mathfrak{m}_v \cap B_\mathfrak{q}$. An element of $A' \setminus \mathfrak{p}'$ lies in $B_\mathfrak{q}$ and is a unit of $\mathcal{O}_v$, so it is a unit of $B_\mathfrak{q}$. Thus $A'_{\mathfrak{p}'} \subseteq B_\mathfrak{q}$.

So $S \subseteq B \subseteq \mathcal{O}_v$ and $B_\mathfrak{q}$ is regular. This proves local uniformization of $v$ over $k$. The residue field of $k'$ is $k(\bar{y}_1, \dots, \bar{y}_m)$. If the residues form a transcendence basis, then $\kappa_v$ is algebraic over it, and the tower law gives the last claim. $\square$

Thus local uniformization in dimension $n$ follows from local uniformization of zero-dimensional valuations of function fields of transcendence degree at most $n$, over all ground fields of the given characteristic. The ground field $k'$ is not algebraically closed, even if $k$ is. This is one reason to prove local uniformization over each field, and not only over algebraically closed fields.

**Corollary 1.4.3.** Let $k$ be a field of characteristic 0, let $K/k$ be a function field of transcendence degree 3, and let $v$ be a valuation of $K/k$ such that $\Gamma_v$ is finitely generated and $\kappa_v$ is not algebraic over $k$. Then $v$ has local uniformization.

Lean: none yet

*Proof.* If $\operatorname{trdeg}_k \kappa_v \ge 2$, this is Volume 3, Proposition 4.1.8. If $\operatorname{trdeg}_k \kappa_v = 1$, choose $y \in \mathcal{O}_v$ whose residue is transcendental over $k$, and let $k' = k(y)$. By Lemma 1.4.2, $K/k'$ is a function field of transcendence degree 2, and $v$ is a valuation of $K/k'$ with the same value group. The field $k'$ has characteristic 0. By Corollary 1.3.6 over $k'$, $v$ has local uniformization over $k'$, and by Lemma 1.4.2 also over $k$. $\square$

**Example 1.4.4.** Let $K = k(x, y, z)$ over a field $k$ of any characteristic. Let $v$ be the valuation that is trivial on $k(y)$ and is the monomial valuation of $k(y)(x, z)$ with $v(x) = 1$ and $v(z) = \sqrt{2}$, as in Volume 3, Lemma 1.6.1, over the field $k(y)$. Its residue field is $k(y)$, and $\Gamma_v = \mathbb{Z} + \mathbb{Z}\sqrt{2}$. By Corollary 1.2.8 over the field $k(y)$, the valuation $v$ of $K/k(y)$ has local uniformization, and by Lemma 1.4.2 so has $v$ as a valuation of $K/k$. This works in each characteristic, because $K$ is a field of rational functions over $k(y)$. The valuation is an Abhyankar valuation, and Chapter 2 gives a second proof.

### Resolution implies local uniformization

**Proposition 1.4.5.** Let $v$ be a valuation of $K/k$, let $X$ be a model of $K/k$ on which $v$ has a center, and let $\pi : X' \to X$ be a resolution of $X$, that is, a proper birational morphism with $X'$ regular. Then the center of $v$ on $X'$ is a regular point of $X'$. In particular, if each model of $K/k$ has a resolution, then each valuation of $K/k$ has local uniformization.

Node: SG0000004E · Lean: none yet

*Proof.* The center of $v$ on $X'$ exists, by the valuative criterion of properness (see the remark after Volume 3, Definition 4.1.1). Each point of $X'$ is regular. So $\pi$ is a proper birational morphism as in Volume 3, Definition 4.1.1, and the center of $v$ on $X'$ is regular. $\square$

The proposition is trivial, but it shows how the two problems relate. Resolution gives one model that is good for all valuations at once. Local uniformization gives a model for each valuation, and then one must patch these models. In dimension at most 3, the known proofs go the other way: they prove local uniformization first and then patch [Zar44].

**Corollary 1.4.6.** Theorem 1.4.1 follows from the theorem of Hironaka [Hir64].

Node: SG0000004E · Lean: none yet

*Proof.* Let $X$ be a model of $K/k$. It is an integral variety over a field of characteristic 0. By the theorem of Hironaka, in the form of Volume 9, Theorem 1.2.6, it has a resolution. Proposition 1.4.5 gives the claim. $\square$

This is not a proof that one would give to understand local uniformization, because the theorem of Hironaka is much harder than Theorem 1.4.1, and because [Zar40] came first. But it is a complete reduction to a theorem that this handbook states with a Lean proof: Volume 9, Theorem 1.2.6, is node SG0000000D with the Lean name `Singularity.resolutionInDim_charZero`. The step from resolution to local uniformization is not in the library. To check Corollary 1.4.6 in Lean one must prove Proposition 1.4.5 for the definition `Singularity.HasLocalUniformization`, which uses the affine form of Volume 3, Proposition 4.1.6. That needs a link between the models of Volume 3, Definition 4.1.1, and the affine form, such as Proposition 4.1.6, and the library does not have it.

### The proofs of Theorem 1.4.1

The proof of Zariski [Zar40] is algebraic and works with valuations directly. It does not use the theorem of Hironaka, which came later and uses other methods. We do not give a summary of its steps here, because we cannot make one short and exact. The reader can find the method of Zariski for surfaces in [Cut04], which also contains a proof of resolution in characteristic 0. Sections 1.1 to 1.3 of this chapter follow the same ideas in the case of surfaces: quadratic transforms for $k(x, y)$, and a finite extension $K/k(x, y)$ that is unramified at the valuation.

There are two later proofs of Theorem 1.4.1 that go through general results.

1. The theorem of Temkin [Tem13] holds in each characteristic. In characteristic 0 each finite purely inseparable extension is trivial, so the theorem gives local uniformization of $v$ itself. Section 4.1 states the theorem and shows how it gives local uniformization. In characteristic 0 this is a second proof of Theorem 1.4.1.
2. Novacoski-Spivakovsky [NS14] reduce local uniformization to valuations of rank 1. Together with Lemma 1.4.2, this reduces the problem to valuations of rank 1 whose residue field is algebraic over the ground field. We do not state the precise hypotheses of [NS14] here.

### Patching

Volume 3, Proposition 4.1.2, shows that local uniformization in dimension $n$ gives finitely many models $X_1, \dots, X_m$ over a proper model $X$, such that each valuation has a regular center on at least one $X_i$. The proof uses the quasi-compactness of the Zariski-Riemann space, node SG0000000X, with the Lean proof `Singularity.ZariskiRiemann.compactSpace`. Zariski showed how to patch such a finite family into one resolution for surfaces and for threefolds in characteristic 0 [Zar44]. Piltant gives the patching argument in an axiomatic form [Pil]. In characteristic $p$ and dimension 4, the patching step is open even if local uniformization holds. This is Volume 9, Conjecture 2.3.2, node SG0000001J, stated in Lean as `Singularity.resolution_of_localUniformization_four`.

### Notes and references

The theorem of Zariski is [Zar40], and the patching theorem is [Zar44]. The theorem of Hironaka is [Hir64]. The reduction to rank 1 is [NS14]. Lemma 1.4.2, Corollary 1.4.3, Proposition 1.4.5 and Corollary 1.4.6 are not in the Lean library. The library proves the case $\operatorname{trdeg}_k K \le 1$ of Theorem 1.4.1 in each characteristic, in `Singularity.hasLocalUniformization_of_trdeg_le_one`, and the case of Volume 3, Proposition 4.1.8, in `Singularity.hasLocalUniformization_of_trdeg_le_trdeg_residueField_add_one`.
