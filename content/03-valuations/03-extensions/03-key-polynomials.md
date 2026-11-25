---
title: Key polynomials
nodes: [SG0000000Z]
sources: [Mac36, Vaq07, HMOS22]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Key polynomials

Let $(K, v)$ be a valued field and let $y$ be an indeterminate. Let $K(s)$ be a simple extension, and let $\mathfrak{q}$ be the kernel of the map $K[y] \to K(s)$ with $y \mapsto s$. Thus $\mathfrak{q} = 0$ if $s$ is transcendental over $K$, and $\mathfrak{q} = (F)$ with $F$ the minimal polynomial of $s$ if $s$ is algebraic. An extension of $v$ to $K(s)$ is the same as a valuation on $K[y]$ that extends $v$ and has support $\mathfrak{q}$, in the sense defined below. MacLane found a way to build such valuations in steps, by a sequence of polynomials in $y$ of increasing degree [Mac36]. The polynomials are the *key polynomials*. In this section we give the definitions, we state the main theorem, we prove the parts listed after it, and we work out one example.

### Valuations on a polynomial ring

Fix an ordered abelian group $\Gamma$ that contains $\Gamma_v$. A *valuation on $K[y]$* is a map $\mu \colon K[y] \to \Gamma \cup \{\infty\}$ with $\mu(fg) = \mu(f) + \mu(g)$, $\mu(f + g) \ge \min(\mu(f), \mu(g))$, $\mu(1) = 0$ and $\mu(0) = \infty$. Its *support* $\mu^{-1}(\infty)$ is a prime ideal. If the support is 0, then $\mu$ extends to a valuation of $K(y)$. If the support is $(F)$ with $F$ irreducible, then $\mu$ induces a valuation of the field $K[y]/(F)$. We say that $\mu$ *extends* $v$ if $\mu(a) = v(a)$ for $a \in K$. For two valuations we write $\mu \le \mu'$ if $\mu(f) \le \mu'(f)$ for all $f$.

**Definition 3.3.1 (graded algebra).** Let $\mu$ be a valuation on $K[y]$. For $\gamma \in \Gamma$ let $P_\gamma = \{f : \mu(f) \ge \gamma\}$ and $P_\gamma^+ = \{f : \mu(f) > \gamma\}$. The *graded algebra* of $\mu$ is
$$\operatorname{gr}_\mu = \bigoplus_{\gamma \in \Gamma} P_\gamma / P_\gamma^+.$$
For $f$ with $\mu(f) < \infty$, the *initial form* $\operatorname{in}_\mu f$ is the class of $f$ in $P_{\mu(f)}/P_{\mu(f)}^+$. Two polynomials $f$ and $g$ are *$\mu$-equivalent* if $\operatorname{in}_\mu f = \operatorname{in}_\mu g$, that is, if $\mu(f - g) > \mu(f)$. We say that $f$ *$\mu$-divides* $g$ if $\operatorname{in}_\mu f$ divides $\operatorname{in}_\mu g$ in $\operatorname{gr}_\mu$.

The product of $P_\gamma$ and $P_\delta$ is in $P_{\gamma + \delta}$, so $\operatorname{gr}_\mu$ is a graded ring. We have $\operatorname{in}_\mu(fg) = \operatorname{in}_\mu f \cdot \operatorname{in}_\mu g$, and this is not 0, because $\mu(fg) = \mu(f) + \mu(g)$. So the product of two nonzero homogeneous elements is not 0. Let $F$ and $G$ be nonzero elements of $\operatorname{gr}_\mu$. Each has finitely many nonzero homogeneous components, and the degrees are totally ordered. The component of $FG$ in the least degree is the product of the components of $F$ and $G$ in their least degrees, so it is not 0. Thus $\operatorname{gr}_\mu$ is an integral domain.

**Lemma 3.3.2 (monomial valuations).** Let $\gamma \in \Gamma$. For $f = \sum_i a_iy^i$ with $a_i \in K$ let
$$\mu_0(f) = \min_i\big(v(a_i) + i\gamma\big).$$
Then $\mu_0$ is a valuation on $K[y]$ with support 0 that extends $v$. We write $\mu_0 = [v; y, \gamma]$.

Lean: `Singularity.monomialValuation`

*Proof.* The inequality $\mu_0(f + g) \ge \min(\mu_0(f), \mu_0(g))$ holds term by term, and $\mu_0(fg) \ge \mu_0(f) + \mu_0(g)$ holds for the same reason. Let $g = \sum_j b_jy^j$. Let $i_0$ be the smallest index with $v(a_{i_0}) + i_0\gamma = \mu_0(f)$, and let $j_0$ be the smallest index with $v(b_{j_0}) + j_0\gamma = \mu_0(g)$. The coefficient of $y^{i_0 + j_0}$ in $fg$ is $\sum_{i + j = i_0 + j_0} a_ib_j$. The term $a_{i_0}b_{j_0}$ has value $\mu_0(f) + \mu_0(g) - (i_0 + j_0)\gamma$. Each other term has $i < i_0$ or $j < j_0$, so its value is strictly larger. By Lemma 1.1.3 the coefficient has value $\mu_0(f) + \mu_0(g) - (i_0 + j_0)\gamma$, so $\mu_0(fg) \le \mu_0(f) + \mu_0(g)$. $\square$

### Key polynomials and augmentations

**Definition 3.3.3 (key polynomial).** Let $\mu$ be a valuation on $K[y]$ with support 0 that extends $v$. A monic polynomial $\varphi \in K[y]$ is a *key polynomial* for $\mu$ if it has these two properties.

1. $\varphi$ is *$\mu$-irreducible*: $\operatorname{in}_\mu \varphi$ is a prime element of $\operatorname{gr}_\mu$. Thus it is not a unit, and if $\varphi$ $\mu$-divides $fg$, then $\varphi$ $\mu$-divides $f$ or $g$.
2. $\varphi$ is *$\mu$-minimal*: if $\varphi$ $\mu$-divides a nonzero $f$, then $\deg f \ge \deg \varphi$.

Node: SG0000000Z · Lean: `Singularity.KeyPolynomial`

Let $\varphi$ be monic of degree $m \ge 1$. Each $f \in K[y]$ has a unique *$\varphi$-expansion* $f = \sum_j a_j\varphi^j$ with $\deg a_j < m$, by repeated division with remainder by $\varphi$.

**Definition 3.3.4 (augmented valuation).** Let $\mu$ and $\varphi$ be as in Definition 3.3.3, and let $\gamma \in \Gamma \cup \{\infty\}$ with $\gamma > \mu(\varphi)$. The *augmented valuation* $\mu' = [\mu; \varphi, \gamma]$ is
$$\mu'\Big(\sum_j a_j\varphi^j\Big) = \min_j\big(\mu(a_j) + j\gamma\big),$$
with the $\varphi$-expansion on the left.

Lean: `Singularity.augmentedValuationFun`

**Theorem 3.3.5 (MacLane-Vaquié).** Let $\mu$, $\varphi$, $\gamma$ and $\mu' = [\mu; \varphi, \gamma]$ be as in Definition 3.3.4, and let $m = \deg \varphi$.

1. $\mu'$ is a valuation on $K[y]$ that extends $v$. Its support is 0 if $\gamma < \infty$ and $(\varphi)$ if $\gamma = \infty$.
2. $\mu \le \mu'$, $\mu'(f) = \mu(f)$ if $\deg f < m$, and $\mu'(\varphi) = \gamma > \mu(\varphi)$.
3. If $\gamma < \infty$, then $\varphi$ is a key polynomial for $\mu'$. Let $\Delta \subseteq \operatorname{gr}_{\mu'}$ be the subring generated by the initial forms of the nonzero polynomials of degree $< m$. Then $\operatorname{in}_{\mu'} \varphi$ is transcendental over $\Delta$, and $\operatorname{gr}_{\mu'} = \Delta[\operatorname{in}_{\mu'} \varphi]$ is a polynomial ring.
4. Let $\nu$ be a valuation on $K[y]$ that extends $v$. Then $\nu$ is the end of a chain
$$\mu_0 = [v; \varphi_0, \gamma_0] < \mu_1 = [\mu_0; \varphi_1, \gamma_1] < \mu_2 < \cdots$$
of augmentations and *limit augmentations* with $\deg \varphi_0 = 1$, $\deg \varphi_i \le \deg \varphi_{i+1}$ and $\mu_i \le \nu$, in the following sense. Either the chain is finite and ends with $\nu$, or $\nu$ is the limit of the chain, or the chain is finite and $\nu$ is the limit of a continuous family of augmentations of one degree over its last valuation. In the last two cases $\nu$ has no key polynomial in the sense of Definition 3.3.47 (Theorem 3.3.52).

Lean: `Singularity.augmentedValuation`, `Singularity.KeyPolynomial.augmentedValuationFun_mul`, `Singularity.augmentedValuation_le` (parts 1 and 2), `Singularity.KeyPolynomial.keyPolynomial_augmentedValuation` (the first claim of part 3), `Singularity.KeyPolynomial.muEquiv_augmentedValuation_sum_filter` and `Singularity.KeyPolynomial.augmentedValuation_sum_mul_pow` (the claim on the graded algebra in part 3, Proposition 3.3.19), `Singularity.exists_keyPolynomial_augmentedValuation` (one step of the chain of part 4, Lemma 3.3.9), `Singularity.macLaneChain_eventually_eq` (part 4 without limit augmentations for $\nu$ with discrete values, Theorem 3.3.12), `Singularity.ContinuousFamily.limitAugmentedValuation` (the limit augmentation of part 4 for one continuous family, Theorem 3.3.29), `Singularity.exists_macLaneVaquie_seq_or_forall_isStable` (the chain of part 4 with limit steps for each $\nu$, in the weak form of Theorem 3.3.44), `Singularity.reflTransGen_macLaneVaquieStep_of_map_eq_zero` (part 4 for $\nu$ with nonzero support, Theorem 3.3.46)

MacLane proved parts 1 to 3 for a discrete valuation $v$ of rank 1 [Mac36]. He proved part 4 without limit augmentations when $\nu$ is also discrete of rank 1. In that case the chain is finite or $\nu$ is its limit. Vaquié extended the theorem to an arbitrary valuation $v$ [Vaq07]. He introduced the limit augmentations of part 4, and in the general case one indexes the chain by an ordinal. Herrera Govantes, Mahboub, Olalla Acosta and Spivakovsky give a different approach to key polynomials for a simple extension $K(s)/K$ [HMOS22]. We prove parts 1 and 2 and the first claim of part 3 below, and the claim on $\operatorname{gr}_{\mu'}$ in part 3 in Proposition 3.3.19. Of part 4 we prove the first step and the inductive step of the chain, in Lemmas 3.3.10 and 3.3.9, and the properties of the chain in Lemma 3.3.11. If the values of $\nu$ are discrete, for example if $\nu$ has values in $\mathbb{Z} \cup \{\infty\}$, we prove part 4 without limit augmentations in Theorem 3.3.12. Then the chain is finite and ends with $\nu$, or $\nu$ is its limit. Proposition 3.3.13 gives a criterion for a finite chain, and Example 3.3.14 shows that the chain can be infinite, also when $\nu$ has a nonzero support. Proposition 3.3.15 to Example 3.3.18 describe the choice of the key polynomials of the chain. Definition 3.3.20 to Theorem 3.3.29 construct the limit augmentation of Vaquié for one continuous family of augmentations of one degree. Theorem 3.3.31 proves that the limit key polynomial is a key polynomial for the limit augmentation, and Theorem 3.3.33 gives one limit step of the chain for a limit key polynomial of largest value. For $\nu$ with discrete values, Lemma 3.3.34 to Theorem 3.3.36 show that the limit augmentations give nothing new: the values of an infinite chain with bounded degrees tend to $\infty$, and a limit step of a continuous family below $\nu$ can only be the last step and gives $\nu$. Definition 3.3.37 to Theorem 3.3.46 build the chain with ordinary and limit steps for each $\nu$. Each round uses all monic polynomials of one degree at once. Either $\nu$ is the limit of a sequence of valuations of the chain, or $\nu$ is the limit of a continuous family over a valuation of the chain (Theorem 3.3.44). If $\nu$ has a nonzero support, then a finite chain of ordinary and limit steps ends with $\nu$, for any values (Theorem 3.3.46). Definition 3.3.47 to Theorem 3.3.52 prove that a finite chain ends with $\nu$ if and only if $\nu$ has a key polynomial, for any values and any support (Theorem 3.3.51), and give part 4 in three cases (Theorem 3.3.52). If $\nu$ has no key polynomial, then $\nu$ is the limit of an infinite chain, or $\nu$ is the limit of a continuous family of one degree over a valuation of a finite chain. We do not decide which of these two cases holds. We do not prove the uniqueness of the chain, and our families are not indexed by well ordered sets as in [Vaq07]. In the example below we use only parts 1 to 3, and we compute the last step by hand.

Over a henselian field $K$, part 4 for the valuation $\nu$ with support $(F)$ describes the extension of $v$ to $K[y]/(F)$. Defect is related to the limit augmentations of part 4. A family of key polynomials of the same degree whose values increase but have no maximum is the same phenomenon as the sequence $s_m$ of Proposition 3.2.5.

### The proof of parts 1 and 2

The proof uses two lemmas. In both, $\mu$ is a valuation on $K[y]$ with support 0 that extends $v$, and $\varphi$ is monic of degree $m \ge 1$. For $f \in K[y]$ we write $f = \sum_j a_j\varphi^j$ for its $\varphi$-expansion.

**Lemma 3.3.6 (the expansion criterion).** The polynomial $\varphi$ is $\mu$-minimal if and only if
$$\mu(f) = \min_j\big(\mu(a_j) + j\mu(\varphi)\big)$$
for each $f \in K[y]$.

Lean: `Singularity.isMuMinimal_iff`

*Proof.* Assume that $\varphi$ is $\mu$-minimal. Step 1. Let $r, q \in K[y]$ with $\deg r < m$. We show that $\mu(r + \varphi q) = \min(\mu(r), \mu(\varphi q))$. The inequality $\ge$ is the ultrametric inequality, and it is an equality if $\mu(r) \neq \mu(\varphi q)$. Assume that $\mu(r) = \mu(\varphi q)$ and $\mu(r + \varphi q) > \mu(r)$. Then $r \neq 0$, because otherwise $\mu(r + \varphi q) = \mu(\varphi q) = \mu(r)$. Now $\mu(r - \varphi(-q)) > \mu(r)$, so $r$ is $\mu$-equivalent to $\varphi \cdot (-q)$, and $\varphi$ $\mu$-divides $r$. By minimality $\deg r \ge m$. This is a contradiction. Step 2. Write $f = a_0 + \varphi f_1$ with $f_1 = \sum_{j \ge 1} a_j\varphi^{j-1}$. By Step 1, $\mu(f) = \min(\mu(a_0), \mu(\varphi) + \mu(f_1))$. The $\varphi$-expansion of $f_1$ has fewer terms, so by induction $\mu(f_1) = \min_{j \ge 1}(\mu(a_j) + (j - 1)\mu(\varphi))$. This gives the formula.

Conversely, assume the formula, and let $f \neq 0$ with $\deg f < m$. Assume that $\varphi$ $\mu$-divides $f$, so that $\mu(f - \varphi h) > \mu(f)$ for some $h$. The $\varphi$-expansion of $f - \varphi h$ has the coefficient $a_0 = f$, so the formula gives $\mu(f - \varphi h) \le \mu(f)$. This is a contradiction. Thus $\varphi$ $\mu$-divides no nonzero polynomial of degree less than $m$, and $\varphi$ is $\mu$-minimal. $\square$

**Lemma 3.3.7 (products in low degree).** Let $\varphi$ be a key polynomial for $\mu$. Let $a, b \in K[y]$ with $\deg a < m$ and $\deg b < m$, and write $ab = q\varphi + r$ with $\deg r < m$. Then $\mu(r) = \mu(ab)$ and $\mu(q\varphi) \ge \mu(ab)$.

Lean: `Singularity.KeyPolynomial.map_mul_modByMonic` (the first claim; the second claim follows from the first by the ultrametric inequality, because $q\varphi = ab - r$)

*Proof.* We can assume that $a \neq 0$ and $b \neq 0$. Since $\deg(ab) \le 2m - 2$, we have $\deg q < m$, so $r + q\varphi$ is the $\varphi$-expansion of $ab$. By Lemma 3.3.6, $\mu(ab) = \min(\mu(r), \mu(q\varphi))$. If $\mu(q\varphi) < \mu(r)$, then $\mu(ab - q\varphi) = \mu(r) > \mu(ab)$. Thus $ab$ is $\mu$-equivalent to $\varphi q$, and $\varphi$ $\mu$-divides $ab$. Since $\varphi$ is $\mu$-irreducible, it $\mu$-divides $a$ or $b$. This is not possible by minimality, because $a$ and $b$ are nonzero of degree less than $m$. So $\mu(r) \le \mu(q\varphi)$, and $\mu(r) = \mu(ab)$. $\square$

*Proof of parts 1 and 2 of Theorem 3.3.5.* The function $\mu'$ satisfies $\mu'(f + g) \ge \min(\mu'(f), \mu'(g))$, because the $\varphi$-expansion of $f + g$ is the sum of the expansions. For $c$ of degree less than $m$ and $k \ge 0$, the $\varphi$-expansion of $c\varphi^k$ has one term, so $\mu'(c\varphi^k) = \mu(c) + k\gamma$. In particular $\mu'(f) = \mu(f)$ if $\deg f < m$, $\mu'(\varphi) = \gamma$, and $\mu'$ extends $v$.

We show part 2, $\mu \le \mu'$. By Lemma 3.3.6 and $\gamma > \mu(\varphi)$,
$$\mu(f) = \min_j\big(\mu(a_j) + j\mu(\varphi)\big) \le \min_j\big(\mu(a_j) + j\gamma\big) = \mu'(f).$$

We show that $\mu'(fg) = \mu'(f) + \mu'(g)$. Let $f = \sum_i a_i\varphi^i$ and $g = \sum_j b_j\varphi^j$, and write $a_ib_j = q_{ij}\varphi + r_{ij}$ with $\deg r_{ij} < m$. Then
$$fg = \sum_{i,j}\big(r_{ij}\varphi^{i+j} + q_{ij}\varphi^{i+j+1}\big),$$
and $\deg q_{ij} < m$. By Lemma 3.3.7, $\mu'(r_{ij}\varphi^{i+j}) = \mu(a_i) + \mu(b_j) + (i + j)\gamma$ and
$$\mu'(q_{ij}\varphi^{i+j+1}) = \mu(q_{ij}) + (i + j + 1)\gamma \ge \mu(q_{ij}\varphi) + (i + j)\gamma \ge \mu(a_i) + \mu(b_j) + (i + j)\gamma.$$
Each term is at least $\mu'(f) + \mu'(g)$, so $\mu'(fg) \ge \mu'(f) + \mu'(g)$. For the other inequality we can assume that $\mu'(f)$ and $\mu'(g)$ are finite. Let $i_0$ be the least index with $\mu(a_{i_0}) + i_0\gamma = \mu'(f)$, let $j_0$ be the least index with $\mu(b_{j_0}) + j_0\gamma = \mu'(g)$, and let $k = i_0 + j_0$. Let $\delta = \mu'(f) + \mu'(g) - k\gamma$. If $\gamma = \infty$, then $i_0 = j_0 = 0$. By the uniqueness of the $\varphi$-expansion, the coefficient of $\varphi^k$ in the expansion of $fg$ is
$$c_k = \sum_{i + j = k} r_{ij} + \sum_{i + j = k - 1} q_{ij}.$$
The term $r_{i_0j_0}$ has the value $\mu(a_{i_0}) + \mu(b_{j_0}) = \delta$. Another term $r_{ij}$ with $i + j = k$ has $i < i_0$ or $j < j_0$, so its value $\mu(a_i) + \mu(b_j)$ is larger than $\delta$. A term $q_{ij}$ with $i + j = k - 1$ has the value
$$\mu(q_{ij}) \ge \mu(a_i) + \mu(b_j) - \mu(\varphi) \ge \delta + \gamma - \mu(\varphi) > \delta.$$
By Lemma 1.1.3, $\mu(c_k) = \delta$. Thus $\mu'(fg) \le \mu(c_k) + k\gamma = \mu'(f) + \mu'(g)$.

The support of $\mu'$ is the set of $f$ with $\mu(a_j) + j\gamma = \infty$ for each $j$. If $\gamma < \infty$, this means that each $a_j$ is 0, because the support of $\mu$ is 0, so the support of $\mu'$ is 0. If $\gamma = \infty$, it means that $a_0 = 0$, that is $f \in (\varphi)$. $\square$

The proof of the multiplicativity uses $\gamma > \mu(\varphi)$ only in the strict inequality for the terms $q_{ij}$. For $\gamma = \mu(\varphi)$, Lemma 3.3.6 gives $\mu' = \mu$, so $\mu'$ is a valuation also in this case.

### The first claim of part 3

The first claim of part 3 follows from a criterion for $\mu'$-divisibility. Let $\varphi$ be a key polynomial for $\mu$ of degree $m$, let $\gamma > \mu(\varphi)$, and let $\mu' = [\mu; \varphi, \gamma]$. For $f \in K[y]$ we write $f = \sum_j a_j\varphi^j$ for the $\varphi$-expansion. Thus $a_0$ is the remainder of $f$ on division by $\varphi$.

**Lemma 3.3.8 (the divisibility criterion).** Let $f \in K[y]$. Then $\varphi$ $\mu'$-divides $f$ if and only if $\mu(a_0) > \mu'(f)$.

Lean: `Singularity.muDvd_iff_of_forall_eq`

*Proof.* Write $f = a_0 + \varphi q$. Assume that $\mu(a_0) > \mu'(f)$. Since $\deg a_0 < m$, part 2 gives $\mu'(f - \varphi q) = \mu'(a_0) = \mu(a_0) > \mu'(f)$. Thus $f$ is $\mu'$-equivalent to $\varphi q$, and $\varphi$ $\mu'$-divides $f$. Conversely, assume that $\mu'(f - \varphi h) > \mu'(f)$ for some $h$. The remainder of $\varphi h$ on division by $\varphi$ is 0, so the coefficient of $\varphi^0$ in the $\varphi$-expansion of $f - \varphi h$ is $a_0$. By the definition of $\mu'$ we get $\mu'(f - \varphi h) \le \mu(a_0)$. Thus $\mu(a_0) > \mu'(f)$. $\square$

The inequality $\mu(a_0) \ge \mu'(f)$ is always true, by the definition of $\mu'$. Thus the lemma says that $\varphi$ $\mu'$-divides $f$ if and only if the minimum in Definition 3.3.4 is not attained at $j = 0$.

*Proof that $\varphi$ is a key polynomial for $\mu'$.* Let $f \neq 0$ with $\deg f < m$. Then $a_0 = f$, and $\mu(f) = \mu'(f)$ by part 2. By Lemma 3.3.8, $\varphi$ does not $\mu'$-divide $f$. Thus $\varphi$ is $\mu'$-minimal. In particular $\varphi$ does not $\mu'$-divide 1, so $\operatorname{in}_{\mu'} \varphi$ is not a unit.

Now let $f, g \in K[y]$, and assume that $\varphi$ $\mu'$-divides neither $f$ nor $g$. Let $a$ and $b$ be the remainders of $f$ and $g$ on division by $\varphi$. By Lemma 3.3.8, $\mu(a) = \mu'(f)$ and $\mu(b) = \mu'(g)$. The remainder $r$ of $fg$ is the remainder of $ab$. By Lemma 3.3.7, $\mu(r) = \mu(ab) = \mu'(f) + \mu'(g)$. By part 1 this is $\mu'(fg)$. By Lemma 3.3.8, $\varphi$ does not $\mu'$-divide $fg$. Thus $\varphi$ is $\mu'$-irreducible. $\square$

This proof does not use the least indices $i_0$ and $j_0$ of the proof of part 1. It uses the hypothesis $\gamma > \mu(\varphi)$ only through parts 1 and 2. For $\gamma = \mu(\varphi)$ we have $\mu' = \mu$, and the claim is the hypothesis. The Lean form also allows $\gamma = \infty$. Then $\mu'(f) = \mu(a_0)$, so $\varphi$ $\mu'$-divides no polynomial, and the two conditions hold trivially. Definition 3.3.3 asks for support 0, so this case is not in Theorem 3.3.5. We prove the second claim of part 3 in Proposition 3.3.19 below.

### The step of MacLane

Part 4 of Theorem 3.3.5 builds the chain one augmentation at a time. Lemma 3.3.9 gives one step. It compares a valuation $\mu$ of the chain with the valuation $\nu$ that the chain must reach. Lemma 3.3.10 gives the first valuation of the chain.

**Lemma 3.3.9 (the step of MacLane).** Let $\mu$ and $\nu$ be valuations on $K[y]$ that extend $v$, with $\mu \le \nu$ and $\mu \ne \nu$. Assume that $\mu$ has support 0.

1. There is a monic polynomial $\varphi$ with $\mu(\varphi) < \nu(\varphi)$. Let $\varphi$ be such a polynomial of least degree, and let $m = \deg \varphi$. Then $\mu(f) = \nu(f)$ for each $f$ with $\deg f < m$.
2. Let $f \in K[y]$. Then $\varphi$ $\mu$-divides $f$ if and only if $\mu(f) < \nu(f)$.
3. The polynomial $\varphi$ is a key polynomial for $\mu$.
4. Let $\mu' = [\mu; \varphi, \nu(\varphi)]$. Then $\mu < \mu' \le \nu$ and $\mu'(\varphi) = \nu(\varphi)$, and $\mu'(f) = \nu(f)$ for each $f$ with $\deg f < m$.

Lean: `Singularity.exists_keyPolynomial_augmentedValuation`, `Singularity.exists_monic_map_lt` (part 1), `Singularity.muDvd_iff_map_lt` (part 2), `Singularity.keyPolynomial_of_map_lt` (part 3), `Singularity.map_le_augmentedValuation_of_map_lt` and `Singularity.augmentedValuation_eq_of_map_lt` (part 4)

*Proof.* Part 1. Since $\mu \le \nu$ and $\mu \ne \nu$, there is an $f$ with $\mu(f) < \nu(f)$. Then $\mu(f) < \infty$, so $f \ne 0$. Let $c$ be the leading coefficient of $f$. The polynomial $c^{-1}f$ is monic, and $\mu(c^{-1}f) = \mu(f) - v(c) < \nu(f) - v(c) = \nu(c^{-1}f)$. Thus a monic $\varphi$ with $\mu(\varphi) < \nu(\varphi)$ exists, and we can take one of least degree. Now let $f \ne 0$ with $\deg f < m$, and let $c$ be its leading coefficient. The monic polynomial $c^{-1}f$ has degree less than $m$, so $\mu(c^{-1}f) \ge \nu(c^{-1}f)$ by the choice of $\varphi$. Since $\mu \le \nu$, we get $\mu(c^{-1}f) = \nu(c^{-1}f)$, and thus $\mu(f) = \nu(f)$. For $f = 0$ both values are $\infty$.

Part 2. Assume that $\varphi$ $\mu$-divides $f$, so that $\mu(f - \varphi h) > \mu(f)$ for some $h$. Then $\mu(\varphi h) = \mu(f) < \infty$, so $\mu(h) < \infty$. Since $\mu(\varphi) < \nu(\varphi)$ and $\mu(h) \le \nu(h)$, we get $\nu(\varphi h) > \mu(\varphi h) = \mu(f)$. Also $\nu(f - \varphi h) \ge \mu(f - \varphi h) > \mu(f)$. Thus $\nu(f) \ge \min(\nu(f - \varphi h), \nu(\varphi h)) > \mu(f)$.

Conversely, assume that $\mu(f) < \nu(f)$. Write $f = a + \varphi q$ with $\deg a < m$. By part 1, $\mu(a) = \nu(a)$. Assume that $\mu(a) \le \mu(f)$. Then $\nu(a) = \mu(a) \le \mu(f) < \nu(f)$. If $\nu(\varphi q) \ne \nu(a)$, then $\nu(f) = \min(\nu(a), \nu(\varphi q)) \le \nu(a)$, and this is a contradiction. So $\nu(\varphi q) = \nu(a) = \mu(a)$, and this value is finite. Then $\nu(q) < \infty$, so $\mu(q) \le \nu(q) < \infty$, and
$$\mu(\varphi q) = \mu(\varphi) + \mu(q) < \nu(\varphi) + \nu(q) = \nu(\varphi q) = \mu(a).$$
Thus $\mu(f) = \mu(a + \varphi q) = \mu(\varphi q) < \mu(a)$. This contradicts $\mu(a) \le \mu(f)$. So $\mu(f - \varphi q) = \mu(a) > \mu(f)$. Thus $f$ is $\mu$-equivalent to $\varphi q$, and $\varphi$ $\mu$-divides $f$.

Part 3. The polynomial $\varphi$ is monic. By part 2, $\varphi$ does not $\mu$-divide 1, because $\mu(1) = \nu(1)$. So $\operatorname{in}_\mu \varphi$ is not a unit. Assume that $\varphi$ $\mu$-divides $fg$. By part 2, $\mu(f) + \mu(g) < \nu(f) + \nu(g)$. Since $\mu(f) \le \nu(f)$ and $\mu(g) \le \nu(g)$, we get $\mu(f) < \nu(f)$ or $\mu(g) < \nu(g)$. By part 2, $\varphi$ $\mu$-divides $f$ or $g$. Thus $\varphi$ is $\mu$-irreducible. If $\varphi$ $\mu$-divides a nonzero $f$, then $\mu(f) < \nu(f)$ by part 2, so $\deg f \ge m$ by part 1. Thus $\varphi$ is $\mu$-minimal.

Part 4. We have $\nu(\varphi) > \mu(\varphi)$, so $\mu'$ is defined. By part 3 and Theorem 3.3.5, $\mu'$ is a valuation with $\mu \le \mu'$ and $\mu'(\varphi) = \nu(\varphi) > \mu(\varphi)$. Thus $\mu \ne \mu'$. For $\deg f < m$, Theorem 3.3.5 and part 1 give $\mu'(f) = \mu(f) = \nu(f)$. Let $f = \sum_j a_j\varphi^j$ be the $\varphi$-expansion of $f$. Since $\deg a_j < m$, part 1 gives $\nu(a_j) = \mu(a_j)$. Thus
$$\nu(f) \ge \min_j\big(\nu(a_j) + j\nu(\varphi)\big) = \min_j\big(\mu(a_j) + j\nu(\varphi)\big) = \mu'(f).$$
So $\mu' \le \nu$. $\square$

The proof of parts 1 to 3 does not use that $\mu$ has support 0. We need this hypothesis because Definition 3.3.3 and Theorem 3.3.5 ask for it. The proof of part 1 uses only that $\mu$ and $\nu$ agree on $K$.

**Lemma 3.3.10 (the first step).** Let $\nu$ be a valuation on $K[y]$ that extends $v$, with $\nu(y) < \infty$. Then $\mu_0 = [v; y, \nu(y)]$ satisfies $\mu_0 \le \nu$, and $\mu_0(y) = \nu(y)$.

Lean: `Singularity.map_le_monomialValuation`, `Singularity.map_le_monomialValuationFun`

*Proof.* Let $f = \sum_i a_iy^i$ with $a_i \in K$. Then
$$\nu(f) \ge \min_i\big(v(a_i) + i\nu(y)\big) = \mu_0(f).$$
The value $\mu_0(y) = \nu(y)$ is the definition of $\mu_0$. $\square$

### The chain of MacLane

Let $\nu$ be a valuation on $K[y]$ that extends $v$, with $\nu(y) < \infty$. The two lemmas give the chain of part 4 of Theorem 3.3.5 step by step. Let $\varphi_0 = y$ and let $\mu_0 = [v; y, \nu(y)]$ be the valuation of Lemma 3.3.10. Let $i \ge 0$, and assume that $\mu_i$ is defined, that $\mu_i \le \nu$, and that $\mu_i$ has support 0. If $\mu_i = \nu$, let $\mu_{i+1} = \nu$. If $\mu_i \ne \nu$, let $\varphi_{i+1}$ be a monic polynomial of least degree with $\mu_i(\varphi_{i+1}) < \nu(\varphi_{i+1})$, as in part 1 of Lemma 3.3.9, and let $\mu_{i+1} = [\mu_i; \varphi_{i+1}, \nu(\varphi_{i+1})]$. By Lemma 3.3.9, $\varphi_{i+1}$ is a key polynomial for $\mu_i$ and $\mu_{i+1} \le \nu$. If $\nu(\varphi_{i+1}) < \infty$, then $\mu_{i+1}$ has support 0 by part 1 of Theorem 3.3.5. If $\nu(\varphi_{i+1}) = \infty$, then $\mu_{i+1} = \nu$ by part 4 of Lemma 3.3.11 below, and the chain stops. We call $(\mu_i)$ the *MacLane chain* of $\nu$. If $\mu_n = \nu$ for some $n$, we say that the chain is *finite* and ends with $\nu$. The chain depends on the choice of each $\varphi_{i+1}$. The results below hold for each choice. Proposition 3.3.15 describes the possible choices.

**Lemma 3.3.11 (the chain of MacLane).** Let $\nu$ be a valuation on $K[y]$ that extends $v$, with $\nu(y) < \infty$, and let $(\mu_i)$ be its MacLane chain. Let $i \ge 0$ with $\mu_i \ne \nu$, and let $\varphi = \varphi_{i+1}$.

1. $\mu_i \le \mu_{i+1} \le \nu$, and $\mu_i(\varphi) < \mu_{i+1}(\varphi) = \nu(\varphi)$.
2. Let $f \in K[y]$. Then $\mu_i(f) < \mu_{i+1}(f)$ if and only if $\mu_i(f) < \nu(f)$.
3. Each value of $\mu_0$ and each value of $\mu_{i+1}$ is a value of $\nu$.
4. If $\nu(\varphi) = \infty$, then $\mu_{i+1} = \nu$.
5. If $\mu_{i+1} \ne \nu$, then $\deg \varphi_{i+1} \le \deg \varphi_{i+2}$. If in addition $\deg \varphi_{i+1} = \deg \varphi_{i+2}$, then $\nu(\varphi_{i+1}) < \nu(\varphi_{i+2})$.
6. If $\nu(F) = \infty$ for some $F \ne 0$, then $\deg \varphi \le \deg F$.

Lean: `Singularity.macLaneChain_succ_le`, `Singularity.le_macLaneChain`, `Singularity.macLaneChain_succ_lt_self` (part 1), `Singularity.macLaneChain_succ_lt_iff`, `Singularity.augmentedValuationFun_lt_iff_map_lt` (part 2), `Singularity.exists_eq_macLaneChain` (part 3), `Singularity.macLaneChain_succ_eq_of_map_eq_zero` (part 4), `Singularity.natDegree_macLaneChainKey_le_succ`, `Singularity.map_macLaneChainKey_succ_lt`, `Singularity.map_lt_map_of_natDegree_eq` (part 5), `Singularity.natDegree_macLaneChainKey_le_of_map_eq_zero` (part 6)

*Proof.* Let $m = \deg \varphi$. For $f \in K[y]$ we write $f = \sum_j a_j\varphi^j$ for the $\varphi$-expansion. By the construction, $\mu_i \le \nu$ and $\mu_i$ has support 0. Thus Lemma 3.3.9 applies to $\mu_i$ and $\nu$. By part 1 of Lemma 3.3.9, $\mu_i(a) = \nu(a)$ for each $a$ with $\deg a < m$.

Part 1. This is part 4 of Lemma 3.3.9.

Part 2. If $\mu_i(f) < \mu_{i+1}(f)$, then $\mu_i(f) < \nu(f)$ by part 1. Conversely, assume that $\mu_i(f) < \nu(f)$. By part 2 of Lemma 3.3.9, $\varphi$ $\mu_i$-divides $f$, so that $\mu_i(f - \varphi h) > \mu_i(f)$ for some $h$. Then $\mu_i(\varphi h) = \mu_i(f) < \infty$, so $\mu_i(h) < \infty$. By part 1, $\mu_{i+1}(\varphi h) = \mu_{i+1}(\varphi) + \mu_{i+1}(h) > \mu_i(\varphi) + \mu_i(h) = \mu_i(f)$. Also $\mu_{i+1}(f - \varphi h) \ge \mu_i(f - \varphi h) > \mu_i(f)$. Thus $\mu_{i+1}(f) \ge \min(\mu_{i+1}(f - \varphi h), \mu_{i+1}(\varphi h)) > \mu_i(f)$.

Part 3. Let $f = \sum_j a_jy^j$ with $a_j \in K$. Then $\mu_0(f) = v(a_j) + j\nu(y) = \nu(a_jy^j)$ for some $j$. Now let $f = \sum_j a_j\varphi^j$ be the $\varphi$-expansion. Then $\mu_{i+1}(f) = \mu_i(a_j) + j\nu(\varphi)$ for some $j$, and $\mu_i(a_j) = \nu(a_j)$ because $\deg a_j < m$. Thus $\mu_{i+1}(f) = \nu(a_j\varphi^j)$.

Part 4. Write $f = a_0 + \varphi q$ with $\deg a_0 < m$. Then $\nu(\varphi q) = \infty$, so $\nu(f) = \nu(a_0) = \mu_i(a_0)$. The terms with $j \ge 1$ in Definition 3.3.4 are $\infty$, so $\mu_{i+1}(f) = \mu_i(a_0)$. Thus $\mu_{i+1}(f) = \nu(f)$.

Part 5. By part 4 of Lemma 3.3.9, $\mu_{i+1}(f) = \nu(f)$ for each $f$ with $\deg f < m$. Since $\mu_{i+1}(\varphi_{i+2}) < \nu(\varphi_{i+2})$, we get $\deg \varphi_{i+2} \ge m$. Now assume that $\deg \varphi_{i+2} = m$, and let $\psi = \varphi_{i+2}$ and $a = \psi - \varphi$. The two polynomials are monic of degree $m$, so $\deg a < m$ and $\mu_{i+1}(a) = \nu(a)$. Assume that $\nu(a) < \nu(\varphi)$. Then $\nu(\psi) = \nu(a)$, and
$$\mu_{i+1}(\psi) \ge \min(\mu_{i+1}(\varphi), \mu_{i+1}(a)) = \min(\nu(\varphi), \nu(a)) = \nu(a) = \nu(\psi).$$
This contradicts $\mu_{i+1}(\psi) < \nu(\psi)$. Thus $\nu(a) \ge \nu(\varphi)$, and
$$\nu(\psi) > \mu_{i+1}(\psi) \ge \min(\nu(\varphi), \nu(a)) = \nu(\varphi).$$

Part 6. Assume that $\deg F < m$. Then $\mu_i(F) = \nu(F) = \infty$. This is false, because $\mu_i$ has support 0. Thus $m \le \deg F$. $\square$

**Theorem 3.3.12 (MacLane).** Let $\nu$ be a valuation on $K[y]$ that extends $v$, with $\nu(y) < \infty$, and let $(\mu_i)$ be its MacLane chain. Assume that the values of $\nu$ are discrete: for $\alpha, \beta \in \Gamma$, only finitely many values of $\nu$ lie in the interval $[\alpha, \beta]$. Then $\nu$ is the limit of the chain, in this sense. Let $f \in K[y]$ and $\beta \in \Gamma$ with $\beta \le \nu(f)$. Then $\mu_i(f) \ge \beta$ for all large $i$. If $\nu(f) < \infty$, then $\mu_i(f) = \nu(f)$ for all large $i$.

Lean: `Singularity.macLaneChain_eventually_eq`, `Singularity.macLaneChain_eventually_le`, `Singularity.eventually_eq_of_succ_lt`, `Singularity.eventually_le_of_succ_lt`

*Proof.* By part 1 of Lemma 3.3.11 and the construction, $\mu_i(f) \le \mu_{i+1}(f) \le \nu(f)$ for each $i$. Assume that $\mu_i(f) < \beta$ for each $i$. Then $\mu_i(f) < \nu(f)$, so $\mu_i \ne \nu$ for each $i$. By part 2 of Lemma 3.3.11, $\mu_i(f) < \mu_{i+1}(f)$ for each $i$. Since $\mu_0(f) < \beta$, we have $\mu_0(f) \in \Gamma$. Thus the values $\mu_i(f)$ are infinitely many distinct elements of the interval $[\mu_0(f), \beta]$. Each $\mu_i$ is $\mu_0$ or an augmentation $\mu_{j+1}$ with $\mu_j \ne \nu$, so by part 3 of Lemma 3.3.11 these elements are values of $\nu$. This contradicts the hypothesis. So $\mu_N(f) \ge \beta$ for some $N$, and then $\mu_i(f) \ge \beta$ for each $i \ge N$. If $\nu(f) < \infty$, take $\beta = \nu(f)$. Then $\nu(f) \le \mu_i(f) \le \nu(f)$ for each $i \ge N$. $\square$

The hypothesis of the theorem holds if $\Gamma$ is a subgroup of $\mathbb{R}$ and the value group of $\nu$ is 0 or is isomorphic to $\mathbb{Z}$, that is, if $\nu$ is discrete of rank 1. It does not hold for a discrete valuation of rank 2. The proof does not use that $v$ is discrete, or that $\nu$ has support 0. With Lemma 3.3.11, the theorem gives part 4 of Theorem 3.3.5 without limit augmentations for such $\nu$. The chain has $\deg \varphi_0 = 1$, $\deg \varphi_i \le \deg \varphi_{i+1}$ and $\mu_i \le \nu$, and $\mu_i < \mu_{i+1}$ as long as $\mu_i \ne \nu$. Either the chain is finite and ends with $\nu$, or $\nu$ is its limit. If $\nu(y) = \infty$, then $\nu(f) = v(f(0))$ for each $f$, because $\nu(yq) = \infty$ for each $q$. The example in the last section of this page has a finite chain.

**Proposition 3.3.13 (finite chains).** Let $\nu$ and $(\mu_i)$ be as in Theorem 3.3.12. In particular the values of $\nu$ are discrete. Assume that the degrees $\deg \varphi_i$ are bounded, and that there is $\beta \in \Gamma$ with $\nu(\varphi_i) \le \beta$ for each $i$ with $\nu(\varphi_i) < \infty$. Then the chain is finite and ends with $\nu$. If $\nu(F) = \infty$ for some $F \ne 0$, then the degrees are bounded by $\deg F$.

Lean: `Singularity.exists_macLaneChain_eq`, `Singularity.exists_macLaneChain_eq_of_map_eq_zero`

*Proof.* The last claim is part 6 of Lemma 3.3.11. Assume that $\mu_i \ne \nu$ for each $i$. By part 5 of Lemma 3.3.11, the degrees $\deg \varphi_i$ do not decrease for $i \ge 1$. They are bounded, so there are $N \ge 1$ and $m$ with $\deg \varphi_i = m$ for each $i \ge N$. By part 4 of Lemma 3.3.11, $\nu(\varphi_i) < \infty$ for each $i \ge 1$, because $\mu_i \ne \nu$. By part 5 of Lemma 3.3.11,
$$\nu(\varphi_N) < \nu(\varphi_{N+1}) < \nu(\varphi_{N+2}) < \cdots \le \beta.$$
These are infinitely many values of $\nu$ in the interval $[\nu(\varphi_N), \beta]$. This contradicts the hypothesis. $\square$

The bound on the values $\nu(\varphi_i)$ is necessary, also when $\nu$ has a nonzero support.

**Example 3.3.14 (an infinite chain).** Let $p$ be a prime, let $K = \mathbb{Q}$ and let $v$ be the $p$-adic valuation. Let $s \in \mathbb{Z}_p$ with $s \notin \mathbb{Q}$, and let $\nu(f) = v_p(f(s))$ for $f \in \mathbb{Q}[y]$. Then $\nu$ is a valuation on $\mathbb{Q}[y]$ that extends $v$, with values in $\mathbb{Z} \cup \{\infty\}$. Its support is 0 if $s$ is transcendental over $\mathbb{Q}$, and $(F)$ with $F$ the minimal polynomial of $s$ if $s$ is algebraic. By Theorem 3.3.12, $\nu$ is the limit of its MacLane chain. We show that the chain is infinite.

Since $\mathbb{Z}$ is dense in $\mathbb{Z}_p$, for each $n$ there is $b \in \mathbb{Z}$ with $v_p(s - b) \ge n$. Thus the values $\nu(y - b)$ with $b \in \mathbb{Q}$ are not bounded. We show by induction on $i$ that there is $\beta_i \in \mathbb{Z}$ with $\mu_i(y - b) \le \beta_i$ for each $b \in \mathbb{Q}$. This gives $\mu_i \ne \nu$ for each $i$, so the chain is infinite. Since $s \ne 0$, we have $\mu_0(y - b) = \min(v(b), \nu(y)) \le \nu(y) = v_p(s) < \infty$. Assume the bound for $\mu_i$. Then $\mu_i \ne \nu$, so $\mu_{i+1} = [\mu_i; \varphi_{i+1}, \nu(\varphi_{i+1})]$. If $\deg \varphi_{i+1} \ge 2$, then $\mu_{i+1}(y - b) = \mu_i(y - b) \le \beta_i$ by part 2 of Theorem 3.3.5. If $\deg \varphi_{i+1} = 1$, then $\varphi_{i+1} = y - a$ with $a \in \mathbb{Q}$. The $\varphi_{i+1}$-expansion of $y - b$ is $(a - b) + \varphi_{i+1}$, so
$$\mu_{i+1}(y - b) = \min(v(a - b), \nu(y - a)) \le v_p(s - a) < \infty,$$
because $s \ne a$. This completes the induction. If $s$ is algebraic, the degrees $\deg \varphi_i$ are at most $\deg F$ by Proposition 3.3.13. The chain is infinite, so by Proposition 3.3.13 the finite values $\nu(\varphi_i)$ are not bounded. $\square$

For other value groups, a family of key polynomials of the same degree can have values that increase and are bounded. Then part 4 of Theorem 3.3.5 can need the limit augmentations of Vaquié [Vaq07]. We construct the limit augmentation for one such family in Theorem 3.3.29 below. For discrete values, Theorem 3.3.36 below shows that a limit augmentation is not needed.

### The choice of the key polynomial

The construction of the MacLane chain chooses $\varphi_{i+1}$ among the monic polynomials of least degree with $\mu_i(\varphi_{i+1}) < \nu(\varphi_{i+1})$. We describe this set of polynomials, and we show how the augmentation depends on the choice. In this section $\mu$ and $\nu$ are as in Lemma 3.3.9, $\varphi$ is as in part 1 of Lemma 3.3.9, and $m = \deg \varphi$.

**Proposition 3.3.15 (the choice of the key polynomial).** Let $\psi \in K[y]$ be monic.

1. If $\psi$ is a monic polynomial of least degree with $\mu(\psi) < \nu(\psi)$, then $\deg \psi = m$.
2. Assume that $\deg \psi = m$. Then $\mu(\psi) < \nu(\psi)$ if and only if $\psi$ is $\mu$-equivalent to $\varphi$. In this case $\mu(\psi) = \mu(\varphi)$.
3. Assume that $\deg \psi = m$, that $\mu(\psi) < \nu(\psi)$ and that $\nu(\psi) \le \nu(\varphi)$. Then $\mu(\psi - \varphi) \ge \nu(\psi)$.

Thus the possible choices of $\varphi_{i+1}$ in the MacLane chain are the monic polynomials of degree $\deg \varphi_{i+1}$ that are $\mu_i$-equivalent to $\varphi_{i+1}$.

Lean: `Singularity.natDegree_eq_of_map_lt` (part 1), `Singularity.muEquiv_iff_map_lt` (part 2), `Singularity.map_sub_le_of_map_le` (part 3), `Singularity.muEquiv_macLaneChainKey_iff` (part 2 for the chain)

*Proof.* Part 1. By part 1 of Lemma 3.3.9, $\mu(f) = \nu(f)$ for each $f$ with $\deg f < m$. Thus $\deg \psi \ge m$. Since $\varphi$ is monic of degree $m$ with $\mu(\varphi) < \nu(\varphi)$, the choice of $\psi$ gives $\deg \psi \le m$.

For parts 2 and 3, let $a = \psi - \varphi$. The polynomials $\psi$ and $\varphi$ are monic of degree $m$, so $\deg a < m$. By part 1 of Lemma 3.3.9, $\mu(a) = \nu(a)$.

Part 2. Assume that $\psi$ is $\mu$-equivalent to $\varphi$, that is $\mu(a) > \mu(\varphi)$. Then $\mu(\psi) = \mu(\varphi + a) = \mu(\varphi)$, and
$$\nu(\psi) \ge \min(\nu(\varphi), \nu(a)) = \min(\nu(\varphi), \mu(a)) > \mu(\varphi) = \mu(\psi).$$
Conversely, assume that $\mu(\psi) < \nu(\psi)$, and assume that $\mu(a) \le \mu(\varphi)$. Then $\nu(a) = \mu(a) \le \mu(\varphi) < \nu(\varphi)$, so $\nu(\psi) = \nu(\varphi + a) = \nu(a)$. Also $\mu(\psi) \ge \min(\mu(\varphi), \mu(a)) = \mu(a) = \nu(\psi)$. This is a contradiction. Thus $\mu(a) > \mu(\varphi)$.

Part 3. Assume that $\mu(a) < \nu(\psi)$. Then $\nu(a) = \mu(a) < \nu(\psi) \le \nu(\varphi)$, so $\nu(\psi) = \nu(\varphi + a) = \nu(a) < \nu(\psi)$. This is a contradiction. $\square$

Part 5 of Lemma 3.3.11 uses the same argument as part 3. By part 3 of Lemma 3.3.9, each polynomial $\psi$ of part 2 is a key polynomial for $\mu$. The next lemma compares augmentations with two key polynomials of the same degree.

**Lemma 3.3.16 (equal augmentations).** Let $\varphi$ and $\psi$ be key polynomials for $\mu$ of the same degree $m$. Let $\gamma \in \Gamma \cup \{\infty\}$ with $\gamma > \mu(\varphi)$ and $\mu(\psi - \varphi) \ge \gamma$. Then $\gamma > \mu(\psi)$ and $[\mu; \varphi, \gamma] = [\mu; \psi, \gamma]$.

Lean: `Singularity.augmentedValuation_eq_of_map_sub_le`, `Singularity.KeyPolynomial.augmentedValuationFun_eq_of_map_sub_le`

*Proof.* Since $\mu(\psi - \varphi) \ge \gamma > \mu(\varphi)$, we have $\mu(\psi) = \mu(\varphi) < \gamma$. Let $\mu' = [\mu; \varphi, \gamma]$ and $\mu'' = [\mu; \psi, \gamma]$. By Theorem 3.3.5, both are valuations. We show that $\mu'' \le \mu'$. By part 2 of Theorem 3.3.5, $\mu'(f) = \mu(f)$ for each $f$ with $\deg f < m$. Since $\deg(\psi - \varphi) < m$, we get
$$\mu'(\psi) \ge \min(\mu'(\varphi), \mu'(\psi - \varphi)) = \min(\gamma, \mu(\psi - \varphi)) = \gamma.$$
Let $f = \sum_j b_j\psi^j$ be the $\psi$-expansion of $f$. Then
$$\mu'(f) \ge \min_j\big(\mu'(b_j) + j\mu'(\psi)\big) \ge \min_j\big(\mu(b_j) + j\gamma\big) = \mu''(f).$$
The hypotheses are symmetric in $\varphi$ and $\psi$, because $\mu(\varphi - \psi) = \mu(\psi - \varphi)$ and $\gamma > \mu(\psi)$. Thus also $\mu' \le \mu''$. $\square$

**Proposition 3.3.17 (two choices of the step).** Let $\psi$ be monic of degree $m$ with $\mu(\psi) < \nu(\psi) \le \nu(\varphi)$. Then
$$[\mu; \psi, \nu(\psi)] = [\mu; \varphi, \nu(\psi)] \le [\mu; \varphi, \nu(\varphi)].$$
If $\nu(\psi) = \nu(\varphi)$, then $[\mu; \psi, \nu(\psi)] = [\mu; \varphi, \nu(\varphi)]$. If $\nu(\psi) < \nu(\varphi)$, then the two augmentations are different, because $[\mu; \psi, \nu(\psi)](\varphi) = \nu(\psi)$ and $[\mu; \varphi, \nu(\varphi)](\varphi) = \nu(\varphi)$.

Lean: `Singularity.augmentedValuation_eq_of_map_le`, `Singularity.augmentedValuation_le_of_map_le`, `Singularity.augmentedValuationFun_le_of_map_le`, `Singularity.augmentedValuation_eq_of_map_eq`

*Proof.* By part 1 of Proposition 3.3.15, $\psi$ is a monic polynomial of least degree with $\mu(\psi) < \nu(\psi)$. By part 3 of Lemma 3.3.9, $\varphi$ and $\psi$ are key polynomials for $\mu$. By part 2 of Proposition 3.3.15, $\mu(\varphi) = \mu(\psi) < \nu(\psi)$. By part 3 of Proposition 3.3.15, $\mu(\psi - \varphi) \ge \nu(\psi)$. Lemma 3.3.16 with $\gamma = \nu(\psi)$ gives the equality. For the inequality, let $f = \sum_j a_j\varphi^j$ be the $\varphi$-expansion of $f$. Since $\nu(\psi) \le \nu(\varphi)$,
$$[\mu; \varphi, \nu(\psi)](f) = \min_j\big(\mu(a_j) + j\nu(\psi)\big) \le \min_j\big(\mu(a_j) + j\nu(\varphi)\big) = [\mu; \varphi, \nu(\varphi)](f).$$
If $\nu(\psi) = \nu(\varphi)$, the two sides are equal. The values at $\varphi$ follow from the equality and part 2 of Theorem 3.3.5. $\square$

Thus the MacLane chain depends on the choice of each $\varphi_{i+1}$. A choice with a larger value $\nu(\varphi_{i+1})$ gives a larger valuation $\mu_{i+1}$. There need not be a choice with the largest value. In Example 3.3.14 the polynomials $y - b$ with $b \in \mathbb{Q}$ and $v_p(s - b) > \nu(y)$ are possible choices of $\varphi_1$, and their values $\nu(y - b)$ are not bounded. A family of key polynomials of the same degree with increasing values is also the situation of the limit augmentations of Vaquié [Vaq07].

**Example 3.3.18 (two choices of the key polynomial).** Let $p$ be a prime, let $K = \mathbb{Q}$ and let $v$ be the $p$-adic valuation. Let $s = 1 + p + p^2$, and let $\nu(f) = v_p(f(s))$ for $f \in \mathbb{Q}[y]$. Then $\nu$ is a valuation on $\mathbb{Q}[y]$ that extends $v$, with support $(y - s)$. Since $\nu(y) = v_p(s) = 0$, the first valuation of the MacLane chain is $\mu_0 = [v; y, 0]$. The valuations $\mu_0$ and $\nu$ agree on $\mathbb{Q}$, so the monic polynomials of least degree with $\mu_0(f) < \nu(f)$ have degree 1. Let $\varphi = y - 1$ and $\psi = y - 1 - p$. Then
$$\mu_0(\varphi) = \mu_0(\psi) = 0, \quad \nu(\varphi) = v_p(p + p^2) = 1, \quad \nu(\psi) = v_p(p^2) = 2.$$
So both are possible choices of $\varphi_1$. The $\varphi$-expansion of $\psi$ is $(-p) + \varphi$, so
$$[\mu_0; \varphi, 1](\psi) = \min(v(-p), 1) = 1 < 2 = [\mu_0; \psi, 2](\psi).$$
Thus $[\mu_0; \varphi, 1] \ne [\mu_0; \psi, 2]$. The polynomial $y - s$ is a third choice, with $\nu(y - s) = \infty$. With this choice $\mu_1 = \nu$ by part 4 of Lemma 3.3.11, and the chain ends after one step. With the choice $\varphi$, the valuation $\mu_1 = [\mu_0; \varphi, 1]$ is not $\nu$, because $\mu_1(\psi) = 1 < \nu(\psi)$. $\square$

The example shows that the two augmentations of the step of MacLane with two key polynomials of least degree are not equal in general. They are equal if the two values of $\nu$ are equal, by Proposition 3.3.17.

### The graded algebra of an augmentation

We prove the claim on $\operatorname{gr}_{\mu'}$ in part 3 of Theorem 3.3.5. In this section $\varphi$ is a key polynomial for $\mu$ of degree $m$, $\gamma \in \Gamma$ with $\gamma > \mu(\varphi)$, and $\mu' = [\mu; \varphi, \gamma]$. We write $\operatorname{in}$ for $\operatorname{in}_{\mu'}$. By part 1 of Theorem 3.3.5, $\mu'$ has support 0, so $\operatorname{in} f$ is defined for each $f \ne 0$. Let $\Delta \subseteq \operatorname{gr}_{\mu'}$ be the subring generated by the initial forms of the nonzero polynomials of degree less than $m$. For $\delta \in \Gamma$, let $\Delta_\delta$ be the set of the elements $\operatorname{in} a$ with $\deg a < m$ and $\mu'(a) = \delta$, together with 0.

**Proposition 3.3.19 (the graded algebra of an augmentation).**

1. $\Delta = \bigoplus_{\delta \in \Gamma} \Delta_\delta$. Thus the nonzero homogeneous elements of $\Delta$ are the initial forms of the nonzero polynomials of degree less than $m$.
2. Let $f \ne 0$ with $\varphi$-expansion $f = \sum_j a_j\varphi^j$, and let $J$ be the set of the indices $j$ with $\mu(a_j) + j\gamma = \mu'(f)$. Then $f$ is $\mu'$-equivalent to $\sum_{j \in J} a_j\varphi^j$, and
$$\operatorname{in} f = \sum_{j \in J} \operatorname{in}(a_j)\,(\operatorname{in} \varphi)^j.$$
3. Let $c_0, \ldots, c_N \in K[y]$ with $\deg c_j < m$. Then $\mu'\big(\sum_j c_j\varphi^j\big) = \min_j\big(\mu(c_j) + j\gamma\big)$.
4. $\operatorname{in} \varphi$ is transcendental over $\Delta$, and $\operatorname{gr}_{\mu'} = \Delta[\operatorname{in} \varphi]$.

Lean: `Singularity.KeyPolynomial.muEquiv_augmentedValuation_mul_modByMonic` (products in part 1), `Singularity.KeyPolynomial.muEquiv_augmentedValuation_sum_filter`, `Singularity.KeyPolynomial.augmentedValuationFun_sub_sum_filter_lt` (part 2), `Singularity.KeyPolynomial.augmentedValuation_sum_mul_pow`, `Singularity.augmentedValuationFun_sum_mul_pow` (part 3)

*Proof.* Part 1. For $\deg a < m$ we have $\mu'(a) = \mu(a)$ by part 2 of Theorem 3.3.5. Each $\Delta_\delta$ is a subgroup of $P_\delta/P_\delta^+$. Indeed, $-\operatorname{in} a = \operatorname{in}(-a)$. Let $a$ and $b$ be nonzero of degree less than $m$ with $\mu'(a) = \mu'(b) = \delta$. The sum $\operatorname{in} a + \operatorname{in} b$ is the class of $a + b$ in $P_\delta/P_\delta^+$. This class is 0 if $\mu'(a + b) > \delta$, and it is $\operatorname{in}(a + b)$ if $\mu'(a + b) = \delta$. In both cases it is in $\Delta_\delta$, because $\deg(a + b) < m$. Now we show that $\Delta_\delta\Delta_\varepsilon \subseteq \Delta_{\delta + \varepsilon}$. Let $a$ and $b$ be as before, with $\mu'(a) = \delta$ and $\mu'(b) = \varepsilon$. Write $ab = q\varphi + r$ with $\deg r < m$. Since $\deg(ab) \le 2m - 2$, we have $\deg q < m$. By Lemma 3.3.7, $\mu(r) = \mu(ab)$ and $\mu(q\varphi) \ge \mu(ab)$. By part 2 of Theorem 3.3.5 and $\gamma > \mu(\varphi)$, if $q \ne 0$, then
$$\mu'(ab - r) = \mu'(q\varphi) = \mu(q) + \gamma > \mu(q) + \mu(\varphi) = \mu(q\varphi) \ge \mu(ab) = \mu'(ab).$$
The last equality holds because $\mu'(ab) = \mu'(a) + \mu'(b) = \mu(a) + \mu(b)$. If $q = 0$, then $ab = r$. Thus $ab$ is $\mu'$-equivalent to $r$, and $\operatorname{in} a \cdot \operatorname{in} b = \operatorname{in}(ab) = \operatorname{in} r \in \Delta_{\delta + \varepsilon}$. Also $1 = \operatorname{in} 1 \in \Delta_0$. Thus $\bigoplus_\delta \Delta_\delta$ is a subring of $\operatorname{gr}_{\mu'}$. It contains the generators of $\Delta$, and it is contained in $\Delta$. So it is equal to $\Delta$.

Part 2. For each $j$, part 2 of Theorem 3.3.5 gives $\mu'(a_j\varphi^j) = \mu(a_j) + j\gamma$. By Definition 3.3.4, $\mu'(f)$ is the least of these values, so $J$ is not empty, and $\mu'(a_j\varphi^j) > \mu'(f)$ for $j \notin J$. Let $g = \sum_{j \in J} a_j\varphi^j$. Then $f - g = \sum_{j \notin J} a_j\varphi^j$, so $\mu'(f - g) > \mu'(f)$. Thus $f$ is $\mu'$-equivalent to $g$, and $\operatorname{in} f = \operatorname{in} g$. Let $\delta = \mu'(f)$. Each term $a_j\varphi^j$ with $j \in J$ is in $P_\delta$ and has the value $\delta$, so the class of $g$ in $P_\delta/P_\delta^+$ is the sum of the classes $\operatorname{in}(a_j\varphi^j) = \operatorname{in}(a_j)(\operatorname{in} \varphi)^j$.

Part 3. Since $\deg c_j < m$, the sum $\sum_j c_j\varphi^j$ is the $\varphi$-expansion of this polynomial, because the $\varphi$-expansion is unique. Definition 3.3.4 gives the claim.

Part 4. Each nonzero element of $P_\delta/P_\delta^+$ is $\operatorname{in} f$ for some $f$ with $\mu'(f) = \delta$. By part 2 and part 1, it is in $\Delta[\operatorname{in} \varphi]$. Thus $\operatorname{gr}_{\mu'} = \Delta[\operatorname{in} \varphi]$. Now let $P = \sum_{j=0}^N d_jT^j$ be a nonzero polynomial with coefficients $d_j \in \Delta$. We show that $P(\operatorname{in} \varphi) \ne 0$. Choose $k$ with $d_k \ne 0$, and choose $\varepsilon$ such that the component $(d_k)_\varepsilon$ of $d_k$ of degree $\varepsilon$ is not 0. Let $\delta = \varepsilon + k\gamma$. The element $\operatorname{in} \varphi$ is homogeneous of degree $\gamma$, so the component of $P(\operatorname{in} \varphi)$ of degree $\delta$ is
$$\sum_{j=0}^N (d_j)_{\delta - j\gamma}\,(\operatorname{in} \varphi)^j.$$
By part 1, $(d_j)_{\delta - j\gamma} \in \Delta_{\delta - j\gamma}$. Let $J$ be the set of the indices $j$ with $(d_j)_{\delta - j\gamma} \ne 0$. Then $k \in J$, and for $j \in J$ we can write $(d_j)_{\delta - j\gamma} = \operatorname{in} c_j$ with $c_j \ne 0$, $\deg c_j < m$ and $\mu(c_j) = \delta - j\gamma$. Let $h = \sum_{j \in J} c_j\varphi^j$. By part 3, $\mu'(h) = \delta$. As in part 2, the component of degree $\delta$ is the class of $h$ in $P_\delta/P_\delta^+$, and this class is $\operatorname{in} h \ne 0$. Thus $P(\operatorname{in} \varphi) \ne 0$. $\square$

MacLane [Mac36] and Vaquié [Vaq07] give other proofs. The proof of part 1 uses $\gamma > \mu(\varphi)$, and the proof of part 4 uses $\gamma < \infty$. The Lean library has no graded algebra. It states parts 1 to 3 with $\mu'$-equivalence, as in Definition 3.3.3. The product of part 1 is `Singularity.KeyPolynomial.muEquiv_augmentedValuation_mul_modByMonic`, which says that $ab$ is $\mu'$-equivalent to its remainder $r$. Part 2 is `Singularity.KeyPolynomial.muEquiv_augmentedValuation_sum_filter`. The transcendence in part 4 follows from part 3, which is `Singularity.KeyPolynomial.augmentedValuation_sum_mul_pow`, and from the uniqueness of the $\varphi$-expansion, `Singularity.expansionCoeff_sum_mul_pow`.

### Continuous families and limit augmentations

We construct the limit augmentations of part 4 of Theorem 3.3.5 for a family of key polynomials of one degree. We follow Vaquié [Vaq07]. Herrera Govantes, Mahboub, Olalla Acosta and Spivakovsky give the corresponding notions in their approach to key polynomials [HMOS22]. In this section $\mu$ is a valuation on $K[y]$ that extends $v$ and has support 0, as in Definition 3.3.3, and $d \ge 1$.

**Definition 3.3.20 (continuous family).** Let $I$ be a nonempty totally ordered set without a largest element. A *continuous family* of augmentations of $\mu$ of degree $d$ is a family $(\varphi_i, \gamma_i)_{i \in I}$ with these properties.

1. Each $\varphi_i$ is a key polynomial for $\mu$ of degree $d$, and $\gamma_i \in \Gamma$ with $\gamma_i > \mu(\varphi_i)$.
2. $\gamma_i < \gamma_j$ for $i < j$.
3. $\mu(\varphi_j - \varphi_i) \ge \gamma_i$ for $i < j$.

We write $\mu_i = [\mu; \varphi_i, \gamma_i]$.

Lean: `Singularity.ContinuousFamily`

In [Vaq07] and [HMOS22] the index set is well ordered. The proofs below use only a total order.

**Lemma 3.3.21 (the family).** Let $i \le j$ in $I$.

1. $\mu(\varphi_j) = \mu(\varphi_i)$, and $\mu_i = [\mu; \varphi_j, \gamma_i]$.
2. $\mu_i \le \mu_j$, and $\mu_i(\varphi_j) = \gamma_i$.
3. $\mu_j(a) = \mu(a)$ for each $a$ with $\deg a < d$.

Lean: `Singularity.ContinuousFamily.val_apply_eq_of_le`, `Singularity.ContinuousFamily.val_le_val`, `Singularity.ContinuousFamily.val_key_of_le`, `Singularity.ContinuousFamily.val_of_degree_lt`

*Proof.* We can assume that $i < j$. Part 1. Since $\mu(\varphi_j - \varphi_i) \ge \gamma_i > \mu(\varphi_i)$, we get $\mu(\varphi_j) = \mu(\varphi_i) < \gamma_i$. Lemma 3.3.16 with $\gamma = \gamma_i$ gives $[\mu; \varphi_i, \gamma_i] = [\mu; \varphi_j, \gamma_i]$. Part 2. Let $f = \sum_k a_k\varphi_j^k$ be the $\varphi_j$-expansion of $f$. By part 1 and $\gamma_i < \gamma_j$,
$$\mu_i(f) = \min_k\big(\mu(a_k) + k\gamma_i\big) \le \min_k\big(\mu(a_k) + k\gamma_j\big) = \mu_j(f).$$
By part 1 and part 2 of Theorem 3.3.5, $\mu_i(\varphi_j) = \gamma_i$. Part 3 is part 2 of Theorem 3.3.5. $\square$

**Definition 3.3.22 (stable polynomials and the limit).** A polynomial $f \in K[y]$ is *stable* for the family if there is $i \in I$ with $\mu_j(f) = \mu_i(f)$ for each $j \ge i$. Then the *limit* $\mu_\infty(f)$ is this value $\mu_i(f)$. If $f$ is not stable, we set $\mu_\infty(f) = \infty$.

Lean: `Singularity.ContinuousFamily.IsStable`, `Singularity.ContinuousFamily.stableValue`

By part 2 of Lemma 3.3.21, $\mu_\infty(f) \ge \mu_i(f)$ for each $i$, and $\mu_\infty(f) = \sup_i \mu_i(f)$ for each stable $f$. By part 3, each polynomial of degree less than $d$ is stable, with $\mu_\infty(a) = \mu(a)$. If $f$ and $g$ are stable, then there is one index $i$ with $\mu_j(f) = \mu_\infty(f)$ and $\mu_j(g) = \mu_\infty(g)$ for each $j \ge i$. Thus $fg$ is stable, with $\mu_\infty(fg) = \mu_\infty(f) + \mu_\infty(g)$. The same holds for each finite set of stable polynomials.

**Lemma 3.3.23 (stability).** Let $i < j$ in $I$ and $f \in K[y]$ with $\mu_i(f) = \mu_j(f)$. Then $f$ is stable, and $\mu_k(f) = \mu_i(f)$ for each $k \ge i$. If $f \ne 0$ and $r$ is the remainder of $f$ modulo $\varphi_j$, then $\mu_j(f - r) > \mu_j(f) = \mu(r)$. Thus a polynomial $f$ is not stable if and only if $\mu_i(f) < \mu_j(f)$ for all $i < j$.

Lean: `Singularity.ContinuousFamily.val_sub_modByMonic_lt`, `Singularity.ContinuousFamily.val_eq_of_val_eq`, `Singularity.ContinuousFamily.not_isStable_iff`

*Proof.* The claims are clear if $f = 0$. Let $f \ne 0$, and let $f = \sum_k a_k\varphi_j^k$ be the $\varphi_j$-expansion of $f$, so that $a_0 = r$. By Theorem 3.3.5, $\mu_j$ has support 0, so $\mu_j(f) < \infty$. By part 1 of Lemma 3.3.21, for each $k \ge 1$ with $a_k \ne 0$,
$$\mu(a_k) + k\gamma_j > \mu(a_k) + k\gamma_i \ge \mu_i(f) = \mu_j(f).$$
Thus $\mu_j(f - r) = \min_{k \ge 1}\big(\mu(a_k) + k\gamma_j\big) > \mu_j(f)$, and $\mu_j(f) = \mu(a_0) = \mu(r)$. Let $k \in I$ with $k \ge i$. If $k \le j$, then $\mu_i(f) \le \mu_k(f) \le \mu_j(f) = \mu_i(f)$ by part 2 of Lemma 3.3.21. Let $k > j$. By parts 2 and 3 of Lemma 3.3.21, $\mu_k(r) = \mu(r)$ and $\mu_k(f - r) \ge \mu_j(f - r) > \mu(r)$. So $\mu_k(f) = \mu_k(r + (f - r)) = \mu(r) = \mu_i(f)$. For the last claim, let $f$ be not stable and let $i < j$. Then $\mu_i(f) \le \mu_j(f)$ by part 2 of Lemma 3.3.21, and equality is not possible by the first claim. Conversely, if $\mu_i(f) < \mu_j(f)$ for all $i < j$, then $f$ is not stable, because $I$ has no largest element. $\square$

**Proposition 3.3.24 (the limit and $\nu$).** Let $\nu$ be a valuation on $K[y]$ with $\mu_i \le \nu$ for each $i \in I$, and with $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$.

1. $\mu_\infty(f) = \nu(f)$ for each stable $f$.
2. Some polynomial is not stable if and only if there is $f \in K[y]$ with $\mu_i(f) \ne \nu(f)$ for each $i \in I$.

Lean: `Singularity.ContinuousFamily.stableValue_eq_of_isStable` (part 1), `Singularity.ContinuousFamily.exists_not_isStable_iff` (part 2)

*Proof.* Part 1. Let $f$ be stable and choose $i < j$ with $\mu_i(f) = \mu_j(f) = \mu_\infty(f)$. If $f = 0$, both sides are $\infty$. Let $f \ne 0$, and let $r$ be the remainder of $f$ modulo $\varphi_j$. By Lemma 3.3.23, $\mu_j(f - r) > \mu(r) = \mu_\infty(f)$. Since $\deg r < d$, we have $\nu(r) = \mu(r)$. Since $\mu_j \le \nu$, we have $\nu(f - r) \ge \mu_j(f - r) > \nu(r)$. Thus $\nu(f) = \nu(r) = \mu_\infty(f)$.

Part 2. Let $f$ be not stable, and let $i \in I$. Choose $j > i$. By Lemma 3.3.23, $\mu_i(f) < \mu_j(f) \le \nu(f)$. Conversely, assume that each polynomial is stable, and let $f \in K[y]$. By part 1, $\mu_i(f) = \mu_\infty(f) = \nu(f)$ for all large $i$. $\square$

For $i < j$ we have $\mu_i(\varphi_j) = \gamma_i < \gamma_j = \mu_j(\varphi_j) \le \nu(\varphi_j)$. Thus $\mu_i \ne \nu$ for each $i$, for each family below $\nu$. The condition of part 2 says that the family does not reach $\nu$ even polynomial by polynomial. The hypothesis on $\nu$ in degree less than $d$ does not follow from $\mu_i \le \nu$ alone. It holds in the situation of the step of MacLane. Indeed, assume that $\mu \le \nu$, that $\mu \ne \nu$, and that $d$ is the least degree of a monic polynomial $f$ with $\mu(f) < \nu(f)$. Then $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$, by part 1 of Lemma 3.3.9.

**Definition 3.3.25 (limit key polynomial).** Assume that some polynomial is not stable. A *limit key polynomial* for the family is a monic polynomial $\varphi$ that is not stable, such that $\deg \varphi \le \deg f$ for each polynomial $f$ that is not stable. We say that $\varphi$ *divides $f$ in the limit* if there is $i \in I$ such that $\varphi$ $\mu_j$-divides $f$ for each $j \ge i$.

Lean: `Singularity.ContinuousFamily.IsLimitKeyPolynomial`, `Singularity.ContinuousFamily.LimitDvd`

A limit key polynomial exists. Indeed, let $f$ be a polynomial of least degree that is not stable. Then $f \ne 0$, because $0$ is stable. Let $c$ be the leading coefficient of $f$. If $c^{-1}f$ were stable, then $f = c \cdot c^{-1}f$ would be stable, because the constant $c$ is stable. So $c^{-1}f$ is a limit key polynomial.

**Proposition 3.3.26 (limit key polynomials).** Let $\varphi$ be a limit key polynomial of degree $m$.

1. $m \ge d$, and each polynomial of degree less than $m$ is stable.
2. $\mu_i(\varphi) < \mu_j(\varphi)$ for all $i < j$.
3. $\varphi$ divides $f$ in the limit if and only if $f$ is not stable.
4. $\varphi$ does not divide 1 in the limit. If $\varphi$ divides $fg$ in the limit, then $\varphi$ divides $f$ or $g$ in the limit. If $\varphi$ divides $f$ in the limit, then $\deg f \ge m$.

Lean: `Singularity.ContinuousFamily.exists_isLimitKeyPolynomial` (existence), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.isStable_of_degree_lt` (part 1), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.val_lt` (part 2), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitDvd_iff` (part 3), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.not_limitDvd_one`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitDvd_or_limitDvd`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.natDegree_le_of_limitDvd` (part 4)

*Proof.* Part 1. The polynomials of degree less than $d$ are stable, so $m \ge d$. A nonzero polynomial of degree less than $m$ is stable by the choice of $\varphi$, and $0$ is stable. Part 2 is Lemma 3.3.23.

Part 3. Assume that $\varphi$ divides $f$ in the limit and that $f$ is stable. Choose $k$ such that $\varphi$ $\mu_k$-divides $f$ and $\mu_l(f) = \mu_\infty(f)$ for each $l \ge k$. Then there is $h$ with $\mu_k(f - \varphi h) > \mu_k(f)$. In particular $\mu_k(f) < \infty$ and $\mu_k(\varphi h) = \mu_k(f)$, so $\mu_k(h) < \infty$. Choose $l > k$. By part 2 and Lemma 3.3.21,
$$\mu_l(\varphi h) = \mu_l(\varphi) + \mu_l(h) > \mu_k(\varphi) + \mu_k(h) = \mu_k(f), \quad \mu_l(f - \varphi h) \ge \mu_k(f - \varphi h) > \mu_k(f).$$
Thus $\mu_l(f) > \mu_k(f)$, which contradicts $\mu_l(f) = \mu_k(f)$.

Conversely, let $f$ be not stable. Write $f = r + \varphi q$ with $\deg r < m$. By part 1, $r$ is stable. Choose $i_0$ with $\mu_j(r) = \mu_\infty(r)$ for each $j \ge i_0$. First assume that there is $i$ with $\mu_j(\varphi q) < \mu_\infty(r)$ for each $j \ge i$. Let $j \ge i$ and $j \ge i_0$. Then $\mu_j(\varphi q) < \mu_j(r)$, so $\mu_j(f) = \mu_j(\varphi q)$ and
$$\mu_j(f - \varphi q) = \mu_j(r) > \mu_j(\varphi q) = \mu_j(f).$$
Thus $\varphi$ $\mu_j$-divides $f$ for each such $j$, and $\varphi$ divides $f$ in the limit. Now assume that for each $i$ there is $j \ge i$ with $\mu_j(\varphi q) \ge \mu_\infty(r)$. We show that $f$ is stable, which is a contradiction. Choose such a $j$ with $j \ge i_0$. If $\mu_\infty(r) = \infty$, then $\mu_j(\varphi q) = \infty$, and for each $l \ge j$ we get $\mu_l(f) \ge \min(\mu_l(r), \mu_l(\varphi q)) \ge \min(\mu_\infty(r), \mu_j(\varphi q)) = \infty$. So $f$ is stable. Let $\mu_\infty(r) < \infty$, and choose $k > j$. If $\mu_j(q) = \infty$, then $\mu_k(\varphi q) = \infty > \mu_\infty(r)$. Otherwise part 2 gives
$$\mu_k(\varphi q) = \mu_k(\varphi) + \mu_k(q) > \mu_j(\varphi) + \mu_j(q) = \mu_j(\varphi q) \ge \mu_\infty(r).$$
For each $l \ge k$ we get $\mu_l(\varphi q) \ge \mu_k(\varphi q) > \mu_\infty(r) = \mu_l(r)$, so $\mu_l(f) = \mu_\infty(r)$. Thus $f$ is stable.

Part 4. The polynomial 1 is stable, so $\varphi$ does not divide 1 in the limit by part 3. If $f$ and $g$ are stable, then $fg$ is stable. So if $\varphi$ divides $fg$ in the limit, then $fg$ is not stable by part 3, so $f$ or $g$ is not stable, and $\varphi$ divides $f$ or $g$ in the limit by part 3. If $\varphi$ divides $f$ in the limit, then $f$ is not stable, so $\deg f \ge m$ by the choice of $\varphi$. $\square$

Part 4 says that $\varphi$ is irreducible and minimal for the divisibility in the limit. These are the properties that Vaquié uses to define the limit key polynomials [Vaq07]. We do not prove the converse, that each monic polynomial with these properties has the least degree among the polynomials that are not stable.

**Lemma 3.3.27 (the limit in degree less than $m$).** Let $\varphi$ be a limit key polynomial of degree $m$, and let $\gamma \in \Gamma \cup \{\infty\}$ with $\gamma \ge \mu_i(\varphi)$ for each $i \in I$.

1. Let $x_1, \ldots, x_n \in K[y]$ with $\deg x_t < m$. Then $\mu_\infty(x_1 + \cdots + x_n) \ge \min_t \mu_\infty(x_t)$. If the minimum is attained at exactly one index $t$, then $\mu_\infty(x_1 + \cdots + x_n) = \mu_\infty(x_t)$.
2. Let $f \in K[y]$, and write $f = q\varphi + r$ with $\deg r < m$. Assume that $f$ and $q$ are stable. Then $\mu_\infty(r) = \mu_\infty(f)$ and $\mu_\infty(q) + \gamma \ge \mu_\infty(f)$.

Lean: `Singularity.ContinuousFamily.IsLimitKeyPolynomial.stableValue_add_le`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.stableValue_add_eq_of_lt` (part 1), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.stableValue_modByMonic`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.stableValue_divByMonic_mul_le` (part 2)

*Proof.* Part 1. The polynomials $x_t$ and $x_1 + \cdots + x_n$ have degree less than $m$, so they are stable by part 1 of Proposition 3.3.26. These are finitely many stable polynomials, so there is $i \in I$ such that $\mu_i$ agrees with $\mu_\infty$ on all of them. Lemma 1.1.3 for the valuation $\mu_i$ gives the claims.

Part 2. By part 1 of Proposition 3.3.26, $r$ is stable. Choose $i \in I$ such that $\mu_k(f) = \mu_\infty(f)$, $\mu_k(r) = \mu_\infty(r)$ and $\mu_k(q) = \mu_\infty(q)$ for each $k \ge i$, and choose $j > i$. Assume that $\mu_\infty(r) \ne \mu_\infty(f)$. Let $k \ge i$. Since $\varphi q = f - r$ and $\mu_k(f) \ne \mu_k(r)$, we get
$$\mu_k(\varphi) + \mu_\infty(q) = \mu_k(\varphi q) = \min\big(\mu_\infty(f), \mu_\infty(r)\big).$$
The right side does not depend on $k$, and it is finite, because $\mu_\infty(f)$ and $\mu_\infty(r)$ are not both $\infty$. So $\mu_\infty(q) < \infty$, and the cases $k = i$ and $k = j$ give $\mu_i(\varphi) = \mu_j(\varphi)$. This contradicts part 2 of Proposition 3.3.26. Thus $\mu_\infty(r) = \mu_\infty(f)$. For the second claim,
$$\mu_\infty(q) + \gamma \ge \mu_i(q) + \mu_i(\varphi) = \mu_i(f - r) \ge \min\big(\mu_i(f), \mu_i(r)\big) = \mu_\infty(f). \quad \square$$

Since the values $\mu_i(\varphi)$ increase strictly, the condition $\gamma \ge \mu_i(\varphi)$ for each $i$ gives $\gamma > \mu_i(\varphi)$ for each $i$. It is the analogue of the condition $\gamma > \mu(\varphi)$ of Definition 3.3.4.

**Definition 3.3.28 (limit augmentation).** Let $\varphi$ be a limit key polynomial of degree $m$, and let $\gamma \in \Gamma \cup \{\infty\}$ with $\gamma \ge \mu_i(\varphi)$ for each $i \in I$. The *limit augmentation* $\mu' = [\mu_\infty; \varphi, \gamma]$ is
$$\mu'\Big(\sum_j a_j\varphi^j\Big) = \min_j\big(\mu_\infty(a_j) + j\gamma\big),$$
with the $\varphi$-expansion on the left and the convention $0 \cdot \gamma = 0$.

Lean: `Singularity.ContinuousFamily.limitAugmentedValuationFun`

The coefficients $a_j$ have degree less than $m$. So they are stable by part 1 of Proposition 3.3.26, and the values $\mu_\infty(a_j)$ are the limits of the values $\mu_i(a_j)$.

**Theorem 3.3.29 (the limit augmentation).** Let $\varphi$, $\gamma$ and $\mu' = [\mu_\infty; \varphi, \gamma]$ be as in Definition 3.3.28.

1. $\mu'$ is a valuation on $K[y]$ that extends $v$. We have $\mu'(a) = \mu_\infty(a)$ for each $a$ with $\deg a < m$, and $\mu'(\varphi) = \gamma$.
2. $\mu_i \le \mu'$ for each $i \in I$.
3. Let $\nu$ be a valuation on $K[y]$ with $\mu_i \le \nu$ for each $i \in I$, and with $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$. If $\gamma \le \nu(\varphi)$, then $\mu' \le \nu$. In particular $\gamma = \nu(\varphi)$ satisfies the condition of Definition 3.3.28, and
$$\mu_i \le [\mu_\infty; \varphi, \nu(\varphi)] \le \nu \quad \text{for each } i \in I.$$

Lean: `Singularity.ContinuousFamily.limitAugmentedValuation`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitAugmentedValuationFun_mul`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitAugmentedValuationFun_add_le_max`, `Singularity.ContinuousFamily.limitAugmentedValuationFun_of_degree_lt`, `Singularity.ContinuousFamily.limitAugmentedValuationFun_self` (part 1), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitAugmentedValuationFun_le` (part 2), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.map_le_limitAugmentedValuationFun`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitAugmentedValuationFun_map_le` (part 3)

*Proof.* Part 1. We follow the proof of parts 1 and 2 of Theorem 3.3.5, with $\mu_\infty$ in place of $\mu$. The $\varphi$-expansion of $f + g$ is the sum of the expansions of $f$ and $g$. So part 1 of Lemma 3.3.27, applied to each coefficient, gives $\mu'(f + g) \ge \min(\mu'(f), \mu'(g))$. For $c$ of degree less than $m$ and $k \ge 0$, the $\varphi$-expansion of $c\varphi^k$ has one term, so $\mu'(c\varphi^k) = \mu_\infty(c) + k\gamma$. In particular $\mu'(a) = \mu_\infty(a)$ if $\deg a < m$, $\mu'(\varphi) = \gamma$, and $\mu'(0) = \infty$. For $c \in K$ we have $\deg c < d \le m$, so $\mu'(c) = \mu(c) = v(c)$ by part 3 of Lemma 3.3.21. Thus $\mu'$ extends $v$.

We show that $\mu'(fg) = \mu'(f) + \mu'(g)$. Let $f = \sum_i a_i\varphi^i$ and $g = \sum_j b_j\varphi^j$, and write $a_ib_j = q_{ij}\varphi + r_{ij}$ with $\deg r_{ij} < m$. Since $\deg(a_ib_j) \le 2m - 2$, we have $\deg q_{ij} < m$. The polynomials $a_i$, $b_j$ and $q_{ij}$ are stable by part 1 of Proposition 3.3.26, so $a_ib_j$ is stable with $\mu_\infty(a_ib_j) = \mu_\infty(a_i) + \mu_\infty(b_j)$. By part 2 of Lemma 3.3.27,
$$\mu_\infty(r_{ij}) = \mu_\infty(a_i) + \mu_\infty(b_j), \quad \mu_\infty(q_{ij}) + \gamma \ge \mu_\infty(a_i) + \mu_\infty(b_j).$$
Now $fg = \sum_{i,j}\big(r_{ij}\varphi^{i+j} + q_{ij}\varphi^{i+j+1}\big)$. By the uniqueness of the $\varphi$-expansion, the coefficient of $\varphi^k$ in the expansion of $fg$ is
$$c_k = \sum_{i + j = k} r_{ij} + \sum_{i + j = k - 1} q_{ij}.$$
For a term $r_{ij}$ of $c_k$ we have $\mu_\infty(r_{ij}) + k\gamma = \big(\mu_\infty(a_i) + i\gamma\big) + \big(\mu_\infty(b_j) + j\gamma\big)$. For a term $q_{ij}$ of $c_k$ we have
$$\mu_\infty(q_{ij}) + k\gamma = \mu_\infty(q_{ij}) + \gamma + (i + j)\gamma \ge \big(\mu_\infty(a_i) + i\gamma\big) + \big(\mu_\infty(b_j) + j\gamma\big).$$
In both cases the right side is at least $\mu'(f) + \mu'(g)$. By part 1 of Lemma 3.3.27, $\mu_\infty(c_k) + k\gamma \ge \mu'(f) + \mu'(g)$ for each $k$, so $\mu'(fg) \ge \mu'(f) + \mu'(g)$.

For the other inequality we can assume that $\mu'(f)$ and $\mu'(g)$ are finite. Let $i_0$ be the least index with $\mu_\infty(a_{i_0}) + i_0\gamma = \mu'(f)$, let $j_0$ be the least index with $\mu_\infty(b_{j_0}) + j_0\gamma = \mu'(g)$, and let $k = i_0 + j_0$. The term $r_{i_0j_0}$ of $c_k$ has $\mu_\infty(r_{i_0j_0}) + k\gamma = \mu'(f) + \mu'(g)$, and this value is finite. Let $t$ be another term of $c_k$. Then $t = r_{ij}$ with $i + j = k$ and $(i, j) \ne (i_0, j_0)$, or $t = q_{ij}$ with $i + j = k - 1$. In both cases $i < i_0$ or $j < j_0$. If $i < i_0$, then $\mu_\infty(a_i) + i\gamma > \mu'(f)$, and if $j < j_0$, then $\mu_\infty(b_j) + j\gamma > \mu'(g)$. With the inequalities above, $\mu_\infty(t) + k\gamma > \mu'(f) + \mu'(g) = \mu_\infty(r_{i_0j_0}) + k\gamma$. Since $k\gamma$ is finite, $\mu_\infty(t) > \mu_\infty(r_{i_0j_0})$. By part 1 of Lemma 3.3.27, $\mu_\infty(c_k) = \mu_\infty(r_{i_0j_0})$. Thus $\mu'(fg) \le \mu_\infty(c_k) + k\gamma = \mu'(f) + \mu'(g)$.

Part 2. Let $i \in I$. By part 1 of Proposition 3.3.26, $d \le m$. Let $a$ have degree less than $d$. Then $\mu'(a) = \mu_\infty(a) = \mu(a)$ by part 1 of the theorem and part 3 of Lemma 3.3.21. We show that $\mu'(\varphi_i) \ge \gamma_i$. If $\deg \varphi_i < m$, then $\mu'(\varphi_i) = \mu_\infty(\varphi_i) \ge \mu_i(\varphi_i) = \gamma_i$. Let $\deg \varphi_i = m$, so $m = d$, and let $a = \varphi - \varphi_i$. The two polynomials are monic of degree $d$, so $\deg a < d$. Assume that $\mu(a) < \gamma_i$. For each $j \ge i$, part 2 of Lemma 3.3.21 gives $\mu_j(\varphi_i) \ge \mu_i(\varphi_i) = \gamma_i > \mu(a) = \mu_j(a)$, so $\mu_j(\varphi) = \mu_j(\varphi_i + a) = \mu(a)$. Then $\varphi$ is stable, and this is a contradiction. So $\mu(a) \ge \gamma_i$. Then
$$\gamma \ge \mu_i(\varphi) \ge \min\big(\mu_i(\varphi_i), \mu_i(a)\big) = \min\big(\gamma_i, \mu(a)\big) = \gamma_i,$$
and $\mu'(\varphi_i) \ge \min(\mu'(\varphi), \mu'(a)) = \min(\gamma, \mu(a)) \ge \gamma_i$. Now let $f = \sum_k c_k\varphi_i^k$ be the $\varphi_i$-expansion of $f$. Since $\deg c_k < d$,
$$\mu'(f) \ge \min_k\big(\mu'(c_k) + k\mu'(\varphi_i)\big) \ge \min_k\big(\mu(c_k) + k\gamma_i\big) = \mu_i(f).$$

Part 3. Let $f = \sum_j a_j\varphi^j$ be the $\varphi$-expansion of $f$. Each $a_j$ is stable, so $\nu(a_j) = \mu_\infty(a_j)$ by part 1 of Proposition 3.3.24. Since $\nu(\varphi) \ge \gamma$,
$$\nu(f) \ge \min_j\big(\nu(a_j) + j\nu(\varphi)\big) \ge \min_j\big(\mu_\infty(a_j) + j\gamma\big) = \mu'(f).$$
Since $\mu_i \le \nu$, we have $\nu(\varphi) \ge \mu_i(\varphi)$ for each $i$. So $\gamma = \nu(\varphi)$ satisfies the condition of Definition 3.3.28, and part 2 gives the last claim. $\square$

The proof of part 1 does not use the strict inequality $\gamma > \mu_i(\varphi)$. The strict inequality for the terms $q_{ij}$ comes from the least indices $i_0$ and $j_0$. In the proof of Theorem 3.3.5 it came from $\gamma > \mu(\varphi)$.

We prove in the next subsection that $\varphi$ is a key polynomial for $\mu'$. We do not describe $\operatorname{gr}_{\mu'}$. The last subsection of this part builds a chain with limit steps from these augmentations (Theorems 3.3.43 to 3.3.46). It is not indexed by an ordinal, and for $\nu$ with support 0 and values that are not discrete we do not prove that it reaches $\nu$.

### Key polynomials for the limit augmentation

In this subsection $\varphi$ is a limit key polynomial of degree $m$, $\gamma \in \Gamma \cup \{\infty\}$ with $\gamma \ge \mu_i(\varphi)$ for each $i \in I$, and $\mu' = [\mu_\infty; \varphi, \gamma]$ is the limit augmentation of Definition 3.3.28. We use the elementwise form of $\mu'$-divisibility: $\varphi$ $\mu'$-divides $f$ if there is $h$ with $\mu'(f - \varphi h) > \mu'(f)$. As for Theorem 3.3.5, this is the form of the Lean library.

**Lemma 3.3.30 (divisibility by $\varphi$ in the limit augmentation).** Let $f \in K[y]$, and let $r$ be the remainder of $f$ modulo $\varphi$.

1. $\mu_\infty(r) \ge \mu'(f)$, and $\varphi$ $\mu'$-divides $f$ if and only if $\mu_\infty(r) > \mu'(f)$.
2. Let $a, b \in K[y]$ with $\deg a < m$ and $\deg b < m$, and let $s$ be the remainder of $ab$ modulo $\varphi$. Then $\mu_\infty(s) = \mu_\infty(a) + \mu_\infty(b)$.

Lean: `Singularity.ContinuousFamily.stableValue_modByMonic_le_limitAugmentedValuationFun`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.muDvd_iff_of_forall_eq` (part 1), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.stableValue_mul_modByMonic` (part 2)

*Proof.* Part 1. The remainder $r$ is the coefficient $a_0$ of the $\varphi$-expansion $f = \sum_j a_j\varphi^j$. So $\mu'(f) \le \mu_\infty(a_0) + 0 \cdot \gamma = \mu_\infty(r)$. Assume that $\varphi$ $\mu'$-divides $f$, and choose $h$ with $\mu'(f - \varphi h) > \mu'(f)$. The remainder of $f - \varphi h$ modulo $\varphi$ is also $r$. By the first claim, applied to $f - \varphi h$, we get $\mu_\infty(r) \ge \mu'(f - \varphi h) > \mu'(f)$. Conversely, assume that $\mu_\infty(r) > \mu'(f)$, and let $h$ be the quotient of $f$ by $\varphi$. Then $f - \varphi h = r$. Since $\deg r < m$, part 1 of Theorem 3.3.29 gives $\mu'(r) = \mu_\infty(r)$. Thus $\mu'(f - \varphi h) > \mu'(f)$, and $\varphi$ $\mu'$-divides $f$.

Part 2. By part 1 of Proposition 3.3.26, $a$ and $b$ are stable. So $ab$ is stable, with $\mu_\infty(ab) = \mu_\infty(a) + \mu_\infty(b)$. Write $ab = q\varphi + s$. Since $\deg(ab) \le 2m - 2$, we have $\deg q < m$, so $q$ is stable. Part 2 of Lemma 3.3.27 gives $\mu_\infty(s) = \mu_\infty(ab)$. $\square$

**Theorem 3.3.31 (the limit key polynomial is a key polynomial).** The polynomial $\varphi$ is $\mu'$-irreducible and $\mu'$-minimal. Thus $\varphi$ is a key polynomial for $\mu'$ if $\gamma < \infty$.

Lean: `Singularity.ContinuousFamily.IsLimitKeyPolynomial.keyPolynomial_of_forall_eq`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.keyPolynomial_limitAugmentedValuation`

*Proof.* We follow the proof of part 3 of Theorem 3.3.5, with $\mu_\infty$ in place of $\mu$. Let $f \ne 0$ with $\deg f < m$. Then $f$ is its own remainder, and $\mu'(f) = \mu_\infty(f)$ by part 1 of Theorem 3.3.29. By part 1 of Lemma 3.3.30, $\varphi$ does not $\mu'$-divide $f$. Thus $\varphi$ is $\mu'$-minimal. In particular $\varphi$ does not $\mu'$-divide 1.

Now let $f, g \in K[y]$, and assume that $\varphi$ $\mu'$-divides neither $f$ nor $g$. Let $a$ and $b$ be the remainders of $f$ and $g$ modulo $\varphi$. By part 1 of Lemma 3.3.30 and its first claim, $\mu_\infty(a) = \mu'(f)$ and $\mu_\infty(b) = \mu'(g)$. The remainder $s$ of $fg$ modulo $\varphi$ is the remainder of $ab$. By part 2 of Lemma 3.3.30, $\mu_\infty(s) = \mu'(f) + \mu'(g)$. By part 1 of Theorem 3.3.29 this is $\mu'(fg)$. By part 1 of Lemma 3.3.30, $\varphi$ does not $\mu'$-divide $fg$. Thus $\varphi$ is $\mu'$-irreducible.

Let $\gamma < \infty$. We show that $\mu'$ has support 0, so that Definition 3.3.3 applies. Let $f \ne 0$ with $\varphi$-expansion $\sum_j a_j\varphi^j$, and choose $j$ with $a_j \ne 0$. The polynomial $a_j$ is stable, so $\mu_\infty(a_j) = \mu_k(a_j)$ for some $k \in I$. This value is finite, because $\mu_k$ has support 0 by part 1 of Theorem 3.3.5. Thus $\mu'(f) \le \mu_\infty(a_j) + j\gamma < \infty$. $\square$

The theorem needs no hypothesis beyond the hypotheses of Definition 3.3.28, which make $\mu'$ a valuation. The proof uses only Lemma 3.3.27 and the equality $\mu'(a) = \mu_\infty(a)$ for $\deg a < m$. For $\gamma = \infty$ we have $\mu'(f) = \mu_\infty(r)$, so $\varphi$ $\mu'$-divides no polynomial, and the two conditions hold trivially. The Lean form includes this case.

Now let $\nu$ be a valuation on $K[y]$ with $\mu_i \le \nu$ for each $i \in I$, and with $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$, as in part 3 of Theorem 3.3.29. The limit key polynomial is not unique. The next results say which limit key polynomial gives a limit augmentation $[\mu_\infty; \varphi, \nu(\varphi)]$ that agrees with $\nu$ up to degree $m$.

**Proposition 3.3.32 (other limit key polynomials).** Let $\psi$ be a monic polynomial of degree $m$ with $\nu(\psi) \ge \nu(\varphi)$. Then $\psi$ is a limit key polynomial.

Lean: `Singularity.ContinuousFamily.IsLimitKeyPolynomial.of_map_le`

*Proof.* Let $s = \psi - \varphi$. The two polynomials are monic of degree $m$, so $\deg s < m$, and $s$ is stable by part 1 of Proposition 3.3.26. We have $\nu(s) \ge \min(\nu(\psi), \nu(\varphi)) = \nu(\varphi)$. Assume that $\psi$ is stable. By part 1 of Proposition 3.3.24, $\mu_\infty(\psi) = \nu(\psi)$ and $\mu_\infty(s) = \nu(s)$. Choose $i \in I$ with $\mu_j(\psi) = \nu(\psi)$ and $\mu_j(s) = \nu(s)$ for each $j \ge i$. For $j \ge i$,
$$\mu_j(\varphi) = \mu_j(\psi - s) \ge \min\big(\nu(\psi), \nu(s)\big) \ge \nu(\varphi) \ge \mu_j(\varphi).$$
Thus $\mu_j(\varphi) = \nu(\varphi)$ for each $j \ge i$, and $\varphi$ is stable. This is a contradiction. So $\psi$ is monic and not stable, and $\deg \psi = m \le \deg f$ for each polynomial $f$ that is not stable. $\square$

**Theorem 3.3.33 (the limit step).** Let $\mu' = [\mu_\infty; \varphi, \nu(\varphi)]$. Then $\mu'(f) = \nu(f)$ for each $f$ with $\deg f \le m$ if and only if $\nu(\varphi) \ge \nu(\psi)$ for each monic polynomial $\psi$ of degree $m$. In this case $\varphi$ is $\mu'$-irreducible and $\mu'$-minimal, and $\mu_i \le \mu' \le \nu$ for each $i \in I$.

Lean: `Singularity.ContinuousFamily.IsLimitKeyPolynomial.forall_limitAugmentedValuationFun_eq_iff`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitAugmentedValuationFun_eq_of_natDegree_le`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.map_le_of_forall_eq`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitStep`

*Proof.* By part 3 of Theorem 3.3.29, $\gamma = \nu(\varphi)$ satisfies the condition of Definition 3.3.28, and $\mu' \le \nu$. Assume that $\nu(\varphi) \ge \nu(\psi)$ for each monic $\psi$ of degree $m$, and let $\deg f \le m$. The quotient of $f$ by $\varphi$ has degree at most 0, so $f = c\varphi + r$ with $c \in K$ and $\deg r < m$. We show that $\nu(c\varphi) \ge \nu(f)$. This is clear if $c = 0$. If $c \ne 0$, then $f = c\psi$ with $\psi = \varphi + c^{-1}r$ monic of degree $m$, so $\nu(f) = \nu(c) + \nu(\psi) \le \nu(c) + \nu(\varphi) = \nu(c\varphi)$. Then $\nu(r) = \nu(f - c\varphi) \ge \min(\nu(f), \nu(c\varphi)) = \nu(f)$. The polynomials $r$ and $c$ have degree less than $m$. By part 1 of Theorem 3.3.29, part 1 of Proposition 3.3.26 and part 1 of Proposition 3.3.24, $\mu'(r) = \mu_\infty(r) = \nu(r)$ and $\mu'(c) = \nu(c)$. Also $\mu'(\varphi) = \nu(\varphi)$. So
$$\mu'(f) \ge \min\big(\mu'(r), \mu'(c\varphi)\big) = \min\big(\nu(r), \nu(c\varphi)\big) \ge \nu(f).$$
With $\mu' \le \nu$ we get $\mu'(f) = \nu(f)$.

Conversely, assume that $\mu'$ and $\nu$ agree in degree at most $m$, and let $\psi$ be monic of degree $m$. The $\varphi$-expansion of $\psi$ is $\psi = (\psi - \varphi) + 1 \cdot \varphi$, with the coefficient $a_1 = 1$. So $\nu(\psi) = \mu'(\psi) \le \mu_\infty(1) + \nu(\varphi) = \nu(\varphi)$.

The last claim is Theorem 3.3.31 and parts 2 and 3 of Theorem 3.3.29. $\square$

By Proposition 3.3.32, a monic polynomial of degree $m$ with the largest value $\nu(\psi)$ among the monic polynomials of degree $m$, if it exists, is a limit key polynomial. For such a choice of $\varphi$, Theorem 3.3.33 gives one limit step of the chain of part 4 of Theorem 3.3.5: the limit augmentation $\mu'$ lies between the family and $\nu$, it has the key polynomial $\varphi$, and it agrees with $\nu$ up to degree $m$. This is the analogue of Lemma 3.3.9. For an arbitrary limit key polynomial the agreement up to degree $m$ is false: if $\nu(\varphi) < \nu(\psi)$ for some monic $\psi$ of degree $m$, then $\mu'(\psi) \le \nu(\varphi) < \nu(\psi)$. We do not prove that the largest value is attained. If the set of values $\nu(\psi)$ has no largest element, then no limit augmentation $[\mu_\infty; \varphi, \nu(\varphi)]$ agrees with $\nu$ up to degree $m$, by Theorem 3.3.33. The chain of Theorem 3.3.44 does not need agreement up to degree $m$ at a limit step. A limit step with an arbitrary limit key polynomial agrees with $\nu$ in degree less than $m$, and the next round of Theorem 3.3.43 treats the degree $m$.

### The discrete case

We return to the case of Theorem 3.3.12, in which the values of $\nu$ are discrete. MacLane proved part 4 of Theorem 3.3.5 without limit augmentations for discrete valuations $v$ and $\nu$ of rank 1 [Mac36]. We show that in this case the limit augmentations of Vaquié give nothing new. A limit step can only be the last step of a chain, and it gives $\nu$. The discreteness enters the proofs at one point only, which is the next lemma.

**Lemma 3.3.34 (increasing values).** Let $\nu$ be a valuation on $K[y]$ whose values are discrete: for $\alpha, \beta \in \Gamma$, only finitely many values of $\nu$ lie in the interval $[\alpha, \beta]$. Let $I$ be a nonempty totally ordered set without a largest element, and let $(s_i)_{i \in I}$ be values of $\nu$ with $s_i < s_j$ for $i < j$. Then for each $\beta \in \Gamma$ there is $i \in I$ with $s_j > \beta$ for each $j \ge i$.

Lean: `Singularity.false_of_strictAnti_of_noMaxOrder`, `Singularity.false_of_strictAnti`

*Proof.* It is sufficient to find $i$ with $s_i > \beta$, because $s_j \ge s_i$ for $j \ge i$. Assume that $s_i \le \beta$ for each $i \in I$. Choose $i_0 \in I$. Since $I$ has no largest element, we can choose $i_{n+1} > i_n$ for each $n \ge 0$. Then $s_{i_0} < s_{i_1} < s_{i_2} < \cdots \le \beta$. In particular $s_{i_0} < \beta$, so $s_{i_0} \in \Gamma$. The elements $s_{i_n}$ are infinitely many distinct values of $\nu$ in the interval $[s_{i_0}, \beta]$. This contradicts the hypothesis. $\square$

The hypothesis holds if $\nu$ has values in $\mathbb{Z} \cup \{\infty\}$, because an interval $[\alpha, \beta]$ of $\mathbb{Z}$ is finite. Thus Theorem 3.3.12 holds for each valuation $\nu$ with values in $\mathbb{Z} \cup \{\infty\}$ that extends $v$.

Lean: `Singularity.finite_Icc_inter_range_int`, `Singularity.macLaneChain_eventually_eq_int`

**Proposition 3.3.35 (the values of an infinite chain).** Let $\nu$ and $(\mu_i)$ be as in Theorem 3.3.12. Assume that $\mu_i \ne \nu$ for each $i$, and that the degrees $\deg \varphi_i$ are bounded. Then $\nu(\varphi_i)$ tends to $\infty$: for each $\beta \in \Gamma$ we have $\nu(\varphi_i) > \beta$ for all large $i$. This holds in particular if $\nu(F) = \infty$ for some $F \ne 0$.

Lean: `Singularity.macLaneChainKey_eventually_lt`, `Singularity.macLaneChainKey_eventually_lt_of_map_eq_zero`

*Proof.* As in the proof of Proposition 3.3.13, there are $N \ge 1$ and $m$ with $\deg \varphi_i = m$ for each $i \ge N$, and $\nu(\varphi_i) < \nu(\varphi_{i+1})$ for each $i \ge N$ by part 5 of Lemma 3.3.11. Lemma 3.3.34 for the index set $\{i : i \ge N\}$ and the values $s_i = \nu(\varphi_i)$ gives the first claim. If $\nu(F) = \infty$ with $F \ne 0$, then the degrees are bounded by $\deg F$, by part 6 of Lemma 3.3.11. $\square$

Proposition 3.3.13 is a consequence of Proposition 3.3.35. In Example 3.3.14 with $s$ algebraic, the values $\nu(\varphi_i)$ tend to $\infty$.

Now let $(\varphi_i, \gamma_i)_{i \in I}$ be a continuous family of augmentations of $\mu$ of degree $d$, as in Definition 3.3.20, with $\mu_i = [\mu; \varphi_i, \gamma_i]$.

**Theorem 3.3.36 (continuous families for discrete values).** Let $\nu$ be a valuation on $K[y]$ whose values are discrete, as in Lemma 3.3.34. Assume that $\mu_i \le \nu$ for each $i \in I$, that $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$, and that each $\gamma_i$ is a value of $\nu$.

1. For each $\beta \in \Gamma$ we have $\gamma_i > \beta$ for all large $i$.
2. Each $f$ with $\nu(f) < \infty$ is stable, and $\mu_i(f) = \nu(f)$ for all large $i$.
3. If $\nu$ has support 0, then each polynomial is stable, $\mu_\infty = \nu$, and the family has no limit key polynomial.
4. Let $\varphi$ be a limit key polynomial. Then $\nu(\varphi) = \infty$. If $\gamma \in \Gamma \cup \{\infty\}$ and $\gamma \ge \mu_i(\varphi)$ for each $i \in I$, then $\gamma = \infty$. The limit augmentation $[\mu_\infty; \varphi, \infty]$ is $\nu$.

Lean: `Singularity.ContinuousFamily.eventually_value_lt` (part 1), `Singularity.ContinuousFamily.isStable_of_map_ne_zero`, `Singularity.ContinuousFamily.eventually_val_eq_of_map_ne_zero` (part 2), `Singularity.ContinuousFamily.isStable_of_supp_eq_bot`, `Singularity.ContinuousFamily.stableValue_eq_of_supp_eq_bot`, `Singularity.ContinuousFamily.not_isLimitKeyPolynomial` (part 3), `Singularity.ContinuousFamily.IsLimitKeyPolynomial.map_eq_zero`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.eq_zero_of_le`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitAugmentedValuationFun_eq_of_le`, `Singularity.ContinuousFamily.IsLimitKeyPolynomial.limitAugmentedValuation_eq` (part 4)

*Proof.* First we show that each value $\mu_i(f)$ is a value of $\nu$. If $f = 0$, then $\mu_i(f) = \infty = \nu(0)$. Let $f \ne 0$, and let $f = \sum_k a_k\varphi_i^k$ be the $\varphi_i$-expansion of $f$. By Definition 3.3.4, $\mu_i(f) = \mu(a_k) + k\gamma_i$ for some $k$. Since $\deg a_k < d$, we have $\mu(a_k) = \nu(a_k)$. Choose $g$ with $\gamma_i = \nu(g)$. Then $\mu_i(f) = \nu(a_k) + k\nu(g) = \nu(a_kg^k)$.

Part 1. By Definition 3.3.20, the values $\gamma_i$ increase strictly. Lemma 3.3.34 for $s_i = \gamma_i$ gives the claim.

Part 2. Let $f$ be a polynomial that is not stable. By Lemma 3.3.23, $\mu_i(f) < \mu_j(f)$ for $i < j$. These are values of $\nu$, and $\mu_i(f) \le \nu(f)$ for each $i$. If $\nu(f) < \infty$, Lemma 3.3.34 with $\beta = \nu(f)$ gives a contradiction. So each $f$ with $\nu(f) < \infty$ is stable. Then there is $i$ with $\mu_j(f) = \mu_\infty(f)$ for each $j \ge i$, and $\mu_\infty(f) = \nu(f)$ by part 1 of Proposition 3.3.24.

Part 3. If $\nu$ has support 0, then $\nu(f) < \infty$ for each $f \ne 0$, and $0$ is stable. So each polynomial is stable by part 2, and $\mu_\infty = \nu$ by part 1 of Proposition 3.3.24. A limit key polynomial is not stable by Definition 3.3.25, so there is none.

Part 4. The polynomial $\varphi$ is not stable, so $\nu(\varphi) = \infty$ by part 2. Let $\gamma \ge \mu_i(\varphi)$ for each $i$, and assume that $\gamma < \infty$. By part 2 of Proposition 3.3.26, $\mu_i(\varphi) < \mu_j(\varphi)$ for $i < j$. These are values of $\nu$, and they are at most $\gamma$. This contradicts Lemma 3.3.34 with $\beta = \gamma$. So $\gamma = \infty$. Let $\mu' = [\mu_\infty; \varphi, \infty]$, let $f \in K[y]$, and write $f = q\varphi + r$ with $\deg r < m$, where $m = \deg \varphi$. In Definition 3.3.28 the terms with $j \ge 1$ are $\infty$, so $\mu'(f) = \mu_\infty(r)$. By part 1 of Proposition 3.3.26, $r$ is stable, so $\mu_\infty(r) = \nu(r)$ by part 1 of Proposition 3.3.24. Since $\nu(q\varphi) = \infty$, we have $\nu(f) = \nu(r)$. Thus $\mu'(f) = \nu(f)$. $\square$

If $\gamma_i = \nu(\varphi_i)$ for each $i$, as for the steps of the chain of MacLane, then each $\gamma_i$ is a value of $\nu$. By part 3 of Theorem 3.3.29, $\gamma = \nu(\varphi)$ is the value of the limit step, and Theorem 3.3.36 says that $\nu(\varphi) = \infty$ and that the limit step gives $\nu$. If $\nu$ has support 0, there is no limit step. So for $\nu$ with discrete values, part 4 of Theorem 3.3.5 has the form of MacLane [Mac36]. The chain of ordinary augmentations is finite and ends with $\nu$, or $\nu$ is its limit, by Theorem 3.3.12. A limit augmentation can only be a last step, and it gives $\nu$. In the second case the statement of Theorem 3.3.12 is the strongest one. Let $\nu$ have the support $(F)$ with $F \ne 0$, and let the chain be infinite, as in Example 3.3.14 with $s$ algebraic. Each $\mu_i$ has support 0 by the construction of the chain, so $\mu_i(F) < \infty = \nu(F)$ for each $i$. Thus $\mu_i(f) = \nu(f)$ for all large $i$ holds only for $f$ with $\nu(f) < \infty$. For $f = F$ the values $\mu_i(F)$ tend to $\infty$.

### The chain with limit steps

We now build the chain of part 4 of Theorem 3.3.5 with limit steps, for a valuation $\nu$ with arbitrary values. Theorem 3.3.12 needs discrete values. Without this hypothesis we do not choose the key polynomials of one degree one at a time. We use all monic polynomials of one degree at once, as in the complete families of Vaquié [Vaq07]. In this subsection $\nu$ is a valuation on $K[y]$ that extends $v$.

First we note a fact on the support. Let $\mu$ be a valuation on $K[y]$ that extends $v$, with $\mu \le \nu$ and $\mu \ne \nu$. Then $\mu$ has support 0. Indeed, assume that $\mu(G) = \infty$ for some $G \ne 0$. The support $\mathfrak p$ of $\mu$ is a nonzero prime ideal of $K[y]$, so it is maximal. Since $\mu \le \nu$, the support of $\nu$ contains $\mathfrak p$. It is a prime ideal different from $K[y]$, because $\nu(1) = 0$, so it is $\mathfrak p$. Let $f \notin \mathfrak p$, and choose $g$ with $fg - 1 \in \mathfrak p$. Then $\mu(fg - 1) = \nu(fg - 1) = \infty$, so $\mu(f) + \mu(g) = \mu(1) = 0$ and $\nu(f) + \nu(g) = 0$. Since $\mu(f) \le \nu(f)$ and $\mu(g) \le \nu(g)$, we get $\mu(f) = \nu(f)$. For $f \in \mathfrak p$ both values are $\infty$. So $\mu = \nu$, and this is a contradiction. Thus Lemma 3.3.9 applies to each valuation $\mu \le \nu$ that extends $v$ with $\mu \ne \nu$, and Definition 3.3.20 applies to $\mu$. The Lean forms do not need this fact, because the Lean forms of Lemma 3.3.9 and Definition 3.3.20 do not ask for support 0.

**Definition 3.3.37 (step of MacLane-Vaquié).** Let $\mu$ and $\mu'$ be valuations on $K[y]$. A *step of MacLane-Vaquié* from $\mu$ to $\mu'$ towards $\nu$ is one of the following.

1. An *ordinary step*. We have $\mu \le \nu$, and $\varphi$ is a monic polynomial with $\mu(\varphi) < \nu(\varphi)$ and $\mu(f) = \nu(f)$ for each $f$ with $\deg f < \deg \varphi$. Then $\mu' = [\mu; \varphi, \nu(\varphi)]$.
2. A *limit step*. There are a continuous family $(\varphi_i, \gamma_i)_{i \in I}$ of augmentations of $\mu$ of a degree $d$, with $\mu_i \le \nu$ for each $i \in I$ and $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$, and a limit key polynomial $\varphi$ for the family with $\deg \varphi > d$. Then $\mu' = [\mu_\infty; \varphi, \nu(\varphi)]$.

Lean: `Singularity.MacLaneVaquieStep`

In an ordinary step, $\varphi$ is a monic polynomial of least degree with $\mu(\varphi) < \nu(\varphi)$, so $\deg \varphi \ge 1$. If $\mu$ extends $v$, then $\mu$ has support 0 by the fact above, $\varphi$ is a key polynomial for $\mu$ by part 3 of Lemma 3.3.9, and $\mu'$ is the augmented valuation of Definition 3.3.4. In a limit step, $\mu'$ is the limit augmentation of Definition 3.3.28, by part 3 of Theorem 3.3.29. The Lean form gives $\mu'$ by its values.

**Lemma 3.3.38 (steps stay below $\nu$).** Let $\mu$ be a valuation on $K[y]$ that extends $v$, with $\mu \le \nu$. Let $\mu'$ be obtained from $\mu$ by finitely many steps of MacLane-Vaquié towards $\nu$. Then $\mu'$ extends $v$, and $\mu' \le \nu$.

Lean: `Singularity.MacLaneVaquieStep.macLaneBelow`, `Singularity.macLaneBelow_of_reflTransGen`

*Proof.* By induction on the number of steps, it is sufficient to treat one step. Let the step be ordinary. By the remark after Definition 3.3.37, Lemma 3.3.9 applies, and part 4 of Lemma 3.3.9 gives $\mu' \le \nu$. Since $\deg \varphi \ge 1$, part 2 of Theorem 3.3.5 gives $\mu'(c) = \mu(c) = v(c)$ for $c \in K$. Let the step be a limit step. Part 3 of Theorem 3.3.29 gives $\mu' \le \nu$, and part 1 of Theorem 3.3.29 shows that $\mu'$ extends $v$. $\square$

**Lemma 3.3.39 (agreement in low degree).** Let $w$ be a valuation on $K[y]$.

1. Let $D \ge 1$, and assume that $w(f) = \nu(f)$ for each $f$ with $\deg f < D$. If $\nu(a) = \infty$ for some $a \ne 0$ with $\deg a < D$, then $w = \nu$.
2. Assume that $w \le \nu$. Let $\psi$ be monic of degree $m \ge 1$, with $w(\psi) = \nu(\psi)$ and $w(a) = \nu(a)$ for each $a$ with $\deg a < m$. Assume that $\nu(\psi) \ge \nu(\psi')$ for each monic $\psi'$ of degree $m$. Then $w(f) = \nu(f)$ for each $f$ with $\deg f \le m$.

Lean: `Singularity.eq_of_map_eq_zero_of_degree_lt` (part 1), `Singularity.map_eq_of_natDegree_le_of_forall_le` (part 2)

*Proof.* Part 1. Let $c$ be the leading coefficient of $a$, and let $G = c^{-1}a$. Then $G$ is monic, $\deg G < D$ and $\nu(G) = \infty$. So $w(G) = \nu(G) = \infty$. Let $f \in K[y]$, and write $f = qG + r$ with $\deg r < \deg G$. Then $w(qG) = \nu(qG) = \infty$, so $w(f) = w(r)$ and $\nu(f) = \nu(r)$. Since $\deg r < D$, we get $w(f) = w(r) = \nu(r) = \nu(f)$.

Part 2. We follow the proof of Theorem 3.3.33. Let $\deg f \le m$, and write $f = c\psi + r$ with $c \in K$ and $\deg r < m$. We show that $\nu(c\psi) \ge \nu(f)$. This is clear if $c = 0$. If $c \ne 0$, then $f = c\psi'$ with $\psi' = \psi + c^{-1}r$ monic of degree $m$, so $\nu(f) = \nu(c) + \nu(\psi') \le \nu(c) + \nu(\psi) = \nu(c\psi)$. Then $\nu(r) = \nu(f - c\psi) \ge \nu(f)$. Since $\deg r < m$ and $\deg c < m$, we have $w(r) = \nu(r)$ and $w(c) = \nu(c)$. So
$$w(f) \ge \min\big(w(r), w(c\psi)\big) = \min\big(\nu(r), \nu(c\psi)\big) \ge \nu(f).$$
With $w \le \nu$ we get $w(f) = \nu(f)$. $\square$

Now let $w$ be a valuation on $K[y]$ that extends $v$, with $w \le \nu$ and $w \ne \nu$. Let $\varphi_0$ be a monic polynomial of least degree $d$ with $w(\varphi_0) < \nu(\varphi_0)$. By the remark after Definition 3.3.37, $w$ has support 0, and part 1 of Lemma 3.3.9 gives $w(a) = \nu(a)$ for each $a$ with $\deg a < d$. In particular $d \ge 1$.

**Lemma 3.3.40 (monic polynomials of degree $d$).** Let $\psi$ be monic of degree $d$ with $\nu(\psi) \ge \nu(\varphi_0)$. Then $w(\psi) = w(\varphi_0) < \nu(\psi)$, the polynomial $\psi$ is a key polynomial for $w$, and $[w; \psi, \nu(\psi)] \le \nu$.

Lean: `Singularity.keyPolynomial_of_map_le_of_natDegree_eq`

*Proof.* Let $a = \psi - \varphi_0$. The two polynomials are monic of degree $d$, so $\deg a < d$, and $w(a) = \nu(a) \ge \min(\nu(\psi), \nu(\varphi_0)) = \nu(\varphi_0) > w(\varphi_0)$. Thus $w(\psi) = w(\varphi_0 + a) = w(\varphi_0) < \nu(\varphi_0) \le \nu(\psi)$. So $\psi$ is a monic polynomial of least degree with $w(\psi) < \nu(\psi)$. Parts 3 and 4 of Lemma 3.3.9 give the other claims. $\square$

**Definition 3.3.41 (complete family).** Assume that no monic polynomial of degree $d$ has the largest value for $\nu$ among the monic polynomials of degree $d$. Let $S \subseteq \Gamma \cup \{\infty\}$ be the set of the values $\nu(\psi)$ of the monic polynomials $\psi$ of degree $d$ with $\nu(\psi) \ge \nu(\varphi_0)$, with the order of $\Gamma$. For each $s \in S$ choose a monic $\psi_s$ of degree $d$ with $\nu(\psi_s) = s$. The *complete family* in degree $d$ is the family $(\psi_s, s)_{s \in S}$, with $\mu_s = [w; \psi_s, s]$.

Lean: `Singularity.completeValues`, `Singularity.completeFamily`

**Proposition 3.3.42 (the complete family).** In the situation of Definition 3.3.41:

1. $S$ is not empty, $S$ has no largest element, and $S \subseteq \Gamma$.
2. The complete family is a continuous family of augmentations of $w$ of degree $d$. We have $\mu_s \le \nu$ for each $s \in S$, and $\nu(a) = w(a)$ for each $a$ with $\deg a < d$.
3. Each monic polynomial $\psi$ of degree $d$ is stable for the complete family, and $\mu_\infty(\psi) = \nu(\psi)$.

Lean: `Singularity.completeValues_nonempty`, `Singularity.completeValues_noMaxOrder` (part 1), `Singularity.completeFamily`, `Singularity.completeFamily_le` (part 2), `Singularity.completeFamily_isStable` (part 3)

*Proof.* Part 1. We have $\nu(\varphi_0) \in S$. Let $s \in S$. By the hypothesis, there is a monic $\psi$ of degree $d$ with $\nu(\psi) > \nu(\psi_s) = s \ge \nu(\varphi_0)$. Then $\nu(\psi) \in S$ and $\nu(\psi) > s$. So $S$ has no largest element, and $s < \nu(\psi) \le \infty$ gives $s \in \Gamma$.

Part 2. By Lemma 3.3.40, each $\psi_s$ is a key polynomial for $w$ of degree $d$, with $s = \nu(\psi_s) > w(\psi_s)$. The values $s$ increase strictly with the index $s$. Let $s < t$ in $S$, and let $a = \psi_t - \psi_s$. Then $\deg a < d$, so $w(a) = \nu(a) \ge \min(t, s) = s$. So the conditions of Definition 3.3.20 hold. By Lemma 3.3.40, $\mu_s \le \nu$. The last claim is part 1 of Lemma 3.3.9.

Part 3. Let $s_0 = \max(\nu(\psi), \nu(\varphi_0))$. Then $s_0 \in S$, since $s_0$ is $\nu(\psi)$ or $\nu(\varphi_0)$. Let $t \in S$ with $t \ge s_0$, and let $a = \psi - \psi_t$. Then $\deg a < d$. By part 2 of Theorem 3.3.5, $\mu_t(a) = w(a) = \nu(a)$, and $\nu(a) \ge \min(\nu(\psi), t) = \nu(\psi)$ because $t \ge s_0 \ge \nu(\psi)$. Also $\mu_t(\psi_t) = t \ge \nu(\psi)$. So
$$\nu(\psi) \ge \mu_t(\psi) \ge \min\big(\mu_t(\psi_t), \mu_t(a)\big) \ge \nu(\psi).$$
Thus $\mu_t(\psi) = \nu(\psi)$ for each $t \ge s_0$. So $\psi$ is stable, and $\mu_\infty(\psi) = \nu(\psi)$. $\square$

**Theorem 3.3.43 (one round).** Let $w$ be a valuation on $K[y]$ that extends $v$, with $w \le \nu$ and $w \ne \nu$. Let $d$ be the least degree of a monic polynomial $\varphi_0$ with $w(\varphi_0) < \nu(\varphi_0)$. Then $w(f) = \nu(f)$ for each $f$ with $\deg f < d$, and one of the following holds.

1. There are a valuation $w'$ and one step of MacLane-Vaquié from $w$ to $w'$ towards $\nu$ such that $w'(f) = \nu(f)$ for each $f$ with $\deg f \le d$.
2. There is a continuous family of augmentations $\mu_i$ of $w$, with $\mu_i \le \nu$ for each $i$ and $\nu(a) = w(a)$ for each $a$ of degree less than the degree of the family, such that each polynomial is stable and $\mu_\infty = \nu$.

Lean: `Singularity.exists_macLaneVaquieStep_or_forall_isStable`

*Proof.* The first claim is part 1 of Lemma 3.3.9, as above. First assume that some monic $\psi_0$ of degree $d$ satisfies $\nu(\psi_0) \ge \nu(\psi)$ for each monic $\psi$ of degree $d$. Then $\nu(\psi_0) \ge \nu(\varphi_0)$. By Lemma 3.3.40, $w(\psi_0) < \nu(\psi_0)$, so $\psi_0$ is a monic polynomial of least degree with this property. Let $w' = [w; \psi_0, \nu(\psi_0)]$. This is an ordinary step. By Lemma 3.3.40, $w' \le \nu$. By part 2 of Theorem 3.3.5, $w'(\psi_0) = \nu(\psi_0)$ and $w'(a) = w(a) = \nu(a)$ for each $a$ with $\deg a < d$. Part 2 of Lemma 3.3.39 gives $w'(f) = \nu(f)$ for each $f$ with $\deg f \le d$. So case 1 holds.

Now assume that no such $\psi_0$ exists, and take the complete family of Definition 3.3.41. By Proposition 3.3.42, it is a continuous family of augmentations of $w$ of degree $d$ below $\nu$, and $\nu(a) = w(a)$ for each $a$ with $\deg a < d$. If each polynomial is stable, then $\mu_\infty = \nu$ by part 1 of Proposition 3.3.24, and case 2 holds. Otherwise let $\varphi$ be a limit key polynomial for the family, and let $m = \deg \varphi$. It exists by the remark after Definition 3.3.25. By part 1 of Proposition 3.3.26, $m \ge d$. By part 3 of Proposition 3.3.42, each monic polynomial of degree $d$ is stable. Since $\varphi$ is monic and not stable, $m > d$. Let $w' = [\mu_\infty; \varphi, \nu(\varphi)]$. This is a limit step. Let $\deg f \le d$. Then $\deg f < m$, so $f$ is stable by part 1 of Proposition 3.3.26. Part 1 of Theorem 3.3.29 and part 1 of Proposition 3.3.24 give $w'(f) = \mu_\infty(f) = \nu(f)$. So case 1 holds. $\square$

A round uses at most one step. If the largest value of $\nu$ in degree $d$ is attained, the step is ordinary. Otherwise the step is a limit step over the complete family in degree $d$, and the degree of the key polynomial increases strictly at it, or $\nu$ is the limit of the complete family. The limit step of the proof uses an arbitrary limit key polynomial $\varphi$. Then $w'$ agrees with $\nu$ in degree less than $\deg \varphi$, but by Theorem 3.3.33 perhaps not in degree $\deg \varphi$. The next round treats this degree.

**Theorem 3.3.44 (the chain with limit steps).** Let $w_0$ be a valuation on $K[y]$ that extends $v$, with $w_0 \le \nu$. Then one of the following holds.

1. There is a sequence $(w_n)_{n \ge 0}$ that starts with $w_0$, such that $w_{n+1}$ is obtained from $w_n$ by finitely many steps of MacLane-Vaquié towards $\nu$, and $w_n(f) = \nu(f)$ for each $n$ and each $f$ with $\deg f \le n$.
2. There is a valuation $\mu \ne \nu$ that is obtained from $w_0$ by finitely many steps of MacLane-Vaquié towards $\nu$, and a continuous family of augmentations $\mu_i$ of $\mu$, with $\mu_i \le \nu$ for each $i$ and $\nu(a) = \mu(a)$ for each $a$ of degree less than the degree of the family, such that each polynomial is stable and $\mu_\infty = \nu$.

Lean: `Singularity.exists_macLaneVaquie_seq_or_forall_isStable`

*Proof.* Assume that case 2 does not hold. We build $w_n$ by induction, such that $w_n$ is obtained from $w_0$ by finitely many steps, and $w_n(f) = \nu(f)$ for each $f$ with $\deg f \le n$. By Lemma 3.3.38, each such $w_n$ extends $v$ and $w_n \le \nu$. For $n = 0$, the polynomials of degree at most 0 are the constants, and $w_0$ and $\nu$ both extend $v$. Let $w_n$ be given. If $w_n = \nu$, let $w_{n+1} = \nu$. Otherwise apply Theorem 3.3.43 to $w = w_n$, and let $d$ and $\varphi_0$ be as there. Since $w_n(\varphi_0) \ne \nu(\varphi_0)$, we have $d > n$. Case 2 of Theorem 3.3.43 would give case 2 of the theorem with $\mu = w_n$. So case 1 of Theorem 3.3.43 holds, and we let $w_{n+1} = w'$. Then $w_{n+1}$ agrees with $\nu$ in degree at most $d$, so in degree at most $n + 1$. $\square$

In case 1, $w_n(f) = \nu(f)$ for each $f$ and each $n \ge \deg f$. So $\nu$ is the limit of the chain, polynomial by polynomial. In case 2, $\nu$ is the limit of a continuous family over a valuation of the chain. The proof uses at most one step from $w_n$ to $w_{n+1}$, so $w_n$ is obtained from $w_0$ by at most $n$ steps. The Lean statement records only that the number of steps is finite.

**Lemma 3.3.45 (families and nonzero support).** Let $\mu$ be a valuation on $K[y]$ that extends $v$, with $\mu \ne \nu$. Let $(\varphi_i, \gamma_i)_{i \in I}$ be a continuous family of augmentations of $\mu$ of degree $d$, with $\mu_i \le \nu$ for each $i \in I$ and $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$. Let $P \ne 0$ with $\nu(P) = \infty$. Then $P$ is not stable. In particular, case 2 of Theorem 3.3.44 does not hold if $\nu$ has a nonzero support.

Lean: `Singularity.ContinuousFamily.not_isStable_of_map_eq_zero`

*Proof.* Assume that $P$ is stable, and choose $i \in I$ with $\mu_i(P) = \mu_\infty(P)$. By part 1 of Proposition 3.3.24, $\mu_\infty(P) = \nu(P) = \infty$. Let $P = \sum_k a_k\varphi_i^k$ be the $\varphi_i$-expansion, and choose $k$ with $a_k \ne 0$. By Definition 3.3.4, $\mu(a_k) + k\gamma_i \ge \mu_i(P) = \infty$. Since $\gamma_i \in \Gamma$, we get $\mu(a_k) = \infty$. This contradicts the hypothesis of Definition 3.3.20 that $\mu$ has support 0. The Lean form of Definition 3.3.20 does not ask for support 0. The Lean proof uses part 1 of Lemma 3.3.39 instead: since $\deg a_k < d$, we have $\nu(a_k) = \mu(a_k) = \infty$, so $\mu = \nu$, and this contradicts $\mu \ne \nu$. $\square$

**Theorem 3.3.46 (part 4 for nonzero support).** Assume that $\nu(F) = \infty$ for some $F \ne 0$. Let $w_0$ be a valuation on $K[y]$ that extends $v$, with $w_0 \le \nu$. Then $\nu$ is obtained from $w_0$ by finitely many steps of MacLane-Vaquié towards $\nu$. If $\nu(y) < \infty$, this holds in particular for $w_0 = [v; y, \nu(y)]$, the first valuation of Lemma 3.3.10.

Lean: `Singularity.reflTransGen_macLaneVaquieStep_of_map_eq_zero`, `Singularity.reflTransGen_monomialValuation_of_map_eq_zero`

*Proof.* By Lemma 3.3.38 and Lemma 3.3.45, case 2 of Theorem 3.3.44 does not hold. So case 1 holds. Let $n = \deg F$. Then $w_n(f) = \nu(f)$ for each $f$ with $\deg f < n + 1$, and $\nu(F) = \infty$. Part 1 of Lemma 3.3.39 with $D = n + 1$ gives $w_n = \nu$. The valuation $w_n$ is obtained from $w_0$ by finitely many steps. The last claim follows from Lemma 3.3.10. $\square$

The value group of $\nu$ is arbitrary in Theorem 3.3.46. By the remark after Theorem 3.3.44, the proof uses at most $\deg F$ steps. The Lean form of the last claim does not need $\nu(y) < \infty$. So for $\nu$ with nonzero support, a finite chain of ordinary and limit steps ends with $\nu$. Let $F$ be irreducible. A valuation $\nu$ with support $(F)$ that extends $v$ is the same as an extension of $v$ to the field $K[y]/(F)$ with values in $\Gamma \cup \{\infty\}$. So Theorem 3.3.46 applies to each such extension.

We now decide when finitely many steps reach $\nu$. The answer uses key polynomials for $\nu$ itself. Definition 3.3.3 asks for support 0, and $\nu$ can have a nonzero support. So we state the conditions of Definition 3.3.3 in an elementwise form, for a valuation with any support.

**Definition 3.3.47 (key polynomials for any support).** Let $w$ be a valuation on $K[y]$, with any support. Let $\varphi, f \in K[y]$. We say that $\varphi$ *$w$-divides* $f$ if there is $h \in K[y]$ with $w(f - \varphi h) > w(f)$. A monic polynomial $\varphi \in K[y]$ is a *key polynomial* for $w$ if it has these three properties.

1. $\varphi$ does not $w$-divide 1.
2. If $\varphi$ $w$-divides $fg$, then $\varphi$ $w$-divides $f$ or $g$.
3. If $\varphi$ $w$-divides a nonzero $f$, then $\deg f \ge \deg \varphi$.

We say that *$\nu$ has a key polynomial* if some monic $\varphi \in K[y]$ is a key polynomial for $\nu$ in this sense.

Lean: `Singularity.KeyPolynomial`

Properties 1 and 2 say that $\varphi$ is *$w$-irreducible*, and property 3 says that $\varphi$ is *$w$-minimal*. If $\varphi$ $w$-divides $f$, then $w(f) < \infty$. Let $w$ have support 0 and extend $v$. Then the definition is Definition 3.3.3. Indeed, $\operatorname{in}_w \varphi$ divides $\operatorname{in}_w f$ if and only if $\operatorname{in}_w f = \operatorname{in}_w(\varphi h)$ for some $h$, because each nonzero homogeneous element of $\operatorname{gr}_w$ is an initial form, and $\operatorname{in}_w f = \operatorname{in}_w(\varphi h)$ means $w(f - \varphi h) > w(f)$. A key polynomial $\varphi$ for $w$ has degree at least 1. Indeed, 1 $w$-divides 1, because $w(1 - 1 \cdot 1) = \infty > w(1)$, and 1 is the only monic polynomial of degree 0.

Let $\nu$ have support $(F)$, with $F$ monic. Then $F$ is a key polynomial for $\nu$. Indeed, let $f, h \in K[y]$, and write $f = r + Fq$ with $\deg r < \deg F$. Since $\nu(F) = \infty$, we have $\nu(f) = \nu(r)$ and $\nu(f - Fh) = \nu(r + F(q - h)) = \nu(r)$. So $F$ $\nu$-divides no polynomial, and the three properties hold. This agrees with Theorem 3.3.46 and Theorem 3.3.51 below.

**Lemma 3.3.48 (agreement at a minimal polynomial).** Let $\varphi$ be a monic polynomial of degree $m \ge 1$ that is $\nu$-minimal in the sense of Definition 3.3.47. Let $w$ be a valuation on $K[y]$ with $w \le \nu$. Assume that $w(a) = \nu(a)$ for each $a$ with $\deg a < m$, and that $w(\varphi) = \nu(\varphi)$. Then $w = \nu$.

*Proof.* The proof of the first direction of Lemma 3.3.6 does not use that $\mu$ has support 0 or extends $v$. It uses only that $\varphi$ is monic of degree $m \ge 1$ and $\mu$-minimal. So it applies to $\nu$. Let $f \in K[y]$, with $\varphi$-expansion $f = \sum_j a_j\varphi^j$. Then $\nu(f) = \min_j\big(\nu(a_j) + j\nu(\varphi)\big)$. Since $\deg a_j < m$, we have $w(a_j) = \nu(a_j)$. The ultrametric inequality and $w(\varphi) = \nu(\varphi)$ give
$$w(f) \ge \min_j\big(w(a_j) + jw(\varphi)\big) = \min_j\big(\nu(a_j) + j\nu(\varphi)\big) = \nu(f).$$
With $w \le \nu$ we get $w(f) = \nu(f)$. $\square$

**Lemma 3.3.49 (the last step gives a key polynomial).** Let $\mu$ be a valuation on $K[y]$ that extends $v$, with $\mu \le \nu$. Let one step of MacLane-Vaquié lead from $\mu$ to $\mu'$ towards $\nu$. Let $\varphi$ be the key polynomial of the step: the polynomial $\varphi$ of an ordinary step, or the limit key polynomial of a limit step, as in Definition 3.3.37. Then $\varphi$ is a key polynomial for $\mu'$ in the sense of Definition 3.3.47.

*Proof.* Let the step be ordinary. Then $\mu(\varphi) < \nu(\varphi)$, so $\mu \ne \nu$. By the remark after Definition 3.3.37, $\mu$ has support 0, $\varphi$ is a key polynomial for $\mu$, and $\mu' = [\mu; \varphi, \nu(\varphi)]$. Let $\nu(\varphi) < \infty$. By parts 1 and 3 of Theorem 3.3.5, $\mu'$ has support 0 and $\varphi$ is a key polynomial for $\mu'$. By the remark after Definition 3.3.47, this is the claim. Let $\nu(\varphi) = \infty$. Then $\mu'(f) = \mu(a_0)$ for each $f$, with $a_0$ the remainder of $f$ modulo $\varphi$. By the remark after the proof of part 3 of Theorem 3.3.5, $\varphi$ $\mu'$-divides no polynomial, so the three properties hold. Let the step be a limit step. By the remark after Definition 3.3.37, $\mu' = [\mu_\infty; \varphi, \nu(\varphi)]$ is the limit augmentation of Definition 3.3.28. The limit key polynomial $\varphi$ is monic by Definition 3.3.25. By Theorem 3.3.31 and the remark after it, $\varphi$ is $\mu'$-irreducible and $\mu'$-minimal, also if $\nu(\varphi) = \infty$. $\square$

**Lemma 3.3.50 (no family has $\nu$ as its limit).** Let $\mu$ be a valuation on $K[y]$ that extends $v$, with $\mu \ne \nu$. Let $(\varphi_i, \gamma_i)_{i \in I}$ be a continuous family of augmentations of $\mu$ of degree $d$, with $\mu_i \le \nu$ for each $i \in I$ and $\nu(a) = \mu(a)$ for each $a$ with $\deg a < d$. Assume that some monic polynomial $\varphi$ of degree $m \ge 1$ is $\nu$-minimal in the sense of Definition 3.3.47. Then some polynomial is not stable for the family. In particular, $\nu$ is not the limit of the family in the sense of case 2 of Theorem 3.3.44.

*Proof.* Assume that each polynomial is stable. First let $m < d$. Fix $i \in I$. By part 2 of Theorem 3.3.5, $\mu \le \mu_i \le \nu$. Each $a$ with $\deg a < m$ has $\deg a < d$, so $\mu(a) = \nu(a)$. Also $\deg \varphi = m < d$, so $\mu(\varphi) = \nu(\varphi)$. Lemma 3.3.48 with $w = \mu$ gives $\mu = \nu$. This contradicts the hypothesis $\mu \ne \nu$.

Now let $m \ge d$. The polynomial $\varphi$ is stable. So there is $i_0 \in I$ with $\mu_j(\varphi) = \mu_{i_0}(\varphi)$ for each $j \ge i_0$, and $\mu_{i_0}(\varphi) = \mu_\infty(\varphi) = \nu(\varphi)$ by part 1 of Proposition 3.3.24. Since $I$ has no largest element, we can choose $j > i_0$. Then $\mu_{i_0}(\varphi) = \mu_j(\varphi) = \nu(\varphi)$. Let $r$ be the remainder of $\varphi$ modulo $\varphi_j$. Since $\varphi \ne 0$, Lemma 3.3.23 gives
$$\mu_j(\varphi - r) > \mu_j(\varphi) = \nu(\varphi).$$
On the other side, $\deg r < \deg \varphi_j = d \le m$. Step 1 of the proof of Lemma 3.3.6 uses only that $\varphi$ is monic of degree $m$ and minimal, so it applies to $\nu$, as in the proof of Lemma 3.3.48. With $-r$ in place of $r$ and $q = 1$, it gives $\nu(\varphi - r) = \min\big(\nu(r), \nu(\varphi)\big) \le \nu(\varphi)$. Since $\mu_j \le \nu$, we get
$$\nu(\varphi) \ge \nu(\varphi - r) \ge \mu_j(\varphi - r) > \nu(\varphi).$$
This is a contradiction. $\square$

The proof of the case $m \ge d$ does not use $\mu \ne \nu$. Since $\mu_j$ has support 0, the value $\nu(\varphi) = \mu_j(\varphi)$ is finite. The Lean form of Definition 3.3.20 does not ask for support 0. So the Lean proof treats the case $\nu(\varphi) = \infty$ apart, with Lemma 3.3.45.

**Theorem 3.3.51 (the finite chain criterion).** Let $w_0$ be a valuation on $K[y]$ that extends $v$, with $w_0 \le \nu$. The value group and the support of $\nu$ are arbitrary.

1. Assume that some monic polynomial of degree at least 1 is $\nu$-minimal in the sense of Definition 3.3.47. Then $\nu$ is obtained from $w_0$ by finitely many steps of MacLane-Vaquié towards $\nu$.
2. Let $w_0 \ne \nu$. Then $\nu$ is obtained from $w_0$ by finitely many steps of MacLane-Vaquié towards $\nu$ if and only if $\nu$ has a key polynomial in the sense of Definition 3.3.47.

*Proof.* Part 1. Let $\varphi$ be monic of degree $m \ge 1$ and $\nu$-minimal. We apply Theorem 3.3.44. In case 1 of Theorem 3.3.44, the valuation $w_m$ is obtained from $w_0$ by finitely many steps, by induction on $m$. So $w_m \le \nu$ by Lemma 3.3.38. Also $w_m(f) = \nu(f)$ for each $f$ with $\deg f \le m$. In particular $w_m(\varphi) = \nu(\varphi)$, and $w_m(a) = \nu(a)$ for each $a$ with $\deg a < m$. Lemma 3.3.48 with $w = w_m$ gives $w_m = \nu$. So $\nu$ is obtained from $w_0$ by finitely many steps. In case 2 of Theorem 3.3.44, the valuation $\mu$ extends $v$ by Lemma 3.3.38, $\mu \ne \nu$, and each polynomial is stable for the family. This contradicts Lemma 3.3.50. So case 2 does not hold.

Part 2. Let $\varphi$ be a key polynomial for $\nu$. It is monic and $\nu$-minimal, and it has degree at least 1 by the remark after Definition 3.3.47. Part 1 gives finitely many steps from $w_0$ to $\nu$. Conversely, let finitely many steps lead from $w_0$ to $\nu$. Since $w_0 \ne \nu$, there is at least one step. Let the last step lead from $\mu$ to $\nu$. Then $\mu$ is obtained from $w_0$ by finitely many steps, so $\mu$ extends $v$ and $\mu \le \nu$ by Lemma 3.3.38. By Lemma 3.3.49, the key polynomial of the last step is a key polynomial for $\nu$. $\square$

For $w_0 = \nu$ the chain with no step reaches $\nu$, and part 2 says nothing about $\nu$. If $\nu$ has a nonzero support $(F)$, then $F$ is a key polynomial for $\nu$ by the remark after Definition 3.3.47. So part 1 gives Theorem 3.3.46 again.

**Theorem 3.3.52 (part 4 in three cases).** Let $w_0$ be a valuation on $K[y]$ that extends $v$, with $w_0 \le \nu$. The value group and the support of $\nu$ are arbitrary. Then one of the following holds.

1. $\nu$ is obtained from $w_0$ by finitely many steps of MacLane-Vaquié towards $\nu$.
2. $\nu$ has no key polynomial in the sense of Definition 3.3.47, and there is a sequence $(w_n)_{n \ge 0}$ as in case 1 of Theorem 3.3.44 with $w_n \ne \nu$ for each $n$. Thus $\nu$ is the limit of an infinite chain of steps, and no valuation of the chain is $\nu$.
3. $\nu$ has no key polynomial in the sense of Definition 3.3.47, and case 2 of Theorem 3.3.44 holds. Thus a valuation $\mu \ne \nu$ is obtained from $w_0$ by finitely many steps, and $\nu$ is the limit of a continuous family of augmentations of $\mu$ of one degree.

If $\nu$ has a nonzero support, then case 1 holds.

*Proof.* Assume that case 1 does not hold. Then $\nu$ has no key polynomial. Indeed, a key polynomial for $\nu$ is monic, $\nu$-minimal and of degree at least 1, so part 1 of Theorem 3.3.51 would give case 1. We apply Theorem 3.3.44. In case 2 of Theorem 3.3.44, case 3 holds. In case 1 of Theorem 3.3.44, let $(w_n)$ be the sequence. By induction on $n$, each $w_n$ is obtained from $w_0$ by finitely many steps. If $w_n = \nu$ for some $n$, then case 1 holds, and this is false. So $w_n \ne \nu$ for each $n$, and case 2 holds. The last claim is Theorem 3.3.46. $\square$

Theorem 3.3.52 is the precise form of part 4 of Theorem 3.3.5 that we prove. Let $w_0 \ne \nu$. If $\nu$ has a key polynomial, then a finite chain of ordinary and limit steps from $w_0$ ends with $\nu$. If $\nu$ has no key polynomial, then no finite chain from $w_0$ ends with $\nu$, and $\nu$ is the limit of an infinite chain or the limit of a continuous family of one degree over a valuation of a finite chain. In cases 2 and 3 the support of $\nu$ is 0.

We do not prove the following. For $\nu$ without a key polynomial, we do not decide which of cases 2 and 3 of Theorem 3.3.52 holds. We do not relate the existence of a key polynomial for $\nu$ to the value group or the residue field of $\nu$. The families of Theorems 3.3.43 and 3.3.44 are indexed by totally ordered sets of values. Vaquié uses well ordered index sets [Vaq07], and we do not extract a cofinal well ordered subfamily. We do not prove that the chain is unique, or that the degrees and the values $\nu(\varphi)$ of its key polynomials depend only on $\nu$. We do not prove the conditions of Vaquié on two consecutive steps of an admissible family. The Lean statements do not record the degrees of the key polynomials of the chain.

### The Lean definitions

The Lean library states Definition 3.3.3 without the graded algebra $\operatorname{gr}_\mu$. Mathlib writes valuations multiplicatively, so the condition $\mu(f - g) > \mu(f)$ of Definition 3.3.1 becomes $\mu(f - g) < \mu(f)$. The library calls this relation `Singularity.MuEquiv`. It says that $f$ and $g$ have the same initial form. Then $\varphi$ $\mu$-divides $f$ if $f$ is $\mu$-equivalent to $\varphi h$ for some $h$. With this relation, `Singularity.IsMuIrreducible` and `Singularity.IsMuMinimal` are the two conditions of Definition 3.3.3, written for elements of $K[y]$ and not for elements of $\operatorname{gr}_\mu$. The two forms are equivalent, because each homogeneous element of $\operatorname{gr}_\mu$ is an initial form. The elementwise form needs only the valuation, and Mathlib does not yet have the graded algebra of a valuation.

The library proves Lemma 3.3.2 as the valuation `Singularity.monomialValuation`. It also proves that $y$ is a key polynomial for $[v; y, \gamma]$, in `Singularity.keyPolynomial_X_monomialValuation`. This is the first step of each chain in part 4 of Theorem 3.3.5. For $a \in K$, the polynomial $y - a$ is a key polynomial for $[v; y, \gamma]$ if $v(a) \ge \gamma$. It is not a key polynomial if $v(a) < \gamma$, because then its initial form is the initial form of the unit $-a$. The $\varphi$-expansion is `Singularity.expansionCoeff`, and `Singularity.eq_sum_expansionCoeff` proves that the expansion gives $f$ back. The function `Singularity.augmentedValuationFun` is the right side of Definition 3.3.4. For a key polynomial $\varphi$, the valuation `Singularity.augmentedValuation` is this function, and `Singularity.KeyPolynomial.augmentedValuationFun_mul` is its multiplicativity. The Lean proof follows the proof above. In multiplicative notation the condition $\gamma > \mu(\varphi)$ is $\gamma < \mu(\varphi)$. The Lean theorems ask only for $\gamma \le \mu(\varphi)$ in multiplicative notation, that is $\gamma \ge \mu(\varphi)$ in additive notation, so they include the case $\mu' = \mu$ of the last remark, and `Singularity.augmentedValuation_eq_self` proves this case. The value $\gamma = \infty$ is the element 0 of the group with zero. The library proves the first claim of part 3 as `Singularity.KeyPolynomial.keyPolynomial_augmentedValuation`, with Lemma 3.3.8 as `Singularity.muDvd_iff_of_forall_eq`. It also proves that the $\varphi$-expansion is unique, in `Singularity.expansionCoeff_sum_mul_pow`. The library proves Lemma 3.3.9 in `Singularity.exists_keyPolynomial_augmentedValuation`. The Lean form does not ask that $\mu$ or $\nu$ has support 0. For a given $\varphi$, it asks only that $\mu \le \nu$, that $\varphi$ is monic with $\mu(\varphi) < \nu(\varphi)$, and that $\mu(f) = \nu(f)$ for $\deg f < \deg \varphi$. The library proves Lemma 3.3.10 in `Singularity.map_le_monomialValuation`. The library has no graded algebra, and it proves the claim on $\operatorname{gr}_{\mu'}$ in part 3 in the elementwise form of Proposition 3.3.19. The library builds the MacLane chain as `Singularity.macLaneChain v ν`, with the key polynomials `Singularity.macLaneChainKey v ν`. The index is shifted: `Singularity.macLaneChainKey v ν i` is $\varphi_{i+1}$. The step `Singularity.macLaneStep` chooses $\varphi_{i+1}$ with the axiom of choice, and it does not change $\mu_i$ if $\mu_i = \nu$. The Lean chain does not need $\nu(y) < \infty$, and the Lean theorems do not ask that $\mu_i$ has support 0. The hypothesis of Theorem 3.3.12 is the Lean hypothesis `hdisc`: for $c \ne 0$ and each $d$, the set of values of $\nu$ between $c$ and $d$ is finite. The library proves the limit principle of the proof of Theorem 3.3.12 for each sequence of valuations with the properties of Lemma 3.3.11, in `Singularity.eventually_eq_of_succ_lt`. Example 3.3.14 has no Lean proof. The library proves Definition 3.3.20 to Theorem 3.3.33 for one continuous family. The library proves Definition 3.3.37 to Theorem 3.3.46 in the file `Singularity/Valuation/MacLaneVaquie.lean`. The step `Singularity.MacLaneVaquieStep` gives $\mu'$ by its values, and a finite chain of steps is `Relation.ReflTransGen (Singularity.MacLaneVaquieStep ν)`. The index set of the complete family is the set `Singularity.completeValues ν φ` with the reverse order of the multiplicative values. Thus part 4 of Theorem 3.3.5 has a Lean proof for valuations $\nu$ with discrete values and for valuations $\nu$ with nonzero support, and the weak form of Theorem 3.3.44 has a Lean proof for each $\nu$. Definition 3.3.47 is `Singularity.KeyPolynomial`, with the relation `Singularity.MuDvd` for $w$-divisibility. tamnd/singularity-lean#115 proves Lemma 3.3.48 as `Singularity.eq_of_isMuMinimal`, Lemma 3.3.49 as `Singularity.MacLaneVaquieStep.exists_keyPolynomial` with the corollary `Singularity.exists_keyPolynomial_of_reflTransGen` for a finite chain, Lemma 3.3.50 as `Singularity.ContinuousFamily.not_forall_isStable_of_isMuMinimal`, part 1 of Theorem 3.3.51 as `Singularity.reflTransGen_macLaneVaquieStep_of_isMuMinimal`, part 2 of Theorem 3.3.51 as `Singularity.reflTransGen_macLaneVaquieStep_iff_exists_keyPolynomial`, and Theorem 3.3.52 as `Singularity.reflTransGen_macLaneVaquieStep_or_forall_not_keyPolynomial`. The records of the map do not have these names yet, so these results have no Lean line. The Lean forms ask that $w_0$ and $\nu$ agree on the constants, in place of the hypothesis that $w_0$ extends $v$. The Lean form of Lemma 3.3.49 holds for each step, with no hypothesis on $\mu$. The library proves Lemma 3.3.34 to Theorem 3.3.36 in the file `Singularity/Valuation/MacLaneDiscrete.lean`. In the Lean form of Theorem 3.3.36, the hypotheses on $\nu$ are `hν` ($\mu_i \le \nu$), `hlow` ($\nu = \mu$ in degree less than $d$), `hval` (each $\gamma_i$ is a value of $\nu$) and `hdisc`, and the support 0 in part 3 is `hsupp`. The library proves that $\varphi_{i+1}$ is unique up to $\mu_i$-equivalence among the monic polynomials of its degree, in `Singularity.muEquiv_macLaneChainKey_iff`. The Lean forms of Proposition 3.3.15, Lemma 3.3.16 and Proposition 3.3.17 do not ask that $\mu$ or $\nu$ has support 0. Example 3.3.18 has no Lean proof.

### An example

Let $k$ be a field of characteristic not 2, let $K = k(t)$ and let $v = \operatorname{ord}_t$. Let $\Gamma = \mathbb{Q}$. Let $s = t^{3/2} + t^2$, an element of the field $k((t^{1/2}))$. Let $\nu(f) = \operatorname{ord}_t f(s)$ for $f \in K[y]$, with values in $\frac12\mathbb{Z} \cup \{\infty\}$. Then $\nu$ is a valuation on $K[y]$ that extends $v$. We find its MacLane chain.

*Step 1.* We have $\nu(y) = 3/2$. Let $\mu_0 = [v; y, 3/2]$, a valuation by Lemma 3.3.2. Let $\tau = \operatorname{in}_{\mu_0} t$ and $Y = \operatorname{in}_{\mu_0} y$, of degrees 1 and $3/2$. For $a \in K^\times$ with $v(a) = n$, $\operatorname{in}_{\mu_0} a = c\tau^n$, where $c \in k^\times$ is the residue of $at^{-n}$. So $\operatorname{in}_{\mu_0} f$ is the sum of the terms $c_i\tau^{n_i}Y^i$ for which $v(a_i) + \frac32 i$ is minimal. Distinct monomials $\tau^nY^i$ of the same degree have distinct $i$, so by the definition of $\mu_0$ no sum of them with nonzero coefficients is 0. Thus
$$\operatorname{gr}_{\mu_0} = k[\tau, \tau^{-1}][Y],$$
a polynomial ring in $Y$.

*Step 2.* Let $\varphi_1 = y^2 - t^3$. Then $\mu_0(\varphi_1) = 3$ and $\operatorname{in}_{\mu_0} \varphi_1 = Y^2 - \tau^3$. This polynomial is monic in $Y$ and irreducible over $k(\tau)$, because $\tau^3$ is not a square in $k(\tau)$. Since $k[\tau, \tau^{-1}]$ is a unique factorization domain, it is a prime element of $k[\tau, \tau^{-1}][Y]$. Let $f = a + by$ be nonzero with $a, b \in K$. The values $v(a) \in \mathbb{Z}$ and $v(b) + \frac32 \in \frac12 + \mathbb{Z}$ differ, so $\operatorname{in}_{\mu_0} f$ is a single monomial $c\tau^nY^i$ with $i \le 1$. Its only prime factor is $Y$, so $Y^2 - \tau^3$ does not divide it. Thus $\varphi_1$ is a key polynomial for $\mu_0$.

The same argument gives $\nu(a + by) = \min(v(a), v(b) + \frac32) = \mu_0(a + by)$, because $\operatorname{ord}_t(a)$ and $\operatorname{ord}_t(bs)$ differ. Now $\varphi_1(s) = s^2 - t^3 = 2t^{7/2} + t^4$, so $\nu(\varphi_1) = 7/2 > 3$.

*Step 3.* Let $\mu_1 = [\mu_0; \varphi_1, 7/2]$. By Theorem 3.3.5 it is a valuation with support 0. For $f = \sum_j a_j\varphi_1^j$ with $\deg a_j < 2$,
$$\nu(f) \ge \min_j\big(\nu(a_j) + \tfrac72 j\big) = \min_j\big(\mu_0(a_j) + \tfrac72 j\big) = \mu_1(f),$$
so $\mu_1 \le \nu$. Lemma 3.3.9 gives this again. Indeed, $\varphi_1$ is a monic polynomial of least degree with $\mu_0(\varphi_1) < \nu(\varphi_1)$, because $\nu(a + by) = \mu_0(a + by)$ by Step 2. Let
$$\psi = (y - t^2)^2 - t^3 = \varphi_1 - 2t^2y + t^4.$$
Then $\psi(s) = 0$, so $\nu(\psi) = \infty$. The $\varphi_1$-expansion of $\psi$ has $a_1 = 1$ and $a_0 = -2t^2y + t^4$, with $\mu_0(a_0) = \min(\frac72, 4) = \frac72$. So $\mu_1(\psi) = \min(\frac72, \frac72) = \frac72 < \nu(\psi)$.

*Step 4.* We describe $\operatorname{gr}_{\mu_1}$. By part 2 of Theorem 3.3.5, $\mu_1 = \mu_0$ on polynomials of degree $< 2$, so their initial forms are monomials in $\tau = \operatorname{in}_{\mu_1} t$ and $Y = \operatorname{in}_{\mu_1} y$ as in Step 2. Now $y^2 = \varphi_1 + t^3$ with $\mu_1(\varphi_1) = \frac72 > 3 = \mu_1(t^3)$, so $Y^2 = \tau^3$ in $\operatorname{gr}_{\mu_1}$. Thus $Y$ is a unit. Let $u = Y\tau^{-1}$, of degree $\frac12$. Then $u^2 = \tau$ and $u^3 = Y$. So the ring $\Delta$ of part 3 is generated over $k$ by $u$ and $u^{-1}$. The powers $u^n$ have distinct degrees $n/2$, so $\Delta = k[u, u^{-1}]$ is a ring of Laurent polynomials. By part 3,
$$\operatorname{gr}_{\mu_1} = k[u, u^{-1}][\Phi], \qquad \Phi = \operatorname{in}_{\mu_1} \varphi_1.$$
The initial form of $a_0 = -2t^2y + t^4$ is $-2\tau^2Y = -2u^7$, so
$$\operatorname{in}_{\mu_1} \psi = \Phi - 2u^7.$$
This is monic of degree 1 in $\Phi$, so it is a prime element. The initial form of a nonzero polynomial of degree $< 2$ is in $\Delta$, and $\Phi - 2u^7$ divides no nonzero element of $\Delta$. So $\psi$ is a key polynomial for $\mu_1$. It has the same degree as $\varphi_1$.

*Step 5.* Let $\mu_2 = [\mu_1; \psi, \infty]$. For $f$ with $\psi$-expansion $f = \sum_j b_j\psi^j$ and $\deg b_j < 2$, we have $\nu(f) = \nu(b_0)$ because $\nu(\psi) = \infty$. Also $\nu(b_0) = \mu_0(b_0) = \mu_1(b_0) = \mu_2(f)$. So $\nu = \mu_2$, and the MacLane chain of $\nu$ is
$$\mu_0 = [v; y, \tfrac32] < \mu_1 = [\mu_0; y^2 - t^3, \tfrac72] < \nu = [\mu_1; (y - t^2)^2 - t^3, \infty].$$

The valuation $\nu$ induces the valuation $\operatorname{ord}_t$ on $K(s) = K[y]/(\psi)$. Its value group is $\frac12\mathbb{Z}$ and its residue field is $k$, so $e = 2$, $f = 1$ and $ef = 2 = [K(s) : K]$.

The middle step $\mu_1$ is also interesting. It has support 0, so it is a valuation of the plane $k(t, y)$. Let $Z = \varphi_1^2/t^7$, with $\mu_1(Z) = 0$. Let $c_0, \dots, c_d \in k$ with $c_d \ne 0$. The $\varphi_1$-expansion of $F = \sum_j c_j\varphi_1^{2j}t^{7(d - j)}$ has the terms $c_jt^{7(d-j)}\varphi_1^{2j}$, each of value $7d$ if $c_j \ne 0$. So $\mu_1(F) = 7d$ and $\mu_1(\sum_j c_jZ^j) = 0$. Thus the residue of $Z$ is transcendental over $k$. The value group of $\mu_1$ contains $\frac12\mathbb{Z}$. So the rational rank of $\mu_1$ and the transcendence degree of its residue field over $k$ are at least 1. By Theorem 2.1.5 both are 1, and equality holds. So $\mu_1$ is a divisorial valuation of $k(t, y)$. In the language of Section 1.6, the chain approximates the arc of the cusp $\psi = 0$ by divisorial valuations.
