---
title: Examples
nodes: []
sources: [ZS2, Zar39, Spi90]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Examples

In this section we test the Abhyankar inequality on the valuations of Section 1.6, and we classify the valuations of the plane. The field $k$ is arbitrary unless we say otherwise.

**Example 2.4.1 (monomial valuations with independent weights).** Let $K = k(x_1, \dots, x_n)$, and let $v$ be the monomial valuation of Lemma 1.6.1 with weights $\gamma_1, \dots, \gamma_n$ that are linearly independent over $\mathbb{Z}$. Apply Lemma 2.2.1 to $(K/k, v)$ with $r = n$ and $s = 0$. Here $K_0 = K$, so $\Gamma_v = \mathbb{Z}\gamma_1 \oplus \dots \oplus \mathbb{Z}\gamma_n$ and $Kv = k$. Thus $\operatorname{rr} \Gamma_v + \operatorname{trdeg}(Kv/k) = n + 0 = n$, and $v$ is an Abhyankar valuation. Examples 1.6.3 and 1.6.4 are the cases $n = 2$ with weights $(1, \alpha)$ in $\mathbb{R}$ and $((0, 1), (1, 0))$ in $\mathbb{Z}^2$.

**Example 2.4.2 (equality and strict inequality on the plane).** Let $K = k(x, y)$.

1. The valuation of Example 1.6.2 has $\Gamma_v = \mathbb{Z}$ and $Kv = k(\bar{t})$. So $1 + 1 = 2$, and it is a divisorial valuation.
2. The valuation $v_\varphi$ of Example 1.6.6 has $\Gamma_{v_\varphi} = \mathbb{Z}$ and residue field $k$. So $1 + 0 < 2$, and the inequality is strict.
3. The valuation $v = \operatorname{ord}_x$ of $K$, the order of vanishing along the line $x = 0$, has $\Gamma_v = \mathbb{Z}$ and $Kv = k(\bar{y})$. So $1 + 1 = 2$. Its center on $\mathbb{A}^2_k$ is the generic point of the line. The local ring there is $R = k[x, y]_{(x)}$, with $\dim R = 1$ and $\kappa = k(y)$. The local form gives $1 + 0 = 1$, as Corollary 2.3.4 predicts.

For $v_\varphi$ the local form at the origin $R = k[x, y]_{(x, y)}$ gives $1 + 0 < 2$. A valuation is an Abhyankar valuation exactly when the local form is an equality at its center.

**Example 2.4.3 (no equality without finite generation).** Theorem 2.2.2 needs $L/K$ finitely generated. Let $K_0 = \mathbb{F}_p((t))$ with the $t$-adic valuation, and let $K$ be its perfect hull. Section 3.2 shows that $K$ has value group $\mathbb{Z}[1/p]$ and residue field $\mathbb{F}_p$. Then $\operatorname{rr}(\Gamma_K/\Gamma_{K_0}) = 0$ and both transcendence degrees are 0, so equality holds. But $\Gamma_K/\Gamma_{K_0} = \mathbb{Z}[1/p]/\mathbb{Z}$ is an infinite torsion group, so it is not finitely generated. Theorem 2.2.2 does not apply, because $K/K_0$ is algebraic and not finite, so it is not finitely generated.

**Example 2.4.4 (the valuations of the plane).** Let $K = k(x, y)$ and let $v$ be a nontrivial valuation of $K/k$. Let $r = \operatorname{rr} \Gamma_v$ and $s = \operatorname{trdeg}(Kv/k)$. Since $\Gamma_v \ne 0$ is torsion free, $r \ge 1$. By Theorem 2.1.5, $r + s \le 2$. So there are three cases.

1. $r = 1$ and $s = 1$. Then $v$ is divisorial. By Corollary 2.2.4, $\Gamma_v \cong \mathbb{Z}$, and $Kv$ is a finitely generated extension of $k$ of transcendence degree 1. Example 1.6.2 is of this kind.
2. $r = 2$ and $s = 0$. Then $v$ is an Abhyankar valuation. By Corollary 2.2.4, $\Gamma_v \cong \mathbb{Z}^2$ as a group, and $Kv$ is a finite extension of $k$. By Proposition 1.2.5 the rank is 1 or 2. Example 1.6.3 has rank 1 and Example 1.6.4 has rank 2.
3. $r = 1$ and $s = 0$. Then $Kv$ is algebraic over $k$. Choose $\gamma > 0$ in $\Gamma_v$. For each $\gamma' \in \Gamma_v$ there are integers $m, n$ with $n > 0$ and $n\gamma' = m\gamma$, because $r = 1$. The map $\gamma' \mapsto m/n$ is well defined, injective and order preserving, because $\Gamma_v$ is torsion free and ordered. So $\Gamma_v$ is isomorphic to a subgroup of $\mathbb{Q}$ as an ordered group, and $v$ has rank 1. A finitely generated subgroup of $\mathbb{Q}$ is cyclic. So either $\Gamma_v \cong \mathbb{Z}$ and $v$ is discrete, as in Example 1.6.6, or $\Gamma_v$ is not finitely generated, as for the Puiseux series of Section 1.6.

The inequality is strict only in case 3. This is the classification of Zariski [Zar39]. Spivakovsky studies the valuations of the plane through the sequence of their centers on successive blowups [Spi90].

**Example 2.4.5 (the two cases of the local proof).** Let $R = k[x, y]_{(x, y)}$, with $\kappa = k$ and $\dim R = 2$. We follow the proof of Theorem 2.3.3 for two valuations that dominate $R$.

Lean: `Singularity.IsConvexSubgroup.eq_top_of_one_lt_mem`, `Singularity.isLeast_delta_one_lexValueX` (the two computations of the smallest convex subgroup). The claims on lengths and residue fields are not in Lean yet.

First let $v$ be the valuation of Example 1.6.3, with $v(x) = 1$ and $v(y) = \alpha$ for an irrational $\alpha > 0$. The least value of the generators $x, y$ is $\mu = \min(1, \alpha)$. Since $\Gamma_v \subseteq \mathbb{R}$ is archimedean, the smallest convex subgroup that contains $\mu$ is $\Delta = \Gamma_v$, so $\mathfrak{q} = 0$ and we are in Case A. There $r = 2$ and $s = 0$, and Step 3 gives $\ell(R/\mathfrak{m}^N) \ge CN^2$, which matches the degree 2 of the Hilbert-Samuel polynomial of $R$. So $2 + 0 \le 2$, with equality.

Next let $v$ be the valuation of rank 2 of Example 1.6.4, with $v(x) = (0, 1)$ and $v(y) = (1, 0)$. Now $\mu = (0, 1)$, and the smallest convex subgroup that contains $\mu$ is $\Delta = 0 \times \mathbb{Z}$, by Example 1.2.7. An element $f \in R$ has $v(f) > \Delta$ if and only if $\operatorname{ord}_y f > 0$, so $\mathfrak{q} = yR \ne 0$ and we are in Case B. By Example 1.6.8, $W = k[x, y]_{(y)}$, $\Gamma_v/\Delta \cong \mathbb{Z}$, and $L = W/\mathfrak{p} = k(x) = \kappa(\mathfrak{q})$. The ring $R/\mathfrak{q} = k[x]_{(x)}$ has dimension 1, and $\bar{v}$ is $\operatorname{ord}_x$ on $k(x)$. So $\Delta' = \Delta$ and $\kappa' = k$. The three inequalities of Case B are
$$1 + 0 \le 1, \qquad 1 + 0 \le 1, \qquad 0 + 0 \le 0,$$
for $R_\mathfrak{q}$, for $R/\mathfrak{q}$ and for the extension $(L/\kappa(\mathfrak{q}), \bar{v})$. Their sum is $2 + 0 \le 2$. Both valuations are Abhyankar valuations, as Example 2.4.1 says. In the second case, the proof splits the computation along the flag of Example 1.6.8: the line $y = 0$ and the origin on it.
