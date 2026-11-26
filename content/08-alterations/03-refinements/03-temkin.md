---
title: Alterations of degree a power of the characteristic
nodes: [SG0000001N, SG0000001G]
sources: [Tem17, CP19, CP09, Lip78, ILO14, Tem13, AdJ97, Hir64]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Alterations of degree a power of the characteristic

The theorem of Gabber removes one prime $\ell \ne p$ at a time from the degree. Temkin proved that all primes $\ell \ne p$ can be removed at once [Tem17]. In characteristic $p > 0$ the degree becomes a power of $p$. In characteristic 0 it becomes 1, so the theorem gives a modification with regular source. This is a weak resolution, not a resolution in the sense of Volume 0, because the modification need not be an isomorphism over the regular locus. In this section we state the theorem, we explain the new idea of its proof, and we explain what it gives for the open problem.

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

We make the word *tame* precise in the simplest case. Let $(K, v)$ be a henselian valued field with residue field of characteristic $p$, and let $L/K$ be a finite extension, with the unique extension $w$ of $v$, ramification index $e$ and residue degree $f$. The extension is *tame* if $e$ is prime to $p$, the residue field extension is separable, and $[L : K] = ef$. The next example gives a tame extension and a wild one of the same base field.

**Example 3.3.4 (Kummer and Artin-Schreier).** Let $k$ be an algebraically closed field of characteristic $p > 0$, let $K = k((t))$, and let $v$ be the $t$-adic valuation, with $v(t) = 1$. It is complete, hence henselian, and its residue field is $k$. So $f = 1$ for each finite extension.

Let $n \ge 2$ be prime to $p$, and let $L = K(s)$ with $s^n = t$. Then $n w(s) = 1$, so the value group of $w$ contains $\frac{1}{n}\mathbb{Z}$, and $e \ge n$. Volume 3, Corollary 2.1.3 gives $ef \le [L : K] \le n$. So $e = [L : K] = n$. The degree $n$ is prime to $p$, so $L/K$ is tame. The field $k$ contains the $n$-th roots of unity, because $n$ is prime to $p$, so $L/K$ is Galois with a cyclic group of order $n$.

Let $L = K(y)$ with $y^p - y = t^{-1}$. If $w(y) \ge 0$, then $w(y^p - y) \ge 0$, but $v(t^{-1}) = -1$. So $w(y) < 0$, and $w(y^p) = p w(y) < w(y)$. Then $w(y^p - y) = p w(y)$, so $w(y) = -1/p$ and $e \ge p$. As before, $e = [L : K] = p$. The roots of $T^p - T - t^{-1}$ are $y + i$ for $i \in \mathbb{F}_p$, so $L/K$ is Galois with group $\mathbb{Z}/p$, generated by $y \mapsto y + 1$. The polynomial is separable, because its derivative is $-1$. But $e = p$, so $L/K$ is not tame. It is *wild*: separable, but with the ramification of an inseparable extension. In tame distillation such an extension is part of the purely wild factor, whose degree is a power of $p$.

The two cases behave differently under the methods of Sections 3.1 and 3.2. The tame extension has a group of order prime to $p$, and the Reynolds operator of Lemma 3.1.8 exists. The wild extension has the group $\mathbb{Z}/p$, and $p = 0$ in $k$. Example 3.1.9 is a global form of the second case.

Roughly, the proof then follows the method of Gabber, with the subgroup that tame distillation gives in place of the Sylow subgroup [Tem17, 1.3.5]. The quotient by this subgroup is a $\operatorname{char}(X)$-alteration of $X$, and it has tame quotient singularities in a log smooth setting. The modification theorem of Gabber [ILO14, Exposé X, Theorem 1.1] resolves them by a modification, which does not change the degree. The main result of the paper [Tem17, Theorem 4.3.1] is a statement on morphisms, and Theorem 3.3.2 is one of its consequences.

Temkin states that the method loses the Galois property: the alteration $b$ of Theorem 3.3.2 is not shown to be Galois [Tem17, 1.2.1].

### What the theorem gives for the open problem

Let $X$ be a variety of dimension 4 over an algebraically closed field of characteristic $p > 0$. By Corollary 3.3.3 there is a regular alteration $X_1 \to X$ of degree $p^e$, generically étale. It does not give a resolution. There are three reasons.

1. The degree $p^e$ is not invertible in characteristic $p$, so the trace splitting of Proposition 1.3.2 fails. For coefficients in which $p$ is invertible, such as $\mathbb{Z}[1/p]$-modules, the trace argument works.
2. The alteration is not Galois. If it were Galois with a group $G$, then by Section 3.1 the variety $X$ would be birational to $X_1/G$ up to a purely inseparable map, with $|G|$ a power of $p$ in the generically étale case. So $G$ would be a $p$-group, and its action on $X_1$ would be wild. No known method resolves such wild quotients in dimension 4 in general.
3. A generically étale alteration of degree $p$ can be an Artin-Schreier covering, as in Example 3.3.4, and its descent is the problem of resolving the quotient by a group of order $p$. This is the case that Volume 9 isolates.

So Temkin's theorem reduces the degree to its $p$-part, and the $p$-part is the open problem. Compare with the theorem of Temkin on inseparable local uniformization, Volume 3, Theorem 4.2.2 and [Tem13], in which the local problem is solved after a purely inseparable extension of the function field.

Node: SG0000001G · Lean: `Singularity.localUniformization_inseparable` (the statement only)

In the local theorem the extension is purely inseparable, and in Corollary 3.3.3 it is generically étale over a perfect field. Neither theorem alone gives local uniformization or resolution without an extension of the function field.

### Desingularization of morphisms

The main theorem of [Tem17] is a statement on morphisms. We state it for completeness. A morphism of schemes is *maximally dominating* if it maps each generic point of an irreducible component to a generic point of an irreducible component [Tem17, 1.2.8]. For the notion of a log smooth morphism of pairs we refer to [Tem17, 1.2.7]. If $X$ and $Y$ are regular and $Z \subseteq X$ and $T \subseteq Y$ are divisors with strict normal crossings, a log smooth morphism $(X, Z) \to (Y, T)$ is locally, up to a smooth morphism, a monomial map between the coordinates that define $Z$ and $T$, with a condition on the orders of the kernel and the cokernel of the matrix of exponents.

**Theorem 3.3.5 (Temkin, desingularization of morphisms).** Let $f \colon X \to S$ be a maximally dominating morphism of finite type, let $Z \subseteq X$ be a nowhere dense closed subset, and assume that $X$ is separated and that $S$ admits a morphism of finite type to a Noetherian quasi-excellent scheme of dimension at most 3.

1. There are projective $\operatorname{char}(S)$-alterations $a \colon S' \to S$ and $b \colon X' \to X$ with $S'$ and $X'$ regular, a quasi-projective morphism $f' \colon X' \to S'$ with $f \circ b = a \circ f'$, and divisors $W' \subseteq S'$ and $Z' \subseteq X'$ with strict normal crossings, such that $Z' = b^{-1}(Z) \cup f'^{-1}(W')$ and the morphism $(X', Z') \to (S', W')$ is log smooth.
2. If $S = \operatorname{Spec} k$ with $k$ a perfect field, then one can choose in addition $a$ to be an isomorphism and $b$ to be separable.

Lean: none yet

This is [Tem17, Theorem 1.2.9]. As for Theorem 3.3.2, the case of a general quasi-excellent threefold uses the work of Cossart-Piltant [CP19], and the published results of [Lip78] and [CP09] cover the case $\dim S \le 2$ and the case of a threefold over a field of finite imperfection rank [Tem17, Remark 1.2.6]. For $S = \operatorname{Spec} k$ with $k$ perfect, the divisor $W'$ is empty, so $Z' = b^{-1}(Z)$, and part 2 gives Theorem 3.3.2 for separated $X$ over a perfect field. Temkin proves a more general form, without the separatedness of $X$, in [Tem17, Theorem 4.3.1]. The theorem is the analogue for $\operatorname{char}(S)$-alterations of the semistable form of the theorem of de Jong (Theorem 1.2.5 and Theorem 3.2.7): the morphism $f'$ is not semistable, but it is log smooth, and log smooth morphisms are the toroidal morphisms of the theory of Abramovich and de Jong [AdJ97]. For a variety over a field of characteristic 0 and $S = \operatorname{Spec} k$, part 2 gives a modification $b$ with $X'$ regular, because $\operatorname{char}(S) = \emptyset$.

### Why the refinements do not give resolution

We collect the reasons why the theorems of Gabber and Temkin, even together, do not give resolution of singularities in characteristic $p > 0$. Let $X$ be an integral variety of dimension $d$ over an algebraically closed field of characteristic $p$.

1. In characteristic $p$ the degree can only be made a power of $p$, by Corollary 3.3.3, and prime to a given $\ell \ne p$, by Corollary 3.2.5. Neither theorem makes the degree 1. An alteration of degree $p^e$ with $e \ge 1$ is not a resolution, by Lemma 1.1.15, part 2.
2. The theorem of Temkin does not give a Galois alteration [Tem17, 1.2.1]. So the theorem does not write $X$ as a quotient of a regular variety up to a modification.
3. If a Galois alteration of degree $p^e$ is given, then $X$ is birational to the quotient by a $p$-group, up to a purely inseparable map (Section 3.1). The action of a $p$-group in characteristic $p$ is wild, and the tame methods of Gabber (Section 3.2) do not apply to it. No known method resolves these quotients in dimension at least 4.
4. In the proofs of Gabber and Temkin the tame quotient singularities are resolved by the modification theorem of Gabber [ILO14, Exposé X, Theorem 1.1]. Its proof uses the theory of log regular schemes and canonical desingularization in characteristic 0 [ILO14, Introduction]. It applies to tame actions on log regular schemes, for example on regular schemes. It gives no information on wild quotients.
5. A regular alteration of degree $p^e$ is useful for the cohomology with coefficients in which $p$ is invertible: by the hypercovering argument of Section 1.3, and, when the alteration is finite locally free, by the trace of Proposition 1.3.8. A regular alteration is in general not finite, so Proposition 1.3.8 does not apply to it directly. For coherent cohomology and for $p$-adic cohomology it gives much less, because the trace is multiplication by $p^e$, which is 0 in characteristic $p$. A resolution would give both. This is the reason why the theorems of this chapter are not a substitute for resolution in the applications of Section 1.3.

In characteristic 0 the situation is different. There $\operatorname{char}(X) = \emptyset$, so the theorem of Temkin gives a modification $X' \to X$ with $X'$ regular. This is a weak resolution: the theorem does not say that the modification is an isomorphism over the regular locus of $X$, and it does not say that it is a composition of blowups in regular centers. Weak resolution in characteristic 0 was first obtained by the methods of alterations by Abramovich and de Jong [AdJ97], and resolution in characteristic 0 is the theorem of Hironaka [Hir64].

In characteristic $p$ resolution is known in dimension at most 3 (Volume 9, and Cossart-Piltant [CP09, CP19]), and in dimension at least 4 it is open. The theorems of this volume do not prove it, and nothing in this volume should be read as a proof of it.

### Notes and references

The main source is the introduction and Section 3 of [Tem17]. The theorem in characteristic 0 is a weak form of the resolution of Hironaka, since it does not make the modification an isomorphism over the regular locus. The map has node SG0000001N for Corollary 3.3.3 and node SG0000001G for inseparable local uniformization. Only SG0000001G has a Lean statement, and it is not proved.
