---
title: Alterations of degree a power of the characteristic
nodes: [SG0000001N, SG0000001G]
sources: [Tem17, CP19, CP09, Lip78, ILO14, Tem13]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Alterations of degree a power of the characteristic

The theorem of Gabber removes one prime $\ell \ne p$ at a time from the degree. Temkin proved that all primes $\ell \ne p$ can be removed at once [Tem17]. In characteristic $p > 0$ the degree becomes a power of $p$. In characteristic 0 it becomes 1, so the theorem contains a resolution result. In this section we state the theorem, we explain the new idea of its proof, and we explain what it gives for the open problem.

### Definitions

**Definition 3.3.1.** Let $X$ be a scheme. The set $\operatorname{char}(X)$ is the set of primes $p$ such that $p = \operatorname{char} k(x)$ for some point $x \in X$. For a set $P$ of primes, a positive integer $n$ is a *$P$-number* if each prime divisor of $n$ lies in $P$. A *$P$-alteration* is an alteration whose degree is a $P$-number.

This is [Tem17, 1.2.1]. The number 1 is a $P$-number for each $P$, also for $P = \emptyset$. For a variety $X$ over a field of characteristic $p > 0$, $\operatorname{char}(X) = \{p\}$, and a $\operatorname{char}(X)$-alteration is an alteration whose degree is a power of $p$. For a variety over a field of characteristic 0, $\operatorname{char}(X) = \emptyset$, and a $\operatorname{char}(X)$-alteration is an alteration of degree 1, that is, a modification. For a scheme of finite type over $\mathbb{Z}$ with points in several characteristics, $\operatorname{char}(X)$ contains all these characteristics.

### The theorem of Temkin

**Theorem 3.3.2 (Temkin).** Let $X$ be a scheme with a nowhere dense closed subset $Z$, and assume that $X$ admits a morphism of finite type to a quasi-excellent scheme $S$ with $\dim S \le 3$. There is a projective $\operatorname{char}(X)$-alteration $b \colon X' \to X$ with $X'$ regular such that $b^{-1}(Z)$ is a strict normal crossings divisor. If $S = \operatorname{Spec} k$ with $k$ a perfect field, then $b$ can be chosen separable.

Lean: none yet

This is [Tem17, Theorem 1.2.5]. For non-integral $X$ Temkin uses a general notion of alteration [Tem17, Section 4.1.2], and he notes that the case of integral $X$ and $S$ is not essentially weaker [Tem17, 1.2.4]. The proof needs that each alteration of $S$ can be desingularized by a $\operatorname{char}(S)$-alteration [Tem17, 1.2.2]. For $\dim S \le 3$ this follows from the theorem of Cossart-Piltant on the resolution of quasi-excellent threefolds [CP19]. When [Tem17] appeared, that paper was a preprint, and Temkin remarks that the result rests on published work when $\dim S \le 2$, by [Lip78], or when $S$ is a threefold over a field of finite imperfection rank, by [CP09] [Tem17, Remarks 1.2.3 and 1.2.6]. The paper of Cossart-Piltant has since been published as [CP19]. For a variety over a field we can take $S = \operatorname{Spec} k$, with $\dim S = 0$, and only the trivial case of the base is needed.

**Corollary 3.3.3.** Let $X$ be an integral variety over a field $k$ of characteristic $p > 0$, and let $Z \subsetneq X$ be a proper closed subset. There is an alteration $\varphi \colon X_1 \to X$, with $X_1$ integral and regular and $\varphi$ projective, whose degree is a power of $p$, such that $\varphi^{-1}(Z)$ is a strict normal crossings divisor. If $k$ is perfect, then $\varphi$ can be chosen generically étale, and then $X_1$ is smooth over $k$.

Node: SG0000001N · Lean: `Singularity.exists_regular_p_alteration` (planned, no Lean statement yet)

*Proof.* Apply Theorem 3.3.2 with $S = \operatorname{Spec} k$. The set $Z$ is nowhere dense, because $X$ is irreducible and $Z \ne X$. Since $X$ is integral, we can take $X'$ integral [Tem17, 1.2.4], and we put $X_1 = X'$. Since $\operatorname{char}(X) = \{p\}$, the degree is a power of $p$. If $k$ is perfect, then $b$ is separable, so $k(X_1)/k(X)$ is separable, and $\varphi$ is generically étale by Lemma 1.1.5. A regular scheme of finite type over a perfect field is smooth over it. $\square$

The node SG0000001N states the corollary over a perfect field. The theorem gives the regular alteration of degree a power of $p$ over each field of characteristic $p$. The perfect field is needed only for separability and smoothness.

### The idea of the proof

The proof of Gabber uses the Sylow subgroups of a Galois group (Proposition 3.2.3). A Sylow subgroup removes one prime from the degree. To remove all primes $\ell \ne p$ at once, Temkin replaces the Sylow subgroup by a different subgroup, which comes from valuation theory.

Let $K$ be a field with a valuation of residue characteristic $p$, and let $L/K$ be a finite extension. In valuation theory the extension is *tame* if, roughly, it has no part of degree divisible by $p$ in the ramification. Wild ramification in valuation theory plays the role of inseparability in field theory. Proposition 3.1.1 splits a field extension, after an enlargement, as a purely inseparable extension followed by a Galois extension. Temkin proves an analogue for valued fields, which he calls *tame distillation*. Roughly, after an enlargement, a finite extension factors as a purely wild extension, whose degree is a power of $p$, followed by a tame extension. For a henselian valued field this goes back to a theorem of Pank [Tem17, 1.3.2]. Temkin globalizes it to alterations [Tem17, Theorem 3.3.6]: each alteration $Y \to X$ is dominated by a Galois alteration $Y' \to X$ that factors as a tame Galois alteration $Y' \to X''$ followed by a $\operatorname{char}(X)$-alteration $X'' \to X$ [Tem17, 1.3.4]. The definition of a tame Galois alteration uses the valuations of $k(Y')$ with center on $X$, and we do not give it here.

Roughly, the proof then follows the method of Gabber, with the subgroup that tame distillation gives in place of the Sylow subgroup [Tem17, 1.3.5]. The quotient by this subgroup is a $\operatorname{char}(X)$-alteration of $X$, and it has tame quotient singularities in a log smooth setting. The modification theorem of Gabber [ILO14, Exposé X, Theorem 1.1] resolves them by a modification, which does not change the degree. The main result of the paper [Tem17, Theorem 4.3.1] is a statement on morphisms, and Theorem 3.3.2 is one of its consequences.

Temkin states that the method loses the Galois property: the alteration $b$ of Theorem 3.3.2 is not shown to be Galois [Tem17, 1.2.1].

### What the theorem gives for the open problem

Let $X$ be a variety of dimension 4 over an algebraically closed field of characteristic $p > 0$. By Corollary 3.3.3 there is a regular alteration $X_1 \to X$ of degree $p^e$, generically étale. It does not give a resolution. There are three reasons.

1. The degree $p^e$ is not invertible in characteristic $p$, so the trace splitting of Proposition 1.3.2 fails. For coefficients in which $p$ is invertible, such as $\mathbb{Z}[1/p]$-modules, the trace argument works.
2. The alteration is not Galois. If it were Galois with a group $G$, then by Section 3.1 the variety $X$ would be birational to $X_1/G$ up to a purely inseparable map, with $|G|$ a power of $p$ in the generically étale case. So $G$ would be a $p$-group, and its action on $X_1$ would be wild. No known method resolves such wild quotients in dimension 4 in general.
3. A generically étale alteration of degree $p$ can be an Artin-Schreier covering, and its descent is the problem of resolving the quotient by a group of order $p$. This is the case that Volume 9 isolates.

So Temkin's theorem reduces the degree to its $p$-part, and the $p$-part is the open problem. Compare with the theorem of Temkin on inseparable local uniformization, Volume 3, Theorem 4.2.2 and [Tem13], in which the local problem is solved after a purely inseparable extension of the function field.

Node: SG0000001G · Lean: `Singularity.localUniformization_inseparable` (the statement only)

In the local theorem the extension is purely inseparable, and in Corollary 3.3.3 it is generically étale over a perfect field. Neither theorem alone gives local uniformization or resolution without an extension of the function field.

### Notes and references

The main source is the introduction and Section 3 of [Tem17]. The theorem in characteristic 0 is a weak form of the resolution of Hironaka, since it does not make the modification an isomorphism over the regular locus. The map has node SG0000001N for Corollary 3.3.3 and node SG0000001G for inseparable local uniformization. Only SG0000001G has a Lean statement, and it is not proved.
