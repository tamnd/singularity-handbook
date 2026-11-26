---
title: Embedded resolution and history
nodes: [SG0000000T, SG0000000V, SG0000001C]
sources: [CJS20, Zar39, Zar40, Zar44, Abh56s, Abh56, Abh66, CGO, Lip78, Hir64, Hir67b, Benn70, BenV13, HP24, Cut04, Kol07, CP19, Har, Stacks, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Embedded resolution and history

The process of Lipman changes the surface. It does not keep an embedding of the surface in a regular ambient scheme, and the normalization step has no analogue for the ambient scheme. In many applications one needs more: a sequence of blowups of the ambient scheme after which the strict transform of the surface is regular and meets the exceptional divisor well. This is the embedded problem. In this section we state the embedded theorem for surfaces, and we give the history of the resolution of surfaces. We do not prove the theorem for surfaces. We prove the claims of the examples, which compute embedded resolutions in charts. For a curve on a smooth surface over an algebraically closed field we prove the embedded resolution in full, by blowups of points, in Theorem 3.1.8.

### The definitions

**Definition 3.1.1.** Let $Z$ be a Noetherian scheme, let $X \subseteq Z$ be a closed subscheme, and let $C \subseteq X$ be a closed subscheme with ideal $\mathcal{I}_C$ in $\mathcal{O}_X$. The center $C$ is *permissible* for $X$ if $C$ is regular and $X$ is normally flat along $C$, that is, each sheaf $\mathcal{I}_C^n/\mathcal{I}_C^{n+1}$ is a flat $\mathcal{O}_C$-module.

Node: SG0000000T · Lean: `Singularity.IsPermissible`

The theorem of Bennett [Benn70] says that the Hilbert-Samuel function of $X$ does not go up under the blowup in a permissible center. The Hilbert-Samuel function is in Chapter 3 of Volume 1. A closed point is a permissible center, because each module over a field is flat. This fact has a Lean proof, `Singularity.isPermissible_vanishingIdeal_singleton`.

**Definition 3.1.2.** Let $Z$ be a regular Noetherian scheme. An effective Cartier divisor $D = \sum_i D_i$ on $Z$, with irreducible components $D_i$, has *simple normal crossings* if each $D_i$ is regular and, at each point $z \in Z$, the components that contain $z$ have local equations $t_1, \dots, t_r$ that are part of a regular system of parameters of $\mathcal{O}_{Z,z}$. A regular closed subscheme $X \subseteq Z$ has *normal crossings with* $D$ if, at each point $z \in X$, there is a regular system of parameters of $\mathcal{O}_{Z,z}$ such that $X$ is defined by some of its members and each component of $D$ through $z$ is defined by another of its members.

Node: SG0000000V · Lean: `Singularity.IsSncDivisor`

**Definition 3.1.3.** Let $Z$ be a regular excellent scheme and let $X \subseteq Z$ be a reduced closed subscheme. An *embedded resolution* of $X$ is a sequence of blowups $Z_n \to Z_{n-1} \to \dots \to Z_0 = Z$, each in a permissible center for the strict transform $X_i$ of $X$, such that $X_n$ is regular, the union $E_n$ of the exceptional divisors is a divisor with simple normal crossings on $Z_n$, and $X_n$ has normal crossings with $E_n$.

Lean: `Singularity.IsEmbeddedResolution` (a form of the result without the sequence of blowups, see "The Lean statement" below)

The conditions vary a little between authors. Some ask that each center lies over the singular locus of $X$, or over the locus where the condition of normal crossings fails. Some ask that the sequence be canonical, that is, compatible with the regular morphisms and the automorphisms of the pair $(Z, X)$.

### The theorem

**Theorem 3.1.4 (Cossart-Jannsen-Saito).** Let $Z$ be a regular excellent scheme and let $X \subseteq Z$ be a reduced closed subscheme of dimension at most 2. There is a canonical sequence of blowups in permissible centers after which the strict transform of $X$ is regular and has normal crossings with the exceptional divisor.

Node: SG0000001C · Lean: `Singularity.EmbeddedResolutionSurface` (the statement only)

This is the main theorem of [CJS20]. The same work gives a canonical non-embedded resolution of each reduced excellent scheme of dimension at most 2. The proof uses the Hilbert-Samuel function, the directrix and the characteristic polyhedron of Hironaka. It does not use the characteristic, and it includes the case of mixed characteristic.

The theorem gives again a resolution as in Theorem 2.2.1, for the schemes that embed in a regular excellent scheme. Each variety over a field embeds locally in an affine space, so the theorem applies locally. The non-embedded theorem of [CJS20] does not need an embedding, and it gives a resolution of each reduced excellent scheme of dimension at most 2.

### The Lean statement

The Lean library states Theorem 3.1.4 in a weaker form. Mathlib has no excellent schemes and no blowups of schemes, so the Lean statement changes two things.

1. The scheme $Z$ is regular and of finite type over a field $k$. The field can be imperfect. Such a scheme is excellent, so this is a special case of Theorem 3.1.4.
2. The Lean statement does not ask for a sequence of blowups. It asks for the result: a proper morphism $\pi \colon Z' \to Z$ with $Z'$ regular, an open set $U \subseteq Z$ whose complement consists of points of $X$ where $X$ is not regular, and an ideal sheaf $E$ on $Z'$. The morphism $\pi$ is an isomorphism over $U$, the support of $E$ is $\pi^{-1}(Z \setminus U)$, $E$ has simple normal crossings, and the strict transform of $X$ has normal crossings with $E$.

The local conditions are stated at the stalks. A divisor with simple normal crossings is an ideal sheaf whose stalk at each point is generated by the product of some members of a regular system of parameters [Stacks, Tag 0BI9]. On a regular Noetherian scheme this is the same as Definition 3.1.2. The strict transform is the reduced closed subscheme on the closure of $\pi^{-1}(X \cap U)$. Each generic point of $Z'$ has a field as local ring, so it is not in the support of $E$. Thus $\pi^{-1}(U)$ is dense in $Z'$.

The Lean library proves two facts of this section. A closed point of $X$ is a permissible center (`Singularity.isPermissible_vanishingIdeal_singleton`). A regular closed subscheme of codimension 1 of a regular scheme is a divisor with simple normal crossings (`Singularity.isSncDivisor_of_codim_one`), because its ideal at each point is generated by one member of a regular system of parameters (Theorem 1.1.11 and [Stacks]). The Lean library does not prove Theorem 3.1.4.

### Examples

**Example 3.1.5.** Let $k$ be a field of any characteristic, let $Z = \mathbb{A}^3_k$ and let $X = V(xy - z^2)$. The blowup $Z' \to Z$ at the origin is an embedded resolution of $X$. The exceptional divisor $E \cong \mathbb{P}^2_k$ has one component, and it is regular.

Lean: none yet

*Proof.* A closed point is a permissible center. By Proposition 2.3.2, the strict transform $X'$ is regular. In the $x$-chart $\operatorname{Spec} k[x, y_1, z_1]$ we have $E = V(x)$ and $X' = V(y_1 - z_1^2)$. With $y_2 = y_1 - z_1^2$ we get $k[x, y_1, z_1] = k[x, y_2, z_1]$, so $x$ and $y_2$ are coordinates. Let $R$ be the local ring of $Z'$ at a point of $V(x, y_2)$. Then $R/(x)$ and $R/(x, y_2)$ are local rings of $k[y_2, z_1]$ and of $k[z_1]$, so they are regular. By Proposition 1.2.8 of Volume 1, applied twice, $\dim R/(x, y_2) = \dim R - 2$. Thus $x$ and $y_2$, together with a regular system of parameters of $R/(x, y_2)$, give a regular system of parameters of $R$. The $y$-chart is the same. In the $z$-chart $\operatorname{Spec} k[x_1, y_1, z]$ we have $E = V(z)$ and $X' = V(x_1 y_1 - 1)$. On the open set $D(x_1)$, which contains $X'$, put $u = x_1 y_1 - 1$. Then $k[x_1, x_1^{-1}, y_1, z] = k[x_1, x_1^{-1}, u, z]$, and $u$ and $z$ are coordinates in the same way. Thus $X'$ has normal crossings with $E$. $\square$

In Example 2.3.6 the embedded process can not use the normalization. After the blowup of the origin of $\mathbb{A}^3_k$, the strict transform $V(z_1^2 - x^2 h(y_1))$ in the $x$-chart is singular along the line $L = V(x, z_1)$. Blow up the ambient chart along the regular curve $L$, and take the chart with $z_1 = x z_2$. Then $z_1^2 - x^2 h = x^2 (z_2^2 - h)$, and the strict transform is $V(z_2^2 - h(y_1))$. This is the chart $\operatorname{Spec} C$ of the normalization in Example 2.3.6. Thus a blowup in a regular curve does the work of the normalization here.

The next example shows that the embedded problem needs centers of dimension 1. Blowups of points alone can not resolve a surface that is singular along a curve.

**Example 3.1.6.** Let $k$ be a field of any characteristic, let $Z = \mathbb{A}^3_k$, let $X = V(F)$ with $F = x^2 - y^2z$ be the Whitney umbrella of Example 1.2.7, and let $L = V(x, y)$.

1. The line $L$ is a permissible center for $X$.
2. Let $Z' \to Z$ be the blowup along $L$, with exceptional divisor $E$. The strict transform $X'$ of $X$ is regular, $E$ is a regular irreducible divisor, and $X'$ has normal crossings with $E$. Thus $Z' \to Z$ is an embedded resolution of $X$ in one step. The morphism $X' \to X$ is the normalization $\nu$ of Example 1.2.7.
3. Let $Z_1 \to Z$ be the blowup at the origin. In the $z$-chart the strict transform of $X$ is $V(x_1^2 - y_1^2z)$, so it is isomorphic to $X$. Each finite sequence of blowups of closed points leaves a strict transform of $X$ that is not regular.

Lean: none yet

*Proof.* 1. Let $P = k[z][x, y]$, let $A = P/(F)$ and let $I = (x, y)A$, the ideal of $L$ in $A$. Let $P_n$ be the free $k[z]$-module spanned by the monomials of degree $n$ in $x$ and $y$, with $P_n = 0$ for $n < 0$. The polynomial $F$ lies in $P_2$, so the ideal $(F) = \bigoplus_n FP_{n-2}$ is homogeneous. We have $(x, y)^n = \bigoplus_{m \ge n} P_m$ and $I^n = ((x, y)^n + (F))/(F)$. Thus $I^n/I^{n+1} \cong P_n/FP_{n-2}$. In this quotient, $x^iy^{n-i} = x^{i-2}y^{n-i+2}z$ for $i \ge 2$. By induction on $i$, the quotient is spanned by $y^n$ and $xy^{n-1}$ for $n \ge 1$. These two elements are independent over $k[z]$. Indeed, $F$ is monic of degree 2 in $x$, so each nonzero element of $FP_{n-2}$ has degree at least 2 in $x$, and $ay^n + bxy^{n-1}$ has degree at most 1 in $x$. Thus each $I^n/I^{n+1}$ is a free module over $A/I = k[z]$, and it is flat. The line $L \cong \mathbb{A}^1_k$ is regular. So $L$ is permissible.

2. The ideal $(x, y)$ of $P$ gives two charts by Lemma 1.1.3. The first chart is $\operatorname{Spec} k[x_2, y, z]$ with $x = yx_2$. It is a polynomial ring by the argument of Lemma 1.1.6. There $F = y^2(x_2^2 - z)$ and $E = V(y)$. As in the proof of Lemma 1.1.6, the strict transform is $V(x_2^2 - z)$. Let $u = z - x_2^2$. Then $k[x_2, y, z] = k[x_2, y, u]$, $X' = V(u)$ and $E = V(y)$. As in the proof of Example 3.1.5, $u$ and $y$ are part of a regular system of parameters at each point of $V(u, y)$. So $X'$ is regular and has normal crossings with $E$ in this chart. The second chart is $\operatorname{Spec} k[x, y_3, z]$ with $y = xy_3$. There $F = x^2(1 - y_3^2z)$, the strict transform is $V(1 - y_3^2z)$, and $E = V(x)$. On the strict transform $y_3$ is a unit. So by $(\ast)$ in Section 1.1, each point of $X'$ in the second chart lies in the first chart. Thus $X' = V(u) \cong \operatorname{Spec} k[x_2, y]$, and it is regular. The divisor $E$ is $\operatorname{Spec} k[x_2, z]$ and $\operatorname{Spec} k[y_3, z]$ in the two charts. These are regular and irreducible, and they meet in a nonempty open set, so $E$ is regular and irreducible. Its local equation is $y$ or $x$, a coordinate of a polynomial ring. By the same argument, it is part of a regular system of parameters at each point of $E$, so $E$ has simple normal crossings. With part 1, the blowup is an embedded resolution. The morphism $X' \to X$ is $(x_2, y) \mapsto (yx_2, y, x_2^2)$. This is $\nu$ with $s = y$ and $t = x_2$.

3. In the $z$-chart, $x = zx_1$ and $y = zy_1$, and $F = z^2x_1^2 - z^3y_1^2 = z^2(x_1^2 - y_1^2z)$. By Lemma 1.1.6, with the roles of the variables exchanged, the strict transform is $V(x_1^2 - y_1^2z)$. This is the same equation as $F$. Now let $Z_m \to \dots \to Z_1 \to Z_0 = Z$ be blowups of closed points, and let $X_i$ be the strict transform of $X$ in $Z_i$. Each morphism $Z_i \to Z$ is of finite type, so it maps closed points to closed points. By Theorem 1.1.2, part 2, the composite $Z_m \to Z$ is an isomorphism over $Z \setminus S$ for a finite set $S$ of closed points. The strict transform agrees with the inverse image over an open set where the blowup is an isomorphism. Thus $X_m$ contains an open subscheme isomorphic to $X \setminus S$. Let $\eta$ be the generic point of $L$. It is not in $S$, and $\mathcal{O}_{X,\eta}$ is not regular by Example 1.2.7. Thus $X_m$ is not regular. $\square$

The blowup in part 2 is an isomorphism over $Z \setminus L$. Over $L$ it has the fibre $\mathbb{P}^1$, and the curve $X' \cap E = V(y, z - x_2^2)$ maps onto $L$ with degree 2. This is the map $t \mapsto t^2$ of the normalization on the line $s = 0$. In part 3, the blowup of the origin also creates a new singular point. In the $y$-chart, $x = yx_1$ and $z = yz_1$, and the strict transform is $V(x_1^2 - yz_1)$, a cone with a singular point at its origin.

### Curves on a smooth surface

For a curve on a smooth surface the embedded problem has a short and complete proof by blowups of points. We give it here. It is the model for the embedded problem in higher dimension: an invariant goes down at each blowup, and a second process makes the total transform a divisor with simple normal crossings. In this subsection $k$ is an algebraically closed field of any characteristic, and $S$ is a smooth surface over $k$, that is, a regular integral separated scheme of finite type over $k$ of dimension 2. A *curve* $C \subseteq S$ is a reduced closed subscheme whose irreducible components have dimension 1.

Let $P \in C$ be a closed point. Let $R = \mathcal{O}_{S,P}$, with maximal ideal $\mathfrak{m}$, and let $f \in R$ be a local equation of $C$. The *multiplicity* of $C$ at $P$ is the largest $m$ with $f \in \mathfrak{m}^m$. Let $\mathcal{O} = \mathcal{O}_{C,P} = R/(f)$ and let $\tilde{\mathcal{O}}$ be its normalization, the integral closure in its total ring of fractions. It is finite over $\mathcal{O}$, by Theorem 1.2.2, part 1, applied to an affine open neighbourhood of $P$ in $C$, since the integral closure commutes with localization. The *delta invariant* is $\delta_P(C) = \ell_{\mathcal{O}}(\tilde{\mathcal{O}}/\mathcal{O})$. It is 0 if and only if $\mathcal{O}$ is normal. A normal local ring is a domain, and a normal local domain of dimension 1 is regular (Theorem 1.4.2 of Volume 1). Thus $\delta_P(C) = 0$ if and only if $C$ is regular at $P$. This holds if and only if $m = 1$. Indeed, if $f \notin \mathfrak{m}^2$, then $\mathcal{O}$ is regular by Proposition 1.2.6 of Volume 1. If $f \in \mathfrak{m}^2$, then the maximal ideal of $\mathcal{O}$ needs two generators, and $\mathcal{O}$ has dimension 1, so it is not regular. The curve $C$ has finitely many singular points, since $C$ is reduced and excellent, so its regular locus is open and contains the generic points. Let $\delta(C) = \sum_P \delta_P(C)$.

Let $u, v$ be a regular system of parameters of $R$. Since $\mathfrak{m}^m$ is generated by the monomials of degree $m$ in $u, v$, we can write $f = \sum_{i + j = m} a_{ij} u^i v^j$ with $a_{ij} \in R$. The *initial form* of $f$ is $f_m = \sum \bar a_{ij} X_0^i X_1^j$, a nonzero form of degree $m$ over $k$, by Proposition 1.10.1 of Volume 1. Since $k$ is infinite, after a linear change of $u, v$ we may assume that $\bar a_{0m} \ne 0$, that is, $f_m(0, 1) \ne 0$. We call such $u$ *transversal* to $C$.

**Lemma 3.1.7.** Let $C \subseteq S$, $P$, $m$, $R$, $f$ be as above, with $u, v$ a regular system of parameters of $R$ and $u$ transversal to $C$. Let $\pi : S' \to S$ be the blowup at $P$, with exceptional curve $E \cong \mathbb{P}^1_k$, and let $C'$ be the strict transform of $C$.

1. The points of $C'$ over $P$ lie in the chart $\operatorname{Spec} B$, $B = R[v/u]$. Let $t = v/u$ and $f' = f/u^m = \sum a_{ij} t^j$. Then $C' \cap \operatorname{Spec} B = \operatorname{Spec} \mathcal{O}'$ with $\mathcal{O}' = B/(f')$, and $\pi^* C = C' + mE$ near $E$.
2. The ring $\mathcal{O}'$ is generated as an $\mathcal{O}$-module by $1, t, \dots, t^{m-1}$, and $\mathcal{O} \subseteq \mathcal{O}' \subseteq \tilde{\mathcal{O}}$.
3. $\ell(\mathcal{O}'/u\mathcal{O}') = m$ and $\ell_{\mathcal{O}}(\mathcal{O}'/\mathcal{O}) = m(m-1)/2$.
4. For each point $Q$ of $C'$ over $P$, the multiplicity of $C'$ at $Q$ is at most $m$.
5. $\delta_P(C) = m(m-1)/2 + \sum_{Q} \delta_Q(C')$, where $Q$ runs over the points of $C'$ over $P$.

Lean: none yet

*Proof.* 1. By Theorem 1.1.7 we may work over $\operatorname{Spec} R$, with the two charts $B = R[v/u] \cong R[T]/(uT - v)$ and $B'' = R[u/v]$. In $B$ we have $v^j = u^j t^j$, so $f = u^m f'$. The ideal of $E$ is $uB$, and $B/uB = k[T]$. The image of $f'$ in $k[T]$ is $f_m(1, T)$, which is not 0, so $u \nmid f'$, and the strict transform is $V(f')$ in this chart, as in Lemma 1.1.6. The only point of $E$ outside $\operatorname{Spec} B$ is the point $u/v = 0$ of $\operatorname{Spec} B''$. There $f/v^m = \sum a_{ij} (u/v)^i$, and its image at this point is $\bar a_{0m} \ne 0$. So this point is not on $C'$. Near $E$ the total transform is $V(f) = V(u^m f')$, which gives $\pi^* C = C' + mE$.

2. In $B/(f')$ we have $a_{0m} t^m = -\sum_{j < m} a_{m-j,j} t^j$, and $a_{0m}$ is a unit of $R$. Thus each power of $t$ is an $R$-linear combination of $1, \dots, t^{m-1}$, and $\mathcal{O}' = B/(f')$ is generated by them as an $R$-module. The element $f = u^m f'$ kills $\mathcal{O}'$, so this is an $\mathcal{O}$-module. The element $u$ is a nonzerodivisor on $\mathcal{O}'$. Indeed, $B$ is a domain and $u$ is a prime element of $B$, since $B/uB = k[T]$ is a domain. Let $g, h \in B$ with $u g = f' h$. Since $u \nmid f'$, we get $u \mid h$, say $h = u h'$, and then $g = f' h'$. So $u g \in (f')$ implies $g \in (f')$. Thus $\mathcal{O}' \subseteq \mathcal{O}'_u = R_u/(f) = \mathcal{O}_u$. The element $u$ is a nonzerodivisor on $\mathcal{O}$ too, since $u \nmid f$ in the factorial ring $R$ and $u$ is prime. So $\mathcal{O} \to \mathcal{O}_u$ is injective, and we get $\mathcal{O} \subseteq \mathcal{O}' \subseteq \mathcal{O}_u$, inside the total ring of fractions of $\mathcal{O}$. The ring $\mathcal{O}'$ is finite over $\mathcal{O}$, so it is integral over $\mathcal{O}$, and $\mathcal{O}' \subseteq \tilde{\mathcal{O}}$.

3. We have $\mathcal{O}'/u\mathcal{O}' = B/(u, f') = k[T]/(f_m(1, T))$. The polynomial $f_m(1, T)$ has degree exactly $m$, since its leading coefficient is $\bar a_{0m} \ne 0$. Thus $\mathcal{O}'/u\mathcal{O}'$ has dimension $m$ over $k$. It is killed by $u$ and $v = ut$, so it is killed by $\mathfrak{m}$, and its length is $m$. Next, $u^{m-1} \mathcal{O}'$ is generated by the elements $u^{m-1} t^j = u^{m-1-j} v^j$ for $0 \le j \le m - 1$. These generate the ideal $\mathfrak{m}^{m-1}\mathcal{O}$. Since $u$ is a nonzerodivisor on $\mathcal{O}'$, each quotient $u^i \mathcal{O}'/u^{i+1} \mathcal{O}'$ is isomorphic to $\mathcal{O}'/u\mathcal{O}'$. Thus $\ell(\mathcal{O}'/\mathfrak{m}^{m-1}\mathcal{O}) = (m - 1) m$. Since $f \in \mathfrak{m}^m$, we have $\mathcal{O}/\mathfrak{m}^{m-1}\mathcal{O} = R/\mathfrak{m}^{m-1}$, and its length is $1 + 2 + \dots + (m-1) = m(m-1)/2$, by Proposition 1.10.1 of Volume 1. Thus $\ell(\mathcal{O}'/\mathcal{O}) = m(m-1) - m(m-1)/2 = m(m-1)/2$.

4. Let $Q$ be a point of $C'$ over $P$ and let $\mu$ be the multiplicity of $C'$ at $Q$. The ring $\mathcal{O}_{S',Q}/(u)$ is the local ring of $E \cong \mathbb{P}^1_k$ at $Q$, a discrete valuation ring. The image of $f' \in \mathfrak{m}_Q^\mu$ in it has order at least $\mu$. Thus $\mu \le \ell(\mathcal{O}_{S',Q}/(u, f'))$. By part 3, the sum of these lengths over all $Q$ is $m$.

5. By part 2, $\tilde{\mathcal{O}}$ is also the normalization of $\mathcal{O}'$. The ring $\mathcal{O}'$ is finite over $\mathcal{O}$, so it is semilocal, and its maximal ideals are the points $Q$. Thus $\tilde{\mathcal{O}}/\mathcal{O}' = \bigoplus_Q (\tilde{\mathcal{O}}/\mathcal{O}')_Q$, and the summand at $Q$ has length $\delta_Q(C')$. All residue fields are $k$, so lengths over $\mathcal{O}$ and over $\mathcal{O}'$ agree. Part 3 and $\ell(\tilde{\mathcal{O}}/\mathcal{O}) = \ell(\tilde{\mathcal{O}}/\mathcal{O}') + \ell(\mathcal{O}'/\mathcal{O})$ give the claim. $\square$

Part 3 also says that $C' \cdot E = m$ in the sense of Lemma 2.3.9, part 2. For $m = 1$ the curve $C'$ meets $E$ in one point, transversally, and it is isomorphic to $C$ near $P$.

**Theorem 3.1.8.** Let $k$ be an algebraically closed field, let $S$ be a smooth surface over $k$, and let $C \subseteq S$ be a curve. There is a finite sequence of blowups of closed points $S_n \to S_{n-1} \to \dots \to S_0 = S$ with the following properties.

1. After at most $\delta(C)$ blowups the strict transform of $C$ is regular.
2. In $S_n$, the reduced total transform $D_n$, which is the union of the strict transform $C_n$ of $C$ and the strict transforms of all exceptional curves, is a divisor with simple normal crossings in the sense of Definition 3.1.2.

Lean: none yet

*Proof.* *Step 1: the strict transform.* If $C$ is not regular, blow up a singular point $P$ of $C$, with multiplicity $m \ge 2$. By Lemma 3.1.7, part 5, the number $\delta$ of the strict transform is $\delta(C) - m(m-1)/2 \le \delta(C) - 1$. The blowup is an isomorphism away from $P$, so the other points do not change. Repeat. After at most $\delta(C)$ steps, $\delta = 0$, and the strict transform is regular.

*Step 2: the components are regular.* Let $D$ be the reduced total transform after Step 1. Its components are the components of the strict transform $C_r$ and the strict transforms of the exceptional curves. Each exceptional curve is a projective line when it appears (Theorem 1.1.7). By the remark after Lemma 2.3.9, a later blowup of a point does not change a regular curve up to isomorphism. Thus all components of $D$ are regular, and they stay regular under further blowups of points. A new exceptional curve is also regular.

*Step 3: the tangencies.* Let $Q$ be a point of the regular surface $S_r$. Let $D_1, D_2$ be two components of $D$ through $Q$, with local equations $a, b$ at $Q$, and let $\ell_Q = \ell(\mathcal{O}_{S_r,Q}/(a, b))$. Then $\ell_Q = 1$ if and only if $a, b$ is a regular system of parameters. Let $\tau$ be the sum of $\ell_Q - 1$ over all pairs of components and all their common points. Assume $\tau > 0$, and let $Q$ and $D_1, D_2$ have $\ell_Q \ge 2$. Choose a regular system of parameters $u, v$ at $Q$ with $a = v$. Since $\ell_Q \ge 2$, the element $b$ lies in $(v) + \mathfrak{m}_Q^2$. Write $b = cv + q$ with $q \in \mathfrak{m}_Q^2$. Since $b \notin \mathfrak{m}_Q^2$, the element $c$ is a unit. Thus $u$ is transversal to both curves, and by Lemma 3.1.7 for $m = 1$ both strict transforms meet $E$ only in the chart $B = R[v/u]$, at the point $t = 0$, where $t = v/u$. There the strict transforms are $V(t)$ and $V(b/u)$. We have $B/(t) \cong R/(v)$, a discrete valuation ring with uniformizer $u$, and the image of $b$ in it has order $\ell_Q$. So the image of $b/u$ has order $\ell_Q - 1$. Thus the new contact is $\ell_Q - 1$.

The other pairs behave as follows. Two components through $Q$ with distinct tangent lines meet $E$ in distinct points, by Lemma 3.1.7, part 1, for $m = 1$. So they are separated over $Q$. Two components through $Q$ with the same tangent line lose 1 from their contact, by the computation above. Each component through $Q$ meets $E$ in one point, transversally. The pairs that do not pass through $Q$ do not change. Thus $\tau$ goes down by at least 1. After finitely many blowups, $\tau = 0$, and any two components meet transversally.

*Step 4: the triple points.* Assume $\tau = 0$, and let $Q$ be a point on $r \ge 3$ components. They meet pairwise transversally, so their tangent lines at $Q$ are pairwise distinct. After the blowup at $Q$ they meet $E$ in $r$ distinct points, each transversally, and they are disjoint over $Q$. So $\tau$ stays 0, no new point on three components appears, and the number of points on at least three components goes down by 1. After finitely many blowups, each point lies on at most two components, and two components through a point have local equations that form a regular system of parameters. This is the condition of Definition 3.1.2. $\square$

The first part of the theorem is in [Har, Section V.3], where the invariant is the arithmetic genus of a projective curve. The second part is the embedded resolution of a curve on a surface, also in [Har, Section V.3]. The proof works in every characteristic. The definitions of $\delta$ and $\tau$ do not use the characteristic, and no step uses a derivative.

**Corollary 3.1.9.** Let $C \subseteq S$ and $P$ be as above. Run Step 1 of the proof only at $P$ and at the points over $P$. Then $\delta_P(C) = \sum_Q m_Q(m_Q - 1)/2$, where $Q$ runs over the centers of the blowups, and $m_Q$ is the multiplicity of the strict transform of $C$ at $Q$.

Lean: none yet

*Proof.* Use induction on the number of blowups and Lemma 3.1.7, part 5. At the end the strict transform is regular over $P$, so the remaining $\delta$ is 0. $\square$

The cusp of Section 1.1 is the simplest case. There $m = 2$ and $\delta = 1$, one blowup makes the curve regular, and two more blowups give simple normal crossings.

**Example 3.1.10.** Let $k$ be an algebraically closed field of any characteristic. Let $C_1 = V(y^2 - x^3)$ and $C_2 = V(y^2 - x^5)$, and let $C = C_1 \cup C_2 = V(f)$ with $f = (y^2 - x^3)(y^2 - x^5)$. Let $S = \mathbb{A}^2_k \setminus V(1 - x^2)$.

1. In $S$ the curve $C$ is regular outside the origin, and $C_1 \cap C_2$ is the origin. At the origin $m = 4$ and $\delta = 9$.
2. Two blowups make the strict transform regular. Three more blowups give simple normal crossings. Thus the process of the proof of Theorem 3.1.8 uses five blowups, and each of them is at a point where the conditions fail.
3. In the end the exceptional curves $E_1, \dots, E_5$ (numbered by the order of the blowups) form the chain $E_1, E_4, E_2, E_5, E_3$, with self-intersections $-3, -1, -4, -1, -2$. The curve $C_1$ meets $E_4$, the curve $C_2$ meets $E_5$, and both transversally.
4. The orders of $f$ along $E_1, \dots, E_5$ are $4, 7, 8, 12, 16$.

Lean: none yet

*Proof.* 1. A common point of $C_1$ and $C_2$ has $x^3 = x^5$, so $x = 0$ or $x^2 = 1$, and in $S$ only $x = 0$, $y = 0$ is left. The curve $C_1$ is singular only at the origin: the derivatives $2y$ and $-3x^2$ vanish together on $C_1$ only there in each characteristic. Indeed, in characteristic 2 the derivative $-3x^2 = x^2$ gives $x = 0$ and then $y^2 = 0$. In characteristic 3 the derivative $2y$ gives $y = 0$ and then $x^3 = 0$. In the other characteristics both derivatives give $x = y = 0$. The same argument works for $C_2$, with $-5x^4$ in place of $-3x^2$. The lowest form of $f$ is $y^4$, so $m = 4$. The value $\delta = 9$ follows from part 2 and Corollary 3.1.9.

2. *First blowup.* The coordinate $u = x$ is transversal, since $f_4 = y^4$. In the chart $y = x y_1$ we get

$$f = (x^2 y_1^2 - x^3)(x^2 y_1^2 - x^5) = x^4 (y_1^2 - x)(y_1^2 - x^3).$$

Thus $C' = V((y_1^2 - x)(y_1^2 - x^3))$, the exceptional curve $E_1$ is $V(x)$, and $C'$ meets $E_1$ only at the origin, since $f_4(1, y_1) = y_1^4$. At the origin the multiplicity of $C'$ is $1 + 2 = 3$. The first factor is the strict transform of $C_1$, and it is regular. The second factor is the strict transform of $C_2$. It is a cusp.

*Second blowup.* Blow up the origin of this chart. In the chart $y_1 = x y_2$,

$$(x^2 y_2^2 - x)(x^2 y_2^2 - x^3) = x^3 (x y_2^2 - 1)(y_2^2 - x).$$

The new exceptional curve $E_2$ is $V(x)$, and near the origin the strict transform is $C_2'' = V(y_2^2 - x)$, since $x y_2^2 - 1$ is a unit there. In the chart $x = y_1 x_2$,

$$(y_1^2 - y_1 x_2)(y_1^2 - y_1^3 x_2^3) = y_1^3 (y_1 - x_2)(1 - y_1 x_2^3).$$

Here $E_2 = V(y_1)$, the strict transform of $E_1$ is $V(x_2)$, and near the origin the strict transform of $C_1$ is $C_1'' = V(y_1 - x_2)$. Both $C_1''$ and $C_2''$ are regular, so the strict transform of $C$ is regular. This used $6 + 3 = 9$ for the sum of $m(m-1)/2$, which gives $\delta = 9$ by Corollary 3.1.9.

*The configuration after two blowups.* There are two bad points. At the origin $P$ of the chart $x = y_1 x_2$, the three curves $C_1''$, $E_1$ and $E_2$ pass, pairwise transversally. At the origin $Q$ of the chart $y_1 = x y_2$, the curve $C_2'' = V(y_2^2 - x)$ is tangent to $E_2 = V(x)$, with contact $\ell(k[x, y_2]_{(x, y_2)}/(x, y_2^2)) = 2$.

*Third blowup, at $Q$.* In the chart $x = y_2 x_3$ we get $y_2^2 - y_2 x_3 = y_2(y_2 - x_3)$. The curves $C_2''' = V(y_2 - x_3)$, $E_2 = V(x_3)$ and $E_3 = V(y_2)$ pass through the origin $R$ of this chart, pairwise transversally. This is the same as the cusp in Section 1.1.

*Fourth and fifth blowups.* Blow up $P$, with exceptional curve $E_4$, and blow up $R$, with exceptional curve $E_5$. By Step 4 of the proof of Theorem 3.1.8, the three curves through each of these points become disjoint over the point, and each meets the new exceptional curve transversally. Now each point lies on at most two components, and the components meet transversally. This proves part 2.

3. The curve $E_4$ meets $C_1$, $E_1$ and $E_2$, and $E_5$ meets $C_2$, $E_2$ and $E_3$. The curves $E_1$ and $E_2$ met only at $P$, and $E_2$ and $E_3$ met only at $R$, since each pair meets transversally in one point by Lemma 3.1.7 for $m = 1$. So after the last two blowups the only intersections of exceptional curves are those of $E_4$ and $E_5$ with their three neighbours. This is the chain $E_1, E_4, E_2, E_5, E_3$, with $C_1$ on $E_4$ and $C_2$ on $E_5$.

4. Let $E$ be the exceptional curve of the blowup at a point $Q$, and let $g$ be a function near $Q$ with $g \in \mathfrak{m}_Q^\mu \setminus \mathfrak{m}_Q^{\mu+1}$. Then $v_E(g) = \mu$, by the proof of Lemma 3.1.7, part 1, which does not use that $g$ is reduced. If the components of $\operatorname{div}(g)$ through $Q$ are regular, with orders $e_1, \dots, e_s$, then $\mu = e_1 + \dots + e_s$, since the multiplicity of a product is the sum of the multiplicities. This holds because the associated graded ring of $\mathcal{O}_{S,Q}$ is a polynomial ring, hence a domain (Proposition 1.10.1 of Volume 1). This gives $v_{E_1}(f) = 4$ and $v_{E_2}(f) = 4 + 3 = 7$, since the second center lies on $E_1$ and $C'$ has multiplicity 3 there. The point $Q$ lies on $E_2$ and $C_2''$, so $v_{E_3}(f) = 7 + 1 = 8$. The point $P$ lies on $E_1$, $E_2$ and $C_1''$, so $v_{E_4}(f) = 4 + 7 + 1 = 12$. The point $R$ lies on $E_2$, $E_3$ and $C_2'''$, so $v_{E_5}(f) = 7 + 8 + 1 = 16$.

Now the self-intersections follow from Lemma 2.3.9, part 3, applied to $g = f$ on $S_5$. The divisor is $\operatorname{div}(f) = C_1 + C_2 + 4E_1 + 7E_2 + 8E_3 + 12E_4 + 16E_5$, and adjacent curves meet transversally in one point. Thus

$$4 E_1^2 + 12 = 0, \quad 7 E_2^2 + 12 + 16 = 0, \quad 8 E_3^2 + 16 = 0, \quad 12 E_4^2 + 4 + 7 + 1 = 0, \quad 16 E_5^2 + 7 + 8 + 1 = 0.$$

This gives $E_1^2 = -3$, $E_2^2 = -4$, $E_3^2 = -2$ and $E_4^2 = E_5^2 = -1$. $\square$

The values agree with the count of the blowups. A blowup at a point of a regular curve $\Gamma \cong \mathbb{P}^1$ lowers $\Gamma \cdot \Gamma$ by 1 [Har, Section V.3]. We do not prove this here. The curve $E_1$ starts with $-1$ and its strict transform contains the second center and $P$, so it ends with $-3$. The curve $E_2$ contains $Q$, $P$ and $R$, so it ends with $-4$. The curve $E_3$ contains $R$, so it ends with $-2$. The value $\delta = 9$ also agrees with the classical formula $\delta = \delta(C_1) + \delta(C_2) + \ell(\mathcal{O}/(y^2 - x^3, y^2 - x^5)) = 1 + 2 + 6$, which we do not prove. The example works in every characteristic, because all the computations use only the multiplication of monomials.

### History

Zariski proved the resolution of algebraic surfaces in characteristic 0 [Zar39]. He then proved local uniformization in characteristic 0 [Zar40], and he used it for the resolution of threefolds in characteristic 0 [Zar44].

Abhyankar proved the resolution of surfaces over an algebraically closed field of characteristic $p > 0$ [Abh56s]. His proof goes through local uniformization along each valuation of the function field. The paper [Abh56] studies the valuations centered in a local domain, and it contains the inequality of Abhyankar. Later Abhyankar proved the embedded resolution of surfaces in a nonsingular threefold over an algebraically closed field of characteristic $p > 0$, and he used it for threefolds over an algebraically closed field of characteristic $p > 5$ [Abh66].

Hironaka [Hir64] proved resolution and embedded resolution in characteristic 0 in each dimension. Later he gave a proof of the resolution of excellent surfaces in each characteristic, with the characteristic polyhedron [Hir67b]. The volume [CGO] treats the resolution of excellent surfaces along these lines. Lipman [Lip78] proved Theorem 2.2.1 for each reduced excellent surface with no embedding. Cossart, Jannsen and Saito [CJS20] proved the canonical embedded version, Theorem 3.1.4.

Benito and Villamayor defined an invariant in characteristic $p$ by elimination, and they used it for the embedded resolution of two-dimensional schemes [BenV13]. Hauser and Perlega treat the embedded resolution of surfaces in a regular threefold in characteristic $p$ [HP24]. The book of Cutkosky [Cut04] gives the resolution of surfaces, and it gives the method of Abhyankar in a short form. The lectures of Kollár [Kol07] treat resolution in characteristic 0.

### What is open

For dimension 3, Cossart-Piltant [CP19] prove a non-embedded resolution of each reduced separated quasi-excellent Noetherian scheme of dimension at most 3. The embedded resolution of a threefold in a regular scheme of dimension 4 in characteristic $p$, by blowups in regular centers, is still open. The resolution of varieties of dimension 4 and higher in characteristic $p$ is open. Volume 9 explains the state of these problems. This volume shows the case of surfaces, where every characteristic is known.

### Notes and references

Normal flatness is in [Hir64] and in [CJS20]. The definitions of simple normal crossings vary a little. We follow the form that the project uses for its nodes. For the history of the resolution of surfaces see [Cut04], [Kol07] and the introduction of [CJS20]. For the blowup of a regular point and the surfaces over an algebraically closed field see [Har, Chapter V]. The embedded resolution of a curve on a smooth surface, Theorem 3.1.8, is in [Har, Section V.3], and its history is in [Cut04] and [Kol07]. Our proof uses the delta invariant in place of the arithmetic genus, so that it is local and needs no projective model. Lemma 3.1.7 is the local form of the formula for the change of the arithmetic genus under a blowup in [Har, Section V.3]. Corollary 3.1.9 is the classical formula for $\delta$ by the multiplicities of the infinitely near points.
