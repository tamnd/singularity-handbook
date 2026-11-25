# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The versions follow the line `version` of `EDITION`.

## [Unreleased]

## [0.4.25] - 2026-11-26

### Added

- Volume 0, Section 5.1 describes edition 0.4.25.
- Volume 7, Section 3.9 has Examples 3.9.5 and 3.9.6, for $p = 2$ in five and four variables. In each one $\rho$ stays, both points are in the first case, $p$ divides $|r| + d$, and $\tau_\rho$ goes down. So the hypothesis of Theorem 3.9.1 is necessary. This is the node SG00000051, for the milestone S7.11 (tamnd/singularity#198).
- Volume 9, Section 3.7 gives the same result as the seventh research report of the milestone S7, with what it means for route R1.

### Changed

- The edition pins the map release 0.4.27, with the node SG00000051 and its Lean proof.
- Volume 7, Section 3.9 and Volume 9, Section 3.7 give the Lean names of tamnd/singularity-lean#128 for Example 3.9.5, and Section 3.9 has a paragraph on the Lean proof of the example.
- Volume 7, Section 3.9 no longer says that the case where $p$ divides $|r| + d$ is open. It explains where the proof fails in the examples, and why a definition of $T_\rho$ with $\widetilde\Theta(G)$ in the first case does not help.
- Volume 9, Section 3.6 and the introductions of Volume 7, Chapter 3 and Volume 9, Chapter 3 refer to the new result.

## [0.4.24] - 2026-11-26

### Added

- Volume 0, Section 5.1 describes edition 0.4.24.
- Volume 7, Section 3.9 proves that the codimension $\tau_\rho$ of the directrix of the log-Jacobian order does not go down at a point where $\rho$ stays and both points are in the first case, if $p$ does not divide $|r| + d$ (Theorem 3.9.1). Lemma 3.9.2 gives $\Phi_i = r_i F$ for the indices with $v_i \ne 0$, and Lemma 3.9.3 gives the exact weak transforms of the elements $r_i G + x_i \partial_i G$ with $v_i = 0$ and of the Euler element. Example 3.9.4, for $p = 2$, shows that the weak transform of an element of $H(g)$ need not be in $H(g'_c)$. This is the node SG00000050, for the milestone S7.10 (tamnd/singularity#193).
- Volume 9, Section 3.6 gives the same result as the sixth research report of the milestone S7, with what it does not give.
- Volume 7, Section 3.9 and Volume 9, Section 3.6 give the Lean names of tamnd/singularity-lean#126, and a subsection on the Lean proof. The Lean theorem assumes $\rho = d$ in the place of the first case at the old point, and Section 3.9 shows that the two hypotheses are equivalent.

### Changed

- The edition pins the map release 0.4.25, with the node SG00000050 and its Lean proof.
- Volume 7, Section 3.8 and Volume 9, Section 3.5 no longer say that the forms of the weak transforms lie in the span of the new forms in the cases from the first to the first. A larger test found 17 points of 2,583 where this is false. Both sections now refer to the new sections.

## [0.4.23] - 2026-11-25

### Changed

- Volume 6, Section 2.2 gives the Lean names of the passage from the decomposition field to the inertia field (tamnd/singularity-lean#124).
- Volume 6, Chapter 2 has the Lean names of tamnd/singularity-lean#123. Proposition 2.1.4 (a Galois extension of degree $p^r$ in characteristic $p$ is a tower of Artin-Schreier steps) has its Lean line. Section 2.2 has a new subsection on the induction on the degree in Steps 3 and 4 of Proposition 2.2.1: the Lean library proves it with the step of degree $p$ as an explicit hypothesis, and it does not prove this hypothesis or Proposition 2.2.1. The introduction of Volume 6 says this.
- Volume 5, Section 2.2 has a new subsection on the case of one extension. Proposition 2.2.7 gives local uniformization over a monomial subfield when the residue field extension is separable of full degree, with a complete proof and the Lean name of tamnd/singularity-lean#121.

### Added

- Volume 0, Section 5.1 describes edition 0.4.23.
- Volume 7, Section 3.8 gives the codimension $\tau_\rho$ of the directrix of the log-Jacobian order. Proposition 3.8.2 says that $\tau_\rho$ does not go down at a point where $\rho$ stays if the new point is in the second case, and Example 3.8.3, for $p = 2$, shows that $\tau_\rho$ can go down from the second case to the first case. The Lean names are from tamnd/singularity-lean#122. This is the node SG0000004Z, for the milestone S7.9 (tamnd/singularity#173).
- Volume 9, Section 3.5 gives the same result as the fifth research report of the milestone S7, with what it does not give.

## [0.4.22] - 2026-11-25

### Added

- Volume 0, Section 5.1 describes edition 0.4.22.
- Volume 7, Section 3.7 gives the points where the log-Jacobian order $\rho$ stays under a point blowup. Theorem 3.7.1 says that they lie in the directrices of the initial forms of the elements of order $\rho$ of $\widetilde\Theta_0(G)$ or of $\widetilde\Theta(G)$, Corollary 3.7.2 says that $\rho$ goes down if these directrices meet only in $0$, Corollary 3.7.3 gives the case of the initial form of $G$, and Example 3.7.4 shows that the first case is false with $\widetilde\Theta(G)$. The Lean names are from tamnd/singularity-lean#119. This is the node SG0000004X, for the milestone S7.8 (tamnd/singularity#164).
- Volume 9, Section 3.4 gives the same result as the fourth research report of the milestone S7, with what it does not give.

### Changed

- `EDITION` now pins the map at 3256549, the release 0.4.22 of the map, with the nodes SG0000004X, SG0000004Y and SG0000004Z.
- Volume 5, Section 1.3 has the Lean name of tamnd/singularity-lean#118: the existence of an étale generator in the case $f = [K : K_0]$, with a separable residue extension. The general case has no Lean proof.
- Volume 5, Section 1.3 has the Lean names of tamnd/singularity-lean#116: the lemma of Euler (Lemma 1.3.1), the étale generator (Definition 1.3.2), the first part of Lemma 1.3.3 and the lifting theorem (Theorem 1.3.4). The second part of Lemma 1.3.3 is now the node SG0000004Y of the map, with no Lean proof.

## [0.4.21] - 2026-11-25

### Changed

- `EDITION` now pins the map at d89d32f, the release 0.4.21 of the map, and Volume 0, Section 5.1 describes edition 0.4.21.
- Volume 3, Section 3.3 gives the Lean lines of Lemma 3.3.48 to Theorem 3.3.52, the finite chain criterion of MacLane-Vaquié, now that the records of the map have the names of tamnd/singularity-lean#115. Definition 3.3.47 also gives `Singularity.MuDvd`. The introduction of Volume 3 and the Lean notes of Section 3.3 no longer say that the records do not have these names.

- Volume 3, Section 3.3 adds the finite chain criterion of MacLane-Vaquié. Definition 3.3.47 states key polynomials for a valuation with any support. Theorem 3.3.51 proves that finitely many steps of MacLane-Vaquié reach $\nu$ if and only if $\nu$ has a key polynomial, for any value group and support, and Theorem 3.3.52 gives part 4 in three cases, with Lemmas 3.3.48 to 3.3.50. The proofs follow tamnd/singularity-lean#115. Part 4 of Theorem 3.3.5 no longer says that one needs limit augmentations along an infinite family. It now says that $\nu$ is the limit of a continuous family of one degree, and that $\nu$ has no key polynomial. The introduction of Volume 3 and Volume 0, Section 5.1 give the new status of part 4.

- Volume 5, Section 3.1 no longer says that Volume 4 proves the theorem of Lipman. Volume 4 gives the structure of the proof and cites the hard steps.
- Volume 4, referee fixes. The history in Section 3.1 now gives the hypotheses of each result: Zariski proved the resolution of algebraic surfaces in characteristic 0 [Zar39], without the claim on his method that we cannot confirm for that paper. Abhyankar proved the embedded resolution of surfaces in a nonsingular threefold over an algebraically closed field of characteristic $p > 0$, and threefolds over an algebraically closed field of characteristic $p > 5$ [Abh66]. The theorem of Lipman is for reduced excellent surfaces, the theorem of Cossart-Piltant [CP19] is for reduced separated quasi-excellent schemes, and the proof of Hironaka for excellent surfaces cites [Hir67b]. Lemma 1.1.6 writes $F'$ for the strict transform, so that the name no longer clashes with the homogeneous part $F_1$. Section 1.1 now says only that the blowup of a regular surface along a regular curve is an isomorphism. The introduction and the notes of Section 2.2 say what the records show for `Singularity.resolutionInDim_two`: it is planned, it has no Lean statement yet, and the bridge to the Lipman proof in AxiomMath/Stacks needs a review that is not done.

- Volume 3, referee fixes. The introduction said that nothing in the volume is proved in Lean. It now gives the Lean status of the records: the quasi-compactness of the Zariski-Riemann space, the Abhyankar inequality, parts 1 to 3 of MacLane-Vaquié and the results on part 4 up to Theorems 3.3.44 and 3.3.46, and Propositions 4.1.7 and 4.1.8, with the statements of Theorems 4.1.5, 4.2.1 and 4.2.2. It says that part 4 is proved for discrete values, not only for rank 1, and that Volume 5 proves more cases. Section 4.2 no longer says that the volume proves no local uniformization, and it cites [Tem13] without the theorem number that we cannot confirm. Section 4.1 lists the four facts of the fidelity file and points to the Lean proof of the monomial case in Volume 5. Section 3.3 no longer says that it only states the main theorem, and the intro of Chapter 3 writes $K(s)$ for the simple extension.

- Volume 6, referee fixes. Abhyankar's theorem now has its hypotheses: projective threefolds over an algebraically closed field of characteristic $p > 5$. The results of [CP08, CP09] are stated for quasi-projective varieties over a field $k$ with $[k : k^p] < \infty$. Section 1.1 now says what [Kol20] and [BMP20, Proposition 2.14] prove, and that neither is an embedded resolution. In Section 2.2, local uniformization is the condition (LU) of [CP19, Section 4.1], Step 3 gets local uniformization for $K^{\mathrm{sep}}$ from Step 4, Step 4 no longer calls $K^r/F^r$ totally ramified, the claim on immediate steps and [CP19, Remark 4.11] is restricted to the Galois steps, and the local ring $A_P$ at a non-maximal prime has dimension at most 2. Section 4.1 gives the scope of [CP19, Remark 1.7] correctly, and Section 4.2 says that Step 4 of [CP19] uses principalization in dimension 3 [CP19, Proposition 4.4]. The introduction now says which Lean names are proofs and which are statements only.

## [0.4.20] - 2026-11-25

### Changed

- `EDITION` now pins the map at b2b76e2, the release 0.4.20 of the map, and Volume 0, Section 5.1 describes edition 0.4.20.
- Volume 5, Sections 1.4 and 2.1 have the Lean names of tamnd/singularity-lean#113: parts 1 and 2 of Lemma 2.1.2, of Corollary 2.1.6 and of Lemma 1.4.2 except its last claim. Corollary 2.1.6 now says that its local uniformization is over $k$, not over $k(y)$, and why the proof of Theorem 2.2.1 needs this form. Section 2.1 gives the Lean proof of parts 1 and 2 of Lemma 2.1.2.

- Volume 5, Section 2.1 has the Lean names of tamnd/singularity-lean#111: the lattice lemma in each rank (Lemma 2.1.4), the monomial case for value groups of each rank (Theorem 2.1.5), and part 3 of Lemma 2.1.2. A second proof of Lemma 2.1.4 follows the Lean proof: induction on a convex subgroup, Lemma 2.1.8 on the archimedean complement, and a shear. The notes of Section 2.1 and the introductions of Volume 5 and of its Chapter 2 now say what the library proves.

- Volume 0, referee fixes. Section 5.1 now gives the current Lean status of the results that its first summary names: the bound of Moh for a point blowup and the claim on the graded algebra of MacLane-Vaquié have Lean proofs, part 4 of MacLane-Vaquié has a Lean proof for discrete values of rank 1 and for nonzero support but not for support 0 with values that are not discrete, the theorems of Zariski and Abhyankar on local uniformization have no Lean statement, and Proposition 4.1.8 of Volume 3 and Corollary 2.1.10 of Volume 5 have Lean proofs. The summary of S1 is in the past tense, a dangling label is fixed, and the note on $\omega$ in edition 0.4.18 says that it needs an algebraically closed field. Section 2.4 states maximal contact in the right coordinates, describes the residual order and the bound of Moh for $z^q + g$, and says that the cycle of Hauser-Perlega is for $z^{p^3} + g$. Section 2.2 names the core problem P1, the table of Section 2.3 says where Abhyankar needs an algebraically closed field, and Section 2.3 explains how the Lean statement of the theorem of de Jong differs from Theorem 2.3.5. Section 4.1 corrects the volumes of the tiers T3, T5 and T6, and Section 4.2 marks `Singularity.WeightedInvariantCharP` as planned. Sections 2.1 and 3.1 add Nakayama's lemma and the Noetherian hypothesis.

## [0.4.19] - 2026-11-25

### Changed

- `EDITION` now pins the map at 8b7a2d5, the release 0.4.19 of the map, and Volume 0, Section 5.1 describes edition 0.4.19.
- Volume 5, Section 2.1 has a new subsection on the case of rank 1, with the Lean names of tamnd/singularity-lean#110: the lattice lemma in rank 1 (Lemma 2.1.8) in the dual form with cones, local uniformization of a monomial valuation from the conclusion of the lattice lemma (Proposition 2.1.9), and the monomial case for value groups of rank 1 (Corollary 2.1.10). The notes of Section 2.1 and the introductions of Volume 5 and of its Chapter 2 now say what the library proves.

## [0.4.18] - 2026-11-25

### Added

- Volume 9, Section 3.2, the second report of the milestone S7: the end case of the log-Jacobian route. At a point with $\rho = 0$ the equation is binomial after a change of the formal coordinates. The section gives the Lean proof of the first part and what the result does not give.
- Volume 9, Section 3.3, the third report of the milestone S7: the invariant $\omega$ of Cossart and Piltant is the residual order $\rho$ of the log-Jacobian ideal for the equations $z^p + g$ over a perfect field, so it does not depend on the coordinates and does not go up under the blowups of Section 3.1 without condition (E). The section gives the Lean proof of parts 1 and 3 and what the result does not give.

### Changed

- The introduction of Volume 3 now says that Chapter 3 proves parts 1 to 3 of the theorem of MacLane-Vaquié, and part 4 for discrete values of rank 1 and for nonzero support. It cites part 4 only for support 0 with values that are not discrete.
- The introduction of Volume 9, Chapter 3 now gives Sections 3.2 and 3.3.
- Volume 7, Section 3.6 now gives the Lean names of tamnd/singularity-lean#107 for Proposition 3.6.1, Corollary 3.6.3 and Example 3.6.4. Corollary 3.6.2 has no Lean proof.
- Volume 7, Proposition 3.5.1 now gives the Lean names of tamnd/singularity-lean#100, and the subsection on the Lean proof says which steps use that $F$ is clean.
- The edition is 0.4.18, with the map at tamnd/singularity@1fdcc3c, the release 0.4.18 of the map. This map has the Lean fields of SG0000004S and SG0000004T. Volume 0, Section 5.1 describes edition 0.4.18.
- Volume 3, Section 3.3 has a new subsection on the chain of MacLane-Vaquié with limit steps (Definition 3.3.37 to Theorem 3.3.46), with the Lean names of tamnd/singularity-lean#109. A round in one degree uses the complete family of all monic polynomials of this degree. Either $\nu$ is the limit of a chain of ordinary and limit steps, or $\nu$ is the limit of a continuous family over a valuation of the chain. For $\nu$ with nonzero support, a finite chain ends with $\nu$, for any values. Theorem 3.3.5 and the text on part 4 now say what is proved and what is not.

## [0.4.17] - 2026-11-25

### Changed

- `EDITION` now pins the map at 56bd1ff, the release 0.4.17 of the map, and Volume 0, Section 5.1 describes edition 0.4.17.
- Volume 8, referee fixes. A trait is now the spectrum of a complete discrete valuation ring, as in [dJ96, 2.12]. In Example 2.1.6 the chart of $u$ now has $v = u^{n-1} t'^n$. Step 6 of Section 2.3 now defines the open set $U$ by the smoothness of $f$ at each point of the fibre, and it proves that $U$ is open and contains the generic point, so no generic flatness is needed. Section 2.3 now says that de Jong cites the finite étale Stein factorization in [dJ96, 4.12] and does not prove it. Section 2.4 applies the flattening of [dJ96, 2.19] to proper morphisms, not projective ones. Section 1.2 now refers to Theorem 2.2.2 for stable reduction and quotes the introduction of [dJ96] correctly. The introduction of Section 1.3 now asks that the alteration is finite for the trace splitting. Section 3.2 now names the log étale desingularization in Step 3 of the sketch and drops an announcement claim that we could not check. The introductions of the volume and of Chapter 4 now say that SG0000001K has the Lean statement `Singularity.deJongAlteration` with no proof, and they mention `Singularity.IsAlteration`.
- Volume 6, Chapter 2, Lean names for the steps of degree $p$ in the reduction of Cossart-Piltant. Lemma 2.1.1, Lemma 2.1.2, Theorem 2.1.3 (Part 2), Lemma 2.2.2 and Lemma 2.3.1 now give the Lean names of singularity-lean PR #105. The new Lemma 2.1.5 in Section 2.1 states and proves that a valuation ring has exactly one extension to a purely inseparable extension, and that the tower of Lemma 2.1.2 can be chosen with each $\theta_i$ in this extension. Proposition 2.2.1, the reduction itself, still has no Lean proof.
- Volume 5, referee fixes. Section 1.2 now defines the sets $I$ and $J$ in the proof of Lemma 1.2.4 before the case split, and Proposition 1.2.5 now treats the case where $p$ is associate to $y$. Section 1.4 no longer says that all known proofs in dimension at most 3 go through local uniformization, and it now calls [NS14] a reduction, not a proof. Section 2.1 cites the theorem of Hölder as [ZS2, Chapter VI] without a section number. Section 4.2 now states Conjecture 2.3.1 for valuations trivial on $k$, as in Volume 9, and gives Theorem 2.3.10 the planned Lean name `Singularity.exists_regular_p_alteration` of node SG0000001N. The mentions of the defect now give the planned Lean name `Singularity.Valuation.defect` of node SG00000010.
- Volume 2, referee fixes. Section 1.1 now says that the morphism of Theorem 1.1.6 is birational when $I$ is nonzero on each component, and that the divisor in part 2 of Theorem 1.1.7 may have multiplicities. Section 1.2 now cites Example 1.2.2 to Section "Order reduction for ideals" of [Kol07, Chapter 3]. Section 1.3 now cites the Whitney umbrella to Section "What is a good resolution algorithm?", calls the cusp a classical example, and gives Kollár's conclusion from the umbrella: the rough invariant gives the right center. Lemma 3.3.3 (2) now removes the center from $E|_S$ only when it is a component of $E|_S$, and Step A of Theorem 3.3.5 gives Kollár's reason for the cited fact on simple normal crossings.
- Volume 1, referee fixes. Citations to [Mat] whose theorem numbers were not sure now cite the section only (Sections 13, 16, 24 and 26). Proposition 1.10.1 now cites [AM69, Theorem 11.22]. The Krull intersection theorem now refers to Corollary 4.1.8, and Section 2.3 cites [Stacks] for Nagata rings without a tag number. Section 1.7 now says that an excellent ring is J-2 by definition. Section 1.8 now names the rings that Grothendieck proved to be excellent. Section 2.3 now defines a Japanese ring correctly. The proof of Theorem 3.3.13 now gives the formula for $\chi_R(n)$ only for $n \ge 1$. Section 5.2 now gives a correct example of a regular algebra over an imperfect field that is not smooth. The introduction of Chapter 5 now says that resolution fails for some schemes of finite type over a ring that is not excellent. Theorems 4.4.7 and 6.4.7 and Example 6.2.7 now give the planned Lean names of their nodes.
- Volume 0, Sections 2.4 and 2.5 now mark `Singularity.exists_regular_not_smooth` of SG0000000C as planned. The library does not have this name.

## [0.4.16] - 2026-11-25

### Added

- Volume 7, Section 3.5, the end case of the log-Jacobian ideal. Proposition 3.5.1 says that $\rho = 0$ if and only if the equation is of type 0 or of type 1. Theorem 3.5.3 gives the normal forms $z^p + x^r$ and $z^p + x^r x_j$ over $K[[x]]$, so the equation is binomial. Example 3.5.2 shows why the proposition needs a clean $F$.
- Volume 7, Section 3.6, the invariant $\omega$ of Cossart and Piltant. Proposition 3.6.1 says that $\omega = \rho$ for the equations $Z^p + f$ over a perfect field. Corollary 3.6.2 gives the independence of $\omega$ from the well adapted coordinates. Corollary 3.6.3 says that $\omega$ does not go up under a point blowup and under the blowup of a center with (H1) and (H2), in each dimension and without condition (E). Example 3.6.4 is a Hironaka-permissible blowup at which $\omega$ goes up from $2$ to $3$.

### Changed

- Volume 3, referee fixes. Section 3.3 now says that MacLane proved part 4 of Theorem 3.3.5 when $\nu$ is also discrete of rank 1, and it gives the Lean condition on $\gamma$ in additive notation. Sections 1.2, 1.5, 2.1, 3.1 and 3.2 cite [ZS2] and [Kuh-book] without the section, chapter and theorem numbers that the text cannot confirm. Section 2.3 has a small fix of wording.
- Volume 0, Section 2.3 now gives the Lean statement `Singularity.deJongAlteration` of SG0000001K, with no proof, in the place of the old planned name.
- Volume 8, Sections 1.1, 1.2 and 4.1: the Lean lines of the alterations. Definition 1.1.1 is `Singularity.IsAlteration`, and Lemmas 1.1.2, 1.1.6 and 1.1.15 point to the Lean lemmas for the parts that the library proves. Theorem 1.2.1 and Corollary 1.2.2 point to the Lean statement `Singularity.deJongAlteration`, which has no proof.
- Volume 9, referee fixes. Theorem 2.3.5 now assumes an excellent local ring and says that the Samuel slope is infinite if and only if $R_{\mathrm{red}}$ is regular [BBE25]. Theorem 2.3.3 now has the hypothesis of Knaf-Kuhlmann that the residue field is separable. Theorem 2.4.3 is now the theorem of Włodarczyk for étale locally binomial varieties. The text now says that the cycles of [HP19a] are for $q = p^3$, and not in the family $z^p + g$. The failures of [Abr25, Remark 5.9.3], the result of [Cut15], the sources [Kol20], [BMP20], [HP24], [TemD1], [TemD2], [HOST26], [MN26] and [AS22], and the description of the lab experiments E1, E2 and E4 now match the sources and the runs. The Lean lines of SG00000015, SG00000017, SG0000000C, SG00000010, SG0000001T, SG0000001C and SG0000001K now match the map and the library.
- Volume 3, Section 3.3 has the new subsection "The discrete case", after MacLane [Mac36]. Lemma 3.3.34 is the one point where the discreteness of the values of $\nu$ is used. Proposition 3.3.35 says that the values $\nu(\varphi_i)$ of an infinite MacLane chain with bounded degrees tend to $\infty$. Theorem 3.3.36 says that for a continuous family below $\nu$ each $f$ with $\nu(f) < \infty$ is stable, that support 0 gives no limit key polynomial, and that a limit key polynomial has $\nu(\varphi) = \infty$ and gives the limit augmentation $\nu$. The Lean proofs are in `Singularity/Valuation/MacLaneDiscrete.lean` of the Lean library.
- Volume 3, Section 3.3 has the new subsection "Key polynomials for the limit augmentation". Lemma 3.3.30 gives the criterion for divisibility by the limit key polynomial $\varphi$ in the limit augmentation $\mu' = [\mu_\infty; \varphi, \gamma]$. Theorem 3.3.31 proves that $\varphi$ is a key polynomial for $\mu'$, with no new hypothesis. Proposition 3.3.32 proves that each monic $\psi$ of degree $\deg \varphi$ with $\nu(\psi) \ge \nu(\varphi)$ is again a limit key polynomial. Theorem 3.3.33 proves that $[\mu_\infty; \varphi, \nu(\varphi)]$ agrees with $\nu$ up to degree $\deg \varphi$ if and only if $\varphi$ has the largest $\nu$-value among the monic polynomials of its degree, and gives one limit step of the chain in this case. The text says that the largest value is not proved to exist and that the full chain with limit steps is not built. The text gives the Lean names from tamnd/singularity-lean#99.
- The introduction of Volume 7, Chapter 3 now gives Sections 3.5 and 3.6.
- Volume 6, the remark after Definition 3.2.5 now refers to Volume 7, Section 3.6.
- `EDITION` now pins the map at 6f980c4, the release 0.4.16 of the map, and Volume 0, Section 5.1 describes edition 0.4.16.
- `EDITION` now pins the map at da3d7f5, which has the nodes SG0000004S and SG0000004T.
- Volume 4, referee fixes. The introduction now says that the text cites three steps of [Lip78], not two: the bound on $H^1$, the fact that the process reaches rational singularities, and the end of the process. Section 1.2 now says that a Noetherian domain whose normalization is not finite has no resolution (Proposition 2.2.2), and not that each ring that is not excellent has no resolution. Sections 1.1 and 3.1 cite the lemma of [Stacks] on regular quotients of a regular local ring without a tag number. Theorem 1.1.7 now gives the node SG0000003C. Section 2.2 no longer says that no step of the proof of [Lip78] uses the characteristic of a residue field, and its notes now say that the Lean library does not prove Theorem 2.2.1. Section 3.1 no longer says that a canonical embedded resolution glues for the local embeddings of a variety. It refers to the non-embedded theorem of [CJS20] instead.

## [0.4.15] - 2026-11-25

### Added

- Volume 9, Chapter 3, the research results. Section 3.1 is the first report of the milestone S7: the residual order of the log-Jacobian ideal does not go up under the blowup of a regular center that satisfies (H1) and (H2), and Example 3.1.2 shows that (H2) cannot be omitted. The section gives the statement, the proof, the Lean names of tamnd/singularity-lean#95 and tamnd/singularity-lean#96, what the result does not give, and its status.

### Changed

- The introduction of Volume 9 now gives Chapter 3.

- Volume 7, Theorem 3.4.5 and Example 3.4.6 now give the Lean names of tamnd/singularity-lean#96. A new paragraph after the proof of Theorem 3.4.5 gives the form of (H1) and (H2) in the Lean statement, with the factor $x^r$, and explains why it is the same as the form with $G$.
- The edition is 0.4.15, with the map at tamnd/singularity@475cea1, the release 0.4.15 of the map. This map has the Lean fields of SG0000004Q and SG0000004R.
- Referee fixes in Volume 6. Step 1 of the plan in Section 2.2 now cites [CP19, Propositions 4.6 and 4.8] for the reduction to complete local domains. Case 2 of condition (E), Definition 2.2.3, now also asks that $E$ lies in the locus $p = 0$ when $S$ has characteristic 0, as in [CP19, Definition 2.32]. Theorem 3.2.6 now says that the initial form of $h$ has no terms in $Z^1, \dots, Z^{p-1}$, and no longer says that $h$ is purely inseparable. The note after Theorem 3.2.7 now has $\delta \in \frac{1}{p!} \mathbb{N}$. The citations of Section 3.2 and Section 4.3 now give [CP19, Section 2.7], where $\omega$ is defined. The plan in Section 1.2, the list in Section 4.1 and the remarks after Theorem 3.2.6 and in Section 4.2 now give the hypotheses of [CP19, Theorem 3.13]: condition (E), $m = p$, $\omega > 0$ and a center of the first or the second kind. Moh's bound is now stated for point blowups, and its Node lines give `Singularity.moh_bound_holds`, which proves it. Example 2.3.4 now says hyperplane for $z = 0$ in $\mathbb{A}^4$.

## [0.4.14] - 2026-11-25

### Changed

- Volume 6 has the new Section 4.3, which reports the experiment E4 of the lab. It computes the invariants $\delta$, $\epsilon$, $\omega$ and $\iota$ of Cossart-Piltant on the random point blowups of the lab for $n = 3$ and $n = 4$ and $p = 2, 3, 5$. No step has $\omega$ or $\iota$ going up, and each increase of $\epsilon$ has the form of Theorem 3.2.6. The section proves the test for $\omega$ (Lemma 4.3.1), derives the point center case of Theorem 3.2.6 (Corollary 4.3.2), checks one step for $n = 4$ by hand (Example 4.3.3) and lists what the data does not show. The introductions of the volume and of Chapter 4 mention it.
- Referee fixes in Volume 2. Theorem 1.1.4 and the Notes of Section 1.1 no longer call embedded resolution the second main theorem of [Hir64]. The proof that resolution gives Theorem 1.1.5 now asks for an integral quasi-projective variety and the projective resolution of Theorem 1.1.3. The gluing example of Kollár in Section 1.1 has its missing hypotheses, and its last claim is attributed to Kollár. Section 2.4 says that Theorem 2.2.7 needs a perfect field and the theorem of Zariski-Nagata in characteristic $p$. Section 3.2 says that its blowup sequences take $E = \emptyset$, and the remark after Corollary 3.2.10 claims only the first center, formally. Section 3.3 says that the induction uses the functorial form of Theorem 3.3.10, which is cited. The titles of the sections of [Kol07, Chapter 3] are corrected.
- Volume 7, Section 3.4 now gives the Lean names of tamnd/singularity-lean#95 for Definition 3.4.1, Lemma 3.4.2, Theorem 3.4.3 and Lemma 3.4.4. Two new paragraphs explain the Lean form of Theorem 3.4.3 in $K[x]$, as two inclusions, and the Lean proof of Lemma 3.4.4, which reduces to a point blowup in the variables of the center. Theorem 3.4.5 and Example 3.4.6 have no Lean proof yet.
- The edition is 0.4.14, with the map at tamnd/singularity@1ddb7a8, the release 0.4.14 of the map. This map has the Lean field of SG0000004P and the runs of the experiment E4.

## [0.4.13] - 2026-11-25

### Changed

- Volume 7, Theorem 3.2.4 and Corollary 3.2.5 now give the Lean names of tamnd/singularity-lean#93. A new paragraph after the proof of Theorem 3.2.4 explains the Lean proof in $K[x]$. It uses divisibility by monomials in the place of the ideal $W$ and of unique factorization in $K[[x]]$.
- The edition is 0.4.13, with the map at tamnd/singularity@4352077, the release 0.4.13 of the map. This map has the Lean field of SG0000003N.

## [0.4.12] - 2026-11-25

### Added

- Volume 7, Section 3.4, "The log-Jacobian ideal under a blowup in a regular center", is new. It gives the ideal $\Theta_C$ of the log derivations tangent to a coordinate center $C$, the transformation law in the charts of the blowup of $C$ (Theorem 3.4.3), the bound for the order of an equimultiple weak transform (Lemma 3.4.4) and the non-increase of $\rho$ under the conditions (H1) and (H2) (Theorem 3.4.5). Example 3.4.6 shows that $\rho$ can go up when (H1) holds and (H2) fails. The proofs hold for each number of variables. The results have no Lean proof yet (tamnd/singularity#130).

### Changed

- The edition is 0.4.12, with the map at tamnd/singularity@8c6246d, the release 0.4.12 of the map. This map has the nodes SG0000004P, SG0000004Q and SG0000004R.

## [0.4.11] - 2026-11-25

### Added

- Volume 1, Corollary 6.3.7 is new: a polynomial in characteristic $p$ is a polynomial in $x_1^q, \dots, x_n^q$ if and only if each $\partial^{(\beta)}$ with $\beta \ne 0$ and $\beta_i < q$ kills it. The proof uses the theorem of Lucas in the form $\binom{qa + b}{b} \equiv 1 \pmod p$ for $b < q$. A new paragraph in Section 6.3 gives the Leibniz rule and the composition rule of the operators $\partial^{(\beta)}$.
- Volume 7, Remark 3.1.8 is new. It explains why the log-Jacobian ideal does not see the $q$-th powers for $q = p^e$ with $e \ge 2$, with the example $x^2 y^2$ for $p = 2$.

### Changed

- Volume 1, Section 6.3 and Volume 7, Proposition 1.1.4 now give the Lean names of tamnd/singularity-lean#91: the operators $\partial^{(\beta)}$, the agreement with the Hasse derivatives of Mathlib, the first step of the proof of Theorem 6.3.6 and the order criterion at a point. The notes of Section 6.3 now say which results of the section are in Lean.
- The edition is 0.4.11, with the map at tamnd/singularity@99f6d07, the release 0.4.11 of the map. This map has the nodes SG0000004M and SG0000004N, the Lean field of SG0000003M and the Lean name of SG0000000W.
- Volume 7, Section 3.2 now gives the Lean names of Definition 3.2.1, Lemma 3.2.2 and Theorem 3.2.3, from tamnd/singularity-lean#90. A new paragraph after the proof of Theorem 3.2.3 explains the Lean form in $K[x]$: two inclusions with the product $u$ of the factors $x_i + t_i$, which is a unit only in $K[[x]]$. Theorem 3.2.4 has no Lean proof yet.
- Review of Volumes 5 and 8. Volume 5, Examples 3.2.2 and 4.2.2 said that the resolution of one model, with Proposition 1.4.5, gives local uniformization. It gives a regular center over that model only, so the text now takes local uniformization from Proposition 3.1.2. Volume 8, Proposition 1.2.3 and Section 2.3 cited Chow's lemma from [Har, Exercise II.4.10], which assumes $X$ proper; they now cite [Stacks]. Volume 8, Section 2.4 referred to Proposition 2.4.5, which does not exist; it now refers to Proposition 2.4.3. Volume 8, Proposition 1.3.4 now says "no nonempty open subset". Volume 5, Section 4.2 now says that its Lean line for SG00000009 is the statement only. Volume 5, Section 4.1 now says that the proof of Temkin uses Berkovich analytic curves, not adic spaces. Volume 8, Section 3.3 no longer calls the theorem of Temkin the strongest known result toward resolution.

## [0.4.10] - 2026-11-25

### Added

- Volume 7, Chapter 3, "The log-Jacobian ideal", is new. Section 3.1 defines the ideal, proves that it does not change when a p-th power is added, and proves the dichotomy $d - 1 \le \rho \le d$ for a clean $F$ (Theorem 3.1.4). Section 3.2 proves the transformation law under a point blowup (Theorem 3.2.3) and proves that $\rho$ does not go up (Theorem 3.2.4). Section 3.3 gives the Newton criterion for $z^p + g$ (Theorem 3.3.3) and the mod $p$ Euler identity (Proposition 3.3.6). The Lean lines name the theorems of tamnd/singularity-lean#85, tamnd/singularity-lean#86 and tamnd/singularity-lean#87. Theorem 3.2.3 and Theorem 3.2.4 have no Lean proof yet.
- Volume 7, Chapter 4, "Multiplicities divisible by p", is new. Section 4.1 proves that the inseparable layer of a translation is rigid (Theorem 4.1.3) and gives the formula for $a_{p^e}$ (Proposition 4.1.4). Section 4.2 proves the lifting test for $z^q + g$ (Proposition 4.2.1).

### Changed

- The edition is 0.4.10, with the map at tamnd/singularity@11300a2, the release 0.4.10 of the map. This map has the nodes SG0000003E to SG0000003N of Volume 7 and the nodes SG00000040 to SG0000004K of Volumes 2, 5 and 8.
- Volumes 2, 5 and 8 have Node lines for the new nodes SG00000040 to SG0000004K of tamnd/singularity#123. Each line has the form `Node: TAG · Lean: none yet`, and the tags are in the `nodes` of their sections. Volume 8, Hypotheses 2.2.4 and 2.2.5 now have Node lines. Volume 2, Section 4.2 lists the results with a node and no Lean statement, and Volume 8, Section 4.1 lists the four new nodes of the volume.

## [0.4.9] - 2026-11-25

### Changed

- The edition is 0.4.9, with the map at tamnd/singularity@70120f9. The build workflow now builds all ten volumes. The releases 0.4.7 and 0.4.8 had no files for Volume 6, because the workflow did not build it.
- Volume 3, Theorem 4.2.2 now takes the finite set $S$ first, so that the extension $L$ depends on $S$, as in [Tem13] and in the Lean statement. Volume 9, Theorem 2.3.4 has the same correction. The old form, with one $L$ for all finite sets, was stronger than the theorem of Temkin.
- Volume 5, on local uniformization, is new, as a draft in four chapters. Chapter 1 proves the theorem of Abhyankar on quadratic sequences (Theorem 1.2.6), local uniformization for $k(x, y)$ over each field (Corollary 1.2.8), the lifting theorem along an étale generator (Theorem 1.3.4), the case of surfaces in characteristic 0 with a finitely generated value group (Corollary 1.3.6), the reduction to a larger ground field (Lemma 1.4.2), and the fact that a resolution gives local uniformization (Proposition 1.4.5), so that the theorem of Hironaka gives the theorem of Zariski. Chapter 2 proves the lattice lemma and the monomial case (Lemma 2.1.4 and Theorem 2.1.5), and the theorem of Knaf-Kuhlmann up to the generalized stability theorem [Kuh10] and facts on the henselization. Chapter 3 states the theorem of Abhyankar for surfaces, deduces local uniformization of surfaces over each field from the theorem of Lipman, proves the converse of the lifting theorem, and gives examples of the defect. Chapter 4 states the theorem of Temkin [Tem13], proves that it implies the Lean statement, and shows with the surface of Volume 4, Example 2.3.5, why it does not give the open case. Volume 3, Section 4.2 now says what Volume 5 proves.
- Volume 2, on resolution in characteristic 0, is new, as a draft in four chapters. Chapter 1 states the theorems of Hironaka (resolution, strong and embedded resolution, principalization in three forms and the functorial form), proves that principalization gives resolution, and works out curves, the cusp and the Whitney umbrella. Chapter 2 proves the lemmas on derivative ideals and transforms of marked ideals and the theorem on maximal contact, says exactly where characteristic 0 is used, and gives the example of Narasimhan in characteristic 2 with its Lean line. Chapter 3 proves the restriction theorem, the going-down and going-up theorems for the coefficient ideal, the formal uniqueness of maximal contact, the monomial case and the induction from order reduction to principalization, after [Kol07, Chapter 3]; it cites Kollár for tuning, the étale uniqueness and the globalization. Chapter 4 explains the Lean statement, its proof from Main Theorem I of the base, the checks, and the results of the volume that have no node.
- Volume 0, Theorem 2.3.5 now says that its Lean statement is planned. Volume 9, Section 2.3 now says that the theorem of Temkin does not give a Galois extension.
- Volume 7, Section 1.2 has the new subsection "The purely inseparable equation". The new Proposition 1.2.7 proves that for $f = z^q + F$ with $q = p^e$ and $F$ clean, over a ring of exponential characteristic $p$, the coordinate $z$ attains the characteristic polyhedron, no vertex $v \ne 0$ is solvable, and $\Delta(f; x) = \frac{1}{q} N(F)$ for a polynomial $F$. It has a complete proof, Example 1.2.8 with $p = q = 2$ and $F = x^3 + y^5$, and Remark 1.2.9 on what is not proved. The text gives the Lean names from tamnd/singularity-lean#83. Volume 6, Sections 3.1, 3.2 and 4.2, and Volume 9, Section 2.3, refer to the new proposition.
- Volume 3, Section 3.3 has the new subsection "Continuous families and limit augmentations". It constructs the limit augmentation of Vaquié [Vaq07] for a continuous family of augmentations of one degree. Definition 3.3.20 to Lemma 3.3.23 define the family, the stable polynomials and the limit $\mu_\infty$. Proposition 3.3.24 proves that $\mu_\infty$ agrees with $\nu$ on the stable polynomials, and that some polynomial is not stable exactly when the family does not reach $\nu$. Proposition 3.3.26 proves the properties of the limit key polynomials. Theorem 3.3.29 proves that the limit augmentation is a valuation with $\mu_i \le [\mu_\infty; \varphi, \nu(\varphi)] \le \nu$. The text says what part 4 of Theorem 3.3.5 still does not have. The text gives the Lean names from tamnd/singularity-lean#84.
- Volume 8, on alterations, is new, as a draft in four chapters: the theorem of de Jong with the definitions, the curve case and the limits of the theorem for resolution; the proof of de Jong, with the local computations of the blowups of semistable curves, the reductions and the induction by fibrations in curves, from the moduli of stable curves as the named Hypotheses 2.2.4 and 2.2.5 (Proposition 2.2.6 proves that the first implies the second); Galois alterations and the separable distillation of fields, the theorem of Gabber on alterations of degree prime to $\ell$ with the Sylow step, and the theorem of Temkin on alterations of degree a power of $p$; and a Lean plan with the nodes SG0000001K, SG0000001M and SG0000001N.

## [0.4.8] - 2026-11-25

### Changed

- The edition is 0.4.8, with the map at tamnd/singularity@7519db1.
- The intros of Volume 3 and of its Chapter 4 now say that Propositions 4.1.7 and 4.1.8 prove local uniformization in two easy cases.
- Volume 3, Section 3.3 has the new subsections "The choice of the key polynomial" and "The graded algebra of an augmentation". The key polynomial of a step of the chain is not unique, and the augmentation depends on the choice: Example 3.3.18 gives two choices with different augmentations. Proposition 3.3.15 proves that all key polynomials of the step have the same degree and are $\mu$-equivalent, Lemma 3.3.16 and Proposition 3.3.17 compare the augmentations, and the text says that there is no maximal choice in general [Vaq07]. Proposition 3.3.19 proves the claim of part 3 of Theorem 3.3.5 on the graded algebra, in the form with $\mu$-equivalence of the library. The text gives the Lean names from tamnd/singularity-lean#80.
- Volume 3, Section 4.1 has the new subsection "Divisorial valuations". The new Proposition 4.1.8 proves local uniformization for a valuation ring that is essentially of finite type over $k$, and for each valuation with $\operatorname{trdeg}_k K \le \operatorname{trdeg}_k \kappa_v + 1$, in particular for each divisorial valuation, in each characteristic. It has a complete proof and its Lean line, from tamnd/singularity-lean#81.

## [0.4.7] - 2026-11-25

### Changed

- Citations of Matsumura [Mat] are checked against sources that quote its theorem numbers. Volume 1, Sections 2.3 and 2.4 no longer cite [Mat, Section 33] for the finiteness of the normalization. They cite [Eis95, Corollary 13.13] and [Stacks, Tag 0335]. Volume 4, Section 1.1 says that [Mat, Theorem 14.2] gives Step 2 of Theorem 1.1.11, and it cites [Stacks, Tag 00NR] for the full statement. Volume 4, Section 3.1 cites Theorem 1.1.11 and [Stacks, Tag 00NR] for the same fact. Volume 1, Section 3.3 states the theorem of Hilbert and Serre in its form with the Poincaré series, and Section 1.6 states [Mat, Theorem 7.10] exactly. Volume 0, Section 2.1 cites [EGA4, Section 6.12] in the usual form.
- Volume 7, Section 1.4: Theorem 1.4.1 (Moh's bound) is now stated for a point blowup in the coordinates of the chart, over a field of characteristic $p$, with the second claim that $d' \le d$ if $q \nmid \operatorname{ord} F$. It has a complete proof with diagonal operators, the same as the Lean proof. The text gives the Lean names from tamnd/singularity-lean#78. The text no longer says that the theorem is not proved, and it says that blowups with larger centers are not treated.
- Volume 6, on threefolds in characteristic $p$, is new, as a draft in four chapters: the theorems of Abhyankar, Cutkosky and Cossart-Piltant and the plan of their proofs; the reduction to purely inseparable and Artin-Schreier equations of degree $p$; the characteristic polyhedron of Hironaka and the invariants of Cossart-Piltant, with examples computed by hand; and the places where the method uses dimension 3. Proposition 3.2.4 proves that cleaning gives the minimal polyhedron of $X^p + f$ over a perfect field, so that the invariant $\epsilon$ is the residual order of Volume 7.
- Volume 0, Section 5.1 says that Volume 6 is drafted.
- Volume 3, Section 3.3 has the new subsection "The chain of MacLane". It defines the MacLane chain of $\nu$ and proves its properties in Lemma 3.3.11, the theorem of MacLane for $\nu$ with discrete values in Theorem 3.3.12, and a criterion for a finite chain in Proposition 3.3.13, with complete proofs. Example 3.3.14 shows that the chain can be infinite, also for a nonzero support. The text now says that part 4 of Theorem 3.3.5 is proved without limit augmentations for $\nu$ with discrete values, and not in general. The text gives the Lean names from tamnd/singularity-lean#77.
- Volume 6 cites the works that the text names: [Abh56], [Abh59], [Cos87], [Cos92], [CP15], [Cut04], [Hir67b], [Moh96] and [Moh14].
- Volume 7, Section 1.3 said that changes of the $x$ coordinates that keep $E$ can change the residual order. This is false. The new Proposition 1.3.5 proves that the residual order, computed after cleaning, does not depend on these coordinates, as Volume 6, Proposition 3.2.4(5) says for $q = p$. The text gives an example in which the change of coordinates makes $F$ unclean. Definition 1.3.5 and Lemma 1.3.6 are now Definition 1.3.6 and Lemma 1.3.7. Section 1.4 no longer says that the Lean statement of Moh's bound may need a hypothesis on the coordinates.
- Volume 3, Section 3.3 has the new subsection "The step of MacLane". The new Lemma 3.3.9 is the inductive step of the chain of part 4 of Theorem 3.3.5, with a complete proof, and the new Lemma 3.3.10 is the first step. The text now says which parts of part 4 are proved and which are not. The text gives the Lean names from tamnd/singularity-lean#75.
- Volume 3, Section 3.3: the Lean line of Lemma 3.3.7 says that `Singularity.KeyPolynomial.map_mul_modByMonic` proves only the first claim, and it gives the short argument for the second claim.
- Volume 9, introduction of Chapter 1: Section 1.3 proves the step from integral to reduced varieties, in `Singularity.Reduction.reductionToIntegral`, so the text no longer calls it a named hypothesis.
- Volume 9, Section 1.2: the name `Singularity.Base.hironaka` does not exist in the library, so its Lean line is marked as planned.
- Volume 9, Section 1.3: five arrows in Lemma 1.3.5 and its proof had a tab character in place of `\to`.
- Volume 9, Section 1.5: P1 for $n \le 3$ holds over each field, so the text cites Theorem 2.1.4 and [CP19], and not only [CP08, CP09], which need a differentially finite field.
- Volume 9, Section 2.2: Kuhlmann introduced dependent and independent Artin-Schreier defect extensions [Kuh10b], and Kuhlmann-Rzepka extended them to mixed characteristic [KR23]. The criterion of [CKR25] is for Galois defect extensions of degree $p$ and uses the Kähler differentials of the extension of valuation rings.
- Volume 9, Section 2.3: the definition of local uniformization has the quantifier over the varieties $X$. Conjecture 2.3.2 is stated in characteristic $p$ and for the components of $X$, as in its Lean statement. The text no longer says that it is open in characteristic 0, where Hironaka's theorem proves the statement.
- Volume 1, review: the text now says that the openness of the regular locus is proved in Lean over each field (Theorem 1.9.5), in Sections 1.3, 1.7, 1.8, 2.5, 5.2 and 5.3 and in the introduction of Chapter 5. Theorem 5.2.3 has a Lean line for the case of a field. Section 1.1 proves the case $x \in \mathfrak{m}^2$ of its Lean paragraph and cites Chapter 3 for the Hilbert-Samuel polynomial. Section 1.2 states what [Stacks, Tag 00NQ] gives. Section 3.2 proves $\operatorname{ord}(fg) = \operatorname{ord} f + \operatorname{ord} g$ and says that it has no Lean proof yet. Section 4.4 corrects the example of a coefficient field that is not unique. Citations with a wrong number are corrected in Sections 1.6, 2.3, 2.4, 2.5 and 4.1.
- Volume 4, review: the introduction lists the Lean names of Chapter 3 as a fifth kind. Section 3.1 states the open set $U$ of the Lean statement as in `Singularity.IsEmbeddedResolution`: its complement consists of points of $X$ where $X$ is not regular. The Lean line of Definition 3.1.3 says that the Lean definition has no sequence of blowups, and the Lean name of the permissible closed point is given.

## [0.4.6] - 2026-11-24

### Changed

- Volume 3, Section 3.3 proves the first claim of part 3 of Theorem 3.3.5 in the new subsection "The first claim of part 3". The new Lemma 3.3.8 is the criterion for $\mu'$-divisibility. The text gives the Lean names from tamnd/singularity-lean#72.
- Volume 3, Section 4.1 has the new Proposition 4.1.7, local uniformization in transcendence degree at most 1 in each characteristic, with a proof in the affine form. The text gives the Lean names from tamnd/singularity-lean#73.
- Volume 0, Section 5.1 gives the new Lean proofs of Volume 3.
- `EDITION` has the version 0.4.6 and the commit of tamnd/singularity with the records of tamnd/singularity-lean#72 and tamnd/singularity-lean#73.

## [0.4.5] - 2026-11-24

### Changed

- Volume 3, Section 4.1 has the new Proposition 4.1.6, the affine form of local uniformization, with a proof. The new subsection "The Lean statements" gives the Lean names of tamnd/singularity-lean#69 and tamnd/singularity-lean#70. Volume 3, Section 4.2 tells how the Lean statements of Theorems 4.2.1 and 4.2.2 are written, and Volume 9, Section 2.3 tells how the Lean statement of Conjecture 2.3.2 is written. The Node lines of the nodes SG0000001E to SG0000001J give the Lean statements.
- Volume 3, Section 3.3 proves parts 1 and 2 of Theorem 3.3.5 with two new lemmas, the expansion criterion for $\mu$-minimal polynomials (Lemma 3.3.6) and the products in low degree (Lemma 3.3.7). It gives the Lean names of these results, from tamnd/singularity-lean#68.
- `EDITION` has the version 0.4.5 and the commit of tamnd/singularity with the Lean statements of local uniformization.

## [0.4.4] - 2026-11-24

### Changed

- Volume 3, Section 3.3 gives the Lean names of Lemma 3.3.2 and Definitions 3.3.3 and 3.3.4, from tamnd/singularity-lean#66. The new subsection "The Lean definitions" tells how the Lean definitions use $\mu$-equivalence in place of the graded algebra, and which parts of Theorem 3.3.5 have Lean proofs.
- `EDITION` has the version 0.4.4 and the commit of tamnd/singularity with the Lean definitions of the key polynomials.

## [0.4.3] - 2026-11-24

### Changed

- Volume 3, Section 1.5 gives the Lean names of Definition 1.5.1 and Theorem 1.5.3, from tamnd/singularity-lean#64, and it explains the Lean proof of Theorem 1.5.3 by ultrafilters.
- Volume 3, Section 2.1 gives the Lean names of Theorems 2.1.4 and 2.1.5, from tamnd/singularity-lean#63. The new subsection "The Lean proof" tells how the Lean statements are written.
- `EDITION` has the version 0.4.3 and the commit of tamnd/singularity with the Lean proofs of the Zariski-Riemann theorem and the Abhyankar inequality.

## [0.4.2] - 2026-11-24

### Changed

- Volume 4, Section 3.1 gives the Lean names of Definitions 3.1.1 to 3.1.3 and of Theorem 3.1.4, from tamnd/singularity-lean#61. The new subsection "The Lean statement" tells how the Lean statement of Theorem 3.1.4 is weaker than the theorem, and it names the two facts of the section that have Lean proofs. Volume 9, Section 2.1 and Volume 0, Section 5.1 give the new Lean name.
- `EDITION` has the version 0.4.2 and the commit of tamnd/singularity with the Lean statement of embedded resolution.

## [0.4.1] - 2026-11-24

### Added

- Volume 3, "Valuations", with four chapters at status drafted. Chapter 1 defines valuations and valuation rings, relates the rank to the prime ideals, proves the extension theorem of Chevalley (Theorem 1.3.2) and the quasi-compactness of the Zariski-Riemann space (Theorem 1.5.3, node SG0000000X), and computes the monomial and arc valuations of the plane. Chapter 2 proves the Abhyankar inequality (Theorem 2.1.5, node SG0000000Y) in the form for fields and in the local form of [Abh56], and it proves that the value group and the residue field are finitely generated in the case of equality. Chapter 3 gives the fundamental inequality, defines the defect (Definition 3.2.1, node SG00000010), proves that an extension without defect has best approximations, computes the Artin-Schreier extension with defect $p$ over the perfect hull of $\mathbb{F}_p((t))$, and defines key polynomials (Definition 3.3.3, node SG0000000Z) with the theorem of MacLane cited from [Mac36] and one MacLane chain computed by hand. Chapter 4 defines local uniformization, proves the reduction of Zariski to finitely many models (Proposition 4.1.2), and states the theorems of Zariski, Abhyankar, Cossart-Piltant (node SG0000001F), Knaf-Kuhlmann (node SG0000001E) and Temkin (node SG0000001G) with their sources.

### Changed

- The build workflow builds Volume 3.
- Volume 9, the introduction of Chapter 2 and Section 2.3 refer to Volume 3. Example 2.2.3 refers to Volume 3, Proposition 3.2.5, for the proof of its last statements.
- Volume 0, Section 5.1 describes Volume 3.
- `EDITION` has the version 0.4.1 and the commit of tamnd/singularity with the new papers on valuations.

### Fixed

- Volume 9, Section 2.1 tells that [CP08, CP09] need a base field that is differentially finite over a perfect subfield, and that [CP19] removes this hypothesis.
- The theorem headings of Volume 9, Chapter 2 use the hyphen form for the names of more than one author (Cossart-Piltant, Cossart-Jannsen-Saito, Knaf-Kuhlmann, Benito-Bravo-Encinas, Abramovich-Schober).
- Volume 3 cites [Vaq07], [Kuh10], [Kuh10b], [Zar44b] and [Zar39] with the new records of tamnd/singularity.

## [0.4.0] - 2026-11-24

### Added

- Volume 7, Section 1.4 has the subsection "Computations". It reports the runs of the experiments E1 and E2 of the lab (tamnd/singularity#72). Example 1.4.6 is a new failure of the bound of the proof of Moh for $p = 3$, found by the lab and checked by hand. Remark 1.4.7 gives the candidate secondary invariants that the lab tests, and the steps where each one goes up.

### Changed

- `EDITION` has the version 0.4.0 and the commit of tamnd/singularity with the lab. Volume 0, Section 5.1 tells that Volume 7 reports the lab and that the milestone S3 is complete.

## [0.3.3] - 2026-11-24

### Added

- Volume 4, Section 1.1 has the subsection "The blowup along a regular curve". Theorem 1.1.11 proves that a prime $P$ of a regular local ring $R$ with $R/P$ regular of dimension $\dim R - 1$ is generated by one element of $\mathfrak{m} \setminus \mathfrak{m}^2$. Corollary 1.1.12 proves that the blowup along such a subscheme is an isomorphism (node SG0000003D). Both have the Lean proofs of tamnd/singularity-lean#57, for the local ring and the chart.

### Changed

- Volume 7, Theorem 2.2.5 (the points of the same order lie in the directrix, node SG0000003B) has the Lean proof `Singularity.mem_directrix_of_ord_pointChart_eq` of tamnd/singularity-lean#55. Two new paragraphs describe the Lean definition of the directrix and the route of the Lean proof. Volume 0, Section 5.1 is changed to match.
- `EDITION` has the version 0.3.3 and the commit of tamnd/singularity at the release 0.3.2. Volume 0, Section 5.1 tells that Theorem 1.1.11 and Corollary 1.1.12 of Volume 4 have Lean proofs.

### Fixed

- Volume 7, Lemma 2.2.1 gives its Lean lemmas, and Corollary 2.2.3 states that it has no Lean proof yet. A new paragraph explains how the Lean proof of Theorem 2.2.2 uses the lemma. This removes two warnings of `shb check`.

## [0.3.2] - 2026-11-24

### Added

- Volume 4, "Resolution of surfaces", with three chapters at status drafted. Chapter 1 defines the blowup, computes the blowup of a regular surface at a closed point in each characteristic (Theorem 1.1.7, with the Lean results of Volume 1, Section 1.10), and proves that a normal excellent surface has finitely many singular points. Chapter 2 states the theorem of Lipman (Theorem 2.2.1, node SG0000001B), proves its formal parts and the properties of rational singularities, and cites the two hard steps from [Lip78]. Section 2.3 computes the surfaces $xy = z^n$, the surface $z^p = x^{p+1} + y^{p+1}$ in characteristic $p$, and the surface $z^2 = x^4 + y^4$, where the blowup is not normal and the singularity is not rational. Chapter 3 states the embedded resolution of surfaces of Cossart, Jannsen and Saito (node SG0000001C) and gives the history.

### Changed

- The build workflow builds Volume 4.
- Volume 9, Section 1.1 refers to Volume 1, Chapter 2 for curves and to Volume 4 for surfaces.
- Volume 0, Section 5.1 describes Volume 4.

### Fixed

- Fourteen Node lines in Volume 9 gave a Lean name with the mark "(the statement only)", but the Lean library has no declaration of that name. These lines now say "(planned, no Lean statement yet)". `shb check` now gives a fault when a Node line marks a name as a statement and records/lean.json does not have the name.

## [0.3.1] - 2026-11-24

### Fixed

- Volume 0, Section 5.1 gives the results of Volume 7, Chapter 2 after the results of Chapter 1.
- The build workflow builds Volume 7. The releases 0.2.14 and 0.3.0 have no PDF or EPUB file for Volume 7, and the release 0.3.1 has them.

### Changed

- `EDITION` has the version 0.3.1. It refers to the same commit of tamnd/singularity as the release 0.3.0.

## [0.3.0] - 2026-11-24

### Added

- Volume 7, Chapter 2, "The point blowup". Section 2.1 gives the charts of a point blowup and the weak transform, with Proposition 2.1.1 from tamnd/singularity-lean#52. Section 2.2 proves that the order does not go up under a point blowup (Theorem 2.2.2, node SG0000003A, `Singularity.ord_le_of_pointChart`), defines the directrix and states that the points of the same order lie in the directrix (Theorem 2.2.5, node SG0000003B, no Lean proof). It has two examples, one in characteristic 2.
- Volume 1, Section 1.10, the charts of the blowup of a regular local ring. It proves that the associated graded ring is a polynomial ring over the residue field (Proposition 1.10.1), that $R[\mathfrak{m}/x]/(x)$ is a polynomial ring (Proposition 1.10.4) and that each chart is regular (Theorem 1.10.6, node SG0000003C, `Singularity.Algebra.isRegularRing_blowupChart` from tamnd/singularity-lean#53).

### Changed

- `EDITION` refers to the release v0.3.0 of tamnd/singularity.
- Volume 0, Section 5.1 gives the status at release 0.3.0, with the milestone S2 complete.
- The introduction of Volume 7 and Section 1.3 of Volume 7 refer to Theorem 2.2.2.

## [0.2.14] - 2026-11-24

### Added

- Volume 9, Chapter 2, "The open case". Section 2.1 states the known cases in dimension at most 3 (Lipman, Cossart-Jannsen-Saito, Abhyankar, Cutkosky, Cossart-Piltant) and what is still open there. Section 2.2 explains why the methods of characteristic 0 fail. It has a complete proof that the points of order 2 of the example of Narasimhan are not in a smooth hypersurface germ, an example over an imperfect field, and an Artin-Schreier extension with defect. Section 2.3 describes the routes to dimension 4: valuations and patching, characteristic polyhedra, Rees algebras, weighted blowups, the purely inseparable equations and alterations. Section 2.4 gives the special classes with a resolution in all dimensions, with a toric example, and the next steps of the project.
- Volume 1, Section 1.9, the regular locus over an imperfect field. It proves the flat descent of regularity (Theorem 1.9.1), the descent of generic regularity along a finite injective map (Lemma 1.9.2), generic regularity over an arbitrary field (Theorem 1.9.4) and the openness of the regular locus of a scheme locally of finite type over an arbitrary field (Theorem 1.9.5). Each of these results has a Lean proof from tamnd/singularity-lean#47.
- Volume 7, Example 1.4.5, one certified cycle of Hauser and Perlega in characteristic 2 with $d = 2$. It gives the 20 point blowups of the cycle, the residual order after each step and the final equation, with the Lean names of tamnd/singularity-lean#49. Theorem 1.4.3 still has no Lean proof.

### Changed

- `EDITION` refers to the release v0.2.14 of tamnd/singularity.
- Volume 0, Section 5.1 gives the status at release 0.2.14.
- Volume 7, Chapter 1 has the Lean names of tamnd/singularity-lean#45: the order and its laws, the Newton polyhedron, cleaning, the residual order, the chart of a point blowup, and the example of Section 1.4 (Example 1.4.2, `Singularity.Examples.kangaroo`). Section 1.4 says that the Lean statement of the bound of Moh is not proved.
- Remark 1.8.18, Section 1.7, Theorem 5.3.3 and the introduction of Volume 1, Chapter 1 refer to Section 1.9. The node SG0000000K is proved for a field.
- Volume 9, Example 2.2.1 (Narasimhan) has the Lean name of tamnd/singularity-lean#50, and a paragraph on the Lean proof.
- The guide, Section 2.4, gives SG00000017 as not proved and SG00000039 as the certified cycle.

## [0.2.13] - 2026-11-24

### Added

- Volume 1, Section 3.3, the multiplicity of a regular local ring. It proves that $(\mathfrak{m}^{n+1} : a) = \mathfrak{m}^n$ for the first element $a$ of a regular sequence that generates $\mathfrak{m}$ (Lemma 3.3.12), and that a regular local ring of dimension $d$ has $\ell(R/\mathfrak{m}^{n+1}) = \binom{n+d}{d}$ and $e(R) = 1$ (Theorem 3.3.13). Each of these results has a Lean proof. Remark 3.3.14 states the converse of Nagata and gives a ring that shows that the converse needs a hypothesis.
- Volume 7, "Invariants in positive characteristic", Chapter 1, the order and the residual order. Section 1.1 proves the laws of the order and the closedness of the locus of order at least $d$ with Hasse derivatives. Section 1.2 defines the Newton polyhedron and proves the theorem of Ostrowski (Theorem 1.2.4). Section 1.3 defines cleaning and the residual order of a purely inseparable equation, after [HP19a]. Section 1.4 states the bound of Moh, computes the example of [HP19a] in which the residual order increases from $5$ to $7$ in one blowup (Example 1.4.2), and states the cycles of Hauser and Perlega (Theorem 1.4.3). These sections do not have Lean proofs yet.

### Changed

- `EDITION` refers to the release v0.2.13 of tamnd/singularity.
- Remark 3.1.7 refers to Theorem 3.3.13. Remark 3.3.11 is now Lemma 3.3.11, Lemma 3.3.12, Theorem 3.3.13 and Remark 3.3.14.

## [0.2.12] - 2026-11-24

### Added

- Volume 1, Section 1.8, generic regularity over a perfect field. It proves that a localization of a regular ring is regular (Lemma 1.8.14), generic regularity over a perfect field with a separating transcendence basis (Theorem 1.8.16), and the openness of the regular locus of an algebra of finite type and of a scheme locally of finite type over a perfect field (Theorem 1.8.17). Remark 1.8.18 explains why the method fails over an imperfect field. Each of these results has a Lean proof.

### Changed

- `EDITION` refers to the release v0.2.12 of tamnd/singularity.
- Section 1.8 has the title "Generic regularity". Sections 1.7, 5.2 and 5.3, the introduction of Chapter 5 and Volume 0, Section 5.1 now say that the openness of the regular locus is proved in Lean over a perfect field, and that the case of an imperfect field is open.

## [0.2.11] - 2026-11-24

### Added

- Volume 1, Chapter 4, completion and the Cohen structure theorem. It proves the Artin-Rees lemma (Theorem 4.1.5) and the intersection theorem of Krull (Theorem 4.1.7), the exactness and flatness of completion (Proposition 4.2.5 and Theorem 4.2.7), that the completion of a Noetherian ring is Noetherian (Theorem 4.2.9), and that a Noetherian local ring and its completion have the same dimension and embedding dimension, so that one is regular if and only if the other is (Theorem 4.3.3). It proves the existence of coefficient fields in characteristic $0$ and for a perfect residue field (Theorem 4.4.4) and the Cohen structure theorem (Theorem 4.4.7), and it states the case of mixed characteristic (Theorem 4.4.9). Example 4.3.5 shows that the completion of the local ring of the node is not a domain.
- Volume 1, Chapter 5, excellent rings. It defines G-rings, the J-2 property, universally catenary rings and excellent rings, and it proves that a Dedekind domain of characteristic $0$ is a G-ring (Proposition 5.1.6) and that a complete local ring is universally catenary (Proposition 5.2.6). It states the theorems of Grothendieck on excellent rings (Theorem 5.2.8) and on resolution and quasi-excellence (Theorem 5.3.6), proves that the regular locus of a quasi-excellent scheme is open (Proposition 5.3.2 and Theorem 5.3.3), and gives the discrete valuation ring of Nagata that is not quasi-excellent (Example 5.3.7).
- Volume 1, Chapter 6, the Frobenius and positive characteristic. It proves the first properties of the Frobenius, computes the differentials of a field extension with a $p$-basis (Theorem 6.2.3), gives a regular curve that is not smooth (Example 6.2.7), computes the differential operators of a polynomial ring with the Hasse derivatives (Theorem 6.3.6), and proves that the Frobenius of a regular ring is flat, one direction of the theorem of Kunz (Theorem 6.4.7).
- Volume 1, Section 3.3, the Hilbert-Samuel polynomial and the multiplicity. It proves the criterion for eventual polynomials by forward differences (Lemma 3.3.2), the theorem of Hilbert and Serre (Theorem 3.3.5) and the Hilbert-Samuel polynomial (Theorem 3.3.6). It defines the multiplicity (Definition 3.3.7) and proves its first laws (Proposition 3.3.8). Each of these results has a Lean proof.

### Changed

- The introduction of Volume 1 lists Chapters 4, 5 and 6.
- Remark 3.1.7 and the intro of Chapter 3 now refer to Section 3.3.
- Volume 0, Section 5.1 gives the results of the milestone S2 at this release.
- `EDITION` refers to the release v0.2.11 of tamnd/singularity.

## [0.2.10] - 2026-11-24

### Added

- Volume 1, Section 1.8, Theorem 1.8.12: the regular locus of a scheme that is locally of finite type over a field of characteristic $0$ is open.

### Changed

- `EDITION` refers to the release v0.2.10 of tamnd/singularity.

## [0.2.9] - 2026-11-24

### Added

- Volume 1, Section 1.8, generic regularity in characteristic zero. It proves the Jacobian criterion for a hypersurface (Proposition 1.8.2 and Corollary 1.8.3), the conductor lemma (Lemma 1.8.4), generic regularity over a regular base (Theorem 1.8.8) and over a field of characteristic $0$ (Theorem 1.8.9), and the openness of the regular locus of an algebra of finite type over a field of characteristic $0$ (Theorem 1.8.10). Example 1.8.11 applies the method to the cuspidal cubic. Each result has the name of its Lean proof.

### Changed

- The introduction of Chapter 1 and Section 1.7 refer to Section 1.8.
- `EDITION` refers to the release v0.2.9 of tamnd/singularity.

## [0.2.8] - 2026-11-24

### Added

- Volume 1, Section 1.7, the regular locus and the criterion of Nagata. It proves that the regular locus is stable under generization (Proposition 1.7.2), the topological criterion for an open set (Lemma 1.7.3), the spreading of a regular system of parameters (Proposition 1.7.5) and the criterion of Nagata (Theorem 1.7.7). Example 1.7.8 computes the regular locus of the cuspidal cubic. Each result has the name of its Lean proof.

### Changed

- The introduction of Chapter 1 and Section 1.6 refer to Section 1.7.
- `EDITION` refers to the release v0.2.8 of tamnd/singularity.

## [0.2.7] - 2026-11-24

### Added

- Volume 1, Section 1.6, the theorem of Serre and localization. It proves the Ext criterion for projective dimension (Lemma 1.6.1), the bound $\operatorname{pd}_R M \le \dim R$ over a regular local ring (Theorem 1.6.3), the theorem of Serre in both directions (Theorem 1.6.8), and the regularity of $R_\mathfrak{p}$ for a regular local ring $R$ (Corollary 1.6.9). Each result has the name of its Lean proof.

### Changed

- Section 1.5 and the introduction of Chapter 1 no longer say that the converse of Serre is not in Lean.
- `EDITION` refers to the release v0.2.7 of tamnd/singularity.

## [0.2.6] - 2026-11-24

### Added

- Volume 1, Section 1.5, regular sequences and the residue field. It proves that the maximal ideal of a regular local ring is generated by a regular sequence of length $\dim R$ (Theorem 1.5.3), and that the residue field has projective dimension $\dim R$ (Theorem 1.5.6). This is the first half of the theorem of Serre. The section says that the converse, which gives the localization theorem, is not in Lean yet.
- Volume 1, Chapter 3, the Hilbert-Samuel function. Section 3.1 defines the function $n \mapsto \ell(M/I^n M)$, proves that its values are finite when $I$ contains a power of a maximal ideal, and gives the count for the local ring of affine space. Section 3.2 defines the order of an element for an ideal, proves its laws, and proves with the intersection theorem of Krull that only $0$ has infinite order in a Noetherian local ring. The Lean proofs are in `Singularity/Algebra/HilbertSamuel.lean`. The chapter says that the Samuel multiplicity is not proved in Lean yet.

## [0.2.5] - 2026-11-24

### Changed

- Volume 9, Section 1.3. The reduction to integral varieties is now Theorem 1.3.1 with the Lean proof `Singularity.Reduction.reductionToIntegral`. It was a hypothesis. The new Lemma 1.3.5 proves with the valuative criterion that a finite disjoint union of proper morphisms is proper. The section "The Lean proof" gives the four steps of the formal proof.
- Volume 9, Section 1.2. Theorem 1.2.6 (characteristic 0) is now unconditional, with the Lean proof `Singularity.resolutionInDim_charZero`.
- Volume 9, Section 1.6, and Volume 1, Section 2.5. The resolution of each curve, not only of each integral curve, is now proved, with the Lean proof `Singularity.Curves.resolutionInDim_one`.
- Volume 0, Section 2.3. Theorems 2.3.3 and 2.3.4 are now unconditional.

## [0.2.4] - 2026-11-24

### Added

- Volume 1, Section 2.5, the resolution of curves. It proves that the normal locus of a domain with a finite normalization is open with the conductor, that the regular locus of a curve is open, and that the normalization of each integral curve over a field is a resolution, in each characteristic. Each result has its Lean proof.
- Volume 9, Section 1.6, curves in each characteristic. It states the result in the form of the map, and it says that the general case of curves waits for the Lean proof of the reduction to integral varieties.

### Changed

- Volume 1, Sections 1.4, 2.3 and 2.4 and the introductions of Chapters 1 and 2 now refer to Section 2.5 for the resolution of curves. Section 1.4 no longer says that the case of characteristic p is open in Lean.

## [0.2.3] - 2026-11-24

### Added

- Volume 1, Section 2.4, the normalization in characteristic p. It proves the finiteness of the integral closure of a polynomial ring in a purely inseparable extension with the $q$-th roots of the coefficients, the reduction of the general case with the normal closure, the theorem of E. Noether over each field, and the resolution of affine curves over each field. Each result has its node and its Lean proof.

### Changed

- Volume 1, Section 2.3 now refers to Section 2.4 for the general case. The paragraph on perfect fields is clearer.
- Volume 1, Chapter 2, the introduction describes Section 2.4.
- `EDITION` is 0.2.3 and points to the map at the release v0.2.3 of tamnd/singularity.

## [0.2.2] - 2026-11-24

### Added

- Volume 1, Chapter 2, Integral closure and normalization. Section 2.1 recalls integral dependence and proves that a unique factorization domain is integrally closed. Section 2.2 proves the normalization lemma of Noether with the substitution of Nagata. Section 2.3 proves that the normalization is finite when the field extension is separable, with the trace form, and in particular for each finitely generated domain in characteristic 0. It ends with the resolution of affine curves in characteristic 0.

### Changed

- Volume 1, Corollary 1.4.3, a normal scheme of dimension at most 1 is regular, now has the node SG00000024 and its Lean proof.
- Volume 1, Corollary 2.3.6, the normalization of an affine curve in characteristic 0, now has the node SG00000027 and its Lean proof, and Section 2.3 explains the Lean proof.

## [0.2.1] - 2026-11-24

### Added

- Volume 1, Commutative algebra for resolution, with Chapter 1, Regular local rings. It has four sections: dimension and the cotangent space, regular local rings and the quotient by a parameter, the proof that a regular local ring is a domain, and the description of regular local rings of dimension 1. Each section gives complete proofs for a graduate student with references to Atiyah and Macdonald, Matsumura and the Stacks project, examples (the cusp, the node, the cone, the union of two axes), an explanation of the Lean proof and notes.
- The workflow `build` builds Volumes 0, 1 and 9.

### Changed

- `shb` reads the record of the Lean build in the form with the key `decls`, that tamnd/singularity-lean writes. Before this change it did not find the declarations, and each node had the status planned. A node with named hypotheses now has the status proved-mod.
- Volume 9, Section 1.3 refers to the full proof in Volume 1 and gives the Lean name of SG0000000J.
- `EDITION` is 0.2.1 and points to the map at the release v0.2.1 of tamnd/singularity.

## [0.2.0] - 2026-11-23

### Added

- Volume 9, The open problem, Chapter 1, The proved cases and the reductions. It has five sections: dimension 0, integral varieties in characteristic 0, the reduction to integral varieties, the bridge to formal-conjectures, and the purely inseparable hypersurfaces of P1. Each section gives the statements, complete proofs for a graduate student, examples and counterexamples, an explanation of the Lean proof, and notes with references.
- Volume 0: Theorem 2.3.2 (integral varieties in characteristic 0), Hypothesis 2.3.3 (the reduction to integral varieties), Theorem 2.3.4 (characteristic 0 from the hypothesis), Proposition 2.5.4 (the bridge to formal-conjectures) and Corollary 2.5.5 (Hironaka's theorem in the form of formal-conjectures).
- The statement kind Hypothesis in `shb`.
- The workflow `build` builds Volumes 0 and 9.

### Changed

- The edition page of Volume 0 describes the milestone S1.
- `EDITION` is 0.2.0 and points to the map after the records of S1.

## [0.1.0] - 2026-11-23

### Added

- The builder `shb`, a fork of `rhb`, the builder of The Riemann Handbook. It keeps the pipeline: Markdown, then pandoc with `filters/shb.lua`, then LaTeX with `tex/handbook.sty`, then Tectonic for the PDF, and pandoc for the EPUB 3 with MathML. It keeps the fonts, the fallback fonts and the cover.
- The content format: a volume is `content/<NN-slug>/` with a `volume.yaml`, a chapter is a folder `<NN-chapter>/` with an optional `intro.md` and one file per section. A section has the front matter `title`, `nodes`, `sources`, `status`, `drafted_by` and `reviewed_by`.
- `shb check`: checks the front matter, the `Node:` lines, the node tags and the paper keys against the map of tamnd/singularity, and the dashes and the banned words.
- `shb number --write`: writes the numbers of the statements into the section files.
- `shb build`: writes `build/singularity-handbook-<NN-slug>-<version>.pdf` and `.epub`. Each `Node:` line gets a link to the node on singularity.tamnd.com and the status of the node, computed from `records/lean.json` of the map, or "planned".
- A Draft mark on the first page of each chapter that is not `reviewed`, in the PDF and in the EPUB.
- The list of the papers that the sections of a chapter cite, at the end of the chapter.
- The option `--map PATH` and the environment variable `SHB_MAP` for the checkout of tamnd/singularity.
- Tests of `shb` on a small volume in `tests/fixture`.
- The workflows `check` (the style rules, `shb check` and the tests) and `build` (Volume 0 as PDF and EPUB, and the release on a tag `v*`), with each action pinned to a commit.
- `scripts/style.py`, the writing rules of tamnd/singularity.
- `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE` (MIT, for the builder) and `LICENSE-CONTENT` (CC BY 4.0, for the text).
- Volume 0, Section 2.3: Theorem 2.3.1, resolution in dimension 0, with its proof and its Lean name.
- Volume 0, Section 2.5: Proposition 2.5.3, the core problem P1 is a special case of the main statement, with its proof and its Lean name.

### Removed

- From `rhb`: the sources of tamnd/riemann and tamnd/riemann-lean, the ledger of declarations and its dominator tree (`corpus.py`, `ledger.py`), the links `/entry/<id>/` and their numbers, the named results, the index of Lean names, the commands `survey` and `ledger`, and the list of the riemann volumes.
