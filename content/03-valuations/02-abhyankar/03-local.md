---
title: The local form
nodes: []
sources: [Abh56, Har]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The local form

Abhyankar stated his inequality for a valuation that dominates a Noetherian local domain [Abh56]. The dimension of the ring replaces the transcendence degree. In this section we prove this local form with the Hilbert-Samuel function of Volume 1, Chapter 3, and an induction on the dimension. Then we compare it with the field form of Section 2.1.

In this section $(R, \mathfrak{m}, \kappa)$ is a Noetherian local domain with field of fractions $K$, and $v$ is a valuation of $K$ that dominates $R$. So $R \subseteq \mathcal{O}_v$ and $\mathfrak{m}_v \cap R = \mathfrak{m}$, and $\kappa$ is a subfield of $Kv$. For $\gamma \in \Gamma_v$ we put
$$P_\gamma = \{x \in R : v(x) \ge \gamma\}, \qquad P_\gamma^+ = \{x \in R : v(x) > \gamma\}.$$
These are ideals of $R$, and $P_\gamma^+ \subseteq P_\gamma$.

**Lemma 2.3.1.** Let $\gamma \in \Gamma_v$ and let $z_1, \dots, z_n \in R$ with $v(z_k) = \gamma$ for each $k$. Assume that the residues of $z_1/z_1, z_2/z_1, \dots, z_n/z_1$ in $Kv$ are linearly independent over $\kappa$. Then the classes of $z_1, \dots, z_n$ in $P_\gamma/P_\gamma^+$ are linearly independent over $\kappa$. Here $P_\gamma/P_\gamma^+$ is a $\kappa$-vector space, because $\mathfrak{m}P_\gamma \subseteq P_\gamma^+$.

Lean: none yet

*Proof.* Each element of $\mathfrak{m}$ has positive value, so $\mathfrak{m}P_\gamma \subseteq P_\gamma^+$. Let $c_1, \dots, c_n \in R$, not all in $\mathfrak{m}$, and assume that $\sum c_kz_k \in P_\gamma^+$. We divide by $z_1$. Then $\sum c_k(z_k/z_1)$ has positive value, so $\sum \bar{c}_k\overline{z_k/z_1} = 0$ in $Kv$, with $\bar{c}_k \in \kappa$ not all 0. This contradicts the assumption. $\square$

### Composite valuations

The proof of the local form uses an induction that splits a valuation into two. Let $v$ be a valuation of $K$, let $\Delta \subseteq \Gamma_v$ be a convex subgroup, and let $\mathfrak{p} = \mathfrak{p}_\Delta$ be the prime ideal of $\mathcal{O}_v$ of Proposition 1.2.3.

**Lemma 2.3.2.** Let $W = \{x \in K : v(x) \ge \delta \text{ for some } \delta \in \Delta\}$.

1. $W$ is a valuation ring of $K$ with $\mathcal{O}_v \subseteq W$ and maximal ideal $\mathfrak{p}$. Its group of units is $\{x : v(x) \in \Delta\}$, so $\Gamma_{v_W} \cong \Gamma_v/\Delta$ as groups.
2. The ring $\mathcal{O}_v/\mathfrak{p}$ is a valuation ring of the field $W/\mathfrak{p}$. Its valuation $\bar{v}$ has value group $\Delta$ and residue field $Kv$.

Lean: none yet

*Proof.* Since $\Delta$ is convex, an element $x$ is in $W$ if and only if $v(x) \in \Delta$ or $v(x) > \Delta$. This set is closed under sums and products, it contains $\mathcal{O}_v$, and for $x \ne 0$ it contains $x$ or $x^{-1}$. So $W$ is a valuation ring. The element $x \in W$ is a unit of $W$ if and only if $x^{-1} \in W$, that is, if and only if $v(x) \in \Delta$. So the maximal ideal of $W$ is $\{x : v(x) > \Delta\} = \mathfrak{p}$, and $v$ induces an isomorphism $K^\times/W^\times \cong \Gamma_v/\Delta$.

For part 2, note that $\mathfrak{p} \subseteq \mathcal{O}_v \subseteq W$. Let $z \in W/\mathfrak{p}$ be nonzero, with a lift $\hat{z} \in W \setminus \mathfrak{p}$. Then $\hat{z}$ is a unit of $W$, and $\hat{z} \in \mathcal{O}_v$ or $\hat{z}^{-1} \in \mathcal{O}_v$. So $z$ or $z^{-1}$ is in $\mathcal{O}_v/\mathfrak{p}$. The units of $W/\mathfrak{p}$ are the classes of the units of $W$, so $\bar{v}(z) = v(\hat{z})$ defines the valuation, and its value group is $\Delta$. Its maximal ideal is $\mathfrak{m}_v/\mathfrak{p}$, so its residue field is $\mathcal{O}_v/\mathfrak{m}_v = Kv$. $\square$

### The theorem

**Theorem 2.3.3 (Abhyankar).** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local domain with field of fractions $K$, and let $v$ be a valuation of $K$ that dominates $R$. Then
$$\operatorname{rr} \Gamma_v + \operatorname{trdeg}(Kv/\kappa) \le \dim R.$$

Lean: none yet

*Proof.* We use induction on $d = \dim R$. If $d = 0$, then $R = K$ is a field. Then $\mathfrak{m}_v \cap K = 0$, so $v$ is trivial and $Kv = K = \kappa$. Let $d \ge 1$. Choose generators of $\mathfrak{m}$, and let $\mu > 0$ be the least value of one of them. Then $v(x) \ge \mu$ for each $x \in \mathfrak{m}$. Let $\Delta$ be the set of $\gamma \in \Gamma_v$ with $|\gamma| \le k\mu$ for some integer $k$. It is the smallest convex subgroup that contains $\mu$. Let $\mathfrak{q} = \{x \in R : v(x) > \Delta\}$. This is $\mathfrak{p}_\Delta \cap R$, a prime ideal of $R$. It is not $\mathfrak{m}$, since $\mathfrak{m}$ has an element of value $\mu \in \Delta$.

Case A: $\mathfrak{q} = 0$. Then each nonzero element of $R$ has its value in $\Delta$. Let $r, s \ge 0$ be integers such that $\Gamma_v$ has $r$ elements that are linearly independent over $\mathbb{Z}$, and $Kv$ has $s$ elements that are algebraically independent over $\kappa$. We show that $r + s \le d$.

Step 1: the choice of elements. Each element of $K^\times$ is a quotient of elements of $R$, so $v(R \setminus 0)$ generates $\Gamma_v$. Thus we can choose $x_1, \dots, x_r \in R$ whose values $\gamma_1, \dots, \gamma_r$ are linearly independent. Next, each element of $\mathcal{O}_v$ is a quotient of two elements of $R$. We choose algebraically independent residues $\bar{u}_1, \dots, \bar{u}_s$ with $u_i = f'_i/g'_i$ and $f'_i, g'_i \in R$. Put $g = g'_1 \cdots g'_s$ and $f_i = f'_i\prod_{j \ne i} g'_j$. Then $u_i = f_i/g$, and $f_1, \dots, f_s, g$ all have the same value $\beta = v(g)$, since $v(u_i) = 0$. All these values are in $\Delta$, so there is an integer $k_0 \ge 1$ with $\gamma_i \le k_0\mu$ for each $i$ and $\beta \le k_0\mu$.

Step 2: many independent classes. Let $D \ge 0$ be an integer. For $b \in \mathbb{N}^s$ with $|b| = b_1 + \dots + b_s \le D$ put $h_b = f_1^{b_1} \cdots f_s^{b_s}g^{D - |b|} \in R$. Then $v(h_b) = D\beta$, and $h_b/g^D = u^b$. For $a \in \mathbb{N}^r$ the elements $x^ah_b$ with $|b| \le D$ all have the value $\delta_a = a \cdot \gamma + D\beta$. The quotient of $x^ah_b$ by $x^ag^D$ is $u^b$, and the residues $\bar{u}^b$ are distinct monomials in algebraically independent elements. So they are linearly independent over $\kappa$. By Lemma 2.3.1,
$$\dim_\kappa P_{\delta_a}/P_{\delta_a}^+ \ge \#\{b \in \mathbb{N}^s : |b| \le D\} = \binom{D + s}{s}.$$
For a fixed $D$, distinct $a$ give distinct values $\delta_a$, because the $\gamma_i$ are linearly independent.

Step 3: a lower bound for the length. For $N \ge 1$ we have $\mathfrak{m}^N \subseteq P_{N\mu}$. Let $\delta_1 < \delta_2 < \dots < \delta_t$ be values in $\Gamma_v$ with $0 \le \delta_j < N\mu$. Then
$$R \supseteq P_{\delta_1} \supseteq P_{\delta_1}^+ \supseteq P_{\delta_2} \supseteq P_{\delta_2}^+ \supseteq \dots \supseteq P_{\delta_t}^+ \supseteq P_{N\mu} \supseteq \mathfrak{m}^N.$$
The module $R/\mathfrak{m}^N$ has finite length. By Lemma 3.1.2 and Lemma 3.1.4 of Volume 1,
$$\ell(R/\mathfrak{m}^N) \ge \sum_{j=1}^t \dim_\kappa P_{\delta_j}/P_{\delta_j}^+.$$
Let $M = \lfloor (N - 1)/(2k_0) \rfloor$ and $D = M$. Let $a \in \mathbb{N}^r$ with $|a| \le M$. Then $2a \cdot \gamma \le 2Mk_0\mu < N\mu$ and $2D\beta \le 2Mk_0\mu < N\mu$, so $2\delta_a < 2N\mu$ and $\delta_a < N\mu$. We apply the inequality to the distinct values $\delta_a$ with $|a| \le M$, and we use Step 2:
$$\ell(R/\mathfrak{m}^N) \ge \binom{M + r}{r}\binom{M + s}{s} \ge \frac{M^{r+s}}{r!\,s!}.$$
Since $M \ge N/(2k_0) - 1$, there is a constant $C > 0$ with $\ell(R/\mathfrak{m}^N) \ge CN^{r+s}$ for all large $N$.

Step 4: an upper bound. By Theorem 1.1.2 of Volume 1, there is an $\mathfrak{m}$-primary ideal $I$ generated by $d$ elements. Then $I^N \subseteq \mathfrak{m}^N$, so $\ell(R/\mathfrak{m}^N) \le \ell(R/I^N)$. By Theorem 3.3.6 of Volume 1, $\ell(R/I^N)$ is a polynomial in $N$ of degree at most $d$ for large $N$. Together with Step 3 this gives $r + s \le d$. So $\operatorname{rr} \Gamma_v$ and $\operatorname{trdeg}(Kv/\kappa)$ are finite, and their sum is at most $d$.

Case B: $\mathfrak{q} \ne 0$. Let $W$, $\mathfrak{p} = \mathfrak{p}_\Delta$ and $\bar{v}$ be as in Lemma 2.3.2, and let $w = v_W$ and $L = W/\mathfrak{p}$. Then $R \subseteq W$ and $\mathfrak{p} \cap R = \mathfrak{q}$. As in Lemma 1.4.2, $W$ dominates the local ring $R_\mathfrak{q}$. Its dimension is $\operatorname{ht} \mathfrak{q} < d$, because $\mathfrak{q} \ne \mathfrak{m}$. By induction,
$$\operatorname{rr}(\Gamma_v/\Delta) + \operatorname{trdeg}(L/\kappa(\mathfrak{q})) \le \operatorname{ht} \mathfrak{q}.$$
The domain $R/\mathfrak{q}$ is a subring of $L$, and its field of fractions is $\kappa(\mathfrak{q}) \subseteq L$. Let $v'$ be the restriction of $\bar{v}$ to $\kappa(\mathfrak{q})$, with value group $\Delta' \subseteq \Delta$ and residue field $\kappa' \subseteq Kv$. An element of $R/\mathfrak{q}$ has positive value for $\bar{v}$ if and only if it comes from $\mathfrak{m}$. So $v'$ dominates $R/\mathfrak{q}$, and $\kappa \subseteq \kappa'$. Since $\mathfrak{q} \ne 0$, we have $\dim R/\mathfrak{q} \le d - \operatorname{ht} \mathfrak{q} < d$. By induction,
$$\operatorname{rr} \Delta' + \operatorname{trdeg}(\kappa'/\kappa) \le \dim R/\mathfrak{q}.$$
Theorem 2.1.4 for the extension $(L/\kappa(\mathfrak{q}), \bar{v})$ gives
$$\operatorname{rr}(\Delta/\Delta') + \operatorname{trdeg}(Kv/\kappa') \le \operatorname{trdeg}(L/\kappa(\mathfrak{q})).$$
The rational rank is additive in short exact sequences, because $- \otimes \mathbb{Q}$ is exact. So $\operatorname{rr} \Gamma_v = \operatorname{rr}(\Gamma_v/\Delta) + \operatorname{rr}(\Delta/\Delta') + \operatorname{rr} \Delta'$. The transcendence degree is additive in the tower $\kappa \subseteq \kappa' \subseteq Kv$. We add the three inequalities and get
$$\operatorname{rr} \Gamma_v + \operatorname{trdeg}(Kv/\kappa) \le \operatorname{ht} \mathfrak{q} + \dim R/\mathfrak{q} \le d. \qquad \square$$

In Case A with $r = 0$ or $s = 0$, the corresponding binomial coefficient is 1, and the proof works without change.

Abhyankar also proves that in the case of equality $\Gamma_v \cong \mathbb{Z}^r$ as a group and $Kv$ is a finitely generated extension of $\kappa$ [Abh56]. We do not prove this for a general $R$. For the local rings of varieties it follows from Theorem 2.2.2, as we show now.

### Comparison with the field form

**Corollary 2.3.4.** Let $X$ be an integral variety over a field $k$ with function field $K$, let $v$ be a valuation of $K/k$ with center $x$ on $X$, and let $R = \mathcal{O}_{X,x}$ with residue field $\kappa = \kappa(x)$. Then
$$\operatorname{trdeg}(K/k) - \operatorname{rr} \Gamma_v - \operatorname{trdeg}(Kv/k) = \dim R - \operatorname{rr} \Gamma_v - \operatorname{trdeg}(Kv/\kappa).$$
In particular Theorem 2.3.3 for $R$ gives Theorem 2.1.5 for $v$, and $v$ is an Abhyankar valuation if and only if equality holds in Theorem 2.3.3.

Lean: none yet

*Proof.* Let $\operatorname{Spec} B$ be an affine open set that contains $x$, and let $\mathfrak{p} \subseteq B$ be the prime of $x$. Then $B$ is a domain of finite type over $k$ with field of fractions $K$, and $R = B_\mathfrak{p}$. By [Har, Chapter I, Theorem 1.8A], $\dim B = \operatorname{trdeg}(K/k)$ and $\operatorname{ht} \mathfrak{p} + \dim B/\mathfrak{p} = \dim B$. Also $\dim B/\mathfrak{p} = \operatorname{trdeg}(\kappa/k)$ by the same theorem applied to $B/\mathfrak{p}$. So $\dim R + \operatorname{trdeg}(\kappa/k) = \operatorname{trdeg}(K/k)$. Since $k \subseteq \kappa \subseteq Kv$, transcendence degrees add: $\operatorname{trdeg}(Kv/k) = \operatorname{trdeg}(Kv/\kappa) + \operatorname{trdeg}(\kappa/k)$. Subtract the two equations. $\square$

By Proposition 1.4.4 each valuation of $K/k$ has a center on a projective model, so Theorem 2.3.3 implies Theorem 2.1.5 for function fields. The proof of Section 2.1 is shorter, and it needs no model.
