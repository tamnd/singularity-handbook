---
title: The statement (D) is the valuative form of the end case rho = 0
nodes: [SG000000BR, SG0000003E, SG0000003F]
sources: [Kunz69, Cos87, Pos24, CP08, CP09, Kuh10b, KR23, Tem13, NS14, CM17, Mat]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The statement (D) is the valuative form of the end case rho = 0

This section reports the thirty-first research result. It is from the track FP (tamnd/singularity#320), and it works on Problem 3.29.23, the statement (D) of Definition 3.29.21 for valuations with defect. This is the last open node of route V$'$ to $\mathrm{PILU}_4$, given $\mathrm{ELU}_3$, and one of the three open nodes on the critical path of the review of the road (tamnd/singularity#334). The section does not solve Problem 3.29.23. It shows that (D) is not a new problem: on a fixed model, (D) is the statement $\rho = 0$ of Volume 7, Definition 3.1.3, so Problem 3.29.23 is the valuative form of Cossart's problem in dimension 4 (Conjecture 2.5.3), with arbitrary models and no conditions on the centers. It then proves (D) for each instance where the valuation is discrete of rank one on $L$, with or without defect. So the open cases of Problem 3.29.23 have a value group that is not $\mathbb{Z}$.

The results come from research note 97 and from its referee report, research note 99. The referee report checked each proof of note 97, found one gap and one wrong step, settled one question of note 97, and added the result on valuations that are discrete of rank one. This section follows the referee report where the two notes differ (see the Status).

We keep the notation of Section 3.29 from Definition 3.29.13 on. So $k$ is algebraically closed of characteristic $p$, $(A, a, \nu)$ is an instance of $\mathrm{PILU}_4$, $L$ is the fraction field of $A$, $b = a^{1/p}$, $\nu$ is zero dimensional, and $\Delta = \{\nu(b - c) : c \in L\}$. The instance has defect if and only if $\Delta$ has no maximum (Lemma 3.29.18). A *model* is a regular local ring $A_1 \subset L$, essentially of finite type over $k$, with fraction field $L$, that contains $A$ and is dominated by $\nu$. Its residue field is $k$. For a regular system of parameters $x = (x_1, \dots, x_n)$ of a model, $\partial_1, \dots, \partial_n$ are the derivations of $A_1$ over $k$ dual to $dx_1, \dots, dx_n$, and $\theta_i = x_i \partial_i$. For $E \subseteq \{1, \dots, n\}$ we put, as in Volume 7, Definition 3.1.1 (node SG0000003E),
$$\Theta_{x,E}(g) = \bigl(\theta_i g \ (i \in E),\ \partial_j g \ (j \notin E)\bigr), \qquad \Theta^{\log}_x(g) = \Theta_{x,\{1,\dots,n\}}(g).$$
We call $E$ the *boundary*. We drop $x$ from the notation when the regular system of parameters is clear. Since each derivation kills $p$-th powers, $\Theta_{x,E}(g + h^p) = \Theta_{x,E}(g)$ (Volume 7, Lemma 3.1.2).

### Motivation

Section 3.29 reduced $\mathrm{PILU}_4$, given $\mathrm{ELU}_3$, to the statement (D): there are $c \in L$ and a model $A_1 \ni c$ on which $a - c^p$ is a unit times a monomial $x^\alpha$ with $\alpha \not\equiv 0$. Without defect, $\mathrm{ELU}_3$ gives (D) (Proposition 3.29.22). With defect, the loop of Section 3.29 improves the approximation $c$ of $b$ step by step, and it stops only if some step gives an exponent that is not divisible by $p$. Section 3.29 asked whether $\mathrm{ELU}_3$ makes it stop.

The loop mixes two choices: the approximation $c$ and the model $A_1$. The first result of this section separates them. The test of (D) on a fixed model does not see $c$, because it is a statement about the derivatives of $a$, and $a$ and $a - c^p$ have the same derivatives. Precisely, (D) holds on $A_1$ if and only if the log-Jacobian ideal of $a$ is a principal monomial ideal for some boundary. This is the end case $\rho = 0$ of Volume 7, Section 3.5. So the hard part of (D) is the same as the hard part of Conjecture 2.5.3: to make $\rho$ drop. The difference is that (D) allows each model along the valuation, not only blowups with the conditions (H1) and (H2).

The second part of the section studies what $\mathrm{ELU}_3$ gives toward $\rho = 0$. It gives a principal ideal $\Theta_{E_1}(a) A_2$ on a new model $A_2$, but the ideal $\Theta_{E_2}(a)$ that is computed on $A_2$ can be smaller. The factor between the two is the determinant of a log-Jacobian matrix, and Proposition 3.31.11 computes it: up to monomials, it is the ordinary Jacobian determinant of $A_1 \to A_2$, whose zero set is the exceptional locus. The third part proves (D) when $\nu|_L$ is discrete of rank one, by a direct computation along the formal arc of $\nu$.

A reader needs Section 3.29 from Definition 3.29.13 on, and Volume 7, Sections 3.1 and 3.5.

### The p-basis

**Lemma 3.31.1 ($p$-basis).** Let $A_1$ be a model with a regular system of parameters $x = (x_1, \dots, x_n)$, and let $A_1^p = \{g^p : g \in A_1\}$.

1. $A_1 = \bigoplus_{\varepsilon \in [0, p-1]^n} A_1^p\, x^\varepsilon$.
2. Let $\gamma \in \mathbb{Z}_{\ge 0}^n$. An element $g = \sum_\varepsilon g_\varepsilon^p x^\varepsilon$ lies in $x^\gamma A_1$ if and only if each summand $g_\varepsilon^p x^\varepsilon$ lies in $x^\gamma A_1$.
3. $\theta_i(g_\varepsilon^p x^\varepsilon) = \varepsilon_i\, g_\varepsilon^p x^\varepsilon$ and $\partial_j(g_\varepsilon^p x^\varepsilon) = \varepsilon_j\, g_\varepsilon^p x^{\varepsilon - e_j}$.

Lean: none yet

*Proof.* (1) $A_1$ is essentially of finite type over the perfect field $k$, so it is finite over $A_1^p$. It is regular, so it is flat over $A_1^p$ by Kunz's theorem [Kunz69], and so it is free. The residue field is $k = k^p$, so $A_1 / \mathfrak{m}_{A_1^p} A_1 = A_1 / (x_1^p, \dots, x_n^p)$, and this ring has the basis $(x^\varepsilon)_{\varepsilon \in [0,p-1]^n}$ over $k$. By Nakayama the $x^\varepsilon$ are a basis of $A_1$ over $A_1^p$. One can also pass to $\widehat{A_1} = k[[x]]$, where the decomposition is clear, and descend by faithful flatness.

(2) Write $\gamma = pq + r$ with $0 \le r_i < p$. For $h \in A_1$ and $\varepsilon \in [0, p-1]^n$, the product $x^\gamma h^p x^\varepsilon$ is $(x^q h x^s)^p x^{\varepsilon'}$, where $\varepsilon'_i \equiv r_i + \varepsilon_i \bmod p$, $0 \le \varepsilon'_i < p$, and $s_i = 1$ if $r_i + \varepsilon_i \ge p$ and $s_i = 0$ otherwise. There is a carry $s_i = 1$ exactly when $\varepsilon'_i < r_i$. So
$$x^\gamma A_1 = \bigoplus_{\varepsilon'} \Bigl(x^q \prod_{i : \varepsilon'_i < r_i} x_i\Bigr)^p A_1^p\, x^{\varepsilon'},$$
which is a graded submodule for the decomposition of (1). This is (2).

(3) The derivations kill $g_\varepsilon^p$, and the formulas follow from the Leibniz rule. $\square$

For $g \in A_1$ we write $g_0$ for the component with $\varepsilon = 0$ and $g^\natural = g - g_0^p = \sum_{\varepsilon \ne 0} g_\varepsilon^p x^\varepsilon$. By (3), $g^\natural = 0$ if and only if all the derivations $\partial_j$ kill $g$, if and only if $g \in A_1^p$. If $a \notin L^p$, then $a^\natural \ne 0$ and $\Theta_{x,E}(a) \ne 0$ for each $E$.

### The equivalence

**Theorem 3.31.2 ((D) and the log-Jacobian ideal).** Let $A_1$ be a model with a regular system of parameters $x$, and let $a \in A_1$ with $a \notin L^p$.

1. There is $c \in A_1$ with $a - c^p = u x^\alpha$, $u \in A_1^\times$ and $\alpha \not\equiv 0$, if and only if $\Theta^{\log}_x(a)$ is a principal monomial ideal $(x^\gamma)$. Then $\alpha = \gamma$, and one can take $c = a_0$.
2. Let $E \subseteq \{1, \dots, n\}$, and assume that $\Theta_{x,E}(a) = (x^\gamma)$ with $\operatorname{supp} \gamma \subseteq E$. Then there are $c \in A_1$ and a regular system of parameters $y$ of $A_1$ with $y_i = x_i$ for $i \in E$, such that $a - c^p = u y^\alpha$ with $u \in A_1^\times$ and $\alpha \not\equiv 0$. Conversely, if $a - c^p = u x^\alpha$ with $c \in A_1$ and $\alpha \not\equiv 0$, then $\Theta_{x,E}(a) = (x^\alpha)$ for each $E \supseteq \operatorname{supp} \alpha$.
3. The instance $(A, a, \nu)$ satisfies (D) if and only if some model has a regular system of parameters $x$ and a boundary $E$ with $\Theta_{x,E}(a) = (x^\gamma)$ and $\operatorname{supp} \gamma \subseteq E$, and if and only if some model has a regular system of parameters $x$ with $\Theta^{\log}_x(a)$ principal monomial.

Lean: none yet

*Proof.* First the converse in (2). Let $a - c^p = u x^\alpha$ with $\alpha \not\equiv 0$, and let $E \supseteq \operatorname{supp} \alpha$. Then $\Theta_{x,E}(a) = \Theta_{x,E}(u x^\alpha)$. Its generators are $x^\alpha(\alpha_i u + \theta_i u)$ for $i \in E$ and $x^\alpha \partial_j u$ for $j \notin E$, because $\alpha_j = 0$ for $j \notin E$. Choose $i$ with $p \nmid \alpha_i$. Then $i \in E$, and $\alpha_i u + \theta_i u$ is a unit, since $\theta_i u \in \mathfrak{m}$. So $\Theta_{x,E}(a) = (x^\alpha)$.

Now assume that $\Theta_{x,E}(a) = (x^\gamma)$ with $\operatorname{supp} \gamma \subseteq E$. Write $a = \sum_\varepsilon a_\varepsilon^p x^\varepsilon$ as in Lemma 3.31.1, and let $\varepsilon \ne 0$. If $\varepsilon_i \ne 0$ for some $i \in E$, then $\theta_i a \in x^\gamma A_1$, and Lemma 3.31.1(2) and (3) show that $\varepsilon_i a_\varepsilon^p x^\varepsilon \in x^\gamma A_1$, so $a_\varepsilon^p x^\varepsilon \in x^\gamma A_1$. Otherwise $\varepsilon_j \ne 0$ for some $j \notin E$. Then $\partial_j a \in x^\gamma A_1$ gives $a_\varepsilon^p x^{\varepsilon - e_j} \in x^\gamma A_1$, so again $a_\varepsilon^p x^\varepsilon \in x^\gamma A_1$. Hence $a^\natural = g x^\gamma$ for some $g \in A_1$. Since $\gamma_j = 0$ for $j \notin E$, the Leibniz rule gives
$$\Theta_{x,E}(a) = \Theta_{x,E}(a^\natural) = x^\gamma J, \qquad J = \bigl(\gamma_i g + \theta_i g \ (i \in E),\ \partial_j g \ (j \notin E)\bigr).$$
As $A_1$ is a domain and $\Theta_{x,E}(a) = (x^\gamma)$, we get $J = (1)$.

If $\gamma \equiv 0$, then $g \in \mathfrak{m}$. Indeed, write $\gamma = p\beta$ and $g = \sum_\varepsilon g_\varepsilon^p x^\varepsilon$. Then $g x^{p\beta} = \sum_\varepsilon (x^\beta g_\varepsilon)^p x^\varepsilon$ is the decomposition of $a^\natural$, and the component of $a^\natural$ with $\varepsilon = 0$ is $0$. So $g_0 = 0$, and $g = g^\natural$ is a sum of terms $g_\varepsilon^p x^\varepsilon$ with $\varepsilon \ne 0$, which lie in $\mathfrak{m}$. So two cases remain.

*Case $g$ a unit.* Then $\gamma \not\equiv 0$, and $a - a_0^p = g x^\gamma$. Take $c = a_0$ and $y = x$.

*Case $g \in \mathfrak{m}$.* Then $\gamma_i g + \theta_i g \in \mathfrak{m}$ for each $i \in E$, so $J = (1)$ forces $\partial_j g \notin \mathfrak{m}$ for some $j \notin E$. So the linear part of $g$ contains $x_j$ with a nonzero coefficient, and $y_j = g$ together with $(x_l)_{l \ne j}$ is a regular system of parameters. Then $a - a_0^p = y_j x^\gamma$. The exponent has the entry $1$ at $j$, because $\gamma_j = 0$, so it is not divisible by $p$. Take $c = a_0$.

This proves (2). For (1), let $E = \{1, \dots, n\}$. Then $J = (\gamma_i g + \theta_i g)_i$, and $J = (1)$ forces $g \notin \mathfrak{m}$. So only the first case occurs: $g$ is a unit, $\gamma \not\equiv 0$, $c = a_0$, and no parameter changes. The converse in (1) is the converse in (2) with $E = \{1, \dots, n\}$. For (3), a model that contains $c$ satisfies $\nu(c) \ge 0$ and $A_1 \supseteq A[c]$, so (2) gives (D) in the sense of Definition 3.29.21. Conversely, if (D) holds with $a - c^p = u x^\alpha$ on $A_1$, then $c \in A_1$, and the converse in (2) gives $\Theta_{x,E}(a) = (x^\alpha)$ for $E = \operatorname{supp} \alpha$ and for $E = \{1, \dots, n\}$. $\square$

Theorem 3.31.2 is the form of Volume 7, Proposition 3.5.1 and Theorem 3.5.3, in a regular local ring essentially of finite type over $k$ instead of $K[[x]]$, with an explicit $c$. The case "$g$ a unit and $\gamma \equiv 0$" of note 97 cannot occur, by the argument above. In part (2) the new parameter $y_j$ is a free parameter, that is, $j \notin E$. So in general the end form of (D) changes one free parameter, and this is the type 1 of Volume 7, Theorem 3.5.3.

### The residue field must be perfect

The proof uses that the residue field $k$ of $A_1$ is perfect twice: in Lemma 3.31.1(1), and in the fact that $p$-th roots of residues exist. The next two examples show that the theorem fails at a point whose residue field is not perfect. Such points occur in each global argument, as the generic points of the strata of the boundary. So (D) at the closed points does not spread to the generic points of the strata.

**Example 3.31.3 (no $p$-th root of the residue).** Let $A = k[t, x]_{(x)}$. This is a discrete valuation ring with the residue field $K = k(t)$ and the parameter $x$. Let $a = t + x^{p+1}$. With the parameter $x$ alone, $\Theta^{\log}(a) = (x \partial_x a) = (x^{p+1})$ is principal, and $p + 1 \not\equiv 0$. But $a - c^p$ is a unit for each $c \in A$, because its residue $t - \bar c^{\,p}$ is not $0$ in $K$. So part (1) of Theorem 3.31.2 fails. If one adds the derivation $\partial_t$, since $\{t, x\}$ and not $\{x\}$ is a $p$-basis of $A$, then $\Theta(a) = (1)$, and the case $\gamma = 0$ would need a $p$-th root of $t$ in $K$.

**Example 3.31.4 (a free parameter is missing).** Let $A = k[x, t]_{(x)}$ again, $E = \{x\}$ and $a = x^p(t + x)$. Then $x \partial_x a = x^{p+1}$ and $\partial_t a = x^p$, so $\Theta_E(a) = (x^p)$, principal with support in $E$. But for each $c \in A$ the $x$-adic order of $a - c^p$ is $0$ or $p$. Indeed, in $K[[x]]$ write $c = \sum_i c_i x^i$. If $c_0 \ne 0$, the order is $0$. If $c_0 = 0$, the coefficient of $x^p$ in $a - c^p$ is $t - c_1^p \ne 0$, because $t$ is not a $p$-th power in $K$. In dimension 1 there is no free parameter, so the conclusion of part (2) fails. At the closed point of $k[x, t]_{(x, t)}$ the theorem applies: $y = t + x$ is a free parameter and $a = x^p y$.

### Consequences

**Corollary 3.31.5 ((D) is the end case $\rho = 0$).** Let $A_1$ be a model with a regular system of parameters $x$ and a boundary $E$, and let $F = -a$, cleaned in $\widehat{A_1} = k[[x]]$ as in Volume 7, Definition 1.3.3. Then $\rho(F) = 0$ for the divisor $\prod_{i \in E} x_i$ if and only if $\Theta_{x,E}(a) = (x^\gamma)$ with $\operatorname{supp} \gamma \subseteq E$. So the instance satisfies (D) if and only if some model has a regular system of parameters and a boundary with $\rho = 0$. In particular, each statement that gives $\rho = 0$ at the center of $\nu|_L$ on some model, for some boundary, gives (D). The strong form of $\mathrm{C4}^{\rm val}$ of Section 2.5, which asks for $\rho = 0$ at each multiplicity, is such a statement.

Lean: none yet

*Proof.* $\Theta(-a) = \Theta(a)$, and $\Theta$ does not change under cleaning (Volume 7, Lemma 3.1.2). An ideal $I$ of $A_1$ with $I \widehat{A_1} = x^\gamma \widehat{A_1}$ is $x^\gamma A_1$, by faithful flatness, so we can compute in $k[[x]]$. Write the cleaned $F = x^r G$ as in Volume 7, Definition 1.3.3, with $\operatorname{supp} r \subseteq E$. Then $\Theta(F) = x^r \widetilde\Theta(G)$, and $\rho(F) = 0$ means $\widetilde\Theta(G) = (1)$, so $\Theta(F) = (x^r)$. Conversely, if $\Theta(F) = (x^\gamma)$ with $\operatorname{supp} \gamma \subseteq E$, then $x^\gamma$ is the largest monomial in the variables of $E$ that divides each element of $\Theta(F)$, so $\gamma = r$ by Volume 7, Theorem 3.1.4(1), and $\widetilde\Theta(G) = (1)$. The rest is Theorem 3.31.2(3). $\square$

The boundary must be chosen on the model. For a fixed boundary, (D) does not give $\rho = 0$. For example, let $E = \emptyset$ and $a = x_1^{p+1}$. Then (D) holds with $c = 0$, but $\Theta_\emptyset(a) = (x_1^p)$, and $\rho = p$ for this boundary. So Problem 3.29.23 is the form of Conjecture 2.5.3 along one valuation, with three changes: the models are arbitrary, there are no conditions (H1) and (H2) on the centers, and there is no condition on the multiplicity of $z^p - a$.

**Corollary 3.31.6 (the approximation does not matter on a fixed model).** Let $A_1$ be a model with a regular system of parameters $x$ and a boundary $E$, and let $c \in A_1$. Then $\Theta_{x,E}(a - c^p) = \Theta_{x,E}(a)$. So the condition of Theorem 3.31.2(2) on $(A_1, x, E)$ does not depend on $c$, and when it holds the theorem gives a suitable $c$, namely $a_0$.

Lean: none yet

*Proof.* Volume 7, Lemma 3.1.2. The second sentence is Theorem 3.31.2(2). $\square$

So the test for (D) on a given model does not need the approximation $c$. This does not mean that the choice of $c$ in the loop of Section 3.29 is irrelevant: the choice of $c$ decides which element $\mathrm{ELU}_3$ is applied to, and so it can steer which models the loop reaches. What the corollary says is that the loop is a search over models, and that $c$ enters only through this steering.

### Changing the equation

Let $a' \in A$ with $L(a'^{1/p}) = L(b)$. Then $a' \in L(b)^p = L^p(a)$, so $a' = \sum_{i < p} \lambda_i^p a^i$ with $\lambda_i \in L$. For each derivation $D$ of $L$ over $k$,
$$D(a') = h\, D(a), \qquad h = \sum_{i < p} i \lambda_i^p a^{i-1} \in L.$$
Here $h \ne 0$, because $a' \notin L^p$, and an element of $L$ is in $L^p$ if and only if all derivations kill it. So $\Theta_{x,E}(a') = h\, \Theta_{x,E}(a)$ as submodules of $L$, on each model that contains $a'$.

**Proposition 3.31.7 (a change of the equation, the proved form).** Let $a' \in A$ be as above. Assume that on a model $A_1$ with a regular system of parameters $x$ and a boundary $E$ we have $\Theta_{x,E}(a) = (x^\gamma)$ with $\operatorname{supp} \gamma \subseteq E$, and $h = w x^\delta$ with $w \in A_1^\times$, $\delta \in \mathbb{Z}^n$ and $\operatorname{supp} \delta \subseteq E$. Then $(A, a', \nu)$ satisfies (D).

Lean: none yet

*Proof.* $\Theta_{x,E}(a') = h\,\Theta_{x,E}(a) = (x^{\gamma + \delta})$. This ideal lies in $A_1$, and $A_1$ is factorial with the $x_i$ as distinct primes, so $\gamma + \delta \ge 0$. Its support lies in $E$. Theorem 3.31.2(2) and (3) give (D) for $a'$. $\square$

The special case $a' = a - c^p$ with $c \in A$ needs no proposition: then $h = 1$, and this is Corollary 3.31.6. Note 97 stated a stronger form, Proposition 97.4: given $\mathrm{ELU}_3$, (D) holds for $a$ if and only if it holds for $a'$. Its proof is not complete, and the statement is open.

**Problem 3.31.8.** Assume $\mathrm{ELU}_3$. If $(A, a, \nu)$ satisfies (D), does $(A, a', \nu)$ satisfy (D) for each $a' \in A$ with $L(a'^{1/p}) = L(b)$? Then (D) would be a property of the extension $L(b) \mid L$ and of $\nu$ only.

Status: open. The proof in note 97 makes $h$ monomial by $\mathrm{ELU}_3$ and claims that $\Theta_{E_2}(a)$ stays principal monomial on the new model. There are two gaps. First, on the model that $\mathrm{ELU}_3$ gives, Lemma 3.31.9(1) below gives only the inclusions $\det(T)\,\Theta_{E_1}(a) A_2 \subseteq \Theta_{E_2}(a) \subseteq \Theta_{E_1}(a) A_2$, and Example 3.31.12 shows that $\Theta_{E_2}$ can stop being principal. Second, $h$ becomes a unit times a Laurent monomial $x'^\delta$, and $\delta$ can have negative entries, or entries at coordinates outside $E_2$. Then the support of $\gamma + \delta$ need not lie in $E_2$, and Theorem 3.31.2(2) does not apply.

### The transformation law

Let $A_1 \subseteq A_2$ be models with regular systems of parameters $x$, $x'$ and boundaries $E_1$, $E_2$. Assume that each $x_k$ with $k \in E_1$ is a unit times a monomial in the $x'_l$ with $l \in E_2$. Let $\Omega_i$ be the free module with the basis $dx_k / x_k$ ($k \in E_i$) and $dx_j$ ($j \notin E_i$). Let $T$ be the matrix over $A_2$ of the natural map $\Omega_1 \otimes A_2 \to \Omega_2$, with the rows indexed by the basis of $\Omega_1$. The hypothesis on $E_1$ and $E_2$ makes the entries of $T$ lie in $A_2$. We write $\Theta_1 = \Theta_{x,E_1}$ and $\Theta_2 = \Theta_{x',E_2}$.

**Lemma 3.31.9 (transformation law).**

1. For each $f \in A_1$, $\det(T)\, \Theta_1(f) A_2 \subseteq \Theta_2(f) \subseteq \Theta_1(f) A_2$.
2. If $x_k = u_k x'^{M_k}$ with $u_k \in A_2^\times$ for all $k$, and $E_1 = E_2 = \{1, \dots, n\}$, then $T = M + (\theta'_l u_k / u_k)_{k,l}$, so $\det T \equiv \det M \bmod \mathfrak{m}_2$. If $p \nmid \det M$, then $T$ is invertible and $\Theta^{\log}$ is preserved. For the charts of Lemma 3.29.15 with $\alpha = 0$, where $x_k = y^{N_k}$ exactly with $\det N = \pm 1$, at each point of the chart, with $E_1 = \{1, \dots, n\}$ and $E_2$ the set of the $l$ with $y_l \in \mathfrak{m}_2$, we have $\det T = \pm 1 / \prod_{l \notin E_2} y_l$, a unit.
3. Let $A_2$ be the local ring of a point of the exceptional divisor of the blowup of the center $(x_i : i \in I)$, in the chart of $x_{i_0}$ with $i_0 \in I$, so that $x_{i_0} = x'_{i_0}$ and $x_i = x'_{i_0}(x'_i + \lambda_i)$ with $\lambda_i \in k$ for $i \in I \setminus \{i_0\}$, and $x_l = x'_l$ for $l \notin I$. Put $E_2 = \{i_0\} \cup (E_1 \setminus I) \cup \{i \in I \cap E_1 : \lambda_i = 0\}$. Then $\det T$ is a unit times $x_{i_0}'^{\,|I \setminus E_1|}$. In particular, if the center is a stratum of $E_1$, that is, $I \subseteq E_1$, then $\det T$ is a unit, also at the points with some $\lambda_i \ne 0$, and $\Theta_2(f) = \Theta_1(f) A_2$.

Lean: none yet

*Proof.* (1) The coefficients of $df$ in the basis of $\Omega_1$ generate $\Theta_1(f)$, and its coefficients in the basis of $\Omega_2$ generate $\Theta_2(f)$. The second vector is the first vector times $T$. This gives the second inclusion. Multiplication with the adjugate matrix of $T$ gives the first one.

(2) $d \log x_k = \sum_l M_{kl}\, d \log x'_l + d \log u_k$, and $d \log u_k = \sum_l (\theta'_l u_k / u_k)\, d\log x'_l$ with $\theta'_l u_k \in \mathfrak{m}_2$. For the toric charts, Lemma 3.29.15 with $\alpha = 0$ gives a ring $A_2$ that is essentially étale over $k[y_1, \dots, y_n]$ localized at the center, so the $y_l$ with $y_l \in \mathfrak{m}_2$ and the $y_l - \lambda_l$ with $\lambda_l \ne 0$ the residue of $y_l$ form a regular system of parameters $x'$. Then $d\log x_k = \sum_l N_{kl}\, dy_l / y_l$. For $l \in E_2$ the basis vector of $\Omega_2$ is $dy_l / y_l$, with the coefficient $N_{kl}$. For $l \notin E_2$ it is $dy_l$, with the coefficient $N_{kl} / y_l$. So $\det T = \det N / \prod_{l \notin E_2} y_l$.

(3) For $k \notin I$ the basis vector does not change. Let $i \in I \setminus \{i_0\}$. If $i \in E_1$, then $d\log x_i = d \log x'_{i_0} + dx'_i / (x'_i + \lambda_i)$. If $\lambda_i = 0$, the new basis vector is $d\log x'_i$ with the coefficient $1$. If $\lambda_i \ne 0$, then $i \notin E_2$, the new basis vector is $dx'_i$, and its coefficient $1/(x'_i + \lambda_i)$ is a unit. If $i \notin E_1$, then $i \notin E_2$, and $dx_i = x'_{i_0}\bigl((x'_i + \lambda_i)\, d\log x'_{i_0} + dx'_i\bigr)$, which gives the diagonal entry $x'_{i_0}$. Finally, $d\log x_{i_0} = d\log x'_{i_0}$ if $i_0 \in E_1$, and $dx_{i_0} = x'_{i_0}\, d\log x'_{i_0}$ otherwise. So all entries of $T$ off the diagonal are in the column of $i_0$. After moving $i_0$ to the first place, $T$ is triangular, and $\det T$ is the product of the diagonal entries, which is a unit times $x_{i_0}'^{\,|I \setminus E_1|}$. The last claim follows from (1). $\square$

The condition $I \subseteq E_1$ in (3) says that the center is a stratum of $E_1$. A center that only lies inside a stratum is not enough. For example, let $I = \{1, 2, 3\}$ and $E_1 = \{1, 2\}$. The center lies in the stratum $x_1 = x_2 = 0$, but $\det T$ is a unit times $x'_{i_0}$. Also, a center that is a stratum keeps $\Theta_2 = \Theta_1 A_2$, but it can still lower $\rho$, because the pullback of a monomial ideal that is not principal can become principal. The next example shows this, and it also shows that $\Theta^{\log}_x$ depends on the regular system of parameters.

### Worked example

**Example 3.31.10 (a blowup in a stratum gives (D)).** Let $p = 2$, $A_1 = k[x_1, x_2, x_3, x_4]_{(x)}$, $E_1 = \{1, 2, 3, 4\}$ and
$$a = x_1 x_2 + x_1^4 x_3^3.$$
In characteristic 2 we have $\theta_1 a = x_1 x_2$, $\theta_2 a = x_1 x_2$, $\theta_3 a = x_1^4 x_3^3$ and $\theta_4 a = 0$. So $\Theta^{\log}(a) = (x_1 x_2, x_1^4 x_3^3)$, which is not principal, and $\rho > 0$ on $A_1$ for this boundary.

Blow up the stratum $x_1 = x_2 = 0$, so $I = \{1, 2\} \subseteq E_1$, and take the chart of $x_1$ at the point with $x_2 = x_1(1 + t)$, that is, $\lambda_2 = 1$. The new regular system of parameters is $(x_1, t, x_3, x_4)$, and Lemma 3.31.9(3) gives $E_2 = \{1, 3, 4\}$ and $\det T$ a unit. So
$$\Theta_{E_2}(a) = \Theta^{\log}(a) A_2 = (x_1^2 (1 + t), x_1^4 x_3^3) = (x_1^2).$$
We check this directly. On $A_2$, $a = x_1^2 + x_1^2 t + x_1^4 x_3^3$, so $\theta_1 a = 0$, $\partial_t a = x_1^2$, $\theta_3 a = x_1^4 x_3^3$ and $\theta_4 a = 0$. The ideal is principal with support in $E_2$, so $\rho = 0$. The proof of Theorem 3.31.2 gives the following. The $p$-basis decomposition is $a = x_1^2 + x_1^2 t + (x_1^2 x_3)^2 x_3$, so $a_0 = x_1$ and $a^\natural = x_1^2 (t + x_1^2 x_3^3)$. Here $g = t + x_1^2 x_3^3$ lies in $\mathfrak{m}$, and $\partial_t g = 1$ with $t \notin E_2$. So $y = t + x_1^2 x_3^3$ is a free parameter, and
$$a - x_1^2 = x_1^2\, y,$$
with the exponent $(2, 1, 0, 0)$ in the regular system of parameters $(x_1, y, x_3, x_4)$. So (D) holds on $A_2$ with $c = x_1$.

Now compute $\Theta^{\log}$ in the regular system of parameters $(x_1, t, x_3, x_4)$, that is, with the boundary $E'_2 = \{1, 2, 3, 4\}$. Then $\theta_t a = x_1^2 t$, and $\Theta^{\log}(a) = (x_1^2 t, x_1^4 x_3^3)$, which is not principal. The reason is the factor $\det T = t/(1+t)$ for this boundary, by Proposition 3.31.11 below. So $\Theta^{\log}_x$ depends on the regular system of parameters, and the coordinate $t$ of a point that is not torus fixed is a bad choice for the boundary. In the regular system of parameters $(x_1, y, x_3, x_4)$, part (1) of Theorem 3.31.2 applies, with $\Theta^{\log}(a) = (x_1^2 y)$. The program `lab97/check_sandwich.py` found 179 cases of this kind.

### The determinant of the log-Jacobian matrix

Note 97 asked when $\det T$ is a unit times a monomial (its question Q97.2). The answer is a formula for $\det T$.

**Proposition 3.31.11 (the determinant).** Let $A_1 \subseteq A_2$, $x$, $x'$, $E_1$, $E_2$ and $T$ be as before Lemma 3.31.9. Let $J_{\rm ord} = \det(\partial x_k / \partial x'_l) \in A_2$ be the ordinary Jacobian determinant. Then
$$\det T = J_{\rm ord} \cdot \frac{\prod_{l \in E_2} x'_l}{\prod_{k \in E_1} x_k}.$$
The zero set $V(J_{\rm ord})$ is the exceptional locus of $\operatorname{Spec} A_2 \to \operatorname{Spec} A_1$, that is, the set of the primes $Q$ of $A_2$ such that $(A_2)_Q$ is not the local ring $(A_1)_{Q \cap A_1}$. So $\det T$ is a unit times a monomial in $x'$ if and only if each component of the exceptional locus through the closed point of $A_2$ is a coordinate hyperplane $V(x'_l)$.

Lean: none yet

*Proof.* Let $\mathrm{Jac} = (\partial x_k / \partial x'_l)$, $D_1 = \operatorname{diag}(x_k \text{ for } k \in E_1, 1 \text{ otherwise})$ and $D_2 = \operatorname{diag}(x'_l \text{ for } l \in E_2, 1 \text{ otherwise})$. Then $dx_k = \sum_l (\partial x_k / \partial x'_l)\, dx'_l$ and $dx'_l = x'_l\, d\log x'_l$ for $l \in E_2$ give $T = D_1^{-1}\, \mathrm{Jac}\, D_2$, and the formula follows.

$\Omega_{A_2/A_1}$ is the cokernel of the map $\Omega_{A_1/k} \otimes A_2 \to \Omega_{A_2/k}$ of free modules with the matrix $\mathrm{Jac}$, so $J_{\rm ord}$ generates its zeroth Fitting ideal. Also $J_{\rm ord} \ne 0$, because the two rings have the same fraction field, so both $dx$ and $dx'$ are bases of $\Omega_{L/k}$. If $J_{\rm ord} \notin Q$, then $\Omega_{A_2/A_1}$ vanishes at $Q$, so $A_1 \to A_2$ is unramified at $Q$, and in particular quasi finite at $Q$. The map is birational and $A_1$ is normal, so by Zariski's main theorem $(A_2)_Q = (A_1)_{Q \cap A_1}$ [Mat]. Conversely, if $(A_2)_Q$ is a local ring of $A_1$, then $\Omega_{A_2/A_1}$ vanishes at $Q$, and its Fitting ideal is the unit ideal at $Q$. So $V(J_{\rm ord})$ is the exceptional locus, and it is a divisor.

By hypothesis $\prod_{k \in E_1} x_k$ is a unit times a monomial in $x'$. So $\det T$ is a unit times a monomial if and only if $J_{\rm ord}$ is. Since $A_2$ is factorial, this holds if and only if each prime factor of $J_{\rm ord}$ is associate to some $x'_l$, that is, if and only if each component of $V(J_{\rm ord})$ through the closed point is some $V(x'_l)$. $\square$

The condition "$p \mid \det M$" of note 97 is not the right condition. For example, let $x = x'$ and $y = x'^p (1 + y')$, with $E_1 = \{x, y\}$ and $E_2 = \{x'\}$. The matrix of exponents has $\det M = 0$. But $J_{\rm ord} = x'^p$, and the formula gives $\det T = 1/(1 + y')$, a unit. In Lemma 3.31.9(2) the boundary $E_2$ is the full set, and there the two conditions agree.

**Example 3.31.12 (a model where $\Theta_2$ is not principal).** Let $A_1 = k[x, y, z, w]_{(x,y,z,w)}$ and $A_2 = k[s, t, u, v]_{(s,t,u,v)}$ with
$$x = s, \quad y = s(1 + t), \quad z = s(1 + u g), \quad w = s(1 + v), \qquad g = t^2 + s^3.$$
The map is birational, with $t = y/x - 1$, $v = w/x - 1$ and $u = (z/x - 1)/g$. The Jacobian matrix is triangular, and $J_{\rm ord} = 1 \cdot s \cdot sg \cdot s = s^3 g$ in each characteristic. With $E_1 = \{x, y, z, w\}$ and $E_2 = \{s\}$, each $x_k$ is a unit times $s$, and Proposition 3.31.11 gives $\det T = s^3 g \cdot s / s^4 = g$ up to a unit. The element $g$ is irreducible and lies in $\mathfrak{m}^2$, so it is not a unit times a monomial in any regular system of parameters of $A_2$. Now let $p = 2$ and $f = xz$. Then $\Theta^{\log}(f) = (xz)$, and $f = s^2(1 + u g)$ is a unit times a monomial on $A_2$, so $\Theta_1(f) A_2 = (s^2)$ is principal. But $\theta_s f = 3 s^5 u = s^5 u$, $\partial_t f = 0$, $\partial_u f = s^2 g$ and $\partial_v f = 0$, so
$$\Theta_2(f) = s^2\,(s^3 u,\ t^2 + s^3),$$
which is not principal. The program `lab99/q972.py` checks the example for $p = 2, 3, 5$. So $A_2$ has the properties that the proof of Proposition 97.6 of note 97 takes from $\mathrm{ELU}_3$: $f$ and all the $x_k$ are units times monomials. But $\det T$ is not a unit times a monomial, and $\Theta_2(f)$ is not principal.

### What a log form of ELU_3 gives

Example 3.31.12 shows that $\mathrm{ELU}_3$ as stated in Definition 3.29.13(3) does not control $\det T$. The following form does.

**Definition 3.31.13 ($\mathrm{ELU}_3^{\log}$).** $\mathrm{ELU}_3^{\log}$ says: for each regular local ring $A$ of dimension 4, essentially of finite type over $k$, with fraction field $L$, each valuation $\mu$ of $L/k$ that dominates $A$, and each $f \in A \setminus \{0\}$, there are a regular local ring $A_1 \supseteq A$, essentially of finite type, with fraction field $L$ and dominated by $\mu$, and a regular system of parameters $x'$ of $A_1$, such that $f$ and the Jacobian determinant $J_{\rm ord}$ of $A \to A_1$ are both units times monomials in $x'$.

The Jacobian determinant is taken with respect to a regular system of parameters of $A$ and to $x'$. Another choice changes it by a unit.

**Lemma 3.31.14 ($\mathrm{Emb}_3^{\rm bd}$ gives $\mathrm{ELU}_3^{\log}$).** Assume $\mathrm{Emb}_3^{\rm bd}$ for regular 4-folds over $k$. Then $\mathrm{ELU}_3^{\log}$ holds.

Lean: none yet

*Proof.* Follow the proof of Lemma 3.29.28 with the boundary $E = \emptyset$. It gives $\pi \colon Y_r \to Y$, a composite of blowups in regular centers, with $X_r + E^{(r)}$ snc, where $X$ is the reduced divisor of $f$ and $E^{(r)}$ is the union of the exceptional divisors. Let $y_r$ be the center of $\mu$ and $A_1 = \mathcal{O}_{Y_r, y_r}$. Choose a regular system of parameters $x'$ of $A_1$ such that each component of $X_r + E^{(r)}$ through $y_r$ is some $V(x'_l)$. The divisor of $f$ is supported on $X_r \cup E^{(r)}$. The morphism $\pi$ is an isomorphism outside the preimages of the centers, and these preimages lie in $E^{(r)}$. So by Proposition 3.31.11 the divisor of $J_{\rm ord}$ is supported on $E^{(r)}$. As $A_1$ is factorial, $f$ and $J_{\rm ord}$ are units times monomials in $x'$. $\square$

**Proposition 3.31.15 (what $\mathrm{ELU}_3^{\log}$ gives).** Assume $\mathrm{ELU}_3^{\log}$. Let $A_1$ be a model with a regular system of parameters $x$ and a boundary $E_1$, and let $a \in A_1 \setminus L^p$. Then there is a model $A_2 \supseteq A_1$ with a regular system of parameters $x'$ and a boundary $E_2$ as before Lemma 3.31.9, such that $\Theta_{E_1}(a) A_2 = (x'^\gamma)$ with $\operatorname{supp} \gamma \subseteq E_2$, and $\det T = \text{unit} \cdot x'^\mu$ with $\operatorname{supp} \mu \subseteq E_2$. So
$$\Theta_{E_2}(a) = x'^\gamma J \quad \text{with} \quad x'^\mu \in J.$$

Lean: none yet

*Proof.* Let $g_1, \dots, g_r$ be the nonzero generators of $\Theta_{E_1}(a)$. There is at least one, since $a \notin L^p$. Apply $\mathrm{ELU}_3^{\log}$ to $f = g_1 \cdots g_r \cdot x_1 \cdots x_n$ and $\mu = \nu|_L$. This gives a model $A'_2$ with a regular system of parameters $y$ such that $f$ and the Jacobian determinant $J'$ of $A_1 \to A'_2$ are units times monomials in $y$. As $A'_2$ is factorial, each $g_i$ and each $x_k$ is a unit times a monomial in $y$. Let $S$ be the set of the differences of the exponents of the $g_i$, and apply Lemma 3.29.15 with $\alpha = 0$ and this $S$ to $A'_2$. It gives a model $A_2$ with $y_k = w^{N_k}$ for a toric chart $w$ with $\det N = \pm 1$. Let $E_2$ be the set of the $l$ with $w_l \in \mathfrak{m}_{A_2}$, and let $x'$ be the regular system of parameters of Lemma 3.31.9(2), so that $x'_l = w_l$ for $l \in E_2$ and the $w_l$ with $l \notin E_2$ are units.

Each monomial in $y$ is a unit times a monomial in the $x'_l$ with $l \in E_2$. So the $x_k$ and the $g_i$ are units times $E_2$-monomials. For $s \in S$, Lemma 3.29.15 gives $y^s \in A_2$ or $y^{-s} \in A_2$, so the monomials of the $g_i$ are totally ordered by divisibility, and $\Theta_{E_1}(a) A_2 = (g_1, \dots, g_r) A_2 = (x'^\gamma)$ with $\operatorname{supp} \gamma \subseteq E_2$. The Jacobian determinant of $A'_2 \to A_2$ is $\pm \prod_k y_k / \prod_l w_l$, by the computation of Lemma 3.31.9(2), and it is a unit times an $E_2$-monomial. The Jacobian determinant is multiplicative under composition, by the chain rule. So the Jacobian determinant $J_{\rm ord}$ of $A_1 \to A_2$ is a unit times an $E_2$-monomial. By Proposition 3.31.11, $\det T$ is a unit times a Laurent monomial in the $x'_l$ with $l \in E_2$. It lies in $A_2$, and $A_2$ is factorial, so it is a unit times $x'^\mu$ with $\mu \ge 0$ and $\operatorname{supp} \mu \subseteq E_2$. Lemma 3.31.9(1) gives $x'^{\gamma + \mu} A_2 \subseteq \Theta_{E_2}(a) \subseteq x'^\gamma A_2$, which is the last claim. $\square$

By Theorem 3.31.2, (D) holds on $A_2$ if $J = (1)$. In general $J$ is a proper ideal that contains $x'^\mu$.

**Remark 3.31.16 (the obstruction).** Given $\mathrm{ELU}_3^{\log}$, each model leads to a model with $\Theta_{E_2}(a) = x'^\gamma J$ and $x'^\mu \in J$. One can apply $\mathrm{ELU}_3^{\log}$ again to the generators of $J$, but on the new model the residual ideal satisfies only the same inclusions, with a new factor $\det T$. Nothing in $\mathrm{ELU}_3^{\log}$ makes this process stop. This is the problem of making $\rho$ drop, Conjecture 2.5.3, with the extra freedom that the models are arbitrary. With bare $\mathrm{ELU}_3$ the factor $\det T$ is not a monomial, and it is $J_{\rm ord}$ up to monomials, by Proposition 3.31.11. The known difficulty is also here: by Lemma 3.31.9(3), blowups in centers that are strata of the boundary keep $\Theta$, and centers that are not strata give a factor $x_{i_0}'^{\,|I \setminus E|}$.

**Problem 3.31.17.** Does $\mathrm{ELU}_3$ imply $\mathrm{ELU}_3^{\log}$?

Status: open. This is a question of the known type "embedded or not embedded uniformization", and it is not special to (D). In Example 3.31.12 one more toric chart in $(s, t)$ makes $g$ a monomial, because $g$ is nondegenerate for its Newton polygon. In general a toric chart turns $J_{\rm ord}$ only into a monomial times its strict transform, and for a branch with two characteristic pairs one chart is not enough [S]. Applying $\mathrm{ELU}_3$ to $J_{\rm ord}$ gives a new model with a new Jacobian determinant, and the determinants multiply, so the problem repeats. By Lemma 3.31.14 the question does not arise if $\mathrm{ELU}_3$ comes from $\mathrm{Emb}_3^{\rm bd}$, which is the way the road map obtains it.

### PILU_4 and (D)

**Proposition 3.31.18 (a regular $A[b]$ gives (D)).** If $A[b] = A[z]/(z^p - a)$ is regular at its closed point, then (D) holds on $A$ itself.

Lean: none yet

*Proof.* Let $\tilde c \in A$ be a lift of the $p$-th root of the residue of $a$. By the formula after Definition 3.29.13, the multiplicity of $A[b]$ at its closed point is $\min(p, \operatorname{ord}_A(a - \tilde c^{\,p}))$. It is $1$, so $a - \tilde c^{\,p}$ has order 1 and is a regular parameter of $A$. Extend it to a regular system of parameters $x$ with $x_1 = a - \tilde c^{\,p}$. Then $a - \tilde c^{\,p} = x^{e_1}$ and $e_1 \not\equiv 0$. $\square$

So $\mathrm{PILU}_4$ and (D) agree when the solution is $A[b]$ itself. In general a solution $A'$ of $\mathrm{PILU}_4$ is a regular local ring of $L(b)$, and (D) asks for a model of $L$. The natural candidate $A' \cap L$ is the ring of constants of a $p$-closed derivation of $A'$, and such rings are in general singular; the Zariski surfaces are the basic example [S]. A model $A_1 \supseteq A' \cap L$ exists by Lemma 3.29.17, given $\mathrm{ELU}_3$, but then $A_1[b]$ need not contain $A'$, and the regularity of $A'$ does not control the log-Jacobian ideal of $a$ on $A_1$. So no proof is known that $\mathrm{PILU}_4$ for an instance implies (D) for it. This is the second question of Problem 3.29.23, and it stays open.

### Valuations that are discrete of rank one

**Proposition 3.31.19 ((D) for discrete valuations of rank one).** Let $(A, a, \nu)$ be an instance such that $\nu|_L$ is discrete of rank one, that is, its value group is $\mathbb{Z}$. Then (D) holds on a model obtained from $A$ by finitely many blowups of the center of $\nu$. This holds with or without defect, and it does not use $\mathrm{ELU}_3$.

Lean: none yet

*Proof.* The residue field of $\nu|_L$ is $k$, because $\nu$ is zero dimensional. So the completion of the valuation ring of $\nu|_L$ is $k[[t]]$, and $\nu|_L$ is the order in $t$. For each model $A_i$ let $\psi_i \colon \widehat{A_i} \to k[[t]]$ be the induced map. It is injective on $A_i$, because $A_i$ lies in the valuation ring. Its image $B_i$ is a complete local domain. It contains $\psi_i(x)$ for some $x \in \mathfrak{m}_{A_i} \setminus \{0\}$, an element of finite positive order $e$, so $k[[t]]$ is finite over $k[[\psi_i(x)]] \subseteq B_i$. The field $\operatorname{Frac} B_i$ is finite over the complete field $k((\psi_i(x)))$, so it is complete, and it contains an element of order 1, the image of an element of $L$ of value 1. So $\operatorname{Frac} B_i = k((t))$, and $k[[t]]$ is the normalization of $B_i$. So $B_i$ is a formal branch.

*Step 1 (the branch becomes regular).* Let $A_0 = A, A_1, \dots$ be the local rings of the successive blowups of the center of $\nu$. The rings $B_i$ increase, and $\dim_k k[[t]]/B_i$ is finite and drops while $B_i \ne k[[t]]$. So after finitely many blowups $B_i = k[[t]]$ [S]. Fix such an $i$. Then $\psi_i(\mathfrak{m}_{A_i}) = (t)$, so some regular parameter $x_1$ of $A_i$ has $\psi_i(x_1) = t \cdot \text{unit}$. We change the parameter $t$ of $k[[t]]$ so that $\psi_i(x_1) = t$. Complete $x_1$ to a regular system of parameters $x_1, \dots, x_4$ of $A_i$, and let $\psi_j(t) = \psi_i(x_j) \in t k[[t]]$. Then $X'_j = x_j - \psi_j(x_1)$, for $j = 2, 3, 4$, together with $x_1$ are formal coordinates of $\widehat{A_i}$, and $\ker \psi_i = (X'_2, X'_3, X'_4)$.

*Step 2 ($m$ more blowups).* Since $\nu(x_j) \ge 1 = \nu(x_1)$ for all $j$, the center of $\nu$ on each further blowup lies in the chart of $x_1$. After $m$ more blowups we get a model $A_{i+m}$ with a regular system of parameters $x_1, x^{(m)}_2, x^{(m)}_3, x^{(m)}_4$, and $X'_j = x_1^m X''_j$, where $X''_j = x^{(m)}_j - \varphi_j(x_1)$ for some $\varphi_j \in k[[x_1]]$. So $(x_1, X'')$ are formal coordinates of $\widehat{A_{i+m}}$. Take $E = \{1\}$. The change from $(x_1, x^{(m)})$ to $(x_1, X'')$ has $dX''_j = dx^{(m)}_j - x_1 \varphi'_j(x_1)\, d\log x_1$, so its matrix $T$ is triangular with $1$ on the diagonal. By the argument of Lemma 3.31.9(1) both coordinate systems give the same ideal $\Theta_E(a) \widehat{A_{i+m}}$. By faithful flatness, it suffices to show that this ideal is $(x_1^N)$ for some $N$.

*Step 3 (the computation).* In $\widehat{A_i} = k[[x_1, X']]$ write
$$a = G(x_1) + \sum_j h_j(x_1)\, X'_j + R, \qquad R \in (X')^2,$$
with $G, h_j \in k[[x_1]]$. Here $h_j = \psi_i(\partial a / \partial X'_j)$, and $\partial / \partial X'_j$ with $x_1$ and the other $X'$ fixed is the derivation $\partial_j$ of $A_i$. So $h_j = \psi_i(\partial_j a)$, and $h_j \ne 0$ if $\partial_j a \ne 0$, since $\psi_i$ is injective on $A_i$.

*Case 1: $\partial_j a \ne 0$ for some $j$.* Let $v = \min_j \operatorname{ord} h_j$ and $w = \operatorname{ord}(x_1 G')$, possibly infinite, and take $m > v$. In the coordinates $(x_1, X'')$ we have $a = G + \sum_j h_j x_1^m X''_j + R$ with $R \in x_1^{2m}(X'')^2$. So $\partial a / \partial X''_j = x_1^m (h_j + O(x_1^m))$. For the $j$ with $\operatorname{ord} h_j = v$ this is $x_1^{m+v}$ times a unit, and the others lie in $(x_1^{m+v})$. Also $\theta_1 a = x_1 G' + \sum_j (x_1 h'_j + m h_j)\, x_1^m X''_j + \theta_1 R$, and the last two terms lie in $(x_1^{m+v})$. So $\Theta_E(a) = (x_1^{\min(w, m+v)})$.

*Case 2: $\partial_j a = 0$ for all $j \ne 1$.* Then $\theta_1 a \ne 0$, since $a \notin L^p$. A blowup in the chart of $x_1$ changes $\theta_1$ by a combination of the $\partial_j$, and multiplies each $\partial_j$ by $x_1$, so on each $A_{i+m}$ we have $\Theta_E(a) = (\theta_1 a)$ for the same element $\theta_1 a$ of $A_i$. Let $N = \nu(\theta_1 a)$. In $\widehat{A_i}$, $\theta_1 a = H(x_1) + (\text{element of } (X'))$ with $\operatorname{ord} H = N$. After $m > N$ blowups the second term lies in $(x_1^m)$, so $\theta_1 a = x_1^N \cdot \text{unit}$.

In both cases $\Theta_E(a)$ is principal monomial with support in $E = \{1\}$ on $A_{i+m}$, and Theorem 3.31.2(2) and (3) give (D). $\square$

With defect we have $e = 1$, so $\nu(a - c^p) = p\,\nu(b - c) \in p\mathbb{Z}$ for each $c \in L$. In the end form $a - c^p = u y^\alpha$ of Theorem 3.31.2(2), with $y_1 = x_1$ of value 1, the case "$g$ a unit" would give $a - c^p = u x_1^\gamma$ with $\gamma = \nu(a - c^p) \in p\mathbb{Z}$, which is excluded. So with defect the end form always uses a free parameter: $a - c^p = y_j x_1^\gamma$ with $\nu(y_j) + \gamma \equiv 0 \bmod p$. The computations below show this.

So all instances of Problem 3.29.23 with $\nu|_L$ discrete of rank one are solved, and the hard instances have a value group that is not $\mathbb{Z}$: of rank at least two, of rational rank at least two, or a subgroup of $\mathbb{Q}$ that is not discrete, such as $\mathbb{Z}[1/p]$. These are also the classical sources of defect. Example 3.29.24 is of this easy kind, and so is the whole class of the instances with value group $\mathbb{Z}$, for a reason that does not depend on whether $b$ lies in the completion of $L$.

### Computations

**Proposition 3.31.20 (checks by computation).** The following are exact computations [C]. The programs of note 97 are in `lab97/`, and the programs of note 99, which share no code with them, are in `lab99/`. All use fixed seeds and plain Python.

1. Theorem 3.31.2(1). `lab97/check_thmA.py` compares "$\Theta^{\log}(a)$ is principal monomial" with "$a^\natural$ is a unit times $x^\gamma$ with $\gamma \not\equiv 0$" on 36000 random elements of $\mathbb{F}_p[x_1, \dots, x_n]$ localized at the origin, with $p \in \{2, 3, 5\}$ and $n \in \{2, 3, 4\}$. There are no mismatches, with 21206 positive and 14794 negative cases. This test is close to a restatement of Lemma 3.31.1, and the next one tests the content of the theorem.
2. Theorem 3.31.2(2). `lab99/check_thm2b.py` (seed 991) takes random $a$ and random $E$, half of them of the form $h^p + x^\gamma g$ with $\operatorname{supp} \gamma \subseteq E$, and builds $c$ and $y$ as in the proof when $\Theta_E(a) = (x^\gamma)$ with $\operatorname{supp} \gamma \subseteq E$. It checks the identity $a - c^p = u y^\alpha$, the condition that $y$ is a regular system of parameters, and $\alpha \not\equiv 0$. There are 4014 cases with $g$ a unit, 1904 cases with $g \in \mathfrak{m}$, and no failure. In all 1615 cases with $E$ the full set only the unit case occurs, as part (1) says. The converse was checked on 2986 elements $c^p + u x^\alpha$, with no failure, and $\Theta(a - c^p) = \Theta(a)$ held in all of them.
3. Lemma 3.31.9(3). `lab97/check_law.py` takes 6000 random blowups of $\mathbb{F}_p[x_1, \dots, x_4]_{(x)}$ with $p \in \{2, 3\}$ and random $E_1$, center, chart and point. When $I \subseteq E_1$ and $\Theta_{E_1}(f) A_2$ is principal monomial, $\Theta_{E_2}(f)$ is the same ideal in 880 of 880 cases. When $I \not\subseteq E_1$, the generator changes in 1016 of 1808 cases. `lab99/check_law99.py` (seed 992) checks $\det T = \text{unit} \cdot x_{i_0}'^{\,|I \setminus E_1|}$ on 2490 random blowups by the formula of Proposition 3.31.11, with no failure. It finds the same ideal in 211 of 211 cases with $I \subseteq E_1$, and a different ideal in 408 of 663 cases with $I \not\subseteq E_1$.
4. Example 3.31.12 and the example after Proposition 3.31.11, by `lab99/q972.py`, for $p = 2, 3, 5$.
5. Explicit defect valuations. Let $a = x y^p + z^p w$ on $L = k(x, y, z, w)$. Choose $Y, Z, R \in \mathbb{F}_p[[t]]$ with prescribed initial terms and random further coefficients (seed 993), and put $\varphi(x) = t$, $\varphi(y) = Y$, $\varphi(z) = Z$ and $\varphi(w) = W = (R^p - t Y^p)/Z^p$. Then $\varphi(a) = R^p$, and $\nu = \operatorname{ord}_t \circ \varphi$ extends to $L(b)$ by $b \mapsto R$. If the tails of $Y$, $Z$ and $R$ are algebraically independent over $k(t)$, then $\varphi$ is injective on $L$, and the extension is immediate with $\Delta$ unbounded, so it has defect. Only finite jets enter the computation. `lab99/arc99.py` blows up the center of $\nu$ in the chart of the coordinate of least value, keeps the boundary as in Lemma 3.31.9(3), and computes $\Theta_E(a)$, $\rho$ and, when $\rho = 0$, the $c$ and $y$ of the proof. The results are in the table below.

Lean: none yet

| Example | $p$ | data | $\rho$ along the models | (D) reached at | end form |
|---|---|---|---|---|---|
| A | 2 | $\operatorname{ord} Y = 1$, $\operatorname{ord} Z = 1$, $\operatorname{ord} R = 2$ | 2, 0 | $m = 1$ | $a - c^2 = x^3 y_w$, $\nu(a - c^2) = 4$ |
| B | 2 | $\operatorname{ord} Y = 3$, $\operatorname{ord} Z = 3$, $\operatorname{ord} R = 4$ | 2, 2, 2, 2, 1, 0 | $m = 5$ | $a - c^2 = x^{11} y_w$, $\nu = 14$ |
| C | 3 | $\operatorname{ord} Y = 1$, $\operatorname{ord} Z = 1$, $\operatorname{ord} R = 2$ | 3, 0 | $m = 1$ | $a - c^3 = x^4 y_w$, $\nu = 6$ |
| D | 2 | singular start $\varphi(x) = t^2$, $\operatorname{ord} Y = 3$, $\operatorname{ord} Z = 2$ | 2, 0 | $m = 1$ | $a - c^2 = \text{unit} \cdot x^3$, $\nu = 6$ |
| E | 2 | $a = x y^2 + z^2 w + x y z^2$ | 2, 0 | $m = 1$ | $a - c^2 = x^3 y_w$, $\nu = 6$ |

In example D the arc is singular at the start and $\nu(x) = 2$, so $\nu(x^3) = 6 \in 2\mathbb{Z}$, and the unit case occurs without a free parameter. In all other examples the end form uses the free parameter, as the remark after Proposition 3.31.19 says. In example B the bound of the proof of Proposition 3.31.19 is $m > v = 6$, but the computation reaches (D) at $m = 5$, so the bound is not sharp. In each example $\nu(a - c^p)$ is divisible by $p$. At each final model Theorem 3.31.2(2) applies for several boundaries $E'$, all of which contain $x$, and on the earlier models for none. These experiments do not test the open case: by Proposition 3.31.19 no experiment with value group $\mathbb{Z}$ can. A real test needs a valuation with value group $\mathbb{Z}[1/p]$, for example with $y$ mapped to a Hahn series with the exponents $1 - 1/p^n$ and generic coefficients, or a valuation of rational rank at least two. Then the charts are Perron transforms, and the program must follow toric charts. This is not done.

### Kuhlmann's classification and key polynomials

Kuhlmann divides the Artin-Schreier defect extensions into dependent and independent ones [Kuh10b]. For a purely inseparable extension of degree $p$, the work of Kuhlmann and Rzepka [KR23] suggests the dichotomy "$b$ lies in the completion $\widehat{L}$ of $(L, \nu|_L)$ or not": a field is an independent defect field if and only if each immediate purely inseparable extension of degree $p$ lies in the completion, and a purely inseparable defect extension that is not in the completion gives dependent Artin-Schreier defect extensions. These statements of the sources are not checked against the text here [U]. The reductions below do not depend on them. If $\nu$ has rank one, then $b \in \widehat{L}$ if and only if $\Delta$ is unbounded in $\mathbb{R}$, by the definition of the completion.

The dichotomy does not decide (D) by any argument known here. In the class with $b \in \widehat{L}$, for each $N$ there is $c$ with $\nu(a - c^p) > N$. But (D) is a property of $\Theta(a)$ on models, and $\Theta(a) = \Theta(a - c^p)$ does not see $c$ (Corollary 3.31.6). A change of $c$ does not change the extension $L(b) \mid L$, so it cannot move an instance from one class to the other. The passage of Kuhlmann from purely inseparable to Artin-Schreier extensions changes the extension to a separable one, so it leaves the setting of $\mathrm{PILU}_4$.

Key polynomials [NS14] describe $\nu$ on $L[z]$ relative to $\nu|_L$. For our extension they produce the approximations $c$ and the set $\Delta$. By Corollary 3.31.6 the approximations do not decide (D) on a model. What (D) needs is a statement about the models of $L$, that is, about the position of $\nu|_L$ relative to the derivatives of $a$. In other words, Theorem 3.31.2 says that (D) holds if and only if, on some model, $da$ is a monomial times a log differential form that does not vanish at the closed point. This is a form of local uniformization of the codimension one foliation $\ker(da)$, and key polynomials of the extension $L(b) \mid L$ do not carry this information.

### Dimension 3 and the multiplicity

Lemma 3.31.1 and Theorem 3.31.2 hold in each dimension. In dimension 3 Cossart's theorem [Cos87], in the form of Section 2.5 and of Posva [Pos24], brings $\rho$ to $0$ by blowups on the locus where $z^p + g$ has multiplicity $p$. So, granted this theorem, (D) holds in dimension 3 for each valuation whose center stays in the locus of multiplicity $p$, with or without defect. The defect plays no separate role there. In dimension 4 no rule of this kind is known (Conjecture 2.5.3), and Volume 7, Sections 3.7 to 3.19, show runs where $\rho$ does not drop for the natural rules. The parts of the work of Cossart and Piltant [CP08, CP09] that would show which step fails in dimension 4 were not read for this section [U].

At multiplicity $m < p$ a generic projection gives a separable extension of degree $m$, which has no defect. This suggests the separable theory without defect of Cutkosky and Mourtada [CM17], but by Example 3.29.27 the condition on the multiplicity is lost after a few blowups. This direction is not pursued here.

### The open statement

**Problem 3.31.21 ((D) for value groups other than $\mathbb{Z}$).** Let $(A, a, \nu)$ be an instance with defect, and assume that $\nu|_L$ is not discrete of rank one, that is, its value group has rank at least two, or rational rank at least two, or is a subgroup of $\mathbb{Q}$ that is not discrete, such as $\mathbb{Z}[1/p]$. Is there a model with a regular system of parameters $x$ and a boundary $E$ such that $\Theta_{x,E}(a) = (x^\gamma)$ with $\operatorname{supp} \gamma \subseteq E$?

Status: open. By Theorem 3.31.2 and Proposition 3.31.19 it is equivalent to (D) for the instances with defect, and so to the first question of Problem 3.29.23. A positive answer gives $\mathrm{PILU}_4$ for these instances (Proposition 3.29.22), and so, with Theorem 3.29.19, $\mathrm{PILU}_4$ for each instance, given $\mathrm{ELU}_3$, and (O7). By Proposition 3.31.15, given $\mathrm{ELU}_3^{\log}$, it reduces to the following: the residual ideal $J = \Theta_{E_2}(a) : x'^\gamma$, which contains an exceptional monomial, becomes $(1)$ on some model. No counterexample and no proof is known.

### What is open

1. Problem 3.31.21, equivalently (D) for the instances with defect whose value group on $L$ is not $\mathbb{Z}$, the first question of Problem 3.29.23.
2. The second question of Problem 3.29.23: does $\mathrm{PILU}_4$ for an instance imply (D) for it? Proposition 3.31.18 settles only the case where $A[b]$ is regular.
3. Problem 3.31.8: the independence of (D) of the equation, given $\mathrm{ELU}_3$. Proposition 3.31.7 is the proved form.
4. Problem 3.31.17: does $\mathrm{ELU}_3$ imply $\mathrm{ELU}_3^{\log}$? It holds if $\mathrm{ELU}_3$ comes from $\mathrm{Emb}_3^{\rm bd}$ (Lemma 3.31.14).
5. A computation along a defect valuation with value group $\mathbb{Z}[1/p]$ or of rational rank two, with Perron charts. This is the first experiment that can test Problem 3.31.21.
6. The step of Cossart and Piltant [CP09] in dimension 3 that fails in dimension 4. This needs a reading of the source [U].
7. A global form: by Examples 3.31.3 and 3.31.4, (D) at closed points does not give the end form at the generic points of strata, so a global argument must treat points with imperfect residue fields separately.

### Exercises

1. Prove Lemma 3.31.1(2) for $p = 2$, $n = 1$ and $\gamma = 3$ by hand: show that $x^3 A_1 = x^4 A_1^p \oplus x^2 A_1^p\, x$.
2. Let $p = 3$ and $a = x_1^2 x_2 + x_1^3 x_2^3 x_3$ in $k[x_1, x_2, x_3]_{(x)}$. Compute $\Theta^{\log}(a)$, decide whether it is principal, and find $c$ with $a - c^3 = u x^\alpha$ if it is.
3. In Theorem 3.31.2(2), let $E = \{1\}$ and $a = x_1^p (x_2 + x_1)$ in $k[x_1, x_2]_{(x)}$. Find $c$ and the free parameter $y_2$, and compare with Example 3.31.4.
4. Show that $\Theta_\emptyset(x_1^{p+1}) = (x_1^p)$, so that $\rho = p$ for the boundary $\emptyset$, and find a boundary for which $\rho = 0$.
5. In Lemma 3.31.9(3), let $n = 3$, $I = \{1, 2, 3\}$, $E_1 = \{1, 2\}$ and $i_0 = 1$. Write down $T$ at the point $\lambda_2 = 0$, $\lambda_3 = 1$, and check that $\det T$ is a unit times $x'_1$.
6. Compute $J_{\rm ord}$ for the blowup of a point of $\mathbb{A}^4$ in the chart of $x_1$, and check the formula of Proposition 3.31.11 against Lemma 3.31.9(3).
7. In Example 3.31.12, find the toric chart in $(s, t)$ that makes $g = t^2 + s^3$ a unit times a monomial at the center of a valuation with $\nu(s) = 2$ and $\nu(t) = 3$, and compute $\Theta_2(f)$ there.
8. In the proof of Proposition 3.31.19, Case 1, let $a = x_1 + x_1^2 X'_2 + (X'_2)^p$. Compute $v$, $w$ and the least $m$ for which the proof gives $\Theta_E(a)$ principal.

### Status

The results come from research note 97 and from its referee report, research note 99. Lemma 3.31.1, Theorem 3.31.2, Corollaries 3.31.5 and 3.31.6, Proposition 3.31.7, Lemma 3.31.9, Propositions 3.31.11, 3.31.15, 3.31.18 and 3.31.19, and Lemma 3.31.14 are proved here. They use cited results: Kunz's theorem in Lemma 3.31.1, Zariski's main theorem in Proposition 3.31.11, Lemma 3.29.15 in Proposition 3.31.15, and the resolution of plane branches by point blowups in Proposition 3.31.19. The computations of Proposition 3.31.20 were run for notes 97 and 99, and the referee ran the programs of note 97 again and got the same counts. This section applies the twelve fixes of the referee report. (1) Proposition 97.4 of note 97 is not proved: Proposition 3.31.7 is the proved form, and the general form is Problem 3.31.8. (2) The proof of Proposition 97.6 of note 97 factors $T$ in a wrong way when $E_2$ is not the full set: Proposition 3.31.15 states it under $\mathrm{ELU}_3^{\log}$, with the formula of Proposition 3.31.11, and Example 3.31.12 shows that the given proof fails with bare $\mathrm{ELU}_3$. (3) The factor in the inclusions is a monomial only in that setting, and in general it is $J_{\rm ord}$ up to monomials (Remark 3.31.16). (4) Corollary 3.31.5 says that the boundary is chosen on the model. (5) Corollary 3.31.6 drops the claim of note 97 that each improvement of $c$ is wasted work. (6) Lemma 3.31.9(3) needs a center that is a stratum, not a center inside a stratum. (7) Lemma 3.31.9(2) covers the toric charts at points that are not torus fixed, centers that are strata keep $\Theta$ but can lower $\rho$, and Example 3.31.10 says that $\Theta^{\log}$ depends on the regular system of parameters. (8) The claim on dimension 3 is restricted to valuations whose center stays in the locus of multiplicity $p$. (9) The statements of Kuhlmann and Rzepka are marked as not checked. (10) Examples 3.31.3 and 3.31.4 show that the residue field must be perfect. (11) The test of Theorem 3.31.2(2) builds $c$ and $y$ as in the proof. (12) Proposition 3.31.19 removes the instances with value group $\mathbb{Z}$, and Problem 3.31.21 is restated for the other value groups. The referee also answered the question Q97.2 of note 97 by Proposition 3.31.11. Problems 3.31.8, 3.31.17 and 3.31.21 are open. The map has nodes for the log-Jacobian ideal, for $\rho$ and for $\mathrm{PILU}_4$, which this section uses, and no nodes yet for its new statements. None of the statements has a Lean proof. An outside expert has not yet read the result.

### Notes and references

The results are in research notes 97 and 99, which continue notes 03, 77, 82 and 96 and Section 3.29. The log-Jacobian ideal and $\rho$ are those of Volume 7, Chapter 3, which follows Cossart [Cos87] and Posva [Pos24]. We list the items that this section uses.

- [Kunz69] E. Kunz, Characterizations of regular local rings of characteristic $p$, Amer. J. Math. 91 (1969), 772-784. Used for Lemma 3.31.1(1).
- [Mat] H. Matsumura, Commutative ring theory. Zariski's main theorem and the facts on flatness and differentials.
- [Cos87] V. Cossart, the thesis with the theorem on a base of dimension 3, and [Pos24] Q. Posva, its modern account. Used for the remark on dimension 3, in the form of Section 2.5.
- [CP08, CP09] V. Cossart and O. Piltant, Resolution of singularities of threefolds in positive characteristic I and II, J. Algebra 320 (2008), 1051-1082, and 321 (2009), 1836-1976. Only the abstracts were read for note 97 [U]. Temkin [Tem13] summarizes the coverings $t^p + g^{p-1} t + f = 0$ that they treat.
- [Kuh10b] F.-V. Kuhlmann, A classification of Artin-Schreier defect extensions and characterizations of defectless fields, Illinois J. Math. 54 (2010), 397-448, arXiv 1003.5639. The definition of dependent and independent defect [U for the statements used here].
- [KR23] F.-V. Kuhlmann and A. Rzepka, The valuation theory of deeply ramified fields and its connection with defect extensions, arXiv 1811.04396 [U for the statements used here].
- [NS14] J. Novacoski and M. Spivakovsky, key polynomials. The finer results on limit key polynomials that note 97 quotes are not checked [U].
