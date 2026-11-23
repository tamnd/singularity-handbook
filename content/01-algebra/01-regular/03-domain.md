---
title: A regular local ring is a domain
nodes: [SG0000000J]
sources: [AM69, Mat, Stacks, Ser55, Mathlib, HirLean]
status: drafted
drafted_by: writer
reviewed_by: []
---
## A regular local ring is a domain

In this section we prove that a regular local ring is a domain. The proof is by induction on the dimension, with Proposition 1.2.6 as the inductive step. To use Proposition 1.2.6 we need an element $x \in \mathfrak{m} \setminus \mathfrak{m}^2$, and for the induction to work, $x$ must also avoid the minimal prime ideals of $R$. The tool that finds such an element is prime avoidance.

### Prime avoidance

The usual form of prime avoidance says that an ideal contained in a finite union of prime ideals is contained in one of them [AM69, Proposition 1.11]. We need a slightly stronger form, because the ideal $\mathfrak{m}^2$ is not prime.

**Lemma 1.3.1 (prime avoidance).** Let $R$ be a ring, and let $I, I_1, \dots, I_n$ be ideals of $R$ with $n \ge 1$. Assume that $I_2, \dots, I_n$ are prime ideals. If $I \subseteq I_1 \cup \dots \cup I_n$, then $I \subseteq I_j$ for some $j$.

Lean: `Ideal.subset_union_prime` (in Mathlib)

*Proof.* We use induction on $n$. For $n = 1$ there is nothing to prove. Let $n \ge 2$. If $I$ is contained in the union of $n - 1$ of the ideals $I_j$, then the induction hypothesis gives the result. Note that at most one of these $n - 1$ ideals is not prime, so the induction hypothesis applies after a change of the order. Thus we can assume that for each $j$ there is an element
$$a_j \in I \quad\text{with}\quad a_j \notin I_l \text{ for all } l \ne j.$$
Since $I \subseteq I_1 \cup \dots \cup I_n$, we have $a_j \in I_j$. We show that this gives a contradiction. Let
$$b = a_1 a_3 a_4 \cdots a_n \quad\text{and}\quad y = a_2 + b.$$
For $n = 2$ the product $b$ is $a_1$. The element $y$ is in $I$. We show that $y$ is in no $I_j$.

* The element $b$ is not in $I_2$. For $n = 2$ this is the choice of $a_1$. For $n \ge 3$, the ideal $I_2$ is prime and no factor of $b$ is in $I_2$. Since $a_2 \in I_2$, we get $y \notin I_2$.
* For $j \ne 2$, the element $b$ is in $I_j$, because $a_j$ is a factor of $b$. Since $a_2 \notin I_j$, we get $y \notin I_j$.

This contradicts $I \subseteq I_1 \cup \dots \cup I_n$. $\square$

The Mathlib lemma `Ideal.subset_union_prime` allows two ideals that are not prime. We need only one.

**Lemma 1.3.2.** Let $(R, \mathfrak{m})$ be a Noetherian local ring with $\dim R \ge 1$. Then there is an element $x \in \mathfrak{m}$ such that $x \notin \mathfrak{m}^2$ and $x$ is in no minimal prime ideal of $R$.

Lean: `Singularity.Algebra.exists_mem_maximalIdeal_notMem_sq_notMem_minimalPrimes`

*Proof.* A Noetherian ring has only finitely many minimal prime ideals [Mat, Theorem 6.5]. Let $\mathfrak{p}_1, \dots, \mathfrak{p}_k$ be the minimal prime ideals of $R$. Assume that the lemma is false. Then
$$\mathfrak{m} \subseteq \mathfrak{m}^2 \cup \mathfrak{p}_1 \cup \dots \cup \mathfrak{p}_k.$$
By Lemma 1.3.1, with $I_1 = \mathfrak{m}^2$, either $\mathfrak{m} \subseteq \mathfrak{m}^2$ or $\mathfrak{m} \subseteq \mathfrak{p}_i$ for some $i$.

In the first case $\mathfrak{m} = \mathfrak{m}^2$. By Nakayama's lemma, $\mathfrak{m} = 0$. Then $R$ is a field and $\dim R = 0$.

In the second case $\mathfrak{m} = \mathfrak{p}_i$, so the maximal ideal is a minimal prime ideal. Each prime ideal $\mathfrak{p}$ satisfies $\mathfrak{p} \subseteq \mathfrak{m} = \mathfrak{p}_i$, and so $\mathfrak{p} = \mathfrak{m}$ by the minimality of $\mathfrak{p}_i$. Thus $\mathfrak{m}$ is the only prime ideal and $\dim R = 0$.

Both cases contradict $\dim R \ge 1$. $\square$

### The theorem

**Theorem 1.3.3.** A regular local ring is a domain.

Node: SG0000000J · Lean: `Singularity.Algebra.isDomain_of_isRegularLocalRing`

*Proof.* Let $(R, \mathfrak{m})$ be a regular local ring of dimension $d$. We use induction on $d$.

Let $d = 0$. Then $\mu(\mathfrak{m}) = 0$, so $\mathfrak{m} = 0$. Thus $R$ is a field (Example 1.2.2), and a field is a domain.

Let $d \ge 1$, and assume that each regular local ring of dimension $d - 1$ is a domain. Lemma 1.3.2 gives an element $x \in \mathfrak{m} \setminus \mathfrak{m}^2$ that is in no minimal prime ideal of $R$. By Proposition 1.2.6, the ring $R/(x)$ is a regular local ring of dimension $d - 1$. By the induction hypothesis it is a domain, that is, the ideal $(x)$ is prime.

Each prime ideal contains a minimal prime ideal [AM69, Chapter 1, Exercise 8]. Let $\mathfrak{p} \subseteq (x)$ be a minimal prime ideal. We show that $\mathfrak{p} = x \mathfrak{p}$. Let $y \in \mathfrak{p}$. Then $y \in (x)$, so $y = zx$ for some $z \in R$. The ideal $\mathfrak{p}$ is prime and $x \notin \mathfrak{p}$ by the choice of $x$, so $z \in \mathfrak{p}$. Thus $y \in x\mathfrak{p}$. This shows $\mathfrak{p} \subseteq x\mathfrak{p}$, and the other inclusion is clear.

The ideal $\mathfrak{p}$ is a finitely generated $R$-module because $R$ is Noetherian, and $x \in \mathfrak{m}$. Thus $\mathfrak{p} = x\mathfrak{p} \subseteq \mathfrak{m}\mathfrak{p}$, and Nakayama's lemma [AM69, Proposition 2.6] gives $\mathfrak{p} = 0$. So the zero ideal is prime, and $R$ is a domain. $\square$

The proof uses the choice of $x$ twice. Proposition 1.2.6 needs $x \notin \mathfrak{m}^2$, and the step $\mathfrak{p} = x\mathfrak{p}$ needs $x \notin \mathfrak{p}$. Without the second condition the proof fails. For example, in the ring $k[x, y]_{(x,y)}/(xy)$ of Example 1.2.9, the quotient by the element $x$ is a domain, but $x$ is in the minimal prime ideal $(x)$, and the ring is not a domain. Of course, that ring is not regular.

**Corollary 1.3.4.** Let $X$ be a locally Noetherian scheme and let $x \in X$ be a point such that $\mathcal{O}_{X,x}$ is a regular local ring. Then $x$ lies on exactly one irreducible component of $X$.

Lean: none yet

*Proof.* Let $U = \operatorname{Spec} A$ be an affine open neighbourhood of $x$, and let $\mathfrak{q} \subseteq A$ be the prime ideal of $x$. The irreducible components of $U$ are the closed sets $V(\mathfrak{p})$ for the minimal prime ideals $\mathfrak{p}$ of $A$, and $x$ lies on $V(\mathfrak{p})$ if and only if $\mathfrak{p} \subseteq \mathfrak{q}$. The minimal prime ideals of $A$ that are contained in $\mathfrak{q}$ correspond to the minimal prime ideals of $A_\mathfrak{q} = \mathcal{O}_{X,x}$ [AM69, Proposition 3.11]. By Theorem 1.3.3, $\mathcal{O}_{X,x}$ is a domain, so it has exactly one minimal prime ideal, the zero ideal. Thus $x$ lies on exactly one irreducible component of $U$. The irreducible components of $X$ that contain $x$ meet $U$ in the irreducible components of $U$ that contain $x$, so the claim follows. $\square$

Volume 9, Section 1.3 uses Theorem 1.3.3 for this reason. A resolution of a variety can be made from resolutions of its irreducible components, because the components do not meet at a regular point.

### What this section does not prove

A regular local ring has two more properties that we do not prove here.

1. A regular local ring is a unique factorization domain. This is the theorem of Auslander and Buchsbaum [Mat, Theorem 20.3]. In particular, a regular local ring is integrally closed. The project has the node SG00000023 for this result, and it is not yet in Lean.
2. Let $R$ be a regular local ring and let $\mathfrak{p}$ be a prime ideal. Then $R_\mathfrak{p}$ is a regular local ring. This is a theorem of Serre [Ser55], and its proof uses homological algebra: a Noetherian local ring is regular if and only if it has finite global dimension [Mat, Theorems 19.2 and 19.3]. The project has the node SG0000000H for this result. Mathlib does not yet have it, and its definition of a regular ring has a TODO for it. Section 1.5 proves the first half of the theorem of Serre.

The second property is important for geometry. It says that the set of regular points of a scheme is stable under generization, and it is the first step to prove that the regular locus is open. The chapter of this volume on excellence returns to this question.

### The Lean proof

The Lean proof of Theorem 1.3.3 is `Singularity.Algebra.isDomain_of_isRegularLocalRing`. It applies the theorem `Singularity.Algebra.isDomain_of_isRegularLocalRing_of_ringKrullDim_eq`, which proves the statement for each dimension $n \in \mathbb{N}$ by induction on $n$. The statement in this lemma quantifies over all rings $R$, so that the induction hypothesis applies to the quotient ring $R/(x)$, which is a different type.

Prime avoidance is the Mathlib lemma `Ideal.subset_union_prime`. The step $\mathfrak{p} = x\mathfrak{p}$ is written as the inclusion `P ≤ span {x} • P`, and the Nakayama step is the Mathlib lemma `Submodule.eq_bot_of_le_smul_of_le_jacobson_bot`. The Lean proof is adapted from the file `Hironaka/Algebra/Local/Regular.lean` of [HirLean].

### Notes and references

Theorem 1.3.3 is [Mat, Theorem 14.3] and [Stacks, Tag 00NP]. Atiyah and Macdonald prove it in [AM69, Lemma 11.23] with the associated graded ring: for a regular local ring $R$, the graded ring $\bigoplus_n \mathfrak{m}^n/\mathfrak{m}^{n+1}$ is a polynomial ring over $\kappa$, and so it is a domain, and this implies that $R$ is a domain. The proof here is shorter, but the graded ring is useful for multiplicity theory, and Chapter 2 of this volume uses it.
