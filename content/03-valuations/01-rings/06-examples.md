---
title: Examples on the plane
nodes: []
sources: [ZS2, Zar39, Spi90]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Examples on the plane

In this section $k$ is a field and $K = k(x, y)$ is the function field of the plane. We construct valuations of $K/k$ of each type that occurs in the classification of Zariski. We use them again in Chapter 2 to test the Abhyankar inequality. Monomial valuations give most of the examples, and the valuation of an arc gives the last one.

### Monomial valuations

For $a = (a_1, \dots, a_n) \in \mathbb{N}^n$ we write $x^a = x_1^{a_1} \cdots x_n^{a_n}$.

**Lemma 1.6.1 (monomial valuations).** Let $\Gamma$ be an ordered group and let $\gamma_1, \dots, \gamma_n \in \Gamma$. For $a \in \mathbb{N}^n$ put $a \cdot \gamma = \sum a_i\gamma_i$. For a nonzero polynomial $f = \sum_a c_ax^a \in k[x_1, \dots, x_n]$ put
$$v(f) = \min\{a \cdot \gamma : c_a \ne 0\}.$$
Then $v(f/g) = v(f) - v(g)$ defines a valuation of $k(x_1, \dots, x_n)/k$.

Lean: `Singularity.monomialAddValuationFrac`, `Singularity.monomialAddValuationFrac_mk'`, `Singularity.monomialAddValuationFrac_X`

*Proof.* For $\delta \in \Gamma$ let $R_\delta$ be the $k$-span of the monomials $x^a$ with $a \cdot \gamma = \delta$. Then $k[x_1, \dots, x_n] = \bigoplus_\delta R_\delta$, and $R_\delta R_\varepsilon \subseteq R_{\delta + \varepsilon}$. For $f \ne 0$ write $f = \sum_\delta f_\delta$ with $f_\delta \in R_\delta$. Then $v(f)$ is the least $\delta$ with $f_\delta \ne 0$. Let $\operatorname{in}(f) = f_{v(f)}$ be the *initial form* of $f$.

Clearly $v(f + g) \ge \min(v(f), v(g))$. Let $f, g \ne 0$. The component of $fg$ in degree $\delta$ is $\sum_{\alpha + \beta = \delta} f_\alpha g_\beta$. If $\delta < v(f) + v(g)$, each term has $\alpha < v(f)$ or $\beta < v(g)$, so the component is 0. If $\delta = v(f) + v(g)$, the only nonzero term is $\operatorname{in}(f)\operatorname{in}(g)$, which is not 0 because $k[x_1, \dots, x_n]$ is a domain. So $v(fg) = v(f) + v(g)$ and $\operatorname{in}(fg) = \operatorname{in}(f)\operatorname{in}(g)$. Now the formula $v(f/g) = v(f) - v(g)$ is well defined on $K^\times$, it is multiplicative, and the inequality for sums follows from the case of polynomials, because $f/g + f'/g' = (fg' + f'g)/(gg')$. $\square$

If all $\gamma_i \ge 0$, then $k[x_1, \dots, x_n] \subseteq \mathcal{O}_v$. If all $\gamma_i > 0$, then $\mathfrak{m}_v \cap k[x_1, \dots, x_n] = (x_1, \dots, x_n)$, so the center of $v$ on $\mathbb{A}^n_k$ is the origin. Let $f, g$ be nonzero polynomials with $v(f) = v(g)$. Then $f = \operatorname{in}(f)(1 + h)$ with $h = (f - \operatorname{in}(f))/\operatorname{in}(f)$ and $v(h) > 0$, and the same holds for $g$. So
$$\overline{f/g} = \overline{\operatorname{in}(f)/\operatorname{in}(g)} \quad \text{in } Kv.$$
We call this the *residue formula*. Thus the residue field is generated over $k$ by the residues of quotients of homogeneous elements of the same degree.

**Example 1.6.2 (rational weights).** Let $n = 2$ and $\Gamma = \mathbb{Z}$, and let $v(x) = a$ and $v(y) = b$ with coprime integers $a, b \ge 1$. Then $\Gamma_v = \mathbb{Z}$, since $a$ and $b$ generate $\mathbb{Z}$. Let $t = x^b/y^a$. Then $v(t) = 0$, and we claim that $Kv = k(\bar{t})$ with $\bar{t}$ transcendental over $k$.

Let $P = \sum_{j=0}^d c_jT^j \in k[T]$ be nonzero of degree $d$. Then $y^{ad}P(t) = \sum_j c_jx^{bj}y^{a(d-j)}$. Each monomial in this sum has value $abd$, and the monomials are distinct, so $v(y^{ad}P(t)) = abd = v(y^{ad})$. Thus $v(P(t)) = 0$ and $P(\bar{t}) = \overline{P(t)} \ne 0$. So $\bar{t}$ is transcendental. Two monomials $x^iy^j$ and $x^{i'}y^{j'}$ of the same value satisfy $a(i - i') = b(j' - j)$. Since $a, b$ are coprime, $i - i' = bm$ and $j' - j = am$ for some $m \in \mathbb{Z}$, and the quotient of the monomials is $t^m$. So a quotient of homogeneous elements of the same degree is in $k(t)$, and the residue formula gives $Kv = k(\bar{t})$.

For $a = b = 1$ the valuation is the order of vanishing at the origin, $v(f) = \max\{n : f \in (x, y)^n\}$. In general, $v$ is the order of vanishing along the exceptional curve of a weighted blowup of the origin. Its value group is $\mathbb{Z}$, its rank is 1, and its residue field has transcendence degree 1 over $k$.

**Example 1.6.3 (an irrational weight).** Let $\alpha > 0$ be an irrational real number, $\Gamma = \mathbb{R}$, $v(x) = 1$ and $v(y) = \alpha$. Then distinct monomials $x^iy^j$ have distinct values $i + j\alpha$. So $\Gamma_v = \mathbb{Z} + \mathbb{Z}\alpha$, which has rank 1 and rational rank 2 (Section 1.2). The initial form of each polynomial is one monomial, so by the residue formula each element of value 0 has residue in $k$, and $Kv = k$. The group $\Gamma_v$ has no least positive element. Indeed, if $\varepsilon$ were the least positive element, then for $\gamma > 0$ in $\Gamma_v$ the element $\gamma - \lfloor \gamma/\varepsilon \rfloor \varepsilon$ would be in $\Gamma_v$ and in $[0, \varepsilon)$, so it would be 0, and $\Gamma_v = \mathbb{Z}\varepsilon$, which is false since $\alpha \notin \mathbb{Q}$. Thus $v$ is a valuation of rank 1 that is not discrete.

One can view this valuation as the valuation of the generalized power series $y = x^\alpha$: in a field of power series with real exponents, $v(f) = \operatorname{ord}_t f(t, t^\alpha)$. This is a power series of Puiseux type with one irrational exponent.

**Example 1.6.4 (rank 2).** Let $\Gamma = \mathbb{Z}^2$ with the lexicographic order, $v(x) = (0, 1)$ and $v(y) = (1, 0)$. Then $v(x^iy^j) = (j, i)$, so distinct monomials have distinct values, and $\Gamma_v = \mathbb{Z}^2$. By Section 1.2 the valuation has rank 2 and rational rank 2, and $\dim \mathcal{O}_v = 2$ by Corollary 1.2.4. As in Example 1.6.3, $Kv = k$. Both values are positive, so the center on $\mathbb{A}^2_k$ is the origin. For a nonzero polynomial $f$, let $j = \operatorname{ord}_y f$ and write $f = y^jg$. Then $v(f) = (j, \operatorname{ord}_x g(x, 0))$. So $v$ first measures the order of $f$ along the line $y = 0$, and then the order at the origin of what remains. The prime ideals of $\mathcal{O}_v$ are $0$, $\mathfrak{m}_v$ and one prime between them. The middle prime meets $k[x, y]$ in $(y)$.

### The valuation of an arc

Let $\varphi \in k[[t]]$ with $\varphi(0) = 0$, and assume that $\varphi$ is transcendental over $k(t)$. Then the map $k[x, y] \to k[[t]]$ with $x \mapsto t$ and $y \mapsto \varphi$ is injective, so it extends to an embedding $K \to k((t))$. The $t$-adic valuation $\operatorname{ord}_t$ of $k((t))$ restricts to a valuation $v_\varphi$ of $K/k$, with
$$v_\varphi(f) = \operatorname{ord}_t f(t, \varphi(t)).$$
This is the *valuation of the arc* $(t, \varphi(t))$. Its value group is a subgroup of $\mathbb{Z}$ that contains $v_\varphi(x) = 1$, so it is $\mathbb{Z}$. Its residue field is a subfield of $k$ that contains $k$, so it is $k$. Its center on $\mathbb{A}^2_k$ is the origin.

**Lemma 1.6.5.** The power series $\varphi = \sum_{i \ge 1} t^{i!}$ is transcendental over $k(t)$, for each field $k$.

Lean: `Singularity.transcendental_factorialSeries`, `Singularity.transcendental_factorialSeries_ratFunc`

*Proof.* Assume that $\varphi$ is algebraic over $k(t)$. Let $P \in k[t][Y]$ be a nonzero multiple of its minimal polynomial by an element of $k[t]$. So $P$ is irreducible in $k(t)[Y]$, $P(t, \varphi) = 0$, and $P$ has degree $d \ge 1$ in $Y$. Let $c$ be the largest degree in $t$ of a coefficient of $P$. For $N \ge 1$ let $\varphi_N = \sum_{i=1}^N t^{i!} \in k[t]$, a polynomial of degree $N!$.

First, $P(t, \varphi_N) \ne 0$. If $d \ge 2$, then $P$ has no root in $k(t)$ because it is irreducible. If $d = 1$, the only root of $P$ is $\varphi$, and $\varphi \ne \varphi_N$. Second, $Y - Y'$ divides $P(t, Y) - P(t, Y')$ in $k[t][Y, Y']$. So $\varphi - \varphi_N$ divides $P(t, \varphi) - P(t, \varphi_N) = -P(t, \varphi_N)$ in $k[[t]]$, and
$$\operatorname{ord}_t P(t, \varphi_N) \ge \operatorname{ord}_t(\varphi - \varphi_N) = (N + 1)!.$$
But $P(t, \varphi_N)$ is a nonzero polynomial of degree at most $c + d \cdot N!$, and the order of a nonzero polynomial is at most its degree. So $(N + 1) \cdot N! \le c + d \cdot N!$. This is false for $N \ge c + d$. $\square$

The Lean proof uses the same gap argument, but it does not use the minimal polynomial. If a nonzero $P \in k[t][Y]$ has $P(t, \varphi) = 0$, then the gap argument gives $P(t, \varphi_N) = 0$ for each large $N$. The partial sums $\varphi_N$ are distinct, and a nonzero polynomial in $Y$ over $k[t]$ has only finitely many roots. This is a contradiction. The second Lean name states the lemma over $k(t)$, with $\varphi$ in the field $k((t))$ of Laurent series.

**Example 1.6.6 (an arc).** Let $\varphi = \sum_{i \ge 1} t^{i!}$. By Lemma 1.6.5, $v_\varphi$ is a valuation of $K/k$. It is discrete of rank 1, with $\Gamma_{v_\varphi} = \mathbb{Z}$ and residue field $k$. Its center on $\mathbb{A}^2_k$ is the origin. Its dimension is 0. So by the last paragraph of Section 1.4, its center on each model of $K/k$ on which it has a center is a closed point. A proper model always contains a center, by Proposition 1.4.4. A model that is not proper need not contain one. For example, $v_\varphi$ has no center on $\mathbb{A}^2_k \setminus \{0\}$. Indeed, a center on this open set would also be a center on $\mathbb{A}^2_k$, and by Proposition 1.4.3 the only center on $\mathbb{A}^2_k$ is the origin. In particular $v_\varphi$ is not the order of vanishing along a curve on any model. Example 2.4.2 shows that the Abhyankar inequality is strict for $v_\varphi$.

### Puiseux series with unbounded denominators

Let $k$ have characteristic 0, and let $\varphi = \sum_i c_it^{\beta_i}$ be a series with rational exponents $0 < \beta_1 < \beta_2 < \dots$ whose denominators are not bounded. Such a series is not algebraic over $k(t)$, since an algebraic Puiseux series has bounded denominators by the theorem of Newton and Puiseux. It lies in the field of power series with rational exponents, and the order in $t$ is a valuation of this field with value group $\mathbb{Q}$ and residue field $k$. The formula $v(f) = \operatorname{ord}_t f(t, \varphi(t))$ defines a valuation of $K/k$ of rank 1, with value group a subgroup of $\mathbb{Q}$ and residue field $k$. One can show that this value group is not finitely generated, so the valuation is not discrete. We do not prove this here. Zariski and Samuel construct valuations with a given value group in [ZS2, Chapter VI, Section 15], and Spivakovsky classifies the valuations of the plane in terms of their Puiseux type expansions [Spi90].

The examples give each kind of valuation of $K/k$ with a center at the origin. The kinds are divisorial (Example 1.6.2), of rank 1 with rational rank 2 (Example 1.6.3), of rank 2 (Example 1.6.4), discrete with residue field $k$ (Example 1.6.6), and of rank 1 with value group not finitely generated (the last paragraph). Example 2.4.4 shows that each nontrivial valuation of $K/k$ is of one of these kinds, if we ignore algebraic extensions of the residue field. This is the classification of Zariski [Zar39].

### Centers on the projective plane

We now compute the centers of some of these valuations on $\mathbb{P}^2_k$, and we look more closely at the rank 2 valuation and at the arc. Let $X, Y, Z$ be homogeneous coordinates on $\mathbb{P}^2_k$, with $x = X/Z$ and $y = Y/Z$. The plane is covered by the three affine charts
$$U_Z = \operatorname{Spec} k[x, y], \qquad U_X = \operatorname{Spec} k[1/x, y/x], \qquad U_Y = \operatorname{Spec} k[x/y, 1/y].$$
By Lemma 1.4.2, a valuation $v$ of $K/k$ has a center on a chart if and only if the two generators of the ring of the chart have values $\ge 0$. If both values are $> 0$, the center is the origin of the chart, because the maximal ideal of the origin is then contained in $\mathfrak{m}_v$.

**Example 1.6.7 (negative weights).** First let $v$ be the monomial valuation with $\Gamma = \mathbb{Z}$ and $v(x) = v(y) = -1$. For a nonzero polynomial $f$, each monomial of degree $d$ has value $-d$, so $v(f) = -\deg f$. Since $v(x) < 0$, the valuation has no center on $U_Z = \mathbb{A}^2_k$. On $U_X$ put $u = 1/x$ and $w = y/x$. Then $v(u) = 1$ and $v(w) = 0$. We claim that $\mathfrak{m}_v \cap k[u, w] = (u)$. Let $P \in k[w]$ be nonzero of degree $d$. Then $P(w) = F(x, y)/x^d$ with $F$ homogeneous of degree $d$ and $F \ne 0$, so $v(P(w)) = -d + d = 0$. Each $g \in k[u, w]$ has the form $g = g_0(w) + ug_1$ with $g_1 \in k[u, w]$. So $g \in \mathfrak{m}_v$ if and only if $g_0 = 0$, that is, if and only if $g \in (u)$. This proves the claim. The center of $v$ on $\mathbb{P}^2_k$ is the generic point of the line $L_\infty = V(Z)$, and $\mathcal{O}_v = k[u, w]_{(u)}$, because $\mathcal{O}_v$ dominates this discrete valuation ring (Step 3 of the proof of Theorem 1.3.2). So $v$ is the order of vanishing along the line at infinity. The residue field is $Kv = k(\bar{w})$, and $\bar{w}$ is transcendental over $k$, as the computation of $v(P(w))$ shows.

Lean: `Singularity.valuation_chartEval_inv_div_lt_one_iff` (the claim $\mathfrak{m}_v \cap k[u, w] = (u)$ for negative weights, with the property of the monomial valuation on homogeneous forms as a hypothesis)

Next let $\alpha > 0$ be irrational, and let $v$ be the monomial valuation with $\Gamma = \mathbb{R}$, $v(x) = -1$ and $v(y) = -\alpha$. As in Example 1.6.3, $\Gamma_v = \mathbb{Z} + \mathbb{Z}\alpha$ and $Kv = k$. If $\alpha < 1$, then $v(1/x) = 1 > 0$ and $v(y/x) = 1 - \alpha > 0$, so the center on $\mathbb{P}^2_k$ is the origin $[1 : 0 : 0]$ of $U_X$. If $\alpha > 1$, then $v(x/y) = \alpha - 1 > 0$ and $v(1/y) = \alpha > 0$, so the center is the origin $[0 : 1 : 0]$ of $U_Y$. In both cases the center is a closed point on the line at infinity. This agrees with the bound $\dim \overline{\{c_X(v)\}} \le \dim v = 0$ of Section 1.4. In both examples the center on $\mathbb{A}^2_k$ does not exist, while the center on the proper model $\mathbb{P}^2_k$ exists, as Proposition 1.4.4 says.

**Example 1.6.8 (the rank 2 valuation as a composite).** Let $v$ be the valuation of Example 1.6.4, with $v(x) = (0, 1)$ and $v(y) = (1, 0)$ in $\mathbb{Z}^2$ with the lexicographic order. By Example 1.2.7, $\Gamma_v$ has the convex subgroups $0 \subsetneq \Delta \subsetneq \mathbb{Z}^2$ with $\Delta = 0 \times \mathbb{Z}$. Let $v_1 = \operatorname{pr}_1 \circ v$ be the first coordinate of $v$. For a nonzero polynomial $f$ we have $v_1(f) = \operatorname{ord}_y f$, so $v_1$ is the order of vanishing along the line $y = 0$, and its ring is $W = k[x, y]_{(y)}$. The residue field of $W$ is $k(x)$, since the residue of $x$ generates it. The ring $W$ is the localization of $\mathcal{O}_v$ at the middle prime $\mathfrak{p}_\Delta$ of Proposition 1.2.3.

Lean: `Singularity.RankTwoExample.v_nonneg_iff`, `Singularity.RankTwoExample.vOne_pos_iff_X_one_dvd`, `Singularity.RankTwoExample.v_pos_iff_constantCoeff_eq_zero` (the rank 2 valuation and its coarsening on polynomials). Lean does not identify the valuation ring of the coarsening or its residue field.

We show that $\mathcal{O}_v$ is the set of $f \in W$ whose residue $\bar{f} \in k(x)$ lies in $k[x]_{(x)}$. Let $f \in K^\times$ with $v(f) = (a, b)$. Then $f \in \mathcal{O}_v$ if and only if $a > 0$, or $a = 0$ and $b \ge 0$. Also $f \in W$ if and only if $a \ge 0$, and $f \in \mathfrak{m}_W$ if and only if $a > 0$. If $a > 0$, then $f \in \mathcal{O}_v$ and $\bar{f} = 0$. Let $a = 0$. Write $f = g/h$ with polynomials $g = y^jg'$ and $h = y^jh'$ such that $g'(x, 0) \ne 0$ and $h'(x, 0) \ne 0$. Then $\bar{f} = g'(x, 0)/h'(x, 0)$ and $b = \operatorname{ord}_x g'(x, 0) - \operatorname{ord}_x h'(x, 0) = \operatorname{ord}_x \bar{f}$. So $b \ge 0$ if and only if $\bar{f} \in k[x]_{(x)}$. Thus $v$ is the composite of $v_1$ with the valuation $\operatorname{ord}_x$ of the residue field $k(x)$ of $v_1$, in the sense of Lemma 2.3.2.

The centers on $\mathbb{A}^2_k$ form a flag. The center of $v_1$ is the generic point of the line $y = 0$, and the center of $v$ is the origin, a point on this line. In $\operatorname{ZR}(K/k)$ the three points $\mathcal{O}_v \subsetneq W \subsetneq K$ satisfy $\mathcal{O}_v \in \overline{\{W\}}$ and $W \in \overline{\{K\}}$, by Proposition 1.5.5. In general, let $X$ be a separated model on which $v$ has a center $c_X(v)$. Since $\mathcal{O}_v \subseteq W$, the ring $W$ has a center $c_X(v_1)$ on each affine chart that contains $c_X(v)$, and $\mathfrak{m}_W \subseteq \mathfrak{m}_v$ shows that $c_X(v)$ lies in the closure of $c_X(v_1)$. The center of $v_1$ can be a closed point on some models. For example, the composite of the order along the exceptional curve of the blowup of the origin with a valuation of the residue field has rank 2, and its coarsening has the origin of $\mathbb{A}^2_k$ as center. Both values $v(x), v(y)$ are positive, so the center of $v$ on $\mathbb{P}^2_k$ is the origin $[0 : 0 : 1]$ of $U_Z$.

**Example 1.6.9 (the arc after one blowup).** Let $\varphi = \sum_{i \ge 1} t^{i!} = t + t^2 + t^6 + t^{24} + \dots$ and $v = v_\varphi$ as in Example 1.6.6. The values of some polynomials are
$$v(y) = 1, \quad v(y - x) = 2, \quad v(y - x - x^2) = 6, \quad v(y - x - x^2 - x^6) = 24.$$
Indeed, $\varphi - t - t^2 - \dots - t^{N!}$ has order $(N + 1)!$. So $v$ is not the monomial valuation in $x, y$ with weights $(1, 1)$, which gives $y - x$ the value 1. Let $\pi : X_1 \to \mathbb{A}^2_k$ be the blowup of the origin, and consider its chart $\operatorname{Spec} k[x, y_1]$ with $y_1 = y/x$. On this chart $y_1$ corresponds to $\varphi/t = 1 + t + t^5 + t^{23} + \dots$. So $v(x) = 1$, $v(y_1) = 0$ and $v(y_1 - 1) = 1$. The center of $v$ on $X_1$ is the closed point $x = 0$, $y_1 = 1$ of the exceptional curve $E = V(x)$.

Lean: none yet

In the coordinates $x$ and $y_1' = y_1 - 1$ at this point, the arc is $(t, \varphi_1(t))$ with $\varphi_1 = \sum_{i \ge 2} t^{i! - 1}$. This series has the same form as $\varphi$: it is transcendental over $k(t)$, because $\varphi = t(1 + \varphi_1)$. So the same computation applies after each further blowup of the center. At each step the center is a closed point, since $\dim v = 0$. The sequence of centers does not stop at the generic point of a curve, which agrees with the fact that $v$ is not divisorial. Example 2.4.2 gives the numerical reason: $\operatorname{rr} v + \operatorname{trdeg}(Kv/k) = 1 < 2$.
