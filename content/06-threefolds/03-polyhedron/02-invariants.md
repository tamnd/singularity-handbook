---
title: The invariants of Cossart and Piltant
nodes: [SG00000014, SG00000013, SG00000015]
sources: [CP19, CP14, Hir67, Mat, Moh87, Moh14, HP19a]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The invariants of Cossart and Piltant

In this section we define the invariants $\delta$, $d_j$, $\epsilon$ and $\omega$ of [CP19, Sections 2.1, 2.2, 2.5 and 2.7], and we prove their first properties. For the purely inseparable equations $X^p + f$ over a perfect field we prove that the cleaning of Volume 7, Section 1.3, gives the minimal polyhedron, without the theorem of Hironaka. Then $\epsilon$ is the residual order of Volume 7. We state the theorem of Cossart and Piltant that the invariant $\iota = (m, \omega, \kappa)$ does not increase under permissible blowups. We prove the step of their algorithm for $\omega = 0$ in the case $\epsilon = 0$, and we state their Projection Theorem. At the end we show how these theorems give Theorem 1.2.6 by an induction on $\iota$.

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

This is [CP19, Definitions 2.67 and 2.68] in the case $i_0(x) = p$, in which the initial form has no terms in $Z^1, \dots, Z^{p - 1}$ [CP19, (1.11) and Remark 2.69]. In this case the module $V(F, E, \mathfrak{m}_S)$ of [CP19, Definition 2.42] is generated by the derivatives $\partial F / \partial U_j$ with $e < j \le n$. So Definition 3.2.5 agrees with the definition of Cossart and Piltant for each residue field, and we use the perfect field $k$ only to find well adapted coordinates by cleaning. The derivations of a $p$-basis of the residue field belong to the larger module $\mathcal{D}(\mathfrak{m}_S)$ of [CP19, (1.10) and Definition 2.41]. They enter the module $J(F, E, \mathfrak{m}_S)$ and the directrix $\operatorname{Dir}(x)$ in the case $\omega(x) = \epsilon(x)$ [CP19, Definitions 2.45 and 2.72], and so the refined $\kappa$, but they do not enter $\omega$ (Example 3.1.11). The Artin-Schreier case $\operatorname{in} h = Z^p - G^{p - 1} Z + F$ needs more care. They prove that $\omega(x)$ does not depend on the choice of the well adapted coordinates [CP19, Remark 2.69]. For the purely inseparable equations over a perfect field, Volume 7, Section 3.6, shows that $\omega(x)$ is the residual order $\rho$ of the log-Jacobian ideal, and it gives a short proof of this independence. Since $\partial F/\partial U_j = U_1^{r_1} \cdots U_e^{r_e} \, \partial \operatorname{in}(G)/\partial U_j$ for $j > e$, we have $\omega(x) = \epsilon(x) - 1$ exactly when $\operatorname{in}(G)$ contains a monomial in which some $U_j$ with $j > e$ has an exponent prime to $p$. If $\epsilon(x) = 0$, then $F$ is a monomial in $U_1, \dots, U_e$, and $\omega(x) = 0$. For $n = 3$, Cossart and Piltant refine $\kappa(x) \ge 2$ to a value in $\{2, 3, 4\}$ [CP19, Definition 5.1]. The values of $\iota$ lie in $\{1, \dots, p\} \times \mathbb{N} \times \{1, 2, 3, 4\}$, and the induction of [CP19] is on this ordered set.

The value of $\omega$ is not determined by the polyhedron [CP19, Remark 2.70]. Section 3.3 computes the example of that remark for $p = 3$.

### The behavior under blowups

Let $Y \subset X$ be an integral closed subscheme that contains $x$, with generic point $y$. It is *Hironaka-permissible* at $x$ if $m(y) = m(x)$ and $Y$ is regular at $x$ [CP19, Definition 2.20]. It is *Hironaka-permissible with respect to $E$* at $x$ if $m(y) = m(x) = m$, where $m$ is the degree of $h$, and $W = \eta(Y)$ has normal crossings with $E$ at $s = \eta(x)$, that is, the family $(u_1, \dots, u_e)$ extends to a regular system of parameters $(u_1, \dots, u_n)$ of $S$ with $I(W) = (u_j : j \in J)$ for a set $J \subseteq \{1, \dots, n\}$ [CP19, Definition 2.21]. Such a center is Hironaka-permissible, and its ideal at $x$ is $(Z, u_j : j \in J)$ in well adapted coordinates $(u; Z)$. Let $\sigma$ be the blowup of $\operatorname{Spec} S$ along $W$. A point $s'$ over $s$ lies in a chart $j_0 \in J$ where $u_{j_0}$ generates the ideal of the exceptional divisor. There $X' = Z / u_{j_0}$, the blowup of $X$ is defined by $h' = u_{j_0}^{-m} h(u_{j_0} X')$, and the divisor is $E' = \sigma^{-1}(E \cup W)_{\mathrm{red}}$ [CP19, Proposition 2.22]. A *local* blowup is the localization at a point of the exceptional divisor. The hypotheses (i) or (ii) of [CP19, Theorem 1.5], which are the conditions 1 and 2 of Theorem 1.2.6, form the condition (G) of [CP19, Section 2.3]. Conditions (G) and (E) are kept by each Hironaka-permissible blowup with respect to $E$ [CP19, Propositions 2.28 and 2.34].

Now let $m(y) = p$. The center $Y$ is *permissible of the first kind* at $x$ if it is Hironaka-permissible with respect to $E$ at $x$ and $\epsilon(y) = \epsilon(x)$ [CP19, Definition 3.1]. The point $Y = \{x\}$ is always permissible of the first kind. It is *permissible of the second kind* if it is Hironaka-permissible with respect to $E$ at $x$, $\epsilon(y) = \epsilon(x) - 1$, and two more conditions hold [CP19, Definition 3.5]. Cossart and Piltant show by an example that resolution by Hironaka-permissible blowups can require a curve of the second kind [CP19, Example 3.6]. For the blowup $\pi$ along such a center, let $x' \in \pi^{-1}(x)$, let $s'$ be its image in the blowup of $\operatorname{Spec} S$, let $S'$ be the local ring at $s'$ and let $E'$ be the reduced total transform of $E$ at $s'$. The strict transform of $h$ defines the triple $(S', h', E')$, and $\iota(x')$ is computed for it.

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

### The first step of Theorem 3.2.7

The proof of Theorem 3.2.7 is short in the case $\epsilon(x) = 0$, and it shows how a well chosen center makes $\delta$ drop. We give it for the purely inseparable equations over an algebraically closed field. If $\omega(x) = 0$, then $\epsilon(x) \in \{0, 1\}$, since $\omega(x) \in \{\epsilon(x) - 1, \epsilon(x)\}$.

**Proposition 3.2.9.** Let $k$ be an algebraically closed field of characteristic $p$, let $S = k[[u_1, \dots, u_n]]$, let $h = Z^p + f$ with $f$ clean, and let $E = \operatorname{div}(u_1 \cdots u_e)$. Assume that $m(x) = p$ and $\epsilon(x) = 0$. Write $f = u^r G$ as in Proposition 3.2.4, with $r_j = 0$ for $j > e$. Let $J \subseteq \{1, \dots, e\}$ be a set with $R = \sum_{j \in J} r_j \ge p$ that is minimal for inclusion among the sets with this property. Then $Y = V(Z, u_j : j \in J)$ is Hironaka-permissible with respect to $E$ at $x$. Let $\pi$ be the blowup along $Y$, and let $x'$ be a closed point of $\pi^{-1}(x)$. Then
$$\delta(x') \le \delta(x) - \tfrac1p.$$

Lean: none yet

*Proof.* By Proposition 3.2.4(4), $\operatorname{ord} G = \epsilon(x) = 0$, so $G$ is a unit. So $f$ contains the monomial $u^r$ with the coefficient $G(0) \ne 0$. Since $f$ is clean, $r \notin p \mathbb{N}^n$. By Proposition 3.2.4(2), $\delta(x) = |r|/p$, where $|r| = r_1 + \dots + r_n$, and $|r| \ge p$ by Proposition 3.2.2(3). Since $\sum_{j \le e} r_j = |r| \ge p$, a set $J$ as in the statement exists. By the minimality, $R - r_j \le p - 1$ for each $j \in J$, and so $r_j \ge 1$.

*The center.* We have $f \in (u_j : j \in J)^R \subseteq (u_j : j \in J)^p$, so $h \in (Z, u_j : j \in J)^p$, and the generic point $y$ of $Y$ has $m(y) \ge p$. The image of $h$ in $S[Z]/(u_j : j \in J)$ is $Z^p$, so $m(y) \le p$. Thus $m(y) = m(x) = p$. The subscheme $W = V(u_j : j \in J)$ has normal crossings with $E$, because $J \subseteq \{1, \dots, e\}$. So $Y$ is Hironaka-permissible with respect to $E$ at $x$.

*The charts.* Let $s'$ be the image of $x'$ in the blowup of $\operatorname{Spec} S$ along $W$. It lies in a chart $j_0 \in J$. Since $k$ is algebraically closed, there are $t_j \in k$ for $j \in J \setminus \{j_0\}$ such that the completion of the local ring at $s'$ is $k[[w]]$ with the coordinates
$$w = \bigl(u_{j_0}, \; v_j = u_j/u_{j_0} - t_j \ (j \in J \setminus \{j_0\}), \; u_i \ (i \notin J)\bigr).$$
Let $\beta \colon S \to k[[w]]$ be the induced map. By [CP19, Proposition 2.22], $h' = Z'^p + f'$ with $Z' = Z/u_{j_0}$ and $f' = \beta(f)/u_{j_0}^p$. Let $J_0 = \{ j \in J \setminus \{j_0\} : t_j = 0 \}$ and $J_1 = \{ j \in J \setminus \{j_0\} : t_j \ne 0 \}$. Then
$$\beta(u^r) = u_{j_0}^p \, w^a \, P, \qquad P = \prod_{j \in J_1} (v_j + t_j)^{r_j},$$
where $P$ is a unit, and $w^a = u_{j_0}^{R - p} \prod_{j \in J_0} v_j^{r_j} \prod_{i \notin J} u_i^{r_i}$. So
$$|a| = |r| - p + \sum_{j \in J_0} r_j \le |r| - p + (R - r_{j_0}) \le |r| - 1. \tag{3.2}$$

*Two bounds for the clean part.* Let $g \in k[[w]]$ and let $w_i$ be one of the coordinates. The series $g - g^{\mathrm{cl}}$ has its support in $p \mathbb{N}^n$, so its derivatives are $0$, and $\partial g / \partial w_i = \partial g^{\mathrm{cl}} / \partial w_i$. Each term $c w^b$ of $g^{\mathrm{cl}}$ has $|b| \ge \operatorname{ord} g^{\mathrm{cl}}$. So
$$\operatorname{ord} g^{\mathrm{cl}} \le \operatorname{ord} \Bigl( w_i \frac{\partial g}{\partial w_i} \Bigr), \qquad \operatorname{ord} g^{\mathrm{cl}} \le \operatorname{ord} \frac{\partial g}{\partial w_i} + 1. \tag{3.3}$$

*Derivatives of the transform.* Since $\partial (u_{j_0}^p) = 0$ in characteristic $p$, the chain rule gives, with $D_j = u_j \partial / \partial u_j$ on $S$,
$$u_i \frac{\partial f'}{\partial u_i} = \frac{\beta(D_i f)}{u_{j_0}^p} \ (i \notin J), \qquad (v_j + t_j) \frac{\partial f'}{\partial v_j} = \frac{\beta(D_j f)}{u_{j_0}^p} \ (j \in J \setminus \{j_0\}), \qquad u_{j_0} \frac{\partial f'}{\partial u_{j_0}} = \frac{\beta\bigl(\sum_{j \in J} D_j f\bigr)}{u_{j_0}^p}.$$
For the last formula, $u_{j_0} \partial \beta(g) / \partial u_{j_0} = \beta(u_{j_0} \partial g / \partial u_{j_0}) + \sum_{j \in J \setminus \{j_0\}} \beta(u_j \partial g / \partial u_j)$, because $\beta(u_j) = u_{j_0}(v_j + t_j)$. Now $D_i f = u^r (r_i G + D_i G)$ and $D_i G \in \mathfrak{m}_S$. So $D_i f$ is $u^r$ times a unit if $p \nmid r_i$. In the same way $\sum_{j \in J} D_j f$ is $u^r$ times a unit if $p \nmid R$. The map $\beta$ is local, so it maps units to units, and $\beta(u^r \cdot \text{unit})/u_{j_0}^p$ is $w^a$ times a unit, of order $|a|$.

*The three cases.* Since $r \notin p \mathbb{N}^n$, one of these cases holds.

1. Some $i \notin J$ has $p \nmid r_i$. Then $\operatorname{ord}(u_i \partial f' / \partial u_i) = |a|$, and (3.3) gives $\operatorname{ord} f'^{\mathrm{cl}} \le |a|$.
2. Some $i \in J \setminus \{j_0\}$ has $p \nmid r_i$. If $t_i = 0$, then $\operatorname{ord}(v_i \partial f' / \partial v_i) = |a|$, and $\operatorname{ord} f'^{\mathrm{cl}} \le |a|$. If $t_i \ne 0$, then $v_i + t_i$ is a unit, so $\operatorname{ord} \partial f' / \partial v_i = |a|$, and $\operatorname{ord} f'^{\mathrm{cl}} \le |a| + 1$. In this case $i \in J_1$, so $\sum_{j \in J_0} r_j \le R - r_{j_0} - r_i \le p - 2$, and (3.2) improves to $|a| \le |r| - 2$.
3. All $r_i$ with $i \ne j_0$ are divisible by $p$. Then $p \nmid r_{j_0}$, so $p \nmid R$, and $\operatorname{ord}(u_{j_0} \partial f' / \partial u_{j_0}) = |a|$. So $\operatorname{ord} f'^{\mathrm{cl}} \le |a|$.

In each case $\operatorname{ord} f'^{\mathrm{cl}} \le |r| - 1$. The invariant $\delta$ does not change under completion [CP19, (2.8)], and Proposition 3.2.4(2) over $k[[w]]$ gives $\delta(x') = \operatorname{ord} f'^{\mathrm{cl}}/p \le (|r| - 1)/p = \delta(x) - \frac1p$. $\square$

This is Case 1, the case $\epsilon(x) = 0$, of the proof of [CP19, Theorem 2.81], where $J$ is a set with $\sum_{j \in J} d_j \ge 1$ and with the smallest number of elements. Such a set is minimal for inclusion, and $d_j = r_j/p$ by Proposition 3.2.4(3). Cossart and Piltant compute the polyhedron at $x'$. The proof above uses derivatives instead. The minimality of $J$ is necessary. If $J$ is too large, a point of the chart with $t_j = 0$ for many $j$ can keep the order. For example, let $p = 2$, $f = u_1 u_2 u_3^2$, $E = \operatorname{div}(u_1 u_2 u_3)$ and $J = \{1, 2, 3\}$. At the origin of the $u_3$-chart, $f' = u_3^2 v_1 v_2$, which is clean of order $4 = \operatorname{ord} f$. The minimal set $J = \{1, 2\}$ gives $f' = (v_2 + t_2) u_3^2$ in the $u_1$-chart and $f' = v_1 u_3^2$ at the origin of the $u_2$-chart, and the clean part of $f'$ has order $3$ at each point. Since $W$ is an intersection of components of $E$, the point $x'$ has $(m(x'), \omega(x')) \le (p, 0)$ [CP19, Proposition 2.79]. So the induction on $\delta \in \frac1p \mathbb{N}$ can go on. If $\epsilon(x') = 1$, Cossart and Piltant use Case 2 of their proof. For $\delta(x) > 1$ it is the same as Case 1. For $\delta(x) = 1$ they choose the coordinates with $H^{-1} f = (u_{e + 1})$, where $H = u_1^{r_1} \cdots u_e^{r_e}$, and they blow up $V(Z, u_j : j \in J)$ with $J = \{ j : d_j > 0 \} \cup \{e + 1\}$. Then $m(x') \le p - 1$ by [CP19, Proposition 2.79]. After finitely many steps $\delta < 1$, and then $m < p$ by Proposition 3.2.2(3). Example 3.2.8 is the case $r = (1, 1, 1)$, $p = 3$ and $J = \{1, 2, 3\}$.

### The induction on the invariant

Theorems 3.2.6 and 3.2.7 have different roles. Theorem 3.2.7 ends the work at a point with $\omega(x) = 0$. Theorem 3.2.6 says that the blowups in the good centers never make $(m, \omega)$ larger. It does not say that $\iota$ drops. The step that makes $\iota$ drop is the Projection Theorem of Cossart and Piltant, which needs the refined value of $\kappa$.

For $n = 3$, $m(x) = p$, $\omega(x) > 0$ and $\kappa(x) \ge 2$, Cossart and Piltant define the *projection number* $\kappa(x) \in \{2, 3, 4\}$ [CP19, Definition 5.1]. It uses the directrix $\operatorname{Dir}(x)$ of the initial form, which is an affine subspace of $\operatorname{Spec} k[U_1, U_2, U_3]$, with underlying vector space $\operatorname{Vdir}(x)$ [CP19, Definition 2.72]. They put $\kappa(x) = 4$ if $\operatorname{Vdir}(x) \subseteq \langle U_1, \dots, U_e \rangle$. Otherwise $\kappa(x) = 3$ if $\omega(x) = \epsilon(x) - 1$ and either $E = \operatorname{div}(u_1 u_2)$, or $E = \operatorname{div}(u_1)$ with a condition on $\operatorname{Vdir}(x)$ and on $\partial F / \partial U_2$. In the remaining cases $\kappa(x) = 2$. In particular $\kappa(x) = 4$ if $e = n = 3$. For a fixed $\omega(x)$, a smaller $\kappa(x)$ means a milder singularity. For $\omega(x) > 0$, the value $\kappa(x) = 1$ means that $\operatorname{in} h$ has the form (1.9) of [CP19] with $G \ne 0$ and that $\omega(x) = \epsilon(x)$ [CP19, Definition 2.68]. Cossart and Piltant give these samples of initial forms with $E = \operatorname{div}(u_1)$, $\lambda \in k \setminus \{0\}$ and integer exponents [CP19, Section 1].

| Initial form $\operatorname{in} h$ | Condition | $\kappa(x)$ |
|---|---|---|
| $Z^p + \lambda U_1^{p d_1} U_3^{\omega(x)}$ | $\omega(x) \equiv 0 \bmod p$ | $2$ |
| $Z^p + \lambda U_1^{p d_1} U_2 U_3^{\omega(x)}$ | $\omega(x) \equiv 0 \bmod p$ | $2$ |
| $Z^p + \lambda U_1^{p d_1} U_3^{1 + \omega(x)}$ | $1 + \omega(x) \not\equiv 0 \bmod p$ | $3$ |
| $Z^p + \lambda U_1^{p d_1 + \omega(x)}$ | | $4$ |
| $Z^p + \lambda U_1^{p d_1 + \omega(x)} U_2$ | | $4$ |

In the first row $\lambda \notin k^p$ if $(d_1, \omega(x)/p) \in \mathbb{N}^2$, and in the fourth row $\lambda \notin k^p$ if $d_1 + \omega(x)/p \in \mathbb{N}$. Otherwise the vertex of the initial face would be solvable. Definition 3.2.5 gives the stated value of $\omega(x)$ in each row. In the fourth and fifth rows the vertex of the initial face has the first coordinate $d_1 + \omega(x)/p$, which is larger than $d_1$, so $d_1$ is attained at another vertex of the polyhedron. For example, in the third row $\epsilon(x) = 1 + \omega(x)$ and $\partial F / \partial U_3 \ne 0$, so $\omega(x) = \epsilon(x) - 1$. In the first row $\epsilon(x) = \omega(x)$, and all the derivatives $\partial F / \partial U_j$ with $j \ge 2$ vanish.

**Lemma 3.2.10.** The set $I = \{1, \dots, p\} \times \mathbb{N} \times \{1, 2, 3, 4\}$ with the lexicographic order is well ordered. So there is no infinite strictly decreasing sequence in $I$.

Lean: none yet

*Proof.* Let $A \subseteq I$ be nonempty. Let $m_0$ be the least first coordinate of an element of $A$, let $\omega_0$ be the least second coordinate of an element of $A$ with first coordinate $m_0$, and let $\kappa_0$ be the least third coordinate of an element of $A$ that begins with $(m_0, \omega_0)$. These exist because $\mathbb{N}$ is well ordered. Then $(m_0, \omega_0, \kappa_0)$ is the least element of $A$. If $(a_i)$ were an infinite strictly decreasing sequence, the set $\{a_i\}$ would have no least element. $\square$

**Theorem 3.2.11 (Cossart-Piltant, Projection Theorem).** Let $S$ be an excellent regular local ring of dimension 3, let $h$ and $E$ be as in Theorem 3.2.6, and let $x$ be the point over $\mathfrak{m}_S$, and assume $m(x) = p$ and $\omega(x) > 0$. Let $\kappa(x)$ be the projection number. Then for each valuation $\mu$ of $L$ with center $x$ there is a finite sequence of local Hironaka-permissible blowups with respect to $E$ along $\mu$,
$$(X, x) = (X_0, x_0) \leftarrow (X_1, x_1) \leftarrow \dots \leftarrow (X_r, x_r),$$
such that $\iota(x_r) < \iota(x)$. The sequence can be chosen independent, that is, the center at $x_i$ does not depend on the valuation with center $x_i$.

Lean: none yet

This is [CP19, Theorem 5.5], with the independence of [CP19, Definition 2.77]. Cossart and Piltant require that the blowups keep conditions (G) and (E) [CP19, Section 5.2], and they call the centers Hironaka-permissible with respect to $E$ [CP19, Remark 2.71]. We do not prove Theorem 3.2.11. Its proof is Corollary 6.4 for $\kappa(x) = 1$, Theorem 7.26 for $\kappa(x) = 2$ and Theorem 9.6 for $\kappa(x) = 3, 4$ of [CP19], and it fills Chapters 6 to 9 there. Section 4.1 describes its structure.

**Proposition 3.2.12.** Let $\mathcal{C}$ be a class of triples $(S, h, E)$ with a point $x$ over $\mathfrak{m}_S$, for which $\iota(x)$ is defined. Assume these four properties.

1. If $(S, h, E)$ is in $\mathcal{C}$, then each local Hironaka-permissible blowup with respect to $E$ gives a triple $(S', h', E')$ in $\mathcal{C}$.
2. If $m(x) < p$, then for each valuation $\mu$ with center $x$ there is a finite sequence of local Hironaka-permissible blowups along $\mu$ with $X_r$ regular at $x_r$.
3. If $(m(x), \omega(x)) = (p, 0)$, then for each $\mu$ there is a finite sequence of local Hironaka-permissible blowups with respect to $E$ along $\mu$ with $m(x_r) < p$.
4. If $m(x) = p$ and $\omega(x) > 0$, then for each $\mu$ there is a finite sequence of local Hironaka-permissible blowups with respect to $E$ along $\mu$ with $\iota(x_r) < \iota(x)$.

Then for each triple in $\mathcal{C}$ and each valuation $\mu$ with center $x$ there is a finite sequence of local Hironaka-permissible blowups along $\mu$ with $X_r$ regular at $x_r$.

Lean: none yet

*Proof.* Assume that the conclusion fails. By Lemma 3.2.10 there is a counterexample $(S, h, E, x, \mu)$ for which $\iota(x)$ is least among all counterexamples. By property 2, $m(x) = p$. By property 3 or 4 there is a sequence along $\mu$ that ends at a point $x_r$ with $\iota(x_r) < \iota(x)$. In the case of property 3 this holds because $m(x_r) < p$. By property 1, applied to each step, the triple at $x_r$ lies in $\mathcal{C}$, and $\mu$ has center $x_r$. Since $\iota(x_r) < \iota(x)$, it is not a counterexample, so there is a sequence along $\mu$ from $x_r$ to a regular point. The composite of the two sequences is a sequence for $(S, h, E, x, \mu)$. This is a contradiction. $\square$

The sequences in the proposition consist of blowups along $\mu$. Cossart and Piltant state Theorems 2.81 and 5.5 with independent sequences [CP19, Definition 2.77]. We do not prove that the composite sequence is independent. Let $\mathcal{C}$ be the class of the triples in dimension 3 that satisfy the hypotheses of Theorem 1.2.6 and condition (E). Property 1 holds by [CP19, Propositions 2.28 and 2.34]. Cossart and Piltant obtain property 2 from [CP14, Main Theorem 1.3]. Property 3 is Theorem 3.2.7, whose proof uses centers that are Hironaka-permissible with respect to $E$ [CP19, proof of Theorem 2.81], and property 4 is Theorem 3.2.11. One can reach condition (E) by preparatory blowups [CP19, Corollary 4.19]. So Proposition 3.2.12 gives Theorem 1.2.6. This is the proof of [CP19, Corollary 5.6], which Cossart and Piltant call a descending induction on $\iota$ [CP19, Section 1].

Theorem 3.2.6 is used inside the proof of Theorem 3.2.11. There Cossart and Piltant consider sequences of blowups along $\mu$ for which conditions (G) and (E) hold and $(m(x_i), \omega(x_i))$ does not increase [CP19, Section 5.2]. For centers of the first or the second kind this holds by Theorem 3.2.6 and [CP19, Propositions 2.28 and 2.34]. The projection number can increase along such a sequence. A point $x_i$ with $\iota(x_i) \ge \iota(x)$ is *very near* $x$ [CP19, Definition 5.4]. The work of Chapters 6 to 9 of [CP19] is to choose the centers so that, for each $\mu$, a point that is not very near $x$ comes after finitely many steps.

### Notes and references

The definitions follow [CP19, Sections 2.1, 2.2, 2.5 and 2.7]. Proposition 3.2.4 is not stated in this form in [CP19]. It is the special case of [CP19, Propositions 2.10 and 2.26] for $X^p + f$ over a perfect field, with a direct proof. The residual order and its increase are studied by Moh [Moh87] and by Hauser and Perlega [HP19a]. Volume 7, Section 1.4, gives the examples of the increase.
