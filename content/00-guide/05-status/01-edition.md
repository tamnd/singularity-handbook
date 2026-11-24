---
title: This edition
nodes: [SG00000007]
sources: []
status: drafted
drafted_by: writer
reviewed_by: []
---
## This edition

This is the second edition of Volume 0, and the first edition of Volume 9. They go with the milestone S1 of the project. At S1 the project has these results in Lean, in addition to the statements and the fidelity checks of S0.

1. Resolution in dimension 0, in each characteristic (Theorem 2.3.1).
2. Resolution of integral varieties in characteristic 0, from the Lean proof of Hironaka's Main Theorem I in resolutionorg/hironaka (Theorem 2.3.2).
3. Resolution in characteristic 0 for all varieties, from the named hypothesis that reduces the problem to integral varieties (Hypothesis 2.3.3 and Theorem 2.3.4). At S1 the Lean proof of the hypothesis was planned, so the map gave this result the status "proved-mod". Release 0.2.5 of the Lean package proves the reduction (Theorem 2.3.3), and the status is now "proved".
4. The bridge to google-deepmind/formal-conjectures (Proposition 2.5.4), and Hironaka's theorem in the form of formal-conjectures, with no hypothesis (Corollary 2.5.5).

Volume 9, Chapter 1 gives the complete proofs of these results, with examples, and it explains how each Lean proof follows the argument.

The open case has this status.

Node: SG00000007 · Lean: `Singularity.ResolutionDimFourCharP`

No route has a new result on the open case yet. The milestone S2 proves the facts on regular local rings that the later milestones need, and the case of curves for each $p$. The milestone S2 is complete at release 0.3.0. It has these results in Lean: the theorem of Serre in both directions and the localization of regular local rings (Section 1.6), the criterion of Nagata and the openness of the regular locus over each field, perfect or not (Sections 1.7 to 1.9), the finiteness of normalization and resolution of curves in each characteristic (Chapter 2), the Hilbert-Samuel polynomial, the multiplicity and the multiplicity $1$ of a regular local ring (Section 3.3), and the regularity of the charts of the blowup of a regular local ring (Section 1.10). Volume 1 has Chapters 1 to 6 in this edition. Volume 7 has Chapter 1, on the order and the residual order in characteristic $p$. Its definitions and laws have Lean proofs, and three examples are certified in Lean: the kangaroo point (Example 1.4.2), one cycle of Hauser and Perlega (Example 1.4.5), and the example of Narasimhan (Volume 9, Example 2.2.1). The bound of Moh and the full theorem of Hauser and Perlega have no Lean proof. Volume 7 also has Chapter 2, on the point blowup. Theorem 2.2.2 of Volume 7, the order does not go up under a point blowup, has a Lean proof. Theorem 2.2.5, the points of the same order lie in the directrix, also has a Lean proof. Section 1.4 of Volume 7 reports the experiments E1 and E2 of the lab, which test the bound of Moh and four candidate secondary invariants on random point blowups. The milestone S3 is complete at release 0.4.0. Volume 9 has Chapter 2, on the open case, with the known cases, the failures of the methods of characteristic 0, and the routes. Volume 4, on surfaces, comes with the milestone S4. In this edition it has three chapters: the blowup of a surface, the theorem of Lipman and rational singularities, and embedded resolution. Theorem 1.1.11 of Volume 4 and Corollary 1.1.12, the blowup along a regular curve on a regular surface is an isomorphism, have Lean proofs. The theorem of Lipman and the embedded resolution of surfaces have no Lean proof yet. The embedded resolution of surfaces has a Lean statement in a weaker form, for a regular scheme of finite type over a field (Volume 4, Section 3.1). Volume 3, on valuations, comes with the milestone S5. In this edition it has four chapters: valuation rings and the Zariski-Riemann space, the Abhyankar inequality, extensions of valuations with the defect and the key polynomials of MacLane, and local uniformization. The quasi-compactness of the Zariski-Riemann space (Theorem 1.5.3 of Volume 3), the Abhyankar inequality (Theorem 2.1.5 of Volume 3) and its relative form have Lean proofs. The other statements of Volume 3 with a map node have no Lean statement yet, and the theorems of local uniformization are stated with their sources and not proved.

The other volumes of the handbook come with the milestones that formalize their tiers. The plan is in the milestone issues of tamnd/singularity.
