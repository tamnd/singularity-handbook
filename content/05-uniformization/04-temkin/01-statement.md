---
title: The theorem of Temkin
nodes: [SG0000001G, SG0000000X, SG00000010, SG0000001E]
sources: [Tem13, Eis95, Stacks, KK05]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem of Temkin

### The statement

Temkin writes $K^\circ$ for a valuation ring of $K$. Let $k$ be a field and $K/k$ a function field. An *affine $k$-model* of $K$ is $X = \operatorname{Spec} A$, where $A \subseteq K$ is a finitely generated $k$-algebra with fraction field $K$. It is a model of $K^\circ$ if $K^\circ$ is centered on $X$, that is, $A \subseteq K^\circ$. An affine model $X' = \operatorname{Spec} A'$ *refines* $X = \operatorname{Spec} A$ if $A \subseteq A'$. For a finite extension $L/K$, the *$L$-normalization* $\operatorname{Nr}_L(X')$ is $\operatorname{Spec} B$, where $B$ is the integral closure of $A'$ in $L$. For a field extension $l/k$, $lK$ is the compositum in an algebraic closure of $K$.

**Theorem 4.1.1 (Temkin).** Let $K/k$ be a finitely generated field extension, $K^\circ$ a valuation ring of $K$ containing $k$ and $X$ an affine $k$-model of $K^\circ$. Then there exist finite purely inseparable extensions $l/k$ and $L/lK$ and an affine model $X'$ of $K^\circ$ such that $X'$ refines $X$ and the unique extension of $K^\circ$ to a valuation ring of $L$ is centered on a simple $l$-smooth point of the $L$-normalization $\operatorname{Nr}_L(X')$.

Node: SG0000001G · Lean: `Singularity.localUniformization_inseparable` (the statement only)

This is [Tem13, Theorem 1.3.2], quoted with the notation of that paper. Here $l$-smooth means smooth over $l$, and a smooth point is *simple* if its residue field is separable over $l$ [Tem13]. The extension of $K^\circ$ to $L$ is unique because $L/K$ is purely inseparable (Volume 3, Section 4.2). Volume 3, Theorem 4.2.2, and Volume 9, Theorem 2.3.4, state the theorem in a short form. Temkin also deduces a global form, with a finite covering of the Zariski-Riemann space, from the quasi-compactness of that space [Tem13]. Quasi-compactness is node SG0000000X, with the Lean proof `Singularity.ZariskiRiemann.compactSpace`.

### The Lean form

The Lean statement takes a finite subset first. It says: for each valuation $v$ of $K/k$ and each finite subset $S \subseteq \mathcal{O}_v$, there are a finite purely inseparable extension $L/K$, an extension $w$ of $v$ to $L$, and an affine model $B$ of $L/k$ with $S \subseteq B \subseteq \mathcal{O}_w$ such that the local ring of $B$ at the center of $w$ is regular.

**Proposition 4.1.2.** Theorem 4.1.1 implies the Lean form.

Lean: none yet

*Proof.* Let $v$ and $S$ be given. Write $K = k(a_1, \dots, a_m)$. After we replace $a_i$ by $a_i^{-1}$ when $a_i \notin \mathcal{O}_v$, all $a_i$ lie in $\mathcal{O}_v$. Let $A = k[S, a_1, \dots, a_m]$. Then $A \subseteq \mathcal{O}_v$, and $X = \operatorname{Spec} A$ is an affine $k$-model of $\mathcal{O}_v$.

Theorem 4.1.1 gives $l$, $L$ and $X' = \operatorname{Spec} A'$ with $A \subseteq A' \subseteq \mathcal{O}_v$. The extension $lK/K$ is finite and purely inseparable, because $l/k$ is, and so $L/K$ is finite and purely inseparable. Let $w$ be the extension of $v$ to $L$, and let $B$ be the integral closure of $A'$ in $L$. Since $A'$ is a finitely generated algebra over a field and $L/K$ is finite, $B$ is a finite $A'$-module [Eis95, Corollary 13.13]. So $B$ is a finitely generated $k$-algebra. Its fraction field is $L$, because each element of $L$ is a quotient of an element integral over $A'$ by a nonzero element of $A'$. Since $\mathcal{O}_w$ is integrally closed and contains $A'$, we have $B \subseteq \mathcal{O}_w$. So $B$ is an affine model of $L/k$ with $S \subseteq A \subseteq B \subseteq \mathcal{O}_w$.

By Theorem 4.1.1, the center $\mathfrak{q} = \mathfrak{m}_w \cap B$ is a point of $\operatorname{Spec} B$ that is smooth over $l$. The local ring of a scheme smooth over a field at a point is regular [Stacks]. So $B_\mathfrak{q}$ is regular. $\square$

**Corollary 4.1.3.** Theorem 4.1.1 implies Theorem 1.4.1, the theorem of Zariski.

Lean: none yet

*Proof.* Let $k$ have characteristic 0. Each finite purely inseparable extension of a field of characteristic 0 is trivial. So in the proof of Proposition 4.1.2 we have $L = K$ and $w = v$, and $B$ is an affine model of $K/k$ with $S \subseteq B \subseteq \mathcal{O}_v$ and a regular center. By Volume 3, Proposition 4.1.6, $v$ has local uniformization. $\square$

The same argument shows that Theorem 4.1.1 gives local uniformization of $v$ whenever the fields $l$ and $L$ that it produces are trivial, for example when $k$ is perfect and $L = K$.

### The structure of the proof

We describe the structure of the proof of [Tem13], following the overview in [Tem13, Section 1.5]. We give no details.

1. Height reduction. The rank of a valuation is also called its height. Temkin reduces the theorem to valuations of height one.
2. Induction on the dimension by curves. Temkin writes the function field as a function field of one variable over a subfield of smaller transcendence degree, and he studies the valuation on this field of one variable over a valued field. The tools are the geometry of curves over valued fields, in the form of Berkovich or adic spaces, and a study of special points of such curves.
3. The case of height one. Here Temkin uses an induction on the transcendence defect, that is, on the difference between the two sides of the Abhyankar inequality. The base of the induction is the Abhyankar case. For it Temkin gives a proof of local uniformization in the separable case, which recovers the theorem of Knaf-Kuhlmann [KK05] (Theorem 2.2.1).
4. Henselization. Temkin names as the main difficulty that the valued fields in the induction are not henselian. The defect (node SG00000010) is defined through the henselization, so this is where the defect of Chapter 3 enters.

The method is local. It produces one model for each valuation and each finite set, and it does not give a resolution. In Section 4.2 we explain what is missing.

### Notes and references

The theorem is [Tem13, Theorem 1.3.2]. Proposition 4.1.2 and Corollary 4.1.3 are not in the Lean library. The Lean statement is in `Singularity/Statements/LocalUniformization.lean`, and it is not proved.
