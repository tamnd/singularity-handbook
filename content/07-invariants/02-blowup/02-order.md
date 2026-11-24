---
title: The order does not go up
nodes: [SG0000003A, SG0000003B]
sources: [Hir64, Hir67, Hir70, Hau03, Kol07, Benn70]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The order does not go up

In this section we prove that the order of the weak transform at a point over the origin is at most the order of $f$. Then we find the points where the order stays the same. The proof uses only the formula of Proposition 2.1.1, and it does not use the characteristic of $K$.

### The theorem

**Lemma 2.2.1.** Let $g \ne 0$ be a homogeneous polynomial of degree $m$, let $j \in \{1, \dots, n\}$ and let $t = (t_i)_{i \ne j}$ in $K^{n-1}$. Let
$$h = g(x_1 + t_1, \dots, 1, \dots, x_n + t_n),$$
with the entry $1$ at the place $j$. Then $h \ne 0$, $h$ does not contain $x_j$, and $\deg h \le m$.

*Proof.* Let $\sigma$ be the homomorphism $x_j \mapsto 1$. Two different monomials of degree $m$ differ in an exponent $\alpha_i$ with $i \ne j$, because the exponent $\alpha_j$ is determined by the others. So $\sigma$ sends the different monomials of $g$ to different monomials, and $\sigma(g) \ne 0$. Each monomial of $\sigma(g)$ has degree at most $m$. The translation $x_i \mapsto x_i + t_i$ is an automorphism of $K[x]$ with the inverse $x_i \mapsto x_i - t_i$, and it does not increase the degree. Thus $h \ne 0$ and $\deg h \le m$. The variable $x_j$ does not occur in $\sigma(g)$, and the translation does not introduce it. $\square$

**Theorem 2.2.2.** Let $f \in K[x]$ with $\operatorname{ord} f = m$, and let $f'$ be the weak transform of $f$ in the chart $\pi_{j,t}$. Then $\operatorname{ord} f' \le m$.

Node: SG0000003A · Lean: `Singularity.ord_le_of_pointChart`

*Proof.* Let $\tau$ be the homomorphism $x_j \mapsto 0$. It sends each monomial to the same monomial or to $0$, so it does not decrease the order: $\operatorname{ord} \tau(f') \ge \operatorname{ord} f'$. By Proposition 2.1.1, the terms with $d > m$ are multiples of $x_j$, so
$$\tau(f') = f_m(x_1 + t_1, \dots, 1, \dots, x_n + t_n).$$
Let $h = \tau(f')$. By Lemma 2.2.1, $h \ne 0$ and $\deg h \le m$. A nonzero polynomial has a monomial of degree at most its degree, so $\operatorname{ord} h \le \deg h$. Thus
$$\operatorname{ord} f' \le \operatorname{ord} h \le \deg h \le m. \qquad \square$$

The theorem is a statement about one chart at its origin. Each point of the exceptional divisor is the origin of a chart, so the order of the strict transform at each point over the origin is at most $m$. At the points of the strict transform that are not on the exceptional divisor, $\pi$ is an isomorphism, so the order is the order of $f$ at a point different from $0$. This proves the claim of Section 1.3 that $\operatorname{ord} f' \le q$ at each point over the origin.

**Corollary 2.2.3.** Let $X_0 = V(f) \subseteq \mathbb{A}^n$, and let $X_0 \leftarrow X_1 \leftarrow X_2 \leftarrow \cdots$ be a sequence of point blowups, where $X_{k+1}$ is the strict transform of $X_k$ under the blowup of a point $a_k$ of $X_k$, and $a_{k+1}$ lies over $a_k$. Then the sequence $\operatorname{ord}_{a_k} X_k$ does not increase.

*Proof.* After a translation, $a_k$ is the origin, and $a_{k+1}$ is the origin of a chart. Apply Theorem 2.2.2. $\square$

Theorem 2.2.2 is the case of a hypersurface and a point center of the theorem of Bennett, which says that the Hilbert-Samuel function does not go up under a permissible blowup [Benn70]. For a hypersurface, the Hilbert-Samuel function at a point is determined by the order, so the two theorems agree.

### The points where the order stays the same

**Definition 2.2.4.** Let $g$ be a homogeneous polynomial. The *directrix* of $g$ is the set $T(g)$ of the vectors $v \in K^n$ such that
$$g(x + s v) = g(x)$$
in the polynomial ring $K[x, s]$.

The set $T(g)$ is a linear subspace of $K^n$. If $v \in T(g)$ and $c \in K$, we substitute $cs$ for $s$ and get $cv \in T(g)$. If $v, w \in T(g)$, then $g(x + s(v + w)) = g((x + sv) + sw) = g(x + sv) = g(x)$. If $y_1, \dots, y_r$ are linear forms whose common zero set is $T(g)$, then $g$ is a polynomial in $y_1, \dots, y_r$ [Hir67, Section 1].

**Theorem 2.2.5.** Let $f \in K[x]$ with $\operatorname{ord} f = m$, and let $f'$ be the weak transform of $f$ in the chart $\pi_{j,t}$, with the vector $v$ of the chart. If $\operatorname{ord} f' = m$, then $v \in T(f_m)$.

Node: SG0000003B · Lean: none yet

*Proof.* Let $h$ be as in the proof of Theorem 2.2.2. Then $m = \operatorname{ord} f' \le \operatorname{ord} h \le \deg h \le m$. So $h$ is homogeneous of degree $m$. Write $f_m = \sum_{k=0}^{m} x_j^{m-k} g_k$, where the $g_k$ do not contain $x_j$ and $g_k$ is homogeneous of degree $k$. Then $h = \sum_k g_k(y + t)$, where $y$ is the vector of the variables $x_i$ with $i \ne j$. The part of degree $m$ of $h$ is $g_m(y)$, so $h = g_m(y)$.

We compute in the ring $K[x_j, x_j^{-1}, y]$. Since $f_m$ is homogeneous of degree $m$,
$$f_m(x_j, y + x_j t) = x_j^m f_m(1, x_j^{-1} y + t) = x_j^m h(x_j^{-1} y) = x_j^m g_m(x_j^{-1} y) = g_m(y).$$
Now let $u = (u_j, w)$ be a vector of new variables and let $s$ be one more variable. Put $a = u_j + s$ and $b = w - u_j t$. Then $u + sv = (a, b + a t)$, so
$$f_m(u + sv) = f_m(a, b + a t) = g_m(b) = g_m(w - u_j t).$$
The right side does not contain $s$. We put $s = 0$ and get $g_m(w - u_j t) = f_m(u)$. Thus $f_m(u + sv) = f_m(u)$, and $v \in T(f_m)$. $\square$

So the points of the exceptional divisor where the order stays $m$ lie in the projective space $\mathbb{P}(T(f_m))$. If $T(f_m) = 0$, then the order goes down at each point after one blowup. The converse of Theorem 2.2.5 is false, because the terms of $f$ of degree more than $m$ can also decrease the order, as the next examples show.

**Example 2.2.6.** Let $f = z^2 - x^3 - y^4$ as in Example 2.1.3, so $f_2 = z^2$. In each characteristic, the condition $(z + s v_z)^2 = z^2$ gives $v_z = 0$. So $T(f_2)$ is the plane $z = 0$. The lines with $v_z \ne 0$ are not in the tangent cone, so they give no points of $V(f')$. In the $y$-chart, $f' = (z + t_z)^2 - y (x + t_x)^3 - y^2$. For $t_z = 0$ and $t_x \ne 0$, the term $-t_x^3 y$ has order $1$, so $\operatorname{ord} f' = 1$. For $t_z = t_x = 0$, we get $f' = z^2 - x^3 y - y^2$, and $\operatorname{ord} f' = 2$. In the $x$-chart, $f' = (z + t_z)^2 - x - x^2 (y + t_y)^4$, and the order is at most $1$. So exactly one point over the origin has order $2$, the line through $(0, 1, 0)$. This line is in $T(f_2)$, as Theorem 2.2.5 says, but the other lines of $T(f_2)$ do not keep the order.

**Example 2.2.7.** Let $g = x^2 + y^2 + z^2$. If $p \ne 2$, then $g(x + sv) - g(x) = 2s(v_x x + v_y y + v_z z) + s^2 g(v)$, and this is $0$ only for $v = 0$. So $T(g) = 0$, and for each $f$ with $f_2 = g$ the order goes down at every point after one blowup. If $p = 2$, then $g = (x + y + z)^2$, and
$$g(x + sv) = g(x) + s^2 (v_x + v_y + v_z)^2.$$
So $T(g)$ is the plane $v_x + v_y + v_z = 0$, and the order $2$ can stay at each point of a line in the exceptional divisor. For $f = g$ itself, the $x$-chart with the translations $t_y$ and $t_z$ gives $f' = (1 + y + t_y + z + t_z)^2$, and $\operatorname{ord} f' = 2$ exactly when $1 + t_y + t_z = 0$, that is, when $v \in T(g)$.

Example 2.2.7 shows one source of the difficulties in characteristic $p$. A quadric of rank $3$ in characteristic $0$ improves after one blowup. In characteristic $2$ the same equation is the square of a linear form, and $V(g)$ is the plane $x + y + z = 0$ with multiplicity $2$. Each point of this plane has order $2$, so the blowup of one point cannot remove the singularity.

### Notes and references

Theorem 2.2.2 is classical. It is a part of the theory of Hironaka [Hir64], and [Kol07, Chapter 3] and [Hau03] give it for ideals. The directrix and the related additive groups in characteristic $p$ are from [Hir67] and [Hir70]. In characteristic $p$, Hironaka studies in [Hir70] the group scheme of the translations that keep $g$. This group scheme is also called the *ridge*. It need not be reduced. For $g = x_1^p$ the ridge is defined by $v_1^p = 0$, while $T(g)$ is the hyperplane $v_1 = 0$. Theorem 2.2.5 uses only $T(g)$.
