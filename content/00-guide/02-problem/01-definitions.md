---
title: Regular schemes and resolutions
nodes: [SG00000001, SG00000002, SG00000003, SG00000004, SG00000005]
sources: [Ser55, EGA4]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Regular schemes and resolutions

Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring. By Krull's principal ideal theorem, the maximal ideal $\mathfrak{m}$ needs at least $\dim R$ generators, and by Nakayama's lemma the minimal number of generators is $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2$.

**Definition 2.1.1 (regular local ring).** A Noetherian local ring $R$ is *regular* when $\dim_\kappa \mathfrak{m}/\mathfrak{m}^2 = \dim R$.

A regular local ring is a domain, and a localization of a regular local ring at a prime ideal is regular (Serre). Mathlib has the class `IsRegularLocalRing`, and the project uses it.

**Definition 2.1.2 (regular locus).** Let $X$ be a scheme. The *regular locus* $\operatorname{Reg}(X)$ is the set of points $x \in X$ such that the local ring $\mathcal{O}_{X,x}$ is regular. The scheme $X$ is *regular* when $\operatorname{Reg}(X) = X$.

Node: SG00000001 · Lean: `Singularity.regularLocus`

Node: SG00000002 · Lean: `Singularity.IsRegularScheme`

**Lemma 2.1.3.** For a scheme $X$, $\operatorname{Reg}(X) = X$ if and only if $X$ is regular.

Node: SG00000003 · Lean: `Singularity.regularLocus_eq_univ_iff`

*Proof.* Both sides say that $\mathcal{O}_{X,x}$ is regular for each $x \in X$. $\square$

**Definition 2.1.4 (variety).** Let $k$ be a field. A *variety over $k$* is a reduced scheme $X$ with a morphism $X \to \operatorname{Spec} k$ that is separated and of finite type. A variety need not be irreducible.

Node: SG00000005 · Lean: `Singularity.IsVariety`

**Definition 2.1.5 (resolution).** Let $X$ be a scheme. A morphism $\pi : Y \to X$ is a *resolution* of $X$ when these four conditions hold.

1. $Y$ is regular.
2. $\pi$ is proper.
3. There is an open set $U \subseteq X$ with $U = \operatorname{Reg}(X)$ such that the restriction $\pi^{-1}(U) \to U$ is an isomorphism.
4. The set $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$.

Node: SG00000004 · Lean: `Singularity.IsResolution`

Condition 3 asks that $\operatorname{Reg}(X)$ is open. For a variety this is a theorem of Nagata [EGA4, Section 6.12], but the definition does not use it. Conditions 3 and 4 together make $\pi$ birational on each component of $Y$ when $X$ is reduced, because each component of $Y$ meets $\pi^{-1}(U)$, and over $U$ the map is an isomorphism.
