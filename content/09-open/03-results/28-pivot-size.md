---
title: Pivot sets and the number of pivots in toric relative strong factorization
nodes: [SG000000CG, SG000000CK]
sources: [Gow05, DSK11, Kar03]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Pivot sets and the number of pivots in toric relative strong factorization

This section reports the twenty-eighth research result, from the track FP (tamnd/singularity#320), the patching of models. It continues Section 3.27. Section 3.27 proved the multi-pivot theorem 3.27.17: a cone $\sigma$ has a certificate if some cones of a subdivision of $\sigma$ turn around a few rays in a way that the octant can follow. This section asks how much this theorem reduces the problem. The answer is: it does not reduce it. The condition of the theorem holds for every cone that has a certificate, and its bounded form, with at most $k$ rays, is the same as a bound on the number of pivots of some certificate. So the real question is the size of the pivot set. When this section was first written, this question was open for each $k \ge 2$. Section 3.30 settles it: the bound is false for every $k$ (Corollary 3.30.12).

The results come from research note 92 and from research note 93, which is a referee report on note 92. Where the two notes differ, this section follows note 93. We keep the notation of Sections 3.26 and 3.27. So $\tau = \langle e_1, e_2, e_3 \rangle$ is the octant in $N = \mathbb{Z}^3$, $\sigma = \langle a_1, a_2, a_3 \rangle \subseteq \tau$ is a regular 3-dimensional cone, a certificate $(\Lambda, F)$ is as in Definition 3.26.15, and $\mathrm{St}_G(b)$ is as in Definition 3.27.8. All fans are regular. For a fan $G$ and a cone $c$ we write $G|_c$ for the fan of the cones of $G$ contained in $c$, as in Lemma 3.26.4.

### Motivation

Toric $\mathrm{RSF}_3$ is a case of the strong factorization conjecture of Oda (Proposition 3.27.26), and this conjecture is open in dimension 3. So a proof of toric $\mathrm{RSF}_3$ should use the structure that it has in addition to the conjecture of Oda. The first part of this section says what this is: a certificate lets us choose the subdivision of $\sigma$, among the restrictions of star sequences of the octant (Proposition 3.28.1).

The second part studies the sets of pivots of Theorem 3.27.17. A set of pivots is the same as a tiling of $\sigma$ by closed stars of rays (Lemma 3.28.6). This view gives a parity rule (Lemma 3.28.7), and the parity rule explains why one certificate of the cone $F_4$ of Proposition 3.27.21 has no set of pivots at all. The worked example of $F_4$ shows the obstruction and how one more star removes it.

The third part is a warning. A simple common star (Lemma 3.28.12) turns each certificate into one with a set of pivots. So the hypotheses of Theorem 3.27.17 hold for every cone that has a certificate, and a statement of the form "a multi-pivot witness exists" is only a new name for "a certificate exists". Research note 92 stated a reduction of $\mathrm{RSF}_3$ to a conjecture on witnesses with at most $k$ pivots. Research note 93 proved that this conjecture is the same as a bound on the number of pivots of certificates (Proposition 3.28.15). The theorem of note 92 is therefore a restatement and not a reduction. The content is the bound $k$.

A reader needs Section 3.26 up to Lemma 3.26.16 and Section 3.27 up to Proposition 3.27.18.

### The subdivision of $\sigma$

**Proposition 3.28.1 (the choice of the subdivision).** Say that a fan $F$ with support $\tau$ *refines* $\sigma$ if $\sigma$ is a union of cones of $F$. Let $\mathcal{D}(\sigma)$ be the set of the fans $F|_\sigma$, where $F$ runs over the star sequences of $\tau$ that refine $\sigma$. Then:

1. $\mathcal{D}(\sigma)$ is not empty;
2. if $D \in \mathcal{D}(\sigma)$ and $D'$ is the star of $D$ at a cone of $D$, then $D' \in \mathcal{D}(\sigma)$;
3. $\sigma$ has a certificate if and only if some $D \in \mathcal{D}(\sigma)$ is a star sequence of $\sigma$.

Lean: none yet

*Proof.* (1) Let $\ell$ be a linear form on $N$ with integer coefficients, and write $\ell = \ell_+ - \ell_-$, where $\ell_+$ and $\ell_-$ have nonnegative coefficients and no common nonzero coefficient. Then $(x^{\ell_+}, x^{\ell_-})$ is a monomial ideal of $F[x, y, z]$. By toric principalization [Gow05] there is a star sequence of $\tau$ on whose charts this ideal is principal. The ideal is principal on the chart of a cone $c$ exactly when one generator divides the other on $c$, that is, when $\ell \ge 0$ on $c$ or $\ell \le 0$ on $c$. Each cone of a later star lies in a cone of the earlier fan, so a later star sequence keeps this property. Do this for the three linear forms that vanish on the three facets of $\sigma$, one after the other, and let $F$ be the result. Each cone of $F$ lies on one side of each facet plane. Since $\sigma$ is the intersection of the three closed half spaces of its facets, each cone of $F$ lies in $\sigma$ or lies on the wrong side of some facet plane, and then it meets $\sigma$ only in this plane, that is, in $\partial \sigma$. The cones of $F$ cover $\tau \supseteq \sigma$, so the cones in $\sigma$ cover the interior of $\sigma$, and since they are closed they cover $\sigma$. So $F$ refines $\sigma$.

(2) Let $D = F|_\sigma$ with $F$ as in the definition, and let $c$ be a cone of $D$. Then $c$ is a cone of $F$, and we make the star $F'$ of $F$ at $c$. Each new cone lies in an old cone. An old cone that lies in $\sigma$ has its pieces in $\sigma$. An old cone $k$ that does not lie in $\sigma$ meets $\sigma$ only in $\partial \sigma$, so its pieces also meet $\sigma$ only in $\partial \sigma$. So $F'$ refines $\sigma$. A piece of a cone $k \supseteq c$ keeps all the generators of $k$ that are not in $c$. If $k \not\subseteq \sigma$, one of these generators is outside $\sigma$, since the generators of $c$ are in $\sigma$, so the piece is not in $\sigma$. So $F'|_\sigma$ consists of the cones of $D$ that do not contain $c$ and of the pieces of the cones of $D$ that contain $c$. This is the star of $D$ at $c$.

(3) Let $(\Lambda, F)$ be a certificate. The cones of $\Lambda$ are cones of $F$ and cover $\sigma$, so $F$ refines $\sigma$ and $\Lambda \subseteq F|_\sigma$. Let $C$ be a 3-dimensional cone of $F|_\sigma$. Its interior meets the interior of a 3-dimensional cone $C'$ of $\Lambda$. Both are cones of the fan $F$, so $C = C'$. A cone of lower dimension of $F|_\sigma$ is a face of a 3-dimensional one, so $F|_\sigma = \Lambda$, and this is a star sequence of $\sigma$. Conversely, if $F$ refines $\sigma$ and $F|_\sigma$ is a star sequence of $\sigma$, then $(F|_\sigma, F)$ is a certificate. $\square$

**Corollary 3.28.2 (a one-sided form of the conjecture of Oda is enough).** Assume that for each fan $D \in \mathcal{D}(\sigma)$ there is a star sequence of $D$ that is also a star sequence of $\sigma$. Then $\sigma$ has a certificate. In particular the strong factorization conjecture of Oda in dimension 3 gives toric $\mathrm{RSF}_3$.

Lean: none yet

*Proof.* Take $D \in \mathcal{D}(\sigma)$ by Proposition 3.28.1(1), and a star sequence $D''$ of $D$ that is a star sequence of $\sigma$. Each star of the sequence from $D$ to $D''$ is at a cone of the current fan, so by Proposition 3.28.1(2) and induction $D'' \in \mathcal{D}(\sigma)$. Then Proposition 3.28.1(3) gives a certificate. The conjecture of Oda gives such a $D''$ for each regular subdivision $D$ of $\sigma$. $\square$

This is a second proof of Proposition 3.27.26, and it shows what $\mathrm{RSF}_3$ has in addition. The conjecture of Oda must treat every regular subdivision $D$ of $\sigma$. A certificate needs only one $D$, and we can choose it in $\mathcal{D}(\sigma)$. A member of $\mathcal{D}(\sigma)$ comes with the fan of $\tau$ outside $\sigma$, and with the monoid $S$ of Corollary 3.27.3 and the moves of Lemma 3.27.4(3) on the matrix $M$. Every result below uses this choice. None of them is about an arbitrary $D$, so none of them is a statement about the conjecture of Oda.

**Lemma 3.28.3 (every vector can be a ray).** Let $v \in \sigma$ be a primitive lattice vector. Then $v$ is a ray of some star sequence of $\sigma$. The same holds for $\tau$.

Lean: none yet

*Proof.* Since $\sigma$ is regular, $v = x_1 a_1 + x_2 a_2 + x_3 a_3$ with integers $x_i \ge 0$. We use induction on $x_1 + x_2 + x_3$. If only one $x_i$ is not zero, then $v = a_i$, since $v$ is primitive. Otherwise take $i \ne j$ with $x_i \ge x_j > 0$, let $l$ be the third index, and make the star at $\langle a_i, a_j \rangle$. The piece $\langle a_i, a_i + a_j, a_l \rangle$ is regular and contains
$$v = (x_i - x_j) a_i + x_j (a_i + a_j) + x_l a_l,$$
whose coefficients have the sum $x_1 + x_2 + x_3 - x_j$. Apply the induction in this piece. A star sequence of the piece is a continuation of the star sequence of $\sigma$, by Lemma 3.26.4. The case of $\tau$ is the case $\sigma = \tau$. $\square$

So pivots are easy to make. The difficulty is to make their stars fit together, and the rest of the section is about this.

### Pivot sets as tilings by stars

**Definition 3.28.4 (pivot sets, the slice and degrees).** Let $\Lambda$ be a star sequence of $\sigma$. A *pivot set* of $\Lambda$ is a set $T$ of rays of $\Lambda$ such that no two rays of $T$ span a 2-face of $\Lambda$ and every 3-dimensional cone of $\Lambda$ contains a ray of $T$. This is the set $T$ of Proposition 3.27.18(2). We write $m = |T|$.

Let $H$ be the plane $x + y + z = 1$. Each ray of $\sigma$ meets $H$ in one point, and $\sigma \cap H$ is a triangle. The *slice* of $\Lambda$ is the triangulation of this triangle by the sets $c \cap H$, $c \in \Lambda$. Its vertices are the rays, its edges are the 2-faces and its triangles are the 3-dimensional cones of $\Lambda$. Two rays are *joined* if they span a 2-face of $\Lambda$. A ray is *interior* if it lies in the interior of $\sigma$. The *link* of a ray $v$ is the set of the rays joined to $v$. For an interior ray the link is a cycle in the slice, and its *degree* is the length of this cycle, that is, the number of 3-dimensional cones that contain $v$. For a ray in $\partial \sigma$ the link is a path.

**Lemma 3.28.5 (pivot sets meet each cone once).** Let $T$ be a set of rays of $\Lambda$. The following are equivalent.

1. $T$ is a pivot set.
2. Every 3-dimensional cone of $\Lambda$ contains exactly one ray of $T$.
3. The closed stars $|\mathrm{St}_\Lambda(b)|$, $b \in T$, cover $\sigma$, and two of them have no common interior point.

Lean: none yet

*Proof.* (1) implies (2): two rays of a 3-dimensional cone span a 2-face of it, so a 3-dimensional cone with two rays of $T$ is not allowed. (2) implies (1): if $b, b' \in T$ span a 2-face of $\Lambda$, a 3-dimensional cone that contains this 2-face contains two rays of $T$. For (2) and (3): $\sigma$ is the union of the 3-dimensional cones of $\Lambda$, and a 3-dimensional cone lies in $|\mathrm{St}_\Lambda(b)|$ only if it contains $b$. So the closed stars of $T$ cover $\sigma$ if and only if each 3-dimensional cone contains at least one ray of $T$. Two closed stars $|\mathrm{St}_\Lambda(b)|$ and $|\mathrm{St}_\Lambda(b')|$ have a common interior point if and only if some 3-dimensional cone lies in both, that is, contains $b$ and $b'$. $\square$

**Lemma 3.28.6 (tilings).** The pivot sets of $\Lambda$ are exactly the sets $T$ such that the closed stars of the rays of $T$ tile $\sigma$. A pivot set with $m$ rays is a way to write $\Lambda$ as the union of $m$ closed stars of rays.

Lean: none yet

*Proof.* This is Lemma 3.28.5(3). $\square$

The tiling view gives a local obstruction.

**Lemma 3.28.7 (parity).** Let $T$ be a pivot set of $\Lambda$ and let $v \notin T$ be an interior ray of $\Lambda$. Then the degree of $v$ is even. So every interior ray of odd degree is in $T$.

Lean: none yet

*Proof.* Let $w_1, \dots, w_k$ be the link cycle of $v$, with indices modulo $k$. The cone $\langle v, w_i, w_{i+1} \rangle$ contains exactly one ray of $T$ by Lemma 3.28.5, and this ray is not $v$. So exactly one of $w_i$ and $w_{i+1}$ is in $T$, for each $i$. Along the cycle the rays $w_i$ are in $T$ and not in $T$ in turn, so $k$ is even. $\square$

The lemma needs the word interior. A ray in $\partial \sigma$ has a path as its link, and the alternation along a path forces nothing (Exercise 3).

**Corollary 3.28.8 (two tests for no pivot set).** The fan $\Lambda$ has no pivot set in each of the following cases.

1. Two interior rays of odd degree are joined.
2. Some 3-dimensional cone of $\Lambda$ has three rays that are each joined to an interior ray of odd degree, and none of its three rays is itself an interior ray of odd degree.

Lean: none yet

*Proof.* Let $T$ be a pivot set. By Lemma 3.28.7 every interior ray of odd degree is in $T$. In case (1) two rays of $T$ are joined, which is not allowed. In case (2) each ray of the cone is joined to a ray of $T$, so it is not in $T$, and the cone contains no ray of $T$. $\square$

Research note 92 stated case (2) with the condition "all three rays outside $T$". That form has $T$ in the hypothesis, so it is not a test. Note 93 gave the form above, which uses only the fan.

The degree of a ray changes in a simple way under stars, and this explains where rays of odd degree come from.

**Lemma 3.28.9 (degrees under stars).** Let $\Lambda'$ be the star of $\Lambda$ at a cone $c$.

1. If $c = \langle x, y \rangle$ is an interior 2-face, in the cones $\langle x, y, z \rangle$ and $\langle x, y, z' \rangle$, then the new ray has degree 4, the degrees of $x$ and $y$ do not change, and the degrees of $z$ and $z'$ go up by 1.
2. If $c = \langle x, y \rangle$ is a 2-face in $\partial \sigma$, in the one cone $\langle x, y, z \rangle$, then the new ray lies in $\partial \sigma$, and the number of cones that contain $z$ goes up by 1.
3. If $c = \langle x, y, z \rangle$ is a 3-dimensional cone, then the new ray has degree 3, and the degrees of $x$, $y$ and $z$ go up by 1.

The other degrees do not change. Call a later star *raising* for a ray $v$ if it adds 1 to the degree of $v$, that is, a star at a 2-face opposite to $v$ or a star at a 3-dimensional cone that contains $v$. Then an interior ray made by a star at an interior 2-face has odd degree if and only if an odd number of later stars are raising for it, and an interior ray made by a star at a 3-dimensional cone has odd degree if and only if an even number of later stars are raising for it.

Lean: none yet

*Proof.* In the slice, the star at an interior edge $xy$ replaces the triangles $xyz$ and $xyz'$ by $xsz$, $syz$, $xsz'$ and $syz'$. The new vertex $s$ has the neighbours $x$, $y$, $z$, $z'$. The vertex $x$ loses $y$ and gets $s$, and so does $y$, while $z$ and $z'$ get $s$. The other two cases are the same count with one triangle, and with the triangle $xyz$ replaced by $sxy$, $syz$ and $sxz$. A ray in $\partial \sigma$ stays in $\partial \sigma$, and an interior ray stays interior, so the start degree of an interior ray is 4 or 3 by the type of its star, and only raising stars change it. $\square$

Research note 92 said that an interior ray has odd degree as soon as an odd number of later stars are raising for it. This is true only for rays made at an interior 2-face. Note 93 corrected it to the form above. So a search that stars freely makes rays of odd degree, and Lemma 3.28.7 is the first rule that a search for certificates with a pivot set must respect.

### Worked example: the cone $F_4$

**Proposition 3.28.10 (a certificate with no pivot set).** Let $F_4 = \langle (0,1,4), (1,2,7), (5,1,0) \rangle$, the cone of Proposition 3.27.21(2) with $k = 4$, with the rays $a_1 = (0,1,4)$, $a_2 = (1,2,7)$, $a_3 = (5,1,0)$. Its certificate of depth 18, found by the search of research note 90, has no pivot set.

Lean: none yet

*Proof.* The fan $\Lambda$ of this certificate has 24 cones of dimension 3 and 5 interior rays. This is an exact computation from note 92, replayed by note 93 with its own program. In the basis $a_1, a_2, a_3$ the interior rays and their degrees are

| ray | in the basis $a_1, a_2, a_3$ | degree |
|---|---|---|
| $(6,4,11)$ | $(1,1,1)$ | 6 |
| $(7,6,18)$ | $(1,2,1)$ | 6 |
| $(22,9,18)$ | $(1,2,4)$ | 4 |
| $u = (6,5,15)$ | $(2,1,1)$ | 5 |
| $u' = (16,6,11)$ | $(1,1,3)$ | 5 |

The five cones of $\Lambda$ that contain $u$ are
$$\langle (5,3,8), (6,4,11), u \rangle, \quad \langle (5,3,8), (5,4,12), u \rangle, \quad \langle (0,1,4), (5,4,12), u \rangle, \quad \langle (6,4,11), u, (7,6,18) \rangle, \quad \langle (0,1,4), u, (7,6,18) \rangle,$$
so the link of $u$ is the 5-cycle $(5,3,8)$, $(6,4,11)$, $(7,6,18)$, $(0,1,4)$, $(5,4,12)$. The cone $\langle (5,2,4), (10,3,4), u' \rangle$ is a cone of $\Lambda$, so $(5,2,4)$ is joined to $u'$. Finally
$$\kappa = \langle (5,2,4), (5,3,8), (6,4,11) \rangle$$
is a cone of $\Lambda$. Its rays $(5,3,8)$ and $(6,4,11)$ are joined to $u$, and its ray $(5,2,4)$ is joined to $u'$. The rays $(5,2,4) = a_1 + a_3$ and $(5,3,8) = 2 a_1 + a_3$ lie in the facet $\langle a_1, a_3 \rangle$, so they are not interior, and $(6,4,11)$ has degree 6. So case (2) of Corollary 3.28.8 applies to $\kappa$. $\square$

Each cone used in the proof has determinant $\pm 1$, which the reader can check (Exercise 1). Case (1) of Corollary 3.28.8 does not apply: $u$ and $u'$ are not joined. Note 93 found by an exhaustive test that this certificate is the only one among the 11426 replayed certificates of notes 90 and 91 with no pivot set. All the others have a pivot set, and in none of them are two interior rays of odd degree joined.

The obstruction is local. Two interior rays of degree 5 at distance 2 in the slice have neighbours that cover a whole triangle. It is not an obstruction for the class of $F_4$.

**Example 3.28.11 (one star removes the obstruction).** Make the common star of $\Lambda$ and $F$ at the 2-face $\langle (0,1,4), (5,4,12) \rangle = \langle a_1, 3 a_1 + a_3 \rangle$, which lies in the facet $\langle a_1, a_3 \rangle$. By Lemma 3.28.12 below the result is a certificate of depth 19, and research note 92 checked it: $F$ has 46 stars and $\Lambda$ has 25 cones. The 2-face is opposite to $u$ in the cone $\langle (0,1,4), (5,4,12), u \rangle$, so by Lemma 3.28.9(2) the degree of $u$ goes up to 6, and Lemma 3.28.7 no longer forces $u$ into $T$. The new fan has the pivot set
$$T = \{(5,3,8), (5,5,16), (6,3,7), (7,6,18), (16,5,7), (16,6,11), (26,7,7)\},$$
with $m = 7$. Note 93 checked with its own program that 7 is the least number of rays of a pivot set of this fan, and that this $T$ is the only pivot set with 7 rays. Of the 68 possible common stars at one face, 12 give a fan with a pivot set: 9 with least $m = 7$ and 3 with least $m = 8$. If we make the common stars at all 24 cones of dimension 3 instead, we get a certificate of depth 42 with 72 cones and least $m = 24$. So $F_4$ has certificates with a pivot set, but none with a small one is known.

### Common stars

**Lemma 3.28.12 (common stars).** Let $(\Lambda, F)$ be a certificate for $\sigma$ and let $f$ be a cone of $\Lambda$. Let $\Lambda^f$ and $F^f$ be the stars of $\Lambda$ and of $F$ at $f$. Then $(\Lambda^f, F^f)$ is a certificate for $\sigma$. If we make such common stars at all the 3-dimensional cones of $\Lambda$, in any order, then the new rays form a pivot set of the result, and $m$ is the number of 3-dimensional cones of $\Lambda$.

Lean: none yet

*Proof.* The cone $f$ is a cone of $F$, since $\Lambda \subseteq F$. By the proof of Proposition 3.28.1(3), $F|_\sigma = \Lambda$. So the cones of $F$ that contain $f$ and lie in $\sigma$ are the cones of $\Lambda$ that contain $f$, and their pieces are the new cones of $\Lambda^f$. As in the proof of Proposition 3.28.1(2), a piece of a cone of $F$ that does not lie in $\sigma$ does not lie in $\sigma$. The cones of $\Lambda$ that do not contain $f$ are cones of $F$ that do not contain $f$, so they stay in $F^f$. So $\Lambda^f \subseteq F^f$. The fan $\Lambda^f$ is a star sequence of $\sigma$ and $F^f$ is a star sequence of $\tau$, and both are regular. Each cone of $\Lambda^f$ is a cone of the star sequence $F^f$ of $\tau$, so it is directly reachable, which is all that Definition 3.26.15 asks.

For the second claim, a star at a 3-dimensional cone changes only this cone. So the stars at the distinct 3-dimensional cones of $\Lambda$ do not interact, and each of them is at a cone of the current fan. The star at $C = \langle x, y, z \rangle$ gives the cones $\langle c_C, x, y \rangle$, $\langle c_C, y, z \rangle$ and $\langle c_C, x, z \rangle$, with the new ray $c_C$. Each new cone contains exactly one of the new rays, so the set of the rays $c_C$ is a pivot set by Lemma 3.28.5. $\square$

**Corollary 3.28.13 (the hypotheses of Theorem 3.27.17 are automatic).** If $\sigma$ has a certificate, then $\sigma$ has a certificate $(\Lambda, F)$ with a pivot set $T$, and $\Lambda_0 = \Lambda$, $F_0 = F$ and the rays of $T$ satisfy the hypotheses of Theorem 3.27.17. So $\sigma$ has data that satisfy the hypotheses of Theorem 3.27.17 if and only if $\sigma$ has a certificate.

Lean: none yet

*Proof.* The first claim is Lemma 3.28.12. For the second claim apply Proposition 3.27.18, (2) implies (1). The converse is Theorem 3.27.17. $\square$

So the existence of a pivot set is no restriction. What can make Theorem 3.27.17 useful is a small $\Lambda_0$ and a small $T$.

### The number of pivots

**Definition 3.28.14 (witnesses with $k$ pivots).** Let $k \ge 1$. A *witness with at most $k$ pivots* for $\sigma$ is a triple $(\Lambda_0, T, F_0)$, where $\Lambda_0$ is a star sequence of $\sigma$, $T$ is a pivot set of $\Lambda_0$ with $|T| \le k$, $F_0$ is a star sequence of $\tau$ that has each ray of $T$ as a ray, and the conditions (b) and (c) of Theorem 3.27.17 hold for the rays of $T$. *Conjecture* $\mathrm{C}(k)$ says that every regular 3-dimensional cone $\sigma \subseteq \tau$ has a witness with at most $k$ pivots.

Research note 92 states $\mathrm{C}(k)$ as a problem on the fan $F_0$ alone: find $F_0$ such that each 3-dimensional cone of $F_0$ whose interior meets the interior of $\sigma$ meets the interior of only one region $|\mathrm{St}_{\Lambda_0}(b)|$, has $b$ as a ray, and has no other ray in $T$. Its Lemma 92.7 proves that this is equivalent to (b) and (c), and note 93 checked the proof. We do not use this form.

**Proposition 3.28.15 (witnesses are certificates with few pivots).** Let $k \ge 1$. The following are equivalent.

1. $\sigma$ has a witness with at most $k$ pivots.
2. $\sigma$ has a certificate $(\Lambda, F)$ such that $\Lambda$ has a pivot set with at most $k$ rays.

Lean: none yet

*Proof.* (2) implies (1): take $\Lambda_0 = \Lambda$, $F_0 = F$ and the given pivot set. Condition (b) holds since the cones of $\Lambda$ are cones of $F$, and (c) holds by the proof of Proposition 3.27.18, (2) implies (1).

(1) implies (2): Theorem 3.27.17 gives a certificate $(\Lambda, F)$, and it remains to see that $T$ is still a pivot set of the final $\Lambda$. This follows from the proof of Proposition 3.27.18, and here is a direct argument. In the construction of Theorem 3.27.17, the fan $\Lambda_0$ changes only by stars at 2-faces $\langle x, x' \rangle$ such that $\langle b, x, x' \rangle$ is a cone of the current $\Lambda$ for some $b \in T$. Assume that $T$ is a pivot set before such a star. The rays $x$ and $x'$ are joined to $b$, so they are not in $T$. If the 2-face is interior, it lies in one more cone $\langle x, x', z \rangle$, and this cone contains exactly one ray of $T$, so $z \in T$. The new ray $s = x + x'$ is joined to $b$ and, in the interior case, to $z$, so $s \notin T$. The new cones are $\langle b, x, s \rangle$ and $\langle b, s, x' \rangle$, and in the interior case also $\langle z, x, s \rangle$ and $\langle z, s, x' \rangle$. Each of them contains exactly one ray of $T$. The other cones do not change. By Lemma 3.28.5, $T$ is a pivot set after the star. $\square$

Note 93 checked the second half by computation. For each of the 14 witnesses of Proposition 3.28.18 below, $T$ is a pivot set of the final $\Lambda$, and no pivot set of this $\Lambda$ has fewer rays.

**Corollary 3.28.16 (what the bound means).** For each $k \ge 1$, Conjecture $\mathrm{C}(k)$ is equivalent to the statement: every regular 3-dimensional cone $\sigma \subseteq \tau$ has a certificate whose fan $\Lambda$ is the union of at most $k$ closed stars of rays with no common interior points. Each $\mathrm{C}(k)$ implies toric $\mathrm{RSF}_3$, and $\sigma$ has a witness with at most $k$ pivots for some $k$ if and only if $\sigma$ has a certificate.

Lean: none yet

*Proof.* The first claim is Proposition 3.28.15 with Lemma 3.28.6. The second claim follows from Proposition 3.28.15. The third claim follows from Proposition 3.28.15 and Lemma 3.28.12. $\square$

Research note 92 stated the second claim as Theorem 92.12, a reduction of $\mathrm{RSF}_3$ to $\mathrm{C}(k)$, and described $\mathrm{C}(k)$ as a statement about one fan of $\tau$. Corollary 3.28.16 shows that this is not right. The theorem is true, and it is not circular, but it says that a stronger form of $\mathrm{RSF}_3$ implies $\mathrm{RSF}_3$. The conjecture $\mathrm{C}(k)$ is a bounded form of $\mathrm{RSF}_3$ itself, and it is not an easier problem. The content of $\mathrm{C}(k)$ is the bound on the size of the pivot set. The real use of Theorem 3.27.17 is different. It compresses a certificate to a witness with a small $\Lambda_0$, and a search for witnesses is much smaller than a search for certificates.

### A necessary condition

The pivot set of a certificate is controlled by the stars of $\tau$ that make its rays.

**Proposition 3.28.17 (where a pivot comes from).** Let $(\Lambda, F)$ be a certificate and let $b$ be a ray of $\Lambda$ that is not a ray of $\tau$. Let $G$ be the stage of the star sequence $F$ just before the star that makes $b$, let $f$ be the center of this star, and let $X_b$ be the set of the cones of $G$ that contain $f$. Then:

1. $b = \sum f$, the sum of the rays of $f$, and $b \in \sigma$;
2. $X_b$ is one directly reachable regular cone, or two directly reachable regular cones with the common 2-face $f$;
3. $|\mathrm{St}_\Lambda(b)| \subseteq |\mathrm{St}_F(b)| \subseteq \bigcup X_b$.

So if $\Lambda$ has a pivot set $T$ with $|T| \le k$ and no ray of $T$ is a ray of $\tau$, then $\sigma$ is covered by at most $k$ sets $\bigcup X_b$ of this kind, and the closed stars $|\mathrm{St}_\Lambda(b)| \subseteq \bigcup X_b$ tile $\sigma$.

Lean: none yet

*Proof.* (1) The new ray of a star at $f$ is $\sum f$, and $b$ is a ray of $\Lambda$, so $b \in \sigma$. (2) The center $f$ is a face of a cone of $G$ of dimension 2 or 3, since a star at a ray changes nothing. If $f$ has dimension 3, then $X_b = \{f\}$. If $f$ has dimension 2, then one or two 3-dimensional cones of $G$ contain $f$, and two of them have the common 2-face $f$. They are cones of a star sequence of $\tau$, so they are regular and directly reachable. (3) The first inclusion holds since $\Lambda \subseteq F$. Just after the star at $f$, the cones that contain $b$ are the pieces of the cones of $X_b$ that contain $b$. A later star replaces a cone that contains $b$ by pieces that lie in it. So every cone of $F$ that contains $b$ lies in a cone of $X_b$. The last statement follows from Lemma 3.28.6. $\square$

Research note 93 states the necessary condition (N$_k$): $\sigma$ is covered by at most $k$ sets, each of them one directly reachable regular cone or the union of two such cones with a common 2-face. But (N$_k$) in this form holds for every $\sigma$, since $\tau$ itself is such a set. The content of Proposition 3.28.17 is in the link between $b$, the face $f$ and the region $|\mathrm{St}_\Lambda(b)|$: the pivot is the sum of the rays of $f$, and its closed star must fit in $\bigcup X_b$. For $k = 1$ this refined condition is exactly the state search of Proposition 3.27.16, where the pivot must lie in $B(\sigma)$ by Proposition 3.27.11, and Theorem 3.27.22 shows that it is a real obstruction. It does not depend on a search for certificates, so it is the natural tool for a lower bound on $m$. Section 3.30 states it as the condition $(\mathrm{N}_k^{\rm ref})$ (Definition 3.30.1) and shows that $\sigma_n$ fails it for $n \ge 4k + 2$ (Theorem 3.30.10).

### Computations

The computations are exact integer computations. Research note 92 searched for witnesses as follows. It lists all star sequences $\Lambda_0$ of $\sigma$ up to a given depth, as fans without repetition, together with all their pivot sets. Up to depth 4 there are 3101 pairs $(\Lambda_0, T)$, up to depth 5 there are 24356, and up to depth 6 there are 205100. These numbers depend only on the shape and not on $\sigma$. For each pair it searches for $F_0$, best first, with stars only at the faces of the cones of $F_0$ that still fail the conditions, and with at most 30000 states. The restriction of the stars is a heuristic, and it is not proved that it loses no solution. So "not found" means "not found by this search". Each witness found is checked again on the full fans, and the certificate of the proof of Theorem 3.27.17 is built from it and replayed. Research note 93 repeated the checks and the construction with its own program, which shares no code with notes 90 to 92.

**Proposition 3.28.18 (the witnesses found).** The following witnesses satisfy the hypotheses of Theorem 3.27.17 with a pivot set $T$. "Blind" means the list of all $(\Lambda_0, T)$ with $\Lambda_0$ of depth at most 4. "Prefix" means that $\Lambda_0$ is a beginning of the star sequence of $\sigma$ of a known certificate. "Restricted" means that $\Lambda_0$ consists of stars at 2-faces that contain $a_2$ or $a_3$. The last three columns describe the certificate of Theorem 3.27.17.

| class | rays of $\sigma$ | source | depth of $\Lambda_0$ | $m$ | $T$ | stars of $F_0$ | depth | stars of $F$ | cones of $\Lambda$ |
|---|---|---|---|---|---|---|---|---|---|
| $F_2$ | $(0,1,2), (1,2,3), (3,1,0)$ | blind | 1 | 1 | $(4,3,3)$ | 9 | 2 | 10 | 3 |
| $\sigma_4$ | $(0,1,3), (1,1,2), (4,1,0)$ | blind | 3 | 2 | $(4,3,6), (8,3,3)$ | 16 | 4 | 17 | 5 |
| $\sigma_4$ | same | prefix | 3 | 2 | $(1,1,2), (8,3,3)$ | 13 | 6 | 22 | 8 |
| $F_3 = A$ | $(0,1,3), (1,2,5), (4,1,0)$ | blind | 4 | 2 | $(5,4,8), (8,3,3)$ | 17 | 9 | 24 | 11 |
| $F_3 = A$ | same | prefix | 6 | 2 | $(5,4,8), (8,3,3)$ | 17 | 9 | 24 | 11 |
| $\sigma_5$ | $(0,1,4), (1,1,3), (5,1,0)$ | prefix, restricted | 6 | 3 | $(1,1,3), (6,2,3), (15,4,4)$ | 20 | 12 | 42 | 14 |
| $O_1$ | $(0,1,3), (1,2,5), (5,2,0)$ | prefix | 11 | 6 | in note 92 | 30 | 17 | 38 | 23 |
| $O_2$ | $(0,2,3), (1,4,5), (5,3,0)$ | prefix | 11 | 6 | in note 92 | 30 | 17 | 38 | 23 |
| $X_1$ | $(0,2,5), (4,3,1), (5,4,2)$ | blind | 3 | 2 | $(0,2,5), (9,9,8)$ | 16 | 9 | 33 | 11 |
| $X_2$ | $(0,2,5), (4,3,2), (5,4,3)$ | blind | 3 | 2 | $(0,2,5), (9,9,10)$ | 16 | 11 | 38 | 13 |
| $X_3$ | $(0,3,5), (4,3,2), (5,4,3)$ | blind | 3 | 2 | $(0,3,5), (9,10,10)$ | 16 | 11 | 38 | 13 |

The following searches found no witness: the blind search up to depth 4 for $D_{10}$, $O_1$, $O_2$, $\sigma_5$, $\sigma_6$, $\sigma_7$ and $F_4$; the blind search up to depth 5 for $D_{10}$ and $O_1$; the restricted search up to depth 8 with $m \le 3$ for $\sigma_6$; and the restricted search with stars at 2-faces that contain any ray of $\sigma$, up to depth 6 with $m \le 3$, for $F_4$. In these searches no pair reached the limit of states.

Lean: none yet

*Proof.* Exact computations from research note 92. Research note 93 checked (a), (b) and (c) of Theorem 3.27.17 on the full fans for all 14 witnesses of note 92, with repetitions (the table lists the distinct data), built the certificates with its own program, and replayed them: each one is regular, has $\Lambda \subseteq F$, and has each cone of $\Lambda$ directly reachable by the column game of Lemma 3.26.12. The depths, the numbers of stars and the numbers of cones agree with note 92. As a negative test, note 93 removed one star of $F_0$ at a time, which gave 56 variants that are still star sequences, and none of them passes. $\square$

Two things are visible in the table. For $\sigma_4$, $F_2$, $F_3$, $X_1$, $X_2$ and $X_3$ two pivots are enough, and $\Lambda_0$ has depth 3 or 4, much less than the depth of the certificate. So here the compression of Theorem 3.27.17 is real. For $O_1$ and $O_2$ the witness has $m = 6$ and a $\Lambda_0$ of depth 11, almost the whole certificate of depth 12, so there is no gain. The side of $\tau$ is short in all cases, 13 to 20 stars, and it consists of a few chains of stars at 2-faces that walk to the pivots along the paths of Lemma 3.28.3. For $X_1$ one chain is the stars at $\langle (1,1,1), w \rangle$ with $w = (2,2,1), (3,3,2), \dots, (8,8,7)$, which end at the pivot $(9,9,8) = a_1 + a_2 + a_3$.

The least $m$ of the certificates found also grows. Over the replayed certificates of notes 90 to 92 the least $m$ is 1, 2, 3 and 6 for $\sigma_3$, $\sigma_4$, $\sigma_5$ and $\sigma_6$, and 1, 2 and 7 for $F_2$, $F_3$ and $F_4$ (the last one at depth 19). In these certificates the number of cones of $\Lambda$ divided by the least $m$ has a mean between 2.50 and 3.41 at each depth from 3 to 16. So $m$ follows the number of cones of the certificate that the search finds, and the searches do not minimize $m$. These values are upper bounds for the least $m$ of the class, and they say nothing about a lower bound.

**Proposition 3.28.19 (the status of $\mathrm{C}(k)$).**

1. $\mathrm{C}(1)$ is false.
2. For each $k \ge 2$, $\mathrm{C}(k)$ is false: the cone $\sigma_{4k+2}$ has no witness with at most $k$ pivots (Corollary 3.30.12). No class with entries at most 6 is known to need more than 2 pivots.

Lean: none yet

*Proof.* (1) By Proposition 3.28.15, a witness with one pivot for $\sigma$ gives a certificate whose cones all contain one ray, and by Proposition 3.27.11 then $\sigma$ is a pivot cone. By Theorem 3.27.22 the cone $O_1$ is not a pivot cone. (2) The first claim is Corollary 3.30.12, which uses the lower bound $m \ge \frac{n-1}4$ for all pivot sets of all certificates of $\sigma_n$ (Corollary 3.30.11). For the second claim: the classes with entries at most 6 include $\sigma_3, \dots, \sigma_6$, for which the bound gives at most 2, and the values above 2 in the data are least values over the certificates found, not over all certificates. $\square$

Research note 92 stated $\mathrm{C}(3)$ and said that $k = 3$ is the smallest value that the data allow. Note 93 showed that the data do not exclude $k = 2$. Its view is that a fixed $k$ is not plausible on present evidence, since the only known way to lower $m$ is a small $\Lambda_0$, and for $\sigma_6$, $\sigma_7$, $F_4$, $O_1$ and $O_2$ the searches found none with $m \le 3$. This was an opinion and not a result when it was written. Corollary 3.30.12 now proves that no fixed $k$ works.

### What is open

1. Conjecture $\mathrm{C}(k)$ for a fixed $k \ge 2$. This item is closed: $\mathrm{C}(k)$ is false for every $k$, by the cone $\sigma_{4k+2}$ (Corollary 3.30.12).
2. A lower bound $m \ge 3$ for the pivot sets of all certificates of one class. This item is closed for the cones $\sigma_n$ with $n \ge 10$, if they have certificates (Corollary 3.30.11). For the classes with entries at most 6 it is open.
3. A decision procedure for the refined necessary condition of Proposition 3.28.17 for each $\sigma$ and $k$, as Proposition 3.27.16 does for $k = 1$. For $\sigma_n$ the projection bound of Theorem 3.30.10 suffices for a lower bound, but it is not a decision procedure.
4. Completeness of the restricted search for witnesses of Proposition 3.28.18.
5. A uniform witness for $\sigma_n$ or for $F_k$. The witness of $\sigma_5$ has its $\Lambda_0$ in a fan around the ray $(5,1,0)$, but the witnesses of $\sigma_4$ have $m = 2$, and no pattern is known.
6. A rule that glues witnesses for the two halves of a star of $\sigma$ without a common fan $F_0$. Research note 92 proves that the gluing works with a common $F_0$, and note 93 adds the hypothesis that the union of the two fans $\Lambda_0$ is a star sequence of $\sigma$.
7. Certificates for $\sigma_7$ and for $F_5$.

### Exercises

1. Check that the cones $\langle (5,3,8), (6,4,11), u \rangle$, $\langle (0,1,4), (5,4,12), u \rangle$, $\langle (5,2,4), (10,3,4), u' \rangle$ and $\kappa$ of Proposition 3.28.10 have determinant $\pm 1$, and write their rays in the basis $a_1, a_2, a_3$ of $F_4$.
2. Let $\Lambda$ be the star of $\sigma$ at $\sigma$, with the new ray $c$. Make the stars at its three cones, as in the second part of Lemma 3.28.12. List the 9 cones, check that the three new rays form a pivot set, and show that no ray lies in all 9 cones.
3. Let $\Lambda$ be the star of $\sigma$ at $\langle a_1, a_2 \rangle$, with the new ray $s$. Show that $T = \{a_3\}$ is a pivot set and that $a_1 \notin T$ lies in only one cone. Explain why this does not contradict Lemma 3.28.7.
4. Prove Lemma 3.28.9(2) and (3) by drawing the slice.
5. Show that the condition (N$_k$) of research note 93, as stated after Proposition 3.28.17, holds for every $\sigma$ and every $k \ge 1$.
6. Prove in detail the case of Proposition 3.28.1(2) where $c$ is a 2-face in a facet of $\sigma$: describe the cone of $F$ on the other side of the facet and its two pieces.
7. Use Corollary 3.28.2 to show that the following statement implies toric $\mathrm{RSF}_3$: for each star sequence $F$ of $\tau$ that refines $\sigma$, the fan $F|_\sigma$ has a star sequence that is a star sequence of $\sigma$.

### Status

The results are new in research note 92, and research note 93 is a referee report on it. Note 93 checked each proof and found Propositions 3.28.1 and 3.28.10, Lemmas 3.28.3, 3.28.5 and 3.28.7, Lemma 92.7 of note 92 and Lemma 3.28.12 correct. It made 9 fixes. Fix 1 adds the proof of Lemma 3.28.5(3). Fix 2 replaces case (2) of Corollary 3.28.8 by a form that does not use $T$. Fix 3 corrects the parity of the degree in Lemma 3.28.9. Fix 4 notes that the six facet planes suffice for the test of disjoint interiors in the search. Fix 5 adds direct reachability to the proof of Lemma 3.28.12. Fix 6 states Corollary 3.28.13 and removes the claim that $\mathrm{C}(k)$ is a statement about one fan of $\tau$. Fix 7 adds a hypothesis to the gluing rule of item 6 of the open list. Fix 8 corrects the range of the ratio of cones to pivots. Fix 9 withdraws the claim that the data need $k = 3$. Note 93 also proved Proposition 3.28.15 and stated the necessary condition after Proposition 3.28.17, and it replayed all witnesses, the 11426 certificates of the parity test and the certificates of $F_4$ with its own program, with agreement in every number. This section adds the remark that (N$_k$) in the form of note 93 holds for every cone, and it gives the refined form of Proposition 3.28.17. The map has nodes for Definition 3.25.8 and Theorem 3.25.12, which this section uses, and no nodes yet for its new statements. None of the statements has a Lean proof. An outside expert has not yet read the result. Section 3.30, from research note 98, proves a lower bound for the number of pivots of $\sigma_n$ and $F_k$, and shows that $\mathrm{C}(k)$ is false for every $k$. This changes Proposition 3.28.19(2) and items 1 to 3 of the open list above.

### Notes and references

The results are in research note 92, which continues notes 88 to 91, and in research note 93, the referee report on note 92. Sections 3.26 and 3.27 give the setting, the certificates, the Pivot Theorem and the multi-pivot theorem. Research note 92 compares the problem with the literature, and note 93 checked the citations without access to the sources. We list the items that this section uses, with the status of note 93.

- [Cut97] S. D. Cutkosky, Local factorization of birational maps, Adv. Math. 132 (1997), 167-315. Local strong factorization for 3-folds in characteristic 0. It treats a map near one valuation, while $\mathrm{RSF}_3$ needs a statement on all of $\sigma$.
- [Dan83] V. I. Danilov, Math. USSR-Izv. 21 (1983), 269-280. Weak factorization of toric maps in dimension 3.
- [DSK11] S. Da Silva and K. Karu, On Oda's strong factorization conjecture, Tohoku Math. J. 63 (2011), 163-182. Partial results, and the statement that the conjecture is open in dimension at least 3.
- [Ewa87] G. Ewald, Abh. Math. Sem. Univ. Hamburg 57 (1987), 193-201. Weak factorization of toric maps in dimension 3. Research note 93 could not check the volume, the year and the pages against the journal, so they are not confirmed.
- [Gow05] R. Goward, A simple algorithm for principalization of monomial ideals, Trans. Amer. Math. Soc. 357 (2005), 4805-4812. The proof of Proposition 3.28.1(1) uses it for the binomial ideals of the facet forms of $\sigma$. Note 93 asks for a precise reference for this use, with centers that are orbit closures.
- [Kar03] K. Karu, Local strong factorization of toric birational maps, J. Algebraic Geom. 14 (2005), 165-175.
- [Oda88] T. Oda, Convex Bodies and Algebraic Geometry, Springer, 1988, Section 1.6.

Weak factorization in all dimensions and the weighted form of the conjecture of Oda are in the references of Section 3.27. Weak factorization allows blowdowns in the middle of the sequence, and $\mathrm{RSF}_3$ allows only blowups on each side, so it does not apply directly. Note 93 could not check the volume and the exact statement of [AP26] of Section 3.27, nor whether [AKMW02] itself records the gap in the proof of Morelli.
