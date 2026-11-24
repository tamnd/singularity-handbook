---
title: The resolution of curves
nodes: [SG0000002B, SG0000002C]
sources: [AM69, Har, Mat, EGA4, Stacks, Mathlib, Curves]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The resolution of curves

In this section we prove that each integral curve over a field has a resolution, in each characteristic. The resolution is the normalization. Section 2.4 gave the affine part of the proof: the normalization of an affine curve is finite and regular. Two steps remain. We must glue the affine pieces, and we must show that the normalization is an isomorphism exactly over the regular locus. For the second step we prove that the regular locus of a curve is open, with an argument that uses the conductor.

Throughout the section, $k$ is a field and $X$ is an integral variety over $k$ with $\dim X \le 1$. We write $\eta$ for the generic point of $X$ and $K = \mathcal{O}_{X,\eta}$ for the function field of $X$.

### The normalization of a curve

Let $U$ be a nonempty affine open subset of $X$ and let $A = \mathcal{O}_X(U)$. The ring $A$ is a domain, because $X$ is integral, and it is a finitely generated $k$-algebra, because $X$ is of finite type over $k$ [Har, Chapter II, Exercise 3.3]. The point $\eta$ is in $U$, and it is the prime ideal $0$ of $A$. Thus $\operatorname{Frac} A = A_{(0)} = K$. Also $\dim A = \dim U \le \dim X \le 1$.

Let $\tilde{A}$ be the integral closure of $A$ in $K$. For a smaller affine open set $U' \subseteq U$, the integral closure of $\mathcal{O}_X(U')$ in $K$ is the localization of $\tilde{A}$ that corresponds to $U'$, because integral closure commutes with localization [AM69, Proposition 5.12]. Thus the affine schemes $\operatorname{Spec} \tilde{A}$ glue to a scheme $Y$ with a morphism $\pi : Y \to X$, and for each affine open set $U$ of $X$,
$$\pi^{-1}(U) = \operatorname{Spec} \tilde{A}, \qquad A = \mathcal{O}_X(U).$$
The morphism $\pi$ is the *normalization* of $X$ [Har, Chapter II, Exercise 3.8]. The map $A \to \tilde{A}$ is the inclusion, so $\pi$ is an isomorphism over $U$ when $A$ is integrally closed.

The scheme $Y$ has a special point. Let $U$ be a nonempty affine open set, and let $\eta' \in \pi^{-1}(U)$ be the prime ideal $0$ of $\tilde{A}$. Each prime ideal $\mathfrak{q}$ of $\tilde{A}$ with $\mathfrak{q} \cap A = 0$ is $0$, because $\tilde{A}$ is integral over $A$ [AM69, Corollary 5.9]. Thus $\eta'$ is the only point of $Y$ over $\eta$, and it does not depend on $U$. The ring $\tilde{A}$ is a domain, so $\eta'$ is in each nonempty open subset of $\operatorname{Spec} \tilde{A}$. The sets $\pi^{-1}(U)$ cover $Y$. It follows that $\eta'$ is in each nonempty open subset of $Y$.

### The normal locus

**Lemma 2.5.1.** Let $A$ be a domain with field of fractions $K$, and assume that the integral closure $\tilde{A}$ of $A$ in $K$ is a finite $A$-module. Let $\mathfrak{p}$ be a prime ideal of $A$ such that $A_\mathfrak{p}$ is integrally closed. Then there is an element $s \in A$ with $s \notin \mathfrak{p}$ and $s \tilde{A} \subseteq A$.

Node: SG0000002B · Lean: `Singularity.Algebra.exists_smul_mem_of_isIntegrallyClosed_localization`

*Proof.* Let $b_1, \dots, b_n$ generate $\tilde{A}$ as an $A$-module. Each $b_i$ is integral over $A$, so it is integral over $A_\mathfrak{p}$. The field of fractions of $A_\mathfrak{p}$ is $K$, and $A_\mathfrak{p}$ is integrally closed, so $b_i \in A_\mathfrak{p}$. Write $b_i = a_i / u_i$ with $a_i \in A$ and $u_i \notin \mathfrak{p}$. Let $s = u_1 \cdots u_n$. Then $s \notin \mathfrak{p}$, because $\mathfrak{p}$ is prime, and $s b_i \in A$ for each $i$. Each element of $\tilde{A}$ is a sum $\sum_i c_i b_i$ with $c_i \in A$, so $s \tilde{A} \subseteq A$. $\square$

The set of the elements $s \in A$ with $s \tilde{A} \subseteq A$ is an ideal of $A$, the *conductor* of $A$ in $\tilde{A}$. Lemma 2.5.1 says that the conductor is not contained in $\mathfrak{p}$ when $A_\mathfrak{p}$ is integrally closed.

**Lemma 2.5.2.** Let $A$ be a domain with field of fractions $K$, and let $s \ne 0$ be an element of $A$ with $s \tilde{A} \subseteq A$. Then the localization $A_s$ is integrally closed.

Lean: `Singularity.Algebra.isIntegrallyClosed_of_isLocalization_away`

*Proof.* The field of fractions of $A_s$ is $K$. Let $x \in K$ be integral over $A_s$, with
$$x^d + c_1 x^{d-1} + \dots + c_d = 0, \qquad c_i \in A_s.$$
Choose $n \ge 0$ such that $s^n c_i \in A$ for each $i$. Multiply the equation by $s^{nd}$. The term $s^{nd} c_i x^{d-i}$ is $(s^{n(i-1)} \cdot s^n c_i)(s^n x)^{d-i}$, so $s^n x$ is a root of a monic polynomial with coefficients in $A$. Thus $s^n x \in \tilde{A}$, and $s \cdot s^n x = a$ for some $a \in A$. Then $x = a / s^{n+1} \in A_s$. $\square$

**Corollary 2.5.3.** Let $A$ be a domain that is a finitely generated algebra over a field, and let $\mathfrak{p}$ be a prime ideal of $A$ such that $A_\mathfrak{p}$ is integrally closed. Then there is an element $s \notin \mathfrak{p}$ such that $A_s$ is integrally closed. Thus the set of the prime ideals $\mathfrak{p}$ such that $A_\mathfrak{p}$ is integrally closed is open in $\operatorname{Spec} A$.

Lean: `Singularity.Algebra.exists_smul_mem_of_isIntegrallyClosed_localization`, `Singularity.Algebra.isIntegrallyClosed_of_isLocalization_away`

*Proof.* By the theorem of Noether (Theorem 2.4.7), $\tilde{A}$ is a finite $A$-module. Lemma 2.5.1 gives $s \notin \mathfrak{p}$ with $s \tilde{A} \subseteq A$, and Lemma 2.5.2 shows that $A_s$ is integrally closed. For each prime ideal $\mathfrak{q}$ of $A$ with $s \notin \mathfrak{q}$, the ring $A_\mathfrak{q}$ is a localization of $A_s$, so it is integrally closed [AM69, Proposition 5.12]. Thus the open set $D(s)$ contains $\mathfrak{p}$, and each of its points has an integrally closed local ring. $\square$

### The normalization is finite

**Proposition 2.5.4.** The normalization $\pi : Y \to X$ is a finite morphism, so it is proper. Let $V$ be a nonempty affine open subset of $X$ such that $\mathcal{O}_X(V)$ is integrally closed. Then the restriction $\pi^{-1}(V) \to V$ is an isomorphism.

Lean: `Singularity.Curves.isFinite_normalizationHom`, `Singularity.Curves.isIso_normalizationHom_restrict`

*Proof.* Let $U$ be an affine open subset of $X$ and let $A = \mathcal{O}_X(U)$. If $U$ is empty, then $\pi^{-1}(U)$ is empty, and there is nothing to prove. If $U$ is not empty, then $\pi^{-1}(U) = \operatorname{Spec} \tilde{A}$, and $\tilde{A}$ is a finite $A$-module by Theorem 2.4.7. Thus $\pi$ is finite. A finite morphism is proper [Har, Chapter II, Exercise 4.1].

If $A = \mathcal{O}_X(V)$ is integrally closed, then $\tilde{A} = A$, and $\pi^{-1}(V) \to V$ is the spectrum of the identity of $A$. $\square$

### The regular locus of a curve

**Proposition 2.5.5.** Let $x \in X$. Then $x \in \operatorname{Reg}(X)$ if and only if there is a nonempty affine open set $V \subseteq X$ with $x \in V$ such that $\mathcal{O}_X(V)$ is integrally closed. In particular, $\operatorname{Reg}(X)$ is open in $X$.

Lean: `Singularity.Curves.exists_isIntegrallyClosed_of_mem_regularLocus`, `Singularity.Curves.mem_regularLocus_of_isIntegrallyClosed`

*Proof.* First we prove a fact about the local rings of $X$. Let $R$ be a Noetherian local domain with $\dim R \le 1$. Then $R$ is regular if and only if $R$ is integrally closed. If $\dim R = 1$, this is Theorem 1.4.2. If $\dim R = 0$, then $0$ is the only prime ideal of $R$, so the maximal ideal is $0$ and $R$ is a field. A field is regular (Example 1.2.2), and a field is integrally closed.

Let $U$ be an affine open set that contains $x$, let $A = \mathcal{O}_X(U)$, and let $\mathfrak{p}$ be the prime ideal of $A$ that is $x$. Then $\mathcal{O}_{X,x} = A_\mathfrak{p}$. This is a Noetherian local domain, and $\dim A_\mathfrak{p} \le \dim A \le 1$.

Assume that $x \in \operatorname{Reg}(X)$. Then $A_\mathfrak{p}$ is regular, so it is integrally closed by the fact above. By Corollary 2.5.3 there is $s \notin \mathfrak{p}$ such that $A_s$ is integrally closed. Let $V = D(s) \subseteq U$. Then $V$ is affine, $\mathcal{O}_X(V) = A_s$, and $x \in V$.

Conversely, let $V$ be as in the statement, let $B = \mathcal{O}_X(V)$, and let $\mathfrak{q}$ be the prime ideal of $B$ that is $x$. The ring $B_\mathfrak{q}$ is a localization of the integrally closed domain $B$, so it is integrally closed [AM69, Proposition 5.12]. It is a Noetherian local domain of dimension at most 1, so it is regular by the fact above. Thus $x \in \operatorname{Reg}(X)$.

The first part shows that $\operatorname{Reg}(X)$ is the union of the open sets $V$ of the statement, so it is open. $\square$

Proposition 2.5.5 is a special case of Theorem 1.9.5: the regular locus of each variety is open [EGA4, Section 6.12]. In dimension 1 the proof is easy, because regular and normal are the same condition on a local ring of dimension at most 1.

### The theorem

**Theorem 2.5.6 (resolution of curves).** Let $k$ be a field of any characteristic and let $X$ be an integral variety over $k$ with $\dim X \le 1$. Then the normalization $\pi : Y \to X$ is a resolution of $X$.

Node: SG0000002C · Lean: `Singularity.Curves.integralResolutionInDim_one`

*Proof.* We prove the four conditions of the definition of a resolution (Volume 0, Definition 2.1.5).

*Step 1. $Y$ is regular.* The sets $\pi^{-1}(U)$, for the nonempty affine open sets $U$ of $X$, cover $Y$. Thus it is sufficient to show that $\operatorname{Spec} \tilde{A}$ is regular for $A = \mathcal{O}_X(U)$. By Theorem 2.4.7, $\tilde{A}$ is a finite $A$-module, so it is a Noetherian ring. It is integrally closed (Section 2.1). It is integral over $A$, so $\dim \tilde{A} = \dim A \le 1$ [AM69, Corollary 5.9 and Theorem 5.11]. Thus $\operatorname{Spec} \tilde{A}$ is a normal Noetherian scheme of dimension at most 1, and it is regular by Corollary 1.4.3. When $\dim A = 1$, this is also Corollary 2.4.8.

*Step 2. $\pi$ is proper.* This is Proposition 2.5.4.

*Step 3. $\pi$ is an isomorphism over $\operatorname{Reg}(X)$.* By Proposition 2.5.5, $\operatorname{Reg}(X)$ is open, and it is the union of the nonempty affine open sets $V$ such that $\mathcal{O}_X(V)$ is integrally closed. By Proposition 2.5.4, $\pi$ is an isomorphism over each such set $V$. A morphism that is an isomorphism over each set of an open cover of its target is an isomorphism. Thus $\pi^{-1}(\operatorname{Reg}(X)) \to \operatorname{Reg}(X)$ is an isomorphism.

*Step 4. $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$.* If $X$ is empty, then $Y$ is empty, and there is nothing to prove. If $X$ is not empty, let $\eta'$ be the point of $Y$ over the generic point $\eta$. The local ring $\mathcal{O}_{X,\eta} = K$ is a field, so it is regular, and $\eta \in \operatorname{Reg}(X)$. Thus the open set $\pi^{-1}(\operatorname{Reg}(X))$ contains $\eta'$. We showed above that $\eta'$ is in each nonempty open subset of $Y$. Thus each nonempty open subset of $Y$ meets $\pi^{-1}(\operatorname{Reg}(X))$, and this set is dense. $\square$

Thus $\mathrm{Res}(p, 1)$ holds for integral varieties for each $p$. For a variety with more than one component, we use the reduction of Volume 9, Section 1.3.

**Corollary 2.5.7.** $\mathrm{Res}(p, 1)$ holds for each $p$.

Lean: `Singularity.Curves.resolutionInDim_one`

*Proof.* By Theorem 2.5.6, each integral variety of dimension at most 1 over a field of characteristic $p$ has a resolution. Theorem 1.3.1 of Volume 9 with $n = 1$ gives $\mathrm{Res}(p, 1)$. $\square$

The Lean development proves Theorem 1.3.1 of Volume 9 with only the three standard axioms. Thus the node SG0000001A of the map, the statement $\mathrm{Res}(p, 1)$ for all curves, is proved in Lean, and so is its integral case, the node SG0000002C.

**Example 2.5.8 (the cusp).** Let $X = \operatorname{Spec} A$ with $A = k[t^2, t^3]$, the cusp of Example 2.1.6. Then $\tilde{A} = k[t]$, and the normalization is the map $\mathbb{A}^1_k \to X$ that sends $t$ to $(t^2, t^3)$. The conductor of $A$ in $k[t]$ contains $t^2$ and $t^3$, because $t^2 \cdot t^i$ and $t^3 \cdot t^i$ are in $A$ for each $i \ge 0$. It does not contain $1$, because $t \notin A$. Thus the conductor is the maximal ideal $(t^2, t^3)$ of $A$, the ideal of the cusp point. By Lemma 2.5.2 with $s = t^2$, the ring $A_{t^2} = k[t, t^{-1}]$ is integrally closed. The regular locus is $X$ minus the cusp point, and the normalization is an isomorphism over it.

### The Lean proof

The Lean proofs are in two files of `tamnd/singularity-lean`. The file `Singularity/Algebra/NormalLocus.lean` has Lemma 2.5.1 and Lemma 2.5.2, and it has a form of Theorem 2.4.7 for each model of the field of fractions. The file `Singularity/Curves/Resolution.lean` has the rest of the section. The proof in Lean follows the proof above, with three changes in the form.

1. In Mathlib, the normalization is the *relative normalization* `Scheme.Hom.normalization` of a quasi-compact and quasi-separated morphism $f : Z \to X$. Over an affine open set $U$ of $X$, its ring of sections is the integral closure of $\mathcal{O}_X(U)$ in $\mathcal{O}_Z(f^{-1}(U))$, and Mathlib glues these affine schemes. We apply it to the morphism $\operatorname{Spec} K \to X$ of the generic point, `genericHom`. Over a nonempty affine open set $U$, the ring $\mathcal{O}_Z(f^{-1}(U))$ is a copy of $K$, and the lemma `isFractionRing_genericHom` proves that it is a field of fractions of $A$.
2. The special point $\eta'$ of Step 4 is the image of the closed point of $\operatorname{Spec} K$ under `toNormalization`. The density uses the fact that $Y$ is irreducible, and Lean finds this fact as an instance.
3. The open set of Step 3 is `normalLocus`, the union of the nonempty affine open sets $V$ with $\mathcal{O}_X(V)$ integrally closed. The lemma `coe_normalLocus` proves that it is the regular locus, which is Proposition 2.5.5.

The main theorem is `isResolution_normalizationHom`. The statement `integralResolutionInDim_one` is Theorem 2.5.6 in the form of the map, and `resolutionInDim_one_of_reductionToIntegral` is Corollary 2.5.7. Each declaration uses only the three standard axioms `propext`, `Classical.choice` and `Quot.sound`.

### Notes and references

The resolution of curves by normalization is classical. For curves over an algebraically closed field it is in [Har, Chapter I, Section 6], where the nonsingular model of a function field of dimension 1 is built from its discrete valuation rings. The proof in this section is the proof by normalization of [Har, Chapter II, Exercise 3.8]. It works over each field, because the theorem of Noether holds over each field. Over a Noetherian domain that is not of finite type over a field, the normalization can fail to be finite (see the notes to Section 2.4), and then the proof fails at Proposition 2.5.4.

The conductor argument of Lemma 2.5.1 is the simplest case of the criterion of Nagata for the openness of the normal locus [Mat, Section 24]. In higher dimension, normal and regular are different conditions. The normalization of a surface is normal, but it can be singular at finitely many points. Thus for surfaces the normalization is only the first step, and Volume 4 continues with blowups.
