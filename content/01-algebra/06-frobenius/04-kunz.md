---
title: The theorem of Kunz
nodes: [SG0000000N]
sources: [Kunz69, Mat, AM69, Coh46]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem of Kunz

The theorem of Kunz characterizes the regular rings of characteristic $p$ by a property of the Frobenius alone: a Noetherian ring of characteristic $p$ is regular if and only if its Frobenius is flat. This section proves that the Frobenius of a regular ring is flat. The proof reduces to a complete regular local ring, which is a ring of power series by the theorem of Cohen (Theorem 4.4.7). For the converse we refer to [Kunz69].

In this section, a homomorphism of rings $\varphi : A \to B$ is *flat* if $B$ is a flat $A$-module. The Frobenius $F$ of $R$ is flat if and only if the $R$-module $F_* R$ is flat. A composite of flat homomorphisms is flat.

### First properties

**Proposition 6.4.1.** Let $(A, \mathfrak{m}) \to (B, \mathfrak{n})$ be a flat local homomorphism of local rings. Then $B$ is faithfully flat over $A$, and the map $A \to B$ is injective. As a consequence, a Noetherian ring $R$ of characteristic $p$ with flat Frobenius is reduced.

Lean: `Singularity.Algebra.faithfullyFlat_and_injective_of_flat_of_isLocalHom`, `Singularity.Algebra.isReduced_of_flat_frobenius` (the last claim)

*Proof.* Let $P$ be a nonzero $A$-module and let $x \in P$ be nonzero. Then $Ax \cong A/J$ for an ideal $J \subseteq \mathfrak{m}$. By flatness, $B \otimes_A Ax \cong B/JB$ is a submodule of $B \otimes_A P$, and $B/JB \ne 0$ because $JB \subseteq \mathfrak{m}B \subseteq \mathfrak{n}$. So $B \otimes_A P \ne 0$. As in Proposition 4.3.2, this shows that a sequence of $A$-modules is exact if it is exact after the tensor product with $B$. Now apply $B \otimes_A -$ to the map $\varphi : A \to B$. The result is the map $B \to B \otimes_A B$, $b \mapsto b \otimes 1$, and it has a left inverse, the multiplication $B \otimes_A B \to B$. So it is injective, and $\varphi$ is injective.

For the last statement, let $\mathfrak{p}$ be a prime of $R$. By Lemma 6.4.2 below, the Frobenius of $R_\mathfrak{p}$ is flat. It is a local homomorphism, so it is injective by the first part. By Proposition 6.1.3, $R_\mathfrak{p}$ is reduced. A ring whose local rings are reduced is reduced, because a nilpotent element is $0$ in each local ring. So its annihilator is not in any prime, and it is the unit ideal. $\square$

The Lean proof of the last claim does not use the hypothesis that $R$ is Noetherian. It uses the equational criterion of flatness to show that $F$ is injective.

**Lemma 6.4.2.** Let $R$ be a ring of characteristic $p$. Then the Frobenius of $R$ is flat if and only if the Frobenius of $R_\mathfrak{p}$ is flat for each prime $\mathfrak{p}$ of $R$.

Lean: `Singularity.Algebra.flat_frobenius_iff_forall_localization`

*Proof.* Let $\mathfrak{p}$ be a prime and $S = R \setminus \mathfrak{p}$. The localization $(F_* R)_\mathfrak{p} = S^{-1}(F_* R)$ inverts the action of each $s \in S$ on $F_* R$, which is the multiplication by $s^p$. To invert $s^p$ is the same as to invert $s$. So $(F_* R)_\mathfrak{p}$ is the ring $R_\mathfrak{p}$, with the $R_\mathfrak{p}$-module structure that the Frobenius of $R_\mathfrak{p}$ gives. That is, $(F_* R)_\mathfrak{p} = F_*(R_\mathfrak{p})$. A module $M$ over $R$ is flat if and only if $M_\mathfrak{p}$ is flat over $R_\mathfrak{p}$ for each prime $\mathfrak{p}$ [AM69, Proposition 3.10]. $\square$

### Power series

To prove that the Frobenius of $K[[x_1, \dots, x_n]]$ is flat for an imperfect field $K$, we need a criterion of flatness by reduction modulo the powers of an ideal.

**Lemma 6.4.3.** Let $A \to B$ be a homomorphism of Noetherian rings, and let $I$ be an ideal of $A$ such that $IB$ is in the Jacobson radical of $B$. Assume that $B/I^nB$ is a flat $A/I^n$-module for each $n \ge 1$. Then $B$ is a flat $A$-module.

Lean: `Singularity.Algebra.flat_of_flat_quotient_pow` (with $(A/I^n) \otimes_A B$ in place of $B/I^nB$)

*Proof.* By [AM69, Proposition 2.19], it is sufficient to show that $N \otimes_A B \to M \otimes_A B$ is injective for each inclusion $N \subseteq M$ of finitely generated $A$-modules. Let $z$ be in the kernel. Fix $n$. The map $N/(I^n M \cap N) \to M/I^n M$ is injective, and both are $A/I^n$-modules. For an $A/I^n$-module $Q$ we have $Q \otimes_A B = Q \otimes_{A/I^n} B/I^nB$. Since $B/I^nB$ is flat over $A/I^n$, the map
$$N/(I^n M \cap N) \otimes_A B \to M/I^n M \otimes_A B$$
is injective. The image of $z$ in $M/I^nM \otimes_A B$ is $0$, so the image of $z$ in $N/(I^nM \cap N) \otimes_A B$ is $0$. By the right exactness of the tensor product, $z$ is in the image of $(I^n M \cap N) \otimes_A B$ in $N \otimes_A B$. By Corollary 4.1.6 there is $c$ with $I^n M \cap N \subseteq I^{n-c} N$ for $n \ge c$. So $z \in I^{n-c}(N \otimes_A B)$ for each $n \ge c$. The module $N \otimes_A B$ is a finitely generated $B$-module, and $IB$ is in the Jacobson radical of $B$. By Corollary 4.1.8, $\bigcap_n I^n (N \otimes_A B) = 0$. Thus $z = 0$. $\square$

**Corollary 6.4.4.** Let $L \subseteq K$ be fields. Then $K[[y_1, \dots, y_n]]$ is a flat $L[[y_1, \dots, y_n]]$-module.

Lean: `Singularity.Algebra.flat_mvPowerSeries_of_finiteDimensional` (when $[K : L]$ is finite)

*Proof.* Let $A = L[[y_1, \dots, y_n]]$, $B = K[[y_1, \dots, y_n]]$ and $I = (y_1, \dots, y_n)A$. Both rings are Noetherian (Theorem 4.2.9 and Example 4.2.2), and $IB$ is the maximal ideal of the local ring $B$. By Example 4.2.2, $A/I^n$ is the free $L$-module on the monomials of degree less than $n$, and $B/I^nB$ is the free $K$-module on the same monomials. Thus $B/I^nB = K \otimes_L A/I^n$. The field $K$ is a free $L$-module, so $K \otimes_L A/I^n$ is a free $A/I^n$-module. By Lemma 6.4.3, $B$ is flat over $A$. $\square$

When $[K : L]$ is infinite, $K[[y]]$ is not $K \otimes_L L[[y]]$: the coefficients of an element of $K \otimes_L L[[y]]$ lie in a finite-dimensional $L$-subspace of $K$. This is the reason for Lemma 6.4.3.

**Proposition 6.4.5.** Let $K$ be a field of characteristic $p$ and let $S = K[[x_1, \dots, x_n]]$. Then the Frobenius of $S$ is flat.

Lean: `Singularity.Algebra.frobenius_mvPowerSeries_finite_and_flat` (when $[K : K^p]$ is finite)

*Proof.* The Frobenius maps $\sum_\alpha c_\alpha x^\alpha$ to $\sum_\alpha c_\alpha^p x^{p\alpha}$. So it is an isomorphism of $S$ onto the subring $S' = K^p[[x_1^p, \dots, x_n^p]]$. Under this isomorphism, the $S$-module $F_* S$ is the ring $S$ as an $S'$-module. So we must show that $S$ is flat over $S'$. Let $y_i = x_i^p$, and consider the rings
$$S' = K^p[[y_1, \dots, y_n]] \subseteq K[[y_1, \dots, y_n]] \subseteq K[[x_1, \dots, x_n]] = S.$$
The first inclusion is flat by Corollary 6.4.4, with $L = K^p$. The second inclusion is free, by Proposition 6.1.5 with $e = 1$. So the composite is flat. $\square$

### The theorem

**Lemma 6.4.6.** Let $A \to B \to C$ be homomorphisms of rings. Assume that $C$ is faithfully flat over $B$ and that $C$ is flat over $A$. Then $B$ is flat over $A$.

Lean: `Singularity.Algebra.flat_of_faithfullyFlat_of_flat`

*Proof.* Let $N \to M$ be an injective map of $A$-modules, and let $Q$ be the kernel of $N \otimes_A B \to M \otimes_A B$. Since $C$ is flat over $B$, the module $Q \otimes_B C$ is the kernel of $N \otimes_A C \to M \otimes_A C$. This map is injective because $C$ is flat over $A$. So $Q \otimes_B C = 0$, and $Q = 0$ because $C$ is faithfully flat over $B$. $\square$

**Theorem 6.4.7 (Kunz).** Let $R$ be a Noetherian ring of characteristic $p$. Then $R$ is regular if and only if the Frobenius of $R$ is flat. In particular, a Noetherian local ring of characteristic $p$ is regular if and only if its Frobenius is flat.

Node: SG0000000N · Lean: `Singularity.isRegularLocalRing_iff_flat_frobenius` (planned, no Lean statement yet)

*Proof that a regular ring has a flat Frobenius.* By Lemma 6.4.2, it is sufficient to treat the local rings $R_\mathfrak{p}$, and they are regular local rings. So let $(R, \mathfrak{m}, \kappa)$ be a regular local ring of characteristic $p$ and dimension $d$, and let $\iota : R \to \hat{R}$ be its completion. By Theorem 4.3.3, $\hat{R}$ is a complete regular local ring of dimension $d$. It contains the field $\mathbb{F}_p$, so by Theorem 4.4.7, $\hat{R} \cong \kappa[[x_1, \dots, x_d]]$. By Proposition 6.4.5, the Frobenius $F_{\hat{R}}$ is flat.

The map $\iota$ commutes with the Frobenius: $\iota \circ F_R = F_{\hat{R}} \circ \iota$. The right side is a composite of flat maps, by Theorem 4.2.7 and the above. So the composite
$$R \xrightarrow{F_R} R \xrightarrow{\iota} \hat{R}$$
is flat. Here $\hat{R}$ is faithfully flat over the second copy of $R$, by Proposition 4.3.2. By Lemma 6.4.6, with $A = B = R$ and $C = \hat{R}$, the map $F_R$ is flat. $\square$

*The converse.* Kunz proved that a Noetherian local ring of characteristic $p$ with flat Frobenius is regular [Kunz69]. In his paper the lengths of the rings $R/\mathfrak{m}^{[q]}$ play the main role, where $\mathfrak{m}^{[q]}$ is the ideal generated by the $q$-th powers of the elements of $\mathfrak{m}$. We do not give the proof. With Lemma 6.4.2, the local case gives the case of a Noetherian ring.

**Remark 6.4.8.** Let $(R, \mathfrak{m}, \kappa)$ be a regular local ring of dimension $d$ and characteristic $p$. If $[\kappa : \kappa^p] = p^r$ is finite, then the proof of Proposition 6.4.5 shows that $F_* \hat{R}$ is a free $\hat{R}$-module of rank $p^{d + r}$: the ring $\kappa[[y]]$ is free of rank $p^r$ over $\kappa^p[[y]]$, because $\kappa$ is free of rank $p^r$ over $\kappa^p$, and $\kappa[[x]]$ is free of rank $p^d$ over $\kappa[[y]]$. For $\kappa$ perfect this is Corollary 6.1.6.

Lean: none yet

The theorem of Kunz is the start of the use of the Frobenius to measure singularities. If $R$ is not regular, then $F_* R$ is not flat, and the failure of flatness measures how far $R$ is from regular. Lemma 6.1.2 and Theorem 6.4.7 together say that, for a regular ring, the Frobenius is a flat map that does not change the points of the spectrum.

The next example shows, with a direct computation, that the Frobenius of the cusp is not flat. It does not use the converse of the theorem of Kunz.

**Example 6.4.9 (the Frobenius of the cusp).** Let $k$ be a perfect field of characteristic $p$, let $A = k[t^2, t^3] \subseteq k[t]$, let $\mathfrak{m} = (t^2, t^3)A$ and let $R = A_\mathfrak{m}$. Then the Frobenius of $R$ is not flat.

Lean: none yet

*Proof.* *Finiteness.* Since $k = k^p$, the image of the Frobenius of $A$ is $A^p = k[t^{2p}, t^{3p}]$. The ring $k[t]$ is a finite module over $k[t^{2p}]$, generated by $1, t, \dots, t^{2p-1}$. The ring $k[t^{2p}]$ is Noetherian, so its submodule $A$ is finite over $k[t^{2p}]$, and so it is finite over $A^p \supseteq k[t^{2p}]$. Thus $F_* A$ is a finite $A$-module. By the proof of Lemma 6.4.2, $F_* R = (F_* A)_\mathfrak{m}$, so $F_* R$ is a finite $R$-module.

*The generic rank.* Let $K = k(t)$ be the field of fractions of $A$. The proof of Lemma 6.4.2 also gives $F_* R \otimes_R K = F_* K$. As a $K$-vector space, $F_* K$ is $K$ over the subfield $K^p = k(t^p)$, and $[k(t) : k(t^p)] = p$, with the basis $1, t, \dots, t^{p-1}$. So $\dim_K (F_* R \otimes_R K) = p$.

*The fibre.* An element $a \in \mathfrak{m}$ acts on $F_* A$ by the multiplication by $a^p$. So $\mathfrak{m} F_* A$ is the ideal $(t^{2p}, t^{3p})A$ of the ring $A$. The ring $A$ has the $k$-basis $t^s$ with $s$ in $S = \{0, 2, 3, 4, \dots\}$, and $(t^{2p}, t^{3p})A$ has the basis $t^s$ with $s \in (2p + S) \cup (3p + S)$. The set $(2p + S) \cup (3p + S)$ contains each integer $s \ge 2p$ except $2p + 1$. So the quotient $A/(t^{2p}, t^{3p})A$ has the basis $t^s$ with $s \in \{0, 2, 3, \dots, 2p - 1\} \cup \{2p + 1\}$, and its dimension is $2p$. The field $k$ acts on $F_* A$ through the Frobenius, $\lambda \cdot a = \lambda^p a$. Since $k$ is perfect, $\lambda \mapsto \lambda^p$ is a bijection of $k$, so a $k$-basis for the usual action is also a $k$-basis for this action. The only prime of $A$ that contains $t^{2p}$ is $\mathfrak{m}$, so $A/(t^{2p}, t^{3p})A$ is a local ring with maximal ideal $\mathfrak{m}$, and the elements of $A \setminus \mathfrak{m}$ act on it as units. Thus $F_* R/\mathfrak{m}F_* R$ is this ring, and $\dim_k F_* R/\mathfrak{m} F_* R = 2p$.

*Conclusion.* Assume that $F_* R$ is flat over $R$. A finite flat module over a Noetherian local ring is free [Mat, Section 7]. Let $r$ be its rank. Then $r = \dim_k F_* R/\mathfrak{m} F_* R = 2p$, and $r = \dim_K (F_* R \otimes_R K) = p$. This is a contradiction. $\square$

The same count works for the node $xy = 0$. Let $R$ be the local ring of $k[x, y]/(xy)$ at the origin, with $k$ perfect. Then $F_* R/\mathfrak{m}F_* R$ is $k[x, y]/(xy, x^p, y^p)$, with the basis $1, x, \dots, x^{p-1}, y, \dots, y^{p-1}$, of dimension $2p - 1$. The localization of $R$ at the minimal prime $(y)$ is the field $k(x)$, and there $F_*$ has rank $[k(x) : k(x^p)] = p$. Since $2p - 1 \ne p$, the Frobenius of $R$ is not flat. In both examples, the dimension of the fibre exceeds the generic rank. As rings, $F_* R/\mathfrak{m}F_* R = R/\mathfrak{m}^{[p]}$, the ring that appears in the converse above. For the two curves its length is $2p$ and $2p - 1$. For the regular ring $k[x]_{(x)}$ it is $p$.

### Notes and references

The theorem is the main result of [Kunz69]. Our proof that a regular ring has a flat Frobenius follows the reduction to power series in that paper, and it uses the Cohen structure theorem of Section 4.4. In the case of an imperfect residue field, Theorem 4.4.7 uses the existence of coefficient fields from [Coh46], which this volume does not prove. Lemma 6.4.3 is a special case of the local criterion of flatness [Mat, Section 22]. Faithful flatness and Lemma 6.4.6 are in [Mat, Section 7]. The project has the node SG0000000N for the theorem. Its Lean statement is planned, and the Lean library of the project does not yet contain the results of this section.
