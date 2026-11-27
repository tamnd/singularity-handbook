---
title: The plan of the proofs
nodes: [SG0000001F, SG00000018, SG0000001C]
sources: [Abh66, Cut09, CP08, CP09, CP19, Zar44, Hir67, Hir67b, Cos92, Cut04, Jac]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The plan of the proofs

In this section we give the plan of the proof of Abhyankar, in the form of Cutkosky [Cut09], and the plan of the proof of Cossart and Piltant [CP19]. We prove one step of the first plan completely: a hypersurface singularity of multiplicity $m$ with $m! \ne 0$ in the field has a regular hypersurface that contains its points of multiplicity $m$. This is the step where the condition $p > 5$ enters.

*Motivation.* Both proofs follow one pattern, which comes from characteristic 0. One attaches to each point an invariant with values in a well ordered set. One shows that the invariant does not increase under suitable blowups, and that a finite sequence of such blowups makes it drop. Then the invariant cannot drop forever, and the process ends at a regular point. The proofs differ in the choice of the invariant and in the way they make it drop. Abhyankar and Cutkosky first lower the multiplicity below $p$ by a global construction, and then they use maximal contact as in characteristic 0. Cossart and Piltant cannot lower the multiplicity in this way, and they work with the multiplicity $p$ directly. They replace the hypersurface of maximal contact by the characteristic polyhedron of Hironaka. This section gives the plan of each proof, the invariants, and the place of the hard part. The later chapters prove the parts that fit in a textbook.

### Three theorems on surfaces and on multiplicities

The proof of Abhyankar uses three theorems that are also of independent interest. We state them in the form of [Cut09]. In this section $k$ is an algebraically closed field.

**Theorem 1.2.1 (Abhyankar).** Let $K$ be a function field of dimension $d$ over $k$. Then there is a normal projective variety $V$ over $k$ with function field $K$ such that each point of $V$ has multiplicity at most $d!$.

Lean: none yet

This is [Cut09, Theorem 1.4]. Cutkosky writes that it generalizes a method of Albanese.

*The idea of Theorem 1.2.1.* Let $V \subset \mathbb{P}^N$ be a projective model of $K$ that lies in no hyperplane, and let $n$ be its degree. The method of Albanese projects $V$ from a point $Q$ of high multiplicity $e$. If the projection is birational onto its image $V'$, then $V' \subset \mathbb{P}^{N - 1}$ has degree $n - e$. So the degree drops by $e$, while the dimension of the ambient space drops by $1$. A variety of dimension $d$ and degree $n$ that lies in no hyperplane of $\mathbb{P}^N$ satisfies $n \ge N - d + 1$. This inequality limits the number of such projections. One first replaces $V$ by its image under the $r$-th Veronese embedding. The multiplicity of a point is a property of its local ring, so the Veronese embedding does not change it. The degree becomes $r^d n$, and the linear span has dimension about $r^d n / d!$ for large $r$, by the leading term of the Hilbert polynomial. So the ratio of the degree to the dimension of the span is close to $d!$, and the number $d!$ of Theorem 1.2.1 comes from this ratio. One must also keep the projections birational and pass to a normal model at the end. We do not give these details, which are in [Cut09]. For $d = 1$ the theorem gives a projective model of the curve whose points have multiplicity 1, that is, a regular model, as the normalization does. For $d = 2$ it gives a normal model of a surface with points of multiplicity at most 2. For $d = 3$ the bound is $6$.

**Theorem 1.2.2 (embedded resolution of surfaces).** Let $V$ be a nonsingular variety of dimension 3 over $k$, let $S \subset V$ be a reduced surface, and let $E$ be a simple normal crossings divisor on $V$. Then there is a sequence of blowups $V_n \to V_{n-1} \to \dots \to V_0 = V$ such that the strict transform $S_n$ of $S$ is nonsingular and the total transform of $S + E$ is a simple normal crossings divisor. Each $V_i \to V_{i-1}$ is the blowup of a point or of a nonsingular curve that lies in the locus where the preimage of $S + E$ is not a simple normal crossings divisor.

Lean: none yet

**Theorem 1.2.3 (principalization).** Let $V$ be a nonsingular variety of dimension 3 over $k$, and let $\mathcal{I} \subseteq \mathcal{O}_V$ be a nonzero ideal sheaf. Then there is a sequence of blowups $V_n \to \dots \to V_0 = V$ such that $\mathcal{I}\mathcal{O}_{V_n}$ is locally principal. Each $V_i \to V_{i-1}$ is the blowup of a point or of a nonsingular curve that lies in the locus where $\mathcal{I}\mathcal{O}_{V_{i-1}}$ is not invertible.

Lean: none yet

These are [Cut09, Theorem 1.2] and [Cut09, Theorem 1.3]. Abhyankar proved them first in [Abh66], and Cutkosky writes that this is the most difficult part of the proof of Abhyankar. Theorem 1.2.2 is a close relative of the theorem of Cossart, Jannsen and Saito, Theorem 3.1.4 of Volume 4, which holds for each excellent surface in a regular excellent scheme.

Node: SG0000001C · Lean: `Singularity.EmbeddedResolutionSurface` (the statement only)

Cutkosky proves Theorems 1.2.2 and 1.2.3 in Sections 5 to 11 of [Cut09]. He follows the algorithm of Levi for a surface in a nonsingular threefold. He uses the invariant and the termination argument that Hironaka outlined for this algorithm in arbitrary characteristic, in his Bowdoin lectures on excellent surfaces [Hir67b]. He resolves ideals by their weak transforms, as Bravo, Encinas and Villamayor do in characteristic 0, so the main invariant is the order of an ideal and not the multiplicity of a variety.

### The five steps

Cutkosky divides the proof of Theorem 1.1.1 into five steps [Cut09].

1. Prove Theorems 1.2.2 and 1.2.3.
2. Prove Theorem 1.2.1. For a threefold $V$ it gives a normal projective model $V_0$ of the function field of $V$ whose points have multiplicity at most $3! = 6$.
3. Prove that a point of multiplicity less than $p$ can be resolved locally.
4. Patch the local resolutions to a nonsingular projective variety that is birational to $V$.
5. Change a resolution $W \to V$ into a resolution that is an isomorphism over the nonsingular locus of $V$.

Steps 1 to 4 are in the proof of Abhyankar. Steps 1 and 4 are also in the proof of Zariski for threefolds in characteristic 0 [Zar44]. Step 5 is due to Cossart [Cos92], and the proof of Step 5 in [Cut09] follows his argument. If $p > 5$, then $6 < p$, so after Step 2 each point of $V_0$ has multiplicity less than $p$, and Step 3 applies to each point. In the plan of [Cut09] this is the only place where the condition $p \ne 2, 3, 5$ enters. Step 3 gives local uniformization of each valuation of the function field. In the language of Volume 3, Chapter 4, Steps 4 and 5 are the patching.

*An outline of the proof of Theorem 1.1.1.* We describe each step by its input, its output, its invariant and its difficulty. The description follows the introduction and Section 3 of [Cut09].

1. *Surfaces in a regular threefold (Step 1).* The input is a reduced surface $S$ in a nonsingular threefold, or an ideal sheaf on it. The output is Theorem 1.2.2 or Theorem 1.2.3. The invariant is the invariant of Hironaka for the algorithm of Levi [Hir67b], built from the order of the ideal and from data of the exceptional divisors. The difficulty is the proof that this invariant drops, in each characteristic. Cutkosky writes that this is the hardest part of the proof of Abhyankar, and it takes Sections 5 to 11 of [Cut09].
2. *A model of small multiplicity (Step 2).* The input is the function field $K$. The output is a normal projective model $V_0$ whose points have multiplicity at most $6$. The tool is Theorem 1.2.1. This step is global, and it has no analogue in the proof of Cossart and Piltant.
3. *Local resolution in small multiplicity (Step 3).* The input is a point of $V_0$ of multiplicity $m < p$ and a valuation centered at it. The output is local uniformization of the valuation. We describe the proof with maximal contact, the second proof of the next subsection. The invariant is first the multiplicity $m$. At a point of multiplicity $m$ with $m!$ a unit, Proposition 1.2.5 gives a regular hypersurface $V(z')$ that contains the points of multiplicity $m$. The points of multiplicity $m$ are then described by an ideal on this regular hypersurface, the coefficient ideal of the remark below. The problem becomes a problem on a regular scheme of dimension 3, and Theorems 1.2.2 and 1.2.3 apply to it. After finitely many blowups the multiplicity along the valuation drops, and one argues by induction on $m$.
4. *Patching (Step 4).* The input is the local uniformizations of Step 3 for all the valuations. The output is a nonsingular projective variety birational to $V$. The tool is the compactness of the Zariski-Riemann space and the method of Zariski [Zar44]. In dimension 3 the patching also needs results on surfaces in regular threefolds, as in [Zar44].
5. *The regular locus (Step 5).* The input is a resolution $W \to V$ that may change $V$ over its nonsingular locus. The output is a resolution that is an isomorphism over this locus. The argument is due to Cossart [Cos92].

The structure shows where the condition $p > 5$ is used and where dimension 3 is used. The condition $p > 5$ enters only in the passage from Step 2 to Step 3. Dimension 3 enters in Steps 1, 3 and 4, because they use theorems on surfaces and ideals in regular threefolds. Without the condition on $p$, Step 2 still gives a model with multiplicity at most 6, but Step 3 has no proof at the points of multiplicity $m \ge p$. This is the gap that the work of Cossart and Piltant fills by a different method.

In dimension 4 the same plan needs $p > 4! = 24$. Volume 9, Section 3.21, shows that Steps 2 and 3 then go through if one assumes embedded resolution of divisors in $\mathbb{P}^4$ in place of Step 1, and give local uniformization of 4-folds. Step 4 has no proof in dimension 4, also in characteristic 0.

### Maximal contact in small multiplicity

Step 3 works because a singularity of small multiplicity behaves as in characteristic 0. Abhyankar proved Step 3 with the method of Jung: he projects to a nonsingular threefold and resolves the branch locus with Theorem 1.2.2. Cutkosky describes a second proof of Step 3, with ideas of Hironaka, Giraud and Cossart: in small multiplicity, a hypersurface of maximal contact exists [Cut09, Section 3]. We prove the first part of this fact. It needs only a derivation.

**Lemma 1.2.4.** Let $B$ be a ring, let $D \colon B \to B$ be an additive map with $D(ab) = a D(b) + b D(a)$ for all $a, b \in B$, and let $I$ be an ideal of $B$. Then $D(I^e) \subseteq I^{e-1}$ for each $e \ge 1$.

Lean: `Singularity.addMonoidHom_mem_pow_pred`, `Singularity.derivation_mem_pow_pred`

*Proof.* The ideal $I^e$ is generated as an additive group by the products $b a_1 \cdots a_e$ with $b \in B$ and $a_1, \dots, a_e \in I$. By the Leibniz rule,
$$D(b a_1 \cdots a_e) = D(b) a_1 \cdots a_e + \sum_{i=1}^{e} b a_1 \cdots a_{i-1} D(a_i) a_{i+1} \cdots a_e.$$
Each term on the right is a product of at least $e - 1$ elements of $I$ and an element of $B$. So it lies in $I^{e-1}$. Since $D$ is additive, $D(I^e) \subseteq I^{e-1}$. $\square$

A derivation of a domain extends to each localization by the quotient rule $D(b/s) = (s D(b) - b D(s))/s^2$. For a point $q$ of $\operatorname{Spec} B$ we write $\operatorname{ord}_q h$ for the largest $e$ with $h \in \mathfrak{m}_q^e$, where $\mathfrak{m}_q$ is the maximal ideal of $\mathcal{O}_q = B_q$. For a hypersurface $X = V(h)$ in a regular scheme, we call $\operatorname{ord}_q h$ the *multiplicity* of $X$ at $q$, as [CP19] does. The order is defined in Volume 1, Section 3.2. It equals the Samuel multiplicity of the local ring of $X$ at $q$, a classical fact that we do not use.

**Proposition 1.2.5 (maximal contact for small multiplicity).** Let $k$ be a field, let $m \ge 1$ be an integer such that $m!$ is a unit in $k$, and let
$$h = z^m + a_1 z^{m-1} + \dots + a_m \in A[z], \qquad A = k[x_1, \dots, x_n].$$
Let $z' = z + a_1/m$. Then $\operatorname{ord}_q h \le m$ for each point $q$ of $\mathbb{A}^{n+1}_k = \operatorname{Spec} A[z]$, and each point $q$ with $\operatorname{ord}_q h = m$ lies on the regular hypersurface $V(z')$.

Lean: `Singularity.maximalContact_small_multiplicity` (at the points with coordinates in $k$)

*Proof.* Let $D = \partial/\partial z$, a $k$-derivation of $A[z]$, and extend it to the local ring $\mathcal{O}_q$. If $h \in \mathfrak{m}_q^e$, then Lemma 1.2.4, applied $j$ times, gives $D^j h \in \mathfrak{m}_q^{e - j}$ for $j \le e$. We have $D^m h = m!$, a unit. So $h \notin \mathfrak{m}_q^{m+1}$, since otherwise $m! \in \mathfrak{m}_q$. This proves $\operatorname{ord}_q h \le m$. Now let $h \in \mathfrak{m}_q^m$. Then $D^{m-1} h \in \mathfrak{m}_q$. The terms $a_i z^{m-i}$ with $i \ge 2$ have degree less than $m - 1$ in $z$, so $D^{m-1}$ kills them, and
$$D^{m-1} h = m! \, z + (m-1)! \, a_1 = m! \, z'.$$
Since $m!$ is a unit, $z' \in \mathfrak{m}_q \cap A[z] = q$. So $q \in V(z')$. The map $A[z] \to A$ with $z \mapsto -a_1/m$ is surjective with kernel $(z')$, so $V(z') \cong \mathbb{A}^n_k$ is regular. $\square$

The proof uses only that $m!$ is a unit in $A$. So the proposition holds with the same proof for each ring $A$ that contains $k$, for example $A = k[[x_1, \dots, x_n]]$, and then $V(z') \cong \operatorname{Spec} A$ is regular when $A$ is regular. By the Weierstrass preparation theorem, a power series in $k[[x, z]]$ of order $m$ in which $z^m$ has a nonzero coefficient is a unit times a polynomial of the form of Proposition 1.2.5 with $A = k[[x]]$. So the proposition covers each hypersurface singularity of multiplicity $m$, after a linear change of coordinates when $k$ is infinite. The full statement of maximal contact also asks that the hypersurface keeps this property after each blowup in a permissible center. This is true for $m!$ a unit, and [Cut09, Section 3] outlines the proof. With maximal contact one can argue by induction on the dimension, as in characteristic 0.

*Remark (the coefficient ideal).* We make the last sentence precise. Let $k$ be algebraically closed, let $m \ge 2$ with $m!$ a unit in $k$, and keep the notation of Proposition 1.2.5. After the translation $z' = z + a_1/m$ the coefficient of $z'^{m-1}$ is $0$, so
$$h = z'^m + b_2 z'^{m-2} + \dots + b_m, \qquad b_i \in A.$$
Let $q$ be a closed point of $V(z')$, and translate the $x_j$ so that $q$ is the origin. Then $(z', x_1, \dots, x_n)$ is a regular system of parameters at $q$, and the graded ring of $A[z']$ at $q$ is the polynomial ring $k[Z', X_1, \dots, X_n]$. The initial form of $b_i z'^{m-i}$ has degree $\operatorname{ord}_q b_i + m - i$ and contains $Z'$ exactly to the power $m - i$. So no two of these initial forms cancel, and
$$\operatorname{ord}_q h = \min\Bigl( m, \; \min_{2 \le i \le m} \bigl( \operatorname{ord}_q b_i + m - i \bigr) \Bigr).$$
Thus $\operatorname{ord}_q h = m$ if and only if $\operatorname{ord}_q b_i \ge i$ for each $i$. Let $\mathcal{C} = (b_i^{m!/i} : 2 \le i \le m) \subseteq A$, the *coefficient ideal*. Since $\operatorname{ord}_q b_i^{m!/i} = (m!/i) \operatorname{ord}_q b_i$, we get
$$\{ q : \operatorname{ord}_q h = m \} = \{ q \in V(z') : \operatorname{ord}_q \mathcal{C} \ge m! \}.$$
So the locus of multiplicity $m$ is described by an ideal on the regular scheme $V(z') \cong \operatorname{Spec} A$, which has one dimension less than the ambient space. Now let $Y \subseteq V(z')$ be a regular center that lies in this locus, with ideal $(z', x_1, \dots, x_s)$ near $q$. Since $Y$ is regular, an element of $A$ of order at least $i$ at the generic point of $Y$ lies in $(x_1, \dots, x_s)^i$. In the $x_1$-chart put $z'' = z'/x_1$ and $b_i' = b_i / x_1^i$. Then
$$x_1^{-m} h = z''^m + b_2' z''^{m-2} + \dots + b_m',$$
which has the same form. So $V(z'')$, the strict transform of $V(z')$, again contains the points of multiplicity $m$ of the chart, and the new coefficient ideal is $x_1^{-m!} \mathcal{C}$. Thus the problem of lowering the multiplicity $m$ becomes the problem of lowering the order of the pair $(\mathcal{C}, m!)$ on a regular scheme of smaller dimension, by blowups in regular centers inside the locus where $\operatorname{ord} \mathcal{C} \ge m!$. For threefolds $V(z')$ has dimension 3. This is why Step 3 needs results on ideals in regular threefolds, as Theorem 1.2.3. Each argument above uses that $m!$ is a unit, so the reduction fails for $m \ge p$.

For $m = p$ the proof breaks down at once. The book of Cutkosky [Cut04] explains the role of maximal contact in characteristic 0 and its failure in characteristic $p$. For $h = z^p + g(x)$ we have $D h = p z^{p-1} = 0$, so no derivative in $z$ sees the variable $z$. In fact no regular hypersurface works. Example 2.2.1 of Volume 9, due to Narasimhan, is the threefold $x^2 + y z^3 + z w^3 + y^7 w = 0$ in characteristic 2. Its points of multiplicity 2 near the origin are not contained in any regular hypersurface germ, also not in a formal one.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

The equation of Narasimhan has the form $z^p + g(x, y, w)$, with the variable called $x$ there in the role of $z$. Chapter 2 shows that these equations, and the Artin-Schreier equations, are the essential cases in dimension 3.

### The plan of Cossart and Piltant

The proof of Theorem 1.1.3 in [CP19] has four parts.

1. A reduction of Theorem 1.1.3 to local uniformization, by the method of Zariski [CP19, Section 4.1]. Volume 3, Chapter 4 explains the first step of this patching.
2. A reduction of local uniformization to equations of degree $p$ of two kinds: purely inseparable equations $X^p - f$ and Artin-Schreier equations [CP19, Proposition 4.10]. Chapter 2 of this volume gives this reduction.
3. An invariant $\iota(x) = (m(x), \omega(x), \kappa(x))$ of a point $x$ on such an equation, defined with the characteristic polyhedron of Hironaka [Hir67]. At a point with $m = p$ and $\omega > 0$, the invariant does not increase under permissible blowups of the first and the second kind [CP19, Theorem 3.13]. Chapter 3 of this volume defines the polyhedron and the first invariants.
4. A proof that, along a given valuation, a suitable sequence of permissible blowups makes $\iota$ drop. This is the Projection Theorem [CP19, Theorem 5.5], and the induction on $\iota$ gives [CP19, Theorem 1.5].

Part 4 is the long part. It fills Chapters 5 to 9 of [CP19], and we do not reproduce it. Chapter 4 of this volume explains where the dimension 3 is used.

**Theorem 1.2.6 (Cossart-Piltant).** Let $S$ be an excellent regular local ring of dimension 3 with residue field of characteristic $p > 0$, and let $K$ be its fraction field. Let $h = X^p + f_1 X^{p-1} + \dots + f_p \in S[X]$ be a reduced polynomial, let $X = \operatorname{Spec} S[X]/(h)$, let $L$ be the total ring of fractions of $S[X]/(h)$, and assume one of the two conditions.

1. $K$ has characteristic $p$ and $f_1 = \dots = f_{p-1} = 0$.
2. The group $G = \operatorname{Aut}_K(L)$ is cyclic of order $p$, and $X$ is $G$-invariant.

Let $\mu$ be a valuation of $L$ with center $\mathfrak{m}_S$ on $S$. Then there is a finite sequence of local blowups $(X, x_0) \leftarrow (X_1, x_1) \leftarrow \dots \leftarrow (X_r, x_r)$ in Hironaka-permissible centers, where $x_i$ is the center of $\mu$ on $X_i$, such that $X_r$ is regular at $x_r$.

Node: SG0000001F · Lean: `Singularity.localUniformization_three` (the statement only)

This is [CP19, Theorem 1.5], stated here in short form. The node SG0000001F is local uniformization of function fields of transcendence degree 3, and Theorem 1.2.6 is the main step of its proof, so we list the node here. The Lean statement is the statement of local uniformization, and it is not a statement of Theorem 1.2.6.

*An outline of the proof of Theorem 1.2.6.* The proof in [CP19] is long, and we do not reproduce it. We give its structure, so that the reader can find each part in [CP19] and in Chapter 3 of this volume. We cite only locations that we checked.

1. *Coordinates.* Fix a regular system of parameters $(u_1, u_2, u_3)$ of $S$ and a divisor $E = \operatorname{div}(u_1 \cdots u_e)$. A change of the variable $X$ changes the polynomial $h$. Hironaka proved that there is a choice of $X$ for which the polyhedron of $h$ is minimal, the characteristic polyhedron [CP19, Proposition 2.7]. Cossart and Piltant also adapt the parameters $u_j$ to $h$ and to $E$ [CP19, Proposition 2.12]. Section 3.1 of this volume gives the polyhedron and the preparation of a vertex.
2. *The invariant.* In good coordinates one reads off $\delta$, $\epsilon$ and $\omega$ [CP19, Definitions 2.67 and 2.68], and in dimension 3 the projection number $\kappa$ [CP19, Definition 5.1]. The invariant of a point $x$ is $\iota(x) = (m(x), \omega(x), \kappa(x))$, ordered lexicographically. Section 3.2 of this volume defines these invariants.
3. *Conditions (G) and (E).* Condition (G) is the hypothesis of the theorem, and condition (E) asks that the divisor $E$ is in a good position with respect to $h$ [CP19, Section 2.3]. Section 2.3 of this volume states condition (E). Both conditions are kept by each Hironaka-permissible blowup with respect to $E$ [CP19, Propositions 2.28 and 2.34], and one reaches (E) by preparatory blowups [CP19, Corollary 4.19].
4. *No increase.* At a point with $m(x) = p$ and $\omega(x) > 0$, the invariant $\iota$ does not increase under a blowup in a center that is permissible of the first or the second kind (Theorem 3.2.6, from [CP19, Theorem 3.13]).
5. *The case $\omega = 0$.* At a point with $m(x) = p$ and $\omega(x) = 0$ a combinatorial argument on $\delta$ lowers the multiplicity (Theorem 3.2.7, from [CP19, Theorem 2.81]). Proposition 3.2.9 is its first step.
6. *Decrease along a valuation.* At a point with $m(x) = p$ and $\omega(x) > 0$, a finite sequence of blowups along a given valuation makes $\iota$ drop. This is the Projection Theorem (Theorem 3.2.11, from [CP19, Theorem 5.5]). Its proof is [CP19, Corollary 6.4] for $\kappa(x) = 1$, [CP19, Theorem 7.26] for $\kappa(x) = 2$ and [CP19, Theorem 9.6] for $\kappa(x) = 3, 4$. It fills Chapters 6 to 9 of [CP19].
7. *Small multiplicity.* At a point with $m(x) < p$ one uses the theorem of Cossart and Piltant on small multiplicity [CP14, Main Theorem 1.3].
8. *Conclusion.* The values of $\iota$ lie in a well ordered set (Lemma 3.2.10). A descending induction on $\iota$ combines Parts 3 to 7 (Proposition 3.2.12, which is the proof of [CP19, Corollary 5.6]).

Parts 1, 4 and 5, and Part 2 without $\kappa$, hold over a regular base of each dimension $n$, as Section 4.1 explains. The dimension 3 is used to reach condition (E) in Part 3, in the definition of $\kappa$ and in Part 6, in Part 7, and in the reduction of Chapter 2. Section 4.1 lists these uses and describes the structure of Part 6.

*Remark (the hypotheses of Theorem 1.2.6).* We say why each hypothesis is there.

1. *$S$ is excellent.* Each localization and each blowup of $S$ is again excellent, and the regular locus of a scheme of finite type over $S$ is open. The patching of Part 1 of the plan uses both facts. Without excellence the normalization of $S[X]/(h)$ can fail to be finite, and then no resolution can exist, by the remark after Theorem 1.1.3.
2. *$\dim S = 3$.* Parts 3, 6 and 7 of the outline use theorems on regular schemes of dimension 2 and 3, and the projection of Part 6 maps a polyhedron in $\mathbb{R}^3$ to a polygon. For $\dim S \ge 4$ the analogue of Theorem 1.2.6 is open. Chapter 4 of this volume says more.
3. *$h$ is reduced.* If $h$ has a multiple factor, then $X$ is not reduced, and no blowup makes it regular.
4. *$h$ has degree $p$.* The invariants of Chapter 3 are made for polynomials of degree $p$. Chapter 2 shows that local uniformization in general reduces to the two cases of the theorem. Other degrees are either prime to $p$, and then tame, or are made of steps of degree $p$.
5. *The two conditions.* Condition 1 is the purely inseparable case $X^p - f$. Condition 2 is the Galois case of degree $p$, which in characteristic $p$ is an Artin-Schreier extension. In characteristic $p$ a translation $X \mapsto X + \theta$ keeps each form: $(X + \theta)^p - f = X^p - (f - \theta^p)$, and $(X + \theta)^p - g^{p-1}(X + \theta) - f = X^p - g^{p-1} X - (f + g^{p-1} \theta - \theta^p)$. The polyhedron of Chapter 3 is a minimum over such translations, so this property is what the method needs.
6. *The valuation.* The theorem is local along one valuation $\mu$. This is local uniformization, not resolution. The passage to resolution is Part 1 of the plan, and it uses the method of Zariski and the compactness of the Zariski-Riemann space.

### One equation in three characteristics

The next example shows Proposition 1.2.5 at work, and it shows what changes when $m = p$.

**Example 1.2.7.** Let $k$ be an algebraically closed field of characteristic $p$, let $A = k[x, y, w]$, and let
$$h = z^2 + x^3 + y^3 + w^3 \in A[z].$$
Here $m = 2$ and $a_1 = 0$, so $z' = z$. The partial derivatives of $h$ are $2z$, $3x^2$, $3y^2$ and $3w^2$. Over a perfect field a point of the hypersurface $X = V(h)$ is singular if and only if all the partial derivatives vanish at it, by the Jacobian criterion [Jac].

*The case $p \ge 5$.* Then $2$ and $3$ are units, so the only singular point is the origin. There $\operatorname{ord} h = 2$, and the origin lies on $V(z)$, as Proposition 1.2.5 says.

*The case $p = 3$.* Then $2! = 2$ is a unit, so Proposition 1.2.5 applies. The Frobenius map gives $h = z^2 + (x + y + w)^3$, and the partial derivatives are $2z$, $0$, $0$ and $0$. So the singular locus of $X$ is the plane $V(z, x + y + w)$. Let $(0, a, b, c)$ be a closed point of this plane, so that $a + b + c = 0$. After the translation $x \mapsto x + a$, $y \mapsto y + b$, $w \mapsto w + c$ we get $h = z^2 + (x + y + w)^3$ again, of order 2. So each point of the plane has $\operatorname{ord} h = 2$, and the plane lies in the regular hypersurface $V(z')$, as Proposition 1.2.5 says. The hypersurface $X$ is singular in codimension 1, so it is not normal. In characteristic 3 the cusp $z^2 + s^3$ appears along a whole plane, while in characteristic $p \ge 5$ the singularity is isolated.

*The case $p = 2$.* Then $2! = 0$ in $k$, and Proposition 1.2.5 does not apply. Now $h = z^2 + g$ with $g = x^3 + y^3 + w^3$, an equation of the form $z^p + g$ of Section 2.3. Since $D h = 2z = 0$, no derivative in $z$ gives the hypersurface $V(z')$. The partial derivatives of $g$ are $x^2$, $y^2$ and $w^2$, so the origin is the only singular point, by Lemma 2.3.2. Here the locus of multiplicity 2 is a point, so it lies in a regular hypersurface. Example 3.3.4 computes the invariants of Cossart and Piltant at this point, and it resolves the singularity by two blowups.

Lean: none yet

We checked the partial derivatives of Example 1.2.7 by computer. The example does not show the failure of maximal contact for $m = p$. For that failure one needs a locus of multiplicity $p$ that is not contained in a regular hypersurface, as in the example of Narasimhan.

*Example (Example 1.2.7 continued, the method of maximal contact).* Let $p \ge 5$. We resolve the singularity of $X = V(h)$ at the origin by the method of the coefficient ideal, to show the method in one case. Here $m = 2$, $b_2 = g = x^3 + y^3 + w^3$ and $m! = 2$, so the coefficient ideal is $\mathcal{C} = (g)$ on the hypersurface $V(z) \cong \mathbb{A}^3_k$. We have $\operatorname{ord}_q \mathcal{C} \ge 2$ only at the origin, since the partial derivatives $3x^2$, $3y^2$ and $3w^2$ of $g$ vanish only there. So the locus of multiplicity 2 is the origin, and we blow it up.

*The first blowup.* In the $x$-chart put $z = x z_1$, $y = x y_1$ and $w = x w_1$. Then
$$h = x^2 \bigl( z_1^2 + x q \bigr), \qquad q = 1 + y_1^3 + w_1^3,$$
so the strict transform is $h_1 = z_1^2 + x q$. Its partial derivatives in $z_1$, $x$, $y_1$ and $w_1$ are $2 z_1$, $q$, $3 x y_1^2$ and $3 x w_1^2$. At a singular point of $V(h_1)$ we have $z_1 = 0$ and $q = 0$. If $x \ne 0$ there, then $y_1 = w_1 = 0$ and $q = 1$, which is false. So the singular locus in this chart is the curve
$$\Gamma = V(z_1, x, q),$$
which is the cubic $U_1^3 + U_2^3 + U_3^3 = 0$ in the exceptional plane $\{U_0 = 0\}$ of the exceptional divisor $\mathbb{P}^3_k$, with homogeneous coordinates $(U_0 : U_1 : U_2 : U_3)$ for $(z, x, y, w)$. The curve $\Gamma$ is smooth, since the partial derivatives $3 U_i^2$ have no common zero in $\mathbb{P}^2_k$. It lies in $V(z_1)$, the strict transform of the maximal contact hypersurface $V(z)$, as the remark on the coefficient ideal says. The equation $h$ is symmetric in $x$, $y$ and $w$, so the $y$-chart and the $w$-chart give the same curve. In the $z$-chart, with $x = z x_1$, $y = z y_1$ and $w = z w_1$, the strict transform is $1 + z(x_1^3 + y_1^3 + w_1^3)$, which is a unit at each point of the exceptional divisor $V(z)$. So the multiplicity did not drop, but the locus of multiplicity 2 became a smooth curve.

*The second blowup.* Let $q_0$ be a closed point of $\Gamma$. Since $\Gamma$ is smooth, the function $q$ has a nonzero derivative in $y_1$ or $w_1$ at $q_0$. So $(z_1, x, q, \ell)$ is a regular system of parameters at $q_0$ for a suitable linear form $\ell$ in $y_1$ and $w_1$. Put $v = q$. Then $h_1 = z_1^2 + x v$, and $\Gamma = V(z_1, x, v)$ near $q_0$. We blow up $\Gamma$. The three charts give
$$z_1 = v z_2, \; x = v x_3: \quad v^2 (z_2^2 + x_3), \qquad z_1 = x z_2, \; v = x v_2: \quad x^2 (z_2^2 + v_2), \qquad x = z_1 x_3, \; v = z_1 v_2: \quad z_1^2 (1 + x_3 v_2).$$
The strict transforms $z_2^2 + x_3$ and $z_2^2 + v_2$ are regular, since they have a linear term, and $1 + x_3 v_2$ is a unit at the points of the exceptional divisor $V(z_1)$. So two blowups resolve the singularity. Both centers are regular and lie in the locus of multiplicity 2, as the method requires. We checked the charts by computer.

In characteristic 2 the same equation is Example 3.3.4, and the same plane cubic appears after the first blowup. There the method of maximal contact does not apply, and Cossart and Piltant compute the invariants instead. The two examples show that the two methods can make the same choice of centers in a simple case, for different reasons.

### Notes and references

The plan of Abhyankar and the five steps are from the introduction of [Cut09]. Section 3 of [Cut09] gives an outline of Steps 2 to 5, and Sections 4 to 11 give the proofs. The description of the plan of Cossart and Piltant follows the introduction and Section 4 of [CP19]. The earlier papers [CP08, CP09] follow the same plan for fields $k$ with $[k : k^p] < \infty$.
