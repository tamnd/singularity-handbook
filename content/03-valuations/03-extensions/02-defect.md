---
title: Defect
nodes: [SG00000010]
sources: [Kuh-book, Kuh16, KR23, CKR25]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Defect

The defect measures how far a finite extension of a henselian field is from the equality $n = ef$. It is 1 in residue characteristic 0. In residue characteristic $p$ it can be a power of $p$, and then the value group and the residue field do not see the whole extension. In this section we define the defect, we prove a criterion that detects it, and we compute the standard example.

### Definition

**Definition 3.2.1 (defect).** Let $(K, v)$ be a henselian valued field, let $L/K$ be a finite extension of degree $n$, and let $w$ be the extension of $v$ to $L$, with ramification index $e$ and residue degree $f$. The *defect* of $L/K$ is
$$d(L/K) = \frac{n}{ef}.$$
The extension is *defectless* if $d(L/K) = 1$, and it is *immediate* if $e = f = 1$.

Node: SG00000010 · Lean: `Singularity.Valuation.defect` (planned, no Lean statement yet)

**Corollary 3.2.2.** In Definition 3.2.1, $d(L/K)$ is a power of the characteristic exponent $p$ of $Kv$. In particular $d(L/K) = 1$ if $\operatorname{char} Kv = 0$, or if $n$ is prime to $p$.

Lean: none yet

*Proof.* By Theorem 3.1.4, $d(L/K) = p^\nu$. If $p = 1$ this is 1. If $p$ is prime and $p \nmid n$, then $p^\nu \mid n$ forces $\nu = 0$. $\square$

For a valued field $(K, v)$ that is not henselian, one defines the defect of an extension of $v$ to $L$ through the henselization of $K$ [Kuh-book]. We need only the henselian case. A valued field is *defectless* if each of its finite extensions satisfies $\sum_i e_if_i = n$, with the sum over all extensions of $v$. By Corollary 3.2.2, each henselian field with residue characteristic 0 is defectless.

### A criterion

The next proposition shows what an extension without defect looks like. Each element has a best approximation in $K$.

**Proposition 3.2.3.** Let $(L/K, w)$ be a finite extension of valued fields of degree $n$ with $ef = n$. Then for each $z \in L \setminus K$ the set $w(z - K) = \{w(z - a) : a \in K\}$ has a largest element.

Lean: none yet

*Proof.* Choose $x_1 = 1, x_2, \dots, x_e \in L^\times$ whose values represent the cosets of $\Gamma_v$ in $\Gamma_w$. Choose $y_1 = 1, y_2, \dots, y_f \in \mathcal{O}_w$ whose residues form a basis of $Lw/Kv$. By Lemma 2.1.2 the $n = ef$ elements $x_iy_j$ are linearly independent, so they form a basis of $L/K$. Write $z = \sum_{i,j} c_{ij}x_iy_j$ with $c_{ij} \in K$. Since $z \notin K$, some $c_{ij}$ with $(i, j) \ne (1, 1)$ is not 0. Let $M = \min_{(i,j) \ne (1,1)}(v(c_{ij}) + w(x_i))$, which is finite. For $a \in K$, Lemma 2.1.2 gives
$$w(z - a) = \min\big(v(c_{11} - a), M\big) \le M,$$
with equality for $a = c_{11}$. So $M$ is the largest element of $w(z - K)$. $\square$

So if some $z \in L \setminus K$ has no best approximation in $K$, then $ef < n$. For a henselian $K$, this means that $L/K$ has defect.

### The Artin-Schreier example

Let $p$ be a prime, let $K_0 = \mathbb{F}_p((t))$ and let $v = \operatorname{ord}_t$. Fix an algebraic closure of $K_0$. For $m \ge 0$ let $t^{1/p^m}$ be the root of $X^{p^m} - t$ in it, which is unique because the characteristic is $p$. Let $K_m = \mathbb{F}_p((t^{1/p^m}))$. It is a field of Laurent series in $u = t^{1/p^m}$, and $v(x) = \operatorname{ord}_u(x)/p^m$ extends $v$ to $K_m$. Its value group is $\frac{1}{p^m}\mathbb{Z}$ and its residue field is $\mathbb{F}_p$. Let $K = \bigcup_m K_m$. The coefficients are in $\mathbb{F}_p$, so the $p$-th root of $\sum a_iu^i \in K_m$ is $\sum a_iu^{i/p} \in K_{m+1}$. Thus $K$ is perfect, and it is the perfect hull of $K_0$. Its value group is $\mathbb{Z}[1/p]$ and its residue field is $\mathbb{F}_p$.

Let $\vartheta$ be a root of $X^p - X - t^{-1}$, and let $L = K(\vartheta)$. For $m \ge 0$ let
$$s_m = \sum_{i=1}^m t^{-1/p^i} \in K_m, \qquad \eta_m = \vartheta - s_m.$$
Then $s_m^p = t^{-1} + s_{m-1}$ for $m \ge 1$, so we have the *Artin-Schreier relation*
$$\eta_m^p - \eta_m = t^{-1/p^m}.$$

**Lemma 3.2.4.** Let $m \ge 0$ and let $w$ be an extension of $v$ from $K_m$ to $K_m(\vartheta)$. Then $w(\eta_m) = -1/p^{m+1}$. The extension $K_m(\vartheta)/K_m$ has degree $p$, with $e = p$ and $f = 1$, and the value group of $w$ is $\frac{1}{p^{m+1}}\mathbb{Z}$.

Lean: none yet

*Proof.* The right side of the Artin-Schreier relation has value $-1/p^m < 0$. If $w(\eta_m) \ge 0$, the left side has value $\ge 0$. So $w(\eta_m) < 0$, and then $w(\eta_m^p) = pw(\eta_m) < w(\eta_m)$. By Lemma 1.1.3 the left side has value $pw(\eta_m)$, so $w(\eta_m) = -1/p^{m+1}$. The value group of $w$ contains $\frac{1}{p^m}\mathbb{Z}$ and $1/p^{m+1}$, so it contains $\frac{1}{p^{m+1}}\mathbb{Z}$, and $e \ge p$. Since $\vartheta$ is a root of a polynomial of degree $p$, Corollary 2.1.3 gives $ef \le [K_m(\vartheta) : K_m] \le p$. So $e = p$, $f = 1$, the degree is $p$, and the value group is $\frac{1}{p^{m+1}}\mathbb{Z}$. $\square$

**Proposition 3.2.5.** The extension $L/K$ has degree $p$. Let $w$ be an extension of $v$ to $L$. Then $\Gamma_w = \mathbb{Z}[1/p]$ and $Lw = \mathbb{F}_p$, so $L/K$ is immediate. The set $w(\vartheta - K)$ has no largest element. Since $K$ is henselian, $d(L/K) = p$.

Lean: none yet

*Proof.* If $\vartheta \in K$, then $\vartheta \in K_m$ for some $m$, and $K_m(\vartheta) = K_m$, which contradicts Lemma 3.2.4. So $\vartheta \notin K$. The roots of $X^p - X - t^{-1}$ are $\vartheta + i$ with $i \in \mathbb{F}_p$, because $(\vartheta + i)^p - (\vartheta + i) = \vartheta^p - \vartheta$. Let $G \in K[X]$ be a monic factor of degree $j$ with $0 < j < p$. Then $G = \prod_{i \in S}(X - \vartheta - i)$ for a set $S$ of $j$ elements of $\mathbb{F}_p$. Its coefficient of $X^{j-1}$ is $-(j\vartheta + \sum_{i \in S} i)$. This is in $K$, and $j$ is invertible in $\mathbb{F}_p$, so $\vartheta \in K$, which is false. Thus $X^p - X - t^{-1}$ is irreducible over $K$, and $[L : K] = p$.

Each element of $L$ is a polynomial in $\vartheta$ with finitely many coefficients in $K$, so it lies in $K_m(\vartheta)$ for some $m$. By Lemma 3.2.4 its value is in $\frac{1}{p^{m+1}}\mathbb{Z} \subseteq \mathbb{Z}[1/p]$, and its residue, if defined, is in $\mathbb{F}_p$. So $\Gamma_w = \mathbb{Z}[1/p] = \Gamma_v$ and $Lw = \mathbb{F}_p = Kv$.

Let $a \in K$, and choose $m$ with $a \in K_m$. Then $\vartheta - a = \eta_m + (s_m - a)$. Here $w(\eta_m) = -1/p^{m+1}$ is not in $\frac{1}{p^m}\mathbb{Z}$, while $v(s_m - a)$ is in $\frac{1}{p^m}\mathbb{Z} \cup \{\infty\}$. So the two values differ, and by Lemma 1.1.3,
$$w(\vartheta - a) = \min\big(-1/p^{m+1}, v(s_m - a)\big) \le -1/p^{m+1} < -1/p^{m+2} = w(\vartheta - s_{m+1}).$$
So no element of $w(\vartheta - K)$ is the largest.

The field $K_0$ is complete for a discrete valuation of rank 1, so it is henselian (Section 3.1). The field $K$ is algebraic over $K_0$, so it is henselian. Thus $w$ is the only extension of $v$ to $L$, and $d(L/K) = p/(1 \cdot 1) = p$. $\square$

The proof of the first three claims does not use that $K$ is henselian. Only the value of the defect uses it, through the uniqueness of $w$. The one fact that we cite is that the complete field $K_0$ is henselian [Kuh-book]. Proposition 3.2.3 and the third claim show again that $ef < p$, without a computation of $e$ and $f$.

The sequence $s_m$ approximates $\vartheta$ better and better. The values $w(\vartheta - s_m) = -1/p^{m+1}$ increase to 0, but they never reach a maximum in $K$. A change of coordinates $\vartheta \mapsto \vartheta - a$ with $a \in K$ can never make the value of $\vartheta$ as large as possible. In residue characteristic 0 this cannot happen in a henselian field, by Corollary 3.2.2 and Proposition 3.2.3. In characteristic $p$, local uniformization must deal with such extensions, and Chapter 4 explains how. Volume 9, Section 2.2, uses the same example. Kuhlmann studies defect extensions in [Kuh16] and [Kuh-book]. Kuhlmann and Rzepka divide the Artin-Schreier defect extensions into dependent and independent ones [KR23], and Cutkosky, Kuhlmann and Rzepka characterize the independent ones by their module of Kähler differentials [CKR25].
