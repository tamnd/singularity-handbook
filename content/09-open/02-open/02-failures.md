---
title: Why the methods of characteristic zero fail
nodes: [SG00000018, SG00000015, SG00000017, SG0000000C, SG00000010, SG0000001Q]
sources: [Nar83, Abr25, Hau03, Hau10, HP19a, AT26, ATW24, CDLL26, Kuh-book, Kuh16, KR23, CKR25, CM17, Cut15]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Why the methods of characteristic zero fail

The proofs of resolution in characteristic 0 have the same plan. They define an invariant of a singular point with values in a well-ordered set. They blow up the locus where the invariant is maximal. Then they prove that the invariant drops. The invariant starts with the order of Volume 7, Section 1.1. Its next entries come from a hypersurface of maximal contact and from the residual order of the coefficient ideal on that hypersurface [Hau03]. In this section we explain, with an example for each, which parts of this plan fail in characteristic $p$.

### Derivatives

In characteristic 0 the points of order at least $d$ of $f$ are the common zeros of the derivatives $\partial^\beta f$ with $|\beta| < d$. In characteristic $p$ this is false. All the usual derivatives of $x^p$ vanish, but the order of $x^p$ is $p$ only on the hyperplane $x = 0$. Proposition 1.1.4 of Volume 7 corrects this with the Hasse derivatives $\partial^{(\beta)}$. The correction is enough for the order, but not for maximal contact. For $f = z^p + F(x)$, each derivative of order $p - 1$ is a derivative of $F$, and it does not contain $z$ (Volume 7, Section 1.1). So the derivatives do not give the natural candidate $z = 0$ for a hypersurface of maximal contact. Hauser explains this in [Hau10].

### Maximal contact

Let $f$ have order $d$ at the point $a$. In characteristic 0 there is a smooth hypersurface $V$ through $a$ that contains all the points of order $d$ of $f$ near $a$. The hypersurface $V$ keeps this property after each permissible blowup, so the induction can work on $V$, which has a smaller dimension [Hau03]. Such a $V$ is a hypersurface of maximal contact. In characteristic $p$ there is no such $V$ in general, also not in a formal neighbourhood of $a$. The next example is due to Narasimhan [Nar83]. We use the form of [Abr25, Remark 5.5.3], and we check the property directly.

**Example 2.2.1 (Narasimhan).** Let $K$ be a field of characteristic 2, and let
$$f = x^2 + y z^3 + z w^3 + y^7 w \in K[x, y, z, w].$$
Let $X = V(f) \subseteq \mathbb{A}^4_K$. Then the points of order 2 of $f$ near the origin are not contained in a smooth hypersurface germ at the origin, also not in a formal one.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

*Proof.* Step 1. The order of $f$ at each point $b$ of $X$ is 1 or 2. Indeed, the Taylor expansion of $f$ at $b$ has the term $x^2$ with the coefficient 1, because $(x + b_1)^2 = x^2 + b_1^2$ in characteristic 2. A point $b$ of $X$ has order 2 if and only if the first partial derivatives of $f$ vanish at $b$. These derivatives are
$$\frac{\partial f}{\partial x} = 0, \quad \frac{\partial f}{\partial y} = z^3 + y^6 w, \quad \frac{\partial f}{\partial z} = y z^2 + w^3, \quad \frac{\partial f}{\partial w} = z w^2 + y^7,$$
because $3 = 1$ and $7 = 1$ in $K$.

Step 2. Let $\gamma(t) = (t^{32}, t^7, t^{19}, t^{15})$. We show that each point of the image of $\gamma$ has order 2. We have
$$y z^3 = t^{64}, \quad z w^3 = t^{64}, \quad y^7 w = t^{64}, \quad x^2 = t^{64},$$
so $f(\gamma(t)) = 4 t^{64} = 0$. Also $z^3 = t^{57} = y^6 w$, $y z^2 = t^{45} = w^3$ and $z w^2 = t^{49} = y^7$, so the three derivatives vanish on $\gamma(t)$. Thus the image of $\gamma$ is a curve $C$ in the locus of order 2, and it contains the origin.

Step 3. Let $h \in K[[x, y, z, w]]$ with $h(0) = 0$ and $h(\gamma(t)) = 0$. We show that $\operatorname{ord} h \ge 2$. A monomial $x^\alpha y^\beta z^\gamma w^\delta$ maps to $t^{32\alpha + 7\beta + 19\gamma + 15\delta}$. Let $S$ be the set of the numbers $32\alpha + 7\beta + 19\gamma + 15\delta$ with $\alpha + \beta + \gamma + \delta \ge 2$. We claim that $7, 15, 19, 32 \notin S$. A sum of at least two of the numbers $7, 15, 19, 32$ is at least $14$. The sums of two are $14, 22, 26, 30, 34, 38, 39, 47, 51, 64$. The sums of three or more that are at most $32$ are $21 = 7 + 7 + 7$, $28 = 7 + 7 + 7 + 7$ and $29 = 7 + 7 + 15$. None of these is $7, 15, 19$ or $32$. Thus the coefficient of $t^7$ in $h(\gamma(t))$ is the coefficient of $y$ in $h$, the coefficient of $t^{15}$ is the coefficient of $w$, the coefficient of $t^{19}$ is the coefficient of $z$, and the coefficient of $t^{32}$ is the coefficient of $x$. All four vanish, so the linear part of $h$ is 0.

Step 4. A smooth hypersurface germ at the origin is $V(h)$ with $\operatorname{ord} h = 1$. If it contains $C$, then $h(\gamma(t)) = 0$, and Step 3 gives $\operatorname{ord} h \ge 2$. This is a contradiction. $\square$

The Lean proof follows Steps 1 to 4. It defines $h(\gamma(t))$ with the substitution of power series of Mathlib, so $h$ is a formal power series. It does not need the hypothesis $h(0) = 0$, because $h(\gamma(t)) = 0$ gives it. The semigroup argument of Step 3 is the lemma `Singularity.Examples.eq_of_weight_eq`, and Step 3 is `Singularity.Examples.two_le_order_of_subst_eq_zero`. Steps 3 and 4 do not use the characteristic.

The proof shows more. The curve $C$ has embedding dimension 4 at the origin, so no smooth subvariety of dimension 3 contains it. Thus no induction on a hypersurface can see all the points of order 2 of $f$. A proof in characteristic $p$ must replace maximal contact. Abramovich discusses the hypersurfaces that realize the characteristic polyhedron as a replacement in [Abr25].

### The residual order goes up

On a hypersurface of maximal contact, the second entry of the invariant of characteristic 0 is the order of the residual factor of the coefficient ideal. It does not go up under a permissible blowup at the points where the order stays the same. Volume 7, Section 1.3, defines the analogue for the purely inseparable equations $z^q + F$, the residual order. Volume 7, Section 1.4, shows that it can go up. Theorem 1.4.1 there, of Moh, bounds the increase in one blowup by $p^{e-1}$, where $q = p^e$.

Node: SG00000015 · Lean: `Singularity.moh_bound` (the statement only, not proved)

Example 1.4.2 of Volume 7 is a point blowup in characteristic 2 along which the residual order goes from 5 to 7. The cycles of Hauser and Perlega [HP19a], Theorem 1.4.3 of Volume 7, are infinite sequences of point blowups along which the residual order goes to infinity.

Node: SG00000017 · Lean: none yet

These examples do not refute resolution, because other centers are permissible (Remark 1.4.4 of Volume 7). But they show that the residual order alone is not an invariant that drops. A proof must add an entry to the invariant that pays for the increases, or it must choose the centers so that the increases do not occur.

### The invariant is not functorial

In characteristic 0 the invariant is compatible with smooth morphisms. This gives two results at the same time. The local blowups glue to a global blowup, and the resolution is compatible with étale maps and with group actions. The weighted method of Abramovich, Temkin and Włodarczyk [ATW24] has the same property. In characteristic $p$ the natural analogues lose it. For the Whitney umbrella in characteristic 2, the natural analogue of the invariant of [ATW24] is not upper semicontinuous, and it is not invariant under smooth morphisms [Abr25, Remark 5.9.3]. Abramovich and Temkin also show that, in characteristic 2, weighted blowups cannot resolve a pinch point in a way that keeps the normal crossings locus [AT26].

Node: SG0000001Q · Lean: `Singularity.weightedBlowup_invariant_lt` (planned, no Lean statement yet)

A different classical method also fails. The Nash blowup replaces each point by the limits of the tangent spaces at nearby regular points. Castillo, Duarte, Leyton-Álvarez and Liendo show that the iteration of the normalized Nash blowup does not resolve some toric varieties of dimension 4 and higher, in each characteristic [CDLL26]. So this method fails in dimension 4 in all characteristics, not only in characteristic $p$.

### Imperfect fields

Over a perfect field, a variety is regular if and only if it is smooth. Over an imperfect field this is false.

**Example 2.2.2.** Let $k = \mathbb{F}_p(t)$ and $A = k[x]/(x^p - t)$. The polynomial $x^p - t$ is irreducible over $k$, because $t$ is not a $p$-th power in $k$. Thus $A$ is a field, and $\operatorname{Spec} A$ is regular. But $\operatorname{Spec} A$ is not smooth over $k$: over the algebraic closure, $x^p - t = (x - t^{1/p})^p$, so $A \otimes_k \bar{k}$ is not reduced.

Node: SG0000000C · Lean: none yet

The proofs of characteristic 0 and the Jacobian criterion use smoothness. Over an imperfect field we must work with regularity, and the Jacobian criterion needs a $p$-basis of $k$. Volume 1 treats the regular locus over an imperfect field. Cossart and Piltant include imperfect fields in dimension 3 [CP19].

### Defect

The last failure is in the theory of valuations. Let $(K, v)$ be a valued field, and let $L/K$ be a finite extension such that $v$ has exactly one extension to $L$. Let $e$ be the ramification index and $f$ the degree of the extension of the residue fields. Then
$$[L : K] = d \, e \, f,$$
where $d$ is a power of the residue characteristic $p$ [Kuh-book]. This is the lemma of Ostrowski. The number $d$ is the *defect* of $L/K$. In residue characteristic 0 the defect is always 1. In residue characteristic $p$ it can be $p$ or more.

Node: SG00000010 · Lean: none yet

**Example 2.2.3.** Let $K$ be the perfect hull of $\mathbb{F}_p((t))$, with the $t$-adic valuation. The value group of $K$ is $\mathbb{Z}[1/p]$ and the residue field is $\mathbb{F}_p$. Let $\vartheta$ be a root of $X^p - X - 1/t$, and let $L = K(\vartheta)$. Let $s_n = \sum_{i=1}^n t^{-1/p^i} \in K$. Then $s_n^p = t^{-1} + s_{n-1}$, so
$$(\vartheta - s_n)^p - (\vartheta - s_n) = t^{-1/p^n}.$$
Thus $v(\vartheta - s_n) = -1/p^{n+1}$. These values increase with $n$ and are bounded by 0. The extension $L/K$ has degree $p$, and $e = f = 1$. So it has defect $p$. We do not give the proof of the last statements, which use the theory of immediate extensions. It is a standard example of [Kuh-book].

The sequence $s_n$ approximates $\vartheta$ better and better, but it does not converge in $K$. This is the behaviour that makes local uniformization hard. In residue characteristic 0, the value group and the residue field determine the degree of each such extension. An extension with defect is different. In Example 2.2.3 the degree is $p$, but the value group and the residue field do not change, so they do not see the extension. Kuhlmann and Rzepka divide the Artin-Schreier defect extensions into dependent and independent ones [KR23]. Cutkosky, Kuhlmann and Rzepka show that a defect extension of degree $p$ is independent if and only if its module of relative Kähler differentials is zero [CKR25]. Cutkosky and Mourtada show that, in their setting, the defect of the extensions that come from projections is the only obstruction to the method of projections [CM17]. Cutkosky also shows that local monomialization, a step of his method in characteristic 0, fails in characteristic $p$ [Cut15].

### Notes and references

The survey [Hau10] gives the failures of this section with more examples. Abramovich's notes [Abr25] explain the failures of the weighted method, and they are the best source for the methods of characteristic 0 since 2018. The book draft [Kuh-book] and the paper [Kuh16] are the sources for defect.
