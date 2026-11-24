---
title: Dimension and the cotangent space
nodes: []
sources: [AM69, Mat, Stacks, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Dimension and the cotangent space

Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring. There are two numbers that measure the size of $R$ near its closed point. The first number is the Krull dimension $\dim R$. It is defined by chains of prime ideals, so it is a global property of the ring. The second number is the least number of generators of $\mathfrak{m}$. It is defined by linear algebra over $\kappa$, so it is easy to compute. A regular local ring is a ring where the two numbers are equal. In this section we compare them.

### The cotangent space

The $R$-module $\mathfrak{m}/\mathfrak{m}^2$ is killed by $\mathfrak{m}$, so it is a vector space over $\kappa$. It is the *cotangent space* of $R$. Its dimension is the *embedding dimension* of $R$, and we write $\operatorname{edim} R = \dim_\kappa \mathfrak{m}/\mathfrak{m}^2$. When $R$ is the local ring of a point $x$ of a variety over an algebraically closed field $k = \kappa$, the dual vector space $(\mathfrak{m}/\mathfrak{m}^2)^\vee$ is the Zariski tangent space of the variety at $x$.

**Lemma 1.1.1 (Nakayama).** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring, and let $x_1, \dots, x_n \in \mathfrak{m}$. Then $x_1, \dots, x_n$ generate $\mathfrak{m}$ if and only if their classes span $\mathfrak{m}/\mathfrak{m}^2$. In particular, $\mu(\mathfrak{m}) = \operatorname{edim} R$.

Lean: `IsLocalRing.spanFinrank_maximalIdeal_eq_finrank_cotangentSpace` (in Mathlib)

*Proof.* If the $x_i$ generate $\mathfrak{m}$, then their classes span $\mathfrak{m}/\mathfrak{m}^2$. Conversely, assume that the classes span $\mathfrak{m}/\mathfrak{m}^2$, and let $N = (x_1, \dots, x_n)$. Then $N + \mathfrak{m}^2 = \mathfrak{m}$, so the finitely generated module $M = \mathfrak{m}/N$ satisfies $\mathfrak{m} M = M$. By Nakayama's lemma [AM69, Proposition 2.6], $M = 0$, that is, $N = \mathfrak{m}$. This is [AM69, Proposition 2.8] for the module $\mathfrak{m}$.

For the last claim, a basis of $\mathfrak{m}/\mathfrak{m}^2$ lifts to a set of $\operatorname{edim} R$ generators of $\mathfrak{m}$, so $\mu(\mathfrak{m}) \le \operatorname{edim} R$. A set of generators of $\mathfrak{m}$ spans $\mathfrak{m}/\mathfrak{m}^2$, so $\operatorname{edim} R \le \mu(\mathfrak{m})$. $\square$

### The dimension theorem

The main theorem of the dimension theory of Noetherian local rings compares $\dim R$ with the number of generators of an ideal that is primary to $\mathfrak{m}$. Recall that an ideal $I$ is $\mathfrak{m}$-primary when $\mathfrak{m}^n \subseteq I \subseteq \mathfrak{m}$ for some $n$, or, in an equivalent form, when $\mathfrak{m}$ is the only prime ideal that contains $I$.

**Theorem 1.1.2 (dimension theorem).** Let $(R, \mathfrak{m})$ be a Noetherian local ring. Then $\dim R$ is finite, and it is equal to the least number $\delta(R)$ of generators of an $\mathfrak{m}$-primary ideal of $R$.

Lean: none yet

We do not prove this theorem here. The proof compares $\dim R$ and $\delta(R)$ with the degree of the Hilbert-Samuel polynomial of $R$. See [AM69, Theorem 11.14] or [Mat, Theorem 13.4]. Chapter 3 of this volume treats the Hilbert-Samuel polynomial. Mathlib has the two inequalities that we use below, and we give their Lean names.

**Corollary 1.1.3.** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring. Then $\dim R \le \mu(\mathfrak{m}) = \operatorname{edim} R$.

Lean: `ringKrullDim_le_spanFinrank_maximalIdeal` (in Mathlib)

*Proof.* The ideal $\mathfrak{m}$ is $\mathfrak{m}$-primary. Thus $\dim R = \delta(R) \le \mu(\mathfrak{m})$, and $\mu(\mathfrak{m}) = \operatorname{edim} R$ by Lemma 1.1.1. $\square$

This is [AM69, Corollary 11.15]. The inequality can be strict. Section 1.2 has examples.

**Lemma 1.1.4.** Let $(R, \mathfrak{m})$ be a Noetherian local ring and let $x \in \mathfrak{m}$. Then $\dim R \le \dim R/(x) + 1$.

Lean: `ringKrullDim_le_ringKrullDim_quotient_add_spanFinrank` (in Mathlib)

*Proof.* The ring $\bar{R} = R/(x)$ is a Noetherian local ring with the maximal ideal $\bar{\mathfrak{m}} = \mathfrak{m}/(x)$. Let $d = \dim \bar{R}$. By Theorem 1.1.2 there are $y_1, \dots, y_d \in \mathfrak{m}$ whose classes generate an $\bar{\mathfrak{m}}$-primary ideal of $\bar{R}$. Let $I = (x, y_1, \dots, y_d) \subseteq R$. A prime ideal $\mathfrak{p}$ of $R$ that contains $I$ contains $x$, so $\mathfrak{p}/(x)$ is a prime ideal of $\bar{R}$ that contains the classes of the $y_i$. Thus $\mathfrak{p}/(x) = \bar{\mathfrak{m}}$ and $\mathfrak{p} = \mathfrak{m}$. So $I$ is $\mathfrak{m}$-primary, and it has $d + 1$ generators. By Theorem 1.1.2, $\dim R = \delta(R) \le d + 1$. $\square$

The Mathlib lemma is more general: for an ideal $I$ in the Jacobson radical of a Noetherian ring $R$, it gives $\dim R \le \dim R/I + \mu(I)$. Lemma 1.1.4 is the case $I = (x)$. When $x$ is not a zero divisor, the inequality is an equality [AM69, Corollary 11.18]. Mathlib has this equality as `ringKrullDim_quotient_span_singleton_succ_eq_ringKrullDim_of_mem_nonZeroDivisors`.

### The embedding dimension of a quotient

The embedding dimension behaves more simply than the dimension under the quotient by one element. The behaviour depends only on whether the element is in $\mathfrak{m}^2$.

**Lemma 1.1.5.** Let $(R, \mathfrak{m}, \kappa)$ be a Noetherian local ring, let $x \in \mathfrak{m}$, and let $\bar{R} = R/(x)$. Then
$$\operatorname{edim} \bar{R} = \begin{cases} \operatorname{edim} R - 1 & \text{if } x \notin \mathfrak{m}^2, \\ \operatorname{edim} R & \text{if } x \in \mathfrak{m}^2. \end{cases}$$

Lean: `Singularity.Algebra.spanFinrank_maximalIdeal_quotient_add_one_le`, `Singularity.Algebra.spanFinrank_maximalIdeal_le_spanFinrank_maximalIdeal_quotient_add_one`

*Proof.* The maximal ideal of $\bar{R}$ is $\bar{\mathfrak{m}} = \mathfrak{m}/(x)$, and its square is $\bar{\mathfrak{m}}^2 = (\mathfrak{m}^2 + (x))/(x)$. Thus
$$\bar{\mathfrak{m}}/\bar{\mathfrak{m}}^2 \cong \mathfrak{m}/(\mathfrak{m}^2 + (x)).$$
This is the quotient of the vector space $\mathfrak{m}/\mathfrak{m}^2$ by the subspace that the class $\bar{x}$ of $x$ spans. That subspace has dimension 1 if $\bar{x} \ne 0$, that is, if $x \notin \mathfrak{m}^2$, and dimension 0 otherwise. $\square$

The Lean proof does not use the cotangent spaces. It proves the two inequalities $\mu(\bar{\mathfrak{m}}) + 1 \le \mu(\mathfrak{m})$ for $x \in \mathfrak{m} \setminus \mathfrak{m}^2$ and $\mu(\mathfrak{m}) \le \mu(\bar{\mathfrak{m}}) + 1$ for each $x \in \mathfrak{m}$ with sets of generators. For the first inequality, write $\mathfrak{m} = (s_1, \dots, s_n)$ with $n = \mu(\mathfrak{m})$, and $x = \sum f_i s_i$. Not all $f_i$ are in $\mathfrak{m}$, since $x \notin \mathfrak{m}^2$. If $f_{i_0}$ is a unit, then $x$ can replace $s_{i_0}$, and the images of the other $n - 1$ elements generate $\bar{\mathfrak{m}}$. For the second inequality, lift a set of generators of $\bar{\mathfrak{m}}$ to $\mathfrak{m}$ and add $x$. Together, the two inequalities give the case $x \notin \mathfrak{m}^2$ of Lemma 1.1.5. For $x \in \mathfrak{m}^2$, the Lean result `Singularity.Algebra.spanFinrank_maximalIdeal_le_of_le_sq`, with $I = (x)$, gives $\mu(\mathfrak{m}) \le \mu(\bar{\mathfrak{m}})$. The reverse inequality holds because the images of a set of generators of $\mathfrak{m}$ generate $\bar{\mathfrak{m}}$.

### The Lean proof

The file `Singularity/Algebra/Regular.lean` of `tamnd/singularity-lean` has the two inequalities of Lemma 1.1.5. Mathlib writes $\mu(I)$ as `I.spanFinrank` and $\dim R$ as `ringKrullDim R`. The dimension is an element of $\mathbb{N} \cup \{\pm\infty\}$, so that the dimension of the zero ring is $-\infty$ and the dimension of a ring with infinite chains is $+\infty$. For a Noetherian local ring the dimension is a natural number. The lemma `Singularity.Algebra.exists_ringKrullDim_eq_natCast` gives this number, and the proofs then work in $\mathbb{N}$ with the tactic `omega`.

The proofs of this section and of Sections 1.2 and 1.3 are adapted from the file `Hironaka/Algebra/Local/Regular.lean` of the Lean proof of Hironaka's theorem [HirLean], under its Apache 2.0 licence. The header of the Lean file gives the attribution.

### Notes and references

The dimension theorem is due to Krull and Chevalley. Atiyah and Macdonald [AM69, Chapter 11] prove it with the Hilbert-Samuel polynomial, and Matsumura [Mat, Section 13] proves it with systems of parameters. Theorem 1.1.2 contains Krull's principal ideal theorem: a minimal prime over a principal ideal has height at most 1. To see this, apply the theorem to the localization at the prime. The Stacks project has the same results in the chapter on commutative algebra [Stacks].
