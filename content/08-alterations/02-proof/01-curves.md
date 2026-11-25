---
title: Semistable curves
nodes: [SG0000000V, SG0000004K]
sources: [dJ96, Mat, Liu]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Semistable curves

The last step of the proof of de Jong has a semistable curve over a regular base. The total space of such a curve is not regular in general, but it is close to regular: its singularities have an explicit local form, and explicit blowups resolve them. This section proves the local computations.

### Definitions

**Definition 2.1.1 (semistable curve).** Let $S$ be a scheme. A *semistable curve* over $S$ is a flat proper morphism $f \colon X \to S$ of finite presentation whose geometric fibres are connected curves with at most ordinary double points as singularities. It is *split* if, for each $s \in S$, the irreducible components of $X_s$ are geometrically irreducible and smooth over $\kappa(s)$, and the singular points of $X_s$ are $\kappa(s)$-rational.

This is [dJ96, 2.21 and 2.22]. An ordinary double point of a curve $C$ over an algebraically closed field $\bar k$ is a closed point where the complete local ring is isomorphic to $\bar k[[u, v]]/(uv)$. A pullback of a split semistable curve is split. The closed subscheme $\operatorname{Sing}(f)$ of $X$, defined by the first Fitting ideal of $\Omega_{X/S}$, is the set of points where $f$ is not smooth, and $\operatorname{Sing}(f) \to S$ is finite and unramified [dJ96, 2.21].

**Proposition 2.1.2 (local form).** Let $f \colon X \to S$ be a split semistable curve with $S$ Noetherian, let $x \in \operatorname{Sing}(f)$, and let $s = f(x)$. Let $A$ be the complete local ring of $S$ at $s$. Then the complete local ring of $X$ at $x$ is isomorphic to $A[[u, v]]/(uv - h)$ for some $h$ in the maximal ideal of $A$.

Lean: none yet

This is [dJ96, 2.23]. The proof in [dJ96] goes as follows. In the split case, the fibre has the complete local ring $\kappa(s)[[u, v]]/(uv)$ at $x$. By flatness, the complete local ring of $X$ at $x$ is $A[[u, v]]/(uv - h)$ for some $h$ in the ideal $\mathfrak{m}_A A[[u, v]]$. A new choice of the coordinates $u$ and $v$ makes $h$ an element of $A$. For a semistable curve that is not split, the same holds with $A$ replaced by a finite étale extension $A'$ of $A$ and $uv$ replaced by a quadratic form in $u, v$ with nonzero discriminant.

### When is the total space regular

**Lemma 2.1.3.** Let $(A, \mathfrak{m}_A)$ be a regular local ring of dimension $r$, let $h \in \mathfrak{m}_A$, and let $B = A[[u, v]]/(uv - h)$. Then $B$ is regular if and only if $h \notin \mathfrak{m}_A^2$.

Lean: none yet

*Proof.* The ring $P = A[[u, v]]$ is a regular local ring of dimension $r + 2$, with maximal ideal $\mathfrak{n} = \mathfrak{m}_A P + (u, v)$, and $\mathfrak{n}/\mathfrak{n}^2 = \mathfrak{m}_A/\mathfrak{m}_A^2 \oplus \kappa u \oplus \kappa v$ with $\kappa = A/\mathfrak{m}_A$ [Mat]. A regular local ring is a domain (Volume 1, Theorem 1.3.3), and $uv - h$ is a nonzero element of $\mathfrak{n}$. In a Noetherian local domain, the quotient by a nonzero element of the maximal ideal has dimension one less, since a chain of primes that contain the element extends by the prime 0, and the inequality in the other direction is the principal ideal theorem. So $\dim B = r + 1$. The maximal ideal of $B$ has the cotangent space $\mathfrak{n}/(\mathfrak{n}^2 + (uv - h))$. Since $uv \in \mathfrak{n}^2$, the image of $uv - h$ in $\mathfrak{n}/\mathfrak{n}^2$ is the image of $-h$, which lies in the summand $\mathfrak{m}_A/\mathfrak{m}_A^2$. If $h \notin \mathfrak{m}_A^2$, this image is not zero, the cotangent space has dimension $r + 1 = \dim B$, and $B$ is regular. If $h \in \mathfrak{m}_A^2$, the image is zero, the cotangent space has dimension $r + 2 > \dim B$, and $B$ is not regular. $\square$

**Corollary 2.1.4.** In Lemma 2.1.3, let $t_1, \dots, t_r$ be a regular system of parameters of $A$ and $h = \varepsilon \, t_1^{n_1} \cdots t_r^{n_r}$ with $\varepsilon$ a unit and $n_i \ge 0$, not all 0. Then $B$ is regular if and only if $n_1 + \dots + n_r = 1$.

Lean: none yet

*Proof.* If $\sum n_i \ge 2$, then $h \in \mathfrak{m}_A^2$. If $\sum n_i = 1$, then $h = \varepsilon t_i$ for one $i$, and $t_i \notin \mathfrak{m}_A^2$. Apply Lemma 2.1.3. $\square$

This is the form in which the lemma is used. Let $f \colon X \to S$ be a semistable curve over a regular scheme $S$ that is smooth over the complement of a divisor $D$ with strict normal crossings. At a singular point $x$ of a fibre, the element $h$ of Proposition 2.1.2 defines the image of $\operatorname{Sing}(f)$ near $x$, which lies in $D$. If $t_1, \dots, t_r$ are local equations of the components of $D$ through $f(x)$, then $t_1, \dots, t_r$ is part of a regular system of parameters of $A$, and $h = \varepsilon t_1^{n_1} \cdots t_r^{n_r}$ with $\varepsilon$ a unit [dJ96, 3.3]. Indeed, $A$ is a regular local ring, so it is a unique factorization domain, each $t_i$ is a prime element, and $V(h) \subseteq V(t_1 \cdots t_r)$ implies that $h$ divides a power of $t_1 \cdots t_r$. So $X$ is regular at $x$ exactly when one exponent is 1 and the others are 0.

### Blowups of the model singularities

We now compute blowups on explicit models. The models are of finite type over a field $k$, and they have the same complete local rings as the semistable curves above, so they show what happens for questions that only depend on the completion. De Jong uses the same models [dJ96, 3.3].

We use a fact on domains of finite type over a field. If $C \to C'$ is a surjective homomorphism of domains of finite type over $k$ and $\dim C = \dim C'$, then it is an isomorphism. Indeed, its kernel is a prime ideal $\mathfrak{p}$, and if $\mathfrak{p} \ne 0$, then $\dim C/\mathfrak{p} < \dim C$, because the dimension of a domain of finite type is the transcendence degree of its fraction field, and a nonzero element of $\mathfrak{p}$ becomes 0 in $C/\mathfrak{p}$.

We also use the description of the blowup of an affine scheme $\operatorname{Spec} P$ with $P$ a domain, along an ideal $I = (a_1, \dots, a_m)$ with each $a_i \ne 0$. It is covered by the affine charts $\operatorname{Spec} P[I/a_i]$, where $P[I/a_i]$ is the subring of the fraction field of $P$ generated by $P$ and the quotients $a_j / a_i$ (Volume 4, Section 1.1).

**Proposition 2.1.5.** Let $k$ be a field, let $g \in k[t_1, \dots, t_m]$ be a nonzero polynomial, and let
$$P = k[u, v, t_1, \dots, t_m]/(uv - t_1 g).$$
Then $P$ is a domain of dimension $m + 1$. Let $X' \to X = \operatorname{Spec} P$ be the blowup of the ideal $I = (u, t_1)$. Then $X'$ is covered by two affine charts:

1. the chart $P[t_1/u] \cong k[u, t_1', t_2, \dots, t_m]$, a polynomial ring, with $t_1 = u t_1'$ and $v = t_1' \, g(u t_1', t_2, \dots, t_m)$;
2. the chart $P[u/t_1] \cong k[u', v, t_1, \dots, t_m]/(u'v - g)$, with $u = t_1 u'$.

The blowup is an isomorphism over the complement of the closed subset $V(u, v, t_1, g)$ of $X$.

Lean: none yet

*Proof.* The polynomial $uv - t_1 g$ has degree 1 in $u$, and its coefficient $v$ does not divide $t_1 g$, so it is irreducible, and $P$ is a domain of dimension $(m + 2) - 1 = m + 1$. In $P$ the element $u$ is not zero, so $P$ is a subring of its fraction field $F$, and $t_1/u, u/t_1 \in F$.

Chart 1. Let $C_1 = k[u, t_1', t_2, \dots, t_m]$ and define $C_1 \to P[t_1/u]$ by $t_1' \mapsto t_1/u$. Its image contains $u$, $t_1 = u \cdot (t_1/u)$, $t_2, \dots, t_m$, and $v = t_1 g / u = (t_1/u) g$, so it is surjective. Both rings are domains of dimension $m + 1$: the fraction field of $P[t_1/u]$ is $F$. So the map is an isomorphism by the fact above.

Chart 2. Let $C_2 = k[u', v, t_1, \dots, t_m]/(u'v - g)$. The polynomial $u'v - g$ is irreducible for the same reason as before, so $C_2$ is a domain of dimension $m + 1$. Define $C_2 \to P[u/t_1]$ by $u' \mapsto u/t_1$. This is well defined, because in $F$ we have $(u/t_1) v = uv/t_1 = g$. Its image contains $u = t_1 \cdot (u/t_1)$, so it is surjective. By the fact above it is an isomorphism.

The ideal $I$ is generated by $u$ and $t_1$, so the two charts cover $X'$. Over the open set where $u \ne 0$ or $t_1 \ne 0$, the ideal $I$ is the unit ideal or is generated by one of its generators, so it is invertible. At a point of $V(u, t_1)$ where $v \ne 0$, we have $u = t_1 g / v \in (t_1)$, so $I = (t_1)$ near the point. At a point of $V(u, t_1)$ where $g \ne 0$, we have $t_1 = uv/g \in (u)$, so $I = (u)$ near the point. The blowup of a locally principal ideal generated by a nonzerodivisor is an isomorphism (Volume 4, Section 1.1). So the blowup is an isomorphism outside $V(u, v, t_1, g)$. $\square$

The proposition covers the two cases that occur. In the first case $g = t_1^{n - 1}$, and we get the curve over a curve with the equation $uv = t_1^n$. In the second case $g = t_2 \cdots t_r$ with distinct coordinates, and we get the equation $uv = t_1 \cdots t_r$ of a node over a divisor with strict normal crossings.

**Example 2.1.6 (a curve over a curve).** Let $n \ge 1$ and $P_n = k[u, v, t]/(uv - t^n)$, a surface with a projection to the $t$-line. For $t = c \ne 0$ the fibre is $uv = c^n$, which is smooth and isomorphic to $\mathbb{G}_m$. For $t = 0$ the fibre is $uv = 0$, two lines that meet in an ordinary double point. We claim that $P_n$ is regular if $n = 1$, and that for $n \ge 2$ its only singular point is the origin $\mathfrak{o} = (u, v, t)$.

A prime ideal of $P_n$ that does not contain $u$ is a prime of $P_n[1/u] = k[u, u^{-1}, t]$, because $v = t^n/u$ there, and this ring is regular. The same holds for $v$. A prime that contains $u$ and $v$ contains $t^n = uv$, so it contains $t$, and it is $\mathfrak{o}$. At $\mathfrak{o}$ the local ring has dimension 2. Its cotangent space is $\mathfrak{o}/\mathfrak{o}^2$, the quotient of the span of $u, v, t$ by the linear part of $uv - t^n$. If $n = 1$ the linear part is $-t$, and the cotangent space has dimension 2, so the local ring is regular. If $n \ge 2$ the linear part is 0, the cotangent space has dimension 3, and the local ring is not regular. This proves the claim, and it agrees with Corollary 2.1.4.

Now apply Proposition 2.1.5 with $m = 1$ and $g = t^{n-1}$. The blowup of $(u, t)$ has the charts $k[u, t']$, which is regular, and $k[u', v, t]/(u'v - t^{n-1}) = P_{n-1}$. The blowup is an isomorphism outside $V(u, v, t, t^{n-1}) = \{\mathfrak{o}\}$. The fibre over $\mathfrak{o}$ is the line $v = t = 0$ in the second chart, with coordinate $u'$, glued to the line $u = 0$ in the first chart, with coordinate $t' = 1/u'$. So it is a projective line. The singular point of the chart $P_{n-1}$ has $u' = 0$, so it is not in the first chart, and the ideal $(u', t)$ of the second chart extends by the unit ideal to an ideal on all of $X'$. After $n - 1$ such blowups, each at the singular point of the chart $P_j$ that remains, we get a regular surface with a projective morphism to $\operatorname{Spec} P_n$ that is an isomorphism outside the origin. It is a resolution of $\operatorname{Spec} P_n$ in the sense of Volume 0, Definition 2.1.5. The fibre over the origin is a chain of $n - 1$ projective lines. The fibre over $t = 0$ is this chain together with the strict transforms of the two lines $u = 0$ and $v = 0$, and each of its singular points is an ordinary double point.

There is a second way, which is the one of [dJ96, 3.4]. Let $n \ge 2$ and blow up the maximal ideal $\mathfrak{o} = (u, v, t)$ of $P_n$. The chart $P_n[u/t, v/t]$ is isomorphic to $k[u', v', t]/(u'v' - t^{n-2})$, with $u = tu'$ and $v = tv'$. The chart $P_n[t/u, v/u]$ is isomorphic to the polynomial ring $k[u, t']$, with $t = ut'$ and $v = u^{n-1} t'^n$, and the chart of $v$ is the same with $u$ and $v$ exchanged. The proof is the same as for Proposition 2.1.5: the maps from these rings are surjective, and the source and target are domains of dimension 2. So one blowup of the singular point replaces $n$ by $n - 2$. For $n = 2$ the chart $u'v' = 1$ is smooth, and for $n = 3$ the chart $u'v' = t$ is regular. So $\lfloor n/2 \rfloor$ blowups of points give a regular surface.

**Example 2.1.7 (a node over a divisor with strict normal crossings).** Let $2 \le r \le m$ and $Q_r = k[u, v, t_1, \dots, t_m]/(uv - t_1 \cdots t_r)$. This is the model of a split semistable curve over $\mathbb{A}^m_k$, smooth over the complement of the divisor $t_1 \cdots t_r = 0$, at a point where the image of the singular locus has $r$ branches. By Corollary 2.1.4 it is not regular at the origin. Its singular locus is the union of the linear subspaces $u = v = t_i = t_j = 0$ for $1 \le i < j \le r$, of codimension 3. The closed subset $V(u, t_1)$ is an irreducible component of the inverse image of the divisor $t_1 = 0$. By Proposition 2.1.5 with $g = t_2 \cdots t_r$, its blowup has a chart that is a polynomial ring, and a chart isomorphic to $k[u', v, t_1, \dots, t_m]/(u'v - t_2 \cdots t_r)$, which is the model $Q_{r-1}$ with one factor less. For $r = 2$ the second chart is $u'v = t_2$, which is regular by Corollary 2.1.4. So $r - 1$ blowups of this kind make the model regular.

### The regular model

The local computations give the following theorem of de Jong.

**Theorem 2.1.8 (de Jong).** Let $S$ be an excellent regular scheme, let $D \subseteq S$ be a divisor with strict normal crossings, and let $f \colon X \to S$ be a split semistable curve that is smooth over $S \setminus D$. There is a projective modification $\varphi \colon X_1 \to X$ such that the center of $\varphi$ lies in $\operatorname{Sing}(X)$, the composition $X_1 \to S$ is a split semistable curve smooth over $S \setminus D$, and $X_1$ is regular.

Node: SG0000004K · Lean: none yet

This is [dJ96, Proposition 3.6]. The proof has two steps. First, [dJ96, Lemma 3.2] gives a projective modification with center in $\operatorname{Sing}(X)$ after which $X$ is still a split semistable curve, smooth over $S \setminus D$, and $\operatorname{Sing}(X)$ has codimension at least 3 in $X$. Its proof blows up an irreducible component $T$ of $\operatorname{Sing}(X)$ of codimension 2. Along $T$ the local equation is $uv = \varepsilon t_1^{n}$ with $n \ge 2$, and the blowup of $T$ replaces $n$ by $n - 2$, as in the second part of Example 2.1.6. After these blowups each exponent is 0 or 1, and the local equations are $uv = t_1 \cdots t_\mu$ with $2 \le \mu \le r$, as in Example 2.1.7 [dJ96, 3.5]. Second, one blows up, one at a time, the irreducible components $E$ of the inverse images $f^{-1}(D_i)$ of the components $D_i$ of $D$. Because $f$ is split, at a singular point where $D_i$ is $t_1 = 0$, the component $E$ is given by the ideal $(u, t_1)$ or $(v, t_1)$, and the blowup is computed by Proposition 2.1.5. De Jong shows that the blowups do not change the number of irreducible components of the inverse image of $D$, and that each blowup makes one more of them a Cartier divisor. When all of them are Cartier divisors, the local equation at each point has $\mu = 1$, and $X_1$ is regular by Corollary 2.1.4.

In the proof over a field, de Jong does not use Theorem 2.1.8 itself; he uses it in the case over a trait [dJ96, 6.16]. Over a field he uses Lemma 3.2 and then blows up the components of the singular locus, which keeps control of the divisor $Z$ at each step. We give this in Section 2.4.

### Notes and references

The theory of semistable curves over a discrete valuation ring and their regular models is in [Liu, Chapter 10]. Nothing of this section is in Lean. The algebra of Proposition 2.1.5 is a natural first target: it needs only polynomial rings, fraction fields, and the dimension of domains of finite type.
