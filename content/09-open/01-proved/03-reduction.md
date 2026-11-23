---
title: The reduction to integral varieties
nodes: [SG0000001Y, SG0000000J]
sources: [Mat, Har, AM69]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The reduction to integral varieties

A variety in our sense is reduced, but it can have several irreducible components. Most proofs of resolution, and the base, treat integral varieties only. This section proves that this is enough: a resolution of each component gives a resolution of the variety. The proof is standard and elementary. Its Lean proof is not yet written, so in Lean the statement is a named hypothesis, and each theorem that uses it takes it as an argument.

**Hypothesis 1.3.1 (reduction to integral varieties).** Let $p$ be $0$ or a prime and let $n \ge 0$. Assume that each integral variety of dimension at most $n$ over a field of characteristic $p$ has a resolution. Then $\mathrm{Res}(p, n)$ holds.

Node: SG0000001Y · Lean: `Singularity.ReductionToIntegral` (status: stated, the Lean proof is planned)

A named hypothesis is not an axiom. In Lean it is a definition of a proposition, `ReductionToIntegral : Prop`. A theorem that uses it has the form `ReductionToIntegral → ...`, so the dependency is visible in its statement, and the map of the project shows it. The mathematical proof is Proposition 1.3.3 below.

### Regular points lie on one component

We need one fact from commutative algebra.

**Theorem 1.3.2.** A regular local ring is a domain.

Node: SG0000000J · Lean: `Singularity.IsRegularLocalRing.isDomain` (status: planned in the project; the base has a Lean proof)

For a proof see [Mat, Theorem 14.3]. The proof is by induction on the dimension. Let $(R, \mathfrak{m})$ be regular of dimension $d > 0$, and choose $x \in \mathfrak{m} \setminus \mathfrak{m}^2$ that is not in any minimal prime of $R$. Then $R/(x)$ is regular of dimension $d - 1$, so it is a domain by induction, and $(x)$ is a prime ideal. Let $\mathfrak{p} \subseteq (x)$ be a minimal prime. Each $y \in \mathfrak{p}$ is $y = xz$, and $z \in \mathfrak{p}$ because $x \notin \mathfrak{p}$. Thus $\mathfrak{p} = x\mathfrak{p}$, and $\mathfrak{p} = 0$ by Nakayama's lemma.

Let $X$ be a Noetherian scheme and let $x \in X$. The minimal prime ideals of $\mathcal{O}_{X,x}$ correspond to the irreducible components of $X$ that contain $x$. If $\mathcal{O}_{X,x}$ is a domain, it has only one minimal prime ideal, $0$. Thus a regular point of $X$ lies on exactly one irreducible component of $X$.

### The proof of the reduction

**Proposition 1.3.3.** Let $X$ be a variety over a field $k$, and let $X_1, \dots, X_r$ be its irreducible components, each with the reduced closed subscheme structure. Assume that each $X_i$ has a resolution $\pi_i : Y_i \to X_i$. Let $Y = Y_1 \sqcup \dots \sqcup Y_r$, and let $\pi : Y \to X$ be the map that is $\pi_i$ followed by the closed immersion $X_i \to X$ on $Y_i$. Then $\pi$ is a resolution of $X$.

Lean: none yet. This is the planned proof of `Singularity.ReductionToIntegral`.

*Proof.* A variety is Noetherian, so it has finitely many irreducible components. Each $X_i$ is a closed subscheme of $X$, so it is separated and of finite type over $k$. It is reduced and irreducible, so it is integral, and $\dim X_i \le \dim X$. Thus the hypothesis of Hypothesis 1.3.1 applies to each $X_i$. For each $i$, let $V_i = X \setminus \bigcup_{j \ne i} X_j$. It is an open subset of $X$, it is contained in $X_i$, and the sets $V_i$ are pairwise disjoint.

*Step 1: the regular locus.* We show that
$$\operatorname{Reg}(X) = \bigcup_{i=1}^r \bigl(\operatorname{Reg}(X_i) \cap V_i\bigr).$$
Let $x \in V_i$. The open subscheme $V_i$ of $X$ is reduced and its underlying set lies in $X_i$. The reduced closed subscheme structure on a closed set is the unique reduced structure on it, so the open subscheme $V_i$ of $X_i$ is equal to the open subscheme $V_i$ of $X$. Thus $\mathcal{O}_{X,x} \cong \mathcal{O}_{X_i,x}$, and $x \in \operatorname{Reg}(X)$ if and only if $x \in \operatorname{Reg}(X_i)$. This gives the inclusion $\supseteq$. For $\subseteq$, let $x \in \operatorname{Reg}(X)$. By Theorem 1.3.2 and the remark after it, $x$ lies on exactly one component $X_i$, so $x \in V_i$, and the first argument gives $x \in \operatorname{Reg}(X_i)$.

The set $\operatorname{Reg}(X_i)$ is open in $X_i$, because $\pi_i$ is a resolution. Thus $R_i = \operatorname{Reg}(X_i) \cap V_i$ is open in $V_i$, so it is open in $X$, and $\operatorname{Reg}(X)$ is open in $X$. The sets $R_i$ are pairwise disjoint.

*Step 2: the four conditions.* The scheme $Y$ is regular, because each $Y_i$ is regular. Each $\pi_i$ is proper and each closed immersion is proper, so each restriction of $\pi$ to $Y_i$ is proper. A finite disjoint union of proper morphisms to $X$ is proper. Thus $\pi$ is proper.

For condition 3, note that $\pi(Y_j) \subseteq X_j$, and $X_j \cap R_i = \emptyset$ for $j \ne i$. Thus $\pi^{-1}(R_i) = \pi_i^{-1}(R_i) \subseteq Y_i$. The morphism $\pi_i$ is an isomorphism over $\operatorname{Reg}(X_i)$, so it is an isomorphism over the open subset $R_i$. The sets $R_i$ are disjoint and open, and their union is $\operatorname{Reg}(X)$. Thus $\pi$ is an isomorphism over $\operatorname{Reg}(X)$.

For condition 4 it is sufficient to show that $\pi_i^{-1}(R_i)$ is dense in $Y_i$ for each $i$. Let $D_i = \pi_i^{-1}(\operatorname{Reg}(X_i))$. It is open, and it is dense because $\pi_i$ is a resolution. Let $W \subseteq Y_i$ be a nonempty open set. Then $W \cap D_i$ is a nonempty open subset of $D_i$, and $\pi_i$ maps it isomorphically onto a nonempty open subset $W'$ of $X_i$. The set $X_i \setminus V_i = X_i \cap \bigcup_{j \ne i} X_j$ is a closed subset of $X_i$ that is not all of $X_i$, because the components are distinct. A proper closed subset of an irreducible space has empty interior. Thus $W'$ meets $V_i$, so $W'$ meets $R_i$, and $W$ meets $\pi_i^{-1}(R_i)$. $\square$

*Proof of Hypothesis 1.3.1 from Proposition 1.3.3.* Let $X$ be a variety of dimension at most $n$ over a field of characteristic $p$. Each component $X_i$ is an integral variety of dimension at most $n$ over the same field, so it has a resolution by assumption. Proposition 1.3.3 gives a resolution of $X$. $\square$

Thus Hypothesis 1.3.1 is true. We keep the word "hypothesis" because the project uses it for each statement whose Lean proof is not complete.

### An example

**Example 1.3.4 (two lines).** Let $k$ be a field and let $X \subset \mathbb{A}^2_k$ be the union of the two axes, $X = V(xy)$. Its components are $X_1 = V(y)$ and $X_2 = V(x)$, two copies of $\mathbb{A}^1_k$. They are regular, so $\pi_i = \mathrm{id}$ is a resolution of $X_i$. Proposition 1.3.3 gives the map $\pi : \mathbb{A}^1 \sqcup \mathbb{A}^1 \to X$. The local ring of $X$ at the origin is $k[x, y]_{(x,y)}/(xy)$. It is not a domain, because $x \cdot y = 0$, so by Theorem 1.3.2 it is not regular. This agrees with the computation of the embedding dimension: the maximal ideal needs the two generators $x$ and $y$, and the dimension is 1. Thus $\operatorname{Reg}(X) = X \setminus \{O\}$. The map $\pi$ is an isomorphism over this set, and the inverse image of this set is $Y$ minus two points, which is dense. The map $\pi$ is the normalization of $X$.

### What the Lean proof needs

The proof uses three constructions that are standard on paper, but each needs work in Lean: the finite set of irreducible components of a Noetherian scheme with the reduced structure, the finite disjoint union of schemes over $X$ with the proof that it is proper, and the identification of the local rings of $X$ and $X_i$ on $V_i$. Mathlib has parts of each. The project plans the Lean proof for a later milestone. Until then the map lists SG0000001Y as a hypothesis of each theorem that uses it.

### Notes and references

For the correspondence between the minimal primes of a local ring and the components through the point, see [AM69, Chapter 3] and [Har, Section II.3]. For Theorem 1.3.2 see [Mat, Theorem 14.3].
