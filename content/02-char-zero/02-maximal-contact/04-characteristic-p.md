---
title: Where characteristic zero is used
nodes: [SG00000018, SG0000003A]
sources: [Kol07, Nar83, Abr25, Gir75, Hau03]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Where characteristic zero is used

The proofs of Sections 2.1 to 2.3 use the characteristic in three places.

1. Lemma 2.1.4 divides by the order $r$ in Euler's identity. This gives $\operatorname{ord}_x D(I) = \operatorname{ord}_x I - 1$, hence the description $\operatorname{cosupp}(I, m) = V(D^{m-1}(I))$ and the existence of an element of order 1 in $MC(I)$ at each point of maximal order.
2. Proposition 2.1.7 divides by $\beta!$, with $|\beta| < r$. This gives $I \subseteq I_Z^m$ for each smooth $Z \subseteq \operatorname{cosupp}(I, m)$. In positive characteristic the same statement holds by the theorem of Zariski-Nagata, so this use is not essential.
3. Lemma 2.1.1 uses that the residue fields are separable over $k$. This holds also over a perfect field of positive characteristic.

The first use is the essential one. The chart formulas of Lemma 2.2.6 hold in every characteristic, and so does Theorem 2.2.7. But in characteristic $p$ the derivative ideal does not compute the order, and the inclusion of Theorem 2.3.3 gives nothing when $MC(I)$ has no element of order 1.

### Small orders

The argument still works when the maximal order is small with respect to the characteristic.

**Proposition 2.4.1.** Let $k$ be a field of characteristic $p > 0$, and let $I$ be an ideal sheaf on a smooth variety over $k$ with closed point $x$ such that $r = \operatorname{ord}_x I$ satisfies $1 \le r < p$, and $k(x)$ is separable over $k$. Then $\operatorname{ord}_x D(I) = r - 1$.

Lean: none yet

*Proof.* The proof of Lemma 2.1.4 works, because $r$ is a unit in $k$. $\square$

So, at a point of order $m < p$ with $m = \operatorname{max\text{-}ord} I$, the ideal $D^{m-1}(I)$ has order 1, because each of the $m - 1$ steps lowers the order by one by Proposition 2.4.1. A hypersurface of maximal contact exists near the point. If $m < p$ and the residue fields at the closed points are separable over $k$, for example if $k$ is perfect, then Theorem 2.3.3 holds with the same proof. Indeed, the proofs of Proposition 2.1.7, Corollary 2.2.8 and Theorem 2.3.3 use Lemma 2.1.4 and the numbers $\beta!$ only for orders at most $m$, and these are units. This is the reason why the resolution of threefolds in characteristic $p > 5$ can use maximal contact at points of small multiplicity; Volume 6, Proposition 1.2.5, gives the classical form with the Tschirnhausen transformation $z' = z + a_1 / m$, which needs $m$ to be a unit. At points of order $m \ge p$ the method fails, as the next two examples show.

**Example 2.4.2.** Let $k$ have characteristic $p$ and let $f = x^p + y^{p+1}$ on $\mathbb{A}^2$. The maximal order of $f$ is $p$, attained only at the origin. The derivatives are $\partial_x f = 0$ and $\partial_y f = (p+1) y^p = y^p$. So $D(f) = (x^p, y^p)$, and every element of $D^{j}(f)$ has order at least $p$ at the origin for each $j \ge 0$. There is no element of order 1 in any $D^j(f)$, and the derivative ideals give no hypersurface of maximal contact. Here the locus of order $p$ is the origin, so the line $x = 0$ contains it. The failure is a failure of the method. The next example shows that the hypersurface itself can fail to exist.

Lean: none yet

### The example of Narasimhan

**Example 2.4.3 (Narasimhan).** Let $K$ be a field of characteristic 2, and let
$$f = x^2 + y z^3 + z w^3 + y^7 w \in K[x, y, z, w].$$
Then the points of order 2 of $f$ near the origin are not contained in any smooth hypersurface germ at the origin, also not in a formal one.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

The proof is in Volume 9, Example 2.2.1, and the Lean theorem checks it. We recall its structure. The partial derivatives are $\partial_x f = 0$, $\partial_y f = z^3 + y^6 w$, $\partial_z f = y z^2 + w^3$ and $\partial_w f = z w^2 + y^7$. A point lies in the locus of order 2 if and only if $f$ and these three derivatives vanish there. The curve $\gamma(t) = (t^{32}, t^7, t^{19}, t^{15})$ lies in this locus, since each of the four terms of $f$ becomes $t^{64}$ and the derivatives vanish identically on it. A power series $h$ with $h(\gamma(t)) = 0$ has no linear term, because $7$, $15$, $19$ and $32$ are not sums of two or more elements of $\{7, 15, 19, 32\}$. So no power series of order 1 vanishes on $\gamma$, and no smooth formal hypersurface contains the locus of order 2.

In the language of this chapter: the maximal order of $f$ near the origin is 2, the ideal
$$D(f) = \big( f, \; z^3 + y^6 w, \; y z^2 + w^3, \; z w^2 + y^7 \big)$$
has order 2 at the origin, not 1, and its zero set is the locus of order 2. Lemma 2.1.4 fails for $r = 2 = p$. The example is stronger than Example 2.4.2: it shows that no hypersurface, with or without the derivative ideals, can play the role of $H$ in Theorem 2.3.3 at the origin. The curve $\gamma$ has embedding dimension 4 at the origin, so it is not contained in any smooth threefold germ.

### What replaces maximal contact

Giraud studies what remains of maximal contact in positive characteristic in [Gir75]. Another replacement uses hypersurfaces that realize the characteristic polyhedron of Hironaka; Abramovich discusses them in [Abr25], and Volume 9, Section 2.2, explains the problems with them. No replacement is known to give an induction on the dimension in general. This is one of the reasons why resolution in positive characteristic is open in dimension 4 and higher.

### Notes and references

The example of Narasimhan is [Nar83]; we use the form of [Abr25]. The role of the characteristic in the derivative ideals is explained in [Kol07, Chapter 3] and in [Hau03].
