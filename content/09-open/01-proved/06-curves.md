---
title: Curves in each characteristic
nodes: [SG0000002C, SG0000001A]
sources: [Har, AM69, Curves]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Curves in each characteristic

This section reports the first result of the project in positive characteristic with no extra hypothesis. Each integral curve over a field has a resolution, and the resolution is the normalization. Volume 1, Section 2.5, gives the full proof. Here we state the result in the form of the map and we say what remains for all curves.

**Theorem 1.6.1 (integral curves).** Let $p$ be $0$ or a prime. Let $k$ be a field of characteristic $p$ and let $X$ be an integral variety over $k$ with $\dim X \le 1$. Then the normalization $\pi : \tilde{X} \to X$ is a resolution of $X$.

Node: SG0000002C · Lean: `Singularity.Curves.integralResolutionInDim_one`

*Proof.* This is Theorem 2.5.6 of Volume 1. We recall the four steps. The normalization is finite by the theorem of E. Noether (Volume 1, Theorem 2.4.7), so it is proper. Its affine pieces are spectra of Noetherian integrally closed domains of dimension at most 1, so it is regular (Volume 1, Corollary 1.4.3). The regular locus of $X$ is the union of the affine open sets with an integrally closed ring of sections, and $\pi$ is an isomorphism over each of them (Volume 1, Proposition 2.5.5). The point of $\tilde{X}$ over the generic point of $X$ is in each nonempty open set of $\tilde{X}$, and it is in $\pi^{-1}(\operatorname{Reg}(X))$, so this set is dense. $\square$

**Corollary 1.6.2.** Let $p$ be $0$ or a prime. Then $\mathrm{Res}(p, 1)$ holds.

Node: SG0000001A · Lean: `Singularity.resolutionInDim_one`

*Proof.* By Theorem 1.6.1, each integral variety of dimension at most 1 over a field of characteristic $p$ has a resolution. By Hypothesis 1.3.1 with $n = 1$, which Section 1.3 proves, $\mathrm{Res}(p, 1)$ holds. $\square$

The Lean proof of Corollary 1.6.2 is not complete. The Lean development proves Theorem 1.6.1 with only the three standard axioms, and it proves the statement `Singularity.Curves.resolutionInDim_one_of_reductionToIntegral`, which is Corollary 1.6.2 with Hypothesis 1.3.1 as an argument. When the Lean proof of Hypothesis 1.3.1 is written, the node SG0000001A will be proved for each $p$.

For $p = 0$ the result also follows from Section 1.2, but the proof here is much simpler and does not use the base. For $p > 0$ the result is new in the project. It is the case $n = 1$ of the open statement. The case $n = 2$ is a theorem of Abhyankar and Lipman, and $n = 3$ is a theorem of Cossart and Piltant. These cases are not yet in Lean. The case $n \ge 4$ is open.

### Notes and references

The proof by normalization is in [Har, Chapter II, Exercise 3.8] and [Har, Chapter I, Section 6]. The only deep input is the finiteness of the normalization over a field of characteristic $p$, and Volume 1, Section 2.4, proves it with the $q$-th roots of the coefficients and no trace form.
