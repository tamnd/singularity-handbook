# The Hilbert-Samuel function and the order

A resolution must make the singularities of a variety better in a precise sense, so we need numbers that measure how far a local ring is from regular. This chapter gives the first two such numbers. The Hilbert-Samuel function of a Noetherian local ring $(R, \mathfrak{m})$ counts the length of $R/\mathfrak{m}^n$. The order of an element $f$ counts the largest power of $\mathfrak{m}$ that contains $f$. For a hypersurface $f = 0$ in a regular ambient space, the order of $f$ at a point is the multiplicity of the hypersurface at that point, and it is the invariant that the classical proofs of resolution make smaller.

Section 3.1 defines the Hilbert-Samuel function and proves its basic laws. The main result is that the function has finite values when the ideal contains a power of a maximal ideal. Section 3.2 defines the order of an element and proves its laws, with the intersection theorem of Krull.

The Samuel multiplicity of a general local ring is the normalized leading coefficient of the Hilbert-Samuel polynomial. The existence of this polynomial is the theorem of Hilbert and Samuel [AM69, Proposition 11.4]. We state it in Remark 3.1.7, but this edition does not prove it, and it has no Lean proof yet.
