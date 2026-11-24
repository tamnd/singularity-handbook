---
title: Valuations and valuation rings
nodes: []
sources: [ZS2]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Valuations and valuation rings

In this section we define Krull valuations and valuation rings. We prove that a valuation ring determines its valuation up to equivalence. All rings are commutative with $1$.

### Ordered groups and valuations

**Definition 1.1.1 (ordered group).** An *ordered group* is an abelian group $\Gamma$, written additively, with a total order $\le$ such that $\alpha \le \beta$ implies $\alpha + \gamma \le \beta + \gamma$ for all $\alpha, \beta, \gamma \in \Gamma$. We add a symbol $\infty$ with $\gamma < \infty$ and $\gamma + \infty = \infty + \infty = \infty$ for each $\gamma \in \Gamma$.

An ordered group is torsion free. Indeed, let $\gamma > 0$ and $n \ge 1$. Then $n\gamma \ge (n-1)\gamma \ge \dots \ge \gamma > 0$, so $n\gamma \ne 0$. The groups $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$ with the usual order are ordered groups. The group $\mathbb{Z}^2$ with the lexicographic order is an ordered group: $(a, b) < (c, d)$ if $a < c$, or if $a = c$ and $b < d$.

**Definition 1.1.2 (valuation).** Let $K$ be a field. A *valuation* of $K$ is a map $v : K \to \Gamma \cup \{\infty\}$ to an ordered group $\Gamma$ with these properties.

1. $v(x) = \infty$ if and only if $x = 0$.
2. $v(xy) = v(x) + v(y)$ for all $x, y \in K$.
3. $v(x + y) \ge \min(v(x), v(y))$ for all $x, y \in K$.

The subgroup $\Gamma_v = v(K^\times)$ of $\Gamma$ is the *value group* of $v$. The valuation is *trivial* if $\Gamma_v = 0$. If $k \subseteq K$ is a subfield, a *valuation of $K/k$* is a valuation of $K$ that is trivial on $k$.

Lean: `Valuation` (in Mathlib, in the multiplicative notation)

In Mathlib a valuation takes values in an ordered group with zero, written multiplicatively, and the inequality in condition 3 goes the other way. The additive form of Definition 1.1.2 is `AddValuation` in Mathlib. We use the additive form, as Zariski and Samuel do [ZS2, Chapter VI].

**Lemma 1.1.3.** Let $v$ be a valuation of $K$ and let $x, y \in K$. Then $v(1) = v(-1) = 0$, $v(-x) = v(x)$, and $v(x^{-1}) = -v(x)$ for $x \ne 0$. If $v(x) \ne v(y)$, then $v(x + y) = \min(v(x), v(y))$.

Lean: none yet

*Proof.* From $1 = 1 \cdot 1$ we get $v(1) = 2v(1)$, so $v(1) = 0$. From $1 = (-1)^2$ we get $2v(-1) = 0$, so $v(-1) = 0$ because $\Gamma$ is torsion free. Then $v(-x) = v(-1) + v(x) = v(x)$, and $v(x) + v(x^{-1}) = v(1) = 0$. Let $v(x) < v(y)$. Then $v(x + y) \ge v(x)$. Also $x = (x + y) + (-y)$, so $v(x) \ge \min(v(x + y), v(y))$. Since $v(x) < v(y)$, this minimum is $v(x + y)$, and $v(x + y) \le v(x)$. $\square$

### Valuation rings

**Definition 1.1.4 (valuation ring).** Let $K$ be a field. A subring $V \subseteq K$ is a *valuation ring of $K$* if for each $x \in K^\times$ we have $x \in V$ or $x^{-1} \in V$. A domain $V$ is a *valuation ring* if it is a valuation ring of its field of fractions.

Let $v$ be a valuation of $K$. The *ring of $v$* is $\mathcal{O}_v = \{x \in K : v(x) \ge 0\}$. Its subset $\mathfrak{m}_v = \{x \in K : v(x) > 0\}$ is the *maximal ideal of $v$*, and $Kv = \mathcal{O}_v/\mathfrak{m}_v$ is the *residue field* of $v$. For $x \in \mathcal{O}_v$ we write $\bar{x}$ for its class in $Kv$. If $v$ is a valuation of $K/k$, then $k \subseteq \mathcal{O}_v$ and $k \to Kv$ is injective, so $Kv$ is an extension of $k$.

**Proposition 1.1.5.** Let $v$ be a valuation of $K$. Then $\mathcal{O}_v$ is a valuation ring of $K$. It is a local ring, its maximal ideal is $\mathfrak{m}_v$, and its group of units is $\{x : v(x) = 0\}$.

Lean: `Valuation.valuationSubring` (in Mathlib)

*Proof.* By conditions 2 and 3 of Definition 1.1.2 and Lemma 1.1.3, $\mathcal{O}_v$ is a subring of $K$ and $\mathfrak{m}_v$ is an ideal of $\mathcal{O}_v$. Let $x \in K^\times$. If $v(x) < 0$, then $v(x^{-1}) = -v(x) > 0$, so $x^{-1} \in \mathcal{O}_v$. Thus $\mathcal{O}_v$ is a valuation ring. An element $x \in \mathcal{O}_v$ is a unit of $\mathcal{O}_v$ if and only if $v(x^{-1}) \ge 0$, that is, if and only if $v(x) = 0$. Thus $\mathfrak{m}_v$ is the set of nonunits of $\mathcal{O}_v$. A ring in which the nonunits form an ideal is local, with this ideal as maximal ideal. $\square$

**Definition 1.1.6 (equivalence).** Two valuations $v : K \to \Gamma \cup \{\infty\}$ and $v' : K \to \Gamma' \cup \{\infty\}$ are *equivalent* if there is an isomorphism of ordered groups $\varphi : \Gamma_v \to \Gamma_{v'}$ with $v'(x) = \varphi(v(x))$ for each $x \in K^\times$.

Equivalent valuations have the same ring. The next theorem gives the converse, and it shows that each valuation ring comes from a valuation.

**Theorem 1.1.7 (valuations and valuation rings).** Let $V$ be a valuation ring of $K$, and let $\Gamma_V = K^\times/V^\times$. For $x, y \in K^\times$ put $xV^\times \le yV^\times$ if $y/x \in V$. Then $\Gamma_V$ is an ordered group, and the map $v_V : K \to \Gamma_V \cup \{\infty\}$ with $v_V(x) = xV^\times$ for $x \ne 0$ and $v_V(0) = \infty$ is a valuation with ring $V$. Two valuations of $K$ are equivalent if and only if they have the same ring. Thus $v \mapsto \mathcal{O}_v$ is a bijection from the set of equivalence classes of valuations of $K$ to the set of valuation rings of $K$.

Lean: `Valuation.isEquiv_iff_valuationSubring` (in Mathlib, for the last two claims)

*Proof.* The relation $\le$ is well defined, because $y/x \in V$ does not change if we multiply $x$ and $y$ by units of $V$. It is reflexive since $1 \in V$, and transitive since $V$ is closed under products. It is antisymmetric: if $y/x \in V$ and $x/y \in V$, then $y/x$ is a unit of $V$, so $xV^\times = yV^\times$. It is total, because $y/x \in V$ or $x/y \in V$. If $y/x \in V$, then $(yz)/(xz) \in V$, so the order is compatible with the group law. Thus $\Gamma_V$ is an ordered group. The neutral element is $1 \cdot V^\times$, and $x \in V$ if and only if $1 \cdot V^\times \le xV^\times$.

Conditions 1 and 2 of Definition 1.1.2 hold for $v_V$ by definition. For condition 3, let $x, y \in K^\times$ with $x + y \ne 0$, and assume that $v_V(x) \le v_V(y)$. Then $y/x \in V$, so $(x + y)/x = 1 + y/x \in V$, and $v_V(x) \le v_V(x + y)$. Thus $v_V$ is a valuation, and $\mathcal{O}_{v_V} = \{x : 1 \cdot V^\times \le xV^\times\} \cup \{0\} = V$.

Let $v$ be a valuation of $K$ with ring $V = \mathcal{O}_v$. By Proposition 1.1.5, $v(x) = v(y)$ if and only if $x/y \in V^\times$, and $v(x) \le v(y)$ if and only if $y/x \in V$. Thus $\varphi(xV^\times) = v(x)$ is a well defined isomorphism of ordered groups $\Gamma_V \to \Gamma_v$ with $v = \varphi \circ v_V$. So $v$ is equivalent to $v_V$. If two valuations have the same ring $V$, then both are equivalent to $v_V$, so they are equivalent to each other. $\square$

From now on we identify equivalent valuations. We write $\mathcal{O}_v$, $\mathfrak{m}_v$, $\Gamma_v$ and $Kv$ for a valuation $v$, and $v_V$ for the valuation of a valuation ring $V$.

**Lemma 1.1.8.** Let $V$ be a valuation ring of $K$.

1. Each ring $W$ with $V \subseteq W \subseteq K$ is a valuation ring of $K$.
2. The ideals of $V$ are totally ordered by inclusion.
3. Each finitely generated ideal of $V$ is principal.
4. $V$ is integrally closed.
5. If $V$ is Noetherian and $V \ne K$, then $V$ is a discrete valuation ring, and $\Gamma_V \cong \mathbb{Z}$.

Lean: none yet

*Proof.* Part 1 is clear from Definition 1.1.4. For part 2, let $I, J$ be ideals with $I \not\subseteq J$, and let $x \in I \setminus J$. Let $y \in J$ with $y \ne 0$. If $x/y \in V$, then $x = (x/y)y \in J$, which is false. So $y/x \in V$ and $y = (y/x)x \in I$. Thus $J \subseteq I$. For part 3, let $I = (x_1, \dots, x_n)$ with $x_i \ne 0$, and choose $i$ with $v_V(x_i)$ minimal. Then $x_j/x_i \in V$ for each $j$, so $I = (x_i)$.

For part 4, let $x \in K$ be integral over $V$, with $x^n + a_1x^{n-1} + \dots + a_n = 0$ and $a_j \in V$. Assume that $x \notin V$. Then $x \ne 0$ and $x^{-1} \in V$. We divide the equation by $x^{n-1}$ and get $x = -(a_1 + a_2x^{-1} + \dots + a_nx^{-(n-1)}) \in V$, a contradiction.

For part 5, the maximal ideal $\mathfrak{m}_V$ is finitely generated, so $\mathfrak{m}_V = (\pi)$ by part 3, and $\pi \ne 0$ because $V \ne K$. Let $x \in V \setminus \{0\}$. Since $V$ is Noetherian, $\bigcap_n (\pi^n) = 0$ by Corollary 4.1.8 of Volume 1, so there is a largest $n$ with $x \in (\pi^n)$. Then $x = u\pi^n$ with $u \notin (\pi)$, so $u$ is a unit. Thus each $x \in K^\times$ is $u\pi^n$ with $u \in V^\times$ and $n \in \mathbb{Z}$, and $v_V(x) \mapsto n$ is an isomorphism $\Gamma_V \cong \mathbb{Z}$ of ordered groups. $\square$

Conversely, a discrete valuation ring is a valuation ring, because each $x \in K^\times$ is $u\pi^n$ with $u$ a unit and $n \in \mathbb{Z}$. Theorem 1.4.2 of Volume 1 characterizes the discrete valuation rings among the Noetherian local domains of dimension 1. A valuation ring of dimension at least 2 is never Noetherian, by part 5 and Corollary 1.2.4 below. Thus most valuation rings of this volume are not Noetherian, and the tools of Volume 1 do not apply to them directly.
