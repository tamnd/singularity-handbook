# The theorem in the Lean library

The Lean library of the project, tamnd/singularity-lean, states resolution of singularities for each characteristic and each dimension. In characteristic 0 it proves the statement, but it does not prove it from the mathematics of Chapters 2 and 3. It takes Hironaka's Main Theorem I from the library resolutionorg/hironaka [HirLean], which we call the base, and it uses that theorem as a black box. This chapter explains the Lean statement, how the library gets it from the base, and what the project checks.

Section 4.1 compares the Lean statement with Theorem 1.1.1 and gives the chain of Lean theorems from the base to the statement. Section 4.2 lists the checks, and it gives the nodes of the map and the Lean names for the results of this volume. It also lists the results of this volume that have no node.
