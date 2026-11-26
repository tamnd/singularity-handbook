---
title: The Hilbert-Samuel polynomial and the multiplicity
nodes: [SG00000031, SG00000032, SG00000033, SG00000034, SG00000037]
sources: [AM69, Mat, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The Hilbert-Samuel polynomial and the multiplicity

In this section $R$ is a commutative ring, $I$ is an ideal of $R$ and $M$ is an $R$-module. We prove that the Hilbert-Samuel function $\chi_{I,M}$ of Section 3.1 is a polynomial in $n$ for large $n$, when $R$ is Noetherian, $M$ is finitely generated and $M/IM$ has finite length. Then we define the multiplicity and prove its first laws. The main tool is the theorem of Hilbert and Serre on graded modules. We follow [AM69, Chapter 11] and [Mat, Section 13].

### Functions that are eventually polynomial

For a function $f : \mathbb{N} \to \mathbb{Z}$, the *forward difference* is the function $\Delta f$ with $(\Delta f)(n) = f(n+1) - f(n)$. We write $\Delta^d$ for the $d$-th iterate of $\Delta$. A property of $n$ holds *for large $n$* if it holds for all $n \ge n_0$ for some $n_0$.

**Definition 3.3.1.** Let $d \in \mathbb{N}$. A function $f : \mathbb{N} \to \mathbb{Z}$ is *eventually polynomial of degree less than $d$* if there is a polynomial $P \in \mathbb{Q}[X]$ of degree less than $d$ such that $f(n) = P(n)$ for large $n$.

Lean: `Singularity.Algebra.IsEventuallyPolynomial`

The polynomial $P$ is unique, because two polynomials that agree at infinitely many points are equal. For $d = 0$ the condition says that $f(n) = 0$ for large $n$, because only the zero polynomial has degree less than $0$.

**Lemma 3.3.2.** A function $f : \mathbb{N} \to \mathbb{Z}$ is eventually polynomial of degree less than $d$ if and only if $(\Delta^d f)(n) = 0$ for large $n$.

Lean: `Singularity.Algebra.isEventuallyPolynomial_iff_fwdDiff`

*Proof.* For a polynomial $P$ we also write $(\Delta P)(X) = P(X+1) - P(X)$. If $P$ is constant, then $\Delta P = 0$. If $P$ has degree $e \ge 1$ and leading coefficient $a$, then $\Delta P$ has degree $e - 1$ and leading coefficient $ea$, by the binomial theorem. Thus $\Delta^d P = 0$ when $P$ has degree less than $d$. If $f(n) = P(n)$ for $n \ge n_0$, then $(\Delta^d f)(n) = (\Delta^d P)(n)$ for $n \ge n_0$, because $(\Delta^d f)(n)$ uses only the values $f(n), \dots, f(n+d)$. This proves the first direction.

We prove the converse by induction on $d$. For $d = 0$ there is nothing to prove. Assume the result for $d$, and let $(\Delta^{d+1} f)(n) = 0$ for large $n$. Then $\Delta^d(\Delta f)$ is $0$ for large $n$, so by induction there is $Q$ of degree less than $d$ with $(\Delta f)(n) = Q(n)$ for large $n$. The polynomials $\binom{X}{j} = X(X-1)\cdots(X-j+1)/j!$ for $j < d$ are a basis of the polynomials of degree less than $d$, and $\Delta \binom{X}{j+1} = \binom{X}{j}$ by the rule of Pascal. Thus there is a polynomial $P$ of degree less than $d+1$ with $\Delta P = Q$. Then $\Delta(f - P)$ is $0$ for large $n$, so $f - P$ is a constant $c$ for large $n$. The polynomial $P + c$ has degree less than $d+1$ and agrees with $f$ for large $n$. $\square$

**Corollary 3.3.3.** Let $f$ be eventually polynomial of degree less than $d$. Then the function $n \mapsto \sum_{k=0}^{n-1} f(k)$ is eventually polynomial of degree less than $d+1$.

Lean: `Singularity.Algebra.IsEventuallyPolynomial.sum_range`

*Proof.* Call the sum $g$. Then $\Delta g = f$, so $\Delta^{d+1} g = \Delta^d f$, and this is $0$ for large $n$ by Lemma 3.3.2. Lemma 3.3.2 again gives the result. $\square$

**Lemma 3.3.4.** Let $P \in \mathbb{Q}[X]$ have degree at most $d$, and let $f(n) = P(n)$ for large $n$. Then $(\Delta^d f)(n) = d! \cdot c_d$ for large $n$, where $c_d$ is the coefficient of $X^d$ in $P$.

Lean: `Singularity.Algebra.IsEventuallyPolynomial.eventually_fwdDiff_iter_eq`

*Proof.* Write $P = c_d X^d + P_1$ with $P_1$ of degree less than $d$. Then $\Delta^d P_1 = 0$ by the proof of Lemma 3.3.2. By the rule for the leading coefficient in that proof, $\Delta^d X^d$ is the constant $d!$. Thus $\Delta^d P = d! \cdot c_d$, and the values of $\Delta^d f$ and $\Delta^d P$ agree for large $n$. $\square$

### The theorem of Hilbert and Serre

Let $S$ be a commutative $R$-algebra and let $N$ be an $S$-module that is also an $R$-module, with the two actions compatible. A *grading* of $N$ is a family $(N_n)_{n \in \mathbb{N}}$ of $R$-submodules of $N$ such that $N = \bigoplus_n N_n$. Let $x_1, \dots, x_r \in S$. We say that the $x_i$ *have degree $1$* if $x_i N_n \subseteq N_{n+1}$ for each $i$ and $n$.

**Theorem 3.3.5 (Hilbert, Serre).** Let $S$ be generated as an $R$-algebra by $x_1, \dots, x_r$, and let $N = \bigoplus_n N_n$ be a graded $S$-module such that the $x_i$ have degree $1$. Assume that $N$ is a Noetherian $S$-module and that each $N_n$ has finite length over $R$. Then $n \mapsto \ell_R(N_n)$ is eventually polynomial of degree less than $r$.

Node: SG00000031 · Lean: `Singularity.Algebra.isEventuallyPolynomial_length_of_grading`

*Proof.* We use induction on $r$. Let $r = 0$. Then $S$ is the image of $R$, so each $R$-submodule of $N$ is an $S$-submodule. The submodules $N_0 \oplus \dots \oplus N_k$ make an increasing chain, and $N$ is Noetherian, so the chain is constant for $k \ge k_0$. Thus $N_n = 0$ for $n > k_0$, and the function is $0$ for large $n$.

Let $r \ge 1$, and let $x = x_r$. Multiplication by $x$ gives $R$-linear maps $x : N_n \to N_{n+1}$. Let $K_n$ be the kernel and let $C_{n+1} = N_{n+1}/xN_n$ be the cokernel, with $C_0 = N_0$. For each $n$ the sequence
$$0 \to K_n \to N_n \xrightarrow{x} N_{n+1} \to C_{n+1} \to 0$$
is exact, and all the terms have finite length. The additivity of length gives
$$\ell(N_{n+1}) - \ell(N_n) = \ell(C_{n+1}) - \ell(K_n).$$
The module $K = \bigoplus_n K_n$ is the kernel of $x$ on $N$, and $C = \bigoplus_n C_n$ is $N/xN$. Both are $S$-modules, $K$ as a submodule and $C$ as a quotient of $N$, so both are Noetherian. Both have gradings in which $x_1, \dots, x_{r-1}$ have degree $1$, and $x$ acts as $0$ on both. Thus the action of $S$ on $K$ and on $C$ factors through the subalgebra generated by $x_1, \dots, x_{r-1}$, and the submodules for this subalgebra are the same as the $S$-submodules. By induction, $\ell(K_n)$ and $\ell(C_n)$ are eventually polynomial of degree less than $r - 1$. Shifts and differences keep this property, so $\Delta \ell(N_n)$ is eventually polynomial of degree less than $r - 1$. By Lemma 3.3.2, $\ell(N_n)$ is eventually polynomial of degree less than $r$. $\square$

In the usual statement, $S = \bigoplus_n S_n$ is a graded Noetherian ring with $S_0$ Artinian and $S$ generated over $S_0$ by elements of $S_1$, and $N$ is a finitely generated graded $S$-module. The theorem of Hilbert and Serre says that the Poincaré series $\sum_n \ell(N_n) t^n$ has the form $f(t)/(1 - t)^r$ with $f \in \mathbb{Z}[t]$, where $r$ is the number of generators of $S$ over $S_0$ [AM69, Theorem 11.1], [Mat, Section 13], and the polynomial form of $\ell(N_n)$ follows from it [AM69, Corollary 11.2]. Theorem 3.3.5 contains this case. Our form does not need a grading on $S$, and this makes the application below simpler.

### The Hilbert-Samuel polynomial

The *associated graded module* of $M$ for $I$ is
$$\operatorname{gr}_I(M) = \bigoplus_{n \ge 0} I^n M / I^{n+1} M.$$
An element $a \in I$ gives $R$-linear maps $I^n M/I^{n+1} M \to I^{n+1} M/I^{n+2} M$, the multiplication by $a$, so $a$ acts on $\operatorname{gr}_I(M)$ as an endomorphism of degree $1$. These endomorphisms commute.

**Theorem 3.3.6.** Let $R$ be a Noetherian ring, let $M$ be a finitely generated $R$-module and let $I = (x_1, \dots, x_r)$. Assume that $M/IM$ has finite length. Then there is a polynomial $P \in \mathbb{Q}[X]$ of degree at most $r$ such that $\chi_{I,M}(n) = P(n)$ for large $n$. In particular, each value $\chi_{I,M}(n)$ is finite.

Node: SG00000032 · Lean: `Singularity.Algebra.exists_hilbertSamuel_polynomial`

*Proof.* First we show that each piece $G_n = I^n M/I^{n+1} M$ has finite length. The module $I^n M$ is generated by the elements $x^\alpha m$, where $x^\alpha$ runs through the monomials of degree $n$ in the $x_i$ and $m \in M$. Thus the map $\bigoplus_\alpha M \to G_n$ that sends $(m_\alpha)$ to the class of $\sum_\alpha x^\alpha m_\alpha$ is surjective. It is $0$ on $\bigoplus_\alpha IM$, so $G_n$ is a quotient of a finite direct sum of copies of $M/IM$. Thus $G_n$ has finite length. By Lemma 3.1.2 and induction on $n$,
$$\chi_{I,M}(n) = \sum_{k=0}^{n-1} \ell(G_k),$$
so each value of $\chi_{I,M}$ is finite.

Let $S$ be the $R$-algebra of endomorphisms of $G = \operatorname{gr}_I(M)$ that is generated by the actions $\xi_1, \dots, \xi_r$ of $x_1, \dots, x_r$. It is commutative, and the $\xi_i$ have degree $1$. Let $m_1, \dots, m_s$ generate $M$. Then $G$ is generated as an $S$-module by the classes of the $m_j$ in $G_0 = M/IM$, because $G_n$ is generated by the classes of the elements $x^\alpha m_j$. The algebra $S$ is a quotient of the polynomial ring $R[X_1, \dots, X_r]$, so it is Noetherian by the basis theorem of Hilbert. Thus $G$ is a finitely generated module over a Noetherian ring, and it is Noetherian. Theorem 3.3.5 says that $n \mapsto \ell(G_n)$ is eventually polynomial of degree less than $r$. By Corollary 3.3.3, $\chi_{I,M}$ is eventually polynomial of degree less than $r + 1$. $\square$

When $(R, \mathfrak{m})$ is a Noetherian local ring and $I$ is $\mathfrak{m}$-primary, $M/IM$ has finite length by Theorem 3.1.5, so Theorem 3.3.6 applies. This is the theorem of Hilbert and Samuel [AM69, Proposition 11.4]. The degree of $P$ is at most $r$ for each set of $r$ generators of $I$. For $M = R$ the degree is the dimension of $R$ [AM69, Theorem 11.14]. This edition does not prove the equality with the dimension, and it has no Lean proof yet.

### The multiplicity

The polynomial of Theorem 3.3.6 has rational coefficients, but the numbers $d! \cdot c_d$ of Lemma 3.3.4 are integers, because they are values of $\Delta^d \chi_{I,M}$. We use them to define the multiplicity. Since the degree is not yet known to be the dimension, we keep the degree $d$ as a parameter.

**Definition 3.3.7.** Let $d \in \mathbb{N}$, and assume that $\Delta^d \chi_{I,M}$ is constant for large $n$, with value $c$. The *multiplicity* of $M$ for $I$ in degree $d$ is $e_d(I, M) = c$. When $(R, \mathfrak{m})$ is local of dimension $d$ we write $e(I, M) = e_d(I, M)$ and $e(R) = e_d(\mathfrak{m}, R)$.

Node: SG00000033 · Lean: `Singularity.Algebra.samuelMultiplicity`

In the situation of Theorem 3.3.6, Lemma 3.3.4 shows that $\Delta^d \chi_{I,M}$ is constant for large $n$ for each $d \ge r$, and that $e_d(I, M) = d! \cdot c_d$, where $c_d$ is the coefficient of $X^d$ in $P$. The value is not negative, because $P(n) = \chi_{I,M}(n) \ge 0$ for large $n$: if $P$ has degree $d$, then its leading coefficient is positive, and if $P$ has smaller degree, then $c_d = 0$.

**Proposition 3.3.8.** Let $R$ be a Noetherian ring, let $M$ be a finitely generated $R$-module, and let $I$ be an ideal with $r$ generators such that $M/IM$ has finite length. Let $P$ be the polynomial of Theorem 3.3.6.

1. If $d > \deg P$, then $e_d(I, M) = 0$.
2. If $R$ is local with maximal ideal $\mathfrak{m}$, $I \subseteq \mathfrak{m}$ and $M \neq 0$, then $e_d(I, M) > 0$ for $d = \deg P$.
3. Let $J \supseteq I$ be an ideal with $s$ generators. Then $e_d(J, M) \le e_d(I, M)$ for each $d \ge \max(r, s)$.

Node: SG00000034 · Lean: `Singularity.Algebra.samuelMultiplicity_pos`

*Proof.* Part 1 is Lemma 3.3.4, because $c_d = 0$ for $d > \deg P$. For part 2, the module $M/IM$ is not $0$ by the lemma of Nakayama, because $I \subseteq \mathfrak{m}$ and $M \neq 0$ is finitely generated [AM69, Proposition 2.6]. Thus $\chi_{I,M}(1) \ge 1$. The function $\chi_{I,M}$ is monotone by Proposition 3.1.3, so $P(n) \ge 1$ for large $n$, and $P \neq 0$. A nonzero polynomial with $P(n) \ge 0$ for large $n$ has a positive leading coefficient. Thus $e_d(I, M) = d! \cdot c_d > 0$ for $d = \deg P$. For part 3, $J^n M \supseteq I^n M$, so $\chi_{J,M}(n) \le \chi_{I,M}(n)$ for each $n$ by Lemma 3.1.2. Let $Q$ be the polynomial of $J$. Then $P - Q$ has degree at most $d$ and $(P - Q)(n) \ge 0$ for large $n$. Thus its coefficient of $X^d$ is not negative: it is $0$ if the degree is less than $d$, and it is the leading coefficient otherwise. This gives $e_d(J, M) \le e_d(I, M)$. $\square$

The Lean names of parts 1 and 3 are `Singularity.Algebra.samuelMultiplicity_eq_zero_of_natDegree_lt` and `Singularity.Algebra.samuelMultiplicity_anti`.

### Examples

**Example 3.3.9.** Let $K$ be a field and $\mathfrak{m} = 0$. Then $\chi_K(0) = 0$ and $\chi_K(n) = \ell(K) = 1$ for $n \ge 1$. So $P = 1$, $\deg P = 0 = \dim K$ and $e(K) = 1$.

Lean: `Singularity.Algebra.samuelMultiplicity_field`

**Example 3.3.10.** Let $R$ be a discrete valuation ring with uniformizer $t$, so $\mathfrak{m} = (t)$. The ideals of $R$ that contain $t^n$ are $(t^k)$ for $0 \le k \le n$, and they make one chain. Thus $\chi_R(n) = \ell(R/t^n R) = n$. So $P = X$, $\deg P = 1 = \dim R$ and $e(R) = 1$.

Lean: `Singularity.Algebra.samuelMultiplicity_dvr`

### Regular local rings

Examples 3.3.9 and 3.3.10 compute the multiplicity of a regular local ring of dimension $0$ and $1$. Now we compute it for each dimension. The proof uses a regular sequence that generates the maximal ideal (Theorem 1.5.3), and it does not use the associated graded ring.

**Lemma 3.3.11.** Let $(R, \mathfrak{m})$ be a Noetherian local ring, let $J$ be an ideal that is generated by a regular sequence in $\mathfrak{m}$, and let $z \in R$ be a nonzerodivisor on $R/J$. Then $z$ is a nonzerodivisor on $R/J^n$ for each $n \ge 1$.

Lean: `Singularity.Algebra.mem_pow_of_mul_mem_of_isWeaklyRegular`

*Proof.* Since $J$ is generated by a regular sequence, $J^k/J^{k+1}$ is a free module over $R/J$ for each $k$ [Mat, Section 16]. Thus $z$ is a nonzerodivisor on each $J^k/J^{k+1}$. We use induction on $n$. The case $n = 1$ is the hypothesis. Assume that $zy \in J^{n+1}$. Then $zy \in J^n$, so $y \in J^n$ by induction. The image of $y$ in $J^n/J^{n+1}$ is killed by $z$, so it is $0$, and $y \in J^{n+1}$. $\square$

**Lemma 3.3.12.** Let $(R, \mathfrak{m})$ be a Noetherian local ring, and assume that $\mathfrak{m}$ is generated by a regular sequence $a, a_2, \dots, a_d$. Then $(\mathfrak{m}^{n+1} : a) = \mathfrak{m}^n$ for each $n \ge 0$. That is, if $au \in \mathfrak{m}^{n+1}$, then $u \in \mathfrak{m}^n$.

Lean: `Singularity.Algebra.mem_maximalIdeal_pow_of_mul_mem`

*Proof.* Let $J = (a_2, \dots, a_d)$. In a Noetherian local ring, a permutation of a regular sequence in $\mathfrak{m}$ is again a regular sequence [Mat, Section 16]. So $a_2, \dots, a_d, a$ is a regular sequence, $J$ is generated by a regular sequence, and $a$ is a nonzerodivisor on $R/J$. Since $\mathfrak{m} = aR + J$, we have $\mathfrak{m}^{n+1} = J^{n+1} + a\mathfrak{m}^n$. Assume that $au \in \mathfrak{m}^{n+1}$, and write $au = j + av$ with $j \in J^{n+1}$ and $v \in \mathfrak{m}^n$. Then $a(u - v) \in J^{n+1}$. By Lemma 3.3.11, $u - v \in J^{n+1} \subseteq \mathfrak{m}^n$. Thus $u \in \mathfrak{m}^n$. The other inclusion is clear. $\square$

**Theorem 3.3.13.** Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$. Then $\chi_R(n+1) = \ell(R/\mathfrak{m}^{n+1}) = \binom{n+d}{d}$ for each $n \ge 0$, and $e(R) = e_d(\mathfrak{m}, R) = 1$. If $d \ge 1$, then $\ell(\mathfrak{m}^n/\mathfrak{m}^{n+1}) = \binom{n+d-1}{d-1}$.

Node: SG00000037 · Lean: `Singularity.Algebra.samuelMultiplicity_regular`, `Singularity.Algebra.hilbertSamuel_succ_eq_choose`, `Singularity.Algebra.length_grPiece_eq_choose`

*Proof.* We prove the formula for $\chi_R$ for each Noetherian local ring whose maximal ideal is generated by a regular sequence of length $d$. A regular local ring has this property by Theorem 1.5.3. We use induction on $d$. If $d = 0$, then $\mathfrak{m} = 0$, $R$ is a field, and $\chi_R(n+1) = 1$.

Let $d \ge 1$, and let $a, a_2, \dots, a_d$ be a regular sequence that generates $\mathfrak{m}$. Let $\bar{R} = R/aR$. Then $\bar{R}$ is a Noetherian local ring, and its maximal ideal $\bar{\mathfrak{m}}$ is generated by the images of $a_2, \dots, a_d$, which are a regular sequence of length $d - 1$. Multiplication by $a$ gives an exact sequence
$$0 \to R/\mathfrak{m}^n \xrightarrow{\ a\ } R/\mathfrak{m}^{n+1} \to R/(aR + \mathfrak{m}^{n+1}) \to 0.$$
The first map is injective by Lemma 3.3.12. The third module is $\bar{R}/\bar{\mathfrak{m}}^{n+1}$. Lengths are additive on exact sequences, so
$$\chi_R(n+1) = \chi_R(n) + \chi_{\bar{R}}(n+1).$$
By induction, $\chi_{\bar{R}}(k+1) = \binom{k+d-1}{d-1}$. Since $\chi_R(0) = 0$, we get
$$\chi_R(n+1) = \sum_{k=0}^{n} \binom{k+d-1}{d-1} = \binom{n+d}{d}.$$
The last equality is the usual sum of binomial coefficients, and it follows from Pascal's rule by induction on $n$.

For $d \ge 1$, the exact sequence $0 \to \mathfrak{m}^n/\mathfrak{m}^{n+1} \to R/\mathfrak{m}^{n+1} \to R/\mathfrak{m}^n \to 0$ gives $\ell(\mathfrak{m}^n/\mathfrak{m}^{n+1}) = \binom{n+d}{d} - \binom{n+d-1}{d} = \binom{n+d-1}{d-1}$. Finally, $\chi_R(n) = \binom{n+d-1}{d}$ for each $n \ge 1$, and $\Delta \binom{n+c}{k} = \binom{n+c}{k-1}$ for $k \ge 1$ by Pascal's rule. Thus $\Delta^d \chi_R$ is the constant function $\binom{n+d-1}{0} = 1$, and $e_d(\mathfrak{m}, R) = 1$. $\square$

The polynomial $P(X) = \binom{X+d-1}{d}$ has degree $d = \dim R$ and leading coefficient $1/d!$, as Lemma 3.3.4 and Theorem 3.3.13 say. For the local ring of affine space at the origin, this is the count of the monomials of degree less than $n$ in $d$ variables.

**Remark 3.3.14.** The converse is a theorem of Nagata: an unmixed Noetherian local ring $R$ with $e(R) = 1$ is regular [Nag62, Section 40]. Without the hypothesis the converse fails. For example, let $R = k[x, y]_{(x, y)}/(x^2, xy)$, the ring of Example 1.5.2. Then $\dim R = 1$ and $e(R) = 1$, but $R$ is not regular. The theorem of Nagata is not in the Lean library.

Lean: none yet

### Hypersurfaces

For a hypersurface, the Hilbert-Samuel function depends only on the dimension and on the order of the equation. So the multiplicity of a hypersurface is the order of its equation (Section 3.2). We use the notation $\operatorname{in}(a)$ of Section 1.10 for the initial form of an element $a \ne 0$ of a regular local ring, and the convention $\binom{m}{n} = 0$ for $0 \le m < n$.

**Proposition 3.3.15.** Let $(S, \mathfrak{m})$ be a regular local ring of dimension $n \ge 1$, let $f \in \mathfrak{m}^d \setminus \mathfrak{m}^{d+1}$ with $d \ge 1$, and let $R = S/(f)$. Then for each $N \ge 0$,
$$\chi_R(N) = \binom{N + n - 1}{n} - \binom{N - d + n - 1}{n} \quad \text{if } N \ge d, \qquad \chi_R(N) = \binom{N + n - 1}{n} \quad \text{if } N \le d.$$
The ring $R$ has dimension $n - 1$, and $e(R) = e_{n-1}(\mathfrak{m}R, R) = d$.

Lean: none yet

*Proof.* The maximal ideal of $R$ is $\mathfrak{m}R$, and $R/\mathfrak{m}^N R = S/(\mathfrak{m}^N + fS)$. First we show that $(\mathfrak{m}^N : f) = \mathfrak{m}^{N-d}$ for $N \ge d$. If $g \in \mathfrak{m}^{N-d}$, then $fg \in \mathfrak{m}^N$. Conversely, let $g \ne 0$ with $fg \in \mathfrak{m}^N$, and let $g \in \mathfrak{m}^i \setminus \mathfrak{m}^{i+1}$. The ring $\operatorname{gr}(S)$ is a domain (Proposition 1.10.1), so $\operatorname{in}(fg) = \operatorname{in}(f) \operatorname{in}(g)$ is a nonzero element of degree $d + i$. Thus $fg \notin \mathfrak{m}^{d+i+1}$, so $N \le d + i$ and $g \in \mathfrak{m}^{N-d}$. For $N \le d$ we have $f \in \mathfrak{m}^N$, so $(\mathfrak{m}^N : f) = S$.

Multiplication by $f$ gives an exact sequence
$$0 \to S/(\mathfrak{m}^N : f) \xrightarrow{\ f\ } S/\mathfrak{m}^N \to S/(\mathfrak{m}^N + fS) \to 0.$$
By Theorem 3.3.13, $\ell(S/\mathfrak{m}^j) = \binom{j + n - 1}{n}$ for each $j \ge 0$. The additivity of length gives the formula for $\chi_R$. The ring $S$ is a domain (Theorem 1.3.3) and $f \ne 0$, so $\dim R = n - 1$ by Proposition 1.2.10.

For the multiplicity, apply $\Delta$ to the formula for $N \ge d$. Pascal's rule gives $\Delta \binom{N + c}{j} = \binom{N + c}{j - 1}$ for $j \ge 1$ and $N + c \ge 0$. After $n - 1$ steps,
$$(\Delta^{n-1} \chi_R)(N) = \binom{N + n - 1}{1} - \binom{N - d + n - 1}{1} = d$$
for $N \ge d$. By Definition 3.3.7, $e_{n-1}(\mathfrak{m}R, R) = d$. $\square$

With Proposition 1.2.10, this gives a special case of the theorem of Nagata in Remark 3.3.14: a hypersurface $R = S/(f)$ is regular if and only if $e(R) = 1$. Indeed, both conditions say that $f \notin \mathfrak{m}^2$.

**Example 3.3.16.** Let $k$ be a field and let $S$ be the local ring of $\mathbb{A}^n_k$ at the origin. For a polynomial $f$ with $f(0) = 0$, the order $d$ is the smallest degree of a monomial of $f$ (Example 3.2.6). We list some values of Proposition 3.3.15, and we checked each of them by a direct count of monomials in $k[x_1, \dots, x_n]/(\mathfrak{n}^N + (f))$.

*Plane curves*, $n = 2$. Then $\chi_R(N) = \binom{N+1}{2} - \binom{N - d + 1}{2} = dN - \binom{d}{2}$ for $N \ge d - 1$. The cusp $y^2 - x^3$ and the node $y^2 - x^2 - x^3$ both have $\chi_R(N) = 2N - 1$ for $N \ge 1$ and $e(R) = 2$. So the multiplicity does not separate the cusp from the node. The curves $x^3 + y^5$ and $x^2 y + y^4$ have $\chi_R(N) = 3N - 3$ for $N \ge 2$ and $e(R) = 3$. More generally, $x^a + y^b$ with $1 \le a \le b$ has multiplicity $a$.

*Surfaces*, $n = 3$. Then $d = 2$ gives $\chi_R(N) = \binom{N+2}{3} - \binom{N}{3} = N^2$ for $N \ge 2$, and $e(R) = 2$. This holds for the cone $xy - z^2$, for each surface $A_m$ given by $xy - z^{m+1}$ with $m \ge 1$, and for the Whitney umbrella $x^2 - y^2 z$, whose order is $2$ because of the monomial $x^2$. The cubic cone $x^3 + y^3 + z^3$ has $d = 3$, and its values $\chi_R(1), \dots, \chi_R(6)$ are $1, 4, 10, 19, 31, 46$, with $\Delta^2 \chi_R(N) = 3$ for $N \ge 3$.

The multiplicity is a coarse invariant. The surfaces $A_m$ all have the same Hilbert-Samuel function, but they behave differently under blowup. One blowup of the vertex resolves $A_1$ (Example 1.10.8). For $m \ge 3$, let $a = x/z$ and $b = y/z$. Then $ab = z^{m-1}$ in the chart for $z$ of the blowup of $A_m$ at the vertex. The ring $k[z, a, b]/(ab - z^{m-1})$ is a domain of dimension $2$ that maps onto this chart, and the chart is a domain of dimension $2$, so the map is an isomorphism. By Proposition 1.2.10 this chart has a singular point at the origin, of type $A_{m-2}$. The resolution algorithms use the order with finer invariants, which Volume 3 and Volume 4 develop.

Lean: none yet

### The Lean proof

The results of this section are in `Singularity/Algebra/FiniteDifference.lean`, `Singularity/Algebra/HilbertSerre.lean`, `Singularity/Algebra/Multiplicity.lean` and `Singularity/Algebra/MultiplicityRegular.lean`. The forward difference is `fwdDiff` of Mathlib, with the notation `Δ_[1]`. In Lean, the Hilbert-Samuel function has values in $\mathbb{N} \cup \{\infty\}$, so the file `Multiplicity.lean` uses the integer function `hilbertSamuelInt`, and `samuelMultiplicity I M d` is the eventual value of `Δ_[1]^[d]` applied to it.

The proof of Theorem 3.3.5 does not use graded rings. A grading of $N$ is a family `𝒩 : ℕ → Submodule R N` with `iSupIndep 𝒩` and `⨆ n, 𝒩 n = ⊤`. The kernel and the cokernel of $x_r$ are the gradings `kerGrading` and `cokerGrading`. For Theorem 3.3.6 the associated graded module is `GrMod I M`, the direct sum of the modules `grPiece I M n`, and the algebra $S$ of the proof is `grAlgebra`, a subalgebra of the endomorphisms of `GrMod I M`. In `MultiplicityRegular.lean`, the induction of Theorem 3.3.13 is stated for each Noetherian local ring whose maximal ideal is generated by a weakly regular sequence (`Singularity.Algebra.hilbertSamuel_succ_of_isWeaklyRegular`), so that the induction hypothesis applies to $R/aR$. The length of $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ is a length over $R$. It is equal to the dimension over the residue field. All the theorems of this section use only the three standard axioms of Lean.

### Notes and references

The theorem of Hilbert and Serre on the Poincaré series is [AM69, Theorem 11.1] and [Mat, Section 13]. Hilbert proved the polynomial nature of the Hilbert function of a graded module over a polynomial ring, and Serre gave the form for modules over graded Noetherian rings. Samuel introduced the polynomial $\chi_{I,M}$ and the multiplicity for local rings. The proof with the kernel and the cokernel is the proof in [AM69]. The definition of the multiplicity by the forward difference is equivalent to the usual one with the leading coefficient, by Lemma 3.3.4. Matsumura treats the multiplicity in [Mat, Section 14], with the formula $e(R) = 1$ for a regular local ring. The usual proof of Theorem 3.3.13 shows that $\operatorname{gr}_\mathfrak{m}(R)$ is a polynomial ring over the residue field [AM69, Theorem 11.22]. Our proof uses only the colon ideal of Lemma 3.3.12, which is a form of the quasi-regularity of a regular sequence [Mat, Section 16].
