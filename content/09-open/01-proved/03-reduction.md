---
title: The reduction to integral varieties
nodes: [SG0000001Y, SG0000000J]
sources: [Mat, Har, AM69, Stacks]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The reduction to integral varieties

A variety in our sense is reduced, but it can have several irreducible components. Most proofs of resolution, and the base, treat integral varieties only. This section proves that this is enough: a resolution of each component gives a resolution of the variety. The proof is standard and elementary, and the Lean development proves it with only the three standard axioms.

**Theorem 1.3.1 (reduction to integral varieties).** Let $p$ be $0$ or a prime and let $n \ge 0$. Assume that each integral variety of dimension at most $n$ over a field of characteristic $p$ has a resolution. Then $\mathrm{Res}(p, n)$ holds.

Node: SG0000001Y · Lean: `Singularity.Reduction.reductionToIntegral`

In Lean the statement is the proposition `Singularity.ReductionToIntegral`, and the theorem `reductionToIntegral` proves it. Some older theorems take `ReductionToIntegral` as an argument, for example the theorem of the base in Section 1.2. The new theorems apply them to `reductionToIntegral`, so they take no hypothesis. The mathematical proof is Proposition 1.3.3 below.

### Regular points lie on one component

We need one fact from commutative algebra.

**Theorem 1.3.2.** A regular local ring is a domain.

Node: SG0000000J · Lean: `Singularity.Algebra.isDomain_of_isRegularLocalRing`

Volume 1, Theorem 1.3.3 gives the full proof, and [Mat, Theorem 14.3] is the standard reference. Here is a summary. The proof is by induction on the dimension. Let $(R, \mathfrak{m})$ be regular of dimension $d > 0$, and choose $x \in \mathfrak{m} \setminus \mathfrak{m}^2$ that is not in any minimal prime of $R$. Then $R/(x)$ is regular of dimension $d - 1$, so it is a domain by induction, and $(x)$ is a prime ideal. Let $\mathfrak{p} \subseteq (x)$ be a minimal prime. Each $y \in \mathfrak{p}$ is $y = xz$, and $z \in \mathfrak{p}$ because $x \notin \mathfrak{p}$. Thus $\mathfrak{p} = x\mathfrak{p}$, and $\mathfrak{p} = 0$ by Nakayama's lemma.

Let $X$ be a Noetherian scheme and let $x \in X$. The minimal prime ideals of $\mathcal{O}_{X,x}$ correspond to the irreducible components of $X$ that contain $x$. If $\mathcal{O}_{X,x}$ is a domain, it has only one minimal prime ideal, $0$. Thus a regular point of $X$ lies on exactly one irreducible component of $X$. This is Volume 1, Corollary 1.3.4.

### The proof of the reduction

**Proposition 1.3.3.** Let $X$ be a variety over a field $k$, and let $X_1, \dots, X_r$ be its irreducible components, each with the reduced closed subscheme structure. Assume that each $X_i$ has a resolution $\pi_i : Y_i \to X_i$. Let $Y = Y_1 \sqcup \dots \sqcup Y_r$, and let $\pi : Y \to X$ be the map that is $\pi_i$ followed by the closed immersion $X_i \to X$ on $Y_i$. Then $\pi$ is a resolution of $X$.

Lean: `Singularity.Reduction.reductionToIntegral`

*Proof.* A variety is Noetherian, so it has finitely many irreducible components. Each $X_i$ is a closed subscheme of $X$, so it is separated and of finite type over $k$. It is reduced and irreducible, so it is integral, and $\dim X_i \le \dim X$. Thus the hypothesis of Theorem 1.3.1 applies to each $X_i$. For each $i$, let $V_i = X \setminus \bigcup_{j \ne i} X_j$. It is an open subset of $X$, it is contained in $X_i$, and the sets $V_i$ are pairwise disjoint.

*Step 1: the regular locus.* We show that
$$\operatorname{Reg}(X) = \bigcup_{i=1}^r \bigl(\operatorname{Reg}(X_i) \cap V_i\bigr).$$
Let $x \in V_i$. The open subscheme $V_i$ of $X$ is reduced and its underlying set lies in $X_i$. The reduced closed subscheme structure on a closed set is the unique reduced structure on it, so the open subscheme $V_i$ of $X_i$ is equal to the open subscheme $V_i$ of $X$. Thus $\mathcal{O}_{X,x} \cong \mathcal{O}_{X_i,x}$, and $x \in \operatorname{Reg}(X)$ if and only if $x \in \operatorname{Reg}(X_i)$. This gives the inclusion $\supseteq$. For $\subseteq$, let $x \in \operatorname{Reg}(X)$. By Theorem 1.3.2 and the remark after it, $x$ lies on exactly one component $X_i$, so $x \in V_i$, and the first argument gives $x \in \operatorname{Reg}(X_i)$.

The set $\operatorname{Reg}(X_i)$ is open in $X_i$, because $\pi_i$ is a resolution. Thus $R_i = \operatorname{Reg}(X_i) \cap V_i$ is open in $V_i$, so it is open in $X$, and $\operatorname{Reg}(X)$ is open in $X$. The sets $R_i$ are pairwise disjoint.

*Step 2: the four conditions.* The scheme $Y$ is regular, because each $Y_i$ is regular. Each $\pi_i$ is proper and each closed immersion is proper, so each restriction of $\pi$ to $Y_i$ is proper. By Lemma 1.3.5 below, a finite disjoint union of proper morphisms to $X$ is proper. Thus $\pi$ is proper.

For condition 3, note that $\pi(Y_j) \subseteq X_j$, and $X_j \cap R_i = \emptyset$ for $j \ne i$. Thus $\pi^{-1}(R_i) = \pi_i^{-1}(R_i) \subseteq Y_i$. The morphism $\pi_i$ is an isomorphism over $\operatorname{Reg}(X_i)$, so it is an isomorphism over the open subset $R_i$. The sets $R_i$ are disjoint and open, and their union is $\operatorname{Reg}(X)$. Thus $\pi$ is an isomorphism over $\operatorname{Reg}(X)$.

For condition 4 it is sufficient to show that $\pi_i^{-1}(R_i)$ is dense in $Y_i$ for each $i$. Let $D_i = \pi_i^{-1}(\operatorname{Reg}(X_i))$. It is open, and it is dense because $\pi_i$ is a resolution. Let $W \subseteq Y_i$ be a nonempty open set. Then $W \cap D_i$ is a nonempty open subset of $D_i$, and $\pi_i$ maps it isomorphically onto a nonempty open subset $W'$ of $X_i$. The set $X_i \setminus V_i = X_i \cap \bigcup_{j \ne i} X_j$ is a closed subset of $X_i$ that is not all of $X_i$, because the components are distinct. A proper closed subset of an irreducible space has empty interior. Thus $W'$ meets $V_i$, so $W'$ meets $R_i$, and $W$ meets $\pi_i^{-1}(R_i)$. $\square$

*Proof of Theorem 1.3.1 from Proposition 1.3.3.* Let $X$ be a variety of dimension at most $n$ over a field of characteristic $p$. Each component $X_i$ is an integral variety of dimension at most $n$ over the same field, so it has a resolution by assumption. Proposition 1.3.3 gives a resolution of $X$. $\square$


### An example

**Example 1.3.4 (two lines).** Let $k$ be a field and let $X \subset \mathbb{A}^2_k$ be the union of the two axes, $X = V(xy)$. Its components are $X_1 = V(y)$ and $X_2 = V(x)$, two copies of $\mathbb{A}^1_k$. They are regular, so $\pi_i = \mathrm{id}$ is a resolution of $X_i$. Proposition 1.3.3 gives the map $\pi : \mathbb{A}^1 \sqcup \mathbb{A}^1 \to X$. The local ring of $X$ at the origin is $k[x, y]_{(x,y)}/(xy)$. It is not a domain, because $x \cdot y = 0$, so by Theorem 1.3.2 it is not regular. This agrees with the computation of the embedding dimension: the maximal ideal needs the two generators $x$ and $y$, and the dimension is 1. Thus $\operatorname{Reg}(X) = X \setminus \{O\}$. The map $\pi$ is an isomorphism over this set, and the inverse image of this set is $Y$ minus two points, which is dense. The map $\pi$ is the normalization of $X$.

### The disjoint union of proper morphisms

The proof of Proposition 1.3.3 uses one lemma that the textbooks often leave to the reader.

**Lemma 1.3.5.** Let $X$ be a scheme, and let $g_i : Y_i \to X$, for $i = 1, \dots, r$, be proper morphisms. Let $Y = Y_1 \sqcup \dots \sqcup Y_r$ and let $g : Y \to X$ be the morphism that is $g_i$ on $Y_i$. Assume that $Y$ is quasi-separated. Then $g$ is proper.

Lean: `Singularity.Reduction.isProper_sigmaDesc`

*Proof.* We use the valuative criterion [Stacks, Tag 0BX5]. A morphism is proper if and only if it is quasi-compact, quasi-separated and locally of finite type, and each valuative square over it has exactly one lift.

The morphism $g$ is locally of finite type, because this property is local on the source. It is quasi-separated, because $Y$ is quasi-separated. It is quasi-compact: for a quasi-compact open $U \subseteq X$, the set $g^{-1}(U)$ is the union of the sets $g_i^{-1}(U)$, and a finite union of quasi-compact sets is quasi-compact.

Let $R$ be a valuation ring with field of fractions $K$, and consider a commutative square with $a : \operatorname{Spec} K \to Y$ on top and $b : \operatorname{Spec} R \to X$ at the bottom. The space $\operatorname{Spec} K$ has one point, so $a$ factors through one $Y_i$. Each $Y_i$ is open in $Y$, so we get a square over $g_i$, and it has a lift $\operatorname{Spec} R \to Y_i$ because $g_i$ is proper. This gives a lift over $g$. For uniqueness, let $l$ be a lift over $g$. Each $Y_j$ is open and closed in $Y$, so $l^{-1}(Y_i)$ is open and closed in $\operatorname{Spec} R$. It contains the image of $\operatorname{Spec} K$, so it is not empty. The space $\operatorname{Spec} R$ is connected, because $R$ is a domain. Thus $l$ factors through $Y_i$. Two lifts over $g$ thus give two lifts over $g_i$, and these are equal because $g_i$ is proper. $\square$

In Proposition 1.3.3 the scheme $Y$ is of finite type over $k$, so it is Noetherian and in particular quasi-separated.

### The Lean proof

The Lean proof follows the proof of Proposition 1.3.3. It has two files.

1. `Singularity/Scheme/Components.lean` gives each irreducible component $Z$ of a reduced Noetherian scheme $X$ the subscheme structure of Mathlib, and proves that this subscheme is reduced and integral. It proves that a point whose local ring is a domain lies on one component only. It also proves that the closed immersion $X_Z \to X$ is an isomorphism over the open set $V_Z$, the complement of the other components.
2. `Singularity/Scheme/Reduction.lean` proves Lemma 1.3.5 with the valuative criterion of Mathlib, and then Proposition 1.3.3. The proof of density uses the generic point of each component: it is in $V_Z$, so $V_Z$ meets each nonempty open subset of $X_Z$.

The Lean proof does not use the identification of Step 1 with the unique reduced structure. It uses the isomorphism over $V_Z$ and the isomorphism of local rings that it gives.

### Notes and references

For the correspondence between the minimal primes of a local ring and the components through the point, see [AM69, Chapter 3] and [Har, Section II.3]. For Theorem 1.3.2 see [Mat, Theorem 14.3]. For the valuative criterion of properness see [Stacks, Tag 0BX5] and [Har, Theorem II.4.7].
