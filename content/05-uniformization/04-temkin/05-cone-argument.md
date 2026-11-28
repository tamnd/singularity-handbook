---
title: "The step of degree $p$ over an Abhyankar base: the cone argument"
nodes: []
sources: [Kap42, KK05, KK09, Kuh10, Kuh-book, Tem13]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The step of degree $p$ over an Abhyankar base: the cone argument

Sections 4.1 to 4.3 reduce local uniformization to one purely inseparable step of degree $p$ (Definition 4.3.1 and Theorem 4.3.2). In one step a field $E$ has a regular center of the valuation, $E' = E(\theta)$ with $\theta^p = f \in E$, and we must find a regular center upstairs. Section 4.3 does the step when $f$ is monomial modulo $p$-th powers, and Section 4.4 does it when the log Jacobian ideal of $f$ is principal on a regular model. At the end of Section 4.3 we saw that along a valuation with a defect the values of $f - h^p$ have no maximum. This is the hard case. In this section we study it in the smallest case where it can occur: the field $E$ is an immediate extension of transcendence degree one of an Abhyankar base of rank one, and the equation has the special form $z^p = g(x^p) + Gx + b$ with coefficients in the base. We prove that the field is henselian rational over the base and that the valuation has local uniformization (Theorem 4.5.16). The main tool is a statement on lattice points in a cone (Lemma 4.5.13).

We recall the notion of henselian rationality. Let $(F/K, \nu)$ be an extension of valued fields, and let $F/K$ be a function field. Kuhlmann calls $(F/K, \nu)$ *henselian rational* if there is a transcendence basis $T$ of $F/K$ such that $F$ lies in the henselization of the rational function field $K(T)$ (F.-V. Kuhlmann, Elimination of ramification II: henselian rationality, Israel J. Math. 234 (2019), arXiv 1701.05508). Kuhlmann proves that an immediate function field of transcendence degree one over a tame field is henselian rational (Theorem 1.2 of that paper), and he proves a form for separably tame fields (Theorem 1.3 of that paper). A tame field is perfect. The base fields of this section are not perfect, and their value groups are not divisible by $p$, so they are not tame and not separably tame, and the theorems of Kuhlmann do not apply.

Henselian rationality gives local uniformization in this way. Let $F \subseteq K(T)^h$, let $F/K(T)$ be finite, and assume that $K(T)$ has local uniformization. The extension $F/K(T)$ is immediate and lies in the henselization, so it has defect 1. By Volume 5, Lemma 1.3.3 it has an étale generator, and Volume 5, Theorem 1.3.4 lifts local uniformization from $K(T)$ to $F$. This is Volume 9, Theorem 3.23.11, and in the language of Knaf and Kuhlmann it is [KK09, Lemma 3.7 and Corollary 3.6]. Conversely, if $(F, \nu)$ has local uniformization and its residue field is the ground field $k$, then $F$ lies in $k(T)^h$ for a transcendence basis $T$ of $F/k$ [KK09, Theorem 1.6]. So henselian rationality is the right form of the step for a valuation with residue field $k$. Knaf and Kuhlmann proved local uniformization for Abhyankar valuations [KK05] (Volume 5, Theorem 2.2.1). The fields of this section are immediate extensions of such a base.

This section proves one case of one step. It does not prove local uniformization in transcendence degree 4 or more. The last part of the section says what it does not prove.

### The setting

In this section $p$ is a prime number and $k$ is an algebraically closed field of characteristic $p$. The proofs below use this hypothesis only through two facts: $k$ is perfect, and the valuation is trivial on $k$. We do not state the results for other fields $k$.

Let $m \ge 1$ and let $K_0 = k(u_1, \dots, u_m)$ be a field of rational functions. Let $\nu$ be a valuation of $K_0$ that is trivial on $k$, with values in $\mathbb{R}$, such that the numbers $\nu(u_1), \dots, \nu(u_m)$ are linearly independent over $\mathbb{Q}$. For $n \in \mathbb{Q}^m$ let $s(n) = \sum_i n_i \nu(u_i)$. The map $s : \mathbb{Q}^m \to \mathbb{R}$ is $\mathbb{Q}$-linear and injective. For $n \in \mathbb{Z}^m$ we write $u^n = u_1^{n_1} \cdots u_m^{n_m}$, so $\nu(u^n) = s(n)$. Distinct Laurent monomials have distinct values, so for a Laurent polynomial $P = \sum_n a_n u^n$ with $a_n \in k$ we have $\nu(P) = \min\{s(n) : a_n \ne 0\}$. Thus $\nu$ is the monomial valuation of Volume 5, Definition 2.1.1. Its value group is $\Gamma = s(\mathbb{Z}^m) = \bigoplus_i \mathbb{Z}\nu(u_i)$, its residue field is $k$, and it is an Abhyankar valuation of $K_0/k$. Let $K = K_0^h$ be a henselization. The extension $K/K_0$ is immediate, so $K$ has the value group $\Gamma$ and the residue field $k$.

A *monomial term* is $au^n$ with $a \in k^\times$ and $n \in \mathbb{Z}^m$. The *class* of $u^n$, and of the term $au^n$, is the class of $n$ in $\mathbb{Z}^m/p\mathbb{Z}^m$. We identify this group with the set $\{0, \dots, p-1\}^m$.

A formal sum $a = \sum_{n \in \mathbb{Z}^m} a_n u^n$ with $a_n \in k$ is an *admissible series* if for each $\lambda \in \mathbb{R}$ the set $\{n : a_n \ne 0, s(n) \le \lambda\}$ is finite. Its *support* is the set of the $n$ with $a_n \ne 0$, and its *terms* are the monomial terms $a_nu^n$ with $a_n \ne 0$. Let $S$ be the set of the admissible series. For $a \ne 0$ in $S$ let $\nu_S(a)$ be the least value $s(n)$ on the support, and let $\nu_S(0) = \infty$.

**Lemma 4.5.1 (admissible series).** The sums and the products of formal series make $S$ a field, and $\nu_S$ is a valuation of $S$ with value group $\Gamma$ and residue field $k$. The field $(S, \nu_S)$ is complete. There is one embedding of $K$ in $S$ that is the identity on $k$ and on $u_1, \dots, u_m$ and that maps $\nu$ to $\nu_S$. For $a = \sum_n a_nu^n$ in $S$ we have $a^p = \sum_n a_n^p u^{pn}$.

This statement is not in Lean.

*Proof.* Products. Let $a, b \in S$ be nonzero, and let $\sigma_a = \nu_S(a)$ and $\sigma_b = \nu_S(b)$. Let $v \in \mathbb{Z}^m$. A pair $(n, n')$ in the supports with $n + n' = v$ has $s(n) \ge \sigma_a$ and $s(n') \ge \sigma_b$, so $s(n) \le s(v) - \sigma_b$. There are only finitely many such $n$, and $n' = v - n$. So the coefficient $\sum_{n + n' = v} a_nb_{n'}$ is a finite sum. If $s(v) \le \lambda$, then $s(n) \le \lambda - \sigma_b$ and $s(n') \le \lambda - \sigma_a$, so only finitely many pairs occur, and $ab \in S$. The ring laws hold as for polynomials. Let $n_a$ and $n_b$ be the points of least value of the supports. A pair $(n, n')$ in the supports with $n + n' = n_a + n_b$ has $s(n) \ge s(n_a)$ and $s(n') \ge s(n_b)$, so these are equalities, and $n = n_a$ because $s$ is injective. So the coefficient of $u^{n_a + n_b}$ in $ab$ is $a_{n_a}b_{n_b} \ne 0$, and the other points of the support of $ab$ have larger values. Thus $\nu_S(ab) = \nu_S(a) + \nu_S(b)$, and clearly $\nu_S(a + b) \ge \min(\nu_S(a), \nu_S(b))$.

Completeness. Let $(a^{(i)})$ be a Cauchy sequence in $S$. For each $\lambda$ there is $i_\lambda$ with $\nu_S(a^{(i)} - a^{(j)}) > \lambda$ for $i, j \ge i_\lambda$, so the coefficients of $u^n$ with $s(n) \le \lambda$ are the same in all $a^{(i)}$ with $i \ge i_\lambda$. Let $a_n$ be this coefficient. The support of $a = \sum_n a_nu^n$ below $\lambda$ is the support of $a^{(i_\lambda)}$ below $\lambda$, so $a \in S$, and $\nu_S(a - a^{(i)}) > \lambda$ for $i \ge i_\lambda$. So $a$ is the limit.

Inverses. Let $a \ne 0$, with least term $a_{n_a}u^{n_a}$. Then $a = a_{n_a}u^{n_a}(1 - \varepsilon)$ with $\nu_S(\varepsilon) > 0$. The partial sums of $\sum_j \varepsilon^j$ are a Cauchy sequence, because $\nu_S(\varepsilon^j) = j\nu_S(\varepsilon)$. Let $w$ be the limit. The multiplication is continuous, so $(1 - \varepsilon)w = 1$, and $a^{-1} = a_{n_a}^{-1}u^{-n_a}w$. So $S$ is a field. The value group is $s(\mathbb{Z}^m) = \Gamma$. An element of value $\ge 0$ has the residue $a_0$, the coefficient of $u^0$, and this map is onto $k$ with kernel the elements of positive value. So the residue field is $k$.

The embedding. The Laurent polynomials $k[u_1^{\pm 1}, \dots, u_m^{\pm 1}]$ are in $S$, and on them $\nu_S = \nu$ by the formula for $\nu(P)$ above. Since $S$ is a field, this inclusion extends in one way to $K_0$, and $\nu_S = \nu$ on $K_0$. A complete field of rank one is henselian [Kuh-book]. By the universal property of the henselization [Kuh-book], there is one embedding of $K = K_0^h$ in $S$ over $K_0$ that respects the valuations.

The $p$-th power. The map $a \mapsto a^p$ is additive in characteristic $p$, and $\nu_S(a^p) = p\nu_S(a)$, so it is continuous. For a finite sum the formula holds, and each $a \in S$ is the limit of its finite truncations. $\square$

From now on each element of $K$ is an admissible series. The *terms* of an element of $K$ are its terms as a series. Each truncation $\sum_{s(n) \le \lambda} a_nu^n$ of an element of $K$ is a Laurent polynomial, so it lies in $K_0$.

**Lemma 4.5.2 (a $p$-basis).** Let $E = \{0, \dots, p-1\}^m$.

1. Let $(F, \nu)$ be a valued field extension of $K_0$ with value group $\Gamma$, and let $\phi_e \in F$ for $e \in E$. Then $\nu(\sum_e u^e\phi_e^p) = \min_e \nu(u^e\phi_e^p)$. In particular the monomials $u^e$, $e \in E$, are linearly independent over $F^p$.
2. Each $\beta \in K$ is $\beta = \sum_{e \in E} u^e\beta_e^p$ with one family $\beta_e \in K$. The same is true for $K_0$, with $\beta_e \in K_0$ when $\beta \in K_0$.
3. In part 2, the terms of the series $u^e\beta_e^p$ are the terms of $\beta$ of the class $e$.

This statement is not in Lean.

*Proof.* 1. The value of $u^e\phi_e^p$ is $s(e) + p\nu(\phi_e)$, and it lies in $s(e) + p\Gamma$. Since $\Gamma = \bigoplus_i \mathbb{Z}\nu(u_i)$, the elements $s(e)$, $e \in E$, lie in distinct classes of $\Gamma/p\Gamma$. So the nonzero summands have distinct values, and the value of the sum is the least of them. If the sum is zero, each summand is zero.

2. Since $k$ is perfect, $K_0^p = k(u_1^p, \dots, u_m^p)$. Each $u_i^p$ lies in $K_0^p$, so $K_0 = K_0^p[u_1, \dots, u_m]$ is spanned by the $u^e$, $e \in E$, over $K_0^p$. The extension $K/K_0$ is algebraic and separable. The field $K$ is separable over its subfield $K^pK_0$, and it is purely inseparable over it, because $y^p \in K^p$ for each $y \in K$. So $K = K^pK_0$, and the $u^e$ span $K$ over $K^p$. Part 1 for $F = K$ and for $F = K_0$ gives the uniqueness.

3. By Lemma 4.5.1 the series $u^e\beta_e^p$ is $\sum_n b_n^pu^{e + pn}$, where $\beta_e = \sum_n b_nu^n$. All its terms have the class $e$. The sum over $e$ is $\beta$, and the classes are disjoint, so no terms cancel. $\square$

### The inputs from the literature

We use pseudo Cauchy sequences as in Volume 9, Section 3.23. A sequence $(d_i)$ in a valued field $L$ is *pseudo Cauchy* if $\nu(d_l - d_j) > \nu(d_j - d_i)$ for $i < j < l$. An element $y$ of an extension is a *limit* of it if $\nu(y - d_i)$ is strictly increasing. The sequence is of *transcendental type* if for each $h \in L[X]$ the value $\nu(h(d_i))$ is constant for large $i$, and of *algebraic type* otherwise (Volume 9, Definition 3.23.12). A valued field is *algebraically maximal* if it has no proper immediate algebraic extension. It is *defectless* if each finite extension of its henselization has defect 1 (Volume 9, Section 3.23).

**Theorem 4.5.3 (Kaplansky [Kap42, Theorems 2 and 3]).** Let $(L, \nu)$ be a valued field and let $(d_i)$ be a pseudo Cauchy sequence in $L$ with no limit in $L$.

1. If $(d_i)$ is of transcendental type, then there is an immediate transcendental extension $L(y)$ of $L$ in which $y$ is a limit of $(d_i)$.
2. If $(d_i)$ is of algebraic type, then there is a proper immediate algebraic extension of $L$.

This statement is not in Lean.

We cite the theorem without proof. We use only part 2.

**Theorem 4.5.4 (the generalized stability theorem [Kuh10, Theorem 1.1]).** Let $(F/K_1, \nu)$ be a valued function field without transcendence defect. If $(K_1, \nu)$ is defectless, then $(F, \nu)$ is defectless.

This statement is not in Lean.

This is Volume 5, Theorem 2.2.2. We cite it without proof.

**Lemma 4.5.5 (Kuhlmann [Kuh-book]).** A henselian defectless valued field has no proper immediate algebraic extension.

This statement is not in Lean.

We cite the lemma. The reason is short: a finite immediate extension $L'$ of a henselian field has $e = f = 1$, and defect 1 means $[L' : K_1] = ef$, so $L'$ is the base field $K_1$; an algebraic extension is the union of its finite subextensions.

**Corollary 4.5.6.** The field $K = K_0^h$ is henselian, defectless and algebraically maximal. Each pseudo Cauchy sequence in $K$ with no limit in $K$ is of transcendental type.

This statement is not in Lean.

*Proof.* The trivially valued field $k$ is defectless, because each finite extension has the trivial valuation and residue degree equal to its degree. The function field $K_0/k$ has no transcendence defect, because the rational rank of $\Gamma$ is $m = \operatorname{trdeg}_k K_0$. Theorem 4.5.4 shows that $K_0$ is defectless. By the definition, a field is defectless if and only if its henselization is defectless, so $K$ is defectless. It is henselian, so Lemma 4.5.5 shows that it is algebraically maximal. Let $(d_i)$ be a pseudo Cauchy sequence in $K$ with no limit in $K$. If it were of algebraic type, part 2 of Theorem 4.5.3 would give a proper immediate algebraic extension of $K$. $\square$

### Leading terms and truncations

From now on $F$ is an immediate extension of $K$, so $F$ has the value group $\Gamma$ and the residue field $k$. Let $x \in F$ be transcendental over $K$. For $h \in K[X]$ we write $h^{[j]}$ for the Hasse derivatives, so that $h(X + T) = \sum_{j \ge 0} h^{[j]}(X)T^j$. We use the rule $(h^{[i]})^{[j]} = \binom{i + j}{i}h^{[i + j]}$, which holds because both sides are the coefficient of $T_1^iT_2^j$ in $h(X + T_1 + T_2)$.

**Lemma 4.5.7 (leading terms).** Each $\phi \in F^\times$ has one monomial term $au^n$ with $\nu(\phi - au^n) > \nu(\phi)$. It is the *leading term* of $\phi$. Let $y \in F \setminus K$ and $\Lambda(y) = \sup\{\nu(y - c) : c \in K\}$ in $\mathbb{R} \cup \{\infty\}$. This supremum is not a maximum. For each $\rho \in \Gamma$ with $\rho < \Lambda(y)$ there is $c \in K$ with $\nu(y - c) = \rho$.

This statement is not in Lean.

*Proof.* Since $\nu(\phi) \in \Gamma$, there is one $n \in \mathbb{Z}^m$ with $s(n) = \nu(\phi)$. The element $\phi/u^n$ has value 0, and its residue is an element $a$ of $k^\times$. Then $\nu(\phi/u^n - a) > 0$, which is the claim. Two terms of value $\nu(\phi)$ have the same exponent $n$, and their coefficients are both the residue of $\phi/u^n$. If $\nu(y - c)$ is the maximum, let $au^n$ be the leading term of $y - c$; then $c + au^n \in K$ and $\nu(y - c - au^n) > \nu(y - c)$, which is a contradiction. For the last claim take $c' \in K$ with $\nu(y - c') > \rho$ and $n$ with $s(n) = \rho$, and let $c = c' + u^n$. Then $\nu(y - c) = \rho$. $\square$

We write $\Lambda = \Lambda(x)$. The set of the values $\nu(x - c)$, $c \in K$, has the supremum $\Lambda$ and no maximum. So for each $\lambda < \Lambda$ it has infinitely many elements in $[\lambda, \Lambda)$.

**Lemma 4.5.8 (truncations).** There are one set $X \subseteq \mathbb{Z}^m$ and one family $x_n \in k^\times$, $n \in X$, with these properties. Each $n \in X$ has $s(n) < \Lambda$, and for each $\lambda < \Lambda$ the set $X \cap \{s \le \lambda\}$ is finite. For $n \in X$ let $c_n = \sum x_{n'}u^{n'}$, the sum over the $n' \in X$ with $s(n') < s(n)$, and let $\xi_n = x - c_n$. Then $c_n \in K_0$, and the leading term of $\xi_n$ is $x_nu^n$. If $\Lambda < \infty$, the set $X$ is infinite.

This statement is not in Lean.

*Proof.* Let $\lambda < \Lambda$. Take $c \in K$ with $\nu(x - c) > \lambda$, and let $x_{\le\lambda}$ be the sum of the terms of the series $c$ with value $\le \lambda$. It is a finite sum. A second element $c'$ with $\nu(x - c') > \lambda$ has $\nu_S(c - c') > \lambda$, so its terms of value $\le \lambda$ are the same, and $x_{\le\lambda}$ does not depend on $c$. For $\lambda < \lambda'$ the sum $x_{\le\lambda}$ is the part of $x_{\le\lambda'}$ with values $\le \lambda$. Let $X$ be the union of the supports of the sums $x_{\le\lambda}$, and let $x_n$ be the coefficients. Then $X \cap \{s \le \lambda\}$ is the support of $x_{\le\lambda}$, which is finite, and each $n \in X$ has $s(n) < \Lambda$. We have $\nu(x - x_{\le\lambda}) > \lambda$ and $x_{\le s(n)} = c_n + x_nu^n$ for $n \in X$. So $c_n$ is a Laurent polynomial, and $\xi_n = x_nu^n + (x - x_{\le s(n)})$ has the leading term $x_nu^n$. Assume that $X$ is finite and $\Lambda < \infty$. The element $c = \sum_{n \in X}x_nu^n$ equals $x_{\le\lambda}$ for each $\lambda < \Lambda$ larger than the values on $X$. So $\nu(x - c) > \lambda$ for these $\lambda$, and $\nu(x - c) \ge \Lambda$. This contradicts Lemma 4.5.7. $\square$

The next lemma says that near $x$ a polynomial does not change its leading term. It is the form of the theorem of Kaplansky that we use.

**Lemma 4.5.9 (stability).** Let $\Lambda < \infty$ and let $h \in K[X]$, $h \ne 0$.

1. There is $\lambda_h < \Lambda$ such that $\nu(h(c) - h(x)) > \nu(h(x))$ for each $c \in K$ with $\nu(x - c) \ge \lambda_h$. Then $h(c)$ and $h(x)$ have the same leading term.
2. Let $h$ be not constant, and let $m_h(\rho) = \min_j(\nu(h^{[j]}(x)) + j\rho)$ for $\rho \in \mathbb{R}$, over the $j \ge 1$ with $h^{[j]} \ne 0$. There is a finite set $E_h \subseteq \mathbb{R}$ such that $\nu(h(c) - h(x)) \ge m_h(\nu(x - c))$ for each $c \in K$, with equality when $\nu(x - c) \notin E_h$.

This statement is not in Lean.

*Proof.* If $h$ is constant, then $h(c) - h(x) = 0$ and part 1 holds with each $\lambda_h$. Let $h$ be not constant. Since $x$ is transcendental over $K$, each $h^{[j]}(x)$ with $h^{[j]} \ne 0$ is not zero, and $\psi_j = \nu(h^{[j]}(x))$ is finite.

Part 2. We have $h(c) - h(x) = \sum_{j \ge 1}h^{[j]}(x)(c - x)^j$, and the $j$-th summand has the value $\psi_j + j\nu(x - c)$. This gives the inequality. The functions $\rho \mapsto \psi_j + j\rho$ are lines with distinct slopes, so two of them meet in at most one point. Let $E_h$ be the finite set of these points. For $\rho \notin E_h$ the least value is attained at one index, and the value of the sum is $m_h(\rho)$. The function $m_h$ is strictly increasing, as a minimum of strictly increasing functions.

Part 1, first step. We show that there is $\rho_0 < \Lambda$ with $\nu(h(c)) = \nu(h(x))$ for each $c \in K$ with $\nu(x - c) \ge \rho_0$. Assume not. Then for each $\rho < \Lambda$ there is $c \in K$ with $\nu(x - c) \ge \rho$ and $\nu(h(c)) \ne \nu(h(x))$. Choose such elements $c_1, c_2, \dots$ so that $\rho_i = \nu(x - c_i)$ is strictly increasing with limit $\Lambda$ and $\rho_i \notin E_h$. This is possible because $E_h$ is finite. Then $\nu(c_j - c_i) = \rho_i$ for $i < j$, so $(c_i)$ is pseudo Cauchy, and $x$ is a limit of it. It has no limit in $K$: a limit $c$ has $\nu(c - c_i) = \rho_i$ for large $i$, so $\nu(x - c) \ge \rho_i$ for each $i$ and $\nu(x - c) \ge \Lambda$, which contradicts Lemma 4.5.7. By Corollary 4.5.6 the sequence is of transcendental type, so $\nu(h(c_i))$ is a constant $\beta$ for large $i$. By part 2, $\nu(h(c_i) - h(x)) = m_h(\rho_i)$, and this is strictly increasing in $i$. If $\beta \ne \nu(h(x))$, then $\nu(h(c_i) - h(x)) = \min(\beta, \nu(h(x)))$ is constant for large $i$, which is false. So $\beta = \nu(h(x))$, and this contradicts the choice of the $c_i$.

Part 1, second step. The values $\nu(x - c)$ in $[\rho_0, \Lambda)$ are infinite in number, so there is $c \in K$ with $\rho_1 = \nu(x - c) \ge \rho_0$ and $\rho_1 \notin E_h$. Then $\nu(h(c)) = \nu(h(x))$, so $m_h(\rho_1) = \nu(h(c) - h(x)) \ge \nu(h(x))$. Take $\lambda_h$ with $\rho_1 < \lambda_h < \Lambda$. For $c' \in K$ with $\rho = \nu(x - c') \ge \lambda_h$, part 2 gives $\nu(h(c') - h(x)) \ge m_h(\rho) > m_h(\rho_1) \ge \nu(h(x))$. If $au^n$ is the leading term of $h(x)$, then $\nu(h(c') - au^n) > \nu(h(x)) = \nu(h(c'))$, so $au^n$ is also the leading term of $h(c')$. $\square$

### The data of a polynomial and the dominant index

Let $f \in K[X]$ be not constant, and write $f_k = f^{[k]}$, so that $f(c + \xi) = \sum_k f_k(c)\xi^k$. Let $L = \{k \ge 1 : f_k \ne 0\}$. It is not empty, because it contains the degree of $f$. For $k \in L$ let $\gamma_ku^{\mu_k}$ be the leading term of $f_k(x)$, with $\gamma_k \in k^\times$ and $\mu_k \in \mathbb{Z}^m$, and let $\varphi_k = \nu(f_k(x)) = s(\mu_k)$.

**Lemma 4.5.10 (the index is a power of $p$).** Let $\Lambda < \infty$, let $k \in L$, and let $0 < i < k$ with $\binom{k}{i} \not\equiv 0 \bmod p$. Then $i \in L$ and $\varphi_i + i\Lambda < \varphi_k + k\Lambda$. So each index where the function $k \mapsto \varphi_k + k\Lambda$ on $L$ has its minimum is a power of $p$, and $p^0 = 1$ is allowed.

This statement is not in Lean.

*Proof.* By the rule for Hasse derivatives, $(f_i)^{[k - i]} = \binom{k}{i}f_k$, and this is not zero. So $f_i \ne 0$ and $i \in L$. Apply Lemma 4.5.9 to $h = f_i$. The index $j = k - i$ occurs in $m_h$, and $\nu(h^{[k - i]}(x)) = \nu(\binom{k}{i}f_k(x)) = \varphi_k$, because $\binom{k}{i}$ is a nonzero element of the prime field. Choose $c \in K$ with $\rho = \nu(x - c) \ge \lambda_h$ and $\rho \notin E_h$. Then $\varphi_k + (k - i)\rho \ge m_h(\rho) = \nu(h(c) - h(x)) > \nu(h(x)) = \varphi_i$. Since $\rho < \Lambda$, we get $\varphi_k + (k - i)\Lambda > \varphi_i$.

Let $k \in L$ be not a power of $p$, and write $k = \sum_j k_jp^j$ in base $p$. Take a position $j$ with $k_j \ne 0$ and let $i = p^j$. Then $i \le k_jp^j \le k$, with equality only if $k = p^j$, so $i < k$. By the theorem of Lucas, $\binom{k}{p^j} \equiv k_j \not\equiv 0 \bmod p$. So $\varphi_i + i\Lambda < \varphi_k + k\Lambda$, and $k$ is not a minimum. $\square$

**Lemma 4.5.11 (the dominant index).** Let $\Lambda < \infty$. Let $k_*$ be the largest index of $L$ where $\varphi_k + k\Lambda$ has its minimum. Then $k_*$ is a power of $p$, and there is $\kappa_0 > 0$ such that $\varphi_{k_*} + k_*\lambda < \varphi_k + k\lambda$ for each $\lambda$ with $\Lambda - \kappa_0 < \lambda < \Lambda$ and each $k \in L$ with $k \ne k_*$.

This statement is not in Lean.

*Proof.* By Lemma 4.5.10, $k_*$ is a power of $p$. Let $k \in L$, $k \ne k_*$. If $\varphi_k + k\Lambda = \varphi_{k_*} + k_*\Lambda$, then $k < k_*$, and $(\varphi_k + k\lambda) - (\varphi_{k_*} + k_*\lambda) = (k_* - k)(\Lambda - \lambda) > 0$ for each $\lambda < \Lambda$. If $\varphi_k + k\Lambda > \varphi_{k_*} + k_*\Lambda$, the strict inequality stays true for $\lambda$ near $\Lambda$, by continuity. The set $L$ is finite. $\square$

We call $k_*$ the *dominant index* of $f$ at $x$, and we say that *the linear term is dominant* if $k_* = 1$.

### The case of a dominant linear term

We use Hensel's lemma in this form [Kuh-book]. Let $(H, \nu)$ be a henselian valued field with valuation ring $\mathcal{O}_H$. Let $Q \in \mathcal{O}_H[V]$ and $a \in \mathcal{O}_H$ with $\nu(Q(a)) > 0$ and $\nu(Q'(a)) = 0$. Then $Q$ has a root $V^* \in \mathcal{O}_H$ with $\nu(V^* - a) > 0$.

**Proposition 4.5.12 (a dominant linear term gives a henselian generator).** Let $(K_1, \nu)$ be a valued field, let $F_1$ be an immediate extension of $K_1$, and let $f \in K_1[X]$ and $x, z \in F_1$ with $z^p = f(x)$. Let $c \in K_1$ with $x \ne c$, and let $\lambda = \nu(x - c)$. Assume that $f_1(c) \ne 0$ and that $\nu(f_k(c)) + k\lambda > \nu(f_1(c)) + \lambda$ for each $k \ge 2$. Then $x \in K_1(z)^h$, where the henselization is taken in a henselization $F_1^h$ of $F_1$.

This statement is not in Lean.

*Proof.* Let $L' = K_1(z)^h \subseteq F_1^h$, and let $\xi = x - c$. Since $F_1/K_1$ is immediate, $\lambda$ is a value of $K_1$, so there is $\eta \in K_1$ with $\nu(\eta) = \lambda$. Let
$$Q(V) = \frac{f(c + \eta V) - z^p}{f_1(c)\eta} = q_0 + V + \sum_{k \ge 2}q_kV^k, \qquad q_0 = \frac{f(c) - z^p}{f_1(c)\eta}, \quad q_k = \frac{f_k(c)\eta^{k - 1}}{f_1(c)}.$$
The coefficients lie in $K_1(z) \subseteq L'$. For $k \ge 2$ we have $\nu(q_k) = \nu(f_k(c)) + (k - 1)\lambda - \nu(f_1(c)) > 0$ by the hypothesis. Next, $f(c) - z^p = f(c) - f(c + \xi) = -\sum_{k \ge 1}f_k(c)\xi^k$. The summand with $k = 1$ has the value $\nu(f_1(c)) + \lambda$, and each other summand has a larger value. So $\nu(f(c) - z^p) = \nu(f_1(c)) + \lambda$ and $\nu(q_0) = 0$. Thus $Q \in \mathcal{O}_{L'}[V]$.

Hensel's lemma. Let $a = -q_0 \in \mathcal{O}_{L'}$. Then $Q(a) = \sum_{k \ge 2}q_ka^k$ has positive value, and $Q'(a) = 1 + \sum_{k \ge 2}kq_ka^{k - 1}$ has value 0. The field $L'$ is henselian, so Hensel's lemma gives a root $V^* \in \mathcal{O}_{L'}$ of $Q$ with $\nu(V^* + q_0) > 0$.

The second root. The element $\xi/\eta$ of $F_1$ has value 0, and $Q(\xi/\eta) = (f(x) - z^p)/(f_1(c)\eta) = 0$. From $\xi/\eta = -q_0 - \sum_{k \ge 2}q_k(\xi/\eta)^k$ we get $\nu(\xi/\eta + q_0) > 0$.

Uniqueness. Let $V_1, V_2 \in \mathcal{O}_{F_1^h}$ be roots of $Q$ with $\nu(V_1 - V_2) > 0$. Then
$$0 = Q(V_1) - Q(V_2) = (V_1 - V_2)(1 + \epsilon), \qquad \epsilon = \sum_{k \ge 2}q_k\sum_{i = 0}^{k - 1}V_1^iV_2^{k - 1 - i},$$
and $\nu(\epsilon) > 0$, so $1 + \epsilon \ne 0$ and $V_1 = V_2$. The roots $V^*$ and $\xi/\eta$ satisfy $\nu(V^* - \xi/\eta) > 0$, so $\xi/\eta = V^* \in L'$, and $x = c + \eta V^* \in L'$. $\square$

### The cone lemma

The idea of the rest of the proof is this. Assume that the dominant index is $k_* = p^a$ with $a \ge 1$, and that the leading term of $f_{k_*}(x)$ is not a $p$-th power. The truncations of $x$ give an infinite set $X$ of exponents (Lemma 4.5.8). We will see that each exponent $n \in X$, except a finite number, gives one equation between exponents. The equation says that the vector from a fixed point $n^*$ of value $\Lambda$ to $n$ is a combination, with positive rational coefficients, of the same vectors for exponents of smaller value. Then all these vectors lie in a cone with a finite number of generators. The part of such a cone where the value is bounded contains only a finite number of points of the lattice $\mathbb{Z}^m$. This contradicts the infinite number of exponents. The lemma below is the statement on cones.

**Lemma 4.5.13 (cone lemma).** Let $n^* \in \mathbb{Q}^m$ and $\Lambda = s(n^*)$. Let $X \subseteq \mathbb{Z}^m$ be a set such that $s(n) < \Lambda$ for each $n \in X$ and $X \cap \{s \le \lambda\}$ is finite for each $\lambda < \Lambda$. Let $P \subseteq X$ be a finite set. Assume that for each $n \in X \setminus P$ there are an integer $k \ge 1$, elements $n'_1, \dots, n'_k \in X$ with $s(n'_i) < s(n)$, and a rational number $r > 0$ such that
$$n - n^* = r\sum_{i = 1}^k(n'_i - n^*).$$
Then $X$ is finite.

Status: a result of this project. The proof is new, and it is not yet in a journal.

Lean: `Singularity.finite_of_cone_relations` (the Lean theorem does not use that $s$ is injective)

*Proof.* Assume $X \ne \emptyset$. Let $C \subseteq \mathbb{Q}^m$ be the set of the sums $\sum_{\beta \in P}r_\beta(\beta - n^*)$ with $r_\beta \in \mathbb{Q}$ and $r_\beta \ge 0$. It is closed under sums and under multiplication by positive rational numbers, and it contains $0$.

Order. The map $s$ is injective, so distinct elements of $X$ have distinct values. For $n \in X$ the set of the $n' \in X$ with $s(n') < s(n)$ is finite, because it lies in $X \cap \{s \le s(n)\}$. Let $N(n)$ be the number of its elements.

Induction. We prove that $n - n^* \in C$ for each $n \in X$, by induction on $N(n)$. Let $n \in X$, and assume the claim for each $n' \in X$ with $N(n') < N(n)$. If $n \in P$, then $n - n^* = 1 \cdot (n - n^*)$ lies in $C$. If $n \notin P$, the hypothesis gives $n'_1, \dots, n'_k \in X$ with $s(n'_i) < s(n)$, so $N(n'_i) < N(n)$. Some of the $n'_i$ can lie in $P$; this does not matter. By the induction hypothesis each $n'_i - n^*$ lies in $C$. So the sum $\sum_i(n'_i - n^*)$ lies in $C$, and $n - n^* = r\sum_i(n'_i - n^*)$ lies in $C$ because $r > 0$. The case $N(n) = 0$ is included: an element with $N(n) = 0$ has no element of smaller value, so it cannot have a relation, and it lies in $P$.

The bound. The set $X \cap \{s \le \lambda\}$ is finite and not empty for a suitable $\lambda < \Lambda$, so $X$ has an element of least value $\sigma_0$. Let $n \in X$ and write $n - n^* = \sum_\beta r_\beta(\beta - n^*)$ with $r_\beta \ge 0$. Apply $s$:
$$\Lambda - s(n) = \sum_{\beta \in P}r_\beta(\Lambda - s(\beta)).$$
Each term on the right is $\ge 0$, because $s(\beta) < \Lambda$, and the left side is at most $\Lambda - \sigma_0$. So $0 \le r_\beta \le (\Lambda - \sigma_0)/(\Lambda - s(\beta))$ for each $\beta \in P$. Thus each $n \in X$ lies in the set $n^* + \{\sum_\beta r_\beta(\beta - n^*) : 0 \le r_\beta \le (\Lambda - \sigma_0)/(\Lambda - s(\beta))\}$, which is a bounded subset of $\mathbb{R}^m$. A bounded subset of $\mathbb{Z}^m$ is finite. $\square$

### The cone theorem

**Theorem 4.5.14 (cone theorem).** Let $F$ be an immediate extension of $K$, let $x \in F$ be transcendental over $K$, let $f \in K[X]$ be not constant, and let $z \in F$ with $z^p = f(x)$. Let $\Lambda < \infty$, and assume that the linear term is not dominant, so that $k_* = p^a$ with $a \ge 1$. Then the leading term $\gamma_{k_*}u^{\mu_{k_*}}$ of $f_{k_*}(x)$ is a $p$-th power: $\mu_{k_*} \in p\mathbb{Z}^m$.

Status: a result of this project. The proof is new, and it is not yet in a journal.

This statement is not in Lean.

Before the proof we explain the constants. We write $\gamma_*$, $\mu_*$ and $\varphi_*$ for $\gamma_{k_*}$, $\mu_{k_*}$ and $\varphi_{k_*}$. The proof takes a center $c_0$ near $x$ and expands $f$ at $c_0$. Three kinds of terms must be controlled, and each constant controls one of them.

- The number $\Delta_k = (\varphi_k + k\Lambda) - (\varphi_* + k_*\Lambda) \ge 0$, for $k \in L$, measures how far the index $k$ is from the minimum at $\Lambda$. An index with $\Delta_k > 0$ cannot take part in the final equation.
- The number $\varphi'_k = \nu(f_k(x) - \gamma_ku^{\mu_k})$, defined when the polynomial $f_k - \gamma_ku^{\mu_k}$ is not zero, is the value of the second term of $f_k(x)$. We have $\varphi'_k > \varphi_k$. A number $\omega_0 > 0$ smaller than each difference $\varphi'_k - \varphi_k$ separates the leading term of $f_k$ from its other terms. If no $\varphi'_k$ is defined, let $\omega_0 = 1$.
- The number $\kappa > 0$ is the width of the window $(\Lambda - \kappa, \Lambda)$ in which we choose all the exponents. It is so small that four things hold: (a) $\kappa < \kappa_0$, so that the index $k_*$ is dominant in the window (Lemma 4.5.11); (b) $\Lambda - \kappa \ge \lambda_h$ for the finitely many polynomials $h = f_k$ and $h = f_k - \gamma_ku^{\mu_k}$, $k \in L$, so that these polynomials keep their leading terms in the window (Lemma 4.5.9); (c) $k\kappa < \Delta_k$ for each $k \in L$ with $\Delta_k > 0$; (d) $k\kappa < \omega_0$ for each $k \in L$.

There are only finitely many conditions, so such a $\kappa$ exists.

*Proof.* Assume that $\mu_* \notin p\mathbb{Z}^m$. We derive a contradiction.

Step 1 (a center near $x$). By Lemma 4.5.8 the set $X$ is infinite and $X \cap \{s \le \Lambda - \kappa\}$ is finite, so there is $n_0 \in X$ with $s(n_0) > \Lambda - \kappa$. Let $c_0 = c_{n_0} \in K_0$, $\tau_0 = f(c_0)$ and $\tau_k = f_k(c_0)$ for $k \in L$. We have $\nu(x - c_0) = s(n_0) > \Lambda - \kappa$. By condition (b) and Lemma 4.5.9 for $h = f_k$, the series $\tau_k$ has the leading term $\gamma_ku^{\mu_k}$. By Lemma 4.5.9 for $h = f_k - \gamma_ku^{\mu_k}$, the element $\tau_k - \gamma_ku^{\mu_k}$ has the value $\varphi'_k > \varphi_k + \omega_0$, or it is zero. So each term of $\tau_k$ other than the leading term has a value $> \varphi_k + \omega_0$. Let $X_1 = \{n \in X : s(n) \ge s(n_0)\}$. It is infinite. For $n \in X_1$ let $\eta_n = c_n - c_0$. It is the sum of the terms $x_{n'}u^{n'}$ with $n' \in X_1$ and $s(n') < s(n)$, and the Taylor formula at $c_0$ gives
$$f(c_n) = \tau_0 + \sum_{k \in L}\tau_k\eta_n^k.$$

Step 2 (one coefficient). Let $n \in X_1$ and $v_n = \mu_* + k_*n$. We have $z^p - f(c_n) = f(x) - f(c_n) = \sum_{k \in L}f_k(c_n)\xi_n^k$. Since $\nu(x - c_n) = s(n) > \Lambda - \kappa$, Lemma 4.5.9 and condition (b) show that $f_k(c_n)$ has the leading term $\gamma_ku^{\mu_k}$. The leading term of $\xi_n$ is $x_nu^n$ (Lemma 4.5.8). So the summand of index $k$ has the value $\varphi_k + ks(n)$ and the leading term $\gamma_kx_n^ku^{\mu_k + kn}$. By condition (a) and Lemma 4.5.11, the summand of index $k_*$ has the least value, and so
$$\nu(z^p - \theta) > s(v_n), \qquad \theta = f(c_n) + \gamma_*x_n^{k_*}u^{v_n} \in K.$$
Write $\theta = \sum_eu^e\theta_e^p$ as in Lemma 4.5.2. Then $z^p - \theta = (z - \theta_0)^p + \sum_{e \ne 0}u^e(-\theta_e)^p$, with $z - \theta_0 \in F$. By Lemma 4.5.2, part 1, in $F$, each summand has a value $\ge \nu(z^p - \theta) > s(v_n)$. So for $e \ne 0$ each term of the series $u^e\theta_e^p$ has a value $> s(v_n)$. By Lemma 4.5.2, part 3, these are the terms of $\theta$ of the class $e$. The class of $v_n$ is the class of $\mu_*$, because $p$ divides $k_*$, and it is not $0$ by our assumption. So the coefficient of $u^{v_n}$ in $\theta$ is zero, and the coefficient of $u^{v_n}$ in the series $f(c_n)$ is $-\gamma_*x_n^{k_*} \ne 0$.

Step 3 (the relation). By Steps 1 and 2 the coefficient of $u^{v_n}$ in $\tau_0 + \sum_{k \in L}\tau_k\eta_n^k$ is not zero. So it is not zero in $\tau_0$ or in some product $\tau_k\eta_n^k$. The coefficient of $u^{v_n}$ in $\tau_k\eta_n^k$ is a finite sum of products of a coefficient of $\tau_k$ and $k$ coefficients of $\eta_n$, over the tuples of exponents with sum $v_n$. If this sum is not zero, at least one tuple occurs. So $u^{v_n}$ is in the support of $\tau_0$, or there are $k \in L$, an exponent $g$ of a term of $\tau_k$, and $n'_1, \dots, n'_k \in X_1$ with $s(n'_i) < s(n)$, such that
$$g + n'_1 + \dots + n'_k = v_n.$$
Let $P$ be the set of the $n \in X_1$ such that $u^{v_n}$ is in the support of $\tau_0$. We have $s(v_n) = \varphi_* + k_*s(n) < \varphi_* + k_*\Lambda$. The series $\tau_0$ has only finitely many terms below $\varphi_* + k_*\Lambda$, and the map $n \mapsto v_n$ is injective. So $P$ is finite.

Let $n \in X_1 \setminus P$, with $k$, $g$ and $n'_i$ as above. Write $s(g) = \varphi_k + \omega$ with $\omega \ge 0$, and let $d(n') = \Lambda - s(n')$ for $n' \in X_1$. Then $0 < d(n) < d(n'_i) < \kappa$, because $\Lambda - \kappa < s(n_0) \le s(n'_i) < s(n) < \Lambda$. Apply $s$ to the equation of the exponents: $\varphi_k + \omega + k\Lambda - \sum_id(n'_i) = \varphi_* + k_*\Lambda - k_*d(n)$. That is,
$$\Delta_k + \omega + k_*d(n) = \sum_{i = 1}^kd(n'_i) < k\kappa.$$
The three terms on the left are $\ge 0$. So $\Delta_k < k\kappa$, and condition (c) gives $\Delta_k = 0$. Also $\omega < k\kappa < \omega_0$ by condition (d). A term of $\tau_k$ other than the leading term has $\omega > \omega_0$ (Step 1), so $g$ is the exponent of the leading term: $\omega = 0$ and $g = \mu_k$. Next, $k_*d(n) = \sum_id(n'_i) > kd(n)$, so $k < k_*$. Let
$$n^* = \frac{\mu_k - \mu_*}{k_* - k} \in \mathbb{Q}^m.$$
From $\Delta_k = 0$ we get $s(n^*) = (\varphi_k - \varphi_*)/(k_* - k) = \Lambda$. The map $s$ is injective on $\mathbb{Q}^m$, so $n^*$ is the same point for each $n \in X_1 \setminus P$ and each $k$ that occurs. The equation of the exponents is $\sum_in'_i = \mu_* - \mu_k + k_*n = k_*n - (k_* - k)n^*$. So $\sum_i(n'_i - n^*) = k_*(n - n^*)$, that is,
$$n - n^* = \frac{1}{k_*}\sum_{i = 1}^k(n'_i - n^*).$$

Step 4 (the cone). If $X_1 = P$, then $X_1$ is finite. In the other case the point $n^*$ of Step 3 exists, and $s(n^*) = \Lambda$. The set $X_1$ has $s < \Lambda$ on it, and $X_1 \cap \{s \le \lambda\}$ is finite for each $\lambda < \Lambda$. Each $n \in X_1 \setminus P$ has a relation as in Lemma 4.5.13, with $r = 1/k_*$ and with $n'_i \in X_1$. Lemma 4.5.13 shows that $X_1$ is finite. In both cases this contradicts Step 1. $\square$

The linear term has no special role in the proof: the index $k = 1$ is one of the indices of Step 3. The proof uses $p \mid k_*$ only for the class of $v_n$ in Step 2.

### Henselian rationality for $z^p = g(x^p) + Gx + b$

For the local uniformization we need one more statement on the base. It is the proof of Volume 9, Theorem 3.23.15, with $m$ monomials in place of two and one more variable. We use the ball property of Volume 9, Definition 3.23.12, and the Taylor lemma, Volume 9, Lemma 3.23.14.

**Proposition 4.5.15 (one variable over the base).** Let $M$ be an immediate extension of $K_0$, and let $y \in M$ be transcendental over $K_0$ with the ball property over $K_0$. Then the restriction of $\nu$ to $K_0(y)$ has local uniformization as a valuation of $K_0(y)/k$.

This statement is not in Lean.

*Proof.* Step A (the base). Let $Z_0 \subseteq K_0^\times$ be finite. We show that there are Laurent monomials $u'_1, \dots, u'_m$ in $u$ whose values are a basis of $\Gamma$ and are positive, such that each $z \in Z_0$ is $u'^c$ times a unit of $R_0 = k[u']_{(u')}$ with $c \in \mathbb{Z}^m$, and $c \in \mathbb{N}^m$ if $\nu(z) \ge 0$. Write each element of $Z_0$ as a quotient of Laurent polynomials. A nonzero Laurent polynomial is $P = a_{n_P}u^{n_P}(1 + \sum_{n \ne n_P}(a_n/a_{n_P})u^{n - n_P})$, where $a_{n_P}u^{n_P}$ is its term of least value, so $s(n - n_P) > 0$ for the other terms. Let $D$ be the finite set of these values $s(n - n_P)$ and of the values $\nu(z) \ge 0$, $z \in Z_0$. The lattice lemma (Volume 5, Lemma 2.1.4) for $\Gamma \cong \mathbb{Z}^m$ gives a basis $\gamma'_1, \dots, \gamma'_m$ of $\Gamma$ of positive elements such that each element of $D$ is a combination of the $\gamma'_i$ with coefficients in $\mathbb{N}$. Let $u'_i = u^{b_i}$ with $s(b_i) = \gamma'_i$. Since $s$ is an isomorphism of $\mathbb{Z}^m$ onto $\Gamma$, the $u'_i$ are a basis of the group of Laurent monomials, $K_0 = k(u')$, and $A_0 = k[u']$ is a polynomial ring. The ring $R_0$ is dominated by $\nu$. A monomial $u^n$ with $s(n) \in D$ is $u'^c$ with $c \in \mathbb{N}^m$. So each $u^{n - n_P}$ above lies in the maximal ideal of $R_0$, each $P$ is a monomial times a unit, and each $z \in Z_0$ is $u'^c$ times a unit with $c \in \mathbb{Z}^m$. If $\nu(z) \ge 0$, then $s$ of the exponent of $z$ in $u$ lies in $D$, so $c \in \mathbb{N}^m$.

Step B (the variable $y$). Let $Z \subseteq K_0(y)^\times$ be finite. Write each element as $f(y)/g(y)$ with $f, g \in K_0[X]$ nonzero, and let $Z'$ be the finite set of these $f$ and $g$. By Volume 9, Lemma 3.23.14, there is $d \in K_0$ such that, with $\gamma = \nu(y - d)$, we have $\nu(h(y)) = \nu(h(d)) < \nu(h^{[j]}(d)) + j\gamma$ for each $h \in Z'$ and each $j \ge 1$ with $h^{[j]} \ne 0$. Since $M/K_0$ is immediate, there is $N \in K_0$ with $\nu(N) = \gamma$. Let $Y = (y - d)/N$, so $\nu(Y) = 0$. Then
$$h(y) = h(d)\Big(1 + \sum_{j \ge 1}\rho_{h,j}Y^j\Big), \qquad \rho_{h,j} = \frac{h^{[j]}(d)N^j}{h(d)}, \quad \nu(\rho_{h,j}) > 0.$$
Apply Step A to the finite set $Z_0$ of the elements $h(d)$, $h \in Z'$, the nonzero $\rho_{h,j}$, and the quotients $f(d)/g(d)$ for $f(y)/g(y) \in Z$. Let $\lambda_Y \in k^\times$ be the residue of $Y$, let $A_1 = A_0[Y]$, and let $\mathfrak{m}_1$ be the ideal of $A_1$ generated by $u'_1, \dots, u'_m$ and $Y - \lambda_Y$. Since $Y$ is transcendental over $K_0$, $A_1$ is a polynomial ring over $k$ with fraction field $K_0(y)$. The ideal $\mathfrak{m}_1$ is maximal with residue field $k$, and its elements have positive value, so it is the center of $\nu$ on $A_1$. The local ring $R_1 = (A_1)_{\mathfrak{m}_1}$ is regular, with the regular system of parameters $u'_1, \dots, u'_m, Y - \lambda_Y$. Each nonzero $\rho_{h,j}$ has positive value, so by Step A it is $u'^c$ times a unit with $c \in \mathbb{N}^m$ and $c \ne 0$, and it lies in the maximal ideal of $R_1$. So $1 + \sum_j\rho_{h,j}Y^j$ is a unit of $R_1$, and $h(y)$ is $u'^{c_h}$ times a unit, where $h(d)$ is $u'^{c_h}$ times a unit of $R_0$. For $z = f(y)/g(y) \in Z$ we get that $z$ is $u'^{c_f - c_g}$ times a unit of $R_1$. If $\nu(z) \ge 0$, then $\nu(f(d)/g(d)) = \nu(z) \ge 0$, and $f(d)/g(d) \in Z_0$ has the exponent $c_f - c_g$, so $c_f - c_g \in \mathbb{N}^m$ by Step A, and $z \in R_1$.

Local uniformization. Let $S_1 \subseteq \mathcal{O}_\nu \cap K_0(y)$ be finite, and apply Step B to $Z = S_1 \setminus \{0\}$. Then $S_1 \subseteq R_1$. Write each $s \in S_1$ as $a_s/b_s$ with $a_s, b_s \in A_1$ and $b_s \notin \mathfrak{m}_1$. Then $\nu(b_s) = 0$, and $A' = A_1[b_s^{-1} : s \in S_1]$ is an affine model of $K_0(y)/k$ with $S_1 \subseteq A' \subseteq \mathcal{O}_\nu$, whose local ring at the center of $\nu$ is $R_1$. This is local uniformization in the form of Volume 3, Proposition 4.1.6. $\square$

**Theorem 4.5.16 (henselian rationality for $z^p = g(x^p) + Gx + b$).** Let $F = K_0(x, z)$ be a valued field extension of $K_0$ that is immediate and of transcendence degree one over $K_0$, with
$$z^p = g(x^p) + Gx + b, \qquad g = \sum_{l \ge 1}\tau_lY^l \in K_0[Y], \quad G \in K_0^\times, \quad b \in K_0.$$
Write $\tau_l = \sum_eu^e\tau_{l,e}^p$ with $\tau_{l,e} \in K_0$ as in Lemma 4.5.2, and let $z' = z - \sum_{l \ge 1}\tau_{l,0}x^l$. Let $f' = g'(X^p) + GX + b$ with $g' = \sum_l(\tau_l - \tau_{l,0}^p)Y^l$. Then:

1. $F \subseteq K_0(z')^h$, so $(F/K_0, \nu)$ is henselian rational with the transcendence basis $\{z'\}$;
2. the valuation $\nu$ of $F/k$ has local uniformization;
3. let $F^h$ be a henselization of $F$, which contains a henselization $K$ of $K_0$, and let $\Lambda = \sup\{\nu(x - c) : c \in K\}$. If $\Lambda < \infty$, the linear term of $f'$ is dominant at $x$. If $\Lambda = \infty$, the inequalities of Proposition 4.5.12 for $f'$, $x$ and $z'$ hold at each $c \in K$ with $\nu(x - c)$ large enough.

Status: a result of this project. The proof is new, and it is not yet in a journal.

This statement is not in Lean.

*Proof.* Preparation. We have $z'^p = z^p - \sum_l\tau_{l,0}^px^{pl} = f'(x)$, and $K_0(x, z') = K_0(x, z) = F$. Each coefficient $\tau_l - \tau_{l,0}^p = \sum_{e \ne 0}u^e\tau_{l,e}^p$ of $g'$ is a series with no term of the class $0$, by Lemma 4.5.2, part 3. The element $x$ is transcendental over $K$: if not, $x$ is algebraic over $K_0$, and then $z$ is algebraic over $K_0$, which contradicts the transcendence degree. The henselization $F^h$ is an immediate extension of $F$, so it is an immediate extension of $K$. So the results above apply in $F^h$ to $x$, $z'$ and $f' \in K_0[X] \subseteq K[X]$.

The Hasse derivatives. We have $(X^{pj})^{[k]} = \binom{pj}{k}X^{pj - k}$. By the theorem of Lucas, $\binom{pj}{k} \equiv 0 \bmod p$ if $p \nmid k$, and $\binom{pj}{pl} \equiv \binom{j}{l}$. So $f'_1 = G$, $f'_{pl} = (g')^{[l]}(X^p)$ for $l \ge 1$, where $(g')^{[l]}$ is the Hasse derivative in $Y$, and $f'_k = 0$ for the other $k \ge 2$. For $c \in K$ the element $f'_{pl}(c) = \sum_{j \ge l}\binom{j}{l}(\tau_j - \tau_{j,0}^p)(c^{j - l})^p$ is a series with no term of the class $0$: by Lemma 4.5.1 the terms of a $p$-th power have the class $0$, so each term of a product of a series with no term of the class $0$ and a $p$-th power has a class $\ne 0$.

Case $\Lambda < \infty$. Assume that $k_* = p^a$ with $a \ge 1$. Then $k_* \in L$, and $k_* = pl$ with $l \ge 1$. By Lemma 4.5.9 the leading term of $f'_{k_*}(x)$ is the leading term of $f'_{k_*}(c)$ for $c \in K$ near $x$, so its class is not $0$. This contradicts Theorem 4.5.14 for $f'$ and $z'$. So $k_* = 1$, which is item 3. Take $c \in K$ with $\lambda = \nu(x - c)$ in $(\Lambda - \kappa_0, \Lambda)$ and $\lambda \ge \lambda_h$ for $h = f'_k$, $k \in L$. Such $c$ exists, because the values $\nu(x - c)$ come arbitrarily close to $\Lambda$. Then $\nu(f'_k(c)) = \varphi_k$ for $k \in L$ by Lemma 4.5.9, and $\varphi_k + k\lambda > \varphi_1 + \lambda$ for $k \in L$, $k \ge 2$, by Lemma 4.5.11. For $k \notin L$ we have $f'_k(c) = 0$. Also $f'_1(c) = G \ne 0$ and $x \ne c$. Proposition 4.5.12 for $K_1 = K$ and $F_1 = F^h$ gives $x \in K(z')^h$.

Case $\Lambda = \infty$. Here $x \ne 0$, and for $c \in K$ with $\nu(x - c) > \nu(x)$ we have $\nu(c) = \nu(x)$. Then $\nu(f'_{pl}(c)) \ge B$ for each $l \ge 1$, where $B$ is the least of the numbers $\nu(\tau_j - \tau_{j,0}^p) + p(j - l)\nu(x)$ over the pairs $(j, l)$ with $j \ge l \ge 1$ and $\tau_j \ne \tau_{j,0}^p$. The set of such $l$ is finite. Since $\Lambda = \infty$, there is $c \in K$ with $\lambda = \nu(x - c) > \nu(x)$ and $B + pl\lambda > \nu(G) + \lambda$ for each $l \ge 1$ with $(g')^{[l]} \ne 0$; this is possible because $pl > 1$. This is item 3 for $\Lambda = \infty$. Proposition 4.5.12 gives $x \in K(z')^h$.

Item 1. In both cases $x \in K(z')^h$, where the henselizations are taken in $F^h$. The field $K_0(z')^h$ is henselian and contains $K_0$, so it contains the henselization $K$ of $K_0$ in $F^h$. So $K_0(z') \subseteq K(z') \subseteq K_0(z')^h$, and thus $K(z')^h = K_0(z')^h$ [Kuh-book]. Hence $x \in K_0(z')^h$, and $F = K_0(x, z') \subseteq K_0(z')^h$. The field $F$ is algebraic over $K_0(z')$, so $z'$ is transcendental over $K_0$ and $\{z'\}$ is a transcendence basis of $F/K_0$.

Item 2. First, $z'$ has the ball property over $K_0$. The extension $F^h/K_0$ is immediate, and $z'$ is transcendental over $K_0$. Let $\Lambda' = \sup\{\nu(z' - c) : c \in K\}$. Each $c \in K$ has truncations in $K_0$ of arbitrarily high precision (Lemma 4.5.1), so $\Lambda'$ is also the supremum over $c \in K_0$. If $\Lambda' = \infty$, then for each $\beta$ there is $a_0 \in K_0$ with $\nu(z' - a_0) \ge \beta$, and Volume 9, Lemma 3.23.13, part 1, gives the ball property. Let $\Lambda' < \infty$. By Lemma 4.5.7 for $y = z'$, the supremum is not a maximum, so there are $a_i \in K_0$ such that $\gamma_i = \nu(z' - a_i)$ is strictly increasing with limit $\Lambda'$. The sequence $(a_i)$ is pseudo Cauchy with the limit $z'$, and it has no limit in $K$, by the argument of the proof of Lemma 4.5.9. By Corollary 4.5.6 it is of transcendental type over $K$, so also over $K_0$. Volume 9, Lemma 3.23.13, part 2, for $L = K_0$ gives the ball property. Now Proposition 4.5.15 for $M = F^h$ and $y = z'$ shows that $K_0(z')$ has local uniformization. The extension $F/K_0(z')$ is finite, because $F$ is finitely generated and algebraic over $K_0(z')$, and $F \subseteq K_0(z')^h$ by item 1. Volume 9, Theorem 3.23.11, shows that $F$ has local uniformization. $\square$

**Corollary 4.5.17 (additive polynomials).** Let $A(X) = \sum_{i = 0}^ra_iX^{p^i}$ with $a_i \in K_0$ and $a_0 \ne 0$, let $b \in K_0$, and let $F = K_0(x, z)$ be an immediate extension of $K_0$ of transcendence degree one with $z^p = A(x) + b$. Write $a_i = \sum_eu^ea_{i,e}^p$ as in Lemma 4.5.2, and let $z' = z - \sum_{i = 1}^ra_{i,0}x^{p^{i - 1}}$. Then $F \subseteq K_0(z')^h$, and the valuation $\nu$ of $F/k$ has local uniformization.

Status: a result of this project. The proof is new, and it is not yet in a journal.

This statement is not in Lean.

*Proof.* Apply Theorem 4.5.16 with $g = \sum_{i = 1}^ra_iY^{p^{i - 1}}$ and $G = a_0$. Then $g(x^p) + Gx = A(x)$, the coefficient $\tau_l$ is $a_i$ for $l = p^{i - 1}$ and $0$ for the other $l$, and $\sum_l\tau_{l,0}x^l = \sum_{i \ge 1}a_{i,0}x^{p^{i - 1}}$. $\square$

For $r = 1$ the corollary is the model $z^p = a_1x^p + a_0x + b$ with $z' = z - a_{1,0}x$.

### Examples

**Example 4.5.18 ($p = 2$ and $m = 1$).** Let $p = 2$, $m = 1$, $u = u_1$ and $\nu(u) = 1$, so $\Gamma = \mathbb{Z}$. Let $F = K_0(x, z)$ be immediate over $K_0$ of transcendence degree one with
$$z^2 = ux^2 + x + b, \qquad b \in K_0.$$

1. Here $\Lambda = \infty$. The values $\nu(x - c)$ lie in the discrete group $\mathbb{Z}$, and by Lemma 4.5.7 a bounded set of them has no maximum. A bounded set of integers has a maximum, so the set is not bounded.
2. The classes. In Theorem 4.5.16, $g = uY$, $\tau_1 = u$, $G = 1$. The exponent of $u = u^1 \cdot 1^2$ is $1$, of the class $1 \ne 0$ in $\mathbb{Z}/2\mathbb{Z}$. So $\tau_{1,0} = 0$, $\tau_{1,1} = 1$, and $z' = z$. The Hasse derivatives of $f = uX^2 + X + b$ are $f_1 = 1$ and $f_2 = u$, so $L = \{1, 2\}$, with the leading terms $1 = u^0$ and $u = u^1$, the values $\varphi_1 = 0$ and $\varphi_2 = 1$, and the classes $0$ and $1$.
3. Why the linear term wins. The inequality of Proposition 4.5.12 is $\nu(f_2(c)) + 2\lambda > \nu(f_1(c)) + \lambda$, that is, $1 + 2\lambda > \lambda$, that is, $\lambda > -1$. Each $c \in K$ with $\nu(x - c) \ge 0$ satisfies it, so $x \in K(z)^h$ and $F \subseteq K_0(z)^h$.
4. A variant with the class $0$. For $z^2 = u^2x^2 + x + b$ we have $\tau_1 = u^2 = u^0 \cdot u^2$, so $\tau_{1,0} = u$ and $z' = z - ux$. Then $z'^2 = x + b$, and $F = K_0(z')$ is a rational function field. Without the change, the leading term $u^2$ of $f_2$ is a square, and nothing forbids the quadratic term to be dominant.
5. A variant with $m = 2$ and $\Lambda < \infty$. Let $m = 2$, $\nu(u_1) = 1$, $\nu(u_2) = \sqrt 2$, and $z^2 = u_1x^2 + x + b$. Then $\varphi_1 = 0$, $\varphi_2 = 1$ and $\mu_2 = (1, 0) \notin 2\mathbb{Z}^2$. The linear term is dominant if and only if $0 + \Lambda < 1 + 2\Lambda$, that is, $\Lambda > -1$. If $\Lambda < -1$, the index $2$ is the dominant index; if $\Lambda = -1$, the two values are equal and the dominant index is the larger index $2$. In both cases Theorem 4.5.14 says that $\mu_2 \in 2\mathbb{Z}^2$, which is false. So $\Lambda > -1$ for each such $F$ with $\Lambda < \infty$, and the linear term is dominant.

Such fields exist for $m = 1$. Let $b \in k[u]$, and write $b = \sum_{n \ge 0}b_nu^n$. Let $x = \sum_{n \ge 0}x_nu^n$ in $k((u))$ with $x_{2j + 1} = x_j^2 + b_{2j + 1}$ for each $j \ge 0$. The coefficients $x_{2j}$ are free, and each choice of them gives one series $x$. The coefficient of $u^{2j + 1}$ in $ux^2 + x + b$ is $x_j^2 + x_{2j + 1} + b_{2j + 1} = 0$. So $ux^2 + x + b$ has only terms of even exponent, and it is a square $z^2$ in $k((u))$, because $k$ is perfect. The field $K_0(x, z) \subseteq k((u))$ is immediate over $K_0$. We show that some choice gives an $x$ that is transcendental over $K_0$. Let $k_0 \subseteq k$ be a countable subfield that contains the coefficients of $b$, and choose the $x_{2j}$ in $k_0$. Then $x \in k_0((u))$. There are uncountably many choices, and only countably many elements of $k_0((u))$ are algebraic over $k_0(u)$. So some $x$ is transcendental over $k_0(u)$. This $x$ is transcendental over $K_0 = k(u)$: let $\sum_ia_ix^i = 0$ with $a_i \in k[u]$, and write $a_i = \sum_\beta e_\beta a_{i\beta}$ with $a_{i\beta} \in k_0[u]$, where the $e_\beta$ are finitely many elements of $k$ that are linearly independent over $k_0$. Then $\sum_\beta e_\beta\big(\sum_ia_{i\beta}x^i\big) = 0$ with $\sum_ia_{i\beta}x^i \in k_0((u))$. The coefficient of each power of $u$ gives a linear relation of the $e_\beta$ over $k_0$, so $\sum_ia_{i\beta}x^i = 0$ for each $\beta$. Thus each $a_{i\beta}$ is zero, and each $a_i$ is zero.

This statement is not in Lean.

**Example 4.5.19 (a change by a product).** Let $G_1 \in K$ and
$$f = X^{p + 1} + G_1^pX = X(X + G_1)^p.$$
Let $F$ be an immediate extension of $K$ and $x, z \in F$ with $x$ transcendental over $K$ and $z^p = f(x)$. Let $F_2 = K(x, z)$.

1. The data. The Hasse derivatives are $f_1 = X^p + G_1^p = (X + G_1)^p$, $f_p = X$ and $f_{p + 1} = 1$, because $\binom{p + 1}{p} \equiv 1$ and $\binom{p + 1}{k} \equiv 0 \bmod p$ for $2 \le k \le p - 1$. So $L = \{1, p, p + 1\}$, $\varphi_1 = p\nu(x + G_1)$, $\varphi_p = \nu(x)$ and $\varphi_{p + 1} = 0$.
2. The field is rational. We have $x^p + G_1^p \ne 0$ and $x = z^p/(x^p + G_1^p)$, so $K(x) = K(x^p, z^p) = KF_2^p$. By Lemma 4.5.2, $K = \sum_eu^eK^p$, so $KF_2^p = \sum_eu^eF_2^p$, and the sum is direct by Lemma 4.5.2, part 1. Write $x = \sum_eu^ey_e^p$ with $y_e \in F_2$. Then $z^p = x(x + G_1)^p = \sum_eu^e((x + G_1)y_e)^p$. The left side has only the component $e = 0$. By uniqueness, $(x + G_1)y_e = 0$ for $e \ne 0$, and $(x + G_1)y_0 = z$. So $y_e = 0$ for $e \ne 0$, $x = y_0^p$, and $z' = z/(x + G_1) = y_0$ satisfies $x = z'^p$ and $z = (z'^p + G_1)z'$. Thus $F_2 = K(z')$ is a rational function field over $K$.
3. The peeling. Let $\Lambda < \infty$. Since $x = z'^p$, Lemma 4.5.2, part 1, gives $\nu(x - c) \le \nu(x - c_0^p)$ for $c = \sum_eu^ec_e^p \in K$, so the best approximations of $x$ are $p$-th powers, and all the terms $x_nu^n$ of Lemma 4.5.8 have the class $0$. Assume that the dominant index is $p$. The change $z_1 = z - \delta x$, with $\delta^p$ the leading term of $f_p(x) = x$, gives $z_1^p = f^{(1)}(x)$ with $f^{(1)} = f - \delta^pX^p$. Only $f_p$ changes: $f^{(1)}_p = X - \delta^p$. After $j$ such steps $f^{(j)}_p = X - D_j^p$, where $D_j$ is the sum of the first $j$ terms of the truncations of $z'$, and $z_j = z - D_jx$. The dominant index is $p$ at step $j$ if and only if $\nu(x - D_j^p) + p\Lambda \le p\nu(x + G_1) + \Lambda$, because the index $p + 1$ is never the minimum (Lemma 4.5.10). Since $-G_1 \in K$, we have $\nu(x + G_1) < \Lambda$, and $\nu(x - D_j^p)$ increases to $\Lambda$. So after a finite number of steps the linear term is dominant, and Proposition 4.5.12 applies. The number of steps is the number of terms of $x$ with value at most $p\nu(x + G_1) - (p - 1)\Lambda$. It depends on $x$, and each step is a sum $z - D_jx$.
4. The product. The single change $z' = z/(x + G_1)$ does more than all the sums: it gives $F_2 = K(z')$ for each $x$ at once. The infinite sum of all the peeling steps would be $z - z'x = G_1z'$, which is again the product, up to the constant $G_1$.

This statement is not in Lean.

### What this section does not prove

The results above are one case of one step. We list what stays open.

- A general $f$. Let $z^p = f(x)$ with $f \in K[X]$, $f' \ne 0$ and $\Lambda < \infty$. By Proposition 4.5.12 the step is done if the linear term is dominant. By Theorem 4.5.14 the other case is a dominant index $k_* = p^a$, $a \ge 1$, where the leading term of $f_{k_*}(x)$ is $\delta^p$ for a monomial term $\delta$. The change $z_1 = z - \delta x^{p^{a - 1}}$ gives $z_1^p = f^{(1)}(x)$ with $f^{(1)} = f - \delta^pX^{k_*}$. This makes $\varphi_{k_*}$ larger and does not change the other $\varphi_k$, because $(X^{p^a})^{[k]} = 0$ for $0 < k < p^a$ and for $k > p^a$. We can repeat the change. It stops when the linear term is dominant. For $f$ as in Theorem 4.5.16 one change does all the steps. For a general $f$ we do not know that the peeling stops: the peeling can be infinite. Example 4.5.19 shows that the right change can be a product and not a sum.
- A base that is not a field of admissible series. Let $K' = K(x_1)^h$, where $x_1$ is transcendental and immediate over $K$ with $\Lambda(x_1) < \infty$. Lemma 4.5.8 for $x_1$ shows that $x_1$ has an infinite number of terms below the finite value $\Lambda(x_1)$. So the truncation lemma, Lemma 4.5.8, is false for elements of $K'$, and the proofs of Lemma 4.5.9 and Theorem 4.5.14 do not apply over $K'$. We do not know if Theorem 4.5.14 holds over such a base.
- Rank more than one. The proofs use values in $\mathbb{R}$: the supremum $\Lambda$, the window $(\Lambda - \kappa, \Lambda)$ and the bounded part of the cone. They do not apply to a valuation of rank 2 or more.
- The global problem. The section works along one valuation, for one step, and the base must be an Abhyankar field $K_0$ of rank one with residue field $k$. It does not give a regular center of a step of degree $p$ over a general regular model, and it does not give the hypothesis $\mathrm{WLM}(n, k)$ of Section 4.3 or $\mathrm{FLM}(n, k)$ of Section 4.4.

Local uniformization in characteristic $p$ in transcendence degree 4 or more is open (Volume 9, Conjecture 2.3.1, for transcendence degree 4). Resolution of singularities in characteristic $p$ in dimension 4 or more is open. This section does not prove either of them. It proves one case of one step.

We state the status of the parts of this section in plain words.

- Lemmas 4.5.1 and 4.5.2 are standard facts. We prove them here in full.
- Theorems 4.5.3 and 4.5.4 and Lemma 4.5.5 are cited from [Kap42], [Kuh10] and [Kuh-book], with no proof.
- Corollary 4.5.6, Lemmas 4.5.7 to 4.5.11 and Proposition 4.5.12 are proved here in full. They are forms of known arguments of Kaplansky and of Hensel's lemma.
- Proposition 4.5.15 is proved here in full. Its proof is the proof of Volume 9, Theorem 3.23.15, for $m$ monomials and one more variable.
- Lemma 4.5.13, Theorem 4.5.14, Theorem 4.5.16 and Corollary 4.5.17 are a result of this project. The proofs are new, and they are not yet in a journal. An outside expert has not yet read them.
- The cone lemma (Lemma 4.5.13) is in Lean. No other statement of this section is in Lean.

### References and remarks

Pseudo Cauchy sequences and their types are from Kaplansky [Kap42]. The generalized stability theorem is [Kuh10, Theorem 1.1], and the facts on the henselization, on complete fields of rank one and on Hensel's lemma are in [Kuh-book]. Henselian rationality and its theorem over tame fields are in F.-V. Kuhlmann, Elimination of ramification II: henselian rationality, Israel J. Math. 234 (2019), arXiv 1701.05508, Theorems 1.2 and 1.3. The use of henselian rationality for local uniformization is in [KK09], and local uniformization of Abhyankar valuations is [KK05]. The reduction to steps of degree $p$ is from [Tem13]; see Sections 4.1 to 4.3. Volume 7, Sections 3.15 to 3.18, use pseudo Cauchy sequences of transcendental type and the generalized stability theorem in a related setting. The cone lemma uses only that the elements of the base have a finite number of terms below each value and that the exponents lie in a lattice. It does not use additive polynomials.
