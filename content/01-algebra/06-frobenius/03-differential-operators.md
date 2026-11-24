---
title: Hasse-Schmidt derivations and differential operators
nodes: [SG0000000W, SG0000004N]
sources: [HSDer, EGA4, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Hasse-Schmidt derivations and differential operators

In characteristic $0$, the order of a polynomial $f$ at the origin is the least $n$ such that some derivative $\partial^\beta f$ with $|\beta| = n$ does not vanish at the origin. In characteristic $p$ this fails: the polynomial $x^p$ has order $p$, but all its derivatives vanish. The cause is the factor $n!$ in $\partial^n(x^n) = n!$. The remedy is to divide by $n!$ before the reduction modulo $p$. This gives the Hasse derivatives, and more generally the Hasse-Schmidt derivations and the differential operators of Grothendieck.

In this section $k$ is a ring and $A$ is a $k$-algebra. For $a \in A$ we also write $a$ for the map $A \to A$ of multiplication by $a$.

### Hasse-Schmidt derivations

**Definition 6.3.1.** A *Hasse-Schmidt derivation* of $A$ over $k$ is a sequence $D = (D_0, D_1, D_2, \dots)$ of $k$-linear maps $A \to A$ such that $D_0$ is the identity and
$$D_n(ab) = \sum_{i + j = n} D_i(a) D_j(b) \quad \text{for each } n \text{ and all } a, b \in A.$$
In an equivalent form, the map $A \to A[[t]]$, $a \mapsto \sum_n D_n(a) t^n$, is a homomorphism of $k$-algebras whose reduction modulo $t$ is the identity.

Node: SG0000000W · Lean: `Singularity.Algebra.MvHasse.hasseDeriv` (the operators $\partial^{(\beta)}$ of a polynomial ring below, not the general notion)

The rule for $n = 1$ says that $D_1$ is a $k$-derivation. If $\mathbb{Q} \subseteq k$ and $\partial$ is a $k$-derivation of $A$, then $D_n = \partial^n / n!$ is a Hasse-Schmidt derivation, by the Leibniz rule $\partial^n(ab) = \sum_i \binom{n}{i} \partial^i(a) \partial^{n-i}(b)$. In characteristic $p$, a derivation need not extend to a Hasse-Schmidt derivation, and a Hasse-Schmidt derivation contains more information than its first term.

**Proposition 6.3.2 (Hasse derivatives).** Let $A = k[x]$. Define $k$-linear maps $D_n : A \to A$ by
$$f(x + t) = \sum_{n \ge 0} D_n(f) \, t^n \quad \text{in } A[t].$$
Then $(D_n)$ is a Hasse-Schmidt derivation of $A$ over $k$, $D_1 = d/dx$, and
$$D_n(x^m) = \binom{m}{n} x^{m - n}$$
for all $m, n$, where $\binom{m}{n} = 0$ for $n > m$. In particular, if $k$ has characteristic $p$, then $D_p(x^p) = 1$, while $(d/dx)^p = 0$.

Lean: `Polynomial.hasseDeriv`, `Polynomial.hasseDeriv_monomial`, `Polynomial.hasseDeriv_one` and `Polynomial.hasseDeriv_mul` in Mathlib, and `Singularity.Algebra.MvHasse.uniqueAlgEquiv_hasseDeriv` (the agreement with the operators in several variables)

*Proof.* The map $A \to A[t]$, $f \mapsto f(x + t)$, is a homomorphism of $k$-algebras, and its reduction modulo $t$ is the identity. So $(D_n)$ is a Hasse-Schmidt derivation. The binomial theorem gives $(x + t)^m = \sum_n \binom{m}{n} x^{m-n} t^n$. For $n = 1$ this is $D_1(x^m) = m x^{m-1}$. In characteristic $p$, $(d/dx)^p (x^m) = m(m-1)\cdots(m-p+1) x^{m-p}$, and the product of $p$ consecutive integers is divisible by $p$. $\square$

For $A = k[x_1, \dots, x_n]$ we define the operators $\partial^{(\beta)}$, $\beta \in \mathbb{N}^n$, by $f(x_1 + t_1, \dots, x_n + t_n) = \sum_\beta \partial^{(\beta)}(f) \, t^\beta$. Then $\partial^{(\beta)}$ is the composite of the Hasse derivatives $D_{\beta_i}$ in the variables $x_i$, and $\partial^{(\beta)}(x^\alpha) = \binom{\alpha}{\beta} x^{\alpha - \beta}$, with $\binom{\alpha}{\beta} = \prod_i \binom{\alpha_i}{\beta_i}$. If $\mathbb{Q} \subseteq k$, then $\partial^{(\beta)} = \partial^\beta / \beta!$.

The operators $\partial^{(\beta)}$ have the same formal properties as the Hasse derivatives. The map $f \mapsto f(x + t)$ is a homomorphism of rings, so the comparison of the coefficients of $t^\beta$ in $(fg)(x + t) = f(x + t) \, g(x + t)$ gives the Leibniz rule
$$\partial^{(\beta)}(fg) = \sum_{\gamma + \delta = \beta} \partial^{(\gamma)}(f) \, \partial^{(\delta)}(g).$$
On a monomial, $\binom{\alpha}{\beta} \binom{\alpha - \beta}{\gamma} = \binom{\beta + \gamma}{\beta} \binom{\alpha}{\beta + \gamma}$ in each coordinate, and this gives the composition rule $\partial^{(\gamma)} \partial^{(\beta)} = \binom{\beta + \gamma}{\beta} \partial^{(\beta + \gamma)}$. In particular, $\partial^{(e_i)} = \partial/\partial x_i$, and in characteristic $p$ the composite of $p$ copies of $\partial^{(e_i)}$ is $p! \, \partial^{(p e_i)} = 0$. These statements hold over each commutative ring $k$.

Lean: `Singularity.Algebra.MvHasse.hasseDeriv_monomial`, `Singularity.Algebra.MvHasse.hasseDeriv_mul`, `Singularity.Algebra.MvHasse.hasseDeriv_comp`, `Singularity.Algebra.MvHasse.hasseDeriv_single_one` and `Singularity.Algebra.MvHasse.taylor_eq_sum`

### Differential operators

**Definition 6.3.3.** Let $D : A \to A$ be a $k$-linear map. Then $D$ is a *differential operator of order at most $0$* if it is $A$-linear. For $n \ge 1$, $D$ is a *differential operator of order at most $n$* if, for each $a \in A$, the commutator $[D, a] = D \circ a - a \circ D$ is a differential operator of order at most $n - 1$. We write $\mathcal{D}^n_{A/k}$ for the set of these operators, and $\mathcal{D}_{A/k} = \bigcup_n \mathcal{D}^n_{A/k}$.

An operator of order at most $0$ is the multiplication by $D(1)$. A $k$-derivation $D$ has order at most $1$, because $[D, a]$ is the multiplication by $D(a)$.

**Lemma 6.3.4.** Let $D \in \mathcal{D}^m_{A/k}$ and $E \in \mathcal{D}^n_{A/k}$, and let $c \in A$. Then $D + E \in \mathcal{D}^{\max(m, n)}_{A/k}$, $cD \in \mathcal{D}^m_{A/k}$ and $D \circ E \in \mathcal{D}^{m+n}_{A/k}$. If $(D_n)$ is a Hasse-Schmidt derivation of $A$ over $k$, then $D_n \in \mathcal{D}^n_{A/k}$ for each $n$. In particular, $\partial^{(\beta)} \in \mathcal{D}^{|\beta|}_{A/k}$ for $A = k[x_1, \dots, x_n]$.

Lean: none yet

*Proof.* The first two statements follow by induction on the order from $[D + E, a] = [D, a] + [E, a]$ and $[cD, a] = c[D, a]$. The third follows by induction on $m + n$ from $[D \circ E, a] = D \circ [E, a] + [D, a] \circ E$. For a Hasse-Schmidt derivation and $a, b \in A$,
$$[D_n, a](b) = D_n(ab) - a D_n(b) = \sum_{i=1}^{n} D_i(a) D_{n-i}(b).$$
So $[D_n, a] = \sum_{i=1}^n D_i(a) \, D_{n-i}$. By induction on $n$ and the first two statements, this has order at most $n - 1$. For $n = 0$, $D_0$ is the identity, which is $A$-linear. The operator $\partial^{(\beta)}$ is a composite of Hasse derivatives $D_{\beta_i}$, so the third statement gives the last claim. $\square$

**Lemma 6.3.5.** Let $A$ have characteristic $p$, let $q = p^e$ and let $D \in \mathcal{D}^n_{A/k}$ with $n < q$. Then $D$ is linear over the subring $k[A^q]$ of $A$ that $k$ and the $q$-th powers generate.

Lean: none yet

*Proof.* For $a \in A$, let $\lambda_a$ and $\rho_a$ be the maps $E \mapsto a \circ E$ and $E \mapsto E \circ a$ on the group $\operatorname{End}_k(A)$. They commute, and $[E, a] = (\rho_a - \lambda_a)(E)$. The group $\operatorname{End}_k(A)$ has characteristic $p$, so $(\rho_a - \lambda_a)^q = \rho_a^q - \lambda_a^q = \rho_{a^q} - \lambda_{a^q}$. By induction on the order, applying $\rho_a - \lambda_a$ to $D$ a total of $n + 1$ times gives $0$. Since $q \ge n + 1$, we get $[D, a^q] = (\rho_a - \lambda_a)^q(D) = 0$. So $D$ commutes with the multiplication by each $q$-th power. It is $k$-linear, so it is $k[A^q]$-linear. $\square$

### The differential operators of a polynomial ring

**Theorem 6.3.6.** Let $k$ be a field of characteristic $p$, let $A = k[x_1, \dots, x_n]$, let $q = p^e$ and let $A_e = k[x_1^q, \dots, x_n^q]$. Then
$$\operatorname{End}_{A_e}(A) = \bigoplus_{\beta \in [0, q)^n} A \, \partial^{(\beta)},$$
and the operators $\partial^{(\beta)}$ with $\beta \in [0, q)^n$ are a basis of this $A$-module. Also,
$$\mathcal{D}_{A/k} = \bigcup_{e \ge 1} \operatorname{End}_{A_e}(A) = \bigoplus_{\beta \in \mathbb{N}^n} A \, \partial^{(\beta)}.$$

Lean: `Singularity.Algebra.MvHasse.hasseDeriv_expand_mul` (only the first step of the proof: each $\partial^{(\beta)}$ with $\beta \in [0, q)^n$ is $A_e$-linear)

*Proof.* Write $[0, q)^n$ for the set of the exponents $\beta$ with $0 \le \beta_i < q$. First, the operators $\partial^{(\beta)}$ with $\beta \in [0, q)^n$ are $A_e$-linear. In one variable, $(x + t)^{qm} = (x^q + t^q)^m$, so the series $x^{qm}$ has no terms $t^j$ with $0 < j < q$ in its expansion. The rule of Definition 6.3.1 then gives $D_j(x^{qm} g) = x^{qm} D_j(g)$ for $j < q$. The same holds for $\partial^{(\beta)}$ in several variables, one variable at a time.

By Proposition 6.1.5, $A$ is a free $A_e$-module with basis $x^\alpha$, $\alpha \in [0, q)^n$. So the map $E \mapsto (E(x^\alpha))_\alpha$ is an isomorphism of $A$-modules from $\operatorname{End}_{A_e}(A)$ onto $A^{q^n}$. Consider the $A$-linear map from $\bigoplus_\beta A\,\partial^{(\beta)}$ (the free module on symbols) to $A^{q^n}$ that sends $\sum_\beta c_\beta \partial^{(\beta)}$ to the family $\big(\sum_\beta c_\beta \binom{\alpha}{\beta} x^{\alpha - \beta}\big)_\alpha$. Its matrix has the entry $\binom{\alpha}{\beta} x^{\alpha - \beta}$ at $(\alpha, \beta)$. This entry is $0$ unless $\beta \le \alpha$ in each coordinate, and it is $1$ for $\beta = \alpha$. Order the exponents by a total order that refines the partial order $\le$. Then the matrix is triangular with $1$ on the diagonal, so it is invertible. This proves the first statement.

For the second statement, let $D \in \mathcal{D}^m_{A/k}$ and take $e$ with $q = p^e > m$. The ring $k[A^q]$ is $A_e$, because $A^q = k^q[x_1^q, \dots, x_n^q]$. By Lemma 6.3.5, $D$ is $A_e$-linear, so $D \in \operatorname{End}_{A_e}(A)$, and by the first statement $D$ is a finite sum $\sum c_\beta \partial^{(\beta)}$. Conversely, each $A$-linear combination of operators $\partial^{(\beta)}$ is a differential operator by Lemma 6.3.4, and it is $A_e$-linear for large $e$. The sum is direct, because it is direct in each $\operatorname{End}_{A_e}(A)$. $\square$

The operators $\partial^{(\beta)}$ with $\beta \in [0, q)^n$ also find the elements of $A_e$. Volume 7 uses this test for the equations $z^q + F$.

**Corollary 6.3.7.** Let $k$ be a commutative ring of characteristic $p$, let $q = p^e$ and let $f \in k[x_1, \dots, x_n]$. Then $f$ is a polynomial in $x_1^q, \dots, x_n^q$ if and only if $\partial^{(\beta)}(f) = 0$ for each $\beta \in [0, q)^n$ with $\beta \ne 0$.

Node: SG0000004N · Lean: `Singularity.Algebra.MvHasse.exists_expand_eq_iff_hasseDeriv`

*Proof.* Let $f$ be a polynomial in $x_1^q, \dots, x_n^q$, and let $\beta \in [0, q)^n$ with $\beta \ne 0$. The first step of the proof of Theorem 6.3.6 holds over each ring of characteristic $p$, so $\partial^{(\beta)}$ is linear over $k[x_1^q, \dots, x_n^q]$. Thus $\partial^{(\beta)}(f) = f \, \partial^{(\beta)}(1) = 0$.

Conversely, assume that $f$ is not a polynomial in $x_1^q, \dots, x_n^q$. Then $f$ has a monomial $c \, x^\alpha$ with $c \ne 0$ and some $\alpha_i$ not divisible by $q$. Let $\beta_i$ be the remainder of $\alpha_i$ modulo $q$. Then $\beta \in [0, q)^n$ and $\beta \ne 0$. The operator $\partial^{(\beta)}$ sends the monomial $x^\gamma$ to a multiple of $x^{\gamma - \beta}$, and $\gamma - \beta = \alpha - \beta$ only for $\gamma = \alpha$. So the coefficient of $x^{\alpha - \beta}$ in $\partial^{(\beta)}(f)$ is $\binom{\alpha}{\beta} c$. We show that $\binom{\alpha_i}{\beta_i} \equiv 1 \pmod p$ for each $i$. Write $\alpha_i = qa + \beta_i$. In $\mathbb{F}_p[t]$,
$$(1 + t)^{\alpha_i} = (1 + t^q)^a (1 + t)^{\beta_i}.$$
Since $\beta_i < q$, the only term of $(1 + t^q)^a$ that contributes to the coefficient of $t^{\beta_i}$ is $1$. So this coefficient is $\binom{\beta_i}{\beta_i} = 1$. Thus $\binom{\alpha}{\beta} c = c \ne 0$, and $\partial^{(\beta)}(f) \ne 0$. $\square$

For $e \ge 2$ the first derivatives do not give this test. For example, let $f = x^p y^p$. Each derivation of $k[x, y]$ kills $f$, but $f$ is not a polynomial in $x^{p^2}$ and $y^{p^2}$, and $\partial^{((p, 0))}(f) = y^p$.

In characteristic $0$, $\mathcal{D}_{A/k}$ is the Weyl algebra: it is generated by $A$ and the derivations $\partial/\partial x_i$. In characteristic $p$ this is not true. Each derivation is $k[A^p]$-linear, by Lemma 6.3.5 with $q = p$, so the subring of $\operatorname{End}_k(A)$ that $A$ and the derivations generate consists of $k[A^p]$-linear maps. The operator $\partial^{(p)}$ in one variable is not $k[x^p]$-linear, since $\partial^{(p)}(x^p \cdot 1) = 1$ and $x^p \partial^{(p)}(1) = 0$. So $\mathcal{D}_{A/k}$ is not generated by $A$ and the derivations.

### Notes and references

Hasse and Schmidt introduced the higher derivations for the theory of function fields in characteristic $p$ [HSDer]. Matsumura treats them in [Mat, Section 27]. The differential operators of Definition 6.3.3 are due to Grothendieck [EGA4, Section 16], where they are defined with the module of principal parts. In the theory of resolution, the operators $\partial^{(\beta)}$ give the order of an element in positive characteristic: the order of $f$ at the origin is the least $|\beta|$ with $\partial^{(\beta)}(f)(0) \ne 0$, because $\partial^{(\beta)}(f)(0)$ is the coefficient of $x^\beta$ in $f$. This is the starting point of the use of differential operators in the work of Giraud, Hironaka and others on resolution in positive characteristic. Theorem 6.3.6 is classical. The Lean library of the project has the operators $\partial^{(\beta)}$ of a polynomial ring, their Leibniz rule, their composition rule, the first step of the proof of Theorem 6.3.6 and Corollary 6.3.7. It does not have Definition 6.3.3, Lemmas 6.3.4 and 6.3.5 and the rest of Theorem 6.3.6.
