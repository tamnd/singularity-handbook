---
title: Galois alterations
nodes: []
sources: [dJ96, ILO14, Tem17, Lan02, Stacks, AdJ97, KKMS]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Galois alterations

The proof of Chapter 2 gives an alteration $\varphi_1 \colon X_1 \to X$ with no special structure. De Jong also proves an equivariant form of the theorem. Its output is an alteration with a group action whose quotient is purely inseparable over $X$. This is the form that Gabber and Temkin use. In this section we explain the definition, we prove the field theory and the elementary geometry behind it, and we state the theorem of de Jong.

### Separable distillation of field extensions

Let $L/K$ be a finite field extension. The separable closure $L_s$ of $K$ in $L$ gives the canonical factorization $K \subseteq L_s \subseteq L$, with $L_s/K$ separable and $L/L_s$ purely inseparable. Temkin calls a factorization in the other order, $K \subseteq L_i \subseteq L$ with $L_i/K$ purely inseparable and $L/L_i$ separable, a *separable distillation* of $L/K$ [Tem17, 1.3.1]. It does not always exist, but it exists after we enlarge $L$.

**Proposition 3.1.1 (separable distillation).** Let $L/K$ be a finite field extension. There are a finite extension $L'$ of $L$ and an intermediate field $K \subseteq M \subseteq L'$ such that $M/K$ is purely inseparable and $L'/M$ is a Galois extension. We can take for $L'$ a normal closure of $L/K$, for $G$ the group of the $K$-automorphisms of $L'$, and for $M$ the fixed field of $G$. Then $\operatorname{Gal}(L'/M) = G$.

Lean: `Singularity.separable_distillation`, `Singularity.isPurelyInseparable_isGalois_fixedField_top`, `Singularity.bijective_restrictScalars_fixedField_top`

*Proof.* A normal closure $L'$ of $L$ over $K$ is a finite normal extension of $K$ that contains $L$ [Lan02, Chapter V, Section 3]. By Volume 1, Lemma 2.4.5, the fixed field $M$ of $G$ is purely inseparable over $K$, and $L'/M$ is Galois. Each $K$-automorphism of $L'$ fixes $M$, and each $M$-automorphism of $L'$ fixes $K$, so $\operatorname{Gal}(L'/M) = G$. $\square$

In Lean, $L'$ is the normal closure of $L/K$ in an algebraic closure of $L$, and $M$ is the fixed field of the group of all $K$-automorphisms of $L'$. The claim on the Galois group is the statement that each $M$-automorphism of $L'$ is a $K$-automorphism, and that each $K$-automorphism is an $M$-automorphism.

The Lean library has the main step: Volume 1, Lemma 2.4.5 is `Singularity.Algebra.isPurelyInseparable_fixedField_top`, together with `IsGalois.of_fixed_field` of Mathlib.

**Example 3.1.2.** Let $k$ be a field of characteristic $p > 2$, let $K = k(s, t)$, and let $L = K(\alpha)$ with $\alpha$ a root of $x^{2p} - s x^p - t$. Put $\beta = \alpha^p$. Then $\beta^2 - s \beta - t = 0$, so $K(\beta)/K$ is separable of degree 2, and $L/K(\beta)$ is purely inseparable of degree $p$. So $L_s = K(\beta)$. Let $\beta'$ be the other root of $y^2 - s y - t$, and let $\alpha'$ be the $p$-th root of $\beta'$. A normal closure is $L' = K(\alpha, \alpha')$. The $K$-automorphisms of $L'$ are determined by their action on $\beta$, because $\alpha$ and $\alpha'$ are the only $p$-th roots of $\beta$ and $\beta'$. So $G$ has order 2, and it exchanges $\alpha$ and $\alpha'$. The fixed field contains $\alpha + \alpha'$ and $\alpha \alpha'$, whose $p$-th powers are $\beta + \beta' = s$ and $\beta \beta' = -t$. So $M \supseteq K(s^{1/p}, t^{1/p})$, which is purely inseparable of degree $p^2$ over $K$, and $L'/M$ has degree 2. The degree count below shows that $M = K(s^{1/p}, t^{1/p})$.

We check the degree count. The field $L'$ is obtained from $L$ by adjoining a root of $x^p - \beta'$, so $[L' : K] \le 2p \cdot p = 2p^2$. The field $L'$ contains $K(s^{1/p}, t^{1/p}, \beta)$. Here $K(s^{1/p}, t^{1/p})$ is purely inseparable of degree $p^2$ over $K$, and $\beta$ is separable of degree 2 over $K$, so $\beta$ has degree 2 over $K(s^{1/p}, t^{1/p})$. So $[L' : K] = 2p^2$, and $[M : K] = p^2$.

### Galois alterations

**Definition 3.1.3 (Galois alteration).** Let $X$ be an integral variety over a field. A *Galois alteration* of $X$ is an alteration $\varphi \colon X' \to X$ together with a finite group $G$ of automorphisms of $X'$ over $X$, such that the extension $k(X) \subseteq k(X')^G$ is purely inseparable. It is a *separable Galois alteration* if $k(X')^G = k(X)$.

This is the notion of [dJ96, Section 7]. Illusie-Temkin add the word *separable* for the case where the quotient is birational to $X$, and they remark that a Galois alteration in the sense of de Jong factors as a separable Galois alteration followed by a purely inseparable one [ILO14, Exposé X, Remark 3.3.2]. An automorphism of an integral scheme $X'$ over $X$ that induces the identity on $k(X')$ is the identity on a dense open subset, hence on $X'$, because $X'$ is reduced and separated over $X$. So $G$ acts faithfully on $k(X')$, and by Artin's theorem $k(X')$ is a Galois extension of $k(X')^G$ with group $G$ [Lan02, Chapter VI, Theorem 1.8]. The degree of a Galois alteration is
$$\deg \varphi = [k(X') : k(X')^G] \cdot [k(X')^G : k(X)] = |G| \cdot p^e$$
for some $e \ge 0$, where $p$ is the characteristic exponent of the field.

For a separable Galois alteration the group is determined by $\varphi$. Indeed, $k(X')/k(X)$ is then Galois with group $G$, and the map from $\operatorname{Aut}_X(X')$ to $\operatorname{Aut}(k(X')/k(X))$ is injective by the argument above. So $G = \operatorname{Aut}_X(X')$. This is the form of the definition in [Tem17, 3.3.1]. Temkin takes $G = \operatorname{Aut}_X(X')$ from the start, and he calls a Galois alteration separable if it is generically étale. By Lemma 1.1.5 this agrees with Definition 3.1.3.

The next proposition shows that each finite alteration of a normal variety is dominated by a Galois alteration, and it describes the quotient.

**Proposition 3.1.4.** Let $X$ be a normal integral variety over a field, with function field $K$, and let $L/K$ be a finite extension. Let $L'$, $G$ and $M$ be as in Proposition 3.1.1, let $Y \to X$ be the normalization of $X$ in $L'$, and let $X_M \to X$ be the normalization of $X$ in $M$. Then:

1. $G$ acts on $Y$ over $X$, and $Y \to X$ is a finite Galois alteration with group $G$;
2. over each affine open $\operatorname{Spec} A$ of $X$, with inverse image $\operatorname{Spec} B$ in $Y$, the ring of invariants $B^G$ is the integral closure of $A$ in $M$; so the quotient $Y/G$ exists and is $X_M$;
3. $X_M \to X$ is a finite universal homeomorphism, and it is an isomorphism if $L/K$ is separable.

Lean: `Singularity.isIntegral_algEquiv_apply`, `Singularity.mem_integralClosure_and_fixed_iff`, `Singularity.exists_algebraMap_eq_pow_of_isPurelyInseparable`, `Singularity.eq_of_comap_eq_integralClosure` (the algebra of parts 1 to 3, with the injectivity of $\operatorname{Spec} A_M \to \operatorname{Spec} A$ but not the surjectivity or the claim on residue fields)

*Proof.* The normalization is finite (Volume 1, Theorem 2.4.7). Over $\operatorname{Spec} A$, the ring $B$ is the integral closure of $A$ in $L'$. Each $\sigma \in G$ fixes $A$ and maps elements integral over $A$ to elements integral over $A$, so $\sigma(B) = B$, and $G$ acts on $B$ over $A$. These actions glue, so $G$ acts on $Y$ over $X$. Since $k(Y)^G = L'^G = M$ is purely inseparable over $K$, part 1 follows.

For part 2, an element of $B^G$ lies in $L'^G = M$ and is integral over $A$. Conversely, an element of $M$ that is integral over $A$ lies in $B$ and is fixed by $G$. So $B^G$ is the integral closure $A_M$ of $A$ in $M$. These rings glue to $X_M$, and $\operatorname{Spec} B^G$ is the quotient of $\operatorname{Spec} B$ by $G$ in the sense of [Stacks].

For part 3, let $q = p^e$ with $M^q \subseteq K$, where $p$ is the characteristic exponent. For $b \in A_M$ the element $b^q$ lies in $K$ and is integral over $A$, so $b^q \in A$, because $A$ is normal. Let $\mathfrak{p}$ be a prime of $A$. A prime $\mathfrak{q}$ of $A_M$ over $\mathfrak{p}$ contains $b$ if and only if it contains $b^q$, that is, if and only if $b^q \in \mathfrak{p}$. So $\mathfrak{q} = \{ b \in A_M : b^q \in \mathfrak{p} \}$ is determined by $\mathfrak{p}$. This set is a prime ideal, and it lies over $\mathfrak{p}$, so the map $\operatorname{Spec} A_M \to \operatorname{Spec} A$ is bijective. For the same reason each residue field extension is purely inseparable. A morphism that is integral, surjective and radicial is a universal homeomorphism [Stacks]. If $L/K$ is separable, then $L' / K$ is Galois, $M = K$, and $X_M = X$ because $X$ is normal. $\square$

So let $X' \to X$ be the normalization of $X$ in $L$. Then $Y$ dominates $X'$, because $L \subseteq L'$, and $Y \to X$ factors as $Y \to Y/G \to X$, a Galois covering at the generic point followed by a finite universal homeomorphism. Over a perfect field, the extension $L'/K$ of function fields of an alteration can still be inseparable: Example 1.1.8 (Frobenius) shows this. Galois alterations in the sense of Definition 3.1.3 allow this case.

### The theorem of de Jong with a group

A divisor $D$ with strict normal crossings on a scheme with an action of a finite group $G$ that preserves $D$ is a *$G$-strict normal crossings divisor* if for each component $D_i$ and each $g \in G$, either $g(D_i) = D_i$ or $g(D_i) \cap D_i = \emptyset$ [dJ96, 7.1].

**Theorem 3.1.5 (de Jong).** Let $k$ be an algebraically closed field, let $X$ be a variety over $k$, let $G$ be a finite group of automorphisms of $X$ over $k$, and let $Z \subsetneq X$ be a $G$-stable closed subset. There are an alteration $\varphi_1 \colon X_1 \to X$, an open immersion $j_1 \colon X_1 \to \bar X_1$, and a finite group $G_1$ of automorphisms of $\bar X_1$ such that:

1. $G_1$ preserves $X_1$, there is a surjection $G_1 \to G$ for which $\varphi_1$ is equivariant, and the extension $k(X)^G \subseteq k(X_1)^{G_1}$ is purely inseparable;
2. $\bar X_1$ is a projective regular variety over $k$;
3. $j_1(\varphi_1^{-1}(Z)) \cup (\bar X_1 \setminus j_1(X_1))$ is a $G_1$-strict normal crossings divisor in $\bar X_1$.

Lean: none yet

This is [dJ96, Theorem 7.3]. With $G$ trivial, part 1 says that $\varphi_1$ with the group $G_1$ is a Galois alteration in the sense of Definition 3.1.3. The proof follows Chapter 2. At each step the constructions are made equivariant, and the group $G_1$ grows when a step needs a choice that the group does not preserve [dJ96, Section 7].

**Corollary 3.1.6 (de Jong).** Let $X$ be a variety over a field $k$. There are a finite extension $k'$ of $k$, an irreducible component $X'$ of $X \times_k k'$, a radicial morphism $X'' \to X'$ of varieties over $k'$, and a modification $Y \to X''$ such that $Y$ has only quotient singularities.

Lean: none yet

This is [dJ96, Corollary 7.4]. The idea is to apply Theorem 3.1.5 over an algebraic closure of $k$, with $G$ trivial, and to take for $Y$ the quotient $X_1 / G_1$, which has quotient singularities because $X_1$ is regular. Since $k(X_1)^{G_1}$ is purely inseparable over $k(X)$, the quotient is a modification of the normalization $X''$ of $X$ in $k(X_1)^{G_1}$, and $X''$ is radicial over $X$. A limit argument then descends the data to a finite extension $k'$ of $k$. A quotient singularity is a singularity of the quotient of a regular variety by a finite group. In characteristic 0 a quotient singularity can be resolved, and Corollary 3.1.6 reduces resolution to quotient singularities in a weak sense. Abramovich-de Jong [AdJ97] use Galois alterations and the toroidal methods of [KKMS] to give a proof of a weak form of resolution of singularities in characteristic 0. In characteristic $p$ the quotient of a regular variety by a group of order divisible by $p$ can be very singular, and the corollary gives no resolution. If $|G_1|$ is prime to $p$, the action of $G_1$ on $X_1$ is tame, and it is generically free, because $G_1$ acts faithfully on $k(X_1)$. A regular scheme with the trivial log structure is log regular. So the modification theorem of Gabber [ILO14, Exposé VIII, Theorem 1.1] gives an equivariant projective modification $X_1' \to X_1$ with a very tame action, and $X_1'/G_1$ is log regular and has a resolution by a modification [ILO14, Exposé VIII, Section 3]. In this case $X_1/G_1$ has a regular modification, and $X$ has a regular alteration that is generically purely inseparable. This is still not a resolution of $X$. So in characteristic $p$ the corollary is not a resolution, and with Theorem 1.2.1 it does not give resolution of singularities in dimension at least 4.

### Where the groups come from

The groups of Galois alterations are not an extra structure that we add by hand. They come from the proof of Chapter 2. The two alterations of the base in Steps 5 and 6 of the table of Section 2.3 are base changes by Galois covers of the base: in Step 5 by construction, and in Step 6 by Lemma 2.2.9. The next proposition shows that the group of the base passes to the total space. This is the mechanism behind the equivariant proof of [dJ96, Section 7].

**Proposition 3.1.7.** Let $f \colon X \to Y$ be a dominant morphism of integral varieties over a field, with $F = k(X)$ and $K = k(Y)$, and assume that the generic fibre $X_\eta$ of $f$ is geometrically integral over $K$. Let $\psi \colon Y' \to Y$ be a separable Galois alteration with group $\Gamma$, and let $L = k(Y')$. Let $X'$ be the closure, with its reduced structure, of the fibre of $Y' \times_Y X$ over the generic point of $X$. Then:

1. this fibre is the single point $\operatorname{Spec}(F \otimes_K L)$, and $F \otimes_K L$ is a field;
2. $\Gamma$ acts on $X'$ over $X$, and the projection $X' \to X$ is a separable Galois alteration with group $\Gamma$ and of degree $|\Gamma|$.

Lean: `Singularity.exists_eq_tmul_one_of_forall_fixed`, `Singularity.galTensorAction_tmul_one`, `Singularity.finrank_tensorProduct_eq_card_gal` (the invariants of the Galois action on $F \otimes_K L$). The action on schemes is not in Lean yet.

*Proof.* The generic fibre of $\psi$ is the single point $\operatorname{Spec} L$ (Lemma 1.1.2). So the fibre of $Y' \times_Y X$ over the generic point $\operatorname{Spec} F$ of $X$ is $\operatorname{Spec} F \times_{\operatorname{Spec} K} \operatorname{Spec} L = \operatorname{Spec}(F \otimes_K L)$. The ring $F \otimes_K L$ is a localization of the coordinate rings of the affine opens of $X_\eta \times_K L$, and this scheme is integral by hypothesis. So $F \otimes_K L$ is a domain. It is finite over the field $F$, and a domain that is finite over a field is a field. This proves part 1.

So $X'$ is integral with function field $F' = F \otimes_K L$. The projection $X' \to X$ is proper, as the composite of a closed immersion and a base change of $\psi$. It is dominant, and $[F' : F] = [L : K] = |\Gamma|$, because $L$ is Galois over $K$ with group $\Gamma$ (Definition 3.1.3 and the remark after it). By Lemma 1.1.4 it is an alteration of degree $|\Gamma|$. The group $\Gamma$ acts on $Y' \times_Y X$ through the first factor, over $X$. It maps the fibre over the generic point of $X$ to itself, and this fibre is one point, so $\Gamma$ maps $X'$ to itself. On $F' = F \otimes_K L$ an element $\gamma$ acts by $1 \otimes \gamma$. The invariants $L^\Gamma = K$ are the kernel of the $K$-linear map $L \to \prod_{\gamma \in \Gamma} L$, $b \mapsto (\gamma(b) - b)_\gamma$. The functor $F \otimes_K -$ is exact, so the kernel of the corresponding map for $F'$ is $F \otimes_K K = F$. So $F'^\Gamma = F$, and $X' \to X$ is a separable Galois alteration with group $\Gamma$. $\square$

The hypothesis on the generic fibre holds in the proof of Chapter 2. By (vi)(a) and (vi)(c), the generic fibre of $f$ is smooth and geometrically connected, so it is geometrically integral. Also $X'$ is the scheme of Lemma 2.3.5, because that scheme is integral and its generic point is the point of part 1.

We apply the proposition to Step 5. There $Y'$ is the normalization of $Y$ in the Galois extension $L$ of $k(Y)$, and $\Gamma = \operatorname{Gal}(L/k(Y))$ acts on $Y'$ by Proposition 3.1.4. By Proposition 3.1.7 the base change $X' \to X$ is a separable Galois alteration with group $\Gamma$. The group acts on $Z' = \varphi^{-1}(Z)$, because it acts over $X$. So it permutes the irreducible components of $Z'$, and hence it permutes the sections $\sigma_j$. The sections that come from one component $Z_i$ of $Z$ correspond to the $k(Y)$-embeddings of $k(Z_i)$ into $L$, and $\Gamma$ acts transitively on these embeddings. The same argument applies to the level cover of Step 6, by Lemma 2.2.9, and there the group $H \subseteq \mathrm{GL}_{2g}(\mathbb{F}_\ell)$ also acts on the level structures. The equivariant proof of Theorem 3.1.5 keeps track of these actions through all the steps, and it has to treat the steps that are not equivariant, such as the general choices of Lemma 2.3.3. We do not give the details, which are in [dJ96, Section 7].

The group matters because the quotients by its subgroups are alterations of smaller degree. If $X' \to X$ is a Galois alteration with group $G$ and $H \subseteq G$ is a subgroup, then $k(X')^H$ has degree $[G : H]$ over $k(X')^G$ [Lan02, Chapter VI, Theorem 1.1]. The proofs of Gabber and Temkin in the next two sections choose $H$ so that this index has no prime factor that they want to avoid. A second use of the group is a splitting that needs fewer hypotheses than Proposition 1.3.2.

**Lemma 3.1.8 (Reynolds operator).** Let $B$ be a ring, let $G$ be a finite group of automorphisms of $B$, and let $A = B^G$. Assume that $|G|$ is invertible in $B$. Then the map
$$\rho \colon B \to A, \quad \rho(b) = \frac{1}{|G|} \sum_{g \in G} g(b),$$
is $A$-linear and $\rho(a) = a$ for $a \in A$. So $A$ is a direct summand of $B$ as an $A$-module, and $IB \cap A = I$ for each ideal $I$ of $A$.

Lean: `Singularity.reynolds_mem`, `Singularity.reynolds_add`, `Singularity.reynolds_mul_of_mem`, `Singularity.reynolds_of_mem`, `Singularity.comap_map_invariantSubring`

*Proof.* The element $|G|$ lies in $A$, and its inverse in $B$ is fixed by $G$, so $1/|G| \in A$. For $h \in G$ the map $g \mapsto hg$ is a bijection of $G$, so $h(\rho(b)) = \rho(b)$, and $\rho(b) \in A$. For $a \in A$ and $b \in B$ we have $g(ab) = a \, g(b)$, so $\rho(ab) = a \rho(b)$, and $\rho(a) = |G| a / |G| = a$. So $\rho$ is an $A$-linear left inverse of the inclusion $A \to B$, and $B = A \oplus \ker \rho$. Let $x \in IB \cap A$, and write $x = \sum_k i_k b_k$ with $i_k \in I$ and $b_k \in B$. Then $x = \rho(x) = \sum_k i_k \rho(b_k) \in I$. The other inclusion is clear. $\square$

Let $G$ act faithfully on a domain $B$ with fraction field $L$, and let $K = L^G$. Then $L/K$ is Galois with group $G$, and $\sum_{g \in G} g$ is the trace $\operatorname{Tr}_{L/K}$, because for a Galois extension the trace is the sum of the conjugates [Lan02, Chapter VI, Section 5]. So $\rho$ is the restriction to $B$ of $\frac{1}{|G|} \operatorname{Tr}_{L/K}$, the map of the proof of Proposition 1.3.2 with $d = [L : K] = |G|$. Lemma 3.1.8 does not need $A$ to be normal or $B$ to be a domain. If $|G|$ is not invertible, then the trace can fail to be surjective, as the next example shows.

**Example 3.1.9 (a wild involution).** Let $k$ be a field of characteristic 2, let $B = k[s, t]$, and let $\sigma$ be the automorphism of $B$ over $k$ with $\sigma(s) = s$ and $\sigma(t) = t + s$. Then $\sigma^2(t) = t + 2s = t$, so $G = \{1, \sigma\}$ has order 2, and $|G| = 0$ in $k$. Let $n = t(t + s) = t^2 + st$ and $A_0 = k[s, n]$. Both $s$ and $n$ are fixed by $\sigma$, so $A_0 \subseteq B^G$.

We claim that $B = A_0 \oplus A_0 t$. The relation $t^2 = n + st$ lets us write each polynomial in $s$ and $t$ as $a + bt$ with $a, b \in A_0$. If $a + bt = 0$, then also $\sigma(a + bt) = a + bt + bs = 0$, so $bs = 0$ and $b = 0$, and then $a = 0$. This proves the claim. An element $a + bt$ is fixed by $\sigma$ if and only if $bs = 0$, that is, $b = 0$. So $B^G = A_0 = k[s, n]$, a polynomial ring, and the quotient $\mathbb{A}^2_k / G$ is the regular surface $\mathbb{A}^2_k$.

The trace of $a + bt$ is $(a + bt) + (a + bt + bs) = bs$, so $\operatorname{Tr}(B) = sA_0$, a proper ideal. So the trace gives no splitting. The ring $A_0$ is still a direct summand of $B$, by the projection $a + bt \mapsto a$, but this projection does not come from the group. The quotient map is ramified along the line $s = 0$, where $\sigma$ acts trivially, because $\sigma(t) - t = s$. The prime $sB$ lies over the prime $sA_0$, since $B/sB = k[t]$ and the image of $A_0$ in it is $k[t^2]$. The residue field of $B$ at $sB$ is $k(t)$, and the residue field of $A_0$ at $sA_0$ is $k(n) = k(t^2)$. So the extension of residue fields is purely inseparable of degree 2, although the extension of function fields is separable. This is a form of wild ramification. Over the open set $s \ne 0$, put $w = t/s$. Then $w^2 + w = n/s^2$, so the cover is an Artin-Schreier cover there, as in Example 3.3.4.

Lean: `Singularity.wildSigma_wildSigma`, `Singularity.wildSigma_eq_self_iff`, `Singularity.exists_eq_add_mul_X_one`, `Singularity.eq_zero_of_add_mul_X_one_eq_zero`, `Singularity.exists_add_wildSigma_eq_iff` (the decomposition $B = A_0 \oplus A_0 t$ and the trace, not the claims on ramification)

### Notes and references

The definitions of this section are from [dJ96, Section 7] and [ILO14, Exposé X, Remark 3.3.2]. The separable distillation is the field theory part of [Tem17, 1.3.1]. The Lean library has the fixed field lemma of Volume 1, Lemma 2.4.5, and so the field theory of Proposition 3.1.1. It has no Galois alterations.
