---
title: The regular locus and the criterion of Nagata
nodes: [SG0000002N, SG0000002P, SG0000002Q, SG0000000K]
sources: [Mat, Nag62, EGA4-7, Mathlib]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The regular locus and the criterion of Nagata

A resolution of singularities changes a variety only along its singular points. Thus we must know that the singular points form a closed set, and that the regular points form an open set. In this section we prove the criterion of Nagata. It reduces the openness of the regular locus of a Noetherian ring $A$ to a weaker property of the quotients $A/\mathfrak{p}$: each one must have a nonempty open set of regular points.

Throughout the section, $A$ is a Noetherian ring. For a prime ideal $\mathfrak{p}$ of $A$ we write $V(\mathfrak{p})$ for the set of the primes that contain $\mathfrak{p}$, and for $f \in A$ we write $D(f)$ for the set of the primes that do not contain $f$. The sets $D(f)$ are a basis of the topology of $\operatorname{Spec} A$.

**Definition 1.7.1.** The *regular locus* of $A$ is the set
$$\operatorname{Reg}(A) = \{\mathfrak{p} \in \operatorname{Spec} A : A_\mathfrak{p} \text{ is a regular local ring}\}.$$

For a scheme $X$, a point $x$ is regular when $\mathcal{O}_{X,x}$ is regular. If $X = \operatorname{Spec} A$, then the regular points of $X$ are the points of $\operatorname{Reg}(A)$.

### Generization

**Proposition 1.7.2.** Let $\mathfrak{q} \subseteq \mathfrak{p}$ be prime ideals of $A$. If $\mathfrak{p} \in \operatorname{Reg}(A)$, then $\mathfrak{q} \in \operatorname{Reg}(A)$.

Node: SG0000002N · Lean: `Singularity.Algebra.regularLocus_stableUnderGeneralization`

*Proof.* The ideal $\mathfrak{q}A_\mathfrak{p}$ is a prime ideal of $A_\mathfrak{p}$, and $A_\mathfrak{q}$ is isomorphic to the localization of $A_\mathfrak{p}$ at $\mathfrak{q}A_\mathfrak{p}$. By Corollary 1.6.9, this localization is a regular local ring. $\square$

In topological terms, $\operatorname{Reg}(A)$ is stable under generization: if a point is in $\operatorname{Reg}(A)$, then each point whose closure contains it is in $\operatorname{Reg}(A)$. An open set has this property, but the property alone does not make a set open.

### A topological criterion

**Lemma 1.7.3.** Let $U \subseteq \operatorname{Spec} A$ be stable under generization. Assume that for each $\mathfrak{p} \in U$ there is $f \notin \mathfrak{p}$ with $D(f) \cap V(\mathfrak{p}) \subseteq U$. Then $U$ is open.

Lean: `Singularity.Algebra.isOpen_of_stableUnderGeneralization`

*Proof.* Let $Z$ be the complement of $U$. We show that $Z$ is closed. The closure of $Z$ is $V(J)$, where $J$ is the intersection of the primes in $Z$. Since $A$ is Noetherian, $J$ has only finitely many minimal primes $\mathfrak{p}_1, \dots, \mathfrak{p}_n$.

First we show that each $\mathfrak{p}_i$ is in $Z$. Assume that $\mathfrak{p}_1 \in U$, and take $f \notin \mathfrak{p}_1$ with $D(f) \cap V(\mathfrak{p}_1) \subseteq U$. Let
$$O = D(f) \setminus (V(\mathfrak{p}_2) \cup \dots \cup V(\mathfrak{p}_n)).$$
The set $O$ is open. For $i \ge 2$, the prime $\mathfrak{p}_i$ is not contained in $\mathfrak{p}_1$, because both are minimal over $J$. Thus $\mathfrak{p}_1 \in O$. Since $\mathfrak{p}_1$ is in the closure of $Z$, the open set $O$ contains a point $\mathfrak{q} \in Z$. Then $\mathfrak{q} \supseteq J$, so $\mathfrak{q}$ contains some $\mathfrak{p}_i$. Since $\mathfrak{q} \in O$, we have $i = 1$. Thus $\mathfrak{q} \in D(f) \cap V(\mathfrak{p}_1) \subseteq U$. This is a contradiction, because $\mathfrak{q} \in Z$.

Now let $\mathfrak{z}$ be in the closure of $Z$. Then $\mathfrak{z}$ contains some $\mathfrak{p}_i$. If $\mathfrak{z} \in U$, then $\mathfrak{p}_i \in U$, because $U$ is stable under generization. This is not possible, so $\mathfrak{z} \in Z$. Thus $Z$ is closed. $\square$

Lemma 1.7.3 is the topological criterion of Nagata [Mat, Theorem 24.2]. Matsumura states it as an equivalence. The converse is clear, because an open set $U$ contains $D(f)$ for some $f \notin \mathfrak{p}$.

### Spreading a regular system of parameters

We need an elementary lemma that makes a choice uniform. It uses only that each ideal of $A$ is finitely generated.

**Lemma 1.7.4.** Let $\mathfrak{p}$ be a prime ideal of $A$, and let $I$ and $J$ be ideals of $A$. Assume that for each $y \in J$ there is $s \notin \mathfrak{p}$ with $sy \in I$. Then there is $g \notin \mathfrak{p}$ with $gJ \subseteq I$.

Lean: `Singularity.Algebra.exists_notMem_forall_mul_mem`

*Proof.* Let $y_1, \dots, y_n$ generate $J$, and take $s_i \notin \mathfrak{p}$ with $s_i y_i \in I$. Let $g = s_1 \cdots s_n$. Then $g \notin \mathfrak{p}$, because $\mathfrak{p}$ is prime, and $g y_i \in I$ for each $i$. Thus $gJ \subseteq I$. $\square$

The next result is the main step. It says that a regular system of parameters at $\mathfrak{p}$ stays a good system at the primes near $\mathfrak{p}$, as long as we stay on $V(\mathfrak{p})$.

**Proposition 1.7.5.** Let $\mathfrak{p} \in \operatorname{Reg}(A)$. Then there is $f \notin \mathfrak{p}$ with this property: for each prime $\mathfrak{q} \supseteq \mathfrak{p}$ with $f \notin \mathfrak{q}$, if $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ is a regular local ring, then $A_\mathfrak{q}$ is a regular local ring.

Node: SG0000002P · Lean: `Singularity.Algebra.exists_notMem_isRegularLocalRing_of_quotient`

*Proof.* We prove a stronger statement. Let $I \subseteq \mathfrak{p}$ be an ideal such that $B = A_\mathfrak{p}/IA_\mathfrak{p}$ is a regular local ring of dimension $r$. We show that there is $f \notin \mathfrak{p}$ such that for each prime $\mathfrak{q} \supseteq \mathfrak{p}$ with $f \notin \mathfrak{q}$, if $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ is regular, then $A_\mathfrak{q}/IA_\mathfrak{q}$ is regular. The proposition is the case $I = 0$. We use induction on $r$.

Let $r = 0$. Then the maximal ideal $\mathfrak{p}B$ of $B$ is $0$, so $\mathfrak{p}A_\mathfrak{p} = IA_\mathfrak{p}$. Thus for each $y \in \mathfrak{p}$ there is $s \notin \mathfrak{p}$ with $sy \in I$. By Lemma 1.7.4 there is $f \notin \mathfrak{p}$ with $f\mathfrak{p} \subseteq I$. Let $\mathfrak{q} \supseteq \mathfrak{p}$ be a prime with $f \notin \mathfrak{q}$. Then $f$ is a unit in $A_\mathfrak{q}$, so $\mathfrak{p}A_\mathfrak{q} = IA_\mathfrak{q}$. Thus $A_\mathfrak{q}/IA_\mathfrak{q} = A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$, and the claim is clear.

Let $r \ge 1$. By Lemma 1.3.2 there is an element $z$ of the maximal ideal of $B$ with $z$ not in its square. Write $z$ as the image of $a/s$ with $a \in A$ and $s \notin \mathfrak{p}$. Then $a \in \mathfrak{p}$, and the image $x$ of $a$ in $B$ is $zs$. Since $s$ is a unit of $B$, the element $x$ is in the maximal ideal and not in its square. By Proposition 1.2.6, $B/(x)$ is a regular local ring of dimension $r - 1$. Also $B/(x) \cong A_\mathfrak{p}/(I + aA)A_\mathfrak{p}$. By the induction hypothesis for the ideal $I + aA$, there is $f_1 \notin \mathfrak{p}$ such that $A_\mathfrak{q}/(I + aA)A_\mathfrak{q}$ is regular for each prime $\mathfrak{q} \supseteq \mathfrak{p}$ with $f_1 \notin \mathfrak{q}$ and $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ regular.

Now we spread the fact that $x$ is a nonzerodivisor. By Theorem 1.3.3, $B$ is a domain, and $x \ne 0$. Let $(I : a) = \{y \in A : ya \in I\}$. For $y \in (I : a)$, the image of $y$ in $B$ times $x$ is $0$, so the image of $y$ is $0$, and there is $s \notin \mathfrak{p}$ with $sy \in I$. By Lemma 1.7.4 there is $g \notin \mathfrak{p}$ with $g(I : a) \subseteq I$.

Let $f = f_1 g$. Then $f \notin \mathfrak{p}$. Let $\mathfrak{q} \supseteq \mathfrak{p}$ be a prime with $f \notin \mathfrak{q}$ and $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ regular, and let $C = A_\mathfrak{q}/IA_\mathfrak{q}$. Let $x'$ be the image of $a$ in $C$. Since $a \in \mathfrak{p} \subseteq \mathfrak{q}$, the element $x'$ is in the maximal ideal of $C$. We show that $x'$ is a nonzerodivisor of $C$. Let $b/t \in A_\mathfrak{q}$ with $(b/t) a \in IA_\mathfrak{q}$. Then there is $u \notin \mathfrak{q}$ with $uba \in I$. Thus $ub \in (I : a)$ and $gub \in I$. Since $gu \notin \mathfrak{q}$, the element $b/t$ is in $IA_\mathfrak{q}$. By the choice of $f_1$, the ring $C/(x') \cong A_\mathfrak{q}/(I + aA)A_\mathfrak{q}$ is regular. By Proposition 1.2.8, $C$ is regular. $\square$

### The criterion of Nagata

To apply Proposition 1.7.5, we must know that $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ is regular for the primes $\mathfrak{q}$ near $\mathfrak{p}$. This is a property of the ring $A/\mathfrak{p}$.

**Lemma 1.7.6.** Let $\mathfrak{p} \subseteq \mathfrak{q}$ be prime ideals of $A$. Then $\mathfrak{q}/\mathfrak{p}$ is a prime ideal of $A/\mathfrak{p}$, and
$$(A/\mathfrak{p})_{\mathfrak{q}/\mathfrak{p}} \cong A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}.$$

Lean: `Singularity.Algebra.localizationQuotientEquiv`

*Proof.* The first claim is clear. For the second claim, we show that $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ has the universal property of the localization of $A/\mathfrak{p}$ at the complement of $\mathfrak{q}/\mathfrak{p}$. The map $A/\mathfrak{p} \to A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ sends each element $\bar{s}$ with $s \notin \mathfrak{q}$ to a unit. Each element of $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ is the image of some $a/s$, and $a/s \cdot \bar{s} = \bar{a}$. If $\bar{x}$ and $\bar{y}$ have the same image, then $x - y \in \mathfrak{p}A_\mathfrak{q}$, so there is $u \notin \mathfrak{q}$ with $u(x - y) \in \mathfrak{p}$, and $\bar{u}\bar{x} = \bar{u}\bar{y}$ in $A/\mathfrak{p}$. These three properties characterize the localization. $\square$

**Theorem 1.7.7 (Nagata).** Let $A$ be a Noetherian ring. Assume that for each $\mathfrak{p} \in \operatorname{Reg}(A)$ the set $\operatorname{Reg}(A/\mathfrak{p})$ contains a nonempty open subset of $\operatorname{Spec} A/\mathfrak{p}$. Then $\operatorname{Reg}(A)$ is open in $\operatorname{Spec} A$.

Node: SG0000002Q · Lean: `Singularity.Algebra.isOpen_regularLocus_of_exists_isOpen`

*Proof.* We apply Lemma 1.7.3 to $U = \operatorname{Reg}(A)$. By Proposition 1.7.2, $U$ is stable under generization. Let $\mathfrak{p} \in U$, and let $W \subseteq \operatorname{Reg}(A/\mathfrak{p})$ be a nonempty open set. An open set is stable under generization, and the zero ideal is the generic point of $\operatorname{Spec} A/\mathfrak{p}$, so $(0) \in W$. Since the basic open sets are a basis, there is $\bar{g} \in A/\mathfrak{p}$ with $(0) \in D(\bar{g}) \subseteq W$. Then $\bar{g} \ne 0$, so $\bar{g}$ is the image of some $g \notin \mathfrak{p}$. Take $f$ as in Proposition 1.7.5.

Let $\mathfrak{q} \in D(fg) \cap V(\mathfrak{p})$. Then $\bar{g} \notin \mathfrak{q}/\mathfrak{p}$, so $\mathfrak{q}/\mathfrak{p} \in W$, and $(A/\mathfrak{p})_{\mathfrak{q}/\mathfrak{p}}$ is regular. By Lemma 1.7.6, $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ is regular. Since $f \notin \mathfrak{q}$, Proposition 1.7.5 gives that $A_\mathfrak{q}$ is regular. Thus $D(fg) \cap V(\mathfrak{p}) \subseteq U$ with $fg \notin \mathfrak{p}$, and Lemma 1.7.3 completes the proof. $\square$

**Example 1.7.8.** Let $k$ be a field and let $A = k[x, y]/(y^2 - x^3)$, the ring of the cuspidal cubic. We compute $\operatorname{Reg}(A)$. In $A$ we have $y^2 = x^3$. Let $t = y/x$ in the fraction field. Then $t^2 = x$ and $t^3 = y$, so $A[1/x] = k[t, 1/t]$. This ring is a localization of the principal ideal domain $k[t]$, so each of its local rings is regular. Thus $D(x) \subseteq \operatorname{Reg}(A)$. If a prime $\mathfrak{q}$ contains $x$, then it contains $y^2 = x^3$, so $\mathfrak{q} = (x, y)$. The maximal ideal of $A_{(x, y)}$ needs two generators, because $y^2 - x^3 \in (x, y)^2$ in $k[x, y]$. But $\dim A_{(x, y)} = 1$, so $(x, y) \notin \operatorname{Reg}(A)$. Thus $\operatorname{Reg}(A) = D(x)$, and this set is open.

### The regular locus of a variety

Let $A$ be a finitely generated algebra over a field $k$. Then each quotient $A/\mathfrak{p}$ is also finitely generated over $k$. Thus, by Theorem 1.7.7, the regular locus of $A$ is open if each domain $D$ of finite type over $k$ has a nonempty open regular locus. The generic point of $\operatorname{Spec} D$ is regular, because $D_{(0)}$ is a field. The problem is to find an open neighbourhood of it.

If $k$ is perfect, then the fraction field of $D$ is separable over $k$, and $D$ is smooth over $k$ on a nonempty open set. A smooth algebra over a field is regular, by the Jacobian criterion. Over an imperfect field, $D$ can fail to be smooth at every point, and the proof needs other tools, for example $p$-bases or the theory of excellent rings [EGA4-7]. The openness of the regular locus of a variety is the node SG0000000K. With Theorem 1.7.7, the node now needs only the existence of a nonempty open regular set for a domain of finite type over a field. Section 1.8 proves this existence when $k$ has characteristic $0$ (Theorem 1.8.9).

### The Lean proof

All the results of this section are in `Singularity/Algebra/RegularLocus.lean`. In Lean, $\operatorname{Reg}(A)$ is `Singularity.Algebra.regularLocus A`, a set of points of `PrimeSpectrum A`. The ring $A_\mathfrak{q}/\mathfrak{p}A_\mathfrak{q}$ is `Localization.AtPrime q ⧸ p.map (algebraMap A _)`.

The induction in Proposition 1.7.5 is the theorem `Singularity.Algebra.exists_notMem_isRegularLocalRing_quotient`, and it quantifies over all ideals $I \subseteq \mathfrak{p}$ with $\dim A_\mathfrak{p}/IA_\mathfrak{p} = r$. The isomorphism $B/(x) \cong A_\mathfrak{p}/(I + aA)A_\mathfrak{p}$ is `Singularity.Algebra.quotQuotSpanEquiv`, which composes the Mathlib isomorphism `DoubleQuot.quotQuotEquivQuotSup` with the equality $(I + aA)A_\mathfrak{p} = IA_\mathfrak{p} + aA_\mathfrak{p}$. Lemma 1.7.4 uses the induction principle `Submodule.fg_induction` in place of a list of generators.

Lemma 1.7.3 uses the Mathlib lemmas `PrimeSpectrum.zeroLocus_vanishingIdeal_eq_closure` for the closure of $Z$ and `Ideal.finite_minimalPrimes_of_isNoetherianRing` for the finiteness of the minimal primes. Lemma 1.7.6 is proved with `isLocalization_iff`, which is the universal property in the proof above, and `IsLocalization.algEquiv`. All the theorems of this section use only the three standard axioms of Lean.

### Notes and references

The criterion is due to Nagata [Nag62], and our proof follows [Mat, Section 24]. Matsumura proves Lemma 1.7.3 as [Mat, Theorem 24.2] and then uses it for several loci: the regular locus, the normal locus and the Cohen-Macaulay locus. A Noetherian ring in which $\operatorname{Reg}(B)$ is open for each finitely generated $A$-algebra $B$ is called J-2. Grothendieck proved that each excellent ring is J-2 [EGA4-7], and a ring of finite type over a field is excellent. The Lean proof of the openness of the regular locus of a variety is complete over a perfect field (Theorem 1.8.17), and thus in characteristic $0$. Over an imperfect field it is not complete.
