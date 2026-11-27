---
title: Foliations in dimension 4 that a torus fixes
nodes: [SG000000A7, SG000000A8, SG000000A9, SG000000AA, SG000000AB, SG000000AC, SG000000AD, SG000000AE, SG000000AF, SG000000AG, SG000000AH, SG000000AJ, SG000000AK, SG000000AM, SG000000AN, SG000000AP, SG000000AQ, SG000000AR]
sources: [Pos24, Pos23, KKMS, Quek22]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Foliations in dimension 4 that a torus fixes

This section reports the twenty-second research result, from the track FO (tamnd/singularity#299). It treats Problems 4.9 and 4.10 of research note 04: the resolution of the singularities of $p$-closed foliations on 4-folds, first for foliations that a torus fixes. For the maximal torus the answer is complete: the foliations are classified by subspaces of $\mathbb{F}_p^4$, and weighted blowups with weights less than $p$ make them regular. For tori of rank 1, 2 and 3 there are examples that no toric method resolves, in any coordinates. For a linear action of $\mathbb{G}_m$ with positive weights prime to $p$, one weighted blowup reduces the problem to a problem on threefolds with a twist, and the section solves a part of the twisted problem. The section also corrects a claim of the research notes: one of the examples was said to be resolved, and this is not proved.

We work over an algebraically closed field $k$ of characteristic $p > 0$. For a vector $c = (c_1, \dots, c_n)$ we write $c^{[p]} = (c_1^p, \dots, c_n^p)$, and for $m \in \mathbb{Z}^n$ we write $\bar{m}$ for its image in $\mathbb{F}_p^n$.

### Why foliations enter

Route R5 of the map reduces resolution in characteristic $p$ to purely inseparable covers of degree $p$: the normalization $Z$ of a regular variety $B$ in the field $k(B)(g^{1/p})$, where $g \in k(B)$ is not a $p$-th power. Such covers are quotients by foliations. Let $B^{(1/p)}$ be the variety $B$ with the field $k(B)^{1/p}$ as its function field, so that $B^{(1/p)}$ is regular and its Frobenius twist is $B$. Then
$$k(B) \subset k(B)(g^{1/p}) \subset k(B)^{1/p},$$
and the field in the middle has index $p^{n-1}$ in $k(B)^{1/p}$, where $n = \dim B$. By the Jacobson correspondence below, $Z$ is the quotient of the regular variety $B^{(1/p)}$ by a foliation of rank $n - 1$, that is, of corank one. A resolution of the singularities of the foliation gives a model on which the quotient is regular, and so a resolution of $Z$. Volume 6, Chapter 2, treats these covers as hypersurfaces $z^p + g$.

Posva proves this program on surfaces and threefolds [Pos24]. On threefolds his normal form theorem (Theorem 1 of [Pos24]) is proved in corank one, and the introduction of [Pos24] says so. In dimension 4 the corank one foliations of route R5 have rank 3, and the rank one foliations of Problem 4.9 have corank 3, so these are different problems. A torus action gives a class of examples where one can compute.

### Foliations

**Definition 3.22.1 (1-foliation).** Let $X$ be a normal variety over $k$ with tangent sheaf $T_X$. A *1-foliation* on $X$ is a subsheaf $\mathcal{F} \subset T_X$ such that $T_X / \mathcal{F}$ is torsion free (that is, $\mathcal{F}$ is *saturated*), $[D, E] \in \mathcal{F}$ and $D^p \in \mathcal{F}$ for local sections $D, E$ of $\mathcal{F}$. Its *rank* is the generic rank of $\mathcal{F}$. It is *regular* at a point if $\mathcal{F}$ and $T_X / \mathcal{F}$ are free near the point, and $\operatorname{Sing} \mathcal{F}$ is the closed set of points where it is not regular. The *quotient* $X / \mathcal{F}$ is the space $X$ with the sheaf of functions $f$ such that $D(f) = 0$ for each local section $D$ of $\mathcal{F}$.

Node: SG000000A7 · Lean: none yet

Here $D^p$ is the $p$-fold composite of $D$ as an operator, which is again a derivation in characteristic $p$. Let $X$ be regular with function field $L$. Then the Frobenius $X \to X^{(p)}$ factors through $X / \mathcal{F}$, and $X / \mathcal{F}$ is normal and finite over $X^{(p)}$. The Jacobson correspondence [Pos23, Section 2.5] says that $\mathcal{F} \mapsto k(X / \mathcal{F})$ is a bijection from the foliations of rank $r$ to the fields $L^p \subseteq M \subseteq L$ with $[L : M] = p^r$, and $X / \mathcal{F}$ is the normalization of $X^{(p)}$ in $M$. For a rank one foliation on a regular $n$-fold, $[k(X / \mathcal{F}) : L^p] = p^{n-1}$.

On a regular affine variety $X = \operatorname{Spec} A$ with coordinates, a rank one foliation is $A \cdot D$ with $D = \sum_i f_i \partial_i$ and $\gcd(f_1, \dots, f_n) = 1$, and $\operatorname{Sing}(A \cdot D) = V(f_1, \dots, f_n)$. The module $A \cdot D$ is $p$-closed if and only if $D^p = h D$ for some $h \in A$: the coefficients of $D^p$ are in $A$, and $\gcd(f_i) = 1$.

**Definition 3.22.2 (additive and multiplicative; invariance).** Let $\mathcal{F} = A \cdot D$ be a rank one foliation with $D^p = h D$. It is *additive* if $D^p = 0$, and *multiplicative* at a point $q$ if $h(q) \ne 0$ [Pos23, Section 2.3]. Let a torus $T$ act on $X$. Then $T$ acts on derivations by $(t \cdot D)(f) = t \cdot D(t^{-1} \cdot f)$, and $\mathcal{F}$ is *$T$-invariant* if $t \cdot \mathcal{F} = \mathcal{F}$ for each $t \in T$.

Node: SG000000A7 · Lean: none yet

The model of a multiplicative singularity is $\sum_i \lambda_i t_i \partial_{t_i}$ with $\lambda_i \in \mathbb{F}_p$, whose $p$-th power is itself. The model of an additive singularity is $x^p \partial_y$ on $\mathbb{A}^2$. Posva's result for threefolds says that resolution reaches the multiplicative form in corank one. We state the parts that this section uses as a hypothesis on the map.

**Hypothesis 3.22.3 (Posva).** Let $X$ be a normal threefold over $k$ and $\mathcal{F}$ a 1-foliation on $X$.

1. If $\mathcal{F}$ has corank one, there is a projective birational morphism $f : X' \to X$ with $X'$ regular such that $f^* \mathcal{F}$ has at worst multiplicative singularities [Pos24, Theorem 5.1.1].
2. If $p > 2$ and $\mathcal{F}$ has corank two, there is a proper birational morphism $f : \mathcal{Y}' \to X$ with $\mathcal{Y}'$ a regular tame Deligne-Mumford stack such that $f^* \mathcal{F}$ is regular [Pos24, Theorem 5.2.1].
3. If $p = 2$, there is a projective birational morphism $f : X' \to X$ with $X'$ regular such that $f^* \mathcal{F}$ is regular [Pos24, Theorem 5.3.1].

Node: SG000000AG · Lean: none yet

A rank one foliation on a threefold has corank two, so part 2 is the case that we use. For corank two on a regular variety instead of a stack, Posva can lift the multiplicative generators to a resolution when the singular locus of $f^* \mathcal{F}$ is a regular curve, and he does not know the answer in general [Pos24, Remark 5.2.2]. His methods are not functorial for etale morphisms [Pos24, Remark 5.1.5]. This matters below, where the charts of a weighted blowup must be resolved compatibly.

### The maximal torus: classification

Let $A = k[x_1, \dots, x_n]$ with fraction field $K$, and let $T = \mathbb{G}_m^n$ act on $\mathbb{A}^n$ by $t \cdot x_i = t_i x_i$. For $c \in k^n$ put
$$D_c = \sum_{i=1}^n c_i x_i \partial_i .$$
Then $D_c(x^m) = (c \cdot m) x^m$ for $m \in \mathbb{N}^n$. The ring $A$ and the module $T_{\mathbb{A}^n}$ are graded by $\mathbb{Z}^n$, with $\deg x^m = m$ and $\deg \partial_i = -e_i$, and a $T$-invariant submodule is the same as a graded submodule, since $T$ is a torus.

**Lemma 3.22.4.** (1) $D_c^p = D_{c^{[p]}}$ and $[D_c, D_{c'}] = 0$. (2) The part of degree $m$ of $T_{\mathbb{A}^n}$ is $x^m \cdot \{D_c : c \in k^n\}$ if $m \in \mathbb{N}^n$; it is $k \cdot x^{m + e_j} \partial_j$ if $m = m' - e_j$ with $m' \in \mathbb{N}^n$ and $m'_j = 0$; and it is $0$ in the other cases.

Node: SG000000A8 · Lean: none yet

*Proof.* (1) Both sides are derivations, so it is enough to compare them on monomials: $D_c^p(x^m) = (c \cdot m)^p x^m$, and $(c \cdot m)^p = \sum_i c_i^p m_i^p = \sum_i c_i^p m_i = c^{[p]} \cdot m$ because $m_i \in \mathbb{Z}$. The bracket is zero because both fields act diagonally on the monomials. (2) The field $x^a \partial_j$ has degree $a - e_j$. For a fixed $m$, the indices $j$ with $m + e_j \in \mathbb{N}^n$ are all $j$ if $m \in \mathbb{N}^n$, and only $j$ if $m_j = -1$ is the only negative entry. In the first case $\sum_j a_j x^{m + e_j} \partial_j = x^m D_a$. $\square$

**Lemma 3.22.5.** Let $W \subseteq k^n$ be a subspace with $c^{[p]} \in W$ for each $c \in W$. Then $W$ is spanned by vectors of $\mathbb{F}_p^n$.

Node: SG000000A8 · Lean: none yet

*Proof.* The map $c \mapsto c^{[p]}$ is injective and additive, and $(\lambda c)^{[p]} = \lambda^p c^{[p]}$. Since $k$ is perfect, the image of a basis of $W$ is linearly independent: apply the inverse of Frobenius to the coordinates of a relation. So the vectors $c^{[p]}$ span a subspace of dimension $\dim W$ in $W$, which is $W$. Let $R$ be the basis of $W$ in reduced row echelon form. The entries $0$ and $1$ at the pivots do not change under Frobenius, so $R^{[p]}$ is a basis of $W$ in reduced row echelon form with the same pivots. The reduced row echelon basis is unique, so $R^{[p]} = R$, and the entries of $R$ are in $\mathbb{F}_p$. $\square$

**Theorem 3.22.6 (classification).** For a subspace $V \subseteq \mathbb{F}_p^n$ of dimension $r$ put
$$\mathcal{F}_V = (V \otimes_{\mathbb{F}_p} K) \cap T_{\mathbb{A}^n},$$
where $V \otimes K$ lies in $T_{\mathbb{A}^n} \otimes K = \bigoplus_i K \, x_i \partial_i$ through $c \mapsto D_c$. Then $\mathcal{F}_V$ is a $T$-invariant 1-foliation of rank $r$. Let $J = \{j : e_j \in V\}$. Then $\mathcal{F}_V$ is generated by the $\partial_j$ with $j \in J$ and the $D_c$ with $c \in V$, and it is free with the basis $\{\partial_j : j \in J\} \cup \{D_c : c \in C\}$ for each basis $C$ of $\{c \in V : c_j = 0 \text{ for } j \in J\}$. Each $T$-invariant 1-foliation on $\mathbb{A}^n$ is $\mathcal{F}_V$ for exactly one $V$.

Node: SG000000A8 · Lean: none yet

*Proof.* First, $\mathcal{F}_V$ is a graded submodule. Let $\ell^{(1)}, \dots, \ell^{(n-r)} \in \mathbb{F}_p^n$ be a basis of the orthogonal of $V$. A field $\theta = \sum_i g_i \partial_i$ is $\sum_i (g_i / x_i) x_i \partial_i$, so $\theta \in \mathcal{F}_V$ if and only if $\sum_i \ell^{(s)}_i g_i \prod_{l \ne i} x_l = 0$ for each $s$. This map sends a field of degree $m$ to a polynomial of degree $m + (1, \dots, 1)$, so its kernel is graded. The module $\mathcal{F}_V$ is saturated, since $V \otimes K$ is a $K$-subspace. The fields $D_c$, $c \in V$, commute and satisfy $D_c^p = D_c$ by Lemma 3.22.4. Since $[D_c, f D_{c'}] = D_c(f) D_{c'}$, the $K$-space $V \otimes K$ is closed under the bracket, and a $K$-subspace of derivations that is closed under the bracket and has a basis with $p$-th powers in it is closed under the $p$-th power: $(f D)^p$ is in it by Hochschild's formula (below), and $(D + E)^p - D^p - E^p$ is a sum of iterated brackets of $D$ and $E$ by Jacobson's formula for sums. So $V \otimes K$ is closed under the bracket and the $p$-th power, and so is its intersection with $T_{\mathbb{A}^n}$. So $\mathcal{F}_V$ is a $T$-invariant foliation of rank $r$.

Generators. By Lemma 3.22.4, a homogeneous element of degree $m \in \mathbb{N}^n$ is $x^m D_c$ with $c \in k^n$, and it lies in $\mathcal{F}_V$ if and only if $c \in V \otimes k$, so it is an $A$-combination of the $D_c$ with $c \in V$. A homogeneous element of degree $m' - e_j$ with $m'_j = 0$ is $a x^{m'} \partial_j = a x^{m'} x_j^{-1} D_{e_j}$ with $a \in k$, and it lies in $\mathcal{F}_V$ if and only if $a = 0$ or $e_j \in V$. So the stated set generates. For $c \in V$, write $c = c' + \sum_{j \in J} c_j e_j$ with $c'_j = 0$ for $j \in J$; then $c' \in V$, and $D_c = D_{c'} + \sum_{j \in J} c_j x_j \partial_j$. So the $r$ elements of the basis generate. They are linearly independent over $K$, so the surjection $A^r \to \mathcal{F}_V$ has a kernel of rank $0$ in a free module, which is $0$.

Classification. Let $\mathcal{F}$ be a $T$-invariant foliation, and put $V_k = \{c \in k^n : D_c \in \mathcal{F}\}$. The module $\mathcal{F}$ is graded, so it is generated by homogeneous elements. By Lemma 3.22.4 each of them is $x^m D_c$ with $m \in \mathbb{N}^n$, or $a x^{m'} \partial_j$. In the first case $D_c \in \mathcal{F}$ because $\mathcal{F}$ is saturated, so $c \in V_k$. In the second case $\partial_j \in \mathcal{F}$, so $x_j \partial_j = D_{e_j} \in \mathcal{F}$ and $e_j \in V_k$. So $\mathcal{F} \otimes K = V_k \otimes_k K$. By Lemma 3.22.4, $D_c^p = D_{c^{[p]}}$, so $V_k$ is closed under $c \mapsto c^{[p]}$, and Lemma 3.22.5 gives $V_k = V \otimes_{\mathbb{F}_p} k$ with $V = V_k \cap \mathbb{F}_p^n$. Since $\mathcal{F}$ is saturated, $\mathcal{F} = (\mathcal{F} \otimes K) \cap T_{\mathbb{A}^n} = \mathcal{F}_V$. The subspace $V$ is determined by $\mathcal{F}_V$, as $V = \{c \in \mathbb{F}_p^n : D_c \in \mathcal{F}_V\}$. $\square$

So each foliation of this class is already in the multiplicative normal form of Posva's Theorem 1, in the global coordinates: it is generated by the $\partial_j$ and by commuting fields $\sum_i \lambda_i x_i \partial_i$ with $\lambda \in \mathbb{F}_p^n$. Problem 4.9 of note 04 is trivial for this class, and the content of Problem 4.10 is regularity.

**Proposition 3.22.7.** The foliation $\mathcal{F}_V$ is regular on $\mathbb{A}^n$ if and only if $V$ is spanned by coordinate vectors, that is, $V = \operatorname{span}(e_j : j \in J)$. Then $\mathcal{F}_V = \bigoplus_{j \in J} A \, \partial_j$. If $\mathcal{F}_V$ is not regular, then $0 \in \operatorname{Sing} \mathcal{F}_V$.

Node: SG000000A8 · Lean: none yet

*Proof.* If $V = \operatorname{span}(e_j : j \in J)$, Theorem 3.22.6 gives $\mathcal{F}_V = \bigoplus_{j \in J} A \partial_j$, which is regular, with quotient $T_{\mathbb{A}^n} / \mathcal{F}_V = \bigoplus_{j \notin J} A \partial_j$. Conversely, look at the image of $\mathcal{F}_V$ in the fibre $T_{\mathbb{A}^n} \otimes k(0)$. Each $D_c$ vanishes at $0$, so the image is spanned by the $\partial_j$ with $j \in J$. If $\mathcal{F}_V$ is regular at $0$, then $\mathcal{F}_V$ is a direct summand near $0$ and the image has dimension $r$, so $|J| = r$ and $V = \operatorname{span}(e_j : j \in J)$. Finally, $\operatorname{Sing} \mathcal{F}_V$ is closed and $T$-stable, and the closure of each $T$-orbit contains $0$: take $t = (s, \dots, s)$ and let $s \to 0$. So a nonempty singular locus contains $0$. $\square$

### The maximal torus: weighted blowups resolve

We use toric modifications of $\mathbb{A}^n$. Let $\Sigma$ be a simplicial fan that subdivides the orthant $\mathbb{R}^n_{\ge 0}$, and take each cone with its primitive generators in $\mathbb{Z}^n$. Assume that the determinant of each maximal cone is prime to $p$. Let $\sigma$ be a maximal cone, and let $B$ be the matrix with the generators $b_1, \dots, b_n$ of $\sigma$ as columns. The chart of $\sigma$ is $[\mathbb{A}^n_y / G_\sigma] \to \mathbb{A}^n_x$, with $x_i = \prod_k y_k^{B_{ik}}$, where $G_\sigma$ is the finite diagonalizable group of order $|\det B|$. Since $p \nmid \det B$, the group $G_\sigma$ is etale. These charts glue to the canonical smooth toric Deligne-Mumford stack $\mathcal{X}_\Sigma$ of the fan $\Sigma$ in the lattice $\mathbb{Z}^n$, a regular tame stack with a proper birational morphism $f : \mathcal{X}_\Sigma \to \mathbb{A}^n$. The pullback $f^* \mathcal{F}$ of a foliation is, on each chart $\mathbb{A}^n_y$, the saturation of the pullback. A *toric resolution* of $\mathcal{F}$ in the coordinates $x$ is such a fan with $f^* \mathcal{F}$ regular.

**Lemma 3.22.8 (charts).** Let $\sigma$ be a maximal cone of $\Sigma$ with matrix $B$, and let $\bar{B}$ be $B$ modulo $p$. On the chart $\mathbb{A}^n_y$ of $\sigma$, the pullback of $\mathcal{F}_V$ is $\mathcal{F}_{\bar{B}^{-1} V}$. It is regular if and only if $V$ is spanned by $r$ of the vectors $\bar{b}_k$.

Node: SG000000A9 · Lean: none yet

*Proof.* From $x_i = \prod_k y_k^{B_{ik}}$ we get $y_k \partial_{y_k}(x_i) = B_{ik} x_i$, so $y_k \partial_{y_k} = \sum_i B_{ik} x_i \partial_{x_i}$ on the torus. Hence $D^x_c = D^y_{B^{-1} c}$, where $B^{-1}$ has entries in $\mathbb{Z}_{(p)}$ since $p \nmid \det B$, and its reduction is $\bar{B}^{-1}$. The pullback is a foliation on $\mathbb{A}^n_y$, invariant under the torus of the chart, whose generic fibre is $\bar{B}^{-1} V \otimes K'$, where $K' = k(y)$. By Theorem 3.22.6 it is $\mathcal{F}_{\bar{B}^{-1} V}$. By Proposition 3.22.7 it is regular if and only if $\bar{B}^{-1} V$ is spanned by $r$ coordinate vectors $e_k$, that is, if and only if $V$ is spanned by the corresponding $\bar{b}_k$. $\square$

For a maximal cone $\sigma$ put $s(\sigma) = \#\{k : \bar{b}_k \in V\}$. These $\bar{b}_k$ are linearly independent, since $\bar{B}$ is invertible, so $s(\sigma) \le r$. Call $\sigma$ *good* if $s(\sigma) = r$. By Lemma 3.22.8 the pullback is regular on the chart of $\sigma$ if and only if $\sigma$ is good. The algorithm makes all cones good.

**Algorithm.** Start with $\Sigma = \{\mathbb{R}^n_{\ge 0}\}$. While some maximal cone $\sigma$ is not good:

1. Let $J = \{k : \bar{b}_k \in V\}$. Then $e_k \in \bar{B}^{-1} V$ for $k \in J$, and $\dim \bar{B}^{-1} V = r > |J|$, so there is $c \in \bar{B}^{-1} V$, $c \ne 0$, with $c_k = 0$ for $k \in J$.
2. Lift $c$ to $w \in \{0, \dots, p - 1\}^n$. Put $v = \sum_k w_k b_k$, let $g$ be the gcd of the entries of $v$, and put $v' = v / g$.
3. Let $\varphi$ be the face of $\sigma$ spanned by the $b_k$ with $w_k \ne 0$. Replace $\Sigma$ by its stellar subdivision at $v'$. This replaces each cone $\tau \supseteq \varphi$ by the cones obtained from $\tau$ by replacing one generator $b_k$ of $\varphi$ by $v'$.

The vector $c$ of step 1 has at least two nonzero entries. If $c = \lambda e_k$, then $e_k \in \bar{B}^{-1} V$, so $\bar{b}_k \in V$ and $k \in J$, which contradicts $c_k \ne 0$. So $\dim \varphi \ge 2$, and the subdivision is a genuine blowup.

**Lemma 3.22.9.** In step 2, $p \nmid g$ and $\bar{v}' \in V$. Let $\tau'$ be a new cone, obtained from $\tau \supseteq \varphi$ by replacing $b_k$ by $v'$. Then $\det \tau' = (w_k / g) \det \tau$, so $\det \tau'$ is prime to $p$, and $s(\tau') = s(\tau) + 1$.

Node: SG000000A9 · Lean: none yet

*Proof.* We have $\bar{v} = \bar{B} c \ne 0$, since $c \ne 0$ and $\bar{B}$ is invertible. So $p \nmid g$, and $\bar{v}' = g^{-1} \bar{B} c \in V$, since $c \in \bar{B}^{-1} V$. The vector $v'$ is $\sum_k (w_k / g) b_k$, a combination of the generators of $\varphi$ with the same coefficients in each cone $\tau \supseteq \varphi$. So replacing $b_k$ by $v'$ multiplies the determinant by $w_k / g$, and $1 \le w_k \le p - 1$ with $p \nmid g$. The generators $b_k$ of $\varphi$ are not in $V$ modulo $p$: for $\tau = \sigma$ this is the choice $c_k = 0$ for $k \in J$, and the other cones that contain $\varphi$ have the same vectors $b_k$. So $\tau'$ loses a vector that is not in $V$ modulo $p$ and gains $v'$, which is. $\square$

**Theorem 3.22.10.** For each subspace $V \subseteq \mathbb{F}_p^n$ the algorithm stops. It gives a simplicial fan $\Sigma$ whose maximal cones have determinants prime to $p$, such that $f : \mathcal{X}_\Sigma \to \mathbb{A}^n$ is proper and birational, $\mathcal{X}_\Sigma$ is a regular tame Deligne-Mumford stack, and $f^* \mathcal{F}_V$ is regular. Up to a root stack of order prime to $p$ along the new divisor, each step is a weighted blowup in the coordinates of a chart, with weights in $\{1, \dots, p - 1\}$. If $V = \mathbb{F}_p c$ has rank one and $c$ is not a multiple of a coordinate vector, one weighted blowup suffices: its center is $\{x_k = 0 : c_k \ne 0\}$, and its weights are in $\{1, \dots, p - 1\}$ and reduce modulo $p$ to a generator of $V$. If $p = 2$, then $\Sigma$ is a smooth fan, and $\mathcal{X}_\Sigma$ is a regular toric variety.

Node: SG000000A9 · Lean: none yet

*Proof.* Fix an integer $N > n$ and put $\Phi(\Sigma) = \sum_\sigma N^{r - s(\sigma)}$, the sum over the maximal cones. A step replaces each cone $\tau \supseteq \varphi$ by at most $n$ cones with exponent $r - s(\tau) - 1$ (Lemma 3.22.9), and does not change the other cones. Since $n N^{e - 1} < N^e$, the positive integer $\Phi$ goes down at each step, so the algorithm stops, and then each cone is good. By Lemma 3.22.8 the pullback is regular on each chart, and by Lemma 3.22.9 all determinants are prime to $p$, so all charts are tame.

The ray of $v'$ is the ray of $v = \sum_k w_k b_k$. So the stellar subdivision of the face $\varphi$ of $\sigma$ at $v'$ is, in the coordinates $y$ of the chart of $\sigma$, the weighted blowup of $\{y_k = 0 : w_k \ne 0\}$ with the weights $w_k \in \{1, \dots, p - 1\}$. The chart $D_+(y_k)$ of this weighted blowup is $[\mathbb{A}^n / \mu_{w_k}]$, while the canonical stack puts the group of the new cone there. The two differ by a root stack of order $g$, prime to $p$, along the new divisor. Such a root is etale outside the divisor, so it changes neither tameness nor the regularity of the saturated pullback, which is computed by Lemma 3.22.8 in both cases.

If $r = 1$ and $c$ is not a multiple of a coordinate vector, then for the orthant $J$ is empty, and the first step gives new cones that all contain $v'$, with $\bar{v}' \in V$, so $s = 1 = r$ on each of them. Here $v = w$, the center is $\{x_k = 0 : c_k \ne 0\}$, and $v' = w / g$ reduces to $g^{-1} c$, a generator of $V$. If $p = 2$, then $w \in \{0, 1\}^n$, and Lemma 3.22.9 gives $\det \tau' = \det \tau / g$. By induction all determinants are $\pm 1$: if $\det \tau = \pm 1$, then $\pm 1 / g$ is a nonzero integer, so $g = 1$ and $\det \tau' = \pm 1$. A smooth fan gives a regular toric variety. $\square$

The weights must be reduced modulo $p$. For $p = 2$, the field $D_{(0, 0, 1, 2)}$ is $D_{(0, 0, 1, 0)}$, which is regular. The weighted blowup with the weights $(1, 2)$ on $(x_3, x_4)$ has a chart $[\mathbb{A}^4 / \mu_2]$, which is wild in characteristic $2$. This matches Posva's choice of a lift in $\{1, \dots, p - 1\}$ in his treatment of $x \partial_x + \lambda y \partial_y$ [Pos24, Claim 4.0.4]. The script of the research notes resolves all subspaces of $\mathbb{F}_p^4$ for $p = 2, 3, 5$ with this algorithm, with at most 6 blowups; this is numerical evidence only.

**Corollary 3.22.11 (the quotient).** Let $T$ act diagonally in the coordinates $x$. Then
$$\mathbb{A}^n / \mathcal{F}_V = \operatorname{Spec} k[x^m : m \in \mathbb{N}^n, \ \bar{m} \in V^\perp],$$
where $V^\perp \subseteq \mathbb{F}_p^n$ is the orthogonal of $V$ for the dot product. This is the affine toric variety of the orthant in the lattice $\{m \in \mathbb{Z}^n : \bar{m} \in V^\perp\}$ of index $p^r$, which is simplicial, so it has a toric resolution.

Node: SG000000AA · Lean: none yet

*Proof.* The foliation $\mathcal{F}_V$ is graded, so its ring of constants in $A$ is spanned by monomials. For a monomial, $D_c(x^m) = (c \cdot \bar{m}) x^m$ and $\partial_j(x^m) = m_j x^{m - e_j}$. So $x^m$ is a constant if and only if $c \cdot \bar{m} = 0$ for each $c \in V$. The conditions from the $\partial_j$ with $e_j \in V$ are among these. The toric resolution is Theorem 2.4.1 [KKMS]. $\square$

With Theorem 3.22.10 this answers Problem 4.10 of note 04 for the diagonal maximal torus in both of its readings: resolve the foliation, and resolve the quotient. For an arbitrary embedding of $\mathbb{G}_m^n$ in $\operatorname{Aut} \mathbb{A}^n$ one needs a linearization theorem in characteristic $p$, and the research notes did not check its hypotheses. For smaller tori, actions on affine space need not be linear in positive characteristic, so the hypothesis "diagonal" is part of the statements below too.

### The limits of toric methods

Let $U_1 \subseteq \mathbb{A}^n$ be the set of points with at most one coordinate equal to $0$. Its complement is the union of the planes $\{x_a = x_b = 0\}$ of codimension 2.

**Lemma 3.22.12.** Let $\mathcal{F} = A \cdot D$ be a rank one foliation on $\mathbb{A}^n$, and let $\Sigma$ be a toric modification in the coordinates $x$, as above, such that $f^* \mathcal{F}$ is regular. Then $\operatorname{Sing} \mathcal{F} \cap U_1 = \emptyset$.

Node: SG000000AB · Lean: none yet

*Proof.* The ray $\mathbb{R}_{\ge 0} e_i$ is a face of the support $\mathbb{R}^n_{\ge 0}$ of $\Sigma$, so it is a cone of $\Sigma$. Its toric open set maps onto the open set $\{x_j \ne 0 \text{ for } j \ne i\}$ of $\mathbb{A}^n$, and etale locally the map is $x_i = s^m$ with $p \nmid m$ (with $m = 1$ for the canonical stack). Let $q$ be a singular point with $x_j(q) \ne 0$ for $j \ne i$, and write $D = \sum_l f_l \partial_l$ with all $f_l(q) = 0$. The map is etale outside $s = 0$ and $D$ is saturated, so the only possible common factor of the pulled back coefficients is a power of $s$. We have $\partial_{x_i} = (m s^{m-1})^{-1} \partial_s$. If $f_i \in (x_i)$, the saturated pullback is $(f_i / m s^{m-1}) \partial_s + \sum_{l \ne i} f_l \partial_l$: the $f_l$ with $l \ne i$ are not all divisible by $x_i$, so not all by $s$, and the field is saturated. It vanishes over $q$. If $f_i \notin (x_i)$, the saturated pullback is $m^{-1} f_i \partial_s + s^{m-1} \sum_{l \ne i} f_l \partial_l$, and it vanishes over $q$ because $f_i(q) = 0$. In both cases $f^* \mathcal{F}$ is singular over $q$. $\square$

**Corollary 3.22.13.** If the reduced set $\operatorname{Sing} \mathcal{F}$ has an irreducible component of dimension $2$ in $\mathbb{A}^4$ that is not of the form $\{y_a = y_b = 0\}$ for the coordinate system $y$, then $\mathcal{F}$ has no toric resolution in the coordinates $y$.

Node: SG000000AB · Lean: none yet

*Proof.* By Lemma 3.22.12 the component lies in the complement of $U_1(y)$, a finite union of irreducible surfaces $\{y_a = y_b = 0\}$. An irreducible surface in this union is one of them. $\square$

We give examples for tori of each rank less than 4. The first one is additive and invariant under the scalar $\mathbb{G}_m$.

**Example 3.22.14 (rank one).** Let
$$D = (x^p - z^{p-1} w) \, \partial_x + (y^p - z w^{p-1}) \, \partial_y \quad \text{on } \mathbb{A}^4_{x, y, z, w} .$$
Then $\mathcal{F} = A \cdot D$ is a rank one foliation with $D^p = 0$, invariant under $\mathbb{G}_m$ with the weights $(1, 1, 1, 1)$. Its singular locus is the cone over the rational curve $\Gamma = \{(s : s^{p-1} : 1 : s^p)\} \subset \mathbb{P}^3$ of degree $p$. In no coordinate system on $\mathbb{A}^4$ does $\mathcal{F}$ have a toric resolution.

Node: SG000000AC · Lean: none yet

*Proof.* Put $f = x^p - z^{p-1} w$ and $g = y^p - z w^{p-1}$. The polynomial $f$ is linear in $w$ with the coefficient $z^{p-1}$, which is prime to $x^p$, so $f$ is irreducible, and $f$ does not divide $g$, since $g$ does not involve $x$. So $\gcd(f, g) = 1$, and $\mathcal{F}$ is saturated. We have $D(z) = D(w) = 0$, $D(x^p) = p x^{p-1} f = 0$ and $D(y^p) = 0$, so $D(f) = D(g) = 0$, $D^2(x) = D^2(y) = 0$, and $D^p = 0$. Each coefficient is homogeneous of degree $p$ and $\partial_x$, $\partial_y$ have degree $-1$, so $D$ is homogeneous of degree $p - 1$, and it is invariant under the scalars. For the singular locus, solve $f = g = 0$. If $z = 0$, then $x = y = 0$, which gives the line $(0, 0, 0, w)$, the point $s = \infty$ of $\Gamma$. If $z = 1$, then $w = x^p$ and $y^p = x^{p(p-1)}$, so $y = x^{p-1}$, which gives the other points of $\Gamma$ with $s = x$. The curve $\Gamma$ is irreducible of degree $p \ge 2$, so it is not a line, and the cone over it is singular at the vertex. A surface $\{y_a = y_b = 0\}$ is smooth, so Corollary 3.22.13 applies in each coordinate system. $\square$

For $p = 2$, $\Gamma$ is the conic $x^2 = z w$ in the plane $x = y$. The example is a family over $\mathbb{A}^2_{z, w}$ of additive foliations of the plane $\mathbb{A}^2_{x, y}$. The obstruction is not the end of the story. Blow up the origin. In the chart $x = z X$, $y = z Y$, $w = z W$ we get $D = z^{p-1} \delta$ with
$$\delta = (X^p - W) \, \partial_X + (Y^p - W^{p-1}) \, \partial_Y ,$$
which involves neither $z$ nor $\partial_z$. This is the product of $\mathbb{A}^1_z$ with a rank one foliation on $\mathbb{A}^3$ whose singular locus is the smooth curve $W = X^p$, $Y = X^{p-1}$. The chart $w$ is similar. The research notes stopped here and said that the example is resolved. This is not proved: the charts $x$ and $y$ contain more singular points.

**Proposition 3.22.15.** In the chart $x = u$, $y = u Y$, $z = u Z$, $w = u W$ of the blowup of the origin, $D = u^{p-1} D'$ with
$$D' = \alpha \, u \partial_u + \delta, \quad \alpha = 1 - Z^{p-1} W, \quad \delta = (Y^p - Z W^{p-1} - Y \alpha) \, \partial_Y - Z \alpha \, \partial_Z - W \alpha \, \partial_W ,$$
and $D'^p = \alpha^{p-1} D'$. The pullback of $\mathcal{F}$ to the blowup is singular along the strict transform $S$ of the cone and at the $p + 1$ points of $\mathbb{P}^1(\mathbb{F}_p) \subset \{z = w = 0\}$ of the exceptional $\mathbb{P}^3$. In the chart $x$ these points are $q_c = (u, Y, Z, W) = (0, c, 0, 0)$ with $c \in \mathbb{F}_p$, and the last one is $(0 : 1 : 0 : 0)$ in the chart $y$. At each of them $\alpha = 1$, the foliation is multiplicative, and the linear part of the generator is $\operatorname{diag}(1, -1, -1, -1)$.

Node: SG000000AC · Lean: none yet

*Proof.* We have $D(u) = f = u^p \alpha$, $D(Y) = (D(y) - Y D(u)) / u = u^{p-1} (Y^p - Z W^{p-1} - Y \alpha)$, $D(Z) = -Z D(u) / u = -u^{p-1} Z \alpha$, and in the same way $D(W) = -u^{p-1} W \alpha$. This gives $D = u^{p-1} D'$. The field $D'$ is saturated: a prime factor of all the coefficients divides $Z \alpha$ and $W \alpha$, so it divides $\alpha$, and then it divides $Y^p - Z W^{p-1}$. But $\alpha$ does not involve $Y$ and $Y^p - Z W^{p-1}$ is monic in $Y$, so no prime divides both.

For the $p$-th power we use Hochschild's formula $(h E)^p = h^p E^p + (h E)^{p-1}(h) \, E$ for a derivation $E$ and a function $h$ [Pos23, Section 2.3]. With $h = u^{p-1}$ and $E = D'$ it gives $0 = D^p = u^{p(p-1)} D'^p + D^{p-1}(x^{p-1}) D'$. Since $D(x) = f$ and $D(f) = 0$, induction gives $D^k(x^{p-1}) = (p - 1)(p - 2) \cdots (p - k) \, x^{p-1-k} f^k$, so $D^{p-1}(x^{p-1}) = (p - 1)! \, f^{p-1} = -f^{p-1}$ by Wilson's theorem. Hence $D'^p = (f / u^p)^{p-1} D' = \alpha^{p-1} D'$.

The singular locus of $D'$ is the set where $\alpha u$ and the coefficients of $\delta$ vanish. Where $\alpha = 0$, we get $Z^{p-1} W = 1$ and $Y^p = Z W^{p-1}$, and $u$ is free: this is the strict transform $S$ of the cone, which also lies in the charts $z$ and $w$. Where $\alpha \ne 0$, we get $u = 0$, $Z = W = 0$, so $\alpha = 1$ and $Y^p = Y$: these are the points $q_c$. The chart $y$ is the same computation with $x$ and $y$ exchanged, and its only new point is $(0 : 1 : 0 : 0)$. At $q_c$ the linear parts of the coefficients are $u$, $-(Y - c)$, $-Z$ and $-W$: the term $Y^p$ has no linear part at $c$, and $Z W^{p-1}$ and $Y Z^{p-1} W$ have order at least $2$. Since $\alpha^{p-1}(q_c) = 1$, the foliation is multiplicative at $q_c$. $\square$

At a singular multiplicative point there are formal coordinates $t_1, \dots, t_4$ in which a generator is diagonal, with the eigenvalues of its linear part [Pos23, Section 4.1]. Here this gives $t_1 \partial_{t_1} - t_2 \partial_{t_2} - t_3 \partial_{t_3} - t_4 \partial_{t_4}$, the rank one field $D_{(1, -1, -1, -1)}$ of Theorem 3.22.10. In formal coordinates one weighted blowup with the weights $(1, p - 1, p - 1, p - 1)$ makes it regular. To use this, one needs the following statement, which is open.

**Conjecture 3.22.16 (one weighted blowup at a multiplicative point).** Let $q$ be a closed point of a regular 4-fold $Y$, and let $\mathcal{F}$ be a rank one foliation that is singular and multiplicative at $q$, with formal normal form $\sum_i \lambda_i t_i \partial_{t_i}$. Let $y_1, \dots, y_4$ be polynomial coordinates at $q$ with $y_i \equiv t_i$ modulo $\mathfrak{m}_q^p$. Then the weighted blowup of $q$ in the coordinates $y$, with the weights the lifts in $\{1, \dots, p - 1\}$ of $\lambda$ (after a common factor in $\mathbb{F}_p^\times$), makes $\mathcal{F}$ regular over $q$.

Node: SG000000AD · Lean: none yet

The expected proof is short: the weighted filtration depends only on the coordinates modulo terms of high weight, and blowups commute with the flat base change to the completion. The missing step is that the regularity of the saturated pullback can be checked after completion at the points over $q$. Under Conjecture 3.22.16, one weighted blowup at each of the $p + 1$ points removes them from the singular locus. Along $S$ the foliation is, chart by chart, the product of a line with the threefold field $\delta$ of the chart $z$ or $w$, and Hypothesis 3.22.3 resolves each chart. The gluing of these resolutions is Conjecture 3.22.21 below. So it is not proved that Example 3.22.14 can be resolved, and it is not proved that it is a counterexample to Problem 4.10.

The second example is invariant under a torus of rank 3.

**Example 3.22.17 (rank three).** Let $p \ge 3$, and let $T = \{(s, s, t, u)\} \cong \mathbb{G}_m^3$ act on $\mathbb{A}^4$ by $(x_1, x_2, x_3, x_4) \mapsto (s x_1, s x_2, t x_3, u x_4)$. Let $D = a \partial_1 + b \partial_3 + c \partial_4$ with
$$a = x_1 (x_1 + x_2)(x_1 - x_2), \quad b = x_3 (2 x_1 + x_2)(x_1 - x_2), \quad c = x_4 x_1 (x_1 + x_2) .$$
Then $\mathcal{F} = A \cdot D$ is a $T$-invariant $p$-closed rank one foliation, the annihilator of the functions $x_2$, $x_3 x_2^2 / (x_1 (x_1 + x_2))$ and $x_4 x_2 / (x_1 - x_2)$. Its singular locus is the union of the planes $P_0 = \{x_1 = x_2 = 0\}$, $P_1 = \{x_1 = x_3 = 0\}$, $P_2 = \{x_1 + x_2 = x_3 = 0\}$ and $P_3 = \{x_1 - x_2 = x_4 = 0\}$. In no coordinate system on $\mathbb{A}^4$ does $\mathcal{F}$ have a toric resolution.

Node: SG000000AE · Lean: none yet

*Proof.* Each term of $D$ has the weight $s^2$, so $D$ is semi-invariant and $\mathcal{F}$ is $T$-invariant. The field $D$ kills $x_2$, and
$$\frac{D(x_3 / (x_1 (x_1 + x_2)))}{x_3 / (x_1 (x_1 + x_2))} = \frac{b}{x_3} - a \Bigl(\frac{1}{x_1} + \frac{1}{x_1 + x_2}\Bigr) = (x_1 - x_2) \bigl((2 x_1 + x_2) - (x_1 + x_2) - x_1\bigr) = 0,$$
$$\frac{D(x_4 / (x_1 - x_2))}{x_4 / (x_1 - x_2)} = \frac{c}{x_4} - \frac{a}{x_1 - x_2} = x_1 (x_1 + x_2) - x_1 (x_1 + x_2) = 0 .$$
The three functions have linearly independent differentials, so they are $p$-independent, and the derivations of $K$ that kill them form a $K$-line closed under the bracket and the $p$-th power. Its intersection with $T_{\mathbb{A}^4}$ is a rank one foliation that contains $D$. The coefficients of $D$ have no common factor: the factors of $a$ are $x_1$, $x_1 + x_2$ and $x_1 - x_2$; $b$ is $-x_3 x_2^2 \ne 0$ on $x_1 = 0$ and $2 x_3 x_2^2 \ne 0$ on $x_1 = -x_2$ (here $p \ne 2$ is used), and $c$ is $2 x_4 x_1^2 \ne 0$ on $x_1 = x_2$. So the foliation is $A \cdot D$.

For the singular locus, $a = 0$ gives three cases. If $x_1 = 0$, then $c = 0$ and $b = -x_3 x_2^2$, so $x_2 = 0$ or $x_3 = 0$, which gives $P_0$ and $P_1$. If $x_1 = -x_2 \ne 0$, then $c = 0$ and $b = 2 x_3 x_2^2$, so $x_3 = 0$, which gives $P_2$. If $x_1 = x_2 \ne 0$, then $b = 0$ and $c = 2 x_4 x_1^2$, so $x_4 = 0$, which gives $P_3$.

Assume that $\mathcal{F}$ has a toric resolution in coordinates $y$. By Corollary 3.22.13, $P_k = \{y_{a_k} = y_{b_k} = 0\}$ for $k = 1, 2, 3$. Two such planes meet in a point if their pairs of indices are disjoint, and in a line if the pairs have one common index. Here $P_1 \cap P_3 = \{0\}$ and $P_2 \cap P_3 = \{0\}$ (this uses $p \ne 2$), so $\{a_1, b_1\}$ and $\{a_2, b_2\}$ are both the complement of $\{a_3, b_3\}$ in $\{1, 2, 3, 4\}$. Then $P_1 = P_2$, but $P_1 \cap P_2 = \{x_1 = x_2 = x_3 = 0\}$ is a line. This is a contradiction. $\square$

A foliation invariant under $T$ is invariant under each subtorus of $T$, for instance the scalars $\{(s, s, s, s)\}$ of rank 1 and $\{(s, s, t, t)\}$ of rank 2. So for each rank $1$, $2$ and $3$ there is a torus of that rank and an invariant $p$-closed foliation on $\mathbb{A}^4$ with no toric resolution in any coordinates. For the rank $4$ torus, Theorem 3.22.10 gives a toric resolution. These examples are a no-go for toric methods, not for Problem 4.10.

### The case of $\mathbb{G}_m$

In this part $\mathbb{G}_m$ acts linearly on $\mathbb{A}^4$ with weights $w_1, \dots, w_4 \ge 1$, all prime to $p$. Weights of mixed sign or zero, weights divisible by $p$ and actions that are not linear are not covered. Let $\mathcal{F}$ be a $\mathbb{G}_m$-invariant rank one foliation. As in Proposition 3.22.7, if $\operatorname{Sing} \mathcal{F}$ is not empty, it contains $0$. Blow up the origin with the weights $w$. The chart $D_+(x_i)$ is $[\operatorname{Spec} k[u, v] / \mu_{w_i}]$ with $x_i = u^{w_i}$ and $x_j = u^{w_j} v_j$ for $j \ne i$ [Pos24, Example 2.4.3], and $\mathbb{G}_m$ acts on it by $u \mapsto t u$ and trivially on $v = (v_j)_{j \ne i}$. We work on the chart $\mathbb{A}^4 = \operatorname{Spec} k[u, v]$ above it.

**Proposition 3.22.18.** On the chart, the pullback of $\mathcal{F}$ is generated either by $\partial_u$, or by
$$D' = \alpha(v) \, u \partial_u + \delta, \quad \delta = \sum_{j} b_j(v) \partial_{v_j}, \quad \gcd(\alpha, b_1, b_2, b_3) = 1 .$$
In the second case $D'^p = \delta^p + \psi(\alpha) \, u \partial_u$ with $\psi(\alpha) = \alpha^p + \delta^{p-1}(\alpha)$, so $p$-closure is equivalent to
$$\delta^p = H \delta, \qquad \alpha^p + \delta^{p-1}(\alpha) = H \alpha$$
for one $H \in k[v]$, and $\operatorname{Sing} = (\{u = 0\} \times Z(\delta)) \cup (\mathbb{A}^1_u \times (Z(\delta) \cap V(\alpha)))$, where $Z(\delta) = V(b_1, b_2, b_3)$.

Node: SG000000AF · Lean: none yet

*Proof.* The pullback is a $\mathbb{G}_m$-invariant rank one foliation $k[u, v] \cdot D$. For $t \in \mathbb{G}_m$, $t \cdot D$ generates $t \cdot \mathcal{F} = \mathcal{F}$, so $t \cdot D = a_t D$ with $a_t \in k[u, v]^\times = k^\times$, and $t \mapsto a_t$ is a character. So $D$ is semi-invariant, of some weight $e$. Since $u$ has weight $1$, $\partial_u$ weight $-1$, and $v_j$ and $\partial_{v_j}$ weight $0$, we get $D = a(v) u^{e+1} \partial_u + u^e \sum_j b_j(v) \partial_{v_j}$. If all $b_j$ are $0$, the saturation is $\partial_u$. Otherwise $e \ge 0$, and saturation gives $e = 0$ and $\gcd(\alpha u, b_1, b_2, b_3) = 1$ with $\alpha = a$, which is $\gcd(\alpha, b_1, b_2, b_3) = 1$.

On $u^m k[v]$ the field $D'$ acts as the operator $\delta + m \alpha$, where $m \alpha$ is a multiplication. Jacobson's formula $(\delta + a)^p = \delta^p + a^p + \delta^{p-1}(a)$ for a derivation $\delta$ and a multiplication $a$ gives $(\delta + m \alpha)^p = \delta^p + m^p \alpha^p + m \, \delta^{p-1}(\alpha) = \delta^p + m \psi(\alpha)$, because $m^p = m$ in $\mathbb{F}_p$. The derivation $\delta^p + \psi(\alpha) u \partial_u$ acts in the same way on $u^m k[v]$, so it is $D'^p$. If $D'^p = H D'$, then $H$ is a polynomial, since the coefficients of $D'$ have no common factor, and $H$ has weight $0$, so $H \in k[v]$. Comparing the parts in $\partial_v$ and in $u \partial_u$ gives the two equations. The singular locus is $V(\alpha u, b_1, b_2, b_3)$. $\square$

The field $\delta$ is a rank one foliation on $\mathbb{A}^3_v$ if it is saturated, but $\alpha$ twists it. In the untwisted case $\alpha = 0$, Posva's theorems apply on each chart.

**Corollary 3.22.19.** In the setting of Proposition 3.22.18, assume $\alpha = 0$ on the chart. Then the pullback is the product of $\mathbb{A}^1_u$ with the rank one foliation $k[v] \cdot \delta$ on $\mathbb{A}^3_v$. Under Hypothesis 3.22.3, for $p > 2$ there is a proper birational morphism from a regular tame Deligne-Mumford stack to $\mathbb{A}^3_v$, and for $p = 2$ a projective birational morphism from a regular variety, on which the pullback of $\delta$ is regular. Its product with $\mathbb{A}^1_u$ makes the pullback of $\mathcal{F}$ regular on the chart.

Node: SG000000AH · Lean: none yet

*Proof.* If $\alpha = 0$, then $D' = \delta$ does not involve $u$ or $\partial_u$, and $\gcd(b_j) = 1$, so $k[v] \cdot \delta$ is saturated. It is $p$-closed since $\delta^p = H \delta$. Apply part 2 or part 3 of Hypothesis 3.22.3 to it, and take the product with $\mathbb{A}^1_u$; regularity is preserved by the product with a line. $\square$

The statement is for one chart. A resolution of the weighted blowup must be $\mu_{w_i}$-equivariant on each chart and must agree on the overlaps, and this cannot be had by citation, since Posva's methods are not functorial for etale morphisms [Pos24, Remark 5.1.5]. Two statements are open.

**Conjecture 3.22.20 (the twisted pair problem).** Let $Y$ be a regular threefold, let $\delta = \sum_j b_j \partial_{v_j}$ generate a rank one $p$-closed foliation with $\delta^p = H \delta$, and let $\alpha \in \mathcal{O}_Y$ with $\alpha^p + \delta^{p-1}(\alpha) = H \alpha$ and $\gcd(\alpha, b_1, b_2, b_3) = 1$. Then there are proper birational modifications of $Y$, together with weighted blowups of $Y \times \mathbb{A}^1_u$ along centers over $\{u = 0\}$, from a regular tame Deligne-Mumford stack (a regular variety if $p = 2$), that make the pullback of $\alpha u \partial_u + \delta$ regular.

Node: SG000000AJ · Lean: none yet

**Conjecture 3.22.21 (equivariant gluing).** Let $\mathcal{F}$ be as in Proposition 3.22.18, and assume $\alpha = 0$ on each chart of the weighted blowup of the origin where the pullback is not generated by $\partial_u$. Then there is a proper birational morphism from a regular tame Deligne-Mumford stack (a regular variety if $p = 2$) to the weighted blowup on which the pullback of $\mathcal{F}$ is regular.

Node: SG000000AK · Lean: none yet

Conjecture 3.22.21 says that the chart resolutions of Corollary 3.22.19 can be chosen $\mu_{w_i}$-equivariant and compatible on the overlaps. Example 3.22.14 is the first test case: there $D$ has the two first integrals $z$ and $w$, and the singular locus of the chart field $\delta$ is a smooth curve.

### The twisted problem when $H = 0$

In this part $R = k[v_1, \dots, v_d]$ with fraction field $K$, $\delta = \sum_j b_j \partial_{v_j}$ is a saturated derivation of $R$ with $\delta^p = H \delta$, $\alpha \in R$, and $D' = \alpha u \partial_u + \delta$ on $R[u]$. Put $\psi(\alpha) = \alpha^p + \delta^{p-1}(\alpha)$ and $\nabla = \delta + \alpha$, an operator on $K$. Jacobson's formula reads $\nabla^p = \delta^p + \psi(\alpha)$ as operators. The first remark is that $\alpha$ is not an invariant of the foliation.

**Lemma 3.22.22 (gauge).** Let $g$ be a unit of a localization of $R$. The change of coordinates $u' = u g$ turns $D'$ into $(\alpha + \delta(g) / g) \, u' \partial_{u'} + \delta$. The function $H$ and the set $\operatorname{Sing} D'$ do not change, and if $H = 0$, then $\psi(\alpha + \delta(g) / g) = \psi(\alpha)$.

Node: SG000000AM · Lean: none yet

*Proof.* $D'(u g) = \alpha u g + u \delta(g) = (\alpha + \delta(g)/g) u'$, and $D'$ acts on $v$ as before. The function $H$ depends only on $\delta$, and the singular locus is a property of the foliation. As operators, $\delta + \alpha + \delta(g)/g = g^{-1} \circ (\delta + \alpha) \circ g$, so the $p$-th powers are conjugate, and $\psi$ is the $p$-th power of $\nabla$ minus $\delta^p = 0$. A conjugate of a multiplication by $g$ is the same multiplication. $\square$

So $\alpha$ is a connection form, defined up to logarithmic derivatives of units. This explains why the chart $z$ of Example 3.22.14 has $\alpha = 0$ while the chart $x$ has $\alpha = 1 - Z^{p-1} W$: the trivializations differ. When $H = 0$ the condition on $\alpha$ is $\psi(\alpha) = 0$, and it has a complete answer.

**Theorem 3.22.23.** Assume $\delta^p = 0$ and $\delta \ne 0$. The following are equivalent:

1. $\psi(\alpha) = 0$, that is, $D'$ is additive;
2. there is $s \in R \setminus \{0\}$ with $\delta(s) = -\alpha s$;
3. $D'$ has a nonzero first integral of $\mathbb{G}_m$-weight one, namely $u s$ with $s$ as in 2;
4. $\alpha = \sum_i e_i \lambda_i$ with $e_i \in \mathbb{F}_p$, where the $s_i$ are prime elements of $R$ with $\delta(s_i) = \lambda_i s_i$.

The set $\{\alpha \in R : \psi(\alpha) = 0\}$ is the $\mathbb{F}_p$-span of the cofactors $\lambda$ of the $\delta$-invariant primes, and $s$ in 2 is unique up to a factor $c \in K$ with $\delta(c) = 0$.

Node: SG000000AM · Lean: none yet

*Proof.* (1) implies (2). Let $K^\delta = \ker(\delta : K \to K)$, a subfield that contains $K^p$. The operator $\nabla$ is $K^\delta$-linear: $\nabla(c f) = c \nabla(f)$ when $\delta(c) = 0$. Since $[K : K^p] = p^d$, the space $K$ has finite dimension over $K^\delta$. By Jacobson's formula $\nabla^p = \delta^p + \psi(\alpha) = 0$. A nilpotent endomorphism of a nonzero vector space of finite dimension has a nonzero kernel, so there is $s \in K^\times$ with $\delta(s) = -\alpha s$. Write $s = a / b$ with $a, b \in R$. Then $b^p \in K^\delta$, so $b^p s = a b^{p-1} \in R$ is also in $\ker \nabla$.

(2) implies (1). $0 = \nabla^p(s) = \delta^p(s) + \psi(\alpha) s = \psi(\alpha) s$, and $s \ne 0$.

(2) is equivalent to (3). $D'(u s) = u (\alpha s + \delta(s))$. Conversely, a first integral of weight one is $u s$ with $s \in R$, by the grading.

(2) implies (4). Write $s = c \prod_i s_i^{m_i}$ with $c \in k^\times$ and distinct primes $s_i$. If $p \mid m_i$, then $s_i^{p} \in K^\delta$, and division by it keeps $s$ in $R$ and in $\ker \nabla$. So we can assume $1 \le m_i \le p - 1$. Write $s = s_1^m t$ with $s_1 \nmid t$. Then $s_1^m$ divides $\delta(s) = m s_1^{m-1} \delta(s_1) t + s_1^m \delta(t)$, so $s_1 \mid m \delta(s_1) t$, and $p \nmid m$ gives $s_1 \mid \delta(s_1)$. So each $s_i$ is invariant, $\delta(s_i) = \lambda_i s_i$, and $-\alpha = \delta(s) / s = \sum_i m_i \lambda_i$. Take $e_i = -m_i$.

(4) implies (2). Take $s = \prod_i s_i^{m_i}$ with $m_i \in \{0, \dots, p - 1\}$ and $m_i \equiv -e_i$ modulo $p$. Then $\delta(s) / s = \sum_i m_i \lambda_i = -\alpha$, since $p \lambda_i = 0$.

The span statement is the equivalence of (1) and (4). It is consistent: $\psi(\alpha) = \alpha^p + \delta^{p-1}(\alpha)$ is additive and $\psi(e \alpha) = e \psi(\alpha)$ for $e \in \mathbb{F}_p$, and each cofactor satisfies $\psi(-\lambda_i) = 0$ by (2) implies (1) with $s = s_i$. If $\nabla s = \nabla s' = 0$ with $s \ne 0$, then $\delta(s' / s) = (\delta(s') s - s' \delta(s)) / s^2 = (-\alpha s' s + s' \alpha s) / s^2 = 0$. $\square$

**Corollary 3.22.24 (untwisting off a divisor).** Assume $\delta^p = 0$, $\psi(\alpha) = 0$, and let $s$ be as in Theorem 3.22.23. On $\mathbb{A}^1_u \times D(s)$ the $\mathbb{G}_m$-equivariant automorphism $(u, v) \mapsto (u s, v)$ turns $D'$ into the product field $\delta$. Hence the singularities of $D'$ outside $\mathbb{A}^1_u \times V(s)$ are those of the untwisted case $\alpha = 0$, and the twisted part of the problem lies over $Z(\delta) \cap V(s)$, where $V(s)$ is $\delta$-invariant.

Node: SG000000AN · Lean: none yet

*Proof.* Apply Lemma 3.22.22 with $g = s$, a unit on $D(s)$: the new form is $\alpha + \delta(s) / s = 0$. The divisor $V(s)$ is invariant since $\delta(s) = -\alpha s \in (s)$. $\square$

Along the invariant divisor a second torus symmetry untwists by one weighted blowup. This holds for each $H$.

**Proposition 3.22.25.** Let $Y = \operatorname{Spec} k[v_1, v']$, and let $\delta = \lambda(v') v_1 \partial_{v_1} + \delta''$, where $\lambda \in k[v']$ and $\delta''$ is a derivation in the variables $v'$ with coefficients in $k[v']$. Assume that $\delta$ is saturated with $\delta^p = H \delta$, and let $\alpha = -e \lambda$ with $1 \le e \le p - 1$. Put $w = p - e$. Then the weighted blowup of $\mathbb{A}^1_u \times Y$ along $\{u = v_1 = 0\}$ with the weights $(w, 1)$ is tame, and on both charts the pullback of $D' = \alpha u \partial_u + \delta$ is untwisted:

1. on $D_+(v_1)$, with $v_1 = t$ and $u = t^w u_1$, it is $\lambda t \partial_t + \delta''$, the product of $\mathbb{A}^1_{u_1}$ with $(Y, \delta)$;
2. on $D_+(u) = [\operatorname{Spec} k[\tau, v_1', v'] / \mu_w]$, with $u = \tau^w$ and $v_1 = \tau v_1'$, it is $\lambda \tau \partial_\tau + \delta''$, the product of $\mathbb{A}^1_{v_1'}$ with a copy of $(Y, \delta)$ in the coordinates $(\tau, v')$.

In this situation $\psi(\alpha) = H \alpha$ holds, and for $H = 0$ one can take $s = v_1^e$ in Theorem 3.22.23.

Node: SG000000AP · Lean: none yet

*Proof.* The weight $w$ is prime to $p$, so the blowup is tame. (1) $D'(t) = \lambda t$, $D'(v') = \delta''(v')$, and $D'(u_1) = D'(u) t^{-w} - w u t^{-w-1} D'(t) = (\alpha - w \lambda) u_1 = (-e - p + e) \lambda u_1 = 0$. (2) From $u = \tau^w$, $D'(\tau) = \alpha u / (w \tau^{w-1}) = (\alpha / w) \tau = \lambda \tau$, since $w \equiv -e$ modulo $p$. Then $D'(v_1') = (D'(v_1) \tau - v_1 D'(\tau)) / \tau^2 = (\lambda v_1 \tau - v_1 \lambda \tau) / \tau^2 = 0$, and $D'(v') = \delta''(v')$ does not involve $v_1$. Both fields are saturated because $\delta$ is. For the last claim, $\nabla(v_1^e) = (e \lambda + \alpha) v_1^e = 0$, so $0 = \nabla^p(v_1^e) = (\delta^p + \psi(\alpha))(v_1^e) = (H e \lambda + \psi(\alpha)) v_1^e$, and $\psi(\alpha) = -H e \lambda = H \alpha$. $\square$

Without the symmetry, the chart $D_+(u)$ of the same blowup carries a family over $\mathbb{A}^1_{v_1'}$ of threefold foliations that degenerates at $v_1' = 0$ to the normal linearization of $\delta$ along $V(v_1)$, and Posva's theorems say nothing about families. The next example shows that the case $H = 0$ with $\alpha \ne 0$ occurs.

**Example 3.22.26.** Let $e \in \{1, \dots, p - 1\}$, and on $\mathbb{A}^3$ let
$$\delta = v_1 v_2 \, \partial_{v_1} + v_2^2 \, \partial_{v_2} + v_3^p \, \partial_{v_3}, \qquad \alpha = e \, v_2 .$$
Then $\delta$ is saturated, $\delta^p = 0$, $\psi(\alpha) = 0$ and $\alpha \ne 0$, so $D' = e v_2 u \partial_u + \delta$ is an instance of Conjecture 3.22.20 with $H = 0$. Since the units of $k[v]$ are constants, $\alpha$ is not $\delta(g)/g$ for a unit $g$. The singular locus is $\mathbb{A}^1_u \times \{v_2 = v_3 = 0\}$, and $u v_1^{p-e}$ is a first integral. One weighted blowup of $\{u = v_1 = 0\}$ with the weights $(e, 1)$ reduces it to the untwisted threefold field $\delta$.

Node: SG000000AQ · Lean: none yet

*Proof.* The coefficients have no common factor. By induction $\delta^k(v_2) = k! \, v_2^{k+1}$, so $\delta^p(v_2) = 0$. Next $\delta(v_3) = v_3^p$ and $\delta^2(v_3) = p v_3^{p-1} v_3^p = 0$. On $v_1 k[v_2, v_3]$ the field $\delta$ acts as $\delta_0 + v_2$ with $\delta_0 = v_2^2 \partial_{v_2} + v_3^p \partial_{v_3}$, so Jacobson's formula gives $\delta^p(v_1) = (v_2^p + \delta_0^{p-1}(v_2)) v_1 = (1 + (p - 1)!) v_2^p v_1 = 0$ by Wilson's theorem. So $\delta^p = 0$, and in the same way $\psi(\alpha) = e (v_2^p + (p - 1)! \, v_2^p) = 0$. The zero set of the coefficients is $\{v_2 = v_3 = 0\}$, and it lies in $V(\alpha)$, so Proposition 3.22.18 gives the singular locus. We have $D'(u v_1^{p-e}) = u v_1^{p-e} v_2 (e + p - e) = 0$. Finally $\delta$ has the form of Proposition 3.22.25 with $\lambda = v_2$, and $\alpha = e v_2 = -(p - e) \lambda$, so Proposition 3.22.25 applies with $p - e$ in place of $e$, and $w = e$. $\square$

It is not known whether the twist of Example 3.22.26 is trivial in the local ring at the origin. The last result says where the case $H = 0$ comes from.

**Proposition 3.22.27.** Let $D$ be an additive foliation on $\mathbb{A}^4$, homogeneous of degree $d$ for a linear $\mathbb{G}_m$-action with positive weights prime to $p$. Assume that on the chart $D_+(x_i)$ the pullback is $u^d D'$ with $D' = \alpha u \partial_u + \delta$ saturated and $D'^p = H D'$. Put $c_0 = 1$ and $c_{k+1} = \delta(c_k) + d (k + 1) \alpha c_k$. Then $H = -c_{p-1}$. In particular, $p \mid d$ implies $H = 0$, and $\delta(\alpha) = 0$ implies $H = d^{p-1} \alpha^{p-1}$.

Node: SG000000AR · Lean: none yet

*Proof.* Hochschild's formula gives $0 = (u^d D')^p = u^{dp} H D' + (u^d D')^{p-1}(u^d) \, D'$. For $c \in k[v]$ we have $u^d D'(c u^m) = (\delta(c) + m \alpha c) u^{m+d}$, so by induction $(u^d D')^k(u^d) = c_k u^{d(k+1)}$. Hence $u^{dp} H = -c_{p-1} u^{dp}$. If $p \mid d$, then $c_1 = d \alpha = 0$, and all $c_k$ with $k \ge 1$ are $0$. If $\delta(\alpha) = 0$, then $c_k = k! \, d^k \alpha^k$, and $-c_{p-1} = -(p - 1)! \, d^{p-1} \alpha^{p-1} = d^{p-1} \alpha^{p-1}$. $\square$

In Example 3.22.14, $d = p - 1$ and $\delta(\alpha) = 0$ in the chart $x$, which gives $H = \alpha^{p-1}$ again, as in Proposition 3.22.15. So the case $H = 0$ of the twisted problem is the one that additive invariant foliations of degree divisible by $p$ produce, together with the untwisted charts.

### What is open

1. Conjecture 3.22.16, one weighted blowup at a multiplicative point in truncated coordinates. A short proof is expected.
2. Conjecture 3.22.21, the equivariant gluing of the chart resolutions of Corollary 3.22.19. Posva's Remark 5.1.5 shows that this is a real issue. With Conjecture 3.22.16 it would resolve Example 3.22.14.
3. Conjecture 3.22.20 with $H = 0$ at the points of $Z(\delta) \cap V(s)$, when $\delta$ has no second torus symmetry as in Proposition 3.22.25.
4. Conjecture 3.22.20 with $H \ne 0$.
5. Problem 4.10 of note 04 for tori of rank 1, 2 and 3, and for actions of $\mathbb{G}_m$ with weights of mixed sign, zero or divisible by $p$.

### Exercises

1. Show that for $p = 2$ the regular rank one foliations $\mathcal{F}_V$ on $\mathbb{A}^2$ are the ones with $V = \mathbb{F}_2 e_1$ or $V = \mathbb{F}_2 e_2$, and resolve $\mathcal{F}_V$ for $V = \mathbb{F}_2 (1, 1)$ by one blowup of the origin. Compute the quotient $\mathbb{A}^2 / \mathcal{F}_V$ by Corollary 3.22.11 and check that it is the cone $\operatorname{Spec} k[x^2, x y, y^2]$.
2. Let $p = 3$ and $V = \mathbb{F}_3 (1, 2)$ in $\mathbb{F}_3^2$. Run the algorithm, find the weights, and check that the chart $D_+(x_2)$ is $[\mathbb{A}^2 / \mu_2]$, which is tame. Why would the weights $(1, -1)$ not make sense?
3. Let $p = 5$ and $V = \mathbb{F}_5 (1, 1, 0, 0) + \mathbb{F}_5 (0, 1, 1, 1) \subseteq \mathbb{F}_5^4$. Find the free basis of $\mathcal{F}_V$ of Theorem 3.22.6, and carry out the first step of the algorithm.
4. Let $c = (1, \dots, 1) \in \mathbb{F}_p^n$ and $V = \mathbb{F}_p c$. Show that $\mathcal{F}_V = A \cdot D_c$, that $\operatorname{Sing} \mathcal{F}_V = \{0\}$ for $n \ge 2$, and that the ordinary blowup of the origin resolves it.
5. In Example 3.22.17, show that the statement fails for $p = 2$: the coefficients of $D$ have a common factor, and the singular locus changes.
6. In Example 3.22.14 for $p = 2$, compute the chart $y$ of the blowup of the origin and find the singular point $(0 : 1 : 0 : 0)$ and the linear part of the generator there.
7. Prove Hochschild's formula $(h E)^p = h^p E^p + (h E)^{p-1}(h) \, E$ for $p = 2$ and $p = 3$ by direct expansion.
8. Show that the field $\delta$ of the chart $z$ in Example 3.22.14 satisfies $\delta^p = 0$, and that $X$ and $Y$ satisfy $\delta^2(X) = \delta^2(Y) = 0$.
9. In Theorem 3.22.23, take $d = 2$ and $\delta = v_1 v_2 \partial_{v_1} + v_2^2 \partial_{v_2}$. Show that $\delta^p = 0$, that $v_1$, $v_2$ and $v_1 - c v_2$ with $c \in k$ are invariant primes with the cofactor $v_2$, and deduce that $\psi(e v_2) = 0$ for $e \in \mathbb{F}_p$. Find $s$ for $\alpha = e v_2$.

### Status

The results are the nodes SG000000A7 to SG000000AR of the map. Theorems 3.22.6 and 3.22.10, Corollary 3.22.11, Lemma 3.22.12, Examples 3.22.14 and 3.22.17 and Proposition 3.22.18 are from research note 58, with the corrections of the referee report in note 73. Proposition 3.22.15, Lemma 3.22.22, Theorem 3.22.23, Corollary 3.22.24, Propositions 3.22.25 and 3.22.27 and Example 3.22.26 are new in note 73. Corollary 3.22.19 depends on the threefold theorems of Posva, which are a hypothesis on the map. Conjectures 3.22.16, 3.22.20 and 3.22.21 are open, and so it is not known whether Example 3.22.14 has a resolution. The computer checks of notes 58 and 73 (all subspaces of $\mathbb{F}_p^4$ for $p = 2, 3, 5$, and the examples for $p \le 7$) are evidence only. None of the nodes has a Lean proof yet. An outside expert has not yet read the result.

### Notes and references

The results are in research note 58, with the corrections of note 73, which is a referee report on note 58. Note 73 found that the charts $x$ and $y$ of Example 3.22.14 were missing, proved Proposition 3.22.15, stated Conjecture 3.22.16, restricted Corollary 3.22.11 to the diagonal action and the case of $\mathbb{G}_m$ to linear actions with positive weights prime to $p$, and proved the results on the case $H = 0$. The definitions and the theory of quotients by 1-foliations are in [Pos23]: additive and multiplicative derivations and Hochschild's formula in Section 2.3, the Jacobson correspondence in Section 2.5, and the normal form of singular multiplicative derivations in Section 4.1. The resolution of 1-foliations on surfaces and threefolds is [Pos24], and the weighted blowups there are in Example 2.4.3. Weighted blowups as stacks are in [Quek22]. Toric resolution is [KKMS]. Jacobson's formula $(\delta + a)^p = \delta^p + a^p + \delta^{p-1}(a)$ is classical.
