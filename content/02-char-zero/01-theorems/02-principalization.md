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

*Remark (why the codimension is at least 2).* The proof needs the stalk $I_\eta$ to be a non principal ideal, so that the principalization must change $P$ near $\eta$. If $\bar X$ is a hypersurface, then $c = 1$, the local ring $\mathcal{O}_{P,\eta}$ is a discrete valuation ring, and $I_\eta$ is principal. The ideal $I$ is then locally principal on all of $P$, because the ideal sheaf of a hypersurface in a smooth variety is invertible. So Theorem 1.1.6 holds for $(P, I)$ with the empty sequence of blowups, and the proof gives no center $Z_j$ at all. The linear embedding into $\mathbb{P}^{N+2}$ avoids this. It changes nothing in $X$, but it makes $\bar X$ a subvariety of codimension $c + 2 \ge 2$, whose ideal is not principal at the generic point.

*Remark (the center $Z_j$ near $\eta$).* The proof shows a little more than the statement. The component $Z'$ has the generic point $\eta_j$, which lies over $\eta$, so $\dim Z' = \dim \bar X$. Near $\eta_j$ the center $Z_j$ is $\Pi_j^{-1}(\bar X)$, a smooth subvariety of codimension $c$. In particular $\bar X$ is smooth on the open set $\bar X \cap V$, as it must be, since $\bar X \cap V \cong Z' \cap \Pi_j^{-1}(V)$. What the proof does not control is the part of $Z'$ over the singular points of $\bar X$. There $Z'$ is smooth, but the map $Z' \to \bar X$ can contract subvarieties, and it can also fail to be an isomorphism over smooth points of $\bar X$ that lie outside $V$. The next subsection deals with the second problem.

The morphism $g$ is a composite of blowups of $X$, but their centers are the intersections of the $Z_i$ with the transforms of $X$, and these can be singular. Kollár gives an example of Bierstone-Milman; we check its first step.

**Example 1.2.2.** Let $X \subseteq \mathbb{A}^4$ be defined by $I = (x^3 - y^2, \; x^4 + x z^2 - w^3)$. Both generators have order at least 2 at the origin, and $x^3 - y^2$ has order exactly 2. Blow up the origin and take the chart $x = x_1$, $y = x_1 y_1$, $z = x_1 z_1$, $w = x_1 w_1$. Then
$$x^3 - y^2 = x_1^2 (x_1 - y_1^2), \qquad x^4 + x z^2 - w^3 = x_1^3 (x_1 + z_1^2 - w_1^3).$$
The strict transform of $X$ in this chart is $X_1 = (x_1 = y_1^2, \; x_1 + z_1^2 = w_1^3)$. Its intersection with the plane $x_1 = y_1 = 0$ is the cuspidal curve $z_1^2 = w_1^3$ in that plane.

Lean: none yet

According to [Kol07, Chapter 3], the principalization algorithm blows up the origin first and then the plane $(x_1 = y_1 = 0)$, which lies in the exceptional divisor. So the induced resolution of $X$ blows up first a point and then the cuspidal curve, a singular center. We do not verify here which centers the algorithm chooses; the computation above only shows that the second center meets $X_1$ in a singular curve.

### What the strong form needs

Theorem 1.2.1 gives a projective birational morphism from a smooth variety. It does not say that $g$ is an isomorphism over $\operatorname{Reg}(X)$. For that, [Kol07, Chapter 3] uses the third form, Theorem 1.1.7, with the extra condition that the sequence is compatible with smooth morphisms. Kollár argues as follows. Let $F'$ be the strict transform in $P_r$ of the exceptional divisor of $\pi_j$. It is a smooth divisor, so its map to $\bar X$ is smooth over some smooth point $x$ of $\bar X$. Any two smooth points of $\bar X$ of the same dimension have embeddings in $P$ with isomorphic étale neighbourhoods, so by functoriality the map $F' \to \bar X$ is smooth over each smooth point. This map factors through $Z' \to \bar X$, and Kollár concludes that $\bar g$ is smooth over the smooth locus. Being birational, it is an isomorphism there. Kollár stresses that functoriality is needed here for the intermediate step $P_j \to P$ and not only for $P_r \to P$, and that this is the reason for the notion of a blowup sequence that keeps its centers; see [Kol07, Chapter 3], Section "Statement of the main theorems". The conclusion is Theorem 1.1.3.

*A direct argument with functoriality.* We give a proof of the isomorphism over the regular locus that uses only the functorial form, Theorem 1.1.8, with $E = \emptyset$. It is a variant of Kollár's argument. Let $B$ be the rule of Theorem 1.1.8, and let the sequence in the proof of Theorem 1.2.1 be $B(P, I, \emptyset)$. We claim that $\bar g \colon Z' \to \bar X$ is an isomorphism over $\operatorname{Reg}(\bar X)$.

Let $x$ be a closed point of $\operatorname{Reg}(\bar X)$, and let $d = N - c$ be the dimension of $\bar X$. Since $\bar X$ is smooth at $x$, there are an open set $U \ni x$ of $P$ and local coordinates $z_1, \dots, z_N$ on $U$ with $I|_U = (z_1, \dots, z_c)$ [Har, Section II.8]. After we shrink $U$, the coordinates define an étale morphism $h \colon U \to \mathbb{A}^N$, and $I|_U = h^* I_L$, where $L = (z_1 = \dots = z_c = 0) \cong \mathbb{A}^d$ is a linear subspace with ideal $I_L$.

First consider the model $(\mathbb{A}^N, I_L, \emptyset)$ and its sequence $B(\mathbb{A}^N, I_L, \emptyset)$. For $a \in k^d$, let $\tau_a$ be the translation by $(0, a)$, an automorphism of $\mathbb{A}^N$ with $\tau_a^* I_L = I_L$. An automorphism is a smooth morphism, and the pullback of a nonempty center by an isomorphism is not empty. So by part 4 of Theorem 1.1.8 the sequence is its own pullback by $\tau_a$, and each center is invariant under the lift of $\tau_a$. Let $Z^{\mathrm{mod}}_l$ be the first center that is not empty. The earlier blowups are the identity, so $Z^{\mathrm{mod}}_l$ is a closed subset of $\mathbb{A}^N$, and it lies in $L$ by part 3. It is invariant under all the translations $\tau_a$. We show that it is all of $L$. Let $\varphi \in k[z_{c+1}, \dots, z_N]$ vanish on $Z^{\mathrm{mod}}_l$, and let $q \in Z^{\mathrm{mod}}_l$ be a closed point, with coordinates $q_{c+1}, \dots, q_N$ in the residue field $K = k(q)$. Then $\varphi(q + a) = 0$ for all $a \in k^d$. The polynomial $\psi(t) = \varphi(q + t)$ in $K[t_1, \dots, t_d]$ vanishes on $k^d$, and $k$ is infinite since it has characteristic 0. So $\psi = 0$, and then $\varphi(t) = \psi(t - q) = 0$. Hence the ideal of $Z^{\mathrm{mod}}_l$ in $L$ is zero, and $Z^{\mathrm{mod}}_l = L$.

Now go back to $U$. An open immersion is smooth, so the restriction of $B(P, I, \emptyset)$ to $U$ is $B(U, I|_U, \emptyset)$, up to blowups with empty centers. The étale map $h$ is smooth, so $B(U, I|_U, \emptyset)$ is the pullback of the model sequence, up to blowups with empty centers. The pullback of an empty center is empty, and the pullback of $L$ is $\bar X \cap U$, which is not empty. Hence, in the sequence on $P$, the centers before a certain step $j'$ do not meet the inverse image of $U$, and the center of step $j'$ meets the inverse image of $U$ in the inverse image of $\bar X \cap U$. Since $\eta \in U$, the step $j'$ is the step $j$ of the proof of Theorem 1.2.1. So $\Pi_j$ is an isomorphism over $U$, and $Z' \cap \Pi_j^{-1}(U) \to \bar X \cap U$ is an isomorphism.

The open sets $U \cap \bar X$ for all closed points $x \in \operatorname{Reg}(\bar X)$ cover an open set of $\bar X$ that contains all closed points of $\operatorname{Reg}(\bar X)$. Since $\bar X$ is Jacobson, this open set contains $\operatorname{Reg}(\bar X)$. So $\bar g$ is an isomorphism over $\operatorname{Reg}(\bar X)$, and $g$ is an isomorphism over $\operatorname{Reg}(X) = \operatorname{Reg}(\bar X) \cap X$. Since $Z'$ is irreducible, $g^{-1}(\operatorname{Reg}(X))$ is dense in $X'$. With Theorem 1.2.1 this proves Theorem 1.1.1 for integral quasi-projective varieties, once Theorem 1.1.8 is known. It does not prove part 3 of Theorem 1.1.3, which needs the divisor $E$ of Theorem 1.1.7 and more work [Kol07, Chapter 3].

The argument shows what functoriality does. It is used for the intermediate step $P_j \to P$: we must know that the first $j$ centers miss the regular part of $\bar X$, and this does not follow from any property of the final morphism $P_r \to P$. It is used with the étale map $h$, which is not an open immersion, and with the translations of the model, which are automorphisms. A rule that commutes only with open immersions would not be enough.

The proof of Theorem 1.2.1 also explains why Kollár works with ideal sheaves on a smooth ambient variety. An induction on the dimension needs to restrict the problem to a smooth hypersurface, and restriction is easy for an ideal sheaf on a smooth variety, but there is no good restriction of a singular variety to a hypersurface of an embedding that it does not lie in. Chapter 2 finds the right hypersurface, and Chapter 3 the right ideal on it.

### The plan of the proof of principalization

The rest of the volume proves principalization. Here is the plan, in the form of [Kol07, Chapter 3], Section "Plan of the proof". We work with marked ideals $(I, m)$: an ideal sheaf $I$ on a smooth variety and a natural number $m$, the mark. Section 2.2 defines the blowups of order at least $m$ and the birational transform of a marked ideal. There are two statements for each dimension $n$.

- Order reduction for ideals in dimension $n$: for an ideal $I$ on a smooth variety of dimension $n$ with maximal order $m$, there is a sequence of blowups of order $m$ after which the maximal order of the transform is less than $m$.
- Order reduction for marked ideals in dimension $n$: for a marked ideal $(I, m)$ on a smooth variety of dimension $n$, there is a sequence of blowups of order at least $m$ after which the transform has order less than $m$ at every point.

The induction goes in the order: marked ideals in dimension $n - 1$ give ideals in dimension $n$, and ideals in dimension $n$ give marked ideals in dimension $n$. The first step uses a hypersurface of maximal contact (Chapter 2) and the coefficient ideal on it (Chapter 3). Order reduction for the marked ideal $(I, 1)$ is principalization: Section 3.3 explains why. In each step one must also keep a divisor with simple normal crossings and prove that the construction commutes with smooth morphisms; this is where most of the length of the full proof goes.

*Remark (positive characteristic).* The proof of Theorem 1.2.1 and the direct argument above do not use the characteristic, except through the assumption that principalization holds. The infinite field in the direct argument is available in every characteristic after a base change, if the rule commutes with change of fields. So in each characteristic, a functorial principalization of ideal sheaves on smooth varieties would give resolution of quasi-projective varieties in the same way. The difficulty in characteristic $p$ is principalization itself. Section 2.4 shows that the induction on the dimension breaks at its first step, and Volume 7 studies what can be said about the invariants in that case.

### Notes and references

Theorem 1.2.1 is from [Kol07, Chapter 3], Section "Statement of the main theorems". Example 1.2.2 is from Section "Order reduction for ideals" of the same chapter, where Kollár attributes it to Bierstone-Milman. The fact that a maximal ideal of a regular local ring of dimension $c$ needs exactly $c$ generators is the definition of a regular local ring [Mat, Section 14]. The fact that the resolution produced by an embedded method need not be a sequence of smooth blowups of $X$ is a known feature of all the canonical algorithms, see also [BM97].
