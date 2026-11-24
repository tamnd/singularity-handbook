---
title: The open case of dimension four
nodes: [SG00000007, SG0000001H, SG0000001J, SG00000009, SG0000001X, SG00000014, SG00000015, SG00000016, SG00000017]
sources: [CP19, CP08, Moh87, HP19a, Hau10, Hir67, CJSch19, CSch21]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The open case of dimension four

This section says what a proof in dimension 4 along the lines of Cossart and Piltant would need, and it points to the statements of Volume 9. We prove no new result here. The section is a map of the gaps.

### The statements

Resolution of varieties of dimension 4 in characteristic $p$ is Conjecture 2.1.1 of Volume 9.

Node: SG00000007 · Lean: `Singularity.ResolutionDimFourCharP`

The method of Zariski splits it into two statements: local uniformization in transcendence degree 4, Conjecture 2.3.1 of Volume 9, and the patching of local solutions in dimension 4, Conjecture 2.3.2 of Volume 9. Both are open.

Node: SG0000001H · Lean: `Singularity.LocalUniformizationFour` (the statement only)

Node: SG0000001J · Lean: `Singularity.resolution_of_localUniformization_four` (the statement only)

The equations of Section 2.3 in four variables, $z^p + g(x_1, \dots, x_4)$, are the case $n = 4$ of the problem P1, Conjecture 1.5.1 and Conjecture 2.3.7 of Volume 9. By Theorem 1.5.5 of Volume 9, resolution in dimension 4 implies this case.

Node: SG00000009 · Lean: `Singularity.PurelyInseparableHypersurfaceResolution`

Node: SG0000001X · Lean: `Singularity.purelyInseparableHypersurfaceResolution_of_resolutionInDim`

### The plan of Cossart and Piltant in dimension four

We sort the proof of Theorem 1.1.3 into four parts, close to the plan of Section 1.2. For each part we say what is known when $n = 4$.

1. *The reduction to degree $p$.* The plan of proof of Proposition 2.2.1 has four steps. Steps 2 and 4, the Noether normalization and the ramification theory of valuations, do not use the dimension. For varieties, Step 1, the patching, becomes Conjecture 2.3.2 of Volume 9 when $n = 4$. Step 3 and condition (E) use principalization and embedded resolution in dimension 3 (Section 4.1). Their analogues in dimension 4 are open.
2. *The polyhedron and the invariants.* The polyhedron of Hironaka, the invariants $\delta$, $\epsilon$, $\omega$ and $\iota$, and Theorems 3.2.6 and 3.2.7 hold for each $n$ (Section 4.1).
3. *The decrease.* An analogue of the Projection Theorem for $n = 4$ is not known. The projection of [CP19] maps a polyhedron in $\mathbb{R}^3$ to a polygon in $\mathbb{R}^2$, and for $n = 4$ there is no known replacement. The phenomenon of Example 4.1.1 and the open questions of [CP19, Remark 3.19 and Section 9.2.1] enter here.
4. *Small multiplicity.* The step from multiplicity less than $p$ to a regular point is [CP14] for $n = 3$.

So part 2 is available, and parts 1, 3 and 4 need new theorems. Part 3 is the core of the problem. A proof of an analogue of Theorem 1.2.6 for $n = 4$ would not be enough by itself, because the reduction of part 1 also uses dimension 3. Volume 9, Section 2.3, describes this route, the route of characteristic polyhedra, together with the other routes.

Node: SG00000014 · Lean: `Singularity.charPolyhedron` (the definition, invariance under $z \mapsto z + \psi$, and one direction of the vertex criterion) and Volume 7, Proposition 1.2.7, for $z^q + F$ with $F$ clean

Cossart, Jannsen and Schober prove that the characteristic polyhedron is intrinsic [CJSch19], and Cossart and Schober use it to build an invariant that drops for surfaces without completion [CSch21]. These results are steps toward a theory of the polyhedron that does not depend on the dimension 3.

### Degree p and the residual order

The reduction of Chapter 2 needs only equations of degree $p$. This is the reason why the examples of Volume 7 do not contradict the method of Cossart and Piltant. The kangaroo example, Example 1.4.2 of Volume 7, has degree $q = 4$, and the cycle of Hauser and Perlega, Theorem 1.4.3 of Volume 7, has degree $q = p^3$.

Node: SG00000016 · Lean: `Singularity.Examples.kangaroo` (the computation of Example 1.4.2 of Volume 7)

Node: SG00000017 · Lean: none yet (one cycle is certified, Example 1.4.5 of Volume 7)

For $q = p$, Moh's bound allows an increase of the residual order by at most $1$ under a permissible blowup, and Example 3.3.1 shows such an increase. Proposition 3.2.4 shows that, for $X^p + f$ over a perfect field, the residual order is the invariant $\epsilon$ of Cossart and Piltant, and Theorem 3.2.6 shows that $\omega \in \{\epsilon - 1, \epsilon\}$ does not increase. Both facts hold for each $n$. So for the equations $z^p + g(x_1, \dots, x_4)$ the difficulty is not an increase of $\omega$ but the lack of a proof that it decreases.

Node: SG00000015 · Lean: `Singularity.moh_bound` (the statement only, not proved)

Hauser and Perlega study the residual order in all dimensions [HP19a], and Hauser explains why the equations $z^p + g$ are the core of the problem [Hau10]. Volume 7 develops this approach, and Volume 9, Section 1.5, states the problem P1 for these equations.

### Lean

The map has Lean statements for the conjectures of Volume 9 that we quote, and none of them is proved. The Lean work on the characteristic polyhedron and on Moh's bound belongs to other parts of the project. This volume does not claim a Lean proof of any statement in Chapters 3 and 4.

### Notes and references

For the open problems in dimension 4 and the other routes see Volume 9, Chapter 2. For the residual order see Volume 7, Chapter 1.
