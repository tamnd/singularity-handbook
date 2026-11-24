---
title: The Zariski-Riemann space
nodes: [SG0000000X]
sources: [ZS2, Zar40, Zar44, Tem13]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Zariski-Riemann space

Zariski collected all valuation rings of a function field into one topological space, which he called the Riemann manifold, and he used it in his work on resolution [Zar40, Zar44]. He proved its quasi-compactness in a separate short note of 1944. The main property of this space is quasi-compactness. It lets one pass from a local statement at each valuation to a statement about finitely many models. In this section we define the space and its topology, and we prove that it is quasi-compact.

### The space and its topology

**Definition 1.5.1 (Zariski-Riemann space).** Let $K$ be a field and let $A \subseteq K$ be a subring. The *Zariski-Riemann space* $\operatorname{ZR}(K/A)$ is the set of valuation rings $V$ of $K$ with $A \subseteq V$. For a finite subset $F \subseteq K$ let
$$U(F) = \{V \in \operatorname{ZR}(K/A) : F \subseteq V\}.$$
The *Zariski topology* on $\operatorname{ZR}(K/A)$ is the topology with the sets $U(F)$ as a basis of open sets.

The sets $U(F)$ form a basis of a topology, because $U(\emptyset)$ is the whole space and $U(F) \cap U(G) = U(F \cup G)$. If $B = A[f_1, \dots, f_n]$, then $U(\{f_1, \dots, f_n\}) = \operatorname{ZR}(K/B)$, so $\operatorname{ZR}(K/B)$ is an open subset of $\operatorname{ZR}(K/A)$. For a function field $K/k$, the space $\operatorname{ZR}(K/k)$ is the set of all valuations of $K/k$, up to equivalence.

The next proposition relates the space to the spectrum of a ring. For a subring $B \subseteq K$ we define the *center map* $c_B : \operatorname{ZR}(K/B) \to \operatorname{Spec} B$ by $c_B(V) = \mathfrak{m}_V \cap B$. If $\operatorname{Frac} B = K$, then $c_B(V)$ is the center of $V$ on $\operatorname{Spec} B$ by Lemma 1.4.2.

**Proposition 1.5.2.** Let $B \subseteq K$ be a subring. The center map $c_B$ is continuous and surjective.

Lean: none yet

*Proof.* Let $f \in B$ with $f \ne 0$. For $V \in \operatorname{ZR}(K/B)$ we have $f \in V$, so $f \notin \mathfrak{m}_V$ if and only if $f$ is a unit of $V$, that is, if and only if $f^{-1} \in V$. Thus $c_B^{-1}(D(f)) = U(\{f^{-1}\})$, which is open. Also $c_B^{-1}(D(0)) = \emptyset$. The sets $D(f)$ form a basis of $\operatorname{Spec} B$, so $c_B$ is continuous. Surjectivity is Corollary 1.3.3. $\square$

### Quasi-compactness

**Theorem 1.5.3 (Zariski).** Let $K$ be a field and let $A \subseteq K$ be a subring. Then $\operatorname{ZR}(K/A)$ is quasi-compact. In particular, for a function field $K/k$ the space $\operatorname{ZR}(K/k)$ is quasi-compact.

Node: SG0000000X · Lean: `Singularity.ZariskiRiemann.compactSpace` (planned, no Lean statement yet)

*Proof.* Let $2 = \{0, 1\}$ with the discrete topology, and let $P = 2^K$ be the set of all maps $K \to 2$ with the product topology. By the theorem of Tychonoff, $P$ is compact. A subset of $K$ is the same as its indicator function, so $\operatorname{ZR}(K/A)$ is a subset of $P$.

We show that $\operatorname{ZR}(K/A)$ is closed in $P$. Let $Z \subseteq P$ be a subset that is defined by a condition on finitely many coordinates. That is, there is a finite set $E \subseteq K$ and a set $T$ of maps $E \to 2$ such that $Z$ is the set of $\chi \in P$ with $\chi|_E \in T$. Then $Z$ is a finite union of basic open sets of $P$, and its complement is of the same form. So $Z$ is open and closed. A subset $V \subseteq K$ is in $\operatorname{ZR}(K/A)$ if and only if its indicator function $\chi$ satisfies these conditions.

1. $\chi(a) = 1$ for each $a \in A$. This includes $\chi(1) = 1$.
2. For all $x, y \in K$: if $\chi(x) = \chi(y) = 1$, then $\chi(x + y) = \chi(xy) = \chi(-x) = 1$.
3. For all $x \in K^\times$: $\chi(x) = 1$ or $\chi(x^{-1}) = 1$.

Conditions 1 and 2 say that $V$ is a subring of $K$ that contains $A$, and condition 3 says that it is a valuation ring of $K$. Each single condition, for one element $a$, one pair $(x, y)$ or one element $x$, involves at most five coordinates. So each single condition defines a closed subset of $P$. The set $\operatorname{ZR}(K/A)$ is the intersection of all these closed subsets, so it is closed in $P$. A closed subset of a compact space is compact. Thus $\operatorname{ZR}(K/A)$ is compact in the topology induced by $P$.

Now we compare the two topologies. For a finite $F \subseteq K$ the set $U(F)$ is the set of $V \in \operatorname{ZR}(K/A)$ whose indicator function is 1 at each point of $F$. This is the intersection of $\operatorname{ZR}(K/A)$ with a basic open set of $P$. So each open set of the Zariski topology is open in the topology induced by $P$. Let $\mathcal{U}$ be a cover of $\operatorname{ZR}(K/A)$ by Zariski open sets. These sets are open in the induced topology, so a finite subfamily of $\mathcal{U}$ covers $\operatorname{ZR}(K/A)$. $\square$

This is the theorem of Zariski in [ZS2, Chapter VI, Section 17, Theorem 40]. The induced topology of $P$ is the *patch topology* (or constructible topology) of $\operatorname{ZR}(K/A)$. It is Hausdorff and compact. The Zariski topology is not Hausdorff, except in trivial cases. For example, if $V \subsetneq W$ are valuation rings, then each open set that contains $V$ also contains $W$.

### Zariski-Riemann space and models

**Corollary 1.5.4.** Let $K/k$ be a function field. For each $v \in \operatorname{ZR}(K/k)$ let $B_v \subseteq \mathcal{O}_v$ be a finitely generated $k$-algebra with $\operatorname{Frac} B_v = K$, and let $G_v \subseteq \operatorname{Spec} B_v$ be an open set that contains the center of $v$. Then there are finitely many $v_1, \dots, v_m$ with this property: for each $w \in \operatorname{ZR}(K/k)$ there is an $i$ such that $w$ has a center on $\operatorname{Spec} B_{v_i}$ and this center lies in $G_{v_i}$.

Lean: none yet

*Proof.* Let $B_v = k[f_1, \dots, f_n]$. The set $\operatorname{ZR}(K/B_v) = U(\{f_1, \dots, f_n\})$ is open in $\operatorname{ZR}(K/k)$. By Proposition 1.5.2 the set $W_v = c_{B_v}^{-1}(G_v)$ is open in $\operatorname{ZR}(K/B_v)$, so it is open in $\operatorname{ZR}(K/k)$. It contains $v$. By Lemma 1.4.2, $W_v$ is the set of $w$ that have a center on $\operatorname{Spec} B_v$ and whose center lies in $G_v$. The sets $W_v$ cover $\operatorname{ZR}(K/k)$, and by Theorem 1.5.3 finitely many of them cover it. $\square$

This is the form in which quasi-compactness enters the method of Zariski. In Chapter 4, $\operatorname{Spec} B_v$ is an affine open set of a model on which $v$ has a regular center, and $G_v$ is its regular locus. The corollary then gives finitely many models such that each valuation has a regular center on one of them.

The space $\operatorname{ZR}(K/k)$ is also the inverse limit of all projective models of $K/k$, with the maps $v \mapsto c_X(v)$ of Proposition 1.4.4 [ZS2, Chapter VI, Section 17, Theorem 41]. We do not use this description. Temkin uses relative forms of the Zariski-Riemann space in his work on inseparable local uniformization [Tem13].
