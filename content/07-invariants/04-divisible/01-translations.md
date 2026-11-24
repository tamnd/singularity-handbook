---
title: Translations and the rigid layer
nodes: [SG0000003J]
sources: [Hir64, Hir67, Cos87, CP08]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Translations and the rigid layer

Let $m = p^e m_0$ with $e \ge 1$ and $p \nmid m_0$, and let
$$f = z^m + a_1 z^{m-1} + \dots + a_{m-1} z + a_m \in R[z].$$
We put $a_0 = 1$. For $c \in R$ we write $f(z + c) = \sum_{i=0}^{m} a_i' z^{m-i}$. The question of this section is: which coefficients can a translation change?

### The Frobenius form of a translation

**Lemma 4.1.1.** For each $c \in R$,
$$(z + c)^m = \bigl(z^{p^e} + c^{p^e}\bigr)^{m_0}.$$
So the coefficient of $z^k$ in $(z + c)^m$ is $0$ unless $p^e \mid k$.

Node: SG0000003J · Lean: `Singularity.X_add_C_pow_pow_mul`, `Singularity.cast_choose_pow_mul_eq_zero`

*Proof.* The ring $R[z]$ has characteristic $p$, so the map $u \mapsto u^{p^e}$ is a ring homomorphism of $R[z]$. Thus $(z + c)^{p^e} = z^{p^e} + c^{p^e}$. Raise both sides to the power $m_0$. The binomial theorem gives
$$\bigl(z^{p^e} + c^{p^e}\bigr)^{m_0} = \sum_{k=0}^{m_0} \binom{m_0}{k} c^{p^e k} z^{p^e (m_0 - k)},$$
and each exponent of $z$ is a multiple of $p^e$. $\square$

Lemma 4.1.1 replaces the theorem of Lucas on binomial coefficients modulo $p$. The theorem of Lucas gives the same conclusion: $\binom{m}{k} \equiv 0 \pmod p$ when $p^e \nmid k$. The proof above needs only the Frobenius.

**Lemma 4.1.2.** For each $i$ with $0 \le i \le m$,
$$a_i' = \sum_{j=0}^{i} \binom{m-j}{i-j} a_j c^{i-j}.$$

*Proof.* We have $f(z + c) = \sum_j a_j (z + c)^{m-j}$. By the binomial theorem, the coefficient of $z^{m-i}$ in $(z + c)^{m-j}$ is $\binom{m-j}{i-j} c^{i-j}$ for $j \le i$, and it is $0$ for $j > i$. $\square$

Node: SG0000003J · Lean: `Singularity.coeff_taylor_natDegree_sub`

In Lean the statements of this section have weaker hypotheses than in the text. No statement needs $p \nmid m_0$ or $e \ge 1$, and Lemma 4.1.2 and Theorem 4.1.3 do not need $f$ to be monic. The ring $R$ can be any commutative semiring of exponential characteristic $p$.

### The rigid layer

**Theorem 4.1.3.** Let $0 < i < p^e$. Then
$$a_i' = a_i + \sum_{0 < j < i} \binom{m-j}{i-j} a_j c^{i-j}.$$
In particular $a_1' = a_1$ for each $c \in R$. If $a_1 = \dots = a_{i-1} = 0$, then $a_i' = a_i$ for each $c \in R$.

Node: SG0000003J · Lean: `Singularity.coeff_taylor_sub_of_lt_pow`, `Singularity.coeff_taylor_natDegree_sub_one`, `Singularity.coeff_taylor_sub_of_lt_pow_of_eq_zero`

*Proof.* In Lemma 4.1.2, the term with $j = i$ is $a_i$. The term with $j = 0$ is $\binom{m}{i} c^i$, the coefficient of $z^{m-i}$ in $(z + c)^m$. Since $p^e \mid m$ and $0 < i < p^e$, the number $p^e$ does not divide $m - i$. By Lemma 4.1.1 this term is $0$. For $i = 1$ no other term is left. If $a_1 = \dots = a_{i-1} = 0$, then every term of the sum is $0$. $\square$

So a translation cannot change $a_1$. If $a_1 = 0$, it cannot change $a_2$, and so on up to $a_{p^e - 1}$. We call $a_1, \dots, a_{p^e - 1}$ the *rigid layer* of $f$. Note that the theorem does not say that each $a_i$ with $i < p^e$ is invariant. If $a_1 \ne 0$, then $a_2$ can change, by $\binom{m-1}{1} a_1 c = (m - 1) a_1 c = -a_1 c$.

**Proposition 4.1.4.** The coefficient $a_{p^e}$ changes as
$$a_{p^e}' = a_{p^e} + m_0\, c^{p^e} + \sum_{0 < j < p^e} \binom{m-j}{p^e-j} a_j c^{p^e-j}.$$
In particular, if $a_1 = \dots = a_{p^e - 1} = 0$, then $a_{p^e}' = a_{p^e} + m_0 c^{p^e}$.

Node: SG0000003J · Lean: `Singularity.coeff_taylor_sub_pow`, `Singularity.coeff_taylor_sub_pow_of_eq_zero`

*Proof.* In Lemma 4.1.2 with $i = p^e$, the term with $j = 0$ is the coefficient of $z^{m - p^e}$ in $(z + c)^m$. By Lemma 4.1.1 it is the coefficient of $z^{p^e (m_0 - 1)}$ in $(z^{p^e} + c^{p^e})^{m_0}$, which is $\binom{m_0}{1} c^{p^e} = m_0 c^{p^e}$. The term with $j = p^e$ is $a_{p^e}$. $\square$

Since $p \nmid m_0$, the element $m_0$ is a unit of $R$. So when the rigid layer is $0$, the translations change $a_{p^e}$ by exactly the $p^e$-th powers, up to the unit $m_0$. For $m = q$ and $f = z^q + F$ this is the cleaning of Section 1.3: the translation $z \mapsto z + c$ replaces $F$ by $F + c^q$. For $e = 0$, the proposition is the classical Tschirnhausen step, $a_1' = a_1 + m c$.

**Example 4.1.5.** Let $p = 2$ and $m = 4$, so $e = 2$ and $m_0 = 1$. Modulo $2$, the binomial coefficients $\binom{3}{1}$, $\binom{3}{2}$ and $\binom{3}{3}$ are $1$, and $\binom{2}{1}$ is $0$. So
$$a_1' = a_1, \quad a_2' = a_2 + a_1 c, \quad a_3' = a_3 + a_1 c^2, \quad a_4' = a_4 + a_3 c + a_2 c^2 + a_1 c^3 + c^4.$$
The coefficient $a_1$ never changes. If $a_1 = 0$, then $a_2$ and $a_3$ do not change, and $a_4$ changes by $c^4$. Theorem 4.1.3 for $i = 3$ predicts the term $\binom{3}{2} a_1 c^2 + \binom{2}{1} a_2 c$, and the second coefficient is $0$ in characteristic $2$.

**Example 4.1.6.** Let $p = 2$ and $m = 6$, so $e = 1$ and $m_0 = 3$. Then $a_1' = a_1$ and
$$a_2' = a_2 + \binom{5}{1} a_1 c + \binom{6}{2} c^2 = a_2 + a_1 c + c^2,$$
since $5$ and $15$ are odd. This agrees with Proposition 4.1.4, because $m_0 = 3 \equiv 1$.

The Lean library states these results for a polynomial in one variable over a commutative ring of characteristic $p$. The main theorems use only the axioms `propext`, `Classical.choice` and `Quot.sound`.

### What the rigid layer means

In characteristic $0$, the Tschirnhausen step gives a hypersurface of maximal contact, and the problem descends to the coefficient ideal of $a_2, \dots, a_m$ on that hypersurface. Theorem 4.1.3 shows that, when $p \mid m$, the coefficients of the rigid layer are invariants of $f$ under the translations of $z$. A choice of $z$ cannot make them small. A resolution process must make their orders large by blowups of the base instead. After that, one can hope that $f$ is close to $(z^{p^e} + b)^{m_0}$, and that a Tschirnhausen step in the variable $z^{p^e}$, with the unit $m_0$, gives an object of multiplicity prime to $p$. Whether blowups can always do this is an open question. It is a part of the problem of embedded resolution of threefolds in positive characteristic, which is open in general. Volume 9 reports on it.

### Notes and references

The obstruction to the Tschirnhausen step in characteristic $p$ is classical, and every account of the failure of maximal contact mentions it [Hir64, Hir67]. The precise form of Theorem 4.1.3 and Proposition 4.1.4, with the Frobenius in place of the theorem of Lucas, is elementary, and the project found no source that states it in this form. Cossart and Piltant work with the equation $z^p + f_1 z^{p-1} + \dots$ of multiplicity $p$ in dimension $3$, where the rigid layer is $f_1, \dots, f_{p-1}$ and its role is visible in their reductions [CP08, Cos87].
