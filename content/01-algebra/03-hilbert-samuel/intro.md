# The Hilbert-Samuel function and the order

A resolution must make the singularities of a variety better in a precise sense, so we need numbers that measure how far a local ring is from regular. This chapter gives the first three such numbers. The Hilbert-Samuel function of a Noetherian local ring $(R, \mathfrak{m})$ counts the length of $R/\mathfrak{m}^n$. The order of an element $f$ counts the largest power of $\mathfrak{m}$ that contains $f$. For a hypersurface $f = 0$ in a regular ambient space, the order of $f$ at a point is the multiplicity of the hypersurface at that point, and it is the invariant that the classical proofs of resolution make smaller.

Section 3.1 defines the Hilbert-Samuel function and proves its basic laws. The main result is that the function has finite values when the ideal contains a power of a maximal ideal. Section 3.2 defines the order of an element and proves its laws, with the intersection theorem of Krull.

Section 3.3 proves the theorem of Hilbert and Serre on graded modules, and it deduces that the Hilbert-Samuel function is a polynomial in $n$ for large $n$. The Samuel multiplicity is the normalized leading coefficient of this polynomial. Section 3.3 defines it and proves its first laws. The value $e(R) = 1$ for a regular local ring is proved there only in dimension $0$ and $1$ in Lean.
