---
title: Regular local rings
nodes: [SG00000021]
sources: [AM69, Mat, Stacks, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Regular local rings

Section 1.1 showed that $\dim R \le \operatorname{edim} R$ for each Noetherian local ring $R$. In this section we study the rings where the two numbers are equal. We first give the definition and examples. Then we show how regularity behaves when we divide by one element. This is the main tool of the chapter, because it lets us prove a property of regular local rings by induction on the dimension.

**Definition 1.2.1.** A Noetherian local ring $(R, \mathfrak{m}, \kappa)$ is *regular* if $\operatorname{edim} R = \dim R$. By Lemma 1.1.1, this is the case if and only if $\mathfrak{m}$ has a set of $\dim R$ generators.

Lean: `IsRegularLocalRing` (in Mathlib)

Let $d = \dim R$. Since each set of generators of $\mathfrak{m}$ has at least $d$ elements (Corollary 1.1.3), a regular local ring is a local ring where $\mathfrak{m}$ has the least possible number of generators. Geometrically, the tangent space at the point has the same dimension as the variety at the point. This is the algebraic form of the condition that the point is not singular.

The Mathlib definition uses $\mu(\mathfrak{m})$ and not $\operatorname{edim} R$. The lemma `IsRegularLocalRing.iff_finrank_cotangentSpace` of Mathlib gives the form with the cotangent space.

### Examples

**Example 1.2.2 (dimension 0 and 1).** A field $K$ is a regular local ring of dimension 0. Its maximal ideal is $0$, so $\operatorname{edim} K = 0$, and $0$ is its only prime ideal, so $\dim K = 0$. Conversely, a regular local ring of dimension 0 has $\mu(\mathfrak{m}) = 0$, so $\mathfrak{m} = 0$ and $R$ is a field.

A discrete valuation ring $R$ with uniformizer $t$ is a regular local ring of dimension 1. Its maximal ideal is $(t)$, so $\operatorname{edim} R \le 1$, and its prime ideals are $0$ and $(t)$, so $\dim R = 1$. Examples are the ring $\mathbb{Z}_{(p)}$ for a prime number $p$, the ring $k[x]_{(x)}$ and the ring $k[[x]]$ of formal power series over a field $k$. Section 1.4 proves the converse: a regular local ring of dimension 1 is a discrete valuation ring.

**Example 1.2.3 (the origin of affine space).** Let $k$ be a field and let $R = k[x_1, \dots, x_n]_{(x_1, \dots, x_n)}$ be the local ring of $\mathbb{A}^n_k$ at the origin. Then $R$ is a regular local ring of dimension $n$.

The ideal $\mathfrak{m} = (x_1, \dots, x_n)$ has $n$ generators, so $\operatorname{edim} R \le n$. For the other inequality, let $\mathfrak{p}_i = (x_1, \dots, x_i)$ for $0 \le i \le n$. The quotient of the polynomial ring by $(x_1, \dots, x_i)$ is the polynomial ring $k[x_{i+1}, \dots, x_n]$, which is a domain. Thus each $\mathfrak{p}_i$ is a prime ideal of the polynomial ring, and it is contained in the maximal ideal of the origin, so it gives a prime ideal of $R$. The chain
$$0 = \mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \dots \subsetneq \mathfrak{p}_n = \mathfrak{m}$$
has length $n$, so $\dim R \ge n$. With Corollary 1.1.3 we get $n \le \dim R \le \operatorname{edim} R \le n$. Note that we did not use the theorem that $\dim k[x_1, \dots, x_n] = n$. The local computation is sufficient.

**Example 1.2.4 (the cusp).** Let $k$ be a field and let $R = k[x, y]_{(x,y)}/(y^2 - x^3)$. This is the local ring at the origin of the plane curve $y^2 = x^3$. We show that $\dim R = 1$ and $\operatorname{edim} R = 2$, so $R$ is not regular.

Let $A = k[x, y]_{(x,y)}$. By Example 1.2.3, $\operatorname{edim} A = 2$. The element $f = y^2 - x^3$ is in $\mathfrak{m}_A^2$, so Lemma 1.1.5 gives $\operatorname{edim} R = \operatorname{edim} A = 2$. For the dimension, the polynomial $y^2 - x^3$ is irreducible, so $R$ is a domain. It is not a field, because $x \ne 0$ in $R$ and $x$ is not a unit. Thus $0 \subsetneq \mathfrak{m}$ is a chain of prime ideals and $\dim R \ge 1$. The quotient $R/(x) = k[y]_{(y)}/(y^2)$ has only one prime ideal, so $\dim R/(x) = 0$, and Lemma 1.1.4 gives $\dim R \le 1$.

The tangent space of the cusp at the origin is the whole plane, but the curve has dimension 1. Section 1.4 shows the same fact from a second point of view: the ring $R$ is not integrally closed.

**Example 1.2.5 (a fat point).** Let $k$ be a field and let $R = k[\varepsilon]/(\varepsilon^2)$. Then $R$ is a local ring with $\mathfrak{m} = (\varepsilon)$ and $\mathfrak{m}^2 = 0$. Thus $\operatorname{edim} R = 1$. The only prime ideal is $\mathfrak{m}$, since each prime ideal contains the nilpotent element $\varepsilon$. Thus $\dim R = 0$ and $R$ is not regular. This example shows a general fact. Each regular local ring is reduced, because it is a domain (Theorem 1.3.3).

### The quotient by a parameter

Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d \ge 1$. The next proposition tells us how to make a regular local ring of dimension $d - 1$ from $R$. Geometrically, we cut the variety with a hypersurface that is regular at the point.

**Proposition 1.2.6.** Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$, and let $x \in \mathfrak{m} \setminus \mathfrak{m}^2$. Then $R/(x)$ is a regular local ring of dimension $d - 1$.

Node: SG00000021 · Lean: `Singularity.Algebra.quotient_span_singleton`

*Proof.* Let $\bar{R} = R/(x)$. Since $x \in \mathfrak{m}$, the ring $\bar{R}$ is a Noetherian local ring with the maximal ideal $\mathfrak{m}/(x)$. We compare four numbers. Since $x \notin \mathfrak{m}^2$, Lemma 1.1.5 gives
$$\operatorname{edim} \bar{R} = \operatorname{edim} R - 1 = d - 1.$$
Corollary 1.1.3 for $\bar{R}$ gives $\dim \bar{R} \le \operatorname{edim} \bar{R} = d - 1$. Lemma 1.1.4 gives $d = \dim R \le \dim \bar{R} + 1$, that is, $\dim \bar{R} \ge d - 1$. Thus
$$d - 1 \le \dim \bar{R} \le \operatorname{edim} \bar{R} = d - 1,$$
and all these numbers are equal. So $\bar{R}$ is regular of dimension $d - 1$. $\square$

The hypothesis $x \notin \mathfrak{m}^2$ is necessary. If $x \in \mathfrak{m}^2$ and $x \ne 0$, then $\operatorname{edim} R/(x) = d$ by Lemma 1.1.5. The dimension of $R/(x)$ is $d - 1$, because $R$ is a domain (Theorem 1.3.3) and so $x$ is not a zero divisor [AM69, Corollary 11.18]. Thus $R/(x)$ is not regular. Example 1.2.4 is this case, with $R = k[x, y]_{(x,y)}$ and the element $y^2 - x^3$.

Proposition 1.2.6 is [Stacks, Tag 00NQ]. A repeated application gives the following corollary. We give a direct proof.

**Corollary 1.2.7 (regular systems of parameters).** Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$, and let $x_1, \dots, x_d$ generate $\mathfrak{m}$. Then for each $0 \le i \le d$ the ring $R_i = R/(x_1, \dots, x_i)$ is a regular local ring of dimension $d - i$. In particular, $R_d$ is the residue field $\kappa$.

Lean: none yet

*Proof.* The maximal ideal of $R_i$ is generated by the classes of $x_{i+1}, \dots, x_d$, so $\operatorname{edim} R_i \le d - i$. For $j \ge 1$ we have $R_j = R_{j-1}/(\bar{x}_j)$, so Lemma 1.1.4 gives $\dim R_{j-1} \le \dim R_j + 1$. With $j = 1, \dots, i$ we get $d = \dim R_0 \le \dim R_i + i$. Thus
$$d - i \le \dim R_i \le \operatorname{edim} R_i \le d - i,$$
where the middle inequality is Corollary 1.1.3. $\square$

A set of $d$ generators of $\mathfrak{m}$ is a *regular system of parameters* of $R$. In Example 1.2.3 the coordinates $x_1, \dots, x_n$ are a regular system of parameters. In geometric terms, they are local coordinates at the point.

### The converse

The converse of Proposition 1.2.6 is false in general. If $R/(x)$ is regular, then $R$ need not be regular. We need one more hypothesis.

**Proposition 1.2.8.** Let $(R, \mathfrak{m})$ be a Noetherian local ring and let $x \in \mathfrak{m}$ be a nonzerodivisor. If $R/(x)$ is a regular local ring, then $R$ is a regular local ring and $\dim R/(x) = \dim R - 1$.

Lean: `Singularity.Algebra.of_quotient_span_singleton`

*Proof.* First we show that $\dim R/(x) = \dim R - 1$. This is [AM69, Corollary 11.18], and we recall the argument. Lemma 1.1.4 gives $\dim R \le \dim R/(x) + 1$. For the other inequality, recall that in a Noetherian ring the set of zero divisors is the union of the associated primes of $0$, and that each minimal prime ideal is an associated prime of $0$ [Mat, Theorems 6.1 and 6.5]. Since $x$ is not a zero divisor, $x$ is in no minimal prime ideal of $R$. Let $e = \dim R/(x)$ and let $\mathfrak{q}_0 \subsetneq \dots \subsetneq \mathfrak{q}_e$ be a chain of prime ideals of $R$ that contain $x$. The prime ideal $\mathfrak{q}_0$ contains $x$, so it is not minimal. Thus there is a prime ideal $\mathfrak{q}_{-1} \subsetneq \mathfrak{q}_0$, and the chain $\mathfrak{q}_{-1} \subsetneq \mathfrak{q}_0 \subsetneq \dots \subsetneq \mathfrak{q}_e$ shows that $\dim R \ge e + 1$.

Now let $\bar{R} = R/(x)$. By Lemma 1.1.5, $\operatorname{edim} R \le \operatorname{edim} \bar{R} + 1$. Since $\bar{R}$ is regular, $\operatorname{edim} \bar{R} = \dim \bar{R} = \dim R - 1$. Thus $\operatorname{edim} R \le \dim R$, and Corollary 1.1.3 gives equality. $\square$

**Example 1.2.9.** The hypothesis on $x$ is necessary. Let $k$ be a field and let $R = k[x, y]_{(x,y)}/(xy)$, the local ring at the origin of the union of the two axes. The element $x$ is a zero divisor, since $x \cdot y = 0$ and $y \ne 0$ in $R$. The quotient $R/(x) = k[y]_{(y)}$ is a discrete valuation ring, so it is regular of dimension 1. But $R$ is not regular. The element $xy$ is in the square of the maximal ideal of $k[x, y]_{(x,y)}$, so $\operatorname{edim} R = 2$ by Lemma 1.1.5. The ideals $(x)$ and $(y)$ are the minimal prime ideals of $R$. Each chain of prime ideals starts at one of them, and the quotients $R/(x) \cong k[y]_{(y)}$ and $R/(y) \cong k[x]_{(x)}$ have dimension 1, so $\dim R = 1$. Volume 9, Example 1.3.4 uses this ring.

Proposition 1.2.8 is [Stacks, Tag 00NU]. It is useful in the other direction from Proposition 1.2.6: it lets us prove that a ring is regular from a smaller ring.

### The Lean proof

The two propositions are `Singularity.Algebra.quotient_span_singleton` and `Singularity.Algebra.of_quotient_span_singleton` in the file `Singularity/Algebra/Regular.lean`. Each one states two facts: the quotient or the ring is regular, and `ringKrullDim (R ⧸ span {x}) + 1 = ringKrullDim R`. The Lean proofs follow the proofs above. The proof of Proposition 1.2.6 uses the Mathlib lemma `ringKrullDim_le_ringKrullDim_quotient_add_spanFinrank` for Lemma 1.1.4 and the two inequalities of Lemma 1.1.5. The proof of Proposition 1.2.8 uses the Mathlib lemma `ringKrullDim_quotient_span_singleton_succ_eq_ringKrullDim_of_mem_nonZeroDivisors` for [AM69, Corollary 11.18]. Corollary 1.2.7 is not yet in Lean.

### Notes and references

Regular local rings were introduced by Krull, and Zariski showed that they are the algebraic form of the simple points of a variety. The definitions and the results of this section are in [AM69, Chapter 11], [Mat, Section 14] and [Stacks]. Matsumura uses Proposition 1.2.6 and Corollary 1.2.7 in the form of [Mat, Theorem 14.2]: for a regular system of parameters, each quotient $R/(x_1, \dots, x_i)$ is regular. Example 1.2.9 shows why a regular local ring must be a domain, and Section 1.3 proves this.
