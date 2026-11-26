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

Lean: `Singularity.ValuationSubring.eq_of_le_of_comap_eq`

*Proof.* Assume that there is an element $z \in \mathcal{O}_{w'} \setminus \mathcal{O}_w$. Then $w(z^{-1}) > 0$. If $w'(z) > 0$, then $z^{-1} \notin \mathcal{O}_{w'}$, so $z^{-1} \notin \mathcal{O}_w$, and $z \in \mathcal{O}_w$. This is false, so $w'(z) = 0$. By Corollary 2.1.3 the group $\Gamma_w/\Gamma_v$ is finite, say of order $e$. So $w(z^{-e}) = v(c)$ for some $c \in K^\times$, and $v(c) > 0$. The element $u = z^{-e}/c$ has $w(u) = 0$, so it is a unit of $\mathcal{O}_w$ and of $\mathcal{O}_{w'}$, and $w'(u) = 0$. But $w'(u) = -e\,w'(z) - v(c) = -v(c) < 0$. This is a contradiction, so $\mathcal{O}_{w'} = \mathcal{O}_w$, and $w = w'$ by Theorem 1.1.7. $\square$

The Lean statement is for each algebraic extension $L/K$, and for two valuation rings of $L$ with the same intersection with $K$. The proof uses only the fact that a power of each value of $L$ is a value of $K$.

**Theorem 3.1.2 (fundamental inequality).** Let $w_1, \dots, w_g$ be distinct extensions of $v$ to $L$, with ramification indices $e_i$ and residue degrees $f_i$. Then
$$\sum_{i=1}^g e_if_i \le n.$$
In particular $v$ has at most $n$ extensions to $L$.

Lean: none yet

For $g = 1$ this is Corollary 2.1.3. For $g \ge 2$ one combines the elements of Lemma 2.1.2 for the different $w_i$ with the approximation theorem for incomparable valuation rings. Lemma 3.1.1 shows that the rings $\mathcal{O}_{w_i}$ are incomparable. We prove the theorem when $v$ has rank 1 at the end of this section, with a simple form of the approximation theorem (Lemma 3.1.5). This case contains the discrete valuations of rank 1 and all the examples of this chapter. For $v$ of higher rank we do not prove the approximation theorem, and we cite the inequality from [ZS2, Chapter VI]. The approximation theorem is also in [ZS2, Chapter VI].

### Henselian fields

**Definition 3.1.3 (henselian field).** A valued field $(K, v)$ is *henselian* if $v$ has exactly one extension to each algebraic extension of $K$.

If $(K, v)$ is henselian and $L/K$ is algebraic, then $L$ with the unique extension of $v$ is henselian, because an algebraic extension of $L$ is an algebraic extension of $K$. A field that is complete for a valuation of rank 1 is henselian [Kuh-book]. This holds in particular for a discrete valuation of rank 1. For example, $k((t))$ with $\operatorname{ord}_t$ is henselian. The name comes from Hensel's lemma, which holds for the valuation ring of a henselian field. For complete local rings it is Lemma 4.4.3 of Volume 1.

When $(K, v)$ is henselian, Theorem 3.1.2 says $ef \le n$ for the unique extension. In general the fundamental inequality is strict. The defect of the next section measures the difference.

**Theorem 3.1.4 (Ostrowski).** Let $(K, v)$ be henselian, let $L/K$ be finite of degree $n$, and let $w$ be the extension of $v$ to $L$. Let $p$ be the characteristic of $Kv$ if it is positive, and let $p = 1$ if $\operatorname{char} Kv = 0$. Then
$$n = p^\nu \cdot e \cdot f$$
for an integer $\nu \ge 0$.

Lean: none yet

We cite this from [Kuh-book]. The proof reduces to a tower of extensions of degree prime to $p$, where the defect is 1, and extensions of degree a power of $p$. In residue characteristic 0 the theorem gives $n = ef$.

### A proof in rank 1

In this subsection $v$ has rank 1, and $w_1, \dots, w_g$ are distinct extensions of $v$ to $L$. By Lemma 1.2.6 the group $\Gamma_v$ is archimedean. By Corollary 2.1.3 each $\Gamma_{w_i}/\Gamma_v$ is finite, so each $\Gamma_{w_i}$ is archimedean, by the remark after Lemma 1.2.6. We only compare values of one $w_i$ with each other, so we never need to compare elements of different groups $\Gamma_{w_i}$.

**Lemma 3.1.5 (approximation in rank 1).** Let $g \ge 2$, and let $1 \le i \le g$.

1. There is $x \in L$ with $w_i(x) < 0$ and $w_j(x) > 0$ for each $j \ne i$.
2. For all $\gamma_1 \in \Gamma_{w_1}, \dots, \gamma_g \in \Gamma_{w_g}$ there is $u \in L$ with $w_i(u - 1) > \gamma_i$ and $w_j(u) > \gamma_j$ for each $j \ne i$.

Lean: none yet

*Proof.* We renumber so that $i = 1$. We prove part 1 by induction on $g$. Let $g = 2$. By Lemma 3.1.1, $\mathcal{O}_{w_1} \not\subseteq \mathcal{O}_{w_2}$ and $\mathcal{O}_{w_2} \not\subseteq \mathcal{O}_{w_1}$. Choose $a \in \mathcal{O}_{w_1} \setminus \mathcal{O}_{w_2}$ and $b \in \mathcal{O}_{w_2} \setminus \mathcal{O}_{w_1}$, and let $x = b/a$. Then $w_1(x) = w_1(b) - w_1(a) < 0$ and $w_2(x) = w_2(b) - w_2(a) > 0$.

Let $g \ge 3$. By induction for $w_1, \dots, w_{g-1}$ there is $z$ with $w_1(z) < 0$ and $w_j(z) > 0$ for $2 \le j \le g - 1$. By the case $g = 2$ for $w_1, w_g$ there is $y$ with $w_1(y) < 0$ and $w_g(y) > 0$. There are three cases.

1. $w_g(z) > 0$. Take $x = z$.
2. $w_g(z) = 0$. Take $x = z^my$ with an integer $m \ge 1$. Then $w_1(x) = mw_1(z) + w_1(y) < 0$ and $w_g(x) = w_g(y) > 0$. For $2 \le j \le g - 1$ we have $w_j(x) = mw_j(z) + w_j(y)$, and this is positive for large $m$ because $\Gamma_{w_j}$ is archimedean and $w_j(z) > 0$.
3. $w_g(z) < 0$. Since $w_1(z) \ne 0$, we have $z^m \ne -1$, and we take $x = yz^m/(1 + z^m)$. If $w_j(z) < 0$, then $w_j(1 + z^m) = mw_j(z)$, so $w_j(z^m/(1 + z^m)) = 0$. This holds for $j = 1$ and $j = g$, so $w_1(x) = w_1(y) < 0$ and $w_g(x) = w_g(y) > 0$. If $w_j(z) > 0$, then $w_j(1 + z^m) = 0$, so $w_j(x) = w_j(y) + mw_j(z)$. This holds for $2 \le j \le g - 1$, and it is positive for large $m$.

For part 2, let $x$ be as in part 1 with $i = 1$, and let $u = x^m/(1 + x^m)$ for an integer $m \ge 1$. Here $1 + x^m \ne 0$, since $w_1(x^m) \ne 0$. We have $u - 1 = -1/(1 + x^m)$ and $w_1(1 + x^m) = mw_1(x)$, so $w_1(u - 1) = -mw_1(x)$. For $j \ne 1$ we have $w_j(1 + x^m) = 0$, so $w_j(u) = mw_j(x)$. Both $-w_1(x)$ and $w_j(x)$ are positive. Since each $\Gamma_{w_j}$ is archimedean, a large $m$ gives all the inequalities. $\square$

Part 2 says that one element of $L$ can be close to 1 for $w_i$ and close to 0 for the other $w_j$, to any given precision. Without the hypothesis of rank 1 this argument fails. Let $\Delta \subsetneq \Gamma_{w_j}$ be a convex subgroup with $w_j(x) \in \Delta$, and let $\gamma_j > 0$ with $\gamma_j \notin \Delta$. Then $mw_j(x) \in \Delta$, so $mw_j(x) < \gamma_j$ for each $m$.

*Proof of Theorem 3.1.2 when $v$ has rank 1.* If $g = 1$, this is Corollary 2.1.3, so let $g \ge 2$. For each $i$, the numbers $e_i$ and $f_i$ are finite by Corollary 2.1.3. Choose $x_{i1}, \dots, x_{ie_i} \in L^\times$ whose values $w_i(x_{ij})$ represent the cosets of $\Gamma_v$ in $\Gamma_{w_i}$, and choose $y_{i1}, \dots, y_{if_i} \in \mathcal{O}_{w_i}$ whose residues form a basis of $Lw_i/Kv$. Put $b_{ijk} = x_{ij}y_{ik}$. All these elements are nonzero. For $i \ne l$ put
$$A_i = \max_j w_i(x_{ij}) \in \Gamma_{w_i}, \qquad B_{il} = \min_{j, k} w_i(b_{ljk}) \in \Gamma_{w_i}.$$
By Lemma 3.1.5, for each $l$ there is $u_l \in L$ with $w_l(u_l - 1) > 0$ and $w_i(u_l) > A_i - B_{il}$ for each $i \ne l$. Then $w_l(u_l) = 0$. Put $z_{ljk} = u_lb_{ljk}$. These are $\sum_l e_lf_l$ elements of $L$, and we show that they are linearly independent over $K$. This gives $\sum_l e_lf_l \le n$.

Let $c_{ljk} \in K$, not all 0, and let $S_l = \sum_{j,k} c_{ljk}b_{ljk}$. We must show that $\sum_l u_lS_l \ne 0$. Choose the coefficient $c = c_{ijk}$ with the least value $v(c)$. We divide all coefficients by $c$. Then all $c_{ljk}$ are in $\mathcal{O}_v$, and $c_{ij_0k_0} = 1$ for some $j_0, k_0$. By Lemma 2.1.2 for $w_i$,
$$w_i(u_iS_i) = w_i(S_i) = \min_{j,k}\big(v(c_{ijk}) + w_i(x_{ij})\big) \le w_i(x_{ij_0}) \le A_i.$$
Let $l \ne i$. All $c_{ljk}$ have $v(c_{ljk}) \ge 0$, so $w_i(S_l) \ge B_{il}$ if $S_l \ne 0$. Then
$$w_i(u_lS_l) = w_i(u_l) + w_i(S_l) > A_i - B_{il} + B_{il} = A_i.$$
So the term $u_iS_i$ has the strictly least value for $w_i$ among the nonzero terms of the sum. By Lemma 1.1.3, $w_i(\sum_l u_lS_l) = w_i(S_i) \ne \infty$, and the sum is not 0. $\square$

If $v$ is trivial, then each $w_i$ is trivial, because $\Gamma_{w_i}$ is a torsion group and has no nonzero element. A field has one trivial valuation, so $g = 1$, and Theorem 3.1.2 holds. Thus the theorem is proved for all $v$ of rank at most 1.

### Immediate extensions of degree prime to $p$

The next proposition proves a special case of Corollary 3.2.2 without the theorem of Ostrowski. It shows the basic mechanism: in a henselian field, the trace of an element cannot have a smaller value than the element, and this kills immediate extensions of degree prime to $p$.

**Proposition 3.1.6.** Let $(K, v)$ be henselian, and let $p$ be the characteristic exponent of $Kv$. Let $L/K$ be a finite extension of degree $n$, prime to $p$, and let $w$ be the extension of $v$ to $L$. If $e = f = 1$, then $L = K$.

Lean: none yet

*Proof.* The integer $n$ is prime to $p$, so its image in $Kv$ is not 0, and $v(n) = 0$. If $\operatorname{char} K = q > 0$, then $\operatorname{char} Kv = q$ and $q = p$. So $n$ is prime to the characteristic of $K$, and $L/K$ is separable, because the degree of inseparability of $L/K$ is a power of $\operatorname{char} K$ that divides $n$. Let $\operatorname{Tr} : L \to K$ be the trace. Fix an algebraic closure $\bar{K}$ of $K$ that contains $L$, and let $\bar{w}$ be the extension of $v$ to $\bar{K}$. It is unique, since $K$ is henselian, and so $\bar{w}$ extends $w$.

Step 1: $\bar{w}(\sigma(y)) = \bar{w}(y)$ for each $y \in \bar{K}$ and each automorphism $\sigma$ of $\bar{K}$ over $K$. The ring $\sigma(\mathcal{O}_{\bar{w}})$ is a valuation ring of $\bar{K}$ that extends $\mathcal{O}_v$, so it is $\mathcal{O}_{\bar{w}}$. Let $y \ne 0$. By Corollary 2.1.3 there are $m \ge 1$ and $a \in K^\times$ with $\bar{w}(y^m) = v(a)$. Then $y^m/a$ is a unit of $\mathcal{O}_{\bar{w}}$, so $\sigma(y)^m/a = \sigma(y^m/a)$ is a unit too. So $m\bar{w}(\sigma(y)) = v(a) = m\bar{w}(y)$, and $\bar{w}(\sigma(y)) = \bar{w}(y)$ because $\Gamma_{\bar{w}}$ is torsion free.

Step 2: $v(\operatorname{Tr}(y)) \ge w(y)$ for each $y \in L$. Since $L/K$ is separable, $\operatorname{Tr}(y) = \sum_{i=1}^n \sigma_i(y)$, where $\sigma_1, \dots, \sigma_n$ are the $K$-embeddings of $L$ into $\bar{K}$. Each $\sigma_i$ extends to an automorphism of $\bar{K}$, so $\bar{w}(\sigma_i(y)) = w(y)$ by Step 1. The claim follows.

Step 3. Assume that $L \ne K$, and let $z \in L \setminus K$. Put $z' = z - \operatorname{Tr}(z)/n$. Then $z' \notin K$, so $z' \ne 0$, and $\operatorname{Tr}(z') = \operatorname{Tr}(z) - \operatorname{Tr}(z) = 0$. Since $e = 1$, there is $c_0 \in K$ with $v(c_0) = w(z')$. Since $f = 1$, the residue of $z'/c_0$ is the residue of some $c_1 \in \mathcal{O}_v$, and $c_1$ is a unit. Let $c = c_0c_1$. Then $w(z'/c - 1) > 0$, that is, $w(z' - c) > v(c)$. By Step 2, $v(\operatorname{Tr}(z' - c)) \ge w(z' - c) > v(c)$. But $\operatorname{Tr}(z' - c) = 0 - nc$, and $v(-nc) = v(n) + v(c) = v(c)$. This is a contradiction. So $L = K$. $\square$

The proof fails when $p$ divides $n$: then $v(n) > 0$, or $n = 0$ in $K$, and the value of $\operatorname{Tr}(z' - c) = -nc$ is larger than $v(c)$. Proposition 3.2.5 shows that immediate extensions of degree $p$ do exist.

**Example 3.1.7 (extensions of $\operatorname{ord}_t$ of degree 2).** Let $k$ be a field with $\operatorname{char} k \ne 2$, let $K = k(t)$ and let $v = \operatorname{ord}_t$. So $\Gamma_v = \mathbb{Z}$ and $Kv = k$. We compute the extensions of $v$ to three quadratic extensions $L/K$, and we check Theorem 3.1.2 with $n = 2$.

Lean: none yet

1. $L = K(\sqrt{1 + t})$. First we find a square root of $1 + t$ in $k[[t]]$. We look for $\sigma = \sum_{i \ge 0} a_it^i$ with $\sigma^2 = 1 + t$. Comparing the coefficients of $t^0$ and $t^1$ gives $a_0 = 1$ and $2a_1 = 1$, and for $m \ge 2$ the coefficient of $t^m$ gives $2a_m + \sum_{0 < i < m} a_ia_{m-i} = 0$. Since 2 is invertible in $k$, these equations determine all $a_m$. The polynomial $X^2 - 1 - t$ is irreducible over $K$, because $1 + t$ is not a square in $k(t)$. So there are two $K$-embeddings of $L$ into $k((t))$, with $\sqrt{1 + t} \mapsto \sigma$ and $\sqrt{1 + t} \mapsto -\sigma$. The restrictions of $\operatorname{ord}_t$ along them are extensions $w_+$ and $w_-$ of $v$. They are distinct: $\sigma - 1 = t/2 + \dots$ has order 1, and $-\sigma - 1 = -2 - t/2 - \dots$ has order 0, so $w_+(\sqrt{1 + t} - 1) = 1$ and $w_-(\sqrt{1 + t} - 1) = 0$. Each $w_\pm$ has value group a subgroup of $\mathbb{Z}$ that contains $1 = w_\pm(t)$, and residue field a field between $k$ and $k$. So $e_\pm = f_\pm = 1$, and $e_+f_+ + e_-f_- = 2 = n$. By Theorem 3.1.2 there is no third extension.
2. $L = K(\sqrt{t})$. Let $w$ be an extension of $v$. Then $2w(\sqrt{t}) = v(t) = 1$, so $w(\sqrt{t}) = 1/2$ and $e \ge 2$. By Theorem 3.1.2, $e = 2$, $f = 1$, and $w$ is the only extension.
3. $L = K(\sqrt{c})$ with $c \in k$ not a square in $k$. Then $L = k'(t)$ with $k' = k(\sqrt{c})$, and $X^2 - c$ is irreducible over $K$, because $k$ is algebraically closed in $k(t)$. Let $w$ be an extension of $v$. Then $w(\sqrt{c}) = 0$, and the residue of $\sqrt{c}$ is a root of $X^2 - c$, so it is not in $k$. Thus $f \ge 2$. By Theorem 3.1.2, $f = 2$, $e = 1$, and $w$ is the only extension. It is $\operatorname{ord}_t$ on $k'(t)$.

In all three cases $\sum_i e_if_i = n$. The field $K = k(t)$ is not henselian, as case 1 shows. Over the henselian field $k((t))$, case 1 does not give a field extension at all, since $1 + t$ is a square there, and cases 2 and 3 give the same values of $e$ and $f$ as over $k(t)$.
