---
title: The role of the defect
nodes: [SG00000010, SG0000001B]
sources: [Kuh-book, Kuh10b, Cut15, Cut21, CM17, Spi90, Mat, Tem13, Abh56s, CP08, CP09]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The role of the defect

Theorem 3.1.5 shows that the method of Section 1.3 works for a surface exactly when one can choose $x, y$ such that $K/k(x, y)$ has $e = 1$, a separable residue extension and no defect. In characteristic 0 only the condition $e = 1$ matters. In characteristic $p$ the defect enters. In this section we show that the defect is a property of the pair $K/K_0$ and not of $(K, v)$ alone, and we connect it with the examples of the other volumes.

### The defect depends on the subfield

**Example 3.2.1.** Let $k$ be a field of characteristic $p > 0$, let $K = k(x, y)$, and let $v$ be the arc valuation $v(g) = \operatorname{ord}_t g(t, \varphi(t))$ of Volume 3, Example 1.6.6, with $\varphi = \sum_{i \ge 1} t^{i!}$. Then $\Gamma_v = \mathbb{Z}$, $v(x) = 1$, and $Kv = k$. Let $K_0 = k(x, y^p)$, and let $v_0$ be the restriction of $v$. Then:

1. $[K : K_0] = p$, and $K/K_0$ is purely inseparable.
2. $e = 1$ and $f = 1$.
3. $d = p$.
4. $v$ has local uniformization.

Lean: none yet

*Proof.* Part 1. The element $y$ is a root of $Y^p - y^p$ over $K_0$, and $y \notin K_0$, because $x$ and $y$ are algebraically independent. In characteristic $p$, a polynomial $Y^p - c$ is irreducible over a field that does not contain a $p$-th root of $c$. So $[K : K_0] = p$, and $y$ is purely inseparable over $K_0$.

Part 2. $\Gamma_{v_0}$ contains $v(x) = 1$, so $\Gamma_{v_0} = \Gamma_v$ and $e = 1$. The residue field of $v_0$ contains $k$ and is contained in $Kv = k$, so $f = 1$.

Part 3. The henselization $K_0^h$ is a separable algebraic extension of $K_0$, and $y$ is purely inseparable over $K_0$ and not in $K_0$. So $y \notin K_0^h$. Then $K^h = K \cdot K_0^h = K_0^h(y)$ has degree $p$ over $K_0^h$, by the argument of part 1. So $d = p/(ef) = p$.

Part 4. This is Corollary 1.2.8, since $K$ is a field of rational functions. $\square$

So the extension $K/K_0$ is immediate with defect $p$, and Theorem 1.3.4 does not apply to it. But for the subfield $K$ itself the extension is trivial. The defect is a property of the extension $K/K_0$, and a good choice of $K_0$ can avoid it. We do not discuss here when a good choice exists.

**Example 3.2.2.** Let $k$ be an algebraically closed field of characteristic $p$, and let $X = V(z^p - x^{p+1} - y^{p+1}) \subseteq \mathbb{A}^3_k$, the surface of Volume 4, Example 2.3.5. Its function field is $K = k(x, y, z)$, and $K/k(x, y)$ is purely inseparable of degree $p$. So for each valuation $v$ of $K/k$, the extension $K/k(x, y)$ has no étale generator at $v$, and Theorem 1.3.4 does not apply with this subfield. For each such $v$, one of $e$, $f$ and $d$ is $p$, as we show next. Volume 4, Example 2.3.5, resolves $X$ by $1 + \lfloor p/2 \rfloor$ blowups, and Proposition 1.4.5 gives a regular center on this resolution for each valuation of $K/k$ with a center on $X$. Local uniformization asks for a regular center over each model of $K/k$, and Proposition 3.1.2 gives it, because $K/k$ has transcendence degree 2.

In Example 3.2.2 the product $efd$ is $[K^h : K_0^h]$, with $K_0 = k(x, y)$. The henselization $K_0^h$ is separable over $K_0$, so $z \notin K_0^h$, and $K^h = K_0^h(z)$ has degree $p$. Since $p$ is prime, one of the three factors is $p$ and the others are 1. Which one depends on the valuation.

### How the defect blocks the lifting

In Example 3.2.1 the field $K$ is rational, so local uniformization holds for another reason. The next example shows what goes wrong with the method of Section 1.3 for the subfield $K_0 = k(x, y^p)$. Three things fail. There is no étale generator. No element of $K_0$ is a best approximation of $y$. And a regular chart of $K_0$ does not lift to a regular chart of $K$ in a stable way: a finer chart below can give a worse chart above. In the étale case Theorem 1.3.4 lifts each chart, so the third failure is the one that matters for the method.

**Example 3.2.3 (the defect blocks the naive lifting).** Keep the notation of Example 3.2.1, and let $w = y^p$, so that $K_0 = k(x, w)$ is a field of rational functions with $v_0(x) = 1$ and $v_0(w) = p$.

1. There is no étale generator of $K/K_0$ at $v$. Indeed, $K^p = k^p(x^p, y^p) \subseteq K_0$. So each $z \in K \setminus K_0$ has the minimal polynomial $Z^p - z^p$ over $K_0$, whose derivative is 0.
2. The set $v(y - K_0)$ has no largest element. Let $\varphi_N = \sum_{i=1}^N x^{i!} \in k[x] \subseteq K_0$. Then $v(y - \varphi_N) = \operatorname{ord}_t \sum_{i > N} t^{i!} = (N + 1)!$. These values are unbounded, and $y \notin K_0$. This agrees with Volume 3, Proposition 3.2.3, because $ef = 1 < p = [K : K_0]$.
3. A criterion for the lift. Let $A_0 \subseteq \mathcal{O}_{v_0}$ be an affine model of $K_0/k$ whose local ring $R_0$ at the center of $v_0$ is regular of dimension 2, with maximal ideal $\mathfrak{m}_0$. Let $z \in \mathcal{O}_v \setminus K_0$ with $z^p \in A_0$. Then the local ring of $A_0[z]$ at the center of $v$ is regular if and only if $z^p - c \notin \mathfrak{m}_0^2$, where $c \in k$ is the residue of $z^p$.
4. A finer chart can give a worse lift. Take $z = y$. In $R_0 = k[x, w]_{(x, w)}$ the element $y^p = w$ has order 1, and indeed $A_0[y] = k[x, y]$ is regular. Now let $R_1$ be the quadratic transform of $R_0$ along $v_0$, with $w_1 = w/x$. Then $v_0(w_1) = p - 1 > 0$, so $R_1 = k[x, w_1]_{(x, w_1)}$, and $y^p = xw_1$ has order 2 in $R_1$. By part 3 the ring $k[x, w_1, y]$ is singular at the center of $v$. After $p$ transforms we reach $w' = w/x^p = (y/x)^p$, with $v_0(w') = 0$ and residue 1, and the center $(x, w' - 1)$. There $y^p = x^pw'$ has order $p$. The generator $y/x$ works for this chart, because $(y/x)^p - 1 = w' - 1$ has order 1. But the next quadratic transform has the same problem for $y/x$.

*Proof of part 3.* The residue field $\kappa_0$ of $R_0$ lies between $k$ and $K_0v_0 = k$, so $\kappa_0 = k$. The residue $\bar{z}$ of $z$ lies in $Kv = k$, and $c = \bar{z}^p$. Let $c' = z^p - c \in \mathfrak{m}_0$. It is not 0, because $z \notin k$. By part 1, $A_0[z] \cong A_0[Z]/(Z^p - z^p)$, as in the proof of Theorem 1.3.4. Put $\zeta = Z - \bar{z}$. In characteristic $p$ we have $Z^p - z^p = \zeta^p - c'$. Let $T$ be the localization of $R_0[\zeta]$ at the maximal ideal $(\mathfrak{m}_0, \zeta)$. It is a regular local ring of dimension 3, and $\operatorname{gr}(T) = \operatorname{gr}(R_0)[\bar{\zeta}]$, so an element of $R_0$ has the same order in $T$ as in $R_0$. The center of $v$ on $A_0[z]$ contains the center of $v_0$ on $A_0$ and $z - \bar{z}$, so the local ring of $A_0[z]$ there is $T/gT$ with $g = \zeta^p - c'$. A quotient of a regular local ring by a nonzero element $g$ of its maximal ideal is regular if and only if $g$ is not in the square of the maximal ideal [Mat]. If $c' \notin \mathfrak{m}_0^2$, then $c'$ has order 1 in $T$, and $\zeta^p$ has order $p \ge 2$, so $g$ has order 1. If $c' \in \mathfrak{m}_0^2$, then $g \in (\mathfrak{m}_0, \zeta)^2$. $\square$

The proof of Theorem 1.3.4 uses that the fiber of $A_0[z]$ over the center of $v_0$ is a field. In part 3 this fiber is $k[\zeta]/(\zeta^p)$, which is not reduced. The maximal ideal of the lift needs the new generator $\zeta$, and the lift is regular only if $c' \notin \mathfrak{m}_0^2$. Local uniformization of $v_0$ gives finer and finer regular charts, but it gives no control of the order of $c'$. In part 4 the order grows under quadratic transforms, and a generator that works for a chart fails for a finer chart. So the proof of Theorem 1.3.4 does not extend to defect extensions. The proofs of Abhyankar for surfaces [Abh56s] and of Cossart-Piltant for threefolds [CP08, CP09] use other methods. The ring $A_0[Z]/(Z^p - z^p)$ of part 3 is a hypersurface of the form $t^p = f$ over a regular ring. By [Tem13, Remark 1.3.5], if $[k : k^p]$ is finite, then local uniformization in general reduces to this inseparable case, and Section 4.2 discusses this reduction.

### Defect extensions in the other volumes

The basic example of a defect extension is the Artin-Schreier extension of Volume 3, Proposition 3.2.5. It is an extension of degree $p$ of a henselian field with value group $\mathbb{Z}[1/p]$ and residue field $\mathbb{F}_p$, with $e = f = 1$ and $d = p$. Volume 9, Example 2.2.3, gives the same phenomenon over the perfect hull of $\mathbb{F}_p((t))$. Kuhlmann classifies Artin-Schreier defect extensions into two types [Kuh10b]. The defect is node SG00000010 of the map, with the planned Lean name `Singularity.Valuation.defect` (no Lean statement yet).

For valuations of function fields the defect is the main obstruction to the methods of this chapter and of Chapter 2. Cutkosky-Mourtada study the defect as an obstruction to local uniformization by these methods [CM17]. Cutkosky shows that the defect can behave erratically in towers of extensions [Cut21]. Cutkosky also shows that local monomialization of finite extensions, which holds in characteristic 0, fails in characteristic $p$ [Cut15]. The valuations of function fields of surfaces are classified in [Spi90].

### Notes and references

The facts on the henselization used in Example 3.2.1 are in [Kuh-book]. The resolution of the surface of Example 3.2.2 is in Volume 4. Example 3.2.1 is not in the Lean library, and the library has no Lean definition of the defect.
