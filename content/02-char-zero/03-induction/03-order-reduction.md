---
title: Order reduction and principalization
nodes: [SG0000001P, SG0000001Q, SG00000048, SG00000049, SG00000042]
sources: [Kol07, Vil89, BM97, EH02, Wlo05, ATW24, McQ20]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Order reduction and principalization

This section assembles the induction. We prove that order reduction for marked ideals in dimension $n - 1$ gives order reduction for ideals of maximal order $m$ in dimension $n$, when there is a global hypersurface of maximal contact. We state the passage to the general case, which needs the uniqueness results of Remark 3.2.12 and a gluing theorem of Kollár. Then we prove that order reduction for ideals gives order reduction for marked ideals, and that the mark 1 gives principalization.

### The two statements

All varieties are smooth over a field $k$ of characteristic 0, but not necessarily connected. A divisor $E$ always has simple normal crossings and an ordered index set (Definition 2.2.1), and a blowup sequence for $(X, I, E)$ has centers with simple normal crossings with the transforms $E_i$, the new exceptional divisor being put last.

**Definition 3.3.1 (order reduction).** Let $n \ge 0$.

1. *Order reduction for ideals in dimension $n$*, or $(\mathrm{O}_n)$, is the statement: for each $m \ge 1$ and each triple $(X, I, E)$ with $\dim X = n$ and $\operatorname{max\text{-}ord} I \le m$, there is a blowup sequence of order $m$ for $(I, m)$ with $\operatorname{max\text{-}ord} I_r < m$.
2. *Order reduction for marked ideals in dimension $n$*, or $(\mathrm{M}_n)$, is the statement: for each $m \ge 1$ and each $(X, I, m, E)$ with $\dim X = n$ and $I$ nonzero on each irreducible component of $X$, there is a blowup sequence of order at least $m$ for $(I, m)$ with $\operatorname{cosupp}(I_r, m) = \emptyset$.

The hypothesis $\operatorname{max\text{-}ord} I \le m$ implies that $I$ is nonzero on each component. In (M$_n$) this hypothesis is needed: if $I$ vanishes on a component, that component lies in $\operatorname{cosupp}(I_i, m)$ for all $i$. Kollár proves the functorial forms of both statements: the sequences are given by rules that commute with smooth morphisms and with change of fields [Kol07, Chapter 3], Sections "Order reduction for ideals" and "Order reduction for marked ideals". We prove existence and we indicate where functoriality enters.

The statement (M$_0$) holds: a smooth variety of dimension 0 is a finite disjoint union of spectra of fields, so an ideal that is nonzero on each component is the unit ideal, and its cosupport is empty.

**Lemma 3.3.2 (localization).** Let $U \subseteq X$ be an open set that contains $\operatorname{cosupp}(I, m)$. Then each blowup sequence of order at least $m$ for $(I|_U, m, E|_U)$ extends uniquely to a blowup sequence of order at least $m$ for $(I, m, E)$ that is an isomorphism over $X \setminus U$, and the cosupports of the transforms agree.

Lean: none yet

*Proof.* Let $U_i \subseteq X_i$ be the inverse image of $U$. We show by induction on $i$ that $\operatorname{cosupp}(I_i, m) \subseteq U_i$. For $i = 0$ this is the hypothesis, and Lemma 2.2.4 (4) gives the step. The center $Z_i$ is closed in $U_i$ and lies in $\operatorname{cosupp}(I_i, m) \cap U_i = \operatorname{cosupp}(I_i, m)$, which is closed in $X_i$. So $Z_i$ is closed in $X_i$, and we blow it up in $X_i$. Smoothness and simple normal crossings are local conditions at the points of $Z_i$. $\square$

**Lemma 3.3.3 (restriction of simple normal crossings).** Let $S \subseteq X$ be a smooth hypersurface and $E = \sum_i E^i$ a divisor, with no $E^i$ containing a component of $S$, such that $S + E$ has simple normal crossings. Let $E|_S = \sum_i E^i|_S$, a divisor with simple normal crossings on $S$.

1. If $Z \subseteq S$ is a smooth closed subvariety that has simple normal crossings with $E|_S$, then $Z$ has simple normal crossings with $S + E$.
2. If also $Z$ contains no component of $S$, and $\pi$ is the blowup of $Z$, then $S' + E'$ has simple normal crossings, where $E'$ is the transform of $E$, and $E'|_{S'}$ is the transform of $E|_S$ under the blowup $\pi_S$ of $S$ along $Z$.
3. If $Z \subseteq S$ is a smooth closed subvariety and $x \in Z$ is a closed point such that $Z$ has simple normal crossings with $E$ near $x$, then $Z$ has simple normal crossings with $S + E$ near $x$.

Lean: none yet

*Proof.* (1) Let $x \in Z$. Choose local coordinates $z_2, \dots, z_n$ on $S$ at $x$ such that each $E^i|_S$ through $x$ is some $(z_l = 0)$ and $Z$ is a coordinate subspace. If $e_i$ is a local equation of $E^i$, then $e_i|_S$ is a unit times $z_l$, and we may replace $z_l$ by $e_i|_S$. Let $h$ be a local equation of $S$. Lift the other $z_l$ to functions on $X$, and take the $e_i$ as lifts of the $z_l = e_i|_S$. The differentials at $x$ of the lifts restrict to a basis of the cotangent space of $S$, and the differential of $h$ spans the kernel of the restriction map. So $h$ and the lifts are local coordinates on $X$ at $x$. In them $S$ and the $E^i$ are coordinate hyperplanes, and $Z$ is the coordinate subspace given by $h$ and the $z_l$ that define $Z$ in $S$.

(2) Use the coordinates of (1), with $x_1 = h$, and write $Z = (x_1 = x_{l_1} = \dots = x_{l_c} = 0)$ with $c \ge 1$. The transform $S'$ lies in the charts $U_{l_k}$ of Lemma 2.2.2, and there $S' = (y_1 = 0)$. In the chart $U_{l_k}$ the exceptional divisor is $(y_{l_k} = 0)$, and the birational transform of each $E^i = (x_l = 0)$ through $x$ is $(y_l = 0)$ if $l \ne l_k$ and does not meet the chart if $l = l_k$. So all components of $S' + E'$ are coordinate hyperplanes. Restricting to $S' = (y_1 = 0)$ gives exactly the chart description of the blowup of $S$ along $Z = (x_{l_1} = \dots = x_{l_c} = 0)$, with the same exceptional divisor and the same birational transforms. If $c = 1$, the blowup of $S$ is the identity. Both descriptions then remove $Z$ from $E|_S$ if $Z$ is a component of some $E^i|_S$, and both add $Z$ as the new divisor $F_S$.

(3) Let $V = \mathfrak{m}_x / \mathfrak{m}_x^2$, and let $N \subseteq V$ be the image of the ideal of $Z$. Since $Z$ is smooth, $\dim N$ is the codimension $c$ of $Z$ at $x$. For a function $g \in \mathfrak{m}_x$ let $\bar g$ be its class in $V$. We first prove a criterion. Let $D$ be a divisor with simple normal crossings, and let $d_1, \dots, d_t$ be local equations of the components of $D$ through $x$. Let $A$ be the set of $i$ with $d_i$ in the ideal of $Z$, and let $B$ be the other indices. Then $Z$ has simple normal crossings with $D$ near $x$ if and only if the classes $\bar d_1, \dots, \bar d_t$ are linearly independent and $N \cap \operatorname{span}(\bar d_i : i \in B) = 0$.

If there are parameters as in Definition 1.1.2, then their classes form a basis of $V$, the $\bar d_i$ are multiples of distinct basis vectors by units, and $N$ is spanned by the basis vectors of the parameters that define $Z$. For $i \in B$ the parameter of $d_i$ is not one of these, so both conditions hold. Conversely, assume the two conditions. For $i \in A$ we have $\bar d_i \in N$. Extend the classes $\bar d_i$ with $i \in A$ to a basis of $N$ by classes $\bar g_1, \dots, \bar g_u$ of elements $g_k$ of the ideal of $Z$. The second condition says that the sum $N + \operatorname{span}(\bar d_i : i \in B)$ is direct. So the classes $\bar d_i$ ($i \in A$), $\bar g_k$ and $\bar d_i$ ($i \in B$) are linearly independent. Extend them to a basis of $V$ by classes of further functions. These functions form a regular system of parameters at $x$, and as in the proof of Lemma 2.3.2 they are local coordinates near $x$. The functions $d_i$ ($i \in A$) and $g_k$ are $c$ of these coordinates, so they define a smooth subvariety of codimension $c$ near $x$. It contains $Z$, and $Z$ is smooth of the same codimension, so the two agree near $x$. Thus the coordinates satisfy Definition 1.1.2 for $Z$ and $D$.

Now let $h$ be a local equation of $S$, and apply the criterion to $D = S + E$. Since $S + E$ has simple normal crossings, $\bar h$ and the classes of the local equations of the $E^i$ through $x$ are linearly independent. Since $Z \subseteq S$, the function $h$ lies in the ideal of $Z$. So the set $B$ for $S + E$ is the same as the set $B$ for $E$. The second condition for $S + E$ is the second condition for $E$, and it holds because $Z$ has simple normal crossings with $E$ near $x$. $\square$

### Ideals in dimension n

The main step moves the points of order $m$ away from one divisor.

**Lemma 3.3.4 (moving the cosupport off a divisor).** Assume (M$_{n-1}$). Let $(X, I, E)$ be a triple with $\dim X = n$, let $m \ge 1$, and let $E^j$ be one of the divisors of $E$. Then there is a blowup sequence of order at least $m$ for $(I, m, E)$ such that the birational transform $E^j_r$ of $E^j$ is disjoint from $\operatorname{cosupp}(I_r, m)$.

Lean: none yet

*Proof.* Let $Z_{-1}$ be the union of the irreducible components of $E^j$ that lie in $\operatorname{cosupp}(I, m)$. It is a union of connected components of the smooth divisor $E^j$, so it is a smooth center of codimension 1 with simple normal crossings with $E$. Its blowup is the identity of $X$; the transform of $(I, m)$ is $I_0 = \mathcal{O}_X(m Z_{-1}) \cdot I$, and $Z_{-1}$ becomes the last divisor, while the birational transform of $E^j$ is the union $S$ of the other components. The divisor $S$ is disjoint from $Z_{-1}$, so $I_0 = I$ near $S$, and no component of $S$ lies in $\operatorname{cosupp}(I_0, m)$.

Let $E_S$ be the restriction to $S$ of the divisors of $E_0$ other than $S$, in the same order. Since $S + (E_0 - S) = E_0$ has simple normal crossings, $E_S$ is a divisor with simple normal crossings on $S$. The ideal $C_S(I_0)$ is nonzero on each component of $S$, by the last part of the proof of Theorem 3.2.4. Apply (M$_{n-1}$) to $(S, C_S(I_0), m!, E_S)$. We get a blowup sequence $S_r \to \dots \to S_0 = S$ of order at least $m!$ with $\operatorname{cosupp}(C_{S, r}, m!) = \emptyset$. Blow up the same centers $Z_i \subseteq S_i$ in $X_i$, so that $S_{i+1}$ is the birational transform of $S_i$.

By Theorem 3.2.4, this is a blowup sequence of order at least $m$ for $(I_0, m)$, each $Z_i$ contains no component of $S_i$, and
$$S_r \cap \operatorname{cosupp}(I_r, m) = \operatorname{cosupp}(C_{S, r}, m!) = \emptyset.$$
It remains to check the conditions on the divisors. By induction on $i$, Lemma 3.3.3 (2) shows that $E_i$ has simple normal crossings and that the restriction to $S_i$ of the divisors of $E_i$ other than $S_i$ is the transform $E_{S, i}$ of $E_S$. The center $Z_i$ has simple normal crossings with $E_{S, i}$, so by Lemma 3.3.3 (1) it has simple normal crossings with $E_i$. $\square$

The centers of this sequence are chosen by the rule of (M$_{n-1}$) on $S$. If that rule commutes with smooth morphisms, so does the sequence of the lemma, because restriction to $E^j$ commutes with smooth morphisms [Kol07, Chapter 3], Section "Order reduction for ideals".

**Theorem 3.3.5 (order reduction with a global hypersurface of maximal contact).** Assume (M$_{n-1}$). Let $(X, I, E)$ be a triple with $\dim X = n$ and $\operatorname{max\text{-}ord} I = m \ge 1$, and assume that there is a hypersurface of maximal contact $H \subseteq X$ for $I$. Then there is a blowup sequence of order $m$ for $(I, m, E)$ with $\operatorname{max\text{-}ord} I_r < m$.

Lean: none yet

*Proof.* Throughout, if the maximal order drops below $m$ we stop. While it is $m$, Theorem 2.3.3 shows that the centers lie in the transforms $H_i$ and that $H_i$ is a hypersurface of maximal contact for $I_i$.

Step A. Apply Lemma 3.3.4 to the divisor $E^1$, then to the transform of $E^2$, and so on up to the transform of $E^s$. When the transform of $E^l$ is disjoint from the cosupport, it stays disjoint in the later steps, because by Lemma 2.2.4 (4) the cosupport of a transform lies over the old cosupport. At the end, the transforms of $E^1, \dots, E^s$ are disjoint from $\operatorname{cosupp}(I_r, m)$. So near $\operatorname{cosupp}(I_r, m)$ the divisor $E_r$ consists of exceptional divisors of Step A. Kollár observes that these divisors are transversal to the transforms of $H$, because the center of each blowup lies in the transform of $H$ [Kol07, Chapter 3], Section "Order reduction for ideals". We prove the precise form we need. Number the blowups of Step A as one sequence $X_r \to \dots \to X_0 = X$, with the centers $Z_i$ and the exceptional divisors $F_i$. Let $G_i$ be the sum of the birational transforms in $X_i$ of $F_0, \dots, F_{i-1}$. We show by induction on $i$:

(P$_i$) there is an open set $V_i \supseteq H_i$ such that $H_i + G_i$ is a divisor with simple normal crossings on $V_i$, and no component of $H_i$ is a component of $G_i$.

For $i = 0$ we have $G_0 = 0$, and $H$ is smooth. Assume (P$_i$). By Theorem 2.3.3 (2), $Z_i \subseteq \operatorname{cosupp}(I_i, m) \subseteq H_i \subseteq V_i$. First let $Z_i$ have codimension 1 in $X_i$. This happens only in the first blowup of an application of Lemma 3.3.4, and then $Z_i$ is a union of components of a divisor of $E_i$ that lie in $H_i$. A component of $Z_i$ is an irreducible smooth hypersurface in $H_i$, so it is a component of $H_i$. The blowup is the identity, $G_{i+1} = G_i + Z_i$, and $H_{i+1}$ is the union of the other components of $H_i$. Since $H_i$ is smooth, its components are disjoint, so $Z_i$ does not meet $H_{i+1}$. Then $V_{i+1} = V_i \setminus Z_i$ works. Now let $Z_i$ have codimension at least 2. The divisors of $G_i$ are among the divisors of $E_i$, and $Z_i$ has simple normal crossings with $E_i$. So by Lemma 3.3.3 (3), applied on $V_i$ with $S = H_i$ and with $G_i$ in the role of $E$, the center $Z_i$ has simple normal crossings with $H_i + G_i$. By the charts of Lemma 2.2.2 and the paragraph after it, the birational transform of $H_i + G_i$ plus $F_i$ has simple normal crossings on $\pi_i^{-1}(V_i)$. This divisor is $H_{i+1} + G_{i+1}$, and $V_{i+1} = \pi_i^{-1}(V_i)$ contains $H_{i+1}$. No component of $H_{i+1}$ is $F_i$, since $Z_i$ contains no component of $H_i$. This proves (P$_{i+1}$).

By (P$_r$) and $\operatorname{cosupp}(I_r, m) \subseteq H_r$, the divisor $H_r + G_r$ has simple normal crossings near $\operatorname{cosupp}(I_r, m)$. Near this set the divisors of $E_r$ are components of $G_r$, so $H_r + E_r$ has simple normal crossings near $\operatorname{cosupp}(I_r, m)$.

Step B. Simple normal crossings is an open condition, so there is an open set $U \supseteq \operatorname{cosupp}(I_r, m)$ on which $H_r + E_r$ has simple normal crossings. On $U$ consider the divisor $(H_r, E_r^1, E_r^2, \dots)$, with $H_r$ put first. Apply Lemma 3.3.4 to it and to its first divisor $H_r$. By Lemma 3.3.2 the resulting sequence extends to $X$. Its centers have simple normal crossings with the transforms of $H_r + E_r$, so in particular with the transforms of $E_r$. At the end, the transform of $H$ is disjoint from the cosupport of the last transform of $(I, m)$. But this cosupport lies in the transform of $H$, by Theorem 2.3.3 (2). This holds also for the first blowup of Lemma 3.3.4, whose center is a union of components of $H_r$, since the proof of Theorem 2.3.3 allows such centers. So the cosupport is empty, and the maximal order is less than $m$. $\square$

In general there is no global hypersurface of maximal contact. Kollár deals with this in two steps.

**Theorem 3.3.6 (order reduction for ideals).** Assume (M$_{n-1}$), in the functorial form. Then (O$_n$) holds, in the functorial form.

Node: SG00000048 · Lean: none yet

*Proof sketch.* We follow [Kol07, Chapter 3], Section "Order reduction for ideals". Let $\operatorname{max\text{-}ord} I \le m$; if it is less than $m$ there is nothing to do.

1. By Remark 3.2.12, we may replace $(I, m)$ by $(W_s(I), s)$ for a suitable $s$, so we may assume that $I$ is MC-invariant.
2. By Lemma 2.3.2, $X$ is covered by open sets $X^{(l)}$ with hypersurfaces of maximal contact $H^{(l)}$; on $X \setminus \operatorname{cosupp}(I, m)$ we have $MC(I) = \mathcal{O}$, and the empty hypersurface works. The disjoint union $X^* = \coprod_l X^{(l)}$ has the global hypersurface of maximal contact $H^* = \coprod_l H^{(l)}$, and the map $g \colon X^* \to X$ is étale and surjective.
3. The proof of Theorem 3.3.5 gives a sequence on $X^*$. It is built from (M$_{n-1}$) by restriction to divisors, so it commutes with smooth morphisms that respect the hypersurface. By Corollary 3.2.11 and its étale form, two hypersurfaces of maximal contact $H$ and $H'$ with $H + E$ and $H' + E$ of simple normal crossings give étale equivalent data, and Kollár proves that equivalent blowup sequences of order $m$ for an MC-invariant ideal are equal (Section "Uniqueness of maximal contact"). Since the ideals $I_i$ are not MC-invariant in general, Kollár applies the tuning again at the start of Step B. So the sequence of Theorem 3.3.5 does not depend on the choice of $H$.
4. Hence the two pullbacks of the sequence on $X^*$ to $X^* \times_X X^*$ agree, and Kollár's globalization theorem, for a class of smooth morphisms closed under fiber products and coproducts, descends the sequence to $X$ (Section "Order reduction for ideals").

We do not reproduce the details of steps 3 and 4. $\square$

### Marked ideals in dimension n

The second step of the induction removes the condition on the maximal order. The new problem is that the transforms of a marked ideal $(I, m)$ with $m$ less than the maximal order contain the exceptional divisors with high multiplicity. We split off this part.

**Lemma 3.3.7 (monomial part).** Let $(X, I, E)$ be a triple with $I$ nonzero on each component of $X$. For each irreducible component $D$ of the divisors $E^l$, let $c_D$ be the largest integer $c$ with $I \subseteq \mathcal{O}_X(-cD)$.

1. Let $M(I) = \mathcal{O}_X(-\sum_D c_D D)$ and $N(I) = \mathcal{O}_X(\sum_D c_D D) \cdot I$. Then $I = M(I) \cdot N(I)$, $N(I)$ is an ideal sheaf, and $N(I) \not\subseteq \mathcal{O}_X(-D)$ for each $D$. This decomposition with $M(I)$ monomial is unique.
2. If $G$ is a divisor with integer coefficients supported on $E$, and $B$ and $\mathcal{O}_X(-G) \cdot B$ are both ideal sheaves, then $N(\mathcal{O}_X(-G) \cdot B) = N(B)$.
3. $B \subseteq N(B)$, so $\operatorname{ord}_x N(B) \le \operatorname{ord}_x B$ for each closed point $x$.

We call $M(I)$ the *monomial part* and $N(I)$ the *nonmonomial part* of $I$.

Lean: none yet

*Proof.* Let $t$ be a local equation of $D$ at a point of $D$. The condition $B \subseteq \mathcal{O}_X(-cD)$ says that $t^{-c} B$ is regular. Since $X$ is normal, this holds if it holds at the generic points of the codimension 1 subvarieties, and away from $D$ it is automatic. So $c_D(B) = \operatorname{ord}_D B$, the order of $B$ at the generic point of $D$, whose local ring is a discrete valuation ring. Different components $D$ have different generic points, and the equations of the other components are units at the generic point of $D$. So $\operatorname{ord}_D$ is additive, and $\operatorname{ord}_D(\mathcal{O}(-G) B) = g_D + \operatorname{ord}_D B$, where $g_D$ is the coefficient of $D$ in $G$. This gives (2), since then $N(\mathcal{O}(-G) B) = \mathcal{O}(\sum_D (g_D + c_D) D) \, \mathcal{O}(-G) \, B = N(B)$. For (1), $N(I)$ is an ideal because $\operatorname{ord}_D(\mathcal{O}(c_D D) I) = 0$ for each $D$ and the other generic points of codimension 1 are not affected; the same equality gives $N(I) \not\subseteq \mathcal{O}(-D)$. If $I = \mathcal{O}(-\sum a_D D) \cdot N'$ with $N'$ an ideal not contained in any $\mathcal{O}(-D)$, then $a_D = \operatorname{ord}_D I = c_D$. (3) holds because $\mathcal{O}(\sum c_D D) \supseteq \mathcal{O}_X$. $\square$

We allow different coefficients on the components of one divisor $E^l$; then part (2) holds for all divisors $G$ supported on $E$. The monomial case is treated by an explicit combinatorial rule. For a set $A$ of indices of divisors with $E^A = \bigcap_{l \in A} E^l$ nonempty, and a point $y \in E^A$, let $a_A(y) = \sum_{l \in A} a_l(y)$, where $a_l(y)$ is the coefficient of the component of $E^l$ through $y$. This number is locally constant on $E^A$. Since $E$ has simple normal crossings, $E^A$ is smooth of codimension $|A|$, and no $E^l$ with $l \notin A$ contains a component of $E^A$.

**Theorem 3.3.8 (order reduction for monomial ideals).** Let $I = \mathcal{O}_X(-\sum_D a_D D)$ be a monomial ideal for $E$, with $D$ running over the components of the $E^l$, and let $m \ge 1$. Then there is a blowup sequence of order at least $m$ for $(I, m, E)$ whose centers are intersections of components of the transforms of $E$, with $\operatorname{cosupp}(I_r, m) = \emptyset$.

Node: SG00000049 · Lean: none yet

*Proof.* The transforms of $I$ stay monomial: if $Z$ is a connected component of some $E^B$ and $\pi$ is its blowup, then $\pi^* \mathcal{O}(-D)$ is $\mathcal{O}(-D' - F)$ if $Z \subseteq D$ and $\mathcal{O}(-D')$ otherwise, where $D'$ is the birational transform. So if $Z \subseteq \operatorname{cosupp}(I, m)$, the transform of $(I, m)$ is monomial, with the old coefficients on the transforms $D'$ and the coefficient $a_B(Z) - m$ on the new divisor $F$ over $Z$; by the remark above, no other divisor contains $Z$. Also $\operatorname{ord}_y I = a_{A(y)}(y)$, where $A(y)$ is the set of all $l$ with $y \in E^l$. So a union of connected components of $E^B$ on which $a_B \ge m$ lies in $\operatorname{cosupp}(I, m)$ and is an allowed center.

We run Steps $r = 1, \dots, n$. Before Step $r$ we have the property
$$(\ast_s) \qquad a_A(y) < m \quad \text{for all } A \text{ with } |A| = s \text{ and all } y \in E^A$$
for all $s < r$. In Step $r$, let $\mu$ be the maximum of $a_B(y)$ over all $B$ with $|B| = r$ and $y \in E^B$. If $\mu < m$, then $(\ast_r)$ holds and we go to Step $r + 1$. Otherwise, let $B$ be the lexicographically smallest set of $r$ indices for which the value $\mu$ is attained, and blow up the union $Z$ of the connected components of $E^B$ on which $a_B = \mu$. The new divisor $F$ is put last, with coefficient $\mu - m$ on each of its components.

Consider the new intersections. The intersections not involving $F$ are birational transforms of old ones, or empty, with the same values of $a$; the transforms of $E^l$, $l \in B$, no longer meet over $Z$. Let $A$ be a set of old indices with $F \cap E'^A \ne \emptyset$, and let $y \in Z \cap E^A$ be the image of a point of the intersection. Then:

- If $|A| = r - 1$, the new value is $\mu - m + a_A(y) < \mu$, because $a_A(y) < m$ by $(\ast_{r-1})$, or trivially if $r = 1$.
- If $|A| = s - 1$ with $s < r$, choose $l \in B \setminus A$, which exists since $|B| > |A|$, and let $P = A \cup \{l\}$ and $Q = B \setminus \{l\}$. Then $y \in E^P \cap E^Q$, $|P| = s$ and $|Q| = r - 1$, so $a_A(y) + \mu = a_P(y) + a_Q(y) < 2m$ by $(\ast_s)$ and $(\ast_{r-1})$. Hence the new value $\mu - m + a_A(y)$ is less than $m$, and $(\ast_s)$ still holds.

So the properties $(\ast_s)$, $s < r$, are kept, and the pair consisting of $\mu$ and of the number of sets $B$ with $|B| = r$ that attain $\mu$ decreases in the lexicographic order. After finitely many blowups $\mu < m$, and Step $r$ ends. After Step $n$ all the $(\ast_s)$ hold, and intersections of more than $n$ divisors are empty. So $\operatorname{ord}_y I_r = a_{A(y)}(y) < m$ for every $y$, and $\operatorname{cosupp}(I_r, m) = \emptyset$. $\square$

The order of the divisors is used to choose $B$. Without a rule of this kind the obvious method fails.

**Example 3.3.9 (Fibonacci numbers).** Let $X$ be a smooth surface, $E^1$ and $E^2$ smooth curves that meet transversally at one point $p$, and $I = \mathcal{O}_X(-(m+1)(E^1 + E^2))$. The locus of maximal order is $p$, of order $2m + 2$. Blow up $p$: the new divisor $E^3$ gets the coefficient $2(m+1) - m = m + 2$. Now the points $E^1 \cap E^3$ and $E^2 \cap E^3$ have order $2m + 3$, which is larger than before. Blow up $E^2 \cap E^3$; the new divisor $E^4$ gets $m + 3$, and $E^3 \cap E^4$ has order $2m + 5$. Continuing with the intersection of the last two divisors, the coefficients are $m + p_i$ with $p_i$ the Fibonacci numbers $1, 1, 2, 3, 5, \dots$, and the maximal order grows without bound [Kol07, Chapter 3], Section "Order reduction for marked ideals". The rule of Theorem 3.3.8 does better. We follow it. In Step 1 the maximum of the single coefficients is $\mu = m + 1 \ge m$, and it is attained first by $E^1$. So we blow up the curve $E^1$. This blowup is the identity of $X$. The birational transform of $E^1$ is empty, and the curve comes back as the new last divisor $E^3$, with the coefficient $\mu - m = 1$. In the same way we blow up $E^2$, and the curve comes back as $E^4$ with the coefficient 1. The ideal does not change, but the bookkeeping does: the transform of $(I, m)$ is now $\mathcal{O}_X(-E^3 - E^4)$. If $m = 1$, Step 1 continues, and the blowups of $E^3$ and $E^4$ give the coefficients 0 and the unit ideal. Let $m \ge 2$. Then all single coefficients are $1 < m$, and Step 2 starts. The only pair is $\{3, 4\}$, at the point $p$, with $\mu = 2$. If $m \ge 3$, then $\mu < m$, and the cosupport is already empty: the order is 2 at $p$ and at most 1 elsewhere. If $m = 2$, we blow up $p$. The new divisor $E^5$ gets the coefficient $\mu - m = 0$, and the new pairs $\{3, 5\}$ and $\{4, 5\}$ have the value $1 + 0 = 1 < 2$. So in all cases the rule ends after at most four blowups, while the method of blowing up the locus of maximal order never ends. The difference is that the rule first lowers the coefficients of single divisors below $m$, and only then looks at their intersections.

Lean: none yet

**Theorem 3.3.10 (order reduction for marked ideals).** Assume (O$_n$). Then (M$_n$) holds.

Node: SG00000049 · Lean: none yet

*Proof.* Let $(X, I, m, E)$ be given, with $I$ nonzero on each component. Write $I = M(I) \cdot N(I)$ as in Lemma 3.3.7. If $\operatorname{cosupp}(I, m) = \emptyset$ we stop. Otherwise let
$$s = \max \{ \operatorname{ord}_x N(I) : x \in \operatorname{cosupp}(I, m) \}.$$

Case $s \ge 1$. Let $J = N(I)^m + I^s$, with the mark $ms$. By Lemma 3.2.2 (1), $\operatorname{ord}_x J \ge ms$ if and only if $\operatorname{ord}_x N(I) \ge s$ and $\operatorname{ord}_x I \ge m$. Also $\operatorname{max\text{-}ord} J \le ms$: at a point of $\operatorname{cosupp}(I, m)$ the ideal $N(I)^m$ has order at most $ms$, and at other points $I^s$ has order less than $ms$. Apply (O$_n$) to $(X, J, E)$ with the mark $ms$. Each center lies in $\operatorname{cosupp}(J_i, ms)$, and by Lemma 3.2.2 (2) we have $J_i = N_i^m + I_i^s$, where $N_i$ is the transform of $(N(I), s)$ and $I_i$ that of $(I, m)$. So the sequence is a blowup sequence of order at least $m$ for $(I, m)$, and at the end $\operatorname{cosupp}(I_r, m) \cap \operatorname{cosupp}(N_r, s) = \emptyset$. By induction on $i$, $I_i = \mathcal{O}(-G_i) N_i$ with $G_0$ the divisor of $M(I)$ and $G_{i+1} = \pi_i^* G_i + (s - m) F_i$, a divisor supported on $E_{i+1}$. By Lemma 3.3.7 (2) and (3), $N(I_r) = N(N_r) \supseteq N_r$. So $N(I_r)$ has order less than $s$ at each point of $\operatorname{cosupp}(I_r, m)$, and the number $s$ for $(I_r, m)$ is smaller. Repeat.

Case $s = 0$. Then $\operatorname{cosupp}(I, m)$ does not meet the zero set of $N(I)$. On the open set $U = X \setminus V(N(I))$ the ideal $I$ equals $M(I)$, which is monomial. Apply Theorem 3.3.8 on $U$ and extend the sequence to $X$ by Lemma 3.3.2.

Since $s$ decreases in each round of the first case, we reach the second case, and at its end the cosupport is empty. $\square$

Kollár first applies order reduction to $N(I)$ until its maximal order is less than $m$, and only then lowers $s$ [Kol07, Chapter 3], Section "Order reduction for marked ideals". The argument above does not need this preliminary step. Each step is given by a rule from (O$_n$) or from Theorem 3.3.8, and Kollár checks that the composite rule commutes with smooth morphisms.

### Principalization

**Theorem 3.3.11 (principalization).** Assume (M$_n$). Let $X$ be a smooth variety of dimension $n$, $I$ an ideal sheaf nonzero on each component, and $E$ a divisor with simple normal crossings and ordered index set. Then there is a blowup sequence $\Pi \colon X_r \to \dots \to X_0 = X$ with smooth centers that have simple normal crossings with the transforms of $E$, each lying over $V(I)$, such that $\Pi^* I = \mathcal{O}_{X_r}(-G)$ for a divisor $G \ge 0$ supported on the exceptional divisors, which are part of the divisor $E_r$ with simple normal crossings.

Node: SG00000042 · Lean: none yet

*Proof.* Apply (M$_n$) with $m = 1$. A blowup sequence of order at least 1 is a sequence whose centers lie in $V(I_i)$, and $\operatorname{cosupp}(I_r, 1) = \emptyset$ means $I_r = \mathcal{O}_{X_r}$. Since $I_{i+1} = \mathcal{O}(F_i) \cdot \pi_i^* I_i$, we get $\Pi^* I = \mathcal{O}(-G) \cdot I_r = \mathcal{O}(-G)$, with $G$ the sum of the pullbacks to $X_r$ of the exceptional divisors $F_i$. By induction, $\Pi_i^* I = \mathcal{O}(-G_i) \cdot I_i \subseteq I_i$, where $\Pi_i \colon X_i \to X$, so $Z_i \subseteq V(I_i) \subseteq \Pi_i^{-1}(V(I))$. $\square$

With (M$_0$) and Theorems 3.3.6 and 3.3.10, induction on $n$ gives (M$_n$) for all $n$. Theorem 3.3.6 needs (M$_{n-1}$) in the functorial form, and our proof of Theorem 3.3.10 gives only existence, so this induction uses the functorial form of Theorem 3.3.10 from [Kol07, Chapter 3]. So Theorem 3.3.11 proves Theorem 1.1.6, with $E = \emptyset$, and Theorem 1.1.7, after we order the index set of $E$ in any way. The functorial forms of the steps give Theorem 1.1.8 [Kol07, Chapter 3]. For an unordered divisor $E$, Kollár first blows up the intersections of the components of $E$ to make them disjoint; these centers need not lie over $V(I)$.

### The map of the induction

The proof has the following structure. Each arrow is a theorem of this volume; the steps marked "cited" use results of [Kol07, Chapter 3] that we state without proof.

1. (M$_0$) holds, since the ideals are unit ideals.
2. (M$_{n-1}$) gives Lemma 3.3.4, by the going-up theorem (Theorem 3.2.4, which rests on the restriction theorem, Theorem 3.1.3, and on Theorem 2.2.7) and Lemma 3.3.3.
3. Lemma 3.3.4, Lemma 3.3.3 (3) and maximal contact (Theorem 2.3.3) give Theorem 3.3.5.
4. Theorem 3.3.5, tuning (Remark 3.2.12, cited), uniqueness of maximal contact (Corollary 3.2.11, with the étale form cited) and globalization (cited) give (O$_n$), Theorem 3.3.6.
5. (O$_n$), Lemma 3.3.7 and Theorem 3.3.8 give (M$_n$), Theorem 3.3.10. Step 4 in dimension $n + 1$ needs the functorial form of (M$_n$), which is cited.
6. (M$_n$) with the mark 1 gives principalization, Theorem 3.3.11, and so Theorems 1.1.6 and 1.1.7; Theorem 1.2.1 then gives resolution.

The characteristic is used in step 2, through Lemma 2.1.4 and the division by $k!$ in Theorem 3.1.3, in step 3, through Theorem 2.3.3, and in step 4, through Proposition 3.2.10. Section 2.4 explains why each of these fails in characteristic $p$.

### The invariant

Kollár explains the role of an invariant as follows [Kol07, Chapter 3]. The inductive proof gives resolutions only locally. The best way to patch them would be an invariant $\operatorname{inv}(x, X)$ of the points, with values in an ordered set, that is upper semicontinuous and such that each step of the resolution blows up the locus where it is maximal. With some modification this is done in [Vil89], [BM97] and [EH02], but the known invariants are complicated. Informally, they record the order of $I$ at $x$, then the order of the coefficient ideal on a hypersurface of maximal contact, then the same data in the next dimension, together with the exceptional divisors through $x$. Kollár's proof does not define an invariant. The uniqueness of Corollary 3.2.11 and the globalization theorem take its place, following a suggestion of Włodarczyk [Wlo05].

A different approach blows up weighted centers. Abramovich, Temkin and Włodarczyk [ATW24] and McQuillan [McQ20] attach to each point a simpler invariant, and a single weighted blowup at the locus of its maximal value makes it drop. Volume 9, Section 2.2, explains why this invariant does not extend to positive characteristic.

Node: SG0000001Q · Lean: `Singularity.weightedBlowup_invariant_lt` (planned, no Lean statement yet)

### Notes and references

The structure of the induction, Lemma 3.3.4, Theorems 3.3.5, 3.3.6 and 3.3.10, and Example 3.3.9 are from [Kol07, Chapter 3], Sections "Plan of the proof", "Order reduction for ideals" and "Order reduction for marked ideals". The monomial case, Theorem 3.3.8, follows Kollár's Step 3 with the coefficients attached to the components. Włodarczyk's proof [Wlo05] has the same shape, with a homogenized coefficient ideal in place of $W_s(I)$. The Lean library does not state principalization; Chapter 4 explains what it states instead (node SG0000001P).
