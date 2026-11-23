---
title: Regular local rings of dimension 1
nodes: [SG00000022, SG00000024]
sources: [AM69, Mat, Stacks, Mathlib, Har]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Regular local rings of dimension 1

In dimension 1 there is a complete description of the regular local rings. A Noetherian local domain of dimension 1 is regular if and only if it is a discrete valuation ring, and if and only if it is integrally closed. The last condition is the important one for geometry. Integral closure is a construction that we can do on each curve, and the theorem tells us that its result is regular. This is the reason why the resolution of curves is easy, and Volume 4 uses it.

Throughout this section, $(R, \mathfrak{m}, \kappa)$ is a Noetherian local domain of dimension 1, and $K$ is its field of fractions.

### The prime ideals

**Lemma 1.4.1.** Let $(R, \mathfrak{m})$ be a Noetherian local domain of dimension 1. Then the prime ideals of $R$ are $0$ and $\mathfrak{m}$.

Lean: `Singularity.Algebra.eq_maximalIdeal_of_isPrime_of_ne_bot`

*Proof.* The ideal $0$ is prime because $R$ is a domain, and $\mathfrak{m}$ is prime because it is maximal. Let $\mathfrak{p} \ne 0$ be a prime ideal. If $\mathfrak{p} \ne \mathfrak{m}$, then $0 \subsetneq \mathfrak{p} \subsetneq \mathfrak{m}$ is a chain of length 2, and this contradicts $\dim R = 1$. Thus $\mathfrak{p} = \mathfrak{m}$. $\square$

A consequence is that $\mathfrak{m}$ is the radical of each nonzero ideal $I \subseteq \mathfrak{m}$. Indeed, the radical of $I$ is the intersection of the prime ideals that contain $I$ [AM69, Proposition 1.14], and the only prime ideal that contains $I$ is $\mathfrak{m}$.

### The theorem

**Theorem 1.4.2.** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local domain of dimension 1. Then the following conditions are equivalent.

1. $R$ is a regular local ring.
2. The ideal $\mathfrak{m}$ is principal.
3. $R$ is a discrete valuation ring.
4. $R$ is integrally closed.

Node: SG00000022 · Lean: `Singularity.Algebra.isRegularLocalRing_iff_isIntegrallyClosed`

We prove $1 \Leftrightarrow 2$, $2 \Rightarrow 3$, $3 \Rightarrow 4$ and $4 \Rightarrow 2$.

*Proof of $1 \Leftrightarrow 2$.* Since $\dim R = 1$, the ring $R$ is regular if and only if $\mu(\mathfrak{m}) = 1$. The ideal $\mathfrak{m}$ is not zero, because $R$ is not a field. Thus $\mu(\mathfrak{m}) = 1$ if and only if $\mathfrak{m}$ is principal. $\square$

*Proof of $2 \Rightarrow 3$.* Let $\mathfrak{m} = (t)$. Then $t \ne 0$. We first show that each nonzero $a \in R$ has the form $a = u t^n$ with $u$ a unit and $n \ge 0$, and that $n$ is unique.

By the Krull intersection theorem [AM69, Corollary 10.20], $\bigcap_{n \ge 0} \mathfrak{m}^n = 0$. Thus there is a largest $n$ such that $a \in \mathfrak{m}^n = (t^n)$. Write $a = u t^n$. If $u \in \mathfrak{m}$, then $a \in \mathfrak{m}^{n+1}$, and this contradicts the choice of $n$. Thus $u$ is a unit. For the uniqueness, assume that $u t^n = u' t^{n'}$ with units $u, u'$ and $n < n'$. Since $R$ is a domain, we can cancel $t^n$ and get $u = u' t^{n'-n} \in \mathfrak{m}$. This is false, because $u$ is a unit.

Now define $v : K^\times \to \mathbb{Z}$ by $v(a/b) = n - m$, where $a = u t^n$ and $b = u' t^m$. The value does not depend on the choice of $a$ and $b$, because $a/b = (u/u') t^{n-m}$, and the uniqueness above shows that the exponent is determined by the element of $K$. The map $v$ is a homomorphism of groups, and $v(x + y) \ge \min(v(x), v(y))$, because $u t^n + u' t^m = t^{\min(n,m)} \cdot (\text{an element of } R)$. An element $x \in K^\times$ is in $R$ if and only if $v(x) \ge 0$. Thus $R$ is the valuation ring of the discrete valuation $v$, and $t$ is a uniformizer. $\square$

*Proof of $3 \Rightarrow 4$.* Each valuation ring is integrally closed [AM69, Proposition 5.18]. We give the argument. Let $v$ be the valuation, let $x \in K$ be integral over $R$, and assume that $x \notin R$. Then $v(x) < 0$, so $x^{-1} \in \mathfrak{m}$. Let
$$x^n + a_1 x^{n-1} + \dots + a_n = 0$$
with $a_i \in R$. Multiply by $x^{-(n-1)}$. Then
$$x = -(a_1 + a_2 x^{-1} + \dots + a_n x^{-(n-1)}),$$
and the right side is in $R$. This is a contradiction. $\square$

*Proof of $4 \Rightarrow 2$.* This is the main step. Let $a \in \mathfrak{m}$ with $a \ne 0$.

*Step 1.* By Lemma 1.4.1, the radical of $(a)$ is $\mathfrak{m}$. In a Noetherian ring, each ideal contains a power of its radical [AM69, Proposition 7.14]. Thus $\mathfrak{m}^n \subseteq (a)$ for some $n$. Let $n$ be the least such number. Since $(a) \ne R$, we have $n \ge 1$. By the choice of $n$, there is an element $b \in \mathfrak{m}^{n-1}$ with $b \notin (a)$.

*Step 2.* Let $y = a/b \in K$. Then $y^{-1} = b/a$, and $y^{-1} \notin R$, because $b \notin (a)$. On the other hand, $b\mathfrak{m} \subseteq \mathfrak{m}^n \subseteq (a)$, so $y^{-1}\mathfrak{m} \subseteq R$. Thus $y^{-1}\mathfrak{m}$ is an ideal of $R$.

*Step 3.* Assume that $y^{-1}\mathfrak{m} \subseteq \mathfrak{m}$. The ideal $\mathfrak{m}$ is a finitely generated $R$-module, and it is a faithful $R[y^{-1}]$-module, since it is a nonzero submodule of the field $K$. By [AM69, Proposition 5.1], the element $y^{-1}$ is integral over $R$. Since $R$ is integrally closed, $y^{-1} \in R$, and this contradicts Step 2.

*Step 4.* Thus $y^{-1}\mathfrak{m}$ is an ideal of $R$ that is not contained in $\mathfrak{m}$. Since $R$ is local, $y^{-1}\mathfrak{m} = R$, that is, $\mathfrak{m} = yR$. In particular $y = y \cdot 1 \in \mathfrak{m} \subseteq R$, and $\mathfrak{m} = (y)$ is principal. $\square$

The proof of $4 \Rightarrow 2$ is the proof of [AM69, Proposition 9.2]. It is useful to see where each hypothesis is used. The dimension is 1 in Step 1, where it makes $\mathfrak{m}$ the radical of $(a)$. The ring is Noetherian in Step 1 and in Step 3. The ring is integrally closed in Step 3. Example 1.4.6 below shows that the theorem is false in dimension 2.

### Normal curves are regular

A scheme $X$ is *normal* if each local ring $\mathcal{O}_{X,x}$ is an integrally closed domain [Har, Chapter II, Exercise 3.8].

**Corollary 1.4.3.** Let $X$ be a normal locally Noetherian scheme with $\dim X \le 1$. Then $X$ is regular.

Node: SG00000024 · Lean: `Singularity.isRegularScheme_of_isIntegrallyClosed_stalk`

*Proof.* Let $x \in X$ and let $R = \mathcal{O}_{X,x}$. Then $R$ is a Noetherian local domain that is integrally closed, and $\dim R \le \dim X \le 1$ (Volume 9, Lemma 1.1.2). If $\dim R = 0$, then $0$ is the only prime ideal of the domain $R$, so $\mathfrak{m} = 0$ and $R$ is a field. A field is regular (Example 1.2.2). If $\dim R = 1$, then $R$ is regular by Theorem 1.4.2. $\square$

For a curve $X$ over a field, Corollary 1.4.3 reduces the resolution to the construction of the normalization $\tilde{X} \to X$. Volume 4 shows that the normalization is a resolution when it is a finite morphism, and the finiteness is a theorem of E. Noether for varieties [Har, Chapter I, Theorem 3.9A]. Chapter 2 proves the finiteness in characteristic 0 (Corollary 2.3.5), and the Lean development has this case. The case of characteristic $p$ is still open in Lean.

### Examples

**Example 1.4.4 (the cusp).** Let $R = k[x, y]_{(x,y)}/(y^2 - x^3)$, as in Example 1.2.4. We showed there that $R$ is not regular. By Theorem 1.4.2, $R$ is not integrally closed. We can see this directly. Let $t = y/x \in K$. Then
$$t^2 = \frac{y^2}{x^2} = \frac{x^3}{x^2} = x,$$
so $t$ is a root of the monic polynomial $T^2 - x$ over $R$, and $t$ is integral over $R$. But $t \notin R$. Indeed, if $y = xr$ for some $r \in R$, then $y \in (x)$, and so the class of $y$ is zero in $R/(x) = k[y]_{(y)}/(y^2)$. This is false.

The element $t$ gives the normalization of the cusp. We have $x = t^2$ and $y = tx = t^3$, so the affine curve $y^2 = x^3$ is the image of the map $t \mapsto (t^2, t^3)$ from the affine line, and its coordinate ring is $k[t^2, t^3] \subseteq k[t]$. The integral closure is $k[t]$, which is regular. The map from the line to the cusp is a bijection, but it is not an isomorphism.

**Example 1.4.5 (the node).** Let $k$ be a field of characteristic different from 2, and let $R = k[x, y]_{(x,y)}/(y^2 - x^2(x + 1))$. This is the local ring at the origin of a plane curve that crosses itself at the origin. The same argument as in Example 1.2.4 shows that $\dim R = 1$ and $\operatorname{edim} R = 2$, so $R$ is not regular. The element $t = y/x$ satisfies
$$t^2 = \frac{y^2}{x^2} = x + 1,$$
so it is integral over $R$, and it is not in $R$ by the argument of Example 1.4.4. The normalization of the affine curve is the line with the coordinate $t$, and the map is $t \mapsto (t^2 - 1, t^3 - t)$. The two points $t = 1$ and $t = -1$ go to the origin. They are different points because the characteristic is not 2. The two branches of the curve at the origin are separated in the normalization.

**Example 1.4.6 (the cone).** The dimension 1 hypothesis in Theorem 1.4.2 is necessary. Let $k$ be a field and let $A = k[x, y, z]/(xy - z^2)$. Let $R$ be the localization of $A$ at the ideal $(x, y, z)$. Then $R$ is integrally closed, but it is not regular.

First, $R$ is not regular. Let $B = k[x, y, z]_{(x,y,z)}$, a regular local ring of dimension 3 (Example 1.2.3). The element $xy - z^2$ is in $\mathfrak{m}_B^2$, so $\operatorname{edim} R = 3$ by Lemma 1.1.5. The element $xy - z^2$ is not zero and $B$ is a domain, so $\dim R = 3 - 1 = 2$ by [AM69, Corollary 11.18].

Next, $R$ is integrally closed. Let $S \subseteq k[u, v]$ be the subring of the polynomials that have only terms of even degree. The map $A \to S$ with $x \mapsto u^2$, $y \mapsto v^2$ and $z \mapsto uv$ is well defined, because $u^2 v^2 = (uv)^2$. It is surjective, because the monomials of degree $2n$ are the products of $n$ elements of $\{u^2, uv, v^2\}$. Give $x, y, z$ the degree 1 and $u, v$ the degree 1. Then the map sends the part of degree $n$ of $A$ onto the part of degree $2n$ of $S$. Since $xy - z^2$ is homogeneous of degree 2, the part of degree $n$ of $A$ has dimension $\binom{n+2}{2} - \binom{n}{2} = 2n + 1$, and the part of degree $2n$ of $k[u, v]$ also has dimension $2n + 1$. Thus the map is an isomorphism $A \cong S$.

Now let $f \in \operatorname{Frac}(S)$ be integral over $S$. Then $f$ is integral over $k[u, v]$, and $k[u, v]$ is integrally closed. Indeed, $k[u, v]$ is a unique factorization domain. Write an element of its field of fractions as $g'/h'$ with no common prime factor. If it is a root of a monic polynomial of degree $m$, then $h'$ divides $g'^m$, so $h'$ has no prime factor, and $h'$ is a unit. Thus $f \in k[u, v]$. Write $f = g/h$ with $g, h \in S$ and $h \ne 0$, and write $f = f_0 + f_1$, where $f_0$ has the terms of even degree and $f_1$ has the terms of odd degree. Then $f_1 h = g - f_0 h$. The left side has only terms of odd degree, and the right side has only terms of even degree. Thus $f_1 h = 0$, so $f_1 = 0$ and $f \in S$. This shows that $S$ is integrally closed. A localization of an integrally closed domain is integrally closed [AM69, Proposition 5.12], so $R$ is integrally closed.

Geometrically, $V(xy - z^2) \subseteq \mathbb{A}^3_k$ is a cone over a conic. It is normal, and its vertex is a singular point. Normalization resolves the singularities of curves, but it does not resolve the singularities of surfaces.

### The Lean proof

The equivalence $1 \Leftrightarrow 3$ is `Singularity.Algebra.isRegularLocalRing_iff_isDiscreteValuationRing`, and the equivalence $1 \Leftrightarrow 4$ is `Singularity.Algebra.isRegularLocalRing_iff_isIntegrallyClosed`. Both take the hypothesis `ringKrullDim R = 1`, with `R` a Noetherian local domain.

The proofs are short, because Mathlib has the theorem `IsDiscreteValuationRing.TFAE`. It gives seven equivalent conditions for a Noetherian local domain that is not a field, among them "$R$ is a discrete valuation ring", "$R$ is integrally closed and has exactly one nonzero prime ideal", and "the cotangent space has dimension 1". The Lean proof does three things. It shows that $R$ is not a field, since a field has dimension 0. It uses `IsRegularLocalRing.iff_finrank_cotangentSpace` to write regularity as "the cotangent space has dimension $\dim R = 1$". For condition 4, it shows that $\mathfrak{m}$ is the only nonzero prime ideal, which is Lemma 1.4.1. The Lean proof of Lemma 1.4.1 uses heights of prime ideals: the height of $\mathfrak{m}$ is $\dim R = 1$, so a prime ideal $\mathfrak{p} \subsetneq \mathfrak{m}$ has height 0, and in a domain this means $\mathfrak{p} = 0$.

The Lean proof of Corollary 1.4.3 is `Singularity.isRegularScheme_of_isIntegrallyClosed_stalk` in the file `Singularity/Scheme/NormalDimOne.lean`. Mathlib has no class for normal schemes, so the theorem takes two hypotheses on the local rings: each local ring is a domain, and each local ring is integrally closed. The proof has two steps. First, the lemma `Singularity.ringKrullDim_stalk_le_topologicalKrullDim` gives $\dim \mathcal{O}_{X,x} \le \dim X$. Its proof identifies $\dim \mathcal{O}_{X,x}$ with the length of the longest chain of irreducible closed sets that contain $x$, with the Mathlib lemma `ringKrullDim_stalk_eq_coheight`. Second, the theorem `Singularity.isRegularLocalRing_of_isIntegrallyClosed` treats the local rings of dimension 0 and 1, as in the proof above. The examples are not yet in Lean.

### Notes and references

Theorem 1.4.2 is [AM69, Proposition 9.2] and [Mat, Theorem 11.2]. Atiyah and Macdonald list two more equivalent conditions: each nonzero ideal is a power of $\mathfrak{m}$, and there is $t$ such that each nonzero ideal is $(t^k)$ for some $k \ge 0$. The theorem is the local part of the theory of Dedekind domains [AM69, Chapter 9]: a Noetherian domain of dimension 1 is a Dedekind domain if and only if it is integrally closed, and if and only if each of its localizations at a nonzero prime ideal is a discrete valuation ring.

In higher dimension, a regular local ring is integrally closed (Section 1.3 states this result without proof), but the converse is false, as Example 1.4.6 shows. Serre's criterion says that a Noetherian domain is normal if and only if it is regular in codimension 1 and satisfies the condition $S_2$ [Mat, Theorem 23.8]. Thus a normal variety is regular outside a closed subset of codimension at least 2.
