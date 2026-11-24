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

No route has a new result on the open case yet. The milestone S2 proves the facts on regular local rings that the later milestones need, and the case of curves for each $p$. At release 0.2.11, S2 has these results in Lean: the theorem of Serre in both directions and the localization of regular local rings (Section 1.6), the criterion of Nagata and the openness of the regular locus over a perfect field (Sections 1.7 and 1.8), the finiteness of normalization and resolution of curves in each characteristic (Chapter 2), and the Hilbert-Samuel polynomial and the multiplicity (Section 3.3). The openness of the regular locus over an imperfect field is not yet proved. Volume 1 has Chapters 1 to 6 in this edition.

The other volumes of the handbook come with the milestones that formalize their tiers. The plan is in the milestone issues of tamnd/singularity.
