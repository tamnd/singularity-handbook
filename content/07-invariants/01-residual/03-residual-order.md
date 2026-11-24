---
title: Purely inseparable equations and the residual order
nodes: [SG00000013]
sources: [HP19a, Hau10, HW14, Moh87]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Purely inseparable equations and the residual order

In this section $K$ is a perfect field of characteristic $p > 0$, $e \ge 1$ and $q = p^e$. We study the hypersurfaces
$$f = z^q + F(x_1, \dots, x_n), \qquad F \in K[[x]], \quad \operatorname{ord} F \ge q,$$
in the power series ring $K[[z, x]]$. Such an $f$ is a *purely inseparable equation*. Its order is $q$. The projection to the coordinates $x$ is a bijection from its zero set onto the $x$-space, since $z^q = -F$ determines $z$. These equations are the core case of the problem in characteristic $p$ [Hau10], and the residual order is their second invariant. We follow Section 2 of [HP19a].

### Cleaning

Let $z_1 = z - g$ with $g \in K[[x]]$. Since the Frobenius is a ring homomorphism, $(z_1 + g)^q = z_1^q + g^q$, so
$$f = z_1^q + \bigl(g^q + F\bigr).$$
Thus the change of the variable $z$ changes $F$ by a $q$-th power, and the monomials of $F$ that are $q$-th powers carry no information on the singularity. A monomial $c x^\alpha$ with $c \ne 0$ is a $q$-th power in $K[[x]]$ if and only if $q$ divides each $\alpha_i$, because $K$ is perfect.

**Definition 1.3.1.** The power series $F = \sum_\alpha c_\alpha x^\alpha$ is *clean* if $c_\alpha = 0$ for each $\alpha \in q\mathbb{N}^n$. The *clean part* of $F$ is $F^{\mathrm{cl}} = \sum_{\alpha \notin q\mathbb{N}^n} c_\alpha x^\alpha$.

Lean: Singularity.IsClean, Singularity.cleanPart

**Lemma 1.3.2.** Let $F \in K[[x]]$. There is exactly one $g \in K[[x]]$ such that $g^q + F$ is clean. For this $g$, $g^q + F = F^{\mathrm{cl}}$.

Lean: Singularity.exists_add_pow_eq_cleanPart (the existence of $g$)

*Proof.* Let $g = \sum_\beta b_\beta x^\beta$. Then $g^q = \sum_\beta b_\beta^q x^{q\beta}$, so $g^q$ has its support in $q\mathbb{N}^n$. Thus $g^q + F$ is clean if and only if $b_\beta^q = -c_{q\beta}$ for each $\beta$. Since $K$ is perfect, the map $b \mapsto b^q$ is a bijection of $K$, so there is exactly one such $g$. Then $g^q + F$ and $F$ have the same coefficients outside $q\mathbb{N}^n$, and $g^q + F = F^{\mathrm{cl}}$. $\square$

The change $z_1 = z - g$ of Lemma 1.3.2 is the *cleaning* of $f$. After cleaning, $f = z_1^q + F^{\mathrm{cl}}$. Note that $\operatorname{ord} F^{\mathrm{cl}} \ge \operatorname{ord} F$, and the inequality can be strict.

### The residual order

The resolution process keeps a normal crossings divisor $E$, the union of the exceptional components of the earlier blowups. In the coordinates of this section it has the form $E = V(\prod_{i \in \Delta} x_i)$ for a subset $\Delta \subseteq \{1, \dots, n\}$.

**Definition 1.3.3.** Let $f = z^q + F$ with $F$ clean and $F \ne 0$, and let $E = V(\prod_{i \in \Delta} x_i)$. For $i \in \Delta$, let $r_i$ be the largest integer with $x_i^{r_i} \mid F$. Write
$$F = \prod_{i \in \Delta} x_i^{r_i} \cdot G.$$
The *residual order* of $f$ for $E$ is $\operatorname{ord}_E^{\mathrm{res}} f = \operatorname{ord} G$. For a general $f = z^q + F$, the residual order is the residual order after cleaning, that is, $\operatorname{ord} G$ for $F^{\mathrm{cl}}$.

Node: SG00000013 · Lean: Singularity.residualOrderAlong, Singularity.residualOrder_eq_ord_cleanPart

The power series $G$ is unique, because $K[[x]]$ is a domain. The residual order measures how far $F$ is from a monomial times a unit: it is $0$ if and only if $F^{\mathrm{cl}}$ is a monomial in the $x_i$, $i \in \Delta$, times a unit. In characteristic $0$, the analogue is the order of the residual factor of the coefficient ideal, the second component of the invariant of the proofs of Villamayor, Bierstone and Milman, and Encinas and Hauser [Hau03]. The term *residual order* is from Hironaka [HP19a, Section 2].

**Example 1.3.4.** Let $p = 2$, $q = 4$, $\Delta = \{x, y, w\}$ and
$$F = x^2 y^2 w^3 \bigl(w (x + y)^4 + x^{13}\bigr) = x^6 y^2 w^4 + x^2 y^6 w^4 + x^{15} y^2 w^3,$$
since $(x + y)^4 = x^4 + y^4$ in characteristic $2$. No exponent is in $4\mathbb{N}^3$, so $F$ is clean. The factor $G = w x^4 + w y^4 + x^{13}$ is not divisible by $x$, by $y$ or by $w$, so $r = (2, 2, 3)$ and the residual order of $z^4 + F$ is $\operatorname{ord} G = 5$. Section 1.4 blows up this example.

The definition uses the given coordinates $x$ and the given divisor $E$. Changes of the $x$ coordinates that keep $E$ can change $\operatorname{ord} G$. A resolution proof must choose the coordinates well, for example so that the order of the residual factor is maximal [HP19a, Section 1], or it must use an invariant that does not depend on the choice [HW14]. The examples of Section 1.4 compute the residual order in explicit coordinates, as [HP19a] does.

### Permissible centers and point blowups

**Definition 1.3.5.** Let $f = z^q + F$ with $F$ clean, with $E$ and $G$ as above, and let $d = \operatorname{ord} G$. An ideal $P = (z, x_i : i \in \Gamma)$ with $\Gamma \subseteq \{1, \dots, n\}$ is a *permissible center* for $f$ and $E$ if $f \in P^q$ and $G \in P^d$.

The maximal ideal $(z, x_1, \dots, x_n)$ is always a permissible center, because $\operatorname{ord} f = q$ and $\operatorname{ord} G = d$. Its blowup is a *point blowup*.

Let $\pi$ be the blowup with center $P$, and let $f'$ be the strict transform of $f$. Then $\operatorname{ord} f' \le q$ at each point over the origin. If $\operatorname{ord} f' < q$, the singularity has improved. The interesting points are those where $\operatorname{ord} f' = q$. At such a point, after a translation, the blowup is given in a chart by a map of the form
$$\pi(z) = x_j z, \qquad \pi(x_j) = x_j, \qquad \pi(x_i) = x_j (x_i + t_i) \ (i \in \Gamma \setminus \{j\}), \qquad \pi(x_l) = x_l \ (l \notin \Gamma),$$
with $j \in \Gamma$ and constants $t_i \in K$ [HP19a, Section 2]. This is the *$x_j$-chart* with the translations $x_i \mapsto x_i + t_i$.

**Lemma 1.3.6.** In this situation, $\pi(F)$ is divisible by $x_j^q$, and the strict transform of $f$ is
$$f' = z^q + F', \qquad F' = x_j^{-q} \pi(F).$$

Lean: Singularity.pointChartZ_purelyInseparable

*Proof.* The homomorphism $K[[z, x]] \to K[[x]]$ that sends $z$ to $0$ maps $f$ to $F$ and $P^q$ onto $(x_i : i \in \Gamma)^q$. Since $f \in P^q$, we have $F \in (x_i : i \in \Gamma)^q$. The map $\pi$ sends each $x_i$ with $i \in \Gamma$ to a multiple of $x_j$, so it sends $(x_i : i \in \Gamma)^q$ into $x_j^q K[[z, x]]$. Thus $\pi(F) = x_j^q F'$ with $F' \in K[[x]]$. Also $\pi(z^q) = x_j^q z^q$. So $\pi(f) = x_j^q (z^q + F')$, and the strict transform is $z^q + F'$, since this power series is not divisible by $x_j$. $\square$

The new divisor is the total transform of $E$. In the $x_j$-chart with the translations $t_i$, it is $E' = V(x_j \prod_{i \in \Delta \setminus B} x_i)$, where $B = \{j\} \cup \{ i : t_i \ne 0 \}$, because the component $x_i = 0$ with $t_i \neq 0$ does not pass through the new origin [HP19a, Section 2]. The power series $F'$ need not be clean, even when $F$ is clean. So we clean $f'$ again before we compute its residual order for $E'$.

### Notes and references

Cleaning and the residual order appear, often only implicitly, in the work of Abhyankar, Moh, Cossart and Piltant, Cutkosky, Benito and Villamayor, and Kawanoue and Matsuki [HP19a, Section 2]. We follow the definitions of [HP19a]. Hauser and Wagner study alternative invariants for purely inseparable surfaces in [HW14]. The paper [Moh87] and the survey [Hau10] give the behaviour of the residual order under one blowup, which Section 1.4 states.
