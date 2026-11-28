---
title: The completion of a local ring
nodes: [SG0000002Z]
sources: [AM69, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The completion of a local ring

Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring, and let $\hat{R}$ be its $\mathfrak{m}$-adic completion. This section proves that $\hat{R}$ is a Noetherian local ring with the same residue field, the same dimension and the same embedding dimension as $R$. Thus $R$ is regular if and only if $\hat{R}$ is regular (Theorem 4.3.3). The completion can lose a property that $R$ has: Example 4.3.5 gives a local domain whose completion is not a domain.

**Proposition 4.3.1.** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring. Then:

1. $\hat{R}$ is a Noetherian local ring with maximal ideal $\hat{\mathfrak{m}} = \mathfrak{m}\hat{R}$ and residue field $\kappa$.
2. The map $R \to \hat{R}$ is injective.
3. For each ideal $J$ of $R$, $J\hat{R} \cap R = J$, and $\hat{R}/J\hat{R}$ is the completion of $R/J$.

Lean: `Singularity.Algebra.adicCompletion_isLocalRing` (parts 1 and 2, without the claim that $\hat{R}$ is Noetherian)

*Proof.* For 1, $\hat{R}$ is Noetherian by Theorem 4.2.9. By Proposition 4.2.8, $\hat{R}/\mathfrak{m}\hat{R} \cong R/\mathfrak{m} = \kappa$, so $\mathfrak{m}\hat{R}$ is a maximal ideal. It is in the Jacobson radical of $\hat{R}$, by Proposition 4.2.8. So it is the only maximal ideal. For 2, the kernel of $R \to \hat{R}$ is $\bigcap_n \mathfrak{m}^n$, and this is $0$ by Corollary 4.1.8. For 3, apply Proposition 4.2.5 and Theorem 4.2.6 to the sequence $0 \to J \to R \to R/J \to 0$. They give that the completion of $R/J$ is $\hat{R}/J\hat{R}$. The completion of $R/J$ as an $R$-module is its completion as a local ring, because $\mathfrak{m}^n (R/J)$ is the $n$-th power of the maximal ideal of $R/J$. By 2, applied to the Noetherian local ring $R/J$, the map $R/J \to \hat{R}/J\hat{R}$ is injective. This says that $J\hat{R} \cap R = J$. $\square$

**Proposition 4.3.2.** Let $(R, \mathfrak{m})$ be a Noetherian local ring. Then $\hat{R}$ is a faithfully flat $R$-module: for each $R$-module $P$, $\hat{R} \otimes_R P = 0$ implies $P = 0$. Thus a sequence of $R$-modules is exact if it is exact after the tensor product with $\hat{R}$.

Lean: `Singularity.Algebra.faithfullyFlat_adicCompletion` (faithful flatness, without the last sentence on exact sequences)

*Proof.* The module $\hat{R}$ is flat by Theorem 4.2.7. Let $P \ne 0$, and let $x \in P$ be a nonzero element. The submodule $Rx$ is isomorphic to $R/J$ for an ideal $J \ne R$. By flatness, $\hat{R} \otimes_R Rx \cong \hat{R}/J\hat{R}$ is a submodule of $\hat{R} \otimes_R P$. Since $J \subseteq \mathfrak{m}$, the ring $\hat{R}/J\hat{R}$ maps onto $\hat{R}/\mathfrak{m}\hat{R} = \kappa \ne 0$. Thus $\hat{R} \otimes_R P \ne 0$. For the last statement, let $N \to M \to P$ be a sequence with composite $0$, and let $H$ be its homology at $M$. By flatness, $\hat{R} \otimes_R H$ is the homology of the sequence after the tensor product with $\hat{R}$. If this homology is $0$, then $H = 0$. $\square$

**Theorem 4.3.3.** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring with completion $(\hat{R}, \hat{\mathfrak{m}})$. Then $\operatorname{edim} \hat{R} = \operatorname{edim} R$ and $\dim \hat{R} = \dim R$. In particular, $R$ is regular if and only if $\hat{R}$ is regular.

Node: SG0000002Z · Lean: `Singularity.Algebra.ringKrullDim_adicCompletion`, `Singularity.Algebra.spanFinrank_maximalIdeal_adicCompletion`, `Singularity.Algebra.isRegularLocalRing_adicCompletion_iff`

*Proof.* By Proposition 4.2.8, $\hat{R}/\hat{\mathfrak{m}}^2 = \hat{R}/\mathfrak{m}^2\hat{R} \cong R/\mathfrak{m}^2$, and this isomorphism maps $\hat{\mathfrak{m}}/\hat{\mathfrak{m}}^2$ onto $\mathfrak{m}/\mathfrak{m}^2$. Thus the two ideals have the same dimension over $\kappa$, so the embedding dimensions are equal.

For the dimension we use the dimension theorem, Theorem 1.1.2: the dimension of a Noetherian local ring is the least number of elements that generate an ideal primary to the maximal ideal. Let $d = \dim R$ and let $x_1, \dots, x_d$ generate an $\mathfrak{m}$-primary ideal $\mathfrak{q}$. Then $\mathfrak{m}^n \subseteq \mathfrak{q}$ for some $n$, so $\hat{\mathfrak{m}}^n = \mathfrak{m}^n \hat{R} \subseteq \mathfrak{q}\hat{R}$. Thus $\mathfrak{q}\hat{R}$ is $\hat{\mathfrak{m}}$-primary, and $\dim \hat{R} \le d$.

Conversely, let $e = \dim \hat{R}$ and let $y_1, \dots, y_e$ generate an $\hat{\mathfrak{m}}$-primary ideal of $\hat{R}$. Take $n$ with $\hat{\mathfrak{m}}^n \subseteq (y_1, \dots, y_e)$. By Proposition 4.2.8 the map $R \to \hat{R}/\hat{\mathfrak{m}}^{n+1}$ is surjective, so there are $x_i \in R$ with $y_i - x_i \in \hat{\mathfrak{m}}^{n+1}$. Let $\mathfrak{q} = (x_1, \dots, x_e) \subseteq R$. Then
$$\hat{\mathfrak{m}}^n \subseteq (y_1, \dots, y_e) \subseteq \mathfrak{q}\hat{R} + \hat{\mathfrak{m}}^{n+1} \subseteq \mathfrak{q}\hat{R} + \hat{\mathfrak{m}} \cdot \hat{\mathfrak{m}}^n.$$
Apply the lemma of Nakayama to the finitely generated module $(\mathfrak{q}\hat{R} + \hat{\mathfrak{m}}^n)/\mathfrak{q}\hat{R}$. It gives $\hat{\mathfrak{m}}^n \subseteq \mathfrak{q}\hat{R}$. Thus $\mathfrak{m}^n \subseteq \mathfrak{m}^n\hat{R} \cap R \subseteq \mathfrak{q}\hat{R} \cap R = \mathfrak{q}$, by Proposition 4.3.1. So $\mathfrak{q}$ is $\mathfrak{m}$-primary, and $d \le e$.

The ring $R$ is regular if and only if $\operatorname{edim} R = \dim R$, and the same holds for $\hat{R}$. Both numbers are the same for $R$ and $\hat{R}$. $\square$

**Corollary 4.3.4.** Let $k$ be a field and let $A = k[x_1, \dots, x_n]_{(x_1, \dots, x_n)}$. Then the completion of $A$ is the ring of formal power series $k[[x_1, \dots, x_n]]$. It is a regular local ring of dimension $n$, and in particular it is a domain.

Lean: `Singularity.Algebra.adicCompletionLocalPolynomialRingEquiv`, `Singularity.Algebra.isDomain_adicCompletion_localPolynomialRing` (the completion is the power series ring, and it is a domain). Lean does not prove that the completion is regular of dimension $n$.

*Proof.* Let $\mathfrak{n} = (x_1, \dots, x_n)$ in $S = k[x_1, \dots, x_n]$. Let $\mathfrak{m} = \mathfrak{n}A$. Localization is exact, so $A/\mathfrak{m}^j$ is the localization of $S/\mathfrak{n}^j$ at $\mathfrak{n}$. The ring $S/\mathfrak{n}^j$ is already local, because each prime ideal contains the nilpotent ideal $\mathfrak{n}/\mathfrak{n}^j$, and $\mathfrak{n}/\mathfrak{n}^j$ is maximal. So the elements outside $\mathfrak{n}$ are units in $S/\mathfrak{n}^j$, and $A/\mathfrak{m}^j \cong S/\mathfrak{n}^j$. These isomorphisms are compatible for different $j$. So $\hat{A} = \varprojlim S/\mathfrak{n}^j$, and this is $k[[x_1, \dots, x_n]]$ by Example 4.2.2. The ring $A$ is regular of dimension $n$ by Example 1.2.3. By Theorem 4.3.3 the same holds for $\hat{A}$. A regular local ring is a domain, by Theorem 1.3.3. $\square$

**Example 4.3.5 (the node).** Let $k$ be a field with $\operatorname{char} k \ne 2$, let $f = y^2 - x^2(1 + x)$ in $k[x, y]$ and let $R$ be the local ring of the curve $f = 0$ at the origin. The polynomial $f$ is irreducible, because $1 + x$ is not a square in $k(x)$. Thus $R$ is a domain. By Proposition 4.3.1 and Corollary 4.3.4, the completion of $R$ is $\hat{R} = k[[x, y]]/(f)$. In $k[[x]]$ the element $1 + x$ is a square: the binomial series
$$u = \sum_{j \ge 0} \binom{1/2}{j} x^j$$
has coefficients in $\mathbb{Z}[1/2]$, so it is defined over $k$, and $u^2 = 1 + x$. Thus $f = (y - xu)(y + xu)$ in $k[[x, y]]$. Neither factor is in the ideal $(f)$, since both have order $1$ and $f$ has order $2$. So $\hat{R}$ is not a domain. Geometrically, the curve is irreducible, but in a formal neighbourhood of the origin it has two branches, the curves $y = xu$ and $y = -xu$. $\square$

In Example 4.3.5 the ring $R$ is not regular, since $f \in \mathfrak{m}^2$. For a regular local ring this does not happen: by Theorem 4.3.3 and Theorem 1.3.3, the completion of a regular local ring is again a domain.

### Notes and references

Proposition 4.3.1 and Proposition 4.3.2 follow [AM69, Chapter 10] and [Mat, Section 8]. The equality of dimensions is [AM69, Corollary 11.19], and the equivalence of regularity is [AM69, Proposition 11.24]. Atiyah and Macdonald prove both with the associated graded ring and the Hilbert-Samuel function of Chapter 3: the rings $R$ and $\hat{R}$ have the same associated graded ring, so they have the same Hilbert-Samuel function and the same dimension. Our proof of the equality of dimensions uses the dimension theorem directly. Matsumura treats the relation between a local ring and its completion with the theory of flat local homomorphisms; see [Mat, Theorem 15.1] for the dimension formula for a flat local homomorphism.
