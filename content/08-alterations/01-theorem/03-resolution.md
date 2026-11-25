---
title: Alterations and resolution
nodes: [SG0000001K, SG0000001N]
sources: [dJ96, Tem17, ILO14]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Alterations and resolution

This section compares the theorem of de Jong with the problem of this handbook. The problem asks for a resolution of each variety of dimension 4 in characteristic $p$, in the sense of Volume 0, Definition 2.1.5. Theorem 1.2.1 gives a regular alteration $\varphi \colon X_1 \to X$. The alteration fails to be a resolution in two ways. Its degree $d$ can be greater than 1, and even when $d = 1$ the morphism need not be an isomorphism over the regular locus. We study the degree. When $d$ is prime to $p$ and $\varphi$ is finite, the structure sheaf of a normal $X$ is a direct summand of the direct image of the structure sheaf of $X_1$. When $p$ divides $d$, this fails in general, and the theorems of Gabber and Temkin in Chapter 3 show that the powers of $p$ are the only obstruction left by these methods.

### The trace

Let $A$ be a domain with fraction field $K$, and let $L$ be a finite extension of $K$ of degree $d$. For $b \in L$, the trace $\operatorname{Tr}_{L/K}(b)$ is the trace of the $K$-linear map $L \to L$, $x \mapsto bx$. It is $K$-linear, and $\operatorname{Tr}_{L/K}(a) = d a$ for $a \in K$.

**Lemma 1.3.1.** Let $A$ be a normal Noetherian domain with fraction field $K$, let $L/K$ be a finite extension, and let $b \in L$ be integral over $A$. Then $\operatorname{Tr}_{L/K}(b) \in A$.

Lean: none yet

*Proof.* Let $f \in K[T]$ be the minimal polynomial of $b$ over $K$, of degree $m$. In a splitting field of $f$, each root of $f$ is a conjugate of $b$, so it satisfies the same integral equation as $b$ and is integral over $A$. The coefficients of $f$ are polynomials in the roots, so they are integral over $A$, and they lie in $K$. Since $A$ is normal, the coefficients lie in $A$. The matrix of multiplication by $b$ on $K(b)$ in the basis $1, b, \dots, b^{m-1}$ is the companion matrix of $f$, so $\operatorname{Tr}_{K(b)/K}(b) = -c_{m-1}$, where $c_{m-1}$ is the coefficient of $T^{m-1}$. Choose a basis of $L$ over $K(b)$. In the basis of products, multiplication by $b$ is block diagonal with $[L : K(b)]$ copies of the companion matrix. So $\operatorname{Tr}_{L/K}(b) = -[L : K(b)] \, c_{m-1} \in A$. $\square$

**Proposition 1.3.2.** Let $\varphi \colon X' \to X$ be a finite alteration of degree $d$, with $X$ normal and Noetherian, and assume that $d$ is invertible on $X$. Then the map $\mathcal{O}_X \to \varphi_* \mathcal{O}_{X'}$ has an $\mathcal{O}_X$-linear left inverse.

Lean: none yet

*Proof.* Let $K = k(X)$ and $L = k(X')$, so $[L : K] = d$. For an affine open subset $\operatorname{Spec} A \subseteq X$, the ring $B = \Gamma(\varphi^{-1}(\operatorname{Spec} A), \mathcal{O}_{X'})$ is a domain finite over $A$ with fraction field $L$. Each element of $B$ is integral over $A$, so by Lemma 1.3.1 the map $s_A = \frac{1}{d} \operatorname{Tr}_{L/K}$ sends $B$ to $A$. It is $A$-linear, and $s_A(a) = a$ for $a \in A$. The maps $s_A$ are restrictions of the one map $\frac{1}{d} \operatorname{Tr}_{L/K} \colon L \to K$, so they agree on the overlaps and glue to a map $\varphi_* \mathcal{O}_{X'} \to \mathcal{O}_X$. $\square$

**Remark 1.3.3.** Two remarks show the limits of the proposition. First, if $p = \operatorname{char} K$ divides $d$, the proof fails, and if $L/K$ is inseparable it fails completely, because then $\operatorname{Tr}_{L/K} = 0$. Second, even when $d$ is prime to $p$, the splitting does not make $X$ regular. In Example 1.1.9, the ring $k[s^2, st, t^2]$ is a direct summand of $k[s, t]$ in each characteristic, by the map that keeps the monomials of even degree, but the cone is singular. The splitting passes some properties of $X'$ to $X$, but regularity is not one of them.

### The degree and the open problem

Theorem 1.2.1 gives no control of the degree. The proof of Chapter 2 makes alterations at many steps: normalizations in Galois extensions to make the components of $Z$ into sections, the finite étale covers of level structures, and the alterations of the induction hypothesis. Each of them multiplies the degree. If $k$ is perfect, each step is generically étale, but the degrees of these extensions can be divisible by $p$.

**Proposition 1.3.4.** Let $\varphi \colon X_1 \to X$ be an alteration of degree $d$ of an integral variety $X$ over a field $k$, with $X_1$ regular. If $d = 1$ and $\varphi$ is an isomorphism over $\operatorname{Reg}(X)$, then $\varphi$ is a resolution of $X$. If $d > 1$, then no nonempty open subset of $X_1$ maps isomorphically onto an open subset of $X$.

Lean: none yet

*Proof.* If $d = 1$ and $\varphi$ is an isomorphism over $\operatorname{Reg}(X)$, then $\varphi$ is proper, $X_1$ is regular, and $\varphi^{-1}(\operatorname{Reg}(X))$ is a nonempty open subset of the irreducible space $X_1$, so it is dense. These are the conditions of Volume 0, Definition 2.1.5. If an open subset of $X_1$ maps isomorphically onto an open subset of $X$, then the two function fields are isomorphic over $k(X)$, so $d = 1$. $\square$

The problem is therefore to remove the degree. There are two cases. If the extension $k(X_1)/k(X)$ is Galois with group $G$, then $X$ is birational to the quotient $X_1/G$ (Section 3.1), and one must resolve the quotient. If $|G|$ is prime to $p$, the action is tame, and the modification theorem of Gabber resolves such quotients by toroidal methods, in the setting of log regular schemes [ILO14] (Section 3.2). If $p$ divides $|G|$, the action can be wild, and no general method is known. Temkin's theorem (Section 3.3) makes the degree a power of $p$. So after the theorems of this volume, the part of the degree that no known method removes is a power of $p$, and for a Galois alteration it comes from a $p$-group, whose action is wild. This is route R6 of the map, and Volume 9, Section 2.3 records that nobody knows how to do this descent in dimension 4.

**Example 1.3.5.** In characteristic $p$, a purely inseparable alteration carries no information. Let $X$ be an integral variety over a perfect field $k$ of characteristic $p$, and let $F \colon X \to X$ be the absolute Frobenius, which is the identity on points and the $p$-th power on functions. It lies over the Frobenius of $\operatorname{Spec} k$. Let $X'$ be the scheme $X$ with the structure morphism composed with the Frobenius of $\operatorname{Spec} k$, which is an isomorphism because $k$ is perfect. Then $F$ is a $k$-morphism $X' \to X$. On function fields it is the inclusion $K^p \subseteq K$ with $K = k(X)$, and $[K : K^p] = p^{\dim X}$ for a function field over a perfect field. So $F$ is a finite alteration of degree $p^{\dim X}$, purely inseparable, and a homeomorphism. Its source is $X$ itself, so it is regular only when $X$ is regular. This shows that the purely inseparable part of an alteration does not help. In Theorem 1.2.1 over a perfect field, de Jong can choose $\varphi_1$ generically étale, so the degree is the degree of a separable extension.

### Notes and references

The introduction of [Tem17] explains that alterations of degree prime to $\ell$ extend the applications of de Jong's theorem to étale cohomology with coefficients in $\mathbb{Z}/\ell$ and $\mathbb{Z}_\ell$. A trace map as in Proposition 1.3.2 is the basic tool there. Nothing of this section is in Lean.
