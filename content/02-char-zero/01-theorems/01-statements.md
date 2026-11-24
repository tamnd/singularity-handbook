---
title: The statements
nodes: [SG0000001P, SG0000000D, SG00000004, SG00000005, SG0000000V]
sources: [Hir64, Kol07, BM97, EV98, EH02, Wlo05, Vil89, Hau03, Cut04, Har]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The statements

In this volume $k$ is a field of characteristic 0. A variety over $k$ is a reduced separated scheme of finite type over $k$, as in Volume 0, Definition 2.1.4; it need not be irreducible. A scheme of finite type over a perfect field is regular if and only if it is smooth over the field, so for varieties over $k$ we use the words regular and smooth in the same sense. We write $\operatorname{Sing}(X)$ for the singular locus of $X$, the complement of the regular locus $\operatorname{Reg}(X)$.

### Resolution

We use the definition of Volume 0, Definition 2.1.5. A *resolution* of a scheme $X$ is a proper morphism $\pi \colon Y \to X$ with $Y$ regular, such that $\pi$ is an isomorphism over $\operatorname{Reg}(X)$ and $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$.

**Theorem 1.1.1 (Hironaka).** Let $X$ be a variety over a field $k$ of characteristic 0. Then $X$ has a resolution.

Node: SG0000001P · Lean: `Singularity.ResolutionInDim`, `Singularity.resolutionInDim_charZero`

This is the main theorem of [Hir64]. In the notation of Volume 0, Definition 2.2.1, it says that $\mathrm{Res}(0, n)$ holds for each $n$. The Lean library proves this form from Main Theorem I of the base; see Chapter 4 and Volume 9, Section 1.2.

Hironaka proved more. The resolution is a composite of blowups with smooth centers, it is projective, and the inverse image of the singular locus is a divisor with simple normal crossings. We state the strong form for quasi-projective varieties, as in [Kol07, Chapter 3]. First we recall the definition of simple normal crossings.

**Definition 1.1.2 (simple normal crossings).** Let $X$ be a smooth variety over $k$. A *divisor with simple normal crossings* on $X$ is a sum $E = \sum_{i \in J} E^i$ of smooth divisors $E^i$, indexed by a finite set $J$, such that each closed point $x \in X$ has a regular system of parameters $z_1, \dots, z_n$ of $\mathcal{O}_{X,x}$ with this property: for each $i$ with $x \in E^i$ there is an index $c(i)$ with $E^i = (z_{c(i)} = 0)$ near $x$, and $c(i) \ne c(i')$ for $i \ne i'$. A closed subvariety $Z \subseteq X$ has *simple normal crossings with* $E$ if, in addition, the parameters can be chosen so that $Z = (z_{j_1} = \dots = z_{j_s} = 0)$ near $x$, for some indices $j_1, \dots, j_s$.

Node: SG0000000V · Lean: `Singularity.IsSncDivisor`

A divisor $E^i$ need not be irreducible, but it is smooth, so its irreducible components are disjoint. A subvariety with simple normal crossings with $E$ is smooth, and it may lie in some of the $E^i$. We often give the index set $J$ an order; Chapter 3 uses the order.

**Theorem 1.1.3 (strong resolution).** Let $X$ be an integral quasi-projective variety over $k$. Then there is a projective birational morphism $\Pi \colon X' \to X$ such that

1. $X'$ is smooth,
2. $\Pi$ is an isomorphism over $\operatorname{Reg}(X)$, and
3. $\Pi^{-1}(\operatorname{Sing}(X))$ is a divisor with simple normal crossings on $X'$.

Lean: none yet

This is the second form of resolution in [Kol07, Chapter 3], Section "Statement of main theorems". A morphism with the three properties is a resolution in the sense of Volume 0: it is proper since it is projective, and $\Pi^{-1}(\operatorname{Reg}(X))$ is the complement of a divisor in the smooth variety $X'$, so it is dense. The map has no node for the strong form; the node SG0000001P records only the weaker form of Theorem 1.1.1.

### Embedded resolution

Let $Y$ be a smooth variety and $X \subseteq Y$ a reduced closed subscheme. We use the definition of an embedded resolution of Volume 4, Definition 3.1.3: a finite sequence of blowups $Y_r \to \dots \to Y_0 = Y$, each in a permissible center for the strict transform $X_i$ of $X$, such that $X_r$ is regular, the union $E_r$ of the exceptional divisors is a divisor with simple normal crossings on $Y_r$, and $X_r$ has normal crossings with $E_r$.

**Theorem 1.1.4 (Hironaka, embedded resolution).** Let $Y$ be a smooth variety over $k$ and let $X \subseteq Y$ be a reduced closed subscheme. Then $X$ has an embedded resolution.

Lean: none yet

This is the second main theorem of [Hir64]. The constructive proofs of [Vil89], [BM97], [EV98] and [EH02] give an embedded resolution that is determined by the pair $(Y, X)$ and compatible with smooth morphisms. The Lean library defines the conclusion in a weak form without the sequence of blowups, as `Singularity.IsEmbeddedResolution` (Volume 4, Section 3.1), but it has no statement of Theorem 1.1.4 in characteristic 0, and the map has no node for it.

### Principalization

Kollár does not prove resolution directly. He proves a theorem about ideal sheaves on smooth varieties, and he deduces resolution from it. Let $g \colon Y \to X$ be a morphism of schemes and $I \subseteq \mathcal{O}_X$ an ideal sheaf. We write $g^* I$ for the inverse image ideal sheaf $g^{-1} I \cdot \mathcal{O}_Y$, the ideal sheaf generated by the pullbacks of the local sections of $I$ [Har, Section II.7]. It can differ from the pullback of $I$ as an $\mathcal{O}_X$-module, and in this volume $g^* I$ always means the inverse image ideal sheaf. The *cosupport* of $I$ is $\operatorname{cosupp} I = \operatorname{Supp}(\mathcal{O}_X / I)$. An ideal sheaf on a smooth variety is *nonzero* if it is nonzero on each irreducible component.

**Theorem 1.1.5 (principalization, first form).** Let $X$ be a smooth variety over $k$ and let $I \subseteq \mathcal{O}_X$ be a nonzero ideal sheaf. Then there are a smooth variety $X'$ and a projective birational morphism $f \colon X' \to X$ such that $f^* I$ is locally principal.

Lean: none yet

Resolution implies this form. Let $\pi \colon B_I X \to X$ be the blowup of $I$. Then $\pi^* I$ is invertible [Har, Proposition II.7.13], and for a resolution $h \colon X' \to B_I X$ the composite $\pi \circ h$ is a principalization, because the pullback of an invertible ideal sheaf is locally principal. To get resolution back from principalization we need more control on the morphism.

**Theorem 1.1.6 (principalization, second form).** Let $X$ be a smooth variety over $k$ and let $I \subseteq \mathcal{O}_X$ be a nonzero ideal sheaf. Then there is a morphism $f \colon X' \to X$ with these properties.

1. $f^* I$ is locally principal.
2. $f$ is a composite of blowups $X' = X_r \to X_{r-1} \to \dots \to X_1 \to X_0 = X$, where $X_{i+1} \to X_i$ is the blowup of a smooth closed subvariety $Z_i \subseteq X_i$.
3. Each center $Z_i$ lies over $\operatorname{cosupp} I$, that is, its image in $X$ is contained in $\operatorname{cosupp} I$. In particular $f$ is an isomorphism over $X \setminus \operatorname{cosupp} I$.

Lean: none yet

The variety $X'$ is smooth and $f$ is projective and birational, because each blowup of a smooth variety along a smooth center has these properties. Section 1.2 deduces from Theorem 1.1.6 that each integral quasi-projective variety $X$ has a projective birational morphism $X' \to X$ with $X'$ smooth. Kollár states part 3 as the condition that $f$ is an isomorphism over $X \setminus \operatorname{cosupp} I$; the proof gives the form above. The next form keeps track of a divisor.

**Theorem 1.1.7 (principalization, third form).** Let $X$ be a smooth variety over $k$, let $I \subseteq \mathcal{O}_X$ be a nonzero ideal sheaf, and let $E$ be a divisor with simple normal crossings on $X$. Then there is a composite of blowups $\Pi \colon X_r \to \dots \to X_0 = X$ with smooth centers $Z_i \subseteq X_i$ such that

1. each $Z_i$ has simple normal crossings with the divisor $E_i$, the sum of the strict transform of $E$ and of the inverse images of the earlier centers,
2. $\Pi^* I$ is the ideal sheaf of a divisor with simple normal crossings, and
3. $\Pi$ is an isomorphism over $X \setminus \operatorname{cosupp} I$.

Lean: none yet

An ideal sheaf of the form $\mathcal{O}_X(-\sum_j c_j E^j)$, with $\sum_j E^j$ a divisor with simple normal crossings and $c_j \ge 0$, is called *monomial*: at each point it is generated by a monomial in a regular system of parameters. So Theorem 1.1.7 says that the inverse image of $I$ becomes monomial. Kollár calls this monomialization.

### Functoriality

A canonical algorithm assigns to each triple $(X, I, E)$ a blowup sequence, and it is compatible with smooth morphisms. Let us make this precise in the way of [Kol07, Chapter 3]. A *blowup sequence* on $X$ is a chain $X_r \to \dots \to X_1 \to X_0 = X$ in which $X_{i+1} \to X_i$ is the blowup of a given closed subscheme $Z_i \subseteq X_i$, the center. We keep the centers as part of the data, since the morphism does not determine the center when the center is a divisor. We allow empty centers. Let $h \colon Y \to X$ be a smooth morphism. The *pullback* of the sequence to $Y$ is the sequence $X_r \times_X Y \to \dots \to Y$ with centers $Z_i \times_X Y$; blowups commute with flat base change, so this is again a blowup sequence. A rule $B$ that assigns a blowup sequence to each triple *commutes with smooth morphisms* if for each smooth morphism $h \colon Y \to X$ the sequence $B(Y, h^* I, h^{-1} E)$ is obtained from the pullback of $B(X, I, E)$ by deleting the blowups with empty center. It *commutes with change of fields* if for each field extension $k \subseteq L$ the sequence of $(X_L, I_L, E_L)$ is the base change of the sequence of $(X, I, E)$.

**Theorem 1.1.8 (principalization, functorial form).** There is a rule $B$ that assigns to each triple $(X, I, E)$, where $X$ is a smooth scheme of finite type over a field of characteristic 0, $I$ is a nonzero ideal sheaf and $E$ is a divisor with simple normal crossings with ordered index set, a blowup sequence $\Pi \colon X_r \to \dots \to X_0 = X$ with these properties.

1. Each center is smooth and has simple normal crossings with the transform of $E$.
2. $\Pi^* I$ is the ideal sheaf of a divisor with simple normal crossings.
3. $\Pi$ is an isomorphism over $X \setminus \operatorname{cosupp} I$.
4. $B$ commutes with smooth morphisms and with change of fields.

Lean: none yet

This is the fourth and strongest form of principalization in [Kol07, Chapter 3]. Kollár proves also a compatibility with closed embeddings when $E$ is empty, which is needed to make the resolution independent of an embedding. From it he deduces a functorial resolution: a rule that assigns to each reduced scheme $X$ of finite type over $k$ a blowup sequence $X_r \to \dots \to X$ with $X_r$ smooth, which is an isomorphism over the smooth locus, with $\Pi^{-1}(\operatorname{Sing} X)$ a divisor with simple normal crossings, and which commutes with smooth morphisms and with change of fields. In this resolution the centers are subschemes of the singular varieties $X_i$, and they need not be smooth. Example 1.2.2 explains why.

The compatibility with smooth morphisms does two things. First, it lets us glue. Let $X = \bigcup U_i$ be an open cover by affine varieties. The sequences of the $U_i$ agree on the overlaps, because an open immersion is smooth, and so they glue to a sequence on $X$. Without functoriality, gluing fails. Kollár gives the example of two curves $C_1, C_2$ in a smooth threefold that meet in two points $p_1, p_2$, where $C_i$ has a cusp at $p_i$ and is smooth elsewhere. On $X \setminus \{p_1\}$ one can blow up $C_1$ first and then the transform of $C_2$, and on $X \setminus \{p_2\}$ the other way round. The two results glue to a proper morphism that is locally projective but not projective [Kol07, Chapter 3]. A functorial algorithm must blow up $p_1$ and $p_2$ first, at the same time. Second, functoriality makes the resolution compatible with group actions, since an automorphism is a smooth morphism, and with étale maps, so that it is a local construction in the étale topology.

### Notes and references

Hironaka's paper [Hir64] has the two main theorems: resolution and embedded resolution, with blowups along permissible centers. The proof was made constructive by Villamayor [Vil89] and Bierstone-Milman [BM97], who blow up the maximum locus of a local invariant. Encinas-Villamayor [EV98] and Encinas-Hauser [EH02] simplified it, and Włodarczyk [Wlo05] gave a short proof with a homogenized coefficient ideal. Kollár's chapter [Kol07, Chapter 3] combines these ideas into a proof that we follow; its Section "What is a good resolution algorithm" explains the conditions of a good algorithm. The survey [Hau03] explains the proof with many examples, and the book [Cut04] proves resolution of surfaces and the theorem of Hironaka in characteristic 0 in the style of a textbook.
