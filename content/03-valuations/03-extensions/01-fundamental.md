---
title: The fundamental inequality
nodes: []
sources: [ZS2, Kuh-book]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The fundamental inequality

In this section $v$ is a valuation of a field $K$ and $L/K$ is a finite extension of degree $n$. By Corollary 1.3.5, $v$ has at least one extension to $L$. We bound the number of extensions and their invariants.

**Lemma 3.1.1.** Let $w$ and $w'$ be extensions of $v$ to $L$ with $\mathcal{O}_w \subseteq \mathcal{O}_{w'}$. Then $w = w'$.

Lean: none yet

*Proof.* Assume that there is an element $z \in \mathcal{O}_{w'} \setminus \mathcal{O}_w$. Then $w(z^{-1}) > 0$. If $w'(z) > 0$, then $z^{-1} \notin \mathcal{O}_{w'}$, so $z^{-1} \notin \mathcal{O}_w$, and $z \in \mathcal{O}_w$. This is false, so $w'(z) = 0$. By Corollary 2.1.3 the group $\Gamma_w/\Gamma_v$ is finite, say of order $e$. So $w(z^{-e}) = v(c)$ for some $c \in K^\times$, and $v(c) > 0$. The element $u = z^{-e}/c$ has $w(u) = 0$, so it is a unit of $\mathcal{O}_w$ and of $\mathcal{O}_{w'}$, and $w'(u) = 0$. But $w'(u) = -e\,w'(z) - v(c) = -v(c) < 0$. This is a contradiction, so $\mathcal{O}_{w'} = \mathcal{O}_w$, and $w = w'$ by Theorem 1.1.7. $\square$

**Theorem 3.1.2 (fundamental inequality).** Let $w_1, \dots, w_g$ be distinct extensions of $v$ to $L$, with ramification indices $e_i$ and residue degrees $f_i$. Then
$$\sum_{i=1}^g e_if_i \le n.$$
In particular $v$ has at most $n$ extensions to $L$.

Lean: none yet

For $g = 1$ this is Corollary 2.1.3. For $g \ge 2$ one combines the elements of Lemma 2.1.2 for the different $w_i$ with the approximation theorem for incomparable valuation rings. Lemma 3.1.1 shows that the rings $\mathcal{O}_{w_i}$ are incomparable. We do not prove the approximation theorem, and we cite the inequality from [ZS2, Chapter VI, Section 11, Theorem 19]. The approximation theorem is [ZS2, Chapter VI, Section 10, Theorem 18].

### Henselian fields

**Definition 3.1.3 (henselian field).** A valued field $(K, v)$ is *henselian* if $v$ has exactly one extension to each algebraic extension of $K$.

If $(K, v)$ is henselian and $L/K$ is algebraic, then $L$ with the unique extension of $v$ is henselian, because an algebraic extension of $L$ is an algebraic extension of $K$. A field that is complete for a valuation of rank 1 is henselian [Kuh-book, Chapter 9]. This holds in particular for a discrete valuation of rank 1. For example, $k((t))$ with $\operatorname{ord}_t$ is henselian. The name comes from Hensel's lemma, which holds for the valuation ring of a henselian field. For complete local rings it is Lemma 4.4.3 of Volume 1.

When $(K, v)$ is henselian, Theorem 3.1.2 says $ef \le n$ for the unique extension. In general the fundamental inequality is strict. The defect of the next section measures the difference.

**Theorem 3.1.4 (Ostrowski).** Let $(K, v)$ be henselian, let $L/K$ be finite of degree $n$, and let $w$ be the extension of $v$ to $L$. Let $p$ be the characteristic of $Kv$ if it is positive, and let $p = 1$ if $\operatorname{char} Kv = 0$. Then
$$n = p^\nu \cdot e \cdot f$$
for an integer $\nu \ge 0$.

Lean: none yet

We cite this from [Kuh-book]. The proof reduces to a tower of extensions of degree prime to $p$, where the defect is 1, and extensions of degree a power of $p$. In residue characteristic 0 the theorem gives $n = ef$.
