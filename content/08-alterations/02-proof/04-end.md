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

Let $S' \to S$ be a modification. Then the strict transforms of $X$, $\mathcal{C}$ and $T$ over $S'$ again have the properties (a) to (c), (e) and (g), and the strict transform of $T$ is the closure of the graph of the pullback of $\beta$ [dJ96, 4.18]. The flattening theorem of Raynaud-Gruson, in the form of [dJ96, 2.19], gives a modification $S' \to S$ such that the strict transforms of the projective morphisms $X \to S$ and $T \to S$ are flat. After a further normalization of $S$, we may assume:

(h) $X$ and $T$ are flat over $S$;

(i) $S$ is normal.

Fix $s \in S$. Write $X_s = X_1 \cup \dots \cup X_r$, $\mathcal{C}_s = C_1 \cup \dots \cup C_c$ and $T_s = T_1 \cup \dots \cup T_t$ for the decompositions into irreducible components. Since $T$ is flat over $S$, the fibre $T_s$ has pure dimension 1.

**Lemma 2.4.1 (de Jong).** In this situation:

1. for each $i$ there is exactly one $j$ with $\mathrm{pr}_2(T_j) = X_i$, and $\mathrm{pr}_1$ is not constant on this $T_j$;
2. for each $i$ there is exactly one $j$ with $\mathrm{pr}_1(T_j) = C_i$.

Lean: none yet

This is [dJ96, Lemma 4.20]. *Sketch of proof.* The first statement of each part comes from normality. At a point $x$ of $\operatorname{sm}(X/S) \cap X_s$, the scheme $X$ is normal, since $S$ is normal and $X \to S$ is smooth at $x$. There are only finitely many closed points of $X_s$ over which $\mathrm{pr}_2$ has a fibre of dimension 1, so near a general point $x$ of $X_i$ in the smooth locus, $\mathrm{pr}_2$ is finite and birational over a normal scheme, hence an isomorphism. This gives exactly one component $T_j$ over $X_i$. The same argument for $\mathrm{pr}_1$ and the smooth locus of $\mathcal{C} \to S$ gives the first statement of part 2. By Zariski's main theorem in the form of the Stein factorization, $\mathrm{pr}_2^{-1}(x)$ is connected for each normal point $x$ of $X$.

Now suppose that $\mathrm{pr}_1$ is constant on the component $T_j$ over $X_i$, with image a point $c \in \mathcal{C}_s$. By (e) there are three distinct marked points $x_\alpha = \sigma_\alpha(s)$, $x_{\beta'}$, $x_\gamma$ on $X_i$ in the smooth locus. Let $T_\alpha = \mathrm{pr}_2^{-1}(x_\alpha)$, and similarly for $\beta'$ and $\gamma$; they are connected and meet $T_j$. Let $c_\alpha = \tau_\alpha(s)$, and similarly for $\beta'$ and $\gamma$. These are three distinct points of $\mathcal{C}_s$, because the sections of a stable curve are disjoint, and $T_\alpha$ connects $c$ with $c_\alpha$. If $c$ is not one of $c_\alpha, c_{\beta'}, c_\gamma$, then $\mathrm{pr}_1(T_\alpha)$, $\mathrm{pr}_1(T_{\beta'})$ and $\mathrm{pr}_1(T_\gamma)$ are curves through $c$ with no common component, by part 2, so at least three components of $\mathcal{C}_s$ pass through $c$. A nodal curve does not allow this. If $c = c_\alpha$, then the curves $\mathrm{pr}_1(T_{\beta'})$ and $\mathrm{pr}_1(T_\gamma)$ meet at the marked point $c_\alpha$, and this is not possible because a marked point of a stable curve lies on only one component, in the smooth locus. $\square$

**Proposition 2.4.2.** In the situation of (a) to (c), (e) and (g) to (i), the projection $\mathrm{pr}_1 \colon T \to \mathcal{C}$ is an isomorphism. So $\beta$ extends to a proper birational morphism $\mathrm{pr}_2 \circ \mathrm{pr}_1^{-1} \colon \mathcal{C} \to X$.

Lean: none yet

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

In Situation A the total space $X$ need not be regular. Its singularities are the ones of Section 2.1. By [dJ96, Lemma 3.2], recalled after Theorem 2.1.8, a projective modification with center in $\operatorname{Sing}(X)$ makes $\operatorname{Sing}(X)$ of codimension at least 3. The sections $\tau_i$ still map to the smooth locus, because the center of the modification lies in $\operatorname{Sing}(X) \subseteq \operatorname{Sing}(f)$, which is disjoint from them. At a closed point the fibre is split, since $k$ is algebraically closed. By [dJ96, 3.5] and Corollary 2.1.4, we arrive at the following situation [dJ96, 4.25].

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

Lean: none yet

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

Lean: none yet

This is [dJ96, 4.26 and 4.27]. The local statements are Proposition 2.4.3 and the discussion after it. De Jong adds the global statement: the strict transform of another component $E'$ of $\operatorname{Sing}(X)$ is the blowup of $E'$ in the regular closed subscheme $E \cap E'$, so it is regular, and $\operatorname{Sing}(X')$ is the union of these strict transforms.

**End of the proof of Theorem 1.2.1.** After finitely many blowups as in Proposition 2.4.4, the scheme $X$ is regular and $Z$ is a divisor with normal crossings. A further sequence of blowups in regular centers inside $Z$ makes $Z$ a divisor with strict normal crossings and keeps $X$ regular [dJ96, 2.4 and 4.28]. All the alterations in Sections 2.3 and 2.4 are projective. Over the algebraically closed field of Step 1 they are generically étale, and if $k$ is perfect the alteration of Step 1 is generically étale too. This finishes the proof. $\square$

### What is proved and what is cited

We list what the proof in this chapter takes from outside. This is the precise sense in which the volume proves Theorem 1.2.1 *modulo the moduli of stable curves*.

1. Hypothesis 2.2.5, the extension of a family of smooth pointed curves to a stable curve after a generically étale alteration of the base. It follows from Hypothesis 2.2.4 by Proposition 2.2.6, and Hypothesis 2.2.4 summarizes [DM69, Knu83] as in [dJ96, 2.24].
2. Standard results of algebraic geometry: the limit theorems of [EGA4] in Step 1, Chow's lemma, generic flatness, the Stein factorization, the fact that $\mathbb{P}^{d-1}$ over an algebraically closed field has no nontrivial connected finite étale covers, Serre's criterion for normality, and the flattening of [dJ96, 2.19].
3. Results of de Jong that we state with a sketch: Lemma 2.3.3 (the fibration, with the projections of [dJ96, 2.11] and a Bertini argument), the étaleness of the Stein factorization [dJ96, 4.12], Lemma 2.3.4, Lemma 2.4.1, the local form of semistable curves [dJ96, 2.23 and 3.5], Lemma 3.2 of [dJ96], the global part of Proposition 2.4.4, and the passage from normal crossings to strict normal crossings [dJ96, 2.4].

The reductions (Lemmas 2.3.1, 2.3.2 and 2.3.5, Steps 1 to 6), Proposition 2.2.6, Proposition 2.4.2, and the local algebra (Lemma 2.1.3, Propositions 2.1.5 and 2.4.3) are proved here, modulo the standard results of item 2. A complete proof of Theorem 1.2.1 modulo Hypothesis 2.2.5 alone would need full proofs of the items in 3. Each of them is elementary in the sense that it uses no moduli theory, but some of them, for example Lemma 2.3.3, need careful general position arguments.

### Notes and references

The structure of the proof is the one of [dJ96, Section 4]. The semistable version over a trait, Theorem 1.2.5, has a proof with the same structure [dJ96, Section 6]. It uses a relative form of the fibration in curves [dJ96, Theorem 5.8], and at the end it uses Theorem 2.1.8 in place of Proposition 2.4.4 [dJ96, 6.16]. Nothing of this chapter is in Lean.
