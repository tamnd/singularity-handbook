---
title: The extension theorem of Chevalley
nodes: []
sources: [ZS2, Stacks]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The extension theorem of Chevalley

In this section we prove that each local subring of a field is dominated by a valuation ring. This theorem gives the existence of valuations with a prescribed center, and it is the main tool to construct valuations.

**Definition 1.3.1 (domination).** Let $A$ and $B$ be local subrings of a field $K$. Then $B$ *dominates* $A$ if $A \subseteq B$ and $\mathfrak{m}_B \cap A = \mathfrak{m}_A$.

Domination is a partial order on the set of local subrings of $K$. If $A \subseteq B$ are local, then $B$ dominates $A$ if and only if $\mathfrak{m}_A \subseteq \mathfrak{m}_B$, because $\mathfrak{m}_B \cap A$ is a proper ideal of $A$ and so it is contained in $\mathfrak{m}_A$.

**Theorem 1.3.2 (Chevalley).** Let $K$ be a field and let $A \subseteq K$ be a local subring. Then there is a valuation ring of $K$ that dominates $A$. The valuation rings of $K$ are exactly the local subrings of $K$ that are maximal for domination.

Lean: `LocalSubring.exists_le_valuationSubring` (in Mathlib, for the first claim)

*Proof.* We prove three claims.

Step 1: a maximal element exists. Let $\Sigma$ be the set of local subrings of $K$ that dominate $A$. It contains $A$. Let $(B_i)_{i \in I}$ be a nonempty chain in $\Sigma$, and let $B = \bigcup_i B_i$ and $\mathfrak{n} = \bigcup_i \mathfrak{m}_{B_i}$. Since the $B_i$ form a chain, $B$ is a ring and $\mathfrak{n}$ is an ideal of $B$. If $j \ge i$ in the chain, then $\mathfrak{m}_{B_j} \cap B_i = \mathfrak{m}_{B_i}$. Let $x \in \mathfrak{m}_{B_i}$. If $x$ is a unit of $B$, then $x^{-1} \in B_j$ for some $j \ge i$, and $x \in \mathfrak{m}_{B_j}$ is a unit of $B_j$, which is false. Let $x \in B \setminus \mathfrak{n}$. Then $x \in B_i \setminus \mathfrak{m}_{B_i}$ for some $i$, so $x$ is a unit of $B_i$ and of $B$. Thus $\mathfrak{n}$ is the set of nonunits of $B$, so $B$ is local with maximal ideal $\mathfrak{n}$. Also $\mathfrak{n} \cap B_i = \mathfrak{m}_{B_i}$, so $B$ dominates each $B_i$, and $B \in \Sigma$. By the lemma of Zorn, $\Sigma$ has a maximal element $V$. It is maximal among all local subrings of $K$ for domination, since a local ring that dominates $V$ also dominates $A$.

Step 2: $V$ is a valuation ring. Let $x \in K^\times$. First we show: if $x \notin V$, then $\mathfrak{m}_V V[x] = V[x]$. Assume the contrary. Then $\mathfrak{m}_V V[x]$ is contained in a maximal ideal $\mathfrak{n}$ of $V[x]$. The ideal $\mathfrak{n} \cap V$ contains $\mathfrak{m}_V$ and does not contain $1$, so it is $\mathfrak{m}_V$. The local ring $V[x]_\mathfrak{n} \subseteq K$ contains $V$, and its maximal ideal meets $V$ in $\mathfrak{n} \cap V = \mathfrak{m}_V$. Thus $V[x]_\mathfrak{n}$ dominates $V$, so it equals $V$ by maximality, and $x \in V$. This is a contradiction.

Now assume that $x \notin V$ and $x^{-1} \notin V$. By the first part there are relations
$$1 = a_0 + a_1x + \dots + a_nx^n, \qquad 1 = b_0 + b_1x^{-1} + \dots + b_kx^{-k}$$
with all $a_i, b_j \in \mathfrak{m}_V$. Choose such relations with $n$ and $k$ as small as possible. Since $x$ and $x^{-1}$ play the same role, we may assume $n \ge k$. Also $n \ge 1$, since $1 \notin \mathfrak{m}_V$. The element $1 - b_0$ is a unit of $V$. Let $c_j = b_j/(1 - b_0) \in \mathfrak{m}_V$. Then $1 = c_1x^{-1} + \dots + c_kx^{-k}$, and we multiply by $x^n$:
$$x^n = c_1x^{n-1} + \dots + c_kx^{n-k}.$$
We put this into the first relation. We get $1 = a_0 + a_1x + \dots + a_{n-1}x^{n-1} + a_n(c_1x^{n-1} + \dots + c_kx^{n-k})$. This is a relation of degree at most $n - 1$ with coefficients in $\mathfrak{m}_V$, which contradicts the choice of $n$. So $x \in V$ or $x^{-1} \in V$.

Step 3: each valuation ring is maximal. Let $W$ be a valuation ring of $K$ and let $B$ be a local subring that dominates $W$. Let $x \in B$. If $x \notin W$, then $x^{-1} \in W$, and $x^{-1}$ is not a unit of $W$. So $x^{-1} \in \mathfrak{m}_W \subseteq \mathfrak{m}_B$. But $x^{-1}$ is a unit of $B$, because $x \in B$. This is a contradiction, so $B = W$.

Steps 1 and 2 give the first claim. Steps 2 and 3 give the second claim: a maximal local subring is the ring $V$ of Step 1 for $A = V$, so it is a valuation ring. $\square$

This is [ZS2, Chapter VI, Section 4] and [Stacks, Tag 00IA]. The proof uses the axiom of choice. The valuation ring is not unique in general, and the examples of Section 1.6 give many valuation rings that dominate the same local ring.

**Corollary 1.3.3.** Let $K$ be a field, let $A \subseteq K$ be a subring and let $\mathfrak{p}$ be a prime ideal of $A$. Then there is a valuation ring $V$ of $K$ with $A \subseteq V$ and $\mathfrak{m}_V \cap A = \mathfrak{p}$.

Lean: none yet

*Proof.* The ring $A$ is a domain, and $A_\mathfrak{p}$ is a local subring of $K$. By Theorem 1.3.2 there is a valuation ring $V$ that dominates $A_\mathfrak{p}$. Then $\mathfrak{m}_V \cap A = \mathfrak{m}_V \cap A_\mathfrak{p} \cap A = \mathfrak{p}A_\mathfrak{p} \cap A = \mathfrak{p}$. $\square$

**Corollary 1.3.4.** Let $K$ be a field and let $A \subseteq K$ be a subring. The integral closure of $A$ in $K$ is the intersection of the valuation rings of $K$ that contain $A$.

Lean: `iInf_valuationSubring_superset` (in Mathlib)

*Proof.* Let $V$ be a valuation ring with $A \subseteq V$. By Lemma 1.1.8, $V$ is integrally closed, so it contains the integral closure of $A$. Conversely, let $x \in K$ be not integral over $A$. Then $x \ne 0$. Let $y = x^{-1}$. We claim that $y$ is not a unit of $A[y]$. Otherwise $1 = y(c_0 + c_1y + \dots + c_my^m)$ with $c_i \in A$. We multiply by $x^{m+1}$ and get $x^{m+1} = c_0x^m + c_1x^{m-1} + \dots + c_m$, so $x$ is integral over $A$, which is false. Thus $y$ lies in a maximal ideal $\mathfrak{n}$ of $A[y]$. By Corollary 1.3.3 there is a valuation ring $V$ with $A[y] \subseteq V$ and $\mathfrak{m}_V \cap A[y] = \mathfrak{n}$. Then $y \in \mathfrak{m}_V$, so $x = y^{-1} \notin V$. $\square$

In particular an integrally closed domain is the intersection of the valuation rings of its field of fractions that contain it. In Mathlib this is `Subring.eq_iInf_of_isIntegrallyClosedIn`.

### Extension to a larger field

**Corollary 1.3.5.** Let $L/K$ be a field extension and let $v$ be a valuation of $K$. Then there is a valuation $w$ of $L$ whose restriction to $K$ is equivalent to $v$.

Lean: none yet

*Proof.* The ring $\mathcal{O}_v$ is a local subring of $L$. By Theorem 1.3.2 there is a valuation ring $W$ of $L$ that dominates $\mathcal{O}_v$. The ring $W \cap K$ is a valuation ring of $K$, it contains $\mathcal{O}_v$, and its maximal ideal $\mathfrak{m}_W \cap K$ meets $\mathcal{O}_v$ in $\mathfrak{m}_v$. So $W \cap K$ dominates $\mathcal{O}_v$, and $W \cap K = \mathcal{O}_v$ by Step 3 of the proof of Theorem 1.3.2. The valuation $w = v_W$ restricts to a valuation of $K$ with ring $W \cap K = \mathcal{O}_v$. By Theorem 1.1.7 this restriction is equivalent to $v$. $\square$

When $w$ extends $v$, we identify $\Gamma_v$ with a subgroup of $\Gamma_w$, and $Kv$ with a subfield of $Lw$. We write $(L/K, w)$ for this situation, and we call $w$ an *extension* of $v$.
