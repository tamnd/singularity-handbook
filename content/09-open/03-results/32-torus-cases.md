---
title: Torus actions and the cases of resolution in dimension 4 that they give
nodes: [SG000000A7, SG000000A8]
sources: [MN26, KKMS, CP19, CJS20, Lip78, Pos23, CP08, CP09]
status: drafted
drafted_by: writer
reviewed_by: []
---

## Torus actions and the cases of resolution in dimension 4 that they give

This section reports the thirty-second research result. It is from the review of the track FO (tamnd/singularity#299) that the review of the road (tamnd/singularity#334) asked for. The preprint [MN26] of Martínez-Núnez proves that each variety with an effective action of a torus of complexity at most 3, over an algebraically closed field of characteristic $p > 0$, has a resolution. The handbook cited this result at the level of the abstract only. This section reads the paper, says what it proves and under which hypotheses, and proves the cases of resolution in dimension 4 that follow from it. The main one is $\mathrm{FQ}_4$ for each $p$-closed foliation that is invariant under a torus of rank at least 1, which solves Problem 4.10 of note 04 in its quotient form. The section also proves $\mathrm{PIRes}_4$ for semi-invariant data, and gives cases for hypersurfaces with few monomials, for affine 4-folds with a torus of dimension at least 2 (a projective resolution), for reductive groups and for finite quotients.

The results come from research note 101 and from its check, research note 101a. The check proved each statement from first principles, removed the word "equivariant" from all conclusions, and closed the gap in the projective case (see the Status).

### Motivation

Route A of Section 2.5 needs $\mathrm{FQ}_4$: for each regular 4-fold $Y$ and each $p$-closed foliation $\mathcal F$ on $Y$, the quotient $Y/\mathcal F$ has a resolution. Track FO approaches it through torus symmetry. Section 3.22 resolves the foliations that the maximal torus fixes (Theorem 3.22.10), and shows that for smaller tori the toric method fails (Examples 3.22.14 and 3.22.17). Two problems must be kept apart, as Section 3.22 does after Corollary 3.22.11.

- The *foliation form*: find blowups $f$ such that the saturated pullback $f^* \mathcal F$ is regular, or multiplicative. This is Conjecture 2.5.10 for rank one.
- The *quotient form*: find a resolution of the variety $Y/\mathcal F$. This is what $\mathrm{FQ}_4$ asks.

[MN26] is a statement on varieties, so it is about the quotient form only. It says nothing on the foliation form.

### Setting and hypotheses

In this section $k$ is an algebraically closed field of characteristic $p > 0$, with no other condition on $p$. A *variety* is a separated integral scheme of finite type over $k$. A torus is $T \cong \mathbb G_m^r$ over $k$, with character lattice $M \cong \mathbb Z^r$. A *$T$-variety* is a variety with an effective action of $T$, that is, the kernel of the action is trivial as a group scheme. The *complexity* of a $T$-variety $X$ is $\dim X - \dim T$. A *resolution* of $X$ is a proper birational morphism $W \to X$ with $W$ regular. Since $k$ is perfect, regular is the same as smooth.

Three points must be kept in mind.

1. The field is algebraically closed. Nothing here is proved over other fields.
2. A resolution is only proper. It is not asked to be projective, to be an isomorphism over $\operatorname{Reg}(X)$, or to have an exceptional set with simple normal crossings. So the results below are not cases of $\mathrm{Res}_4^{\rm pr}$ of Section 3.24, except Proposition 3.32.11.
3. [MN26] is a preprint, and it is not refereed. Its proof rests on two earlier preprints of the same author, which this review read at the level of the abstract only.

### What the paper proves

**Theorem 3.32.1 ([MN26], Theorem 1.1).** Each $T$-variety of complexity at most 3 over $k$ has a resolution.

Lean: none yet

The paper states the theorem with an equivariant resolution. Here the word is dropped, for the reason given in the list of steps below. The proof has these steps.

1. *Normalize.* The torus is smooth, so the action lifts to the normalization, and the normalization is finite.
2. *Combinatorial data.* An affine normal $T$-variety is $X(\mathcal D) = \operatorname{Spec} \Gamma(Y, \mathcal A(\mathcal D))$ for a proper polyhedral divisor $\mathcal D$ on a normal semi-projective variety $Y$ of dimension equal to the complexity [MN25a, Theorem 1.2(ii)]. A normal $T$-variety is $X(\mathcal S)$ for a divisorial fan $\mathcal S$ [MN25b, Theorem 1.4]. In characteristic 0 these are the theorems of Altmann, Hausen and Süß.
3. *Log resolution of the base* (Proposition 3.9 of [MN26]). For $Y$ normal of dimension at most 3 and $B \subset Y$ closed of codimension at least 1, there is a proper birational $\psi : Y' \to Y$ with $Y'$ regular, an isomorphism over $Y \setminus (B \cup \operatorname{Sing} Y)$, such that $\psi^{-1}(B \cup \operatorname{Sing} Y)$ is the support of a divisor with simple normal crossings. The proof applies [CP19, Theorem 1.1] to $Y$ and then [CJS20, Corollary 0.4] to the preimage of $B \cup \operatorname{Sing} Y$, which has dimension at most 2. For $\dim Y \le 2$ the resolution of surfaces of Lipman [Lip78] and the embedded resolution of curves give a projective $\psi$. For $\dim Y = 3$ the paper says that $\psi$ is only known to be proper.
4. *Pullback* (Lemma 3.8 and Proposition 3.11 of [MN26]). The pullback $\psi^* \mathcal D$ has support in the boundary, and the relative spectrum $\tilde X' \to Y'$ of its algebra maps properly and birationally onto $X$.
5. *Toroidal structure* (Proposition 3.4 of [MN26]). Over a regular base with a boundary $B'$ with simple normal crossings, $\tilde X'$ is a strict toroidal embedding. At a point of $Y'$ on the components $D_1, \dots, D_r$ of $B'$, the local model is $V \times_{\mathbb A^r} X_\sigma$, where $\sigma$ is the Cayley cone spanned by $\omega \times \{0\}$ and $\Delta_i \times \{e_i\}$. The proof is a computation in coordinates, and it does not use the characteristic.
6. *Toroidal resolution.* A strict toroidal embedding has a resolution by [KKMS, Theorem 11*]. Chapters I and II of [KKMS] work over an algebraically closed field of any characteristic. For equivariance, the paper uses the canonical resolution of Włodarczyk [Wlo20, Theorem 7.4.1]. The paper [Wlo20] works in characteristic 0, and this review did not check whether its Theorem 7.4.1 holds in characteristic $p$. Existence uses only [KKMS], so Theorem 3.32.1 is stated without equivariance.
7. *Gluing.* Section 4 of [MN26] does steps 4 to 6 for divisorial fans.

So the input in dimension 3 is only [CP19, Theorem 1.1] and [CJS20, Corollary 0.4], applied on the base. The paper uses no form of $\mathrm{Emb}_3$ and no input in dimension 4. For a $T$-variety of dimension 4, the case $\dim T = 4$ is the toric case of [KKMS], the case $\dim T = 3$ has a curve as base, the case $\dim T = 2$ has a surface as base, and only the case $\dim T = 1$ uses [CP19] and [CJS20].

Remark 5.5 of [MN26] shows that in general the base must be modified, and Example 5.6 resolves the 3-fold $t^2 = s x y (x - y)$ with the $\mathbb G_m$-weights $(0, 0, 2, 1)$. These are not used below.

### Torus actions in dimension 4

**Lemma 3.32.2 (nontrivial actions).** Let a torus $T_0$ act nontrivially on a variety $X$. Then a torus $T$ with $1 \le \dim T \le \dim T_0$ acts effectively on $X$, with the same orbits as $T_0$.

Lean: none yet

*Proof.* The kernel $K$ of the action is a closed subgroup scheme of $T_0$, and $K \ne T_0$. The quotient $T = T_0 / K$ is a quotient of a smooth connected diagonalizable group, so it is a torus. Since $T_0$ is connected and $K \ne T_0$, we have $\dim K < \dim T_0$, so $\dim T \ge 1$. The induced action of $T$ is effective, and its orbits are those of $T_0$. $\square$

**Corollary 3.32.3.** Let $X$ be a variety of dimension 4 over $k$ with a nontrivial action of a torus. Then $X$ has a resolution.

Lean: none yet

*Proof.* By Lemma 3.32.2 a torus of dimension $r \ge 1$ acts effectively on $X$, so $X$ has complexity $4 - r \le 3$. Apply Theorem 3.32.1. $\square$

**Example 3.32.4 (4-folds with no torus action).** Let $X \subset \mathbb P^5$ be a smooth hypersurface of degree $d \ge 3$. By the theorem of Matsumura and Monsky [MM64], valid in each characteristic, $\operatorname{Aut}(X)$ is finite. The group $T(k) \cong (k^\times)^r$ is divisible, and a divisible group has no nontrivial homomorphism to a finite group. So $T(k)$ acts trivially on $X$, and since $X$ is reduced and $k = \bar k$, the action is trivial. So no torus acts nontrivially on $X$, and Corollary 3.32.3 and the results below say nothing about $X$, about its open sets, or about the foliations on $X$.

### The quotient form of FQ_4

A *$p$-closed foliation* on a regular variety $Y$ is a saturated subsheaf $\mathcal F \subseteq T_Y$ that is closed under the bracket and under $p$-th powers. Its *quotient* $Y/\mathcal F$ is the scheme with the structure sheaf $\mathcal O_Y^{\mathcal F} = \{f : D(f) = 0 \text{ for each } D \in \mathcal F\}$ on the topological space of $Y$, and $q : Y \to Y/\mathcal F$ is the quotient map [Pos23, Section 2.5]. If a torus $T$ acts on $Y$, then $T(k)$ acts on derivations by $(t \cdot D)(f) = t \cdot D(t^{-1} \cdot f)$, and $\mathcal F$ is *$T$-invariant* if $t \cdot \mathcal F = \mathcal F$ for each $t \in T(k)$. This is Definition 3.22.2 for each rank.

**Lemma 3.32.5 (the action passes to the quotient).** Let $Y$ be a regular variety over $k$ with an effective action of a torus $T$, and let $\mathcal F$ be a $T$-invariant $p$-closed foliation on $Y$. Then $Y/\mathcal F$ is a normal variety, $T$ acts on $Y/\mathcal F$ so that $q$ is equivariant, and a torus of dimension $\dim T$ acts effectively on $Y/\mathcal F$.

Lean: none yet

*Proof.* (1) *The quotient.* Let $V = \operatorname{Spec} R$ be an affine open of $Y$, and put $R^{\mathcal F} = \{f \in R : D(f) = 0 \text{ for each } D \in \mathcal F(V)\}$. Since $D(f^p) = p f^{p-1} D(f) = 0$, we have $R^p \subseteq R^{\mathcal F} \subseteq R$. The ring $R$ is finite over $R^p$, because $k$ is perfect and $R$ is of finite type, and $R^p \cong R$ is noetherian. So $R^{\mathcal F}$ is a finite $R^p$-module, it is of finite type over $k$, and $R$ is finite over $R^{\mathcal F}$. The ring $R^{\mathcal F}$ is normal: if $u$ in its fraction field is integral over $R^{\mathcal F}$, then $u \in R$, because $R$ is normal, and $D(u) = 0$, because $u = a/b$ with $D(a) = D(b) = 0$. The map $\operatorname{Spec} R \to \operatorname{Spec} R^{\mathcal F}$ is finite and surjective, and it is injective because the only prime of $R$ over a prime $\mathfrak p$ of $R^{\mathcal F}$ is $\{f : f^p \in \mathfrak p\}$. So $q$ is a finite homeomorphism. For $f \in R^{\mathcal F}$ we have $(R_f)^{\mathcal F} = (R^{\mathcal F})_f$, so these affine pieces glue, and $Y/\mathcal F$ is a normal integral scheme of finite type. It is separated, because $q \times q$ is a homeomorphism that maps the diagonal of $Y$ onto the diagonal of $Y/\mathcal F$, and the diagonal of $Y$ is closed.

(2) *The action descends.* Let $a, \mathrm{pr}_2 : T \times Y \to Y$ be the action and the projection. Let $V = \operatorname{Spec} R$ be a $T$-stable affine open set. Such sets cover $Y$, by Sumihiro's theorem, which holds for normal varieties with a torus action in each characteristic. The derivations $1 \otimes D$, $D \in \mathcal F(V)$, on $k[T] \otimes_k R$ have the common kernel $k[T] \otimes_k R^{\mathcal F}$, since $k[T]$ is flat over $k$. Let $f \in R^{\mathcal F}$ and $D \in \mathcal F(V)$, and put $h = (1 \otimes D)(a^* f)$. For $t \in T(k)$ the restriction of $h$ to the slice $\{t\} \times V$ is $D(t^* f)$, because restriction to a slice commutes with $1 \otimes D$. By the formula for $t \cdot D$, the function $D(t^* f)$ is $t^*((t' \cdot D)(f))$ for $t' = t^{\pm 1}$, and this is $0$, since $t' \cdot D \in \mathcal F$ and $f \in R^{\mathcal F}$. So $h$ vanishes at each closed point of the reduced scheme $T \times V$ of finite type over $k = \bar k$, so $h = 0$. Hence $a^* f \in k[T] \otimes_k R^{\mathcal F}$, and $q \circ a$ factors through a morphism $T \times (Y/\mathcal F) \to Y/\mathcal F$. The axioms of an action hold for it, because they hold on $Y$, the map $\mathrm{id} \times q$ is a homeomorphism, and the maps of structure sheaves are injective. So $q$ is equivariant.

(3) *Effectivity.* Let $t \in T(k)$ act trivially on $Y/\mathcal F$. Since $q$ is a homeomorphism and equivariant, $t$ fixes each point of $Y$. For a local function $f$ we have $f^p \in \mathcal O_Y^{\mathcal F}$, so $(t^* f - f)^p = t^* (f^p) - f^p = 0$, and $t^* f = f$ because $Y$ is reduced. So $t$ acts trivially on $Y$, and $t = 1$. So the kernel $K$ of the action on $Y/\mathcal F$ is a subgroup scheme of $T$ with $K(k) = 1$. Then $K$ is infinitesimal, $T/K$ is a torus of dimension $\dim T$, and it acts effectively on $Y/\mathcal F$. $\square$

**Proposition 3.32.6 ($\mathrm{FQ}_4$ for torus-invariant foliations).** Let $Y$ be a regular 4-fold over $k$ with a nontrivial action of a torus $T_0$, and let $\mathcal F$ be a $T_0$-invariant $p$-closed foliation on $Y$, of any rank. Then $Y/\mathcal F$ has a resolution.

Lean: none yet

*Proof.* By Lemma 3.32.2 a torus $T = T_0/K$ of dimension at least 1 acts effectively on $Y$. Since $T_0(k) \to T(k)$ is onto, $\mathcal F$ is $T$-invariant. By Lemma 3.32.5, $Y/\mathcal F$ is a normal 4-fold with an effective action of a torus of dimension $\dim T \ge 1$, so it has complexity at most 3. Apply Theorem 3.32.1. $\square$

**Corollary 3.32.7 (Problem 4.10 of note 04, quotient form).** Let $\mathcal F$ be a $p$-closed foliation on $\mathbb A^4$ that is invariant under a nontrivial action of a torus, linear or not, with any weights. Then $\mathbb A^4/\mathcal F$ has a resolution. In particular the quotients by the foliations of Examples 3.22.14 (the scalar $\mathbb G_m$) and 3.22.17 (a torus of rank 3), and the quotients in the setting of Proposition 3.22.18, have resolutions.

Lean: none yet

*Proof.* Proposition 3.32.6 with $Y = \mathbb A^4$. $\square$

This does not need the linearization theorem that Section 3.22 asks for after Corollary 3.22.11. The resolution part of Corollary 3.22.11 is a special case, and the explicit toric description there is still useful.

### PIRes_4 for semi-invariant data

An element $b \in k(Y)$ is *semi-invariant* for an action of $T$ if $t \cdot b = \chi(t) b$ for each $t \in T(k)$ and a character $\chi \in M$.

**Proposition 3.32.8 ($\mathrm{PIRes}_4$ for semi-invariant functions).** Let $Y$ be a regular 4-fold over $k$ with an effective action of a torus $T$ of dimension $r \ge 1$, and let $b \in k(Y)$ be semi-invariant and not a $p$-th power in $K = k(Y)$. Then the normalization $Z$ of $Y$ in $K(b^{1/p})$ has a resolution.

Lean: none yet

*Proof.* (1) *A homogeneous equation.* By Sumihiro's theorem, $Y$ is covered by $T$-stable affine open sets $V = \operatorname{Spec} R$, and $R = \bigoplus_{m \in M} R_m$ is graded by the characters. A $T(k)$-stable subspace of $R$ is graded, by the linear independence of characters. The ideal $\{r \in R : r b \in R\}$ is nonzero and $T(k)$-stable, so it contains a nonzero homogeneous $b_2$. Then $b b_2^p = (b b_2) b_2^{p-1}$ is a homogeneous element of $R$, and $K((b b_2^p)^{1/p}) = K(b^{1/p})$. So on $V$ we may assume that $b \in R_\chi$.

(2) *The action on $Z$.* Since $b \notin K^p$, the polynomial $z^p - b$ is irreducible over $K$, and $S = R[z]/(z^p - b)$ is a domain with fraction field $K(b^{1/p})$. Grade $S$ by the lattice $M' = \frac1p M$ with $\deg z = \frac1p \chi$. A grading by $M'$ is an action of the torus $T'$ with character lattice $M'$, and the inclusion $M \subset M'$ gives an isogeny $T' \to T$ with kernel $\mu_p^r$. The torus $T'$ is smooth, so its action lifts to the normalization $R_Z$ of $S$, and $Z \cap q^{-1}(V) = \operatorname{Spec} R_Z$. The grading of $R_Z$ does not depend on the choice of $b$: an element $u \in R_Z$ is homogeneous of degree $\mu \in M'$ if and only if $u^p$ lies in $R_{p\mu}$. Indeed $u^p \in K$ is integral over $R$, so $u^p \in R$, as $R$ is normal. So the actions on the pieces agree on the overlaps, and they glue to an action of $T'$ on $Z$.

(3) *Effectivity.* If $t \in T'(k)$ acts trivially on $Z$, it acts trivially on $R \subseteq R_Z$, so its image in $T(k)$ is $1$, and $t \in \mu_p^r(k) = 1$. So the kernel of the action of $T'$ on $Z$ is infinitesimal, and a torus of dimension $r$ acts effectively on $Z$. So $Z$ is a 4-fold of complexity at most 3. Apply Theorem 3.32.1. $\square$

### Hypersurfaces with few monomials

**Corollary 3.32.9 (exponents in a hyperplane).** Let $f \in k[x_1, \dots, x_5]$ be irreducible, and assume that the exponents of the monomials of $f$ lie in an affine hyperplane of $\mathbb R^5$. This holds if $f$ has at most 5 monomials, and if $f$ is weighted homogeneous for a nonzero weight vector, with weights of any sign. Then $V(f) \subset \mathbb A^5$ has a resolution.

Lean: none yet

*Proof.* The exponents are integer points, so the hyperplane can be chosen as $\{m : \langle w, m \rangle = d\}$ with $w \in \mathbb Z^5 \setminus \{0\}$ and $d \in \mathbb Z$. Let $\mathbb G_m$ act by $\lambda \cdot x_i = \lambda^{w_i} x_i$. Then $f(\lambda \cdot x) = \lambda^d f(x)$, so $V(f)$ is stable. The fixed locus of the action on $\mathbb A^5$ is the linear space $L = \{x_i = 0 \text{ for } w_i \ne 0\}$, of dimension at most 4. If the action on $V(f)$ is trivial, then $V(f) \subseteq L$, so $V(f) = L$ is a coordinate hyperplane, which is regular. Otherwise apply Corollary 3.32.3. Five points of $\mathbb R^5$ always lie in an affine hyperplane. $\square$

The same proof gives each closed subvariety of dimension 4 of $\mathbb A^n$ that is stable under a nontrivial diagonal $\mathbb G_m$, for example a complete intersection by equations that are semi-invariant for one weight vector.

**Corollary 3.32.10 (the equation of $\mathrm{PIRes}_4$).** Let $g \in k[x_1, \dots, x_4]$ be not a $p$-th power, and assume that the exponents of $g$ lie in an affine hyperplane $\{m : \langle w', m \rangle = d'\}$ of $\mathbb R^4$ with $w' \in \mathbb Z^4 \setminus \{0\}$. This holds if $g$ has at most 4 monomials, and if $g$ is weighted homogeneous. Then the hypersurface $X = V(z^p + g) \subset \mathbb A^5$ has a resolution, and so has its normalization, which is the normalization of $\mathbb A^4$ in $k(x)(g^{1/p})$.

Lean: none yet

*Proof.* The ring $k[x]$ is normal, so $g$ is not a $p$-th power in $k(x)$ either, and $z^p + g$ is irreducible in $k(x)[z]$, hence in $k[x, z]$ by Gauss's lemma. Give $x_i$ the weight $p w'_i$ and $z$ the weight $d'$. Then $z^p$ and each monomial of $g$ have the weight $p d'$, so $X$ is $\mathbb G_m$-stable. The projection $X \to \mathbb A^4$ is onto and equivariant, and $\mathbb G_m$ acts nontrivially on $\mathbb A^4$ because $w' \ne 0$, so the action on $X$ is nontrivial. Corollary 3.32.3 gives a resolution of $X$. The normalization $X^\nu$ of $X$ is the normalization of $\mathbb A^4$ in $k(x)(g^{1/p})$. A resolution $W \to X$ factors through $X^\nu$, because $W$ is normal, and $W \to X^\nu$ is proper and birational. $\square$

**Remark 3.32.11 (the limit of the method).** If the exponents of $g$ span $\mathbb R^4$ affinely, then no diagonal $\mathbb G_m$ in the coordinates $(x, z)$ preserves $X$. A weight vector $(w', w_z)$ would need $\langle w', m \rangle = p w_z$ on all exponents $m$ of $g$, so $w' = 0$ and $w_z = 0$. Then Theorem 3.32.1 applies only if other coordinates, or an action that is not diagonal, exist. The method also says nothing on Conjecture 2.5.3: it resolves the hypersurface, but it gives no sequence of permissible blowups with the conditions (H1) and (H2) that ends with $\rho = 0$. The binomial case $z^p - u x^\alpha$ was known before, by Theorem 2.4.3 (Włodarczyk) and by [BM06].

### A projective resolution in complexity at most 2

**Proposition 3.32.12 (projective, affine, $\dim T \ge 2$).** Let $X$ be an affine 4-fold over $k$ with an effective action of a torus of dimension at least 2. Then $X$ has a projective resolution.

Lean: none yet

*Proof.* The normalization of $X$ is finite, so projective, and it is affine with a lifted effective action. So we may assume $X$ normal. Then $X = X(\mathcal D)$ for a proper polyhedral divisor $\mathcal D$ on a normal semi-projective variety $Y$ of dimension at most 2 [MN25a, Theorem 1.2(ii)]. For $\dim Y \le 2$ the log resolution $\psi : Y' \to Y$ of step 3 is projective. So Proposition 3.10 of [MN26] gives a proper polyhedral divisor $\mathcal D'$ on $Y'$ with support of simple normal crossings and $X(\mathcal D') \cong X$. Put $Y'_{\rm aff} = \operatorname{Spec} \Gamma(Y', \mathcal O_{Y'})$. Since $\psi$ is proper and birational and $Y$ is normal, $\Gamma(Y', \mathcal O_{Y'}) = \Gamma(Y, \mathcal O_Y)$, so $Y'_{\rm aff} = Y_{\rm aff}$. It is of finite type over $k$, and $Y' \to Y'_{\rm aff}$ is projective, because $Y'$ is semi-projective (Lemma 3.8(iv) of [MN26]). The resolution of [MN26] is the composite
$$W \longrightarrow \tilde X(\mathcal D') \xrightarrow{\ r\ } X(\mathcal D') = X .$$
The map $\tilde X(\mathcal D') \to Y'$ is affine, so the pullback of a relatively ample line bundle for $Y' \to Y'_{\rm aff}$ is relatively ample [EGA II, 5.1.12], and $\tilde X(\mathcal D')$ is quasi-projective over $Y'_{\rm aff}$. The map $r$ is proper [MN25a] and is a morphism over $Y'_{\rm aff}$, and $X \to Y'_{\rm aff}$ is separated. So $r$ is quasi-projective [EGA II, 5.3.4], and being proper, it is projective. The map $W \to \tilde X(\mathcal D')$ of [KKMS, Theorem 11*] is a composite of normalized blowups, so it is projective. A composite of projective morphisms to an affine scheme is projective. $\square$

So the 4-folds of Proposition 3.32.12 satisfy $\mathrm{Res}_4^{\rm pr}$ of Section 3.24. For complexity 3 the same proof works if the log resolution of a 3-fold in step 3 can be chosen projective. This is Problem 3.32.16.

### Reductive groups and finite quotients

**Proposition 3.32.13 (reductive groups and finite quotients).** Each of the following 4-folds over $k$ has a resolution.
1. A 4-fold $X$ with a nontrivial action of a connected reductive group $G$.
2. A quotient $X/G$, where $X$ is a 4-fold with a nontrivial action of a torus $T$, and $G$ is a finite group that acts on $X$ and commutes with $T$, provided that $X/G$ exists as a variety (for example if $X$ is quasi-projective). In particular each linear quotient $\mathbb A^4/G$ with $G \subset \mathrm{GL}_4(k)$ finite, of order prime to $p$ or not.

Lean: none yet

*Proof.* (1) A connected reductive group is generated by its maximal tori, and these are conjugate. If a maximal torus acted trivially, all of them would, and so would $G$. So a maximal torus acts nontrivially. Apply Corollary 3.32.3.

(2) The action of $T$ on $X$ commutes with $G$, so it descends to $X/G$, since taking invariants commutes with the flat base change $k[T] \otimes_k -$. Let $t \in T(k)$ act trivially on $X/G$. Then each point $x$ satisfies $t x = g x$ for some $g \in G$, so $X$ is the finite union of the closed sets $\{x : t x = g x\}$, $g \in G$. As $X$ is irreducible, $t$ acts on $X$ as one $g \in G$. So the group of $k$-points of the kernel $K$ of the action on $X/G$ maps injectively to $G$ modulo the kernel on $X$, and $K(k)$ is finite. Hence $K \ne T$, the action on $X/G$ is nontrivial, and Corollary 3.32.3 applies. For $\mathbb A^4/G$, take the scalar $\mathbb G_m$, which commutes with each linear $G$. $\square$

Part (2) for $\mathbb A^4/G$ is the case of wild quotient singularities in note 08, Section 8.4, and in note 12, row K12.

### The list of cases

All of these hold over an algebraically closed field $k$ of characteristic $p > 0$, for each $p$, in the form "a proper birational morphism from a regular variety". Each rests on Theorem 3.32.1, which is cited.

1. Each 4-fold with a nontrivial action of a torus (Corollary 3.32.3).
2. $\mathrm{FQ}_4$ for each $p$-closed foliation, of each rank, that is invariant under a nontrivial torus action on a regular 4-fold (Proposition 3.32.6). So Problem 4.10 of note 04 in its quotient form, also for the quotients of Examples 3.22.14 and 3.22.17 (Corollary 3.32.7).
3. $\mathrm{PIRes}_4$ for $(Y, b)$ with $Y$ a regular 4-fold with an effective torus action and $b$ semi-invariant (Proposition 3.32.8).
4. Each irreducible hypersurface of $\mathbb A^5$ whose exponents lie in an affine hyperplane, so each one with at most 5 monomials and each weighted homogeneous one (Corollary 3.32.9).
5. Each hypersurface $z^p + g = 0$ in $\mathbb A^5$ where the exponents of $g$ lie in an affine hyperplane of $\mathbb R^4$, so each $g$ with at most 4 monomials (Corollary 3.32.10).
6. A projective resolution of each affine 4-fold with an effective action of a torus of dimension at least 2 (Proposition 3.32.12).
7. Each 4-fold with a nontrivial action of a connected reductive group, and each quotient by a finite group of a 4-fold with a commuting torus action, so $\mathbb A^4/G$ for each finite $G \subset \mathrm{GL}_4(k)$ (Proposition 3.32.13).

This section does not claim that any of these cases is new. The toric case [KKMS] and the binomial case (Theorem 2.4.3, [BM06]) were known, and the review did not survey the literature on the other cases.

### What does not carry over

1. No general case of $\mathrm{Res}_4$, $\mathrm{FQ}_4$ or $\mathrm{PIRes}_4$. A general 4-fold has no torus action (Example 3.32.4), and the method needs the torus to act on the variety itself. A birational model with a torus action does not help.
2. No embedded resolution. [MN26] gives no form of $\mathrm{Emb}_3$, not even for $T$-stable hypersurfaces in a regular 4-fold with a torus action.
3. No local statement. [MN26] says nothing on $\mathrm{LU}_4$, $\mathrm{PILU}_4$, the statement (D) or $\mathrm{Fund}_4$.
4. No foliation statement. Nothing on Conjectures 2.5.10, 3.22.16, 3.22.20 and 3.22.21, and nothing on the foliation form of Problem 4.10.
5. No statement over a field that is not algebraically closed.
6. No isomorphism over the regular locus, no exceptional set with simple normal crossings, and no equivariance. A projective resolution only in the case of Proposition 3.32.12.

### What is open

**Problem 3.32.14 (equivariance).** Is Theorem 7.4.1 of [Wlo20] valid in characteristic $p$? Or does equivariance follow from [KKMS] alone? A possible argument: $T$ is connected, so each $t \in T(k)$ maps each component of the boundary to itself and acts trivially on the conical complex. So each ideal that a piecewise linear function on the complex defines is $T(k)$-stable, and so $T$-stable, by the argument of Lemma 3.32.5(2). Then the action lifts to each normalized blowup. The details are not checked.

**Problem 3.32.15 (the field).** Does Theorem 3.32.1 hold over a perfect field that is not algebraically closed? The descriptions of [MN25a, MN25b] work over all fields, with Galois semilinear data, so one needs a log resolution of the base and a toroidal resolution that are both compatible with the Galois action.

**Problem 3.32.16 (projectivity in complexity 3).** Can the log resolution of step 3 be chosen projective for a quasi-projective 3-fold over $k$, by the theorems of Cossart and Piltant [CP08, CP09]? Then Proposition 3.32.12 holds for each affine 4-fold with a nontrivial $\mathbb G_m$-action.

**Problem 3.32.17 (an embedded form).** Let $X$ be a $T$-variety of complexity at most 3 and $H \subset X$ a $T$-stable divisor. Does $(X, H)$ have a log resolution by the method of [MN26]? A vertical part of $H$ can be put into the boundary $B$ of step 3, and the horizontal $T$-stable prime divisors are in the toroidal boundary. But the exceptional divisors of the map $r$ need not lie over $B'$. A positive answer gives $\mathrm{Emb}_3$ for $T$-stable hypersurfaces in a regular 4-fold with a torus action, a first test case of the central node.

**Problem 3.32.18 (the foliation form).** Let $\mathcal F$ be a $T$-invariant foliation on a regular 4-fold. Does the toroidal structure that [MN26] puts on $Y/\mathcal F$ give a candidate for the blowups of Conjecture 2.5.10? The first test case is Example 3.22.14.

### Exercises

1. In Example 3.22.14, show that $z$, $w$, $x^p$, $y^p$ and $h = g x - f y$ are constants of $D$, and find their weights for the scalar $\mathbb G_m$. Conclude directly that the scalar action descends to $\mathbb A^4/\mathcal F$ and is nontrivial there.
2. Let $\mathbb G_m$ act on $\mathbb A^5$ with the weights $w \in \mathbb Z^5 \setminus \{0\}$. Show that the fixed locus is the linear space $\{x_i = 0 \text{ for } w_i \ne 0\}$.
3. Find a weight vector for $f = x_1^2 x_2 + x_3^3 + x_4 x_5^2 + x_1 x_3 x_5$ as in the proof of Corollary 3.32.9, and check that the action on $V(f)$ is nontrivial.
4. Let $p \ne 2$ and let $G = \{\pm 1\}$ act on $\mathbb A^4$ by scalars. Show that the scalar $\mathbb G_m$ acts on $\mathbb A^4/G$ with the kernel $\mu_2$, and that $\mathbb G_m/\mu_2$ acts effectively.
5. Show that a divisible group has no nontrivial homomorphism to a finite group, and that $k^\times$ is divisible for $k$ algebraically closed.
6. Let $g = 1 + x_1 + x_2 + x_3 + x_4$. Show that Corollary 3.32.10 does not apply to $z^p + g$ in these coordinates, but that $V(z^p + g)$ is regular. What does this say about the dependence of the method on coordinates?
7. In the proof of Proposition 3.32.8, let $Y = \mathbb A^1 \times \mathbb G_m^3$ with $T = \mathbb G_m^3$ acting on the second factor, and $b = x t_1$. Write down the grading of $R[z]/(z^p - b)$ and the kernel of $T' \to T$.

### Status

The results come from research note 101 and from its check, research note 101a. Theorem 3.32.1 is cited from [MN26]. Its proof was read in full, and steps 3 and 5 were checked, given [CP19], [CJS20] and [KKMS]. The descriptions of [MN25a] and [MN25b] were read at the level of the abstract only. Lemmas 3.32.2 and 3.32.5, Corollaries 3.32.3, 3.32.7, 3.32.9 and 3.32.10, and Propositions 3.32.6, 3.32.8, 3.32.12 and 3.32.13 are proved here, given Theorem 3.32.1, Sumihiro's theorem and the cited facts of [EGA II]. The check made these changes to note 101. (1) The word "equivariant" is removed from all conclusions, because [Wlo20] works in characteristic 0, and equivariance is Problem 3.32.14. (2) Proposition 3.32.12 was a sketch in note 101, and the check proved it. (3) The proof of Proposition 3.32.8 shows directly that the gradings glue, and the second proof of note 101 is removed. (4) The remark of note 101 that a 4-fold of general type has no torus action is replaced by Example 3.32.4. (5) The claims that some cases are new are removed. No case of note 101 had to be dropped. Problems 3.32.14 to 3.32.18 are open. The map has nodes for foliations and their quotients and for the maximal torus, which this section uses, and no nodes yet for its new statements. None of the statements has a Lean proof. An outside expert has not yet read the result.

### Notes and references

The results are in research notes 101 and 101a, which continue Sections 3.22 and 3.29 and the track FO of Section 2.5. The items that this section uses are these.

- [MN26] G. Martínez-Núnez, Equivariant resolution of singularities for $T$-varieties in positive characteristic, arXiv:2611.18258v1 (13 November 2026). Preprint, not refereed. Read in full.
- [MN25a] G. Martínez-Núnez, Polyhedral divisors and algebraic torus actions over arbitrary fields, arXiv:2506.22734. Abstract only.
- [MN25b] G. Martínez-Núnez, Divisorial fans and algebraic torus actions over arbitrary fields, arXiv:2512.22432. Abstract only.
- [Wlo20] J. Włodarczyk, Functorial resolution except for toroidal locus. Toroidal compactification, Adv. Math. 373 (2020), 107303, arXiv:2007.13846. A paper in characteristic 0. Used in [MN26] for equivariance only.
- [CP19] V. Cossart and O. Piltant, Resolution of singularities of arithmetical threefolds, J. Algebra 529 (2019), 268-535. Theorem 1.1.
- [CJS20] V. Cossart, U. Jannsen and S. Saito, Canonical embedded and non-embedded resolution of singularities for excellent two-dimensional schemes, arXiv:0905.2191. The book version is Desingularization: invariants and strategy, Application to dimension 2, Lecture Notes in Math. 2270, Springer, 2020. Corollary 0.4 of the arXiv version.
- [KKMS] G. Kempf, F. Knudsen, D. Mumford and B. Saint-Donat, Toroidal embeddings I, Lecture Notes in Math. 339 (1973). Theorem 11*.
- [Lip78] J. Lipman, Desingularization of two-dimensional schemes, Ann. of Math. 107 (1978), 151-207.
- [CP08, CP09] V. Cossart and O. Piltant, Resolution of singularities of threefolds in positive characteristic I and II. For Problem 3.32.16 only.
- [Pos23] Q. Posva, Singularities of quotients by 1-foliations, arXiv:2311.16694. Section 2.5, for the quotient by a foliation.
- [MM64] H. Matsumura and P. Monsky, On the automorphisms of hypersurfaces, J. Math. Kyoto Univ. 3 (1964), 347-361.
- [EGA II] A. Grothendieck, Éléments de géométrie algébrique II, Publ. Math. IHÉS 8 (1961). Propositions 5.1.12 and 5.3.4.
- [BM06] E. Bierstone and P. Milman, Desingularization of toric and binomial varieties, J. Algebraic Geom. 15 (2006), 443-486.
- The theorem of Altmann, Hausen and Süß in characteristic 0: K. Altmann and J. Hausen, Polyhedral divisors and algebraic torus actions, Math. Ann. 334 (2006), and K. Altmann, J. Hausen and H. Süß, Gluing affine torus actions via divisorial fans, Transform. Groups 13 (2008).
