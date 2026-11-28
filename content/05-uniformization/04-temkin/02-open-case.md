---
title: What the theorem does not give
nodes: [SG0000001G, SG00000009, SG0000001H, SG0000001J, SG0000001N, SG00000010]
sources: [Tem13, Tem23, Tem17, Eis95]
status: drafted
drafted_by: writer
reviewed_by: []
---
## What the theorem does not give

A reader who sees Theorem 4.1.1 for the first time may ask why it does not finish the problem. For a purely inseparable extension $L/K$, each valuation of $K$ has exactly one extension to $L$, and the normalization of a normal model in $L$ is homeomorphic to the model (Proposition 4.2.1). So it may seem that a regular center upstairs should give a regular center downstairs. It does not, and the reason is algebraic: the local rings change, and regularity is a property of the local ring and not of the topological space. This section makes the failure explicit and connects it with the defect.

Theorem 4.1.1 gives a regular center after a finite purely inseparable extension $L/K$. In this section we explain why this does not give a regular center for $v$ itself. There are three points. First, $L$ depends on the model, so no single extension serves all finite sets. Second, the map from the normalization in $L$ back to the model is a homeomorphism, but it is not birational, and regularity does not descend along it. Third, the extension of $v$ to $L$ can involve a defect. At the end we connect the remaining problem with the conjectures of Volume 9.

### The extension depends on the model

In Theorem 4.1.1 the fields $l$ and $L$ depend on $X$. So the Lean statement `Singularity.localUniformization_inseparable` takes the finite subset $S$ first, as in Section 4.1. Volume 3, Section 4.2, makes the same remark. If $S$ grows, the field $L$ can grow, and the degree $[L : K]$ need not stay bounded. A statement with one field $L$ for all finite sets $S$ would be stronger than the theorem of Temkin. We do not know if it is true.

### Regularity does not descend

**Proposition 4.2.1.** Let $k$ be a field of characteristic $p > 0$, let $A$ be a normal domain that is a finitely generated $k$-algebra with fraction field $K$, let $L/K$ be a finite purely inseparable extension, and let $B$ be the integral closure of $A$ in $L$. Then $B$ is a finite $A$-module, and the map $\operatorname{Spec} B \to \operatorname{Spec} A$ is a homeomorphism.

Lean: `Singularity.isHomeomorph_comap_integralClosure` (the map of spectra for a purely inseparable extension, in algebra). The statement on schemes is not in Lean yet.

*Proof.* The module $B$ is finite by [Eis95, Corollary 13.13]. Since $L/K$ is finite and purely inseparable, there is $n$ with $L^{p^n} \subseteq K$. Let $b \in B$. Then $b^{p^n}$ lies in $K$ and it is integral over $A$. Since $A$ is normal, $b^{p^n} \in A$.

The map is surjective, because $B$ is integral over $A$ and $A \subseteq B$ (lying over). It is closed, because an integral morphism is closed (going up). It is injective. Let $\mathfrak{q}_1$ and $\mathfrak{q}_2$ be primes of $B$ with $\mathfrak{q}_1 \cap A = \mathfrak{q}_2 \cap A$. If $b \in \mathfrak{q}_1$, then $b^{p^n} \in \mathfrak{q}_1 \cap A \subseteq \mathfrak{q}_2$, so $b \in \mathfrak{q}_2$. By symmetry $\mathfrak{q}_1 = \mathfrak{q}_2$. A continuous closed bijection is a homeomorphism. $\square$

So Theorem 4.1.1 gives a regular point $\mathfrak{q}$ of $\operatorname{Spec} B$ over the center $\mathfrak{p}$ of $v$ on $\operatorname{Spec} A'$. The point $\mathfrak{p}$ is the only point under $\mathfrak{q}$, but the local rings $A'_\mathfrak{p}$ and $B_\mathfrak{q}$ are different. The ring $B_\mathfrak{q}$ is regular, and $A'_\mathfrak{p}$ need not be. The next example shows this with the surface of Volume 4.

**Example 4.2.2.** Let $k$ be an algebraically closed field of characteristic $p > 0$, and let $L = k(a, b)$ be a field of rational functions in two variables. Let $x = a^p$, $y = b^p$ and $z = a^{p+1} + b^{p+1}$, and let $K = k(x, y, z) \subseteq L$. Let $A = k[x, y, z] \subseteq K$. Then:

1. $z^p = x^{p+1} + y^{p+1}$, and $A$ is the coordinate ring of the surface $X = V(z^p - x^{p+1} - y^{p+1}) \subseteq \mathbb{A}^3_k$ of Volume 4, Example 2.3.5.
2. $[K : k(x, y)] = p$ and $[L : K] = p$, and $L/K$ is purely inseparable.
3. The integral closure of $A$ in $L$ is $k[a, b]$.
4. The point $\mathfrak{m} = (x, y, z)$ of $X$ is singular.

Lean: `Singularity.add_pow_pow_succ_char`, `Singularity.surface_relation_mem_sq` (parts 1 and 4). Parts 2 and 3 are not in Lean yet.

*Proof.* We prove part 2 first. Part 2. Since $k$ is perfect, $k(x, y) = L^p$, the field of $p$-th powers of $L$. The monomials $a^i b^j$ with $0 \le i, j < p$ form a basis of $L$ over $L^p$, and the elements of $L^p$ are the multiples of the basis vector $1$. Now $z = a^p \cdot a + b^p \cdot b$ has the nonzero coordinates $a^p$ and $b^p$ on the basis vectors $a$ and $b$, which differ from $1$ because $p \ge 2$. So $z \notin k(x, y)$. Since $z^p \in k(x, y)$, the polynomial $T^p - z^p$ is irreducible over $k(x, y)$, and $[K : k(x, y)] = p$. The degree $[L : k(x, y)]$ is $p^2$, so $[L : K] = p$. Each element of $L$ has its $p$-th power in $L^p \subseteq K$, so $L/K$ is purely inseparable.

Part 1. In characteristic $p$ we have $(a^{p+1} + b^{p+1})^p = a^{p(p+1)} + b^{p(p+1)} = x^{p+1} + y^{p+1}$. The elements $x$ and $y$ are algebraically independent over $k$, since $L$ is algebraic over $k(x, y)$ and has transcendence degree 2. Let $\varphi \colon k[X, Y, Z] \to A$ map $X, Y, Z$ to $x, y, z$, and let $F = Z^p - X^{p+1} - Y^{p+1}$. Then $F$ is in the kernel of $\varphi$. By part 2 the polynomial $T^p - z^p$ is irreducible over $k(x, y)$, so by Gauss's lemma $F$ is irreducible in $k[X, Y][Z]$. The kernel of $\varphi$ is a prime ideal of height 1, because $A$ is a domain of dimension 2. In the unique factorization domain $k[X, Y, Z]$ a prime ideal of height 1 is principal, so the kernel is $(F)$.

Part 3. The elements $a$ and $b$ are integral over $A$, because $a^p = x$ and $b^p = y$. So $k[a, b]$ is integral over $A$. The ring $k[a, b]$ is a polynomial ring, so it is normal, and its fraction field is $L$. Hence it is the integral closure of $A$ in $L$.

Part 4. The ring $A_\mathfrak{m}$ has dimension 2. Its maximal ideal is generated by $x, y, z$. The relation $z^p - x^{p+1} - y^{p+1} = 0$ lies in the square of $(X, Y, Z)$, because $p \ge 2$. So $\mathfrak{m}/\mathfrak{m}^2$ has dimension 3 over $k$, and $A_\mathfrak{m}$ is not regular. $\square$

Let $v$ be a valuation of $K/k$ with center $\mathfrak{m}$ on $X$, and let $w$ be its extension to $L$. The center $\mathfrak{q}$ of $w$ on $\operatorname{Spec} k[a, b]$ lies over $\mathfrak{m}$. So $a^p = x$ and $b^p = y$ lie in $\mathfrak{q}$, hence $a, b \in \mathfrak{q}$, and $\mathfrak{q}$ is the origin $(a, b)$. The origin is a point of $\mathbb{A}^2_k$ with residue field $k$, so it is a simple $k$-smooth point. So the conclusion of Theorem 4.1.1 holds for $X$ itself, with $l = k$ and $X' = X$. But the center of $v$ on $X$ is singular. The conclusion of Theorem 4.1.1 gives no information on the singularities of $X'$.

In this example $v$ has local uniformization by Proposition 3.1.2, because $K/k$ has transcendence degree 2. The resolution of $X$ in Volume 4 and Proposition 1.4.5 give a regular center over $X$ itself. In dimension 4 no such resolution is known.

*Example (a defect step in Example 4.2.2).* Let $p$ be odd, keep the notation of Example 4.2.2, and let $w$ be the arc valuation of $L = k(a, b)$ given by $w(g) = \operatorname{ord}_t g(t, \varphi(t))$ with $\varphi = \sum_{i \ge 1} t^{i!}$, as in Example 3.2.1. Let $v$ be its restriction to $K$. Then $w(a) = w(b) = 1$, so the center of $w$ on $\operatorname{Spec} k[a, b]$ is the origin, and the center of $v$ on $X$ is the singular point $\mathfrak{m}$. We compute the invariants of $L/K$ at $w$. The coefficients of $\varphi$ lie in $\mathbb{F}_p$, so $\varphi(t)^p = \varphi(t^p)$, and
$$z \mapsto t^{p+1} + \varphi(t)^p\varphi(t) = t^{p+1} + (t^p + t^{2p} + \dots)(t + t^2 + t^6 + \dots) = 2t^{p+1} + t^{p+2} + \dots.$$
Since $p$ is odd, $v(z) = p + 1$. Also $v(x) = p$. So $\Gamma_v$ contains $p$ and $p + 1$, and $\Gamma_v = \mathbb{Z} = \Gamma_w$. The residue fields are both $k$. So $e = f = 1$ for $L/K$. The extension $L/K$ is purely inseparable of degree $p$. As in part 3 of Example 3.2.1, an element of $L \setminus K$ is not in the henselization $K^h$, which is separable over $K$, so $[L^h : K^h] = p$ and the defect of $w$ over $v$ is $p$. Thus the simple smooth center that Theorem 4.1.1 gives on $\operatorname{Spec} k[a, b]$ sits over the singular point $\mathfrak{m}$ through an immediate extension with defect $p$. The value group and the residue field cannot see the difference between $K$ and $L$. We checked the order $p + 1$ for $p = 3, 5, 7$ with sympy, using the truncation $t + t^2 + t^6 + t^{24}$ of $\varphi$. For $p = 2$ the leading term cancels, and we do not treat this case.

### The reduction to equations of the form $t^p = f$

Example 4.2.2 has a second reading. The Frobenius map $c \mapsto c^p$ is an isomorphism from $L$ onto $L^p = k(x, y)$. It maps $k[a, b]$ onto $k[x, y]$. So $K$ is a purely inseparable extension of degree $p$ of the field $K_0 = k(x, y)$, and $K_0$ has the regular model $k[x, y]$. The model $A$ of $K$ is $k[x, y][t]/(t^p - f)$ with $f = x^{p+1} + y^{p+1}$.

Temkin observes that this is the general situation [Tem13, Remark 1.3.5]. We state his remark in our notation, and we do not prove it. Assume that $[k : k^p]$ is finite. The remark gives a subfield $K_0 \subseteq K$ that contains $k$, such that $K/K_0$ is finite and purely inseparable and the restriction of $v$ to $K_0$ is centered on a regular point of a model of $K_0$. The idea is the following. Let $L$ be as in Theorem 4.1.1, and choose $n$ with $L^{p^n} \subseteq K$. The Frobenius map $c \mapsto c^{p^n}$ is an isomorphism of rings from $L$ onto $L^{p^n}$, and it maps a regular local ring to a regular local ring. But $L^{p^n}$ contains only $k^{p^n}$, and in general it does not contain $k$. So one must pass to the compositum $K_0 = k \cdot L^{p^n}$, a finite purely inseparable extension of $L^{p^n}$, and show that a regular center survives this passage. This is where the hypothesis on $[k : k^p]$ enters. We do not prove this step, and we only state the conclusion as Temkin's claim. The extension $K/K_0$ is finite and purely inseparable, so it is a tower
$$K_0 \subset K_1 \subset \dots \subset K_m = K, \qquad K_i = K_{i-1}(a_i), \quad a_i^p \in K_{i-1},$$
with each step of degree $p$. Roughly, if one can uniformize each valuation centered on a hypersurface $t^p = f$ over a regular model, then one can go up the tower one step at a time and uniformize $v$. In this sense Theorem 4.1.1 reduces local uniformization to the case of these hypersurfaces, which is called the inseparable case. Section 4.3 proves a form of this reduction over a perfect field (Theorem 4.3.2), and it reduces one step to weak log monomialization along a valuation. Section 4.4 weakens this input: it is sufficient that the log Jacobian ideal of the equation is principal on a regular model along the valuation (Corollaries 4.4.12 and 4.4.17). The existence of such a model is open in transcendence degree 4 and more.

The hypersurfaces $z^p + g = 0$ of Volume 9, Conjecture 2.3.7, are of this form, with $f = -g$ and the regular model a polynomial ring.

Node: SG00000009 · Lean: `Singularity.PurelyInseparableHypersurfaceResolution` (the statement only)

Volume 9, Conjecture 2.3.7, asks for a resolution, which is a global statement. By Proposition 1.4.5 a resolution of such a hypersurface gives local uniformization of the valuations of its function field. The remark of Temkin needs a local statement over each regular model, not only over a polynomial ring.

### The defect in the tower

Each step $K_i/K_{i-1}$ of the tower has degree $p$. So after the henselization, one of $e$, $f$ and $d$ for this step is $p$, as in Example 3.2.2. If $e = p$ or $f = p$, the step is seen by the value group or the residue field. If $d = p$, it is seen by neither, and this is the defect of Chapter 3 (node SG00000010, planned Lean name `Singularity.Valuation.defect`, no Lean statement yet). Volume 3, Section 4.2, shows that a purely inseparable extension can even create a defect. The method of Section 1.3 lifts local uniformization only through extensions with an étale generator. An étale generator $z$ has $P'(z) \ne 0$, so its minimal polynomial is separable. Hence a purely inseparable step of degree $p$ never has an étale generator. So Theorem 1.3.4 is of no use in the tower, and the inseparable case needs a new method. Example 3.2.3 shows one such step on a plane. There the lift $A_0[t]/(t^p - f)$ of a regular chart is regular exactly when $f - c$ is not in the square of the maximal ideal, where $c$ is the residue of $f$. A finer chart of $K_0$ can destroy this condition.

### The open steps in dimension 4

Volume 9, Section 2.3, describes the route of valuations in dimension 4. It needs two theorems, which are open.

The first one is Volume 9, Conjecture 2.3.1: let $K$ be a function field of transcendence degree 4 over a field $k$ of characteristic $p > 0$. Each valuation of $K$ that is trivial on $k$ has local uniformization.

Node: SG0000001H · Lean: `Singularity.LocalUniformizationFour` (the statement only)

The second one is Volume 9, Conjecture 2.3.2: let $X$ be a variety of dimension 4 over a field of characteristic $p > 0$. If each valuation of the function field of each component of $X$ has local uniformization, then $X$ has a resolution.

Node: SG0000001J · Lean: `Singularity.resolution_of_localUniformization_four` (the statement only)

Theorem 4.1.1 is not enough for the first conjecture, for the reasons of this section. Its local solutions also do not fit the patching of the second conjecture. A patching argument glues local solutions on finitely many models of $K$. Theorem 4.1.1 gives local solutions on the normalizations in different fields $L$, and these normalizations are not models of $K$.

Two other results of Temkin go in the same direction. He reduces local uniformization to valuations of height one [Tem23], as stated in Volume 9, Section 2.3. He also proves a global theorem with a cost of a power of $p$.

This is Volume 9, Theorem 2.3.10: each variety over a perfect field of characteristic $p$ has a regular alteration whose degree is a power of $p$.

Node: SG0000001N · Lean: `Singularity.exists_regular_p_alteration` (planned, no Lean statement yet)

This is [Tem17], and Volume 8 treats alterations. The alteration is not birational, as the map of Example 4.2.2 is not birational. In both results the variety becomes regular only after an extension of the function field whose degree is a power of $p$. To descend the regularity to $X$ is the open problem.

*Remark (what is open).* We repeat the status, to avoid a misreading of this chapter. For function fields of transcendence degree at least 4 over a field of characteristic $p > 0$, local uniformization of all valuations is open. Theorem 4.1.1 does not settle it, and neither do the reduction to height one [Tem23] and the $p$-alterations [Tem17]. Among the cases that are known in dimension 4 are those covered by the reductions of this volume: valuations whose residue field is not algebraic over $k$ (the remark on dimension 4 in Section 3.1) and Abhyankar valuations (Chapter 2). The programs of Volume 5, Chapter 5, and of Volume 7 aim at the remaining cases, and none of them is complete.

### Notes and references

The theorem and the remark on the tower are [Tem13, Theorem 1.3.2 and Remark 1.3.5]. The reduction to height one is [Tem23], and the $p$-alterations are [Tem17]. Proposition 4.2.1 is a standard fact on purely inseparable extensions. Example 4.2.2 uses the surface of Volume 4, Example 2.3.5. None of the results of this section is in the Lean library.
