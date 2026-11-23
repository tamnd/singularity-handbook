---
title: What the handbook is
nodes: []
sources: [Hir64, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## What the handbook is

Resolution of singularities asks for a regular variety that maps properly and birationally onto a given variety. Hironaka proved that each variety over a field of characteristic 0 has a resolution. In characteristic $p > 0$ the problem is solved in dimension at most 3 and open in dimension 4 and higher. Hauser's survey gives the reasons why the methods of characteristic 0 fail in characteristic $p$.

The handbook has ten volumes. Volume 0 is this guide. Volumes 1 to 8 explain the known theory: commutative algebra, characteristic 0, valuations, curves and surfaces, local uniformization, threefolds, the invariants of characteristic $p$, and alterations. Volume 9 reports on the open problem. It changes at each milestone of the project.

The handbook is a part of a project that states the problem in Lean 4 and works on it. The handbook follows the published proofs. It is not a translation of Lean code. Where a result has a Lean form, the handbook gives the name of the Lean declaration and the status of the proof.

**The open case is not proved.** No part of this handbook gives a proof of resolution in dimension 4 and characteristic $p$. Volume 9 describes the work on the open case and says which results are new, which are checked in Lean, and which are only conjectures.
