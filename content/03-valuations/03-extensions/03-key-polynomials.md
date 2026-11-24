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

Lean: none yet

*Proof.* The inequality $\mu_0(f + g) \ge \min(\mu_0(f), \mu_0(g))$ holds term by term, and $\mu_0(fg) \ge \mu_0(f) + \mu_0(g)$ holds for the same reason. Let $g = \sum_j b_jy^j$. Let $i_0$ be the smallest index with $v(a_{i_0}) + i_0\gamma = \mu_0(f)$, and let $j_0$ be the smallest index with $v(b_{j_0}) + j_0\gamma = \mu_0(g)$. The coefficient of $y^{i_0 + j_0}$ in $fg$ is $\sum_{i + j = i_0 + j_0} a_ib_j$. The term $a_{i_0}b_{j_0}$ has value $\mu_0(f) + \mu_0(g) - (i_0 + j_0)\gamma$. Each other term has $i < i_0$ or $j < j_0$, so its value is strictly larger. By Lemma 1.1.3 the coefficient has value $\mu_0(f) + \mu_0(g) - (i_0 + j_0)\gamma$, so $\mu_0(fg) \le \mu_0(f) + \mu_0(g)$. $\square$

### Key polynomials and augmentations

**Definition 3.3.3 (key polynomial).** Let $\mu$ be a valuation on $K[y]$ with support 0 that extends $v$. A monic polynomial $\varphi \in K[y]$ is a *key polynomial* for $\mu$ if it has these two properties.

1. $\varphi$ is *$\mu$-irreducible*: $\operatorname{in}_\mu \varphi$ is a prime element of $\operatorname{gr}_\mu$. Thus it is not a unit, and if $\varphi$ $\mu$-divides $fg$, then $\varphi$ $\mu$-divides $f$ or $g$.
2. $\varphi$ is *$\mu$-minimal*: if $\varphi$ $\mu$-divides a nonzero $f$, then $\deg f \ge \deg \varphi$.

Node: SG0000000Z · Lean: `Singularity.KeyPolynomial` (planned, no Lean statement yet)

Let $\varphi$ be monic of degree $m \ge 1$. Each $f \in K[y]$ has a unique *$\varphi$-expansion* $f = \sum_j a_j\varphi^j$ with $\deg a_j < m$, by repeated division with remainder by $\varphi$.

**Definition 3.3.4 (augmented valuation).** Let $\mu$ and $\varphi$ be as in Definition 3.3.3, and let $\gamma \in \Gamma \cup \{\infty\}$ with $\gamma > \mu(\varphi)$. The *augmented valuation* $\mu' = [\mu; \varphi, \gamma]$ is
$$\mu'\Big(\sum_j a_j\varphi^j\Big) = \min_j\big(\mu(a_j) + j\gamma\big),$$
with the $\varphi$-expansion on the left.

**Theorem 3.3.5 (MacLane-Vaquié).** Let $\mu$, $\varphi$, $\gamma$ and $\mu' = [\mu; \varphi, \gamma]$ be as in Definition 3.3.4, and let $m = \deg \varphi$.

1. $\mu'$ is a valuation on $K[y]$ that extends $v$. Its support is 0 if $\gamma < \infty$ and $(\varphi)$ if $\gamma = \infty$.
2. $\mu \le \mu'$, $\mu'(f) = \mu(f)$ if $\deg f < m$, and $\mu'(\varphi) = \gamma > \mu(\varphi)$.
3. If $\gamma < \infty$, then $\varphi$ is a key polynomial for $\mu'$. Let $\Delta \subseteq \operatorname{gr}_{\mu'}$ be the subring generated by the initial forms of the nonzero polynomials of degree $< m$. Then $\operatorname{in}_{\mu'} \varphi$ is transcendental over $\Delta$, and $\operatorname{gr}_{\mu'} = \Delta[\operatorname{in}_{\mu'} \varphi]$ is a polynomial ring.
4. Let $\nu$ be a valuation on $K[y]$ that extends $v$. Then $\nu$ is the end of a chain
$$\mu_0 = [v; \varphi_0, \gamma_0] < \mu_1 = [\mu_0; \varphi_1, \gamma_1] < \mu_2 < \cdots$$
of augmentations with $\deg \varphi_0 = 1$, $\deg \varphi_i \le \deg \varphi_{i+1}$ and $\mu_i \le \nu$, in the following sense. Either the chain is finite and ends with $\nu$, or $\nu$ is the limit of the chain, or one needs *limit augmentations* along an infinite family of key polynomials of the same degree.

Lean: none yet

MacLane proved parts 1 to 3, and part 4 without limit augmentations, for a discrete valuation $v$ of rank 1 [Mac36]. In that case the chain is finite or $\nu$ is its limit. Vaquié extended the theorem to an arbitrary valuation $v$ [Vaq07]. He introduced the limit augmentations of part 4, and in the general case one indexes the chain by an ordinal. Herrera Govantes, Mahboub, Olalla Acosta and Spivakovsky give a different approach to key polynomials for a simple extension $K(s)/K$ [HMOS22]. We do not prove the theorem. In the example below we use only parts 1 to 3, and we compute the last step by hand.

Over a henselian field $K$, part 4 for the valuation $\nu$ with support $(F)$ describes the extension of $v$ to $K[y]/(F)$. Defect is related to the limit augmentations of part 4. A family of key polynomials of the same degree whose values increase but have no maximum is the same phenomenon as the sequence $s_m$ of Proposition 3.2.5.

### An example

Let $k$ be a field of characteristic not 2, let $K = k(t)$ and let $v = \operatorname{ord}_t$. Let $\Gamma = \mathbb{Q}$. Let $s = t^{3/2} + t^2$, an element of the field $k((t^{1/2}))$. Let $\nu(f) = \operatorname{ord}_t f(s)$ for $f \in K[y]$, with values in $\frac12\mathbb{Z} \cup \{\infty\}$. Then $\nu$ is a valuation on $K[y]$ that extends $v$. We find its MacLane chain.

*Step 1.* We have $\nu(y) = 3/2$. Let $\mu_0 = [v; y, 3/2]$, a valuation by Lemma 3.3.2. Let $\tau = \operatorname{in}_{\mu_0} t$ and $Y = \operatorname{in}_{\mu_0} y$, of degrees 1 and $3/2$. For $a \in K^\times$ with $v(a) = n$, $\operatorname{in}_{\mu_0} a = c\tau^n$, where $c \in k^\times$ is the residue of $at^{-n}$. So $\operatorname{in}_{\mu_0} f$ is the sum of the terms $c_i\tau^{n_i}Y^i$ for which $v(a_i) + \frac32 i$ is minimal. Distinct monomials $\tau^nY^i$ of the same degree have distinct $i$, so by the definition of $\mu_0$ no sum of them with nonzero coefficients is 0. Thus
$$\operatorname{gr}_{\mu_0} = k[\tau, \tau^{-1}][Y],$$
a polynomial ring in $Y$.

*Step 2.* Let $\varphi_1 = y^2 - t^3$. Then $\mu_0(\varphi_1) = 3$ and $\operatorname{in}_{\mu_0} \varphi_1 = Y^2 - \tau^3$. This polynomial is monic in $Y$ and irreducible over $k(\tau)$, because $\tau^3$ is not a square in $k(\tau)$. Since $k[\tau, \tau^{-1}]$ is a unique factorization domain, it is a prime element of $k[\tau, \tau^{-1}][Y]$. Let $f = a + by$ be nonzero with $a, b \in K$. The values $v(a) \in \mathbb{Z}$ and $v(b) + \frac32 \in \frac12 + \mathbb{Z}$ differ, so $\operatorname{in}_{\mu_0} f$ is a single monomial $c\tau^nY^i$ with $i \le 1$. Its only prime factor is $Y$, so $Y^2 - \tau^3$ does not divide it. Thus $\varphi_1$ is a key polynomial for $\mu_0$.

The same argument gives $\nu(a + by) = \min(v(a), v(b) + \frac32) = \mu_0(a + by)$, because $\operatorname{ord}_t(a)$ and $\operatorname{ord}_t(bs)$ differ. Now $\varphi_1(s) = s^2 - t^3 = 2t^{7/2} + t^4$, so $\nu(\varphi_1) = 7/2 > 3$.

*Step 3.* Let $\mu_1 = [\mu_0; \varphi_1, 7/2]$. By Theorem 3.3.5 it is a valuation with support 0. For $f = \sum_j a_j\varphi_1^j$ with $\deg a_j < 2$,
$$\nu(f) \ge \min_j\big(\nu(a_j) + \tfrac72 j\big) = \min_j\big(\mu_0(a_j) + \tfrac72 j\big) = \mu_1(f),$$
so $\mu_1 \le \nu$. Let
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
