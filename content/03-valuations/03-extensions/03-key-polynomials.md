---
title: Key polynomials
nodes: [SG0000000Z]
sources: [Mac36, Vaq07, HMOS22]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Key polynomials

Let $(K, v)$ be a valued field and let $y$ be an indeterminate. Let $K(s)$ be a simple extension, and let $\mathfrak{q}$ be the kernel of the map $K[y] \to K(s)$ with $y \mapsto s$. Thus $\mathfrak{q} = 0$ if $s$ is transcendental over $K$, and $\mathfrak{q} = (F)$ with $F$ the minimal polynomial of $s$ if $s$ is algebraic. An extension of $v$ to $K(s)$ is the same as a valuation on $K[y]$ that extends $v$ and has support $\mathfrak{q}$, in the sense defined below. MacLane found a way to build such valuations in steps, by a sequence of polynomials in $y$ of increasing degree [Mac36]. The polynomials are the *key polynomials*. In this section we give the definitions, we state the main theorem with a citation, and we work out one example.

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
of augmentations with $\deg \varphi_0 = 1$, $\deg \varphi_i \le \deg \varphi_{i+1}$ and $\mu_i \le \nu$, in the following sense. Either the chain is finite and ends with $\nu$, or $\nu$ is the limit of the chain, or one needs *limit augmentations* along an infinite family of key polynomials of the same degree.

Lean: `Singularity.augmentedValuation`, `Singularity.KeyPolynomial.augmentedValuationFun_mul`, `Singularity.augmentedValuation_le` (parts 1 and 2), `Singularity.KeyPolynomial.keyPolynomial_augmentedValuation` (the first claim of part 3), `Singularity.exists_keyPolynomial_augmentedValuation` (one step of the chain of part 4, Lemma 3.3.9), `Singularity.macLaneChain_eventually_eq` (part 4 without limit augmentations for $\nu$ with discrete values, Theorem 3.3.12)

MacLane proved parts 1 to 3, and part 4 without limit augmentations, for a discrete valuation $v$ of rank 1 [Mac36]. In that case the chain is finite or $\nu$ is its limit. Vaquié extended the theorem to an arbitrary valuation $v$ [Vaq07]. He introduced the limit augmentations of part 4, and in the general case one indexes the chain by an ordinal. Herrera Govantes, Mahboub, Olalla Acosta and Spivakovsky give a different approach to key polynomials for a simple extension $K(s)/K$ [HMOS22]. We prove parts 1 and 2 and the first claim of part 3 below. We do not prove the claim on $\operatorname{gr}_{\mu'}$ in part 3. Of part 4 we prove the first step and the inductive step of the chain, in Lemmas 3.3.10 and 3.3.9, and the properties of the chain in Lemma 3.3.11. If the values of $\nu$ are discrete, for example if $\nu$ has values in $\mathbb{Z} \cup \{\infty\}$, we prove part 4 without limit augmentations in Theorem 3.3.12. Then the chain is finite and ends with $\nu$, or $\nu$ is its limit. Proposition 3.3.13 gives a criterion for a finite chain, and Example 3.3.14 shows that the chain can be infinite, also when $\nu$ has a nonzero support. We do not treat the limit augmentations, so we do not prove part 4 for other values of $\nu$. In the example below we use only parts 1 to 3, and we compute the last step by hand.

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

This proof does not use the least indices $i_0$ and $j_0$ of the proof of part 1. It uses the hypothesis $\gamma > \mu(\varphi)$ only through parts 1 and 2. For $\gamma = \mu(\varphi)$ we have $\mu' = \mu$, and the claim is the hypothesis. The Lean form also allows $\gamma = \infty$. Then $\mu'(f) = \mu(a_0)$, so $\varphi$ $\mu'$-divides no polynomial, and the two conditions hold trivially. Definition 3.3.3 asks for support 0, so this case is not in Theorem 3.3.5. The second claim of part 3 needs the graded algebra, and we do not prove it here. See [Mac36] and [Vaq07] for a proof.

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

Let $\nu$ be a valuation on $K[y]$ that extends $v$, with $\nu(y) < \infty$. The two lemmas give the chain of part 4 of Theorem 3.3.5 step by step. Let $\varphi_0 = y$ and let $\mu_0 = [v; y, \nu(y)]$ be the valuation of Lemma 3.3.10. Let $i \ge 0$, and assume that $\mu_i$ is defined, that $\mu_i \le \nu$, and that $\mu_i$ has support 0. If $\mu_i = \nu$, let $\mu_{i+1} = \nu$. If $\mu_i \ne \nu$, let $\varphi_{i+1}$ be a monic polynomial of least degree with $\mu_i(\varphi_{i+1}) < \nu(\varphi_{i+1})$, as in part 1 of Lemma 3.3.9, and let $\mu_{i+1} = [\mu_i; \varphi_{i+1}, \nu(\varphi_{i+1})]$. By Lemma 3.3.9, $\varphi_{i+1}$ is a key polynomial for $\mu_i$ and $\mu_{i+1} \le \nu$. If $\nu(\varphi_{i+1}) < \infty$, then $\mu_{i+1}$ has support 0 by part 1 of Theorem 3.3.5. If $\nu(\varphi_{i+1}) = \infty$, then $\mu_{i+1} = \nu$ by part 4 of Lemma 3.3.11 below, and the chain stops. We call $(\mu_i)$ the *MacLane chain* of $\nu$. If $\mu_n = \nu$ for some $n$, we say that the chain is *finite* and ends with $\nu$. The chain depends on the choice of each $\varphi_{i+1}$. The results below hold for each choice.

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

For other value groups, a family of key polynomials of the same degree can have values that increase and are bounded. Then part 4 of Theorem 3.3.5 can need the limit augmentations of Vaquié [Vaq07]. We do not treat them.

### The Lean definitions

The Lean library states Definition 3.3.3 without the graded algebra $\operatorname{gr}_\mu$. Mathlib writes valuations multiplicatively, so the condition $\mu(f - g) > \mu(f)$ of Definition 3.3.1 becomes $\mu(f - g) < \mu(f)$. The library calls this relation `Singularity.MuEquiv`. It says that $f$ and $g$ have the same initial form. Then $\varphi$ $\mu$-divides $f$ if $f$ is $\mu$-equivalent to $\varphi h$ for some $h$. With this relation, `Singularity.IsMuIrreducible` and `Singularity.IsMuMinimal` are the two conditions of Definition 3.3.3, written for elements of $K[y]$ and not for elements of $\operatorname{gr}_\mu$. The two forms are equivalent, because each homogeneous element of $\operatorname{gr}_\mu$ is an initial form. The elementwise form needs only the valuation, and Mathlib does not yet have the graded algebra of a valuation.

The library proves Lemma 3.3.2 as the valuation `Singularity.monomialValuation`. It also proves that $y$ is a key polynomial for $[v; y, \gamma]$, in `Singularity.keyPolynomial_X_monomialValuation`. This is the first step of each chain in part 4 of Theorem 3.3.5. For $a \in K$, the polynomial $y - a$ is a key polynomial for $[v; y, \gamma]$ if $v(a) \ge \gamma$. It is not a key polynomial if $v(a) < \gamma$, because then its initial form is the initial form of the unit $-a$. The $\varphi$-expansion is `Singularity.expansionCoeff`, and `Singularity.eq_sum_expansionCoeff` proves that the expansion gives $f$ back. The function `Singularity.augmentedValuationFun` is the right side of Definition 3.3.4. For a key polynomial $\varphi$, the valuation `Singularity.augmentedValuation` is this function, and `Singularity.KeyPolynomial.augmentedValuationFun_mul` is its multiplicativity. The Lean proof follows the proof above. In multiplicative notation the condition $\gamma > \mu(\varphi)$ is $\gamma < \mu(\varphi)$. The Lean theorems ask only for $\gamma \le \mu(\varphi)$, so they include the case $\mu' = \mu$ of the last remark, and `Singularity.augmentedValuation_eq_self` proves this case. The value $\gamma = \infty$ is the element 0 of the group with zero. The library proves the first claim of part 3 as `Singularity.KeyPolynomial.keyPolynomial_augmentedValuation`, with Lemma 3.3.8 as `Singularity.muDvd_iff_of_forall_eq`. It also proves that the $\varphi$-expansion is unique, in `Singularity.expansionCoeff_sum_mul_pow`. The library proves Lemma 3.3.9 in `Singularity.exists_keyPolynomial_augmentedValuation`. The Lean form does not ask that $\mu$ or $\nu$ has support 0. For a given $\varphi$, it asks only that $\mu \le \nu$, that $\varphi$ is monic with $\mu(\varphi) < \nu(\varphi)$, and that $\mu(f) = \nu(f)$ for $\deg f < \deg \varphi$. The library proves Lemma 3.3.10 in `Singularity.map_le_monomialValuation`. The claim on $\operatorname{gr}_{\mu'}$ in part 3 has no Lean proof. The library builds the MacLane chain as `Singularity.macLaneChain v ν`, with the key polynomials `Singularity.macLaneChainKey v ν`. The index is shifted: `Singularity.macLaneChainKey v ν i` is $\varphi_{i+1}$. The step `Singularity.macLaneStep` chooses $\varphi_{i+1}$ with the axiom of choice, and it does not change $\mu_i$ if $\mu_i = \nu$. The Lean chain does not need $\nu(y) < \infty$, and the Lean theorems do not ask that $\mu_i$ has support 0. The hypothesis of Theorem 3.3.12 is the Lean hypothesis `hdisc`: for $c \ne 0$ and each $d$, the set of values of $\nu$ between $c$ and $d$ is finite. The library proves the limit principle of the proof of Theorem 3.3.12 for each sequence of valuations with the properties of Lemma 3.3.11, in `Singularity.eventually_eq_of_succ_lt`. Example 3.3.14 has no Lean proof. The limit augmentations of part 4 of Theorem 3.3.5 have no Lean proof. Thus part 4 has a Lean proof only for valuations $\nu$ with discrete values. The library does not prove that $\varphi_{i+1}$ is unique up to $\mu_i$-equivalence.

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
