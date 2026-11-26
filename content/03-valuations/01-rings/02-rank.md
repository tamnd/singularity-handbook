---
title: Rank and rational rank
nodes: []
sources: [ZS2]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Rank and rational rank

The value group of a valuation has two numerical invariants. The rank counts the convex subgroups, and it is the dimension of the valuation ring. The rational rank is the dimension of the group over $\mathbb{Q}$. The Abhyankar inequality of Chapter 2 bounds the rational rank, and so it bounds the rank too.

### Convex subgroups

**Definition 1.2.1 (convex subgroup, rank, rational rank).** Let $\Gamma$ be an ordered group. A subgroup $\Delta \subseteq \Gamma$ is *convex* if $0 \le \gamma \le \delta$ and $\delta \in \Delta$ imply $\gamma \in \Delta$. The *rank* of $\Gamma$ is the number of convex subgroups $\Delta \ne \Gamma$, if this number is finite. The *rational rank* of $\Gamma$ is $\operatorname{rr} \Gamma = \dim_\mathbb{Q} (\Gamma \otimes_\mathbb{Z} \mathbb{Q})$. The rank and the rational rank of a valuation $v$ are those of $\Gamma_v$.

Since $\Gamma$ is torsion free, $\operatorname{rr} \Gamma$ is the largest number of elements of $\Gamma$ that are linearly independent over $\mathbb{Z}$. The group $\mathbb{Z}$ has rank 1 and rational rank 1. The group $\mathbb{Z}^2$ with the lexicographic order has the convex subgroups $0$, $0 \times \mathbb{Z}$ and $\mathbb{Z}^2$, so it has rank 2 and rational rank 2. A subgroup $\Gamma \ne 0$ of $\mathbb{R}$ has rank 1. Indeed, let $\Delta \ne 0$ be a convex subgroup, and let $\delta \in \Delta$ with $\delta > 0$. For each $\gamma \in \Gamma$ there is an integer $n$ with $|\gamma| \le n\delta$, so $\gamma \in \Delta$. The group $\mathbb{Z} + \mathbb{Z}\sqrt{2} \subseteq \mathbb{R}$ thus has rank 1 and rational rank 2.

**Lemma 1.2.2.** The convex subgroups of an ordered group $\Gamma$ are totally ordered by inclusion.

Lean: `Singularity.IsConvexSubgroup.le_or_le`

*Proof.* Let $\Delta, \Delta'$ be convex subgroups with $\Delta \not\subseteq \Delta'$. Choose $\delta \in \Delta \setminus \Delta'$. We may assume $\delta > 0$, because we can replace $\delta$ by $-\delta$. Let $\delta' \in \Delta'$ with $\delta' \ge 0$. If $\delta \le \delta'$, then $\delta \in \Delta'$ by convexity, which is false. So $0 \le \delta' < \delta$, and $\delta' \in \Delta$ by convexity. Each element of $\Delta'$ is $\pm\delta'$ with $\delta' \ge 0$, so $\Delta' \subseteq \Delta$. $\square$

### Prime ideals and convex subgroups

**Proposition 1.2.3.** Let $V$ be a valuation ring of $K$ with valuation $v$ and value group $\Gamma$. For a prime ideal $\mathfrak{p}$ of $V$, let $\Delta_\mathfrak{p}$ be the set of $\gamma \in \Gamma$ such that $\gamma = v(x)$ or $\gamma = -v(x)$ for some $x \in V \setminus \mathfrak{p}$. For a convex subgroup $\Delta$ of $\Gamma$, let $\mathfrak{p}_\Delta$ be the set of $x \in V$ such that $v(x) > \delta$ for each $\delta \in \Delta$. Then $\mathfrak{p} \mapsto \Delta_\mathfrak{p}$ and $\Delta \mapsto \mathfrak{p}_\Delta$ are inverse bijections between the prime ideals of $V$ and the convex subgroups of $\Gamma$. They reverse inclusion.

Lean: `ValuationSubring.primeSpectrumOrderEquiv` (in Mathlib, in the form of primes and rings between $V$ and $K$), `Singularity.primeSpectrumEquivConvexSubgroup` (the bijection with the convex subgroups)

*Proof.* Let $\mathfrak{p}$ be a prime ideal and let $S = v(V \setminus \mathfrak{p}) \subseteq \Gamma_{\ge 0}$. If $x \in V \setminus \mathfrak{p}$ and $y \in V$ with $0 \le v(y) \le v(x)$, then $x = (x/y)y$ with $x/y \in V$, so $y \notin \mathfrak{p}$. Thus $S$ is closed downwards in $\Gamma_{\ge 0}$. Since $\mathfrak{p}$ is prime, $S$ is closed under addition. Now $\Delta_\mathfrak{p} = S \cup (-S)$. This set is closed under negation and contains $0$. Let $\alpha, \beta \in S$. Then $\alpha + \beta \in S$, and $|\alpha - \beta| \le \max(\alpha, \beta)$, so $|\alpha - \beta| \in S$. Thus $\Delta_\mathfrak{p}$ is a subgroup. It is convex, because $S$ is closed downwards.

Let $\Delta$ be a convex subgroup. The set $\mathfrak{p}_\Delta$ is an ideal of $V$: if $v(x) > \Delta$ and $y \in V$, then $v(xy) \ge v(x) > \Delta$, and if $v(x), v(y) > \Delta$, then $v(x + y) > \Delta$. It does not contain $1$, because $0 \in \Delta$. Let $x, y \in V \setminus \mathfrak{p}_\Delta$. Then $0 \le v(x) \le \delta$ for some $\delta \in \Delta$, so $v(x) \in \Delta$ by convexity. In the same way $v(y) \in \Delta$, so $v(xy) \in \Delta$. The condition $v(xy) > \delta$ fails for $\delta = v(xy) \in \Delta$, so $xy \notin \mathfrak{p}_\Delta$. Thus $\mathfrak{p}_\Delta$ is prime. We also proved that $V \setminus \mathfrak{p}_\Delta = \{x \in V : v(x) \in \Delta\}$.

From the last fact, $v(V \setminus \mathfrak{p}_\Delta) = \Delta \cap \Gamma_{\ge 0}$, so $\Delta_{\mathfrak{p}_\Delta} = \Delta$. Conversely, let $\mathfrak{p}$ be prime and $x \in V$. If $x \notin \mathfrak{p}$, then $v(x) \in \Delta_\mathfrak{p}$, so $x \notin \mathfrak{p}_{\Delta_\mathfrak{p}}$. If $x \in \mathfrak{p}$, then $v(x) > \delta$ for each $\delta \in S$, since otherwise $x \notin \mathfrak{p}$ because $S$ is closed downwards. So $x \in \mathfrak{p}_{\Delta_\mathfrak{p}}$. Thus $\mathfrak{p}_{\Delta_\mathfrak{p}} = \mathfrak{p}$. Both maps clearly reverse inclusion. $\square$

The prime $\mathfrak{m}_V$ corresponds to $\Delta = 0$, and the prime $0$ corresponds to $\Delta = \Gamma$.

**Corollary 1.2.4.** Let $v$ be a valuation of finite rank. Then $\dim \mathcal{O}_v$ is the rank of $v$.

Lean: `Singularity.ringKrullDim_eq_natCard_convexSubgroup_sub_one` (for finitely many convex subgroups)

*Proof.* By Lemma 1.2.2 and Proposition 1.2.3, the prime ideals of $\mathcal{O}_v$ form a chain with as many elements as there are convex subgroups. If the rank is $t$, there are $t + 1$ convex subgroups, so there are $t + 1$ primes, and the longest chain of primes has length $t$. $\square$

### The rank is at most the rational rank

**Proposition 1.2.5.** Let $\Gamma$ be an ordered group with $\operatorname{rr} \Gamma = r < \infty$. Then $\Gamma$ has at most $r + 1$ convex subgroups. In particular, the rank of $\Gamma$ is at most $r$.

Lean: `Singularity.IsConvexSubgroup.finite_and_card_le`

*Proof.* Let $\Delta_0 \subsetneq \Delta_1 \subsetneq \dots \subsetneq \Delta_t$ be convex subgroups. For $1 \le i \le t$ choose $\delta_i \in \Delta_i \setminus \Delta_{i-1}$ with $\delta_i > 0$. We show that $\delta_1, \dots, \delta_t$ are linearly independent over $\mathbb{Z}$. Assume that $\sum n_i\delta_i = 0$ with integers $n_i$ that are not all 0, and let $j$ be the largest index with $n_j \ne 0$. Then $n_j\delta_j = -\sum_{i < j} n_i\delta_i \in \Delta_{j-1}$, so $|n_j|\delta_j \in \Delta_{j-1}$. Since $0 < \delta_j \le |n_j|\delta_j$, convexity gives $\delta_j \in \Delta_{j-1}$, which is false. Thus $t \le r$, and a chain of convex subgroups has at most $r + 1$ members. By Lemma 1.2.2 all convex subgroups form one chain. $\square$

The rank can be smaller than the rational rank, as the group $\mathbb{Z} + \mathbb{Z}\sqrt{2}$ shows. A valuation is *discrete of rank 1* if $\Gamma_v \cong \mathbb{Z}$ as ordered groups. Then $\mathcal{O}_v$ is a discrete valuation ring: if $v(\pi) = 1$, each nonzero ideal of $\mathcal{O}_v$ is $(\pi^n)$ for some $n \ge 0$. By part 5 of Lemma 1.1.8, each Noetherian valuation ring that is not a field arises in this way. An ordered group of rank 1 is isomorphic to a subgroup of $\mathbb{R}$, by a theorem of Hölder [ZS2, Chapter VI]. We do not use this fact.

### Rank 1 and the archimedean property

An ordered group $\Gamma$ is *archimedean* if for all $\alpha, \beta \in \Gamma$ with $\alpha > 0$ there is an integer $n \ge 1$ with $\beta \le n\alpha$. The next lemma gives the usual test for rank 1. We use it in Section 3.1.

**Lemma 1.2.6.** Let $\Gamma \ne 0$ be an ordered group. Then $\Gamma$ has rank 1 if and only if $\Gamma$ is archimedean.

Lean: `Singularity.rankOne_iff_mulArchimedean`

*Proof.* For $\alpha \in \Gamma$ with $\alpha > 0$, let $\Delta_\alpha$ be the set of $\gamma \in \Gamma$ with $|\gamma| \le n\alpha$ for some integer $n \ge 1$. In an ordered abelian group, $|\gamma + \gamma'| \le |\gamma| + |\gamma'|$. So $\Delta_\alpha$ is a subgroup. It is convex by its definition, and it contains $\alpha$. Assume that $\Gamma$ has rank 1. Then the convex subgroups are $0$ and $\Gamma$, so $\Delta_\alpha = \Gamma$ for each $\alpha > 0$. This is the archimedean property. Conversely, assume that $\Gamma$ is archimedean, and let $\Delta \ne 0$ be a convex subgroup. Choose $\alpha \in \Delta$ with $\alpha > 0$. For $\gamma \in \Gamma$ there is $n$ with $|\gamma| \le n\alpha$, and $n\alpha \in \Delta$. By convexity $|\gamma| \in \Delta$, so $\gamma \in \Delta$. Thus $\Delta = \Gamma$, and the rank is 1. $\square$

The argument for subgroups of $\mathbb{R}$ above is the case of this lemma for an archimedean group. A subgroup of finite index in an archimedean group is archimedean. Conversely, let $\Gamma' \supseteq \Gamma$ be ordered groups with $\Gamma'/\Gamma$ finite of order $m$, and let $\Gamma$ be archimedean. For $\alpha, \beta \in \Gamma'$ with $\alpha > 0$, the elements $m\alpha$ and $m\beta$ are in $\Gamma$, so $m\beta \le nm\alpha$ for some $n$, and then $\beta \le n\alpha$. So $\Gamma'$ is archimedean too.

**Example 1.2.7 (the lexicographic group $\mathbb{Z}^n$).** Order $\mathbb{Z}^n$ lexicographically: $(a_1, \dots, a_n) > 0$ if the first nonzero entry is positive. For $0 \le j \le n$ let $\Delta_j = 0^{n-j} \times \mathbb{Z}^j$, the set of vectors whose first $n - j$ entries are 0. Each $\Delta_j$ is convex. Indeed, let $0 \le \gamma \le \delta$ with $\delta \in \Delta_j$, and let $a_i$ be the first nonzero entry of $\gamma$. If $i \le n - j$, then $a_i > 0$ and $\delta - \gamma$ has first nonzero entry $-a_i < 0$ at place $i$, so $\delta < \gamma$, which is false. We show that these are all the convex subgroups. Let $\Delta \ne 0$ be convex, and let $j$ be the largest index such that $\Delta$ contains a vector $\delta > 0$ whose first nonzero entry is at place $n - j + 1$. Then $\Delta \subseteq \Delta_j$, because a vector of $\Delta$ with an earlier nonzero entry would give a larger $j$. Each $\gamma \in \Delta_j$ with $\gamma \ge 0$ satisfies $0 \le \gamma \le N\delta$ for a large integer $N$, since the first entry of $\delta$ in the block $\Delta_j$ is positive. So $\Delta = \Delta_j$. The case $\Delta = 0$ is $\Delta_0$. Thus $\mathbb{Z}^n$ with the lexicographic order has the $n + 1$ convex subgroups $\Delta_0 \subsetneq \dots \subsetneq \Delta_n$. Its rank is $n$, and its rational rank is $n$. This is the case of equality in Proposition 1.2.5.

Lean: `Singularity.LexZn.isConvexSubgroup_iff`, `Singularity.LexZn.natCard_convexSubgroup` (the convex subgroups, not the rational rank)
