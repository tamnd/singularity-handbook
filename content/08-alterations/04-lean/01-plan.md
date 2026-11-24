---
title: Nodes and a plan
nodes: [SG0000001K, SG0000001M, SG0000001N, SG0000001G, SG00000002, SG0000000V, SG00000004, SG0000004K, SG0000004G, SG0000004H, SG0000004J]
sources: [dJ96, DM69, Knu83, ILO14, Tem17]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Nodes and a plan

### The nodes of the map

The theorems of this volume are on route R6 of the map, the route through alterations. The table lists the nodes and their state in the Lean library.

| Node | Content | Section | Lean |
| --- | --- | --- | --- |
| SG0000001K | de Jong, regular alterations | Theorem 1.2.1 | `Singularity.exists_regular_alteration`, planned, no statement yet |
| SG0000001M | Gabber, degree prime to $\ell$ | Corollary 3.2.5 | `Singularity.exists_regular_alteration_coprime`, planned, no statement yet |
| SG0000001N | Temkin, degree a power of $p$ | Corollary 3.3.3 | `Singularity.exists_regular_p_alteration`, planned, no statement yet |
| SG0000001G | inseparable local uniformization | Section 3.3 | `Singularity.localUniformization_inseparable`, statement only |
| SG00000002 | regular schemes | Theorem 1.2.1 | `Singularity.IsRegularScheme` |
| SG0000000V | divisors with simple normal crossings | Definition 1.1.10 | `Singularity.IsSncDivisor` |
| SG00000004 | resolutions | Proposition 1.3.4 | `Singularity.IsResolution` |
| SG0000004K | de Jong, regular model of a semistable curve | Theorem 2.1.8 | none yet |
| SG0000004G | Deligne-Mumford, Knudsen, moduli of stable pointed curves | Theorem 2.2.2 | none yet |
| SG0000004H | the level-$\ell$ moduli | Hypothesis 2.2.4 | none yet |
| SG0000004J | extension after an alteration | Hypothesis 2.2.5 | none yet |

The node SG0000001K uses SG00000002, SG0000000V and SG0000004J, and its note records Q-08. The nodes SG0000001M and SG0000001N use SG0000001K, and SG0000001N also uses SG0000001G. The node SG0000004J uses SG0000004H, and SG0000004H uses SG0000004G. The stable reduction theorem is part of the properness in SG0000004G, and the map has no separate node for it. The map has no node for the definition of a semistable curve in Section 2.1.

### The named hypothesis

Q-08 asks for a first form of the theorem of de Jong that takes the moduli of stable curves as a hypothesis. Chapter 2 gives two candidates.

1. Hypothesis 2.2.4 states the existence and the projectivity of the fine moduli scheme of stable $n$-pointed curves with level-$\ell$ structure. This is the input that [dJ96, 2.24] takes from [DM69] and [Knu83]. A Lean form would need the definitions of a stable curve, of a level structure, and of the functor that the moduli scheme represents.
2. Hypothesis 2.2.5 states only the consequence that the proof uses: a smooth proper pointed curve over a dense open subset extends, after a projective generically étale alteration of the base, to a stable pointed curve over the whole base. Proposition 2.2.6 deduces it from Hypothesis 2.2.4.

We propose Hypothesis 2.2.5 as the named hypothesis of the first Lean statement. It needs the definitions of a family of semistable and of stable pointed curves, but no moduli functor, no level structure and no representability. It is also the exact point where Chapter 2 uses the moduli, in Step 6 of Section 2.3. The statement with Hypothesis 2.2.4 can come later, together with a Lean proof of Proposition 2.2.6. A formalization of [DM69] itself is a large separate project.

The proposed Lean statement has the form "Hypothesis 2.2.5 implies Theorem 1.2.1". Its conclusion uses `Singularity.IsRegularScheme` and `Singularity.IsSncDivisor`, which are in the library. It also needs a definition of an alteration of an integral scheme, Definition 1.1.1, which is not in the library. The name of the hypothesis and the name of the definition are not fixed. The node SG0000001K plans the name `Singularity.exists_regular_alteration` for the theorem.

### The pieces that the proof needs

The proof of Chapter 2 uses the following results. For each we give the state of the library.

1. Blowups of ideals and their charts (Volume 4, Chapter 1). The library has the algebraic charts, for example `Singularity.Algebra.blowupChart`. It has no global blowup of a scheme along an ideal sheaf with its universal property.
2. Normalization in a finite extension of the function field, and its finiteness (Volume 1, Theorem 2.4.7). The library has the normalization of a curve, `Singularity.Curves.normalizationHom`, with `Singularity.Curves.isFinite_normalizationHom`. It has no normalization of a variety of higher dimension in an extension field.
3. The lemma of Chow, the theorem of flattening of Raynaud-Gruson [dJ96, 2.19], and the generic projections of Lemma 2.3.3. None of them is in the library.
4. Semistable and stable curves, and the local structure of Proposition 2.1.2 [dJ96, 2.23]. Not in the library.
5. The local computations: Lemma 2.1.3, Proposition 2.1.5 and Proposition 2.4.3. These are statements on explicit rings, and they are the best first targets. Lemma 2.1.3 says that $A[[u, v]]/(uv - h)$ is regular if and only if $h \notin \mathfrak{m}_A^2$. The other two describe the charts of a blowup of an explicit ideal, which is the kind of statement that the algebraic charts of the library treat.
6. The criterion for strict normal crossings, Lemma 1.1.11. The library has `Singularity.isSncAt_of_isRegularLocalRing_quotient`, which treats one component: a prime $P$ of a regular local ring $R$ with $R/P$ regular of dimension $\dim R - 1$ gives a divisor with simple normal crossings at $P$. This is close to the case $r = 1$ of Lemma 1.1.11.

For Chapter 3, the field theory of Proposition 3.1.1 rests on `Singularity.Algebra.isPurelyInseparable_fixedField_top` (Volume 1, Lemma 2.4.5). Lemma 3.2.2 is finite group theory and Galois theory, and Mathlib has the Sylow theorems and the Galois correspondence. The theorems of Gabber and Temkin need the modification theorem of Gabber and log geometry [ILO14], and the tame distillation of [Tem17]. We see no short path to them in Lean.

### Summary

The first Lean goal for this volume is the statement "Hypothesis 2.2.5 implies the theorem of de Jong", with the local computations of Sections 2.1 and 2.4 proved as lemmas. The global inputs (blowups, normalization, Chow, flattening, projections) are general library work that other volumes also need. The refinements of Chapter 3 are far from the library.
