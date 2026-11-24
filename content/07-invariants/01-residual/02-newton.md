---
title: The Newton polyhedron
nodes: [SG00000011, SG00000014]
sources: [Newt, Hir67, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Newton polyhedron

The order of $f$ remembers only the smallest degree of a monomial of $f$. The Newton polyhedron remembers all the monomials that can be minimal for some choice of weights on the variables. In this section we define it, prove that its vertices are monomials of $f$, and prove the theorem of Ostrowski on products. We write $\mathbb{R}_{\ge 0}^n$ for the closed positive orthant, and $\langle \omega, u \rangle = \sum_i \omega_i u_i$.

### Definition and first properties

**Definition 1.2.1.** Let $f \in R$ be nonzero. The *Newton polyhedron* of $f$ is
$$N(f) = \operatorname{conv}(\operatorname{supp} f) + \mathbb{R}_{\ge 0}^n \subseteq \mathbb{R}_{\ge 0}^n,$$
the convex hull of the support plus the positive orthant.

Lean: Singularity.newtonPolyhedron (for polynomials)

For example, $N(x^2 - y^3)$ is the set of the points of $\mathbb{R}_{\ge 0}^2$ above the segment from $(2, 0)$ to $(0, 3)$. For a monomial times a unit, $N(x^\alpha u) = \alpha + \mathbb{R}_{\ge 0}^n$, because the support of $x^\alpha u$ contains $\alpha$ and is in $\alpha + \mathbb{N}^n$.

**Lemma 1.2.2.** Let $f \ne 0$, and let $V$ be the set of the minimal elements of $\operatorname{supp} f$ for the partial order of $\mathbb{N}^n$. Then $V$ is finite and $N(f) = \operatorname{conv}(V) + \mathbb{R}_{\ge 0}^n$. In particular, $N(f)$ is a polyhedron, and each vertex of $N(f)$ is in $\operatorname{supp} f$.

Lean: none yet

*Proof.* By the lemma of Dickson, each subset of $\mathbb{N}^n$ has only finitely many minimal elements, and each element of the subset is above a minimal element. So $V$ is finite, and $\operatorname{supp} f \subseteq V + \mathbb{N}^n$. Thus $\operatorname{conv}(\operatorname{supp} f) + \mathbb{R}_{\ge 0}^n \subseteq \operatorname{conv}(V) + \mathbb{R}_{\ge 0}^n$. The other inclusion is clear, because $V \subseteq \operatorname{supp} f$. A set of the form $\operatorname{conv}(V) + \mathbb{R}_{\ge 0}^n$ with $V$ finite is a polyhedron, and its vertices are in $V$. $\square$

### Weights and initial forms

Let $\omega \in \mathbb{R}_{>0}^n$ be a *weight vector*. The *$\omega$-order* of $f \ne 0$ is $\operatorname{ord}_\omega f = \min \{ \langle \omega, \alpha \rangle : \alpha \in \operatorname{supp} f \}$. The minimum exists, because the set of the $\alpha \in \mathbb{N}^n$ with $\langle \omega, \alpha \rangle \le c$ is finite for each $c$. The *$\omega$-initial form* of $f$ is the polynomial
$$\operatorname{in}_\omega(f) = \sum_{\langle \omega, \alpha \rangle = \operatorname{ord}_\omega f} c_\alpha x^\alpha.$$
For $\omega = (1, \dots, 1)$ these are the order and the initial form of Section 1.1. The linear function $\langle \omega, \cdot \rangle$ is bounded below on $N(f)$, and its minimum on $N(f)$ is $\operatorname{ord}_\omega f$, because a linear function has the same minimum on a set and on its convex hull, and it does not decrease in the directions of the orthant. The points of $N(f)$ where the minimum is attained are a face of $N(f)$, and the exponents of $\operatorname{in}_\omega(f)$ are the points of $\operatorname{supp} f$ on this face.

**Proposition 1.2.3.** Let $f \ne 0$. Then $\operatorname{ord} f = \min \{ u_1 + \cdots + u_n : u \in N(f) \}$.

Lean: Singularity.isLeast_sum_newtonPolyhedron

*Proof.* This is the case $\omega = (1, \dots, 1)$ of the remark before the proposition. $\square$

**Theorem 1.2.4 (Ostrowski).** Let $f, g \in R$ be nonzero and let $\omega \in \mathbb{R}_{>0}^n$. Then

1. $\operatorname{in}_\omega(fg) = \operatorname{in}_\omega(f) \operatorname{in}_\omega(g)$ and $\operatorname{ord}_\omega(fg) = \operatorname{ord}_\omega f + \operatorname{ord}_\omega g$;
2. $N(fg) = N(f) + N(g)$, the Minkowski sum.

Lean: Singularity.initialForm_mul, Singularity.newtonPolyhedron_mul_subset (part (1) for integer weights, and the inclusion $N(fg) \subseteq N(f) + N(g)$ of part (2))

*Proof.* (1) Let $a = \operatorname{ord}_\omega f$ and $b = \operatorname{ord}_\omega g$. Each monomial of $fg$ is a product of a monomial of $f$ and a monomial of $g$, so it has $\omega$-weight at least $a + b$. The sum of the terms of weight $a + b$ is $\operatorname{in}_\omega(f) \operatorname{in}_\omega(g)$. This product is not $0$, because $K[x]$ is a domain.

(2) Since $\operatorname{supp}(fg) \subseteq \operatorname{supp} f + \operatorname{supp} g$ and the right side of (2) is convex and stable under the addition of $\mathbb{R}_{\ge 0}^n$, we have $N(fg) \subseteq N(f) + N(g)$. By Lemma 1.2.2, $P = N(f) + N(g)$ is a polyhedron of the form $\operatorname{conv}(W) + \mathbb{R}_{\ge 0}^n$ with $W$ finite, so it is the convex hull of its vertices plus the orthant. Thus it is sufficient to prove that each vertex $v$ of $P$ is in $\operatorname{supp}(fg)$. The set of the linear functions whose minimum on $P$ is attained only at $v$ is open and not empty, and each of them is nonnegative on the orthant. So there is $\omega \in \mathbb{R}_{>0}^n$ such that $v$ is the only point of $P$ where $\langle \omega, \cdot \rangle$ is minimal. Write $v = u + w$ with $u \in N(f)$ and $w \in N(g)$. Then $u$ is the only point of $N(f)$ where $\langle \omega, \cdot \rangle$ is minimal, and $w$ is the only such point of $N(g)$. So $\operatorname{in}_\omega(f) = c_u x^u$ and $\operatorname{in}_\omega(g) = d_w x^w$ are monomials. By (1), $\operatorname{in}_\omega(fg) = c_u d_w x^v \ne 0$, and $v \in \operatorname{supp}(fg)$. $\square$

**Example 1.2.5.** Let $f = x^2 - y^3$ and $\omega = (3, 2)$. Both monomials have weight $6$, so $\operatorname{in}_\omega(f) = f$, and the face of $N(f)$ for $\omega$ is the segment from $(2, 0)$ to $(0, 3)$. For $\omega = (1, 1)$, the initial form is $x^2$, and the face is the vertex $(2, 0)$. The polyhedron $N(f^2)$ is $2 N(f)$, with the vertices $(4, 0)$ and $(0, 6)$, as Theorem 1.2.4 says.

### The projected polyhedron and the characteristic polyhedron

Let $f = z^q + F(x)$ with $\operatorname{ord} F \ge q$. The polyhedron that the resolution theory in characteristic $p$ uses is the *projected Newton polyhedron* $\Delta(f; x; z) = \frac{1}{q} N(F)$, a polyhedron in the space of the exponents of $x$. For a general $f = z^q + \sum_{k < q} a_k(x) z^k$, it is the polyhedron generated by the points $\alpha/(q - k)$ with $\alpha \in \operatorname{supp} a_k$ [Hir67]. It depends on the choice of $z$ and of $x$. Hironaka defined the *characteristic polyhedron* as the intersection of the polyhedra $\Delta(f; x; z)$ over all choices of $z$, for fixed $x$, and he proved that a choice of $z$ that attains it exists [Hir67]. This volume does not prove that theorem. The polyhedron is the main tool of Cossart and Piltant in dimension $3$ and of the surface case of Cossart, Jannsen and Saito.

We fix the setting of the Lean library. Let $k$ be a commutative ring, let $A = k[[x_1, \dots, x_n]]$, and let $f = z^m + a_1 z^{m-1} + \dots + a_m$ with $a_i \in A$. Let $\Delta(f; x; z)$ be the convex hull of the points $\alpha / i$, for $1 \le i \le m$ and $x^\alpha$ a monomial of $a_i$, plus $\mathbb{R}_{\ge 0}^n$. Let $\Delta(f; x)$ be the intersection of the polyhedra $\Delta(f(z + \varphi); x; z)$ over all $\varphi \in A$ with $\varphi(0) = 0$. For $v \in \mathbb{N}^n$, the *initial polynomial* of $f$ at $v$ is $P_v(Z) = \sum_d c_d Z^d$ in $k[Z]$, where $c_d$ is the coefficient of $x^{(m - d) v}$ in the coefficient of $z^d$ of $f$. It is the initial form of $f$ at $v$ after the substitution $z = Z x^v$ and the division by $x^{m v}$. We say that $v$ is *solvable* with the constant $c \in k$ if $P_v(Z) = (Z + c)^m$.

**Proposition 1.2.6.** In this setting, the following hold.

(1) The set $\Delta(f; x)$ is convex, and $\Delta(f; x) + \mathbb{R}_{\ge 0}^n = \Delta(f; x)$.

(2) If $\psi \in A$ and $\psi(0) = 0$, then $\Delta(f(z + \psi); x) = \Delta(f; x)$.

(3) Let $v \in \mathbb{N}^n$ be a vertex of $\Delta(f; x; z)$ that is solvable with the constant $c$. Then $v \notin \Delta(f(z - c x^v); x; z)$. If also $v \ne 0$, then $v \notin \Delta(f; x)$, and so $\Delta(f; x; z) \ne \Delta(f; x)$.

Lean: Singularity.convex_charPolyhedron, Singularity.charPolyhedron_add_orthant, Singularity.charPolyhedron_taylor, Singularity.notMem_projPolyhedron_taylor_of_isSolvable, Singularity.not_isSolvableVertex_of_charPolyhedron_eq

*Proof.* (1) Each $\Delta(f(z + \varphi); x; z)$ is convex and stable under the addition of the orthant. Both properties pass to intersections.

(2) The map $\varphi \mapsto \varphi + \psi$ is a bijection of the set of the series with constant term $0$, and $f(z + \psi)(z + \varphi) = f(z + \psi + \varphi)$. So the two intersections run over the same polyhedra.

(3) Write $b_e$ for the coefficient of $z^e$ in $f$. By the Taylor formula, the coefficient of $z^d$ in $f(z + h)$ is $\sum_{e \ge d} \binom{e}{d} b_e h^{e - d}$. Take $h = t x^\beta$ with $t \in k$. A monomial $x^\gamma$ of the new coefficient of $z^{m - i}$ has the form $\gamma = (i - j) \beta + \alpha'$, with $x^{\alpha'}$ a monomial of $a_j$ and $j \le i$. If $j \ge 1$, then $\gamma / i$ is a convex combination of $\beta$ and $\alpha' / j$. If $j = 0$, then $\gamma / i = \beta$. Thus $\Delta(f(z + t x^\beta); x; z)$ lies in the convex hull of $\Delta(f; x; z)$ and $\beta + \mathbb{R}_{\ge 0}^n$. If $\beta \in \Delta(f; x; z)$, this convex hull is $\Delta(f; x; z)$ itself.

The same formula, applied to the coefficient of $x^{(m - d) v}$ with $\beta = v$, gives $P_v$ of $f(z + t x^v)$ equal to $P_v(Z + t)$. This identity needs no hypothesis on $v$. Now let $t = -c$ and $g = f(z - c x^v)$. Then $P_v$ of $g$ is $(Z - c + c)^m = Z^m$. Since $v \in \Delta(f; x; z)$, we have $\Delta(g; x; z) \subseteq \Delta(f; x; z)$. Suppose that $v \in \Delta(g; x; z)$. Then $v$ is an extreme point of the smaller set, because it is an extreme point of the larger set. As in the proof of Lemma 1.2.2, each vertex of a set $\operatorname{conv}(S) + \mathbb{R}_{\ge 0}^n$ is in $S$. So $v = \alpha / i$ for some $1 \le i \le m$ and some monomial $x^\alpha$ of the coefficient of $z^{m - i}$ of $g$. Then $\alpha = i v$, so the coefficient of $Z^{m - i}$ in $P_v$ of $g$ is not $0$. This is false for $Z^m$, because $i \ge 1$. So $v \notin \Delta(g; x; z)$.

If $v \ne 0$, then $-c x^v$ has constant term $0$. So $\Delta(f; x) \subseteq \Delta(g; x; z)$, and $v \notin \Delta(f; x)$. Since $v \in \Delta(f; x; z)$, the two polyhedra are not equal. $\square$

Part (3) is one direction of the vertex criterion of Hironaka [Hir67]: if $z$ attains $\Delta(f; x)$, then no vertex $v \ne 0$ of $\Delta(f; x; z)$ is solvable. The converse is the hard direction. It says that when no vertex is solvable, $z$ already attains $\Delta(f; x)$. Hironaka proves it, and he also proves that a sequence of vertex preparations converges in the $(x)$-adic topology to a $z$ that attains the polyhedron [Hir67]. Neither of these results is in the Lean library yet. Proposition 1.2.7 below proves the converse for the equations $z^q + F$ with $F$ clean, by a direct argument. When the vertices are not in $\mathbb{N}^n$, the criterion needs the initial form on a face, and not only at a point. Cossart, Jannsen and Schober give a full proof over a general regular local ring [CJSch19].

### The purely inseparable equation

For the equation $f = z^q + F$ of Section 1.3, the characteristic polyhedron can be computed directly. The computation needs no limit, and it gives the converse of Proposition 1.2.6(3) for these equations. We keep the setting of Proposition 1.2.6, and we assume in addition that $k \ne 0$ and that $k$ has exponential characteristic $p$. This means that either $p$ is a prime number and $p = 0$ in $k$, or $p = 1$ and $k$ has characteristic $0$. Let $e \ge 0$ and $q = p^e$. As in Definition 1.3.1, a series $F = \sum_\alpha c_\alpha x^\alpha$ in $A$ is *clean* if $c_\alpha = 0$ for each $\alpha \in q\mathbb{N}^n$. Since $0 \in q\mathbb{N}^n$, a clean series has $F(0) = 0$. If $p = 1$, then $q = 1$, and only $F = 0$ is clean.

**Proposition 1.2.7.** Let $F \in A$ be clean, and let $f = z^q + F$.

(1) For each $\varphi \in A$, we have $f(z + \varphi) = z^q + (\varphi^q + F)$ and $\Delta(f; x; z) \subseteq \Delta(f(z + \varphi); x; z)$.

(2) The coordinate $z$ attains the characteristic polyhedron: $\Delta(f; x) = \Delta(f; x; z)$.

(3) No vertex $v \in \mathbb{N}^n$ of $\Delta(f; x; z)$ with $v \ne 0$ is solvable.

(4) If $F$ is a polynomial, then $\Delta(f; x) = \frac{1}{q} N(F)$.

Lean: `Singularity.taylor_X_pow_add_C`, `Singularity.projPolyhedron_subset_taylor_of_clean`, `Singularity.charPolyhedron_X_pow_add_C_of_clean`, `Singularity.not_isSolvableVertex_of_clean`, `Singularity.charPolyhedron_X_pow_add_C_eq_smul_newtonPolyhedron`, with the lemmas `Singularity.coeff_pow_expChar_pow_eq_zero` (Step 1), `Singularity.projPoints_X_pow_add_C` (Step 3) and `Singularity.projPolyhedron_X_pow_add_C_coe` (the formula $\Delta(z^m + F; x; z) = \frac{1}{m} N(F)$ for each polynomial $F$ and $m \ge 1$)

*Proof.* Step 1. We show that each exponent of $\varphi^q$ lies in $q\mathbb{N}^n$, for each $\varphi = \sum_\beta b_\beta x^\beta$ in $A$. If $p = 1$, there is nothing to prove. Let $p$ be a prime number. The binomial coefficients $\binom{p}{i}$ with $0 < i < p$ are divisible by $p$. So the map $a \mapsto a^p$ is a ring endomorphism of each commutative $k$-algebra, and so is its $e$-th iterate $a \mapsto a^q$. Fix $d \in \mathbb{N}^n$ and let $N = d_1 + \dots + d_n$. Write $\varphi = \varphi_0 + \psi$, where $\varphi_0$ is the sum of the terms of $\varphi$ of degree at most $N$, and $\psi \in (x)^{N + 1}$. Then $\varphi^q = \varphi_0^q + \psi^q$. The series $\psi^q$ is in $(x)^{q(N + 1)}$, so its coefficient of $x^d$ is $0$. The polynomial $\varphi_0$ is a finite sum of terms $b_\beta x^\beta$, so $\varphi_0^q = \sum_{|\beta| \le N} b_\beta^q x^{q\beta}$. Thus the coefficient of $x^d$ in $\varphi^q$ is $0$ if $d \notin q\mathbb{N}^n$.

Step 2. The ring $A[z]$ is a $k$-algebra, so by Step 1 the map $a \mapsto a^q$ is additive on $A[z]$. Thus $(z + \varphi)^q = z^q + \varphi^q$, and $f(z + \varphi) = z^q + (\varphi^q + F)$. This is the first claim of (1).

Step 3. Let $m \ge 1$ and $G \in A$. In $z^m + G$, the coefficient of $z^{m - i}$ is $0$ for $1 \le i < m$, and it is $G$ for $i = m$. Since $k \ne 0$, the degree of $z^m + G$ is $m$. So the points that define $\Delta(z^m + G; x; z)$ are the points $\alpha / m$ with $\alpha \in \operatorname{supp} G$, and
$$\Delta(z^m + G; x; z) = \operatorname{conv}\bigl\{ \tfrac{1}{m} \alpha : \alpha \in \operatorname{supp} G \bigr\} + \mathbb{R}_{\ge 0}^n.$$

Step 4. We prove the second claim of (1). Let $\alpha \in \operatorname{supp} F$. Since $F$ is clean, $\alpha \notin q\mathbb{N}^n$. By Step 1, the coefficient of $x^\alpha$ in $\varphi^q$ is $0$, so the coefficient of $x^\alpha$ in $\varphi^q + F$ is $c_\alpha \ne 0$. Thus $\operatorname{supp} F \subseteq \operatorname{supp}(\varphi^q + F)$. By Step 2 and Step 3 with $m = q$, the points that define $\Delta(f; x; z)$ are among the points that define $\Delta(f(z + \varphi); x; z)$. The convex hull plus the orthant is monotone in the set of points, so $\Delta(f; x; z) \subseteq \Delta(f(z + \varphi); x; z)$.

(2) The series $\varphi = 0$ has constant term $0$, so $\Delta(f; x) \subseteq \Delta(f; x; z)$ by the definition of $\Delta(f; x)$. By (1), $\Delta(f; x; z)$ is contained in each polyhedron of the intersection that defines $\Delta(f; x)$, so $\Delta(f; x; z) \subseteq \Delta(f; x)$.

(3) Suppose that a vertex $v \ne 0$ of $\Delta(f; x; z)$ is solvable. Then $\Delta(f; x; z) \ne \Delta(f; x)$ by Proposition 1.2.6(3). This contradicts (2).

(4) Let $S = \operatorname{supp} F$. By (2) and Step 3 with $m = q$, we have $\Delta(f; x) = \operatorname{conv}(\frac{1}{q} S) + \mathbb{R}_{\ge 0}^n$. The map $u \mapsto \frac{1}{q} u$ is linear, so $\operatorname{conv}(\frac{1}{q} S) = \frac{1}{q} \operatorname{conv}(S)$. Also $\frac{1}{q} \mathbb{R}_{\ge 0}^n = \mathbb{R}_{\ge 0}^n$, and multiplication by $\frac{1}{q}$ distributes over the Minkowski sum. So $\Delta(f; x) = \frac{1}{q} \bigl( \operatorname{conv}(S) + \mathbb{R}_{\ge 0}^n \bigr) = \frac{1}{q} N(F)$. $\square$

Part (3) also has a direct proof. As in the proof of Proposition 1.2.6(3), each vertex of $\Delta(f; x; z)$ is a point $\alpha / q$ with $\alpha \in \operatorname{supp} F$. Since $\alpha \notin q\mathbb{N}^n$, the point $\alpha / q$ is not in $\mathbb{N}^n$. So $\Delta(f; x; z)$ has no vertex in $\mathbb{N}^n$ at all, and the content of (3) in this case is small. The content of the proposition is (2). For these equations, the hypothesis of the converse of Proposition 1.2.6(3) and its conclusion both always hold. The proof uses only that a translation of $z$ adds a $q$-th power to $F$, and that a $q$-th power has no monomial in common with a clean series. For $q = p$ and a perfect field, this is the argument of Volume 6, Proposition 3.2.4(1).

**Example 1.2.8.** Let $k$ be a field of characteristic $2$, so $p = 2$. Let $e = 1$, so $q = 2$, let $n = 2$ with the variables $x$ and $y$, and let $F = x^3 + y^5$ and $f = z^2 + x^3 + y^5$. The exponents of $F$ are $(3, 0)$ and $(0, 5)$. Neither is in $2\mathbb{N}^2$, because $3$ and $5$ are odd. So $F$ is clean. By Proposition 1.2.7(4),
$$\Delta(f; x) = \tfrac{1}{2} N(F) = \operatorname{conv}\{ (\tfrac{3}{2}, 0), (0, \tfrac{5}{2}) \} + \mathbb{R}_{\ge 0}^2 = \{ (u, w) \in \mathbb{R}_{\ge 0}^2 : 10 u + 6 w \ge 15 \}.$$
The last equality holds because the line $10 u + 6 w = 15$ passes through $(\frac{3}{2}, 0)$ and $(0, \frac{5}{2})$. The two vertices are not in $\mathbb{N}^2$, as the remark after the proof says.

Now we translate $z$ by $\varphi = x$. Then $f(z + x) = z^2 + x^2 + x^3 + y^5$, by Step 2 of the proof. Its points are $(1, 0)$, $(\frac{3}{2}, 0)$ and $(0, \frac{5}{2})$, so
$$\Delta(f(z + x); x; z) = \operatorname{conv}\{ (1, 0), (0, \tfrac{5}{2}) \} + \mathbb{R}_{\ge 0}^2 = \{ (u, w) \in \mathbb{R}_{\ge 0}^2 : 5 u + 2 w \ge 5 \}.$$
The point $(\frac{3}{2}, 0)$ is in this set, since $5 \cdot \frac{3}{2} = \frac{15}{2} \ge 5$. The new polyhedron contains $\Delta(f; x)$, as Proposition 1.2.7(1) says, and it is strictly larger: it contains $(1, 0)$, and $10 \cdot 1 + 6 \cdot 0 = 10 < 15$. The point $v = (1, 0)$ is a vertex of the new polyhedron, and $v \in \mathbb{N}^2$. Its initial polynomial is $P_v(Z) = Z^2 + 0 \cdot Z + 1$. Here the constant $1$ is the coefficient of $x^{2v} = x^2$ in $x^2 + x^3 + y^5$, and the coefficient of $z$ is $0$. In characteristic $2$, $Z^2 + 1 = (Z + 1)^2$. So $v$ is solvable with the constant $c = 1$. The vertex preparation of Proposition 1.2.6(3) replaces $z$ by $z - x$, and it gives back $f$. The series $F' = x^2 + x^3 + y^5$ is not clean, and $F$ is its clean part. By Proposition 1.2.6(2), $\Delta(f(z + x); x) = \Delta(f; x)$, which is strictly smaller than $\Delta(f(z + x); x; z)$.

**Remark 1.2.9 (what is not proved).** (1) The converse of Proposition 1.2.6(3) for a general $f = z^m + a_1 z^{m - 1} + \dots + a_m$ is not proved here and is not in the Lean library. This also holds for the existence of a $z$ that attains $\Delta(f; x)$, and for the convergence of the vertex preparations [Hir67]. Proposition 1.2.7 avoids these results, because for $z^q + F$ with $F$ clean a translation of $z$ can only add points. For a general $f$, a translation can remove points, as in Example 1.2.8 read from $f(z + x)$ back to $f$.

(2) If $F$ is not clean, Proposition 1.2.7 does not apply. Over a perfect field of characteristic $p$, Lemma 1.3.2 gives $g$ with $g^q + F = F^{\mathrm{cl}}$. If $F(0) = 0$, then $g(0)^q = -F(0) = 0$, so $g(0) = 0$. Then $f(z + g) = z^q + F^{\mathrm{cl}}$ by Step 2, and Proposition 1.2.6(2) and Proposition 1.2.7(2) give $\Delta(f; x) = \Delta(z^q + F^{\mathrm{cl}}; x; z)$. The Lean library has the existence of $g$ for a polynomial $F$ (`Singularity.exists_add_pow_eq_cleanPart`), but it does not state this result. Over a field that is not perfect, a monomial $c x^{q\beta}$ such that $c$ is not a $q$-th power cannot be removed in this way, and we do not compute $\Delta(f; x)$ in that case.

(3) Parts (1), (2) and (3) of Proposition 1.2.7 are in Lean for each power series $F$. Part (4) is in Lean only for a polynomial $F$, because the Lean definition `Singularity.newtonPolyhedron` is for polynomials. The proof of part (4) works without change for a power series $F$, with $N(F)$ as in Definition 1.2.1.

### Notes and references

The theorem of Ostrowski is usually stated for polynomials. The proof above is the usual proof, and it works for power series because Lemma 1.2.2 makes $N(f)$ a polyhedron with finitely many vertices. Newton polyhedra in resolution go back to Newton's method for plane curves. Hironaka introduced the characteristic polyhedron in [Hir67], and [Hau10] explains its role in characteristic $p$.
