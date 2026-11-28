---
title: A lower bound for the number of pivots, and the rises of the residual slope
nodes: [SG000000CG, SG000000CK, SG000000BG, SG000000CX]
sources: [DSK11, Kar03]
status: drafted
drafted_by: writer
reviewed_by: []
---
## A lower bound for the number of pivots, and the rises of the residual slope

This section reports the thirtieth research result. It has two parts. The first part is from the track FP (tamnd/singularity#320). It continues Section 3.28 and settles the question that Section 3.28 left open: the bound $\mathrm{C}(k)$ on the number of pivots of certificates (Definition 3.28.14) is false for every $k$. The cone $\sigma_n$ of Proposition 3.27.21 needs at least $\frac{n-1}4$ pivots, and $F_k$ needs at least $\frac{k+1}4$. The second part is from the track M2 (tamnd/singularity#287). It studies the rises of the residual slope $\omega$ of Volume 7, Section 4.4, at a solvable vertex for the weight $(1,1,1)$. It proves that the quantity $h$ of Volume 7, Section 4.5, is not defined at the known rises, and it reports the computed trees. The second part does not settle its question, and the open question is stated at its end. Both parts are the tasks T4 and T3 of the review of the road (tamnd/singularity#334).

The results come from research note 98. Before this section was written, the proofs of the main results of note 98 were checked again from first principles, and the main lemmas were repeated by computation with a new program. The check is research note 98a. It found the main results correct, and it found one gap in a statement, which this section fixes (see the Status).

We keep the notation of Sections 3.26 to 3.28. So $\tau = \langle e_1, e_2, e_3 \rangle$ is the octant in $N = \mathbb{Z}^3$, $\sigma \subseteq \tau$ is a regular 3-dimensional cone, a certificate $(\Lambda, F)$ is as in Definition 3.26.15, a cone is *directly reachable* if it is a cone of some star sequence of $\tau$ (Definition 3.26.3), and $\mathrm{St}_G(b)$ and $|\mathrm{St}_G(b)|$ are as in Definition 3.27.8. A pivot set is as in Definition 3.28.4. For a cone $f$ we write $\sum f$ for the sum of its rays. In the second part we use the notation of Volume 7, Sections 4.4 and 4.5.

### Motivation

Section 3.28 showed that the multi-pivot theorem 3.27.17 does not reduce toric $\mathrm{RSF}_3$ to a smaller problem: data that satisfy its hypotheses exist exactly when a certificate exists. What is left is the size of the pivot set. Conjecture $\mathrm{C}(k)$ says that each $\sigma$ has a certificate with a pivot set of at most $k$ rays (Proposition 3.28.15). The searches found 1, 2, 3 and 6 pivots for $\sigma_3, \dots, \sigma_6$, but these are the least values over the certificates found, and they give no lower bound. A lower bound must hold for all certificates, and there is no way to list them.

Proposition 3.28.17 gives a way around this. Each pivot $b$ is the new ray of one star of $\tau$, and its closed star must fit in the one or two cones around the center of this star. This is a condition on cones of $\tau$, and it does not mention the rest of the certificate. Section 3.28 stated this refined condition and asked whether it can be decided for $\sigma_n$. Here it is decided, by an estimate on the long and thin shape of $\sigma_n$. The cone $\sigma_n$ is a needle along the edge $\langle e_1, e_3 \rangle$ of $\tau$. A directly reachable cone that is long along the needle must have its apex at height 1 and two rays at height 0, and the only lattice points of $\sigma_n$ at height 1 are its three rays. So the region of each pivot is short, and many regions are necessary to cover the needle.

The second part is about the track M2. Volume 7, Theorems 4.4.7 and 4.4.8, show that $\omega$ can go up under Rule 61.9', and Volume 7, Proposition 4.5.30, shows that each such rise needs a solvable vertex of $z'$ for the weight $(1,1,1)$ at the new point. Conjecture 4.4.6 of Volume 7 would follow from a bound on the number of rises along a branch, together with an invariant that controls the runs between the rises. The first candidate for such an invariant is the quantity $h$ of Volume 7, Lemma 4.5.6. The second part shows that $h$ is not available at the rises, and it gives the computed data on the rises.

A reader needs Sections 3.26 to 3.28 for the first part and Volume 7, Sections 4.4 and 4.5, for the second part.

### The refined condition

**Definition 3.30.1 (the refined condition).** Let $k \ge 1$. The cone $\sigma$ satisfies $(\mathrm{N}_k^{\rm ref})$ if there are $j \le k$ triples $(X_i, f_i, R_i)$ with the following properties.

1. $X_i$ is a set of directly reachable regular 3-dimensional cones, and $f_i$ is a cone of dimension 2 or 3. There are three cases: $X_i = \{f_i\}$ with $\dim f_i = 3$; or $X_i = \{K\}$, where $f_i$ is a 2-face of $K$ that lies in $\partial \tau$; or $X_i = \{K, K'\}$ with $K \ne K'$ and $K \cap K' = f_i$ a 2-face.
2. $b_i = \sum f_i$ lies in $\sigma$, and the $b_i$ are distinct.
3. $R_i$ is a union of 3-dimensional cones of a regular fan, and each of these cones has $b_i$ as a ray.
4. $R_i \subseteq \sigma \cap \bigcup X_i$, the sets $R_i$ have pairwise no common interior points, their union is $\sigma$, and $b_i \notin R_l$ for $l \ne i$.

The condition (N$_k$) of research note 93, stated after Proposition 3.28.17, keeps only the covering of $\sigma$ by the sets $\bigcup X_i$. It holds for every $\sigma$, since $X = \{\tau\}$ is allowed. In the refined condition this trivial cover is not available in general: it needs $\sum \tau = (1,1,1) \in \sigma$, and for the cones $\sigma_n$ with $n \ge 4$ this is false (Lemma 3.30.4).

We now prove Proposition 3.28.17 again, in a form that gives the refined condition, and we make explicit one step that the proof in Section 3.28 leaves to the reader.

**Lemma 3.30.2 (a ray inside a cone).** Let $G$ be a fan, let $\rho = \mathbb{R}_{\ge 0} b$ be a ray of $G$, and let $c$ be a cone of $G$ with $b \in c$. Then $\rho$ is a face of $c$. If $c$ is simplicial, then $b$ is a multiple of one of the generators of $c$.

Lean: none yet

*Proof.* The cones $\rho$ and $c$ are cones of one fan, so $\rho \cap c$ is a face of $\rho$ and a face of $c$. It contains the point $b \ne 0$, and the only face of $\rho$ that contains $b$ is $\rho$. So $\rho = \rho \cap c$ is a face of $c$. The 1-dimensional faces of a simplicial cone are the rays through its generators. $\square$

**Proposition 3.30.3 (where a pivot comes from).** Let $(\Lambda, F)$ be a certificate for $\sigma$, let $b$ be a ray of $\Lambda$ that is not a ray of $\tau$, let $G$ be the stage of $F$ just before the star that makes $b$, let $f$ be its center, and let $X_b$ be the set of the 3-dimensional cones of $G$ that contain $f$.

1. $\dim f \in \{2, 3\}$, $b = \sum f$ and $b \in \sigma$.
2. $X_b = \{f\}$ if $\dim f = 3$. If $\dim f = 2$, then $X_b$ has one cone if $f \subseteq \partial \tau$ and two cones with the common 2-face $f$ otherwise. The cones of $X_b$ are directly reachable and regular.
3. Every cone of $F$ that has $b$ as a ray lies in a cone of $X_b$. So $|\mathrm{St}_\Lambda(b)| \subseteq |\mathrm{St}_F(b)| \subseteq \bigcup X_b$, and $|\mathrm{St}_\Lambda(b)| \subseteq \sigma \cap \bigcup X_b$.
4. Let $T$ be a pivot set of $\Lambda$ with $|T| \le k$, such that no ray of $T$ is a ray of $\tau$. Then the triples $(X_b, f, |\mathrm{St}_\Lambda(b)|)$, $b \in T$, satisfy Definition 3.30.1. So $\sigma$ satisfies $(\mathrm{N}_k^{\rm ref})$.

Lean: none yet

*Proof.* (1) The rays of a fan are never removed by a star, and $b$ is a ray of $\Lambda \subseteq F$ that is not a ray of $\tau$. So some star of the sequence $F$ makes $b$ for the first time, and $G$ and $f$ are well defined. A star at a ray does not change the fan, so $\dim f \ge 2$, and $\dim f \le 3$. The new ray of a star at $f$ is $\sum f$. Since $b$ is a ray of $\Lambda$, $b \in |\Lambda| = \sigma$.

(2) If $\dim f = 3$, the only 3-dimensional cone of $G$ that contains $f$ is $f$. Let $\dim f = 2$. The fan $G$ is a star sequence of $\tau$, so its support is $\tau$ and each of its cones is a face of a 3-dimensional cone. A 2-dimensional cone of a fan with support $\tau$ lies in exactly two 3-dimensional cones if its relative interior meets the interior of $\tau$, and in exactly one if it lies in $\partial \tau$. Two such cones meet in a common face that contains $f$, and this face is $f$. The cones of $G$ are cones of a star sequence of $\tau$, so they are directly reachable, and they are regular because each star keeps a fan regular.

(3) Write $G_0 = G$, let $G_1$ be the star of $G$ at $f$, and let $G_1, G_2, \dots, G_r = F$ be the remaining stages. We prove by induction on $s \ge 1$ that each cone of $G_s$ that has $b$ as a ray lies in a cone of $X_b$. For $s = 1$: the point $b$ lies in the relative interior of $f$. If a cone $c'$ of $G$ contains $b$, then $c' \cap f$ is a face of $f$ that contains a point of the relative interior of $f$, so $c' \supseteq f$. So the cones of $G$ that do not contain $f$ do not contain $b$, and they are not changed by the star. The cones of $G_1$ that have $b$ as a ray are the new cones, and each of them is a piece of a cone of $G$ that contains $f$. So it lies in a cone of $X_b$. Let $s \ge 1$ and let $c$ be a cone of $G_{s+1}$ that has $b$ as a ray. If $c$ is a cone of $G_s$, the claim holds by induction. Otherwise $c$ is a piece of a cone $c_0$ of $G_s$ that contains the center of the star, and $c \subseteq c_0$. Then $b \in c_0$, and $b$ is a ray of $G_s$, so $b$ is a ray of $c_0$ by Lemma 3.30.2. By induction $c_0$, and so $c$, lies in a cone of $X_b$. This proves the claim for $F = G_r$. The first inclusion of (3) holds since $\Lambda \subseteq F$, and $|\mathrm{St}_\Lambda(b)| \subseteq |\Lambda| = \sigma$.

(4) Conditions (1) and (2) of Definition 3.30.1 are parts (1) and (2) of the proposition; the rays of $T$ are distinct, so the sums $b$ are distinct. Condition (3) holds since $\Lambda$ is a regular fan. For (4): $|\mathrm{St}_\Lambda(b)| \subseteq \sigma \cap \bigcup X_b$ by part (3). By Lemma 3.28.5 each 3-dimensional cone of $\Lambda$ contains exactly one ray of $T$, so the closed stars of the rays of $T$ cover $\sigma$ and two of them have no common interior point. Let $b, b' \in T$ with $b \ne b'$, and assume that $b' \in |\mathrm{St}_\Lambda(b)|$. Then $b'$ lies in a cone $c$ of $\mathrm{St}_\Lambda(b)$, and $b'$ is a ray of $c$ by Lemma 3.30.2. So $c$ contains the two rays $b$ and $b'$ of $T$, which is not possible. $\square$

The proposition is the same as Proposition 3.28.17, with two additions: the step from "a cone contains the point $b$" to "the cone has $b$ as a ray" is Lemma 3.30.2, and the case of one cone in (2) includes a 2-face in $\partial \tau$. Research note 98 also checked the proposition on 5940 stored certificates (Proposition 3.30.15).

### The needle $\sigma_n$

Let $n \ge 3$ and
$$\sigma_n = \langle A, B, C \rangle, \qquad A = (0, 1, n-1), \quad B = (1, 1, n-2), \quad C = (n, 1, 0),$$
as in Proposition 3.27.21. We write the coordinates as $(x, y, z)$, and we call $y$ the *height*. Put
$$\psi = x + z - (n-1)y, \qquad \varphi = n(n-1)y - (n-1)x - nz.$$
For a nonzero point $w$ of $\sigma_n$ put $\chi(w) = w_x / w_y$, the $x$-coordinate of the point where the ray through $w$ meets the plane $y = 1$. For a set $Y \subseteq \sigma_n$ the *extent* $\operatorname{ext}(Y)$ is the length of the smallest interval that contains $\chi(Y \setminus \{0\})$, with $\operatorname{ext}(Y) = 0$ if $Y \subseteq \{0\}$. For a cone $K$ put $I(K) = \chi(K \cap \sigma_n \setminus \{0\})$. If $K$ is convex, then $I(K)$ is an interval and its length is $\operatorname{ext}(K \cap \sigma_n)$.

**Lemma 3.30.4 (the needle).** Let $n \ge 3$.

1. $\det(A, B, C) = -1$, so $\sigma_n$ is regular, and $\sigma_n \subseteq \tau$.
2. Each nonzero point $w$ of $\sigma_n$ has $w_y > 0$, $0 \le \psi(w) \le w_y$, $\varphi(w) \ge 0$ and $w_x \ge 0$. So in the plane $y = 1$ the cone $\sigma_n$ lies in the slab $0 \le x + z - (n-1) \le 1$ and under the line $\frac xn + \frac z{n-1} = 1$ through $A$ and $C$.
3. $\chi(\sigma_n \setminus \{0\}) = [0, n]$, so $\operatorname{ext}(\sigma_n) = n$.
4. The lattice points of $\sigma_n$ at height 1 are $A$, $B$ and $C$, and $\sigma_n$ has no lattice point at height 0 other than 0.
5. No ray of $\tau$ lies in $\sigma_n$. For $n \ge 4$ the point $(1,1,1)$ does not lie in $\sigma_n$.

Lean: none yet

*Proof.* (1) Expand along the first row of the matrix with the rows $A, B, C$:
$$\det(A, B, C) = 0 - 1 \cdot (0 - n(n-2)) + (n-1)(1 - n) = n^2 - 2n - (n-1)^2 = -1.$$
The rays have nonnegative entries.

(2) The linear forms $y$, $\psi$, $y - \psi$, $\varphi$ and $x$ take the values $(1, 0, 1, 0, 0)$ at $A$, $(1, 0, 1, 1, 1)$ at $B$ and $(1, 1, 0, 0, n)$ at $C$. So they are nonnegative on $\sigma_n$, and $y > 0$ on $\sigma_n \setminus \{0\}$, since a nonnegative combination of $A, B, C$ with height 0 is 0. In the plane $y = 1$ the inequality $\varphi \ge 0$ is $\frac xn + \frac z{n-1} \le 1$.

(3) $\chi(A) = 0$, $\chi(C) = n$, and $\chi$ takes values in $[0, n]$ on the slice $\sigma_n \cap \{y = 1\}$, which is the triangle with the vertices $(0, n-1)$, $(1, n-2)$ and $(n, 0)$ in the coordinates $(x, z)$.

(4) By (1) the lattice points of $\sigma_n$ are the points $\alpha A + \beta B + \gamma C$ with $\alpha, \beta, \gamma \in \mathbb{Z}_{\ge 0}$, and their height is $\alpha + \beta + \gamma$.

(5) The rays $e_1$ and $e_3$ have height 0, and $\psi(e_2) = 1 - n < 0$. In the basis $A, B, C$ the coefficient of $C$ in $(1,1,1)$ is $3 - n$, which is negative for $n \ge 4$. $\square$

### Directly reachable cones on the needle

A 3-dimensional cone $\langle d_1, d_2, v \rangle \subseteq \tau$ has *type $(0,0,1)$* if $d_1$ and $d_2$ have height 0 and $v$ has height 1. The octant $\tau = \langle e_1, e_3, e_2 \rangle$ has type $(0,0,1)$. In the plane $y = 1$ such a cone is the wedge $v + \operatorname{cone}(d_1, d_2)$ with its apex at $v$, where $d_1$ and $d_2$ are directions with nonnegative entries in the $(x, z)$-plane.

**Lemma 3.30.5 (the replacement tree).** Let $K$ be a 3-dimensional cone of a star sequence of $\tau$. Then there are cones $\tau = K_0 \supseteq K_1 \supseteq \dots \supseteq K_m = K$ such that $K_{i+1}$ comes from $K_i = \langle r_1, r_2, r_3 \rangle$ by the replacement of one ray $r_a$ by $r_a + r_c$, for some $c \ne a$. Each $K_i$ is regular.

Lean: none yet

*Proof.* By induction on the number of stars. Let $G'$ be the star of $G$ at a cone $\kappa$ of $G$. A cone of $G$ that does not contain $\kappa$ is a cone of $G'$, and a star at a ray changes nothing. Let $c = \langle r_1, r_2, r_3 \rangle$ be a 3-dimensional cone of $G$ that contains $\kappa$. If $\kappa = \langle r_1, r_2 \rangle$, the pieces of $c$ are $\langle r_1 + r_2, r_2, r_3 \rangle$ and $\langle r_1, r_1 + r_2, r_3 \rangle$, and each comes from $c$ by one replacement. If $\kappa = c$, the pieces are $\langle r_1 + r_2 + r_3, r_2, r_3 \rangle$ and the two others of the same form, and $\langle r_1 + r_2 + r_3, r_2, r_3 \rangle$ comes from $c$ by the replacement $r_1 \mapsto r_1 + r_2$ and then the replacement $r_1 + r_2 \mapsto r_1 + r_2 + r_3$. A replacement gives a cone in the old cone and keeps the determinant. $\square$

So the 3-dimensional directly reachable cones are nodes of the tree with the root $\tau$, in which the six children of $\langle r_1, r_2, r_3 \rangle$ are the six single replacements, and each node contains its descendants. By Corollary 3.27.3 each node of the tree is directly reachable, but we do not need this.

**Lemma 3.30.6 (half strips).** Let $K = \langle d_1, d_2, v \rangle$ be a regular cone of type $(0,0,1)$, and let $K' = \langle d_1 + v, d_2, v \rangle$. Then $\operatorname{ext}(K' \cap \sigma_n) \le 2$. The same holds for $\langle d_1, d_2 + v, v \rangle$.

Lean: none yet

*Proof.* A point of $K'$ at height 1 is $a(d_1 + v) + \beta d_2 + c v$ with $a + c = 1$, that is, $v + a d_1 + \beta d_2$ with $0 \le a \le 1$ and $\beta \ge 0$. Write $d_2 = (p, 0, q)$, with $p, q \ge 0$ coprime, and put $L = qx - pz$. Then $L$ is constant along $d_2$, and along $d_1$ it changes by $q d_{1,x} - p d_{1,z}$. Expand $\det(d_1, d_2, v)$ along the column of the height: only $v$ has a nonzero height, so the determinant is $\pm(q d_{1,x} - p d_{1,z})$, and this is $\pm 1$ since $K$ is regular. So $L$ takes values in an interval of length 1 on the points of $K'$ at height 1.

At a point of $\sigma_n$ at height 1 we have $z = (n-1) - x + \psi$ with $0 \le \psi \le 1$, by Lemma 3.30.4(2). So
$$(p + q)x = L + p(n-1) + p\psi.$$
On the points of $K' \cap \sigma_n$ at height 1, the right side lies in an interval of length $1 + p$. So $x$ lies in an interval of length $\frac{1+p}{p+q}$. If $q \ge 1$ this is at most 1. If $q = 0$, then $d_2 = e_1$, since it is primitive, and the length is 2. The second claim is the first with $d_1$ and $d_2$ exchanged. $\square$

**Lemma 3.30.7 (long directly reachable cones).** Let $K$ be a 3-dimensional cone of a star sequence of $\tau$ with $\operatorname{ext}(K \cap \sigma_n) > 2$. Then $K$ has type $(0,0,1)$.

Lean: none yet

*Proof.* Take the chain $\tau = K_0 \supseteq \dots \supseteq K_m = K$ of Lemma 3.30.5. Each $K_i$ contains $K$, so $\operatorname{ext}(K_i \cap \sigma_n) > 2$. The cone $K_0$ has type $(0,0,1)$. Let $K_i = \langle d_1, d_2, v \rangle$ have type $(0,0,1)$. Its six children are $\langle d_1 + d_2, d_2, v \rangle$ and $\langle d_1, d_1 + d_2, v \rangle$, with $d_1 + d_2$ at height 0; $\langle d_1, d_2, v + d_1 \rangle$ and $\langle d_1, d_2, v + d_2 \rangle$, with the new apex at height 1; and $\langle d_1 + v, d_2, v \rangle$ and $\langle d_1, d_2 + v, v \rangle$. The first four have type $(0,0,1)$. The last two have extent at most 2 on $\sigma_n$ by Lemma 3.30.6, since $K_i$ is regular. So $K_{i+1}$ is one of the first four, and it has type $(0,0,1)$. By induction $K$ has type $(0,0,1)$. $\square$

**Lemma 3.30.8 (face sums in the needle).** Let $K = \langle d_1, d_2, v \rangle \subseteq \tau$ be a regular cone of type $(0,0,1)$, and let $f$ be a face of $K$ of dimension 2 or 3 with $b = \sum f \in \sigma_n$.

1. $b \in \{A, B, C\}$ and $\operatorname{ext}(K \cap \sigma_n) \le \frac{2n}{n-1}$.
2. If $b \ne B$, then $\operatorname{ext}(K \cap \sigma_n) \le \frac{n}{n-1}$.

Lean: none yet

*Proof.* The face $\langle d_1, d_2 \rangle$ has a sum of height 0, and $\sigma_n$ has no nonzero point of height 0. So $f$ contains $v$, and $b$ has height 1. By Lemma 3.30.4(4), $b \in \{A, B, C\}$. The rays of $f$ have nonnegative entries and sum to $b$, so each of them is at most $b$ in each coordinate. On the plane $y = 1$ the wedge $K$ lies in $\{x \ge v_x,\ z \ge v_z\}$, and on $\sigma_n$ we have $(n-1)x + nz \le n(n-1)$.

*The case $f = K$.* Then $d_1 + d_2 = b - v \le (b_x, 0, b_z)$. If $b = A$, both $d_i$ have $x = 0$ and height 0, so both are $e_3$, and $K$ is not regular. If $b = C$, both are $e_1$ for the same reason. So $b = B$. Not both $d_i$ are $e_3$, so one of them is $e_3$ and the other is $(1, 0, t)$ with $t \ge 0$. Then $v = (0, 1, n-3-t)$, so $t \le n - 3$, and the slice of $K$ is $\{x \ge 0,\ z \ge n - 3 - t + tx\}$. With $(n-1)x + nz \le n(n-1)$ this gives
$$x \le \frac{t + 2}{t + \frac{n-1}n}.$$
For $t = 0$ this is $\frac{2n}{n-1}$. For $t \ge 1$ it is less than 2, since $t + 2 < 2t + 2 - \frac 2n$ when $t > \frac 2n$.

*The case $f = \langle d_1, v \rangle$* (the case $\langle d_2, v \rangle$ is the same). Then $d_1 = b - v \le (b_x, 0, b_z)$.

- $b = A$. Then $d_1 = e_3$ and $v = (0, 1, n-2)$. On the slice, $z \ge n - 2$ gives $(n-1)x \le n$, so $0 \le x \le \frac n{n-1}$.
- $b = C$. Then $d_1 = e_1$ and $v = (n-1, 1, 0)$, so $n - 1 \le x \le n$.
- $b = B$ and $d_1 = e_3$. Then $v = (1, 1, n-3)$, and $z \ge n-3$ gives $1 \le x \le \frac{2n}{n-1}$.
- $b = B$ and $d_1 = (1, 0, t)$ with $0 \le t \le n-2$. Then $v = (0, 1, s)$ with $s = n - 2 - t$. Write $d_2 = (p, 0, q)$. As in the proof of Lemma 3.30.6, $\pm 1 = \det(d_1, d_2, v) = \pm(q - tp)$, so $q = tp \pm 1$. If $t = 0$, then $q = 1$. So each direction in $\operatorname{cone}(d_1, d_2)$ has slope $z/x$ at least $\max(t - 1, 0)$, and the slice of $K$ lies in $\{x \ge 0,\ z \ge s + \max(t-1, 0)\,x\}$. For $t = 0$ this gives $x \le \frac n{n-1}$. For $t \ge 1$ it gives $x(t - \frac1n) \le t + 1$, so $x \le \frac{2n}{n-1}$ for $t = 1$, and $x < 2$ for $t \ge 2$, since then $t > 1 + \frac 2n$.

In each case the extent is at most $\frac{2n}{n-1}$, and in the cases with $b \ne B$ it is at most $\frac n{n-1}$. $\square$

**Theorem 3.30.9 (short regions).** Let $n \ge 3$, let $K$ be a 3-dimensional directly reachable cone, and let $f$ be a face of $K$ of dimension 2 or 3 with $\sum f \in \sigma_n$. Then
$$\operatorname{ext}(K \cap \sigma_n) \le \frac{2n}{n-1}.$$
The bound is attained by $K = \langle e_1, (0, 1, n-3), e_3 \rangle$ with $f = K$ and $\sum f = B$.

Lean: none yet

*Proof.* If $\operatorname{ext}(K \cap \sigma_n) \le 2$, there is nothing to prove, since $2 < \frac{2n}{n-1}$. Otherwise $K$ has type $(0,0,1)$ by Lemma 3.30.7, and Lemma 3.30.8 gives the bound. The cone $\langle e_1, (0,1,n-3), e_3 \rangle$ comes from $\tau$ by $n - 3$ stars at the 2-faces $\langle (0, 1, i), e_3 \rangle$, so it is directly reachable, and the sum of its rays is $B$. Its slice is $\{x \ge 0,\ z \ge n - 3\}$. It contains $A$, and it meets the edge $AC$ of $\sigma_n$ at the point with $z = n - 3$, where $x = n(1 - \frac{n-3}{n-1}) = \frac{2n}{n-1}$. $\square$

### The lower bound

**Theorem 3.30.10 ($\sigma_n$ fails the refined condition).** Let $n \ge 3$, and let $(X_i, f_i, R_i)$, $1 \le i \le j$, be triples that satisfy the conditions (1), (2) and (4) of Definition 3.30.1 for $\sigma = \sigma_n$. Then $j \ge \frac{n-1}4$. In particular, $\sigma_n$ does not satisfy $(\mathrm{N}_k^{\rm ref})$ if $n \ge 4k + 2$.

Lean: none yet

*Proof.* Fix $i$ and let $K \in X_i$. By (1) the cone $K$ is directly reachable, and $f_i$ is a face of $K$ of dimension 2 or 3. By (2), $b_i = \sum f_i \in \sigma_n$, and $b_i \ne 0$. So $\chi(b_i) \in I(K)$, and by Theorem 3.30.9 the interval $I(K)$ has length at most $\frac{2n}{n-1}$. So
$$I(K) \subseteq J_i = \Big[\chi(b_i) - \frac{2n}{n-1},\ \chi(b_i) + \frac{2n}{n-1}\Big]$$
for each cone $K$ of $X_i$. By (4), $R_i \subseteq \sigma_n \cap \bigcup X_i$, so $\chi(R_i \setminus \{0\}) \subseteq J_i$. Also by (4) the union of the $R_i$ is $\sigma_n$, so the intervals $J_i$ cover $\chi(\sigma_n \setminus \{0\}) = [0, n]$ (Lemma 3.30.4(3)). Each $J_i$ has length $\frac{4n}{n-1}$, so $j \cdot \frac{4n}{n-1} \ge n$, that is, $j \ge \frac{n-1}4$. If $n \ge 4k+2$, then $\frac{n-1}4 > k$. $\square$

The proof uses neither condition (3) nor the last part of condition (4). It also does not use the disjointness of the $R_i$. So it bounds the number of sets in any cover of $\sigma_n$ by sets that lie in the union of the cones around a face with its sum in $\sigma_n$.

**Corollary 3.30.11 (pivot sets of $\sigma_n$).** Let $n \ge 3$, and let $(\Lambda, F)$ be a certificate for $\sigma_n$. Each pivot set of $\Lambda$ has at least $\frac{n-1}4$ rays. Equivalently, if $\Lambda$ is the union of $m$ closed stars of rays with no common interior points, then $m \ge \frac{n-1}4$.

Lean: none yet

*Proof.* The rays of $\Lambda$ lie in $\sigma_n$, so none of them is a ray of $\tau$, by Lemma 3.30.4(5). Let $T$ be a pivot set. By Proposition 3.30.3(4) the triples $(X_b, f, |\mathrm{St}_\Lambda(b)|)$, $b \in T$, satisfy Definition 3.30.1, with $j = |T|$. Theorem 3.30.10 gives $|T| \ge \frac{n-1}4$. The second form is Lemma 3.28.6. $\square$

**Corollary 3.30.12 ($\mathrm{C}(k)$ is false for every $k$).** For each $k \ge 1$ the cone $\sigma_{4k+2}$ has no witness with at most $k$ pivots (Definition 3.28.14). So Conjecture $\mathrm{C}(k)$ is false for every $k \ge 1$. Also, every certificate of $\sigma_n$ needs at least 3 pivots for $n \ge 10$, and at least 4 for $n \ge 14$.

Lean: none yet

*Proof.* Let $n = 4k + 2$. If $\sigma_n$ had a witness with at most $k$ pivots, Proposition 3.28.15 would give a certificate whose fan $\Lambda$ has a pivot set with at most $k$ rays. By Corollary 3.30.11 each pivot set has at least $\frac{4k+1}4 > k$ rays. For the last claim, $\frac{n-1}4 > 2$ for $n \ge 10$ and $\frac{n-1}4 > 3$ for $n \ge 14$. $\square$

The corollary does not say whether $\sigma_n$ has a certificate. If it has none, then toric $\mathrm{RSF}_3$ is false; if it has one, the certificate has many pivots. So the corollary does not touch toric $\mathrm{RSF}_3$ itself. It shows that a proof of toric $\mathrm{RSF}_3$ through Theorem 3.27.17 cannot use a fixed number of pivots, and that a uniform witness for the family $\sigma_n$ (item 5 of the open list of Section 3.28) must have a number of pivots that grows at least linearly in $n$.

The second family of Proposition 3.27.21 lies inside the first one, and the same method applies.

**Proposition 3.30.13 (the family $F_k$).** Let $k \ge 2$ and $F_k = \langle (0, 1, k), (1, 2, 2k-1), (k+1, 1, 0) \rangle$.

1. With $A, B, C$ the rays of $\sigma_{k+1}$, we have $F_k = \langle A, A + B, C \rangle \subseteq \sigma_{k+1}$, and $B \notin F_k$.
2. Let $K$ be a 3-dimensional directly reachable cone, and let $f$ be a face of $K$ of dimension 2 or 3 with $\sum f \in F_k$. Then $\operatorname{ext}(K \cap F_k) \le 2$.
3. Every family of triples that satisfies (1), (2) and (4) of Definition 3.30.1 for $F_k$ has at least $\frac{k+1}4$ members. Every pivot set of every certificate of $F_k$ has at least $\frac{k+1}4$ rays.

Lean: none yet

*Proof.* (1) For $n = k + 1$ the rays of $\sigma_n$ are $A = (0, 1, k)$, $B = (1, 1, k-1)$ and $C = (k+1, 1, 0)$, and $A + B = (1, 2, 2k-1)$. In the basis $A, A + B, C$ of $N$ the point $B$ has the coordinates $(-1, 1, 0)$, so $B \notin F_k$.

(2) Suppose that $\operatorname{ext}(K \cap F_k) > 2$. Then $\operatorname{ext}(K \cap \sigma_{k+1}) > 2$, and $K$ has type $(0,0,1)$ by Lemma 3.30.7 for $n = k + 1 \ge 3$. The sum $b = \sum f$ lies in $F_k \subseteq \sigma_{k+1}$, so Lemma 3.30.8(1) gives $b \in \{A, B, C\}$, and $b \ne B$ by (1). By Lemma 3.30.8(2), $\operatorname{ext}(K \cap \sigma_{k+1}) \le \frac{k+1}k \le 2$, a contradiction.

(3) The rays of $F_k$ have $\chi$ equal to $0$, $\frac12$ and $k + 1$, so $\chi(F_k \setminus \{0\}) = [0, k+1]$. The proof of Theorem 3.30.10, with $F_k$ in place of $\sigma_n$ and the bound 2 of (2) in place of $\frac{2n}{n-1}$, gives intervals $J_i$ of length 4 that cover $[0, k+1]$. No ray of $\tau$ lies in $F_k \subseteq \sigma_{k+1}$, so Proposition 3.30.3(4) applies as in Corollary 3.30.11. $\square$

So $F_k$ needs at least 2 pivots for $k \ge 4$ and at least 3 for $k \ge 8$. For $F_4$ the lower bound is 2, and the least $m$ found in Section 3.28 is 7, which is an upper bound for the least $m$ of the class.

### Worked example: the needle $\sigma_{10}$

**Example 3.30.14 (the needle $\sigma_{10}$).** Let $n = 10$. Then $A = (0, 1, 9)$, $B = (1, 1, 8)$ and $C = (10, 1, 0)$. In the plane $y = 1$ the cone $\sigma_{10}$ is the triangle with the vertices $(0, 9)$, $(1, 8)$ and $(10, 0)$ in the coordinates $(x, z)$. Its extent is 10, and its width across the needle is at most 1 in the coordinate $\psi$.

The table lists the cases of Lemma 3.30.8 for $n = 10$. In each row the cone $K = \langle d_1, d_2, v \rangle$ has type $(0,0,1)$ and the face $f$ has the sum $b$. The column "region" is a set in the plane $y = 1$ that contains the slice of $K$.

| $b$ | $f$ | data | region | bound on the extent | value for $n = 10$ |
|---|---|---|---|---|---|
| $A$ | $K$ | impossible | | | |
| $C$ | $K$ | impossible | | | |
| $B$ | $K$ | $e_3$, $(1, 0, t)$, $v = (0, 1, 7 - t)$ | $x \ge 0$, $z \ge 7 - t + tx$ | $\frac{t+2}{t + 9/10}$ | $\frac{20}9$ for $t = 0$, $\frac{30}{19}$ for $t = 1$ |
| $A$ | $\langle d_1, v \rangle$ | $d_1 = e_3$, $v = (0, 1, 8)$ | $x \ge 0$, $z \ge 8$ | $\frac n{n-1}$ | $\frac{10}9$ |
| $C$ | $\langle d_1, v \rangle$ | $d_1 = e_1$, $v = (9, 1, 0)$ | $x \ge 9$ | $1$ | $1$ |
| $B$ | $\langle d_1, v \rangle$ | $d_1 = e_3$, $v = (1, 1, 7)$ | $x \ge 1$, $z \ge 7$ | $\frac{n+1}{n-1}$ | $\frac{11}9$ |
| $B$ | $\langle d_1, v \rangle$ | $d_1 = (1, 0, t)$, $v = (0, 1, 8 - t)$ | $x \ge 0$, $z \ge 8 - t + \max(t-1, 0)x$ | $\frac{10}9$, $\frac{20}9$, $\frac{t+1}{t - 1/10}$ | $\frac{10}9$ for $t = 0$, $\frac{20}9$ for $t = 1$, $\frac{30}{19}$ for $t = 2$ |

The largest value is $\frac{20}9$, at the cone $K = \langle e_1, (0, 1, 7), e_3 \rangle$ of Theorem 3.30.9. Its slice is $\{x \ge 0, z \ge 7\}$. The line $z = 7$ meets the edge $AC$ at $x = \frac{20}9$ and the edge $BC$ at $x = \frac{17}8$, so $K \cap \sigma_{10}$ is the quadrilateral with the vertices $(0, 9)$, $(1, 8)$, $(\frac{17}8, 7)$ and $(\frac{20}9, 7)$, of extent $\frac{20}9$. The sum of the rays of $K$ is $B$, which is a ray of $\sigma_{10}$. So a pivot at $B$, made by the star of $\tau$ at $K$, has a region of extent at most $\frac{20}9$.

A pivot made by the star at a 2-face $f$ can have a region in the union of two cones $K$ and $K'$, each of extent at most $\frac{20}9$, and both contain $b$. So each region lies in an interval of length $\frac{40}9$ around $\chi(b)$. To cover $[0, 10]$ one needs at least $10 / \frac{40}9 = \frac 94$ regions, that is, at least 3. So every certificate of $\sigma_{10}$ has at least 3 pivots, and $\sigma_{10}$ is a counterexample to $\mathrm{C}(2)$. The computer finds 116 directly reachable cones with extent greater than 2 on $\sigma_{10}$. All of them have type $(0,0,1)$, as Lemma 3.30.7 says, and the largest extent of one of them with a face sum in $\sigma_{10}$ is $\frac{20}9$, as the table says.

The next table compares the bound with the data for small $n$. The second column is the number of directly reachable cones $K$ with $\operatorname{ext}(K \cap \sigma_n) > 2$. The fourth column is the lower bound of Corollary 3.30.11, and the fifth is the least $m$ over the certificates found by the searches of notes 90 to 92 (Section 3.28), which is an upper bound for the least $m$ of the class.

| $n$ | long cones | largest extent with a face sum | lower bound for $m$ | least $m$ found |
|---|---|---|---|---|
| 3 | 1 | $3$ | 1 | 1 |
| 4 | 4 | $\frac83$ | 1 | 2 |
| 5 | 10 | $\frac52$ | 1 | 3 |
| 6 | 20 | $\frac{12}5$ | 2 | 6 |
| 7 | 34 | $\frac73$ | 2 | no certificate known |
| 8 | 54 | $\frac{16}7$ | 2 | no certificate known |
| 9 | 81 | $\frac94$ | 2 | no certificate known |
| 10 | 116 | $\frac{20}9$ | 3 | no certificate known |
| 14 | 361 | $\frac{28}{13}$ | 4 | no certificate known |
| 24 | 2162 | $\frac{48}{23}$ | 6 | no certificate known |

The gap between the two last columns for $n = 4, 5, 6$ shows that the constant 4 in the bound is weak. The largest closed star in the stored certificates has extent 3, 3, $\frac52$ and $\frac73$ for $\sigma_3, \dots, \sigma_6$ (Proposition 3.30.15), while the proof allows $\frac{4n}{n-1}$, that is, 6, $\frac{16}3$, 5 and $\frac{24}5$.

**Proposition 3.30.15 (checks by computation).** The following are exact computations [C].

1. For $3 \le n \le 24$, the breadth-first search in the tree of Lemma 3.30.5 that keeps the cones $K$ with $\operatorname{ext}(K \cap \sigma_n) > 2$ ends. It finds 1, 4, 10, 20, 34, 54, 81, 116, 159, 213, 280, 361, 457, 567, 694, 839, 1003, 1189, 1395, 1625, 1880 and 2162 cones. All of them have type $(0,0,1)$, and the largest extent of one of them with a face sum in $\sigma_n$ is exactly $\frac{2n}{n-1}$, at the cone of Theorem 3.30.9.
2. For $F_k$ with $2 \le k \le 16$ the same search finds 1, 4, 10, 19, 33, 53, 80, 115, 158, 212, 279, 360, 454, 564 and 691 cones, all of type $(0,0,1)$, and none of them has a face sum in $F_k$.
3. The 5940 certificates stored by research notes 90 and 92 (with repetitions; the classes include $\sigma_3, \dots, \sigma_6$, $F_2$, $F_3$, $F_4$, $O_1$, $O_2$ and the classes with entries at most 6) all satisfy parts (1) to (3) of Proposition 3.30.3, with the cones of $X_b$ directly reachable by the column game of Lemma 3.26.12. The largest extent of a closed star $|\mathrm{St}_\Lambda(b)|$ is 3, 3, $\frac52$ and $\frac73$ for $\sigma_3$, $\sigma_4$, $\sigma_5$ and $\sigma_6$, at the rays $(3,2,2)$, $(5,2,2)$, $(1,1,3)$ and $(1,1,4)$.

Lean: none yet

*Proof.* Exact computations of research note 98, with programs that share no code with notes 90 to 93. The search in (1) and (2) is complete, since each ancestor of a cone with extent greater than 2 has extent greater than 2 (Lemma 3.30.5). The extents are computed exactly, as the length of the projection of a polygon that is cut out by six linear inequalities. Research note 98a repeated (1) for $3 \le n \le 14$ and (2) for $2 \le k \le 11$ with its own program, with agreement in every number. $\square$

### The rises of $\omega$

We now turn to the track M2 and use the notation of Volume 7, Sections 4.4 and 4.5. So $p$ is an odd prime, $f = z^{2p} + a_1 z^{2p-1} + \dots + a_{2p}$ is the equation at a point $\xi$ of multiplicity $2p$ over $k[[x_0, x_1, x_2]]$, $E$ is the boundary, $\delta$, $\mu_k$ and $\omega = \delta - \sum_{k \in E} \mu_k$ are the slopes and the residual slope, and Rule 61.9' chooses the center. A point $\xi'$ over the center has the generic value $\omega''$ of Volume 7, Lemma 4.5.23. The normalised points, the bottom face $\mathcal{F}$ and the quantity $h$ are as in Volume 7, Definition 4.5.20 and Section 4.5, after Proposition 4.5.5: $h$ is defined only when $\mathcal{F} = \{\omega e_b\}$ is an axis vertex.

**Definition 3.30.16 (rises).** A *rise* is a step $\xi \to \xi'$ of Rule 61.9' between points of multiplicity $2p$ with $\omega(\xi') > \omega(\xi)$. It is a *$(1,1,1)$ rise* if the vertex of $z'$ for the weight $(1,1,1)$ at $\xi'$ is solvable, so that $z'$ must be prepared again at $\xi'$.

If a rise goes to a point that is not a chart origin and (G1) of Volume 7, Definition 4.5.22, holds there, then $\omega(\xi') > \omega(\xi) \ge \omega''$, and Volume 7, Proposition 4.5.30, shows that the rise is a $(1,1,1)$ rise. The rises of Volume 7, Theorems 4.4.7 and 4.4.8, are $(1,1,1)$ rises.

### The quantity $h$ at the known rises

A natural plan for Conjecture 4.4.6 of Volume 7 is a lexicographic invariant. Volume 7, Proposition 4.5.14, already shows that no pair $(\omega, s)$ decreases at each step, because $\omega$ goes up. A weaker plan is to count the rises by a second quantity. On the toric branches with an axis vertex the quantity $h$ controls the runs (Volume 7, Lemma 4.5.6 and Proposition 4.5.7), so it is the first candidate. The next proposition shows that $h$ does not exist at the rises.

**Proposition 3.30.17 ($h$ at the rises of Theorems 4.4.7 and 4.4.8).** Let $p$ be an odd prime.

1. At the point $\xi$ of Volume 7, Theorem 4.4.8, the bottom face is $\{\omega e_1\}$ with $\omega = 1$, and $h(\xi) = \frac{2(p+2)}{p-1}$.
2. At the point $\xi'$ of Volume 7, Theorem 4.4.8(3), after the new preparation, the bottom face is the single point $(0, 1, \frac1p)$. It is not an axis vertex, so $h(\xi')$ is not defined.
3. At the point $\xi$ of Volume 7, Theorem 4.4.7, the bottom face contains the point $\big(\frac1{p(p+1)}, \frac12, \frac{p-1}{p(p+1)}\big)$, which has three positive coordinates. So it is not an axis vertex, and $h(\xi)$ is not defined.

Lean: none yet

*Proof.* (1) Here $E = \{0, 2\}$ and $\mu = (\frac1p, \frac12, \frac{p-1}p)$, so the normalised points are $v = (u_0 - \frac1p, u_1, u_2 - \frac{p-1}p)$ for the points $u = \alpha / i$ of the monomials $x^\alpha$ of $a_i$. The monomial $F$ of $a_p$, and $F^2$ in $a_{2p}$, give $u = (\frac1p, 1, \frac{p-1}p)$ and $v = (0, 1, 0) = \omega e_1$. The monomial $G = x_0^2 x_1^{p+1} x_2^{4p+2}$ of $a_{2p}$ gives $v = (0, \frac{p+1}{2p}, \frac{p+2}p)$, with $|v| = \frac{3p+5}{2p} > 1$. The monomial $a_2 = x_0^{2p} x_1 x_2^2$ gives $v = (p - \frac1p, \frac12, \frac1p)$, with $|v| = p + \frac12 > 1$. So $\mathcal{F} = \{\omega e_1\}$ and $b = 1$. For the points $g$ with $w(g) = \omega - g_1 > 0$ the projection is $q(g) = (g_0, g_2) / w(g)$. The point of $G$ has $w = \frac{p-1}{2p}$ and $s + t = \frac{p+2}p \cdot \frac{2p}{p-1} = \frac{2(p+2)}{p-1}$. The point of $a_2$ has $w = \frac12$ and $s + t = 2p$. Since $p^2 - 2p - 2 > 0$ for $p \ge 3$, the least value is $\frac{2(p+2)}{p-1}$.

(2) By the proof of Volume 7, Theorem 4.4.8(3), after the translation $z' = Z + \gamma$ the equation is $(Z^p + H)^2 + a_2' \sum_j \binom{2p-2}{j} \gamma^j Z^{2p-2-j} + G'$, in the coordinates $x_0$, $x_1'$, $y = x_2' - \lambda$, with $E' = \{0\}$. Here $H = x_0^p x_1'^p\big((\lambda + y)^{p-1} - \lambda^{p-1}\big)$, so the lowest monomial of $H$ is a nonzero multiple of $x_0^p x_1'^p y$ and the others are $x_0^p x_1'^p y^e$ with $e \ge 2$. Also $a_2' = x_0^{2p+1} x_1' (\lambda + y)^2$, $\gamma = c\, x_0 x_1'$ with $c \ne 0$, and $G' = x_0^{3p+5} x_1'^{p+1} (\lambda + y)^{4p+2}$. The points $u = \alpha / i$ of the lowest monomials are:

- $2H$ in $b_p$ and $H^2$ in $b_{2p}$: $u = (1, 1, \frac1p)$;
- the rigid $b_{2+j} = \binom{2p-2}{j} \gamma^j a_2'$, for $j \le 2p - 3$ with a nonzero binomial and $2 + j \ne p$: $u = (\frac{2p+1+j}{2+j}, \frac{1+j}{2+j}, 0)$;
- the term $\binom{2p-2}{p-2} \gamma^{p-2} a_2'$ of $b_p$: $u = (\frac{3p-1}p, \frac{p-1}p, 0)$;
- the term $\gamma^{2p-2} a_2'$ of $b_{2p}$: $u = (\frac{4p-1}{2p}, \frac{2p-1}{2p}, 0)$;
- $G'$ in $b_{2p}$: $u = (\frac{3p+5}{2p}, \frac{p+1}{2p}, 0)$.

The least first coordinate is 1, so $\mu_0' = 1$, and the normalised points are $v = u - e_0$. Their values of $|v|$ are $\frac{p+1}p$; $\frac{2p+j}{2+j} \ge \frac{4p-3}{2p-1}$; $\frac{3p-2}p$; $\frac{2p-1}p$; and $\frac{p+3}p$. Each value after the first is larger than $\frac{p+1}p$: for the second, $(4p-3)p - (p+1)(2p-1) = 2p^2 - 4p + 1 > 0$, and the others are clear for $p \ge 3$. The other monomials of $H$ give points that are larger in each coordinate. So $\omega(\xi') = \frac{p+1}p$, in agreement with the theorem, and it is reached only at $v = (0, 1, \frac1p)$. So $\mathcal{F}' = \{(0, 1, \frac1p)\}$, which has two nonzero coordinates.

(3) Here $E = \{0, 1, 2\}$ and $\mu = (\frac1{p+1}, \frac12, \frac{p-1}{p+1})$. The monomial $F = x_0 x_1^p x_2^{p-1}$ of $a_p$ gives $u = (\frac1p, 1, \frac{p-1}p)$, and
$$v = u - \mu = \Big(\frac1{p(p+1)}, \frac12, \frac{p-1}{p(p+1)}\Big), \qquad |v| = \frac1{p+1} + \frac12 = \frac{p+3}{2(p+1)} = \omega.$$
So $v \in \mathcal{F}$, and $\mathcal{F} \ne \{\omega e_b\}$ for each $b$. $\square$

So $h$ is defined before the rise of Theorem 4.4.8 and not after it, and it is not defined before the rise of Theorem 4.4.7. Proposition 3.30.17 is a stronger statement than "the pair $(\omega, h)$ is not lexicographic", which already follows from Proposition 4.5.14 of Volume 7. It says that $h$ cannot even be evaluated on both sides of a rise. So $h$ cannot count the rises, and a second quantity for the rises must be defined for every bottom face.

### Why a rise does not repeat at once

In Theorems 4.4.7 and 4.4.8 of Volume 7 the rise comes from the monomial $F = x_0 x_1^p x_2^{p-1}$ with $\operatorname{in} a_p = 2F$. At the point $x_2' = \lambda \ne 0$ of the chart of $x_0$ the image of $F$ has the lowest term $\lambda^{p-1} x_0^p x_1'^p$, a constant times a $p$-th power, and this makes the vertex for $(1,1,1)$ solvable. The next lemma says when a monomial can do this.

**Lemma 3.30.18 (the congruence).** Let $x^\alpha$ be a monomial of $a_p$. Consider the blowup of the closed point, the chart of $x_j$, and a point with $x_k' = \lambda \ne 0$ and $x_l' = 0$, where $\{j, k, l\} = \{0, 1, 2\}$. Then $x^\alpha / x_j^p$ has the lowest term $\lambda^{\alpha_k} x_j^{|\alpha| - p} x_l'^{\alpha_l}$, and this term is a constant times the $p$-th power of a monomial if and only if
$$|\alpha| \equiv 0 \quad \text{and} \quad \alpha_l \equiv 0 \pmod p.$$

Lean: none yet

*Proof.* With $x_k = x_j(\lambda + y_k)$ and $x_l = x_j x_l'$ we get $x^\alpha = x_j^{|\alpha|} x_l'^{\alpha_l} (\lambda + y_k)^{\alpha_k}$. Divide by $x_j^p$. The lowest term of $(\lambda + y_k)^{\alpha_k}$ is $\lambda^{\alpha_k} \ne 0$. A monomial is a $p$-th power of a monomial if and only if all its exponents are divisible by $p$. $\square$

For $F$ in the chart of $x_0$ at $x_2' = \lambda$ we have $|\alpha| = 2p$ and $\alpha_1 = p$, so the congruence holds. After the rise of Theorem 4.4.8 the leading part of $b_p$ is $2H$, and $H$ has the lowest monomial $x_0^p x_1'^p y$, with $|\alpha| = 2p + 1$. After the divisorial step at $x_0$, which the rule makes since $\mu_0' = 1$, it becomes $x_1'^p y$, with $|\alpha| = p + 1$. Neither satisfies the congruence. So the next point blowup with one nonzero $\lambda_k$ cannot make the image of the leading monomial of $b_p$ the initial form of a solvable vertex for $(1,1,1)$. This explains why the trees below have no second rise right after the first. It does not exclude that a later step restores the congruence, for example through a change of the leading monomial.

### The computed trees

Research note 98 built the full germ-level tree of Rule 61.9' from a germ: all centers for all tie-breaks, all charts, all $\mathbb{F}_p$-rational points of multiplicity $2p$ over the center, and a new preparation of $z$ at each new point. It counted the rises on each branch.

**Proposition 3.30.19 (the trees after the known rises).** The following are exact computations over $\mathbb{F}_p$ [C].

| start | $p$ | depth limit | nodes | leaves with $\omega = 0$ | leaves at the depth limit | rises | most rises on one branch |
|---|---|---|---|---|---|---|---|
| Volume 7, Theorem 4.4.8 | 3 | 40 | 575 | 187 | 0 | 2 | 1 |
| Volume 7, Theorem 4.4.8 | 5 | 25 | 711 | 350 | 9 | 4 | 1 |
| Volume 7, Theorem 4.4.7 | 3 | 40 | 253 | 116 | 0 | 2 | 1 |
| Volume 7, Theorem 4.4.7 | 5 | 25 | 277 | 154 | 0 | 4 | 1 |

In each tree the rises are the $p - 1$ points $x_2' = \lambda \ne 0$ of the theorem, at depth 0, and all of them are $(1,1,1)$ rises. The values at the rises agree with the theorems: $\omega$ goes from 1 to $\frac43$ and $\frac65$ for Theorem 4.4.8, and from $\frac34$ to $\frac56$ and from $\frac23$ to $\frac7{10}$ for Theorem 4.4.7, for $p = 3$ and $p = 5$. In all four cases the generic value is $\omega'' = 1$ for Theorem 4.4.8 and $\omega'' = \frac12$ for Theorem 4.4.7. After the rise no branch has a second rise. The quantity $h$ is not defined after any of the four rises, and before them it is $5$ and $\frac72$ for Theorem 4.4.8 and not defined for Theorem 4.4.7, in agreement with Proposition 3.30.17.

Lean: none yet

*Proof.* Exact computations of research note 98, at the germ level, with the programs of note 86. $\square$

For $p = 3$ both trees are finite. For $p = 5$ the tree of Theorem 4.4.8 has 9 branches that reach the depth limit 25, so it is not known to be finite.

**Proposition 3.30.20 (searches for germs with several rises).** Let $p = 3$. The following are exact computations, with all tie-breaks, at most 20000 nodes and 20 seconds for each germ [C].

1. The 80 germs of the search of research note 72, followed to depth 16, have no rise.
2. Of 300 random germs of the form $(z^p + x^\alpha)^2 + c\,x^\rho z^{2p-i} + x^\gamma$, with one rigid term, up to two more terms in $a_{2p}$ and a random boundary, followed to depth 14, none has a rise.
3. Of 1200 random germs of the same form with $x^\alpha$ chosen so that $|\alpha| \equiv 0$ and $\alpha_l \equiv 0 \pmod p$ for some $l$ with $\alpha_l > 0$, as in Lemma 3.30.18, followed to depth 14, 7 germs have rises, with 22 rises in all. Every rise is a $(1,1,1)$ rise at a point blowup, and in each of the 7 trees each branch has at most one rise. For 524 of the 1200 germs the tree reached the limit of nodes or the depth limit, so it is not complete.

The rises in (3) are the following. The count includes the $p - 1 = 2$ points $\lambda$ of each rise. In the column $\delta$ the first value is the slope before the blowup, which in each row is an integer, as Volume 7, Proposition 4.5.30, requires for $\delta''$, and the second value is the slope at $\xi'$ after the new preparation.

| depth | $\delta \to \delta'$ | $\omega \to \omega'$ | $\omega''$ | $E \to E'$ | $h$ before, after | count |
|---|---|---|---|---|---|---|
| 0 | $2 \to \frac73$ | $\frac23 \to \frac56$ | $\frac12$ | $\{0,1,2\} \to \{0,1\}$ | undefined, undefined | 2 |
| 1 | $2 \to \frac73$ | $\frac12 \to \frac56$ | $\frac12$ | $\{0,1,2\} \to \{0,1\}$ | $3$, undefined | 2 |
| 2 | $2 \to \frac73$ | $\frac13 \to \frac12$ | $\frac16$ | $\{0,1,2\} \to \{0,2\}$ | undefined, undefined | 4 |
| 6 | $2 \to \frac73$ | $\frac5{12} \to \frac23$ | $\frac13$ | $\{0,1,2\} \to \{0,2\}$ | undefined, undefined | 2 |
| 8 | $2 \to \frac73$ | $\frac12 \to \frac23$ | $\frac13$ | $\{0,1,2\} \to \{0,1\}$ | undefined, undefined | 2 |
| 9 | $2 \to \frac76$ | $\frac2{15} \to \frac16$ | $0$ | $\{0,1,2\} \to \{0\}$ | undefined, $2$ | 4 |
| 10 | $2 \to \frac{13}6$ | $\frac5{12} \to \frac12$ | $\frac13$ | $\{0,1,2\} \to \{0,2\}$ | undefined, undefined | 2 |
| 10 | $3 \to \frac{13}3$ | $\frac{13}6 \to \frac73$ | $2$ | $\{1,2\} \to \{1\}$ | undefined, undefined | 2 |
| 13 | $2 \to \frac{13}6$ | $\frac13 \to \frac{11}{30}$ | $\frac15$ | $\{0,1,2\} \to \{0,2\}$ | undefined, undefined | 2 |

Lean: none yet

*Proof.* Exact computations of research note 98, with the seeds 98 for (2) and 981 and 982 for (3). $\square$

The searches show three things that Theorems 4.4.7 and 4.4.8 of Volume 7 do not show. First, rises occur deep inside a tree, not only at its root. Second, the integer slope $\delta''$ can be 3, and the jump of $\delta$ need not be $\frac1p$: it is $\frac16$ in two rows, and in the row at depth 9 the slope $\delta$ drops while $\omega$ goes up, because $E$ loses two components. Third, $h$ can be defined on one side of a rise: before the rise in the row at depth 1, and after it in the row at depth 9. So Proposition 3.30.17(2) is a statement about Theorem 4.4.8 and not a general rule. But in each of the 22 rises $h$ is undefined on at least one side, so the conclusion of Proposition 3.30.17 holds for all of them.

The rows also bear on item 4 of the open list of Volume 7, Section 4.5. They are steps to points that are not chart origins, with a new preparation, at which $\omega$ goes up, and they are not in the two families of Theorems 4.4.7 and 4.4.8 [C]. Research note 98 does not record whether (G1) holds at them, so they answer the question in the form "apart from the two families, can $\omega$ go up when $z'$ must be prepared again?", and the answer is yes.

### The open question

**Remark 3.30.21 (the question on the rises).** The data give no branch with two rises, and no candidate for an unbounded number of rises. The question is:

> Is the number of $(1,1,1)$ rises along a branch of Rule 61.9' bounded by a function of $\delta(\xi_0)$ and $|E(\xi_0)|$ at the first point $\xi_0$? Or is there a germ with an unbounded number of them?

There are two natural routes. A counterexample could come from an inverse construction: a germ $\xi_{-1}$ whose rule center has a point that is the germ after the rise of Theorem 4.4.8, and then the same again. A bound could come from a quantity that is defined for every bottom face, that the translation $z' = Z + \gamma$ of Proposition 4.5.30 of Volume 7 lowers, and that the congruence of Lemma 3.30.18 controls. Research note 98 found neither. A bound on the rises alone does not prove Conjecture 4.4.6 of Volume 7: it must be combined with the finiteness of the runs between the rises, which is open at the steps with cancellation (item 3 of the open list of Volume 7, Section 4.5).

### What is open

1. The question of Remark 3.30.21: a bound on the number of $(1,1,1)$ rises along a branch, or a germ with an unbounded number.
2. A quantity for the rises that is defined for every bottom face. By Proposition 3.30.17, $h$ is not one.
3. The best constant in Corollary 3.30.11. The data suggest that a pivot region has extent at most about 3, which would give $m \ge \frac n3$ roughly, and the values 1, 2, 3, 6 for $\sigma_3, \dots, \sigma_6$ agree with this and with the proved bound.
4. Certificates for $\sigma_7$ and for $F_5$, and more generally whether $\sigma_n$ has a certificate for every $n$. Corollary 3.30.12 does not decide this, and toric $\mathrm{RSF}_3$ stays open.
5. A decision procedure for $(\mathrm{N}_k^{\rm ref})$ for each $\sigma$ and $k$. For $\sigma_n$ the projection bound of Theorem 3.30.10 suffices for a lower bound, but it is not a decision procedure.
6. Lower bounds for other thin cones. The proof works for each cone in a slab $0 \le x + z - cy \le y$ whose lattice points at height 1 give short regions. A general statement of this kind is not written down.

### Exercises

1. Show that $\langle e_1, (0, 1, n-3), e_3 \rangle$ comes from $\tau$ by $n - 3$ stars at 2-faces, and draw its slice and $\sigma_n$ in the plane $y = 1$ for $n = 6$.
2. Check the claim of the proof of Lemma 3.30.6 that $\det(d_1, d_2, v) = \pm(q d_{1,x} - p d_{1,z})$ when $d_1$ and $d_2$ have height 0 and $v$ has height 1.
3. Show that the cone $\langle (0,1,1), e_1, e_2 \rangle$, which is the cone $K'$ of Lemma 3.30.6 for $K = \tau$, $d_1 = e_3$ and $d_2 = e_1$, meets $\sigma_n$ in a set of extent exactly 2. So the bound of Lemma 3.30.6 is sharp.
4. Show that the cone $\langle e_1, (0,1,n-2), e_3 \rangle$ has extent $\frac{n}{n-1}$ on $\sigma_n$, and find its face with the sum $A$.
5. Show that in the proof of Theorem 3.30.10 the set $I(K) \cup I(K')$ is an interval, and that its length is at most $\frac{4n}{n-1}$.
6. Compute $h$ before the rise of Theorem 4.4.8 of Volume 7 for $p = 7$, and check that the point of $G$ gives the least value.
7. Show that the congruence of Lemma 3.30.18 holds for $F = x_0 x_1^p x_2^{p-1}$ in the chart of $x_0$ at $x_2' = \lambda$, and fails in the chart of $x_0$ at $x_1' = \lambda$, $x_2' = 0$.

### Status

The results are new in research note 98, which does the tasks T3 and T4 of the review of the road in note 94 (tamnd/singularity#334). Before this section was written, research note 98a checked Proposition 98.2, Lemmas 98.4 to 98.6 and Theorems 98.7 and 98.8 of note 98 from first principles, and it repeated the search for long cones with its own program. It found the main results correct, with these fixes. First, Theorem 98.8 of note 98 said that $\sigma_n$ fails $(\mathrm{N}_k^{\rm ref})$, but its proof started from a certificate, and $(\mathrm{N}_k^{\rm ref})$ does not assume one. This section proves the failure of $(\mathrm{N}_k^{\rm ref})$ directly from Definition 3.30.1 (Theorem 3.30.10) and then derives the bound for pivot sets (Corollary 3.30.11). Second, Definition 98.1 of note 98 allowed $X_i = \{f_i\}$ with $\dim f_i = 2$; Definition 3.30.1 states the three cases with the dimensions. Third, note 98 said that the largest closed star of the stored certificates of $\sigma_6$ has extent $\frac{12}5$; the computed value is $\frac73$. Fourth, the meaning of Proposition 98.11 of note 98 is sharpened in Proposition 3.30.17 and the remark after it. Note 98a also proved the entries of Proposition 3.30.17(1) and (3), which note 98 had only computed. The computations of Propositions 3.30.19 and 3.30.20 have not been repeated by an independent program. The map has nodes for Definition 3.25.8, Theorem 3.25.12, Proposition 4.5.14 and Proposition 4.5.30 of Volume 7, which this section uses, and no nodes yet for its new statements. None of the statements has a Lean proof. An outside expert has not yet read the result.

### Notes and references

The first part continues Sections 3.26 to 3.28 and research notes 88 to 93. The second part continues Volume 7, Sections 4.4 and 4.5, and research notes 61, 65, 66, 72, 81 and 86. The literature on toric factorization is in the references of Sections 3.27 and 3.28. We list the items that this section uses.

- [DSK11] S. Da Silva and K. Karu, On Oda's strong factorization conjecture, Tohoku Math. J. 63 (2011), 163-182. The conjecture of Oda is open in dimension at least 3, and toric $\mathrm{RSF}_3$ is a case of it (Proposition 3.27.26).
- [Kar03] K. Karu, Local strong factorization of toric birational maps, J. Algebraic Geom. 14 (2005), 165-175. Local strong factorization, which does not give a bound on the number of pivots.

The method of Theorem 3.30.10, a projection to one coordinate and a bound on the length of each region, is elementary, and research note 98 does not know a source for it in the literature on factorization.
