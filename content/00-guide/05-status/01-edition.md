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

No route has a new result on the open case yet. The milestone S2 proves the facts on regular local rings that the later milestones need, and the case of curves for each $p$. The milestone S2 is complete at release 0.3.0. It has these results in Lean: the theorem of Serre in both directions and the localization of regular local rings (Section 1.6), the criterion of Nagata and the openness of the regular locus over each field, perfect or not (Sections 1.7 to 1.9), the finiteness of normalization and resolution of curves in each characteristic (Chapter 2), the Hilbert-Samuel polynomial, the multiplicity and the multiplicity $1$ of a regular local ring (Section 3.3), and the regularity of the charts of the blowup of a regular local ring (Section 1.10). Volume 1 has Chapters 1 to 6 in this edition. Volume 7 has Chapter 1, on the order and the residual order in characteristic $p$. Its definitions and laws have Lean proofs, and three examples are certified in Lean: the kangaroo point (Example 1.4.2), one cycle of Hauser and Perlega (Example 1.4.5), and the example of Narasimhan (Volume 9, Example 2.2.1). The bound of Moh and the full theorem of Hauser and Perlega have no Lean proof. Volume 7 also has Chapter 2, on the point blowup. Theorem 2.2.2 of Volume 7, the order does not go up under a point blowup, has a Lean proof. Theorem 2.2.5, the points of the same order lie in the directrix, has no Lean proof. Volume 9 has Chapter 2, on the open case, with the known cases, the failures of the methods of characteristic 0, and the routes.

The other volumes of the handbook come with the milestones that formalize their tiers. The plan is in the milestone issues of tamnd/singularity.
