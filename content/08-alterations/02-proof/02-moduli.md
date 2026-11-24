---
title: Stable curves and their moduli
nodes: [SG0000001K, SG0000004G, SG0000004H, SG0000004J]
sources: [dJ96, DM69, Knu83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Stable curves and their moduli

The proof of de Jong uses one deep input from outside resolution theory: the moduli of stable pointed curves. This section states what is used. We do not prove these theorems. Instead we isolate the part that the proof needs as a named hypothesis, Hypothesis 2.2.5, and we prove the step of [dJ96, 4.17] from it. So the proof of Theorem 1.2.1 in this volume is a proof modulo Hypothesis 2.2.5 and the other cited results, and the hypothesis is the single place where the moduli enter.

### Stable pointed curves

Let $\bar k$ be an algebraically closed field. A *nodal curve* over $\bar k$ is a connected proper curve over $\bar k$ whose singular points are ordinary double points. Its genus is the arithmetic genus $\dim H^1(C, \mathcal{O}_C)$.

**Definition 2.2.1 (stable pointed curve).** Let $g, n \ge 0$ with $2g - 2 + n > 0$. A *stable $n$-pointed curve of genus $g$* over $\bar k$ is a nodal curve $C$ of genus $g$ with $n$ distinct points $x_1, \dots, x_n$ in the smooth locus of $C$, such that the following holds. Let $C_i$ be an irreducible component of $C$, let $\tilde C_i$ be its normalization, and call a point of $\tilde C_i$ *special* if it maps to a singular point of $C$ or to one of the $x_j$. If $\tilde C_i$ has genus 0, then it has at least 3 special points. If $\tilde C_i$ has genus 1, then it has at least 1 special point. Over a scheme $S$, a *stable $n$-pointed curve of genus $g$* is a semistable curve $f \colon C \to S$ (Definition 2.1.1) with $n$ sections $\tau_1, \dots, \tau_n$, such that each geometric fibre, with the points $\tau_i$, is a stable $n$-pointed curve of genus $g$.

The condition says that each component has enough special points to have only finitely many automorphisms that fix them. A projective line with 3 marked points has no automorphism that fixes them, and a projective line with 2 marked points has the automorphisms $x \mapsto cx$. If the sections $\tau_i$ of a stable curve are disjoint and lie in the smooth locus, as the definition requires, then for $n \ge 3$ and $g = 0$ a smooth fibre is a projective line with $n$ distinct points.

**Theorem 2.2.2 (Deligne-Mumford, Knudsen).** Let $g, n \ge 0$ with $2g - 2 + n > 0$. The stable $n$-pointed curves of genus $g$ form an algebraic stack $\overline{\mathcal{M}}_{g,n}$ over $\mathbb{Z}$ that is proper and smooth over $\mathbb{Z}$. The smooth curves form an open substack $\mathcal{M}_{g,n}$.

Node: SG0000004G · Lean: none yet

For $n = 0$ and $g \ge 2$ this is [DM69]. For pointed curves it is [Knu83]. The properness of $\overline{\mathcal{M}}_{g,n}$ contains the stable reduction theorem: over a discrete valuation ring $R$ with fraction field $K$, a smooth $n$-pointed curve of genus $g$ over $K$ extends, after a finite extension of $K$ and the base change to a localization of the integral closure of $R$, to a stable $n$-pointed curve, and the extension is unique up to a unique isomorphism. For $g \ge 2$ and $n = 0$ this is the stable reduction theorem of [DM69].

**Example 2.2.3 (four points on a line).** Let $g = 0$ and $n = 4$. Over $U = \mathbb{P}^1_k \setminus \{0, 1, \infty\}$, with coordinate $\lambda$, take the curve $\mathbb{P}^1_U = U \times \mathbb{P}^1$ with coordinate $x$ on the second factor, and the four sections $x = 0$, $x = 1$, $x = \infty$ and $x = \lambda$. This is a smooth $4$-pointed curve of genus 0 over $U$. The trivial extension $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1_\lambda$ is not stable over $\lambda = 0$: there the sections $x = 0$ and $x = \lambda$ meet at the point $(0, 0)$. Let $X$ be the blowup of $\mathbb{P}^1 \times \mathbb{P}^1$ at the three points $(0, 0)$, $(1, 1)$ and $(\infty, \infty)$, with coordinates $(\lambda, x)$. Near $(0, 0)$ the two sections are the smooth curves $x = 0$ and $x = \lambda$, with different tangent lines, so their strict transforms meet the exceptional curve at two different points. The function $\lambda$ vanishes to order 1 at $(0, 0)$, so the fibre of $X$ over $\lambda = 0$ is the strict transform of the line $\lambda = 0$ plus the exceptional curve. These are two projective lines that meet transversally at one point. The first one carries the points $x = 1$ and $x = \infty$, the second one carries the points $x = 0$ and $x = \lambda$, and each of them has three special points. The points $\lambda = 1$ and $\lambda = \infty$ are the same after a change of coordinates. So $X \to \mathbb{P}^1_\lambda$ is a stable $4$-pointed curve of genus 0 over $\mathbb{P}^1_\lambda$ that extends the family over $U$. It is flat, because $X$ is an integral regular surface and $\mathbb{P}^1_\lambda$ is a regular curve. In this example the base needs no alteration; the total space needs a modification.

The example shows one feature of the general case. To extend a family of curves, one must change the total space and not only the base. In the general case one must also alter the base, because the extension exists only after a finite extension of the function field. The level structures below make the moduli a scheme, and then the extension comes from the closure of a graph.

### Level structures and the moduli scheme

Let $\ell$ be a prime number and let $T$ be a scheme over $\mathbb{Z}[1/\ell]$. Let $C \to T$ be a smooth proper curve with geometrically connected fibres of genus $g$. A *level-$\ell$ structure* on $C/T$ is an isomorphism of group schemes over $T$ from the constant group $(\mathbb{Z}/\ell)^{2g}_T$ to the $\ell$-torsion $\operatorname{Pic}^0_{C/T}[\ell]$ of the Jacobian. For $g = 0$ there is exactly one level-$\ell$ structure.

De Jong uses the following facts [dJ96, 2.24]. Fix $g \ge 0$, $n \ge 3$ and a prime $\ell \ge 3$. Let $\mathcal{M}_{g,n}[\ell] \to \mathcal{M}_{g,n}[1/\ell]$ be the finite étale cover given by the level-$\ell$ structures of the universal curve. Then $\mathcal{M}_{g,n}[\ell]$ is a scheme $M_{g,n}[\ell]$. Let $\overline{M}_{g,n}[\ell]$ be the normalization of $\overline{\mathcal{M}}_{g,n}[1/\ell]$ in the function field of $M_{g,n}[\ell]$. De Jong remarks that $\overline{M}_{g,n}[\ell]$ is a projective scheme over $\mathbb{Z}[1/\ell]$, and the pullback of the universal curve from the stack gives a stable $n$-pointed curve over it. We put these facts into one statement.

**Hypothesis 2.2.4 (the level-$\ell$ moduli).** Let $g \ge 0$, $n \ge 3$, and let $\ell \ge 3$ be a prime. Then the following hold.

1. For each smooth proper $n$-pointed curve $C \to T$ with geometrically connected fibres of genus $g$ over a $\mathbb{Z}[1/\ell]$-scheme $T$, the functor of level-$\ell$ structures on $C/T$ is represented by a $T$-scheme $L(C/T)$ that is finite, étale and surjective over $T$.
2. There are a scheme $M$ over $\mathbb{Z}[1/\ell]$ and a smooth proper $n$-pointed curve of genus $g$ over $M$ with a level-$\ell$ structure that is a universal object: for each $T$ as in part 1, each smooth proper $n$-pointed curve of genus $g$ over $T$ with a level-$\ell$ structure is the pullback of the universal object by a unique morphism $T \to M$, and the isomorphism of the pullback with the curve is unique.
3. There are a projective scheme $\overline{M}$ over $\mathbb{Z}[1/\ell]$, an open immersion $M \to \overline{M}$, and a stable $n$-pointed curve of genus $g$ over $\overline{M}$ whose restriction to $M$ is the universal curve of part 2.

Node: SG0000004H · Lean: none yet

By [dJ96, 2.24] these statements follow from Theorem 2.2.2 and the theory of the Jacobian. We use them as a hypothesis because the proofs are outside this handbook. Part 1 holds because $\operatorname{Pic}^0_{C/T}[\ell]$ is finite étale of rank $\ell^{2g}$ over $T$ when $\ell$ is invertible on $T$, and its geometric fibres are isomorphic to $(\mathbb{Z}/\ell)^{2g}$.

The proof of de Jong only uses the following consequence.

**Hypothesis 2.2.5 (extension after an alteration).** Let $k$ be an algebraically closed field, let $Y$ be a variety over $k$, let $U \subseteq Y$ be a nonempty open subscheme, let $n \ge 3$, and let $(C \to U, \sigma_1, \dots, \sigma_n)$ be a smooth proper $n$-pointed curve of genus $g$ over $U$ with geometrically connected fibres. Then there are a variety $Y'$ over $k$, a projective generically étale alteration $\psi \colon Y' \to Y$, a nonempty open subscheme $U' \subseteq \psi^{-1}(U)$, a stable $n$-pointed curve $(\mathcal{C}', \tau_1, \dots, \tau_n)$ of genus $g$ over $Y'$, and an isomorphism $\mathcal{C}'|_{U'} \cong C \times_U U'$ that maps $\tau_i$ to the pullback of $\sigma_i$ for each $i$. If $Y$ is projective, then $Y'$ is projective.

Node: SG0000004J · Lean: none yet

**Proposition 2.2.6.** Hypothesis 2.2.4 implies Hypothesis 2.2.5.

Lean: none yet

*Proof.* Let $p \ge 0$ be the characteristic of $k$, and choose a prime $\ell \ge 3$ with $\ell \ne p$. Then $k$ is a $\mathbb{Z}[1/\ell]$-algebra. We may shrink $U$, because a smaller $U$ gives the same conclusion. Since $k$ is algebraically closed, hence perfect, the regular locus of $Y$ is a dense open subset, and we may assume that $U$ is regular, and in particular normal.

Let $L = L(C/U)$ be the scheme of part 1 of Hypothesis 2.2.4. It is finite and étale over the normal scheme $U$, so it is normal. A Noetherian normal scheme is the disjoint union of its connected components, and each of them is integral. Let $W$ be one connected component of $L$. Then $W$ is open and closed in $L$, so $W \to U$ is finite and étale. Its image is open, because étale morphisms are open, and closed, because finite morphisms are closed. As $U$ is irreducible, the image is $U$. So the function field $k(W)$ is a finite separable extension of $k(U) = k(Y)$.

Let $Y''$ be the normalization of $Y$ in $k(W)$. It is finite over $Y$ (Volume 1, Theorem 2.4.7). Over $U$ it is the normalization of $U$ in $k(W)$, and this is $W$, because $W$ is normal and finite over $U$. So $W$ is an open subscheme of $Y''$.

The universal property of $L$ gives a level-$\ell$ structure on $C \times_U W$. By part 2 there is a morphism $\mu \colon W \to M$ such that $C \times_U W$, with its sections and its level structure, is the pullback of the universal object by $\mu$. Let $\overline{M}_k = \overline{M} \times_{\mathbb{Z}[1/\ell]} \operatorname{Spec} k$, a projective $k$-scheme. Let $Y'$ be the closure, with its reduced structure, of the graph of $W \to M \to \overline{M}_k$ in $Y'' \times_k \overline{M}_k$. The graph is closed in $W \times_k \overline{M}_k$, because $\overline{M}_k$ is separated, and it is isomorphic to $W$. So the inverse image of $W$ in $Y'$ is the graph, and $W$ is an open subscheme $U'$ of $Y'$. Since $W$ is integral, $Y'$ is integral, and $k(Y') = k(W)$.

The morphism $Y' \to Y''$ is projective, since $Y'$ is closed in $Y'' \times_k \overline{M}_k$, and $Y'' \to Y$ is finite. So $\psi \colon Y' \to Y$ is proper. It is surjective, because its image is closed and contains the dense set $U$. The extension $k(Y')/k(Y)$ is finite and separable. So $\psi$ is an alteration, and it is generically étale (Lemma 1.1.5). A finite morphism is projective, and the composition of projective morphisms to a quasi-compact base is projective, so $\psi$ is projective. If $Y$ is projective, then $Y'$ is projective.

Let $(\mathcal{C}', \tau)$ be the pullback of the stable curve of part 3 by the projection $Y' \to \overline{M}_k$. Over $U' = W$ this projection is $\mu$ followed by $M \to \overline{M}$, and the stable curve of part 3 restricts to the universal curve over $M$. So $\mathcal{C}'|_{U'}$ is the pullback of the universal curve by $\mu$, and this is $C \times_U W$ with its sections. $\square$

This argument is the one of [dJ96, 4.17], with one change. De Jong takes the closure of the image of $W$ in $Y \times \overline{M}_k$. We first pass to the normalization $Y''$, so that $U'$ is an open subscheme of $Y'$ and the isomorphism of curves over $U'$ is the one given by part 2. Both constructions give a generically étale alteration.

### Why stability is needed

The proof in Section 2.4 extends the rational map from the stable curve $\mathcal{C}'$ to the given family $X \to Y$. It uses that $\mathcal{C}'$ is stable and not only semistable, in the proof of [dJ96, Lemma 4.20]. There a component of a fibre of $\mathcal{C}'$ that is contracted to a point in $X$ leads to a contradiction: either three components of a fibre of $\mathcal{C}'$ meet at one point, which is not possible on a nodal curve, or two components meet at a marked point, which is not possible because the marked points lie in the smooth locus. The argument needs three distinct marked points on the fibre of $\mathcal{C}'$, and these exist because the sections of a stable curve are disjoint. This is also the reason why the proof needs $n \ge 3$ sections in the smooth locus, and why Section 2.3 adds sections to the divisor $Z$.

### Notes and references

The stable reduction theorem and the irreducibility of the moduli of curves are the main results of [DM69]. The stacks of stable pointed curves are constructed in [Knu83]. De Jong summarizes what he uses in [dJ96, 2.24]. Hypothesis 2.2.5 is the form that a Lean formalization of Theorem 1.2.1 would assume; Chapter 4 discusses this. Nothing of this section is in Lean.
