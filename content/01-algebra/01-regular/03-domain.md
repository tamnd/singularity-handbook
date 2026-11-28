---
title: A regular local ring is a domain
nodes: [SG0000000J]
sources: [AM69, Mat, Stacks, Ser55, Mathlib, HirLean]
status: drafted
drafted_by: writer
reviewed_by: []
---
## A regular local ring is a domain

In this section we prove that a regular local ring is a domain. The proof is by induction on the dimension, with Proposition 1.2.6 as the inductive step. To use Proposition 1.2.6 we need an element $x \in \mathfrak{m} \setminus \mathfrak{m}^2$, and for the induction to work, $x$ must also avoid the minimal prime ideals of $R$. The tool that finds such an element is prime avoidance. The last part of the section uses the same induction to prove that a regular local ring is integrally closed.

### Prime avoidance

The usual form of prime avoidance says that an ideal contained in a finite union of prime ideals is contained in one of them [AM69, Proposition 1.11]. We need a slightly stronger form, because the ideal $\mathfrak{m}^2$ is not prime.

**Lemma 1.3.1 (prime avoidance).** Let $R$ be a ring, and let $I, I_1, \dots, I_n$ be ideals of $R$ with $n \ge 1$. Assume that $I_2, \dots, I_n$ are prime ideals. If $I \subseteq I_1 \cup \dots \cup I_n$, then $I \subseteq I_j$ for some $j$.

Lean: `Ideal.subset_union_prime` (in Mathlib)

*Proof.* We use induction on $n$. For $n = 1$ there is nothing to prove. Let $n \ge 2$. If $I$ is contained in the union of $n - 1$ of the ideals $I_j$, then the induction hypothesis gives the result. Note that at most one of these $n - 1$ ideals is not prime, so the induction hypothesis applies after a change of the order. Thus we can assume that for each $j$ there is an element
$$a_j \in I \quad\text{with}\quad a_j \notin I_l \text{ for all } l \ne j.$$
Since $I \subseteq I_1 \cup \dots \cup I_n$, we have $a_j \in I_j$. We show that this gives a contradiction. Let
$$b = a_1 a_3 a_4 \cdots a_n \quad\text{and}\quad y = a_2 + b.$$
For $n = 2$ the product $b$ is $a_1$. The element $y$ is in $I$. We show that $y$ is in no $I_j$.

* The element $b$ is not in $I_2$. For $n = 2$ this is the choice of $a_1$. For $n \ge 3$, the ideal $I_2$ is prime and no factor of $b$ is in $I_2$. Since $a_2 \in I_2$, we get $y \notin I_2$.
* For $j \ne 2$, the element $b$ is in $I_j$, because $a_j$ is a factor of $b$. Since $a_2 \notin I_j$, we get $y \notin I_j$.

This contradicts $I \subseteq I_1 \cup \dots \cup I_n$. $\square$

The Mathlib lemma `Ideal.subset_union_prime` allows two ideals that are not prime. We need only one.

**Lemma 1.3.2.** Let $(R, \mathfrak{m})$ be a Noetherian local ring with $\dim R \ge 1$. Then there is an element $x \in \mathfrak{m}$ such that $x \notin \mathfrak{m}^2$ and $x$ is in no minimal prime ideal of $R$.

Lean: `Singularity.Algebra.exists_mem_maximalIdeal_notMem_sq_notMem_minimalPrimes`

*Proof.* A Noetherian ring has only finitely many minimal prime ideals [Mat, Theorem 6.5]. Let $\mathfrak{p}_1, \dots, \mathfrak{p}_k$ be the minimal prime ideals of $R$. Assume that the lemma is false. Then
$$\mathfrak{m} \subseteq \mathfrak{m}^2 \cup \mathfrak{p}_1 \cup \dots \cup \mathfrak{p}_k.$$
By Lemma 1.3.1, with $I_1 = \mathfrak{m}^2$, either $\mathfrak{m} \subseteq \mathfrak{m}^2$ or $\mathfrak{m} \subseteq \mathfrak{p}_i$ for some $i$.

In the first case $\mathfrak{m} = \mathfrak{m}^2$. By Nakayama's lemma, $\mathfrak{m} = 0$. Then $R$ is a field and $\dim R = 0$.

In the second case $\mathfrak{m} = \mathfrak{p}_i$, so the maximal ideal is a minimal prime ideal. Each prime ideal $\mathfrak{p}$ satisfies $\mathfrak{p} \subseteq \mathfrak{m} = \mathfrak{p}_i$, and so $\mathfrak{p} = \mathfrak{m}$ by the minimality of $\mathfrak{p}_i$. Thus $\mathfrak{m}$ is the only prime ideal and $\dim R = 0$.

Both cases contradict $\dim R \ge 1$. $\square$

### The theorem

**Theorem 1.3.3.** A regular local ring is a domain.

Node: SG0000000J · Lean: `Singularity.Algebra.isDomain_of_isRegularLocalRing`

*Proof.* Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$. We use induction on $d$.

Let $d = 0$. Then $\mu(\mathfrak{m}) = 0$, so $\mathfrak{m} = 0$. Thus $R$ is a field (Example 1.2.2), and a field is a domain.

Let $d \ge 1$, and assume that each regular local ring of dimension $d - 1$ is a domain. Lemma 1.3.2 gives an element $x \in \mathfrak{m} \setminus \mathfrak{m}^2$ that is in no minimal prime ideal of $R$. By Proposition 1.2.6, the ring $R/(x)$ is a regular local ring of dimension $d - 1$. By the induction hypothesis it is a domain, that is, the ideal $(x)$ is prime.

Each prime ideal contains a minimal prime ideal [AM69, Chapter 1, Exercise 8]. Let $\mathfrak{p} \subseteq (x)$ be a minimal prime ideal. We show that $\mathfrak{p} = x \mathfrak{p}$. Let $y \in \mathfrak{p}$. Then $y \in (x)$, so $y = zx$ for some $z \in R$. The ideal $\mathfrak{p}$ is prime and $x \notin \mathfrak{p}$ by the choice of $x$, so $z \in \mathfrak{p}$. Thus $y \in x\mathfrak{p}$. This shows $\mathfrak{p} \subseteq x\mathfrak{p}$, and the other inclusion is clear.

The ideal $\mathfrak{p}$ is a finitely generated $R$-module because $R$ is Noetherian, and $x \in \mathfrak{m}$. Thus $\mathfrak{p} = x\mathfrak{p} \subseteq \mathfrak{m}\mathfrak{p}$, and Nakayama's lemma [AM69, Proposition 2.6] gives $\mathfrak{p} = 0$. So the zero ideal is prime, and $R$ is a domain. $\square$

The proof uses the choice of $x$ twice. Proposition 1.2.6 needs $x \notin \mathfrak{m}^2$, and the step $\mathfrak{p} = x\mathfrak{p}$ needs $x \notin \mathfrak{p}$. Without the second condition the proof fails. For example, in the ring $k[x, y]_{(x,y)}/(xy)$ of Example 1.2.9, the quotient by the element $x$ is a domain, but $x$ is in the minimal prime ideal $(x)$, and the ring is not a domain. Of course, that ring is not regular.

**Corollary 1.3.4.** Let $X$ be a locally Noetherian scheme and let $x \in X$ be a point such that $\mathcal{O}_{X,x}$ is a regular local ring. Then $x$ lies on exactly one irreducible component of $X$.

Lean: `Singularity.Algebra.existsUnique_minimalPrimes_le_of_isRegularLocalRing` (affine form)

*Proof.* Let $U = \operatorname{Spec} A$ be an affine open neighbourhood of $x$, and let $\mathfrak{q} \subseteq A$ be the prime ideal of $x$. The irreducible components of $U$ are the closed sets $V(\mathfrak{p})$ for the minimal prime ideals $\mathfrak{p}$ of $A$, and $x$ lies on $V(\mathfrak{p})$ if and only if $\mathfrak{p} \subseteq \mathfrak{q}$. The minimal prime ideals of $A$ that are contained in $\mathfrak{q}$ correspond to the minimal prime ideals of $A_\mathfrak{q} = \mathcal{O}_{X,x}$ [AM69, Proposition 3.11]. By Theorem 1.3.3, $\mathcal{O}_{X,x}$ is a domain, so it has exactly one minimal prime ideal, the zero ideal. Thus $x$ lies on exactly one irreducible component of $U$. The irreducible components of $X$ that contain $x$ meet $U$ in the irreducible components of $U$ that contain $x$, so the claim follows. $\square$

Volume 9, Section 1.3 uses Theorem 1.3.3 for this reason. A resolution of a variety can be made from resolutions of its irreducible components, because the components do not meet at a regular point.

### A regular local ring is integrally closed

Let $R$ be a domain with fraction field $K$. An element $g \in K$ is *integral* over $R$ if it is a root of a monic polynomial with coefficients in $R$. The domain $R$ is *integrally closed* if each element of $K$ that is integral over $R$ lies in $R$. In this subsection we prove that a regular local ring is integrally closed. The book needs this fact in a special form. Volume 5 uses it as follows: if $g \in K$ and a power $g^n$ with $n \ge 1$ lies in the regular local ring $R$, then $g$ lies in $R$.

The usual proof goes through the theorem of Auslander-Buchsbaum, which says that a regular local ring is a unique factorization domain. That theorem is long. The proof here uses the same induction as Theorem 1.3.3. The problem is that integral closure does not pass easily from $R/(x)$ to $R$. So we prove a stronger property (D), which is a statement about divisibility. Property (D) passes from $R/(x)$ to $R$ when $x$ is a prime element of $\mathfrak{m}$. The proof of this step writes $a = br + x^N t$ for each $N$, and then the intersection theorem of Krull gives $b \mid a$.

**Definition 1.3.5 (property (D)).** A ring $R$ has *property (D)* if it satisfies the following condition. Let $a, b, c \in R$ with $b \ne 0$ and $c \ne 0$. If $b^n \mid c a^n$ for all $n \ge 0$, then $b \mid a$.

Lean: `Singularity.Algebra.IsDvdClosed`

Let $R$ be a domain with fraction field $K$. An element $g \in K$ is *almost integral* over $R$ if there is $c \in R$ with $c \ne 0$ and $c g^n \in R$ for all $n \ge 0$. A domain is *completely integrally closed* if each almost integral element of $K$ lies in $R$. For a domain, property (D) is this condition. Write $g = a/b$ with $b \ne 0$. Then $c g^n \in R$ if and only if $b^n \mid c a^n$, and $g \in R$ if and only if $b \mid a$.

**Lemma 1.3.6 ((D) gives integrally closed).** Let $R$ be a domain with property (D). Then $R$ is integrally closed.

Lean: `Singularity.Algebra.IsDvdClosed.isIntegrallyClosed`

*Proof.* Let $K$ be the fraction field of $R$, and let $g \in K$ be integral over $R$. Then $g$ is a root of a monic polynomial
$$T^d + c_{d-1} T^{d-1} + \dots + c_0 \quad\text{with}\quad c_i \in R \text{ and } d \ge 1.$$
Let $M = R + Rg + \dots + Rg^{d-1}$, an $R$-submodule of $K$. We show that $g^n \in M$ for all $n \ge 0$, by induction on $n$. For $n \le d - 1$ this is clear. Let $g^n = r_0 + r_1 g + \dots + r_{d-1} g^{d-1}$ with $r_i \in R$. Then
$$g^{n+1} = r_0 g + \dots + r_{d-2} g^{d-1} + r_{d-1} g^d,$$
and $g^d = -(c_{d-1} g^{d-1} + \dots + c_0)$ is in $M$. So $g^{n+1} \in M$.

Write $g = a/b$ with $a, b \in R$ and $b \ne 0$. For $0 \le i \le d - 1$ we have $b^d g^i = b^{d-i} a^i \in R$. Thus $b^d M \subseteq R$, and so $b^d g^n \in R$ for all $n$. Let $b^d g^n = s$ with $s \in R$. Then $b^d a^n = s b^n$, that is, $b^n \mid b^d a^n$ in $R$. The element $c = b^d$ is not zero, because $R$ is a domain. Property (D) gives $b \mid a$, so $g \in R$. $\square$

The proof shows that an integral element is almost integral, with $c = b^d$. The next three lemmas are about a prime element $x$ of a domain. Recall that $x$ is *prime* if $x \ne 0$, $x$ is not a unit, and $x \mid yz$ implies $x \mid y$ or $x \mid z$. Equivalently, $x \ne 0$ and $(x)$ is a prime ideal.

**Lemma 1.3.7 (cancel a prime).** Let $R$ be a domain, let $x \in R$ be a prime element, and let $d \in R$ with $x \nmid d$. Let $e \ge 0$ and $y \in R$. If $d \mid x^e y$, then $d \mid y$.

Lean: `Singularity.Algebra.dvd_of_dvd_prime_pow_mul`

*Proof.* We use induction on $e$. For $e = 0$ there is nothing to prove. Let $e \ge 0$, assume that the lemma holds for $e$, and let $d \mid x^{e+1} y$. Let $d t = x \cdot x^e y$ with $t \in R$. Then $x \mid dt$. Since $x$ is prime and $x \nmid d$, we get $x \mid t$. Write $t = x t'$. Then $x d t' = x \cdot x^e y$. Since $R$ is a domain and $x \ne 0$, we can cancel $x$, and we get $d t' = x^e y$. So $d \mid x^e y$, and the induction hypothesis gives $d \mid y$. $\square$

We apply Lemma 1.3.7 with $d = b^n$. If $x$ is prime and $x \nmid b$, then $x \nmid b^n$.

**Lemma 1.3.8 (the order at a prime element).** Let $R$ be a Noetherian domain, let $x \in R$ be a prime element, and let $a \in R$ with $a \ne 0$. Then $a = x^e a'$ for some $e \ge 0$ and some $a' \in R$ with $x \nmid a'$.

Lean: `WfDvdMonoid.max_power_factor` (in Mathlib)

*Proof.* Assume that the lemma is false. Then $x \mid a$, since otherwise $e = 0$ and $a' = a$ work. We construct elements $a_0 = a, a_1, a_2, \dots$ with $a_k = x a_{k+1}$ for all $k$. Let $a_k$ be given with $a = x^k a_k$. If $x \nmid a_k$, then $e = k$ and $a' = a_k$ work, and this is not the case. So $a_k = x a_{k+1}$ for some $a_{k+1}$, and $a = x^{k+1} a_{k+1}$. The ideals
$$(a_0) \subseteq (a_1) \subseteq (a_2) \subseteq \cdots$$
form an increasing chain. Since $R$ is Noetherian, $(a_k) = (a_{k+1})$ for some $k$. Then $a_{k+1} = u a_k$ for some $u \in R$, and so $a_{k+1} = u x a_{k+1}$. The element $a_{k+1}$ is not zero, because $a \ne 0$. We cancel $a_{k+1}$ and get $1 = ux$. So $x$ is a unit, and this contradicts the hypothesis that $x$ is prime. $\square$

**Lemma 1.3.9 (reduction).** Let $R$ be a Noetherian domain, and let $x \in R$ be a prime element. Let $a, b, c \in R$ with $b^n \mid c a^n$ for all $n \ge 0$. Assume that $b = x^e b'$ and $c = x^f c'$ with $x \nmid b'$ and $x \nmid c'$. Then there is $a' \in R$ with $a = x^e a'$ and $b'^n \mid c' a'^n$ for all $n \ge 0$.

Lean: `Singularity.Algebra.exists_eq_pow_mul_forall_pow_dvd`

*Proof.* If $a = 0$, then $a' = 0$ works. Let $a \ne 0$. By Lemma 1.3.8, $a = x^g a''$ with $g \ge 0$ and $x \nmid a''$.

First we show that $e \le g$. Assume that $e \ge g + 1$, and let $n = f + 1$. Then
$$en \ge (g + 1)(f + 1) = f + gn + 1.$$
The hypothesis for this $n$ gives
$$x^{f + gn + 1} \mid x^{en} b'^n = b^n \mid c a^n = x^{f + gn} c' a''^n.$$
We cancel $x^{f + gn}$, because $R$ is a domain, and get $x \mid c' a''^n$. This is false, because $x$ is prime, $x \nmid c'$ and $x \nmid a''$. So $e \le g$.

Let $a' = x^{g - e} a''$. Then $a = x^e a'$. For each $n$, the hypothesis says
$$x^{en} b'^n = b^n \mid c a^n = x^{en} \cdot x^f c' a'^n.$$
We cancel $x^{en}$ and get $b'^n \mid x^f (c' a'^n)$. Since $x \nmid b'^n$, Lemma 1.3.7 gives $b'^n \mid c' a'^n$. $\square$

**Lemma 1.3.10 (the binomial step).** Let $R$ be a ring, and let $b, c, u \in R$ with $b^i \mid c u^i$ for all $i \ge 0$. Then $b^n \mid c (u - br)^n$ for all $r \in R$ and all $n \ge 0$.

Lean: `Singularity.Algebra.pow_dvd_mul_sub_mul_pow`

*Proof.* By the binomial formula,
$$c (u - br)^n = \sum_{i=0}^{n} \binom{n}{i} \, (c u^i) \, (-br)^{n-i}.$$
In the term with index $i$, the factor $c u^i$ is divisible by $b^i$, and the factor $(-br)^{n-i}$ is divisible by $b^{n-i}$. So $b^n$ divides each term, and it divides the sum. $\square$

Lemma 1.3.10 says that the set of the elements $t$ with $b^n \mid c t^n$ for all $n$ is stable under the change $t \mapsto t - br$. The next proposition is the main step of the induction.

**Proposition 1.3.11 (the main step).** Let $(R, \mathfrak{m})$ be a Noetherian local domain, and let $x \in \mathfrak{m}$ be a prime element. If $R/(x)$ has property (D), then $R$ has property (D).

Lean: `Singularity.Algebra.isDvdClosed_of_isDvdClosed_quotient`

*Proof.* Let $a, b, c \in R$ with $b \ne 0$, $c \ne 0$ and $b^n \mid c a^n$ for all $n$. We show that $b \mid a$.

*Step 1: we can assume that $x \nmid b$ and $x \nmid c$.* By Lemma 1.3.8, $b = x^e b'$ and $c = x^f c'$ with $x \nmid b'$ and $x \nmid c'$. The elements $b'$ and $c'$ are not zero. By Lemma 1.3.9, $a = x^e a'$ with $b'^n \mid c' a'^n$ for all $n$. If $b' \mid a'$, then $b = x^e b'$ divides $x^e a' = a$. So it is sufficient to prove $b' \mid a'$, and the elements $a'$, $b'$ and $c'$ satisfy the hypotheses with $x \nmid b'$ and $x \nmid c'$.

*Step 2: the claim.* Now let $x \nmid b$ and $x \nmid c$. We show by induction on $N$: for each $N \ge 0$ there are $r, t \in R$ with
$$a = br + x^N t \quad\text{and}\quad b^n \mid c t^n \text{ for all } n \ge 0.$$
For $N = 0$ we take $r = 0$ and $t = a$. Let $N \ge 0$, and let $r$ and $t$ satisfy the claim for $N$. Let $\bar{y}$ denote the class of $y \in R$ in $R/(x)$. Since $x \nmid b$ and $x \nmid c$, we have $\bar{b} \ne 0$ and $\bar{c} \ne 0$. The divisibility $b^n \mid c t^n$ in $R$ gives $\bar{b}^n \mid \bar{c} \bar{t}^n$ in $R/(x)$, for all $n$. Property (D) of $R/(x)$ gives $\bar{b} \mid \bar{t}$. Let $\bar{t} = \bar{b} \bar{q}$, and let $r' \in R$ be a lift of $\bar{q}$. Then $t - br' \in (x)$, so $t - br' = x t'$ for some $t' \in R$. Thus
$$a = br + x^N (br' + x t') = b(r + x^N r') + x^{N+1} t'.$$
It remains to show that $b^n \mid c t'^n$ for all $n$. By Lemma 1.3.10, applied with $u = t$,
$$b^n \mid c (t - br')^n = c x^n t'^n = x^n (c t'^n).$$
Since $x \nmid b^n$, Lemma 1.3.7 gives $b^n \mid c t'^n$. This proves the claim for $N + 1$.

*Step 3: the intersection theorem.* Let $M = R/(b)$. It is a finitely generated $R$-module. Let $\bar{a}$ be the class of $a$ in $M$. By the claim, $a = br + x^N t$ for some $r$ and $t$, so $\bar{a} = x^N \bar{t}$ is in $\mathfrak{m}^N M$, for each $N \ge 0$. The ring $R$ is a Noetherian local ring, so the intersection theorem of Krull gives
$$\bigcap_{N \ge 0} \mathfrak{m}^N M = 0$$
(Corollary 4.1.8 and [AM69, Corollary 10.20]). So $\bar{a} = 0$, that is, $a \in (b)$. In terms of ideals of $R$, we have used that the intersection of the ideals $(b) + \mathfrak{m}^N$ is $(b)$. $\square$

The induction in Step 2 is a form of division with remainder. Property (D) of $R/(x)$ divides $t$ by $b$ modulo $x$, and the remainder $x t'$ has one more factor $x$. Step 3 says that the remainders go to $0$ in the topology of $\mathfrak{m}$.

**Theorem 1.3.12.** A regular local ring has property (D). Thus a regular local ring is integrally closed.

Lean: `Singularity.Algebra.isIntegrallyClosed_of_isRegularLocalRing`, `Singularity.Algebra.dvd_of_forall_pow_dvd_mul_pow` (property (D))

*Proof.* Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$. We show by induction on $d$ that $R$ has property (D). The statement for $d$ is about all regular local rings of dimension $d$, as in the proof of Theorem 1.3.3.

Let $d = 0$. Then $R$ is a field (Example 1.2.2). Let $a, b, c$ be as in Definition 1.3.5. Then $b \ne 0$ is a unit, so $b \mid a$.

Let $d \ge 1$, and assume that each regular local ring of dimension $d - 1$ has property (D). Lemma 1.3.2 gives an element $x \in \mathfrak{m}$ with $x \notin \mathfrak{m}^2$. By Proposition 1.2.6, the ring $R/(x)$ is a regular local ring of dimension $d - 1$. By the induction hypothesis, $R/(x)$ has property (D). By Theorem 1.3.3, $R/(x)$ is a domain, so the ideal $(x)$ is prime. Also $x \ne 0$, because $x \notin \mathfrak{m}^2$. Thus $x$ is a prime element of $R$. By Theorem 1.3.3, $R$ is a domain, and it is Noetherian and local. Proposition 1.3.11 gives that $R$ has property (D).

The second statement follows from the first one and Lemma 1.3.6, because $R$ is a domain by Theorem 1.3.3. $\square$

**Corollary 1.3.13 (roots).** Let $R$ be a regular local ring with fraction field $K$. Let $g \in K$, and assume that $g^n \in R$ for some $n \ge 1$. Then $g \in R$.

Lean: `Singularity.Algebra.mem_range_algebraMap_of_pow_mem`

*Proof.* Let $s = g^n \in R$. Then $g$ is a root of the monic polynomial $T^n - s$ with coefficients in $R$. So $g$ is integral over $R$, and Theorem 1.3.12 gives $g \in R$. $\square$

In characteristic $p > 0$, Volume 5 uses Corollary 1.3.13 with $n = p^N$: if a regular local ring contains $g^{p^N}$, then it contains $g$.

**Example 1.3.14 (the cusp does not have property (D)).** Let $k$ be a field, and let $R$ be the localization of $k[t^2, t^3] \subseteq k[t]$ at the maximal ideal $(t^2, t^3)$. The map $x \mapsto t^2$, $y \mapsto t^3$ identifies $R$ with the local ring $k[x, y]_{(x,y)}/(y^2 - x^3)$ of the cusp in Example 1.2.4. Let
$$a = t^3, \qquad b = t^2, \qquad c = t^2.$$
For each $n \ge 0$, we have $c a^n = t^{3n+2} = t^{2n} \cdot t^{n+2}$. The element $t^{n+2}$ is in $k[t^2, t^3]$, because $n + 2 \ge 2$ and $k[t^2, t^3]$ contains each power $t^m$ with $m \ne 1$. Thus $b^n \mid c a^n$ in $R$ for all $n$.

But $b \nmid a$ in $R$. If $b \mid a$, then $t = a/b$ is in $R$. Then $t = f/h$ with $f, h \in k[t^2, t^3]$ and $h(0) \ne 0$, so $th = f$ in $k[t]$. The coefficient of $t$ in $th$ is $h(0) \ne 0$. The coefficient of $t$ in $f$ is $0$. This is a contradiction. So $R$ does not have property (D).

The element $g = t$ of the fraction field satisfies $g^2 = t^2 \in R$ and $g \notin R$. So $R$ is not integrally closed, and Corollary 1.3.13 fails for $R$. By Theorem 1.3.12, this is a second proof that the cusp is not regular.

Property (D) is stronger than integral closure in general. For example, a valuation ring of rank 2 is integrally closed, but it does not have property (D). For a Noetherian domain, the two properties are equivalent. We do not need this, and we do not prove it.

### What this section does not prove

A regular local ring has two more properties that this section does not prove.

1. A regular local ring is a unique factorization domain. This is the theorem of Auslander-Buchsbaum [Mat, Theorem 20.3]. This section does not prove it, and it is not yet in Lean. The project has the node SG00000023 for this result. A unique factorization domain is integrally closed, so the theorem implies that a regular local ring is integrally closed. This section proves that consequence in a direct way, without unique factorization (Theorem 1.3.12).
2. Let $R$ be a regular local ring and let $\mathfrak{p}$ be a prime ideal. Then $R_\mathfrak{p}$ is a regular local ring. This is a theorem of Serre [Ser55], and its proof uses homological algebra: a Noetherian local ring is regular if and only if it has finite global dimension [Mat, Theorems 19.2 and 19.3]. The project has the node SG0000000H for this result. Sections 1.5 and 1.6 prove it: it is Corollary 1.6.9, and in Lean it is `Singularity.Algebra.isRegularLocalRing_localization`.

The second property is important for geometry. It says that the set of regular points of a scheme is stable under generization, and it is the first step to prove that the regular locus is open. Sections 1.7 to 1.9 prove that the regular locus of a scheme of finite type over a field is open, and the chapter of this volume on excellence returns to this question.

### The Lean proof

The Lean proof of Theorem 1.3.3 is `Singularity.Algebra.isDomain_of_isRegularLocalRing`. It applies the theorem `Singularity.Algebra.isDomain_of_isRegularLocalRing_of_ringKrullDim_eq`, which proves the statement for each dimension $n \in \mathbb{N}$ by induction on $n$. The statement in this lemma quantifies over all rings $R$, so that the induction hypothesis applies to the quotient ring $R/(x)$, which is a different type.

Prime avoidance is the Mathlib lemma `Ideal.subset_union_prime`. The step $\mathfrak{p} = x\mathfrak{p}$ is written as the inclusion `P ≤ span {x} • P`, and the Nakayama step is the Mathlib lemma `Submodule.eq_bot_of_le_smul_of_le_jacobson_bot`. The Lean proof is adapted from the file `Hironaka/Algebra/Local/Regular.lean` of [HirLean].

The Lean form of Corollary 1.3.4 is affine. Let $A$ be a commutative ring and let $\mathfrak{q}$ be a prime ideal such that $A_\mathfrak{q}$ is a regular local ring. The theorem `Singularity.Algebra.existsUnique_minimalPrimes_le_of_isRegularLocalRing` in the file `Singularity/Algebra/RegularComponent.lean` states that exactly one minimal prime of $A$ is contained in $\mathfrak{q}$. The minimal primes of $A$ in $\mathfrak{q}$ correspond to the minimal primes of $A_\mathfrak{q}$, and Theorem 1.3.3 gives that $A_\mathfrak{q}$ is a domain, so its only minimal prime is $(0)$. The irreducible components of $\operatorname{Spec} A$ through $\mathfrak{q}$ are the closed sets $V(\mathfrak{p})$ for these minimal primes $\mathfrak{p}$. The scheme form is not yet in Lean.

The proof of Theorem 1.3.12 is in the file `Singularity/Algebra/RegularIntegrallyClosed.lean`. The induction is the theorem `Singularity.Algebra.isDvdClosed_of_isRegularLocalRing_of_ringKrullDim_eq`, which quantifies over all regular local rings of a given dimension, as in the proof of Theorem 1.3.3. The link with integral closure goes through the Mathlib notion `IsAlmostIntegral`: the theorem `Singularity.Algebra.IsDvdClosed.mem_range_of_isAlmostIntegral` says that each almost integral element of the fraction field of a domain with property (D) is in the ring, and Lemma 1.3.6 follows from it. Lemma 1.3.8 is the Mathlib lemma `WfDvdMonoid.max_power_factor`, which applies because a Noetherian domain has the ascending chain condition on principal ideals. Step 3 of Proposition 1.3.11 uses the intersection theorem of Krull in the form `Ideal.iInf_pow_smul_eq_bot_of_isLocalRing`, with the ideal $(x)$ in place of $\mathfrak{m}$ and the module $R/(b)$. Corollary 1.3.13 uses the Mathlib lemma `IsIntegral.of_pow`.

### Notes and references

Theorem 1.3.3 is [Mat, Theorem 14.3] and [Stacks, Tag 00NP]. Atiyah and Macdonald prove it in [AM69, Lemma 11.23] with the associated graded ring: for a regular local ring $R$, the graded ring $\bigoplus_n \mathfrak{m}^n/\mathfrak{m}^{n+1}$ is a polynomial ring over $\kappa$, and so it is a domain, and this implies that $R$ is a domain. The proof here is shorter, but the graded ring is useful for multiplicity theory, and Section 1.10 and Chapter 3 of this volume use it.

The standard reference for the fact that a regular local ring is integrally closed is [Mat, Theorem 19.4]. One standard proof uses the criterion of Serre [Mat, Theorem 23.8]: a regular local ring is a Cohen-Macaulay ring whose localizations at the prime ideals of height 1 are regular, and so it is normal. A second standard proof uses the theorem of Auslander-Buchsbaum [Mat, Theorem 20.3]. The proof of Theorem 1.3.12 uses only Theorem 1.3.3, Proposition 1.2.6 and the intersection theorem of Krull. We do not claim that this proof is new. Property (D) is the condition that the ring is completely integrally closed, and the proof gives this stronger condition for a regular local ring.
