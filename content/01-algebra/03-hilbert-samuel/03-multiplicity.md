---
title: The Hilbert-Samuel polynomial and the multiplicity
nodes: [SG00000031, SG00000032, SG00000033, SG00000034]
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

In the usual statement, $S = \bigoplus_n S_n$ is a graded Noetherian ring with $S_0$ Artinian and $S$ generated over $S_0$ by elements of $S_1$, and $N$ is a finitely generated graded $S$-module [AM69, Theorem 11.1], [Mat, Theorem 13.2]. Theorem 3.3.5 contains this case. Our form does not need a grading on $S$, and this makes the application below simpler.

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

**Remark 3.3.11.** Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$ with residue field $\kappa$. Then $\operatorname{gr}_\mathfrak{m}(R)$ is a polynomial ring over $\kappa$ in $d$ variables [AM69, Theorem 11.22], so the computation of Example 3.1.6 gives $\chi_R(n) = \binom{n+d-1}{d}$ and $e(R) = 1$. Examples 3.3.9 and 3.3.10 are the cases $d = 0$ and $d = 1$. Conversely, an unmixed local ring with $e(R) = 1$ is regular [Nag62, Section 40]. The general case $e(R) = 1$ for a regular local ring has no Lean proof yet.

Lean: none yet

### The Lean proof

The results of this section are in `Singularity/Algebra/FiniteDifference.lean`, `Singularity/Algebra/HilbertSerre.lean` and `Singularity/Algebra/Multiplicity.lean`. The forward difference is `fwdDiff` of Mathlib, with the notation `Δ_[1]`. In Lean, the Hilbert-Samuel function has values in $\mathbb{N} \cup \{\infty\}$, so the file `Multiplicity.lean` uses the integer function `hilbertSamuelInt`, and `samuelMultiplicity I M d` is the eventual value of `Δ_[1]^[d]` applied to it.

The proof of Theorem 3.3.5 does not use graded rings. A grading of $N$ is a family `𝒩 : ℕ → Submodule R N` with `iSupIndep 𝒩` and `⨆ n, 𝒩 n = ⊤`. The kernel and the cokernel of $x_r$ are the gradings `kerGrading` and `cokerGrading`. For Theorem 3.3.6 the associated graded module is `GrMod I M`, the direct sum of the modules `grPiece I M n`, and the algebra $S$ of the proof is `grAlgebra`, a subalgebra of the endomorphisms of `GrMod I M`. All the theorems of this section use only the three standard axioms of Lean.

### Notes and references

The theorem of Hilbert and Serre is [AM69, Theorem 11.1] and [Mat, Theorem 13.2]. Hilbert proved the polynomial nature of the Hilbert function of a graded module over a polynomial ring, and Serre gave the form for modules over graded Noetherian rings. Samuel introduced the polynomial $\chi_{I,M}$ and the multiplicity for local rings. The proof with the kernel and the cokernel is the proof in [AM69]. The definition of the multiplicity by the forward difference is equivalent to the usual one with the leading coefficient, by Lemma 3.3.4. Matsumura treats the multiplicity in [Mat, Section 14], with the formula $e(R) = 1$ for a regular local ring.
