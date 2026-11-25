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

Lean: none yet

*Proof.* Let $P$ be a nonzero $A$-module and let $x \in P$ be nonzero. Then $Ax \cong A/J$ for an ideal $J \subseteq \mathfrak{m}$. By flatness, $B \otimes_A Ax \cong B/JB$ is a submodule of $B \otimes_A P$, and $B/JB \ne 0$ because $JB \subseteq \mathfrak{m}B \subseteq \mathfrak{n}$. So $B \otimes_A P \ne 0$. As in Proposition 4.3.2, this shows that a sequence of $A$-modules is exact if it is exact after the tensor product with $B$. Now apply $B \otimes_A -$ to the map $\varphi : A \to B$. The result is the map $B \to B \otimes_A B$, $b \mapsto b \otimes 1$, and it has a left inverse, the multiplication $B \otimes_A B \to B$. So it is injective, and $\varphi$ is injective.

For the last statement, let $\mathfrak{p}$ be a prime of $R$. By Lemma 6.4.2 below, the Frobenius of $R_\mathfrak{p}$ is flat. It is a local homomorphism, so it is injective by the first part. By Proposition 6.1.3, $R_\mathfrak{p}$ is reduced. A ring whose local rings are reduced is reduced, because a nilpotent element is $0$ in each local ring. So its annihilator is not in any prime, and it is the unit ideal. $\square$

**Lemma 6.4.2.** Let $R$ be a ring of characteristic $p$. Then the Frobenius of $R$ is flat if and only if the Frobenius of $R_\mathfrak{p}$ is flat for each prime $\mathfrak{p}$ of $R$.

Lean: none yet

*Proof.* Let $\mathfrak{p}$ be a prime and $S = R \setminus \mathfrak{p}$. The localization $(F_* R)_\mathfrak{p} = S^{-1}(F_* R)$ inverts the action of each $s \in S$ on $F_* R$, which is the multiplication by $s^p$. To invert $s^p$ is the same as to invert $s$. So $(F_* R)_\mathfrak{p}$ is the ring $R_\mathfrak{p}$, with the $R_\mathfrak{p}$-module structure that the Frobenius of $R_\mathfrak{p}$ gives. That is, $(F_* R)_\mathfrak{p} = F_*(R_\mathfrak{p})$. A module $M$ over $R$ is flat if and only if $M_\mathfrak{p}$ is flat over $R_\mathfrak{p}$ for each prime $\mathfrak{p}$ [AM69, Proposition 3.10]. $\square$

### Power series

To prove that the Frobenius of $K[[x_1, \dots, x_n]]$ is flat for an imperfect field $K$, we need a criterion of flatness by reduction modulo the powers of an ideal.

**Lemma 6.4.3.** Let $A \to B$ be a homomorphism of Noetherian rings, and let $I$ be an ideal of $A$ such that $IB$ is in the Jacobson radical of $B$. Assume that $B/I^nB$ is a flat $A/I^n$-module for each $n \ge 1$. Then $B$ is a flat $A$-module.

Lean: none yet

*Proof.* By [AM69, Proposition 2.19], it is sufficient to show that $N \otimes_A B \to M \otimes_A B$ is injective for each inclusion $N \subseteq M$ of finitely generated $A$-modules. Let $z$ be in the kernel. Fix $n$. The map $N/(I^n M \cap N) \to M/I^n M$ is injective, and both are $A/I^n$-modules. For an $A/I^n$-module $Q$ we have $Q \otimes_A B = Q \otimes_{A/I^n} B/I^nB$. Since $B/I^nB$ is flat over $A/I^n$, the map
$$N/(I^n M \cap N) \otimes_A B \to M/I^n M \otimes_A B$$
is injective. The image of $z$ in $M/I^nM \otimes_A B$ is $0$, so the image of $z$ in $N/(I^nM \cap N) \otimes_A B$ is $0$. By the right exactness of the tensor product, $z$ is in the image of $(I^n M \cap N) \otimes_A B$ in $N \otimes_A B$. By Corollary 4.1.6 there is $c$ with $I^n M \cap N \subseteq I^{n-c} N$ for $n \ge c$. So $z \in I^{n-c}(N \otimes_A B)$ for each $n \ge c$. The module $N \otimes_A B$ is a finitely generated $B$-module, and $IB$ is in the Jacobson radical of $B$. By Corollary 4.1.8, $\bigcap_n I^n (N \otimes_A B) = 0$. Thus $z = 0$. $\square$

**Corollary 6.4.4.** Let $L \subseteq K$ be fields. Then $K[[y_1, \dots, y_n]]$ is a flat $L[[y_1, \dots, y_n]]$-module.

Lean: none yet

*Proof.* Let $A = L[[y_1, \dots, y_n]]$, $B = K[[y_1, \dots, y_n]]$ and $I = (y_1, \dots, y_n)A$. Both rings are Noetherian (Theorem 4.2.9 and Example 4.2.2), and $IB$ is the maximal ideal of the local ring $B$. By Example 4.2.2, $A/I^n$ is the free $L$-module on the monomials of degree less than $n$, and $B/I^nB$ is the free $K$-module on the same monomials. Thus $B/I^nB = K \otimes_L A/I^n$. The field $K$ is a free $L$-module, so $K \otimes_L A/I^n$ is a free $A/I^n$-module. By Lemma 6.4.3, $B$ is flat over $A$. $\square$

When $[K : L]$ is infinite, $K[[y]]$ is not $K \otimes_L L[[y]]$: the coefficients of an element of $K \otimes_L L[[y]]$ lie in a finite-dimensional $L$-subspace of $K$. This is the reason for Lemma 6.4.3.

**Proposition 6.4.5.** Let $K$ be a field of characteristic $p$ and let $S = K[[x_1, \dots, x_n]]$. Then the Frobenius of $S$ is flat.

Lean: none yet

*Proof.* The Frobenius maps $\sum_\alpha c_\alpha x^\alpha$ to $\sum_\alpha c_\alpha^p x^{p\alpha}$. So it is an isomorphism of $S$ onto the subring $S' = K^p[[x_1^p, \dots, x_n^p]]$. Under this isomorphism, the $S$-module $F_* S$ is the ring $S$ as an $S'$-module. So we must show that $S$ is flat over $S'$. Let $y_i = x_i^p$, and consider the rings
$$S' = K^p[[y_1, \dots, y_n]] \subseteq K[[y_1, \dots, y_n]] \subseteq K[[x_1, \dots, x_n]] = S.$$
The first inclusion is flat by Corollary 6.4.4, with $L = K^p$. The second inclusion is free, by Proposition 6.1.5 with $e = 1$. So the composite is flat. $\square$

### The theorem

**Lemma 6.4.6.** Let $A \to B \to C$ be homomorphisms of rings. Assume that $C$ is faithfully flat over $B$ and that $C$ is flat over $A$. Then $B$ is flat over $A$.

Lean: none yet

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

### Notes and references

The theorem is the main result of [Kunz69]. Our proof that a regular ring has a flat Frobenius follows the reduction to power series in that paper, and it uses the Cohen structure theorem of Section 4.4. In the case of an imperfect residue field, Theorem 4.4.7 uses the existence of coefficient fields from [Coh46], which this volume does not prove. Lemma 6.4.3 is a special case of the local criterion of flatness [Mat, Section 22]. Faithful flatness and Lemma 6.4.6 are in [Mat, Section 7]. The project has the node SG0000000N for the theorem. Its Lean statement is planned, and the Lean library of the project does not yet contain the results of this section.
