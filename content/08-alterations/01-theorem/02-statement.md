---
title: The theorem
nodes: [SG0000001K, SG0000000V]
sources: [dJ96, Stacks, Liu]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem

We state the theorem of de Jong over a field and over a trait. Then we prove the case of curves, which needs only the normalization. The proof of the general case is the subject of Chapter 2.

### Varieties over a field

**Theorem 1.2.1 (de Jong).** Let $X$ be a variety over a field $k$ and let $Z \subsetneq X$ be a proper closed subset. There are an alteration $\varphi_1 \colon X_1 \to X$ and an open immersion $j_1 \colon X_1 \to \bar X_1$ such that:

1. $\bar X_1$ is a projective variety over $k$ and a regular scheme;
2. the closed subset $j_1(\varphi_1^{-1}(Z)) \cup (\bar X_1 \setminus j_1(X_1))$ is a divisor with strict normal crossings in $\bar X_1$.

If $k$ is perfect, then $\varphi_1$ can be chosen generically étale.

Node: SG0000001K · Lean statement: `Singularity.deJongAlteration` (no proof)

This is [dJ96, Theorem 4.1]. Here variety means an integral variety, as in Section 1.1. The proof of de Jong gives more [dJ96, Remark 4.2]. The morphism $\bar X_1 \to \operatorname{Spec} k$ factors through $\operatorname{Spec} k_1$ for a finite extension $k_1$ of $k$, such that $\bar X_1$ is geometrically irreducible and smooth over $k_1$. If $k$ is perfect, then $\bar X_1$ is smooth over $k$.

The theorem has three parts. The source $X_1$ is regular, since it is open in the regular scheme $\bar X_1$. The alteration has a regular projective compactification. The inverse image of $Z$, together with the boundary of the compactification, is a divisor with strict normal crossings. The second and third parts are what make the theorem useful in cohomology: they give a smooth compactification with a good boundary. For the problem of this handbook the first part is the important one.

**Corollary 1.2.2.** Let $X$ be a variety over a field $k$ in the sense of Volume 0, Definition 2.1.4, so reduced, separated and of finite type, but possibly reducible. Then there are a regular scheme $Y$, quasi-projective over $k$, and a proper surjective morphism $Y \to X$ that is generically finite: each irreducible component of $Y$ maps onto an irreducible component of $X$ with a finite extension of function fields.

Node: SG0000001K · Lean statement: `Singularity.deJongAlteration` (no proof)

Lean: `Singularity.regularAlterationInDim_of_deJongAlteration` (for an integral variety, from the Lean statement of Theorem 1.2.1; with no quasi-projective part)

*Proof.* Let $X^{(1)}, \dots, X^{(m)}$ be the irreducible components of $X$ with their reduced structure. Each is an integral variety. If $X^{(i)}$ is not empty, then $\emptyset$ is a proper closed subset of $X^{(i)}$, and Theorem 1.2.1 with $Z = \emptyset$ gives an alteration $\varphi_i \colon Y_i \to X^{(i)}$ with $Y_i$ open in a regular projective variety. So $Y_i$ is regular and quasi-projective. Let $Y = \bigsqcup_i Y_i$ with the morphism to $X$ given by $\varphi_i$ followed by the closed immersion $X^{(i)} \to X$. A finite disjoint union of regular schemes is regular. The morphism is proper, because each $\varphi_i$ is proper and a closed immersion is proper. It is surjective, because each $\varphi_i$ is surjective and the $X^{(i)}$ cover $X$. The extensions of the function fields are finite by Lemma 1.1.2. $\square$

This is the form of Volume 0, Theorem 2.3.5 and of Volume 9, Theorem 2.3.8. It is the statement of the node SG0000001K in the map.

### Curves

For curves the theorem is classical, and an alteration of degree 1 suffices. We give the proof, because it shows the two steps that the proof in dimension $d$ also uses: one first makes $X$ projective, and then one makes it regular.

**Proposition 1.2.3.** Let $X$ be a variety of dimension 1 over a field $k$ and let $Z \subsetneq X$ be a proper closed subset. Then Theorem 1.2.1 holds for $(X, Z)$ with $\varphi_1$ a modification. In particular it is generically étale for each field $k$.

Lean: none yet

*Proof.* By Chow's lemma for varieties [Stacks] there is a modification $X' \to X$ with $X'$ quasi-projective over $k$. Let $X' \subseteq P$ be an open immersion into a projective variety $P$, for example the closure of $X'$ in a projective space. Let $\nu \colon \bar X_1 \to P$ be the normalization. By Volume 1, Theorem 2.4.7 the morphism $\nu$ is finite, so $\bar X_1$ is projective over $k$. By Volume 1, Theorem 2.5.6, $\bar X_1$ is regular, because it is a normal variety of dimension 1. Let $X_1 = \nu^{-1}(X')$, an open subset of $\bar X_1$, and let $\varphi_1$ be the composition $X_1 \to X' \to X$. It is a composition of two modifications, so it is a modification. The closed subset $\varphi_1^{-1}(Z) \cup (\bar X_1 \setminus X_1)$ is a proper closed subset of the irreducible curve $\bar X_1$, so it is a finite set of closed points. A finite set of closed points on a regular curve is a divisor with strict normal crossings, as we saw after Lemma 1.1.11. A modification has degree 1, and an extension of degree 1 is separable, so $\varphi_1$ is generically étale by Lemma 1.1.5. $\square$

The proof does not give the stronger form of Remark 4.2 of [dJ96]: over an imperfect field $k$ the curve $\bar X_1$ is regular, but it need not be smooth over any finite extension of $k$ in $k(\bar X_1)$. De Jong obtains the smooth form by first passing to an algebraically closed field [dJ96, 4.3 and 4.5]. The next example shows a regular curve that is not smooth.

**Example 1.2.4.** Let $p$ be an odd prime, let $k = \mathbb{F}_p(a)$ with $a$ transcendental over $\mathbb{F}_p$, and let $X = \operatorname{Spec} k[x, y]/(y^2 - x^p + a)$. The polynomial $y^2 - (x^p - a)$ is irreducible, since $x^p - a$ is not a square in $k(x)$. So $X$ is an integral curve. We show that $X$ is regular. At a point where $y \ne 0$, the partial derivative $2y$ of the equation in $y$ is a unit, so the projection to the $x$-line is étale there, and $X$ is regular at the point. At a point with $y = 0$ we have $x^p = a$. The polynomial $x^p - a$ is irreducible over $k$, so there is one such point, the maximal ideal $\mathfrak{n} = (x^p - a, y)$, with residue field $k(a^{1/p})$. In the local ring, $x^p - a = y^2 \in (y)$, so $\mathfrak{n}$ is generated by $y$, and the local ring is a discrete valuation ring. So $X$ is regular. But $X$ is not smooth over $k$. Over $k' = k(a^{1/p})$, with $b = a^{1/p}$, the equation becomes $y^2 = (x - b)^p$, and the point $x = b$, $y = 0$ is singular, since the equation lies in the square of the maximal ideal $(x - b, y)$. So the regular curve $X$ is its own normalization, and it becomes singular after the inseparable extension $k'/k$. This is why Remark 4.2 of [dJ96] needs a finite extension $k_1$ of $k$, which can be inseparable.

### Varieties over a trait

De Jong also proves the theorem over a trait, with a semistable conclusion. Recall the strict semistable pairs of Definition 1.1.13.

**Theorem 1.2.5 (de Jong).** Let $S$ be a trait, let $X$ be an $S$-variety and let $Z \subsetneq X$ be a proper closed subset that contains the special fibre of $X$. There are a trait $S_1$ finite over $S$, an $S_1$-variety $X_1$, an alteration $\varphi_1 \colon X_1 \to X$ of schemes over $S$, and an open immersion $j_1 \colon X_1 \to \bar X_1$ of $S_1$-varieties, such that:

1. $\bar X_1$ is a projective $S_1$-variety with geometrically irreducible generic fibre;
2. the pair $(\bar X_1, j_1(\varphi_1^{-1}(Z)) \cup (\bar X_1 \setminus j_1(X_1)))$ is a strict semistable pair over $S_1$.

Lean: none yet

This is [dJ96, Theorem 6.5]. It is the alteration form of the semistable reduction theorem. The finite extension of traits $S_1 \to S$ cannot be avoided in general, already in relative dimension 0. Let $R'$ be a finite extension of $R$ that is a discrete valuation ring with ramification index $e > 1$, and let $X = \operatorname{Spec} R'$. An $S$-variety $X_1$ that is strictly semistable over $S$ of relative dimension 0 has a reduced special fibre that is smooth over $\kappa(s)$, so it is flat with étale fibres, and so it is étale over $S$. Then $\pi$ is a uniformizer of each local ring of $X_1$. A morphism $X_1 \to X$ over $S$ sends a uniformizer $\pi'$ of $R'$ to an element whose $e$-th power is a unit times $\pi$, which is impossible for $e > 1$. So the theorem needs a ramified extension $S_1$ of $S$ for this $X$, as in the stable reduction of curves (Theorem 2.2.3). De Jong also proves a form over a Dedekind scheme [dJ96, Theorem 8.2], and an equivariant form, which we state in Section 3.1.

### Notes and references

The theorem is the main theorem of [dJ96]. De Jong writes that the methods are elementary, except for the use of the moduli of stable pointed curves. The survey in the introduction of [dJ96] lists applications to cohomology: the existence of smooth compactifications up to alteration is enough for many results on étale cohomology and on the weights of Deligne. The book [Liu] gives the theory of curves over a field and over a Dedekind scheme that we use in Chapter 2.

In Lean, the file `Singularity/Alteration/Statement.lean` states Theorem 1.2.1 as the proposition `Singularity.deJongAlteration`. It is a definition, not a theorem, and the library does not prove it. The Lean statement is weaker than Theorem 1.2.1 in two points. It asks that $\bar X_1$ is proper over $k$, because Mathlib has no projective morphisms. It leaves out the generically étale part. The file also proves that the statement gives a regular alteration of each integral variety (`Singularity.regularAlterationInDim_of_deJongAlteration`), and that resolution of singularities in dimension $n$ gives the same in dimension $n$ (`Singularity.regularAlterationInDim_of_resolutionInDim`). The library has no Lean form of the hypothesis on the moduli of stable curves, because Mathlib has no curves with ordinary double points. Chapter 4 proposes the form of this hypothesis.
