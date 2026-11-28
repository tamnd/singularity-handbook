---
title: The Zariski-Riemann space
nodes: [SG0000000X]
sources: [ZS2, Zar40, Zar44, Zar44b, Tem13]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Zariski-Riemann space

Zariski collected all valuation rings of a function field into one topological space, which he called the Riemann manifold, and he used it in his work on resolution [Zar40, Zar44]. He proved its quasi-compactness in a separate short note [Zar44b]. The main property of this space is quasi-compactness. It lets one pass from a local statement at each valuation to a statement about finitely many models. In this section we define the space and its topology, and we prove that it is quasi-compact.

### The space and its topology

**Definition 1.5.1 (Zariski-Riemann space).** Let $K$ be a field and let $A \subseteq K$ be a subring. The *Zariski-Riemann space* $\operatorname{ZR}(K/A)$ is the set of valuation rings $V$ of $K$ with $A \subseteq V$. For a finite subset $F \subseteq K$ let
$$U(F) = \{V \in \operatorname{ZR}(K/A) : F \subseteq V\}.$$
The *Zariski topology* on $\operatorname{ZR}(K/A)$ is the topology with the sets $U(F)$ as a basis of open sets.

Lean: `Singularity.ZariskiRiemann`, `Singularity.ZariskiRiemann.basicOpen`

The sets $U(F)$ form a basis of a topology, because $U(\emptyset)$ is the whole space and $U(F) \cap U(G) = U(F \cup G)$. If $B = A[f_1, \dots, f_n]$, then $U(\{f_1, \dots, f_n\}) = \operatorname{ZR}(K/B)$, so $\operatorname{ZR}(K/B)$ is an open subset of $\operatorname{ZR}(K/A)$. For a function field $K/k$, the space $\operatorname{ZR}(K/k)$ is the set of all valuations of $K/k$, up to equivalence.

The next proposition relates the space to the spectrum of a ring. For a subring $B \subseteq K$ we define the *center map* $c_B : \operatorname{ZR}(K/B) \to \operatorname{Spec} B$ by $c_B(V) = \mathfrak{m}_V \cap B$. If $\operatorname{Frac} B = K$, then $c_B(V)$ is the center of $V$ on $\operatorname{Spec} B$ by Lemma 1.4.2.

**Proposition 1.5.2.** Let $B \subseteq K$ be a subring. The center map $c_B$ is continuous and surjective.

Lean: `Singularity.ZariskiRiemann.continuous_and_surjective_centerMap`

*Proof.* Let $f \in B$ with $f \ne 0$. For $V \in \operatorname{ZR}(K/B)$ we have $f \in V$, so $f \notin \mathfrak{m}_V$ if and only if $f$ is a unit of $V$, that is, if and only if $f^{-1} \in V$. Thus $c_B^{-1}(D(f)) = U(\{f^{-1}\})$, which is open. Also $c_B^{-1}(D(0)) = \emptyset$. The sets $D(f)$ form a basis of $\operatorname{Spec} B$, so $c_B$ is continuous. Surjectivity is Corollary 1.3.3. $\square$

### Quasi-compactness

**Theorem 1.5.3 (Zariski).** Let $K$ be a field and let $A \subseteq K$ be a subring. Then $\operatorname{ZR}(K/A)$ is quasi-compact. In particular, for a function field $K/k$ the space $\operatorname{ZR}(K/k)$ is quasi-compact.

Node: SG0000000X · Lean: `Singularity.ZariskiRiemann.compactSpace`

*Proof.* Let $2 = \{0, 1\}$ with the discrete topology, and let $P = 2^K$ be the set of all maps $K \to 2$ with the product topology. By the theorem of Tychonoff, $P$ is compact. A subset of $K$ is the same as its indicator function, so $\operatorname{ZR}(K/A)$ is a subset of $P$.

We show that $\operatorname{ZR}(K/A)$ is closed in $P$. Let $Z \subseteq P$ be a subset that is defined by a condition on finitely many coordinates. That is, there is a finite set $E \subseteq K$ and a set $T$ of maps $E \to 2$ such that $Z$ is the set of $\chi \in P$ with $\chi|_E \in T$. Then $Z$ is a finite union of basic open sets of $P$, and its complement is of the same form. So $Z$ is open and closed. A subset $V \subseteq K$ is in $\operatorname{ZR}(K/A)$ if and only if its indicator function $\chi$ satisfies these conditions.

1. $\chi(a) = 1$ for each $a \in A$. This includes $\chi(1) = 1$.
2. For all $x, y \in K$: if $\chi(x) = \chi(y) = 1$, then $\chi(x + y) = \chi(xy) = \chi(-x) = 1$.
3. For all $x \in K^\times$: $\chi(x) = 1$ or $\chi(x^{-1}) = 1$.

Conditions 1 and 2 say that $V$ is a subring of $K$ that contains $A$, and condition 3 says that it is a valuation ring of $K$. Each single condition, for one element $a$, one pair $(x, y)$ or one element $x$, involves at most five coordinates. So each single condition defines a closed subset of $P$. The set $\operatorname{ZR}(K/A)$ is the intersection of all these closed subsets, so it is closed in $P$. A closed subset of a compact space is compact. Thus $\operatorname{ZR}(K/A)$ is compact in the topology induced by $P$.

Now we compare the two topologies. For a finite $F \subseteq K$ the set $U(F)$ is the set of $V \in \operatorname{ZR}(K/A)$ whose indicator function is 1 at each point of $F$. This is the intersection of $\operatorname{ZR}(K/A)$ with a basic open set of $P$. So each open set of the Zariski topology is open in the topology induced by $P$. Let $\mathcal{U}$ be a cover of $\operatorname{ZR}(K/A)$ by Zariski open sets. These sets are open in the induced topology, so a finite subfamily of $\mathcal{U}$ covers $\operatorname{ZR}(K/A)$. $\square$

This is the theorem of Zariski in [ZS2, Chapter VI, Section 17, Theorem 40]. The induced topology of $P$ is the *patch topology* (or constructible topology) of $\operatorname{ZR}(K/A)$. It is Hausdorff and compact. The Zariski topology is not Hausdorff, except in trivial cases. For example, if $V \subsetneq W$ are valuation rings, then each open set that contains $V$ also contains $W$.

The Lean proof of Theorem 1.5.3 uses ultrafilters in place of the theorem of Tychonoff. The two arguments are the same in substance. Let $\mathcal{U}$ be an ultrafilter on $\operatorname{ZR}(K/A)$, and let $V$ be the set of the elements $x \in K$ such that the set of the points that contain $x$ is in $\mathcal{U}$. Each of the three conditions above holds for the indicator function of $V$, because each condition involves finitely many sets and an ultrafilter is closed under finite intersections. For $x \ne 0$, each point contains $x$ or $x^{-1}$, so one of the two sets is in $\mathcal{U}$. Thus $V$ is a valuation ring that contains $A$, and $\mathcal{U}$ converges to $V$ in the Zariski topology. A space in which each ultrafilter converges is quasi-compact. In Lean, $A$ is a ring with a homomorphism to $K$, and $V$ contains the image of $A$. The proof is in `Singularity/Valuation/ZariskiRiemann.lean`.

### Zariski-Riemann space and models

**Corollary 1.5.4.** Let $K/k$ be a function field. For each $v \in \operatorname{ZR}(K/k)$ let $B_v \subseteq \mathcal{O}_v$ be a finitely generated $k$-algebra with $\operatorname{Frac} B_v = K$, and let $G_v \subseteq \operatorname{Spec} B_v$ be an open set that contains the center of $v$. Then there are finitely many $v_1, \dots, v_m$ with this property: for each $w \in \operatorname{ZR}(K/k)$ there is an $i$ such that $w$ has a center on $\operatorname{Spec} B_{v_i}$ and this center lies in $G_{v_i}$.

Lean: `Singularity.ZariskiRiemann.exists_finset_forall_exists_centerMap_mem` (without the hypothesis $\operatorname{Frac} B_v = K$)

*Proof.* Let $B_v = k[f_1, \dots, f_n]$. The set $\operatorname{ZR}(K/B_v) = U(\{f_1, \dots, f_n\})$ is open in $\operatorname{ZR}(K/k)$. By Proposition 1.5.2 the set $W_v = c_{B_v}^{-1}(G_v)$ is open in $\operatorname{ZR}(K/B_v)$, so it is open in $\operatorname{ZR}(K/k)$. It contains $v$. By Lemma 1.4.2, $W_v$ is the set of $w$ that have a center on $\operatorname{Spec} B_v$ and whose center lies in $G_v$. The sets $W_v$ cover $\operatorname{ZR}(K/k)$, and by Theorem 1.5.3 finitely many of them cover it. $\square$

This is the form in which quasi-compactness enters the method of Zariski. In Chapter 4, $\operatorname{Spec} B_v$ is an affine open set of a model on which $v$ has a regular center, and $G_v$ is its regular locus. The corollary then gives finitely many models such that each valuation has a regular center on one of them.

### Specialization and the projective line

The Zariski topology on $\operatorname{ZR}(K/A)$ is far from Hausdorff. The next proposition says exactly which points lie in the closure of a point. It shows that a coarsening of a valuation is a generization of it, in the sense of topology.

**Proposition 1.5.5.** Let $V \in \operatorname{ZR}(K/A)$. The closure of $\{V\}$ in $\operatorname{ZR}(K/A)$ is the set of $W \in \operatorname{ZR}(K/A)$ with $W \subseteq V$. In particular $\operatorname{ZR}(K/A)$ is a $T_0$ space.

Lean: `Singularity.ZariskiRiemann.mem_closure_singleton_iff`, `Singularity.ZariskiRiemann.closure_singleton`, `Singularity.ZariskiRiemann.instT0Space`

*Proof.* A point $W$ lies in the closure of $\{V\}$ if and only if each basic open set that contains $W$ also contains $V$. Let $W \subseteq V$, and let $U(F)$ contain $W$. Then $F \subseteq W \subseteq V$, so $V \in U(F)$. Thus $W$ lies in the closure. Conversely, let $W \not\subseteq V$, and choose $f \in W \setminus V$. Then $U(\{f\})$ contains $W$ and does not contain $V$. So $W$ does not lie in the closure. For the last claim, let $V \ne W$. Then $V \not\subseteq W$ or $W \not\subseteq V$, and the open set $U(\{f\})$ above separates the two points in one direction. $\square$

So the closed points of $\operatorname{ZR}(K/A)$ are the valuation rings that are minimal for inclusion, and the trivial valuation ring $K$ is a generic point: it lies in each nonempty open set. The points $W$ with $V$ in the closure of $\{W\}$ are the rings $W \supseteq V$, and they correspond to the primes of $V$. Let $V \subseteq W \subseteq K$, and let $\mathfrak{p} = \mathfrak{m}_W \cap V$. Then $V_\mathfrak{p} \subseteq W$, because the elements of $V \setminus \mathfrak{p}$ are units of $W$. Let $x \in W \setminus V$. Then $1/x \in V$, and $1/x$ is a unit of $W$, so $1/x \in V \setminus \mathfrak{p}$ and $x \in V_\mathfrak{p}$. Thus $W = V_\mathfrak{p}$. So the rings between $V$ and $K$ are the localizations of $V$ at its primes. By Proposition 1.2.3 they form a chain, and for $V$ of finite rank $t$ the chain has $t + 1$ members.

**Example 1.5.6 ($\operatorname{ZR}(k(x)/k)$ is the projective line).** Let $k$ be a field and $K = k(x)$. We list the valuation rings $V$ of $K$ with $k \subseteq V$. Assume $V \ne K$. If $x \in V$, then $k[x] \subseteq V$, and $\mathfrak{p} = \mathfrak{m}_V \cap k[x]$ is a prime of $k[x]$. If $\mathfrak{p} = 0$, then each nonzero polynomial is a unit of $V$, so $V = K$, which is false. So $\mathfrak{p} = (P)$ for a monic irreducible polynomial $P$, and $V$ dominates the discrete valuation ring $k[x]_{(P)}$. By Step 3 of the proof of Theorem 1.3.2, $V = k[x]_{(P)}$. If $x \notin V$, then $1/x \in \mathfrak{m}_V$, and the same argument with $k[1/x]$ gives $V = k[1/x]_{(1/x)}$. Thus $\operatorname{ZR}(K/k)$ consists of $K$, the rings $k[x]_{(P)}$, and the ring $k[1/x]_{(1/x)}$ of Example 1.4.6.

Lean: `Singularity.valuationSubring_ratFunc_trichotomy`, `Singularity.toLocalSubring_eq_ofPrime_centerIdeal` (the list of the valuation rings of $k(x)$ that contain $k$). The bijection with the points of $\mathbb{P}^1$ and the topology are not in Lean yet.

The map $V \mapsto c_{\mathbb{P}^1}(V)$ of Proposition 1.4.4 is a bijection from $\operatorname{ZR}(K/k)$ to the set of points of $\mathbb{P}^1_k$. It sends $K$ to the generic point, $k[x]_{(P)}$ to the closed point $V(P)$ of $\mathbb{A}^1_k$, and $k[1/x]_{(1/x)}$ to $\infty$. The map is a homeomorphism. Indeed, the nonempty open sets of $\mathbb{P}^1_k$ are the complements of finite sets of closed points. For $f \in K$, the set $U(\{f\})$ is the set of points where $f$ has no pole, which is such a complement, and so $U(F)$ is open in $\mathbb{P}^1_k$ for each finite $F$. Conversely, the function $1/P_i$ has its only pole at $V(P_i)$, since $1/P_i$ has positive value at $\infty$. So the complement of $V(P_1) \cup \dots \cup V(P_m)$ in $\mathbb{P}^1_k$ is $U(\{1/P_1, \dots, 1/P_m\})$, and the complement of these points and $\infty$ is $U(\{x, 1/P_1, \dots, 1/P_m\})$. In dimension 2 no single model gives $\operatorname{ZR}(K/k)$ in this way. For $K = k(x, y)$, the monomial valuations of Example 1.6.2 with weights $(a, b)$ and $(a', b')$ coprime and $(a, b) \ne (a', b')$ are not equivalent. Indeed, both have value group $\mathbb{Z}$, the only order automorphism of $\mathbb{Z}$ is the identity, and the two valuations differ on $x$ or on $y$. They all have center at the origin of $\mathbb{A}^2_k$, and so at the same point of $\mathbb{P}^2_k$. Thus the center map $c_{\mathbb{P}^2_k}$ is not injective.

The space $\operatorname{ZR}(K/k)$ is also the inverse limit of all projective models of $K/k$, with the maps $v \mapsto c_X(v)$ of Proposition 1.4.4 [ZS2, Chapter VI, Section 17]. We do not use this description. Temkin uses relative forms of the Zariski-Riemann space in his work on inseparable local uniformization [Tem13].
