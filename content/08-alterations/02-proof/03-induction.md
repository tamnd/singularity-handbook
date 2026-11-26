---
title: The reductions and the fibration in curves
nodes: [SG0000001K]
sources: [dJ96, Stacks, EGA4, Har, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The reductions and the fibration in curves

We now begin the proof of Theorem 1.2.1. The proof is an induction on $d = \dim X$. For $d = 0$ the variety $X$ is the spectrum of a finite field extension of $k$, and we can take $X_1 = \bar X_1 = X$ and $\varphi_1$ the identity. For $d = 1$, Proposition 1.2.3 gives the theorem. Assume $d \ge 2$ and that the theorem holds in dimension $d - 1$. This section reduces the theorem for a pair $(X, Z)$ to a pair with a list of extra properties, and the last of them is a family of stable pointed curves over a dense open subset of a base of dimension $d - 1$. We follow [dJ96, 4.3 to 4.17].

### The method

**Lemma 2.3.1.** Let $(X, Z)$ be as in Theorem 1.2.1, let $\varphi \colon X' \to X$ be an alteration, and let $Z' = \varphi^{-1}(Z)$. Then $Z'$ is a proper closed subset of $X'$. If the theorem holds for $(X', Z')$, then it holds for $(X, Z)$. If also $\varphi$ is generically étale and the theorem holds for $(X', Z')$ with a generically étale alteration, then it holds for $(X, Z)$ with a generically étale alteration.

Lean: none yet

*Proof.* The morphism $\varphi$ is dominant, so it maps the generic point of $X'$ to the generic point of $X$, which is not in $Z$. So $Z' \ne X'$. Let $\varphi_1' \colon X_1 \to X'$ and $j_1 \colon X_1 \to \bar X_1$ solve the problem for $(X', Z')$. Then $\varphi \circ \varphi_1'$ is an alteration (Lemma 1.1.6), and $(\varphi \circ \varphi_1')^{-1}(Z) = \varphi_1'^{-1}(Z')$. So $\varphi \circ \varphi_1'$ and $j_1$ solve the problem for $(X, Z)$. The statement on generically étale alterations is the last part of Lemma 1.1.6. $\square$

We use the lemma in the following way. We name properties (i), (ii), and so on of a pair $(X, Z)$. At each step we construct an alteration $X' \to X$, generically étale if $k$ is perfect, such that the pair $(X', Z')$ has the properties obtained so far and one more. By the lemma it is enough to prove the theorem for $(X', Z')$. In the final form, Theorem 1.2.1 also asks for a generically étale alteration when $k$ is perfect, and we check this at each step.

The table lists the steps of Sections 2.3 and 2.4 and the kind of alteration that each step makes. The degree of the final alteration is the product of the degrees in the last column. Four steps can have a degree greater than 1: the change of field in Step 1, the two alterations of the base in Steps 5 and 6, and the alteration of the base that the induction hypothesis gives in Section 2.4.

| Step | Property obtained | Alteration of $X$ | Degree |
| --- | --- | --- | --- |
| 1 | (i) $k$ algebraically closed | a component of $X \times_k k_1$ | $[k_1 : k]$ at most |
| 2 | (ii), (iii) $X$ projective | Chow's lemma, then a compactification | 1 |
| 3 | (iv) $Z$ a divisor | blowup of $Z$ | 1 |
| 4 | (v) $X$ normal | normalization | 1 |
| Lemma 2.3.3 | (vi)(a) to (d), a fibration in curves | blowup of finitely many points | 1 |
| Lemma 2.3.4 | (vi)(e), three points on each fibre | none, $Z$ is enlarged | 1 |
| 5 | (vi)(f), sections | base change by a Galois cover of $Y$ | $[L : k(Y)]$ |
| 6 | (vi)(g), a stable model | base change by Hypothesis 2.2.5 | $\deg \psi$ |
| Section 2.4 | the extension of $\beta$ | modification of $Y$, then $\beta$ | 1 |
| Section 2.4 | $Y$ regular | base change by the induction hypothesis | $\deg(Y_1 \to Y)$ |
| Section 2.4 | $X$ regular | blowups | 1 |

### Algebraically closed, projective, and a divisor

**Step 1. The field.** We may assume:

(i) the field $k$ is algebraically closed.

Let $\bar k$ be an algebraic closure of $k$, and let $X^\dagger$ be an irreducible component of $X \times_k \bar k$, with its reduced structure, and $Z^\dagger$ the inverse image of $Z$. Assume that the theorem holds for $(X^\dagger, Z^\dagger)$ over $\bar k$. The solution consists of finitely many schemes of finite type and morphisms between them. By the limit theorems of [EGA4, Section 8], they are defined over a finite extension $k_1$ of $k$ inside $\bar k$: there are a component $X'$ of $X \times_k k_1$ and a solution for $(X', \varphi^{-1}(Z))$ over $k_1$ whose base change to $\bar k$ is the given one. The properties that we need (regular, projective, a divisor with strict normal crossings) descend from $\bar k$ to $k_1$ for a large enough $k_1$, since $\operatorname{Spec} \bar k \to \operatorname{Spec} k_1$ is faithfully flat. The morphism $X' \to X$ is finite and surjective, so it is an alteration, and Lemma 2.3.1 gives the theorem for $(X, Z)$. If $k$ is perfect, then $k_1/k$ is separable, $X \times_k k_1 \to X$ is finite étale, and $X' \to X$ is generically étale. This is [dJ96, 4.5].

This step is the reason why the alteration of Theorem 1.2.1 can be inseparable over an imperfect field. The scheme $X_1$ is a $k_1$-scheme, and $k_1/k$ can be inseparable. The step also gives Remark 4.2 of [dJ96]: over $\bar k$ the variety $\bar X_1$ is regular, hence smooth over $\bar k$, and so $\bar X_1$ is smooth over $k_1$.

**Step 2. Projective.** We may assume, in addition to (i):

(ii) $X$ is quasi-projective;

(iii) $X$ is projective.

By Chow's lemma for varieties [Stacks] there is a modification $X' \to X$ with $X'$ quasi-projective, and Lemma 2.3.1 gives (ii). Assume (ii), and let $X \subseteq \bar X$ be an open immersion into a projective variety. Let $\bar Z$ be the union of the closure of $Z$ and of $\bar X \setminus X$. Assume that $\bar\varphi \colon \bar X_1' \to \bar X$ and $\bar j \colon \bar X_1' \to \bar X_1$ solve the problem for $(\bar X, \bar Z)$. Then $\bar X_1'$ is proper over $k$, since $\bar\varphi$ is proper and $\bar X$ is projective. So the open immersion $\bar j$ has a closed image, and as $\bar X_1$ is irreducible, $\bar j$ is an isomorphism. Let $X_1 = \bar\varphi^{-1}(X)$, let $\varphi_1$ be the restriction of $\bar\varphi$, and let $j_1$ be the inclusion of $X_1$ in $\bar X_1'$. Then $\varphi_1$ is an alteration, and since the closure of $Z$ meets $X$ in $Z$,
$$j_1(\varphi_1^{-1}(Z)) \cup (\bar X_1' \setminus X_1) = \bar\varphi^{-1}(\bar Z),$$
which is a divisor with strict normal crossings. This is [dJ96, 4.6 and 4.7].

**Step 3. A divisor.** We may assume, in addition to (i) and (iii):

(iv) $Z$ is the support of a divisor $D$ on $X$.

Let $X' \to X$ be the blowup of $X$ along $Z$, with its reduced structure. It is a projective modification, since $Z \ne X$, and the inverse image of $Z$ is the support of the exceptional divisor, which is an effective Cartier divisor (Volume 4, Theorem 1.1.2). This is [dJ96, 4.8].

Two remarks make the later steps work. First, the properties (i), (iii) and (iv) are kept by each projective alteration $X' \to X$: the inverse image of a Cartier divisor under a dominant morphism of integral schemes is a Cartier divisor. Second, under (iii) and (iv) we may *enlarge* $Z$.

**Lemma 2.3.2.** Assume (iii) and (iv), and let $Z \subseteq Z'$ be a proper closed subset of $X$. If the theorem holds for $(X, Z')$, then it holds for $(X, Z)$, with the same alteration.

Lean: none yet

*Proof.* Let $\varphi_1 \colon X_1 \to X$ and $j_1$ solve the problem for $(X, Z')$. As in Step 2, $X_1$ is proper, so $j_1$ is an isomorphism and we may take $X_1 = \bar X_1$. The set $\varphi_1^{-1}(Z)$ is the support of the Cartier divisor $\varphi_1^* D$, so each of its irreducible components has codimension 1 in $X_1$ by the principal ideal theorem. It is contained in the divisor with strict normal crossings $\varphi_1^{-1}(Z')$. So each irreducible component of $\varphi_1^{-1}(Z)$ is an irreducible closed subset of codimension 1 contained in the union of the components of $\varphi_1^{-1}(Z')$, and so it is one of these components. A union of irreducible components of a divisor with strict normal crossings is a divisor with strict normal crossings, by Definition 1.1.10. $\square$

**Step 4. Normal.** Taking for $X'$ the normalization of $X$, which is a finite modification (Volume 1, Theorem 2.4.7), we may assume, in addition to (i), (iii) and (iv):

(v) $X$ is normal.

### The fibration in curves

The next lemma is the geometric heart of the reduction. It fibres $X$ in curves after a blowup of finitely many points. The idea is classical. A projective variety of dimension $d$ is a finite cover of $\mathbb{P}^d$, and the lines through a point $p$ of $\mathbb{P}^d$ form a family of curves parametrized by $\mathbb{P}^{d-1}$. The inverse images of these lines fibre $X$ in curves, but all of them pass through the finitely many points over $p$. The blowup of these points separates the curves. We prove the lemma of [dJ96, Lemma 4.11] modulo two facts of general position.

**Lemma 2.3.3 (de Jong).** Assume that $(X, Z)$ has the properties (i) to (v), and let $d = \dim X$. There are a modification $\varphi \colon X' \to X$ and a morphism $f \colon X' \to \mathbb{P}^{d-1}_k$ such that:

1. $\varphi$ is the blowup of $X$ in a finite set of closed points of $\operatorname{Reg}(X) \setminus Z$;
2. all fibres of $f$ are nonempty and of pure dimension 1, the smooth locus of $f$ is dense in each fibre, and at least one fibre of $f$ is smooth;
3. the restriction of $f$ to $Z' = \varphi^{-1}(Z)$ is finite, and it is étale over a nonempty open subset of $\mathbb{P}^{d-1}_k$.

Lean: none yet

*Proof.* We use two facts of general position from [dJ96].

(A) Embed $X$ in $\mathbb{P}^N_k$. A composition of general linear projections gives a finite surjective morphism $\pi \colon X \to \mathbb{P}^d_k$ that is étale over a dense open subset of $\mathbb{P}^d_k$ [dJ96, 2.11].

(B) For a general closed point $p$ of $\mathbb{P}^d_k$, the morphism $f$ that we construct below has a smooth fibre, and its restriction to $Z'$ is étale over a nonempty open subset of $\mathbb{P}^{d-1}_k$. This is part of the statement of [dJ96, Lemma 4.11], and its proof is a Bertini argument.

We prove the rest. Let $B \subsetneq \mathbb{P}^d_k$ be the closed set over which $\pi$ is not étale, and let $V = \mathbb{P}^d_k \setminus B$. The image $\pi(Z)$ is closed of dimension at most $d - 1$, because $\pi$ is finite. Choose a closed point $p \notin B \cup \pi(Z)$ that is general in the sense of (B).

Let $\beta \colon P' \to \mathbb{P}^d_k$ be the blowup of the point $p$. It is the closed subscheme of $\mathbb{P}^d_k \times \mathbb{P}^{d-1}_k$ of the pairs $(x, t)$ such that $x$ lies on the line $\ell_t$ through $p$ with direction $t$ [Har, Section II.7]. The second projection $q \colon P' \to \mathbb{P}^{d-1}_k$ is a $\mathbb{P}^1$-bundle, so it is smooth and proper of relative dimension 1, and its fibre over a point $t$ is the line $\ell_t$. The exceptional divisor $E = \beta^{-1}(p)$ maps isomorphically to $\mathbb{P}^{d-1}_k$ by $q$, so it meets each fibre $\ell_t$ in exactly one point $e_t$.

Let $X' = X \times_{\mathbb{P}^d_k} P'$, with the projections $\varphi \colon X' \to X$ and $\pi' \colon X' \to P'$, and let $f = q \circ \pi'$. Over $\mathbb{P}^d_k \setminus \{p\}$ the morphism $\beta$ is an isomorphism, so $\varphi$ is an isomorphism over $X \setminus \pi^{-1}(p)$. Over $V$ the morphism $\pi$ is étale, hence flat, and the formation of a blowup commutes with flat base change [Stacks]. So over $\pi^{-1}(V)$ the morphism $\varphi$ is the blowup of the closed subscheme $\pi^{-1}(p)$. This subscheme is reduced and finite, because $\pi$ is étale over $p$. Its points are regular points of $X$, because $\mathbb{P}^d_k$ is regular and $\pi$ is étale there, and they are not in $Z$, because $p \notin \pi(Z)$. The two open sets $\mathbb{P}^d_k \setminus \{p\}$ and $V$ cover $\mathbb{P}^d_k$, so $\varphi$ is the blowup of $X$ in the finite set $\pi^{-1}(p)$. In particular $X'$ is integral of dimension $d$. This proves part 1.

For part 2, let $t$ be a point of $\mathbb{P}^{d-1}_k$, closed or not, and let $X'_t$ be the fibre of $f$. It is $\pi'^{-1}(\ell_t)$, and $\pi'$ is finite as a base change of $\pi$, so $\dim X'_t \le 1$. The morphism $f$ is surjective, so $X'_t$ is not empty. Each irreducible component of $X'_t$ has dimension at least $\dim X' - \dim \mathbb{P}^{d-1}_k = 1$ [Har, Exercise II.3.22]. So $X'_t$ has pure dimension 1. Let $C$ be an irreducible component of $X'_t$. Its image $\pi'(C)$ is closed, irreducible and of dimension 1 in the irreducible curve $\ell_t$, so $\pi'(C) = \ell_t$, and $C$ contains a point $c$ with $\pi'(c) = e_t$. The set $\beta^{-1}(V)$ is an open neighbourhood of $E$, and $\pi'$ is étale over it, as a base change of $\pi$ over $V$. So $f = q \circ \pi'$ is smooth at $c$. The smooth locus of $f$ is open in $X'$, so its intersection with $C$ is a nonempty open subset of the irreducible space $C$, and it is dense in $C$. This holds for each component, so the smooth locus of $f$ is dense in $X'_t$. The smooth fibre is (B).

For part 3, the morphism $\varphi$ is an isomorphism over a neighbourhood of $Z$, so $Z' \cong Z$, and $f|_{Z'}$ is the composite of the finite morphism $\pi|_Z \colon Z \to \pi(Z)$ and the linear projection from $p$, restricted to the closed subset $\pi(Z)$ of $\mathbb{P}^d_k \setminus \{p\}$. Let $W$ be a closed subset of $\mathbb{P}^d_k$ with $p \notin W$. The projection from $p$ restricted to $W$ is proper, because $W$ is projective. Its fibre over $t$ is $W \cap \ell_t$, which is finite, because the line $\ell_t$ contains $p$ and so is not contained in $W$. A proper morphism with finite fibres is finite. So $f|_{Z'}$ is finite. The generic étaleness is (B). $\square$

For $d = 2$ the lemma says the following. A normal projective surface $X$ is a finite cover $\pi$ of $\mathbb{P}^2$. The lines through a general point $p$ form the pencil $\mathbb{P}^1$, and their inverse images are curves on $X$ that all pass through the points of $\pi^{-1}(p)$. After the blowup of these points, the curves become the fibres of a morphism $f \colon X' \to \mathbb{P}^1$. Each exceptional curve of the blowup is a section of $f$, and $f$ is smooth along it.

Apply the lemma and replace $X$ by $X'$. The blowup is at regular points outside $Z$, so it keeps (i) to (v). Let $X \to Y \to \mathbb{P}^{d-1}_k$ be the Stein factorization of $f$. The morphism $Y \to \mathbb{P}^{d-1}_k$ is finite étale, because the smooth locus of $f$ is dense in each fibre. De Jong does not prove this fact. He cites it from the literature in [dJ96, 4.12]. We give a proof from the purity of the branch locus.

*Proof that $Y \to \mathbb{P}^{d-1}_k$ is étale.* Write $P = \mathbb{P}^{d-1}_k$, $Y = \operatorname{Spec}_P f_* \mathcal{O}_X$ and $g \colon Y \to P$. Since $X$ is normal and integral, $Y$ is normal and integral, and $g$ is finite and surjective. The purity theorem of Zariski-Nagata says that for a finite surjective morphism from a normal integral scheme to a regular integral scheme, the set of points where the morphism is not étale is empty or of pure codimension 1 [Stacks]. So it is enough to show that $g$ is étale at each point $y$ of codimension 1 of $Y$. Since $g$ is finite and surjective, $\xi = g(y)$ has codimension 1 in $P$, and $R = \mathcal{O}_{P, \xi}$ is a discrete valuation ring with a uniformizer $\varpi$. Let $X_R = X \times_P \operatorname{Spec} R$. It is integral and normal, and it dominates $\operatorname{Spec} R$, so it is flat over $R$, because a torsion free module over a discrete valuation ring is flat. The formation of $f_* \mathcal{O}_X$ commutes with flat base change, so $Y \times_P \operatorname{Spec} R$ is the Stein factorization of $X_R \to \operatorname{Spec} R$.

We show that the closed fibre $X_\xi$ is geometrically reduced. It is the principal divisor $V(\varpi)$ on the normal scheme $X_R$. A normal Noetherian scheme has the property $S_2$, so $V(\varpi)$ has the property $S_1$: it has no embedded points. Let $\bar\kappa$ be an algebraic closure of $\kappa(\xi)$. The associated points of $X_\xi \otimes_{\kappa(\xi)} \bar\kappa$ lie over the associated points of $X_\xi$ [Mat], so they are the generic points of its irreducible components. At these points $X_\xi \otimes \bar\kappa$ is reduced, because the smooth locus of $X_\xi$ is dense in $X_\xi$. A Noetherian scheme with no embedded points that is reduced at its generic points is reduced. So $X_\xi$ is geometrically reduced. For a proper flat morphism of finite presentation with geometrically reduced fibres, the Stein factorization is finite étale [Stacks]. So $g$ is étale over $\xi$, and in particular at $y$. $\square$

Since $\mathbb{P}^{d-1}_k$ over an algebraically closed field has no nontrivial connected finite étale covers, $Y = \mathbb{P}^{d-1}_k$, and all fibres of $f$ are geometrically connected. A morphism with a smooth fibre over a regular base is smooth over a dense open subset [dJ96, 2.8], so the generic fibre of $f$ is smooth. We arrive at the following property, in addition to (i) to (v):

(vi) There is a morphism $f \colon X \to Y$ of projective varieties such that: (a) all fibres of $f$ are nonempty, geometrically connected, and of pure dimension 1; (b) the smooth locus of $f$ is dense in each fibre; (c) the generic fibre of $f$ is smooth; (d) the restriction $f|_Z \colon Z \to Y$ is finite and generically étale.

### Enough points on each fibre

**Lemma 2.3.4 (de Jong).** Let $f \colon X \to Y$ be a morphism of projective varieties over an algebraically closed field with the properties (vi)(a) and (vi)(b). There is a divisor $H \subseteq X$ such that $f|_H \colon H \to Y$ is finite and generically étale, and such that, for each geometric point $\bar y$ of $Y$ and each irreducible component $C$ of $X_{\bar y}$, the set $\operatorname{sm}(X/Y) \cap C \cap H$ has at least 3 points.

Lean: none yet

This is [dJ96, Lemma 4.13]. *Sketch of proof.* Let $\mathcal{L}$ be very ample on $X$ and embed $X$ by $\mathcal{L}^{\otimes n}$ with $n \ge 3$. Then each curve $C \subseteq X$ has degree at least $n$ in this embedding, and it is not contained in a linear subspace of dimension $n - 1$. A dimension count shows that a general hyperplane contains no component of any fibre, so it meets $X$ in a divisor $H$ that is finite over $Y$. Near a given closed point $y$ of $Y$, a general hyperplane also meets $f^{-1}(y)$ transversally and only in the smooth locus of $f$. Then $H$ is finite étale over a neighbourhood of $y$, and it meets each component $C$ of a nearby fibre in $\deg C \ge n \ge 3$ distinct smooth points. Noetherian induction on $Y$ and a finite union of such divisors give the lemma. $\square$

Replace $Z$ by $Z \cup H$, which is allowed by Lemma 2.3.2. We get, in addition to (i) to (v) and (vi)(a) to (d):

(vi)(e) for each geometric point $\bar y$ of $Y$ and each irreducible component $C$ of $X_{\bar y}$, the set $\operatorname{sm}(X/Y) \cap C \cap Z$ has at least 3 points.

### Base change by alterations of the base

From now on we alter the base $Y$, and we change $X$ by the strict transform. The next lemma gives the properties of this operation.

**Lemma 2.3.5.** Let $f \colon X \to Y$ and $Z$ have the properties (i), (iii), (iv) and (vi)(a) to (e). Let $\psi \colon Y' \to Y$ be a projective generically étale alteration. Let $X'$ be the reduced scheme of $Y' \times_Y X$, with $f' \colon X' \to Y'$ and $\varphi \colon X' \to X$ the projections, and let $Z' = \varphi^{-1}(Z)$. Then $X'$ is integral, $\varphi$ is a projective generically étale alteration of degree $\deg \psi$, and $(X', Z')$ with $f'$ has the properties (i), (iii), (iv) and (vi)(a) to (e).

Lean: none yet

*Proof.* Let $W = Y' \times_Y X$ and let $W_0 \subseteq W$ be the inverse image of the smooth locus $\operatorname{sm}(X/Y)$. Then $W_0 \to Y'$ is smooth, as a base change of a smooth morphism. Its generic fibre is the base change of the generic fibre $X_\eta$ of $f$ to $k(Y')$. The scheme $X_\eta$ is smooth and geometrically connected over $k(Y)$, so it is geometrically integral, and so the generic fibre of $W_0 \to Y'$ is integral. A smooth morphism is flat, so each irreducible component of $W_0$ dominates $Y'$, by going down for flat morphisms. Its generic point then lies in the generic fibre, which is irreducible. So $W_0$ is irreducible. Each fibre $W_{y'} = X_{\psi(y')} \times \kappa(y')$ contains $W_0 \cap W_{y'}$ as a dense open subset, by (vi)(b). So each point of $W$ is in the closure of $W_0$, and $W$ is irreducible. So $X' = W_{\mathrm{red}}$ is integral.

The projection $W \to X$ is a base change of $\psi$, so it is projective and surjective, and so is $\varphi$. The fibre of $\varphi$ over the generic point of $X$ is the base change of the generic fibre of $\psi$, which is the spectrum of the separable field extension $k(Y')$ of $k(Y)$, to $k(X)$. So it is the spectrum of a finite étale $k(X)$-algebra. As $X'$ is integral, of dimension $\dim X$, the points over the generic point of $X$ are generic points of irreducible components, so there is only one. So $k(X')$ is a finite separable extension of $k(X)$ of degree $[k(Y') : k(Y)]$, and $\varphi$ is a generically étale alteration. The properties (vi)(a) to (c) are stable under base change, and so is the finiteness in (vi)(d). The generic étaleness in (vi)(d) holds because $k(Y')/k(Y)$ is separable. The property (vi)(e) holds because $\varphi^{-1}(\operatorname{sm}(X/Y)) \subseteq \operatorname{sm}(X'/Y')$. The properties (i), (iii) and (iv) are clear. $\square$

The property (v) can be lost, because $Y'$ need not be normal. From now on we do not need it.

### Sections

**Step 5. Sections.** We may assume, in addition to (i), (iii), (iv) and (vi)(a) to (e):

(vi)(f) there are sections $\sigma_1, \dots, \sigma_n \colon Y \to X$ of $f$ such that $Z = \bigcup_i \sigma_i(Y)$.

*Proof.* Let $Z_1, \dots, Z_m$ be the irreducible components of $Z$. Each of them is finite over $Y$ by (vi)(d), and of dimension $d - 1 = \dim Y$ by (iv), so it dominates $Y$, and $k(Z_i)/k(Y)$ is a finite separable extension by (vi)(d). Choose a finite Galois extension $L$ of $k(Y)$ that contains a copy of each $k(Z_i)$ over $k(Y)$, and let $\psi \colon Y' \to Y$ be the normalization of $Y$ in $L$. It is a finite generically étale alteration, and $Y'$ is normal. Apply Lemma 2.3.5. Each irreducible component of $Z'$ has dimension $d - 1$ by (iv), and it is finite over $Y'$, so it dominates $Y'$. The generic fibre of $Z' \to Y'$ is the reduced scheme of the union of the $\operatorname{Spec}(k(Z_i) \otimes_{k(Y)} L)$. Since $L/k(Y)$ is Galois and contains a copy of $k(Z_i)$, the ring $k(Z_i) \otimes_{k(Y)} L$ is a product of $[k(Z_i) : k(Y)]$ copies of $L$. So each component $Z_j'$ of $Z'$ has function field $L = k(Y')$, and $Z_j' \to Y'$ is finite and birational. A finite birational morphism from an integral scheme to a normal integral scheme is an isomorphism, because a normal domain $A$ contains each ring $B$ with $A \subseteq B \subseteq \operatorname{Frac}(A)$ that is finite over $A$. So $Z_j' \to Y'$ is an isomorphism, and its inverse is a section $\sigma_j$ of $f'$. $\square$

The number of sections is at least 3 by (vi)(e), and (vi)(f) is kept by Lemma 2.3.5, with the pullbacks of the sections. This is [dJ96, 4.16].

### The stable model over the base

**Step 6. The stable curve.** We may assume, in addition to (i), (iii), (iv) and (vi)(a) to (f):

(vi)(g) there are a stable $n$-pointed curve $(\mathcal{C}, \tau_1, \dots, \tau_n)$ over $Y$, a nonempty open subscheme $U \subseteq Y$, and an isomorphism $\beta \colon \mathcal{C}|_U \to X|_U$ that maps $\tau_i$ to $\sigma_i$ for each $i$.

*Proof, assuming Hypothesis 2.2.5.* Let $U \subseteq Y$ be the set of points $y$ such that $f$ is smooth at each point of $X_y$ and the points $\sigma_i(y)$ are distinct. It is open, because the smooth locus of $f$ is open in $X$ and $f$ is closed, and because the locus where two sections agree is closed, as $X$ is separated over $Y$. It contains the generic point $\eta$ of $Y$. Indeed, $f$ is flat at each point of $X_\eta$ because $\mathcal{O}_{Y,\eta}$ is a field, the fibre $X_\eta$ is smooth by (vi)(c), and the sections are distinct. So $X|_U \to U$ is smooth and proper, with geometrically connected fibres by (vi)(a). Its fibres have a constant genus $g$, because the Euler characteristic of $\mathcal{O}$ is locally constant in a flat proper family. So $(X|_U, \sigma_1, \dots, \sigma_n)$ is a smooth proper $n$-pointed curve of genus $g$ over $U$, with $n \ge 3$. Hypothesis 2.2.5 gives a projective generically étale alteration $\psi \colon Y' \to Y$, a nonempty open $U' \subseteq \psi^{-1}(U)$, and a stable $n$-pointed curve over $Y'$ that is isomorphic to the pullback of $X|_U$ over $U'$. Apply Lemma 2.3.5 to $\psi$. Over $U'$ the strict transform $X'$ is $X \times_Y U'$, because $X|_U$ is flat over $U$ with geometrically reduced fibres, so $Y' \times_Y X$ is already reduced over $U'$. So (vi)(g) holds for $X' \to Y'$. $\square$

This is [dJ96, 4.17]. Property (vi)(g) is kept by Lemma 2.3.5, with the pullback of $\mathcal{C}$. It is the last property that we need from the moduli. Section 2.4 extends $\beta$ to a morphism and finishes the proof.
