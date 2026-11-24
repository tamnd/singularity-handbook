---
title: Hypersurfaces of maximal contact
nodes: []
sources: [Kol07, Hir64, Gir75, Hau03, EH02]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Hypersurfaces of maximal contact

Let $I$ be an ideal sheaf on $X$ with maximal order $m \ge 1$. By Corollary 2.1.5 the locus of order $m$ is the zero set of $D^{m-1}(I)$. This ideal has order 1 at each point of the locus, so it contains, locally, the equation of a smooth hypersurface. This section shows that such a hypersurface keeps containing the locus of order $m$ after each blowup sequence of order $m$.

**Definition 2.3.1 (maximal contact).** Let $m = \operatorname{max\text{-}ord} I \ge 1$. The ideal $MC(I) = D^{m-1}(I)$ is the *maximal contact ideal* of $I$. A *hypersurface of maximal contact* for $I$ is a smooth hypersurface $H \subseteq X$ whose ideal sheaf $\mathcal{O}_X(-H)$ is contained in $MC(I)$.

**Lemma 2.3.2 (local existence).** Let $m = \operatorname{max\text{-}ord} I \ge 1$ and let $x$ be a closed point with $\operatorname{ord}_x I = m$. Then there are an open set $U \ni x$ and a hypersurface of maximal contact $H \subseteq U$ for $I|_U$. Each hypersurface of maximal contact $H$ contains $\operatorname{cosupp}(I, m)$.

Lean: none yet

*Proof.* By Lemma 2.1.4, $\operatorname{ord}_x MC(I) = 1$, so there is $h \in MC(I)_x$ with $h \notin \mathfrak{m}_x^2$. Then $h$ is part of a regular system of parameters at $x$, so $dh(x) \ne 0$, and $h$ is part of a system of local coordinates on some open set $U \ni x$. On $U$ the hypersurface $H = (h = 0)$ is smooth, and $\mathcal{O}_U(-H) = (h) \subseteq MC(I)$. For the last claim, $\operatorname{cosupp}(I, m)$ is the zero set of $MC(I)$ by Corollary 2.1.5, and this is contained in the zero set of each ideal contained in $MC(I)$. $\square$

A global hypersurface of maximal contact need not exist, and the local ones are not unique. Section 3.2 deals with both problems.

**Theorem 2.3.3 (maximal contact).** Let $m = \operatorname{max\text{-}ord} I \ge 1$, let $H \subseteq X$ be a hypersurface of maximal contact for $I$, and let $(X_r, I_r, E_r) \to \dots \to (X_0, I_0, E_0) = (X, I, E)$ be a blowup sequence of order $m$. Let $H_0 = H$ and let $H_{i+1}$ be the birational transform of $H_i$. Then for each $i$:

1. $\mathcal{O}_{X_i}(-H_i) \subseteq J^{(m-1)}_i \subseteq MC(I_i)$, with $J^{(m-1)}_i$ as in Theorem 2.2.7;
2. $\operatorname{cosupp}(I_i, m) \subseteq H_i$, and in particular the center $Z_i$ lies in $H_i$;
3. $H_{i+1}$ is smooth, and it is a hypersurface of maximal contact for $I_{i+1}$ whenever $\operatorname{max\text{-}ord} I_{i+1} = m$.

Lean: none yet

*Proof.* We prove (1) by induction on $i$. For $i = 0$ it is the definition, since $J^{(m-1)}_0 = D^{m-1}(I)$. The second inclusion holds for each $i$ by Theorem 2.2.7. Assume (1) for $i$. Then $\operatorname{cosupp}(I_i, m)$ lies in the zero set of $MC(I_i)$ by Lemma 2.1.4, and this lies in the zero set of $\mathcal{O}(-H_i)$, which is $H_i$. This is (2) for $i$. So $Z_i \subseteq H_i$. The center $Z_i$ is a smooth subvariety of the smooth hypersurface $H_i$, so $H_i$ has multiplicity 1 along $Z_i$ and
$$\pi_i^* \mathcal{O}_{X_i}(-H_i) = \mathcal{O}_{X_{i+1}}(-H_{i+1} - F_i),$$
where $F_i$ is the exceptional divisor. This holds also when $Z_i$ has codimension 1: then $Z_i$ is a union of connected components of $H_i$, the blowup is the identity, $F_i = Z_i$, and $H_{i+1}$ is the union of the other components. The transform of $(J^{(m-1)}_i, 1)$ is $\mathcal{O}(F_i) \cdot \pi_i^* J^{(m-1)}_i$, and it contains $\mathcal{O}(F_i) \cdot \pi_i^* \mathcal{O}(-H_i) = \mathcal{O}(-H_{i+1})$. This is (1) for $i + 1$.

(3) The birational transform of a smooth hypersurface under the blowup of a smooth center inside it is the blowup of the hypersurface along that center, so it is smooth; in the chart $U_c$ of Lemma 2.2.2 with $H = (x_1 = 0)$ and $c \ge 2$, it is $(y_1 = 0)$. By Corollary 2.2.8, $\operatorname{max\text{-}ord} I_{i+1} \le m$. If it is $m$, then $MC(I_{i+1}) = D^{m-1}(I_{i+1})$, and (1) says that $H_{i+1}$ is a hypersurface of maximal contact. $\square$

The theorem has an important consequence. The whole blowup sequence of order $m$ takes place inside the hypersurfaces $H_i$. So it should be possible to describe it on $H$, a variety of dimension $n - 1$. The problem is to find the right ideal on $H$. The restriction $I|_H$ is not the right ideal, as the next example shows.

**Example 2.3.4.** Let $I = (xy - z^n)$ on $\mathbb{A}^3$ with $n \ge 2$. The order of $I$ is 2 at the origin and at most 1 elsewhere, so $m = 2$, and
$$MC(I) = D(I) = (xy - z^n, \; y, \; x, \; n z^{n-1}) = (x, \; y, \; z^{n-1}).$$
So $\operatorname{cosupp}(I, 2)$ is the origin, and $H = (x = 0)$ and $H' = (x - y = 0)$ are hypersurfaces of maximal contact. The restriction of $I$ to $H$ is $(z^n)$ in the coordinates $y, z$ of $H$. It has order at least 2 along the whole line $(z = 0)$ of $H$, which is not in $\operatorname{cosupp}(I, 2)$. The restriction of $I$ to $H'$ is $(y^2 - z^n)$ in the coordinates $y, z$, which has order 2 only at the origin. So the restriction of $I$ depends on $H$ and it does not see the locus of order $m$. The derivatives of $I$ correct this. On $H$,
$$\big( I + D(I)^2 \big)\big|_H = (z^n) + (y, z^{n-1})^2 = (y^2, \; y z^{n-1}, \; z^n),$$
because $2n - 2 \ge n$. This ideal has order at least 2 only at the origin. It is the coefficient ideal of Section 3.2 for $m = 2$.

Lean: none yet

**Remark 2.3.5.** Theorem 2.3.3 needs the blowup sequence to be of order $m$, with $m$ the maximal order. For a marked ideal $(I, m)$ with $m$ less than the maximal order, the locus $\operatorname{cosupp}(I, m)$ need not lie in a smooth hypersurface. For example, $I = (xy)$ on $\mathbb{A}^2$ has maximal order 2, and $\operatorname{cosupp}(I, 1)$ is the union of the two lines $x = 0$ and $y = 0$, which is not contained in a smooth curve near the origin. This is why the induction of Chapter 3 treats ideals of maximal order $m$ and marked ideals in different steps.

### Notes and references

Maximal contact goes back to Hironaka [Hir64], and Kollár attributes the theory of maximal contact to Hironaka and Giraud [Kol07, Chapter 3]. Giraud studies what remains of it in positive characteristic in [Gir75]. Theorem 2.3.3 is in [Kol07, Chapter 3], Section "Maximal contact and going down"; see also [EH02] and [Hau03] for the same theorem in the language of their invariants.
