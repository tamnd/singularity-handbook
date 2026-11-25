---
title: From principalization to resolution
nodes: [SG0000001P, SG00000044]
sources: [Kol07, Har, Mat, BM97]
status: drafted
drafted_by: writer
reviewed_by: []
---
## From principalization to resolution

This section proves that the second form of principalization, Theorem 1.1.6, gives a resolution of each integral quasi-projective variety, in the weak sense of a projective birational morphism from a smooth variety. The argument is from [Kol07, Chapter 3]. It is short, but it is the reason why the rest of the volume can work with ideal sheaves on smooth varieties instead of singular varieties.

### The theorem

**Theorem 1.2.1 (resolution from principalization).** Assume Theorem 1.1.6. Let $X$ be an integral quasi-projective variety over $k$. Then there are a smooth variety $X'$ and a projective birational morphism $g \colon X' \to X$.

Node: SG00000044 · Lean: none yet

*Proof.* Since $X$ is quasi-projective, it is a locally closed subscheme of a projective space $\mathbb{P}^N$. A linear embedding $\mathbb{P}^N \subseteq \mathbb{P}^{N+2}$ raises the codimension by 2, so we may assume that the closure $\bar X$ of $X$ in $P = \mathbb{P}^N$ has codimension $c \ge 2$. Let $I \subseteq \mathcal{O}_P$ be the ideal sheaf of $\bar X$ and let $\eta$ be the generic point of $\bar X$. The local ring $\mathcal{O}_{P,\eta}$ is regular of dimension $c$, and $I_\eta$ is its maximal ideal. A maximal ideal of a regular local ring of dimension $c$ needs $c$ generators, so $I_\eta$ is not principal.

Apply Theorem 1.1.6 to $(P, I)$. We get blowups $\pi_i \colon P_{i+1} \to P_i$ with smooth centers $Z_i$, with composites $\Pi_i \colon P_i \to P$, such that $\Pi_r^* I$ is locally principal and each $Z_i$ lies over $\bar X$.

We say that $\Pi_i$ is an isomorphism near $\eta$ if there is an open set $V \ni \eta$ of $P$ such that $\Pi_i^{-1}(V) \to V$ is an isomorphism; then let $\eta_i$ be the point of $P_i$ over $\eta$. The map $\Pi_0$ is the identity. Assume that $\Pi_i$ is an isomorphism near $\eta$ and $\eta_i \notin Z_i$. The set $\Pi_i(Z_i)$ is closed, since $\Pi_i$ is proper, and it does not contain $\eta$, since $\Pi_i$ is bijective over $V$. So $V' = V \setminus \Pi_i(Z_i)$ is an open neighbourhood of $\eta$ over which $\pi_i$ and hence $\Pi_{i+1}$ is an isomorphism.

If $\eta_i \notin Z_i$ for all $i$, then $\Pi_r$ is an isomorphism near $\eta$, and the stalk of $\Pi_r^* I$ at $\eta_r$ is $I_\eta$, which is not principal. This contradicts the choice of the sequence. Hence there is a least $j$ with $\eta_j \in Z_j$, and $\Pi_j$ is an isomorphism over an open set $V \ni \eta$.

The center $Z_j$ is smooth, so its connected components are irreducible. Let $Z'$ be the component that contains $\eta_j$. Since $Z_j$ lies over $\bar X$, the set $Z' \cap \Pi_j^{-1}(V)$ is a closed irreducible subset of $\Pi_j^{-1}(\bar X \cap V)$. Under the isomorphism $\Pi_j^{-1}(V) \cong V$ the set $\Pi_j^{-1}(\bar X \cap V)$ corresponds to $\bar X \cap V$, which is irreducible with generic point $\eta$. A closed irreducible subset that contains the generic point of an irreducible space is the whole space. So $Z' \cap \Pi_j^{-1}(V) = \Pi_j^{-1}(\bar X \cap V)$. This set is a nonempty open subset of the irreducible space $Z'$, so it is dense in $Z'$, and the generic point of $Z'$ is $\eta_j$.

Let $\bar g \colon Z' \to \bar X$ be the restriction of $\Pi_j$, with the reduced structure on $Z'$. Over $\bar X \cap V$ it is an isomorphism of reduced schemes, so $\bar g$ is birational. It is projective: $Z'$ is closed in $P_j$, the composite of blowups $P_j \to P$ is projective, and $\bar X$ is closed in $P$. The variety $Z'$ is smooth, since it is a component of the smooth center $Z_j$. Finally $X$ is open in $\bar X$, and $g \colon X' = \bar g^{-1}(X) \to X$ is projective and birational, with $X'$ smooth. $\square$

The morphism $g$ is a composite of blowups of $X$, but their centers are the intersections of the $Z_i$ with the transforms of $X$, and these can be singular. Kollár gives an example of Bierstone-Milman; we check its first step.

**Example 1.2.2.** Let $X \subseteq \mathbb{A}^4$ be defined by $I = (x^3 - y^2, \; x^4 + x z^2 - w^3)$. Both generators have order at least 2 at the origin, and $x^3 - y^2$ has order exactly 2. Blow up the origin and take the chart $x = x_1$, $y = x_1 y_1$, $z = x_1 z_1$, $w = x_1 w_1$. Then
$$x^3 - y^2 = x_1^2 (x_1 - y_1^2), \qquad x^4 + x z^2 - w^3 = x_1^3 (x_1 + z_1^2 - w_1^3).$$
The strict transform of $X$ in this chart is $X_1 = (x_1 = y_1^2, \; x_1 + z_1^2 = w_1^3)$. Its intersection with the plane $x_1 = y_1 = 0$ is the cuspidal curve $z_1^2 = w_1^3$ in that plane.

Lean: none yet

According to [Kol07, Chapter 3], the principalization algorithm blows up the origin first and then the plane $(x_1 = y_1 = 0)$, which lies in the exceptional divisor. So the induced resolution of $X$ blows up first a point and then the cuspidal curve, a singular center. We do not verify here which centers the algorithm chooses; the computation above only shows that the second center meets $X_1$ in a singular curve.

### What the strong form needs

Theorem 1.2.1 gives a projective birational morphism from a smooth variety. It does not say that $g$ is an isomorphism over $\operatorname{Reg}(X)$. For that, [Kol07, Chapter 3] uses the third form, Theorem 1.1.7, with the extra condition that the sequence is compatible with smooth morphisms. Kollár argues as follows. Let $F'$ be the strict transform in $P_r$ of the exceptional divisor of $\pi_j$. It is a smooth divisor, so its map to $\bar X$ is smooth over some smooth point $x$ of $\bar X$. Any two smooth points of $\bar X$ of the same dimension have embeddings in $P$ with isomorphic étale neighbourhoods, so by functoriality the map $F' \to \bar X$ is smooth over each smooth point. This map factors through $Z' \to \bar X$, and Kollár concludes that $\bar g$ is smooth over the smooth locus. Being birational, it is an isomorphism there. Kollár stresses that functoriality is needed here for the intermediate step $P_j \to P$ and not only for $P_r \to P$, and that this is the reason for the notion of a blowup sequence that keeps its centers; see [Kol07, Chapter 3], Section "Statement of the main theorems". The conclusion is Theorem 1.1.3.

The proof of Theorem 1.2.1 also explains why Kollár works with ideal sheaves on a smooth ambient variety. An induction on the dimension needs to restrict the problem to a smooth hypersurface, and restriction is easy for an ideal sheaf on a smooth variety, but there is no good restriction of a singular variety to a hypersurface of an embedding that it does not lie in. Chapter 2 finds the right hypersurface, and Chapter 3 the right ideal on it.

### The plan of the proof of principalization

The rest of the volume proves principalization. Here is the plan, in the form of [Kol07, Chapter 3], Section "Plan of the proof". We work with marked ideals $(I, m)$: an ideal sheaf $I$ on a smooth variety and a natural number $m$, the mark. Section 2.2 defines the blowups of order at least $m$ and the birational transform of a marked ideal. There are two statements for each dimension $n$.

- Order reduction for ideals in dimension $n$: for an ideal $I$ on a smooth variety of dimension $n$ with maximal order $m$, there is a sequence of blowups of order $m$ after which the maximal order of the transform is less than $m$.
- Order reduction for marked ideals in dimension $n$: for a marked ideal $(I, m)$ on a smooth variety of dimension $n$, there is a sequence of blowups of order at least $m$ after which the transform has order less than $m$ at every point.

The induction goes in the order: marked ideals in dimension $n - 1$ give ideals in dimension $n$, and ideals in dimension $n$ give marked ideals in dimension $n$. The first step uses a hypersurface of maximal contact (Chapter 2) and the coefficient ideal on it (Chapter 3). Order reduction for the marked ideal $(I, 1)$ is principalization: Section 3.3 explains why. In each step one must also keep a divisor with simple normal crossings and prove that the construction commutes with smooth morphisms; this is where most of the length of the full proof goes.

### Notes and references

Theorem 1.2.1 is from [Kol07, Chapter 3], Section "Statement of the main theorems". Example 1.2.2 is from Section "Order reduction for ideals" of the same chapter, where Kollár attributes it to Bierstone-Milman. The fact that a maximal ideal of a regular local ring of dimension $c$ needs exactly $c$ generators is the definition of a regular local ring [Mat, Section 14]. The fact that the resolution produced by an embedded method need not be a sequence of smooth blowups of $X$ is a known feature of all the canonical algorithms, see also [BM97].
