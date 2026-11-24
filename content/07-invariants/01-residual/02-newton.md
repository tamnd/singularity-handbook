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

### Notes and references

The theorem of Ostrowski is usually stated for polynomials. The proof above is the usual proof, and it works for power series because Lemma 1.2.2 makes $N(f)$ a polyhedron with finitely many vertices. Newton polyhedra in resolution go back to Newton's method for plane curves. Hironaka introduced the characteristic polyhedron in [Hir67], and [Hau10] explains its role in characteristic $p$.
