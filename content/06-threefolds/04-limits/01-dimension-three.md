---
title: Where the proof uses dimension three
nodes: [SG0000001V, SG0000001F, SG0000001C]
sources: [CP19, CP14, CJS20, Hir67, Abh56]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Where the proof uses dimension three

Cossart and Piltant write the first three chapters of [CP19] for a regular local ring $S$ of arbitrary dimension $n$. From Chapter 4 on they assume $n = 3$. In this section we list the results of Chapter 3 of this volume that hold for each $n$, and the places where the proof of Theorem 1.2.6 uses $n = 3$. We end with an example of Cossart and Piltant in dimension $n = 4$ that shows a new phenomenon.

### What holds in each dimension

Let $S$ be an excellent regular local ring of dimension $n \ge 1$, and let $h \in S[X]$ be monic of degree $p$ and satisfy condition 1 or condition 2 of Theorem 1.2.6. These results of Chapter 3 hold for each $n$.

1. The theorem of Hironaka on the characteristic polyhedron, Theorem 3.1.5.
2. The definitions of $\delta$, $d_j$, $\epsilon$, $\omega$ and $\iota$ (Section 3.2), and Propositions 3.2.2 and 3.2.4. Our proofs of these propositions do not use $n = 3$.
3. Under condition (E), at a point with $m = p$ and $\omega > 0$, the invariant $\iota$ does not increase under permissible blowups, Theorem 3.2.6.
4. If $\omega(x) = 0$, then Hironaka-permissible blowups along a valuation make the multiplicity less than $p$, Theorem 3.2.7.

[CP19] proves more in each dimension: permissibility is stable under regular base change [CP19, Theorem 3.8], and a Hironaka-permissible center is permissible on a dense open subset [CP19, Theorem 3.22]. Cossart and Piltant describe the results of [CP19, Section 3.3], which contains Theorem 3.22, as a guideline for $n \ge 4$ [CP19, Remark 1.7].

So in each dimension the main invariant does not go up. The missing part is a proof that it goes down. For $n = 3$ this is the Projection Theorem [CP19, Theorem 5.5], which we state as Theorem 3.2.11, and its proof fills Chapters 6 to 9 of [CP19].

### The uses of dimension three

We list the places where [CP19] uses $n = 3$. The list follows the remarks of Cossart and Piltant in [CP19, Section 1] and at the places that we cite.

*The reduction.* The reduction of Section 2.2 uses three theorems on regular schemes of dimension 2 and 3 [CP19, Propositions 4.2 to 4.4]: a theorem of Abhyankar that a regular local ring of dimension 2 that dominates another one with the same fraction field is an iterated quadratic transform of it [Abh56], the embedded resolution of a reduced subscheme of an excellent regular scheme of dimension 3 [CJS20], and the principalization of ideals on such a scheme by blowups in regular centers. With these theorems Cossart and Piltant also reach condition (E) [CP19, Corollary 4.19]. In dimension 4 one would need the embedded resolution of threefolds in regular schemes of dimension 4, which is open in characteristic $p$ (Volume 9, Section 2.1).

Node: SG0000001C · Lean: `Singularity.EmbeddedResolutionSurface` (the statement only)

*Small multiplicity.* After the multiplicity has dropped below $p$, one still has to reach a regular point. For $n = 3$ this is [CP14]. Cossart and Piltant call this step relatively easy [CP19, Section 1]. The paper [CP14] is written for $n = 3$.

*The projection.* For $n = 3$ and $\omega(x) > 0$, Cossart and Piltant refine $\kappa(x)$ to a number in $\{2, 3, 4\}$ [CP19, Definition 5.1]. They write that, in contrast with residue characteristic 0, there is no obvious way to attach to $(S, h, E)$ a projected structure of dimension two: there is "no reasonable notion of maximal contact" [CP19, Section 1]. Example 2.3.5 of Narasimhan shows that no regular hypersurface can play this role (Section 1.2). Their method projects only the polyhedron. With well adapted coordinates $(u_1, u_2, u_3; Z)$, a linear projection maps $\Delta(h; u_1, u_2, v; Z) \subseteq \mathbb{R}^3$ to a polygon $\Delta_2(h; u_1, u_2; v; Z) \subseteq \mathbb{R}^2$, where $v = u_3 - \varphi_2$ is chosen to make the polygon minimal [CP19, (1.5)]. New invariants of the polygon control the blowups. In dimension 4 the polyhedron lies in $\mathbb{R}^4$, and [CP19] does not say how to project it or which invariants of the image to use. Volume 9, Section 2.3, lists this as the missing step of the route of characteristic polyhedra.

*The structure of the Projection Theorem.* Cossart and Piltant describe the proof of Theorem 3.2.11 in four steps [CP19, Section 1]. First, $\iota(x)$ is read off from the initial form $\operatorname{in} h$ on the initial face of the characteristic polyhedron. Second, permissible blowups give either a smaller $\iota$, or a point $x'$ with the same $(m, \omega)$ at which $\operatorname{in} h'$ has a *monic form*. A monic form is one in which a certain monomial that computes $\omega$ occurs, and it corresponds to a vertex $v'$ of the polyhedron. Third, the projection (1.5) of [CP19] from $v'$ gives a polygon, and Cossart and Piltant attach to it a number $\gamma(x') \in \mathbb{N}$ [CP19, Theorem 7.18 and Definition 7.19]. Fourth, more Hironaka-permissible blowups give either a smaller $\iota$, or the same $\iota$ with a monic form and a smaller $\gamma$. Since $\gamma \in \mathbb{N}$, the second case can occur only finitely many times. For $\kappa(x) = 2$ the algorithm blows up curves only when $\gamma(x) \in \{0, 1\}$, and it reaches a point $x'$ with $\iota(x') \le (p, \omega(x), 1)$ [CP19, Theorem 7.26].

The proof splits by the value of $\kappa(x)$: Corollary 6.4 of [CP19] treats $\kappa(x) = 1$, Theorem 7.26 treats $\kappa(x) = 2$, and Theorem 9.6 treats $\kappa(x) = 3, 4$. Chapter 6 uses centers in the strict transforms of a fixed component of $E$. Its proof is similar to the resolution of excellent surfaces [Hir67], but it does not follow from it. Cossart and Piltant name three phenomena that make the proof long [CP19, Section 1]. First, except for $\kappa(x) = 1$ and in part for $\kappa(x) = 3, 4$, there is no obvious way to reduce the theorem to a statement on the coefficients of $h$. Second, the reduction to the monic forms is a case analysis [CP19, Sections 7.2 and 8.3]. Third, the blowup of a monic form with $\kappa(x) = 2$ or $3$ in a permissible center, for example a closed point, can give $\iota(x') = (p, \omega(x), 4) > \iota(x)$. This is why $\kappa$ can go up along the sequences of Section 3.2, and it is again treated by a case analysis [CP19, Section 7.1]. Cossart and Piltant write that an extension of these case analyses to higher dimensions seems out of reach [CP19, Section 1]. When Theorem 3.2.11 is known, Theorem 1.2.6 follows from the induction of Proposition 3.2.12.

*The directrix.* The proof compares the directrix $\mathrm{Dir}(x)$ and the closed Hilbert-Samuel stratum $\mathrm{Max}(x)$ of a cone attached to the initial form. By a theorem of Hironaka they are equal if the residue field is perfect or if the cone lies in a space of dimension at most $p + 1$ [CP19, Proposition 2.55]. For $n = 3$ the space has dimension 4, so equality fails only for $p = 2$, an imperfect residue field and one special form of $\operatorname{in} h$, which [CP19, Remark 2.56 and Proposition 5.8] treats. For $n = 4$ the space has dimension 5, which is more than $p + 1$ for $p = 2$ and $p = 3$. In this range the theorem of Hironaka does not give the equality for imperfect residue fields, and cones with $\mathrm{Dir} \ne \mathrm{Max}$ exist [CP19, Remark 2.56].

*Formal arcs.* Let $\varphi$ be a formal arc on $X$ through $x$ with $m = p$ and $\omega > 0$ along the arc. Cossart and Piltant prove, under an assumption on the residue fields, that one of two things happens [CP19, Proposition 3.17]. Either the Zariski closure of the arc is permissible of the first kind at all the centers of the arc after some step of the point blowups along the arc, or finitely many permissible blowups in other centers lead to a situation in which the closure is permissible of the second kind or $\omega = 0$. For $n = 3$ the assumption on the residue fields follows from $m = p$ and $\omega > 0$. For $n \ge 4$ it is not known whether the conclusion holds without it [CP19, Remark 3.19]. Example 4.1.1 below shows that for $n = 4$ the first alternative can fail: the closure of an arc need not become permissible under the point blowups along the arc. For $n = 3$ this happens only for $\omega(x) = 1$, and it is then easy to treat [CP19, Remark 1.8].

*Curves of a third kind.* Chapter 9 of [CP19] blows up Hironaka-permissible curves that are neither of the first nor of the second kind. To make them Hironaka-permissible it uses a stronger condition (E)': if $\omega(x) \ge p$, then $\eta^{-1}(E) = \operatorname{Sing}_p X$ [CP19, Definition 9.7]. Cossart and Piltant do not know if such blowups are needed for resolution in general, or if they are relevant in dimension $n \ge 4$ [CP19, Section 1 and Section 9.2.1].

*Inseparable residue extensions.* Imperfect residue fields cause technical problems in each dimension. For $n = 3$ the authors write that the real difficulties come from one lemma, for inseparable extensions of degree $p = 2$ [CP19, Lemma 7.22 and Section 1].

### An example in dimension four

**Example 4.1.1.** This is [CP19, Example 3.18]. Let $k$ be a field of characteristic $p$, let $S = k[u_1, u_2, u_3, u_4]_{(u_1, u_2, u_3, u_4)}$, let
$$h = Z^p + u_2^p u_4 u_3^p + u_3 u_1^p,$$
and let $E = \operatorname{div}(u_1 u_2)$. We compute the invariants at the origin $x$ when $k$ is perfect. The series $f = u_2^p u_4 u_3^p + u_3 u_1^p$ is clean, since $u_4$ and $u_3$ have the exponent 1 in its two monomials. So $(u; Z)$ is well adapted by Proposition 3.2.4 (in the completion of $S$). The order of $f$ is $\min(2p + 1, p + 1) = p + 1 \ge p$, so $m(x) = p$ and $\delta(x) = (p + 1)/p$. The exponent of $u_1$ in the first monomial and the exponent of $u_2$ in the second monomial are $0$, so $d_1 = d_2 = 0$ and $\epsilon(x) = p + 1$. The initial form is $F = U_1^p U_3$, and $U_3$ is not in $E$. Since $\partial F / \partial U_3 = U_1^p \ne 0$, we get $\omega(x) = \epsilon(x) - 1 = p$. This agrees with [CP19, Example 3.18].

Cossart and Piltant state that the locus of multiplicity $p$ is $V(Z, u_1, u_2) \cup V(Z, u_1, u_3)$. Let $\vartheta(t) = \sum_{i \ge 1} \lambda_i t^i \in k[[t]]$ be transcendental over $k(t)$. The formal arc
$$\varphi(Z) = \varphi(u_1) = \varphi(u_3) = 0, \qquad \varphi(u_2) = t, \qquad \varphi(u_4) = \vartheta(t)^p$$
lies on $X$. Its Zariski closure is the surface $V(Z, u_1, u_3)$, since $\vartheta$ is transcendental. Blow up the closed point along the arc, in the $u_2$-chart. For $p \ge 2$ the first step has no translation: with $u_1 = u_2 u'_1$, $u_3 = u_2 u'_3$, $u_4 = u_2 v_4$ and $Z = u_2 T_1$ we get
$$u_2^{-p} h = T_1^p + u_2 \bigl( u_2^p v_4 u_3'^p + u'_3 u_1'^p \bigr).$$
The arc goes through the origin $x_1$ of this chart, since $\varphi(u_4)/\varphi(u_2) = \vartheta(t)^p/t$ has order $p - 1 \ge 1$. We compute the invariants at $x_1$. The new divisor is $E_1 = \operatorname{div}(u'_1 u_2)$. The series $f_1 = u_2^{p + 1} v_4 u_3'^p + u_2 u'_3 u_1'^p$ is clean, since $v_4$ and $u'_3$ have the exponent 1 in its two monomials. Its order is $\min(2p + 2, p + 2) = p + 2$, so $m(x_1) = p$ and $\delta(x_1) = (p + 2)/p$. The smallest exponents are $r_1 = 0$ for $u'_1$ and $r_2 = 1$ for $u_2$, so $\epsilon(x_1) = p + 1 = \epsilon(x)$. The initial form is $U_1^p U_2 U_3$, and $U_3$ is not in $E_1$, so $\omega(x_1) = p = \omega(x)$. So $(m, \omega)$ does not change, while $\delta$ goes up.

Cossart and Piltant show that after $r$ such blowups the strict transform is
$$h_r = T_r^p + u_2^r \bigl( u_2^p v_4^{(r)} (u_3^{(r)})^p + u_3^{(r)} (u_1^{(r)})^p \bigr)$$
in suitable well adapted coordinates, where $v_4^{(r)}$ and $T_r$ absorb the terms of $\vartheta$ of degree at most $r/p$. The closure of the arc is $V(T_r, u_1^{(r)}, u_3^{(r)})$, and it is not permissible at the center $x_r$ for each $r \ge 1$ [CP19, Example 3.18].

Lean: none yet

We checked the first blowup above by hand, and its invariants by hand and by computer for $p = 2, 3, 5$. We do not check the claim on the locus of multiplicity $p$ or the formula for $h_r$ with $r \ge 2$, and we cite them from [CP19].

### Notes and references

The outline of [CP19, Section 1] describes the chapters of the proof, and it marks the places that we used above. Volume 9, Section 2.1, gives the known results in dimension at most 3 and their nodes in the map.

Node: SG0000001V · Lean: `Singularity.resolution_quasiExcellent_three` (planned, no Lean statement yet)
