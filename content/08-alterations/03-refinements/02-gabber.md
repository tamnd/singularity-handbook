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

Lean: none yet

*Proof.* By the Galois correspondence $[L' : L'^P] = |P|$ and $[L' : M] = |G|$, so $[L'^P : M] = [G : P]$ [Lan02, Chapter VI, Theorem 1.1]. The index of a Sylow subgroup is prime to $\ell$. The degree $[M : K]$ is a power of $p$, so it is also prime to $\ell$. Multiply the two degrees. $\square$

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

*Step 3 (the modification theorem).* The quotient $X_2/L$ is a quotient of a log smooth scheme by a tame group. The modification theorem of Gabber [ILO14, Exposé X, Theorem 1.1] gives a projective modification of $X_2/L$ with the properties of the theorem. A modification has degree 1, so the composition is still an $\ell'$-alteration. $\square$

Illusie-Temkin also give a second proof, by induction on the dimension, in which one passes to the quotient by an $\ell$-Sylow subgroup at each step of the induction [ILO14, Exposé X, Section 3]. They prove variants over more general bases in the same exposé.

**Corollary 3.2.5.** Let $X$ be an integral variety over a field $k$, let $\ell$ be a prime different from the characteristic of $k$, and let $Z \subsetneq X$ be a proper closed subset. There is an alteration $\varphi \colon X_1 \to X$ of degree prime to $\ell$, with $X_1$ regular and projective over $X$, and a finite extension $k'$ of $k$ of degree prime to $\ell$, such that $X_1$ is smooth over $k'$ and $\varphi^{-1}(Z)$ is the support of a relative strict normal crossings divisor in $X_1$ over $k'$.

Lean: none yet

*Proof.* Since $Z$ is a proper closed subset of the integral scheme $X$, it is nowhere dense. Apply Theorem 3.2.4, and let $X_1$ be an irreducible component of $\tilde X$. Then $X_1$ is open and closed in $\tilde X$, because $\tilde X$ is smooth over $k'$ and so its connected components are irreducible. So $X_1$ is regular and integral, and $X_1 \to X$ is projective. Its generic point is a maximal point of $\tilde X$, it maps to the generic point of $X$ because $h$ is maximally dominating, and the degree is prime to $\ell$ by Definition 3.2.1. The morphism $X_1 \to X$ is proper, and its image is closed and contains the generic point, so it is surjective. The restriction of a relative strict normal crossings divisor to the open and closed subscheme $X_1$ is again one. $\square$

In the usual convention, a strict normal crossings divisor also has the property that each nonempty intersection of $c$ distinct components has codimension $c$. With this convention, Lemma 1.1.11 shows that $\varphi^{-1}(Z)$ in Corollary 3.2.5 is a strict normal crossings divisor in the sense of Definition 1.1.10, because the intersections are regular, as they are smooth over $k'$.

### Remarks

1. In characteristic $p > 0$, Corollary 3.2.5 holds for each $\ell \ne p$. Different $\ell$ give different alterations. The theorem of Gabber says nothing about the $p$-part of the degree, and it cannot be combined over all $\ell$ to give a resolution. The next section treats the $p$-part.
2. In characteristic 0, Corollary 3.2.5 holds for each prime $\ell$. Resolution of singularities in characteristic 0 is a much stronger result, with degree 1.
3. Kelly uses the theorem of Gabber to prove results on Voevodsky motives over fields of characteristic $p$, with coefficients in which $p$ is invertible [Kel17].

### Notes and references

The theorem of Gabber was announced in letters and talks and is written in [ILO14], in particular in Exposé X by Illusie-Temkin. The earlier result of de Jong on Galois alterations [dJ97] gives the Galois alteration of Step 2 over a field. The map has node SG0000001M for Corollary 3.2.5 in the form of the statement for a variety. Nothing in this section is in the Lean library.
