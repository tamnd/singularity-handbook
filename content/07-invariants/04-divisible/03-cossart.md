---
title: The base blowups of the algorithm of Cossart
nodes: [SG0000007H, SG0000007J, SG0000007K, SG0000007M, SG0000007N, SG0000007P, SG0000007Q, SG0000007R, SG0000007S, SG0000007T, SG0000007V]
sources: [Cos87, Pos24, Hir64, Benn70, CP08, CP09, Gir75]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The base blowups of the algorithm of Cossart

In his thesis, Cossart resolves the purely inseparable cover $X = V(z^p + g) \to B$ of a regular threefold $B$ by blowups of the base $B$ only [Cos87]. Section 4.2 gives a test for one such blowup: the blowup of $B$ along a regular center $C$ comes from a permissible blowup of $X$ if there is an $h$ with $g + h^p \in I_C^p$. This section answers the question when the test holds. The answer does not depend on the algorithm. For every regular center $C$, the test holds if and only if $X$ has multiplicity $p$ at the generic point of $C$ (Theorem 4.3.6). The residue field at the generic point of $C$ is not perfect, but this is no obstruction, because $C$ is normal.

The second half of the section compares the test with the invariants of Cossart. Many centers of the algorithm fail the test, for every $p$. At such a center $X$ has multiplicity less than $p$ at the generic point, but the center can pass through closed points where $X$ has multiplicity $p$ (Example 4.3.16). So the algorithm of Cossart is not a sequence of permissible blowups of $X$, not even over the locus where $X$ has multiplicity $p$.

Throughout, $p$ is a prime and the rings have characteristic $p$. We write $X = V(z^p + g)$ for the hypersurface of $\operatorname{Spec} R[z]$, or of $B \times \mathbb{A}^1$, defined by $z^p + g$.

### The order along a lifted center

Let $R$ be a commutative ring of characteristic $p$, let $q = p^e$, let $I \ne R$ be an ideal and let $g, h \in R$. Put
$$J = (z - h) + I R[z] \subseteq R[z].$$
For $I$ the ideal of a center $C$ of the base, $V(J)$ is the center $C' = \{z = h\}$ over $C$. For an ideal $K$ and $f \in R[z]$, the *order of $f$ along $K$* is the largest $n$ with $f \in K^n$, with ordinary powers.

**Proposition 4.3.1 (the order along the lifted center).** For each $n \ge 0$,
$$z^q + g \in J^n \iff n \le q \text{ and } g + h^q \in I^n.$$
So the order of $z^q + g$ along $J$ is the minimum of $q$ and the order of $g + h^q$ along $I$. In particular, $z^q + g \in J$, $z^q + g \in J^q$ and $z^q + g \notin J^{q+1}$ hold together if and only if $g + h^q \in I^q$.

Node: SG0000007H · Lean: `Singularity.Portfolio.lift_base_blowup`

*Proof.* First let $h = 0$, so $J = (z) + I R[z]$. We claim that $f \in J^n$ if and only if the coefficient $f_k$ of $z^k$ in $f$ lies in $I^{n-k}$ for each $k$, where $I^m = R$ for $m \le 0$. Let $M_n$ be the set of such $f$. It is an ideal of $R[z]$: it is closed under sums and under products with elements of $R$, and the coefficient of $z^k$ in $z f$ is $f_{k-1} \in I^{n-k+1} \subseteq I^{n-k}$. If $f \in M_a$ and $f' \in M_b$, then the coefficient of $z^k$ in $f f'$ is a sum of products $f_i f'_j$ with $i + j = k$, and $f_i f'_j \in I^{a-i} I^{b-j} \subseteq I^{a+b-k}$. So $M_a M_b \subseteq M_{a+b}$. Since $z \in M_1$ and $I \subseteq M_1$, we get $J \subseteq M_1$ and $J^n \subseteq M_n$. Conversely, let $f \in M_n$. For $k \ge n$, $f_k z^k \in J^k \subseteq J^n$. For $k < n$, $f_k \in I^{n-k} \subseteq J^{n-k}$ and $z^k \in J^k$, so $f_k z^k \in J^n$. Thus $f \in J^n$, and the claim is proved.

Now let $h$ be arbitrary. The automorphism $\tau$ of $R[z]$ over $R$ with $\tau(z) = z + h$ sends $(z) + I R[z]$ onto $J$, so $f \in J^n$ if and only if $\tau^{-1}(f) \in ((z) + I R[z])^n$. In characteristic $p$, $(z + h)^q = z^q + h^q$, so $\tau(z^q + g + h^q) = z^q + g + 2h^q$. In other words, with $z' = z - h$,
$$z^q + g = z'^q + (g + h^q).$$
By the claim, $z'^q + (g + h^q)$ lies in the $n$-th power of $(z') + I R[z']$ if and only if $g + h^q \in I^n$ (the coefficient of $z'^0$) and $1 \in I^{n-q}$ (the coefficient of $z'^q$). Since $I \ne R$, the second condition means $n \le q$. The last statement follows with $n = 1$, $n = q$ and $n = q + 1$, because $I^q \subseteq I$. $\square$

For $n = q$ this is Proposition 4.2.1. The proof also shows why the order cannot exceed $q$: the coefficient $1$ of $z'^q$ is in no proper ideal. The next statement is the chart computation of Corollary 4.2.2, in the form of a ring identity.

**Corollary 4.3.2 (the chart).** Let $\varphi \colon R \to A$ be a ring homomorphism and let $x \in A$ with $\varphi(I) A \subseteq (x)$. Assume $g + h^q \in I^q$. Then there is $g'' \in A$ with $\varphi(g + h^q) = x^q g''$, and the substitution $z = h + x z''$ sends $z^q + g$ to
$$x^q \bigl(z''^q + g''\bigr).$$

Node: SG0000007J · Lean: `Singularity.Portfolio.lift_base_blowup_chart`

*Proof.* Since $g + h^q \in I^q$, its image lies in $(\varphi(I) A)^q \subseteq (x^q)$. This gives $g''$. By the Frobenius, $(h + x z'')^q + g = x^q z''^q + (g + h^q)$, and the image of this in $A[z'']$ is $x^q z''^q + x^q g''$. $\square$

Let $R$ be regular local, let $C = V(I)$ be regular with $I = (x_1, \dots, x_c)$, and let $A$ be the ring of the $x_1$-chart of the blowup of $\operatorname{Spec} R$ along $C$. Then $I A = (x_1)$, and Corollary 4.3.2 gives the strict transform $z''^q + x_1^{-q} \pi^*(g + h^q)$ of Corollary 4.2.2.

### Generic multiplicity

Proposition 4.3.1 uses ordinary powers of ideals. The geometric question is about the multiplicity of $X$ at points. This subsection connects the two. Here $R$ is a noetherian ring of characteristic $p$ and $g \in R$.

**Definition 4.3.3 (generic multiplicity).** Let $P \subset R$ be a prime ideal and let $\bar g$ be the image of $g$ in the residue field $\kappa(P)$. The fiber $\kappa(P)[z]/(z^p + \bar g)$ of $X \to \operatorname{Spec} R$ over $P$ is local. Indeed, if $\bar g = -b^p$ with $b \in \kappa(P)$, then $z^p + \bar g = (z - b)^p$. Otherwise $z^p + \bar g$ is irreducible, since a polynomial $T^p - c$ over a field of characteristic $p$ is irreducible when $c$ is not a $p$-th power. So exactly one point $\eta'$ of $X$ lies over $P$. The *generic multiplicity* of $X$ along $V(P)$ is the multiplicity of the local ring $\mathcal{O}_{X, \eta'}$.

When $R$ is regular, $R[z]$ is regular, and the multiplicity of the hypersurface $X$ at a point is the order of $z^p + g$ in the regular local ring of $R[z]$ at that point. We use this fact without comment.

**Lemma 4.3.4 (powers of a regular prime).** Let $R$ be a regular noetherian ring and let $P$ be a prime ideal with $R/P$ regular. Then $P^n R_P \cap R = P^n$ for each $n \ge 0$.

Node: SG0000007K

*Proof.* Membership in an ideal is local on the maximal ideals. For a maximal ideal $\mathfrak{m}$ with $P \not\subseteq \mathfrak{m}$, both sides become $R_{\mathfrak{m}}$. For $\mathfrak{m} \supseteq P$, we use the prime $P R_{\mathfrak{m}}$ of $R_{\mathfrak{m}}$, whose localization is again $R_P$. So we can assume that $R$ is local. A regular quotient of a regular local ring is cut out by a part of a regular system of parameters. So $P = (u_1, \dots, u_c)$, where $u_1, \dots, u_c$ is a part of a regular system of parameters. Then the associated graded ring $\operatorname{gr}_P(R)$ is the polynomial ring $(R/P)[U_1, \dots, U_c]$ over the domain $R/P$, so it is a domain. By the intersection theorem of Krull, the order $\operatorname{ord}_P$ is finite on nonzero elements. Since $\operatorname{gr}_P(R)$ is a domain, $\operatorname{ord}_P(ab) = \operatorname{ord}_P(a) + \operatorname{ord}_P(b)$. Now let $a \in P^n R_P \cap R$, so $s a \in P^n$ for some $s \notin P$. Then $\operatorname{ord}_P(s) = 0$, so $\operatorname{ord}_P(a) = \operatorname{ord}_P(sa) \ge n$, that is, $a \in P^n$. $\square$

**Lemma 4.3.5 (the generic multiplicity).** Let $P \subset R$ be a prime ideal with $R_P$ regular.

1. If $\bar g$ is not a $p$-th power in $\kappa(P)$, then $\mathcal{O}_{X, \eta'}$ is regular, so the generic multiplicity is $1$.
2. If $\bar g = -b^p$ with $b \in \kappa(P)$, let $h \in R_P$ be a lift of $b$. Then the generic multiplicity is $\min(p, \operatorname{ord}_{P R_P}(g + h^p))$, and this number does not depend on the choice of the lift.

Node: SG0000007M

*Proof.* (1) The fiber $\kappa(P)[z]/(z^p + \bar g)$ is a field, so $\eta'$ is the prime $Q = P R_P[z] + (z^p + g)$ of $R_P[z]$. It is a maximal ideal over the maximal ideal of $R_P$, so $\dim R_P[z]_Q = \dim R_P + 1$. A regular system of parameters of $R_P$, together with $z^p + g$, generates $Q$. So $z^p + g$ is a part of a regular system of parameters of $R_P[z]_Q$, and the quotient by it is regular.

(2) Now the fiber is $\kappa(P)[z]/((z - b)^p)$, and $\eta'$ is the prime $Q = P R_P[z] + (z - h)$. Put $z' = z - h$. The equation is $z'^p + G$ with $G = g + h^p \in R_P$. The ring $A = R_P[z']_{(P, z')}$ is regular local, and its associated graded ring is $\operatorname{gr}_P(R_P)[Z']$, a polynomial ring over $\kappa(P)$. In particular the order in $A$ of an element of $R_P$ is its order along $P R_P$. The initial form of $z'^p$ is $Z'^p$. The initial form of $G$ lies in $\operatorname{gr}_P(R_P)$ and does not contain $Z'$. So the two forms do not cancel, and the order of $z'^p + G$ in $A$ is $\min(p, \operatorname{ord}_P G)$. If we replace $h$ by $h + r$ with $r \in P R_P$, then $G$ changes by $r^p \in P^p R_P$, and $\min(p, \operatorname{ord}_P G)$ does not change. $\square$

### The test is generic equimultiplicity

**Theorem 4.3.6 (the test is generic equimultiplicity).** Let $R$ be a regular noetherian ring of characteristic $p$, let $g \in R$ and $X = V(z^p + g) \subseteq \operatorname{Spec} R[z]$, and let $C = V(P)$ be an irreducible regular closed subscheme of $\operatorname{Spec} R$. The following are equivalent.

1. There is $h \in R$ with $g + h^p \in P^p$.
2. $X$ has multiplicity $p$ at the point $\eta'$ over the generic point of $C$.
3. $X$ has multiplicity $p$ at each point over $C$.

If they hold, then $h$ is unique modulo $P$, and $C' = V(z - h, P)$ is the reduced inverse image of $C$ in $X$. The hypersurface $X$ is equimultiple along $C'$. So $X$ is normally flat along $C'$ [Hir64, Benn70], and the blowup of $X$ along $C'$ is permissible. If $C$ has normal crossings with a divisor $E$ of $\operatorname{Spec} R$, then $C'$ has normal crossings with $E \times \mathbb{A}^1$.

Node: SG0000007N

*Proof.* (1) implies (3). Let $y \in C$ be a point, with the prime $Q \supseteq P$ of $R$. The point of $X$ over $y$ is the prime $N = (Q, z - h)$ of $R[z]$, and $R[z]_N$ is regular. By Proposition 4.3.1 with $I = P$, $z^p + g \in J^p \subseteq N^p R[z]_N$, so the multiplicity at $N$ is at least $p$. Modulo $Q$, the image of $z^p + g$ in $\kappa(Q)[z]$ is $(z - \bar h)^p$, which has order exactly $p$ in the discrete valuation ring $\kappa(Q)[z]_{(z - \bar h)}$. The image of $N^{p+1}$ lies in the $(p+1)$-st power of the maximal ideal of this ring, so $z^p + g \notin N^{p+1} R[z]_N$, and the multiplicity is exactly $p$.

(3) implies (2) is clear.

(2) implies (1). Since $p > 1$, Lemma 4.3.5 (1) shows that $\bar g = -b^p$ for some $b \in \kappa(P)$. The element $b$ is a root of the monic polynomial $T^p + \bar g$ with coefficients in $R/P$. The ring $R/P$ is a regular domain, so it is normal, and $b \in R/P$. Let $h \in R$ be a lift of $b$. By Lemma 4.3.5 (2), multiplicity $p$ at $\eta'$ means $\operatorname{ord}_{P R_P}(g + h^p) \ge p$, that is, $g + h^p \in P^p R_P$. By Lemma 4.3.4, $g + h^p \in P^p$.

If $g + h_1^p$ and $g + h_2^p$ both lie in $P$, then $(h_1 - h_2)^p \in P$. Since $P$ is prime, $h_1 \equiv h_2$ modulo $P$. The ideal $(z - h, P)$ is prime with quotient $R/P$, and it contains $z^p + g$, so $C'$ is the reduced inverse image of $C$. By (3), $X$ has multiplicity $p$ at each point of $C'$. For a hypersurface, equimultiplicity along a regular center implies normal flatness [Hir64, Benn70]. Last, let $(u, t)$ be a regular system of parameters at a point of $C$ such that $C = V(u)$ and each component of $E$ through the point is a coordinate hyperplane. Then $(u, t, z - h)$ is a regular system of parameters at the point of $C'$, adapted to $C'$ and to $E \times \mathbb{A}^1$. $\square$

The theorem is local on the base. Let $B$ be a regular scheme, let $g \in \mathcal{O}(B)$ and let $C \subseteq B$ be an irreducible regular closed subscheme along which $X$ has generic multiplicity $p$. Since $C$ is reduced, a $p$-th root is unique in $\mathcal{O}_C$, so the local elements $b = \bar h$ of the proof glue to a unique $b \in \mathcal{O}(C)$ with $b^p = -g|_C$. The elements $h$ are the local lifts of $b$. They exist on each affine open set of $B$, and in $\mathcal{O}(B)$ when $\mathcal{O}(B) \to \mathcal{O}(C)$ is surjective, for example when $B$ is affine. In each case $C'$ is the image of the section $z = b$ of $X \times_B C \to C$, and this is all that the blowup needs.

**Remark 4.3.7 (the imperfect residue field).** The residue field at the generic point of a curve $C$ is a function field, and it is not perfect. One could fear that the test needs a $p$-th root that exists only after an extension of this field. Theorem 4.3.6 shows that this does not happen. The only element that the test must remove at the generic point is the $p$-th root $b$ of $-\bar g$, and the normality of $C$ puts $b$ in $\mathcal{O}(C)$. The elements of $\kappa(P)$ that are not $p$-th powers, for example the coordinate $t$ of a curve, are never removed. They count in $\operatorname{ord}_P$, and this agrees with the multiplicity. For example, let $p = 3$ and $g = x^3 + y^3 w$ on $\mathbb{A}^3$, and let $C$ be the $w$-axis. Then $\bar g = 0$, $h = 0$ and $g \in (x, y)^3$, so the test holds, and $X$ has multiplicity $3$ along $C$. The term $y^3 w$ is not a cube, because $w$ is not a cube in $k(w)$, but it has order $3$ along $C$. At a closed point $w = w_0 \ne 0$, the substitution $w = w_0 + w'$ gives $y^3 w = w_0 y^3 + y^3 w'$, and the term $y^3 w'$ has order $4$ at the point. Its order along $C$ is still $3$. The test uses only the order along $C$.

**Corollary 4.3.8 (no regular center in the multiplicity $p$ locus fails).** Let $B$ be a regular scheme, $g \in \mathcal{O}(B)$, and let $C$ be an irreducible regular closed subscheme. Let $\operatorname{Sing}_p X$ be the closed set where $X$ has multiplicity $p$. Then exactly one of the following holds.

1. $C$ lies in the image of $\operatorname{Sing}_p X$, and the test of Theorem 4.3.6 holds.
2. The generic multiplicity of $X$ along $C$ is less than $p$, and the test fails.

Node: SG0000007P

*Proof.* The map $X \to B$ is finite, surjective and radicial, so it is a homeomorphism. Hence $C$ lies in the image of $\operatorname{Sing}_p X$ if and only if condition (3) of Theorem 4.3.6 holds. The multiplicity is at most $p$ at every point. So the corollary is the equivalence of the conditions of the theorem. $\square$

In case 2, the center $C$ can still meet the image of $\operatorname{Sing}_p X$ at closed points. Example 4.3.16 shows this.

### The clean part

For computations it is useful to read the test from the power series of $g$ at a closed point. Let $x \in C$ be a closed point with a perfect residue field $k$. Choose formal coordinates
$$\widehat{\mathcal{O}}_{B, x} = k[[u_1, \dots, u_c, t_1, \dots, t_{n-c}]]$$
such that $C = V(u_1, \dots, u_c)$. We say that the coordinates are *adapted* to $C$. The *clean part* $g_c$ of $g$ is $g$ minus the sum of its monomials whose exponents are all divisible by $p$. Since $k$ is perfect, this sum is a $p$-th power. For a series $f$ we write $\operatorname{ord}_C(f)$ for the least $|a|$ over the monomials $u^a t^j$ of $f$.

**Proposition 4.3.9 (the clean order).** Let $B$ be an excellent regular scheme, let $C$ and $x$ be as above, and write $g = \sum_a c_a(t) u^a$ with $c_a \in k[[t]]$. Then the test of Theorem 4.3.6 holds for $C$ if and only if $\operatorname{ord}_C(g_c) \ge p$. If it fails, the maximum of $\operatorname{ord}_{(u)}(g + h^p)$ over the $h \in \widehat{\mathcal{O}}_{B,x}$ is $\operatorname{ord}_C(g_c)$. In each case the generic multiplicity of $X$ along $C$ is
$$\min\bigl(p, \max(1, \operatorname{ord}_C(g_c))\bigr).$$
The test in $\widehat{\mathcal{O}}_{B,x}$ is equivalent to the test in $\mathcal{O}_{B,x}$.

Node: SG0000007Q

*Proof.* Put $R_x = \mathcal{O}_{B,x}$, $\widehat R = \widehat{\mathcal{O}}_{B,x}$, and let $P$ be the ideal of $C$ in $R_x$, so $P \widehat R = (u)$. Write $h = h_0(t) + h_1$ with $h_1 \in (u)$. Then $h^p \equiv h_0^p$ modulo $(u)^p$, and
$$g + h^p \equiv \bigl(c_0 + h_0^p\bigr) + \sum_{0 < |a| < p} c_a u^a \pmod{(u)^p}.$$
For $0 < |a| < p$, some entry $a_i$ satisfies $0 < a_i < p$, so each monomial of $c_a u^a$ is a monomial of $g_c$. The part of $g_c$ with $a = 0$ is the clean part of $c_0$, and it is $0$ exactly when $c_0 \in k[[t^p]] = k[[t]]^p$. So $g + h^p \in (u)^p$ for some $h$ if and only if $c_a = 0$ for $0 < |a| < p$ and $c_0 \in k[[t]]^p$, that is, if and only if $\operatorname{ord}_C(g_c) \ge p$.

Assume that the test fails. If $c_0 \notin k[[t]]^p$, then $c_0 + h_0^p \ne 0$ for each $h_0$, so the maximum is $0 = \operatorname{ord}_C(g_c)$. In this case $\bar g$ is not a $p$-th power in $\kappa(P)$: if $\bar g = -b^p$, then $b \in R_x/P$ by normality, and the image $h_0$ of $b$ in $k[[t]]$ gives $c_0 = -h_0^p$. So Lemma 4.3.5 (1) gives the generic multiplicity $1$. Otherwise choose $h_0$ with $h_0^p = -c_0$. Then the maximum is the least $|a|$ with $0 < |a| < p$ and $c_a \ne 0$, which is $\operatorname{ord}_C(g_c)$. By the descent below, there is $h' \in R_x$ with $h' - h_0 \in P \widehat R$. Then $g + h'^p$ and $g + h_0^p$ differ by an element of $P^p \widehat R$. The orders along $P$ agree in $R_x$, in $R_P$ and in $\widehat R$, by the faithful flatness of $R_x \to \widehat R$ and by Lemma 4.3.4. So Lemma 4.3.5 (2), applied to $h'$, gives the generic multiplicity $\min(p, \operatorname{ord}_C(g_c))$. With the case of the test that holds, this gives the formula.

It remains to compare $\widehat R$ with $R_x$. If the test holds in $R_x$, it holds in $\widehat R$. Conversely, let $h \in \widehat R$ with $g + h^p \in P \widehat R$. Put $A = R_x/P$, with completion $\widehat A = k[[t]]$ and fraction field $K$, and let $b \in \widehat A$ be the image of $h$. Then $b^p = -\bar g \in A$. The ring $A$ is an excellent regular local ring, so $\widehat A$ is a domain and $\operatorname{Frac} \widehat A$ is separable over $K$. A separable extension of $K$ is linearly disjoint from $K^{1/p}$ over $K$, so $b \in K^{1/p} \cap \operatorname{Frac}\widehat A = K$. Since $b$ is integral over the normal ring $A$, $b \in A$. Let $h' \in R_x$ be a lift of $b$. Then $h' - h \in P \widehat R$. If $g + h^p \in P^p \widehat R$, then $g + h'^p \in P^p \widehat R \cap R_x = P^p R_x$, by faithful flatness. $\square$

For varieties over a perfect field, each closed point has a perfect residue field. For a general excellent base this can fail, and then only Theorem 4.3.6 applies. The proposition compares only the truncated order $\min(p, \operatorname{ord}_C(g_c))$ at the generic point and at a closed point. It says nothing about the full cleaned order for values at least $p$, and the comparison of these orders is open.

**Example 4.3.10 (the coordinates must be adapted).** Let $p = 2$, let $C = V(x + y^2, w + y^2)$ in $\mathbb{A}^3$, and let $g = (x + y^2)(w + y^2)$. Then $g \in I_C^2$, and the test holds with $h = 0$. The clean part of $g$ in the coordinates $(x, y, w)$ is $g - y^4 = xw + xy^2 + y^2 w$, and its restriction to $C$ is $y^4 \ne 0$. So in these coordinates its order along $C$ is $0$. In the adapted coordinates $X' = x + y^2$, $W' = w + y^2$, $y$ we have $g = X' W'$, and the clean order is $2 = p$. So Proposition 4.3.9 needs coordinates adapted to $C$. Each regular center has adapted coordinates at each of its points, by regularity alone.

### The invariants of Cossart

We recall the setting of the thesis of Cossart [Cos87, Chapter I], as Posva restates it [Pos24, Appendix A.1]. The thesis and the appendix work over an algebraically closed field. The results above hold over each regular noetherian base.

A *modification* is a sequence of blowups $B(i+1) \to B(i)$ of the base, with a reduced simple normal crossings divisor $E(i)$ on $B(i)$, and the function $g$ is replaced by its pullback, not by a strict transform. For a regular subscheme $Y$ with normal crossings with $E$, let $D(B, E, Y)$ be the derivations that preserve the ideals of $E$ and of $Y$. The ideal $\mathcal{J}(B, g, E, Y)$ is generated by the elements $D(g)$. Since $D$ acts on the base only, $D(z^p + g) = D(g)$. This ideal factors as $H \cdot J(B, g, E, Y)$, where $H$ is a monomial ideal in the components of $E$. Write $J(B, g, E) = J(B, g, E, \emptyset)$ and
$$\nu(x) = \operatorname{ord}_x J(B, g, E), \qquad \alpha(Y, x) = \operatorname{ord}_x J(B, g, E, Y), \qquad \operatorname{Sing}(B) = \{\nu \ge 1\}.$$
The invariant $\nu$ is the residual order $\rho$ of the log-Jacobian ideal of Chapter 3. The goal of the algorithm is $\nu = 0$ at each point. A center $Y$ is *permis* at $x$ in the sense of Cossart [Cos87, I.D.1] if (i) $Y$ is regular at $x$, (ii) $Y$ has normal crossings with $E$ at $x$, (iii) $\alpha(Y, \eta) = \alpha(Y, x)$, where $\eta$ is the generic point of the component of $Y$ through $x$, and (iv) $Y \subseteq \operatorname{Sing}(B)$ near $x$. This condition is about $\alpha$, not about the multiplicity of $X$.

The algorithm first treats the surfaces of the maximal locus $\operatorname{Sing}_\nu$ of $\nu$ [Cos87, II.B.10.8]. It blows up closed points and curves of the intersection with $E$, and, when the surface is transverse to $E$, the surface itself. The last step is an isomorphism of $B$ that changes only $E$, and Cossart remarks that it is the only blowup that is not permis [Cos87, II.B.3.1]. Then it treats a locus of dimension at most $1$ [Cos87, II.C.5.3]. It blows up bad closed points, the curves of $\operatorname{Sing}_\nu$ with maximal invariants, and the curves $C_x$ of [Cos87, II.C.5.1], with $\nu(C_x) = \nu(x) - 1$ and $\alpha(C_x) = \nu(x)$. The test of a good point [Cos87, II.C.3] blows up curves $C$ through $x$ with $\nu(C) = \nu(x)$ or $\nu(C) < \nu(x)$. Each center is a closed point, a regular curve or a regular surface. For the test of Theorem 4.3.6 only the dimension of the center and its position relative to $\operatorname{Sing}_\nu$ and $E$ matter. We use five types.

| type | centers | source | position |
|---|---|---|---|
| S | the surface of $\operatorname{Sing}_\nu$, transverse to $E$ | II.B.10.8 (iv) | a component of $\operatorname{Sing}_\nu$ |
| CE | the curves of $E \cap \operatorname{Sing}_\nu$ | II.B.10.8 (i), (iii) | in $\operatorname{Sing}_\nu$ and in $E$ |
| Cn | the curves with $\nu(C) = \nu$ and $\alpha(C) \ge \nu$ | II.C.2, II.C.3 (iv), II.C.5.3 2(ii) | in $\operatorname{Sing}_\nu$ |
| Cx | the curves $C_x$, and the curves of the test with $\nu(C) < \nu(x)$ | II.C.3 (iii), II.C.5.1, II.C.5.3 2(iii) | in $\operatorname{Sing}$, not in $\operatorname{Sing}_\nu$ |
| P | closed points | II.B.10.8, II.C.1, II.C.5.3 2(i) | in $\operatorname{Sing}$ |

The cases $\kappa \ge 2$ of the second volume of the thesis refine the choice among these centers. We have not checked every proof there, so the statement that they give no other kind of center is not verified. Theorem 4.3.6 applies to each regular center, so the results below do not depend on this.

The next proposition bounds $\nu$ along a failing center.

**Proposition 4.3.11 ($\nu$ is at most the clean order).** Let $C$ be a regular center with normal crossings with $E$, let $\nu(C)$ be the value of $\nu$ at the generic point of $C$, and let $d = \operatorname{ord}_C(g_c)$ in coordinates adapted to $C$ and to $E$ at a closed point with perfect residue field. If $d < p$, then $\nu(C) \le d$. So $\nu(C) \ge p$ implies that $C$ passes the test, and each failing center has $\nu(C) \le p - 1$.

Node: SG0000007R

*Proof.* Work in $k[[u, t]]$ with the components of $E$ among the coordinate hyperplanes. This is possible because $C$ has normal crossings with $E$. The derivations $\partial_{u_i}$, or $u_i \partial_{u_i}$ when $u_i$ is an equation of a component of $E$, and $\partial_{t_j}$ or $t_j \partial_{t_j}$, lie in $D(B, E)$. They kill $p$-th powers, so $D(g) = D(g_c)$. If $d = 0$, the clean part of $c_0$ is not $0$, so it has a monomial $t^j$ with some $j_l$ not divisible by $p$. Then $\partial_{t_l}$ or $t_l \partial_{t_l}$ gives an element of order $0$ along $C$, and $\operatorname{ord}_C \mathcal{J} = 0$. If $1 \le d < p$, choose a term $c_a(t) u^a$ of $g_c$ with $|a| = d$ and $a_i > 0$, so $0 < a_i < p$. Then $\partial_{u_i} g$ contains $a_i c_a u^{a - e_i}$, and $u_i \partial_{u_i} g$ contains $a_i c_a u^a$. No other monomial of $g$ gives these monomials, so they occur in $D(g)$, and $\operatorname{ord}_C \mathcal{J} \le d$. Last, the orders along $C$ add, so $\operatorname{ord}_C J = \operatorname{ord}_C \mathcal{J} - \operatorname{ord}_C H \le \operatorname{ord}_C \mathcal{J}$. $\square$

If $C \subseteq \operatorname{Sing}(B)$, then $\nu(C) \ge 1$, so $d \ge 1$ by the proposition. With Proposition 4.3.9, the generic multiplicity of $X$ along a failing center of the algorithm is exactly $d$, and $\nu(C) \le d \le p - 1$.

**Corollary 4.3.12 (the surfaces).** Let $D = V(u)$ be a regular surface with $d = \operatorname{ord}_D(g_c) < p$. If $u$ is an equation of a component of $E$, then $\nu(D) = 0$. Otherwise $\nu(D) \le \max(0, d - 1) \le p - 2$. So a failing center of type S is not a component of $E$, and it has $1 \le \nu \le p - 2$. For $p = 2$ each center of type S passes the test.

Node: SG0000007S

*Proof.* If $u$ is not in $E$ and $d \ge 1$, then $\partial_u g$ has order $d - 1$ along $D$, by the argument of Proposition 4.3.11. If $d = 0$, then $\nu(D) = 0$ by Proposition 4.3.11. Now let $u$ be in $E$. We can assume $c_0 \in k[[t]]^p$, since otherwise $d = 0$ and $\nu(D) = 0$. Then each generator $u \partial_u g$ and $\partial_{t_j} g$ (or $t_j \partial_{t_j} g$) is divisible by $u^d$. The element $u \partial_u g$ contains $d c_d u^d$, and $p \nmid d$. So the exponent of $u$ in $H$ is exactly $d$, and $u^{-d} \cdot u \partial_u g$ is a unit at the generic point of $D$. Thus $\nu(D) = 0$. $\square$

**Remark 4.3.13 (the lift of a step of type S).** The step of type S is an isomorphism of $B$, and only $E$ changes. When the test holds along $D = V(u)$, its lift in the sense of Corollary 4.3.2 is the blowup of $B \times \mathbb{A}^1$ along the center $C' = V(z - h, u)$ of codimension $2$. On $X$ this is not an isomorphism: it is the finite birational map given by $z'' = (z - h)/u$. So for surfaces, the lift of the base blowup is a different operation from the step of Cossart.

### Centers that fail

In each example below, the center is a valid choice of the stated step of the algorithm, as far as the data $(\nu, m, \alpha)$ at the origin determine it. The history invariant $\sigma$ of Cossart and the tests for $\kappa \ge 2$ are not checked. When $E \ne \emptyset$, the example is a state of a modification, and we do not show that it comes from a run that starts with $E = \emptyset$.

**Example 4.3.14 (type S, each $p \ge 3$).** Let $g = x^d$ with $2 \le d \le p - 1$, and $E = \emptyset$. Then $\mathcal{J} = J = (d x^{d-1})$, so $\nu = d - 1 \ge 1$ on $D = V(x)$ and $\nu = 0$ outside $D$. So $\operatorname{Sing}_\nu = D$, and the step of type S blows up $D$. But $\operatorname{ord}_D(g_c) = d < p$, so the test fails, and $X = V(z^p + x^d)$ has multiplicity $d$ along $D$. After the step, $E = \{x\}$, $\mathcal{J} = (x \partial_x g) = (d x^d)$ and $H = (x^d)$, so $J = (1)$ and the algorithm stops. On $X$ this step is no blowup at all. It only changes the boundary. For $p = 5$ and $d = 4$, $\nu = 3 = p - 2$, the bound of Corollary 4.3.12.

Node: SG0000007T

**Example 4.3.15 (types Cn and P, $p = 2$, with $X$ regular).** Let $g = x + y^3$ and $E = \{x\}$. The derivations $x \partial_x$, $\partial_y$, $\partial_w$ give $\mathcal{J} = (x, y^2)$, since $3 = 1$ in $\mathbb{F}_2$, and $H = 1$. So $J = (x, y^2)$, and $\nu = 1$ exactly on the $w$-axis $C = V(x, y)$. The derivations that preserve $(x)$ and $(x, y)$ are generated by $x \partial_x$, $x \partial_y$, $y \partial_y$, $\partial_w$, and they give $J(B, g, E, C) = (x, x y^2, y^3)$, so $\alpha(C, 0) = 1 \ge \nu$. So the algorithm blows up $C$, or first some closed points of $C$. Both fail the test, since $\operatorname{ord}_C(g_c) = 1 < 2$. In fact $X = V(z^2 + x + y^3)$ is regular along all of $C$, because of the linear term $x$. So the test fails along a curve of $\operatorname{Sing}(B)$ on which $X$ is regular.

**Example 4.3.16 (type Cn, $p = 2$, a failing curve through a point of multiplicity $p$).** Let $g = xw + y^3$ and $E = \{x\}$ on $B = \mathbb{A}^3$. The derivations $x \partial_x$, $\partial_y$, $\partial_w$ give
$$\mathcal{J} = (xw, y^2, x) = (x, y^2), \qquad H = 1.$$
So $\nu = 1$ exactly on the $w$-axis $C$, and $\operatorname{Sing}(B) = \operatorname{Sing}_1 = C$ is one irreducible curve. The derivations that preserve $(x)$ and $(x, y)$ give $J(B, g, E, C) = (x, y^3)$, so $\alpha(C, x) = 1 = \alpha(C, \eta)$ at each point, and $C$ is permis. Also $m(C) = 1$, the number of components of $E$ that contain $C$. Each other curve through the origin has $\nu = 0$. So $C$ is the unique curve of the test of a good point at the origin, it is permis, and $\nu(C) = \nu(0)$: the test at the origin starts with the blowup of $C$ [Cos87, II.C.3 (iv)]. If the origin is good, this is the blowup that the algorithm chooses at the origin. If it is bad, the origin is blown up first.

The test fails along $C$: $g|_C = 0$ and $\operatorname{ord}_C(g) = 1$. So $X$ has multiplicity $1$ at the generic point of $C$, and at each closed point $(0, 0, w_0)$ with $w_0 \ne 0$, because of the linear term $w_0 x$. But $X$ has multiplicity $2 = p$ at the origin, since $g$ has order $2$ there. So a center that the test of a good point selects, at a point of $\operatorname{Sing}_p X$, fails the test of Theorem 4.3.6. We have not decided whether the full algorithm blows up $C$ or the origin first. In both cases, $C$ is a candidate center that meets $\operatorname{Sing}_p X$ and is not permissible for $X$ at that point. This is Example 47.A of the research notes.

Node: SG0000007V

The same happens for $p = 2$, $g = xw + x^5 w + x y^2 + x w^4$, $E = \{w\}$, near the origin, along the curve $V(y, w)$ of type Cn. There $\nu(C) = \nu(0) = 1$ and $\operatorname{ord}_C(g_c) = 1$, so the generic multiplicity is $1$, but the origin has multiplicity $2$. For $p = 5$, $g = 2 y^8 w^4 + 3 y^{12} + 3 x^2 y^4 w^2 + 3 x^4 + 4 x^9 w^3$ with $E = \{x, y\}$ and $C = V(x, y)$ has $\nu(C) = \operatorname{ord}_C(g_c) = 4 = p - 1$, so Proposition 4.3.11 is sharp.

Centers also pass. For $p = 2$, $g = y^2 w + y^3$, $E = \{w\}$ and $C = V(x, y)$, the test holds with $h = 0$, and $\nu(C) = 2$. For $p = 3$, $g = x^3 + y^3 w$ and the $w$-axis of Remark 4.3.7, the test holds with $h = 0$, and $\nu(C) = 3$. Both have generic multiplicity $p$.

### What the results say

Theorem 4.3.6 settles the question of Section 4.2 for each regular center, chosen by any algorithm. A base blowup along $C$ lifts to a permissible blowup of $X$, along $C' = V(z - b, I_C)$ with $C'$ in normal crossings with the boundary, exactly when $X$ has multiplicity $p$ at the generic point of $C$. No center that lies in the multiplicity $p$ locus fails (Corollary 4.3.8). This does not say that the algorithm of Cossart is a sequence of permissible blowups of $X$. It is not. Centers that fail occur for every $p$ (Examples 4.3.14 to 4.3.16), and a failing center can pass through closed points where $X$ has multiplicity $p$ (Example 4.3.16).

For the resolution of $X$ alone this changes nothing. In $B \times \mathbb{A}^1$, the base blowup along $C$ is the blowup along $C \times \mathbb{A}^1$, and the transform of $X$ is $V(z^p + \pi^* g)$, which is integral and birational to $X$. At a passing center, the permissible blowup along $C'$ gives the finite birational map $z'' = (z - h)/x_1$ of this transform, and the invariants of Cossart are the same for both. At the end $\nu = 0$, the normal form of Giraud leaves toric singularities [Gir75], and these are resolved by known means. For the embedded problem, the failing centers must be handled by other methods, and these methods must also work near the points of multiplicity $p$ that the failing centers pass through. Whether a rule for the centers exists that makes $\nu$ drop, and for which each center that meets $\operatorname{Sing}_p X$ lies in $\operatorname{Sing}_p X$, is open. Volume 9, Section 3.20 reports the result and the tests.

*Lean.* The file `Singularity/Portfolio/Mixed.lean` of tamnd/singularity-lean proves Proposition 4.3.1 and Corollary 4.3.2 for a commutative ring of exponential characteristic $p$. The order form is `Singularity.Portfolio.X_pow_add_C_mem_pow_iff_order`, the statement with $J$, $J^q$ and $J^{q+1}$ is `Singularity.Portfolio.lift_base_blowup`, and the chart is `Singularity.Portfolio.lift_base_blowup_chart`. The description of the powers of $(z) + I R[z]$ by the coefficients, which is the claim in the proof of Proposition 4.3.1, is `Singularity.Portfolio.mem_span_X_sup_map_C_pow_iff`. The order along $J$ in Lean is the order with ordinary powers. The generic multiplicity and the order at the generic point of the center are not in Lean, and Lean does not prove that the two orders agree when $R$ and $R/I$ are regular (Lemma 4.3.4 is not in Lean). Lean does not prove that the blowup is permissible, it has no blowup of a scheme, and the chart is a ring identity: Lean does not prove that $z''^q + g''$ is the strict transform. Lemmas 4.3.4 and 4.3.5, Theorem 4.3.6 and the other results of this section have no Lean proof yet.

### Notes and references

The test of Proposition 4.3.1 is Lemma 10.5 of note 10 of the research notes. Theorem 4.3.6 and the results after it are from note 43, with the corrections of the referee report in note 47, as a result of the track Q1 of this project (tamnd/singularity#284). Example 4.3.16 is from note 47. The algorithm and the invariants $\nu$ and $\alpha$ are in the thesis of Cossart, *Polyèdre caractéristique d'une singularité*, Thèse d'État, Orsay 1987 [Cos87]. We cite it with the numbering of the chapters of Posva: Definition I.D.1, Remarque II.B.3.1, Algorithme II.B.10.8, Algorithme du point bon II.C.3, Proposition II.C.5.1 and Algorithme II.C.5.3 are in the first volume. Posva restates the algorithm in [Pos24, Appendix A]. Equimultiplicity and normal flatness are in [Hir64] and [Benn70]. Cossart and Piltant blow up closed points and regular curves that are permissible in the sense of Hironaka [CP08, CP09], so for their proof the question of this section does not arise.
