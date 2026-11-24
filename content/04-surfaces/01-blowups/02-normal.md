---
title: Normal surfaces
nodes: [SG0000000M]
sources: [Mat, EGA4-7, Stacks, Har, Liu, AM69]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Normal surfaces

The process of Lipman alternates the normalization and the blowup of the singular points. For this process to make sense we need two facts. The normalization must be a finite morphism, so that it keeps us among Noetherian schemes of finite type over the old one. And a normal surface must have only finitely many singular points, so that the center of each blowup is a finite set of closed points. This section proves both facts for excellent surfaces.

### Surfaces and normalization

**Definition 1.2.1.** In this volume a *surface* is a Noetherian scheme $X$ with $\dim X \le 2$. The surface is *excellent* if it is locally excellent in the sense of Definition 5.3.1 of Volume 1. A Noetherian scheme $X$ is *normal* if each local ring $\mathcal{O}_{X,x}$ is an integrally closed domain. Let $X$ be a reduced Noetherian scheme with irreducible components $X_1, \dots, X_s$, each with its reduced structure. The *normalization* of an integral $X_i$ with function field $K_i$ is the affine morphism $X_i^\nu \to X_i$ given by the integral closure of $\mathcal{O}_{X_i}$ in $K_i$. The *normalization* of $X$ is $\nu : X^\nu = \coprod_i X_i^\nu \to X$.

Lean: none yet

A Noetherian normal scheme is the disjoint union of its connected components, and each component is integral. The normalization $X^\nu$ is normal. Over an affine open $\operatorname{Spec} R$ of an integral $X_i$, it is $\operatorname{Spec} R'$, where $R'$ is the integral closure of $R$ in $K_i$ [Stacks].

**Theorem 1.2.2.** Let $X$ be a reduced Noetherian scheme.

1. If $X$ is of finite type over a field, then $\nu : X^\nu \to X$ is finite.
2. If $X$ is excellent, then $\nu$ is finite, $X^\nu$ is a normal excellent scheme, and $\dim X^\nu = \dim X$.

Node: SG0000000M · Lean: `Singularity.Algebra.finite_integralClosure` (part 1, for an affine domain)

*Proof.* 1. The question is local on $X$ and we may treat each component. Thus let $R$ be a domain of finite type over a field. By the theorem of E. Noether (Theorem 2.4.7 of Volume 1), the integral closure of $R$ in its field of fractions is a finite $R$-module.

2. An excellent ring is a Nagata ring, that is, for each prime $\mathfrak{p}$ of $R$ and each finite extension $L$ of $\kappa(\mathfrak{p})$, the integral closure of $R/\mathfrak{p}$ in $L$ is finite over $R/\mathfrak{p}$ [EGA4-7, Section 7.8], [Stacks]. Apply this with $L = \kappa(\mathfrak{p})$ for the minimal primes $\mathfrak{p}$ of $R$. This gives the finiteness. A finite $R$-algebra is of finite type, so it is excellent by Theorem 5.2.8 of Volume 1. For the dimension, let $R \subseteq R'$ be an integral extension. By the going up theorem [AM69, Theorem 5.11], each chain of primes of $R$ lifts to a chain of $R'$. By incomparability [AM69, Corollary 5.9], each chain of $R'$ contracts to a chain of $R$ of the same length. Thus $\dim R' = \dim R$. $\square$

For a Noetherian ring that is not excellent, the normalization can fail to be finite. Section 2.2 explains why such a ring has no resolution.

### The singular points

**Lemma 1.2.3.** Let $X$ be a Noetherian scheme with $\dim X \le 2$, and let $Z \subseteq X$ be a closed subset such that $\dim \mathcal{O}_{X,z} = 2$ for each $z \in Z$. Then $Z$ is a finite set of closed points.

Lean: none yet

*Proof.* The space $Z$ is Noetherian, so it has finitely many irreducible components. Let $z_1, \dots, z_s$ be their generic points. Let $z \in Z$. Then $z$ lies in the closure of some $z_i$. Assume that $z \ne z_i$. Then $z_i$ corresponds to a prime $\mathfrak{p}$ of $\mathcal{O}_{X,z}$ that is not maximal, and $\mathcal{O}_{X,z_i} = (\mathcal{O}_{X,z})_\mathfrak{p}$. A chain of primes of length 2 in $(\mathcal{O}_{X,z})_\mathfrak{p}$ ends at $\mathfrak{p}$. If we add the maximal ideal, we get a chain of length 3 in $\mathcal{O}_{X,z}$. Thus $\dim \mathcal{O}_{X,z} \ge 3$. This is false, since $\dim \mathcal{O}_{X,z} \le \dim X \le 2$. Thus $z = z_i$, and $Z = \{z_1, \dots, z_s\}$. The closure of $z_i$ is in $Z$, and by the argument each of its points is $z_i$. Thus $z_i$ is a closed point. $\square$

**Theorem 1.2.4.** Let $X$ be a normal Noetherian scheme with $\dim X \le 2$, and assume that $\operatorname{Reg}(X)$ is open. Then $\operatorname{Sing}(X) = X \setminus \operatorname{Reg}(X)$ is a finite set of closed points, and $\dim \mathcal{O}_{X,x} = 2$ for each $x \in \operatorname{Sing}(X)$. This holds in particular for each normal excellent surface.

Lean: none yet

*Proof.* Let $x \in X$ with $\dim \mathcal{O}_{X,x} \le 1$. If the dimension is 0, then $\mathcal{O}_{X,x}$ is a local domain of dimension 0, that is, a field, and it is regular. If the dimension is 1, then $\mathcal{O}_{X,x}$ is an integrally closed Noetherian local domain of dimension 1, and it is regular by Theorem 1.4.2 of Volume 1. Thus each $x \in \operatorname{Sing}(X)$ has $\dim \mathcal{O}_{X,x} = 2$. The set $\operatorname{Sing}(X)$ is closed by assumption. Lemma 1.2.3 gives the result. For an excellent $X$, the set $\operatorname{Reg}(X)$ is open by Proposition 5.3.2 of Volume 1. $\square$

The theorem fails in dimension 3. The threefold $V(xy - z^2) \subseteq \mathbb{A}^4_k$, with coordinates $x, y, z, w$, is normal by the criterion of Serre, but it is singular along the line $x = y = z = 0$.

### One round of the process

**Corollary 1.2.5.** Let $X$ be a normal excellent surface and let $S = \operatorname{Sing}(X)$ with its reduced structure. Let $X_1$ be the normalization of $\operatorname{Bl}_S X$. Then $X_1$ is a normal excellent surface, the morphism $X_1 \to X$ is proper, and it is an isomorphism over $\operatorname{Reg}(X) = X \setminus S$.

Lean: none yet

*Proof.* By Theorem 1.2.4, $S$ is a finite set of closed points. The morphism $\operatorname{Bl}_S X \to X$ is projective, so it is proper and of finite type. We may work on one connected component of $X$, so we may assume that $X$ is integral. If $S = \emptyset$, there is nothing to prove. Otherwise $S \ne X$, because a point of a normal scheme with $\dim \mathcal{O}_{X,x} = 0$ is regular. By the remark after Lemma 1.1.3, $\operatorname{Bl}_S X$ is integral, and each chart over an affine open $\operatorname{Spec} R$ is a ring $B$ with $R \subseteq B \subseteq K$, where $K$ is the function field.

The scheme $\operatorname{Bl}_S X$ is of finite type over $X$, so it is excellent by Theorem 5.2.8 of Volume 1. For the dimension, let $P$ be a prime of a chart $B$ and let $\mathfrak{p} = P \cap R$. The dimension inequality [Mat, Theorem 15.5] gives $\operatorname{ht} P + \operatorname{tr.deg}_{\kappa(\mathfrak{p})} \kappa(P) \le \operatorname{ht} \mathfrak{p} + \operatorname{tr.deg}_R B$. Here $\operatorname{tr.deg}_R B = 0$, since $B \subseteq K$. Thus $\operatorname{ht} P \le \operatorname{ht} \mathfrak{p} \le 2$, and $\dim \operatorname{Bl}_S X \le 2$.

By Theorem 1.2.2, $X_1 \to \operatorname{Bl}_S X$ is finite, $X_1$ is normal and excellent, and $\dim X_1 \le 2$. The composite $X_1 \to X$ of a finite and a proper morphism is proper. Over $X \setminus S$ the blowup is an isomorphism by Theorem 1.1.2, and $X \setminus S$ is normal, so the normalization does not change it. $\square$

### Normal hypersurfaces

The examples of this volume are surfaces in $\mathbb{A}^3_k$. The next lemma shows that such a surface is normal when its singular points are isolated.

**Lemma 1.2.6.** Let $k$ be a field, let $F \in k[x, y, z]$ be a nonconstant polynomial, and let $X = V(F) \subseteq \mathbb{A}^3_k$. Assume that $\operatorname{Sing}(X)$ is a finite set of closed points. Then $X$ is normal.

Lean: none yet

*Proof.* Let $P = k[x, y, z]$ and $A = P/(F)$. We use the criterion of Serre: a Noetherian ring is normal if and only if it satisfies $R_1$ and $S_2$ [Mat, Theorem 23.8].

*The condition $S_2$.* Let $\mathfrak{q}$ be a prime of $P$ that contains $F$. The ring $P_\mathfrak{q}$ is regular, so it is Cohen-Macaulay, and $F$ is a nonzerodivisor of $P_\mathfrak{q}$. Thus $A_{\mathfrak{q}} = P_\mathfrak{q}/(F)$ is Cohen-Macaulay [Mat, Section 17]. A Cohen-Macaulay ring satisfies $S_n$ for each $n$.

*The condition $R_1$.* Let $\mathfrak{m}$ be a maximal ideal of $P$ that contains $F$. Then $\dim P_\mathfrak{m} = 3$ [Har, Theorem I.1.8A], and $\dim A_\mathfrak{m} = 2$, since $F$ is a nonzerodivisor of $P_\mathfrak{m}$ [AM69, Corollary 11.18]. Thus each closed point of $X$ has a local ring of dimension 2. Let $\mathfrak{p}$ be a prime of $A$ with $\dim A_\mathfrak{p} \le 1$. Then $\mathfrak{p}$ is not a closed point, so $\mathfrak{p} \notin \operatorname{Sing}(X)$, and $A_\mathfrak{p}$ is regular. Thus $A$ satisfies $R_1$. $\square$

The finite set of the lemma is often easy to check. By the Jacobian criterion (Corollary 1.8.3 of Volume 1), applied to the regular ring $k[x, y, z]$ and the derivations $\partial/\partial x$, $\partial/\partial y$, $\partial/\partial z$, each prime of $A$ that does not contain all three partial derivatives of $F$ is in $\operatorname{Reg}(X)$. Section 2.3 uses this together with Lemma 2.3.1.

### Notes and references

Serre's criterion is [Mat, Theorem 23.8]. The finiteness of the normalization of an excellent ring is in [EGA4-7, Section 7.8] and in [Stacks]. For a surface over a field, Theorem 1.2.4 and Corollary 1.2.5 are in [Liu, Chapter 8] and in [Stacks]. The proof of Theorem 1.2.4 shows that a normal Noetherian scheme is regular in codimension 1, so its singular locus has codimension at least 2. For surfaces this means that the singular locus is a finite set of closed points.
