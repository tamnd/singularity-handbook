---
title: Alterations of degree prime to a prime
nodes: [SG0000001M]
sources: [ILO14, dJ96, dJ97, Lan02, Kel17]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Alterations of degree prime to a prime

Let $k$ be a field of characteristic exponent $p$ and let $\ell \ne p$ be a prime. In the study of étale cohomology with coefficients $\mathbb{Z}/\ell^n$ or $\mathbb{Z}_\ell$, an alteration of degree prime to $\ell$ is almost as good as a resolution, because the trace argument of Proposition 1.3.2 works when the degree is invertible in the coefficients. Gabber proved that such alterations exist. The proof is in [ILO14], the volume of the seminar on the work of Gabber on uniformization. In this section we state the theorem with care, and we explain the group theory that turns a Galois alteration into an alteration of degree prime to $\ell$.

### Definitions

The next definition allows non-integral schemes, as in [ILO14]. A *maximal point* of a scheme is a generic point of an irreducible component. A morphism is *maximally dominating* if it maps each maximal point to a maximal point.

**Definition 3.2.1 ($\ell'$-alteration).** Let $X$ be a Noetherian scheme and let $\ell$ be a prime. A morphism $h \colon X' \to X$ is an *$\ell'$-alteration* if $h$ is proper, surjective, generically finite and maximally dominating, and for each maximal point $x'$ of $X'$, with image $x = h(x')$, the degree $[k(x') : k(x)]$ is prime to $\ell$.

This is the definition of [ILO14, Exposé X, Section 2]. For integral $X$ and $X'$ an $\ell'$-alteration is an alteration in the sense of Definition 1.1.1 whose degree is prime to $\ell$.

### The group theory

**Lemma 3.2.2.** Let $L'/M$ be a finite Galois extension with group $G$, let $\ell$ be a prime, and let $P$ be an $\ell$-Sylow subgroup of $G$. Let $K \subseteq M$ be a subfield such that $M/K$ is finite and purely inseparable, of degree a power of a prime $p \ne \ell$. Then $[L'^P : K]$ is prime to $\ell$.

Lean: `Singularity.not_dvd_finrank_fixedField_sylow`

*Proof.* By the Galois correspondence $[L' : L'^P] = |P|$ and $[L' : M] = |G|$, so $[L'^P : M] = [G : P]$ [Lan02, Chapter VI, Theorem 1.1]. The index of a Sylow subgroup is prime to $\ell$. The degree $[M : K]$ is a power of $p$, so it is also prime to $\ell$. Multiply the two degrees. $\square$

The Lean statement does not need the hypothesis that $M/K$ is purely inseparable. It needs only that $[M : K]$ is a power of $p$.

**Proposition 3.2.3.** Let $\varphi \colon X' \to X$ be a Galois alteration of integral varieties over a field of characteristic exponent $p$, with group $G$ (Definition 3.1.3). Assume that $X'$ is quasi-projective over $X$. Let $\ell \ne p$ be a prime and let $P$ be an $\ell$-Sylow subgroup of $G$. Then the quotient $X'/P$ exists, and the induced morphism $X'/P \to X$ is an alteration of degree prime to $\ell$.

Lean: none yet

*Proof.* Since $X'$ is quasi-projective over $X$, each orbit of the finite group $P$ lies in an affine open subset, and the quotient $X'/P$ exists as a scheme, with a finite surjective morphism $X' \to X'/P$ and function field $k(X')^P$ [Stacks]. The morphism $X'/P \to X$ is proper, because $X' \to X$ is proper and $X' \to X'/P$ is surjective, and it is surjective and generically finite. By Artin's theorem $k(X')/k(X')^G$ is Galois with group $G$, as in Section 3.1. Lemma 3.2.2 with $L' = k(X')$, $M = k(X')^G$ and $K = k(X)$ gives that $[k(X')^P : k(X)]$ is prime to $\ell$. $\square$

The variety $X'/P$ is in general singular. If $X'$ is regular, then $X'/P$ has quotient singularities by an $\ell$-group. Since $\ell$ is invertible on $X'$, these are *tame* quotient singularities. The heart of the theorem of Gabber is that tame quotient singularities in a log smooth setting can be resolved by a modification. This is the *modification theorem* of Gabber [ILO14, Exposé VIII] and its log smooth form [ILO14, Exposé X, Theorem 1.1]. We do not state it here, because it needs the language of log schemes.

### The theorem of Gabber

**Theorem 3.2.4 (Gabber).** Let $k$ be a field, let $\ell$ be a prime different from the characteristic of $k$, let $X$ be a separated $k$-scheme of finite type, and let $Z \subseteq X$ be a nowhere dense closed subset. There are a finite extension $k'$ of $k$ of degree prime to $\ell$ and a projective $\ell'$-alteration $h \colon \tilde X \to X$ over $\operatorname{Spec} k' \to \operatorname{Spec} k$, such that $\tilde X$ is smooth and quasi-projective over $k'$, and $h^{-1}(Z)$ is the support of a relative strict normal crossings divisor in $\tilde X$ over $k'$.

Node: SG0000001M · Lean: `Singularity.exists_regular_alteration_coprime` (planned, no Lean statement yet)

This is [ILO14, Exposé X, Theorem 2.1]. A relative strict normal crossings divisor in $\tilde X$ over $k'$ is a divisor $\sum_{i \in I} D_i$ such that each $D_i$ is a closed subscheme of codimension 1, smooth over $k'$, and each scheme-theoretic intersection $\bigcap_{i \in J} D_i$ with $J \subseteq I$ is smooth over $k'$. Two points of the statement need care. First, $\tilde X$ is smooth over the finite extension $k'$, and not over $k$. If $k$ is not perfect, then $k'/k$ can be inseparable, and $\tilde X$ need not be smooth over $k$. It is regular, because it is smooth over a field. Second, the alteration $h$ is not Galois in general.

*Sketch of proof.* We follow [ILO14, Exposé X, 2.3]. The proof has three steps.

*Step 1 (reductions).* By the compactification theorem of Nagata, we can assume that $X$ is proper over $k$. We replace $X$ by the disjoint union of its irreducible components. After a base change by a finite radicial extension of $k$, which has degree a power of $p$, we can assume that $X$ is geometrically reduced. A blowup of $Z$ makes $Z$ a Cartier divisor, and the normalization makes $X$ normal. These steps are of the kind of Lemma 2.3.1.

*Step 2 (a Galois alteration).* A variant of the theorem of de Jong, due to Gabber-Vidal, gives an equivariant alteration with group $G_1$, from a scheme $X_2$ that is regular, with the inverse image of $Z$ a strict normal crossings divisor. It is constructed with a pluri-nodal fibration, as in Chapter 2 and in [dJ97]. It lies over a finite extension $S_1$ of the base field, and over a dense open subset it is of Galois type: a Galois étale covering followed by a universal homeomorphism. Let $L$ be an $\ell$-Sylow subgroup of $G_1$. By the group theory of Lemma 3.2.2, the morphism $X_2 / L \to X$ is an $\ell'$-alteration over $S_1 / L$, and $S_1/L$ has degree prime to $\ell$ over $k$.

*Step 3 (the modification theorem).* The quotient $X_2/L$ is a quotient of a log smooth scheme by a tame group. The modification theorem of Gabber [ILO14, Exposé X, Theorem 1.1], followed by a log étale desingularization, gives a projective modification of $X_2/L$ with the properties of the theorem. A modification has degree 1, so the composition is still an $\ell'$-alteration. $\square$

Illusie-Temkin also give a second proof, by induction on the dimension, in which one passes to the quotient by an $\ell$-Sylow subgroup at each step of the induction [ILO14, Exposé X, Section 3]. They prove variants over more general bases in the same exposé.

**Corollary 3.2.5.** Let $X$ be an integral variety over a field $k$, let $\ell$ be a prime different from the characteristic of $k$, and let $Z \subsetneq X$ be a proper closed subset. There is an alteration $\varphi \colon X_1 \to X$ of degree prime to $\ell$, with $X_1$ regular and projective over $X$, and a finite extension $k'$ of $k$ of degree prime to $\ell$, such that $X_1$ is smooth over $k'$ and $\varphi^{-1}(Z)$ is the support of a relative strict normal crossings divisor in $X_1$ over $k'$.

Lean: none yet

*Proof.* Since $Z$ is a proper closed subset of the integral scheme $X$, it is nowhere dense. Apply Theorem 3.2.4, and let $X_1$ be an irreducible component of $\tilde X$. Then $X_1$ is open and closed in $\tilde X$, because $\tilde X$ is smooth over $k'$ and so its connected components are irreducible. So $X_1$ is regular and integral, and $X_1 \to X$ is projective. Its generic point is a maximal point of $\tilde X$, it maps to the generic point of $X$ because $h$ is maximally dominating, and the degree is prime to $\ell$ by Definition 3.2.1. The morphism $X_1 \to X$ is proper, and its image is closed and contains the generic point, so it is surjective. The restriction of a relative strict normal crossings divisor to the open and closed subscheme $X_1$ is again one. $\square$

In the usual convention, a strict normal crossings divisor also has the property that each nonempty intersection of $c$ distinct components has codimension $c$. With this convention, Lemma 1.1.11 shows that $\varphi^{-1}(Z)$ in Corollary 3.2.5 is a strict normal crossings divisor in the sense of Definition 1.1.10, because the intersections are regular, as they are smooth over $k'$.

### Remarks

1. In characteristic $p > 0$, Corollary 3.2.5 holds for each $\ell \ne p$. Different $\ell$ give different alterations. The theorem of Gabber says nothing about the $p$-part of the degree, and it cannot be combined over all $\ell$ to give a resolution. The next section treats the $p$-part.
2. In characteristic 0, Corollary 3.2.5 holds for each prime $\ell$. Resolution of singularities in characteristic 0 is a much stronger result, with degree 1.
3. Kelly uses the theorem of Gabber to prove results on Voevodsky motives over fields of characteristic $p$, with coefficients in which $p$ is invertible [Kel17].

### An example of the group theory

The next example shows Proposition 3.2.3 for the smallest nonabelian group. It also shows why one Sylow subgroup removes only one prime.

**Example 3.2.6 (the symmetric group $S_3$).** Let $k$ be a field of characteristic different from 2 and 3. Let $S_3$ act on $X' = \mathbb{A}^3_k = \operatorname{Spec} k[x_1, x_2, x_3]$ by permutation of the coordinates. The ring of invariants is $k[e_1, e_2, e_3]$, with $e_1 = x_1 + x_2 + x_3$, $e_2 = x_1 x_2 + x_1 x_3 + x_2 x_3$ and $e_3 = x_1 x_2 x_3$, and the $e_i$ are algebraically independent. This is the fundamental theorem on symmetric polynomials [Lan02]. So $X = X'/S_3$ is again an affine space $\mathbb{A}^3_k$. Each $x_i$ is a root of the monic polynomial $T^3 - e_1 T^2 + e_2 T - e_3$, so $X' \to X$ is finite. It is a separable Galois alteration with group $S_3$ and of degree 6.

Let $\ell = 2$. A 2-Sylow subgroup is $P_2 = \{1, (12)\}$. Its ring of invariants is $k[x_1 + x_2, x_1 x_2, x_3]$, by the same theorem in the two variables $x_1, x_2$. So $X'/P_2 \cong \mathbb{A}^3_k$, and $X'/P_2 \to X$ has degree $[S_3 : P_2] = 3$, which is prime to 2.

Let $\ell = 3$. The 3-Sylow subgroup is the alternating group $A_3$, of index 2. Let $\Delta = (x_1 - x_2)(x_1 - x_3)(x_2 - x_3)$. A transposition $\tau$ maps $\Delta$ to $-\Delta$, and $-\Delta \ne \Delta$ since the characteristic is not 2. Let $f$ be invariant under $A_3$. Then $f + \tau f$ is symmetric and $f - \tau f$ changes sign under each transposition. A polynomial that changes sign under the transposition of $x_i$ and $x_j$ vanishes on $x_i = x_j$, so it is divisible by $x_i - x_j$, and $f - \tau f$ is $\Delta$ times a symmetric polynomial. So the ring of invariants of $A_3$ is $k[e_1, e_2, e_3, \Delta]$, and $\Delta^2$ is the discriminant, a polynomial in $e_1, e_2, e_3$. The morphism $X'/A_3 \to X$ has degree 2, which is prime to 3. It is the double cover of $\mathbb{A}^3_k$ given by a square root of the discriminant, and it is branched over the discriminant surface.

The subgroups of $S_3$ have the orders 1, 2, 3 and 6, so their indices are 6, 3, 2 and 1. No subgroup has an index prime to 6 except $S_3$ itself, and its quotient is $X$. So the method of Proposition 3.2.3 gives one alteration for each prime $\ell$, and no alteration other than the identity of $X$ whose degree is prime to 2 and to 3 at the same time. In characteristic $p$ we want a degree prime to each $\ell \ne p$, and Section 3.3 explains how Temkin obtains it.

### Two further statements of Gabber

The theorem of Gabber has a form over a base of dimension 1, which is the analogue of Theorem 1.2.5, and a local form over quasi-excellent schemes. We state both, because they show what the method gives in mixed characteristic and in a local setting.

**Theorem 3.2.7 (Gabber, over a base of dimension 1).** Let $S$ be a separated, integral, Noetherian, excellent, regular scheme of dimension 1, with generic point $\eta$. Let $X$ be a scheme that is separated, flat and of finite type over $S$, let $\ell$ be a prime invertible on $S$, and let $Z \subseteq X$ be a nowhere dense closed subset. There are a finite extension $\eta'$ of $\eta$ of degree prime to $\ell$, with $S'$ the normalization of $S$ in $\eta'$, a projective $\ell'$-alteration $h \colon \tilde X \to X$ over $S' \to S$ with $\tilde X$ regular and quasi-projective over $S'$, a strict normal crossings divisor $\tilde T$ on $\tilde X$, and a finite closed subset $\Sigma$ of $S'$, such that:

1. outside $\Sigma$, the morphism $\tilde X \to S'$ is smooth and $\tilde T$ is a relative divisor with normal crossings over $S'$;
2. étale locally around each geometric point of a fibre of $\tilde X$ over a point $s' \in \Sigma$, the pair $(\tilde X, \tilde T)$ is isomorphic to the pair
$$S'[u_1^{\pm 1}, \dots, u_s^{\pm 1}, t_1, \dots, t_n]/(u_1^{b_1} \cdots u_s^{b_s} t_1^{a_1} \cdots t_r^{a_r} - \pi), \qquad V(t_{r+1} \cdots t_m),$$
around the point $u_i = 1$, $t_j = 0$, with $1 \le r \le m \le n$, positive integers $a_1, \dots, a_r, b_1, \dots, b_s$ whose greatest common divisor with the characteristic exponent $p$ of $k(s')$ is 1, and $\pi$ a uniformizer at $s'$;
3. $h^{-1}(Z)$, with its reduced structure, is contained in the union of the reduced fibres of $\tilde X$ over $\Sigma$ and of $\tilde T$.

Lean: none yet

This is [ILO14, Exposé X, Theorem 2.4]. Compare with the semistable form of de Jong, Theorem 1.2.5. There the special fibre becomes a reduced divisor with strict normal crossings, so all the exponents are 1, but the degree of the alteration is not controlled. Here the degree is prime to $\ell$, and the price is that the special fibre can have multiplicities $a_j$ and $b_i$. The theorem does not say that the multiplicities can be removed by an alteration of degree prime to $\ell$.

**Theorem 3.2.8 (Gabber, local uniformization prime to $\ell$).** Let $X$ be a Noetherian quasi-excellent scheme, let $Z$ be a nowhere dense closed subset of $X$, and let $\ell$ be a prime invertible on $X$. There is a finite family of morphisms $p_i \colon X_i \to X$, covering for the topology of $\ell'$-alterations, such that for each $i$ the scheme $X_i$ is regular and connected and $p_i^{-1}(Z)$ is the support of a divisor with strict normal crossings.

Lean: none yet

This is [ILO14, Introduction, Theorem 2]. The *topology of $\ell'$-alterations* is a Grothendieck topology in which both the $\ell'$-alterations of Definition 3.2.1 and the Nisnevich coverings are covering families [ILO14, Exposé II]. So the theorem is local in two senses: one may pass to an $\ell'$-alteration, and one may work locally for the Nisnevich topology. It holds for all quasi-excellent schemes, also in mixed characteristic and without a base field. Gabber uses it in place of resolution in the proof of the finiteness theorem for étale cohomology of quasi-excellent schemes [ILO14, Introduction]. The morphisms $p_i$ are not open immersions and are not of degree 1. So the theorem is a local uniformization only after an $\ell'$-alteration. It is not the local uniformization of Volume 3 for the valuations of the function field, and it does not give a resolution.

### Why the theorem of Gabber does not give resolution

The theorem of Gabber is the strongest known form of the theorem of de Jong for coefficients prime to $\ell$. It does not give resolution in characteristic $p > 0$, for the following reasons.

1. It controls the degree only at one prime $\ell \ne p$ at a time. Different $\ell$ give different alterations (Remark 1 above), and Example 3.2.6 shows that the Sylow method cannot remove two primes at once.
2. It says nothing about the $p$-part of the degree. The $\ell$-Sylow subgroup $P$ of Proposition 3.2.3 contains no element of order $p$, but the remaining alteration $X'/P \to X$ can have degree divisible by $p$.
3. The modification theorem treats the tame quotient $X_2/L$ in Step 3 of the proof, because the action is tame and the scheme has a log regular structure. It makes the action very tame by an equivariant modification, and then the desingularization of Kato and Nizioł of log regular schemes resolves the quotient. The proof of the modification theorem uses the theory of canonical desingularization in characteristic 0 [ILO14, Introduction]. None of this applies to wild actions.
4. Theorem 3.2.8 is local for a topology in which the alterations are coverings. A local statement of this kind does not glue to a global modification.

So, with the theorem of Temkin (Section 3.3), the theorem of Gabber reduces the obstruction to resolution to the $p$-part of the degree, and this part is open in dimension at least 4.

### Notes and references

The theorem of Gabber is written in [ILO14], in particular in Exposé X by Illusie-Temkin. The earlier result of de Jong on Galois alterations [dJ97] gives the Galois alteration of Step 2 over a field. The map has node SG0000001M for Corollary 3.2.5 in the form of the statement for a variety. Nothing in this section is in the Lean library.
