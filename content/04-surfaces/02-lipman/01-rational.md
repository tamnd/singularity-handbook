---
title: Rational singularities
nodes: []
sources: [Lip78, Art86, Har, Stacks, Mat, AM69]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Rational singularities

The proof of Lipman has two parts. The first part reduces the problem to surfaces with rational singularities, and the second part resolves rational singularities. In this section we define rational singularities and we prove the formal parts of the first step. The main input is a bound on the length of $H^1(Y, \mathcal{O}_Y)$, which we cite from [Lip78].

Throughout this section, $X$ is a normal integral excellent scheme with $\dim X \le 2$, and $K$ is its function field.

### Normal modifications

**Definition 2.1.1.** A *normal modification* of $X$ is a proper morphism $f : Y \to X$ such that $Y$ is a normal integral scheme and $f$ is birational, that is, there is a dense open $U \subseteq X$ such that $f^{-1}(U)$ is dense in $Y$ and $f^{-1}(U) \to U$ is an isomorphism.

Lean: `Singularity.IsNormalModification`, `Singularity.isNormalModification_id` (with normal read as integrally closed stalks).

By Corollary 1.2.5, the normalization of the blowup of $X$ at its singular points is a normal modification of $X$. A composite of two normal modifications is a normal modification. A normal modification $f : Y \to X$ is of finite type, so $Y$ is excellent by Theorem 5.2.8 of Volume 1, and the function field of $Y$ is $K$.

**Lemma 2.1.2.** Let $f : Y \to X$ be a normal modification.

1. The map $\mathcal{O}_X \to f_* \mathcal{O}_Y$ is an isomorphism.
2. Let $x \in X$ with $\dim \mathcal{O}_{X,x} \le 1$. Then $Y \times_X \operatorname{Spec} \mathcal{O}_{X,x} \to \operatorname{Spec} \mathcal{O}_{X,x}$ is an isomorphism.
3. Each fibre of $f$ has dimension at most 1, and $\dim Y \le 2$.
4. The sheaf $R^1 f_* \mathcal{O}_Y$ is coherent, and its support is a finite set of closed points $x$ with $\dim \mathcal{O}_{X,x} = 2$. If $X = \operatorname{Spec} A$ is affine, then $H^1(Y, \mathcal{O}_Y)$ is an $A$-module of finite length.
5. For each coherent sheaf $\mathcal{F}$ on $Y$ and each $i \ge 2$, we have $R^i f_* \mathcal{F} = 0$. If $X$ is affine, then $H^i(Y, \mathcal{F}) = 0$ for $i \ge 2$.

Lean: `Singularity.Lipman.subalgebra_eq_bot_of_finite` (the affine step of part 1: a finite subalgebra of $K$ over a normal domain $R$ is $R$). The sheaf statement and parts 2 to 5 are not in Lean yet.

*Proof.* 1. For a proper morphism and a coherent sheaf, the higher direct images are coherent [Har, Theorem III.8.8] for projective morphisms, and [Stacks] in general. Let $\operatorname{Spec} R \subseteq X$ be an affine open. Then $B = \Gamma(f^{-1}(\operatorname{Spec} R), \mathcal{O}_Y)$ is a finite $R$-module. It is a subring of $K$, because $Y$ is integral with function field $K$. Thus each element of $B$ is integral over $R$. Since $R$ is integrally closed in $K$, we get $B = R$.

2. Let $\mathcal{O} = \mathcal{O}_{X,x}$ and $Y_x = Y \times_X \operatorname{Spec} \mathcal{O}$. The ring $\mathcal{O}$ is a field or a discrete valuation ring, by Theorem 1.4.2 of Volume 1. Over an affine open $\operatorname{Spec} R$ of $X$, the scheme $Y_x$ is covered by the localizations of the rings of the affine opens of $Y$, and these are subrings of $K$. Thus $Y_x$ is integral with function field $K$. The morphism $Y_x \to \operatorname{Spec} \mathcal{O}$ is proper. By the valuative criterion [Har, Theorem II.4.7], the point $\operatorname{Spec} K \to Y_x$ extends to a section $s : \operatorname{Spec} \mathcal{O} \to Y_x$. A section of a separated morphism is a closed immersion [Stacks]. Its image is closed and contains the generic point of $Y_x$, so it is all of $Y_x$. A closed immersion onto a reduced scheme is an isomorphism. Thus $s$ is an isomorphism, and so is its inverse $Y_x \to \operatorname{Spec} \mathcal{O}$.

3. Let $y \in Y$, let $x = f(y)$, and choose affine opens $\operatorname{Spec} B \ni y$ and $\operatorname{Spec} R \ni x$ with $R \subseteq B \subseteq K$. The dimension inequality [Mat, Theorem 15.5] gives $\dim \mathcal{O}_{Y,y} + \operatorname{tr.deg}_{\kappa(x)} \kappa(y) \le \dim \mathcal{O}_{X,x}$. Thus $\dim \mathcal{O}_{Y,y} \le 2$, and $\dim Y \le 2$. Assume that the fibre over $x$ has dimension 2. Then it has a point $y$ with $\operatorname{tr.deg}_{\kappa(x)} \kappa(y) = 2$. The inequality gives $\dim \mathcal{O}_{X,x} = 2$ and $\dim \mathcal{O}_{Y,y} = 0$. Thus $y$ is the generic point of $Y$, and $f(y)$ is the generic point of $X$. This contradicts $\dim \mathcal{O}_{X,x} = 2$.

4. The sheaf $R^1 f_* \mathcal{O}_Y$ is coherent by the reference in part 1. The morphism $\operatorname{Spec} \mathcal{O}_{X,x} \to X$ is flat. By flat base change [Har, Proposition III.9.3], the stalk $(R^1 f_* \mathcal{O}_Y)_x$ is $H^1(Y_x, \mathcal{O}_{Y_x})$. If $\dim \mathcal{O}_{X,x} \le 1$, then $Y_x$ is affine by part 2, so this group is 0. Thus the support is a closed set of points $x$ with $\dim \mathcal{O}_{X,x} = 2$. By Lemma 1.2.3 it is a finite set of closed points. If $X = \operatorname{Spec} A$, then $H^1(Y, \mathcal{O}_Y)$ is the module of global sections of $R^1 f_* \mathcal{O}_Y$ [Har, Proposition III.8.5]. It is a finitely generated $A$-module with support at finitely many maximal ideals, so it has finite length.

5. By part 3, the fibres of $f$ have dimension at most 1. For a projective morphism this gives $R^i f_* \mathcal{F} = 0$ for $i \ge 2$ by the theorem on formal functions [Har, Corollary III.11.2]. The same argument works for a proper morphism [Stacks]: the completion of the stalk of $R^i f_* \mathcal{F}$ at $x$ is a limit of groups $H^i$ on the thickenings of the fibre, and these vanish for $i \ge 2$ by the theorem of Grothendieck [Har, Theorem III.2.7]. The last claim follows from [Har, Proposition III.8.5]. $\square$

### The definition

Lemma 2.1.2 says that for an affine $X$ and a normal modification $Y \to X$, the group $H^1(Y, \mathcal{O}_Y)$ is a module of finite length, supported at finitely many closed points $x$ with $\dim \mathcal{O}_{X,x} = 2$. This module measures how much the modification changes the structure sheaf. For a curve the analogous module is always 0, because a normal curve is regular (Theorem 1.4.2 of Volume 1). For a surface it can be nonzero. In Example 2.3.6 a resolution of $z^2 = x^4 + y^4$ has a curve of genus 1 over the singular point, and $H^1$ is not 0. In Example 2.3.7 the resolution of $xy = z^2$ has a projective line over the singular point, and $H^1 = 0$. The rational singularities are those for which no normal modification produces such a module.

**Definition 2.1.3.** The scheme $X$ has *rational singularities* if $R^1 f_* \mathcal{O}_Y = 0$ for each normal modification $f : Y \to X$. Let $A$ be an excellent normal local domain of dimension 2. Then $A$ has a *rational singularity* if $\operatorname{Spec} A$ has rational singularities.

Lean: `Singularity.HasRationalSingularities`, `Singularity.IsRationalSingularity` (with the sheaf cohomology of Mathlib, without the hypotheses of excellence).

**Remark 2.1.4.** Many texts define a rational singularity with one resolution: $A$ is rational if $H^1(Y, \mathcal{O}_Y) = 0$ for a resolution $Y \to \operatorname{Spec} A$. Once resolutions exist (Theorem 2.2.1), this agrees with Definition 2.1.3 for excellent $A$. We do not use this fact, and we do not prove it. Definition 2.1.3 has the advantage that it does not need the existence of a resolution.

Lean: none yet

### Two properties

**Lemma 2.1.5.** Assume that $X$ has rational singularities and let $h : Y \to X$ be a normal modification. Then $Y$ has rational singularities.

Lean: `Singularity.subsingleton_of_exact`, `Singularity.subsingleton_of_forall_pi_subsingleton` (the algebra steps). The statement on higher direct images is not in Lean yet.

*Proof.* The scheme $Y$ is a normal integral excellent scheme with $\dim Y \le 2$, by Lemma 2.1.2 and the remarks before it. Let $g : Y' \to Y$ be a normal modification and let $f = h \circ g$. Then $f$ is a normal modification of $X$. The Leray spectral sequence $R^p h_* R^q g_* \mathcal{O}_{Y'} \Rightarrow R^{p+q} f_* \mathcal{O}_{Y'}$ gives the exact sequence of low degrees

$$0 \to R^1 h_* (g_* \mathcal{O}_{Y'}) \to R^1 f_* \mathcal{O}_{Y'} \to h_* R^1 g_* \mathcal{O}_{Y'} \to R^2 h_* (g_* \mathcal{O}_{Y'}).$$

By Lemma 2.1.2 for $g$, we have $g_* \mathcal{O}_{Y'} = \mathcal{O}_Y$. By Lemma 2.1.2 for $h$, we have $R^2 h_* \mathcal{O}_Y = 0$. Since $X$ has rational singularities, $R^1 f_* \mathcal{O}_{Y'} = 0$. Thus $h_* R^1 g_* \mathcal{O}_{Y'} = 0$.

Let $\mathcal{G} = R^1 g_* \mathcal{O}_{Y'}$. By Lemma 2.1.2 for $g$, the support of $\mathcal{G}$ is a finite set of closed points $y_1, \dots, y_s$ of $Y$. Thus $\Gamma(W, \mathcal{G}) = \bigoplus_{y_j \in W} \mathcal{G}_{y_j}$ for each open $W \subseteq Y$. For each affine open $V \subseteq X$ we get $0 = \Gamma(V, h_* \mathcal{G}) = \bigoplus_{y_j \in h^{-1}(V)} \mathcal{G}_{y_j}$. The sets $h^{-1}(V)$ cover $Y$, so $\mathcal{G}_{y_j} = 0$ for each $j$, and $\mathcal{G} = 0$. $\square$

**Theorem 2.1.6 (Lipman).** Let $A$ be an excellent normal local domain of dimension 2. Then there is an integer $N$ such that $\ell_A(H^1(Y, \mathcal{O}_Y)) \le N$ for each normal modification $Y \to \operatorname{Spec} A$.

Lean: none yet

This is the main input of the first part of the proof. We do not prove the theorem. Lipman proves a bound of this kind in [Lip78], and Artin gives an account of the proof in [Art86]. We state it in the form that this volume uses, for an excellent local ring.

**Proposition 2.1.7.** Let $A$ be an excellent normal local domain of dimension 2 and let $h : Y \to \operatorname{Spec} A$ be a normal modification such that $\ell_A(H^1(Y, \mathcal{O}_Y))$ is the largest value over all normal modifications of $\operatorname{Spec} A$. Then $Y$ has rational singularities. Such a $Y$ exists by Theorem 2.1.6.

Lean: `Singularity.Lipman.subsingleton_of_length_le` (the step on lengths). The cohomology is not in Lean yet.

*Proof.* Let $g : Y' \to Y$ be a normal modification. Then $h \circ g$ is a normal modification of $\operatorname{Spec} A$. The Leray spectral sequence $H^p(Y, R^q g_* \mathcal{O}_{Y'}) \Rightarrow H^{p+q}(Y', \mathcal{O}_{Y'})$ and $g_* \mathcal{O}_{Y'} = \mathcal{O}_Y$ give the exact sequence

$$0 \to H^1(Y, \mathcal{O}_Y) \to H^1(Y', \mathcal{O}_{Y'}) \to H^0(Y, R^1 g_* \mathcal{O}_{Y'}) \to H^2(Y, \mathcal{O}_Y).$$

By Lemma 2.1.2 for $h$, we have $H^2(Y, \mathcal{O}_Y) = 0$. Thus

$$\ell_A(H^1(Y', \mathcal{O}_{Y'})) = \ell_A(H^1(Y, \mathcal{O}_Y)) + \ell_A(H^0(Y, R^1 g_* \mathcal{O}_{Y'})),$$

and the lengths are finite by Lemma 2.1.2. By the choice of $Y$, the left side is at most $\ell_A(H^1(Y, \mathcal{O}_Y))$. Thus $H^0(Y, R^1 g_* \mathcal{O}_{Y'}) = 0$. The sheaf $R^1 g_* \mathcal{O}_{Y'}$ is supported on finitely many closed points, as in the proof of Lemma 2.1.5, so it is 0. Since $g$ is arbitrary, $Y$ has rational singularities. $\square$

### Rationality is local

The definition asks for a condition on all normal modifications of $X$. The next lemma reduces it to the local rings of $X$ at its points of dimension 2. These points are closed, by the proof of Lemma 1.2.3. Thus we can check rationality at one point at a time.

**Lemma 2.1.8.** Assume that for each point $x \in X$ with $\dim \mathcal{O}_{X,x} = 2$, the ring $\mathcal{O}_{X,x}$ has a rational singularity. Then $X$ has rational singularities.

Lean: `Singularity.isIntegrallyClosed_localization_of_le` (the algebra step). The statement on cohomology is not in Lean yet.

*Proof.* Let $f : Y \to X$ be a normal modification, and let $x \in X$. Let $\mathcal{O} = \mathcal{O}_{X,x}$, let $Y_x = Y \times_X \operatorname{Spec} \mathcal{O}$, and let $f_x : Y_x \to \operatorname{Spec} \mathcal{O}$ be the projection. As in the proof of Lemma 2.1.2, part 4, flat base change gives $(R^1 f_* \mathcal{O}_Y)_x \cong H^1(Y_x, \mathcal{O}_{Y_x})$. If $\dim \mathcal{O} \le 1$, this group is 0 by Lemma 2.1.2, part 4.

Let $\dim \mathcal{O} = 2$. We show that $f_x$ is a normal modification. It is proper, since properness is stable under base change [Har, Corollary II.4.8]. As in the proof of Lemma 2.1.2, part 2, the scheme $Y_x$ is covered by the spectra of the rings $B_\Sigma$, where $\operatorname{Spec} B$ is an affine open of $Y$ and $\Sigma$ is a multiplicative subset of $B$. Each $B$ is an integrally closed domain with field of fractions $K$, and so is each $B_\Sigma$ [AM69, Proposition 5.12]. Thus $Y_x$ is a normal integral scheme with function field $K$. Let $U \subseteq X$ be a dense open set such that $f^{-1}(U) \to U$ is an isomorphism. It contains the generic point of $X$. Its inverse image $U_x$ in $\operatorname{Spec} \mathcal{O}$ contains the generic point, so it is a dense open set. The morphism $f_x^{-1}(U_x) \to U_x$ is the base change of $f^{-1}(U) \to U$, so it is an isomorphism. In particular $f_x^{-1}(U_x)$ is a nonempty open subset of the integral scheme $Y_x$, so it is dense. Thus $f_x$ is a normal modification. Since $\mathcal{O}$ has a rational singularity, $R^1 f_{x*} \mathcal{O}_{Y_x} = 0$. Its module of global sections is $H^1(Y_x, \mathcal{O}_{Y_x})$ [Har, Proposition III.8.5], so this group is 0.

Thus all stalks of $R^1 f_* \mathcal{O}_Y$ are 0, and $R^1 f_* \mathcal{O}_Y = 0$. Since $f$ is arbitrary, $X$ has rational singularities. $\square$

The converse is also true, but its proof needs more. A normal modification of $\operatorname{Spec} \mathcal{O}_{X,x}$ must be extended to a normal modification of an open neighbourhood of $x$. We do not use the converse.

### The exceptional curves of a rational singularity

The definition of a rational singularity uses the cohomology of the whole modification. The next proposition passes from the modification to its closed subschemes. It gives a bound on the cohomology of the curves over a singular point, and for a rational singularity it gives the vanishing of their $H^1$. This is the main tool that turns rationality into a statement about curves.

**Proposition 2.1.9.** Assume that $X = \operatorname{Spec} A$ is affine, and let $f : Y \to X$ be a normal modification. Let $D \subseteq Y$ be a closed subscheme.

1. The restriction map $H^1(Y, \mathcal{O}_Y) \to H^1(D, \mathcal{O}_D)$ is onto.
2. If $A$ is local of dimension 2, then $\ell_A(H^1(D, \mathcal{O}_D)) \le \ell_A(H^1(Y, \mathcal{O}_Y)) \le N$, where $N$ is the integer of Theorem 2.1.6.
3. If $X$ has rational singularities, then $H^1(D, \mathcal{O}_D) = 0$.

Lean: `Singularity.Lipman.length_le_of_surjective'` (the step on lengths in part 2). The cohomology is not in Lean yet.

*Proof.* 1. Let $\mathcal{I}_D$ be the ideal sheaf of $D$. The exact sequence $0 \to \mathcal{I}_D \to \mathcal{O}_Y \to \mathcal{O}_D \to 0$ gives the exact sequence

$$H^1(Y, \mathcal{O}_Y) \to H^1(D, \mathcal{O}_D) \to H^2(Y, \mathcal{I}_D).$$

The sheaf $\mathcal{I}_D$ is coherent and $X$ is affine, so $H^2(Y, \mathcal{I}_D) = 0$ by Lemma 2.1.2, part 5.

2. The map of part 1 is $A$-linear. The length of $H^1(Y, \mathcal{O}_Y)$ is finite by Lemma 2.1.2, part 4, and it is at most $N$ by Theorem 2.1.6. A quotient module has at most the length of the module.

3. By [Har, Proposition III.8.5], $H^1(Y, \mathcal{O}_Y)$ is the module of global sections of $R^1 f_* \mathcal{O}_Y$, and this sheaf is 0. Part 1 gives the claim. $\square$

Part 2 is the form in which the bound of Lipman controls the curves. Let $A$ be local of dimension 2 with residue field $\kappa$, and let $C \subseteq Y$ be an integral curve that maps to the closed point. Then $C$ is proper over $\kappa$, and $\ell_A(H^1(C, \mathcal{O}_C)) = \dim_\kappa H^1(C, \mathcal{O}_C)$, because $\mathfrak{m}$ kills $\mathcal{O}_C$. If $C$ is regular and $H^0(C, \mathcal{O}_C) = \kappa$, this number is the genus of $C$. Thus the genus of each curve over the singular point, in each normal modification, is at most $N$. Example 2.3.6 and Example 2.3.14 show curves of genus 1.

**Corollary 2.1.10.** Let $A$ be an excellent normal local domain of dimension 2 with residue field $\kappa$, and assume that $A$ has a rational singularity. Let $f : Y \to \operatorname{Spec} A$ be a normal modification, and let $C, C' \subseteq Y$ be distinct integral closed curves that map to the closed point.

1. $H^1(C, \mathcal{O}_C) = 0$.
2. Assume that $H^0(C, \mathcal{O}_C) = H^0(C', \mathcal{O}_{C'}) = \kappa$. Let $T = C \cap C'$ be the closed subscheme with ideal sheaf $\mathcal{I}_C + \mathcal{I}_{C'}$. Then $T$ is empty, or it is one point $t$ with $\mathcal{O}_{T,t} = \kappa$.
3. If $\kappa$ is algebraically closed and $C$ is regular, then $C \cong \mathbb{P}^1_\kappa$.

Lean: `Singularity.Lipman.exact_diagQuotInf_diffQuotSup`, `Singularity.Lipman.length_quot_sup_le_one` (the exact sequence and the count of lengths in part 2, for rings). The step to sheaves and parts 1 and 3 are not in Lean yet.

*Proof.* 1. This is Proposition 2.1.9, part 3, with $D = C$.

2. The curves are distinct and integral, so $C \not\subseteq C'$, and $T$ is a proper closed subset of the curve $C$. Thus $T$ is a finite set of closed points. Let $D$ be the closed subscheme with ideal sheaf $\mathcal{I}_C \cap \mathcal{I}_{C'}$. For ideals $I, J$ of a ring $R$, the sequence $0 \to R/(I \cap J) \to R/I \oplus R/J \to R/(I + J) \to 0$ is exact, with the maps $r \mapsto (r, r)$ and $(a, b) \mapsto a - b$. This gives an exact sequence of sheaves on $Y$:

$$0 \to \mathcal{O}_D \to \mathcal{O}_C \oplus \mathcal{O}_{C'} \to \mathcal{O}_T \to 0.$$

By Proposition 2.1.9, part 3, we have $H^1(D, \mathcal{O}_D) = 0$. Thus the sequence of global sections

$$0 \to H^0(D, \mathcal{O}_D) \to \kappa \oplus \kappa \to H^0(T, \mathcal{O}_T) \to 0$$

is exact. The ring $H^0(D, \mathcal{O}_D)$ is not 0, because $D$ is not empty, so its length over $A$ is at least 1. Thus $\ell_A(H^0(T, \mathcal{O}_T)) \le 2 - 1 = 1$. Since $T$ is finite, $H^0(T, \mathcal{O}_T) = \bigoplus_{t \in T} \mathcal{O}_{T,t}$, and each summand has length at least 1. Thus $T$ has at most one point $t$, and then $\mathcal{O}_{T,t}$ has length 1. An $A$-algebra of length 1 is isomorphic to $\kappa$ as an $A$-module. Thus it is spanned by 1, and it is the field $\kappa$.

3. The curve $C$ is proper over $\kappa$ and regular, and $H^1(C, \mathcal{O}_C) = 0$ by part 1. Since $\kappa$ is algebraically closed and $C$ is integral and proper, $H^0(C, \mathcal{O}_C) = \kappa$. Thus $C$ has genus 0. A regular proper curve of genus 0 over an algebraically closed field is isomorphic to $\mathbb{P}^1_\kappa$ [Har, Section IV.1]. $\square$

Assume also that $Y$ is regular at the point $t$ of part 2. Then the local equations $a$ and $b$ of $C$ and $C'$ at $t$ satisfy $\ell(\mathcal{O}_{Y,t}/(a, b)) = 1$. Thus $(a, b)$ is the maximal ideal, and $a, b$ is a regular system of parameters. So let $Y$ be a resolution of a rational singularity, and let $C, C'$ be two exceptional curves with $H^0(C, \mathcal{O}_C) = H^0(C', \mathcal{O}_{C'}) = \kappa$. This holds for example if $\kappa$ is algebraically closed. Then $C$ and $C'$ meet in at most one point, and they meet transversally there. The resolutions of Section 2.3 show this: their exceptional curves form chains and trees of projective lines. Lipman proves more in his theory of rational singularities, for example that the dual graph is a tree. We do not use these facts.

### Notes and references

Rational singularities of surfaces go back to Artin, for surfaces over a field. Lipman developed the theory for two-dimensional normal local rings, and [Lip78] uses it for the resolution. The definition we use, with all normal modifications, avoids the need for a resolution in the definition. Theorem 2.1.6 and Proposition 2.1.7 together give a normal modification of $\operatorname{Spec} A$ with only rational singularities. Section 2.2 explains how Lipman connects this with the process of Theorem 2.2.1. Proposition 2.1.9 and Corollary 2.1.10 are short consequences of the vanishing of $H^2$ in Lemma 2.1.2. They are the first steps of the study of the exceptional curves of a rational singularity. For the full theory see [Lip78], [Art86] and the chapter "Resolution of Surfaces" of [Stacks].
