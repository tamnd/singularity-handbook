---
title: Principalization in dimension four and relative strong factorization
nodes: [SG000000BV, SG000000C8, SG000000C9, SG000000CA, SG000000CB, SG000000CC, SG000000CD, SG000000CE, SG000000CF, SG000000CG, SG000000CH, SG000000CJ, SG000000CK, SG000000CM, SG000000CN]
sources: [CP19, Cut09, CJS20, AT19, AKMW02, Kar03, DSK11, Gow05, Bla12, Zar44, KK05, Ful93, Har, EGA4]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Principalization in dimension four and relative strong factorization

This section reports the twenty-fifth research result, from the track FP (tamnd/singularity#320), the patching of models. It continues Section 3.24 and answers two of its questions. The first question is which form of principalization in dimension 4 the proof of Theorem 3.24.13 needs, and what is known about it. The answer is that a weak form is sufficient for all steps except one, that the weak form reduces to ideals whose cosupport lies in a divisor with simple normal crossings, and that the weak form already contains resolution of the 4-folds that have a projective birational morphism to a regular 4-fold. The second question is the local input of patching along curves, Conjecture 3.24.25. The answer is a relative form of strong factorization, $\mathrm{RSF}_3$. It holds for the toric ring $S_0$ of Section 3.24, and with it the toric counterexample of Theorem 3.24.20 is repaired near its bad curve when Step 3 is read in the weak form of Lemma 3.25.3(2). The section also proves that 36 more toric rings are not reachable with regular centers, by a "dead chart" argument.

We keep the conventions of Section 3.24. The field $k$ is algebraically closed of characteristic $p > 0$, and the triple $(V_0, V_1, N)$, the models $V_2$, $V_3$ and the sets $L$ and $\Phi$ are as in the proof of Theorem 3.24.13. For toric varieties we use [Ful93] and the book of Cox, Little and Schenck. A smooth star subdivision of a regular fan at a 2-dimensional cone $\langle u, u' \rangle$, with the new ray $u + u'$, is the blowup of the regular torus-invariant curve $D_u \cap D_{u'}$, where $D_u$ is the divisor of the ray $u$ (Cox, Little and Schenck, Proposition 3.3.15).

### Motivation and history

Principalization of ideals on regular varieties is the form of resolution that the patching proofs use. Hironaka proved it in characteristic 0. In characteristic $p$, Cutkosky proved it on regular 3-folds over an algebraically closed field [Cut09, Theorem 1.3], and Cossart and Piltant proved it on regular excellent schemes of dimension 3 [CP19, Proposition 4.4] (Proposition 4.4 in version 2 of arXiv 1412.0868, and Proposition 4.3 in version 1). The introduction of [CP19] says that dimension 4 is open, and Abramovich and Temkin say the same in [AT19, Remark 2.2.3(ii)]. Section 3.24 needs principalization on regular 4-folds three times, in Steps 2, 3 and 5 of the proof of Theorem 3.24.13, and once more in Lemma 3.24.11. The first part of this section separates these uses.

Strong factorization asks for a common blowup of two models that is reached from each of them by blowups along regular centers. Oda conjectured it for toric varieties, and it is open even for toric 3-folds. Abramovich, Karu, Matsuki and Wlodarczyk proved weak factorization in characteristic 0 [AKMW02], and their Section 0.5 discusses strong factorization. Karu proved local strong factorization, along one valuation, for toric data in each characteristic and in general in characteristic 0 [Kar03]. Research note 83 named local strong factorization as the local input of Conjecture 3.24.25. The second part of this section shows that this is not sufficient, and it gives the correct relative form.

### The weak and the strong form

**Lemma 3.25.1.** Let $U$ be a regular variety of dimension 4 and $I \subseteq \mathcal{O}_U$ a nonzero coherent ideal. Then $I = \mathcal{O}_U(-D) \cdot I'$ with $D$ an effective divisor and $V(I')$ of codimension at least 2. The ideal $I$ is invertible at a point $x$ if and only if $I'_x = \mathcal{O}_{U,x}$. So the non-invertible locus of $I$ is $V(I')$, and it has dimension at most 2. A composite of blowups makes $I$ invertible if and only if it makes $I'$ invertible.

Node: SG000000CC · Lean: none yet

*Proof.* The local rings of $U$ are factorial. Locally take for $D$ the divisor of the greatest common divisor of a set of generators of $I$. Then the generators of $I' = I \cdot \mathcal{O}_U(D)$ have no common factor, so $V(I')$ contains no divisor. If $I'_x = (g)$ is principal, then the divisor of $g$ is in $V(I')$, which has codimension at least 2, so $g$ is a unit. The converse is clear. The last statement holds because the pullback of $\mathcal{O}_U(-D)$ is invertible. $\square$

So the condition $\dim V(I) \le 2$ that some texts put on principalization in dimension 4 is not a restriction.

**Definition 3.25.2 (weak and strong principalization).** $\mathrm{Princ}_4^{\rm w}$ is the statement: for each regular quasi-projective 4-fold $U$ over $k$ and each nonzero coherent ideal $I = \mathcal{O}_U(-D) I'$ as in Lemma 3.25.1 there is a projective birational morphism $\sigma \colon W \to U$ with $W$ regular, $\sigma$ an isomorphism over $U \setminus V(I')$, and $I \mathcal{O}_W$ invertible. The strong form $\mathrm{Princ}_4$ is Conjecture 3.24.7: in addition $\sigma$ is a composite of blowups along regular centers that lie over the non-invertible locus.

The strong form implies the weak form. The next lemma says where the proof of Theorem 3.24.13 needs which form.

**Lemma 3.25.3.** In the proof of Theorem 3.24.13, and in its variant Proposition 3.24.21:

1. Step 2 uses only $\mathrm{Princ}_4^{\rm w}$ for $I|_{U_0}$. It needs that $W_0$ is regular and that $I \mathcal{O}_{W_0}$ is invertible.
2. Step 3 uses only a regular $W_1$, projective and birational over $U_1$, that dominates $Z = \alpha^{-1}(U_1)$. $\mathrm{Princ}_4^{\rm w}$ for $K|_{U_1}$ gives it.
3. Step 5 uses $\mathrm{Princ}_4^{\rm w}$ for $J_2$ on $\tilde U_2$, with its condition that $W_2 \to \tilde U_2$ is an isomorphism over $\tilde U_2 \setminus V(J_2)$.
4. The strong form is used only in Lemma 3.24.11, the case $d = 2$ of Claim A. In Proposition 3.24.21 it is used only if one proves (A$^{\rm w}$) for the components with $d = 2$ by the argument of Lemma 3.24.11.

Node: SG000000CC · Lean: none yet

*Proof.* Read the proofs. In Step 2 the centers of $W_0 \to U_0$ do not occur later. In Step 3 the morphism $\tau \colon W_1 \to Z$ exists because $K \mathcal{O}_{W_1}$ is invertible and $W_1$ is normal, by the universal property of the normalized blowup, and only $\tau$ is used later, in the case $p_1 \in U_1$ of Step 6. In Step 5 the argument needs that $W_2 \to \tilde U_2$ is an isomorphism over $\tilde U_2 \setminus G$, and $V(J_2) \subseteq G$ by Lemma 3.24.8. The proof of Lemma 3.24.11 follows the centers of the principalization one at a time, so it needs the strong form. $\square$

### What is known

The following list states each known case of $\mathrm{Princ}_4$ with its source. We checked the statements against the sources, except where the list says otherwise.

**Theorem 3.25.4 (known cases of principalization in dimension 4).** Let $U$ be a regular 4-fold over $k$ and $I$ a nonzero coherent ideal.

1. If $I'$ of Lemma 3.25.1 is $\mathcal{O}_U$, there is nothing to do.
2. In characteristic 0, $\mathrm{Princ}_4$ holds by the theorem of Hironaka and by the functorial algorithms.
3. If $I$ is generated by monomials in a regular system of parameters, or in local equations of a divisor with simple normal crossings, then a toric resolution of the normal fan gives $\mathrm{Princ}_4^{\rm w}$ (Cox, Little and Schenck, Theorem 11.1.9). Goward gives a principalization of monomial ideals in each characteristic [Gow05].
4. For binomial ideals, Blanco gives a log resolution in each characteristic by a combinatorial algorithm [Bla12].
5. Let $\eta \in V(I')$ be a point that is not closed. Then there is an open neighborhood $U_\eta$ of $\eta$ and a principalization of $I|_{U_\eta}$ by blowups along regular centers.

In ambient dimension at most 3 the strong form holds in each characteristic [Cut09, Theorem 1.3], [CP19, Proposition 4.4 of version 2]. For a reduced excellent scheme $X$ of dimension at most 2 in a regular excellent scheme $Z$ there are blowups along regular centers over $X$ after which the reduced preimage of $X$ is a divisor with simple normal crossings, and which are isomorphisms over $Z \setminus X$ [CJS20, Corollary 0.4]. This is embedded resolution of $X$, not principalization of an ideal.

Node: SG000000BV · Lean: none yet

*Proof.* Parts 1 to 4 are the cited results. For part 5, the local ring $\mathcal{O}_{U,\eta}$ is regular and excellent of dimension at most 3, so [CP19, Proposition 4.4] principalizes $I \mathcal{O}_{U,\eta}$ by finitely many blowups along regular centers. The centers and the blowups are of finite type, so they spread out to an open neighborhood of $\eta$, and the centers stay regular on a smaller neighborhood. $\square$

For Goward we read only the main statement, and we did not check whether his centers lie in the non-invertible locus. For Blanco we read only the abstracts. The local principalizations of part 5 for different points $\eta$ are not compatible, and no argument is known that glues them. At the closed points of $V(I')$ both $\mathrm{Princ}_4$ and $\mathrm{Princ}_4^{\rm w}$ are open in characteristic $p$. The programs of Benito and Villamayor and of Kawanoue and Matsuki give results for ambient dimension 3, and the reductions of Temkin give nothing new in dimension 4.

**Proposition 3.25.5 (reduction to simple normal crossings).** Assume $\mathrm{Princ}_4^{\rm w}$ for all pairs $(U', I'')$ such that $V(I'')$ lies in a divisor of $U'$ with simple normal crossings. Then $\mathrm{Princ}_4^{\rm w}$ holds.

Node: SG000000CD · Lean: none yet

*Proof.* Write $I = \mathcal{O}_U(-D) I'$ as in Lemma 3.25.1, and let $X = V(I')_{\rm red}$, of dimension at most 2. By the proof of [CJS20, Corollary 0.4] (Theorem 0.3 with $B = \emptyset$) there is a composite $\pi \colon U' \to U$ of blowups along regular centers over $X$ such that $E = \pi^{-1}(X)_{\rm red}$ is a divisor with simple normal crossings and $\pi$ is an isomorphism over $U \setminus X$. The variety $U'$ is regular and quasi-projective. Write $I \mathcal{O}_{U'} = \mathcal{O}_{U'}(-D') I''$ as in Lemma 3.25.1. Then $V(I'') \subseteq \pi^{-1}(V(I')) = E$ as sets. The hypothesis gives $W \to U'$, an isomorphism over $U' \setminus V(I'')$, with $W$ regular and $I'' \mathcal{O}_W$ invertible. Then $I \mathcal{O}_W$ is invertible, the composite $W \to U$ is projective and birational, and it is an isomorphism over $U \setminus X$. $\square$

The case of simple normal crossings still contains the hard part. For example, the ideal $(z^p + g(x,y,w),\ x^a y^b)$ has its cosupport in the divisor $xy = 0$, and its principalization contains the resolution of the hypersurface $z^p + g = 0$ near the locus $xy = 0$.

**Proposition 3.25.6 (the weak form contains resolution).** Assume $\mathrm{Princ}_4^{\rm w}$. Let $U$ be a regular quasi-projective 4-fold and $X \to U$ a projective birational morphism. Then there is a regular variety $W$ with a projective birational morphism $W \to X$. If $X \to U$ is an isomorphism over $U \setminus G$, with $G$ closed of codimension at least 2, then $W \to X$ is an isomorphism over $U \setminus G$.

Node: SG000000CE · Lean: none yet

*Proof.* By [Har, Theorem II.7.17], $X \cong \mathrm{Bl}_J U$ for a coherent ideal $J$, and by Lemma 3.24.8 we can take $V(J) \subseteq G$ in the second case. $\mathrm{Princ}_4^{\rm w}$ gives $W \to U$ with $W$ regular and $J \mathcal{O}_W$ invertible, and an isomorphism over $U \setminus V(J')$, where $J = \mathcal{O}_U(-D) J'$. By the universal property of the blowup, $W \to U$ factors through $\mathrm{Bl}_J U = X$. In the second case $V(J') \subseteq V(J) \subseteq G$. $\square$

So $\mathrm{Princ}_4^{\rm w}$ implies resolution of each projective 4-fold that has a projective birational morphism to a regular 4-fold, for example each projective rational 4-fold: take the closure of the graph of a birational map to $\mathbb{P}^4$. This is open in characteristic $p$. The argument is not circular for $\mathrm{Fund}_4$, because $V_0$ and $V_1$ need not have a regular birational model, and the proof of Theorem 3.24.13 uses $\mathrm{Princ}_4$ only over $\mathrm{Reg}\, V_0$, $\mathrm{Reg}\, V_1$ and $\tilde U_2$. But it shows that the principalization part of the route of Cutkosky is a resolution problem of the same depth as $\mathrm{Res}_4$ for these 4-folds.

### Freedom in the choice of $V_2$

**Lemma 3.25.7.** Let $(V_0, V_1, N)$ be as in Conjecture 3.24.3, and let $V_2$ be as in Step 2 of the proof of Theorem 3.24.13. Let $\psi \colon V_2' \to V_2$ be projective and birational, with $V_2'$ normal, such that each $v \in N$ whose center on $V_1$ is singular has a regular center on $V_2'$. Run Steps 3 to 6 with $V_2'$ and $\alpha' = \alpha \circ \psi$ in place of $V_2$ and $\alpha$. If (A$^{\rm w}$) of Proposition 3.24.21 holds for $V_2'$, for some choice of $W_1$, then the conclusion of $\mathrm{Fund}_4$ holds for $(V_0, V_1, N)$.

Node: SG000000CF · Lean: none yet

*Proof.* Step 3 needs that $V_2'$ is normal and projective and birational over $V_1$. Then $V_2'$ is the normalized blowup of a coherent ideal $K'$ on $V_1$ [Har, Theorem II.7.17]. Step 4 needs that $L' \subseteq \mathrm{Reg}\, V_2'$, where $L'$ is the set of the centers on $V_2'$ of the valuations in $N$ with singular center on $V_1$. This is the hypothesis on $\psi$. Steps 5 and 6, in the form of Proposition 3.24.21, use only these two facts and that the final model dominates $V_0$. This holds because $V_5 \to V_4 \to V_2' \to V_2 \to V_0$. $\square$

In the toric case the hypothesis is easy to check. If $V_2$ is toric and $V_2'$ is obtained by star subdivisions at regular cones, then the preimage of each regular chart $U_\delta$ is the toric variety of a subdivision of $\delta$ by stars at regular faces, so it is regular. The centers of the valuations in $L$ lie in such charts, so the hypothesis of Lemma 3.25.7 holds.

So there are two ways to remove a component $\Gamma$ of $\Phi$ through $L$ that maps onto a curve of $V_1$ through $\mathrm{Sing}\, V_1$. The first way modifies both sides along $\Gamma$: $V_2' \to V_2$ by Lemma 3.25.7, and $W_1$ by a new choice in Step 3. This is Conjecture 3.24.25. The second way makes $V_2$ regular over $U_1$ near $\Gamma$. If $\alpha^{-1}(U_1)$ is regular, then (A$^{\rm w}$) holds with $\tilde U_2 = U_2$: for a $W_1$ that keeps the regular locus, $\Phi \cap \alpha^{-1}(U_1)$ is empty, so there is nothing to remove. Proposition 3.26.5 proves this in the toric case. But outside the toric case this needs resolution of 4-folds over $U_1$, which is the problem itself.

### Relative strong factorization

Let $\Gamma \subseteq \Phi$ be as in Conjecture 3.24.25, with generic point $\eta_2$, let $\eta_1 = \alpha(\eta_2) \in U_1$, and let $R = \mathcal{O}_{V_1,\eta_1}$ and $S = \mathcal{O}_{V_2,\eta_2}$. Both are regular local rings of dimension 3, essentially of finite type over the field $\kappa(\Gamma)$, which has transcendence degree 1 over $k$.

**Definition 3.25.8 (relative strong factorization).** Let $R \subseteq S$ be regular local rings of dimension 3 with the same fraction field, with $S$ dominating $R$ and essentially of finite type over $R$. The pair $(R, S)$ has *relative strong factorization*, written $\mathrm{RSF}(R, S)$, if there are

1. a composite $Y \to \operatorname{Spec} R$ of blowups along regular centers, and
2. a projective birational morphism $Z \to \operatorname{Spec} R$ and a point $\zeta \in Z$ with $\mathcal{O}_{Z,\zeta} = S$,

such that $Y \to Z$ is a morphism over a neighborhood of $\zeta$, and $Y \times_Z \operatorname{Spec} S \to \operatorname{Spec} S$ is a composite of blowups along regular centers. For an ideal $K$ of $R$ with $K S$ invertible, the *strong variant* asks in addition that the centers of $Y \to \operatorname{Spec} R$ lie over the non-invertible locus of $K$. $\mathrm{RSF}_3$ is the statement that $\mathrm{RSF}(R, S)$ holds for all such pairs.

Node: SG000000CG · Lean: none yet

**Lemma 3.25.9.** If $\mathrm{RSF}(R, S)$ holds, then $(R, S)$ has local strong factorization (Definition 3.24.14) along each valuation $\nu$ that dominates $S$.

Node: SG000000CG · Lean: none yet

*Proof.* Let $T$ be the local ring of the center of $\nu$ on $Y \times_Z \operatorname{Spec} S$. It is a localization of $Y$ at a point, so it is an iterated monoidal transform of $R$ by the first composite, and it is an iterated monoidal transform of $S$ by the second composite. It is regular, because each blowup along a regular center of a regular scheme is regular, and $\nu$ dominates it. $\square$

The converse is open. Local strong factorization along each valuation gives, by compactness of the Zariski-Riemann space, finitely many local solutions, but there is no reason for them to glue to one modification. Conjecture 3.24.25 needs one modification of a neighborhood of $\eta_2$ that serves all the valuations at the same time. So the local input of Conjecture 3.24.25 is $\mathrm{RSF}(R, S)$, and not local strong factorization.

### The toric case for $\sigma_0$

Let $N = \mathbb{Z}^3$ with the basis $e_1, e_2, e_3$ dual to $x, y, z$, let $F$ be a field, and let $R = F[x,y,z]_{(x,y,z)}$. Let $\sigma_0 = \langle g_1, g_2, g_3 \rangle$ with $g_1 = (0,1,3)$, $g_2 = (1,1,1)$, $g_3 = (2,1,0)$, and let $S_0 = F[a,b,c]_{(a,b,c)}$ be its ring, with $g_1 \leftrightarrow a$, $g_2 \leftrightarrow b$, $g_3 \leftrightarrow c$, so that $x = b c^2$, $y = a b c$, $z = a^3 b$ (Proposition 3.24.16). Let $K = (x^3 y^3 z^2,\ x^4 y z^3,\ y^9,\ x^5 z^3)$ be the ideal of the proof of Corollary 3.24.18. By Theorem 3.24.17, $S_0$ has no first center from the side of $R$. The next theorem shows that $S_0$ has a first center from its own side, and that the two sides meet.

**Theorem 3.25.10 (toric relative strong factorization for $\sigma_0$).** Over each field $F$, $\mathrm{RSF}(R, S_0)$ holds in its strong variant for $K$, with torus-invariant centers. In detail:

1. *The side of $R$.* Make 14 smooth star subdivisions at 2-dimensional cones, starting from the octant $\langle e_1, e_2, e_3 \rangle$, in the order of the following table. The result is a regular fan $F_1$ with 24 maximal cones.
2. *The common part.* The cone $\sigma_0$ is the union of 6 maximal cones of $F_1$, and each cone of $F_1$ that meets the interior of $\sigma_0$ is in $\sigma_0$. These 6 cones form the fan $\mathcal{G}$ with the maximal cones
$$\langle (0,1,3), (1,2,4), (2,3,6) \rangle,\ \langle (1,1,1), (2,1,0), (4,3,3) \rangle,\ \langle (1,1,1), (2,2,3), (2,3,5) \rangle,$$
$$\langle (1,1,1), (2,2,3), (4,3,3) \rangle,\ \langle (1,2,4), (2,2,3), (2,3,5) \rangle,\ \langle (1,2,4), (2,2,3), (2,3,6) \rangle.$$
3. *The side of $S_0$.* The fan $\mathcal{G}$ is obtained from $\sigma_0$ by 5 smooth star subdivisions at 2-dimensional cones: at $\langle g_1, g_3 \rangle$, with the new ray $(2,2,3)$; at $\langle g_1, g_2 \rangle$, with the new ray $(1,2,4)$; at $\langle g_3, (2,2,3) \rangle$, with the new ray $(4,3,3)$; at $\langle g_2, (1,2,4) \rangle$, with the new ray $(2,3,5)$; and at $\langle g_1, (2,2,3) \rangle$, with the new ray $(2,3,6)$. The first center is the curve $a = c = 0$ of $\operatorname{Spec} S_0$, and the second one is the strict transform of the curve $a = b = 0$.
4. *The strong variant.* No center of part 1 lies in $\sigma_0$. At each of the 14 centers the ideal $K$ is not principal, so each center lies in the non-invertible locus of $K$ on the current model. The ideal $K$ is principal on each maximal cone of $F_1$. So the 14 blowups principalize $K$ on $\mathbb{A}^3_F$ in the strong sense.

| step | center | new ray | step | center | new ray |
|---|---|---|---|---|---|
| 1 | $\langle e_3, e_2 \rangle$ | $(0,1,1)$ | 8 | $\langle (1,1,1), (1,1,2) \rangle$ | $(2,2,3)$ |
| 2 | $\langle e_3, (0,1,1) \rangle$ | $(0,1,2)$ | 9 | $\langle e_1, (1,1,1) \rangle$ | $(2,1,1)$ |
| 3 | $\langle (0,1,1), e_1 \rangle$ | $(1,1,1)$ | 10 | $\langle (0,1,2), (1,1,2) \rangle$ | $(1,2,4)$ |
| 4 | $\langle e_3, (0,1,2) \rangle$ | $(0,1,3)$ | 11 | $\langle (1,1,2), (1,2,4) \rangle$ | $(2,3,6)$ |
| 5 | $\langle e_2, e_1 \rangle$ | $(1,1,0)$ | 12 | $\langle (0,1,2), (2,2,3) \rangle$ | $(2,3,5)$ |
| 6 | $\langle e_1, (1,1,0) \rangle$ | $(2,1,0)$ | 13 | $\langle (1,1,1), (2,1,1) \rangle$ | $(3,2,2)$ |
| 7 | $\langle (0,1,2), e_1 \rangle$ | $(1,1,2)$ | 14 | $\langle (1,1,1), (3,2,2) \rangle$ | $(4,3,3)$ |

So $Y = X(F_1)$, the normalized blowup $Z = X(\Sigma_K)$ of $K$, and the fixed point $\zeta$ of the chart of $\sigma_0$ satisfy Definition 3.25.8.

Node: SG000000CH · Lean: none yet

*Proof.* Each statement is a finite computation with integer vectors, and we explain how to check it by hand.

(1) At each step the new ray is the sum of the two generators of the center, so the step is a smooth star subdivision, and each maximal cone that contains the center is replaced by two cones of the same determinant. So all cones stay regular. The first step creates 2 maximal cones, and each later step adds as many maximal cones as there are maximal cones that contain its center. The count at the end is 24. For example, the first blowup has the center $\langle e_3, e_2 \rangle$, which is the curve $y = z = 0$.

(2) The cone $\sigma_0$ is the set of $w$ with $\langle w, u_j \rangle \ge 0$ for the inward facet normals $u_1 = (1,-2,1)$, $u_2 = (-3,6,-2)$, $u_3 = (2,-3,1)$ (Proposition 3.24.16). Each ray of the six cones of $\mathcal{G}$ satisfies these three inequalities, so the six cones are in $\sigma_0$. Check in the list of the 24 maximal cones of $F_1$ that these six cones occur in it. By part (3) they are the maximal cones of a subdivision of $\sigma_0$, so their union is $\sigma_0$. Let $\kappa$ be another maximal cone of $F_1$ that meets the interior of $\sigma_0$. Then $\kappa$ meets the interior of one of the six cones, because they cover $\sigma_0$ and the union of their boundaries has no interior points. This is impossible, because two cones of a fan meet in a common face.

(3) Run the 5 stars from $\sigma_0$. Each new ray is the sum of the generators of its center: $(0,1,3) + (2,1,0) = (2,2,3)$, $(0,1,3) + (1,1,1) = (1,2,4)$, $(2,1,0) + (2,2,3) = (4,3,3)$, $(1,1,1) + (1,2,4) = (2,3,5)$, $(0,1,3) + (2,2,3) = (2,3,6)$. The result is $\mathcal{G}$. The ray $g_j$ corresponds to the divisor of the coordinate $a$, $b$ or $c$ of $S_0$, so $\langle g_1, g_3 \rangle$ is the curve $a = c = 0$ and $\langle g_1, g_2 \rangle$ is the curve $a = b = 0$.

(4) For a cone $\kappa$ of the octant, the monomial ideal $K$ is principal on $U_\kappa$ if and only if one exponent of $K$ attains the minimum of $\langle v, \cdot \rangle$ over the four exponents of $K$ for each ray $v$ of $\kappa$. Check this for each of the 24 maximal cones of $F_1$, and check that it fails for each of the 14 centers. The non-invertible locus of $K$ on the current model is closed and torus invariant. If it meets the chart of a 2-dimensional cone, it contains the closed orbit of the chart, which is the center. For $\sigma_0$ itself $K$ is principal, because $\sigma_0$ is the normal cone of the vertex $u_0 = (3,3,2)$ (Corollary 3.24.18).

Finally $F_1$ refines the normal fan $\Sigma_K$ by part (4), so $Y \to Z$ is a morphism, and $Y \times_Z \operatorname{Spec} S_0$ is the localization of $X(\mathcal{G})$, which is reached from $\operatorname{Spec} S_0$ by the 5 blowups of part (3). $\square$

The search for $\mathcal{G}$ is not easy. A breadth first search for a common model, up to 5 steps on each side, finds none. Research note 85 found the certificate by a heuristic that cuts the 2-dimensional cones that cross a facet hyperplane of $\sigma_0$, with the inward normals $u_1$, $u_2$, $u_3$. The scripts of note 85 check each step with exact integer arithmetic.

Now we return to Construction 3.24.19. There $V_2 = V_0 = X(\Sigma_0)$, and the face $\{0\} \times \sigma_0$ of $\Sigma_0$ is a common face of $D = \langle \sigma_0, r \rangle$, of determinant 1, and $D' = \langle \sigma_0, r' \rangle$, of determinant $-2$. Let $\tau_1 = \langle e_x, e_y, e_z \rangle$ be the face of $C$ and $C'$ of Construction 3.24.19.

**Proposition 3.25.11 (the toric counterexample repaired near the bad curve, with the weak Step 3).** Let $(V_0, V_1)$ be the pair of Construction 3.24.19, with $V_2 = V_0$ and $\Gamma = V(\{0\} \times \sigma_0)$. Let $\Sigma_0'$ be obtained from $\Sigma_0$ by the 5 stars of Theorem 3.25.10(3), lifted to $\{0\} \times \mathbb{Z}^3 \subseteq \mathbb{Z}^4$, and let $V_2' = X(\Sigma_0')$, with $\psi \colon V_2' \to V_2$. Let $F_1^{(4)}$ be the fan $\Sigma_1$ with the 14 stars of Theorem 3.25.10(1), lifted to the face $\tau_1$. Let $W_1'$ be a toric resolution, by star subdivisions that keep the regular cones, of the common refinement of $F_1^{(4)}$ and $\Sigma_0'$, restricted over $U_1 = \mathrm{Reg}\, V_1$. Let $\Phi'$ be the fundamental locus of $V_2' \dashrightarrow V_3'$, and $L'$ as in Lemma 3.25.7. Then:

1. $V_2' \to V_2$ satisfies the hypothesis of Lemma 3.25.7, and $W_1'$ is a valid choice in Step 3 in the weak form of Lemma 3.25.3(2).
2. The cones $\{0\} \times \kappa$, for $\kappa \in \mathcal{G}$, and all their faces, are cones of the fan of $W_1'$. In particular the six strict transforms $V(\{0\} \times \kappa)$ of $\Gamma$, for $\kappa$ maximal in $\mathcal{G}$, are not in $\Phi'$.
3. Each irreducible component of $\Phi'$ that meets $\psi^{-1}(\Gamma)$ is an orbit closure $V(\varphi)$ with $r \in \varphi$, and then it lies over $p_1$, or with $r' \in \varphi$, and then it lies over the regular point $p_1'$ and does not meet $L'$.
4. With $\tilde U_2'$ chosen as in Step 5, no point of $\overline{\Phi' \cap \tilde U_2'} \cap \alpha'^{-1}(U_1)$ lies in $\psi^{-1}(\Gamma)$. So the failure of (A$^{\rm w}$) in Theorem 3.24.20(2), which happens at the point $z \in \Gamma$, does not occur for $V_2'$.

Node: SG000000CJ · Lean: none yet

*Proof.* (1) The 2-dimensional cones of the stars lie in $\sigma_0$, which is a regular face, so the toric remark after Lemma 3.25.7 applies. The fan of $W_1'$ is regular, it is projective over $U_1$ because star subdivisions keep projectivity, and it refines the fan of $\alpha'^{-1}(U_1)$, so it dominates $\alpha'^{-1}(U_1)$. By Lemma 3.25.3(2) this is all that Step 3 needs.

(2) The cone $\{0\} \times \kappa$ is a cone of $F_1^{(4)}$ by Theorem 3.25.10(2), and a cone of $\Sigma_0'$ by Theorem 3.25.10(3). So it is a cone of the common refinement, and the resolution keeps it because it is regular. It lies in $\tau_1$, so its orbit lies over $U_1$. For a toric birational morphism $X(\Sigma_W) \to X(\Sigma')$ with $\Sigma_W$ a refinement of $\Sigma'$, the inverse map is defined near the generic point of the orbit $O(\varphi)$ if and only if $\varphi \in \Sigma_W$. Over $U_1$ we have $\beta^{-1}(U_1) \cong W_1'$ and $\gamma = \tau$, so this applies.

(3) The set $\psi^{-1}(\Gamma)$ is the union of the orbits $O(\varphi)$ for the cones $\varphi \in \Sigma_0'$ whose relative interior lies in the relative interior of $\sigma_0$, $D$ or $D'$. An orbit closure $V(\varphi)$ meets $O(\varphi')$ only if $\varphi \subseteq \varphi'$. So a component $V(\varphi)$ of $\Phi'$ that meets $\psi^{-1}(\Gamma)$ has $\varphi \subseteq D$ or $\varphi \subseteq D'$, and $\varphi$ is a cone of the subdivision of $D$ or $D'$. These cones are the faces of the cones of $\mathcal{G}$, the cones $\langle \kappa_0, r \rangle$ and $\langle \kappa_0, r' \rangle$ with $\kappa_0$ a face of a cone of $\mathcal{G}$, and the rays $r$ and $r'$. By (2), $\varphi$ is not a face of a cone of $\mathcal{G}$. So $r \in \varphi$ or $r' \in \varphi$. The ray $r$ lies in the interior of $C$, so $V(\varphi) \subseteq \alpha'^{-1}(p_1)$ when $r \in \varphi$. In the same way, $V(\varphi) \subseteq \alpha'^{-1}(p_1')$ when $r' \in \varphi$. The center of a valuation in $L'$ lies over a singular point of $V_1$, that is, over $p_1$, so it is not in $\alpha'^{-1}(p_1')$.

(4) By (3), the components that meet $\psi^{-1}(\Gamma)$ and stay in $\tilde U_2'$, which are the ones that meet $L'$, lie over $p_1$. So their closures do not meet $\alpha'^{-1}(U_1)$. A component that does not meet $\psi^{-1}(\Gamma)$ is closed, so its closure does not meet $\psi^{-1}(\Gamma)$ either. $\square$

Proposition 3.25.11 does not prove (A$^{\rm w}$) on all of $V_2'$. The stars at faces of $\sigma_0$ also subdivide other cones of $\Sigma_0$ that contain these faces, and they can create new components of $\Phi'$ there. These cones have not been checked. $\mathrm{Fund}_4$ for this pair holds anyway, by Theorem 3.24.20(3). The repair comes from the weak choice of $W_1$ in Step 3, which Lemma 3.25.3(2) allows, and not from Lemma 3.25.7 alone: Proposition 3.26.5 shows that in this weak model (A$^{\rm w}$) holds for every toric pair, also for $V_2 = V_0$. If $W_1$ must be a composite of blowups along regular centers, the question whether Construction 3.24.19 blocks the method of Theorem 3.24.13 is open. Section 3.26 reduces it to a problem on the octant.

The same method works for other cones. A *certificate* for a regular cone $\sigma$ in the octant is a fan, obtained from the octant by smooth stars at 2-dimensional cones, in which $\sigma$ is a union of cones, together with a sequence of smooth stars at 2-dimensional cones that produces this subfan from $\sigma$. A certificate gives $\mathrm{RSF}(R, S_\sigma)$ with torus-invariant centers, by the argument at the end of the proof of Theorem 3.25.10.

**Theorem 3.25.12 (a computation of toric relative strong factorization).** Let $F$ be a field. Each regular cone in the octant whose primitive generators have entries at most 2 has a certificate. There are 61 classes of such cones up to permutation of the coordinates. Of the 429 classes of regular cones with entries at most 3, 418 have a certificate. So $\mathrm{RSF}(R, S_\sigma)$ holds for these cones $\sigma$.

Node: SG000000CK · Lean: none yet

*Proof.* Research note 85 searches for a certificate for each class, and checks each certificate exactly: the fan is built by smooth stars only, so each cone is regular, and a search by inverse smooth stars reduces the subfan exactly to $\{\sigma\}$. For entries at most 3 the first run found 394 certificates. In 202 of them $\sigma$ itself is a cone of the fan, so $\sigma$ is reachable by toric blowups and its side is trivial. Two more runs with larger budgets on the 35 other classes found 24 more certificates. $\square$

The 11 classes without a certificate are $\langle (0,1,2), (0,1,3), (1,3,0) \rangle$, $\langle (0,1,2), (0,2,3), (1,3,0) \rangle$, $\langle (0,1,2), (1,2,3), (3,2,0) \rangle$, $\langle (0,1,2), (2,2,3), (3,1,0) \rangle$, $\langle (0,1,2), (2,3,3), (3,2,0) \rangle$, $\langle (0,1,3), (1,2,3), (2,2,1) \rangle$, $\langle (0,1,3), (2,2,1), (3,3,1) \rangle$, $\langle (0,1,3), (2,2,1), (3,3,2) \rangle$, $\langle (0,1,3), (2,2,3), (3,2,1) \rangle$, $\langle (0,2,3), (1,3,2), (2,3,0) \rangle$ and $\langle (0,2,3), (2,3,3), (3,2,1) \rangle$. The search is a randomized heuristic with a budget, so they are not counterexamples. They are the first test cases for toric $\mathrm{RSF}_3$. Section 3.26 gives a certificate for each of the 11 classes (Theorem 3.26.19(2)), and 5 of them are directly reachable.

**Proposition 3.25.13 (Oda's conjecture implies toric $\mathrm{RSF}_3$).** Assume the strong factorization conjecture of Oda in dimension 3 for regular fans whose support is a convex cone: two such fans with the same support have a common refinement that is reached from each of them by smooth star subdivisions. Then for each regular cone $\sigma$ in a regular 3-dimensional cone $\tau$ there is a fan $F$, obtained from $\tau$ by smooth star subdivisions, such that the cones of $F$ in $\sigma$ form a fan that is obtained from $\sigma$ by smooth star subdivisions. In particular $\mathrm{RSF}(R, S_\sigma)$ holds for each regular cone $\sigma$ in the octant.

Node: SG000000CM · Lean: none yet

*Proof.* Cut $\tau$ by the three facet hyperplanes of $\sigma$. This gives a polyhedral fan with support $\tau$, and $\sigma$ is one of its cones, because $\sigma$ is the intersection of its three facet half spaces and lies in $\tau$. Resolve this fan by star subdivisions that keep the regular cones (Cox, Little and Schenck, Theorem 11.1.9). This gives a regular fan $\Delta$ with $|\Delta| = \tau$ and $\sigma \in \Delta$. Apply the hypothesis to $\Delta$ and $\{\tau\}$, and get $F$, reached from $\tau$ and from $\Delta$ by smooth stars. Each cone of a star subdivision lies in a cone of the old fan, and a star at a cone $\kappa$ changes only the cones that contain $\kappa$. So along the sequence from $\Delta$ to $F$ the cones in $\sigma$ always form a subfan with support $\sigma$. A star at a cone $\kappa \subseteq \sigma$ acts on this subfan as the star at $\kappa$, and a star at a cone $\kappa \not\subseteq \sigma$ does not change it. $\square$

The strong conjecture of Oda is open in dimension 3 [AKMW02, Section 0.5], [AT19]. Da Silva and Karu prove special cases [DSK11]. So toric $\mathrm{RSF}_3$ is open in general. The relative form for one cone in the octant is weaker than the conjecture of Oda, and Theorem 3.25.12 suggests that a direct proof may be possible.

### Local strong factorization in characteristic $p$

In characteristic 0 Karu reduces local strong factorization to the toric case with the local monomialization theorem of Cutkosky [Kar03, Theorem 0.1]. In characteristic $p$ local monomialization of birational extensions of regular local rings of dimension 3 is not known. For one class of valuations the embedded resolution of surfaces of Cossart, Jannsen and Saito replaces it.

**Proposition 3.25.14 (rank 1 and rational rank 3).** Let $k$ be a field of any characteristic. Let $R \subseteq S$ be regular local rings of dimension 3, essentially of finite type over $k$, with the same fraction field $K$ and with $S$ dominating $R$. Let $\nu$ be a valuation of $K$ that dominates $S$, with value group of rank 1 and rational rank 3. Then there is a regular local ring $T$, dominated by $\nu$, that is an iterated monoidal transform along $\nu$ of $R$ and also of $S$.

Node: SG000000CN · Lean: none yet

*Proof.* A monoidal transform along $\nu$ is the local ring, at the center of $\nu$, of the blowup of a regular center. Embed the value group in $\mathbb{R}$.

Step 1 (monomial coordinates). Let $A$ be $R$ or $S$. The value group is generated by values of elements of $A$, so there are $f_1, f_2, f_3 \in A$ with rationally independent values $\nu(f_1), \nu(f_2), \nu(f_3)$. Apply the proof of [CJS20, Corollary 0.4] (Theorem 0.3 with $B = \emptyset$) to the reduced surface $V(f_1 f_2 f_3)_{\rm red}$ in the regular excellent scheme $\operatorname{Spec} A$ of dimension 3. It gives blowups along regular centers after which the total transform has simple normal crossings. Let $A'$ be the local ring at the center of $\nu$. Then $f_i = u_i z^{\alpha_i}$ with units $u_i$, where $z = (z_1, \dots, z_m)$ are local equations of the components through the center, part of a regular system of parameters with $m \le \dim A'$, and $\alpha_i \in \mathbb{N}^m$. The values $\nu(f_i) = \sum_j \alpha_{ij} \nu(z_j)$ are rationally independent, so $m = 3 = \dim A'$, and $w = (\nu(z_1), \nu(z_2), \nu(z_3))$ has rationally independent coordinates. In particular the center is the closed point, and $z$ is a regular system of parameters.

Step 2 ($\nu$ is monomial in $z$). Let $g \in A'$ be nonzero, and choose $n$ with $n \min_j w_j > \nu(g)$. Since $\mathfrak{m}^d / \mathfrak{m}^{d+1}$ is free over the residue field on the monomials of degree $d$, there are $c_e \in A'$, each $0$ or a unit, with $g \equiv \sum_{|e| < n} c_e z^e$ modulo $\mathfrak{m}^n$. Elements of $\mathfrak{m}^n$ have value at least $n \min_j w_j > \nu(g)$, so $\nu(g) = \nu(\sum c_e z^e)$. Distinct monomials have distinct values $\langle e, w \rangle$, so $\nu(\sum c_e z^e) = \min \{ \langle e, w \rangle : c_e \ne 0 \}$. So $\nu$ is the monomial valuation of weight $w$ on $A'$, and the value group is $\bigoplus_j \mathbb{Z} w_j$.

Step 3 (Perron transforms). A toric monoidal transform of $A'$ along $\nu$ is the blowup of $V(z_i, z_j)$ or of $V(z_1, z_2, z_3)$, localized at the center of $\nu$. In terms of fans it is a smooth star of the cone dual to $z$ at a face, taken along $w$. Given finitely many nonzero $c \in \mathbb{Z}^3$ with $\langle c, w \rangle > 0$, a finite sequence of such transforms along $w$ reaches coordinates $z'$ with $z = z'^M$, where $M$ is unimodular with nonnegative entries and $M^{\rm T} c \in \mathbb{N}^3$ for all these $c$. This is the convergence of the algorithm of Perron for a vector with rationally independent coordinates [Zar44], and [Kar03, Section 1] for the toric form. So each $g \in A'$ becomes a unit times a monomial after finitely many such transforms: let $z^{e_0}$ be the monomial of least value in the expansion of Step 2, and apply the transforms for the finitely many vectors $c = e - e_0$ with $c_e \ne 0$ and $c = e - e_0$ with $|e| = n$. Then $g = z'^{M e_0} (c_{e_0} + h)$ with $h \in \mathfrak{m}'$.

Step 4 (the side of $R$ dominates the side of $S$). Apply Steps 1 and 2 to $S$. This gives an iterated monoidal transform $S'$ of $S$ along $\nu$ with a regular system of parameters $y$ in which $\nu$ is monomial with independent values. Apply Steps 1 and 2 to $R$, and get $R'$ with parameters $z$. The ring $S'$ is a localization of $R[s_1, \dots, s_m]$ for some $s_i \in K$, at the prime $\mathfrak{p} = \{ \nu > 0 \} \cap R[s]$. Write $s_i = g_i / h_i$ and $y_j = g_j' / h_j'$ with $g_i, h_i, g_j', h_j' \in R'$, and apply Step 3 to make all of them units times monomials. Then $s_i = \varepsilon_i z^{c_i}$ with $c_i \in \mathbb{Z}^3$ and $\langle c_i, w \rangle = \nu(s_i) \ge 0$, with equality only if $c_i = 0$. One more application of Step 3 makes all $c_i \ge 0$, and the same for the $y_j$. Call the result $R''$. Then $R[s] \subseteq R''$ and $\mathfrak{m}_{R''} \cap R[s] = \mathfrak{p}$, so $R''$ dominates $S'$. Also $y_j = \varepsilon_j z^{A_j}$ with $A_j \in \mathbb{N}^3$. The value group is $\bigoplus \mathbb{Z} \nu(y_j) = \bigoplus \mathbb{Z} \nu(z_j)$ by Step 2 for both rings, so the matrix $A$ with rows $A_j$ is in $GL_3(\mathbb{Z})$.

Step 5 (toric strong factorization). In the lattice dual to the exponents of $z$, the cone of $R''$ is the octant $\sigma_z$, and the cone of $S'$ is $\sigma_y = \{ u : \langle A_j, u \rangle \ge 0 \}$. It is regular because $A$ is unimodular, and both cones contain $w$ in their interiors. Theorem 3.24.23 gives a regular cone $\rho \ni w$ that is reached from $\sigma_z$ and from $\sigma_y$ by smooth stars along $w$. These stars are toric monoidal transforms of $R''$ in $z$ and of $S'$ in $y$. They give $T_1$ with parameters $t$ and $T_2$ with parameters $t'$, both monomials attached to the rays of $\rho$. Since $y = \varepsilon z^A$, after a reordering $t'_j = \varepsilon'_j t_j$ with units $\varepsilon'_j$ of $R'' \subseteq T_1$. So $T_2 \subseteq T_1$, because the elements of $S'[t']$ of value 0 are units of $T_1$. Also $\mathfrak{m}_{T_2} T_1 = (t') T_1 = (t) T_1 = \mathfrak{m}_{T_1}$, and $T_1$ is a localization of a finitely generated $T_2$-algebra with the same fraction field. The residue field extension is algebraic, because $\nu$ is an Abhyankar valuation with rational rank $3 = \dim T_2$, so it is finite. So $T_2 \to T_1$ is quasi-finite at the closed point, and $T_2$ is normal. Zariski's Main Theorem [EGA4, Theorem 8.12.10] gives $T_1 = T_2$. Put $T = T_1$. $\square$

The proposition does not cover the other valuations. For rational rank 3 and rank 2 or 3, Theorem 3.24.23 is stated only for vectors with rationally independent real coordinates, that is, for rank 1. Abhyankar valuations with residue transcendence degree at least 1 have local uniformization in each characteristic [KK05], but no proof of local strong factorization for them in characteristic $p$ is known. The global factorization theorems in positive characteristic give factorization in dimension $d$ from resolution in dimension $d + 1$ [AT19], [AKMW02], which is circular here for $d = 3$, and they give weak factorization, not strong factorization.

### Dead charts

This part goes back to Conjecture 3.24.24, regular reachability of toric rings. It settles 6 of the 22 classes of cones that Section 3.24 leaves open. Let $F$ be a field. For a regular cone $\sigma = \langle g_1, g_2, g_3 \rangle \subseteq \mathbb{R}^3_{\ge 0}$, let $G = (g_{j,i})$ be the matrix with rows $g_j$.

**Definition 3.25.15 (toric pair).** A *toric pair of type $\sigma$* is a tuple $(R, x; S, a)$ such that $R \subseteq S$ are regular local rings of dimension 3 that contain $F$, with residue field $F$ and the same fraction field, $S$ dominates $R$, $x = (x_1, x_2, x_3)$ and $a = (a_1, a_2, a_3)$ are regular systems of parameters of $R$ and $S$ with $x_i = \prod_j a_j^{g_{j,i}}$, and the following condition holds:

(E) each height 1 prime $\mathfrak{q}$ of $S$ with $\operatorname{ht}(\mathfrak{q} \cap R) \ge 2$ contains $a_1 a_2 a_3$.

The model is $R = F[x]_{(x)}$ and $S = S_\sigma$. Then $\hat R = F[[x]]$, $\hat S = F[[a]]$, and $\hat R \to \hat S$ is the monomial map $x^f \mapsto a^{G f}$. A Laurent monomial $x^f$ lies in $S$ if and only if $f \in \sigma^\vee$. For $l \in \{1, 2, 3\}$ put $L_l = \{ i : x_i / x_l \in S \}$. Always $l \in L_l$. For $e \in \mathbb{Z}^3_{\ge 0}$ let $\Sigma_e = (e + \sigma^\vee) \cap \mathbb{Z}^3_{\ge 0}$. By faithful flatness of the completion, an element $s \in R$ lies in $x^e S$ if and only if the support of $s$ in $\hat R$ lies in $\Sigma_e$.

**Lemma 3.25.16 (shape of a first center).** Let $(R, x; S, a)$ be a toric pair and $P$ a prime of $R$ of height 2 with $R/P$ regular and $P S = u S$ principal, with $u \in P$. Then $u = x^e \varepsilon$ with $e \in \mathbb{Z}^3_{\ge 0}$ and $\varepsilon \in S^\times$. For each $l$ with $e_l \ge 1$ the support of each element of $P$ lies in $\Sigma_{e_l}$, where $e_l$ is the unit vector, and the linear parts of the elements of $P$ lie in $\bigoplus_{i \in L_l} F x_i$. In particular $|L_l| \ge 2$.

Node: SG000000C8 · Lean: none yet

*Proof.* Each height 1 prime $\mathfrak{q}$ of $S$ that contains $u$ contains $P S$, so $\mathfrak{q} \cap R \supseteq P$ has height at least 2, and $\mathfrak{q}$ is one of $(a_1)$, $(a_2)$, $(a_3)$ by (E). Since $S$ is factorial, $u = a^\alpha \varepsilon$, and $a^\alpha = x^e$ with $e = G^{-1} \alpha$. The initial monomials in $\hat S$ show that $x^e$ is a monomial of $u \in \hat R$, so $e \ge 0$. Then $P \subseteq u S \cap R = x^e S \cap R$, and $x^e S \subseteq x_l S$ when $e_l \ge 1$. The linear monomials with support in $\Sigma_{e_l}$ are the $x_i$ with $i \in L_l$. Since $P$ is regular of height 2, its linear parts span a plane. $\square$

When $L_l = \{l, i\}$, let $m$ be the third index. Let $k_0$ be the least $n$ with $x_m^n / x_l \in S$, and $k_1$ the least $n$ with $x_m^n / x_i \in S$, or $\infty$ if there is none.

**Lemma 3.25.17 (normal form of a first center).** In Lemma 3.25.16, let $L_l = \{l, i\}$. Then $P \hat R = (x_l - \psi(x_m),\ x_i - \varphi(x_m))$ with $\psi, \varphi \in F[[x_m]]$, each $0$ or of order at least $k_0$. Also $P \hat S = x_l \hat S$.

Node: SG000000CA · Lean: none yet

*Proof.* By Lemma 3.25.16 the linear parts of $P$ span $F x_l + F x_i$. So the cotangent space of the regular ring $\hat R / P \hat R$ of dimension 1 is spanned by the image of $x_m$, and $\hat R / P \hat R = F[[\bar x_m]]$. Hence $x_l \equiv \psi(x_m)$ and $x_i \equiv \varphi(x_m)$ modulo $P \hat R$ for series $\psi$, $\varphi$ without constant term. The ideal $(x_l - \psi, x_i - \varphi)$ is prime with quotient $F[[x_m]]$, it lies in $P \hat R$, and both have height 2, so they are equal. By Lemma 3.25.16 each element of $P \hat R$ has its support in $\Sigma_{e_l}$, so each monomial $x_m^n$ of $\psi$ and $\varphi$ has $n \ge k_0$. Then $x_l - \psi = x_l (1 - \psi / x_l)$ with $\psi / x_l \in \mathfrak{m}_{\hat S}$, and $(x_i - \varphi) / x_l \in \hat S$. $\square$

If $\operatorname{ord} \varphi \ge k_1$, then $P \subseteq (x_l, x_i, x_m^{k_1})$, and a change of the parameters $x_l$, $x_i$ by units of $S$ makes $P$ torus invariant, as in research note 83. Then the blowup is a toric step. The new case is $k_0 \le \operatorname{ord} \varphi < k_1$. Then no admissible change of parameters makes the step toric.

**Theorem 3.25.18 (the dead chart).** Let $(R, x; S, a)$ be a toric pair, and write $(a, b, c)$ for the parameters of $S$, in some order. Assume that for three distinct indices $l, i, m$
$$x_l = b^p c^k, \qquad x_i = a b^{p+1} c^{k+1}, \qquad x_m = a^r b^s c,$$
with $k \ge 2$, $r \ge 1$, $(r, s) \ne (1, 1)$, $E = k r \ge 2$ and $F_b = k s - p \ge 2$. Then $L_l = \{l, i\}$, $k_0 = k$ and $k_1 = k + 1$. Let $P$ be a prime of height 2 with $R/P$ regular, $P S$ principal, and $\operatorname{ord} \varphi = k$ in Lemma 3.25.17, and let $R_1$ be the monoidal transform of $R$ along $P$ dominated by $S$. Then $R_1 \ne S$, and $S$ dominates no monoidal transform $R_2 \ne R_1$ of $R_1$ with any regular center.

Node: SG000000CA · Lean: none yet

*Proof.* The values of $L_l$, $k_0$ and $k_1$. We have $x_i / x_l = a b c \in S$, and $x_m / x_l = a^r b^{s-p} c^{1-k} \notin S$ since $k \ge 2$. The condition $x_m^n / x_l \in S$ means $n \ge k$ and $n s \ge p$, so $k_0 = k$, because $k s \ge p + 2$. The condition $x_m^n / x_i \in S$ means $n \ge k + 1$ and $n s \ge p + 1$, so $k_1 = k + 1$.

The ring $R_1$. By Lemma 3.25.17, $P \hat R = (x_l - \psi, x_i - \varphi)$. As in the proof of the invariance lemma of research note 83, replace $a$ by a regular system of parameters of $\hat S$, with each new parameter a unit times the old one, so that $x_l - \psi(x_m)$ is the monomial $b^p c^k$ while $x_i$ and $x_m$ keep their form. We write $a, b, c$ for the new parameters, $X = x_l - \psi$ and $Z = x_m$. The completion $\hat R_1$ is $F[[X, W, Z]]$ with $W = (x_i - \varphi(Z)) / X$, and $\hat R_1 \to \hat S = F[[a, b, c]]$ is given by $X = b^p c^k$, $Z = a^r b^s c$ and
$$W = a b c - \sum_{n \ge k} \varphi_n a^{n r} b^{n s - p} c^{n - k} = a b c\, U - \lambda a^E b^{F_b},$$
where $\lambda = \varphi_k \ne 0$ and $U = 1 - \sum_{n > k} \varphi_n a^{n r - 1} b^{n s - p - 1} c^{n - k - 1}$ is a unit. Each exponent in $U$ is nonnegative, and $(k+1) r - 1 \ge 1$. We use four facts.

- (F1) $X, Z \in c \hat S$, and $W \equiv -\lambda a^E b^{F_b} \not\equiv 0$ modulo $c$. So for a nonzero series $g$ without constant term, $g(W) \not\equiv 0$ modulo $c$.
- (F2) $W, Z \in a \hat S$, and $X \equiv b^p c^k \not\equiv 0$ modulo $a$.
- (F3) $W = a b\, c'$ with $c' = c U - \lambda a^{E-1} b^{F_b - 1}$. Since $E, F_b \ge 2$, the element $c'$ is in $\mathfrak{m}_{\hat S}$ and it is not divisible by $a$, $b$ or $c$. So $W$ is not a monomial times a unit.
- (F4) An element of $F[[a, b, c]]$ is a monomial times a unit if and only if its support has a least element for the componentwise order.

Exceptional primes. Let $\mathfrak{q}$ be a height 1 prime of $S$ with $a b c \notin \mathfrak{q}$. Then $\operatorname{ht}(\mathfrak{q} \cap R) = 1$ by (E), and $R_{\mathfrak{q} \cap R} \subseteq (R_1)_{\mathfrak{q} \cap R_1} \subseteq S_{\mathfrak{q}}$ with equal outer valuation rings, so $\operatorname{ht}(\mathfrak{q} \cap R_1) = 1$. So, if $Q$ is a prime of $R_1$ of height at least 2 with $Q S = u S$ principal, each height 1 prime that contains $u$ contains $a b c$, and $u$ is a monomial in $a, b, c$ times a unit of $S$, and so of $\hat S$ in the new parameters. By Nakayama's lemma, $u$ can be taken among any given generators of $Q \hat R_1$, because $Q \hat S / \mathfrak{m}_{\hat S} Q \hat S$ has dimension 1.

Height 3. By the above, one of $X$, $W$, $Z$ generates $\mathfrak{m}_{R_1} \hat S$, and it is a monomial times a unit. It is not $W$, by (F3). The element $X$ does not divide $Z$, since $Z / X$ has the factor $c^{1-k}$. The element $Z$ does not divide $X$, by (F2). So $\mathfrak{m}_{R_1} S$ is not principal. In particular $R_1 \ne S$.

Height 2. Let $Q$ be a prime of $R_1$ of height 2 with $R_1 / Q$ regular and $Q S$ principal, and let $\Pi$ be the plane spanned by the linear parts of $Q$ in $F X + F W + F Z$. Choose $t \in \{X, W, Z\}$ with $t \notin \Pi$, and let $s_1, s_2$ be the other two. As in Lemma 3.25.17, $Q \hat R_1 = (s_1 - f(t),\ s_2 - g(t))$ with $f, g \in t F[[t]]$, and one of the two generators, call it $e$, is a monomial times a unit and divides the other one in $\hat S$. There are six cases.

- $t = W$ and $e = X - f(W)$. If $f \ne 0$, then $c \nmid e$ by (F1), and $a \nmid e$ since $e \equiv b^p c^k$ modulo $a$ by (F2). So $e = b^\beta \varepsilon$ with a unit $\varepsilon$, and modulo $a$ this gives $b^p c^k = b^\beta \bar\varepsilon$, which is false since $k \ge 1$. If $f = 0$, then $Z - g(W) \in X \hat S \subseteq c \hat S$, so $g = 0$ by (F1), and then $Z / X \in \hat S$, which is false.
- $t = W$ and $e = Z - g(W)$. The other generator $X - f(W)$ is not $0$ modulo $a$, so $a \nmid e$. But $e \in a \hat S$ by (F2). This is a contradiction.
- $t = X$ and $e = W - f(X)$. If $f \ne 0$, then $c \nmid e$ by (F1), and $e \equiv -f(b^p c^k) \not\equiv 0$ modulo $a$, so $e = b^\beta \varepsilon$. Modulo $a$ this gives $b^\beta \bar\varepsilon = -f(b^p c^k)$, whose right side is divisible by $c$ and whose left side is not. If $f = 0$, then $e = W$, which is not a monomial times a unit by (F3).
- $t = X$ and $e = Z - g(X)$. Then $e \in c \hat S$, so the other generator $W - f(X)$ lies in $c \hat S$. This contradicts (F1), since $f(X) \in c \hat S$.
- $t = Z$ and $e = X - f(Z)$. The monomial $b^p c^k$ is the only monomial of $e$ with $a$-exponent 0, because each monomial of $f(Z)$ has $a$-exponent at least $r \ge 1$. By (F4) the least element of the support is $(0, p, k)$, so $e \in X \hat S \subseteq c \hat S$. Then $W - g(Z) \in c \hat S$, which contradicts (F1).
- $t = Z$ and $e = W - g(Z)$. By (F1), $c \nmid e$, and $e \equiv -\lambda a^E b^{F_b}$ modulo $c$, so $e = a^E b^{F_b} \varepsilon$. But the monomial $a b c$ occurs in $e$ with coefficient 1: it occurs in $a b c\, U$ with coefficient 1, it is not $a^E b^{F_b}$, and it is not a monomial $a^{n r} b^{n s} c^n$ of $g(Z)$ for $n \ge 1$, since $(r, s) \ne (1, 1)$. Since $E \ge 2$, $a b c \notin a^E b^{F_b} \hat S$. This is a contradiction.

So $R_1$ has no prime $Q$ of height 2 or 3 with $R_1 / Q$ regular and $Q S$ principal. A monoidal transform $R_2 \ne R_1$ dominated by $S$ would need one. $\square$

So a chain that starts with a center of this kind stops at $R_1 \ne S$. We call $R_1$ a *dead chart*.

**Remark 3.25.19.** For the cone $\sigma = \langle (0,1,3), (1,2,2), (3,4,1) \rangle$ of Section 3.24 we have $x = b c^3$, $y = a b^2 c^4$ and $z = a^3 b^2 c$. So $(l, i, m)$ is the index triple of $(x, y, z)$, and $(p, k, r, s) = (1, 3, 3, 2)$, with $E = 9$ and $F_b = 5$. The center $P = (x, y + z^3)$ is the case $\varphi = -z^3$, and $W = a b (c + a^8 b^4)$. This agrees with the factorization $y + z^3 = a b^2 c^3 (c + a^8 b^4)$ in Section 3.24.

**Theorem 3.25.20 (thirty-six more cones are not reachable).** Let $F$ be a field and $R = F[x,y,z]_{(x,y,z)}$. For each of the 36 regular cones $\sigma$ in the following 6 classes, up to permutation of the coordinates, the ring $S_\sigma$ is not an iterated monoidal transform of $R$ for any regular centers:
$$\langle (0,1,3), (1,2,2), (3,4,1) \rangle,\ \langle (0,1,3), (2,3,2), (3,4,1) \rangle,\ \langle (0,1,4), (1,2,2), (2,3,1) \rangle,$$
$$\langle (0,1,4), (1,2,3), (2,3,1) \rangle,\ \langle (1,3,3), (2,2,3), (4,1,4) \rangle,\ \langle (1,3,3), (3,2,4), (4,1,4) \rangle.$$

Node: SG000000CB · Lean: none yet

*Proof.* A *toric state* of $\sigma$ is a regular cone $\tau \supseteq \sigma$ reached from the octant by smooth stars, and it gives a toric pair of type $\sigma$ written in the coordinates of $\tau$. For each of the 36 cones, research note 87 lists by computer all toric states of $\sigma$. The cone is not reachable by toric blowups, so $\sigma$ itself is not among them. At each state the computer checks that $|L_l| \le 2$ for all $l$, and it lists the orders of $\varphi$ with $k_0 \le \operatorname{ord} \varphi < k_1$. At each state where such an order exists, it checks that after a permutation of the parameters of $S$ the exponent vectors have the form of Theorem 3.25.18, with $\operatorname{ord} \varphi = k_0 = k$ the only such order. The data $(c_l, c_m, k)$, with $c_l$ and $c_m$ the exponent vectors of $x_l$ and $x_m$, that occur are $((0,1,2), (4,2,1), 2)$, $((0,1,2), (4,3,1), 2)$, $((0,1,3), (3,2,1), 3)$ and $((0,2,3), (3,2,1), 3)$, and they satisfy the conditions of Theorem 3.25.18.

Now let $R = T_0 \subsetneq T_1 \subseteq \dots \subseteq T_n = S_\sigma$ be a chain of monoidal transforms, and consider a state at which $(T_0, S_\sigma)$ is a toric pair. Since $|L_l| \le 2$, the first center has height 2. Either it is torus invariant after a change of parameters, and then $(T_1, S_\sigma)$ is a toric pair at another state, or it has $k_0 \le \operatorname{ord} \varphi < k_1$, and then $T_1$ is a dead chart by Theorem 3.25.18, so the chain cannot reach $S_\sigma$. By induction each $T_j$ with $j < n$ gives a toric pair at a state. At the end, $T_n = S_\sigma$ is a toric pair at a state $\tau$ in which the parameters of $T_n$ and $S_\sigma$ agree up to order, so $\tau = \sigma$. This contradicts the fact that $\sigma$ is not a state. $\square$

With $F = k(t)$ each of these 36 cones gives a counterexample to $\mathrm{Fac}_3$ and a version of Construction 3.24.19. With Section 3.24, for entries at most 4, 804 of the 900 cones that toric blowups do not reach are now known not to be reachable with regular centers, and 96 cones in 16 classes are open. For 9 of the 16 open classes the failure is at a state where $W = a^D h$ with $h$ a regular parameter of $\hat S$. For example, for $\langle (0,1,3), (1,1,2), (4,3,4) \rangle$ one has $x_l = b c^4$, $x_i = a^3 b^2 c^4$, $x_m = a b c^3$ and $k = 2$, and $W = a^2 b (a - \lambda c^2 - \dots)$. Then $(a - \lambda c^2 - \dots, b, c)$ is a new regular system of parameters, and the chart is not dead. For the other 7 classes the failure is at a state with $|L_l| = 3$, where the first centers form a larger family that has not been enumerated.

### What is open

1. $\mathrm{Princ}_4^{\rm w}$ in characteristic $p$, in the form of Proposition 3.25.5. The first case is the ideal $(z^p + g(x,y,w),\ x^a y^b)$.
2. The gluing of the principalizations of Theorem 3.25.4(5) over the points that are not closed into a principalization near a closed point.
3. Toric $\mathrm{RSF}_3$ for all regular cones. Section 3.26 settles the 11 classes of Theorem 3.25.12 and all classes with entries at most 5 except two (Theorem 3.26.19). Then $\mathrm{RSF}_3$ over imperfect fields of characteristic $p$.
4. Whether local strong factorization along all the valuations that dominate $S$ implies $\mathrm{RSF}(R, S)$.
5. Local strong factorization in dimension 3 and characteristic $p$ for the valuations that Proposition 3.25.14 does not cover: rank at least 2, residue transcendence degree at least 1, and valuations that are not Abhyankar.
6. Local monomialization of birational extensions of regular local rings of dimension 3 in characteristic $p$. With Proposition 3.25.14 and the argument of Karu it would give item 5 at least for Abhyankar valuations.
7. The global parts of Conjecture 3.24.25. Research note 85 splits it into five parts: (N1) $\mathrm{RSF}(R, S)$ at the generic point of each bad curve $\Gamma$; (N2) closures of the centers of (N1) in $V_2$ and $W_1$ that stay regular at the points of $L$ on $\bar\Gamma$ and over $U_1$; (N3) no new components of $\Phi$ through $L$ near the special points of $\bar\Gamma$ that map onto curves through $\mathrm{Sing}\, V_1$; (N4) termination of the alternating blowups, with an invariant that goes down; (N5) $\mathrm{Princ}_4^{\rm w}$ at closed points, for Steps 2, 3 and 5. In the toric case (N2) holds, and Proposition 3.25.11(4) is (N3) near $\psi^{-1}(\Gamma)$ in one example. For (N4) in the toric case, Section 3.26 shows that the number of bad cones does not always go down under a repair (Counterexample 3.26.24), and gives a condition under which it does (Proposition 3.26.25).
8. (A$^{\rm w}$) for Construction 3.24.19 with the $V_2'$ and $W_1'$ of Proposition 3.25.11, on all of $V_2'$. In the weak model of Step 3 it holds by Proposition 3.26.5. In the strong model Section 3.26 finds no obstruction on $V_2'$ and reduces the question to Problem $(\mathrm{P}_{\tau_1})$ on the octant, which is open.
9. Conjecture 3.24.24 for the 96 open cones with entries at most 4, and in general. Lemma 3.25.7 makes this question less important, because the patching does not need direct reachability.
10. Theorem 3.24.20(2) for all choices in Step 2, and whether Steps 5 and 6 of the proof of Theorem 3.24.13 give a good model for Construction 3.24.19 with some choices.

Research note 85 recommends the route through Theorem 3.24.13 in the form of Proposition 3.24.21, with Lemma 3.25.7, and with (A$^{\rm w}$) obtained by patching along curves with $\mathrm{RSF}_3$ as the local input. The first test is item 8, then toric $\mathrm{RSF}_3$ for all cones, then the full route for all toric pairs, where principalization of monomial ideals is available. Section 3.26 takes these three steps in the toric case. Without item 1 the route cannot be finished in characteristic $p$.

### Exercises

1. Prove Lemma 3.25.1 for the ideal $I = (x^2 y, x^2 z) \subseteq k[x,y,z,w]$: find $D$ and $I'$, and describe the non-invertible locus.
2. Show that the strong form of principalization implies the weak form of Definition 3.25.2.
3. In Proposition 3.25.6, take $U = \mathbb{A}^4$ and $X$ the blowup of the ideal $(x, y)^2 + (z)$. Describe $J$ and the set $G$.
4. Check the first 6 steps of the table of Theorem 3.25.10: at each step find the maximal cones that contain the center, and the two cones that replace each of them.
5. Check that the six cones of $\mathcal{G}$ in Theorem 3.25.10 are regular and lie in $\sigma_0$, with the inward normals $u_1$, $u_2$, $u_3$.
6. In Theorem 3.25.10(3), write the first blowup of $\operatorname{Spec} S_0$, along $a = c = 0$, in coordinates. Show that the chart of the cone $\langle (2,2,3), g_2, g_3 \rangle$ has the coordinates $a/c$, $b$, $c$, and express $x$, $y$, $z$ in them.
7. Show that $K$ is not principal on the cone $\langle e_3, e_2 \rangle$, the first center of Theorem 3.25.10, and that it is principal on $\sigma_0$.
8. Let $R \subseteq S$ be as in Definition 3.25.8 with $S$ an iterated monoidal transform of $R$. Prove $\mathrm{RSF}(R, S)$.
9. In Theorem 3.25.18, take $(p, k, r, s) = (1, 3, 3, 2)$ and $\varphi = -x_m^3$. Compute $W$ and check (F1) to (F3) directly. Compare with Remark 3.25.19.
10. In Theorem 3.25.18, show that the condition $(r, s) \ne (1, 1)$ is necessary for the last case of the proof. What goes wrong for $(r, s) = (1, 1)$?
11. Show that a valuation of rank 1 and rational rank 3 on a function field of dimension 3 is an Abhyankar valuation, and that its residue field is algebraic over $k$.

### Status

The results are the nodes SG000000CA to SG000000CN of the map, together with SG000000BV, SG000000C8 and SG000000C9, which Section 3.24 also uses. Lemmas 3.25.1, 3.25.3, 3.25.7 and 3.25.9, Definition 3.25.8, Propositions 3.25.5, 3.25.6, 3.25.11, 3.25.13 and 3.25.14 and Theorems 3.25.10 and 3.25.12 are new in research note 85, and the referee report in research note 89 checked them. It found them correct after five corrections, which this section includes: the role of the weak Step 3 in Proposition 3.25.11, the set $\tilde U_2 = U_2$ after Lemma 3.25.7, a polyhedral fan in the proof of Proposition 3.25.13, the citation of the proof of [CJS20, Corollary 0.4], and the version of [CP19]. Theorem 3.25.4 collects cited results. Lemma 3.25.16 is from research note 83, and the referee report in note 87 checked it. Lemma 3.25.17, Theorem 3.25.18 and Theorem 3.25.20 are new in note 87, and a second referee has not read them yet. The computations of Theorems 3.25.10, 3.25.12 and 3.25.20 are exact integer computations, and we checked the 14 stars, the fan $\mathcal{G}$ and the 5 stars of Theorem 3.25.10 again by hand and with a separate script. None of the nodes has a Lean proof. An outside expert has not yet read the result.

### Notes and references

The results are in research note 85, which continues note 83, and in Section 9 of research note 87, the referee report on note 83. Principalization in dimension 3 is [Cut09, Theorem 1.3] and [CP19, Proposition 4.4], with the numbering of arXiv 1412.0868v2. Embedded resolution of surfaces is [CJS20, Theorems 0.2 and 0.3 and Corollary 0.4]. The remark that dimension 4 is open is in the introduction of [CP19] and in [AT19, Remark 2.2.3(ii)]. Monomial and binomial ideals are in [Gow05] and [Bla12]. For toric resolution and star subdivisions see [Ful93] and the book of Cox, Little and Schenck, Proposition 3.3.15 and Theorem 11.1.9. Strong factorization for toric varieties is discussed in [AKMW02, Section 0.5], and special cases are in [DSK11]. Local strong factorization is [Kar03]. The algorithm of Perron is in [Zar44]. Local uniformization of Abhyankar valuations is [KK05]. Zariski's Main Theorem is [EGA4, Theorem 8.12.10]. Section 3.24 gives the setting, and Volume 3, Chapter 4 treats the other parts of route R2.
