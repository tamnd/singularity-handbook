---
title: The coefficient ideal
nodes: [SG00000047]
sources: [Kol07, Vil89, EH02, Wlo05, Mat, BM97, Vil07, Vil08, BV10, Hau08, Hau10, Hau14]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The coefficient ideal

Theorem 3.1.3 describes the points of order at least $m$ on $S_i$ by $m$ marked ideals with different marks. We now pack them into one marked ideal on $S$. Then we prove the going-down and going-up theorem, and we discuss the dependence on the choice of the hypersurface. In the blowup sequences of this section we take $E = \emptyset$, as in Section 3.1. Section 3.3 checks the conditions on $E$ separately.

### Definition and first properties

**Definition 3.2.1 (coefficient ideal).** Let $(I, m)$ be a marked ideal with $m \ge 1$. The *coefficient ideal* of $(I, m)$ is the marked ideal $(C(I), m!)$ with
$$C(I) = \sum_{j=0}^{m-1} \big( D^j(I) \big)^{m! / (m - j)}.$$
For a smooth hypersurface $S$, we write $C_S(I) = C(I)|_S$, with the mark $m!$.

The exponents make all the summands have the same expected order: if $D^j(I)$ has order $m - j$, then its power has order $m!$.

**Lemma 3.2.2.** Let $N \ge 1$, let $B_1, \dots, B_t$ be ideal sheaves, and let $c_1, \dots, c_t \ge 1$ be integers that divide $N$. Let $B = \sum_j B_j^{N / c_j}$.

1. At each closed point $x$, $\operatorname{ord}_x B \ge N$ if and only if $\operatorname{ord}_x B_j \ge c_j$ for all $j$. So $\operatorname{cosupp}(B, N) = \bigcap_j \operatorname{cosupp}(B_j, c_j)$.
2. Let $\pi$ be the blowup of a smooth $Z \subseteq \operatorname{cosupp}(B, N)$, and let $B_j'$ be the transform of $(B_j, c_j)$. Then the transform of $(B, N)$ is $\sum_j (B_j')^{N / c_j}$.

Lean: `Singularity.le_idealOrd_iSup_pow_iff` (part 1, at the origin of affine space), `Singularity.chartTransformIdeal_iSup_pow` (part 2, for the blowup of a point in one chart)

*Proof.* (1) The graded ring of $\hat{\mathcal{O}}_{X, x}$ for the maximal ideal is a polynomial ring, so it has no zero divisors. Hence $\operatorname{ord}_x (fg) = \operatorname{ord}_x f + \operatorname{ord}_x g$, and $\operatorname{ord}_x (A^e) = e \operatorname{ord}_x A$ for each ideal $A$. The order of a sum of ideals is the minimum of the orders. So $\operatorname{ord}_x B = \min_j (N / c_j) \operatorname{ord}_x B_j$, and this is at least $N$ if and only if $\operatorname{ord}_x B_j \ge c_j$ for all $j$. (2) By (1), applied at the points of $Z$, $Z \subseteq \operatorname{cosupp}(B_j, c_j)$ for all $j$. Now apply Lemma 2.2.4 (1) and (2). $\square$

**Proposition 3.2.3 (tuning by the coefficient ideal).** Let $(I, m)$ be a marked ideal with $m \ge 1$. A sequence of blowups with smooth centers is a blowup sequence of order at least $m$ for $(I, m)$ if and only if it is a blowup sequence of order at least $m!$ for $(C(I), m!)$. If this holds, then $\operatorname{cosupp}(I_i, m) = \operatorname{cosupp}(C_i, m!)$ for each $i$, where $C_i$ is the $i$th transform of $(C(I), m!)$.

Lean: none yet

*Proof.* Let $J^{(j)}_i$ be as in Theorem 2.2.7. We show by induction on $i$ that, if the first $i$ blowups are of order at least $m$ for $(I, m)$, then $C_i = \sum_j (J^{(j)}_i)^{m!/(m-j)}$ and $\operatorname{cosupp}(C_i, m!) = \operatorname{cosupp}(I_i, m)$. The first claim follows from Lemma 3.2.2 (2), applied $i$ times. By Lemma 3.2.2 (1), $\operatorname{cosupp}(C_i, m!) = \bigcap_j \operatorname{cosupp}(J^{(j)}_i, m - j)$. Since $J^{(0)}_i = I_i$, this set lies in $\operatorname{cosupp}(I_i, m)$. Conversely, at a point of $\operatorname{cosupp}(I_i, m)$ the ideal $D^j(I_i)$ has order at least $m - j$ by Lemma 2.1.4, and $J^{(j)}_i \subseteq D^j(I_i)$ by Theorem 2.2.7. So the two cosupports are equal, and the center $Z_i$ is allowed for one marked ideal if and only if it is allowed for the other. $\square$

The point of the proposition is not the statement on $X$, which is easy, but the fact that $C(I)$ remembers the derivatives. The restriction of $C(I)$ to a hypersurface sees the derivatives in the normal direction.

### Going down and going up

**Theorem 3.2.4 (going down and going up).** Let $(I, m)$ be a marked ideal with $m \ge 1$, and let $S \subseteq X$ be a smooth hypersurface such that no irreducible component of $S$ lies in $\operatorname{cosupp}(I, m)$. Consider a sequence of blowups $X_r \to \dots \to X_0 = X$ with smooth centers $Z_i \subseteq S_i$, where $S_{i+1}$ is the birational transform of $S_i$, and the induced sequence $S_r \to \dots \to S_0 = S$. Then:

1. the sequence on $X$ is a blowup sequence of order at least $m$ for $(I, m)$ if and only if the sequence on $S$ is a blowup sequence of order at least $m!$ for $(C_S(I), m!)$;
2. if this holds, then each $Z_i$ has codimension at least 2 in $X_i$, no irreducible component of $S_i$ lies in $\operatorname{cosupp}(I_i, m)$, and
$$S_i \cap \operatorname{cosupp}(I_i, m) = \operatorname{cosupp}(C_{S, i}, m!),$$
where $C_{S, i}$ is the $i$th transform of $(C_S(I), m!)$ on $S$.

Node: SG00000047 · Lean: none yet

*Proof.* We argue by induction on the length. For $i = 0$, part (2) except the displayed equality is the hypothesis: a center in $S \cap \operatorname{cosupp}(I, m)$ contains no component of $S$, so it has codimension at least 2 in $X$. Assume that the first $i$ blowups are of order at least $m$ for $(I, m)$, equivalently of order at least $m!$ for $(C_S(I), m!)$, and that (2) holds up to $i$. Let $T^{(j)}_i$ be as in Theorem 3.1.3. By Theorem 3.1.3 (1), the $T^{(j)}_i$ are the transforms of the marked ideals $(D^j(I)|_S, m - j)$ on $S$. Restriction commutes with sums and products, so $C_S(I) = \sum_j (D^j(I)|_S)^{m!/(m-j)}$, and Lemma 3.2.2 (2) on $S$ gives $C_{S, i} = \sum_j (T^{(j)}_i)^{m!/(m-j)}$. By Lemma 3.2.2 (1) and Theorem 3.1.3 (2),
$$\operatorname{cosupp}(C_{S, i}, m!) = \bigcap_{j=0}^{m-1} \operatorname{cosupp}(T^{(j)}_i, m - j) = S_i \cap \operatorname{cosupp}(I_i, m).$$
Since $Z_i \subseteq S_i$, the center $Z_i$ lies in $\operatorname{cosupp}(I_i, m)$ if and only if it lies in $\operatorname{cosupp}(C_{S, i}, m!)$. This gives (1) for the first $i + 1$ blowups.

It remains to see that no component of $S_{i+1}$ lies in $\operatorname{cosupp}(I_{i+1}, m)$; then $Z_{i+1}$ contains no component of $S_{i+1}$, so it has codimension at least 2 in $X_{i+1}$, and Theorem 3.1.3 applies to the next step. Let $S^\circ$ be a component of $S_{i+1}$. By the displayed equality for $i + 1$, it lies in $\operatorname{cosupp}(I_{i+1}, m)$ if and only if $C_{S, i+1}$ has order at least $m! \ge 1$ at all closed points of $S^\circ$. If $C_{S, i+1}$ is not zero on $S^\circ$, then its zero set meets $S^\circ$ in a proper closed subset, and outside this subset the order is 0. So this happens only if $C_{S, i+1}$ vanishes on $S^\circ$. The blowup $S_{i+1} \to S$ is birational on each component, and the transform of a marked ideal is an invertible sheaf times its pullback, so this happens only if $C_S(I)$ vanishes on the image component of $S$. That would mean that this component lies in $\operatorname{cosupp}(C_S(I), m!) = S \cap \operatorname{cosupp}(I, m)$, which is excluded. $\square$

So, if $S$ is a hypersurface of maximal contact, order reduction on $X$ is the same as order reduction on $S$.

**Corollary 3.2.5.** Let $m = \operatorname{max\text{-}ord} I \ge 1$, and let $H$ be a hypersurface of maximal contact for $I$ such that no component of $H$ lies in $\operatorname{cosupp}(I, m)$. Then the blowup sequences of order $m$ for $(I, m)$ are exactly the sequences with centers $Z_i \subseteq H_i$ that are blowup sequences of order at least $m!$ for $(C_H(I), m!)$ on $H$. For them, $\operatorname{cosupp}(I_i, m) = \operatorname{cosupp}(C_{H, i}, m!)$. In particular, $(I_r, m)$ has empty cosupport if and only if $(C_{H, r}, m!)$ has empty cosupport.

Node: SG00000047 · Lean: none yet

*Proof.* By Theorem 2.3.3 (2), the centers of each blowup sequence of order $m$ lie in the transforms $H_i$, and $\operatorname{cosupp}(I_i, m) \subseteq H_i$. Now apply Theorem 3.2.4 with $S = H$. $\square$

**Example 3.2.6 (the Whitney umbrella).** Let $I = (x^2 - y^2 z)$ on $\mathbb{A}^3$, as in Example 1.3.3. The derivatives are $2x$, $-2yz$ and $-y^2$, so
$$D(I) = (x, \; yz, \; y^2), \qquad D^2(I) = \mathcal{O}.$$
So $m = \operatorname{max\text{-}ord} I = 2$, the locus $\operatorname{cosupp}(I, 2) = V(D(I))$ is the line $L = (x = y = 0)$, and $H = (x = 0)$ is a hypersurface of maximal contact. It is irreducible and it is not contained in $L$. The coefficient ideal is $C(I) = I + D(I)^2$, and in the coordinates $y, z$ of $H$,
$$C_H(I) = (y^2 z) + (yz, \; y^2)^2 = (y^2 z, \; y^4) = y^2 \cdot (z, \; y^2).$$
At a point of $H$ with $y \ne 0$ this ideal is the unit ideal. At a point of $L$ other than the origin it has order 2, and at the origin it has order 3. So $\operatorname{cosupp}(C_H(I), 2) = L$, as Corollary 3.2.5 predicts. The line $L$ is a smooth center of codimension 1 in $H$ and of codimension 2 in $\mathbb{A}^3$. Its blowup is the identity on $H$, and the transform of $(C_H(I), 2)$ is
$$\mathcal{O}_H(2L) \cdot C_H(I) = (z, \; y^2),$$
which has order at most 1 everywhere. So its cosupport for the mark 2 is empty, and by Corollary 3.2.5 the blowup of $L$ is a blowup sequence of order 2 with $\operatorname{cosupp}(I_1, 2) = \emptyset$. We check this on $X$: in the chart $x = x_1 y$ the transform of $(I, 2)$ is $(x_1^2 - z)$, and in the chart $y = y_1 x$ it is $(1 - y_1^2 z)$. Both have order at most 1. This is the computation of Example 1.3.3.

Lean: `Singularity.CharZeroExamples.derivIdeal_whitneyEq`, `Singularity.CharZeroExamples.derivIdeal_derivIdeal_whitneyEq`, `Singularity.CharZeroExamples.coeffIdeal_whitney`, `Singularity.CharZeroExamples.coeffIdeal_whitney_eq_mul`, `Singularity.CharZeroExamples.idealOrd_coeffIdeal_whitney`, `Singularity.CharZeroExamples.idealOrd_coeffIdeal_whitney_translate`, `Singularity.CharZeroExamples.idealOrd_transform_whitney` (the computations at the origin and at the points $(0, c)$)

The name of the coefficient ideal comes from the following special case. There the ideal on $H$ is built from the coefficients of $f$ as a polynomial in the normal coordinate, and its transforms are again built from the transformed coefficients.

**Example 3.2.7 (the classical coefficient ideal).** Let $m \ge 2$, let $X = \mathbb{A}^{n-1} \times \mathbb{A}^1$ with coordinates $x = (x_1, \dots, x_{n-1})$ and $z$, and let
$$f = z^m + \sum_{j=2}^m a_j(x) \, z^{m-j}, \qquad a_j \in k[x_1, \dots, x_{n-1}].$$
Assume that $\operatorname{ord}_0 a_j \ge j$ for all $j$. Let $I = (f)$, let $H = (z = 0)$, with the coordinates $x$, and let $A = \sum_{j=2}^m (a_j)^{m!/j}$ on $H$, with the mark $m!$. Then:

1. $\operatorname{max\text{-}ord} I = m$, and $H$ is a hypersurface of maximal contact for $I$.
2. $A \subseteq C_H(I)$, and $\operatorname{cosupp}(I, m) = \operatorname{cosupp}(C_H(I), m!) = \operatorname{cosupp}(A, m!) = \{ x \in H : \operatorname{ord}_x a_j \ge j \text{ for all } j \}$.
3. Let $Z \subseteq \operatorname{cosupp}(I, m)$ be given by $z = x_1 = \dots = x_c = 0$ with $c \ge 1$, and let $\pi \colon X_1 \to X$ be its blowup. We use the charts of Lemma 2.2.2 for the coordinates $z, x_1, \dots, x_c$ of $Z$. Let $U_z$ be the chart in which $z$ is the equation of the exceptional divisor. For $1 \le l \le c$, let $U_l$ be the chart in which $x_l$ is this equation, with the coordinates $z_1 = z / x_l$, $y_i = x_i / x_l$ for $i \le c$ and $i \ne l$, $x_l$, and $x_i$ for $i > c$. Then $U_z$ contains no point of $\operatorname{cosupp}(I_1, m)$, and $I_1$ is generated on $U_l$ by
$$f_1 = z_1^m + \sum_{j=2}^m b_j \, z_1^{m-j}, \qquad b_j = x_l^{-j} \, \pi^* a_j.$$
Here $b_j$ is a polynomial in the coordinates other than $z_1$, and on $H_1 \cap U_l = (z_1 = 0)$ it generates the transform of the marked ideal $(a_j, j)$ under the blowup of $H$ along $Z$.

Lean: none yet

*Proof.* Write $f = \sum_{i=0}^m a_{m-i} z^i$ with $a_0 = 1$ and $a_1 = 0$. Then
$$\partial_z^k f = \sum_{i \ge k} \frac{i!}{(i-k)!} \, a_{m-i} \, z^{i-k}, \qquad \big( \partial_z^k f \big)\big|_H = k! \, a_{m-k}.$$

(1) The function $\partial_z^m f = m!$ is a unit, so $D^m(I) = \mathcal{O}_X$ and $\operatorname{max\text{-}ord} I \le m$ by Corollary 2.1.5. The order at the origin is $m$, because each term $a_j z^{m-j}$ has order at least $j + (m - j) = m$ there. So $\operatorname{max\text{-}ord} I = m$. Also $\partial_z^{m-1} f = m! \, z$, since $a_1 = 0$. So $z \in D^{m-1}(I) = MC(I)$, and $H$ is a hypersurface of maximal contact.

(2) The formula with $k = m - j$ gives $a_j = ((m-j)!)^{-1} (\partial_z^{m-j} f)|_H$ lies in $D^{m-j}(I)|_H$, and so $a_j^{m!/j}$ lies in $\big(D^{m-j}(I)|_H\big)^{m!/j} \subseteq C_H(I)$. Hence $A \subseteq C_H(I)$. A larger ideal has smaller order, so $\operatorname{cosupp}(C_H(I), m!) \subseteq \operatorname{cosupp}(A, m!)$. By Lemma 3.2.2 (1), applied with $N = m!$ and $c_j = j$, the set $\operatorname{cosupp}(A, m!)$ is the set of points where $\operatorname{ord} a_j \ge j$ for all $j$. At such a point $(x', 0)$ each term $a_j z^{m-j}$ has order at least $m$, so $(x', 0) \in \operatorname{cosupp}(I, m)$. Finally, by Theorem 3.1.3 (2) for $i = 0$ and Lemma 3.2.2 (1), $\operatorname{cosupp}(C_H(I), m!) = H \cap \operatorname{cosupp}(I, m)$, and this is $\operatorname{cosupp}(I, m)$ by Lemma 2.3.2. The four sets are therefore equal.

(3) By (2), $a_j$ has order at least $j$ at each point of $Z$, as a function on $H$. By Proposition 2.1.7 on $H$, $a_j \in (x_1, \dots, x_c)^j$. On $U_l$ we have $z = z_1 x_l$, $x_i = y_i x_l$ for $i \le c$ and $i \ne l$, and the other coordinates do not change. So $\pi^* a_j$ is a polynomial in the coordinates other than $z_1$, and it is divisible by $x_l^j$. Then
$$\pi^* f = x_l^m z_1^m + \sum_{j=2}^m \pi^*(a_j) \, x_l^{m-j} z_1^{m-j} = x_l^m \, f_1,$$
so $I_1 = (x_l^{-m} \pi^* f) = (f_1)$ on $U_l$. By the proof of Theorem 2.3.3, $H_1 \cap U_l = (z_1 = 0)$, and the restrictions of the other coordinates are the chart coordinates of the blowup of $H$ along $Z$. On this chart of $H_1$ the exceptional divisor is $(x_l = 0)$, so the transform of $(a_j, j)$ is generated by $x_l^{-j} \pi^* a_j = b_j$. In the chart $U_z$ the function $\pi^* z$ is the equation of the exceptional divisor, so $H_1$ does not meet $U_z$. The blowup of $Z$ is a blowup sequence of order $m$, so $\operatorname{cosupp}(I_1, m) \subseteq H_1$ by Theorem 2.3.3 (2). $\square$

The polynomial $f_1$ has the same form as $f$ in the coordinates of the chart. So we can repeat the step, as long as the centers are coordinate subspaces in the charts. Along such a sequence the points of order $m$ of $I_i$ are the points of $H_i$ where the $i$th transforms of the marked ideals $(a_j, j)$ have order at least $j$. This is the classical form of going down. Two cases of this example appeared before. The running example $y^2 - x^5$ has $m = 2$, $z = y$ and $a_2 = -x^5$. Here $A = (x^5)$, and its transforms $(x^3)$ and $(x)$ are the coefficients of $y_1^2 - x^3$ and $y_2^2 - x$ in Example 2.2.9. The umbrella $x^2 - y^2 z$ of Example 3.2.6 has $m = 2$, the coordinate $x$ in the role of $z$, and $a_2 = -y^2 z$. Here $A = (y^2 z)$ is strictly smaller than $C_H(I) = y^2 \cdot (z, y^2)$, but both have the cosupport $L$ for the mark 2.

In the completion at a point of order $m$, each $f$ with $\partial_z^m f$ a unit takes the form of the example after the Weierstrass preparation theorem and the Tschirnhausen transformation of Section 2.3. The coefficients are then power series and not polynomials. The coefficient ideal $C(I)$ of Definition 3.2.1 needs neither step, and it is defined for every ideal.

*Remark (the order of the coefficient ideal).* In the setting of Example 3.2.7 we can compute the order of $C_H(I)$, not only its cosupport. For a closed point $q \in \operatorname{cosupp}(I, m)$ let
$$\lambda(q) = \min_{2 \le j \le m} \frac{\operatorname{ord}_q a_j}{j},$$
where the order is taken on $H$. By part (2) of the example, $\lambda(q) \ge 1$. We claim that
$$\operatorname{ord}_q C_H(I) = m! \, \lambda(q).$$
The inequality $\le$ holds because $a_j^{m!/j} \in C_H(I)$ by part (2), and this element has order $(m!/j) \operatorname{ord}_q a_j$. For $\ge$, note that $\operatorname{Der}_k$ is generated by the partial derivatives, so by the Leibniz rule $D^i(I)$ is generated by the functions $\partial_x^\alpha \partial_z^\beta f$ with $|\alpha| + \beta \le i$. For $i \le m - 1$ we have $\beta \le m - 1$, and the formula in the proof of Example 3.2.7 gives
$$\big( \partial_x^\alpha \partial_z^\beta f \big)\big|_H = \beta! \, \partial_x^\alpha a_{m - \beta},$$
with $a_1 = 0$. The order of this function at $q$ is at least $\operatorname{ord}_q a_{m-\beta} - |\alpha| \ge (m - \beta) \lambda - (i - \beta)$, with $\lambda = \lambda(q)$. Its power with the exponent $m!/(m - i)$ therefore has order at least $m!$ times
$$\frac{(m - \beta) \lambda - (i - \beta)}{m - i} = \lambda + \frac{(i - \beta)(\lambda - 1)}{m - i} \ge \lambda,$$
since $i \ge \beta$ and $\lambda \ge 1$. The order of a sum of ideals is the minimum of the orders, and the order of a power is the multiple of the order, as in the proof of Lemma 3.2.2. This proves the claim.

The claim explains the exponents of Definition 3.2.1. The derivative ideal $D^{m-j}(I)$ restricts on $H$ to an ideal that contains $a_j$, a coefficient whose expected order is $j$. The exponent $m!/j$ scales it to the common mark $m!$. After the division by $m!$, the order of $C_H(I)$ is the smallest ratio $\operatorname{ord} a_j / j$. This number is read off from the Newton polygon of $f$ in the variable $z$. Up to a normalization, the order of the coefficient ideal divided by its mark is the second entry of the resolution invariants of [BM97] and [EH02], after the order $m$. The derivatives $\partial_x^\alpha a_j$ do not change it. They are in $C(I)$ because the definition must not depend on the coordinates, and the claim shows that they do no harm.

*Example (a coefficient ideal with the mark 6).* Let $f = z^3 + x^4 z + y^5$ on $\mathbb{A}^3$, with $m = 3$, $a_2 = x^4$, $a_3 = y^5$ and $H = (z = 0)$ with the coordinates $x, y$. We compute $C_H(I)$ from Definition 3.2.1, without Example 3.2.7. The partial derivatives of $f$ are $4x^3 z$, $5y^4$ and $3z^2 + x^4$, and the second partial derivatives that do not vanish on $H$ are $\partial_x \partial_z f = 4x^3$ and $\partial_y^2 f = 20 y^3$. So
$$I|_H = (y^5), \qquad D(I)|_H = (y^5, 5y^4, x^4) = (x^4, y^4), \qquad D^2(I)|_H = (x^3, y^3).$$
With $m! = 6$ the exponents are $6/3 = 2$, $6/2 = 3$ and $6/1 = 6$, and
$$C_H(I) = (y^{10}) + (x^4, y^4)^3 + (x^3, y^3)^6.$$
The three summands have the orders 10, 12 and 18 at the origin. So $\operatorname{ord}_0 C_H(I) = 10$, and the claim of the remark gives the same value, $6 \cdot \min(4/2, 5/3) = 10$. The cosupport of $(C_H(I), 6)$ is the origin, the only point of $H$ where $\operatorname{ord} a_2 \ge 2$ and $\operatorname{ord} a_3 \ge 3$. We checked these ideals with a computer algebra system.

Now blow up the origin of $\mathbb{A}^3$, and use the charts of Example 3.2.7 (3). In the chart $U_x$ with $y = y' x$ we get $b_2 = x^{-2} x^4 = x^2$ and $b_3 = x^{-3} x^5 y'^5 = x^2 y'^5$, so
$$f_1 = z_1^3 + x^2 z_1 + x^2 y'^5.$$
At the origin of $U_x$ the ratios are $2/2 = 1$ and $7/3$, so $\lambda = 1$, and the coefficient ideal has order 6, equal to its mark. At the other points of the line $(x = 0)$ the function $b_3$ has order 2 < 3, so they are not in the cosupport. In the chart $U_y$ with $x = x' y$ we get $b_3 = y^{-3} y^5 = y^2$, of order at most 2, so this chart has no point of order 3. Thus $\operatorname{cosupp}(I_1, 3)$ is one point, and at it $\lambda$ dropped from $5/3$ to $1$. When $\lambda = 1$ the coefficient ideal has the order of its mark, and the next steps of the induction, in dimension 2, must lower the order of the coefficient ideal below its mark.

### The choice of the hypersurface

Hypersurfaces of maximal contact are local, and they are not unique. For the induction to give a global and functorial result, the construction on $H$ must not depend on $H$. The coefficient ideals on two hypersurfaces of maximal contact are isomorphic in many examples.

**Example 3.2.8.** Let $I = (xy - z^n)$ on $\mathbb{A}^3$ with $n \ge 2$. By Example 2.3.4, $m = 2$, $D(I) = (x, y, z^{n-1})$, and $H = (x = 0)$ and $H' = (x = y)$ are hypersurfaces of maximal contact. We use the coordinates $y, z$ on both. On $H$,
$$C_H(I) = (z^n) + (y, \; z^{n-1})^2 = (y^2, \; y z^{n-1}, \; z^n),$$
because $2n - 2 \ge n$. On $H'$, the restriction of $I$ is $(y^2 - z^n)$ and the restriction of $D(I)$ is $(y, z^{n-1})$, so
$$C_{H'}(I) = (y^2 - z^n) + (y, \; z^{n-1})^2 = (y^2, \; y z^{n-1}, \; z^n).$$
The restrictions of $I$ to $H$ and $H'$ are not isomorphic, since $(z^n)$ has order $n$ along a line and $(y^2 - z^n)$ has an isolated point of order 2. The coefficient ideals are the same.

Lean: `Singularity.DerivativeIdeals.coeffIdeal_H`, `Singularity.DerivativeIdeals.coeffIdeal_H'` (the ideals on $H$ and $H'$)

In general the coefficient ideals on two hypersurfaces of maximal contact need not be identified by an automorphism. Kollár, following Włodarczyk [Wlo05], solves this by replacing $I$ by an ideal with an extra invariance property.

**Definition 3.2.9 (MC-invariant ideals).** Let $m = \operatorname{max\text{-}ord} I \ge 1$. The ideal $I$ is *MC-invariant* if $MC(I) \cdot D(I) \subseteq I$.

**Proposition 3.2.10 (automorphisms close to the identity).** Let $K$ be a field of characteristic 0, let $R = K[[x_1, \dots, x_n]]$ with maximal ideal $\mathfrak{m}$, and let $I$ and $B \subseteq \mathfrak{m}$ be ideals of $R$ with $B \cdot D(I) \subseteq I$. Let $\varphi$ be a $K$-algebra automorphism of $R$ with $\varphi(x_i) - x_i \in B$ for all $i$. Then $\varphi(I) = I$, and $\varphi(r) - r \in B$ for every $r \in R$.

Lean: `Singularity.map_algEquiv_eq_of_mul_derivIdeal_le` (for $K[x_1, \dots, x_n]$ in place of $K[[x_1, \dots, x_n]]$)

*Proof.* First, $B \cdot D^{a+1}(I) \subseteq D^a(I)$ for all $a \ge 0$. For $a = 0$ this is the hypothesis. It suffices to show that the hypothesis passes from an ideal $J$ to $D(J)$. Let $b \in B$, $h \in D(J)$ and let $\partial$ be a partial derivative. Then
$$b \, \partial h = \partial(bh) - (\partial b) \, h.$$
Here $(\partial b) h \in D(J)$, and $bh \in B \cdot D(J) \subseteq J$, so $\partial(bh) \in D(J)$. Hence $B \cdot D(D(J)) \subseteq D(J)$. By induction, $B^j \cdot D^j(I) \subseteq B^{j-1} \cdot D^{j-1}(I) \subseteq \dots \subseteq I$ for all $j$.

Let $b_i = \varphi(x_i) - x_i \in B$. Since $\varphi$ is a $K$-algebra homomorphism of complete local rings, it is continuous, and $\varphi(f) = f(x_1 + b_1, \dots, x_n + b_n)$. In characteristic 0 the Taylor formula holds in $R$:
$$\varphi(f) = \sum_{\alpha} \frac{1}{\alpha!} \, \partial^\alpha f \cdot b^\alpha,$$
where the series converges in the $\mathfrak{m}$-adic topology, because $b^\alpha \in \mathfrak{m}^{|\alpha|}$. For $f \in I$ the term of index $\alpha$ lies in $B^{|\alpha|} D^{|\alpha|}(I) \subseteq I$. Each ideal $A$ of the Noetherian local ring $R$ is closed, because $\bigcap_s (A + \mathfrak{m}^s) = A$ by the Krull intersection theorem for $R/A$ [Mat, Section 8]. So $\varphi(f) \in I$, and $\varphi(I) \subseteq I$. Then $I \subseteq \varphi^{-1}(I) \subseteq \varphi^{-2}(I) \subseteq \dots$ is an ascending chain of ideals, so $\varphi^{-k}(I) = \varphi^{-k-1}(I)$ for some $k$, and applying $\varphi^{k+1}$ gives $\varphi(I) = I$. For the last claim, apply the Taylor formula to $r$: every term with $\alpha \ne 0$ lies in $B$, and $B$ is closed. $\square$

**Corollary 3.2.11 (formal uniqueness of maximal contact).** Let $I$ be MC-invariant with $m = \operatorname{max\text{-}ord} I$, let $E$ be a divisor with simple normal crossings, and let $x \in \operatorname{cosupp}(I, m)$ be a closed point. Let $H$ and $H'$ be hypersurfaces of maximal contact for $I$ near $x$ such that $H + E$ and $H' + E$ have simple normal crossings at $x$. Then there is an automorphism $\varphi$ of $\hat{\mathcal{O}}_{X, x}$ such that $\varphi(I \hat{\mathcal{O}}) = I \hat{\mathcal{O}}$, $\varphi$ maps the ideal of $\hat{H}$ to the ideal of $\hat{H}'$, it maps the ideal of each component of $\hat{E}$ to itself, and $\varphi(r) - r \in MC(I) \hat{\mathcal{O}}$ for all $r$.

Lean: `Singularity.maximalContact_change` (the last step, for polynomials, with the automorphism as a hypothesis)

*Proof.* Let $h, h' \in MC(I)$ be local equations of $H$ and $H'$, and let $e_2, \dots, e_t$ be local equations of the components of $E$ through $x$. Since $H + E$ and $H' + E$ have simple normal crossings, the classes of $h, e_2, \dots, e_t$ in $\mathfrak{m}_x / \mathfrak{m}_x^2$ are linearly independent, and so are those of $h', e_2, \dots, e_t$. The residue field $K = k(x)$ is infinite, so we can choose $x_{t+1}, \dots, x_n$ whose classes complete both families to a basis. By Lemma 2.1.1, $\hat{\mathcal{O}}_{X, x} = K[[h, e_2, \dots, e_t, x_{t+1}, \dots, x_n]]$, and also with $h'$ in place of $h$. Let $\varphi$ be the automorphism with $\varphi(h) = h'$ that fixes $K$ and the other coordinates. By the chain rule, the partial derivatives for the coordinates $h, e_2, \dots, x_n$ are combinations of those for $x_1, \dots, x_n$, and conversely, so $D(I)\hat{\mathcal{O}}$ is generated by $I \hat{\mathcal{O}}$ and its partial derivatives in either system. Then $\varphi(h) - h = h' - h \in MC(I)$, and the other coordinates are fixed. The ideal $MC(I)$ has order 1 at $x$, so it lies in $\mathfrak{m}_x$. Since $I$ is MC-invariant, $MC(I) \hat{\mathcal{O}} \cdot D(I \hat{\mathcal{O}}) \subseteq I \hat{\mathcal{O}}$. Proposition 3.2.10 with $B = MC(I) \hat{\mathcal{O}}$ gives the claims. $\square$

The last property says that $\varphi$ is the identity on $\hat{\mathcal{O}} / MC(I) \hat{\mathcal{O}}$. Since $\operatorname{cosupp}(I, m) = V(MC(I))$ by Corollary 2.1.5, the automorphism does not move the points of order $m$. So a construction that is invariant under isomorphisms gives the same first center near $x$, formally, when it starts from $H$ or from $H'$. The corollary does not give this for the later centers, and it does not give it for the centers on $X$ itself. For that one needs the étale form and the uniqueness theorem of Remark 3.2.12, which we cite.

**Remark 3.2.12 (tuning and uniqueness in [Kol07]).** We state without proof the results of [Kol07, Chapter 3] that make this work. For $m = \operatorname{max\text{-}ord} I$, Kollár defines
$$W_s(I) = \sum \Big\{ \prod_{j=0}^{m} D^j(I)^{c_j} \;:\; \sum_j (m - j) \, c_j \ge s \Big\}.$$
For suitable $s$, the ideal $W_s(I)$ is MC-invariant, it has maximal order $s$, its maximal contact ideal is $MC(I)$, and the blowup sequences of order at least $m$ for $(I, m)$ are the blowup sequences of order at least $s$ for $(W_s(I), s)$ (Section "Tuning of ideals"). The formal automorphism of Corollary 3.2.11 can be replaced by two étale maps $U \rightrightarrows X$, and then two blowup sequences of order $m$ for an MC-invariant ideal that are equivalent under these maps are equal (Section "Uniqueness of maximal contact"). Section 3.3 uses these results only in the proof of Theorem 3.3.6.

Lean: none yet

*Example (a component of $S$ in the cosupport).* Theorem 3.2.4 asks that no component of $S$ lies in $\operatorname{cosupp}(I, m)$. Let $I = (y^2)$ on $\mathbb{A}^2$ with $m = 2$, and let $S = (y = 0)$. Then $\operatorname{cosupp}(I, 2) = S$. We have $D(I) = (y^2, 2y) = (y)$, so $I|_S = 0$ and $D(I)|_S = 0$, and
$$C_S(I) = (I|_S) + (D(I)|_S)^2 = 0.$$
The zero ideal has every point in its cosupport for every mark, so the problem on $S$ cannot be solved, and order reduction in dimension $n - 1$ does not apply to it, since it needs an ideal that is nonzero on each component. The problem on $X$ is easy: the blowup of the curve $S$, a center of codimension 1, gives the transform $\mathcal{O}(2S) \cdot (y^2) = \mathcal{O}$. This is the first step $Z_{-1}$ in the proof of Lemma 3.3.4, which removes the components of $S$ in the cosupport before the restriction to $S$.

*Remark (positive characteristic).* Definition 3.2.1 makes sense in every characteristic. Theorem 3.2.4 uses Theorem 3.1.3, which divides by $k!$, and Corollary 3.2.5 uses hypersurfaces of maximal contact. These are the steps that fail in characteristic $p$. The coefficient ideal itself survives in several approaches to positive characteristic, for example in the work of Villamayor and his coauthors [Vil07], [Vil08], [BV10], and in the work of Hauser [Hau08], [Hau10], [Hau14].

### Notes and references

The coefficient ideal $C(I)$ is the one of Villamayor [Vil89] and Encinas-Hauser [EH02]. Kollár discusses it in [Kol07, Chapter 3] and prefers the ideals $W_s(I)$, which are both D-balanced and MC-invariant. Theorem 3.2.4 replaces his going-up theorem for D-balanced ideals. Proposition 3.2.10 and Corollary 3.2.11 are the formal part of his uniqueness theorem, whose idea he attributes to Włodarczyk [Wlo05].
