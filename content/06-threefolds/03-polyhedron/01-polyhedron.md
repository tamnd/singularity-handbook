---
title: The polyhedron of Hironaka
nodes: [SG00000014]
sources: [Hir67, CP19, CP15, CSch21, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The polyhedron of Hironaka

Volume 7, Section 1.2, defines the projected polyhedron and the characteristic polyhedron of an equation $z^q + F(x)$, and it states the theorem of Hironaka on the existence of a minimizing coordinate without proof. In this section we give the general definition for a monic polynomial of degree $m$ in the form that Cossart and Piltant use [CP19, Section 2.1]. We define the initial form at a vertex and the solvable vertices. We prove that a translation removes a solvable vertex, and we state the theorem of Hironaka [Hir67]. We compute three examples by hand. At the end we find the solvable vertices of the purely inseparable equations $X^p + f$, and we show that over an imperfect field a vertex in $\mathbb{N}^n$ need not be solvable.

In characteristic 0 the resolution of a hypersurface of multiplicity $m$ uses a hypersurface of maximal contact. After the Tschirnhausen translation $X \mapsto X + f_{1, X}/m$, the hypersurface $X = 0$ has this property, and the next invariant comes from the orders of the coefficients $f_{i, X}$. In characteristic $p$ with $p \mid m$ this translation does not exist, and Example 2.3.5 of Narasimhan shows that no regular hypersurface can take its place in general. Hironaka keeps a coordinate $X$, but he lets it vary over all the translations $X - \varphi$. To each translation he attaches a convex set, which is built from the exponents of the coefficients $f_{i, X}$, and he takes a translation for which this set is smallest. The invariants $\delta$ and $d_j$ of Section 3.2 are minima of linear functions on this smallest set. The invariants $\epsilon$ and $\omega$ are computed from these minima and from the initial form. So they do not depend on a choice of a hypersurface.

### The setting

Let $S$ be a regular local ring of dimension $n$ with maximal ideal $\mathfrak{m}_S$, residue field $k$ and a regular system of parameters $u = (u_1, \dots, u_n)$. Let
$$h = X^m + f_{1, X} X^{m-1} + \dots + f_{m, X} \in S[X], \qquad m \ge 2.$$
A *translation* of the variable is a change $X' = X - \varphi$ with $\varphi$ in the completion $\hat S$. With $f_{0, X} = 1$, the binomial formula gives $h = X'^m + \sum_i f_{i, X'} X'^{m - i}$ with
$$f_{i, X'} = \sum_{j = 0}^{i} \binom{m - j}{i - j} f_{j, X} \varphi^{i - j}, \qquad 1 \le i \le m. \tag{3.1}$$
For each nonzero $f \in S$ there is a unique finite set $\mathcal{S}(f) \subset \mathbb{N}^n$ such that the monomials $u^a$, $a \in \mathcal{S}(f)$, are a minimal set of generators of a monomial ideal, and $f = \sum_{a \in \mathcal{S}(f)} \gamma_a u^a$ with units $\gamma_a$ [CP19, Proposition 2.1]. For $f = 0$ we put $\mathcal{S}(f) = \emptyset$.

In the proofs of this section we take $S = k[[u_1, \dots, u_n]]$ for a field $k$. Then $\mathcal{S}(f)$ is the set of the minimal elements of the support of $f$: each monomial of $f$ is a multiple of a minimal one, and if we group the monomials by a minimal divisor, each group is $u^a$ times a series with nonzero constant term. A complete regular local ring that contains a field has this form, by the structure theorem of Cohen [Mat], and the polyhedron does not change under completion [CP19, (2.8)].

### The polyhedron

**Definition 3.1.1.** The polyhedron of $h$ in the coordinates $(u; X)$ is
$$\Delta(h; u; X) = \operatorname{Conv}\Bigl( \bigcup_{i = 1}^{m} \bigcup_{a \in \mathcal{S}(f_{i, X})} \bigl( \tfrac{1}{i} a + \mathbb{R}_{\ge 0}^n \bigr) \Bigr) \subseteq \mathbb{R}_{\ge 0}^n.$$

Node: SG00000014 · Lean: `Singularity.charPolyhedron` (the definition, invariance under $z \mapsto z + \psi$, and one direction of the vertex criterion) and Volume 7, Proposition 1.2.7, for $z^q + F$ with $F$ clean

This is [CP19, Definition 2.2] with $J = \{1, \dots, n\}$. If $S = k[[u]]$, then $\Delta(h; u; X)$ is the convex hull of the sets $\frac{1}{i} N(f_{i, X})$, where $N$ is the Newton polyhedron of Volume 7, Definition 1.2.1. For $h = X^q + F$ it is $\frac{1}{q} N(F)$, the projected polyhedron of Volume 7, Section 1.2.

For a weight vector $\alpha \in \mathbb{R}_{> 0}^n$ we write $|x|_\alpha = \sum_j \alpha_j x_j$. On $k[[u]]$ let $\mu_\alpha(f) = \min \{ |a|_\alpha : a \in \operatorname{supp} f \}$ for $f \ne 0$, and $\mu_\alpha(0) = \infty$. By the theorem of Ostrowski (Volume 7, Theorem 1.2.4), $\mu_\alpha(fg) = \mu_\alpha(f) + \mu_\alpha(g)$, and clearly $\mu_\alpha(f + g) \ge \min(\mu_\alpha(f), \mu_\alpha(g))$. Put
$$\delta_\alpha(h; u; X) = \min \{ |x|_\alpha : x \in \Delta(h; u; X) \}.$$

**Lemma 3.1.2.** Let $S = k[[u]]$.

1. Each vertex of $\Delta(h; u; X)$ lies in $\frac{1}{m!} \mathbb{N}^n$.
2. $\Delta(h; u; X) = \emptyset$ if and only if $h = X^m$.
3. $\delta_\alpha(h; u; X) = \min_{1 \le i \le m} \mu_\alpha(f_{i, X})/i$ for each $\alpha \in \mathbb{R}_{> 0}^n$.
4. Let $\Delta$ and $\Delta'$ be two such polyhedra. Then $\Delta' \subseteq \Delta$ if and only if $\min_{\Delta'} |\cdot|_\alpha \ge \min_{\Delta} |\cdot|_\alpha$ for each $\alpha \in \mathbb{R}_{> 0}^n$.

Lean: none yet

*Proof.* The polyhedron is the convex hull of finitely many points $a/i$ plus the orthant, so its vertices are among the points $a/i$ with $a \in \mathbb{N}^n$ and $1 \le i \le m$. Since $i$ divides $m!$, $a/i \in \frac{1}{m!} \mathbb{N}^n$. This is part 1. The polyhedron is empty if and only if each $\mathcal{S}(f_{i, X})$ is empty, that is, each $f_{i, X} = 0$. This is part 2. A linear function with positive coefficients has the same minimum on a set and on its convex hull, and it does not decrease in the directions of the orthant. So its minimum on $\Delta(h; u; X)$ is the minimum of $|a|_\alpha / i$ over $a \in \mathcal{S}(f_{i, X})$ and $i$. Each element of the support of $f_{i, X}$ is above an element of $\mathcal{S}(f_{i, X})$, so this minimum is $\min_i \mu_\alpha(f_{i, X})/i$. This is part 3. In part 4, the implication from left to right is clear. Conversely, let $x \in \Delta' \setminus \Delta$. Then $\Delta \ne \emptyset$. The set $\Delta$ is closed and convex, so there is a linear function $\ell$ with $\ell(x) < \min_\Delta \ell$. Since $\Delta + \mathbb{R}_{\ge 0}^n = \Delta$, the coefficients of $\ell$ are nonnegative. Let $\ell_t = \ell + t \sum_j x_j$ for $t > 0$. Since $\Delta \subseteq \mathbb{R}_{\ge 0}^n$, we have $\min_\Delta \ell_t \ge \min_\Delta \ell$, and $\ell_t(x) < \min_\Delta \ell$ for small $t$. Then $\ell_t = |\cdot|_\alpha$ with $\alpha \in \mathbb{R}_{> 0}^n$, and $\min_{\Delta'} |\cdot|_\alpha \le |x|_\alpha < \min_\Delta |\cdot|_\alpha$. $\square$

Part 1 and part 2 are [CP19, Remark 2.4].

### Initial forms and solvable vertices

Let $S = k[[u]]$ and $\alpha \in \mathbb{R}_{> 0}^n$, and let $\delta = \delta_\alpha(h; u; X)$. For $g \in k[[u]]$ and a real number $c$, let $[g]_c \in k[U_1, \dots, U_n]$ be the sum of the terms of $g$ of $\alpha$-weight exactly $c$, with $u$ replaced by $U$. If $c \le \mu_\alpha(g)$ and $d \le \mu_\alpha(g')$, then $[g g']_{c + d} = [g]_c [g']_d$, because a term of weight $c + d$ of $g g'$ comes only from terms of weight $c$ of $g$ and of weight $d$ of $g'$.

**Definition 3.1.3.** The *initial form* of $h$ for $\alpha$ is
$$\operatorname{in}_\alpha h = X^m + \sum_{i = 1}^{m} [f_{i, X}]_{i \delta} X^{m - i} \in k[U_1, \dots, U_n][X].$$
It is homogeneous of degree $m \delta$ if $X$ has degree $\delta$. Let $y$ be a vertex of $\Delta(h; u; X)$, and choose $\alpha$ such that $y$ is the only point of $\Delta(h; u; X)$ where $|\cdot|_\alpha$ is minimal. Then $\operatorname{in}_y h = \operatorname{in}_\alpha h$. The vertex $y$ is *solvable* if $y \in \mathbb{N}^n$ and there is $\lambda \in k$ with
$$\operatorname{in}_y h = (X - \lambda U^y)^m.$$

Lean: none yet

This is [CP19, Definitions 2.3 and 2.6]. A weight $\alpha$ with the property of the definition exists, because the linear functions whose minimum on a polyhedron is attained only at a given vertex form a nonempty open set (see the proof of Volume 7, Theorem 1.2.4). For such $\alpha$, a term $c u^a$ of $f_{i, X}$ has weight $i \delta$ if and only if $a = i y$. So
$$\operatorname{in}_y h = X^m + \sum_{i = 1}^{m} c_i U^{i y} X^{m - i},$$
where $c_i$ is the coefficient of $u^{iy}$ in $f_{i, X}$, and $c_i = 0$ if $iy \notin \mathbb{N}^n$. This does not depend on $\alpha$. Since $y$ is a vertex, it is a point $a/i$ with $a \in \mathcal{S}(f_{i, X})$, so some $c_i \ne 0$ and $\operatorname{in}_y h \ne X^m$. Thus $\lambda \ne 0$ for a solvable vertex. The condition says $c_i = (-1)^i \binom{m}{i} \lambda^i$ for each $i$. If $p = \operatorname{char} k$ divides $\binom{m}{i}$, then $c_i = 0$.

**Lemma 3.1.4 (vertex preparation).** Let $S = k[[u]]$, let $y$ be a solvable vertex of $\Delta(h; u; X)$ with $\operatorname{in}_y h = (X - \lambda U^y)^m$, and let $Z = X - \lambda u^y$. Then $\Delta(h; u; Z) \subseteq \Delta(h; u; X)$ and $y \notin \Delta(h; u; Z)$.

Lean: none yet

*Proof.* Let $\varphi = \lambda u^y$, so $\mu_\alpha(\varphi) = |y|_\alpha$ for each $\alpha$. Let $\alpha \in \mathbb{R}_{> 0}^n$ and $\delta = \delta_\alpha(h; u; X)$. By Lemma 3.1.2(3), $\mu_\alpha(f_{j, X}) \ge j \delta$ for each $j$, and $|y|_\alpha \ge \delta$ since $y \in \Delta(h; u; X)$. By (3.1),
$$\mu_\alpha(f_{i, Z}) \ge \min_{0 \le j \le i} \bigl( \mu_\alpha(f_{j, X}) + (i - j) \mu_\alpha(\varphi) \bigr) \ge \min_j \bigl( j \delta + (i - j) \delta \bigr) = i \delta.$$
So $\delta_\alpha(h; u; Z) \ge \delta_\alpha(h; u; X)$ by Lemma 3.1.2(3), and Lemma 3.1.2(4) gives $\Delta(h; u; Z) \subseteq \Delta(h; u; X)$. Now choose $\alpha$ such that $y$ is the only point of $\Delta(h; u; X)$ where $|\cdot|_\alpha$ is minimal. Then $\delta = |y|_\alpha = \mu_\alpha(\varphi)$, and the product rule for $[\cdot]$ applied to (3.1) gives
$$[f_{i, Z}]_{i \delta} = \sum_{j = 0}^{i} \binom{m - j}{i - j} [f_{j, X}]_{j \delta} (\lambda U^y)^{i - j}.$$
The right side is the coefficient of $Z^{m - i}$ in $\operatorname{in}_y h (Z + \lambda U^y)$, by the binomial formula used for (3.1). Since $\operatorname{in}_y h(Z + \lambda U^y) = Z^m$, we get $[f_{i, Z}]_{i \delta} = 0$ for $i \ge 1$. Thus $\mu_\alpha(f_{i, Z}) > i \delta$ for each $i$, so $\delta_\alpha(h; u; Z) > |y|_\alpha$, and $y \notin \Delta(h; u; Z)$. $\square$

The lemma holds in each characteristic. Its second claim is Volume 7, Proposition 1.2.6(3), in the setting of the Lean library, and the Lean proof is described there. The lemma is the easy part of the Vertex Preparation Lemma of Hironaka [Hir67], which [CP19, Proposition 2.7] quotes. Repeated vertex preparation can need infinitely many steps (Example 3.1.8), and then one must show that the translations converge in $\hat S$.

### The theorem of Hironaka

**Theorem 3.1.5 (Hironaka).** Let $S$ be a regular local ring with a regular system of parameters $u$, and let $h \in S[X]$ be monic of degree $m$.

1. There is $\theta \in \hat S$ such that $Z = X - \theta$ satisfies $\Delta(h; u; Z) \subseteq \Delta(h; u; X - \varphi)$ for each $\varphi \in \hat S$.
2. For $\varphi \in \hat S$, the polyhedron $\Delta(h; u; X - \varphi)$ has this minimal property if and only if it has no solvable vertex.
3. If $S$ is excellent, then one can choose $\theta \in S$.

Lean: none yet

Parts 1 and 2 are [CP19, Proposition 2.7], which refers to the Vertex Preparation Lemma (3.10) and Theorem (4.8) of [Hir67]. Part 3 is the first statement of [CP19, Proposition 2.12], which [CP19] takes from [CP15, Corollary II.4]. We do not prove Theorem 3.1.5. Lemma 3.1.4 proves the implication "minimal implies no solvable vertex" of part 2 for $S = k[[u]]$: a solvable vertex can be removed. The converse, and the convergence of the translations in part 1, are the deep parts, and they are not proved here. For $S = k[[u]]$ and $h = X^q + F$ with $q = p^e$ and $F$ clean, Volume 7, Proposition 1.2.7, proves directly that $\Delta(h; u; X)$ is minimal and has no solvable vertex, with a Lean proof. This special case does not prove the converse in general.

The minimal polyhedron is the *characteristic polyhedron* $\Delta(h; u)$. It is the intersection of the polyhedra $\Delta(h; u; X - \varphi)$ over all $\varphi \in \hat S$. Volume 7, Section 1.2, takes the intersection only over the $\varphi$ with $\varphi(0) = 0$. If the image of $h$ in $k[X]$ is $X^m$, the two intersections agree: for $\varphi(0) \ne 0$ the constant term of $f_{m, X - \varphi}$ is $\varphi(0)^m \ne 0$, so $\Delta(h; u; X - \varphi)$ is the whole orthant. It depends on $u$, and it does not depend on the choice of $X$. A polyhedron $\Delta(h; u; X - \varphi)$ with no solvable vertex is called *minimal* [CP19, Definition 2.8].

**Corollary 3.1.6 (Tschirnhausen).** Let $S = k[[u]]$, assume that $m$ is a unit in $k$, and let $Z = X + f_{1, X}/m$. Then $f_{1, Z} = 0$, the polyhedron $\Delta(h; u; Z)$ has no solvable vertex, and therefore $\Delta(h; u; Z) = \Delta(h; u)$.

Lean: `Singularity.coeff_pred_taylor_tschirnhausen`, `Singularity.tschirnhausen_not_isSolvableVertex` (the first two claims)

*Proof.* By (3.1) with $\varphi = -f_{1, X}/m$, we have $f_{1, Z} = m \varphi + f_{1, X} = 0$. Let $y$ be a solvable vertex of $\Delta(h; u; Z)$, with $\operatorname{in}_y h = (Z - \lambda U^y)^m$. Then $\lambda \ne 0$, and the coefficient of $Z^{m - 1}$ in $(Z - \lambda U^y)^m$ is $-m \lambda U^y \ne 0$. But this coefficient is $[f_{1, Z}]_{\delta} = 0$. This is a contradiction. The last claim is Theorem 3.1.5(2). $\square$

This is the remark of [CP19] before Proposition 2.12 for residue characteristic 0. In characteristic $p$ with $p \mid m$ the Tschirnhausen translation does not exist, and one needs Theorem 3.1.5 in its full form. For $m = p$ in characteristic $p$ and $h = X^p + f$, Section 3.2 replaces it by the cleaning of Volume 7.

### Examples

**Example 3.1.7.** Let $k$ be a field of characteristic 2, let $S = k[[x, y]]$, and let $h = X^2 + x^2 + y^3$. Here $f_{1, X} = 0$ and $\mathcal{S}(f_{2, X}) = \{(2, 0), (0, 3)\}$, so
$$\Delta(h; x, y; X) = \operatorname{Conv}\{(1, 0), (0, 3/2)\} + \mathbb{R}_{\ge 0}^2,$$
with the two vertices $(1, 0)$ and $(0, 3/2)$. The vertex $(0, 3/2)$ is not in $\mathbb{N}^2$, so it is not solvable. For the vertex $y = (1, 0)$, the coefficient of $x^2$ in $f_{2, X}$ is $1$ and the coefficient of $x$ in $f_{1, X}$ is $0$, so $\operatorname{in}_y h = X^2 + U_1^2 = (X - U_1)^2$, since $2 = 0$ in $k$. So $(1, 0)$ is solvable with $\lambda = 1$. Lemma 3.1.4 gives $Z = X - x$. Then $h = Z^2 + 2 x Z + x^2 + x^2 + y^3 = Z^2 + y^3$, and
$$\Delta(h; x, y; Z) = (0, 3/2) + \mathbb{R}_{\ge 0}^2.$$
Its only vertex is not in $\mathbb{N}^2$, so by Theorem 3.1.5(2) this is the characteristic polyhedron. If instead $\operatorname{char} k \ne 2$, the vertex $(1, 0)$ is not solvable: $(X - \lambda U_1)^2 = X^2 + U_1^2$ needs $-2\lambda = 0$ and $\lambda^2 = 1$. Then Corollary 3.1.6 shows that $\Delta(h; x, y; X)$ is already the characteristic polyhedron.

Lean: `Singularity.charPolyhedron_example_3_1_7_eq`

**Example 3.1.8 (infinitely many steps).** Let $k$ be a field of characteristic 2, let $S = k[x, y]_{(x, y)}$, and let
$$h = X^2 + \frac{x^2}{1 + x^2} + y^3 \in S[X].$$
In $\hat S = k[[x, y]]$ we have $x^2/(1 + x^2) = \sum_{l \ge 1} x^{2l}$, since $(1 + x^2) \sum_{l \ge 1} x^{2l} = x^2$. Vertex preparation one vertex at a time does not stop. Assume that after $r \ge 0$ steps $f_{2} = \sum_{l > r} x^{2l} + y^3$ and $f_1 = 0$. The vertices are $(r + 1, 0)$ and $(0, 3/2)$, and the vertex $(r + 1, 0)$ is solvable with $\lambda = 1$, as in Example 3.1.7. The translation by $x^{r + 1}$ adds $x^{2r + 2}$ to $f_2$, by (3.1) with $m = 2$, and it gives the same form with $r + 1$ in place of $r$. The sum of the translations is $\theta = \sum_{l \ge 1} x^l = x/(1 + x)$. It lies in $S$, as Theorem 3.1.5(3) predicts for this excellent ring. In characteristic 2,
$$\theta^2 = \frac{x^2}{1 + 2x + x^2} = \frac{x^2}{1 + x^2},$$
so $Z = X - \theta$ gives $h = Z^2 + y^3$ in one step, with the polyhedron $(0, 3/2) + \mathbb{R}_{\ge 0}^2$.

Lean: `Singularity.sq_mul_one_add_sq_of_mul_one_add` (the identity in characteristic 2)

**Example 3.1.9 (mixed characteristic).** Let $S = \mathbb{Z}_{(3)}$, with $n = 1$ and $u_1 = 3$, and let $h = X^3 - 54$. This is the case $p = 3$, $a = 3$ and the unit $2$ of [CP19, Example 2.9]. Since $54 = 2 \cdot 3^3$, we have $\mathcal{S}(f_{3, X}) = \{3\}$ and $\Delta(h; 3; X) = [1, \infty)$. The residue field is $\mathbb{F}_3$, and $-54 = 3^3 \cdot (-2)$ with $-2 \equiv 1 \pmod 3$. So the initial form at the vertex $1$, in the sense of [CP19, Definition 2.6], is $X^3 + U^3 = (X + U)^3$ in $\mathbb{F}_3[U][X]$. The vertex is solvable with $\lambda = -1 = 2$. We translate by a lift of $\lambda u_1$, here $6 = 2 \cdot 3$. With $Z = X - 6$,
$$h = (Z + 6)^3 - 54 = Z^3 + 18 Z^2 + 108 Z + 162.$$
The $3$-adic orders are $v(18) = 2$, $v(108) = 3$ and $v(162) = 4$, so the points are $2/1$, $3/2$ and $4/3$, and $\Delta(h; 3; Z) = [4/3, \infty)$. Its vertex $4/3$ is not an integer, so it is not solvable, and by Theorem 3.1.5(2) this is the characteristic polyhedron. The lift $-3$ of $\lambda u_1$ gives $(Z - 3)^3 - 54 = Z^3 - 9 Z^2 + 27 Z - 81$, with the same polyhedron. This agrees with [CP19, Example 2.9], which gives $[(a + 1)/p, \infty)$ when $2^3 - 2 = 6$ is not divisible by $9$. Here $X$ has a point of multiplicity $3$ over the maximal ideal: in $\mathbb{Z}_{(3)}[Z]_{(3, Z)}$ the four terms of $h$ have orders $3$, $4$, $4$ and $4$.

Lean: `Singularity.example_3_1_9_expand` (the polynomial identity)

### Purely inseparable equations

The equations of Theorem 1.2.6 in case 1 have the form $X^p + f$ over a ring of characteristic $p$. For these equations the solvable vertices have a simple description. A translation changes only one coefficient, so vertex preparation is a deletion of monomials.

**Lemma 3.1.10.** Let $k$ be a field of characteristic $p$, let $S = k[[u]]$, and let $h = X^p + f$ with $0 \ne f \in S$.

1. $\Delta(h; u; X) = \frac{1}{p} N(f)$.
2. A vertex $y$ of $\Delta(h; u; X)$ is solvable if and only if $y \in \mathbb{N}^n$ and the coefficient $c$ of $u^{p y}$ in $f$ lies in $k^p$.
3. Let $y$ be a solvable vertex, let $\lambda \in k$ with $\lambda^p = -c$, and let $Z = X - \lambda u^y$. Then $h = Z^p + (f - c u^{p y})$.
4. Assume that $k$ is perfect. Then $\Delta(h; u; X)$ is the characteristic polyhedron $\Delta(h; u)$ if and only if no vertex of $\Delta(h; u; X)$ lies in $\mathbb{N}^n$.

Lean: `Singularity.isSolvableVertex_X_pow_add_C_iff` (part 2)

*Proof.* Part 1. Here $f_{i, X} = 0$ for $i < p$ and $f_{p, X} = f$. The set $\mathcal{S}(f)$ is the set of the minimal elements of $\operatorname{supp} f$, so the union of the sets $a + \mathbb{R}_{\ge 0}^n$ with $a \in \mathcal{S}(f)$ has the convex hull $N(f)$. Definition 3.1.1 gives $\Delta(h; u; X) = \frac1p N(f)$.

Part 2. By the formula after Definition 3.1.3, $\operatorname{in}_y h = X^p + c U^{p y}$, because $f_{i, X} = 0$ for $i < p$. Here $c \ne 0$, since $y$ is a vertex. For $\lambda \in k$ the Frobenius map gives $(X - \lambda U^y)^p = X^p + (-\lambda)^p U^{p y} = X^p - \lambda^p U^{p y}$, since $(-1)^p = -1$ in $k$. So $y$ is solvable if and only if $y \in \mathbb{N}^n$ and $-c = \lambda^p$ for some $\lambda \in k$. Since $-1 = (-1)^p$ is a $p$-th power, this holds if and only if $c \in k^p$.

Part 3. By the Frobenius map, $X^p = (Z + \lambda u^y)^p = Z^p + \lambda^p u^{p y} = Z^p - c u^{p y}$.

Part 4. If $\Delta(h; u; X)$ is minimal, then it has no solvable vertex by Lemma 3.1.4. Since $k$ is perfect, $k^p = k$, and part 2 shows that no vertex lies in $\mathbb{N}^n$. Conversely, assume that no vertex lies in $\mathbb{N}^n$. Let $f^{\mathrm{cl}}$ be the clean part of $f$ (Volume 7, Definition 1.3.1). Its support is $\operatorname{supp} f \setminus p \mathbb{N}^n$. The vertices of $N(f)$ lie in $\operatorname{supp} f$ (Volume 7, Lemma 1.2.2), and a vertex $a$ of $N(f)$ is not in $p \mathbb{N}^n$, since $a/p \notin \mathbb{N}^n$. So all the vertices of $N(f)$ lie in $\operatorname{supp} f^{\mathrm{cl}}$. The polyhedron $N(f)$ is the convex hull of its vertices plus $\mathbb{R}_{\ge 0}^n$, so $N(f) \subseteq N(f^{\mathrm{cl}})$. The other inclusion holds since $\operatorname{supp} f^{\mathrm{cl}} \subseteq \operatorname{supp} f$. Thus $\Delta(h; u; X) = \frac1p N(f^{\mathrm{cl}})$, and this is $\Delta(h; u)$ by Proposition 3.2.4(1). $\square$

Part 4 does not use Theorem 3.1.5. Over a perfect field, part 3 says that one step of vertex preparation deletes one monomial $c u^{p y}$ at a vertex $y \in \mathbb{N}^n$. The cleaning of Section 3.2 deletes all the monomials in $p \mathbb{N}^n$ at once. A deletion can make a new vertex appear, which was hidden behind the deleted one. Section 3.3 computes an example with two steps. Over an imperfect field, part 2 shows that a minimal polyhedron can have a vertex in $\mathbb{N}^n$ (Example 3.1.11).

**Example 3.1.11 (imperfect residue field).** Let $k = \mathbb{F}_p(t)$, let $S = k[[u_1, u_2]]$, and let
$$h = X^p + t u_1^p + u_2^{p + 1}.$$
Here $\mathcal{S}(f) = \{(p, 0), (0, p + 1)\}$, so $\Delta(h; u; X) = \operatorname{Conv}\{(1, 0), (0, \frac{p+1}{p})\} + \mathbb{R}_{\ge 0}^2$. The vertex $(1, 0)$ lies in $\mathbb{N}^2$, and the coefficient of $u_1^p$ is $t$. The element $t$ is not a $p$-th power in $k$, so the vertex is not solvable by Lemma 3.1.10(2). The vertex $(0, \frac{p+1}{p})$ is not in $\mathbb{N}^2$. So the polyhedron is minimal by Theorem 3.1.5(2). We can also see this directly. Let $\varphi \in S$, and let $b$ be the coefficient of $u_1$ in $\varphi$. Then $\varphi^p$ contains only monomials in $p \mathbb{N}^2$, and the coefficient of $u_1^p$ in $f + \varphi^p$ is $t + b^p \ne 0$. The monomial $u_2^{p + 1}$ is not in $p \mathbb{N}^2$, so it keeps its coefficient $1$. Thus $N(f + \varphi^p) \supseteq N(f)$, and $\Delta(h; u; X)$ is contained in $\Delta(h; u; X - \varphi)$.

Lean: `Singularity.example_3_1_11`, `Singularity.charPolyhedron_X_pow_add_C_of_forall`

In this example $\delta(x) = 1$, so the point $x$ over $\mathfrak{m}_S$ has multiplicity $p$ by Proposition 3.2.2(3), and the initial form is $\operatorname{in} h = Z^p + t U_1^p$ with $Z = X$. The polynomial $t U_1^p$ is not a $p$-th power in $k[U_1, U_2]$, but all its partial derivatives in $U_1$ and $U_2$ are $0$. The derivation $\partial/\partial t$ of $k$ detects it: $\partial (t U_1^p)/\partial t = U_1^p \ne 0$. For this reason Cossart and Piltant add the derivations of a $p$-basis of the residue field to their module of derivations, and with them a homogeneous form is a $p$-th power if and only if all these derivations kill it [CP19, Definition 2.41 and (2.43)].

### Notes and references

Hironaka introduced the characteristic polyhedron in [Hir67], where he proves its existence for a general system of equations. The hypersurface case above is the form of [CP19, Section 2.1]. Hironaka writes on page 254 of [Hir67] that "reduction of singularities is sharpening of polyhedra", and [CP19, Section 1] quotes this sentence. The proof of Lemma 3.1.4 with weights follows the idea of Hironaka's preparation of a vertex. Cossart and Piltant prove Theorem 3.1.5(3) in their paper on characteristic polyhedra without completion [CP15]. Cossart and Schober continue this work for surfaces [CSch21].
