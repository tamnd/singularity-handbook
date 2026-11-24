---
title: The plan of the proofs
nodes: [SG0000001F, SG00000018, SG0000001C]
sources: [Abh66, Cut09, CP08, CP09, CP19, Zar44, Hir67]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The plan of the proofs

In this section we give the plan of the proof of Abhyankar, in the form of Cutkosky [Cut09], and the plan of the proof of Cossart and Piltant [CP19]. We prove one step of the first plan completely: a hypersurface singularity of multiplicity $m$ with $m! \ne 0$ in the field has a regular hypersurface that contains its points of multiplicity $m$. This is the step where the condition $p > 5$ enters.

### Three theorems on surfaces and on multiplicities

The proof of Abhyankar uses three theorems that are also of independent interest. We state them in the form of [Cut09]. In this section $k$ is an algebraically closed field.

**Theorem 1.2.1 (Abhyankar).** Let $K$ be a function field of dimension $d$ over $k$. Then there is a normal projective variety $V$ over $k$ with function field $K$ such that each point of $V$ has multiplicity at most $d!$.

Lean: none yet

This is [Cut09, Theorem 1.4]. Cutkosky writes that it generalizes a method of Albanese.

**Theorem 1.2.2 (embedded resolution of surfaces).** Let $V$ be a nonsingular variety of dimension 3 over $k$, let $S \subset V$ be a reduced surface, and let $E$ be a simple normal crossings divisor on $V$. Then there is a sequence of blowups $V_n \to V_{n-1} \to \dots \to V_0 = V$ such that the strict transform $S_n$ of $S$ is nonsingular and the total transform of $S + E$ is a simple normal crossings divisor. Each $V_i \to V_{i-1}$ is the blowup of a point or of a nonsingular curve that lies in the locus where the preimage of $S + E$ is not a simple normal crossings divisor.

Lean: none yet

**Theorem 1.2.3 (principalization).** Let $V$ be a nonsingular variety of dimension 3 over $k$, and let $\mathcal{I} \subseteq \mathcal{O}_V$ be a nonzero ideal sheaf. Then there is a sequence of blowups $V_n \to \dots \to V_0 = V$ such that $\mathcal{I}\mathcal{O}_{V_n}$ is locally principal. Each $V_i \to V_{i-1}$ is the blowup of a point or of a nonsingular curve that lies in the locus where $\mathcal{I}\mathcal{O}_{V_{i-1}}$ is not invertible.

Lean: none yet

These are [Cut09, Theorem 1.2] and [Cut09, Theorem 1.3]. Abhyankar proved them first in [Abh66], and Cutkosky writes that this is the most difficult part of the proof of Abhyankar. Theorem 1.2.2 is a close relative of the theorem of Cossart, Jannsen and Saito, Theorem 3.1.4 of Volume 4, which holds for each excellent surface in a regular excellent scheme.

Node: SG0000001C · Lean: `Singularity.EmbeddedResolutionSurface` (the statement only)

Cutkosky proves Theorems 1.2.2 and 1.2.3 in Sections 5 to 11 of [Cut09]. He follows the algorithm of Levi for a surface in a nonsingular threefold. He uses the invariant and the termination argument that Hironaka outlined for this algorithm in arbitrary characteristic. He resolves ideals by their weak transforms, as Bravo, Encinas and Villamayor do in characteristic 0, so the main invariant is the order of an ideal and not the multiplicity of a variety.

### The five steps

Cutkosky divides the proof of Theorem 1.1.1 into five steps [Cut09].

1. Prove Theorems 1.2.2 and 1.2.3.
2. Prove Theorem 1.2.1. For a threefold $V$ it gives a normal projective model $V_0$ of the function field of $V$ whose points have multiplicity at most $3! = 6$.
3. Prove that a point of multiplicity less than $p$ can be resolved locally.
4. Patch the local resolutions to a nonsingular projective variety that is birational to $V$.
5. Change a resolution $W \to V$ into a resolution that is an isomorphism over the nonsingular locus of $V$.

Steps 1 to 4 are in the proof of Abhyankar. Steps 1 and 4 are also in the proof of Zariski for threefolds in characteristic 0 [Zar44]. Step 5 is due to Cossart [Cut09]. If $p > 5$, then $6 < p$, so after Step 2 each point of $V_0$ has multiplicity less than $p$, and Step 3 applies to each point. This is the only place where the condition $p \ne 2, 3, 5$ enters. Step 3 gives local uniformization of each valuation of the function field. In the language of Volume 3, Chapter 4, Steps 4 and 5 are the patching.

### Maximal contact in small multiplicity

Step 3 works because a singularity of small multiplicity behaves as in characteristic 0. Abhyankar proved Step 3 with the method of Jung: he projects to a nonsingular threefold and resolves the branch locus with Theorem 1.2.2. Cutkosky describes a second proof of Step 3, with ideas of Hironaka, Giraud and Cossart: in small multiplicity, a hypersurface of maximal contact exists [Cut09, Section 3]. We prove the first part of this fact. It needs only a derivation.

**Lemma 1.2.4.** Let $B$ be a ring, let $D \colon B \to B$ be an additive map with $D(ab) = a D(b) + b D(a)$ for all $a, b \in B$, and let $I$ be an ideal of $B$. Then $D(I^e) \subseteq I^{e-1}$ for each $e \ge 1$.

Lean: none yet

*Proof.* The ideal $I^e$ is generated as an additive group by the products $b a_1 \cdots a_e$ with $b \in B$ and $a_1, \dots, a_e \in I$. By the Leibniz rule,
$$D(b a_1 \cdots a_e) = D(b) a_1 \cdots a_e + \sum_{i=1}^{e} b a_1 \cdots a_{i-1} D(a_i) a_{i+1} \cdots a_e.$$
Each term on the right is a product of at least $e - 1$ elements of $I$ and an element of $B$. So it lies in $I^{e-1}$. Since $D$ is additive, $D(I^e) \subseteq I^{e-1}$. $\square$

A derivation of a domain extends to each localization by the quotient rule $D(b/s) = (s D(b) - b D(s))/s^2$. For a point $q$ of $\operatorname{Spec} B$ we write $\operatorname{ord}_q h$ for the largest $e$ with $h \in \mathfrak{m}_q^e$, where $\mathfrak{m}_q$ is the maximal ideal of $\mathcal{O}_q = B_q$. For a hypersurface $X = V(h)$ in a regular scheme, we call $\operatorname{ord}_q h$ the *multiplicity* of $X$ at $q$, as [CP19] does. The order is defined in Volume 1, Section 3.2. It equals the Samuel multiplicity of the local ring of $X$ at $q$, a classical fact that we do not use.

**Proposition 1.2.5 (maximal contact for small multiplicity).** Let $k$ be a field, let $m \ge 1$ be an integer such that $m!$ is a unit in $k$, and let
$$h = z^m + a_1 z^{m-1} + \dots + a_m \in A[z], \qquad A = k[x_1, \dots, x_n].$$
Let $z' = z + a_1/m$. Then $\operatorname{ord}_q h \le m$ for each point $q$ of $\mathbb{A}^{n+1}_k = \operatorname{Spec} A[z]$, and each point $q$ with $\operatorname{ord}_q h = m$ lies on the regular hypersurface $V(z')$.

Lean: none yet

*Proof.* Let $D = \partial/\partial z$, a $k$-derivation of $A[z]$, and extend it to the local ring $\mathcal{O}_q$. If $h \in \mathfrak{m}_q^e$, then Lemma 1.2.4, applied $j$ times, gives $D^j h \in \mathfrak{m}_q^{e - j}$ for $j \le e$. We have $D^m h = m!$, a unit. So $h \notin \mathfrak{m}_q^{m+1}$, since otherwise $m! \in \mathfrak{m}_q$. This proves $\operatorname{ord}_q h \le m$. Now let $h \in \mathfrak{m}_q^m$. Then $D^{m-1} h \in \mathfrak{m}_q$. The terms $a_i z^{m-i}$ with $i \ge 2$ have degree less than $m - 1$ in $z$, so $D^{m-1}$ kills them, and
$$D^{m-1} h = m! \, z + (m-1)! \, a_1 = m! \, z'.$$
Since $m!$ is a unit, $z' \in \mathfrak{m}_q \cap A[z] = q$. So $q \in V(z')$. The map $A[z] \to A$ with $z \mapsto -a_1/m$ is surjective with kernel $(z')$, so $V(z') \cong \mathbb{A}^n_k$ is regular. $\square$

The proof uses only that $m!$ is a unit in $A$. So the proposition holds with the same proof for each ring $A$ that contains $k$, for example $A = k[[x_1, \dots, x_n]]$, and then $V(z') \cong \operatorname{Spec} A$ is regular when $A$ is regular. By the Weierstrass preparation theorem, a power series in $k[[x, z]]$ of order $m$ in which $z^m$ has a nonzero coefficient is a unit times a polynomial of the form of Proposition 1.2.5 with $A = k[[x]]$. So the proposition covers each hypersurface singularity of multiplicity $m$, after a linear change of coordinates when $k$ is infinite. The full statement of maximal contact also asks that the hypersurface keeps this property after each blowup in a permissible center. This is true for $m!$ a unit, and [Cut09, Section 3] outlines the proof. With maximal contact one can argue by induction on the dimension, as in characteristic 0.

For $m = p$ the proof breaks down at once. For $h = z^p + g(x)$ we have $D h = p z^{p-1} = 0$, so no derivative in $z$ sees the variable $z$. In fact no regular hypersurface works. Example 2.2.1 of Volume 9, due to Narasimhan, is the threefold $x^2 + y z^3 + z w^3 + y^7 w = 0$ in characteristic 2. Its points of multiplicity 2 near the origin are not contained in any regular hypersurface germ, also not in a formal one.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

The equation of Narasimhan has the form $z^p + g(x, y, w)$, with the variable called $x$ there in the role of $z$. Chapter 2 shows that these equations, and the Artin-Schreier equations, are the essential cases in dimension 3.

### The plan of Cossart and Piltant

The proof of Theorem 1.1.3 in [CP19] has four parts.

1. A reduction of Theorem 1.1.3 to local uniformization, by the method of Zariski [CP19, Section 4.1]. Volume 3, Chapter 4 explains the first step of this patching.
2. A reduction of local uniformization to equations of degree $p$ of two kinds: purely inseparable equations $X^p - f$ and Artin-Schreier equations [CP19, Proposition 4.10]. Chapter 2 of this volume gives this reduction.
3. An invariant $\iota(x) = (m(x), \omega(x), \kappa(x))$ of a point $x$ on such an equation, defined with the characteristic polyhedron of Hironaka [Hir67]. The invariant does not increase under permissible blowups [CP19, Theorem 3.13]. Chapter 3 of this volume defines the polyhedron and the first invariants.
4. A proof that, along a given valuation, a suitable sequence of permissible blowups makes $\iota$ drop. This is the Projection Theorem [CP19, Theorem 5.5], and the induction on $\iota$ gives [CP19, Theorem 1.5].

Part 4 is the long part. It fills Chapters 5 to 9 of [CP19], and we do not reproduce it. Chapter 4 of this volume explains where the dimension 3 is used.

**Theorem 1.2.6 (Cossart-Piltant).** Let $S$ be an excellent regular local ring of dimension 3 with residue field of characteristic $p > 0$, and let $K$ be its fraction field. Let $h = X^p + f_1 X^{p-1} + \dots + f_p \in S[X]$ be a reduced polynomial, let $X = \operatorname{Spec} S[X]/(h)$, let $L$ be the total ring of fractions of $S[X]/(h)$, and assume one of the two conditions.

1. $K$ has characteristic $p$ and $f_1 = \dots = f_{p-1} = 0$.
2. The group $G = \operatorname{Aut}_K(L)$ is cyclic of order $p$, and $X$ is $G$-invariant.

Let $\mu$ be a valuation of $L$ with center $\mathfrak{m}_S$ on $S$. Then there is a finite sequence of local blowups $(X, x_0) \leftarrow (X_1, x_1) \leftarrow \dots \leftarrow (X_r, x_r)$ in Hironaka-permissible centers, where $x_i$ is the center of $\mu$ on $X_i$, such that $X_r$ is regular at $x_r$.

Node: SG0000001F · Lean: `Singularity.localUniformization_three` (the statement only)

This is [CP19, Theorem 1.5], stated here in short form. The node SG0000001F is local uniformization of function fields of transcendence degree 3, and Theorem 1.2.6 is the main step of its proof, so we list the node here. The Lean statement is the statement of local uniformization, and it is not a statement of Theorem 1.2.6.

### Notes and references

The plan of Abhyankar and the five steps are from the introduction of [Cut09]. Section 3 of [Cut09] gives an outline of Steps 2 to 5, and Sections 4 to 11 give the proofs. The description of the plan of Cossart and Piltant follows the introduction and Section 4 of [CP19]. The earlier papers [CP08, CP09] follow the same plan for fields $k$ with $[k : k^p] < \infty$.
