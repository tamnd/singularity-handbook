---
title: Embedded resolution and history
nodes: [SG0000000T, SG0000000V, SG0000001C]
sources: [CJS20, Zar39, Zar40, Zar44, Abh56s, Abh56, Abh66, CGO, Lip78, Hir64, Benn70, BenV13, HP24, Cut04, Kol07, CP19, Har, Stacks, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Embedded resolution and history

The process of Lipman changes the surface. It does not keep an embedding of the surface in a regular ambient scheme, and the normalization step has no analogue for the ambient scheme. In many applications one needs more: a sequence of blowups of the ambient scheme after which the strict transform of the surface is regular and meets the exceptional divisor well. This is the embedded problem. In this section we state the embedded theorem for surfaces, and we give the history of the resolution of surfaces. We prove nothing here.

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

The theorem gives the resolution of Theorem 2.2.1 again, for the schemes that embed in a regular excellent scheme. Each variety over a field embeds locally in an affine space, so the theorem applies locally. A canonical resolution glues, so for a variety the local resolutions give a global one.

### The Lean statement

The Lean library states Theorem 3.1.4 in a weaker form. Mathlib has no excellent schemes and no blowups of schemes, so the Lean statement changes two things.

1. The scheme $Z$ is regular and of finite type over a field $k$. The field can be imperfect. Such a scheme is excellent, so this is a special case of Theorem 3.1.4.
2. The Lean statement does not ask for a sequence of blowups. It asks for the result: a proper morphism $\pi \colon Z' \to Z$ with $Z'$ regular, an open set $U \subseteq Z$ whose complement consists of points of $X$ where $X$ is not regular, and an ideal sheaf $E$ on $Z'$. The morphism $\pi$ is an isomorphism over $U$, the support of $E$ is $\pi^{-1}(Z \setminus U)$, $E$ has simple normal crossings, and the strict transform of $X$ has normal crossings with $E$.

The local conditions are stated at the stalks. A divisor with simple normal crossings is an ideal sheaf whose stalk at each point is generated by the product of some members of a regular system of parameters [Stacks, Tag 0BI9]. On a regular Noetherian scheme this is the same as Definition 3.1.2. The strict transform is the reduced closed subscheme on the closure of $\pi^{-1}(X \cap U)$. Each generic point of $Z'$ has a field as local ring, so it is not in the support of $E$. Thus $\pi^{-1}(U)$ is dense in $Z'$.

The Lean library proves two facts of this section. A closed point of $X$ is a permissible center (`Singularity.isPermissible_vanishingIdeal_singleton`). A regular closed subscheme of codimension 1 of a regular scheme is a divisor with simple normal crossings (`Singularity.isSncDivisor_of_codim_one`), because its ideal at each point is generated by one member of a regular system of parameters [Mat, Theorem 14.2]. The Lean library does not prove Theorem 3.1.4.

### Two examples

**Example 3.1.5.** Let $k$ be a field of any characteristic, let $Z = \mathbb{A}^3_k$ and let $X = V(xy - z^2)$. The blowup $Z' \to Z$ at the origin is an embedded resolution of $X$. The exceptional divisor $E \cong \mathbb{P}^2_k$ has one component, and it is regular.

Lean: none yet

*Proof.* A closed point is a permissible center. By Proposition 2.3.2, the strict transform $X'$ is regular. In the $x$-chart $\operatorname{Spec} k[x, y_1, z_1]$ we have $E = V(x)$ and $X' = V(y_1 - z_1^2)$. With $y_2 = y_1 - z_1^2$ we get $k[x, y_1, z_1] = k[x, y_2, z_1]$, so $x$ and $y_2$ are coordinates. Let $R$ be the local ring of $Z'$ at a point of $V(x, y_2)$. Then $R/(x)$ and $R/(x, y_2)$ are local rings of $k[y_2, z_1]$ and of $k[z_1]$, so they are regular. By Proposition 1.2.8 of Volume 1, applied twice, $\dim R/(x, y_2) = \dim R - 2$. Thus $x$ and $y_2$, together with a regular system of parameters of $R/(x, y_2)$, give a regular system of parameters of $R$. The $y$-chart is the same. In the $z$-chart $\operatorname{Spec} k[x_1, y_1, z]$ we have $E = V(z)$ and $X' = V(x_1 y_1 - 1)$. On the open set $D(x_1)$, which contains $X'$, put $u = x_1 y_1 - 1$. Then $k[x_1, x_1^{-1}, y_1, z] = k[x_1, x_1^{-1}, u, z]$, and $u$ and $z$ are coordinates in the same way. Thus $X'$ has normal crossings with $E$. $\square$

In Example 2.3.6 the embedded process can not use the normalization. After the blowup of the origin of $\mathbb{A}^3_k$, the strict transform $V(z_1^2 - x^2 h(y_1))$ in the $x$-chart is singular along the line $L = V(x, z_1)$. Blow up the ambient chart along the regular curve $L$, and take the chart with $z_1 = x z_2$. Then $z_1^2 - x^2 h = x^2 (z_2^2 - h)$, and the strict transform is $V(z_2^2 - h(y_1))$. This is the chart $\operatorname{Spec} C$ of the normalization in Example 2.3.6. Thus a blowup in a regular curve does the work of the normalization here.

### History

Zariski proved the resolution of surfaces over a field of characteristic 0 by normalization and point blowups. The paper [Zar39] gives this proof for algebraic surfaces. He then proved local uniformization in characteristic 0 [Zar40], and he used it for the resolution of threefolds in characteristic 0 [Zar44].

Abhyankar proved the resolution of surfaces over an algebraically closed field of characteristic $p > 0$ [Abh56s]. His proof goes through local uniformization along each valuation of the function field. The paper [Abh56] studies the valuations centered in a local domain, and it contains the inequality of Abhyankar. Later Abhyankar proved the embedded resolution of surfaces in characteristic $p$, and he used it for threefolds in characteristic $p > 5$ [Abh66].

Hironaka [Hir64] proved resolution and embedded resolution in characteristic 0 in each dimension. Later he gave a proof of the resolution of excellent surfaces in each characteristic, with the characteristic polyhedron. The volume [CGO] treats the resolution of excellent surfaces along these lines. Lipman [Lip78] proved Theorem 2.2.1 for each excellent surface with no embedding. Cossart, Jannsen and Saito [CJS20] proved the canonical embedded version, Theorem 3.1.4.

Benito and Villamayor defined an invariant in characteristic $p$ by elimination, and they used it for the embedded resolution of two-dimensional schemes [BenV13]. Hauser and Perlega treat the embedded resolution of surfaces in a regular threefold in characteristic $p$ [HP24]. The book of Cutkosky [Cut04] gives the resolution of surfaces, and it gives the method of Abhyankar in a short form. The lectures of Kollár [Kol07] treat resolution in characteristic 0.

### What is open

For dimension 3, Cossart-Piltant [CP19] prove a non-embedded resolution of each reduced quasi-excellent Noetherian scheme of dimension at most 3. The embedded resolution of a threefold in a regular scheme of dimension 4 in characteristic $p$, by blowups in regular centers, is still open. The resolution of varieties of dimension 4 and higher in characteristic $p$ is open. Volume 9 explains the state of these problems. This volume shows the case of surfaces, where every characteristic is known.

### Notes and references

Normal flatness is in [Hir64] and in [CJS20]. The definitions of simple normal crossings vary a little. We follow the form that the project uses for its nodes. For the history of the resolution of surfaces see [Cut04], [Kol07] and the introduction of [CJS20]. For the blowup of a regular point and the surfaces over an algebraically closed field see [Har, Chapter V].
