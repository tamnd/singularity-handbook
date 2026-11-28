---
title: Normal surfaces
nodes: [SG0000000M]
sources: [Mat, EGA4-7, Stacks, Har, Liu, AM69]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Normal surfaces

The process of Lipman alternates the normalization and the blowup of the singular points. For this process to make sense we need two facts. The normalization must be a finite morphism, so that it keeps us among Noetherian schemes of finite type over the old one. And a normal surface must have only finitely many singular points, so that the center of each blowup is a finite set of closed points. This section proves both facts for excellent surfaces.

### Surfaces and normalization

**Definition 1.2.1.** In this volume a *surface* is a Noetherian scheme $X$ with $\dim X \le 2$. The surface is *excellent* if it is locally excellent in the sense of Definition 5.3.1 of Volume 1. A Noetherian scheme $X$ is *normal* if each local ring $\mathcal{O}_{X,x}$ is an integrally closed domain. Let $X$ be a reduced Noetherian scheme with irreducible components $X_1, \dots, X_s$, each with its reduced structure. The *normalization* of an integral $X_i$ with function field $K_i$ is the affine morphism $X_i^\nu \to X_i$ given by the integral closure of $\mathcal{O}_{X_i}$ in $K_i$. The *normalization* of $X$ is $\nu : X^\nu = \coprod_i X_i^\nu \to X$.

Lean: `Singularity.affineNormalization`, `Singularity.isIntegrallyClosed_affineNormalization`, `Singularity.affineNormalization_eq_bot_iff` (the affine case).

A Noetherian normal scheme is the disjoint union of its connected components, and each component is integral. The normalization $X^\nu$ is normal. Over an affine open $\operatorname{Spec} R$ of an integral $X_i$, it is $\operatorname{Spec} R'$, where $R'$ is the integral closure of $R$ in $K_i$ [Stacks].

**Theorem 1.2.2.** Let $X$ be a reduced Noetherian scheme.

1. If $X$ is of finite type over a field, then $\nu : X^\nu \to X$ is finite.
2. If $X$ is excellent, then $\nu$ is finite, $X^\nu$ is a normal excellent scheme, and $\dim X^\nu = \dim X$.

Node: SG0000000M · Lean: `Singularity.Algebra.finite_integralClosure` (part 1, for an affine domain)

*Proof.* 1. The question is local on $X$ and we may treat each component. Thus let $R$ be a domain of finite type over a field. By the theorem of E. Noether (Theorem 2.4.7 of Volume 1), the integral closure of $R$ in its field of fractions is a finite $R$-module.

2. An excellent ring is a Nagata ring, that is, for each prime $\mathfrak{p}$ of $R$ and each finite extension $L$ of $\kappa(\mathfrak{p})$, the integral closure of $R/\mathfrak{p}$ in $L$ is finite over $R/\mathfrak{p}$ [EGA4-7, Section 7.8], [Stacks]. Apply this with $L = \kappa(\mathfrak{p})$ for the minimal primes $\mathfrak{p}$ of $R$. This gives the finiteness. A finite $R$-algebra is of finite type, so it is excellent by Theorem 5.2.8 of Volume 1. For the dimension, let $R \subseteq R'$ be an integral extension. By the going up theorem [AM69, Theorem 5.11], each chain of primes of $R$ lifts to a chain of $R'$. By incomparability [AM69, Corollary 5.9], each chain of $R'$ contracts to a chain of $R$ of the same length. Thus $\dim R' = \dim R$. $\square$

For a Noetherian ring that is not excellent, the normalization can fail to be finite. Proposition 2.2.2 shows that a Noetherian domain whose normalization is not finite has no resolution.

### The singular points

**Lemma 1.2.3.** Let $X$ be a Noetherian scheme with $\dim X \le 2$, and let $Z \subseteq X$ be a closed subset such that $\dim \mathcal{O}_{X,z} = 2$ for each $z \in Z$. Then $Z$ is a finite set of closed points.

Lean: `Singularity.finite_isMaximal_of_height_eq_two` (for $X = \operatorname{Spec} R$, without the bound $\dim X \le 2$)

*Proof.* The space $Z$ is Noetherian, so it has finitely many irreducible components. Let $z_1, \dots, z_s$ be their generic points. Let $z \in Z$. Then $z$ lies in the closure of some $z_i$. Assume that $z \ne z_i$. Then $z_i$ corresponds to a prime $\mathfrak{p}$ of $\mathcal{O}_{X,z}$ that is not maximal, and $\mathcal{O}_{X,z_i} = (\mathcal{O}_{X,z})_\mathfrak{p}$. A chain of primes of length 2 in $(\mathcal{O}_{X,z})_\mathfrak{p}$ ends at $\mathfrak{p}$. If we add the maximal ideal, we get a chain of length 3 in $\mathcal{O}_{X,z}$. Thus $\dim \mathcal{O}_{X,z} \ge 3$. This is false, since $\dim \mathcal{O}_{X,z} \le \dim X \le 2$. Thus $z = z_i$, and $Z = \{z_1, \dots, z_s\}$. The closure of $z_i$ is in $Z$, and by the argument each of its points is $z_i$. Thus $z_i$ is a closed point. $\square$

**Theorem 1.2.4.** Let $X$ be a normal Noetherian scheme with $\dim X \le 2$, and assume that $\operatorname{Reg}(X)$ is open. Then $\operatorname{Sing}(X) = X \setminus \operatorname{Reg}(X)$ is a finite set of closed points, and $\dim \mathcal{O}_{X,x} = 2$ for each $x \in \operatorname{Sing}(X)$. This holds in particular for each normal excellent surface.

Lean: `Singularity.finite_isMaximal_compl_regularLocus` (for $X = \operatorname{Spec} R$; not the claim on excellent surfaces)

*Proof.* Let $x \in X$ with $\dim \mathcal{O}_{X,x} \le 1$. If the dimension is 0, then $\mathcal{O}_{X,x}$ is a local domain of dimension 0, that is, a field, and it is regular. If the dimension is 1, then $\mathcal{O}_{X,x}$ is an integrally closed Noetherian local domain of dimension 1, and it is regular by Theorem 1.4.2 of Volume 1. Thus each $x \in \operatorname{Sing}(X)$ has $\dim \mathcal{O}_{X,x} = 2$. The set $\operatorname{Sing}(X)$ is closed by assumption. Lemma 1.2.3 gives the result. For an excellent $X$, the set $\operatorname{Reg}(X)$ is open by Proposition 5.3.2 of Volume 1. $\square$

The theorem fails in dimension 3. The threefold $V(xy - z^2) \subseteq \mathbb{A}^4_k$, with coordinates $x, y, z, w$, is normal by the criterion of Serre, but it is singular along the line $x = y = z = 0$.

### One round of the process

**Corollary 1.2.5.** Let $X$ be a normal excellent surface and let $S = \operatorname{Sing}(X)$ with its reduced structure. Let $X_1$ be the normalization of $\operatorname{Bl}_S X$. Then $X_1$ is a normal excellent surface, the morphism $X_1 \to X$ is proper, and it is an isomorphism over $\operatorname{Reg}(X) = X \setminus S$.

Lean: none yet

*Proof.* By Theorem 1.2.4, $S$ is a finite set of closed points. The morphism $\operatorname{Bl}_S X \to X$ is projective, so it is proper and of finite type. We may work on one connected component of $X$, so we may assume that $X$ is integral. If $S = \emptyset$, there is nothing to prove. Otherwise $S \ne X$, because a point of a normal scheme with $\dim \mathcal{O}_{X,x} = 0$ is regular. By the remark after Lemma 1.1.3, $\operatorname{Bl}_S X$ is integral, and each chart over an affine open $\operatorname{Spec} R$ is a ring $B$ with $R \subseteq B \subseteq K$, where $K$ is the function field.

The scheme $\operatorname{Bl}_S X$ is of finite type over $X$, so it is excellent by Theorem 5.2.8 of Volume 1. For the dimension, let $P$ be a prime of a chart $B$ and let $\mathfrak{p} = P \cap R$. The dimension inequality [Mat, Theorem 15.5] gives $\operatorname{ht} P + \operatorname{tr.deg}_{\kappa(\mathfrak{p})} \kappa(P) \le \operatorname{ht} \mathfrak{p} + \operatorname{tr.deg}_R B$. Here $\operatorname{tr.deg}_R B = 0$, since $B \subseteq K$. Thus $\operatorname{ht} P \le \operatorname{ht} \mathfrak{p} \le 2$, and $\dim \operatorname{Bl}_S X \le 2$.

By Theorem 1.2.2, $X_1 \to \operatorname{Bl}_S X$ is finite, $X_1$ is normal and excellent, and $\dim X_1 \le 2$. The composite $X_1 \to X$ of a finite and a proper morphism is proper. Over $X \setminus S$ the blowup is an isomorphism by Theorem 1.1.2, and $X \setminus S$ is normal, so the normalization does not change it. $\square$

### Normal hypersurfaces

The examples of this volume are surfaces in $\mathbb{A}^3_k$. The next lemma shows that such a surface is normal when its singular points are isolated.

**Lemma 1.2.6.** Let $k$ be a field, let $F \in k[x, y, z]$ be a nonconstant polynomial, and let $X = V(F) \subseteq \mathbb{A}^3_k$. Assume that $\operatorname{Sing}(X)$ is a finite set of closed points. Then $X$ is normal.

Lean: `Singularity.height_isMaximal_quotient_span_singleton_three`, `Singularity.isRegularLocalRing_of_height_le_one` (the dimension of the local rings and the condition $R_1$; the condition $S_2$ and the normality are not in Lean)

*Proof.* Let $P = k[x, y, z]$ and $A = P/(F)$. We use the criterion of Serre: a Noetherian ring is normal if and only if it satisfies $R_1$ and $S_2$ [Mat, Theorem 23.8].

*The condition $S_2$.* Let $\mathfrak{q}$ be a prime of $P$ that contains $F$. The ring $P_\mathfrak{q}$ is regular, so it is Cohen-Macaulay, and $F$ is a nonzerodivisor of $P_\mathfrak{q}$. Thus $A_{\mathfrak{q}} = P_\mathfrak{q}/(F)$ is Cohen-Macaulay [Mat, Section 17]. A Cohen-Macaulay ring satisfies $S_n$ for each $n$.

*The condition $R_1$.* Let $\mathfrak{m}$ be a maximal ideal of $P$ that contains $F$. Then $\dim P_\mathfrak{m} = 3$ [Har, Theorem I.1.8A], and $\dim A_\mathfrak{m} = 2$, since $F$ is a nonzerodivisor of $P_\mathfrak{m}$ [AM69, Corollary 11.18]. Thus each closed point of $X$ has a local ring of dimension 2. Let $\mathfrak{p}$ be a prime of $A$ with $\dim A_\mathfrak{p} \le 1$. Then $\mathfrak{p}$ is not a closed point, so $\mathfrak{p} \notin \operatorname{Sing}(X)$, and $A_\mathfrak{p}$ is regular. Thus $A$ satisfies $R_1$. $\square$

The finite set of the lemma is often easy to check. By the Jacobian criterion (Corollary 1.8.3 of Volume 1), applied to the regular ring $k[x, y, z]$ and the derivations $\partial/\partial x$, $\partial/\partial y$, $\partial/\partial z$, each prime of $A$ that does not contain all three partial derivatives of $F$ is in $\operatorname{Reg}(X)$. Section 2.3 uses this together with Lemma 2.3.1.

### A surface that is not normal

The hypothesis of Lemma 1.2.6 is necessary. The next surface is singular along a line, it is not normal, and its normalization is the plane. Its normalization behaves differently in characteristic 2.

**Example 1.2.7 (the Whitney umbrella).** Let $k$ be a field, let $F = x^2 - y^2z \in k[x, y, z]$, let $X = V(F) \subseteq \mathbb{A}^3_k$ with ring $A = k[x, y, z]/(F)$, and let $L = V(x, y) \subseteq X$.

1. The scheme $X$ is integral. Its regular locus is $X \setminus L$, and $X$ is not normal.
2. Let $\nu : \mathbb{A}^2_k = \operatorname{Spec} k[s, t] \to X$ be the morphism given by $x \mapsto st$, $y \mapsto s$, $z \mapsto t^2$. Then $\nu$ is the normalization of $X$. It is finite, and it is an isomorphism over $X \setminus L$.
3. Let $k$ be algebraically closed and let $c \in k$. If the characteristic of $k$ is not 2 and $c \ne 0$, then the fibre of $\nu$ over $(0, 0, c)$ has two points. If the characteristic is 2 or $c = 0$, it has one point.

Lean: `Singularity.whitneyNormalization_equation`, `Singularity.whitney_exists_eq_add_mul` (part 2, the map and $k[s, t] = A' + A' t$, not the normality)

*Proof.* 1. The polynomial $F$ is monic of degree 2 in $x$ over the factorial ring $k[y, z]$, and its coefficient of $x$ is 0. If $F = (x - r)(x - r')$, then $r' = -r$ and $r^2 = y^2z$. This is impossible, since $z$ is not a square in $k(y, z)$. Thus $F$ is irreducible and $X$ is integral. On $X \setminus L$ we have $y \ne 0$, because $y = 0$ and $F = 0$ give $x^2 = 0$. There $\partial F/\partial z = -y^2$ does not vanish, and the Jacobian criterion (Corollary 1.8.3 of Volume 1) shows that $X \setminus L$ is regular. Let $\mathfrak{q}$ be a prime of $P = k[x, y, z]$ that contains $(x, y)$. Then $P_\mathfrak{q}$ is a regular local ring of some dimension $d$, and $F \in (x, y)^2 \subseteq \mathfrak{q}^2$. The ring $P_\mathfrak{q}/(F)$ has dimension $d - 1$ [AM69, Corollary 11.18], and its maximal ideal $\mathfrak{n}$ has $\mathfrak{n}/\mathfrak{n}^2 \cong \mathfrak{q}P_\mathfrak{q}/\mathfrak{q}^2P_\mathfrak{q}$, of dimension $d$. Thus $A_\mathfrak{q}$ is not regular, and the regular locus is $X \setminus L$. Part 2 shows that $X$ is not normal.

2. The map $\varphi : A \to C = k[s, t]$ is well defined, since $(st)^2 - s^2t^2 = 0$. Its image $A' = k[s, st, t^2]$ contains $s$ and $t^2$, so $C = A' + A't$ is a finite $A'$-module. The kernel of $\varphi$ is a prime $\mathfrak{p}$, since $C$ is a domain. The extension $A/\mathfrak{p} \cong A' \subseteq C$ is integral, so $\dim A/\mathfrak{p} = \dim C = 2$ by the proof of Theorem 1.2.2. Also $\dim A = 2$ [Har, Theorem I.1.8A], and $\operatorname{ht} \mathfrak{p} + \dim A/\mathfrak{p} = \dim A$ by the same theorem. Thus $\mathfrak{p} = 0$, and $\varphi$ is injective. The field of fractions of $C$ is $k(s, t)$, and $s = \varphi(y)$ and $t = \varphi(x)/\varphi(y)$. Thus $A \subseteq C$ have the same field of fractions. The ring $C$ is factorial, so it is integrally closed (Proposition 2.1.4 of Volume 1), and it is integral over $A$. Thus $C$ is the integral closure of $A$, and $\nu$ is the normalization. It is finite, since $C$ is a finite $A$-module. The subring $A'$ is spanned over $k$ by the monomials $s^{a+b}t^{b+2c}$ with $a, b, c \ge 0$. The monomial $t$ is not of this form, since $b + 2c = 1$ forces $b = 1$ and then $a + b \ge 1$. So $t \notin A$, and $A$ is not integrally closed. Over $X \setminus L = D(y)$, the ring $A_y$ contains $x/y$, which maps to $t$. Thus $A_y \to C_s$ is surjective, since $C_s$ is generated by $s$, $s^{-1}$ and $t$. It is injective, so it is an isomorphism.

3. The fibre over $Q = (0, 0, c)$ is $\operatorname{Spec} C/(st, s, t^2 - c)C = \operatorname{Spec} k[t]/(t^2 - c)$. If the characteristic is not 2 and $c \ne 0$, then $t^2 - c$ has two distinct roots in $k$. If $c = 0$, it is $t^2$. If the characteristic is 2, then $t^2 - c = (t - \gamma)^2$ with $\gamma^2 = c$. In the last two cases the fibre has one point. $\square$

In characteristic 2 the normalization $\nu$ is a bijection on the points, and it is finite, but it is not an isomorphism. The fibre over each closed point of $L$ is a double point, and the fibre over the generic point of $L$ is the purely inseparable extension $k(t)$ of $k(z)$, with $z = t^2$. So the surface $X$ is the image of the plane under a map that is injective on points, and $X$ is singular along a curve. The characteristic changes the geometry of the normalization here, but it does not change the process. In each characteristic the process of Chapter 2 ends with the normalization, since $\mathbb{A}^2_k$ is regular.

### Notes and references

Serre's criterion is [Mat, Theorem 23.8]. The finiteness of the normalization of an excellent ring is in [EGA4-7, Section 7.8] and in [Stacks]. For a surface over a field, Theorem 1.2.4 and Corollary 1.2.5 are in [Liu, Chapter 8] and in [Stacks]. The proof of Theorem 1.2.4 shows that a normal Noetherian scheme is regular in codimension 1, so its singular locus has codimension at least 2. For surfaces this means that the singular locus is a finite set of closed points.
