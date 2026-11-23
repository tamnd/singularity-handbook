# Introduction

This volume gives the commutative algebra that the theory of resolution uses. A resolution replaces a singular variety by a regular one, so the first object of study is the regular local ring. The volume then treats the tools that measure how far a local ring is from regular: the Hilbert-Samuel function and the multiplicity, completion and the Cohen structure theorem, excellence and the openness of the regular locus, integral closure and normalization, and, in characteristic $p$, differential operators and the Frobenius map.

The reader we have in mind knows the book of Atiyah and Macdonald [AM69]: localization, Noetherian rings, integral dependence and the dimension theory of Chapter 11. We use Matsumura [Mat] and the Stacks project [Stacks] as the main references for the rest. We give complete proofs of the results that the project uses in Lean, and we give references for the results that we only state.

Each statement that has a Lean proof has a `Lean:` line with the name of the declaration, and each statement on the map of the project has a `Node:` line. A statement with the line "Lean: none yet" has no Lean proof. The reader who does not read Lean can skip these lines and the sections "The Lean proof".

This edition has Chapter 1, on regular local rings. The other chapters come with the milestones S2 and S3 of the project.
