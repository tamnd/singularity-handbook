---
title: The role of the defect
nodes: [SG00000010, SG0000001B]
sources: [Kuh-book, Kuh10b, Cut15, Cut21, CM17, Spi90]
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

### Defect extensions in the other volumes

The basic example of a defect extension is the Artin-Schreier extension of Volume 3, Proposition 3.2.5. It is an extension of degree $p$ of a henselian field with value group $\mathbb{Z}[1/p]$ and residue field $\mathbb{F}_p$, with $e = f = 1$ and $d = p$. Volume 9, Example 2.2.3, gives the same phenomenon over the perfect hull of $\mathbb{F}_p((t))$. Kuhlmann classifies Artin-Schreier defect extensions into two types [Kuh10b]. The defect is node SG00000010 of the map (planned, no Lean statement yet).

For valuations of function fields the defect is the main obstruction to the methods of this chapter and of Chapter 2. Cutkosky-Mourtada study the defect as an obstruction to local uniformization by these methods [CM17]. Cutkosky shows that the defect can behave erratically in towers of extensions [Cut21]. Cutkosky also shows that local monomialization of finite extensions, which holds in characteristic 0, fails in characteristic $p$ [Cut15]. The valuations of function fields of surfaces are classified in [Spi90].

### Notes and references

The facts on the henselization used in Example 3.2.1 are in [Kuh-book]. The resolution of the surface of Example 3.2.2 is in Volume 4. Example 3.2.1 is not in the Lean library, and the library has no Lean definition of the defect.
