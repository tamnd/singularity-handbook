---
title: Alterations
nodes: [SG0000000V, SG00000004, SG00000002]
sources: [dJ96, Har, Mat, Stacks]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Alterations

In this volume a *variety* over a field $k$ is an integral scheme that is separated and of finite type over $k$. This is the convention of [dJ96, 2.9]. Volume 0, Definition 2.1.4 asks only that a variety is reduced, and there a variety can have several irreducible components. We say *integral variety* when we want to stress the difference. For an integral scheme $X$ we write $k(X)$ for its function field and $\eta_X$ for its generic point.

### Alterations and their degree

**Definition 1.1.1 (alteration).** Let $X$ be a Noetherian integral scheme. An *alteration* of $X$ is an integral scheme $X'$ with a morphism $\varphi \colon X' \to X$ that is proper and dominant, such that there is a nonempty open subset $U \subseteq X$ over which $\varphi^{-1}(U) \to U$ is finite. A *modification* of $X$ is an alteration $\varphi$ that is birational, that is, an isomorphism over a nonempty open subset of $X$.

This is [dJ96, 2.20] and [dJ96, 2.17]. A dominant morphism of integral schemes sends the generic point to the generic point. Indeed, $\varphi(X') = \varphi(\overline{\{\eta_{X'}\}})$ lies in the closure of $\varphi(\eta_{X'})$, and this closure is all of $X$ because $\varphi$ is dominant. A proper dominant morphism is surjective, because its image is closed and dense. A composition of modifications is a modification.

**Lemma 1.1.2.** Let $\varphi \colon X' \to X$ be an alteration, and let $U$ be as in Definition 1.1.1. Then $k(X')$ is a finite extension of $k(X)$, and the generic fibre $\varphi^{-1}(\eta_X)$ is the single point $\eta_{X'}$.

Lean: none yet

*Proof.* Let $V = \operatorname{Spec} A$ be a nonempty affine open subset of $U$. A finite morphism is affine, so $\varphi^{-1}(V) = \operatorname{Spec} B$ with $B$ a finite $A$-algebra. The open set $\varphi^{-1}(V)$ contains $\eta_{X'}$, so it is not empty and $B$ is a domain with fraction field $k(X')$. Let $K = k(X) = \operatorname{Frac}(A)$. The ring $B \otimes_A K$ is a localization of $B$, so it is a domain, and it is a finite dimensional $K$-vector space. A domain of finite dimension over a field is a field. So $B \otimes_A K$ is a field that contains $B$ and lies in $\operatorname{Frac}(B)$, and so $B \otimes_A K = k(X')$. This proves that $[k(X') : K]$ is finite. The generic fibre is $\operatorname{Spec}(B \otimes_A K)$, which is one point. $\square$

**Definition 1.1.3 (degree).** The *degree* of an alteration $\varphi \colon X' \to X$ is $\deg \varphi = [k(X') : k(X)]$. The alteration is *generically étale* if there is a nonempty open subset $U \subseteq X$ such that $\varphi^{-1}(U) \to U$ is finite and étale.

A modification has degree 1. Conversely, an alteration of degree 1 is a modification: in the proof of Lemma 1.1.2, if $B \otimes_A K = K$, then $B$ and $A$ have the same fraction field, $B = A[b_1, \dots, b_m]$ with $b_i = a_i / a$, and $B_a = A_a$. So $\varphi$ is an isomorphism over the open set $D(a)$.

**Lemma 1.1.4.** Let $X$ and $X'$ be integral varieties over a field $k$, and let $\varphi \colon X' \to X$ be a proper dominant morphism over $k$. Then $\varphi$ is an alteration if and only if $\dim X' = \dim X$.

Lean: none yet

*Proof.* For an integral variety, the dimension is the transcendence degree of the function field over $k$ [Har, Exercise II.3.20]. If $\varphi$ is an alteration, then $k(X')$ is finite over $k(X)$ by Lemma 1.1.2, so the two transcendence degrees agree.

Conversely, assume that $\dim X' = \dim X = d$. Then $k(X')$ is algebraic over $k(X)$, and it is finitely generated, so it is a finite extension. Let $V = \operatorname{Spec} A \subseteq X$ be a nonempty affine open subset and let $W = \operatorname{Spec} B$ be a nonempty affine open subset of $\varphi^{-1}(V)$. Write $B = A[b_1, \dots, b_m]$. Each $b_i$ is algebraic over $K = \operatorname{Frac}(A)$, so it satisfies an equation $a_i b_i^{n_i} + \dots = 0$ with coefficients in $A$ and $a_i \neq 0$. Let $a = a_1 \cdots a_m$. Then each $b_i$ is integral over $A_a$, and $B_a$ is a finite $A_a$-module. The complement $T = X' \setminus W$ is a closed subset that does not contain $\eta_{X'}$, so each of its irreducible components has dimension less than $d$. The image $\varphi(T)$ is closed because $\varphi$ is proper, and its irreducible components have dimension less than $d$ by the inequality of transcendence degrees. So $\varphi(T)$ does not contain $\eta_X$. Choose $a' \in A$ with $a' \ne 0$ such that $D(a a') \subseteq V \setminus \varphi(T)$. Then $\varphi^{-1}(D(aa'))$ lies in $W$ and is equal to $\operatorname{Spec} B_{aa'}$, which is finite over $A_{aa'}$. $\square$

This is the remark in [dJ96, 2.20] that the finiteness condition is equivalent to $\dim X = \dim X'$. In particular, for integral varieties, an alteration is the same as a proper, surjective and generically finite morphism between varieties of the same dimension. This is the form of Volume 0, Theorem 2.3.5.

**Lemma 1.1.5.** Let $\varphi \colon X' \to X$ be an alteration. Then $\varphi$ is generically étale if and only if $k(X')$ is a separable extension of $k(X)$.

Lean: none yet

*Proof.* Keep the notation of the proof of Lemma 1.1.2, with $K = k(X)$ and $L = k(X') = B \otimes_A K$. If $\varphi$ is étale over a nonempty open subset, then the generic fibre $\operatorname{Spec} L \to \operatorname{Spec} K$ is étale, and so $L$ is separable over $K$. Conversely, assume that $L/K$ is separable. Choose $e_1, \dots, e_n \in B$ that form a basis of $L$ over $K$. Each element of a finite set of generators of the $A$-module $B$ is a $K$-linear combination of the $e_j$, so after we invert one nonzero element of $A$, the module $B$ is free with basis $e_1, \dots, e_n$. Let $\delta = \det(\operatorname{Tr}_{L/K}(e_i e_j))$ be the discriminant. Since $L/K$ is separable, the trace form is nondegenerate and $\delta \neq 0$. Over $A_\delta$, the algebra $B_\delta$ is finite free with a unit discriminant, so it is étale over $A_\delta$ [Stacks]. $\square$

This is the last remark of [dJ96, 2.20]. If $k$ has characteristic 0, then every alteration is generically étale.

**Lemma 1.1.6.** Let $\psi \colon X' \to X$ and $\varphi \colon X'' \to X'$ be alterations. Then $\psi \circ \varphi$ is an alteration of degree $\deg \psi \cdot \deg \varphi$. If $\psi$ and $\varphi$ are generically étale, then so is $\psi \circ \varphi$.

Lean: none yet

*Proof.* The composition is proper and dominant. Let $U \subseteq X$ be a nonempty open subset over which $\psi$ is finite, and let $U' \subseteq X'$ be a nonempty open subset over which $\varphi$ is finite. The set $\psi(X' \setminus U')$ is closed, since $\psi$ is proper. It does not contain $\eta_X$, since by Lemma 1.1.2 the only point of $X'$ over $\eta_X$ is $\eta_{X'}$, and $\eta_{X'} \in U'$. Let $U_1 = U \setminus \psi(X' \setminus U')$. Then $\psi^{-1}(U_1) \subseteq U'$, so $\varphi$ is finite over $\psi^{-1}(U_1)$, and $\psi \circ \varphi$ is finite over $U_1$. The formula for the degree is the tower law for $k(X) \subseteq k(X') \subseteq k(X'')$. The last claim follows from Lemma 1.1.5, because a separable extension of a separable extension is separable. $\square$

### Examples

**Lemma 1.1.7.** Let $X$ be an integral variety over a field $k$ with function field $K$, and let $L$ be a finite extension of $K$. Let $X_L \to X$ be the normalization of $X$ in $L$. Then $X_L \to X$ is a finite alteration of degree $[L : K]$, and $X_L$ is normal. It is generically étale if and only if $L/K$ is separable.

Lean: none yet

*Proof.* Let $\operatorname{Spec} A \subseteq X$ be an affine open subset. Choose a basis of $L$ over $K$ and multiply it by an element of $A$, so that the basis elements $l_1, \dots, l_n$ are integral over $A$. Then $A' = A[l_1, \dots, l_n]$ is a domain that is a finitely generated $k$-algebra and a finite $A$-module, with fraction field $L$. The integral closure $B$ of $A$ in $L$ is the integral closure of $A'$ in its fraction field. By the theorem of E. Noether (Volume 1, Theorem 2.4.7), $B$ is a finite $A'$-module, so it is a finite $A$-module. The rings $B$ glue to the normalization $X_L$ of $X$ in $L$, which is integral, normal, and finite over $X$. A finite morphism is proper, and $X_L \to X$ is surjective because $B$ is integral over $A$. Its function field is $L$. The last claim is Lemma 1.1.5. $\square$

**Example 1.1.8 (Frobenius).** Let $k$ be a field of characteristic $p > 0$ and $X = \mathbb{A}^n_k$. The morphism $F \colon \mathbb{A}^n_k \to \mathbb{A}^n_k$ given by $x_i \mapsto x_i^p$ corresponds to the inclusion $k[x_1^p, \dots, x_n^p] \subseteq k[x_1, \dots, x_n]$. The larger ring is a free module over the smaller ring with basis the monomials $x^a$ with $0 \le a_i < p$, so $F$ is finite and flat of degree $p^n$. The extension of function fields is purely inseparable, so $F$ is an alteration of degree $p^n$ that is not generically étale. The source of $F$ is regular, but $F$ is not a resolution of $\mathbb{A}^n_k$. This example shows that an alteration of degree a power of $p$ can carry no information on the singularities of $X$.

**Example 1.1.9 (the quadric cone).** Let $k$ be a field and let $X = \operatorname{Spec} k[x, y, z]/(xy - z^2)$. The polynomial $xy - z^2$ has degree 1 in $x$ and $y$ does not divide $z^2$, so it is irreducible and $X$ is an integral surface. Consider the morphism $\varphi \colon \mathbb{A}^2_k = \operatorname{Spec} k[s, t] \to X$ given by $x \mapsto s^2$, $y \mapsto t^2$, $z \mapsto st$. Its image ring is the subring $k[s^2, st, t^2]$ of the polynomials of even degree. The map $k[x, y, z]/(xy - z^2) \to k[s^2, st, t^2]$ is surjective, and it is injective because both rings are domains of dimension 2 and a nonzero prime ideal of a domain of finite type over $k$ has a quotient of smaller dimension. The ring $k[s, t]$ is generated by $1, s, t$ as a module over $k[s^2, st, t^2]$, because each monomial of odd degree is $s$ or $t$ times a monomial of even degree. The function field $k(s, t)$ is $k(s, t/s)$, and $k(s^2, st, t^2) = k(s^2, t/s)$. So $\varphi$ is a finite alteration of degree 2, with $s$ a root of $T^2 - s^2$. If $p = \operatorname{char} k \ne 2$, then $\varphi$ is generically étale, and it is the quotient of $\mathbb{A}^2_k$ by the involution $(s, t) \mapsto (-s, -t)$. If $p = 2$, then $\varphi$ is purely inseparable. In each characteristic $\varphi$ is a regular alteration of $X$ of degree 2, and the blowup of the vertex is a resolution of $X$.

### Divisors with simple normal crossings

We use the divisors with simple normal crossings of Volume 4, Definition 3.1.2: on a regular Noetherian scheme $Y$, an effective Cartier divisor $D = \sum_i D_i$ with regular components $D_i$ such that, at each point, the components through the point have local equations that are part of a regular system of parameters. De Jong uses the following form [dJ96, 2.4]. We often identify $D$ with its support, as de Jong does.

**Definition 1.1.10 (strict normal crossings).** Let $Y$ be a regular Noetherian scheme. A closed subset $D \subseteq Y$, with irreducible components $D_i$ for $i \in I$, is a *divisor with strict normal crossings* if each $D_i$ is a divisor on $Y$ and, for each nonempty subset $J \subseteq I$, the scheme theoretic intersection $D_J = \bigcap_{j \in J} D_j$ is a regular scheme of codimension $\# J$ in $Y$ at each of its points (or is empty).

Node: SG0000000V · Lean: `Singularity.IsSncDivisor`

**Lemma 1.1.11.** Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$ and let $t_1, \dots, t_r \in \mathfrak{m}$. Then $t_1, \dots, t_r$ are part of a regular system of parameters if and only if $R/(t_1, \dots, t_r)$ is regular of dimension $d - r$.

Lean: none yet

*Proof.* If the $t_i$ are part of a regular system of parameters, apply Volume 1, Proposition 1.2.6 $r$ times. Each time the image of the next $t_i$ is part of a regular system of parameters of the quotient, so it is not in the square of its maximal ideal. Conversely, let $\bar R = R/(t_1, \dots, t_r)$ with maximal ideal $\bar{\mathfrak{m}}$. Then $\bar{\mathfrak{m}}/\bar{\mathfrak{m}}^2 = \mathfrak{m}/(\mathfrak{m}^2 + (t_1, \dots, t_r))$. The left side has dimension $d - r$ over $R/\mathfrak{m}$ because $\bar R$ is regular of dimension $d - r$, and $\mathfrak{m}/\mathfrak{m}^2$ has dimension $d$. So the images of $t_1, \dots, t_r$ in $\mathfrak{m}/\mathfrak{m}^2$ span a space of dimension $r$, and they are linearly independent. Elements of $\mathfrak{m}$ whose images in $\mathfrak{m}/\mathfrak{m}^2$ are linearly independent can be completed to a regular system of parameters, by Nakayama's lemma. $\square$

Apply the lemma at each point of $Y$ to the local equations of the components through the point. It shows that, for the reduced divisor with components $D_i$, Definition 1.1.10 and Volume 4, Definition 3.1.2 agree. A finite set of closed points on a regular curve is a divisor with strict normal crossings, since a closed point of a regular curve is a regular scheme of codimension 1.

### Semistable schemes over a trait

A *trait* is the spectrum $S$ of a discrete valuation ring $R$, with generic point $\eta$, closed point $s$ and a uniformizer $\pi$. An $S$-variety is an integral separated scheme of finite type and flat over $S$ [dJ96, 2.15]. Its special fibre $X_s = V(\pi)$ is a principal divisor on $X$.

**Definition 1.1.12 (strictly semistable).** Let $S$ be a trait and let $X$ be an $S$-variety. Let $X_i$, $i \in I$, be the irreducible components of $X_s$, and for $J \subseteq I$ nonempty let $X_J = \bigcap_{i \in J} X_i$ be the scheme theoretic intersection. Then $X$ is *strictly semistable* over $S$ if the generic fibre $X_\eta$ is smooth over $\kappa(\eta)$, the special fibre $X_s$ is reduced, each $X_i$ is a divisor on $X$, and each $X_J$ is smooth over $\kappa(s)$ of codimension $\# J$ in $X$.

This is [dJ96, 2.16]. De Jong shows that the complete local ring of $X$ at a point of $X_s$ that lies on exactly $r$ of the components is isomorphic to $B[[t_1, \dots, t_r]]/(t_1 \cdots t_r - \pi)$, with $B$ a complete Noetherian local ring that is formally smooth over $R$, and with $X_i$ given by $t_i = 0$. In particular $X$ is regular and $X_s$ is a divisor with strict normal crossings on $X$.

**Definition 1.1.13 (strict semistable pair).** Let $S$ be a trait, $X$ an $S$-variety, and $Z \subseteq X$ a closed subset that contains the special fibre. Write $Z = Z_h \cup X_s$ with $Z_h$ the union of the irreducible components of $Z$ that are flat over $S$. The pair $(X, Z)$ is a *strict semistable pair* if $X$ is strictly semistable over $S$, $Z$ is a divisor with strict normal crossings on $X$, and, for each nonempty set $J$ of irreducible components of $Z_h$, their intersection $Z_J$ is a disjoint union of $S$-varieties that are strictly semistable over $S$.

This is [dJ96, 6.3]. By [dJ96, 6.4], the complete local ring at a point of $X_s$ is $C[[t_1, \dots, t_n, s_1, \dots, s_m]]/(\pi - t_1 \cdots t_n)$, with $C$ formally smooth over $R$, the components of $X_s$ given by $t_i = 0$ and the components of $Z_h$ given by $s_j = 0$.

**Example 1.1.14.** Let $X = \operatorname{Spec} R[u, v]/(uv - \pi)$. The generic fibre is $uv = \pi$ with $\pi$ a unit, which is isomorphic to $\mathbb{G}_m$ and so smooth. The special fibre is $uv = 0$ over $\kappa(s)$, the union of two lines $X_1 = V(u)$ and $X_2 = V(v)$, each of which is a principal divisor on $X$ and smooth over $\kappa(s)$. Their intersection is the point $u = v = 0$, which is smooth over $\kappa(s)$ and of codimension 2. So $X$ is strictly semistable over $S$. At the origin the maximal ideal is $(u, v, \pi) = (u, v)$ and the dimension is 2, so $X$ is regular there. Section 2.1 shows that $\operatorname{Spec} R[u, v]/(uv - \pi^n)$ with $n \ge 2$ is not regular, and it resolves it by blowups.

### Resolutions are alterations of degree 1

The resolutions of Volume 0, Definition 2.1.5 are the Lean definition `Singularity.IsResolution` of node SG00000004.

**Lemma 1.1.15.** Let $X$ be an integral variety over a field $k$.

1. Let $\pi \colon Y \to X$ be a resolution in the sense of Volume 0, Definition 2.1.5. Then $Y$ is integral and $\pi$ is a modification, so it is an alteration of degree 1 with $Y$ regular.
2. An alteration of $X$ of degree greater than 1 is not a resolution of $X$.

Lean: none yet

*Proof.* The regular locus $\operatorname{Reg}(X)$ is open, because a finitely generated algebra over a field is excellent [Mat]. It contains $\eta_X$, because the local ring there is a field. So $\operatorname{Reg}(X)$ is a nonempty open subset of $X$, and it is irreducible. (1) The morphism $\pi$ is an isomorphism over $\operatorname{Reg}(X)$, so $\pi^{-1}(\operatorname{Reg}(X))$ is irreducible, and it is dense in $Y$. So $Y$ is irreducible. A regular scheme is reduced, so $Y$ is integral. The morphism $\pi$ is proper and an isomorphism over a dense open subset, so it is a modification. (2) A resolution is an isomorphism over the nonempty open set $\operatorname{Reg}(X)$, so it induces an isomorphism of function fields and has degree 1. $\square$

The converse of (1) is false. The blowup of a closed point of $\mathbb{A}^2_k$ is a modification with a regular source, but it is not an isomorphism over $\operatorname{Reg}(\mathbb{A}^2_k) = \mathbb{A}^2_k$. So a regular alteration of degree 1 is only a *weak resolution*. Volume 0, Proposition 2.5.2 shows that the definition of a resolution in the project excludes the maps of degree 2 that look like resolutions. The present lemma says the same for all alterations.

### Notes and references

The definitions follow Section 2 of [dJ96]. The Lean library has the regular schemes (`Singularity.IsRegularScheme`, node SG00000002), the resolutions (`Singularity.IsResolution`, node SG00000004) and the divisors with simple normal crossings (`Singularity.IsSncDivisor`, node SG0000000V). It has no definition of an alteration yet. A Lean definition would ask for an integral scheme, a proper dominant morphism, and a nonempty open set over which the morphism is finite, as in Definition 1.1.1.
