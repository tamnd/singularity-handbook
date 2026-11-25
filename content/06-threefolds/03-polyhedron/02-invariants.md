---
title: The invariants of Cossart and Piltant
nodes: [SG00000014, SG00000013, SG00000015]
sources: [CP19, Hir67, Mat, Moh87, Moh14, HP19a]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The invariants of Cossart and Piltant

In this section we define the invariants $\delta$, $d_j$, $\epsilon$ and $\omega$ of [CP19, Sections 2.1, 2.2, 2.5 and 2.7], and we prove their first properties. For the purely inseparable equations $X^p + f$ over a perfect field we prove that the cleaning of Volume 7, Section 1.3, gives the minimal polyhedron, without the theorem of Hironaka. Then $\epsilon$ is the residual order of Volume 7. We state the theorem of Cossart and Piltant that the invariant $\iota = (m, \omega, \kappa)$ does not increase under permissible blowups.

We keep the notation of Section 3.1, with $S = k[[u_1, \dots, u_n]]$ in the proofs. Let $X = \operatorname{Spec} S[X]/(h)$ and let $\eta \colon X \to \operatorname{Spec} S$ be the projection. For a point $y \in X$ with prime ideal $M_y \subset S[X]$, the *multiplicity* $m(y)$ is the order of $h$ in the regular local ring $S[X]_{M_y}$, as in Section 1.2. By Theorem 3.1.5(1) there are translations $Z = X - \theta$ such that $\Delta(h; u; Z)$ is minimal.

### The invariant delta

**Definition 3.2.1.** Let $Z$ be such that $\Delta(h; u; Z)$ is minimal. Then
$$\delta(x) = \delta_{\mathbf{1}}(h; u; Z) = \min \{ x_1 + \dots + x_n : x \in \Delta(h; u; Z) \} = \min_{1 \le i \le m} \frac{\operatorname{ord} f_{i, Z}}{i},$$
where $\mathbf{1} = (1, \dots, 1)$ and $\operatorname{ord}$ is the order for $\mathfrak{m}_S$.

Lean: none yet

The last equality is Lemma 3.1.2(3), since $\mu_{\mathbf{1}} = \operatorname{ord}$. This is [CP19, Definition 2.11] at the closed point. By Lemma 3.1.2(1), $\delta(x) \in \frac{1}{m!} \mathbb{N}$.

**Proposition 3.2.2.** Let $S = k[[u]]$.

1. The number $\delta(x)$ does not depend on the regular system of parameters $u$ or on the choice of $Z$. It equals $\max_{\varphi} \min_i \operatorname{ord} f_{i, X - \varphi} / i$ over $\varphi \in S$.
2. $\delta(x) > 0$ if and only if $\eta^{-1}(\mathfrak{m}_S)$ is one point $x$ with residue field $k$.
3. $\delta(x) \ge 1$ if and only if $\eta^{-1}(\mathfrak{m}_S)$ contains a point of multiplicity $m$. In this case the point is $x = (\mathfrak{m}_S, Z)$.

Lean: none yet

*Proof.* Part 1. Let $\Delta(h; u; Z)$ be minimal. By Theorem 3.1.5(2), it is contained in $\Delta(h; u; X - \varphi)$ for each $\varphi$, so $\delta_{\mathbf 1}(h; u; Z) \ge \min_i \operatorname{ord} f_{i, X - \varphi}/i$ for each $\varphi$, with equality for $\varphi = \theta$. So $\delta(x)$ is the maximum in part 1. The order, the elements $f_{i, X - \varphi}$ and the set of the $\varphi$ do not depend on $u$, so neither does the maximum.

Part 2. The fiber is $\operatorname{Spec} k[Z]/(\bar h)$, where $\bar h$ is the image of $h$ in $k[Z]$. It is one point with residue field $k$ if and only if $\bar h = (Z - \lambda)^m$ for some $\lambda \in k$. If $\delta(x) > 0$, then each $f_{i, Z}$ lies in $\mathfrak{m}_S$, so $\bar h = Z^m$. Conversely, let $\delta(x) = 0$. Then $0 \in \Delta(h; u; Z)$, and $0$ is a vertex, since the polyhedron lies in the orthant. Its initial form is $\bar h$, since the terms of weight $0$ are the constant terms. If $\bar h = (Z - \lambda)^m$ with $\lambda \in k$, the vertex $0$ is solvable, and Lemma 3.1.4 gives a strictly smaller polyhedron. This contradicts the minimality. So the fiber is not one rational point.

Part 3. The ring $S[Z]$ localized at $M = (\mathfrak{m}_S, Z)$ is regular with the regular system of parameters $(u, Z)$, so its graded ring is $k[U_1, \dots, U_n, Z]$ [Mat]. Let $d_i = \operatorname{ord} f_{i, Z}$ and $d_0 = 0$. The initial form of $f_{i, Z} Z^{m - i}$ has degree $d_i + m - i$ and contains $Z$ exactly to the power $m - i$. So the initial forms of the terms of smallest degree cannot cancel, and the order of $h$ at $M$ is $\min_i (d_i + m - i)$. It is $m$ if and only if $d_i \ge i$ for each $i$, that is, $\delta(x) \ge 1$. This proves "if". Conversely, let $y$ be a point of the fiber with $m(y) = m$. Then $h \in M_y^m S[Z]_{M_y}$. The image of $h$ in the discrete valuation ring $k[Z]_{\bar M_y}$ lies in the $m$-th power of its maximal ideal. Let $T \in k[Z]$ be the monic irreducible polynomial of $y$. Then $T^m$ divides $\bar h$, and $\bar h$ has degree $m$, so $T = Z - \lambda$ and $\bar h = (Z - \lambda)^m$ with $\lambda \in k$. By part 2 and its proof, $\lambda = 0$, so $y = (\mathfrak{m}_S, Z)$, and $\delta(x) \ge 1$ by the first half of this proof. $\square$

This is [CP19, Proposition 2.10], which holds for each regular local ring $S$. The proof there is the same.

### The invariants of the divisor

Let $E = \operatorname{div}(u_1 \cdots u_e)$ with $0 \le e \le n$. The coordinates $(u; Z)$ are *well adapted* if $\Delta(h; u; Z)$ is minimal [CP19, Definition 2.24].

**Definition 3.2.3.** Let $(u; Z)$ be well adapted. For $1 \le j \le e$ let
$$d_j = \min \{ x_j : x \in \Delta(h; u; Z) \}, \qquad \epsilon(x) = m \Bigl( \delta(x) - \sum_{j = 1}^{e} d_j \Bigr).$$

Lean: none yet

Cossart and Piltant define $d_j$ as $\delta$ at the generic point of a component of $\eta^{-1}(\operatorname{div}(u_j))$, and they prove that it equals the minimum above [CP19, Definition 2.25 and Proposition 2.26]. So $d_j$ depends only on $\operatorname{div}(u_j)$, and $\epsilon(x)$ depends only on $(S, h, E)$. Each point of the polyhedron has $x_j \ge d_j$, so $\delta(x) \ge \sum_j d_j$ and $\epsilon(x) \ge 0$.

### Cleaning gives the minimal polyhedron

Now let $k$ be a perfect field of characteristic $p$, let $S = k[[u]]$, and let $h = X^p + f$ with $f \in S$. A translation $X' = X - \varphi$ gives $h = X'^p + \varphi^p + f$, because $\binom{p}{i} = 0$ in $k$ for $0 < i < p$. So $f_{i, X'} = 0$ for $i < p$, $f_{p, X'} = f + \varphi^p$, and
$$\Delta(h; u; X') = \tfrac{1}{p} N(f + \varphi^p).$$
Let $f^{\mathrm{cl}}$ be the clean part of $f$ for $q = p$ (Volume 7, Definition 1.3.1), and let $g \in S$ with $g^p + f = f^{\mathrm{cl}}$ (Volume 7, Lemma 1.3.2). We assume $f^{\mathrm{cl}} \ne 0$. Otherwise $h = (X + g)^p$ is not reduced.

**Proposition 3.2.4.** Let $Z = X - g$, so that $h = Z^p + f^{\mathrm{cl}}$. Let $r_j$ be the largest integer with $u_j^{r_j} \mid f^{\mathrm{cl}}$, and write $f^{\mathrm{cl}} = u_1^{r_1} \cdots u_e^{r_e} G$.

1. $\Delta(h; u; Z) = \frac{1}{p} N(f^{\mathrm{cl}})$ is contained in $\Delta(h; u; X - \varphi)$ for each $\varphi \in S$. So it is the characteristic polyhedron $\Delta(h; u)$, and no vertex of it is in $\mathbb{N}^n$.
2. $\delta(x) = \operatorname{ord} f^{\mathrm{cl}} / p$, and $\operatorname{ord} f^{\mathrm{cl}} = \max_{\varphi \in S} \operatorname{ord}(f + \varphi^p)$.
3. $d_j = r_j / p$, and $r_j = \max_{\varphi \in S} \operatorname{ord}_{u_j}(f + \varphi^p)$, where $\operatorname{ord}_{u_j}$ is the valuation of the prime ideal $(u_j)$.
4. $\epsilon(x) = \operatorname{ord} f^{\mathrm{cl}} - \sum_{j = 1}^{e} r_j = \operatorname{ord} G$, the residual order of $Z^p + f^{\mathrm{cl}}$ for $E$ in Volume 7, Definition 1.3.3.
5. The numbers $\operatorname{ord} f^{\mathrm{cl}}$, $r_j$ and $\epsilon(x)$ do not change if we replace $u$ by another regular system of parameters $u'$ with $\operatorname{div}(u'_j) = \operatorname{div}(u_j)$ for $j \le e$, and compute the clean part in an expansion in $u'$.

Node: SG00000013 · Lean: `Singularity.residualOrder` (the definition of the residual order); the inclusion of part 1 is Volume 7, Proposition 1.2.7(1), which has a Lean proof, and the rest of Proposition 3.2.4 has no Lean proof

*Proof.* Part 1. Let $\varphi \in S$ and $\chi = \varphi - g$. Then $f + \varphi^p = f^{\mathrm{cl}} - g^p + \varphi^p = f^{\mathrm{cl}} + \chi^p$. If $\chi = \sum_b c_b u^b$, then $\chi^p = \sum_b c_b^p u^{p b}$, because the Frobenius map is additive and continuous. So the support of $\chi^p$ lies in $p \mathbb{N}^n$, and the support of $f^{\mathrm{cl}}$ does not meet $p \mathbb{N}^n$. Thus no cancellation occurs, and $\operatorname{supp}(f + \varphi^p) \supseteq \operatorname{supp} f^{\mathrm{cl}}$. So $N(f + \varphi^p) \supseteq N(f^{\mathrm{cl}})$, which proves the inclusion. The minimum over $\varphi \in \hat S = S$ is attained at $\varphi = g$, so this is the characteristic polyhedron. Its vertices are points $a/p$ with $a \in \operatorname{supp} f^{\mathrm{cl}}$ (Volume 7, Lemma 1.2.2). Since $a \notin p \mathbb{N}^n$, $a/p \notin \mathbb{N}^n$.

Part 2. By Volume 7, Proposition 1.2.3, the minimum of $x_1 + \dots + x_n$ on $\frac{1}{p} N(f^{\mathrm{cl}})$ is $\operatorname{ord} f^{\mathrm{cl}} / p$. The order of a series is the smallest degree in its support. With $\chi$ as in part 1, the support of $f + \varphi^p$ contains that of $f^{\mathrm{cl}}$, so $\operatorname{ord}(f + \varphi^p) \le \operatorname{ord} f^{\mathrm{cl}}$, with equality for $\varphi = g$.

Part 3. The minimum of $x_j$ on $\frac{1}{p} N(f^{\mathrm{cl}})$ is $\frac{1}{p} \min \{ a_j : a \in \operatorname{supp} f^{\mathrm{cl}} \} = r_j / p$. The same argument as in part 2, with $\operatorname{ord}_{u_j}$ in place of $\operatorname{ord}$, gives the maximum.

Part 4. By the definitions, $\epsilon(x) = p (\operatorname{ord} f^{\mathrm{cl}}/p - \sum_j r_j/p) = \operatorname{ord} f^{\mathrm{cl}} - \sum_j r_j$. The order is additive on products, because the graded ring $k[U_1, \dots, U_n]$ is a domain. So $\operatorname{ord} f^{\mathrm{cl}} = \sum_j r_j + \operatorname{ord} G$.

Part 5. Let $u'$ be another regular system of parameters. By the structure theorem of Cohen [Mat], $S = k'[[u']]$ for a coefficient field $k'$, and $k' \cong k$ is perfect. Parts 2 and 3 hold in this expansion. The maxima in parts 2 and 3 depend only on $S$, on $f$ and on the ideals $(u_j)$. So they are the same for $u$ and for $u'$. $\square$

Part 4 shows that $\epsilon$ is the residual order of Volume 7 for the equations $z^p + F$, and part 5 shows that, in this case, it does not depend on the coordinates that keep $E$. Volume 7, Proposition 1.3.5, proves part 5 for each $q = p^e$ by the same argument. Part 1 is the special case of Theorem 3.1.5 that one can prove in a few lines. For $h = X^q + f$ with $q = p^e$ and $e \ge 2$ the same proof shows that the clean part for $q$ gives the minimal polyhedron among the translations of $X$.

### The invariant omega

We keep $k$ perfect, $S = k[[u]]$, $h = Z^p + f^{\mathrm{cl}}$ with $(u; Z)$ well adapted, and $E = \operatorname{div}(u_1 \cdots u_e)$. Assume $m(x) = p$, that is, $\operatorname{ord} f^{\mathrm{cl}} \ge p$ by Proposition 3.2.2(3). Let $F \in k[U_1, \dots, U_n]$ be the initial form of $f^{\mathrm{cl}}$, of degree $p \delta(x)$. Then the initial form of $h$ for the weight $\mathbf{1}$ is $\operatorname{in} h = Z^p + F$, with $Z$ of degree $\delta(x)$. With the notation of Proposition 3.2.4, $F = U_1^{r_1} \cdots U_e^{r_e} \operatorname{in}(G)$.

**Definition 3.2.5.** Let
$$\omega(x) = \begin{cases} \epsilon(x) - 1 & \text{if } \partial F / \partial U_j \ne 0 \text{ for some } j \text{ with } e < j \le n, \\ \epsilon(x) & \text{otherwise.} \end{cases}$$
Let $\kappa(x) = 1$ if $\omega(x) = 0$. Otherwise we write $\kappa(x) \ge 2$, and we do not distinguish the values $\ge 2$ until Chapter 4. If $m(x) < p$, let $\omega(x) = 0$ and $\kappa(x) = 1$. The invariant of $x$ is $\iota(x) = (m(x), \omega(x), \kappa(x))$, ordered lexicographically.

Lean: none yet

This is the case of [CP19, (1.11) and Definitions 2.67 and 2.68] for a purely inseparable $h$ over a perfect residue field. In general Cossart and Piltant use a module of logarithmic derivatives, which also contains the derivatives of a $p$-basis of the residue field, and the Artin-Schreier case $\operatorname{in} h = Z^p - G^{p - 1} Z + F$ needs more care. They prove that $\omega(x)$ does not depend on the choice of the well adapted coordinates [CP19, Remark 2.69]. Since $\partial F/\partial U_j = U_1^{r_1} \cdots U_e^{r_e} \, \partial \operatorname{in}(G)/\partial U_j$ for $j > e$, we have $\omega(x) = \epsilon(x) - 1$ exactly when $\operatorname{in}(G)$ contains a monomial in which some $U_j$ with $j > e$ has an exponent prime to $p$. If $\epsilon(x) = 0$, then $F$ is a monomial in $U_1, \dots, U_e$, and $\omega(x) = 0$. For $n = 3$, Cossart and Piltant refine $\kappa(x) \ge 2$ to a value in $\{2, 3, 4\}$ [CP19, Chapter 5]. The values of $\iota$ lie in $\{1, \dots, p\} \times \mathbb{N} \times \{1, 2, 3, 4\}$, and the induction of [CP19] is on this ordered set.

The value of $\omega$ is not determined by the polyhedron [CP19, Remark 2.70]. Section 3.3 computes the example of that remark for $p = 3$.

### The behavior under blowups

Let $Y \subset X$ be an integral closed subscheme that contains $x$, with generic point $y$ and $m(y) = p$. It is *permissible of the first kind* at $x$ if it is Hironaka-permissible for $E$ at $x$ and $\epsilon(y) = \epsilon(x)$ [CP19, Definition 3.1]. The point $Y = \{x\}$ is always permissible of the first kind. It is *permissible of the second kind* if it is Hironaka-permissible, $\epsilon(y) = \epsilon(x) - 1$, and two more conditions hold [CP19, Definition 3.5]. Cossart and Piltant show by an example that resolution by Hironaka-permissible blowups can require a curve of the second kind [CP19, Example 3.6]. For the blowup $\pi$ along such a center, let $x' \in \pi^{-1}(x)$, let $s'$ be its image in the blowup of $\operatorname{Spec} S$, let $S'$ be the local ring at $s'$ and let $E'$ be the reduced total transform of $E$ at $s'$. The strict transform of $h$ defines the triple $(S', h', E')$, and $\iota(x')$ is computed for it.

**Theorem 3.2.6 (Cossart-Piltant).** Let $S$ be an excellent regular local ring of dimension $n \ge 1$ with residue field of characteristic $p$. Let $h \in S[X]$ be a reduced monic polynomial of degree $p$ that satisfies condition 1 or condition 2 of Theorem 1.2.6, and assume that $(S, h, E)$ satisfies condition (E). Let $x$ be the point over $\mathfrak{m}_S$ with $m(x) = p$, and assume $\omega(x) > 0$. Let $\pi$ be the blowup along a center $Y$ that is permissible of the first or the second kind at $x$, with generic point $y$, and let $x' \in \pi^{-1}(x)$. Then
$$\iota(x') \le \iota(x).$$ If $\epsilon(x') > \epsilon(x)$, then in well adapted coordinates $(u; Z)$ the initial form $\operatorname{in}_{\mathbf{1}} h$ of Definition 3.1.3 has no terms in $Z^1, \dots, Z^{p-1}$ (the case $i_0 = p$ of [CP19]), $\epsilon(y) = \epsilon(x) = \omega(x)$, and $\delta(y) \in \mathbb{N}$.

Lean: none yet

This is part of [CP19, Theorem 3.13]. The values $\kappa \ge 2$ are not distinguished there, as in [CP19, (2.76)]. The theorem holds in each dimension $n$. It also says that in the case of equality $x'$ lies in a certain projective cone, and it gives the form of $F$ when $\epsilon$ increases. We do not prove it. Its proof fills Chapter 3 of [CP19].

**Theorem 3.2.7 (Cossart-Piltant).** In the situation of Theorem 3.2.6, assume $\omega(x) = 0$ instead. Then for each valuation $\mu$ of $L$ with center $x$ there is a finite sequence of local Hironaka-permissible blowups along $\mu$ after which the multiplicity of the center of $\mu$ is less than $p$.

Lean: none yet

This is [CP19, Theorem 2.81]. Its proof is combinatorial, as in characteristic 0: it finds a center for which $\delta$ drops, and $\delta \in \frac{1}{p!} \mathbb{N}$ cannot drop forever. So the hard case of Theorem 1.2.6 is $m(x) = p$ and $\omega(x) > 0$.

### Comparison with Moh's bound

Theorem 3.2.6 explains why Cossart and Piltant use $\omega$ and not $\epsilon$. By Proposition 3.2.4(4), $\epsilon$ is the residual order. Moh's bound, Theorem 1.4.1 of Volume 7 with $q = p$, says that a point blowup can increase the residual order by at most $p^0 = 1$.

Node: SG00000015 · Lean: `Singularity.moh_bound_holds` (for point blowups of polynomials)

The residual order can increase by $1$ (Section 3.3). Since $\omega \in \{\epsilon - 1, \epsilon\}$, an increase of $\epsilon$ by $1$ can leave $\omega$ unchanged. Theorem 3.2.6 says that this is what happens: under its hypotheses, $\omega$ does not increase. For $q = p^e$ with $e \ge 2$ the increase of the residual order can be larger (Volume 7, Example 1.4.2 and Theorem 1.4.3). The reduction of Chapter 2 needs only equations of degree $p$, so this case does not occur in [CP19]. Cossart and Piltant know no analogue of $\omega$ with the properties of Theorem 3.2.6 for the equations $X^{p^e} + f$ with $e \ge 2$, and they refer to the work of Moh [Moh14] and of Hauser and Perlega [HP19a] on these equations [CP19, Section 1].

**Example 3.2.8.** Let $p = 3$, let $k$ be perfect of characteristic 3, let $S = k[[u_1, u_2, u_3]]$, let $h = Z^3 + u_1 u_2 u_3$ and let $E = \operatorname{div}(u_1 u_2 u_3)$. This is Example 2.3.4 at the origin. The series $f = u_1 u_2 u_3$ is clean, so $(u; Z)$ is well adapted and $\Delta(h; u) = (\frac13, \frac13, \frac13) + \mathbb{R}_{\ge 0}^3$. So $\delta(x) = 1$ and $m(x) = 3$. Further $d_1 = d_2 = d_3 = \frac13$, $r = (1, 1, 1)$ and $G = 1$. So $\epsilon(x) = 0$ and $\omega(x) = 0$, and Theorem 3.2.7 applies. Here one point blowup suffices. In the $u_1$-chart, with $u_2 = u_1(u'_2 + t_2)$, $u_3 = u_1(u'_3 + t_3)$ and $Z = u_1 Z'$, the strict transform is
$$h' = Z'^3 + (u'_2 + t_2)(u'_3 + t_3).$$
For $k$ algebraically closed, let $c \in k$ with $c^3 = t_2 t_3$, and translate $Z'$ by $-c$. This gives $Z'^3 + u'_2 u'_3 + t_3 u'_2 + t_2 u'_3$, of order at most $2$. By symmetry the same holds in the other charts. So each point over the origin has multiplicity at most $2 < p$, and $\delta < 1$ there by Proposition 3.2.2(3).

Lean: none yet

### Notes and references

The definitions follow [CP19, Sections 2.1, 2.2, 2.5 and 2.7]. Proposition 3.2.4 is not stated in this form in [CP19]. It is the special case of [CP19, Propositions 2.10 and 2.26] for $X^p + f$ over a perfect field, with a direct proof. The residual order and its increase are studied by Moh [Moh87] and by Hauser and Perlega [HP19a]. Volume 7, Section 1.4, gives the examples of the increase.
