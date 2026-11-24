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

Part (3) is one direction of the vertex criterion of Hironaka [Hir67]: if $z$ attains $\Delta(f; x)$, then no vertex $v \ne 0$ of $\Delta(f; x; z)$ is solvable. The converse is the hard direction. It says that when no vertex is solvable, $z$ already attains $\Delta(f; x)$. Hironaka proves it, and he also proves that a sequence of vertex preparations converges in the $(x)$-adic topology to a $z$ that attains the polyhedron [Hir67]. Neither of these results is in the Lean library yet. When the vertices are not in $\mathbb{N}^n$, the criterion needs the initial form on a face, and not only at a point. Cossart, Jannsen and Schober give a full proof over a general regular local ring [CJSch19].

### Notes and references

The theorem of Ostrowski is usually stated for polynomials. The proof above is the usual proof, and it works for power series because Lemma 1.2.2 makes $N(f)$ a polyhedron with finitely many vertices. Newton polyhedra in resolution go back to Newton's method for plane curves. Hironaka introduced the characteristic polyhedron in [Hir67], and [Hau10] explains its role in characteristic $p$.
