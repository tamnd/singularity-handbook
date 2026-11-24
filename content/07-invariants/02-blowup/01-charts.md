---
title: The point blowup in charts
nodes: [SG0000002E]
sources: [Hau03, Kol07, HP19a]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The point blowup in charts

In this section we describe the blowup of $\mathbb{A}^n$ at the origin with explicit coordinates. Each formula of the later sections is a formula in one chart.

### The charts

Let $\pi \colon \widetilde{\mathbb{A}}^n \to \mathbb{A}^n$ be the blowup at the origin. The variety $\widetilde{\mathbb{A}}^n$ is covered by $n$ affine charts $U_1, \dots, U_n$, and each chart is an affine space. In the chart $U_j$, the map $\pi$ is given by the homomorphism of $K$-algebras
$$\pi_j \colon K[x] \to K[x], \qquad \pi_j(x_j) = x_j, \qquad \pi_j(x_i) = x_j x_i \ (i \ne j).$$
The exceptional divisor is $V(x_j)$ in the chart $U_j$. Its points correspond to the lines through the origin of $\mathbb{A}^n$ that are not in the hyperplane $x_j = 0$. The point $(0, t)$ of $V(x_j)$, with $t = (t_i)_{i \ne j}$, corresponds to the line through the vector $v$ with $v_j = 1$ and $v_i = t_i$ for $i \ne j$.

To study the blowup at the point $(0, t)$, we move this point to the origin of the chart. The result is the homomorphism
$$\pi_{j,t} \colon K[x] \to K[x], \qquad \pi_{j,t}(x_j) = x_j, \qquad \pi_{j,t}(x_i) = x_j (x_i + t_i) \ (i \ne j).$$
This is the *$x_j$-chart with the translations $t$*. It is the map of Section 1.3 for $\Gamma = \{1, \dots, n\}$ [HP19a, Section 2]. Each point of the exceptional divisor is the origin of exactly one chart $\pi_{j,t}$ with $j$ the smallest index with $v_j \ne 0$, after we scale $v$ so that $v_j = 1$.

Lean: Singularity.pointChart

### The weak transform

**Proposition 2.1.1.** Let $f \in K[x]$ and let $m \in \mathbb{N}$ with $\operatorname{ord} f \ge m$. Then there is exactly one $f' \in K[x]$ such that
$$\pi_{j,t}(f) = x_j^m f'.$$
If $f = \sum_{d \ge m} f_d$, then
$$f' = \sum_{d \ge m} x_j^{d - m} \, f_d(x_1 + t_1, \dots, 1, \dots, x_n + t_n),$$
where the entry $1$ is at the place $j$.

Lean: Singularity.exists_pointChart_eq_X_pow_mul

*Proof.* Let $x^\alpha$ be a monomial of degree $d = |\alpha|$. Then
$$\pi_{j,t}(x^\alpha) = x_j^{\alpha_j} \prod_{i \ne j} x_j^{\alpha_i} (x_i + t_i)^{\alpha_i} = x_j^d \prod_{i \ne j} (x_i + t_i)^{\alpha_i}.$$
The last product is $x^\alpha$ evaluated at $x_j = 1$ and $x_i = x_i + t_i$ for $i \ne j$. By linearity, $\pi_{j,t}(f_d) = x_j^d f_d(x_1 + t_1, \dots, 1, \dots, x_n + t_n)$ for each $d$. We add these equations for $d \ge m$ and we take out the factor $x_j^m$. This gives the existence. The polynomial $f'$ is unique, because $K[x]$ is a domain and $x_j^m \ne 0$. $\square$

**Definition 2.1.2.** Let $f \ne 0$ with $\operatorname{ord} f = m$. The polynomial $f'$ of Proposition 2.1.1 is the *weak transform* of $f$ in the chart $\pi_{j,t}$.

For a hypersurface, the weak transform is the strict transform. The exceptional divisor $V(x_j)$ is not a component of $V(f')$, because $f'$ is not divisible by $x_j$. Indeed, the image of $f'$ under $x_j \mapsto 0$ is $f_m(x_1 + t_1, \dots, 1, \dots, x_n + t_n)$, and this polynomial is not $0$ by Lemma 2.2.1. For an ideal with more than one generator, the weak transform and the strict transform can be different [Hau03].

The origin of the chart is a point of the strict transform $V(f')$ if and only if $f'(0) = 0$. By Proposition 2.1.1, $f'(0) = f_m(v)$, where $v$ is the vector of the chart. Thus the points of the exceptional divisor that lie on the strict transform are the lines in the cone $f_m = 0$. This is the *tangent cone* of $V(f)$ at the origin.

**Example 2.1.3.** Let $f = z^2 - x^3 - y^4$ in $K[x, y, z]$. Then $\operatorname{ord} f = 2$ and $f_2 = z^2$. In the $y$-chart with the translations $t_x$ and $t_z$, we have
$$\pi(f) = y^2 (z + t_z)^2 - y^3 (x + t_x)^3 - y^4,$$
so $f' = (z + t_z)^2 - y (x + t_x)^3 - y^2$. The origin of the chart is on $V(f')$ if and only if $t_z = 0$, that is, if the line is in the plane $z = 0$, which is the tangent cone.

### Notes and references

The blowup in charts is in every text on resolution, for example and [Hau03, Section 4]. The notation of the charts with translations is from [HP19a, Section 2].
