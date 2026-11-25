---
title: The known cases
nodes: [SG00000007, SG0000001B, SG0000001C, SG0000001D, SG0000001V, SG0000001F]
sources: [Lip78, Art86, CJS20, Abh66, Cut09, CP08, CP09, CP19, Kol20, BMP20, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The known cases

The definitions of resolution and of $\mathrm{Res}(p, n)$ are those of Chapter 1. In this section we state the theorems that give $\mathrm{Res}(p, n)$ for $n \le 3$, and we say what is still open in these dimensions. We do not prove these theorems. Their proofs are long, and the project has not formalized them. Each statement has its node on the map, and the map gives its status.

### The open problem

**Conjecture 2.1.1.** Let $p$ be a prime. Each variety of dimension 4 over a field of characteristic $p$ has a resolution.

Node: SG00000007 · Lean: `Singularity.ResolutionDimFourCharP`

By Theorem 1.5.5, Conjecture 2.1.1 contains the core problem P1 for $n = 4$: the hypersurfaces $z^p + g(x_1, \dots, x_4) = 0$. Thus a counterexample to P1 in four variables $x$ would refute Conjecture 2.1.1. The project expects neither a quick proof nor a counterexample. The rest of this chapter explains why.

### Surfaces

**Theorem 2.1.2 (Lipman).** Let $X$ be a reduced excellent Noetherian scheme of dimension at most 2. Then $X$ has a resolution. In particular, $\mathrm{Res}(p, 2)$ holds for each $p$.

Node: SG0000001B · Lean: `Singularity.ResolutionInDim` (the statement only)

The proof of Lipman [Lip78] is not embedded. It alternates two steps: the normalization, and the blowup of the singular points. A normal surface has only finitely many singular points, so each blowup has a finite center. Lipman proves that the process stops after finitely many steps. The proof uses the rational singularities of surfaces. Artin gives a shorter account in [Art86].

The embedded problem for surfaces is also solved.

**Theorem 2.1.3 (Cossart-Jannsen-Saito).** Let $Z$ be a regular excellent scheme and let $X \subseteq Z$ be a reduced closed subscheme of dimension at most 2. There is a canonical sequence of blowups in permissible centers after which the strict transform of $X$ is regular and has normal crossings with the exceptional divisor.

Node: SG0000001C · Lean: `Singularity.EmbeddedResolutionSurface` (the statement only, in a weaker form)

The Lean statement is weaker than Theorem 2.1.3 in two ways. Mathlib has no excellent schemes, so $Z$ is of finite type over a field. Mathlib has no blowups of schemes, so the statement asks for one proper morphism and not for a sequence of permissible blowups.

The proof [CJS20] uses the Hilbert-Samuel function of Volume 1, the directrix, and the characteristic polyhedron of Hironaka. It is free of the characteristic, and it includes the case of mixed characteristic. It is the main source of invariants for the route of characteristic polyhedra in Section 2.3.

### Threefolds

Abhyankar proved resolution of threefolds over an algebraically closed field of characteristic $p > 5$ [Abh66]. Cutkosky gave a shorter proof of the same theorem [Cut09]. Cossart and Piltant then removed the conditions on $p$ and on the field.

**Theorem 2.1.4 (Cossart-Piltant).** Let $X$ be a reduced quasi-excellent Noetherian scheme of dimension at most 3. Then there is a proper birational morphism $Y \to X$ with $Y$ regular that is an isomorphism over the regular locus of $X$. In particular, $\mathrm{Res}(p, 3)$ holds for each $p$.

Node: SG0000001V · Lean: `Singularity.resolution_quasiExcellent_three` (planned, no Lean statement yet)

Node: SG0000001D · Lean: `Singularity.ResolutionInDim` (the statement only)

The proof is in three papers. The first two [CP08, CP09] prove birational resolution of threefolds over a field $k$ of characteristic $p > 0$ that is differentially finite over a perfect subfield, that is, there is a perfect subfield $k_0 \subseteq k$ such that $\Omega_{k/k_0}$ is a finite-dimensional $k$-vector space. The third [CP19] removes this hypothesis, and it proves the statement above, which is the resolution conjecture of Grothendieck in dimension 3. The method is the method of Zariski. First, the authors prove local uniformization along each valuation.

**Theorem 2.1.5 (Cossart-Piltant).** Let $K$ be a function field of transcendence degree 3 over a field $k$ of characteristic $p > 0$. Each valuation of $K$ over $k$ has local uniformization.

Node: SG0000001F · Lean: `Singularity.localUniformization_three` (the statement only)

Then they patch the local solutions together. Section 2.3 defines local uniformization and explains the patching. For local uniformization, Cossart and Piltant reduce to purely inseparable equations and to Artin-Schreier equations, and they control them with the characteristic polyhedron. Their arguments project the polyhedron to the space of two variables, and they treat many cases one at a time. This analysis is special to three variables.

### What is still open in dimension 3

Theorem 2.1.4 is a non-embedded resolution. Embedded resolution of a threefold in a smooth fourfold by a sequence of blowups in regular centers is open in characteristic $p$. Kollár constructs resolutions with an ample exceptional divisor from projective resolutions, and he gets such resolutions for arithmetic singularities of dimension 3 [Kol20]. Bhatt, Ma, Patakfalvi, Schwede, Tucker, Waldron and Witaszek develop the minimal model program for arithmetic threefolds whose residue characteristics are greater than 5 [BMP20]. Neither result is an embedded resolution by a sequence of blowups in regular centers. Thus the embedded problem in dimension 3 and the problem in dimension 4 are close. A method that solves the problem in dimension 4 must at least handle the embedded problem in dimension 3.

### Notes and references

The survey of Hauser [Hau10] explains the problem in characteristic $p$ for a general reader, and it gives the history up to 2010. The theorems of this section are all proved by methods that do not extend directly to dimension 4. Section 2.2 explains the main reasons.
