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

Lean: none yet

*Proof.* Let $x \in X$ and let $U = \operatorname{Spec} A$ be an affine open neighbourhood of $x$ with $A$ quasi-excellent. The ring $A$ is J-2, and $A$ is a finitely generated $A$-algebra, so $A$ is J-1. Thus $\operatorname{Reg}(A)$ is open in $U$. For $y \in U$ with prime $\mathfrak{p}_y$, the local ring $\mathcal{O}_{X,y}$ is $A_{\mathfrak{p}_y}$, so $\operatorname{Reg}(X) \cap U = \operatorname{Reg}(A)$. Since such sets $U$ cover $X$, the set $\operatorname{Reg}(X)$ is open. $\square$

The proposition is a direct consequence of the definition. The real content is in the examples of Theorem 5.2.8: the rings that occur in geometry are quasi-excellent. The next theorem collects the cases that matter for resolution.

**Theorem 5.3.3.** Let $A$ be a quasi-excellent ring, for example a field, the ring $\mathbb{Z}$ or a complete Noetherian local ring. Let $X$ be a scheme locally of finite type over $A$. Then $\operatorname{Reg}(X)$ is open in $X$. In particular, the regular locus of a variety over any field is open.

Node: SG0000000K · Lean: none yet

*Proof.* The scheme $X$ is covered by affine open sets $\operatorname{Spec} B$ with $B$ a finitely generated $A$-algebra. Since $A$ is J-2, each such $B$ is J-1. Now argue as in the proof of Proposition 5.3.2. The rings in the list are quasi-excellent by Theorem 5.2.8. $\square$

The proof uses Theorem 5.2.8, which this volume does not prove. For a field $k$ of characteristic $0$ the theorem is proved in Section 1.8: it is Theorem 1.8.12. In Lean it is `Singularity.regularLocus_isOpen_of_charZero`, and its proof uses the criterion of Nagata (Theorem 1.7.7, `Singularity.Algebra.isOpen_regularLocus_of_exists_isOpen`) and generic regularity in characteristic $0$ (Theorem 1.8.9). The other cases are not yet proved in Lean. In particular, the openness of the regular locus of a variety over a field of positive characteristic is not yet proved in Lean, and the node SG0000000K is still planned.

### Resolution implies openness

Volume 0 defines a resolution of a scheme $X$ as a proper morphism $\pi : Y \to X$ with $Y$ regular that is an isomorphism over $\operatorname{Reg}(X)$, and the definition asks that $\operatorname{Reg}(X)$ is open (Volume 0, Definition 2.1.5). Thus the existence of a resolution in this sense contains the openness of the regular locus. A weaker form of resolution still gives the openness, by the criterion of Nagata.

**Proposition 5.3.4.** Let $X$ be an integral locally Noetherian scheme. Assume that there are a regular scheme $Y$, a morphism $\pi : Y \to X$ and a nonempty open set $V \subseteq X$ such that $\pi^{-1}(V) \to V$ is an isomorphism. Then $\operatorname{Reg}(X)$ contains a nonempty open set.

Lean: none yet

*Proof.* The set $\pi^{-1}(V)$ is open in $Y$, and each local ring of an open subscheme of $Y$ is a local ring of $Y$. So $\pi^{-1}(V)$ is a regular scheme. Since $V \cong \pi^{-1}(V)$, each local ring of $V$ is regular. Thus $V \subseteq \operatorname{Reg}(X)$. $\square$

**Corollary 5.3.5.** Let $A$ be a Noetherian ring. Assume that for each prime $\mathfrak{p}$ of $A$, the integral scheme $\operatorname{Spec} A/\mathfrak{p}$ has a morphism $\pi$ as in Proposition 5.3.4. Then $\operatorname{Reg}(A)$ is open. If the same holds for each finitely generated $A$-algebra in place of $A$, then $A$ is J-2.

Lean: none yet

*Proof.* By Proposition 5.3.4, for each prime $\mathfrak{p}$ the set $\operatorname{Reg}(A/\mathfrak{p})$ contains a nonempty open subset of $\operatorname{Spec} A/\mathfrak{p}$. By Theorem 1.7.7, $\operatorname{Reg}(A)$ is open. The second statement follows from the first, applied to each finitely generated $A$-algebra. $\square$

The proofs do not use that $\pi$ is proper. Grothendieck proved that resolution gives much more than the J-2 property.

**Theorem 5.3.6 (Grothendieck).** Let $X$ be a locally Noetherian scheme. Assume that for each integral scheme $X'$ of finite type over $X$ there is a proper birational morphism $Y \to X'$ with $Y$ regular. Then $X$ is locally quasi-excellent.

Lean: none yet

This is in [EGA4-7, Section 7.9], where Grothendieck states it with a weaker hypothesis: it is sufficient to ask for the resolution of the integral schemes $X'$ that are finite over $X$. We state the theorem in the form above, which follows from the statement of Grothendieck. The proof of the J-2 property is Corollary 5.3.5. The proof of the G-ring property is longer.

By Theorem 5.3.6, the quasi-excellent schemes form the largest class of locally Noetherian schemes, stable under morphisms of finite type, in which each integral scheme has a resolution. Grothendieck suggested that each quasi-excellent scheme has a resolution [EGA4-7, Section 7.9]. This is known in these cases:

1. quasi-excellent schemes of characteristic $0$, that is, over $\mathbb{Q}$, by Temkin [Tem08];
2. excellent schemes of dimension $2$, by Lipman [Lip78];
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

### Notes and references

Theorem 5.3.3 for excellent rings is in [EGA4-7, Section 7.8], and the discussion of resolution and excellence is [EGA4-7, Section 7.9]. The example of Nagata is in [Nag62, Appendix]. Matsumura gives the excellent rings and examples of this kind in [Mat, Section 32]. The results of Temkin, Lipman, and Cossart and Piltant are the cases of the conjecture of Grothendieck that Volume 0 lists. In positive characteristic, the openness of the regular locus of a variety is not yet in the Lean library of the project, so the node SG0000000K remains planned. Its case of characteristic $0$ is Theorem 1.8.12.
