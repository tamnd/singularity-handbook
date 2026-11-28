---
title: The extension of the family and the end of the proof
nodes: [SG0000001K]
sources: [dJ96]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The extension of the family and the end of the proof

At the end of Section 2.3 we have a family $f \colon X \to Y$ of curves with sections and a stable curve $\mathcal{C}$ over $Y$ that agrees with $X$ over a dense open subset $U$. This section shows that, after a modification of $Y$, the isomorphism $\beta$ extends to a morphism $\mathcal{C} \to X$. Then we replace $X$ by $\mathcal{C}$, apply the induction hypothesis to the base, and finish with the blowups of Section 2.1. We follow [dJ96, 4.18 to 4.28].

### The extension of the isomorphism

We work in a slightly more general setting, as de Jong does in [dJ96, 4.18]. Let $f \colon X \to S$ be a proper morphism of integral excellent schemes, with sections $\sigma_1, \dots, \sigma_n$, and let $Z = \bigcup_i \sigma_i(S)$. Assume:

(a) all fibres of $f$ are nonempty, geometrically connected, and of pure dimension 1;

(b) the smooth locus $\operatorname{sm}(X/S)$ is dense in each fibre;

(c) the generic fibre of $f$ is smooth;

(e) for each geometric point $\bar s$ of $S$ and each irreducible component $C$ of $X_{\bar s}$, there are three indices $\alpha, \beta', \gamma$ such that $\sigma_\alpha(\bar s)$, $\sigma_{\beta'}(\bar s)$, $\sigma_\gamma(\bar s)$ are three distinct points of $C \cap \operatorname{sm}(X/S)$;

(g) there are a stable $n$-pointed curve $(\mathcal{C}, \tau_1, \dots, \tau_n)$ over $S$, a nonempty open $U \subseteq S$, and an isomorphism $\beta \colon \mathcal{C}|_U \to X|_U$ that maps $\tau_i$ to $\sigma_i$.

Let $T$ be the closure of the graph of $\beta$ in $\mathcal{C} \times_S X$, with its reduced structure. It is integral, because the graph is isomorphic to $\mathcal{C}|_U$, which is integral: it is flat over $U$ with geometrically connected and reduced fibres and an irreducible generic fibre. The projections $\mathrm{pr}_1 \colon T \to \mathcal{C}$ and $\mathrm{pr}_2 \colon T \to X$ are proper and are isomorphisms over $U$, so they are modifications.

Let $S' \to S$ be a modification. Then the strict transforms of $X$, $\mathcal{C}$ and $T$ over $S'$ again have the properties (a) to (c), (e) and (g), and the strict transform of $T$ is the closure of the graph of the pullback of $\beta$ [dJ96, 4.18]. The flattening theorem of Raynaud-Gruson, in the form of [dJ96, 2.19], gives a modification $S' \to S$ such that the strict transforms of the proper morphisms $X \to S$ and $T \to S$ are flat. After a further normalization of $S$, we may assume:

(h) $X$ and $T$ are flat over $S$;

(i) $S$ is normal.

Fix $s \in S$. Write $X_s = X_1 \cup \dots \cup X_r$, $\mathcal{C}_s = C_1 \cup \dots \cup C_c$ and $T_s = T_1 \cup \dots \cup T_t$ for the decompositions into irreducible components. Since $T$ is flat over $S$, the fibre $T_s$ has pure dimension 1.

**Lemma 2.4.1 (de Jong).** In this situation:

1. for each $i$ there is exactly one $j$ with $\mathrm{pr}_2(T_j) = X_i$, and $\mathrm{pr}_1$ is not constant on this $T_j$;
2. for each $i$ there is exactly one $j$ with $\mathrm{pr}_1(T_j) = C_i$.

Lean: `Singularity.not_three_disjoint_of_card_le_two` (the counting step). The geometry is not in Lean yet.

This is [dJ96, Lemma 4.20]. *Sketch of proof.* The first statement of each part comes from normality. At a point $x$ of $\operatorname{sm}(X/S) \cap X_s$, the scheme $X$ is normal, since $S$ is normal and $X \to S$ is smooth at $x$. There are only finitely many closed points of $X_s$ over which $\mathrm{pr}_2$ has a fibre of dimension 1, so near a general point $x$ of $X_i$ in the smooth locus, $\mathrm{pr}_2$ is finite and birational over a normal scheme, hence an isomorphism. This gives exactly one component $T_j$ over $X_i$. The same argument for $\mathrm{pr}_1$ and the smooth locus of $\mathcal{C} \to S$ gives the first statement of part 2. By Zariski's main theorem in the form of the Stein factorization, $\mathrm{pr}_2^{-1}(x)$ is connected for each normal point $x$ of $X$.

Now suppose that $\mathrm{pr}_1$ is constant on the component $T_j$ over $X_i$, with image a point $c \in \mathcal{C}_s$. By (e) there are three distinct marked points $x_\alpha = \sigma_\alpha(s)$, $x_{\beta'}$, $x_\gamma$ on $X_i$ in the smooth locus. Let $T_\alpha = \mathrm{pr}_2^{-1}(x_\alpha)$, and similarly for $\beta'$ and $\gamma$; they are connected and meet $T_j$. Let $c_\alpha = \tau_\alpha(s)$, and similarly for $\beta'$ and $\gamma$. These are three distinct points of $\mathcal{C}_s$, because the sections of a stable curve are disjoint, and $T_\alpha$ connects $c$ with $c_\alpha$. If $c$ is not one of $c_\alpha, c_{\beta'}, c_\gamma$, then $\mathrm{pr}_1(T_\alpha)$, $\mathrm{pr}_1(T_{\beta'})$ and $\mathrm{pr}_1(T_\gamma)$ are curves through $c$ with no common component, by part 2, so at least three components of $\mathcal{C}_s$ pass through $c$. A nodal curve does not allow this. If $c = c_\alpha$, then the curves $\mathrm{pr}_1(T_{\beta'})$ and $\mathrm{pr}_1(T_\gamma)$ meet at the marked point $c_\alpha$, and this is not possible because a marked point of a stable curve lies on only one component, in the smooth locus. $\square$

**Proposition 2.4.2.** In the situation of (a) to (c), (e) and (g) to (i), the projection $\mathrm{pr}_1 \colon T \to \mathcal{C}$ is an isomorphism. So $\beta$ extends to a proper birational morphism $\mathrm{pr}_2 \circ \mathrm{pr}_1^{-1} \colon \mathcal{C} \to X$.

Lean: `Singularity.algebraMap_bijective_of_isIntegral_of_birational` (the commutative algebra of the last step). The finite fibres and the normality of the stable curve are not in Lean yet.

*Proof.* We first show that $\mathrm{pr}_1$ has finite fibres. Over $U$ it is an isomorphism. Let $s \in S$ and let $T_j$ be a component of $T_s$. Since $T \subseteq \mathcal{C} \times_S X$, the curve $T_j$ is not mapped to a point by both projections. If $\mathrm{pr}_2$ maps $T_j$ to a point, then $\mathrm{pr}_1$ is not constant on $T_j$. If $\mathrm{pr}_2(T_j)$ is a curve, then it is a component $X_i$ of $X_s$, and by Lemma 2.4.1 $T_j$ is the unique component over $X_i$ and $\mathrm{pr}_1$ is not constant on it. So $\mathrm{pr}_1$ is not constant on any component of $T_s$, and its fibres over the points of $\mathcal{C}_s$ are finite. A proper morphism with finite fibres is finite. So $\mathrm{pr}_1$ is finite and birational.

Next, $\mathcal{C}$ is normal, by Serre's criterion: a Noetherian scheme is normal if it has the properties $S_2$ and $R_1$. The morphism $\mathcal{C} \to S$ is flat, $S$ is normal, and the fibres are reduced curves, which are Cohen-Macaulay; so $\mathcal{C}$ has the property $S_2$. A point of codimension 1 of $\mathcal{C}$ lies either in the generic fibre, which is smooth over $k(S)$, or is a generic point of a component of a fibre over a point of codimension 1 of $S$. In the second case it lies in the smooth locus of $\mathcal{C} \to S$, since the smooth locus is dense in the fibres, and $S$ is regular at its image since $S$ is normal. So $\mathcal{C}$ has the property $R_1$. This is [dJ96, 4.21].

A finite birational morphism from an integral scheme to a normal integral scheme is an isomorphism. So $\mathrm{pr}_1$ is an isomorphism. $\square$

### The induction

We return to the proof of Theorem 1.2.1, with a pair $(X, Z)$ and $f \colon X \to Y$ that have the properties (i), (iii), (iv) and (vi)(a) to (g) of Section 2.3. Apply Proposition 2.4.2 with $S = Y$. We must replace $Y$ by a modification $Y'$, and $X$ by its strict transform; a modification is a generically étale alteration, so Lemma 2.3.5 applies. After this, $\beta$ extends to a proper birational morphism $\beta \colon \mathcal{C} \to X$. So $\beta$ is a modification. By Lemma 2.3.1 we may replace $(X, Z)$ by $(\mathcal{C}, \beta^{-1}(Z))$.

Over $U$ the morphism $\beta$ is an isomorphism and $Z \cap X|_U = \bigcup_i \sigma_i(U)$. So, with $D = Y \setminus U$,
$$\beta^{-1}(Z) \subseteq \tau_1(Y) \cup \dots \cup \tau_n(Y) \cup g^{-1}(D),$$
where $g \colon \mathcal{C} \to Y$ is the structure morphism, which is smooth over $Y \setminus D$. By Lemma 2.3.2 we may enlarge $Z$ to the right hand side. This is [dJ96, 4.22].

Now apply the induction hypothesis to the pair $(Y, D)$. The variety $Y$ has dimension $d - 1$ and $k$ is algebraically closed. So there is a generically étale alteration $\psi \colon Y_1 \to Y$ with $Y_1$ projective and regular, such that $\psi^{-1}(D)$ is a divisor with strict normal crossings; as in Step 2 of Section 2.3, the open immersion of the theorem is an isomorphism, since $Y$ is projective. The pullback $\mathcal{C} \times_Y Y_1$ is a stable curve over the regular scheme $Y_1$. It is flat with geometrically reduced fibres, so it is reduced. The proof of Lemma 2.3.5 uses only the properties (vi)(a) to (c), which hold for a stable curve, and it shows that $\mathcal{C} \times_Y Y_1$ is integral and that its projection to $\mathcal{C}$ is a projective generically étale alteration. By Lemma 2.3.1 we may replace $\mathcal{C}$ by $\mathcal{C} \times_Y Y_1$ and $Z$ by its inverse image. We arrive at the following situation [dJ96, 4.23].

**Situation A.** $Y$ is a regular projective variety over an algebraically closed field $k$, $D \subseteq Y$ is a divisor with strict normal crossings, $f \colon X \to Y$ is a semistable curve that is smooth over $Y \setminus D$, and $Z = \tau_1(Y) \cup \dots \cup \tau_n(Y) \cup f^{-1}(D)$, where the $\tau_i$ are disjoint sections into $\operatorname{sm}(X/Y)$.

Here we use that a stable curve is semistable. The set $Z$ is the support of a divisor: $f^{-1}(D)$ is the support of the pullback of a Cartier divisor by the flat morphism $f$, and a section into the smooth locus of a morphism of relative dimension 1 is a Cartier divisor. The stability is not needed any more.

### The last blowups

In Situation A the total space $X$ need not be regular. Its singularities are the ones of Section 2.1. By [dJ96, Lemma 3.2], recalled after Theorem 2.1.8, a projective modification with center in $\operatorname{Sing}(X)$ makes $\operatorname{Sing}(X)$ of codimension at least 3. The sections $\tau_i$ still map to the smooth locus, because the center of the modification lies in $\operatorname{Sing}(X) \subseteq \operatorname{Sing}(f)$, which is disjoint from them. At a closed point $y$ of $Y$ the residue field is $k$, which is algebraically closed. So each double point of the fibre $X_y$ is a $k$-rational point, and its two branches are defined over $k$. The fibre need not be split in the sense of [dJ96, 2.22], because a component can meet itself, but the local computation needs only the double points. By [dJ96, 3.5] and Corollary 2.1.4, we arrive at the following situation [dJ96, 4.25].

**Situation B.** $X$ is a projective variety of dimension $d$ over an algebraically closed field $k$, $Z \subseteq X$ is a divisor, the irreducible components of $\operatorname{Sing}(X)$ are regular, and for each closed point $x$ of $X$ one of the following holds:

1. $x$ is a regular point of $X$, and $Z$ is a divisor with normal crossings at $x$;
2. $x$ is a singular point of $X$, and there are integers $2 \le \mu \le r \le d - 1$ such that the completion of $\mathcal{O}_{X,x}$ is isomorphic to $k[[u, v, t_1, \dots, t_{d-1}]]/(uv - t_1 \cdots t_\mu)$, with $Z$ given by $t_1 \cdots t_r = 0$.

Here a divisor has *normal crossings* at a regular point if, in the completion of the local ring, it is given by a product of distinct members of a regular system of parameters. The components of $Z$ through $x$ need not be regular, which is the difference with strict normal crossings.

Let $E$ be an irreducible component of $\operatorname{Sing}(X)$ and let $\pi \colon X' \to X$ be the blowup of $X$ along $E$. At a singular point as in part 2, after a renumbering of the $t_i$, the ideal of $E$ is $(u, v, t_1, t_2)$. We compute the blowup on the polynomial model. This is enough: $X$ is excellent, blowing up commutes with the flat base change to the completion, and so the properties that we need can be read on the model, as de Jong explains in [dJ96, 3.4].

**Proposition 2.4.3.** Let $k$ be a field, let $2 \le \mu \le r \le m$, let
$$P = k[u, v, t_1, \dots, t_m]/(uv - t_1 \cdots t_\mu),$$
let $Z \subseteq \operatorname{Spec} P$ be the closed subset $t_1 \cdots t_r = 0$, and let $X' \to \operatorname{Spec} P$ be the blowup of the ideal $I = (u, v, t_1, t_2)$. Then $X'$ is covered by four affine charts, and:

1. the chart $P[I/u]$ is isomorphic to the polynomial ring $k[u, t_1', t_2', t_3, \dots, t_m]$, with $v = u t_1' t_2' t_3 \cdots t_\mu$, $t_1 = u t_1'$ and $t_2 = u t_2'$, and the inverse image of $Z$ is $u t_1' t_2' t_3 \cdots t_r = 0$; the chart $P[I/v]$ is the same with $u$ and $v$ exchanged;
2. the chart $P[I/t_1]$ is isomorphic to $k[u', v', t_1, t_2', t_3, \dots, t_m]/(u'v' - t_2' t_3 \cdots t_\mu)$, with $u = t_1 u'$, $v = t_1 v'$ and $t_2 = t_1 t_2'$, and the inverse image of $Z$ is $t_1 t_2' t_3 \cdots t_r = 0$; the chart $P[I/t_2]$ is the same with $t_1$ and $t_2$ exchanged.

Lean: `Singularity.Algebra.nodeBlowupChartUEquiv`, `Singularity.Algebra.nodeBlowupChartTEquiv`, `Singularity.Algebra.nodeBlowupChartUHom_Z` (the charts $u$ and $t_1$, over any commutative ring). The charts $v$ and $t_2$, the cover by the four charts and the inverse image of $Z$ as a closed set are not in Lean yet.

*Proof.* As in Proposition 2.1.5, $P$ is a domain of dimension $m + 1$, the charts are subrings of its fraction field, and a surjection between domains of finite type over $k$ of the same dimension is an isomorphism (Section 2.1).

Chart $u$. Map $k[u, t_1', t_2', t_3, \dots, t_m] \to P[I/u]$ by $t_1' \mapsto t_1/u$ and $t_2' \mapsto t_2/u$. In the fraction field,
$$\frac{v}{u} = \frac{uv}{u^2} = \frac{t_1 t_2}{u^2} \, t_3 \cdots t_\mu = \frac{t_1}{u} \cdot \frac{t_2}{u} \cdot t_3 \cdots t_\mu,$$
so $v/u$ is in the image, and so are $t_1 = u \cdot (t_1/u)$, $t_2$ and $v$. So the map is surjective. Both rings have dimension $m + 1$, so it is an isomorphism. The function $t_1 \cdots t_r$ becomes $u^2 t_1' t_2' t_3 \cdots t_r$, whose zero set is $u t_1' t_2' t_3 \cdots t_r = 0$.

Chart $t_1$. Let $Q = k[u', v', t_1, t_2', t_3, \dots, t_m]/(u'v' - t_2' t_3 \cdots t_\mu)$. It is a domain of dimension $m + 1$, as in Proposition 2.1.5. Map $Q \to P[I/t_1]$ by $u' \mapsto u/t_1$, $v' \mapsto v/t_1$, $t_2' \mapsto t_2/t_1$. This is well defined, because
$$\frac{u}{t_1} \cdot \frac{v}{t_1} = \frac{t_1 t_2 t_3 \cdots t_\mu}{t_1^2} = \frac{t_2}{t_1} \, t_3 \cdots t_\mu.$$
The image contains $u = t_1 u'$, $v = t_1 v'$ and $t_2 = t_1 t_2'$, so the map is surjective, and it is an isomorphism. The function $t_1 \cdots t_r$ becomes $t_1^2 t_2' t_3 \cdots t_r$.

The four elements $u, v, t_1, t_2$ generate $I$, so the four charts cover $X'$ (Volume 4, Lemma 1.1.3). The charts $v$ and $t_2$ follow by symmetry. $\square$

In chart $u$ the blowup is regular and the inverse image of $Z$ has normal crossings, since $u, t_1', t_2', t_3, \dots, t_r$ are distinct coordinates of a polynomial ring. In chart $t_1$ we have the model of part 2 of Situation B with $\mu - 1$ factors in the equation, in the coordinates $t_2', t_3, \dots, t_\mu$, and with $Z$ given by the $r$ coordinates $t_1, t_2', t_3, \dots, t_r$. If $\mu = 2$, the equation is $u'v' = t_2'$, the chart is regular by Corollary 2.1.4, and $Z$, given by $t_1 \cdot u'v' \cdot t_3 \cdots t_r = 0$, has normal crossings. The singular locus of chart $t_1$ is the union of the sets $u' = v' = t_i = t_j = 0$ for two distinct coordinates among $t_2', t_3, \dots, t_\mu$. None of them is contained in the exceptional divisor $t_1 = 0$. So they are strict transforms of components of $\operatorname{Sing}(X)$ other than $E$.

**Proposition 2.4.4 (de Jong).** In Situation B, let $E$ be an irreducible component of $\operatorname{Sing}(X)$, let $X' \to X$ be the blowup along $E$, and let $Z'$ be the reduced inverse image of $Z$. Then $(X', Z')$ is again as in Situation B, and $\operatorname{Sing}(X')$ has one irreducible component less than $\operatorname{Sing}(X)$.

Lean: `Singularity.nodeBlowupQOneEquiv` (the chart $t_1$ for $\mu = 2$ is a polynomial ring). The case $\mu \geq 3$ and the count of the components of the singular locus are not in Lean yet.

This is [dJ96, 4.26 and 4.27]. The local statements are Proposition 2.4.3 and the discussion after it. De Jong adds the global statement: the strict transform of another component $E'$ of $\operatorname{Sing}(X)$ is the blowup of $E'$ in the regular closed subscheme $E \cap E'$, so it is regular, and $\operatorname{Sing}(X')$ is the union of these strict transforms.

**Example 2.4.5 (the threefold node).** Let $d = 3$. Then $d - 1 = 2$, and in part 2 of Situation B we must have $\mu = r = 2$. So the only singular model is
$$P = k[u, v, t_1, t_2]/(uv - t_1 t_2),$$
with $Z$ given by $t_1 t_2 = 0$. This is the cone over a smooth quadric surface in $\mathbb{P}^3$. Its singular locus is the origin, so here a component $E$ of $\operatorname{Sing}(X)$ is a point, and the blowup of Proposition 2.4.4 is the blowup of the maximal ideal $I = (u, v, t_1, t_2)$. The set $Z$ has four irreducible components, the planes $u = t_1 = 0$, $u = t_2 = 0$, $v = t_1 = 0$ and $v = t_2 = 0$, because $t_1 t_2 = 0$ forces $uv = 0$.

Proposition 2.4.3 with $\mu = r = m = 2$ gives the charts. The chart $u$ is $k[u, t_1', t_2']$, and $Z'$ is $u t_1' t_2' = 0$. The chart $t_1$ is $k[u', v', t_1, t_2']/(u'v' - t_2')$, which is the polynomial ring $k[u', v', t_1]$, and $Z'$ is $t_1 u' v' = 0$. The charts $v$ and $t_2$ are the same up to symmetry. So $X'$ is regular, and in each chart $Z'$ is the union of three coordinate planes of $\mathbb{A}^3$.

The exceptional divisor is $\operatorname{Proj}$ of the graded ring $\bigoplus_n I^n / I^{n+1}$. The equation $uv - t_1 t_2$ is homogeneous, so this graded ring is $P$ itself, with $u, v, t_1, t_2$ in degree 1. So the exceptional divisor is the quadric $UV = T_1 T_2$ in $\mathbb{P}^3_k$, which is smooth and isomorphic to $\mathbb{P}^1_k \times \mathbb{P}^1_k$ by the Segre embedding. The strict transform of each plane of $Z$ is the blowup of $\mathbb{A}^2_k$ at the origin, because $I$ restricts to the maximal ideal of the origin in each plane. So the five components of $Z'$ are regular, and $Z'$ is a divisor with strict normal crossings.

There is a second way, which is the one of Example 2.1.7. Blow up the ideal $(u, t_1)$ of the plane $u = t_1 = 0$. By Proposition 2.1.5 with $m = 2$ and $g = t_2$, the two charts are $k[u, t_1', t_2]$ and $k[u', v, t_1, t_2]/(u'v - t_2) \cong k[u', v, t_1]$. So this blowup is regular too. Its fibre over the origin is the line $v = t_1 = 0$ of the second chart, completed by one point of the first chart, so it is a projective line, of codimension 2. This blowup is a *small* resolution: it adds no divisor. De Jong's procedure always blows up a component of $\operatorname{Sing}(X)$, so it does not depend on the choice of a plane, and its exceptional set is a divisor that becomes part of $Z'$.

**End of the proof of Theorem 1.2.1.** After finitely many blowups as in Proposition 2.4.4, the scheme $X$ is regular and $Z$ is a divisor with normal crossings. A further sequence of blowups in regular centers inside $Z$ makes $Z$ a divisor with strict normal crossings and keeps $X$ regular [dJ96, 2.4 and 4.28]. All the alterations in Sections 2.3 and 2.4 are projective. Over the algebraically closed field of Step 1 they are generically étale, and if $k$ is perfect the alteration of Step 1 is generically étale too. This finishes the proof. $\square$

### The proof for surfaces

We follow the proof once more for $d = 2$, where each step can be seen.

**Example 2.4.6 (surfaces).** Let $X$ be a variety of dimension 2 over an algebraically closed field $k$, and let $Z \subsetneq X$ be closed. Steps 2 to 4 make $X$ a normal projective surface and $Z$ the support of a divisor, so $Z$ is a finite union of curves. Lemma 2.3.3 blows up the finitely many points over a general point $p$ of $\mathbb{P}^2_k$ and gives the pencil $f \colon X \to \mathbb{P}^1_k$. The Stein factorization is $\mathbb{P}^1_k$ itself, so $f$ has connected fibres. Lemma 2.3.4 adds a curve $H$ to $Z$, finite over $\mathbb{P}^1_k$, that meets each component of each fibre in at least three smooth points.

The base is now the curve $Y = \mathbb{P}^1_k$, with function field $k(t)$. The components $Z_i$ of $Z$ are curves, finite over $Y$, and $k(Z_i)$ is a finite separable extension of $k(t)$. Step 5 takes a Galois extension $L$ of $k(t)$ that contains each $k(Z_i)$, and $Y'$ is the smooth projective curve with function field $L$. After the base change, each $Z_i$ splits into sections. Step 6 is the stable reduction of the family of curves over the curve $Y'$. In this case Hypothesis 2.2.5 is the stable reduction of curves over a curve. In the proof of Proposition 2.2.6 the new base has the function field $k(W)$, and by Lemma 2.2.9 it is a Galois extension of the function field of $Y'$ of degree at most $|\mathrm{GL}_{2g}(\mathbb{F}_\ell)|$, where $g$ is the genus of the generic fibre.

In Section 2.4 the base is a curve, and two steps become trivial. Let $S$ be the normalization of the base. It is a regular curve. An integral scheme that dominates a regular curve is flat over it, because a torsion free module over a discrete valuation ring is flat. So (h) and (i) hold after the normalization, with no flattening. The induction hypothesis is Proposition 1.2.3, and for a curve over $k$ it is the normalization, which we have already done. So the alteration of the induction step has degree 1.

In Situation A the set $D$ is a finite set of points of the regular curve $Y$. Let $x$ be a node of the fibre over $y \in D$, and let $t$ be a uniformizer at $y$. By Proposition 2.1.2 the complete local ring of $X$ at $x$ is $k[[t]][[u, v]]/(uv - h)$, and $h = \varepsilon t^n$ with $\varepsilon$ a unit and $n \ge 1$. Replace $u$ by $\varepsilon^{-1} u$. The equation becomes $uv = t^n$. This is the surface of Example 2.1.6, and the $n - 1$ blowups of Example 2.1.6 resolve it, with a chain of $n - 1$ projective lines over $x$. The proof of de Jong uses the second way of Example 2.1.6, as in [dJ96, Lemma 3.2]: it blows up the singular point, and $\lfloor n/2 \rfloor$ blowups give a regular surface. Either way gives a regular surface and a projective morphism that is an isomorphism outside $x$, and for the proof this is all that matters. Example 2.2.10 carries out this step for a family of elliptic curves. Situation B has no singular points for $d = 2$, because part 2 asks for $2 \le \mu \le d - 1 = 1$. Then $X$ is regular, $Z$ is the union of the sections and of the fibres over $D$, and $Z$ has normal crossings. The last blowups of [dJ96, 2.4] separate the self intersections of the components of $Z$.

The degree of the final alteration $X_1 \to X$ is the product in the table of Section 2.3. Here $k$ is algebraically closed, and the only steps of degree greater than 1 are Steps 5 and 6. So the degree is $[k(Y_1) : k(t)]$, where $Y_1$ is the final base curve. The proof gives no bound for this degree in terms of $X$ alone, because the Galois closure in Step 5 depends on the curve $H$ and on the projection.

### What is proved and what is cited

We list what the proof in this chapter takes from outside. This is the precise sense in which the volume proves Theorem 1.2.1 *modulo the moduli of stable curves*.

1. Hypothesis 2.2.5, the extension of a family of smooth pointed curves to a stable curve after a generically étale alteration of the base. It follows from Hypothesis 2.2.4 by Proposition 2.2.6, and Hypothesis 2.2.4 summarizes [DM69, Knu83] as in [dJ96, 2.24].
2. Standard results of algebraic geometry: the limit theorems of [EGA4] in Step 1, Chow's lemma, generic flatness, the Stein factorization, the purity of the branch locus, the étaleness of the Stein factorization of a proper flat morphism with geometrically reduced fibres, the fact that $\mathbb{P}^{d-1}$ over an algebraically closed field has no nontrivial connected finite étale covers, Serre's criterion for normality, and the flattening of [dJ96, 2.19].
3. Results of de Jong that we cite or state with a sketch: the two facts of general position (A) and (B) in the proof of Lemma 2.3.3, Lemma 2.3.4, Lemma 2.4.1, the change of coordinates in the second half of Proposition 2.1.2 [dJ96, 2.23], the local form at a point of a fibre over a divisor with strict normal crossings [dJ96, 3.5], Lemma 3.2 of [dJ96], the global part of Proposition 2.4.4, and the passage from normal crossings to strict normal crossings [dJ96, 2.4].

The reductions (Lemmas 2.3.1, 2.3.2 and 2.3.5, Steps 1 to 6), Lemma 2.3.3 modulo (A) and (B), the étaleness of the Stein factorization in Section 2.3, which de Jong cites in [dJ96, 4.12], Propositions 2.2.6 and 2.4.2, Lemma 2.2.9, the first half of Proposition 2.1.2, and the local algebra (Lemma 2.1.3, Propositions 2.1.5 and 2.4.3) are proved here, modulo the standard results of item 2. A complete proof of Theorem 1.2.1 modulo Hypothesis 2.2.5 alone would need full proofs of the items in 3. Each of them is elementary in the sense that it uses no moduli theory, but some of them, for example Lemma 2.3.3, need careful general position arguments.

### Notes and references

The structure of the proof is the one of [dJ96, Section 4]. The semistable version over a trait, Theorem 1.2.5, has a proof with the same structure [dJ96, Section 6]. It uses a relative form of the fibration in curves [dJ96, Theorem 5.8], and at the end it uses Theorem 2.1.8 in place of Proposition 2.4.4 [dJ96, 6.16]. Nothing of this chapter is in Lean.
