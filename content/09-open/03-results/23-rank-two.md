---
title: Problem V7 for value group Z^2
nodes: [SG000000AS, SG000000AT, SG000000AV, SG000000AW, SG000000AX, SG000000AY, SG000000AZ, SG000000B0, SG000000B1, SG000000B2, SG000000B3, SG000000B4, SG000000B5, SG000000B6, SG000000B7, SG000000B8, SG000000B9, SG000000BA, SG000000BB, SG000000BC, SG000000BD]
sources: [KK09, KK05, NS14, Kuh10c, Kap42, Kuh10, Kuh10b, Kuh-book, Abh56s, CP09]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Problem V7 for value group $\mathbb{Z}^2$

This section reports the twenty-third research result, from the track VD (tamnd/singularity#298). It treats Problem V7 of research note 06 for valuations with value group $\mathbb{Z}^2$ on function fields of dimension 4. In rank 2 the problem is solved when the residue field of the coarsening is finitely generated, and an example shows that this hypothesis cannot simply be dropped from the argument. In rank 1 the problem reduces to a rational projection, and it is solved for every projection whose tower has the ball property at each step. This includes an explicit valuation that is not of the type of Knaf and Kuhlmann. The section also gives defect extensions of three kinds with value group exactly $\mathbb{Z}^2$, and a test family whose status is open.

Throughout, $k$ is an algebraically closed field of characteristic $p > 0$, $F/k$ is a function field of transcendence degree 4, and $\nu$ is a valuation of $F$, trivial on $k$, with residue field $F\nu = k$ and value group $\nu F \cong \mathbb{Z}^2$. We write $F^h$ for a henselization and $F^c$ for a completion of $(F, \nu)$. For an element $\vartheta$ of a valued field extension of $E$ we put $\nu(\vartheta - E) = \{\nu(\vartheta - c) : c \in E\}$ and $\operatorname{dist}(\vartheta, E) = \sup \nu(\vartheta - E)$ when the value group lies in $\mathbb{R}$.

### What Problem V7 asks

Problem V7 of note 06 asks: show that the rank one valuations of 4-dimensional function fields over $\overline{\mathbb{F}}_p$ whose projection has zero defect have local uniformization. Here local uniformization is Volume 3, Definition 4.1.1. By Volume 3, Proposition 4.1.6 it is the affine form: for each finite subset $S$ of $\mathcal{O}_\nu$ there is an affine model $A$ with $S \subseteq A \subseteq \mathcal{O}_\nu$ whose local ring at the center of $\nu$ is regular. So it is the strong form, for each finite set. Knaf and Kuhlmann call this property "strongly smoothly uniformizable" [KK09]. Over the perfect field $k$, smooth and regular centers give the same notion. The zero defect hypothesis is necessary: by [KK09, Theorem 1.6], if $(F, \nu)$ has local uniformization and $F\nu = k$, then $F \subseteq k(T)^h$ for some transcendence basis $T$ of $F/k$.

Two cases with residue field $k$ are known. If $\nu F$ has rational rank 4, then $\nu$ is an Abhyankar valuation and Volume 5, Theorem 2.2.1 applies. If $\nu F \cong \mathbb{Z}$, then $F$ lies in the completion of $k(t)$ for any $t$ with $\nu(t) = 1$ (Corollary 3.10 of note 57), and Theorem 3.23.2 below applies. The simplest group between these two cases is $\mathbb{Z}^2$. An ordered group isomorphic to $\mathbb{Z}^2$ has rank 1 or 2 (Volume 3, Definition 1.2.1), and the two cases behave very differently.

**Definition 3.23.1 (projection, adapted pair, Knaf-Kuhlmann type).** A *projection* is a transcendence basis $x_1, \dots, x_4$ of $F/k$ in $F$, with $K = k(x_1, \dots, x_4)$ and $K_i = k(x_1, \dots, x_i)$. If $\nu$ has rank 1, a pair $x_1, x_2$ is *adapted* if $\nu(x_1), \nu(x_2)$ is a basis of $\nu F$, and then $C = K_2^c$. For a pair $y = (y_1, y_2)$ whose values are a basis we write $C_y$ for the completion of $k(y_1, y_2)$. A subfield $F_0 \subseteq F$ that is a function field over $k$ is *dense* in $F$ if for each $a \in F$ and each $\alpha \in \nu F$ there is $b \in F_0$ with $\nu(a - b) \ge \alpha$, and we then write $F \subseteq F_0^c$. The valuation $\nu$ is of *Knaf-Kuhlmann type* (KK type) if $F \subseteq F_0^c$ for a subfield $F_0$ such that $\nu|_{F_0}$ is an Abhyankar valuation (Volume 3, Definition 2.2.3).

Node: SG000000AS · Lean: none yet

**Theorem 3.23.2 (Knaf-Kuhlmann [KK09, Theorem 1.5]).** Let $(F, v)$ be a valued function field over a perfect field $k$, with $v$ trivial on $k$. Assume that $F \subseteq F_0^c$ for a subfield $F_0$ such that $v|_{F_0}$ is an Abhyankar valuation. Then $v$ has local uniformization.

Lean: none yet

The theorem in [KK09] has two more hypotheses: $vF_0/vk$ is torsion free and $F_0v/kv$ is separable. Here $vk = 0$, and $vF_0$ is free by Volume 3, Corollary 2.2.4, so the first holds. The residue field $F_0v$ is finitely generated over $k$ by the same corollary, so it is separable over the perfect field $k$. We use Theorem 3.23.2 as a cited result. The proof in [KK09] uses only valuation theory.

Two facts on completions are used many times. Let $F_0 \subseteq F$ be dense. If $a \in F^\times$, choose $b \in F_0$ with $\nu(a - b) > \nu(a)$; then $\nu(b) = \nu(a)$. If $\nu(a) = 0$, choose $b$ with $\nu(a - b) > 0$; then $a$ and $b$ have the same residue. So $\nu F_0 = \nu F$ and $F_0\nu = F\nu$. The same argument works for each coarsening of $\nu$ whose topology is the topology of $\nu$.

### Rank 2

Assume that $\nu F$ has rank 2. Then $\nu F$ has a convex subgroup $\Delta$ with $\Delta \ne 0$ and $\Delta \ne \nu F$. Both $\Delta$ and $\nu F/\Delta$ are torsion free of rank 1 and finitely generated, so both are $\mathbb{Z}$, and $\nu F \cong \mathbb{Z}^2$ with the lexicographic order (Exercise 1). We write $\nu(x) = (v_1(x), n)$, where the first coordinate is the image in $\nu F/\Delta$. By Volume 3, Proposition 1.2.3 and Lemma 2.3.2, $\nu = v_1 \circ \bar{v}$: here $v_1$ is a discrete valuation of $F$ of rank 1 with value group $\mathbb{Z}$, and $\bar v$ is a discrete valuation of rank 1 of the residue field $\kappa = Fv_1$ with value group $\Delta = \mathbb{Z}$ and residue field $k$. Put $d = \operatorname{trdeg}(\kappa/k)$. The Abhyankar inequality (Volume 3, Theorem 2.1.4) for $v_1$ gives $1 + d \le 4$. Since $\bar v$ is not trivial on $\kappa$ and is trivial on the algebraically closed field $k$, $\kappa \ne k$, and so $d \ge 1$. Thus $d \in \{1, 2, 3\}$. If $d = 3$, then $v_1$ is an Abhyankar valuation, so $\kappa$ is finitely generated over $k$ by Volume 3, Corollary 2.2.4. For $d \in \{1, 2\}$ this can fail.

The topology of $\nu$ is the topology of $v_1$ (Exercise 3). So $F \subseteq F_0^c$ for $\nu$ if and only if $F \subseteq F_0^c$ for $v_1$, and then also $F_0 v_1 = \kappa$.

**Theorem 3.23.3.** Assume that $\kappa = Fv_1$ is finitely generated over $k$. Then there is a subfield $F_1 = k(z_1, \dots, z_d, \theta_0)$ of $F$ such that $v_1|_{F_1}$ is an Abhyankar valuation with value group $\mathbb{Z}$ and residue field $\kappa$, and $F \subseteq F_1^c$.

1. The valuation $v_1$ has local uniformization.
2. If $d = 1$, then $\nu|_{F_1}$ is an Abhyankar valuation, $\nu$ is of KK type, and $\nu$ has local uniformization.

Node: SG000000AT · Lean: none yet

*Proof.* Since $k$ is perfect, $\kappa/k$ is separable. Choose $z_1, \dots, z_d \in \mathcal{O}_{v_1}$ whose residues $\bar z_1, \dots, \bar z_d$ form a separating transcendence basis of $\kappa/k$, and choose $\bar\theta \in \kappa$ with $\kappa = k(\bar z)(\bar\theta)$, by the theorem of the primitive element. Let $\bar g \in k[Z_1, \dots, Z_d, \Theta]$ be the minimal polynomial of $\bar\theta$ over $k(\bar z)$, with the denominators cleared. Then $\bar g(\bar z, \bar\theta) = 0$, and $\partial_\Theta \bar g(\bar z, \bar\theta) \ne 0$ by separability.

Choose $\theta_0 \in \mathcal{O}_{v_1}$ with residue $\bar\theta$ and put $t = \bar g(z, \theta_0)$. Its residue is $\bar g(\bar z, \bar\theta) = 0$, so $v_1(t) \ge 1$. If $v_1(t) \ge 2$ (this includes $t = 0$), choose $s$ with $v_1(s) = 1$ and replace $\theta_0$ by $\theta_0 + s$. By the Taylor formula, $\bar g(z, \theta_0 + s) = t + \partial_\Theta \bar g(z, \theta_0)\, s + s^2 Q$ with $Q \in \mathcal{O}_{v_1}$. The middle term has value 1, because $\partial_\Theta \bar g(z, \theta_0)$ is a unit, and the other terms have value at least 2. So we may assume $v_1(t) = 1$.

The restriction of $v_1$ to $k(z)$ is trivial: for a nonzero $P \in k[Z]$ the residue of $P(z)$ is $P(\bar z) \ne 0$, so $v_1(P(z)) = 0$. If $\theta_0$ were algebraic over $k(z)$, then $F_1 = k(z, \theta_0)$ would be algebraic over $k(z)$, so $v_1 F_1$ would be a torsion group over $v_1 k(z) = 0$ (Volume 3, Corollary 2.1.3), and $v_1(t) = 1$ would be impossible. So $\operatorname{trdeg} F_1 = d + 1$. Since $t \in F_1$, $v_1 F_1 = \mathbb{Z}$, and since $\bar z, \bar\theta$ are residues of elements of $F_1$, $F_1 v_1 = \kappa$. So the Abhyankar inequality is an equality: $1 + d = \operatorname{trdeg} F_1$, and $v_1|_{F_1}$ is an Abhyankar valuation.

Density. Let $a \in \mathcal{O}_{v_1}$ and $m \ge 1$. Since $F_1v_1 = \kappa$ there is $b_0 \in \mathcal{O}_{v_1} \cap F_1$ with the residue of $a$, so $a = b_0 + t a_1$ with $a_1 \in \mathcal{O}_{v_1}$. Repeat with $a_1$. After $m$ steps, $a = b_0 + b_1 t + \dots + b_{m-1}t^{m-1} + t^m a_m$ with $b_i \in F_1$, so $v_1(a - b) \ge m$ for $b = \sum b_i t^i \in F_1$. For $a \notin \mathcal{O}_{v_1}$ apply this to $t^r a \in \mathcal{O}_{v_1}$. So $F \subseteq F_1^c$ for $v_1$.

Part 1 is Theorem 3.23.2 for $(F, v_1)$ and $F_1$.

Part 2. Let $d = 1$. Then $\operatorname{trdeg} F_1 = 2$. The group $\nu F_1$ contains $\nu(t) = (1, n)$ for some $n$. For $c \in \kappa^\times$ there is a unit $u$ of $\mathcal{O}_{v_1}$ in $F_1$ with residue $c$, and $\nu(u) = (0, \bar v(c))$. Since $\bar v(\kappa^\times) = \mathbb{Z}$, the group $\nu F_1$ contains $0 \times \mathbb{Z}$, and so $\nu F_1 = \mathbb{Z}^2$. The residue field is $F_1\nu = (F_1v_1)\bar v = \kappa\bar v = k$. So $\operatorname{rr}(\nu F_1) + \operatorname{trdeg}(F_1\nu/k) = 2 = \operatorname{trdeg} F_1$, and $\nu|_{F_1}$ is an Abhyankar valuation. Let $a \in F$ and $\alpha = (m, n) \in \nu F$. Choose $b \in F_1$ with $v_1(a - b) \ge m + 1$. Then $\nu(a - b) > (m, n)$ in the lexicographic order. So $F \subseteq F_1^c$ for $\nu$, the valuation $\nu$ is of KK type, and Theorem 3.23.2 gives local uniformization of $\nu$. $\square$

**Theorem 3.23.4.** If $d \ge 2$, then $\nu$ is not of KK type. No hypothesis on $\kappa$ is needed.

Node: SG000000AV · Lean: none yet

*Proof.* Assume that $F \subseteq F_0^c$ with $\nu|_{F_0}$ an Abhyankar valuation. By the facts on completions, $\nu F_0 = \mathbb{Z}^2$, $F_0\nu = k$, and, since the topologies of $\nu$ and $v_1$ agree, $F_0v_1 = \kappa$. The Abhyankar equality for $\nu|_{F_0}$ gives $\operatorname{trdeg} F_0 = 2 + 0 = 2$. The valuation $v_1$ is not trivial on $F_0$, so the Abhyankar inequality for $v_1|_{F_0}$ gives $1 + d \le 2$. This is false for $d \ge 2$. $\square$

So for $d \ge 2$ Theorem 3.23.2 does not apply to $\nu$ directly. The reduction to rank 1 of Novacoski and Spivakovsky closes this gap when $\kappa$ is finitely generated. We use the proof of [NS14, Theorem 1.1] in Section 3.1 of arXiv:1204.4751, which is pointwise. In the terms of [NS14], a local blowup of a local domain $R$ is a local ring $R[b_1/a, \dots, b_n/a]_{\mathfrak q}$, and a valuation centered on $R$ has local uniformization on $R$ if a finite sequence of local blowups of $R$ that the valuation dominates ends in a regular local ring. The proof gives the following. Let $R$ be a noetherian local domain essentially of finite type over $k$, let $\nu = v_1 \circ \bar v$ be centered on $R$, and let $\mathfrak p$ be the center of $v_1$ on $R$. Assume that $v_1$ has local uniformization on $R_{\mathfrak p}$, and that the restriction of $\bar v$ to $\kappa(\mathfrak p)$ has local uniformization on $R/\mathfrak p$. Then $\nu$ has local uniformization on $R$. The proof lifts the two sequences of local blowups and shows regularity with an explicit sequence of blowups.

**Theorem 3.23.5.** If $v_1$ has local uniformization, then $\nu$ has local uniformization. In particular, if $\kappa$ is finitely generated over $k$, then $\nu$ has local uniformization for each $d \in \{1, 2, 3\}$.

Node: SG000000AW · Lean: none yet

*Proof.* Let $S \subseteq \mathcal{O}_\nu$ be finite. Choose generators of $F/k$ in $\mathcal{O}_\nu$ (replace a generator $a \notin \mathcal{O}_\nu$ by $1/a$), and let $R$ be the localization of the $k$-algebra generated by them and by $S$ at the center of $\nu$. Let $\mathfrak p$ be the center of $v_1$ on $R$. The affine form of local uniformization of $v_1$, applied to the generators of $R$, gives an affine model $A \supseteq R$ with $A \subseteq \mathcal{O}_{v_1}$ and a regular local ring $A_{\mathfrak q}$, where $\mathfrak q = \mathfrak m_{v_1} \cap A$. Then $A_{\mathfrak q} \supseteq R_{\mathfrak p}$, and with a common denominator $A_{\mathfrak q}$ is a local blowup $R_{\mathfrak p}[b_1/a, \dots, b_n/a]_{\mathfrak q}$. The field $\kappa(\mathfrak p)$ is a finitely generated subfield of $\kappa$ of transcendence degree at most 3, and $\bar v|_{\kappa(\mathfrak p)}$ is centered on $R/\mathfrak p$. It has local uniformization by Volume 3, Proposition 4.1.7 if the transcendence degree is at most 1, by Theorem 4.1.4 (Abhyankar [Abh56s]) if it is 2, and by Theorem 4.1.5 (Cossart-Piltant [CP09]) if it is 3. The proof of [NS14, Theorem 1.1] then gives a regular local ring $R'$ that $\nu$ dominates, obtained from $R$ by a finite sequence of local blowups. Local blowups only make the ring larger, so $S \subseteq R \subseteq R'$. As $R'$ is a localization of a finitely generated $k$-algebra $A' \subseteq \mathcal{O}_\nu$ at the center of $\nu$, Volume 3, Proposition 4.1.6 gives local uniformization of $\nu$. The second sentence follows from Theorem 3.23.3, part 1. $\square$

For $d = 3$ this gives local uniformization but not local monomialization. [NS14, Theorem 1.2] would give monomialization if both $v_1$ and $\bar v$ had weak embedded local uniformization, and for a valuation of a threefold in characteristic $p$ this is not known in general.

The hypothesis on $\kappa$ is needed in the proof of Theorem 3.23.3. We use the following theorem of Kuhlmann.

**Theorem 3.23.6 ([Kuh10c, Theorem 1.1]).** "Let $K$ be any field. Take $\Gamma$ to be any non-trivial ordered abelian group of finite rational rank $\rho$, and $k$ to be any countably generated extension of $K$ of finite transcendence degree $\tau$. Choose any integer $n > \rho + \tau$. Then the rational function field in $n$ variables over $K$ admits a valuation whose restriction to $K$ is trivial, whose value group is $\Gamma$ and whose residue field is $k$."

Lean: none yet

In this quotation $k$ is the residue field of the theorem, not our ground field.

**Counterexample 3.23.7.** There is a valuation $\nu = v_1 \circ \bar v$ of $F = k(x_1, \dots, x_4)$, trivial on $k$, with $\nu F = \mathbb{Z}^2$ lexicographic, $F\nu = k$ and $d = 1$, that is not of KK type. One can take
$$\kappa = Fv_1 = k\big(z, (1 + z)^{1/\ell} : \ell \text{ prime}, \ell \ne p\big) \subset k((z))$$
and $\bar v$ the $z$-adic valuation.

Node: SG000000AX · Lean: none yet

*Proof.* For a prime $\ell \ne p$ the number $1/\ell$ lies in $\mathbb{Z}_{(p)}$, so the binomial series $\sum_i \binom{1/\ell}{i} z^i$ has coefficients in $\mathbb{F}_p$ and is an $\ell$-th root of $1 + z$ in $k[[z]]$. The polynomial $X^\ell - (1 + z)$ is irreducible over $k(z)$ by the criterion of Eisenstein at the prime $1 + z$ of $k[z]$ (Exercise 8), so $[k(z, (1+z)^{1/\ell}) : k(z)] = \ell$. If $\kappa$ were finitely generated over $k$, then $\kappa/k(z)$ would be finite of some degree $N$, and each prime $\ell \ne p$ would divide $N$. So $\kappa$ is not finitely generated. It is countably generated of transcendence degree 1. The restriction $\bar v$ of the $z$-adic valuation has value group $\mathbb{Z}$, because $\bar v(z) = 1$, and residue field $k$.

Theorem 3.23.6 with $K = k$, $\Gamma = \mathbb{Z}$, $\rho = 1$, $\tau = 1$ and $n = 4$ gives a valuation $v_1$ of $F$, trivial on $k$, with value group $\mathbb{Z}$ and residue field $\kappa$. The composite $\nu = v_1 \circ \bar v$ has a value group that is an extension of $\mathbb{Z}$ by $\mathbb{Z}$ with $0 \times \mathbb{Z}$ convex, that is $\mathbb{Z}^2$ lexicographic, and residue field $k$. Here $d = 1$.

Assume that $F \subseteq F_0^c$ with $\nu|_{F_0}$ an Abhyankar valuation. As in the proof of Theorem 3.23.4, $\operatorname{trdeg} F_0 = 2$, $v_1$ is not trivial on $F_0$, and $F_0v_1 = \kappa$. Then $\operatorname{rr}(v_1F_0) + \operatorname{trdeg}(F_0v_1/k) = 1 + 1 = 2 = \operatorname{trdeg} F_0$, so $v_1|_{F_0}$ is an Abhyankar valuation. By Volume 3, Corollary 2.2.4, $F_0v_1 = \kappa$ is finitely generated over $k$, a contradiction. $\square$

The same method gives examples with $d = 2$. Take $w \in k[[z]]$ transcendental over the countable field $\kappa$ (Exercise 9), and use $\kappa(w)$ with $\tau = 2$. For these, Theorem 3.23.3 does not apply, and Theorem 3.23.4 shows that $\nu$ is not of KK type. The following statement is the only open part of Problem V7 in rank 2.

**Conjecture 3.23.8.** Let $\nu = v_1 \circ \bar v$ be as above, with $d \in \{1, 2\}$ and $\kappa$ not finitely generated over $k$. Then $v_1$ has local uniformization. By Theorem 3.23.5, $\nu$ then has local uniformization.

Node: SG000000BD · Lean: none yet

Here $v_1$ is a discrete valuation of rank 1 whose residue field is not a function field. It is not of KK type (the argument of Counterexample 3.23.7 applies to $v_1$ itself), so Theorem 3.23.2 does not apply. We know no proof. The example of Counterexample 3.23.7 is the first test.

### Rank 1: the reduction to a rational projection

From now on $\nu$ has rank 1. By the theorem of Hölder, $\nu F$ embeds in $\mathbb{R}$, and after scaling $\nu F = \Gamma = \mathbb{Z} + \mathbb{Z}\alpha$ with $\alpha$ irrational. Let $x_1, x_2$ be an adapted pair. The values $\nu(x_1), \nu(x_2)$ are linearly independent over $\mathbb{Z}$, so distinct Laurent monomials in $x_1, x_2$ have distinct values, and $\nu|_{K_2}$ is the monomial valuation of Volume 5, Definition 2.1.1. Its value group is $\Gamma$ and its residue field is $k$. So $\nu|_{K_2}$ is an Abhyankar valuation, and $F/K_2$ is immediate: $\nu F = \nu K_2$ and $F\nu = K_2\nu$. In rank 1 the completion is henselian, so $E^h \subseteq E^c$ for each subfield $E$ [Kuh-book].

The explicit examples live in the Hahn field $H = k((t^\Gamma))$ of formal series $\sum_{\gamma} c_\gamma t^\gamma$ with well-ordered support, with $\nu$ the $t$-adic valuation, for $\Gamma = \mathbb{Z} + \mathbb{Z}\sqrt 2$. The field $H$ is complete and henselian, and $H/k(t, t^{\sqrt 2})$ is immediate [Kuh-book]. Let $D \subseteq H$ be the set of series with only finitely many support points below each bound.

**Lemma 3.23.9.** Let $x = (x_1, x_2)$ and $y = (y_1, y_2)$ be pairs in $F$ whose values are bases of $\Gamma$. If $x_1, x_2 \in C_y$, then $C_x = C_y$.

Node: SG000000AY · Lean: none yet

*Proof.* Write $\Gamma = \mathbb{Z} + \mathbb{Z}\alpha$. The valuations of $k(y_1, y_2)$ and of $k(t, t^\alpha) \subset H$ are monomial, and $y_i \mapsto t^{\nu(y_i)}$ is a $k$-isomorphism $k(y_1, y_2) \to k(t^\gamma : \gamma \in \Gamma) = k(t, t^\alpha)$ that keeps the values. The closure of $k(t, t^\alpha)$ in $H$ is $D$ (Lemma 3.23.18 below, whose proof works for each $\alpha$). So the isomorphism extends to an isomorphism of valued fields $C_y \cong D$, and we identify $C_y = D$.

Write $x_i = \lambda_i t^{\mu_i}(1 + \epsilon_i)$ with $\lambda_i \in k^\times$, $\mu_i = \nu(x_i)$, $\epsilon_i \in D$ and $\nu(\epsilon_i) > 0$. Since $(\mu_1, \mu_2)$ is a basis of $\Gamma$, there are integer vectors $n_1, n_2 \in \mathbb{Z}^2$ with $1 = n_{11}\mu_1 + n_{12}\mu_2$ and $\alpha = n_{21}\mu_1 + n_{22}\mu_2$. Write $X^{n_j} = x_1^{n_{j1}}x_2^{n_{j2}}$, $T_1 = t$ and $T_2 = t^\alpha$. Then
$$T_j = X^{n_j}\lambda'_j(1 + \eta_j), \qquad \lambda'_j = \lambda_1^{-n_{j1}}\lambda_2^{-n_{j2}}, \qquad 1 + \eta_j = (1 + \epsilon_1)^{-n_{j1}}(1 + \epsilon_2)^{-n_{j2}},$$
with $\eta_j \in D$. Let $c = \min(\nu(\eta_1), \nu(\eta_2)) > 0$, so the support of each $\eta_j$ lies in $[c, \infty)$.

Let $C' \subseteq D$ be the closure of $k(x_1, x_2)$, which is a completion $C_x$. Write $\eta_j = \sum_\gamma a_{j\gamma}t^\gamma$, and for $\gamma = a + b\alpha$ write $T'^\gamma = T_1'^aT_2'^b$. For a pair $T' = (T_1', T_2') \in C'^2$ with $\nu(T'_i) = \nu(T_i)$, the series $\eta_j(T') = \sum_\gamma a_{j\gamma}T'^\gamma$ converges in $C'$, because $\nu(T'^\gamma) = \gamma$ and only finitely many $\gamma$ in the support lie below each bound. Put
$$\Phi(T') = \big(X^{n_1}\lambda'_1(1 + \eta_1(T')),\ X^{n_2}\lambda'_2(1 + \eta_2(T'))\big) \in C'^2.$$
Then $\nu(\Phi(T')_j) = \nu(T_j)$, and $\Phi(T) = T$ with $T = (T_1, T_2)$. For two such pairs let $\operatorname{rel}(T', T'') = \min_i(\nu(T_i' - T_i'') - \nu(T_i))$.

Assume $\operatorname{rel}(T', T'') = r > 0$. Write $T''_i = T'_i(1 + \delta_i)$ with $\nu(\delta_i) \ge r$. For $\gamma = a + b\alpha$, $T''^\gamma - T'^\gamma = T'^\gamma\big((1 + \delta_1)^a(1 + \delta_2)^b - 1\big)$, and $\nu((1 + \delta)^a - 1) \ge \nu(\delta)$ for each $a \in \mathbb{Z}$ when $\nu(\delta) > 0$ (Exercise 6). So $\nu(T''^\gamma - T'^\gamma) \ge \gamma + r$, hence $\nu(\eta_j(T') - \eta_j(T'')) \ge c + r$, and $\operatorname{rel}(\Phi T', \Phi T'') \ge r + c$.

Start with $T^{(0)} = (X^{n_1}\lambda'_1, X^{n_2}\lambda'_2) \in C'^2$ and put $T^{(m+1)} = \Phi(T^{(m)})$. Then $\operatorname{rel}(T^{(0)}, T) = \min_j \nu(\eta_j) = c$, and by induction $\operatorname{rel}(T^{(m)}, T) \ge (m + 1)c$. So $T^{(m)} \to T$, and since $C'$ is closed, $t, t^\alpha \in C'$. Then $k(t, t^\alpha) \subseteq C'$, so $D \subseteq C'$. Since $x_1, x_2 \in D$, also $C' \subseteq D$. So $C_x = C' = D = C_y$. $\square$

A valued field $(E, \nu)$ is *algebraically maximal* if it has no proper immediate algebraic extension. It is *defectless* if each finite extension of $E^h$ has defect 1 in the sense of Volume 3, Definition 3.2.1. The defect of a finite extension $F/K$ of valued fields that are not henselian is the defect of $F^h/K^h$.

**Lemma 3.23.10.** Let $K$ be a projection with $x_1, x_2$ adapted.

1. The extension $F/K$ is immediate, and its defect is $[F^h : K^h]$. So $F/K$ has defect 1 if and only if $F \subseteq K^h$.
2. The field $C = K_2^c$ is defectless and algebraically maximal.
3. The valuation $\nu$ is of KK type if and only if $F \subseteq C$.

Node: SG000000AZ · Lean: none yet

*Proof.* 1. We have $K_2 \subseteq K \subseteq F$, and $F/K_2$ is immediate, so $F/K$ is immediate, and so is $F^h/K^h$. By the theorem of Ostrowski (Volume 3, Theorem 3.1.4) with $e = f = 1$, the defect is $[F^h : K^h]$. It is 1 if and only if $F^h = K^h$, that is, if and only if $F \subseteq K^h$.

2. The valuation of $K_2$ is an Abhyankar valuation, so $(K_2, \nu)$ is defectless by the generalized stability theorem (Volume 5, Theorem 2.2.2, [Kuh10]) over the trivially valued field $k$. A valued field of rank 1 is defectless if and only if its completion is defectless [Kuh-book]. So $C$ is defectless, and it is henselian. Let $L/C$ be an immediate algebraic extension and $L' \subseteq L$ a finite subextension. Then $L'/C$ is immediate with defect 1, so $[L' : C] = ef = 1$. So $L = C$.

3. If $F \subseteq C$, then $\nu$ is of KK type with $F_0 = K_2$. Conversely, let $F \subseteq F_0^c$ with $\nu|_{F_0}$ an Abhyankar valuation. Then $\nu F_0 = \Gamma$ and $F_0\nu = k$, so $\operatorname{trdeg} F_0 = 2$. Choose $y_1, y_2 \in F_0$ whose values are a basis of $\Gamma$. They are algebraically independent, $F_0/k(y)$ is finite and immediate, and $k(y)$ is defectless by Theorem 2.2.2 of Volume 5. So the defect of $F_0/k(y)$ is 1, and part 1 for this extension gives $F_0 \subseteq k(y)^h \subseteq C_y$. Hence $F \subseteq F_0^c \subseteq C_y$. In particular $x_1, x_2 \in C_y$, and Lemma 3.23.9 gives $C = C_x = C_y \supseteq F$. $\square$

The first proof of part 3 in note 76 said that $F_0K_2$ is a finite extension of $K_2$. This is false in general: $F_0$ and $K_2$ are two subfields of transcendence degree 2, and their compositum can have transcendence degree 4. Lemma 3.23.9 repairs the proof.

**Theorem 3.23.11.** Let $K \subseteq F$ be a subfield with $F/K$ finite and $F \subseteq K^h$. If $(K, \nu)$ has local uniformization, then $(F, \nu)$ has local uniformization.

Node: SG000000B0 · Lean: none yet

*Proof.* The valuation $\nu|_K$ is not trivial. The ramification index of $F/K$ is $e = 1$ and the residue degree is $f = 1$, because $F\nu = K\nu = k$ and $\nu F = \nu K$, and $k/k$ is separable. The defect is $[F^h : K^h]/(ef) = 1$, because $F^h = K^h$. By Volume 5, Lemma 1.3.3, second part, there is an étale generator of $F/K$ at $\nu$, and Volume 5, Theorem 1.3.4 lifts local uniformization from $K$ to $F$. $\square$

*Remark (the chart).* The chart can be made explicit. Write $F = K(\theta)$ with minimal polynomial $f$. Replace $\theta$ by $b\theta$ with $b \in K$ of large value, so that $f$ is monic with coefficients in $\mathcal{O}_\nu$. Since $K$ is dense in $K^h$, choose $c \in K \cap \mathcal{O}_\nu$ with $\nu(\theta - c) > \nu(f'(\theta))$. Then $\nu(f'(c)) = \nu(f'(\theta))$ and $\nu(f(c)) > 2\nu(f'(c))$. With $g_1 = f'(c)$, the polynomial $G(Y) = f(c + g_1Y)/g_1^2 = f(c)/g_1^2 + Y + Y^2Q(Y)$ has $Q \in \mathcal{O}_\nu[Y]$, and $\eta = (\theta - c)/g_1$ is its root of positive value. If $R$ is a regular local ring of $K$ that contains the coefficients of $G$, then $R' = (R[Y]/(G))_{(\mathfrak m_R, Y)}$ is étale over $R$, regular, with fraction field $F$. Alternatively, [KK09, Lemma 3.7 (2), (3)] with [KK09, Corollary 3.6] gives the theorem in the language of [KK09].

By Lemma 3.23.10 and Theorem 3.23.11, Problem V7 for $F$ follows from local uniformization of one projection $K$ with $F \subseteq K^h$. So the problem is about a rational function field $K = k(x_1, \dots, x_4)$ with an immediate valuation over $K_2$.

### Rank 1: towers with the ball property

Let $(L, \nu)$ be a valued field of rank 1 and $z$ an element of an immediate extension, transcendental over $L$. Following Kaplansky [Kap42], a sequence $(d_n)$ in $L$ is *pseudo Cauchy* if $\nu(d_l - d_m) > \nu(d_m - d_n)$ for $n < m < l$, and $z$ is a *limit* of it if $\gamma_n = \nu(z - d_n)$ is strictly increasing. Since $z$ is immediate over $L$, the set $\nu(z - L)$ has no largest element (Exercise 4). If $z \notin L^c$, this set is bounded, and we can choose $d_n \in L$ such that $\gamma_n$ is strictly increasing and cofinal in $\nu(z - L)$. Then $(d_n)$ is pseudo Cauchy with limit $z$, and we call it *cofinal*. For $h \in L[X]$ we write $h^{[j]}$ for the Hasse derivatives, so that $h(X + T) = \sum_j h^{[j]}(X)T^j$, and $h_j = \nu(h^{[j]}(z))$.

**Definition 3.23.12 (type, ball property).** A pseudo Cauchy sequence $(d_n)$ in $L$ is of *transcendental type* if for each $h \in L[X]$ the value $\nu(h(d_n))$ is constant for large $n$, and of *algebraic type* otherwise. The element $z$ has the *ball property* over $L$ if for each $h \in L[X]$ there are $\alpha$ and $a_0 \in L$ such that $\nu(h(a)) = \alpha$ for each $a \in L$ with $\nu(z - a) \ge \nu(z - a_0)$.

Node: SG000000B1 · Lean: none yet

The ball property is property (3) of [KK09, Lemma 2.17]. The balls $\{a \in L : \nu(z - a) \ge \beta\}$ around $z$ are nested, so the property holds for finitely many $h$ at once on one ball.

The basic computation is the following. Let $(d_n)$ be pseudo Cauchy with limit $z$, and let $h \in L[X]$ be nonconstant. Then $h(d_n) - h(z) = \sum_{j \ge 1} h^{[j]}(z)(d_n - z)^j$. The functions $\gamma \mapsto h_j + j\gamma$ for $j \ge 1$ with $h_j < \infty$ are lines of distinct slopes, so they cross in finitely many points, and the strictly increasing sequence $(\gamma_n)$ meets these points only finitely often. So for large $n$ the values $h_j + j\gamma_n$ are distinct, and
$$\nu(h(z) - h(d_n)) = m_n := \min_{j \ge 1}(h_j + j\gamma_n).$$
The sequence $(m_n)$ is strictly increasing, as a minimum of finitely many strictly increasing sequences.

**Lemma 3.23.13.** Let $z$ be transcendental over $L$ in an immediate extension.

1. If $z \in L^c$, then $z$ has the ball property over $L$.
2. If $z$ is a limit of a pseudo Cauchy sequence $(d_n)$ in $L$ of transcendental type, then $z$ has the ball property over $L$. More precisely, for each $h \in L[X]$ we have $m_n > h_0$ for large $n$, and $\nu(h(a)) = \nu(h(z))$ for each $a \in L$ with $\nu(z - a) \ge \gamma_n$.
3. If $L^c$ is algebraically maximal and $z \notin L^c$, then each cofinal pseudo Cauchy sequence in $L$ with limit $z$ is of transcendental type. So $z$ has the ball property over $L$.

Node: SG000000B2 · Lean: none yet

*Proof.* For $a \in L$ we have $h(a) - h(z) = \sum_{j \ge 1} h^{[j]}(z)(a - z)^j$, so
$$\nu(h(a) - h(z)) \ge \min_{j \ge 1}(h_j + j\nu(z - a)). \qquad (*)$$
Also $h_0 = \nu(h(z)) < \infty$, because $z$ is transcendental.

1. The right side of $(*)$ is larger than $h_0$ when $\nu(z - a) \ge \beta$ for some $\beta$. Since $z \in L^c$ there is $a_0 \in L$ with $\nu(z - a_0) \ge \beta$. Then $\nu(h(a)) = h_0$ for each $a$ with $\nu(z - a) \ge \nu(z - a_0)$.

2. For large $n$ the value $\nu(h(d_n))$ is constant, and $\nu(h(z) - h(d_n)) = m_n$ is strictly increasing. If $m_n < h_0$ for some large $n$, then $m_{n'} < h_0$ for all $n' \le n$, and for those $n'$ that are large $\nu(h(d_{n'})) = m_{n'}$ is strictly increasing; if this holds for all large $n$, we contradict the constancy. So $m_n \ge h_0$ for some $n$, and $m_n > h_0$ for all larger $n$. For such $n$ and $a \in L$ with $\nu(z - a) \ge \gamma_n$, $(*)$ gives $\nu(h(a) - h(z)) \ge m_n > h_0$, so $\nu(h(a)) = h_0$. This is the ball property with $a_0 = d_n$ and $\alpha = h_0$.

3. Let $(d_n)$ be cofinal with limit $z$, and assume that it is of algebraic type over $L$. The same polynomial shows that it is of algebraic type over $L^c$. By a theorem of Kaplansky [Kap42, Theorem 3], a pseudo Cauchy sequence of algebraic type without a limit in a field gives a proper immediate algebraic extension of that field. Since $L^c$ is algebraically maximal, $(d_n)$ has a limit $y \in L^c$, and $y \ne z$. Each limit satisfies $\nu(y - d_n) = \nu(d_{n+1} - d_n) = \gamma_n$. So $\nu(z - y) \ge \min(\nu(z - d_{n+1}), \nu(d_{n+1} - y)) = \gamma_{n+1} > \gamma_n$ for each $n$. Choose $c \in L$ with $\nu(y - c) > \nu(z - y)$. Then $\nu(z - c) = \nu(z - y) > \gamma_n$ for each $n$, which contradicts cofinality. So $(d_n)$ is of transcendental type, and part 2 applies. $\square$

The next lemma is a form of [KK09, Lemma 2.18]. It says that after a good choice of the center $d$, the Taylor expansion of each polynomial has a dominant constant term.

**Lemma 3.23.14 (Taylor expansion).** Let $z$ have the ball property over $L$, and let $Z \subseteq L[X]$ be a finite set of nonzero polynomials. Then there is $d \in L$ such that, with $\gamma = \nu(z - d)$,
$$\nu(h(z)) = \nu(h(d)) < \nu(h^{[j]}(d)) + j\gamma \quad \text{for each } h \in Z \text{ and each } j \ge 1 \text{ with } h^{[j]} \ne 0.$$

Node: SG000000B3 · Lean: none yet

*Proof.* Apply the ball property to all the polynomials $h^{[j]}$ with $h \in Z$ and $h^{[j]} \ne 0$, including $j = 0$. Since the balls are nested, there is one ball $B = \{a : \nu(z - a) \ge \rho\}$, with $\rho = \nu(z - a_0)$ for some $a_0 \in L$, on which each $\nu(h^{[j]}(a)) = \alpha_{h,j}$ is constant. For $a \in B$ with $\nu(z - a) = \gamma$ we have $h(z) = \sum_j h^{[j]}(a)(z - a)^j$. Call $\gamma \ge \rho$ *good* if the finitely many values $\alpha_{h,j} + j\gamma$, $j \ge 0$, are distinct for each $h \in Z$. Only finitely many $\gamma$ are not good. Since $\nu(z - L)$ has no largest element, it has infinitely many good elements $\gamma \ge \rho$. For good $\gamma = \nu(z - a)$ we get $\nu(h(z)) = \min(\alpha_{h,0}, M_h(\gamma))$ with $M_h(\gamma) = \min_{j \ge 1}(\alpha_{h,j} + j\gamma)$, which is strictly increasing in $\gamma$. If two good values $\gamma < \gamma'$ had $M_h(\gamma) \le \alpha_{h,0}$ and $M_h(\gamma') \le \alpha_{h,0}$, then $\nu(h(z))$ would be both $M_h(\gamma)$ and $M_h(\gamma') > M_h(\gamma)$. So for each $h$ at most one good value has $M_h(\gamma) \le \alpha_{h,0}$. Choose a good value $\gamma = \nu(z - d)$, $d \in B$, outside these finitely many exceptions. Then $M_h(\gamma) > \alpha_{h,0} = \nu(h(d)) = \nu(h(z))$ for each $h \in Z$. $\square$

**Theorem 3.23.15.** Let $\nu$ be a valuation of rank 1 of $K = k(x_1, x_2, x_3, x_4)$, trivial on $k$, with $K\nu = k$ and $\nu K = \Gamma \cong \mathbb{Z}^2$, and with $x_1, x_2$ adapted. Assume that $x_3$ has the ball property over $K_2$ and $x_4$ has the ball property over $K_3$. Then $(K, \nu)$ has local uniformization and local monomialization: for each finite $Z \subseteq \mathcal{O}_\nu \setminus \{0\}$ there is a regular local ring $R$ of $K$, essentially of finite type over $k$ and dominated by $\nu$, with a regular system of parameters $u_1, u_2, y_3, y_4$, such that $\nu(u_1), \nu(u_2)$ is a basis of $\Gamma$ and each $z \in Z$ is $u_1^au_2^b$ times a unit of $R$, with $a, b \ge 0$.

Node: SG000000B3 · Lean: none yet

*Proof.* For $i \in \{2, 3, 4\}$ let P($i$) be the statement: for each finite $Z \subseteq K_i^\times$ there is a regular local ring $R_i$ of $K_i$, the localization of a finitely generated $k$-algebra $A_i \subseteq \mathcal{O}_\nu$ with fraction field $K_i$ at the center of $\nu$, with a regular system of parameters $u_1, u_2, y_3, \dots, y_i$, where $u_1, u_2$ are Laurent monomials in $x_1, x_2$ whose values are a positive basis of $\Gamma$, such that each $z \in Z$ is $u_1^au_2^b$ times a unit of $R_i$ with $(a, b) \in \mathbb{Z}^2$, and $a, b \ge 0$ if $\nu(z) \ge 0$. The theorem is P(4): an element $z \in Z \subseteq \mathcal{O}_\nu$ is then in $R_4$, so a localization of $A_4$ at finitely many elements of value 0 is an affine model as in Volume 3, Proposition 4.1.6.

P(2). This is the proof of Volume 5, Theorem 2.1.5. Write each element of $Z$ as $f/g$ with Laurent polynomials $f, g$ in $x_1, x_2$. A Laurent polynomial $f = \sum_m c_mx^m$ has a unique term $c_{m_0}x^{m_0}$ of least value, and $f = c_{m_0}x^{m_0}(1 + \sum_m (c_m/c_{m_0})x^{m - m_0})$ with $\nu(x^{m - m_0}) > 0$. By the lattice lemma (Volume 5, Lemma 2.1.4) there is a positive basis $\nu(u_1), \nu(u_2)$ of $\Gamma$, with $u_1, u_2$ Laurent monomials, such that all these values $\nu(x^{m - m_0})$ and all the values $\nu(z) \ge 0$ of elements of $Z$ are combinations of $\nu(u_1), \nu(u_2)$ with coefficients in $\mathbb{N}$. Then $A_2 = k[u_1, u_2]$ is a polynomial ring with fraction field $K_2$, and $R_2 = (A_2)_{(u_1, u_2)}$ is dominated by $\nu$. Each $x^{m - m_0}$ is $u_1^au_2^b$ with $a, b \ge 0$ not both 0, so it lies in the maximal ideal, and each $f$ is a monomial times a unit. So each $z \in Z$ is $u^e$ times a unit. If $\nu(z) \ge 0$, the vector $e$ is determined by $\nu(z)$ because $\nu(u_1), \nu(u_2)$ is a basis, so $e \in \mathbb{N}^2$.

P($i - 1$) implies P($i$). Let $L = K_{i-1}$ and $z_i = x_i$. Let $Z \subseteq K_i^\times$ be finite, and write each element as $f(x_i)/g(x_i)$ with $f, g \in L[X]$ nonzero. Let $Z'$ be the finite set of these $f$ and $g$. Lemma 3.23.14 gives $d \in L$ with $\gamma = \nu(x_i - d)$ and $\nu(h^{[j]}(d)) + j\gamma > \nu(h(d)) = \nu(h(x_i))$ for each $h \in Z'$ and $j \ge 1$. Choose $N \in L$ with $\nu(N) = \gamma$, which is possible since $\nu L = \Gamma$, and put $Y = (x_i - d)/N$. Then $\nu(Y) = 0$, and
$$h(x_i) = \sum_j h^{[j]}(d)N^jY^j = h(d)\Big(1 + \sum_{j \ge 1}\rho_{h,j}Y^j\Big), \qquad \rho_{h,j} = \frac{h^{[j]}(d)N^j}{h(d)}, \quad \nu(\rho_{h,j}) > 0.$$
Apply P($i - 1$) to the finite set of the elements $h(d)$ for $h \in Z'$, the nonzero $\rho_{h,j}$, and the quotients $f(d)/g(d)$ for $f/g \in Z$. This gives $R_{i-1} = (A_{i-1})_{\mathfrak m}$. Let $\lambda \in k^\times$ be the residue of $Y$, put $A_i = A_{i-1}[Y]$, $y_i = Y - \lambda$, and $R_i = R_{i-1}[Y]_{(\mathfrak m, Y - \lambda)}$. Since $Y$ is transcendental over $L$, $A_i$ is a polynomial ring over $A_{i-1}$ with fraction field $L(Y) = K_i$. The ideal $(\mathfrak m, Y - \lambda)$ is maximal in $R_{i-1}[Y]$ with residue field $k$, and it lies in the center of $\nu$, so it is the center, and $R_i$ is dominated by $\nu$. It is regular with the regular system of parameters $u_1, u_2, y_3, \dots, y_i$. Each nonzero $\rho_{h,j}$ has positive value, so by P($i - 1$) it is $u_1^au_2^b$ times a unit with $a, b \ge 0$ not both 0, and it lies in the maximal ideal. So $1 + \sum_{j \ge 1}\rho_{h,j}Y^j$ is a unit of $R_i$, and $h(x_i) = u^{e_h}$ times a unit, where $h(d) = u^{e_h}$ times a unit of $R_{i-1}$. For $z = f(x_i)/g(x_i) \in Z$ we get $z = u^{e_f - e_g}$ times a unit. If $\nu(z) \ge 0$, then $\nu(f(d)/g(d)) = \nu(z) \ge 0$, and since $f(d)/g(d)$ is in the set, its exponent vector $e_f - e_g$ lies in $\mathbb{N}^2$. $\square$

The quotients $f(d)/g(d)$ are put into the finite set of the induction, so no further change of the monomials $u_1, u_2$ is needed at the end. The rings $R_i$ are localizations of finitely generated $k$-algebras, but in general not of polynomial rings, because $d$ and $N$ have denominators. So the polynomial form of ELU(4) of note 57 is not claimed. The theorem is also a consequence of [KK09, Lemma 3.9] and [KK09, Corollary 3.6], applied twice.

**Corollary 3.23.16.** Let $K$ be a projection with $x_1, x_2$ adapted and $F \subseteq K^h$. Assume one of the following.

1. $x_3 \in C$.
2. $x_4 \in K_3^c$.
3. $K_3^c$ is algebraically maximal.

Then $(F, \nu)$ has local uniformization.

Node: SG000000B4 · Lean: none yet

*Proof.* The element $x_3$ is transcendental over $K_2$ in the immediate extension $F/K_2$. It has the ball property over $K_2$: by Lemma 3.23.13, part 1, if $x_3 \in C$, and by part 3 otherwise, since $C$ is algebraically maximal (Lemma 3.23.10). In case 1, $K_2 \subseteq K_3 \subseteq C$, so $K_3^c = C$ is algebraically maximal. So in each case $x_4$ has the ball property over $K_3$, by part 1 or part 3 of Lemma 3.23.13. Theorem 3.23.15 gives local uniformization of $K$, and Theorem 3.23.11 gives it for $F$. $\square$

When no projection has the ball property at both steps, the situation is as follows. Let $K$ be a projection with $F \subseteq K^h$ and $x_3 \notin C$, and assume that a cofinal pseudo Cauchy sequence of $x_4$ in $K_3$ is of algebraic type. By [Kap42, Theorem 3], $K_3^h$ has a proper immediate algebraic extension, and by the theory of key polynomials (Volume 3, Definition 3.3.25) it is generated by a root of a limit key polynomial of degree $p^e$ with $e \ge 1$, so it has defect $p^e$ [Kuh-book]. So the remaining case of Problem V7 for $\mathbb{Z}^2$ in rank 1 is a question about the choice of the projection.

**Conjecture 3.23.17 (a good projection, Problem 7.2 of note 76).** Let $\nu$ be a valuation of rank 1 of $F$ with $\nu F \cong \mathbb{Z}^2$, $F\nu = k$, and $F \subseteq K^h$ for a projection $K$. Then there is a projection $K' = k(x'_1, \dots, x'_4)$ with $F \subseteq K'^h$ and $x'_1, x'_2$ adapted, such that $x'_3$ has the ball property over $K'_2$ and $x'_4$ has the ball property over $K'_3$.

Node: SG000000BC · Lean: none yet

By Theorems 3.23.11 and 3.23.15, Conjecture 3.23.17 implies Problem V7 for valuations of rank 1 with value group $\mathbb{Z}^2$. It is open. Example 3.23.23 below is the first test.

### An explicit valuation that is not of KK type

For the explicit valuations, let $k = \overline{\mathbb{F}}_p$, $\Gamma = \mathbb{Z} + \mathbb{Z}\sqrt 2$ and $H = k((t^\Gamma))$, and let $K_2 = k(t, t^{\sqrt 2}) \subset H$. Let $r_m/q_m$ be the solutions of $r^2 - 2q^2 = 1$ in positive integers, in increasing order: $3/2$, $17/12$, $99/70$, and so on. Then
$$q_m\sqrt 2 - r_m = \frac{2q_m^2 - r_m^2}{r_m + q_m\sqrt 2} = \frac{-1}{r_m + q_m\sqrt 2} < 0,$$
which increases strictly to 0 (Exercise 5). For $\delta \in \Gamma$ put $\gamma_m(\delta) = \delta + q_m\sqrt 2 - r_m \in \Gamma$ and
$$\vartheta_\delta = \sum_{m \ge 1} t^{\gamma_m(\delta)} \in H.$$
Its support is a strictly increasing sequence with limit $\delta$.

**Lemma 3.23.18.** The closure of $K_2$ in $H$, which is the completion $C$ of $K_2$, is the field $D$ of series with finitely many support points below each bound. Let $\vartheta \in H$ have a support whose least accumulation point is $\delta$, with only finitely many support points below $\delta - \epsilon$ for each $\epsilon > 0$. Then $\operatorname{dist}(\vartheta, K_2) = \operatorname{dist}(\vartheta, C) = \delta$, the supremum is not attained, and $\vartheta \notin C$.

Node: SG000000B5 · Lean: none yet

*Proof.* Let $P = k[t^{\pm 1}, t^{\pm\sqrt 2}]$ be the ring of finite sums $\sum c_\gamma t^\gamma$. A nonzero $f \in P$ is $ct^\gamma(1 - \epsilon)$ with $\epsilon \in P$ of positive value, so $1/f = c^{-1}t^{-\gamma}\sum_n \epsilon^n$ is a limit of elements of $P$. So $K_2$ lies in the closure of $P$, and the closures of $K_2$ and of $P$ agree. An element $c$ of the closure agrees, below each bound $\beta$, with an element of $P$ that approximates it to a value larger than $\beta$, so its support has finitely many points below $\beta$. Conversely, an element of $D$ is the limit of its truncations, which lie in $P$. So the closure is $D$, and since $H$ is complete, $D = C$.

The truncation of $\vartheta$ below $\delta - \epsilon$ lies in $P \subseteq K_2$ and approximates $\vartheta$ to a value at least $\delta - \epsilon$. So $\operatorname{dist}(\vartheta, K_2) \ge \delta$. For $c \in C = D$, the support of $\vartheta$ has infinitely many points below $\delta$ and that of $c$ only finitely many, so $\vartheta - c$ has a support point below $\delta$, and $\nu(\vartheta - c) < \delta$. $\square$

**Example 3.23.19.** Let $\nu$ be the valuation of $K = k(x_1, x_2, x_3, x_4)$ given by the embedding into $H$ with
$$x_1 \mapsto t, \qquad x_2 \mapsto t^{\sqrt 2}, \qquad x_3 \mapsto s = \sum_{n \ge 1}t^{n!}, \qquad x_4 \mapsto \vartheta_0 = \sum_{m \ge 1}t^{q_m\sqrt 2 - r_m}.$$
Then $x_1, \dots, x_4$ are algebraically independent, $\nu K = \Gamma$, $K\nu = k$, the valuation has local uniformization on $K$ and on each $F \subseteq K^h$, and it is not of KK type.

Node: SG000000B6 · Lean: none yet

*Proof.* The series $s$ is transcendental over $k(t)$ (note 59, Lemma R3). Suppose that $Q(s) = 0$ for a nonzero $Q \in k[t][Y]$ of degree $D$ in $Y$ and degree $c$ in $t$. Let $s_n = \sum_{m \le n}t^{m!} \in k[t]$, so $\nu(s - s_n) = (n + 1)!$. Since $Q$ has only finitely many roots, $Q(s_n) \ne 0$ for large $n$. Then $Q(s_n) = Q(s_n) - Q(s)$ is divisible by $s_n - s$ in $k[t][[t]]$, so $\nu(Q(s_n)) \ge (n + 1)!$. But $Q(s_n)$ is a nonzero polynomial in $t$ of degree at most $c + D \cdot n!$, so its value is at most $c + D \cdot n!$. For large $n$ this is less than $(n + 1)!$, a contradiction.

The element $t^{\sqrt 2}$ is transcendental over $k((t)) \supseteq k(t, s)$: an element algebraic of degree $n$ over $k((t))$ has a value in $\frac{1}{n!}\mathbb{Z}$ by Volume 3, Corollary 2.1.3, and $\sqrt 2$ is irrational. So $x_1, x_2, x_3$ are algebraically independent. The support of $s$ has finitely many points below each bound, so $s \in C$ and $K_3 \subseteq C$. By Lemma 3.23.18, $\vartheta_0 \notin C$. If $\vartheta_0$ were algebraic over $C$, then $C(\vartheta_0) \subseteq H$ would be a proper immediate algebraic extension of $C$, since $\nu H = \Gamma$ and $H\nu = k$. This contradicts Lemma 3.23.10, part 2. So $x_1, \dots, x_4$ are algebraically independent, and $\nu K = \Gamma$, $K\nu = k$.

Since $x_3 \in C$, Corollary 3.23.16, case 1, gives local uniformization of each $F \subseteq K^h$. Since $x_4 \in F$ and $x_4 \notin C$, Lemma 3.23.10, part 3, shows that $\nu$ is not of KK type on $F$. $\square$

This answers Problem V7 for the classes of Corollary 3.23.16. They are not covered by Theorem 3.23.2, but the method is the method of [KK09] as a whole. What is new is the identification of the classes and the explicit member. Without Lemma 3.23.9 the last step of the proof would only show that $F \not\subseteq C_x$ for the one pair $x = (t, t^{\sqrt 2})$.

### Defect extensions with value group $\mathbb{Z}^2$

Note 57 gave defect extensions only with value groups that are not finitely generated. The next proposition gives them with value group exactly $\mathbb{Z}^2$. Following Kuhlmann [Kuh10b], an Artin-Schreier defect extension $E(\vartheta)/E$, with $\vartheta^p - \vartheta \in E$, of a valued field of rank 1 is *independent* if $\operatorname{dist}(\vartheta, E^h) = 0$ and *dependent* if $\operatorname{dist}(\vartheta, E^h) < 0$. In rank 1, $E$ is dense in $E^h$, so we may use $E$ in place of $E^h$.

**Proposition 3.23.20.** Let $(E, \nu)$ be a valued field of rank 1 and characteristic $p$, and let $\vartheta$ be an element of an immediate extension, transcendental over $E$, with a cofinal pseudo Cauchy sequence in $E$ of transcendental type. Let $\delta = \operatorname{dist}(\vartheta, E) < \infty$. Let $\varphi(X) = X^p$, or $\varphi(X) = X^p - X$ and $\delta \le 0$, and let $a = \varphi(\vartheta)$. Then $\nu(\vartheta - c) < \delta$ for each $c \in E(a)$, and $\operatorname{dist}(\vartheta, E(a)) = \delta$. So $E(\vartheta)/E(a)$ is immediate of degree $p$ with defect $p$. It is purely inseparable if $\varphi = X^p$, a dependent Artin-Schreier extension if $\varphi = X^p - X$ and $\delta < 0$, and an independent Artin-Schreier extension if $\varphi = X^p - X$ and $\delta = 0$.

Node: SG000000B7 · Lean: none yet

*Proof.* Let $c = g_1(a)/g_2(a)$ with $g_1, g_2 \in E[X]$ and $g_2(a) \ne 0$, and put $\rho = \nu(g_2(a))$ and
$$H(X) = g_2(\varphi(X))X - g_1(\varphi(X)) \in E[X], \qquad H(\vartheta) = g_2(a)(\vartheta - c).$$
The degree of the first term is $1$ modulo $p$ and that of the second is $0$ modulo $p$, so $H \ne 0$, and $H(\vartheta) \ne 0$ since $\vartheta$ is transcendental. Put $\Lambda = \nu(\vartheta - c) = \nu(H(\vartheta)) - \rho$.

Let $P(T) = H(\vartheta + T) = \sum_j H^{[j]}(\vartheta)T^j \in E(\vartheta)[T]$, and let $h_j = \nu(H^{[j]}(\vartheta))$. Since $\varphi$ is additive, $\varphi(\vartheta + T) = a + \varphi(T)$. Expanding $g(a + U) = \sum_i g^{[i]}(a)U^i$ we get
$$P(T) = \sum_{i \ge 0}(A_i + B_iT)\varphi(T)^i, \qquad A_i = g_2^{[i]}(a)\vartheta - g_1^{[i]}(a), \qquad B_i = g_2^{[i]}(a).$$
Note $B_0 = g_2(a)$, so $\nu(B_0) = \rho$. For $\gamma \in \mathbb{R}$ let $w_\gamma$ be the Gauss valuation $w_\gamma(\sum_j c_jT^j) = \min_j(\nu(c_j) + j\gamma)$ (Volume 3, Lemma 3.3.2).

Claim: $w_\gamma(P) \le \rho + \gamma$ for each $\gamma$ if $\varphi = X^p$, and for each $\gamma < 0$ if $\varphi = X^p - X$. Put $m_i = \min(\nu(A_i) + ip\gamma, \nu(B_i) + (ip + 1)\gamma)$, the value of $A_iT^{ip} + B_iT^{ip+1}$. If $\varphi = X^p$, then $(A_i + B_iT)\varphi(T)^i$ is exactly $A_iT^{ip} + B_iT^{ip+1}$. If $\varphi = X^p - X$ and $\gamma < 0$, then $(T^p - T)^i = T^{ip}(1 - T^{1-p})^i$, so $(A_i + B_iT)\varphi(T)^i$ is $A_iT^{ip} + B_iT^{ip+1}$ plus the terms $\binom{i}{l}(-1)^l(A_i + B_iT)T^{ip - (p-1)l}$, $l \ge 1$, whose values $m_i - (p - 1)l\gamma$ are larger than $m_i$. Let $m = \min_i m_i$, attained by the term in degree $e \in \{i_0p, i_0p + 1\}$. The degrees $ip$ and $ip + 1$ are distinct for distinct $i$, because $p \ge 2$. So the coefficient of $T^e$ in $P$ is this term plus terms of value larger than $m$, and every monomial of $P$ has value at least $m$. So $w_\gamma(P) = m \le m_0 \le \nu(B_0) + \gamma = \rho + \gamma$.

Now let $(d_n)$ be the cofinal pseudo Cauchy sequence of transcendental type, with $\gamma_n = \nu(\vartheta - d_n)$ strictly increasing to $\delta$. By Lemma 3.23.13, part 2, applied to $H$, the minimum $m_n = \min_{j \ge 1}(h_j + j\gamma_n)$ satisfies $m_n > h_0 = \rho + \Lambda$ for large $n$. Suppose that $\Lambda \ge \delta$. Then $\gamma_n < \delta$, and in the Artin-Schreier case $\gamma_n < \delta \le 0$, so the claim applies with $\gamma = \gamma_n$:
$$\min(h_0, m_n) = w_{\gamma_n}(P) \le \rho + \gamma_n < \rho + \delta \le \rho + \Lambda = h_0.$$
So $m_n \le \rho + \gamma_n < h_0$ for each $n$, a contradiction for large $n$. Hence $\Lambda < \delta$.

So $\nu(\vartheta - E(a)) \subseteq (-\infty, \delta)$, and it contains $\nu(\vartheta - E)$, whose supremum is $\delta$. In particular $\vartheta \notin E(a)^c \supseteq E(a)^h$. The roots of $\varphi(X) - a$ are $\vartheta + i$ with $i \in \mathbb{F}_p$, or $\vartheta$ alone if $\varphi = X^p$, and none lies in $E(a)^h$. An Artin-Schreier polynomial without a root is irreducible, and so is $X^p - a$ if $a$ is not a $p$-th power (Exercise 7). So $[E(a)^h(\vartheta) : E(a)^h] = p$. The extension is immediate, because $E(\vartheta)/E$ lies in an immediate extension. So $e = f = 1$ and the defect is $p$. The type follows from the definition, since $\operatorname{dist}(\vartheta, E(a)) = \delta$. $\square$

The condition $\delta \le 0$ is needed in the Artin-Schreier case. For $\gamma \ge 0$ the degrees of the leading terms of different $i$ overlap. If $\delta = 1$, then $\vartheta$ lies in $E(a)^h$ by the lemma of Hensel (Exercise 10), and the distance is $\infty$.

**Example 3.23.21.** Let $E = k(x_1, x_2, w)$ with $x_1 \mapsto t$, $x_2 \mapsto t^{\sqrt 2}$ and $w \mapsto s = \sum_n t^{n!}$. Let $\delta \in \Gamma$, $\vartheta = \vartheta_\delta$, $F = E(\vartheta)$ and $K = E(\varphi(\vartheta))$. Then $\nu F = \nu K = \Gamma$, $F\nu = K\nu = k$, and $F/K$ has defect $p$. It is purely inseparable for $\varphi = X^p$, dependent Artin-Schreier for $\varphi = X^p - X$ and $\delta \in \{-1, 1 - \sqrt 2\}$, and independent Artin-Schreier for $\varphi = X^p - X$ and $\delta = 0$. In each case $F = k(x_1, x_2, w, \vartheta)$ has local uniformization.

Node: SG000000B8 · Lean: none yet

*Proof.* As in Example 3.23.19, $x_1, x_2, w$ are algebraically independent and $E \subseteq C$, so $E^c = C$, which is algebraically maximal. By Lemma 3.23.18, $\vartheta \notin C$, and $\vartheta$ is transcendental over $C$. Since $K_2 \subseteq E \subseteq C$, $\operatorname{dist}(\vartheta, E) = \delta$. By Lemma 3.23.13, part 3, a cofinal pseudo Cauchy sequence of $\vartheta$ in $E$ is of transcendental type. The three values of $\delta$ are $\le 0$, so Proposition 3.23.20 applies. Finally, $(x_1, x_2, w, \vartheta)$ is a projection of $F$ with $w \in C$, so Corollary 3.23.16, case 1, gives local uniformization of $F$. $\square$

So a defect in one projection is no obstruction to local uniformization, as in Remark 2.3 of note 57. None of these examples triggers the no-go condition of issue tamnd/singularity#298, because each lives on a field with another projection that has the ball property at each step.

### Family T

The next family has an independent Artin-Schreier defect in its natural projection, and the obvious other projection leads to an open question.

**Lemma 3.23.22 (swap).** Let $K = k(x_1, x_2, x_3, x_4)$ with $x_3 = \varphi(\vartheta)$ and $x_4 = \vartheta + \varepsilon$, where $\varphi = X^p - X$, and $\vartheta, \varepsilon$ lie in $H$ with $\nu(\varepsilon) > 0$. Put $y_3 = x_3 - \varphi(x_4)$. Then $y_3 = \varepsilon - \varepsilon^p$, $K = k(x_1, x_2, y_3, x_4)$, the element $\varepsilon$ lies in $K_2(y_3)^h$, and $\vartheta \in K^h$.

Node: SG000000B9 · Lean: none yet

*Proof.* Since $\varphi$ is additive, $y_3 = \varphi(\vartheta) - \varphi(\vartheta + \varepsilon) = -\varphi(\varepsilon) = \varepsilon - \varepsilon^p$, and $x_3 = y_3 + \varphi(x_4)$, so the two sets of generators give the same field. The polynomial $G(X) = X^p - X + y_3$ has $G(\varepsilon) = 0$, $\nu(G(0)) = \nu(y_3) = \nu(\varepsilon) > 0$ and $G'(X) = -1$. By the lemma of Hensel, $G$ has exactly one root of positive value in the henselian field $K_2(y_3)^h \subseteq H$. The roots of $G$ in $H$ are $\varepsilon + i$ with $i \in \mathbb{F}_p$, and only $\varepsilon$ has positive value. So $\varepsilon \in K_2(y_3)^h$, and $\vartheta = x_4 - \varepsilon \in K^h$. $\square$

Note 76 wrote the polynomial as $X - X^p + y_3$. Its value at $\varepsilon$ is $2y_3$, which is not 0 for $p \ne 2$.

**Example 3.23.23 (family T).** Let $\vartheta = \vartheta_0$, let $\zeta = \sum_m c_mt^{1 + \gamma_m(0)}$ with $c_m \in k$ chosen so that $\zeta$ is transcendental over $k(t, t^{\sqrt 2}, \vartheta)$, and let $\varepsilon = \zeta^p$. Let $\nu$ be the valuation of $K = k(x_1, x_2, x_3, x_4)$ given by
$$x_1 \mapsto t, \qquad x_2 \mapsto t^{\sqrt 2}, \qquad x_3 \mapsto \vartheta^p - \vartheta, \qquad x_4 \mapsto \vartheta + \varepsilon.$$

1. $K_3(\vartheta)/K_3$ is an independent Artin-Schreier defect extension, with $\operatorname{dist}(\vartheta, K_3) = 0$.
2. A cofinal pseudo Cauchy sequence of $x_4$ in $K_3$ is of algebraic type, so $x_4$ does not have the ball property over $K_3$.
3. With $y_3 = \varepsilon - \varepsilon^p = \zeta^p - \zeta^{p^2}$ we have $K = k(x_1, x_2, y_3, x_4)$, $y_3 \notin C$, $y_3$ has the ball property over $K_2$, and $\varepsilon \in K_2(y_3)^h$.
4. $[K(\zeta) : K] = p^2$. The extension $K(\vartheta)/K$ is separable of degree $p$ and lies in $K^h$, and $K^h(\zeta)/K^h$ is purely inseparable of degree $p$ and immediate. So the defect of $K(\zeta)/K$ is $p$, and $\operatorname{dist}(\zeta, K) \ge 1$. The field $K(\zeta) = k(x_1, x_2, \zeta, \vartheta)$ is rational.

Node: SG000000B9 · Lean: none yet

*Proof.* Existence. The field $k(t, t^{\sqrt 2}, \vartheta)$ is countable, so its algebraic closure in $H$ is countable. Distinct sequences $(c_m)$ give distinct $\zeta$, and there are uncountably many sequences, so some $\zeta$ is transcendental over $k(t, t^{\sqrt 2}, \vartheta)$. The choice must be generic: for $c_m = 1$ for each $m$ we get $\zeta = t\vartheta$. The elements $t, t^{\sqrt 2}, \vartheta$ are algebraically independent (Example 3.23.19), so $t, t^{\sqrt 2}, \vartheta, \zeta$ are. The field $K(\vartheta, \zeta)$ is algebraic over $K$, because $\vartheta$ is a root of $X^p - X - x_3$ and $\zeta^p = x_4 - \vartheta$, and it contains $t, t^{\sqrt 2}, \vartheta, \zeta$. So $\operatorname{trdeg} K = 4$. The support of $\zeta$ lies in $(0, 1)$, so $\nu(\varepsilon) = p\nu(\zeta) > 0$.

1. Apply Proposition 3.23.20 with $E = K_2$ and $a = x_3$. Here $E^c = C$ is algebraically maximal, $\vartheta \notin C$, a cofinal pseudo Cauchy sequence of $\vartheta$ in $K_2$ is of transcendental type by Lemma 3.23.13, part 3, and $\delta = 0$ by Lemma 3.23.18.

2. For $c \in K_3$, $\nu(\vartheta - c) < 0 < \nu(\varepsilon)$ by part 1, so $\nu(x_4 - c) = \nu(\vartheta - c)$. The truncations $d_n = \sum_{m \le n}t^{\gamma_m(0)} \in K_2$ have $\nu(x_4 - d_n) = \gamma_{n+1}(0)$, which increases to 0, so $(d_n)$ is a cofinal pseudo Cauchy sequence of $x_4$ in $K_3$. For $h = X^p - X - x_3$ we have $h(d_n) = \varphi(d_n - \vartheta)$, of value $p\gamma_{n+1}(0)$, because $\nu(d_n - \vartheta) < 0$. These values are not eventually constant, so the type is algebraic. Each ball around $x_4$ contains $d_n$ for large $n$, so the ball property fails for $h$.

3. The first claims are Lemma 3.23.22. The support of $\zeta^p$ is $\{p(1 + \gamma_m(0)) : c_m \ne 0\}$, and infinitely many $c_m$ are not 0, since otherwise $\zeta \in K_2$. These points accumulate at $p$. The support of $\zeta^{p^2}$ lies above $p^2(1 - \frac{1}{3 + 2\sqrt 2}) > p$. So the support of $y_3$ has the least accumulation point $p$, and $y_3 \notin C$ by Lemma 3.23.18. Since $x_1, x_2, y_3, x_4$ is a transcendence basis, $y_3$ is transcendental over $K_2$, and Lemma 3.23.13, part 3, gives the ball property.

4. Since $\vartheta = x_4 - \zeta^p$, we have $K(\zeta) = K(\vartheta)(\zeta) = k(t, t^{\sqrt 2}, \vartheta, \zeta)$, which is rational. The elements $\vartheta, \varepsilon$ are algebraically independent over $K_2$, so there is an automorphism $\sigma$ of $K_2(\vartheta, \varepsilon)$ over $K_2$ with $\sigma(\vartheta) = \vartheta + 1$ and $\sigma(\varepsilon) = \varepsilon - 1$. It fixes $x_3 = \varphi(\vartheta)$ and $x_4 = \vartheta + \varepsilon$, so it fixes $K$, and $\vartheta \notin K$. So $X^p - X - x_3$ has no root in $K$ and is irreducible, and $[K(\vartheta) : K] = p$, separable. Also $K(\vartheta) = K_2(\vartheta, \varepsilon) = K_2(\vartheta, \zeta^p)$, and $[K(\zeta) : K(\vartheta)] = [K_2(\vartheta, \zeta) : K_2(\vartheta, \zeta^p)] = p$, because $\zeta$ is transcendental over $K_2(\vartheta)$. So $[K(\zeta) : K] = p^2$. By Lemma 3.23.22, $K(\vartheta) \subseteq K^h$, and $\zeta^p = \varepsilon \in K^h$. If $\zeta \in K^h$, then $\zeta$ would be separable over $K(\vartheta)$ and purely inseparable over it, so $\zeta \in K(\vartheta)$, which is false. So $K^h(\zeta)/K^h$ is purely inseparable of degree $p$. It lies in $H$, so it is immediate, and $K(\zeta)^h = K^h(\zeta)$ gives defect $p$. Finally $\operatorname{dist}(\zeta, K) \ge \operatorname{dist}(\zeta, K_2) = 1$ by Lemma 3.23.18, because the support of $\zeta$ accumulates at 1. $\square$

Note 76 said that $K(\zeta)/K$ is purely inseparable of degree $p$. The correct statement is part 4: the degree is $p^2$, with the separable part inside $K^h$, and the defect is $p$.

So $K$ has local uniformization if $x_4$ has the ball property over $K_2(y_3)$, because then Theorem 3.23.15 applies to the projection $(x_1, x_2, y_3, x_4)$. The following proposition reduces this question. Let $\psi = \sum_m c_mt^{\gamma_m(0)}$, so that $\zeta = t\psi$ and $\varepsilon = t^p\psi^p$. Put $L = K_2(y_3)$ and $M = K_2(\varepsilon) = K_2(\psi^p)$.

**Proposition 3.23.24.**

1. $L^h = M^h$.
2. If $\vartheta$ has the ball property over $M^h$, then $x_4$ has the ball property over $L$, and $K$ has local uniformization.
3. $M^h = \bigoplus_r t^r(K_2(\psi)^h)^p$, where $r$ runs over $\{i + j\sqrt 2 : 0 \le i, j < p\}$, and the sum is orthogonal for $\nu$. So for each $b \in M^h$ there is $B_0 \in K_2(\psi)^h$ with $\nu(\vartheta^p - b) \le p\,\nu(\vartheta - B_0)$. If $\nu(\vartheta - B) < 0$ for each $B \in K_2(\psi)^h$, then for each $b \in M^h$ the values $\nu(d_n^p - b)$ on the pseudo Cauchy sequence of $\vartheta$ are eventually constant.

Node: SG000000BA · Lean: none yet

*Proof.* 1. By Lemma 3.23.22, $\varepsilon \in L^h$, so $M \subseteq L^h$. Also $y_3 = \varepsilon - \varepsilon^p \in M$, so $L \subseteq M$. Hence $L^h = M^h$.

2. Let $g \in L[X]$ and put $\tilde g(X) = g(X + \varepsilon) \in M^h[X]$. The ball property of $\vartheta$ over $M^h$ gives $\alpha$ and $A_0 \in M^h$ with $\nu(\tilde g(A)) = \alpha$ for each $A \in M^h$ with $\nu(\vartheta - A) \ge \nu(\vartheta - A_0)$. Since $L$ is dense in $L^h = M^h$, there is $a_0 \in L$ with $\nu(a_0 - A_0 - \varepsilon) > \nu(x_4 - A_0 - \varepsilon)$, and then $\nu(x_4 - a_0) = \nu(\vartheta - A_0)$. For $a \in L$ with $\nu(x_4 - a) \ge \nu(x_4 - a_0)$, put $A = a - \varepsilon \in M^h$. Then $\nu(\vartheta - A) = \nu(x_4 - a) \ge \nu(\vartheta - A_0)$, so $\nu(g(a)) = \nu(\tilde g(A)) = \alpha$. This is the ball property of $x_4$ over $L$. With part 3 of Example 3.23.23, Theorem 3.23.15 applies to $(x_1, x_2, y_3, x_4)$.

3. Let $M_0 = K_2(\psi)^p = k(t^p, t^{p\sqrt 2}, \psi^p)$. Then $M = M_0(t, t^{\sqrt 2})$. The value group of $K_2(\psi)$ is $\Gamma$, so that of $M_0$ is $p\Gamma$. The elements $t^r$ have values in the $p^2$ distinct cosets of $p\Gamma$ in $\Gamma$, so a sum $\sum_r a_rt^r$ with $a_r \in M_0$ has the value $\min_r \nu(a_rt^r)$. So the $t^r$ are linearly independent over $M_0$, and since $t^p, (t^{\sqrt 2})^p \in M_0$, they form a basis: $M = \bigoplus_r t^rM_0$, orthogonally. The Frobenius map is an isomorphism of $K_2(\psi)$ onto $M_0$ that multiplies the values by $p$, so $M_0^h = (K_2(\psi)^h)^p$. Since $M/M_0$ is finite, $M^h = M \cdot M_0^h = \sum_r t^rM_0^h$, and $M_0^h$ has value group $p\Gamma$, so the same argument shows that the sum is direct and orthogonal.

Each element of $H$ is uniquely a sum of components with supports in the cosets $r + p\Gamma$, and its value is the least value of its components. For $b = \sum_r t^rB_r^p$ with $B_r \in K_2(\psi)^h$, the component of $\vartheta^p - b$ in $p\Gamma$ is $\vartheta^p - B_0^p$, since $\vartheta^p$ and $B_0^p$ have supports in $p\Gamma$. So $\nu(\vartheta^p - b) \le \nu(\vartheta^p - B_0^p) = p\,\nu(\vartheta - B_0)$. Finally, $d_n^p - b = (d_n - \vartheta)^p + (\vartheta^p - b)$, and $\nu(d_n - \vartheta)^p = p\gamma_n$ increases to 0. If $\nu(\vartheta^p - b) < 0$, then for large $n$ the value of $d_n^p - b$ is $\nu(\vartheta^p - b)$. $\square$

So for a key polynomial of the purely inseparable shape $X^p - b$, the question goes one level down: can $\vartheta$ be approximated to value 0 by elements of $K_2(\psi)^h$, where $\psi$ has the same support as $\vartheta$ and generic coefficients? The Artin-Schreier shape $X^p - X - b$ reduces in the same way to the approximation of the coset components of $\vartheta$. Key polynomials of other shapes, and of degree $p^e$ with $e \ge 2$, are not treated.

**Conjecture 3.23.25 (Question T1).** In Example 3.23.23 with a generic sequence $(c_m)$, $x_4$ has the ball property over $K_2(y_3)$. So $K$ has local uniformization.

Node: SG000000BB · Lean: none yet

By Proposition 3.23.24 it is enough that $\vartheta$ has the ball property over $K_2(\psi^p)^h$. What separates $L$ from $\vartheta$ is the pattern of coefficients, $(c_m^p)$ against the constant pattern $(1)$ of $\vartheta^p$, along the support $\{p\gamma_m(0)\}$; the location of the accumulation points does not, because $t^{-p}y_3 \in L$ has support accumulating at 0 exactly at the points $p\gamma_m(0)$ of $\vartheta^p$. For the excluded choice $c_m = 1$ we would have $\psi = \vartheta$ and $\vartheta^p \in M$. We do not know a proof for generic $(c_m)$. Elements of $K_2(\psi)$ that are polynomials in $\psi$ have tails proportional to $(c_m)$ plus sparse corrections, but for rational functions and for the henselization we have no control.

### What is open

1. Conjecture 3.23.8: local uniformization of the discrete valuation $v_1$ of rank 1 when $d \in \{1, 2\}$ and $\kappa$ is not finitely generated. With Theorem 3.23.5 this is the only open part of Problem V7 in rank 2.
2. Conjecture 3.23.17: the existence of a projection with the ball property at each step. It implies Problem V7 in rank 1.
3. Conjecture 3.23.25 (Question T1) for generic $(c_m)$. By Proposition 3.23.24 the inseparable shape of key polynomial reduces to the statement $\nu(\vartheta - B) < 0$ for each $B \in K_2(\psi)^h$.
4. Local monomialization in rank 2 for $d = 3$. It needs weak embedded local uniformization of valuations of threefolds in characteristic $p$.
5. The polynomial form ELU(4) of note 57 for towers with the ball property.

### Exercises

1. Let $\Gamma$ be an ordered group isomorphic to $\mathbb{Z}^2$ with a convex subgroup $\Delta \ne 0, \Gamma$. Show that $\Delta \cong \mathbb{Z}$, that $\Gamma/\Delta$ is torsion free, and that $\Gamma$ is isomorphic to $\mathbb{Z}^2$ with the lexicographic order.
2. In Example 3.23.19, show directly that $\nu(s - s_n) = (n + 1)!$ and that a nonzero polynomial in $t$ of degree $N$ has $t$-adic value at most $N$. Deduce the Liouville argument for $s$.
3. Let $\nu = v_1 \circ \bar v$ have value group $\mathbb{Z}^2$ with the lexicographic order. Show that the sets $\{x : \nu(x) > (m, n)\}$ and $\{x : v_1(x) \ge m\}$ define the same topology on $F$.
4. Let $z$ be an element of an immediate extension of $L$ with $z \notin L$. Show that $\nu(z - L)$ has no largest element. (If $\nu(z - c) = \beta$, choose $c' \in L$ with $\nu(c') = \beta$ and use the residue of $(z - c)/c'$.)
5. Prove that the solutions of $r^2 - 2q^2 = 1$ satisfy $q_m\sqrt 2 - r_m = -1/(r_m + q_m\sqrt 2)$, check the cases $3/2$, $17/12$ and $99/70$, and show that $\gamma_m(\delta)$ increases strictly to $\delta$.
6. Let $\nu(\delta) > 0$ and $a \in \mathbb{Z}$. Show that $\nu((1 + \delta)^a - 1) \ge \nu(\delta)$. Treat $a \ge 0$ with the binomial formula and $a < 0$ with $(1 + \delta)^{-1} - 1 = -\delta/(1 + \delta)$.
7. Let $E$ be a field of characteristic $p$ and $a \in E$. Show that $X^p - X - a$ is irreducible over $E$ if it has no root in $E$, and that $X^p - a$ is irreducible over $E$ if $a$ is not a $p$-th power in $E$.
8. Show that $X^\ell - (1 + z)$ is irreducible over $k(z)$ for each prime $\ell \ne p$, and that the field $\kappa$ of Counterexample 3.23.7 is not finitely generated over $k$.
9. Show that $k[[z]]$ contains an element that is transcendental over a given countable subfield of $k((z))$.
10. In Proposition 3.23.20, take $\varphi = X^p - X$ and $\delta = 1$, for example $\vartheta = \vartheta_1$ over $E = K_2$. Show that $\vartheta - d$ is a root of positive value of $X^p - X - (a - \varphi(d))$ for a suitable truncation $d$, and conclude with the lemma of Hensel that $\vartheta \in E(a)^h$. Which step of the proof of the proposition fails?
11. In Example 3.23.23, show that the two sums of the identity $y_3 = x_3 - \varphi(x_4) = -\varphi(\varepsilon)$ agree, and that $K(\zeta) = k(x_1, x_2, \zeta, \vartheta)$.
12. Show that the sum of the Abhyankar inequalities for $v_1$ on $F$ and for $\bar v$ on $\kappa$ is the Abhyankar inequality for $\nu = v_1 \circ \bar v$, and that equality for $\nu$ gives equality for both.

### Status

The results are the nodes SG000000AS to SG000000BD of the map. They come from research note 76, with the corrections of the referee report in note 80. Theorems 3.23.3 and 3.23.4 and Corollary 3.23.16 use the theorem of Knaf and Kuhlmann [KK09], Theorem 3.23.5 uses the proof of Novacoski and Spivakovsky [NS14] with the theorems of Abhyankar and of Cossart and Piltant, and Counterexample 3.23.7 uses the theorem of Kuhlmann [Kuh10c]. Lemma 3.23.13 and Proposition 3.23.24 use the theorem of Kaplansky [Kap42], and Lemma 3.23.10 uses the generalized stability theorem [Kuh10]. Conjectures 3.23.8, 3.23.17 and 3.23.25 are open. None of the nodes has a Lean proof yet. An outside expert has not yet read the result.

### Notes and references

The results are in research note 76, with the corrections of note 80, which is a referee report on note 76. Note 80 found that Theorem 3.23.3 needs $\kappa$ finitely generated and gave Counterexample 3.23.7. It replaced the rank reduction hypothesis of note 76 by the pointwise form of [NS14] (Theorem 3.23.5), repaired the proof of Lemma 3.23.10, part 3, with Lemma 3.23.9, made the ball property the hypothesis of Theorem 3.23.15, corrected the polynomial of Lemma 3.23.22 and part 4 of Example 3.23.23, and proved Proposition 3.23.24. Note 80 also showed that the computer check of note 76 for Example 3.23.21 carries no information, because its search cannot see values at least $\delta$; we do not use it, and Proposition 3.23.20 does not need it. The heuristic of note 76 for Conjecture 3.23.25, which used the accumulation points of the supports, is wrong, and we do not use it. The theorem of Knaf and Kuhlmann on completions and the necessity of zero defect are [KK09, Theorems 1.5 and 1.6]. Pseudo Cauchy sequences are in [Kap42], and the classification of Artin-Schreier defect extensions is in [Kuh10b], Illinois J. Math. 54 (2010), 397-448, arXiv 1003.5639. The arXiv number 1004.2135 is a different paper, the survey of Kuhlmann "The defect", in Commutative Algebra, Springer, 2011, 277-318. The proofs of Lemma 3.23.14, Theorem 3.23.15 and Proposition 3.23.20 here are simpler than those of note 76: Lemma 3.23.14 makes the constant term dominant, so no final change of the monomials is needed, and Proposition 3.23.20 uses Gauss valuations and no graded ring.
