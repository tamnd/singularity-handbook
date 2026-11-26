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

The first use is the essential one. The chart formulas of Lemma 2.2.6 hold in every characteristic. Theorem 2.2.7 holds over a perfect field of any characteristic, with the theorem of Zariski-Nagata in place of Proposition 2.1.7, because its proof needs only the inequality $\operatorname{ord}_x D^j(I) \ge \operatorname{ord}_x I - j$, and this inequality holds in every characteristic. But in characteristic $p$ the derivative ideal does not compute the order, and the inclusion of Theorem 2.3.3 gives nothing when $MC(I)$ has no element of order 1.

### Small orders

The argument still works when the maximal order is small with respect to the characteristic.

**Proposition 2.4.1.** Let $k$ be a field of characteristic $p > 0$, and let $I$ be an ideal sheaf on a smooth variety over $k$ with closed point $x$ such that $r = \operatorname{ord}_x I$ satisfies $1 \le r < p$, and $k(x)$ is separable over $k$. Then $\operatorname{ord}_x D(I) = r - 1$.

Lean: `Singularity.idealOrd_derivIdeal_of_ne_zero` (at the origin of affine space, with the hypothesis $r \ne 0$ in $k$)

*Proof.* The proof of Lemma 2.1.4 works, because $r$ is a unit in $k$. $\square$

So, at a point of order $m < p$ with $m = \operatorname{max\text{-}ord} I$, the ideal $D^{m-1}(I)$ has order 1, because each of the $m - 1$ steps lowers the order by one by Proposition 2.4.1. A hypersurface of maximal contact exists near the point. If $m < p$ and the residue fields at the closed points are separable over $k$, for example if $k$ is perfect, then Theorem 2.3.3 holds with the same proof. Indeed, the proofs of Proposition 2.1.7, Corollary 2.2.8 and Theorem 2.3.3 use Lemma 2.1.4 and the numbers $\beta!$ only for orders at most $m$, and these are units. This is the reason why the resolution of threefolds in characteristic $p > 5$ can use maximal contact at points of small multiplicity; Volume 6, Proposition 1.2.5, gives the classical form with the Tschirnhausen transformation $z' = z + a_1 / m$, which needs $m$ to be a unit. At points of order $m \ge p$ the method fails, as the next two examples show.

**Example 2.4.2.** Let $k$ have characteristic $p$ and let $f = x^p + y^{p+1}$ on $\mathbb{A}^2$. The maximal order of $f$ is $p$, attained only at the origin. The derivatives are $\partial_x f = 0$ and $\partial_y f = (p+1) y^p = y^p$. So $D(f) = (x^p, y^p)$, and every element of $D^{j}(f)$ has order at least $p$ at the origin for each $j \ge 0$. There is no element of order 1 in any $D^j(f)$, and the derivative ideals give no hypersurface of maximal contact. Here the locus of order $p$ is the origin, so the line $x = 0$ contains it. The failure is a failure of the method. The next example shows that the hypersurface itself can fail to exist.

Lean: `Singularity.DerivativeIdeals.ord_charPExample`, `Singularity.DerivativeIdeals.derivIdeal_charPExample`, `Singularity.DerivativeIdeals.le_idealOrd_derivIdeal_iterate_charPExample`

### The example of Narasimhan

**Example 2.4.3 (Narasimhan).** Let $K$ be a field of characteristic 2, and let
$$f = x^2 + y z^3 + z w^3 + y^7 w \in K[x, y, z, w].$$
Then the points of order 2 of $f$ near the origin are not contained in any smooth hypersurface germ at the origin, also not in a formal one.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

Volume 9, Example 2.2.1, gives the same argument, and the Lean theorem checks it. We give the proof here in full, because it shows which step of this chapter fails. A smooth formal hypersurface germ at the origin is $(h = 0)$ with $h \in \hat R = K[[x, y, z, w]]$ of order 1. Let $J = (f, \partial_x f, \partial_y f, \partial_z f, \partial_w f)$ in $R = K[x, y, z, w]$. We say that a formal germ $(h = 0)$ contains the locus of order 2 if $h$ lies in the radical of $J \hat R$.

*Proof.* Step 1: the order of $f$. Each term of $f$ has degree at least 2, so $f$ has order 2 at the origin. Let $D^{(2)}_x$ be the $K$-linear map of $R$ with $D^{(2)}_x(x^a y^b z^c w^d) = \binom{a}{2} x^{a-2} y^b z^c w^d$, the second Hasse derivative in $x$. It satisfies $D^{(2)}_x(gh) = D^{(2)}_x(g) h + \partial_x g \, \partial_x h + g D^{(2)}_x(h)$. So in the expansion of $D^{(2)}_x$ of a product of $r$ factors, each term differentiates at most two factors. Hence $D^{(2)}_x$ maps $\mathfrak{m}^3$ into $\mathfrak{m}$ for each maximal ideal $\mathfrak{m}$ of $R$. Since $D^{(2)}_x f = 1$, the polynomial $f$ is not in $\mathfrak{m}^3$. So the order of $f$ is at most 2 at every closed point, and the maximal order of $f$ near the origin is $2 = p$.

Step 2: points of order 2. The derivatives are $\partial_x f = 2x = 0$, $\partial_y f = z^3 + y^6 w$, $\partial_z f = y z^2 + w^3$ and $\partial_w f = z w^2 + y^7$, since $3 = 7 = 1$ in $K$. Let $a \in K^4$ be a rational point. In every characteristic, $f(a + t) = f(a) + \sum_i \partial_i f(a) \, t_i + g(t)$ with $g$ of order at least 2 in $t$, because the coefficient of $t_i$ in the expansion of a monomial is its partial derivative at $a$. So $f$ has order 2 at $a$ if and only if $a \in V(J)$. If $K$ is perfect, the residue fields of the closed points are separable over $K$, Lemma 2.1.1 holds with the same proof, and the same argument shows that $V(J)$ is the set of closed points of order 2.

Step 3: the curve. Let $\varphi \colon R \to K[t]$ be the homomorphism with $\varphi(x, y, z, w) = (t^{32}, t^7, t^{19}, t^{15})$. Then
$$\varphi(x^2) = \varphi(y z^3) = \varphi(z w^3) = \varphi(y^7 w) = t^{64},$$
so $\varphi(f) = 4 t^{64} = 0$. Also $\varphi(\partial_y f) = t^{57} + t^{57} = 0$, $\varphi(\partial_z f) = t^{45} + t^{45} = 0$ and $\varphi(\partial_w f) = t^{49} + t^{49} = 0$. So $\varphi(J) = 0$, and the curve $\gamma(t) = (t^{32}, t^7, t^{19}, t^{15})$ lies in $V(J)$. The homomorphism $\varphi$ maps $x, y, z, w$ into $tK[[t]]$, so it extends to a continuous homomorphism $\hat\varphi \colon \hat R \to K[[t]]$ by substitution, and $\hat\varphi(J \hat R) = 0$.

Step 4: no function of order 1 vanishes on the curve. Let $h \in \hat R$ with $\hat\varphi(h) = 0$. Write $h = h_0 + a x + b y + c z + d w + h_2$, with $h_0, a, b, c, d \in K$ and $h_2$ of order at least 2. A monomial of degree $e \ge 2$ maps to $t^s$, where $s$ is a sum of $e$ elements of $\{7, 15, 19, 32\}$, and $s \ge 7e$. So each coefficient of $\hat\varphi(h_2)$ is a finite sum, and $\hat\varphi(h_2)$ has nonzero coefficients only in degrees $s$ that are sums of at least two elements of $\{7, 15, 19, 32\}$. The sums of this kind that are at most 32 are $14, 21, 22, 26, 28, 29$ and $30$. So the coefficients of $1, t^7, t^{15}, t^{19}, t^{32}$ in $\hat\varphi(h)$ are $h_0, b, d, c, a$. They are all zero, and $h$ has order at least 2.

Step 5: conclusion. First let $(h = 0)$ be a formal germ that contains the locus of order 2. Then $h^N \in J \hat R$ for some $N$, so $\hat\varphi(h)^N = 0$. Since $K[[t]]$ is a domain, $\hat\varphi(h) = 0$. Next let $h \in \mathcal{O}_{\mathbb{A}^4, 0}$, and assume that the zero set of $h$ near the origin contains all closed points of order 2 near the origin. A finite field is perfect, so $K$ is perfect or infinite. If $K$ is perfect, the zero set of $h$ contains $V(J)$ near the origin by Step 2, so $h$ lies in the radical of $J \mathcal{O}_{\mathbb{A}^4, 0}$, and $\hat\varphi(h) = 0$ as before. If $K$ is infinite, write $h = g/u$ with $g, u \in R$ and $u(0) \ne 0$. Let $U$ be an open neighborhood of the origin on which $u$ has no zero and $h$ vanishes at all closed points of order 2. The set of $c \in K$ with $\gamma(c) \in U$ is the set of rational points of an open subset of $\mathbb{A}^1$ that contains 0, so it is cofinite in $K$. For such $c$ the point $\gamma(c)$ has order 2 by Steps 2 and 3, so $h(\gamma(c)) = 0$ and $\varphi(g)(c) = g(\gamma(c)) = 0$. So the polynomial $\varphi(g)$ has infinitely many roots, and $\varphi(g) = 0$. Since $\hat\varphi(u)$ is a unit of $K[[t]]$, again $\hat\varphi(h) = 0$. In all cases Step 4 shows that $h$ has order at least 2, so $(h = 0)$ is not smooth at the origin.

A hypersurface that plays the role of $H$ in Theorem 2.3.3 must satisfy part (2) of that theorem for $i = 0$: it must contain $\operatorname{cosupp}(f, 2)$. We have just shown that no smooth hypersurface germ does. $\square$

In the language of this chapter: the maximal order of $f$ near the origin is 2, the ideal
$$D(f) = \big( f, \; z^3 + y^6 w, \; y z^2 + w^3, \; z w^2 + y^7 \big)$$
has order 2 at the origin, not 1, because $f$ has order 2 and the three derivatives have order 3. By Step 2 its zero set is the locus of order 2, at least at the rational points. Lemma 2.1.4 fails for $r = 2 = p$. Compare the same polynomial over a field of characteristic 0. There $\partial_x f = 2x$, so $x \in D(f)$, and $(x = 0)$ is a hypersurface of maximal contact. The curve $\gamma$ is then not in the locus of order 2, since $\varphi(f) = 4t^{64} \ne 0$. In characteristic 2 the terms of $f$ and of its derivatives cancel in pairs on $\gamma$, because $2 = 0$ in $K$. The example is stronger than Example 2.4.2: it shows that no hypersurface, with or without the derivative ideals, can play the role of $H$ in Theorem 2.3.3 at the origin. The curve $\gamma$ has embedding dimension 4 at the origin, so it is not contained in any smooth threefold germ.

### What replaces maximal contact

Giraud studies what remains of maximal contact in positive characteristic in [Gir75]. Another replacement uses hypersurfaces that realize the characteristic polyhedron of Hironaka; Abramovich discusses them in [Abr25], and Volume 9, Section 2.2, explains the problems with them. No replacement is known to give an induction on the dimension in general. This is one of the reasons why resolution in positive characteristic is open in dimension 4 and higher.

### Notes and references

The example of Narasimhan is [Nar83]; we use the form of [Abr25]. The role of the characteristic in the derivative ideals is explained in [Kol07, Chapter 3] and in [Hau03].
