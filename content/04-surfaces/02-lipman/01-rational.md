---
title: Rational singularities
nodes: []
sources: [Lip78, Art86, Har, Stacks, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Rational singularities

The proof of Lipman has two parts. The first part reduces the problem to surfaces with rational singularities, and the second part resolves rational singularities. In this section we define rational singularities and we prove the formal parts of the first step. The main input is a bound on the length of $H^1(Y, \mathcal{O}_Y)$, which we cite from [Lip78].

Throughout this section, $X$ is a normal integral excellent scheme with $\dim X \le 2$, and $K$ is its function field.

### Normal modifications

**Definition 2.1.1.** A *normal modification* of $X$ is a proper morphism $f : Y \to X$ such that $Y$ is a normal integral scheme and $f$ is birational, that is, there is a dense open $U \subseteq X$ such that $f^{-1}(U)$ is dense in $Y$ and $f^{-1}(U) \to U$ is an isomorphism.

Lean: none yet

By Corollary 1.2.5, the normalization of the blowup of $X$ at its singular points is a normal modification of $X$. A composite of two normal modifications is a normal modification. A normal modification $f : Y \to X$ is of finite type, so $Y$ is excellent by Theorem 5.2.8 of Volume 1, and the function field of $Y$ is $K$.

**Lemma 2.1.2.** Let $f : Y \to X$ be a normal modification.

1. The map $\mathcal{O}_X \to f_* \mathcal{O}_Y$ is an isomorphism.
2. Let $x \in X$ with $\dim \mathcal{O}_{X,x} \le 1$. Then $Y \times_X \operatorname{Spec} \mathcal{O}_{X,x} \to \operatorname{Spec} \mathcal{O}_{X,x}$ is an isomorphism.
3. Each fibre of $f$ has dimension at most 1, and $\dim Y \le 2$.
4. The sheaf $R^1 f_* \mathcal{O}_Y$ is coherent, and its support is a finite set of closed points $x$ with $\dim \mathcal{O}_{X,x} = 2$. If $X = \operatorname{Spec} A$ is affine, then $H^1(Y, \mathcal{O}_Y)$ is an $A$-module of finite length.
5. For each coherent sheaf $\mathcal{F}$ on $Y$ and each $i \ge 2$, we have $R^i f_* \mathcal{F} = 0$. If $X$ is affine, then $H^i(Y, \mathcal{F}) = 0$ for $i \ge 2$.

Lean: none yet

*Proof.* 1. For a proper morphism and a coherent sheaf, the higher direct images are coherent [Har, Theorem III.8.8] for projective morphisms, and [Stacks] in general. Let $\operatorname{Spec} R \subseteq X$ be an affine open. Then $B = \Gamma(f^{-1}(\operatorname{Spec} R), \mathcal{O}_Y)$ is a finite $R$-module. It is a subring of $K$, because $Y$ is integral with function field $K$. Thus each element of $B$ is integral over $R$. Since $R$ is integrally closed in $K$, we get $B = R$.

2. Let $\mathcal{O} = \mathcal{O}_{X,x}$ and $Y_x = Y \times_X \operatorname{Spec} \mathcal{O}$. The ring $\mathcal{O}$ is a field or a discrete valuation ring, by Theorem 1.4.2 of Volume 1. Over an affine open $\operatorname{Spec} R$ of $X$, the scheme $Y_x$ is covered by the localizations of the rings of the affine opens of $Y$, and these are subrings of $K$. Thus $Y_x$ is integral with function field $K$. The morphism $Y_x \to \operatorname{Spec} \mathcal{O}$ is proper. By the valuative criterion [Har, Theorem II.4.7], the point $\operatorname{Spec} K \to Y_x$ extends to a section $s : \operatorname{Spec} \mathcal{O} \to Y_x$. A section of a separated morphism is a closed immersion [Stacks]. Its image is closed and contains the generic point of $Y_x$, so it is all of $Y_x$. A closed immersion onto a reduced scheme is an isomorphism. Thus $s$ is an isomorphism, and so is its inverse $Y_x \to \operatorname{Spec} \mathcal{O}$.

3. Let $y \in Y$, let $x = f(y)$, and choose affine opens $\operatorname{Spec} B \ni y$ and $\operatorname{Spec} R \ni x$ with $R \subseteq B \subseteq K$. The dimension inequality [Mat, Theorem 15.5] gives $\dim \mathcal{O}_{Y,y} + \operatorname{tr.deg}_{\kappa(x)} \kappa(y) \le \dim \mathcal{O}_{X,x}$. Thus $\dim \mathcal{O}_{Y,y} \le 2$, and $\dim Y \le 2$. Assume that the fibre over $x$ has dimension 2. Then it has a point $y$ with $\operatorname{tr.deg}_{\kappa(x)} \kappa(y) = 2$. The inequality gives $\dim \mathcal{O}_{X,x} = 2$ and $\dim \mathcal{O}_{Y,y} = 0$. Thus $y$ is the generic point of $Y$, and $f(y)$ is the generic point of $X$. This contradicts $\dim \mathcal{O}_{X,x} = 2$.

4. The sheaf $R^1 f_* \mathcal{O}_Y$ is coherent by the reference in part 1. The morphism $\operatorname{Spec} \mathcal{O}_{X,x} \to X$ is flat. By flat base change [Har, Proposition III.9.3], the stalk $(R^1 f_* \mathcal{O}_Y)_x$ is $H^1(Y_x, \mathcal{O}_{Y_x})$. If $\dim \mathcal{O}_{X,x} \le 1$, then $Y_x$ is affine by part 2, so this group is 0. Thus the support is a closed set of points $x$ with $\dim \mathcal{O}_{X,x} = 2$. By Lemma 1.2.3 it is a finite set of closed points. If $X = \operatorname{Spec} A$, then $H^1(Y, \mathcal{O}_Y)$ is the module of global sections of $R^1 f_* \mathcal{O}_Y$ [Har, Proposition III.8.5]. It is a finitely generated $A$-module with support at finitely many maximal ideals, so it has finite length.

5. By part 3, the fibres of $f$ have dimension at most 1. For a projective morphism this gives $R^i f_* \mathcal{F} = 0$ for $i \ge 2$ by the theorem on formal functions [Har, Corollary III.11.2]. The same argument works for a proper morphism [Stacks]: the completion of the stalk of $R^i f_* \mathcal{F}$ at $x$ is a limit of groups $H^i$ on the thickenings of the fibre, and these vanish for $i \ge 2$ by the theorem of Grothendieck [Har, Theorem III.2.7]. The last claim follows from [Har, Proposition III.8.5]. $\square$

### The definition

**Definition 2.1.3.** The scheme $X$ has *rational singularities* if $R^1 f_* \mathcal{O}_Y = 0$ for each normal modification $f : Y \to X$. Let $A$ be an excellent normal local domain of dimension 2. Then $A$ has a *rational singularity* if $\operatorname{Spec} A$ has rational singularities.

Lean: none yet

**Remark 2.1.4.** Many texts define a rational singularity with one resolution: $A$ is rational if $H^1(Y, \mathcal{O}_Y) = 0$ for a resolution $Y \to \operatorname{Spec} A$. Once resolutions exist (Theorem 2.2.1), this agrees with Definition 2.1.3 for excellent $A$. We do not use this fact, and we do not prove it. Definition 2.1.3 has the advantage that it does not need the existence of a resolution.

Lean: none yet

### Two properties

**Lemma 2.1.5.** Assume that $X$ has rational singularities and let $h : Y \to X$ be a normal modification. Then $Y$ has rational singularities.

Lean: none yet

*Proof.* The scheme $Y$ is a normal integral excellent scheme with $\dim Y \le 2$, by Lemma 2.1.2 and the remarks before it. Let $g : Y' \to Y$ be a normal modification and let $f = h \circ g$. Then $f$ is a normal modification of $X$. The Leray spectral sequence $R^p h_* R^q g_* \mathcal{O}_{Y'} \Rightarrow R^{p+q} f_* \mathcal{O}_{Y'}$ gives the exact sequence of low degrees

$$0 \to R^1 h_* (g_* \mathcal{O}_{Y'}) \to R^1 f_* \mathcal{O}_{Y'} \to h_* R^1 g_* \mathcal{O}_{Y'} \to R^2 h_* (g_* \mathcal{O}_{Y'}).$$

By Lemma 2.1.2 for $g$, we have $g_* \mathcal{O}_{Y'} = \mathcal{O}_Y$. By Lemma 2.1.2 for $h$, we have $R^2 h_* \mathcal{O}_Y = 0$. Since $X$ has rational singularities, $R^1 f_* \mathcal{O}_{Y'} = 0$. Thus $h_* R^1 g_* \mathcal{O}_{Y'} = 0$.

Let $\mathcal{G} = R^1 g_* \mathcal{O}_{Y'}$. By Lemma 2.1.2 for $g$, the support of $\mathcal{G}$ is a finite set of closed points $y_1, \dots, y_s$ of $Y$. Thus $\Gamma(W, \mathcal{G}) = \bigoplus_{y_j \in W} \mathcal{G}_{y_j}$ for each open $W \subseteq Y$. For each affine open $V \subseteq X$ we get $0 = \Gamma(V, h_* \mathcal{G}) = \bigoplus_{y_j \in h^{-1}(V)} \mathcal{G}_{y_j}$. The sets $h^{-1}(V)$ cover $Y$, so $\mathcal{G}_{y_j} = 0$ for each $j$, and $\mathcal{G} = 0$. $\square$

**Theorem 2.1.6 (Lipman).** Let $A$ be an excellent normal local domain of dimension 2. Then there is an integer $N$ such that $\ell_A(H^1(Y, \mathcal{O}_Y)) \le N$ for each normal modification $Y \to \operatorname{Spec} A$.

Lean: none yet

This is the main input of the first part of the proof. We do not prove the theorem. Lipman proves a bound of this kind in [Lip78], and Artin gives an account of the proof in [Art86]. We state it in the form that this volume uses, for an excellent local ring.

**Proposition 2.1.7.** Let $A$ be an excellent normal local domain of dimension 2 and let $h : Y \to \operatorname{Spec} A$ be a normal modification such that $\ell_A(H^1(Y, \mathcal{O}_Y))$ is the largest value over all normal modifications of $\operatorname{Spec} A$. Then $Y$ has rational singularities. Such a $Y$ exists by Theorem 2.1.6.

Lean: none yet

*Proof.* Let $g : Y' \to Y$ be a normal modification. Then $h \circ g$ is a normal modification of $\operatorname{Spec} A$. The Leray spectral sequence $H^p(Y, R^q g_* \mathcal{O}_{Y'}) \Rightarrow H^{p+q}(Y', \mathcal{O}_{Y'})$ and $g_* \mathcal{O}_{Y'} = \mathcal{O}_Y$ give the exact sequence

$$0 \to H^1(Y, \mathcal{O}_Y) \to H^1(Y', \mathcal{O}_{Y'}) \to H^0(Y, R^1 g_* \mathcal{O}_{Y'}) \to H^2(Y, \mathcal{O}_Y).$$

By Lemma 2.1.2 for $h$, we have $H^2(Y, \mathcal{O}_Y) = 0$. Thus

$$\ell_A(H^1(Y', \mathcal{O}_{Y'})) = \ell_A(H^1(Y, \mathcal{O}_Y)) + \ell_A(H^0(Y, R^1 g_* \mathcal{O}_{Y'})),$$

and the lengths are finite by Lemma 2.1.2. By the choice of $Y$, the left side is at most $\ell_A(H^1(Y, \mathcal{O}_Y))$. Thus $H^0(Y, R^1 g_* \mathcal{O}_{Y'}) = 0$. The sheaf $R^1 g_* \mathcal{O}_{Y'}$ is supported on finitely many closed points, as in the proof of Lemma 2.1.5, so it is 0. Since $g$ is arbitrary, $Y$ has rational singularities. $\square$

### Notes and references

Rational singularities of surfaces go back to Artin, for surfaces over a field. Lipman developed the theory for two-dimensional normal local rings, and [Lip78] uses it for the resolution. The definition we use, with all normal modifications, avoids the need for a resolution in the definition. Theorem 2.1.6 and Proposition 2.1.7 together give a normal modification of $\operatorname{Spec} A$ with only rational singularities. Section 2.2 explains how Lipman connects this with the process of Theorem 2.2.1.
