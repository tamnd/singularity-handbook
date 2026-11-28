---
title: Excellence and resolution
nodes: [SG0000000K, SG0000001V]
sources: [EGA4-7, Nag62, Tem08, Lip78, CP19, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Excellence and resolution

This section relates excellence to resolution of singularities. Openness of the regular locus is a necessary condition for resolution, and it holds for quasi-excellent schemes (Theorem 5.3.3). Grothendieck proved that resolution for all integral schemes of finite type over a Noetherian scheme $X$ implies that $X$ is quasi-excellent (Theorem 5.3.6). The example of Nagata at the end of the section is a discrete valuation ring that is not quasi-excellent.

### Quasi-excellent schemes

**Definition 5.3.1.** A locally Noetherian scheme $X$ is *locally quasi-excellent* if each point of $X$ has an affine open neighbourhood $\operatorname{Spec} A$ with $A$ quasi-excellent. It is *locally excellent* if each point has such a neighbourhood with $A$ excellent. A scheme is *quasi-excellent* or *excellent* if it is Noetherian and locally quasi-excellent or locally excellent.

By Theorem 5.2.8, part 2, a scheme locally of finite type over a locally quasi-excellent scheme is locally quasi-excellent, and the same holds for excellent. For a scheme $X$, the *regular locus* $\operatorname{Reg}(X)$ is the set of the points $x$ such that $\mathcal{O}_{X,x}$ is a regular local ring. If $X = \operatorname{Spec} A$, then $\operatorname{Reg}(X) = \operatorname{Reg}(A)$.

**Proposition 5.3.2.** Let $X$ be a locally quasi-excellent scheme. Then $\operatorname{Reg}(X)$ is open in $X$.

Lean: `Singularity.regularLocus_isOpen_of_isJ2_cover` (with J-2 in place of quasi-excellent; a quasi-excellent ring is J-2)

*Proof.* Let $x \in X$ and let $U = \operatorname{Spec} A$ be an affine open neighbourhood of $x$ with $A$ quasi-excellent. The ring $A$ is J-2, and $A$ is a finitely generated $A$-algebra, so $A$ is J-1. Thus $\operatorname{Reg}(A)$ is open in $U$. For $y \in U$ with prime $\mathfrak{p}_y$, the local ring $\mathcal{O}_{X,y}$ is $A_{\mathfrak{p}_y}$, so $\operatorname{Reg}(X) \cap U = \operatorname{Reg}(A)$. Since such sets $U$ cover $X$, the set $\operatorname{Reg}(X)$ is open. $\square$

The proposition is a direct consequence of the definition. The real content is in the examples of Theorem 5.2.8: the rings that occur in geometry are quasi-excellent. The next theorem collects the cases that matter for resolution.

**Theorem 5.3.3.** Let $A$ be a quasi-excellent ring, for example a field, the ring $\mathbb{Z}$ or a complete Noetherian local ring. Let $X$ be a scheme locally of finite type over $A$. Then $\operatorname{Reg}(X)$ is open in $X$. In particular, the regular locus of a variety over any field is open.

Node: SG0000000K · Lean: `Singularity.regularLocus_isOpen_of_field`, `Singularity.regularLocus_isOpen_of_isJ2` (with J-2 in place of quasi-excellent)

*Proof.* The scheme $X$ is covered by affine open sets $\operatorname{Spec} B$ with $B$ a finitely generated $A$-algebra. Since $A$ is J-2, each such $B$ is J-1. Now argue as in the proof of Proposition 5.3.2. The rings in the list are quasi-excellent by Theorem 5.2.8. $\square$

The proof uses Theorem 5.2.8, which this volume does not prove. For a field $k$ of characteristic $0$ the theorem is proved in Section 1.8: it is Theorem 1.8.12. In Lean it is `Singularity.regularLocus_isOpen_of_charZero`, and its proof uses the criterion of Nagata (Theorem 1.7.7, `Singularity.Algebra.isOpen_regularLocus_of_exists_isOpen`) and generic regularity in characteristic $0$ (Theorem 1.8.9). For a perfect field $k$ the theorem is Theorem 1.8.17, and in Lean it is `Singularity.regularLocus_isOpen_of_perfectField`. For an arbitrary field $k$ the theorem is Theorem 1.9.5, and in Lean it is `Singularity.regularLocus_isOpen_of_field`. Thus the node SG0000000K is proved for a field. The other cases of Theorem 5.3.3, for example $A = \mathbb{Z}$ or a complete local ring, are not yet proved in Lean.

### Resolution implies openness

Volume 0 defines a resolution of a scheme $X$ as a proper morphism $\pi : Y \to X$ with $Y$ regular that is an isomorphism over $\operatorname{Reg}(X)$, and the definition asks that $\operatorname{Reg}(X)$ is open (Volume 0, Definition 2.1.5). Thus the existence of a resolution in this sense contains the openness of the regular locus. A weaker form of resolution still gives the openness, by the criterion of Nagata.

**Proposition 5.3.4.** Let $X$ be an integral locally Noetherian scheme. Assume that there are a regular scheme $Y$, a morphism $\pi : Y \to X$ and a nonempty open set $V \subseteq X$ such that $\pi^{-1}(V) \to V$ is an isomorphism. Then $\operatorname{Reg}(X)$ contains a nonempty open set.

Lean: `Singularity.subset_regularLocus_of_isIso_restrict` (the Lean form does not ask that $X$ is integral or locally Noetherian)

*Proof.* The set $\pi^{-1}(V)$ is open in $Y$, and each local ring of an open subscheme of $Y$ is a local ring of $Y$. So $\pi^{-1}(V)$ is a regular scheme. Since $V \cong \pi^{-1}(V)$, each local ring of $V$ is regular. Thus $V \subseteq \operatorname{Reg}(X)$. $\square$

**Corollary 5.3.5.** Let $A$ be a Noetherian ring. Assume that for each prime $\mathfrak{p}$ of $A$, the integral scheme $\operatorname{Spec} A/\mathfrak{p}$ has a morphism $\pi$ as in Proposition 5.3.4. Then $\operatorname{Reg}(A)$ is open. If the same holds for each finitely generated $A$-algebra in place of $A$, then $A$ is J-2.

Lean: `Singularity.isOpen_regularLocus_of_resolution`, `Singularity.isJ2_of_resolution`

*Proof.* By Proposition 5.3.4, for each prime $\mathfrak{p}$ the set $\operatorname{Reg}(A/\mathfrak{p})$ contains a nonempty open subset of $\operatorname{Spec} A/\mathfrak{p}$. By Theorem 1.7.7, $\operatorname{Reg}(A)$ is open. The second statement follows from the first, applied to each finitely generated $A$-algebra. $\square$

The proofs do not use that $\pi$ is proper. Grothendieck proved that resolution gives much more than the J-2 property.

**Theorem 5.3.6 (Grothendieck).** Let $X$ be a locally Noetherian scheme. Assume that for each integral scheme $X'$ of finite type over $X$ there is a proper birational morphism $Y \to X'$ with $Y$ regular. Then $X$ is locally quasi-excellent.

Lean: none yet

This is in [EGA4-7, Section 7.9], where Grothendieck states it with a weaker hypothesis: it is sufficient to ask for the resolution of the integral schemes $X'$ that are finite over $X$. We state the theorem in the form above, which follows from the statement of Grothendieck. The proof of the J-2 property is Corollary 5.3.5. The proof of the G-ring property is longer.

By Theorem 5.3.6, the quasi-excellent schemes form the largest class of locally Noetherian schemes, stable under morphisms of finite type, in which each integral scheme has a resolution. Grothendieck suggested that each quasi-excellent scheme has a resolution [EGA4-7, Section 7.9]. This is known in these cases:

1. reduced quasi-excellent schemes of characteristic $0$, that is, over $\mathbb{Q}$, by Temkin [Tem08];
2. reduced excellent schemes of dimension $2$, by Lipman [Lip78];
3. reduced quasi-excellent schemes of dimension at most $3$, also in mixed characteristic, by Cossart and Piltant [CP19].

The third case is the node SG0000001V of the map. Its Lean statement is planned. In general, the problem is open. Volume 0 describes the open cases.

### The example of Nagata

**Example 5.3.7 (Nagata).** Let $k$ be a field of characteristic $p > 0$ with $[k : k^p] = \infty$, for example $k = \mathbb{F}_p(t_1, t_2, \dots)$. Let $B = k^p[[x]]$ and let $R = B[k]$ be the subring of $k[[x]]$ generated by $B$ and $k$. Then $R$ is a discrete valuation ring with completion $k[[x]]$, and its generic formal fibre is not geometrically regular. So $R$ is not a G-ring, and $R$ is not quasi-excellent.

*Proof.* For a finite extension $L$ of $k^p$ inside $k$, the subring $B[L]$ of $k[[x]]$ is $L[[x]]$. Indeed, take a basis $e_1, \dots, e_m$ of $L$ over $k^p$. Each element of $L[[x]]$ is a sum $\sum_i e_i g_i$ with $g_i \in k^p[[x]]$, so $L[[x]] \subseteq B[L]$, and the other inclusion is clear. Each element of $k$ lies in such a field $L$, so $R$ is the union of the rings $L[[x]]$.

Let $a \in R$ be nonzero, and take $L$ with $a \in L[[x]]$. Then $a = x^n u$ with $u$ a unit of $L[[x]]$, so $u$ is a unit of $R$. Thus each nonzero element of $R$ is a unit times a power of $x$, and each nonzero ideal of $R$ is $(x^n)$ for some $n$. So $R$ is a discrete valuation ring with uniformizer $x$. If $a \in R$ lies in $x^n k[[x]]$, then the exponent above is at least $n$, so $a \in x^n R$. Thus $R/x^n R$ is a subring of $k[[x]]/(x^n)$. It contains $k$ and $x$, so $R/x^n R = k[x]/(x^n)$, and $\hat{R} = \varprojlim k[x]/(x^n) = k[[x]]$.

Let $K = R[1/x]$ be the field of fractions of $R$. Since $[k : k^p] = \infty$, we can choose $b_1, b_2, \dots \in k$ such that $b_{i+1} \notin k^p(b_1, \dots, b_i)$ for each $i$. Let $f = \sum_i b_i x^i \in k[[x]]$. Each element of $K$ lies in $L((x))$ for some finite extension $L$ of $k^p$, and then its coefficients lie in $L$. The degrees $[k^p(b_1, \dots, b_i) : k^p]$ have no bound, so no finite extension $L$ contains all the $b_i$. Thus $f \notin K$. But $f^p = \sum_i b_i^p x^{ip}$ lies in $B \subseteq R$.

Let $c = f^p \in K$. Since $f \notin K$, the polynomial $T^p - c$ has no root in $K$, so it is irreducible over $K$, and $K' = K[T]/(T^p - c)$ is a finite field extension of $K$. The generic formal fibre of $R$ is $F = \hat{R} \otimes_R K = k[[x]][1/x] = k((x))$. Then
$$F \otimes_K K' = F[T]/(T^p - c) = F[T]/((T - f)^p),$$
because $f \in F$ and $\operatorname{char} F = p$. The element $T - f$ is nilpotent and not $0$. So $F \otimes_K K'$ is not reduced, and it is not a regular ring. Thus $F$ is not geometrically regular over $K$. $\square$

The ring $R$ in Example 5.3.7 is regular, so $\operatorname{Spec} R$ is its own resolution. By Theorem 5.3.6, some integral scheme of finite type over $\operatorname{Spec} R$ has no resolution. Nagata used this ring and rings built from it to give examples of bad Noetherian rings, among them rings whose normalization is not finite [Nag62, Appendix].

We now show that the field $K'$ of Example 5.3.7 gives such a ring. We keep the notation of the example: $f = \sum_i b_i x^i$, $c = f^p \in R$, $F = k((x))$, and $K' = K(f) \subseteq F$. The map $K[T]/(T^p - c) \to K'$ with $T \mapsto f$ is an isomorphism, because $T^p - c$ is irreducible over $K$.

**Proposition 5.3.8.** Let $R'$ be the integral closure of $R$ in $K'$. Then $R'$ is not a finite $R$-module.

Lean: `Singularity.Algebra.tmul_sub_tmul_pow_eq_zero`, `Singularity.Algebra.tmul_eq_tmul_of_isReduced` (step 3 of the proof). Steps 1 and 2 are not in Lean yet.

*Proof.* Assume that $R'$ is a finite $R$-module. We derive a contradiction in three steps.

*Step 1. $R'$ is a discrete valuation ring.* The ring $R'$ is a finite module over the Noetherian ring $R$, so it is Noetherian. It is a domain, and it is integral over $R$, so $\dim R' = \dim R = 1$ [AM69, Corollary 5.9 and Theorem 5.11]. Let $y \in R'$. Then $y^p \in K$, because $K'^p = K^p(c) \subseteq K$, and $y^p$ is integral over $R$. The ring $R$ is a discrete valuation ring, so it is integrally closed, and $y^p \in R$. Let $\mathfrak{Q}$ be a maximal ideal of $R'$. Then $\mathfrak{Q} \cap R = xR$ [AM69, Corollary 5.8], and $y \in \mathfrak{Q}$ if and only if $y^p \in xR$, because $\mathfrak{Q}$ is prime. So $\mathfrak{Q}$ is the set of the $y$ with $y^p \in xR$, and $R'$ has only one maximal ideal. Thus $R'$ is a Noetherian local domain of dimension $1$, and it is integrally closed. By Theorem 1.4.2, $R'$ is a discrete valuation ring. Let $\pi$ be a uniformizer. Then $xR' = \pi^e R'$ for some $e \ge 1$.

*Step 2. $R' \otimes_R \hat{R}$ is a domain.* By Theorem 4.2.6, with $I = xR$, the natural map $R' \otimes_R \hat{R} \to \varprojlim_n R'/x^n R'$ is an isomorphism. It is a homomorphism of rings. Since $x^n R' = \pi^{en} R'$, the system $(R'/x^n R')$ is the subsystem of $(R'/\pi^m R')$ for the indices $m = en$. These indices are cofinal, so the two limits are the same. Thus $R' \otimes_R \hat{R}$ is isomorphic to the completion of the local ring $R'$ at its maximal ideal. This completion is a regular local ring by Theorem 4.3.3, so it is a domain by Theorem 1.3.3.

*Step 3. A nilpotent element.* The element $f$ is in $R'$, because $f^p = c \in R$. It is also in $\hat{R} = k[[x]]$. Let $z = f \otimes 1 - 1 \otimes f$ in $R' \otimes_R \hat{R}$. Then $z^p = c \otimes 1 - 1 \otimes c = 0$, because the ring has characteristic $p$ and $c \in R$. We show that $z \ne 0$. The module $\hat{R}$ is flat over $R$ by Theorem 4.2.7, so the inclusion $R' \subseteq K'$ gives an injective map $R' \otimes_R \hat{R} \to K' \otimes_R \hat{R}$. Also
$$K' \otimes_R \hat{R} = K' \otimes_K (K \otimes_R \hat{R}) = K' \otimes_K F = F[T]/(T^p - c).$$
The image of $z$ is the class of $T - f$. This class is not $0$, because the classes of $1, T, \dots, T^{p-1}$ are a basis of $F[T]/(T^p - c)$ over $F$. So $z$ is a nonzero nilpotent element of a domain. This is a contradiction. $\square$

**Example 5.3.9 (a normalization that is not finite).** Let $D = R[f] \subseteq K'$. Since $f$ is integral over $R$, the ring $D$ is a finite $R$-module, so $D$ is a Noetherian domain, and $\dim D = 1$ [AM69, Theorem 5.11]. Each $y \in D$ has $y^p \in R$, so the argument of Step 1 shows that $D$ is local. The field of fractions of $D$ is $K'$. An element of $K'$ is integral over $D$ if and only if it is integral over $R$, because $D$ is integral over $R$ [AM69, Corollary 5.4]. So the normalization of $D$ is $R'$. If $R'$ were a finite $D$-module, then it would be a finite $R$-module, since $D$ is a finite $R$-module. By Proposition 5.3.8, this is not the case.

Thus $D$ is a Noetherian local domain of dimension $1$ whose normalization is not finite. It is finite over the discrete valuation ring $R$. For $X = \operatorname{Spec} D$, the proof of Theorem 2.5.6 fails at Proposition 2.5.4: the normalization of $X$ is not a finite morphism. This does not show that $X$ has no resolution, and we do not claim it. The example shows that the theorem of Noether (Theorem 2.4.7) needs a hypothesis such as finite type over a field.

Lean: `Singularity.Algebra.not_finite_of_not_finite_of_finite` (the last step). The ring of Nagata is not in Lean yet.

### Notes and references

Theorem 5.3.3 for excellent rings is in [EGA4-7, Section 7.8], and the discussion of resolution and excellence is [EGA4-7, Section 7.9]. The example of Nagata is in [Nag62, Appendix]. Matsumura gives the excellent rings and examples of this kind in [Mat, Section 32]. The results of Temkin, Lipman, and Cossart and Piltant are the cases of the conjecture of Grothendieck that Volume 0 lists. The openness of the regular locus of a variety over any field is in the Lean library of the project (Theorem 1.9.5), so the node SG0000000K is proved. Its case of characteristic $0$ is Theorem 1.8.12.
