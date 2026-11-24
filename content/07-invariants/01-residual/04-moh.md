---
title: The increase of the residual order
nodes: [SG00000015, SG00000016, SG00000017]
sources: [Moh87, HP19a, HP19b, Hau08, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The increase of the residual order

In characteristic $0$, the residual order does not increase under a permissible blowup at the points where the order stays the same. This is the step that makes the induction of the proofs of resolution work. In characteristic $p$ the residual order can increase. In this section we state Moh's bound for one blowup, we compute an increase in a short example, and we describe the cycle of Hauser and Perlega, along which the residual order tends to infinity. We keep the notation of Section 1.3: $K$ is a perfect field of characteristic $p$, $q = p^e$, and $f = z^q + F(x)$.

### Moh's bound

**Theorem 1.4.1 (Moh).** Let $f = z^q + F$ with $F$ clean, let $E$ be a normal crossings divisor as in Section 1.3, and let $d$ be the residual order of $f$ for $E$. Let $\pi$ be a permissible blowup, and let $a$ be a point over the origin where the strict transform $f'$ has order $q$. Then the residual order $d'$ of $f'$ at $a$ for the transform $E'$ of $E$ satisfies
$$d' \le d + p^{e-1}.$$

Node: SG00000015 · Lean: none yet

We do not prove Theorem 1.4.1. It is from [Moh87], and [HP19a, Section 3] states it in this form. Hauser gives a further analysis of the increase and necessary conditions on $F$ for an increase in [Hau10], and Hauser and Perlega characterize the increase in [HP19b]. Hauser studies the points where the invariant increases, the *kangaroo points*, in [Hau08].

Moh also claimed a stronger result, the *stability theorem*: along a sequence of permissible blowups under which the order of the strict transforms of $f$ stays $q$, the residual order never exceeds $d + p^{e-1}$ [Moh87]. If it were true, the residual order could not increase without bound, and a refined invariant might drop in the long run. The rest of this section shows that the claim is false.

### An increase in one blowup

Moh's proof of the stability theorem uses this step [HP19a, Section 3]. Let $r$ be the largest integer such that the initial form of $F$ is a $p^r$-th power. Moh assumes, without loss of generality, that $p^r$ divides $d$, and concludes that $d' \le \lfloor d/p^r \rfloor p^r + p^r$ after one blowup. The next example, from [HP19a, Section 3], shows that this bound is false.

**Example 1.4.2.** Let $p = 2$ and $q = 4$, and let
$$f = z^4 + x^2 y^2 w^3 \bigl(w (x + y)^4 + x^{13}\bigr), \qquad E = V(xyw).$$
By Example 1.3.4, $F$ is clean, $G = w (x + y)^4 + x^{13}$, and the residual order is $d = 5$. The initial form of $F$ is
$$x^2 y^2 w^3 \cdot w (x + y)^4 = x^6 y^2 w^4 + x^2 y^6 w^4 = (x^3 y w^2 + x y^3 w^2)^2.$$
It is a square, and it is not a fourth power, because the exponent $6$ is not divisible by $4$. So $p^r = 2$, and Moh's bound is $\lfloor 5/2 \rfloor \cdot 2 + 2 = 6$.

Now take the point blowup in the $x$-chart with the translation $y \mapsto y + 1$. That is, $\pi(z) = xz$, $\pi(x) = x$, $\pi(y) = x(y + 1)$ and $\pi(w) = xw$. In characteristic $2$,
$$\pi(x + y) = x + x(y + 1) = xy, \qquad \pi\bigl(w (x + y)^4\bigr) = x^5 w y^4.$$
Thus
$$\pi(F) = x^2 \cdot x^2 (y + 1)^2 \cdot x^3 w^3 \cdot \bigl(x^5 w y^4 + x^{13}\bigr) = x^{12} (y + 1)^2 w^3 \bigl(w y^4 + x^8\bigr),$$
and by Lemma 1.3.6, with $(y + 1)^2 = y^2 + 1$,
$$F' = x^{-4} \pi(F) = x^8 w^3 \bigl(w y^4 + w y^6 + x^8 + x^8 y^2\bigr).$$
The monomial $x^8 w^4 y^4 = (x^2 w y)^4$ is a fourth power, and it is the only one, since the other exponents of $w$ are $3$. Cleaning removes it:
$$F'^{\mathrm{cl}} = x^8 w^3 \bigl(w y^6 + x^8 + x^8 y^2\bigr).$$
The translation of $y$ is not $0$, so $B = \{x, y\}$ and the new divisor is $E' = V(xw)$. The power series $w y^6 + x^8 + x^8 y^2$ is not divisible by $x$ or by $w$. So $G' = w y^6 + x^8 + x^8 y^2$ and the residual order is $d' = 7$. The order of $f'$ is still $4$.

Thus $d' = 7$ exceeds Moh's bound $6$ for this step. It agrees with Theorem 1.4.1, since $d + p^{e-1} = 5 + 2 = 7$.

Node: SG00000016 · Lean: none yet

The mechanism is visible in the computation. The term $w (x + y)^4$ of $G$ has a large order along the line $x = y$, and the translation $y \mapsto y + 1$ moves this line to the new origin. After the blowup, the term $w y^4$ is a fourth power times the exceptional factor $x^8 w^3$, and cleaning removes it. The remaining terms of $G'$ have larger order.

### The cycle of Hauser and Perlega

**Theorem 1.4.3 (Hauser and Perlega).** Let $K$ be an algebraically closed field of characteristic $p$. There is a purely inseparable equation $f = z^{p^3} + F(x_1, \dots, x_n)$ and an infinite sequence of point blowups such that the order of the strict transforms of $f$ stays $p^3$ and their residual orders tend to infinity. For $p = 2$ one can take $n = 5$, and for $p \ge 3$ one can take $n = 4$.

Node: SG00000017 · Lean: none yet

We do not reproduce the proof, which is a long explicit computation [HP19a, Section 4]. We describe the case $p = 2$, with the variables $x, y, u, v, w$. Let $d$ be an even positive integer. The starting equation is
$$f = z^8 + x^{8a+4} y^{8b+4} u^{8r} w^{8s-d} \bigl(w^d (\lambda + u^{2d+6} Q) + x^{d+1} u^{2d+6} A\bigr),$$
where $\lambda \in K^*$, $A$ is a unit, $Q$ is a power series, and $a, b, r, s$ are nonnegative integers with $8s \ge d$. Its residual order is $d$. The first blowup is in the $x$-chart with the translations $y \mapsto y + 1$ and $u \mapsto u + 1$. As in Example 1.4.2, the translation produces a term that cleaning removes, and the residual order increases from $d$ to $d + 4$. This agrees with Theorem 1.4.1, since $p^{e-1} = 4$. A further sequence of point blowups lowers the residual order to $d + 2$ and gives an equation of the same shape as the starting equation, with $d$ replaced by $d + 2$ and with the roles of $y$ and $u$, and of $b$ and $r$, exchanged. The residual order increases only at the first blowup, and the other blowups rebuild the shape of the equation. Thus the cycle can be repeated, and the residual order increases without bound.

Theorem 1.4.3 disproves Moh's stability theorem for $e \ge 3$. For $e = 1$ the stability theorem is known to hold [HP19a, Section 3].

**Remark 1.4.4.** Theorem 1.4.3 is not a counterexample to resolution in characteristic $p$. At several steps of the cycle, a center larger than a point is permissible, and a different sequence of blowups with a larger center need not make the residual order tend to infinity [HP19a, Section 3]. The examples show that, under point blowups in characteristic $p$, the pair (order, residual order) need not decrease in the long run. Thus a proof must choose the centers well, or it must use a secondary invariant that controls the increases.

### Notes and references

Moh's paper is [Moh87]. The counterexample to the stability theorem and the cycles are [HP19a]. Hauser and Perlega characterize the increase of the residual order in [HP19b]. Hauser introduced the term kangaroo point in [Hau08], and [Hau10] surveys the problem. The lab of the project plans to reproduce the cycles of [HP19a] in experiment E1, and to test candidate secondary invariants on them in experiment E2.
