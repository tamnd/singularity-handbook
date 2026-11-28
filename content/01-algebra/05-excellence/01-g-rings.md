---
title: Formal fibres and G-rings
nodes: []
sources: [EGA4, EGA4-7, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Formal fibres and G-rings

Let $(A, \mathfrak{m})$ be a Noetherian local ring with completion $\hat{A}$. Section 4.3 showed that $A$ and $\hat{A}$ have the same dimension, and that $A$ is regular if and only if $\hat{A}$ is regular. Other properties do not pass from $A$ to $\hat{A}$: the local ring of the node is a domain, but its completion is not (Example 4.3.5). The map $A \to \hat{A}$ is flat, so the difference between $A$ and $\hat{A}$ is in the fibres of $\operatorname{Spec} \hat{A} \to \operatorname{Spec} A$. These are the formal fibres of $A$. A G-ring is a ring whose formal fibres are as good as possible.

Throughout, a Noetherian ring $B$ is *regular* if $B_\mathfrak{q}$ is a regular local ring for each prime ideal $\mathfrak{q}$, that is, if $\operatorname{Reg}(B) = \operatorname{Spec} B$ (Definition 1.7.1).

### Geometric regularity

**Definition 5.1.1.** Let $k$ be a field and let $B$ be a Noetherian $k$-algebra. Then $B$ is *geometrically regular over $k$* if the ring $B \otimes_k k'$ is regular for each finite field extension $k'$ of $k$.

The ring $B \otimes_k k'$ is a finite $B$-algebra, so it is Noetherian. In the definition one can replace "finite" by "finitely generated", and one can also restrict to purely inseparable extensions $k'$ [EGA4, Section 6]. We do not use these facts. The next proposition shows that the definition is new only in positive characteristic.

**Proposition 5.1.2.** Let $k$ be a field of characteristic $0$ and let $B$ be a Noetherian $k$-algebra. Then $B$ is geometrically regular over $k$ if and only if $B$ is regular.

Lean: `Singularity.Algebra.IsGeometricallyRegular.isRegularRing` (one direction), `Singularity.Algebra.isGeometricallyRegular_of_charZero` (the converse for a field over a field of characteristic 0). The converse in general is not in Lean yet.

*Proof.* Take $k' = k$ to see that a geometrically regular ring is regular. Conversely, let $B$ be regular and let $k'$ be a finite extension of $k$. By the theorem of the primitive element, $k' = k[T]/(g)$ for an irreducible polynomial $g$. Since $\operatorname{char} k = 0$, the polynomial $g$ is separable: $g$ and $g'$ generate the unit ideal of $k[T]$. Let $B' = B \otimes_k k' = B[T]/(g)$. It is a free $B$-module of finite rank, so it is flat over $B$.

Let $\mathfrak{q}$ be a prime of $B'$ and let $\mathfrak{p} = \mathfrak{q} \cap B$. The fibre ring $B' \otimes_B \kappa(\mathfrak{p})$ is $L[T]/(g)$ with $L = \kappa(\mathfrak{p})$. The relation $ug + vg' = 1$ in $k[T]$ also holds in $L[T]$, so $g$ has no repeated factor in $L[T]$. By the Chinese remainder theorem, $L[T]/(g)$ is a finite product of fields. Its localization at the image of $\mathfrak{q}$ is a field, so $\mathfrak{p}B'_\mathfrak{q}$ is the maximal ideal of $B'_\mathfrak{q}$. The local homomorphism $B_\mathfrak{p} \to B'_\mathfrak{q}$ is flat, and its closed fibre has dimension $0$. By the dimension formula for flat local homomorphisms [Mat, Theorem 15.1], $\dim B'_\mathfrak{q} = \dim B_\mathfrak{p}$. Let $d = \dim B_\mathfrak{p}$. Since $B_\mathfrak{p}$ is regular, $\mathfrak{p}B_\mathfrak{p}$ has $d$ generators, so the maximal ideal $\mathfrak{p}B'_\mathfrak{q}$ also has $d$ generators. Thus $B'_\mathfrak{q}$ is regular. $\square$

**Example 5.1.3.** Let $p$ be a prime, let $k = \mathbb{F}_p(t)$ and let $k' = k(a)$ with $a^p = t$. The field $k'$ is a regular ring, but it is not geometrically regular over $k$. Indeed, $k' \otimes_k k' = k'[T]/(T^p - t) = k'[T]/((T - a)^p)$. This is a local ring of dimension $0$ whose maximal ideal $(T - a)$ is not $0$. So it is not a field, and it is not regular (Example 1.2.2).

### Regular homomorphisms and formal fibres

**Definition 5.1.4.** A homomorphism $\varphi : A \to B$ of Noetherian rings is *regular* if it is flat and, for each prime $\mathfrak{p}$ of $A$, the fibre $B \otimes_A \kappa(\mathfrak{p})$ is geometrically regular over $\kappa(\mathfrak{p})$.

**Definition 5.1.5.** Let $(A, \mathfrak{m})$ be a Noetherian local ring. For a prime $\mathfrak{p}$ of $A$, the ring $\hat{A} \otimes_A \kappa(\mathfrak{p})$ is the *formal fibre* of $A$ at $\mathfrak{p}$. A Noetherian ring $A$ is a *G-ring* if, for each prime $\mathfrak{p}$ of $A$, the map $A_\mathfrak{p} \to \widehat{A_\mathfrak{p}}$ is regular. Since this map is flat (Theorem 4.2.7), $A$ is a G-ring if and only if the formal fibres of each local ring $A_\mathfrak{p}$ are geometrically regular.

The formal fibre at $\mathfrak{m}$ is $\hat{A}/\mathfrak{m}\hat{A} = \kappa$, a field. It is geometrically regular, because $\kappa \otimes_\kappa k' = k'$ is a field. So only the primes $\mathfrak{p} \ne \mathfrak{m}$ matter. A field is a G-ring, since its only local ring is the field itself, which is complete. In Example 4.3.5, the completion $\hat{R}$ of the local ring $R$ of the node has two minimal primes $(y - xu)$ and $(y + xu)$. Both lie over the prime $0$ of $R$. So the generic formal fibre $\hat{R} \otimes_R \operatorname{Frac}(R)$ has two minimal primes, and it is not a domain.

**Proposition 5.1.6.** Let $A$ be a Dedekind domain whose field of fractions $K$ has characteristic $0$. Then $A$ is a G-ring. In particular, $\mathbb{Z}$ is a G-ring, and $k[x]$ is a G-ring for each field $k$ of characteristic $0$.

Lean: `Singularity.Algebra.isRegularAlgebra_adicCompletion_bot`, `Singularity.Algebra.isGRing_of_field` (the step at the prime 0, and the case of a field). The generic formal fibre of a discrete valuation ring is not in Lean yet.

*Proof.* The localization of $A$ at the prime $0$ is the field $K$, which is a G-ring. Let $\mathfrak{p} \ne 0$ be a prime. Then $R = A_\mathfrak{p}$ is a discrete valuation ring, so it is a regular local ring of dimension $1$ (Example 1.2.2). By Theorem 4.3.3, $\hat{R}$ is a regular local ring of dimension $1$. So $\hat{R}$ is a domain (Theorem 1.3.3), and it is a discrete valuation ring (Section 1.4). Let $t$ generate the maximal ideal of $R$. Then $t$ also generates the maximal ideal of $\hat{R}$, by Proposition 4.3.1. The ring $R$ has two primes, $0$ and $\mathfrak{p}R$. The formal fibre at $\mathfrak{p}R$ is the field $R/\mathfrak{p}R$, which is geometrically regular. The formal fibre at $0$ is $\hat{R} \otimes_R K = \hat{R}[1/t]$. Each nonzero element of $\hat{R}$ is a unit times a power of $t$, so $\hat{R}[1/t]$ is the field of fractions of $\hat{R}$. It is a field that contains $K$, so it has characteristic $0$. By Proposition 5.1.2, it is geometrically regular over $K$. $\square$

The hypothesis on the characteristic is necessary. Nagata gave a discrete valuation ring of characteristic $p$ whose generic formal fibre is not geometrically regular (Example 5.3.7).

### Stability

The G-ring property passes to the rings that occur in geometry. The proof of the next theorem is long, and we do not give it.

**Theorem 5.1.7 (Grothendieck).** In parts 1 to 3, let $A$ be a G-ring.

1. Each localization $S^{-1}A$ and each quotient $A/I$ is a G-ring.
2. Each finitely generated $A$-algebra is a G-ring.
3. If $A$ is local, then $A$ is reduced if and only if $\hat{A}$ is reduced, and $A$ is normal if and only if $\hat{A}$ is normal.
4. A complete Noetherian local ring is a G-ring.

Lean: `Singularity.Algebra.isRegularAlgebra_adicCompletion` (part 4 for the map to the completion of a complete ring). Parts 1 to 3 are not in Lean yet.

For the proofs see [EGA4-7] and [Mat, Section 32]. Part 1 follows from the definitions, because the local rings of $S^{-1}A$ and $A/I$ are localizations and quotients of local rings of $A$, and the formal fibres of a quotient are formal fibres of $A$. Part 2 is the hard part. Part 4 is also hard: the ring $\hat{A} = A$ has trivial formal fibres, but its localizations $A_\mathfrak{p}$ are not complete. By Proposition 5.1.6 and part 2, each algebra of finite type over $\mathbb{Z}$, or over any field, is a G-ring. Part 3 fails for the property of being a domain. The local ring of the node is a G-ring by parts 1 and 2, but its completion is not a domain (Example 4.3.5).

### Notes and references

Geometric regularity is in [EGA4, Section 6], and the formal fibres and G-rings are in [EGA4-7, Section 7]. Matsumura treats regular homomorphisms and G-rings in [Mat, Section 32]. Theorem 4.3.3 is the case of the closed point of the following general fact: if $A \to B$ is a flat local homomorphism of Noetherian local rings, $B$ regular implies $A$ regular, and $A$ regular with a regular closed fibre implies $B$ regular [Mat, Theorem 23.7]. The proof of Proposition 5.1.2 is a special case of this fact.
