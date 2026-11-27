---
title: Hasse-Schmidt ideals for z^q + g and a no-go theorem
nodes: [SG0000009V, SG0000009W, SG0000009X, SG0000009Y, SG0000009Z, SG000000A0, SG000000A1, SG000000A2, SG000000A3, SG000000A4, SG000000A5, SG000000A6]
sources: [HP19a, Moh87, BenV13, CP08, CP19, CJS20]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Hasse-Schmidt ideals for z^q + g and a no-go theorem

Sections 3.1 and 3.2 treat the equation $z^p + g$. There the residual order $\rho$ of the log-Jacobian ideal is $d - 1$ or $d$, and it does not go up under a point blowup. This section asks for the same pair of properties when the equation is $z^q + g$ with $q = p^e$ and $e \ge 2$. The natural candidate replaces the derivations by the Hasse-Schmidt derivatives of order less than $q$. It gives a family of ideals $\Theta^{\le m}(g)$, $1 \le m < q$, that do not see the choice of $z$, and at the levels $m \ge p^{e-1}$ their residual orders satisfy a dichotomy with the gap $m$. The section proves the following.

1. The ideals $\Theta^{\le m}(g)$ do not depend on the coordinates and do not change when a $q$-th power is added to $g$ (Propositions 3.20.3 and 3.20.4). Their residual orders are upper semicontinuous (Lemma 3.20.16).
2. For $p^{e-1} \le m < q$ and $g$ clean, $\rho_m \le d \le \rho_m + m$, and the free order $c$ of the operators splits $\Theta^{\le m}$ into pieces whose weighted orders have the minimum $d$ (Theorem 3.20.6).
3. Under a point blowup each piece is multiplied by a power $x_1^{\varepsilon_c}$ of the exceptional variable, the excess of the piece. So $\rho'_m \le \rho_m + \delta$ with an imbalance $\delta \ge 0$, and $\delta = 0$ if and only if the point is balanced (Theorem 3.20.8). The level $m = 1$ never goes up, and each level $2 \le m < q$ goes up at some point (Corollary 3.20.10 and Proposition 3.20.15).
4. For $e = 3$, in dimension at least $5$ for $p = 2$ and at least $4$ for $p \ge 3$, no function of the germ can bound $d$ on its fibres and not go up under the blowups of closed points of order $q$ (Theorem 3.20.18). The proof uses the theorem of Hauser and Perlega, Theorem 1.4.3, and nothing else of the construction. So no correction of the ideals can help.

The last result has an exact scope, and the subsection after it states what it does not say. It says nothing about threefolds, nothing about invariants that remember the history of a resolution, and nothing about rules that choose larger centres. For $e = 2$ the question is open, and Proposition 3.20.22 turns it into a uniform form of Moh's bound.

### Why the case $e \ge 2$ is harder

For $e = 1$ the argument of Sections 3.1 and 3.2 has three parts. The ideal $\Theta(g)$ does not change when a $p$-th power is added to $g$ (Lemma 3.1.2), and for $e = 1$ these are exactly the changes $z \mapsto z + h$. The dichotomy of Theorem 3.1.4 gives $d \in \{\rho, \rho + 1\}$. The transformation law of Theorem 3.2.3 gives $\rho' \le \rho$ (Theorem 3.2.4). Together these parts bound $d$ along each sequence of point blowups by $\rho + 1$ at the start.

For $e \ge 2$ each part fails. First, the change $z \mapsto z + h$ adds $h^q$ to $g$, and the derivations kill all $p$-th powers, which are more than the $q$-th powers. So $\Theta(g)$ sees $g$ only modulo $p$-th powers (Remark 3.1.8), while the residual order $d$ needs the cleaning modulo $q$-th powers. Second, the residual order can go up by $p^{e-1}$ in one blowup (Theorem 1.4.1 and Example 1.4.2), so a dichotomy with the gap $1$ cannot hold together with non-increase. Third, and decisively, $d$ can tend to infinity along a sequence of point blowups at which the order stays $q$ (Theorem 1.4.3). An invariant $\iota$ with $d \le \iota + C$ that does not go up would bound $d$ by $\iota + C$ at the start of the sequence. So for $e = 3$ the two properties are incompatible, whatever the construction is. Theorem 3.20.18 makes this argument precise, and the rest of the section shows how far the Hasse-Schmidt construction goes before it meets the obstruction.

### The setting

In this section $K$ is an algebraically closed field of characteristic $p > 0$, $e \ge 1$, $q = p^e$ and $P = p^{e-1}$. Let $R = K[[x_1, \dots, x_n]]$, let $\Delta \subseteq \{1, \dots, n\}$ and $E = V(\prod_{i \in \Delta} x_i)$, and let $\Delta^c = \{1, \dots, n\} \setminus \Delta$ be the set of the free indices. We study $f = z^q + g$ with $g \in R$ and $\operatorname{ord} g \ge q$. A system of coordinates $x'$ of $R$ is *adapted* if $x'_i = u_i x_i$ with a unit $u_i$ for each $i \in \Delta$. For a clean $g \ne 0$ (Definition 1.3.1) we write $g = x^r G$ as in Definition 1.3.3, with $r_j = 0$ for $j \notin \Delta$, and $d = \operatorname{ord} G$ is the residual order. By Proposition 1.3.5 the number $d$ does not depend on the adapted coordinates.

For $\beta \in \mathbb{N}^n$ the operator $\partial^{(\beta)}$ is the Hasse derivative of Volume 1, Section 6.3, so $\partial^{(\beta)}(x^a) = \binom{a}{\beta} x^{a - \beta}$ with $\binom{a}{\beta} = \prod_i \binom{a_i}{\beta_i}$. It acts on $R$ term by term. We use the theorem of Lucas: write $a$ and $b$ in base $p$; then $\binom{a}{b} \not\equiv 0 \pmod p$ if and only if each digit of $b$ is at most the digit of $a$ at the same place. In particular, if $a$ has the nonzero digit $a_l$ at the place $l$, then $\binom{a}{p^l} \equiv a_l \not\equiv 0$. If $q \nmid a$, then $a$ has a nonzero digit at a place $l \le e - 1$, and $p^l \le P$.

For $\beta \in \mathbb{N}^\Delta$ and $\gamma \in \mathbb{N}^{\Delta^c}$ we write $s_\Delta^\beta s_{\Delta^c}^\gamma = \prod_{i \in \Delta} s_i^{\beta_i} \prod_{j \notin \Delta} s_j^{\gamma_j}$, and we view $(\beta, \gamma)$ as an element of $\mathbb{N}^n$.

### The ideals

**Definition 3.20.1.** The *logarithmic Taylor map* of $(R, \Delta)$ is the continuous homomorphism of $K$-algebras $\tau : R \to R[[s_1, \dots, s_n]]$ with
$$\tau(x_i) = x_i (1 + s_i) \ (i \in \Delta), \qquad \tau(x_j) = x_j + s_j \ (j \notin \Delta).$$
For $g \in R$ write $\tau(g) = \sum_{\beta, \gamma} \Phi_{\beta,\gamma}(g) \, s_\Delta^\beta s_{\Delta^c}^\gamma$. For $H \in R[[s]]$ and $m \ge 1$ let $C_{\le m}(H)$ be the ideal of $R$ generated by the coefficients of $H$ in the $s$-degrees $1, \dots, m$. For $1 \le m < q$ the *Hasse-Schmidt log-Jacobian ideal* of level $m$ is
$$\Theta^{\le m}(g) = \Theta^{\le m}_\Delta(g) = C_{\le m}(\tau(g)) = \bigl( \Phi_{\beta,\gamma}(g) : 0 < |\beta| + |\gamma| \le m \bigr).$$
Let $x^{\tilde r}$ be the largest monomial in the variables $x_i$, $i \in \Delta$, that divides each element of $\Theta^{\le m}(g)$. The *residual order* of the ideal is $\rho_m = \operatorname{ord} x^{-\tilde r} \Theta^{\le m}(g)$, the least order of an element. In fixed adapted coordinates, for $0 \le c \le m$ the *graded piece* $\Theta_{(c)}$ is the ideal of the generators $\Phi_{\beta,\gamma}(g)$ with $|\gamma| = c$ and $0 < |\beta| + c \le m$. Put $\rho_{(c)} = \operatorname{ord} x^{-\tilde r} \Theta_{(c)}$, with $\rho_{(c)} = \infty$ if $\Theta_{(c)} = 0$, and $\sigma = \min_c (\rho_{(c)} + c)$. Then $\rho_m = \min_c \rho_{(c)}$. The point is *balanced* at the level $m$ in these coordinates if some $c$ minimizes both $\rho_{(c)}$ and $\rho_{(c)} + c$. If $g$ is clean, the *excess* of the piece $c$ is $\varepsilon_c = \rho_{(c)} + c - d$, and the *imbalance* of $g$ is
$$\delta = \min_c \bigl( (\rho_{(c)} - \rho_m) + \varepsilon_c \bigr).$$

Node: SG0000009V · Lean: none yet

The Taylor formula $h(x + u) = \sum_\alpha \partial^{(\alpha)}(h) u^\alpha$ with $u_i = x_i s_i$ for $i \in \Delta$ and $u_j = s_j$ for $j \notin \Delta$ gives
$$\Phi_{\beta,\gamma} = x^\beta \partial^{(\beta)} \partial^{(\gamma)}, \qquad \Phi_{\beta,\gamma}(x^a) = \binom{a_\Delta}{\beta} \binom{a_{\Delta^c}}{\gamma} x^{a - \gamma}. \tag{19.1}$$
The operator $x^\beta \partial^{(\beta)}$ multiplies each monomial by a constant, and $\partial^{(\gamma)}$ lowers the degree by $|\gamma|$. For a fixed $\gamma$ the map $a \mapsto a - \gamma$ is injective. So for a fixed pair $(\beta, \gamma)$ two different monomials of $g$ give two different monomials of $\Phi_{\beta,\gamma}(g)$, and no cancellation occurs: the coefficient of $x^{a - \gamma}$ in $\Phi_{\beta,\gamma}(g)$ is the coefficient of $x^a$ in $g$ times $\binom{a_\Delta}{\beta} \binom{a_{\Delta^c}}{\gamma}$.

The ideal is truncated by the total order $|\beta| + |\gamma| \le m$ and not by the order in each variable. The values $\rho_{(c)}$, $\sigma$, $\varepsilon_c$ and $\delta$ and the balanced condition are defined in fixed coordinates, and they can depend on them. By Proposition 3.20.3 below, $\tilde r$ and $\rho_m$ do not.

**Lemma 3.20.2.** Let $A$ be a ring and $\varphi : A[[s]] \to A[[s']]$ a continuous homomorphism of $A$-algebras with $\varphi(s_i) \in (s')$ for each $i$. Then $C_{\le m}(\varphi(H)) \subseteq C_{\le m}(H)$ for each $H$ and each $m$. If $\varphi$ is an isomorphism, then equality holds.

*Proof.* Write $H = \sum_\alpha H_\alpha s^\alpha$. Then $\varphi(H) = \sum_\alpha H_\alpha \varphi(s)^\alpha$ and $\varphi(s)^\alpha \in (s')^{|\alpha|}$. So the coefficient of $\varphi(H)$ in the degree $0$ is $H_0$, and a coefficient in a degree $k \in [1, m]$ is an $A$-linear combination of the $H_\alpha$ with $1 \le |\alpha| \le k$. For the equality apply the same argument to $\varphi^{-1}$. $\square$

**Proposition 3.20.3.** Let $x'$ be adapted coordinates of $R$, and let $\tau'$ be the logarithmic Taylor map for $x'$, with the variables $s'$. Then $C_{\le m}(\tau'(g)) = C_{\le m}(\tau(g))$ for each $m$ and each $g$. So $\Theta^{\le m}(g)$, $\tilde r$ and $\rho_m$ depend only on $(R, \Delta, g)$.

*Proof.* We construct a homomorphism of $R$-algebras $\varphi : R[[s]] \to R[[s']]$ with $\varphi \circ \tau = \tau'$ on $R$. For $i \in \Delta$, $x_i = x'_i v_i(x')$ with a unit $v_i$, so $\tau'(x_i) = x'_i (1 + s'_i) v_i(\tau'(x'))$ is divisible by $x_i$ in $R[[s']]$, and the quotient is $1$ modulo $(s')$. Put $\varphi(s_i) = \tau'(x_i)/x_i - 1$. For $j \notin \Delta$ put $\varphi(s_j) = \tau'(x_j) - x_j$, which lies in $(s')$. Then $\varphi(\tau(x_l)) = \tau'(x_l)$ for each $l$. Both $\varphi \circ \tau$ and $\tau'$ are continuous homomorphisms on $R$, so $\varphi \circ \tau = \tau'$. The same construction gives $\varphi'$ with $\varphi' \circ \tau' = \tau$. Then $\chi = \varphi' \circ \varphi$ satisfies $\chi \circ \tau = \tau$. From $x_i (1 + \chi(s_i)) = x_i (1 + s_i)$ in the domain $R[[s]]$ we get $\chi(s_i) = s_i$, and in the same way $\chi(s_j) = s_j$. So $\chi$ is the identity, and so is $\varphi \circ \varphi'$. Lemma 3.20.2 gives the equality. $\square$

**Proposition 3.20.4.** Let $j \ge 1$ and $m < p^j$. Then $\Theta^{\le m}(g + h^{p^j}) = \Theta^{\le m}(g)$ for each $h \in R$. In particular, for $m < q$ the ideal $\Theta^{\le m}(g)$ does not change under $g \mapsto g + h^q$, so it does not see the choice of $z$ in $z^q + g$.

*Proof.* The map $\tau$ is a ring homomorphism and $R[[s]]$ has characteristic $p$, so
$$\tau(h^{p^j}) = \tau(h)^{p^j} = \bigl( h + (\tau(h) - h) \bigr)^{p^j} = h^{p^j} + (\tau(h) - h)^{p^j}.$$
Since $\tau(h) - h \in (s)$, the last term lies in $(s)^{p^j}$, and it has no coefficient in the degrees $1, \dots, m$. $\square$

The level $m$ is not invariant in general under the addition of $p^{j}$-th powers with $p^j \le m$. For example, $\Phi_{0, P e_1}(x_1^P) = 1$ for $1 \notin \Delta$. And the bound $m < q$ is necessary: for $1 \in \Delta$, $\tau(x_1^q) = x_1^q (1 + s_1^q)$ has the coefficient $x_1^q$ in the degree $q$.

**Remark 3.20.5 (the level $1$).** The generators of $\Theta^{\le 1}(g)$ are $\Phi_{e_i, 0}(g) = x_i \partial_i g$ for $i \in \Delta$ and $\Phi_{0, e_j}(g) = \partial_j g$ for $j \notin \Delta$. So $\Theta^{\le 1}(g)$ is the log-Jacobian ideal $\Theta(g)$ of Definition 3.1.1, and Proposition 3.20.4 with $j = 1$ is Lemma 3.1.2. For $e = 1$ the only level is $m = 1 = P$, and the results below for $P \le m < q$ give back Theorems 3.1.4 and 3.2.3. For $e \ge 2$ the ideal $\Theta^{\le 1}(g)$ is still defined and still invariant under $g \mapsto g + h^q$, but by Remark 3.1.8 it forgets too much: it can be $0$ for a clean $g$.

### The dichotomy at the top levels

**Theorem 3.20.6.** Let $g \ne 0$ be clean and let $P \le m < q$. Then, in each adapted coordinate system in which $g$ is clean:

1. $\tilde r = r$;
2. $\rho_{(c)} + c \ge d$ for each $c$;
3. there is a $c_0 \in \{0\} \cup \{p^l : 0 \le l \le e - 1\}$ with $\rho_{(c_0)} + c_0 = d$.

So $\sigma = d$, each excess $\varepsilon_c$ is at least $0$ and some $\varepsilon_c$ is $0$, and
$$\rho_m \le d \le \rho_m + m.$$
Also $\delta \ge 0$, and $\delta = 0$ if and only if $g$ is balanced at the level $m$ in these coordinates.

Node: SG0000009W · Lean: none yet

*Proof.* By (19.1), each term of $\Phi_{\beta,\gamma}(g)$ is a constant times $x^{a - \gamma}$ for a monomial $x^a$ of $g$, and $\gamma$ changes only the free exponents. So $x^r$ divides each generator.

Part 1. Fix $i \in \Delta$ and a monomial $x^a$ of $g$ with $a_i = r_i$. Since $g$ is clean, some $a_k$ is not divisible by $q$, so $a_k$ has a nonzero digit at a place $l \le e - 1$. Let $\alpha = p^l e_k$, viewed as $\beta$ if $k \in \Delta$ and as $\gamma$ if $k \notin \Delta$. Then $0 < |\alpha| = p^l \le P \le m$, the coefficient $\binom{a_k}{p^l}$ is not $0$ by Lucas, and by the injectivity after (19.1) the generator $\Phi_\alpha(g)$ contains the monomial $x^{a - \alpha_{\Delta^c}}$. Its exponent at $i$ is $r_i$. So $x_i^{r_i + 1}$ does not divide $\Theta^{\le m}(g)$, and $\tilde r = r$.

Part 2. A term of a generator of $\Theta_{(c)}$ is a constant times $x^{a - \gamma}$ with $|\gamma| = c$ and $x^a$ a monomial of $g$. Here $x^{a - r}$ is a monomial of $G$, of degree at least $d$. So $x^{a - \gamma - r}$ has degree at least $d - c$, and $\rho_{(c)} \ge d - c$ by part 1.

Part 3. Let $x^b$ be a monomial of $\operatorname{in}(G)$, so $|b| = d$, and $x^{r + b}$ is a monomial of $g$. First assume that some $j \notin \Delta$ has $q \nmid b_j$. Take a place $l \le e - 1$ with a nonzero digit of $b_j$ and put $\gamma = p^l e_j$, $\beta = 0$. Then $|\gamma| = p^l \le m$, and $\Phi_{0, \gamma}(g)$ contains $x^{r + b - \gamma}$ with a nonzero coefficient. After the division by $x^r$ it has the degree $d - p^l$. So $\rho_{(p^l)} \le d - p^l$, and part 2 gives equality, with $c_0 = p^l$. Now assume that $q \mid b_j$ for each $j \notin \Delta$. The monomial $x^{r + b}$ of $g$ is not a $q$-th power, so $q \nmid r_i + b_i$ for some $i \in \Delta$. Take a place $l \le e - 1$ with a nonzero digit of $r_i + b_i$ and put $\beta = p^l e_i$, $\gamma = 0$. Then $\Phi_{\beta, 0}(g)$ contains $\binom{r_i + b_i}{p^l} x^{r + b}$, of degree $d$ after the division. So $\rho_{(0)} \le d$, and part 2 gives equality, with $c_0 = 0$.

Parts 2 and 3 give $\sigma = d$, and so $\varepsilon_c \ge 0$ with $\varepsilon_{c_0} = 0$. Then $\rho_m \le \rho_{(c_0)} = d - c_0 \le d$. If $c$ is a value with $\rho_{(c)} = \rho_m$, then $d \le \rho_{(c)} + c \le \rho_m + m$, since $c \le m$. Both terms in the definition of $\delta$ are at least $0$, so $\delta = 0$ if and only if some $c$ has $\rho_{(c)} = \rho_m$ and $\rho_{(c)} + c = d = \sigma$, which is the balanced condition. $\square$

For $e = m = 1$ the theorem is the dichotomy $d \in \{\rho, \rho + 1\}$ of Theorem 3.1.4. For $e \ge 2$ the best choice is $m = P$, with the gap $P = p^{e-1}$, which is the size of the jump in Moh's bound. By Proposition 3.20.3, $\rho_P \le d \le \rho_P + P$ in each adapted clean coordinate system. For $m < P$ the theorem fails in general. For $p = 2$, $q = 4$, $\Delta = \emptyset$ and $g = x^2 y^2$ the ideal $\Theta^{\le 1}(g)$ is $0$ (Remark 3.1.8), and for $\Delta = \{x\}$ and $g = x^2 y^2 + x^3$ the exponent $\tilde r = 3$ is larger than $r = 2$ (Exercise 9).

### The transformation law

We use the chart $\pi = \pi_{1,t}$ of Section 3.2: $\pi(x_1) = x_1$ and $\pi(x_i) = x_1 (x_i + t_i)$ for $i \ne 1$, with $t \in K^{n-1}$. Since $K$ is algebraically closed, after a change of the numbering each closed point of the exceptional divisor is the origin of such a chart. Let $R' = K[[x]]$ be the completed local ring at the origin of the chart, let $g' = x_1^{-q} \pi(g)$ (Lemma 1.3.7), and let $\Delta' = \{1\} \cup \{i \in \Delta : i \ne 1, \ t_i = 0\}$. We write $\Theta' = \Theta^{\le m}_{\Delta'}(g')$ and $\rho'_m$ for its residual order. By Proposition 3.20.4 we do not need to clean $g'$.

**Theorem 3.20.7.** Assume $\operatorname{ord} g \ge q$, and let $1 \le m < q$. Then
$$x_1^q \, \Theta' = \bigl( x_1^{|\gamma|} \pi(\Phi_{\beta,\gamma}(g)) : 0 < |\beta| + |\gamma| \le m \bigr) R'.$$

*Proof.* Let $\tau'$ be the logarithmic Taylor map of $(R', \Delta')$, with the variables $s'$. We compute $\tau'(\pi(x_l))$ for each $l$.

* $l = 1$. Since $1 \in \Delta'$, $\tau'(x_1) = x_1 (1 + s'_1)$. If $1 \in \Delta$ this is $\pi(x_1)(1 + S_1)$ with $S_1 = s'_1$, and if $1 \notin \Delta$ it is $\pi(x_1) + x_1 T_1$ with $T_1 = s'_1$.
* $i \in \Delta$, $i \ne 1$, $t_i = 0$. Then $i \in \Delta'$ and $\tau'(\pi(x_i)) = x_1 (1 + s'_1) x_i (1 + s'_i) = \pi(x_i)(1 + S_i)$ with $S_i = s'_1 + s'_i + s'_1 s'_i$.
* $i \in \Delta$, $t_i \ne 0$. Then $i \notin \Delta'$, the series $x_i + t_i$ is a unit of $R'$, and $\tau'(\pi(x_i)) = x_1 (1 + s'_1)(x_i + t_i + s'_i) = \pi(x_i)(1 + S_i)$ with $S_i = s'_1 + (x_i + t_i)^{-1} (1 + s'_1) s'_i$.
* $j \notin \Delta$, $j \ne 1$. Then $j \notin \Delta'$ and $\tau'(\pi(x_j)) = x_1 (1 + s'_1)(x_j + t_j + s'_j) = \pi(x_j) + x_1 T_j$ with $T_j = (x_j + t_j) s'_1 + (1 + s'_1) s'_j$.

Let $\Lambda : R \to R'[[s]]$ be the composite of $\tau$, of $\pi$ applied to the coefficients, and of the substitution $s_j \mapsto x_1 s_j$ for $j \notin \Delta$. It is a continuous homomorphism, and
$$\Lambda(g) = H = \sum_{\beta, \gamma} \pi(\Phi_{\beta,\gamma}(g)) \, x_1^{|\gamma|} \, s_\Delta^\beta s_{\Delta^c}^\gamma.$$
Let $\psi : R'[[s]] \to R'[[s']]$ be the continuous homomorphism of $R'$-algebras with $\psi(s_i) = S_i$ for $i \in \Delta$ and $\psi(s_j) = T_j$ for $j \notin \Delta$. Then $\psi(\Lambda(x_i)) = \pi(x_i)(1 + S_i) = \tau'(\pi(x_i))$ for $i \in \Delta$ and $\psi(\Lambda(x_j)) = \pi(x_j) + x_1 T_j = \tau'(\pi(x_j))$ for $j \notin \Delta$. Two continuous homomorphisms on $R$ that agree on the variables are equal, so $\tau'(\pi(g)) = \psi(H)$.

All $S_i$ and $T_j$ lie in $(s')$. Their linear parts are $s'_1$ for the index $1$ and $a_l s'_l + b_l s'_1$ for $l \ne 1$, with $b_l \in R'$ and $a_l$ equal to $1$ or to the unit $(x_l + t_l)^{-1}$. With the index $1$ first, the matrix of the linear parts is triangular with units on the diagonal. So $\psi$ is an isomorphism, by the inverse function theorem for formal power series over $R'$. Lemma 3.20.2 gives
$$C_{\le m}(\tau'(\pi(g))) = C_{\le m}(H) = \bigl( x_1^{|\gamma|} \pi(\Phi_{\beta,\gamma}(g)) : 0 < |\beta| + |\gamma| \le m \bigr) R'.$$
Finally $\pi(g) = x_1^q g'$, so $\tau'(\pi(g)) = \tau'(x_1)^q \tau'(g') = x_1^q (1 + s'_1)^q \tau'(g') = x_1^q (1 + s_1'^q) \tau'(g')$. The factor $1 + s_1'^q$ is $1$ modulo $(s')^q$, so it does not change the coefficients in the degrees at most $m < q$. Thus $C_{\le m}(\tau'(\pi(g))) = x_1^q C_{\le m}(\tau'(g')) = x_1^q \Theta'$. $\square$

The free order $c = |\gamma|$ enters only through the factor $x_1^{|\gamma|}$. It comes from $\tau'(\pi(x_j)) - \pi(x_j) = x_1 T_j$: a free variable $x_j = x_1 (x_j + t_j)$ moves by $x_1$ times a unit direction, while a boundary variable moves by a factor. The only input from the characteristic is $(1 + s)^q = 1 + s^q$, and this is where $m < q$ is used. For $e = m = 1$ the theorem is Theorem 3.2.3.

**Theorem 3.20.8 (the graded law).** Assume $\operatorname{ord} g \ge q$, let $1 \le m < q$, and write $\pi(x^{-\tilde r} \Theta_{(c)}) R' = x_1^{\rho_{(c)}} W_c$ for each $c$ with $\Theta_{(c)} \ne 0$. Then each $W_c$ has order at most $\rho_{(c)}$ and is not contained in $(x_1)$. Up to a unit,
$$\Theta' = x_1^{|\tilde r| + \sigma - q} \Bigl( \prod_{i \in \Delta', i \ne 1} x_i^{\tilde r_i} \Bigr) W, \qquad W = \sum_c x_1^{c + \rho_{(c)} - \sigma} W_c,$$
the ideal $W$ is not contained in $(x_1)$, and
$$\rho'_m \le \min_c \bigl( c + 2 \rho_{(c)} - \sigma \bigr).$$
If $g$ is clean and $P \le m < q$, then $\tilde r = r$ and $\sigma = d$, the exponent of the piece $c$ in $W$ is its excess $\varepsilon_c$, and
$$\Theta' = x_1^{|r| + d - q} \Bigl( \prod_{i \in \Delta', i \ne 1} x_i^{r_i} \Bigr) \sum_c x_1^{\varepsilon_c} W_c, \qquad \rho'_m \le \min_c (\varepsilon_c + \rho_{(c)}) = \rho_m + \delta.$$

Node: SG0000009X · Lean: none yet

*Proof.* Let $J_c = x^{-\tilde r} \Theta_{(c)}$, an ideal of order $\rho_{(c)}$. An element $h = \sum_{k \ge \rho_{(c)}} h_k$ of $J_c$, with $h_k$ homogeneous of degree $k$, has $\pi(h) = \sum_k x_1^k h_k(1, x_2 + t_2, \dots, x_n + t_n)$, so $\pi(J_c) R'$ is divisible by $x_1^{\rho_{(c)}}$, and $W_c$ is defined. Take $h \in J_c$ of order $\rho_{(c)}$. Its weak transform $x_1^{-\rho_{(c)}} \pi(h)$ restricts on $x_1 = 0$ to $h_{\rho_{(c)}}(1, x_2 + t_2, \dots, x_n + t_n)$, which is not $0$ and has degree at most $\rho_{(c)}$ by Lemma 2.2.1. So the weak transform is not in $(x_1)$, and its order is at most $\rho_{(c)}$, as in the proof of Theorem 2.2.2. Thus $W_c \not\subseteq (x_1)$ and $\operatorname{ord} W_c \le \rho_{(c)}$.

Group the generators of Theorem 3.20.7 by $c = |\gamma|$. This gives $x_1^q \Theta' = \sum_c x_1^c \pi(\Theta_{(c)}) R'$. Now $\pi(x^{\tilde r}) = x_1^{|\tilde r|} \prod_{i \ne 1} (x_i + t_i)^{\tilde r_i}$, with $\tilde r_i = 0$ for $i \notin \Delta$. The factors with $t_i \ne 0$ are units, and the factors with $t_i = 0$ and $i \in \Delta$, $i \ne 1$, are $x_i^{\tilde r_i}$ with $i \in \Delta'$. So
$$x_1^q \Theta' = x_1^{|\tilde r|} \Bigl( \prod_{i \in \Delta', i \ne 1} x_i^{\tilde r_i} \Bigr) u \sum_c x_1^{c + \rho_{(c)}} W_c$$
with a unit $u$, which is the displayed formula after the division by $x_1^{q + \sigma}$. For a $c$ with $c + \rho_{(c)} = \sigma$ the summand of $W$ is $W_c \not\subseteq (x_1)$, so $W \not\subseteq (x_1)$. Let $\mu$ be the largest monomial in the variables of $\Delta'$ that divides $W$. Then $x_1 \nmid \mu$, the monomial factor of $\Theta'$ is the displayed monomial times $\mu$, and
$$\rho'_m = \operatorname{ord}(\mu^{-1} W) \le \operatorname{ord} W \le \operatorname{ord}\bigl( x_1^{c + \rho_{(c)} - \sigma} W_c \bigr) \le c + \rho_{(c)} - \sigma + \rho_{(c)}$$
for each $c$. For $P \le m < q$ and $g$ clean, Theorem 3.20.6 gives $\tilde r = r$ and $\sigma = d$. Then $c + \rho_{(c)} - \sigma = \varepsilon_c$ and $c + 2 \rho_{(c)} - \sigma = \varepsilon_c + \rho_{(c)} = \rho_m + (\rho_{(c)} - \rho_m) + \varepsilon_c$, and the minimum over $c$ is $\rho_m + \delta$. $\square$

The mechanism is visible in the formula. The piece that gives the minimum $\rho_m$ carries the factor $x_1^{\varepsilon_c}$. After the blowup $x_1$ is a boundary variable, but it does not divide the whole ideal $W$, because the piece with zero excess is not in $(x_1)$. So the powers of $x_1$ in the other pieces count in the residual order, and $\rho_m$ can go up by as much as $\delta$. The piece with zero excess has the order $\rho_{(c)} = d - c$, and this can be larger than $\rho_m$.

**Corollary 3.20.9.** Assume $\operatorname{ord} g \ge q$ and $1 \le m < q$. If $g$ is balanced at the level $m$ in some adapted coordinates, then $\rho'_m \le \rho_m$ at each closed point of order $q$ over the origin.

*Proof.* The values $\rho_m$ and $\rho'_m$ do not depend on the coordinates (Proposition 3.20.3), and the blowup of the origin does not depend on them either. So we can compute in coordinates in which $g$ is balanced, and each closed point over the origin is the origin of a chart of these coordinates. Take $c$ with $\rho_{(c)} = \rho_m$ and $\rho_{(c)} + c = \sigma$. Then $c + 2 \rho_{(c)} - \sigma = \rho_m$, and Theorem 3.20.8 gives $\rho'_m \le \rho_m$. $\square$

**Corollary 3.20.10.** For each $e \ge 1$ the residual order $\rho_1$ does not go up under the blowup of a closed point of order $q$, at each point over it.

*Proof.* At the level $1$ the free orders are $c = 0$ and $c = 1$. If $\rho_1 = \rho_{(0)}$, then $\rho_{(0)} \le \rho_{(1)} < \rho_{(1)} + 1$, so $c = 0$ minimizes both $\rho_{(c)}$ and $\rho_{(c)} + c$. If $\rho_{(1)} < \rho_{(0)}$, then $\rho_{(1)} + 1 \le \rho_{(0)}$, so $c = 1$ minimizes both. So each point is balanced at the level $1$, and Corollary 3.20.9 applies. $\square$

For $e = 1$ this is Theorem 3.2.4. For $e \ge 2$ it says that the log-Jacobian ideal of Section 3.1 keeps its non-increase when the equation is $z^q + g$, but by Theorem 3.20.6 and Remark 3.20.5 its residual order no longer controls $d$. Corollary 3.20.20 below shows that for $e = 3$ it cannot control $d$ in any way.

**Corollary 3.20.11.** Assume $\operatorname{ord} g \ge q$ and $1 \le m < q$. If $\rho'_m > \rho_m$ at some point over the origin, then $g$ is unbalanced at the level $m$ in each adapted coordinate system.

Node: SG000000A2 · Lean: none yet

*Proof.* This is the contrapositive of Corollary 3.20.9. $\square$

**Remark 3.20.12 (Moh's bound again).** Let $g$ be clean with $\operatorname{ord} g \ge q$, and let $c_0$ be as in part 3 of Theorem 3.20.6 for $m = P$. Theorem 3.20.8 with $c = c_0$ gives $\rho'_P \le c_0 + 2 (d - c_0) - d = d - c_0 \le d$. Let $d'$ be the residual order of the clean part of $g'$, if it is not $0$. Its ideal is $\Theta'$ by Proposition 3.20.4, so Theorem 3.20.6 at the new point gives $d' \le \rho'_P + P \le d + P$. This is Theorem 1.4.1 at the closed points over the origin, with a proof that goes through the ideals.

### Examples

The first example shows that the top level $\rho_P$ goes up already for $e = 2$.

**Example 3.20.13.** Let $p = 2$, $q = 4$, $P = 2$, $R = K[[x, y]]$, $\Delta = \{x\}$ and $g = x^5 + x^4 y^2$. Then $g$ is clean, $r = (4, 0)$, $G = x + y^2$ and $d = 1$. By (19.1) the nonzero generators of $\Theta^{\le 2}(g)$ are $\Phi_{e_x, 0}(x^5) = x^5$ and $\Phi_{0, 2 e_y}(x^4 y^2) = x^4$, since $\binom51 = 5$ and $\binom22 = 1$ are odd, while $\binom41$, $\binom42$, $\binom52$ and $\binom21$ are even. So $\Theta^{\le 2}(g) = (x^4)$ and $\rho_2 = 0$, with $\rho_{(0)} = 1$, $\rho_{(2)} = 0$, $\rho_{(1)} = \infty$, $\sigma = 1 = d$ and $\delta = \min(1 + 0, 0 + 1) = 1$. The point is unbalanced. At the origin of the $y$-chart, $g' = x^5 y + x^4 y^2$ and $\Delta' = \{x, y\}$. Each variable is a boundary variable, and both monomials have an odd logarithmic coefficient of order at most $2$, namely $\binom51$ for $x^5 y$ and $\binom22$ for $x^4 y^2$. So $\Theta' = (x^5 y, x^4 y^2) = x^4 y (x, y)$ and $\rho'_2 = 1 = \rho_2 + \delta$, while $d' = 1$.

Node: SG000000A3 · Lean: none yet

The second example shows that a level strictly between $1$ and $P$ goes up.

**Example 3.20.14.** Let $p = 2$, $q = 8$, $P = 4$, $R = K[[x, y, w]]$, $\Delta = \{x, y\}$ and
$$g = x^4 y^8 w + x^4 y^4 w^2 + x^6 y^3.$$
The nonzero generators of $\Theta^{\le 2}(g)$ are $x^6 y^3$, from $\beta = e_y$, $2 e_x$ and $2 e_y$ on the last monomial, $x^4 y^8$, from $\gamma = e_w$, and $x^4 y^4$, from $\gamma = 2 e_w$. So $\Theta^{\le 2}(g) = x^4 y^3 (x^2, y^5, y)$ and $\rho_2 = 1$. In the $w$-chart, $\pi(x) = xw$, $\pi(y) = yw$, and at the origin $g' = x^4 y^8 w^5 + x^4 y^4 w^2 + x^6 y^3 w$ with $\Delta' = \{x, y, w\}$. The three monomials have the odd logarithmic coefficients $\binom51$, $\binom22$ and $\binom11$ of order at most $2$, so $\Theta' = x^4 y^3 w (y^5 w^4, y w, x^2)$ and $\rho'_2 = 2$. Meanwhile $\rho_1 = 2$ and $d = 2$ do not change.

Node: SG000000A4 · Lean: none yet

In Example 3.20.14 the levels $\rho_3$ and $\rho_4$ also go from $1$ to $2$, and the origin of the $w$-chart is the only point with coordinates in $\mathbb{F}_2$ of order $8$ over the origin (research note 78). The next result shows that each level from $2$ on goes up, for each $p$ and $e$.

**Proposition 3.20.15.** Let $q = p^e \ge 3$ and $2 \le m < q$. Let $R = K[[x, y]]$, $\Delta = \{x\}$ and $g = x^{q+1} y^m + x^{q+2}$. Then $g$ is clean, $\operatorname{ord} g \ge q$, $\Theta^{\le m}(g) = (x^{q+1})$ and $\rho_m = 0$. At the origin of the $y$-chart,
$$\Theta' = x^{q+1} y^2 (y^{m-1}, x), \qquad \rho'_m = 1.$$

Node: SG000000A5 · Lean: none yet

*Proof.* The exponent $q + 1$ of $x$ is not divisible by $q$, so $g$ is clean, and $\operatorname{ord} g = \min(q + 1 + m, q + 2) \ge q$. On $x^{q+1} y^m$ the generator with $\beta = 0$ and $\gamma = m$ is $\binom{m}{m} x^{q+1} = x^{q+1}$. Each generator on $x^{q+1} y^m$ is a multiple of $x^{q+1}$, and each generator on $x^{q+2}$ is a multiple of $x^{q+2}$. So $\Theta^{\le m}(g) = (x^{q+1})$, $\tilde r = q + 1$ and $\rho_m = 0$. In the $y$-chart, $\pi(x) = xy$ and $\pi(y) = y$, so $g' = y^{-q} \pi(g) = x^{q+1} y^{m+1} + x^{q+2} y^2$, with $\Delta' = \{x, y\}$ and no free variable. By (19.1) each generator is a constant times a monomial of $g'$, so $\Theta'$ is generated by the monomials of $g'$ that have a nonzero logarithmic coefficient $\binom{a}{\beta}$ for some $0 < |\beta| \le m$. For $x^{q+1} y^{m+1}$ take $\beta = (1, 0)$: $\binom{q+1}{1} = 1$. For $x^{q+2} y^2$, if $p$ is odd take $\beta = (1, 0)$: $\binom{q+2}{1} = 2 \ne 0$; if $p = 2$ take $\beta = (0, 2)$: $\binom22 = 1$, and $|\beta| = 2 \le m$. So $\Theta' = (x^{q+1} y^{m+1}, x^{q+2} y^2) = x^{q+1} y^2 (y^{m-1}, x)$, and its residual order is $\min(m - 1, 1) = 1$ because $m \ge 2$. $\square$

So among the levels $m < q$, exactly the level $m = 1$ does not go up (Corollary 3.20.10). For $e = 2$ and $m = P$ the proposition extends Example 3.20.13 to each $p$. For $m \ge P$ we have $d = 1$, $\rho_{(m)} = 0$, $\rho_{(0)} = 1$ and $\delta = 1$, so the increase attains the bound $\rho_m + \delta$ of Theorem 3.20.8. By Corollary 3.20.11 the origin is unbalanced in each adapted coordinate system.

### Upper semicontinuity

The no-go theorem below is about invariants that do not go up under the blowups of points. Upper semicontinuity is the property that puts each closed point into the local top locus of an invariant, so that the blowup of the point is a blowup inside the top locus. The residual orders $\rho_m$ have this property.

**Lemma 3.20.16.** Let $1 \le m < q$.

1. Let $W$ be a smooth variety over $K$ with a simple normal crossings divisor $E$, and let $g \in \mathcal{O}(W)$. The ideals $\Theta^{\le m}$ of the completed local rings at the closed points, for the components of $E$ through the point, come from one coherent ideal sheaf $\mathcal{T}_m$, which does not change under $g \mapsto g + h^q$. Let $D$ be the largest effective divisor with support in $E$ such that $\mathcal{T}_m \subseteq \mathcal{O}(-D)$. Then $\rho_m(x) = \operatorname{ord}_x (\mathcal{T}_m \cdot \mathcal{O}(D))$ at each closed point $x$, and $x \mapsto \rho_m(x)$ is the restriction to the closed points of an upper semicontinuous function on $W$.
2. Let $\iota$ be an upper semicontinuous function on a scheme, with values in a well-ordered set. Then each point $x$ has an open neighbourhood $U$ with $\iota \le \iota(x)$ on $U$. So each closed point $x$ lies in the top locus of $\iota$ on $U$, and the blowup of $x$ is the blowup of a regular centre inside the local top locus.

Node: SG0000009Y · Lean: none yet

*Proof.* Part 1. Near each closed point there are regular functions $x_1, \dots, x_n$ that are étale coordinates and in which $E$ is $V(\prod_{i \in \Delta} x_i)$. Hasse-Schmidt derivations extend uniquely along étale homomorphisms, so the operators $\Phi_{\beta,\gamma} = x^\beta \partial^{(\beta)} \partial^{(\gamma)}$ are defined on this open set $U$. Let $\mathcal{T}_m$ on $U$ be the ideal generated by the $\Phi_{\beta,\gamma}(g)$ with $0 < |\beta| + |\gamma| \le m$. At a closed point $y \in U$ the completed local ring is $K[[x - x(y)]]$, and its boundary indices are the $i \in \Delta$ with $x_i(y) = 0$. Two changes compare the completion of $\mathcal{T}_m$ at $y$ with $\Theta^{\le m}$ at $y$. First, a translation $x_l \mapsto x_l - x_l(y)$ does not change the Taylor map, because $\tau(x_l - c) = \tau(x_l) - c$. Second, for $i \in \Delta$ with $x_i(y) \ne 0$ the variable $x_i$ is a unit at $y$, and the substitution $s_i \mapsto x_i s_i$, an isomorphism of power series rings, changes $x_i(1 + s_i)$ into $x_i + x_i s_i$, the form of a free variable. By Lemma 3.20.2 neither change alters the ideal. So the completion of $\mathcal{T}_m$ at $y$ is $\Theta^{\le m}$ at $y$. By Proposition 3.20.3 two such ideals on an overlap have the same completions at the closed points, and the completion is faithfully flat, so they agree. Thus the local ideals glue to a coherent ideal $\mathcal{T}_m$. By Proposition 3.20.4 it does not change under $g \mapsto g + h^q$.

Each component $E_i$ of $E$ is smooth, so at a closed point $y \in E_i$ its local equation $x_i$ is a prime element of $\mathcal{O}_{W,y}$, and the prime ideal $(x_i)$ is the generic point of $E_i$. The local ring is factorial, so $\mathcal{T}_{m,y} \subseteq x_i^a \mathcal{O}_{W,y}$ if and only if the valuation of $\mathcal{T}_m$ along $E_i$ is at least $a$, and by faithful flatness the same holds in the completion. So the multiplicity of $D$ along $E_i$ is the local exponent $\tilde r_i$ at each closed point of $E_i$, the local equation of $D$ at $y$ is the monomial $x^{\tilde r}$, and $\rho_m(y) = \operatorname{ord}_y (\mathcal{T}_m \cdot \mathcal{O}(D))$. The order of a coherent ideal $\mathcal{I}$ on $W$ is upper semicontinuous: in étale coordinates the set where it is at least $a$ is the zero set of the ideal generated by the $\partial^{(\alpha)} \mathcal{I}$ with $|\alpha| < a$, as in Proposition 1.1.4. This gives part 1.

Part 2. If $\iota(x)$ is the largest value, take $U$ the whole scheme. Otherwise let $\lambda^+$ be the least value larger than $\iota(x)$, which exists because the set of values is well ordered. The set $\{\iota \ge \lambda^+\}$ is closed by upper semicontinuity, and it does not contain $x$. Its complement $U$ is open, and on $U$ we have $\iota < \lambda^+$, that is, $\iota \le \iota(x)$. $\square$

Part 2 is about the local top locus at a closed point. It is not about the global top locus that a resolution algorithm uses. Upper semicontinuity is not automatic for invariants built from Hasse-Schmidt derivations. Benito and Villamayor define an invariant with differential Rees algebras and elimination algebras that does not depend on the choices, and they show that in positive characteristic it is not upper semicontinuous in general [BenV13, Sections 1.5 and 4.1].

### The no-go theorem

**Definition 3.20.17.** Fix a prime $p$, $e \ge 1$, $q = p^e$ and $n \ge 1$. Let $\mathcal{G}_{e,n}$ be the class of the germs $(R, \Delta, g)$ with $R = K[[x_1, \dots, x_n]]$ over an algebraically closed field $K$ of characteristic $p$, $\Delta \subseteq \{1, \dots, n\}$ and $\operatorname{ord} g \ge q$. An *invariant* is a function $\iota$ of the germ $(R, \Delta, g)$ alone, with values in a well-ordered set $\Lambda$, that does not change under the changes of adapted coordinates and under $g \mapsto g + h^q$. Through the germs at the points, an invariant is a function on the points of order $q$ of each hypersurface $z^q + g = 0$ over a smooth variety with a simple normal crossings divisor. Consider the properties:

* (U) these functions are upper semicontinuous;
* (N) for each closed point $x$ and each regular centre $C \ni x$ that lies in the local top locus of $\iota$ and is permissible for $f$, each point of order $q$ over $x$ of the strict transform has $\iota' \le \iota(x)$;
* (N$_{pt}$) the property (N) for the centres $C = \{x\}$, at each closed point $x$ of order $q$;
* (D) there is a monotone function $F : \Lambda \to \mathbb{N}$ with $d \le F(\iota)$ on each germ;
* (D') for each $\lambda \in \Lambda$, the residual order $d$ is bounded on the germs with $\iota = \lambda$.

The residual order $d$ is computed after cleaning, and by Proposition 1.3.5 it does not depend on the adapted coordinates. The property (D) implies (D'), because $d \le F(\lambda)$ on the fibre of $\lambda$. Each invariant with a dichotomy of bounded gap, $d \le \iota + C$ with values in $\mathbb{N}$, has (D) with $F(\lambda) = \lambda + C$. By Theorem 3.20.6, each invariant with $\rho_P \le F_0(\iota)$ for a monotone $F_0$ has (D) with $F = F_0 + P$. The property (D') also holds for lexicographic invariants such as $(d, \rho_P)$ or $(\rho_P, \pm \delta)$ with values in $\mathbb{N}^2$. By Lemma 3.20.16, part 2, the properties (U) and (N) imply (N$_{pt}$), because a closed point of order $q$ is a permissible centre and lies in the local top locus.

The input from [HP19a] is exactly the following statement, which is Theorem 1.4.3 with the facts of its proof that we use.

> (HP) Let $e = 3$. For $p = 2$ there is a polynomial germ $z^8 + g$ in the variables $x, y, u, v, w$, so with $n = 5$, and for each $p \ge 3$ there is a polynomial germ $z^{p^3} + g$ in the variables $x, y, v, w$, so with $n = 4$, together with an infinite sequence of point blowups with these properties. Each centre is a closed point of order $p^3$ of the strict transform, and the next centre is a point of order $p^3$ over it. The new divisor is the exceptional divisor together with the old components that pass through the new point, as in Section 1.3. The residual order of the cleaned equation for this divisor tends to infinity along the sequence: it goes up by $2$ per pass of the cycle for $p = 2$, and by $p(p - 1)/2$ per pass for $p \ge 3$.

[HP19a, Section 4] proves (HP). The maximal ideal of a point of order $q$ is always a permissible centre. [HP19a] states that the example disproves the stability claim of Moh for $e \ge 3$, which is known to hold for $e = 1$, and that larger centres are also permissible and prevent the phenomenon. Example 1.4.5 is one certified pass of the first cycle.

**Theorem 3.20.18 (no-go).** Let $q = p^3$, and let $n \ge 5$ if $p = 2$ and $n \ge 4$ if $p \ge 3$. Assume (HP). Then no invariant on $\mathcal{G}_{3,n}$ has the properties (N$_{pt}$) and (D'). In particular, no invariant on $\mathcal{G}_{3,n}$ has the properties (U), (N) and (D').

Node: SG0000009Z · Lean: none yet

*Proof.* First we get a sequence as in (HP) in $n$ variables. Let $n_0 = 5$ for $p = 2$ and $n_0 = 4$ for $p \ge 3$, take the germ of (HP), and add $n - n_0$ free variables $t$ that are never translated and never the variable of a chart. Each blowup of the sequence maps each $t_k$ to $x_j t_k$, where $x_j$ is the variable of the chart, and the origin of the chart in the new variables is again the centre. The function $g$ does not contain $t$, so the strict transform is the same function as before, its order and its cleaning do not change, and the boundary indices do not change because the variables $t$ are free. So the order stays $q$ and $d_k \to \infty$, as in (HP).

Let $x_0, x_1, \dots$ be the centres of this sequence, let $\iota_k = \iota(x_k)$, and let $d_k$ be the residual order at $x_k$. The point $x_{k+1}$ is a point of order $q$ over $x_k$, so (N$_{pt}$) gives $\iota_{k+1} \le \iota_k$. A non-increasing sequence in a well-ordered set is eventually constant, since otherwise it would have an infinite strictly decreasing subsequence. So $\iota_k = \lambda$ for $k \ge k_0$. By (D'), the residual orders $d_k$ with $k \ge k_0$ are bounded. This contradicts $d_k \to \infty$. The second statement follows, because (U) and (N) imply (N$_{pt}$). $\square$

The proof is short, and this is the point. The obstruction is the unboundedness of $d$, and not a defect of the Hasse-Schmidt construction. No refinement of $\Theta^{\le m}$ by lexicographic orders, weights, the vector $(\rho_{(c)})_c$ or other data of the germ can give both a bound on $d$ and non-increase under point blowups when $e = 3$.

**Corollary 3.20.19.** Let $p$ and $n$ be as in Theorem 3.20.18, assume (HP), and let $\iota$ be an invariant on $\mathcal{G}_{3,n}$ with the property (D'). Then along the sequence of (HP), $\iota$ goes up at infinitely many steps. This holds when $\rho_P \le F_0(\iota)$ for a monotone $F_0 : \Lambda \to \mathbb{N}$, in particular for $\iota = \rho_P$ and for $\iota = \rho_m$ with $P \le m < q$.

Node: SG000000A0 · Lean: none yet

*Proof.* If $\iota$ went up at finitely many steps only, then it would not go up after some step $k_0$, and the proof of Theorem 3.20.18 applied to the tail $x_{k_0}, x_{k_0 + 1}, \dots$ would give a contradiction. If $\rho_P \le F_0(\iota)$, then $d \le \rho_P + P \le F_0(\iota) + P$ by Theorem 3.20.6, so $\iota$ has (D) and hence (D'). For $P \le m < q$, Theorem 3.20.6 gives $\rho_P \le d \le \rho_m + m$, so $\rho_m$ has (D) with $F(\lambda) = \lambda + m$. $\square$

Research note 75 tested eight candidate corrections by exact computation on five passes of the first cycle and four passes of the second: $\rho_P$, the lexicographic pairs $(d, \rho_P)$, $(\rho_P, \delta)$ and $(\rho_P, -\delta)$, the bound $\rho_P + \delta$, the bound $d - s_P$ of note 45, the type $d - \rho_P$ and $d$. Each of them goes up on each computed pass, and research note 78 reproduced the counts with independent code. Seven of them have (D'), and for these the corollary forces the result.

**Corollary 3.20.20.** Let $p$ and $n$ be as in Theorem 3.20.18 and assume (HP). Then $\rho_1$ is an invariant on $\mathcal{G}_{3,n}$ with the properties (U) and (N$_{pt}$), and it does not have the property (D'). So the hypothesis (D') in Theorem 3.20.18 cannot be removed.

Node: SG000000A1 · Lean: none yet

*Proof.* The value $\rho_1$ is an invariant by Propositions 3.20.3 and 3.20.4, with values in $\mathbb{N} \cup \{\infty\}$. It has (U) by Lemma 3.20.16 with $m = 1$, and (N$_{pt}$) by Corollary 3.20.10. If it had (D'), Theorem 3.20.18 would give a contradiction. $\square$

The computations of notes 45, 48 and 78 find $\rho_1 = 0$ at each computed point of both cycles, which is the explicit form of the failure: $d$ is unbounded on the fibre $\rho_1 = 0$.

### What the theorem says and what it does not say

**The dimension.** The germs of (HP) have $n = 5$ for $p = 2$ and $n = 4$ for $p \ge 3$. They are hypersurfaces of dimension $5$ and $4$ in $n + 1$ variables, not threefolds. Theorem 3.20.18 says nothing about the germs with $n \le 3$. An invariant on $\mathcal{G}_{3,3}$ with (N$_{pt}$) and (D) is not excluded. So there is no conflict with the resolution of threefolds and of quasi-excellent schemes of dimension $3$ by Cossart and Piltant [CP08, CP19], and for $n = 2$ the positive results of [HP19a] and of Cossart, Jannsen and Saito [CJS20] apply.

**The invariants.** The proof uses that $\iota(x_{k+1})$ is a function of the germ at $x_{k+1}$ only. The germ includes the divisor $E$, so an invariant can use the components of $E$ through the point. But an invariant that remembers the history of a resolution, such as the year counters of the algorithms of Hironaka type or the order of creation of the components of $E$, is not a function on $\mathcal{G}_{e,n}$, and the theorem says nothing about it.

**The centres.** The property (N$_{pt}$) quantifies over all closed points of order $q$. The theorem says nothing about a rule that chooses the centres, for example the global top locus of an algorithm or a centre of positive dimension. [HP19a] remark that along the cycles larger centres are permissible and prevent the phenomenon (Remark 1.4.4). By Corollary 3.20.11, a rule that keeps $\rho_m$ from going up must act differently at the points that are unbalanced in each adapted coordinate system. This needs a law like Theorem 3.20.8 for the centres of positive dimension, which this section does not give.

**The construction.** The theorem is not about the Hasse-Schmidt construction. It excludes each germ-local invariant with (N$_{pt}$) and (D'). What remains possible is to drop one of the hypotheses: to use a rule for the centres, to use invariants that depend on the history, or to use non-increasing invariants that do not bound $d$, such as $\rho_1$, together with another mechanism. Cossart and Piltant use such a mechanism for threefolds: they reduce the problem to coverings of degree $p$ [CP08], where $e = 1$ and Sections 3.1 and 3.2 apply.

**Remark 3.20.21 (the exponents $e \ge 4$).** Let $e' \ge 3$ and let $g$ be the function of (HP). Put $\bar g = g^{p^{e' - 3}}$ and $q' = p^{e'}$. Then $z^{q'} + \bar g = (z^{p^3} + g)^{p^{e' - 3}}$. A monomial $x^{p^{e' - 3} a}$ has all its exponents divisible by $q'$ if and only if $x^a$ has all its exponents divisible by $p^3$, so the clean part of $\bar g$ is the $p^{e' - 3}$-th power of the clean part of $g$. Also $\operatorname{ord} \bar g \ge q'$ if and only if $\operatorname{ord} g \ge p^3$, and $x_1^{-q'} \pi(\bar g) = (x_1^{-p^3} \pi(g))^{p^{e' - 3}}$ for each chart and each translation. So the sequence of (HP) is a sequence of blowups of points of order $q'$ for $\bar g$, and the residual orders are $p^{e' - 3} d_k \to \infty$. Thus Theorem 3.20.18 holds for each $e \ge 3$ on the class $\mathcal{G}_{e,n}$, which contains these germs. But the hypersurfaces $z^{q'} + \bar g$ are not reduced for $e' \ge 4$. For invariants that are defined only on the reduced germs, the case $e \ge 4$ is open.

**Proposition 3.20.22.** Fix $p$, $e$ and $n$. For a germ $\gamma \in \mathcal{G}_{e,n}$ let $D^*(\gamma) \in \mathbb{N} \cup \{\infty\}$ be the supremum of the residual orders of the germs obtained from $\gamma$ by the finite sequences of blowups of closed points of order $q$ at which the order stays $q$, including the empty sequence. Then an invariant on $\mathcal{G}_{e,n}$ with (N$_{pt}$) and (D) exists if and only if $D^*$ is finite on each germ. In this case $D^*$ is such an invariant, with $F$ the identity, and $D^* \le F \circ \iota$ for each invariant $\iota$ with (N$_{pt}$) and (D) for the function $F$.

Node: SG000000A6 · Lean: none yet

*Proof.* The finite sequences of blowups from $\gamma$ depend only on the germ, and the residual order does not depend on the adapted coordinates or on the choice of $z$. So $D^*$ is an invariant, with values in the well-ordered set $\mathbb{N} \cup \{\infty\}$. Assume that $D^*$ is finite on each germ. The empty sequence gives $d \le D^*$, so (D) holds with $F$ the identity. A finite sequence from a point $x'$ of order $q$ over $x$, preceded by the blowup of $x$, is a finite sequence from $x$, so $D^*(x') \le D^*(x)$, which is (N$_{pt}$). Conversely, let $\iota$ have (N$_{pt}$) and (D) with the function $F$. Along each finite sequence from $\gamma$ the invariant $\iota$ does not go up, so the residual order of each germ of the sequence is at most $F(\iota) \le F(\iota(\gamma))$. Thus $D^*(\gamma) \le F(\iota(\gamma)) < \infty$. $\square$

For $e = 3$ and $n$ as in Theorem 3.20.18 the function $D^*$ is infinite at the start of the sequence of (HP), which is Theorem 3.20.18 for (D) again. For $e = 2$ no sequence with $d \to \infty$ is known, and by the proposition the existence of an invariant with (N$_{pt}$) and (D) is equivalent to a uniform form of Moh's bound: $d$ is bounded on the whole tree of point blowups above each germ. The weaker statement that $d$ is bounded along each infinite sequence is the analogue for (D'). The two statements do not obviously agree. The tree has infinite branching, since there are infinitely many translations over the infinite field $K$, so the lemma of König does not turn a bound on each branch into a uniform bound. The Frobenius twist of Remark 3.20.21 gives nothing for $e = 2$, because the stability claim of Moh holds for $e = 1$ [HP19a].

### Open questions

1. *The exponent $e = 2$.* Is $D^*$ of Proposition 3.20.22 finite on each germ of $\mathcal{G}_{2,n}$? Equivalently, is there an invariant with (N$_{pt}$) and (D) for $e = 2$? Example 3.20.13 and Proposition 3.20.15 show that $\rho_P$ itself is not such an invariant. A search of the project over rational point blowups for $n = 3$ found no increase of $d$ above Moh's bound, but the depth and the dimension of the search are far below those of the cycles for $e = 3$. A first test case is $p = 2$, $n = 4$, with starting equations of the shape of the cycles.
2. *Threefolds for $e = 3$.* Is Theorem 3.20.18 true for $n = 3$, or is there an invariant on $\mathcal{G}_{3,3}$ with (N$_{pt}$) and (D)? Either answer is consistent with [CP19]. The known cycles need $n \ge 4$.
3. *Reduced germs for $e \ge 4$.* Is Theorem 3.20.18 true for the reduced germs with $e \ge 4$? A positive answer needs cycles for $e \ge 4$, or a reduced perturbation of the Frobenius twist of Remark 3.20.21 that keeps $d \to \infty$.

### Exercises

1. Let $p = 2$, $q = 4$, $\Delta = \emptyset$ and $g = x^2 y^2$, the function of Remark 3.1.8. Show that $\Theta^{\le 1}(g) = 0$, that $\Theta^{\le 2}(g) = (x^2, y^2)$, and that $\rho_2 = 2$ and $d = 4$. Check the dichotomy $\rho_2 \le d \le \rho_2 + 2$ of Theorem 3.20.6.
2. Let $1 \notin \Delta$ and $P = p^{e-1} \le m < q$. Show that $\Theta^{\le m}(g + x_1^P)$ and $\Theta^{\le m}(g)$ can be different. Show that for $1 \in \Delta$ the ideal $C_{\le q}(\tau(g))$ changes under $g \mapsto g + x_1^q$.
3. Prove the formula (19.1) from the Taylor formula of Volume 1, Section 6.3.
4. In Example 3.20.13, show that the origin of the $y$-chart is the only closed point of order $4$ over the origin. Compute $\rho_1$ before and after the blowup, and compare with Corollary 3.20.10.
5. In Proposition 3.20.15 take $m = 1$ and $g = x^{q+1} y + x^{q+2}$. Compute $\Theta^{\le 1}(g)$ and $\Theta'$ at the origin of the $y$-chart, and show that $\rho'_1 = \rho_1 = 0$. Find the step of the proof of Proposition 3.20.15 that uses $m \ge 2$.
6. Let $\kappa$ be an invariant with values in $\mathbb{N}$, and let $\iota = (\kappa, \rho_P)$ with the lexicographic order. Show that $\iota$ has the property (D'). Show that if $\kappa$ takes the values $0$ and $1$ and $\rho_P$ is unbounded on the germs with $\kappa = 0$, then no monotone $F : \mathbb{N}^2 \to \mathbb{N}$ has $d \le F(\iota)$.
7. Let $e = 1$. Use Theorems 3.1.4 and 3.2.4 to show that $D^*(\gamma) \le \rho(\gamma) + 1$ for each germ, so that Proposition 3.20.22 gives an invariant with (N$_{pt}$) and (D).
8. Prove the three claims of Remark 3.20.21 on the Frobenius twist: the cleaning, the order and the commutation with the charts and the translations.
9. Let $p = 2$, $q = 4$, $\Delta = \{x\}$ and $g = x^2 y^2 + x^3$. Show that $g$ is clean with $r = 2$ and $d = 1$, that $\Theta^{\le 1}(g) = (x^3)$, and that $\Theta^{\le 2}(g) = (x^2)$. So part 1 of Theorem 3.20.6 fails for $m = 1 < P$ and holds for $m = 2 = P$.

### Notes and references

The ideals $\Theta^{\le m}$, Propositions 3.20.3 and 3.20.4, Theorem 3.20.6 and Theorem 3.20.7 are from research note 45 of the project, which research note 48 refereed. The form of Theorem 3.20.6 with $\sigma = d$, the excess and the imbalance in Theorem 3.20.8, Lemma 3.20.16, Theorem 3.20.18 and its corollaries, Examples 3.20.13 and 3.20.14 and Remark 3.20.21 are from research note 75. The referee report in research note 78 checked them, restricted Theorem 3.20.18 to the dimensions of the cycles and to the functions of the germ, replaced the hypothesis (D) by (D'), and proved Propositions 3.20.15 and 3.20.22. The cycles and the remark on larger centres are in [HP19a]. Moh's bound and the stability claim are in [Moh87], and Section 1.4 treats them. Benito and Villamayor study invariants built from differential operators in positive characteristic, and they show that their slope invariant is not upper semicontinuous in general [BenV13]. Cossart and Piltant resolve the threefolds [CP08, CP19], and Cossart, Jannsen and Saito resolve the excellent surfaces [CJS20]. None of the results of this section is in Lean.
