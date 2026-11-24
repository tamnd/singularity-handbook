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

Lean: none yet

*Proof.* A normal closure $L'$ of $L$ over $K$ is a finite normal extension of $K$ that contains $L$ [Lan02, Chapter V, Section 3]. By Volume 1, Lemma 2.4.5, the fixed field $M$ of $G$ is purely inseparable over $K$, and $L'/M$ is Galois. Each $K$-automorphism of $L'$ fixes $M$, and each $M$-automorphism of $L'$ fixes $K$, so $\operatorname{Gal}(L'/M) = G$. $\square$

The Lean library has the main step: Volume 1, Lemma 2.4.5 is `Singularity.Algebra.isPurelyInseparable_fixedField_top`, together with `IsGalois.of_fixed_field` of Mathlib.

**Example 3.1.2.** Let $k$ be a field of characteristic $p > 2$, let $K = k(s, t)$, and let $L = K(\alpha)$ with $\alpha$ a root of $x^{2p} - s x^p - t$. Put $\beta = \alpha^p$. Then $\beta^2 - s \beta - t = 0$, so $K(\beta)/K$ is separable of degree 2, and $L/K(\beta)$ is purely inseparable of degree $p$. So $L_s = K(\beta)$. Let $\beta'$ be the other root of $y^2 - s y - t$, and let $\alpha'$ be the $p$-th root of $\beta'$. A normal closure is $L' = K(\alpha, \alpha')$. The $K$-automorphisms of $L'$ are determined by their action on $\beta$, because $\alpha$ and $\alpha'$ are the only $p$-th roots of $\beta$ and $\beta'$. So $G$ has order 2, and it exchanges $\alpha$ and $\alpha'$. The fixed field contains $\alpha + \alpha'$ and $\alpha \alpha'$, whose $p$-th powers are $\beta + \beta' = s$ and $\beta \beta' = -t$. So $M \supseteq K(s^{1/p}, t^{1/p})$, which is purely inseparable of degree $p^2$ over $K$, and $L'/M$ has degree 2. The degree count below shows that $M = K(s^{1/p}, t^{1/p})$.

We check the degree count. The field $L'$ is obtained from $L$ by adjoining a root of $x^p - \beta'$, so $[L' : K] \le 2p \cdot p = 2p^2$. The field $L'$ contains $K(s^{1/p}, t^{1/p}, \beta)$. Here $K(s^{1/p}, t^{1/p})$ is purely inseparable of degree $p^2$ over $K$, and $\beta$ is separable of degree 2 over $K$, so $\beta$ has degree 2 over $K(s^{1/p}, t^{1/p})$. So $[L' : K] = 2p^2$, and $[M : K] = p^2$.

### Galois alterations

**Definition 3.1.3 (Galois alteration).** Let $X$ be an integral variety over a field. A *Galois alteration* of $X$ is an alteration $\varphi \colon X' \to X$ together with a finite group $G$ of automorphisms of $X'$ over $X$, such that the extension $k(X) \subseteq k(X')^G$ is purely inseparable. It is a *separable Galois alteration* if $k(X')^G = k(X)$.

This is the notion of [dJ96, Section 7]. Illusie-Temkin add the word *separable* for the case where the quotient is birational to $X$, and they remark that a Galois alteration in the sense of de Jong factors as a separable Galois alteration followed by a purely inseparable one [ILO14, Exposé X, Remark 3.3.2]. An automorphism of an integral scheme $X'$ over $X$ that induces the identity on $k(X')$ is the identity on a dense open subset, hence on $X'$, because $X'$ is reduced and separated over $X$. So $G$ acts faithfully on $k(X')$, and by Artin's theorem $k(X')$ is a Galois extension of $k(X')^G$ with group $G$ [Lan02, Chapter VI, Theorem 1.8]. The degree of a Galois alteration is
$$\deg \varphi = [k(X') : k(X')^G] \cdot [k(X')^G : k(X)] = |G| \cdot p^e$$
for some $e \ge 0$, where $p$ is the characteristic exponent of the field.

The next proposition shows that each finite alteration of a normal variety is dominated by a Galois alteration, and it describes the quotient.

**Proposition 3.1.4.** Let $X$ be a normal integral variety over a field, with function field $K$, and let $L/K$ be a finite extension. Let $L'$, $G$ and $M$ be as in Proposition 3.1.1, let $Y \to X$ be the normalization of $X$ in $L'$, and let $X_M \to X$ be the normalization of $X$ in $M$. Then:

1. $G$ acts on $Y$ over $X$, and $Y \to X$ is a finite Galois alteration with group $G$;
2. over each affine open $\operatorname{Spec} A$ of $X$, with inverse image $\operatorname{Spec} B$ in $Y$, the ring of invariants $B^G$ is the integral closure of $A$ in $M$; so the quotient $Y/G$ exists and is $X_M$;
3. $X_M \to X$ is a finite universal homeomorphism, and it is an isomorphism if $L/K$ is separable.

Lean: none yet

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

This is [dJ96, Corollary 7.4]. The idea is to apply Theorem 3.1.5 over an algebraic closure of $k$, with $G$ trivial, and to take for $Y$ the quotient $X_1 / G_1$, which has quotient singularities because $X_1$ is regular. Since $k(X_1)^{G_1}$ is purely inseparable over $k(X)$, the quotient is a modification of the normalization $X''$ of $X$ in $k(X_1)^{G_1}$, and $X''$ is radicial over $X$. A limit argument then descends the data to a finite extension $k'$ of $k$. A quotient singularity is a singularity of the quotient of a regular variety by a finite group. In characteristic 0 a quotient singularity can be resolved, and Corollary 3.1.6 reduces resolution to quotient singularities in a weak sense. Abramovich-de Jong [AdJ97] use Galois alterations and the toroidal methods of [KKMS] to give a proof of a weak form of resolution of singularities in characteristic 0. In characteristic $p$ the quotient of a regular variety by a group of order divisible by $p$ can be very singular, and the corollary gives no resolution.

### Notes and references

The definitions of this section are from [dJ96, Section 7] and [ILO14, Exposé X, Remark 3.3.2]. The separable distillation is the field theory part of [Tem17, 1.3.1]. The Lean library has the fixed field lemma of Volume 1, Lemma 2.4.5, and so the field theory of Proposition 3.1.1. It has no Galois alterations.
