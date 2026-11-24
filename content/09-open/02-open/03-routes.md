---
title: The routes to dimension 4
nodes: [SG0000001H, SG0000001J, SG0000001E, SG0000001G, SG00000014, SG00000019, SG0000001R, SG00000009, SG0000001K, SG0000001M, SG0000001N]
sources: [Zar40, Zar44, Pil, KK05, Cut20, Tem13, Tem23, HOST26, Hir67, CJS20, CP08, CJSch19, CSch21, BV10, BenV13, BBE24, BBE25, Kaw07, KM16, ATW24, McQ20, Abr25, TemD1, TemD2, Hau10, HW14, HP19a, HP24, dJ96, ILO14, Tem17]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The routes to dimension 4

A route is a method of proof that works in dimension at most 3, or in characteristic 0, and that has a known obstruction in dimension 4. In this section we describe five routes. For each route we give the main sources, the results that hold in all dimensions, and the step that is missing. The project works on several routes at the same time, because nobody knows which one can succeed.

### Valuations: local uniformization and patching

Let $K$ be a function field over a field $k$, and let $v$ be a valuation of $K$ that is trivial on $k$. Let $X$ be a variety over $k$ with function field $K$. If the valuation ring of $v$ dominates a local ring $\mathcal{O}_{X,x}$, then $x$ is the *center* of $v$ on $X$. The valuation $v$ has *local uniformization* if, for each such $X$ on which $v$ has a center, there are a variety $X'$ with function field $K$ and a proper birational morphism $X' \to X$ such that the center of $v$ on $X'$ is a regular point.

Zariski's method has two steps [Zar40, Zar44]. First, prove local uniformization for each valuation. Second, the space of all valuations, the Zariski-Riemann space, is quasi-compact. So finitely many of the local solutions are enough, and the second step patches them into one regular variety. Zariski did both steps in characteristic 0 in dimension at most 3. Cossart and Piltant did both steps in characteristic $p$ in dimension 3 (Section 2.1). Volume 3 proves the quasi-compactness (Theorem 1.5.3) and the reduction of the first step to finitely many models (Proposition 4.1.2).

**Conjecture 2.3.1.** Let $K$ be a function field of transcendence degree 4 over a field of characteristic $p > 0$. Each valuation of $K$ has local uniformization.

Node: SG0000001H · Lean: `Singularity.LocalUniformizationFour` (the statement only)

**Conjecture 2.3.2 (patching in dimension 4).** Let $p$ be a prime, and let $X$ be a variety of dimension 4 over a field of characteristic $p$. If each valuation of the function field of each irreducible component of $X$ has local uniformization, then $X$ has a resolution.

Node: SG0000001J · Lean: `Singularity.resolution_of_localUniformization_four` (the statement only)

The Lean statements use the affine form of local uniformization (Volume 3, Proposition 4.1.6). The Lean statement of Conjecture 2.3.2 is for characteristic $p$. Its hypothesis is local uniformization in each transcendence degree at most 4, because a variety of dimension 4 can have components of smaller dimension. Local uniformization in transcendence degree at most 3 is known (Section 2.1), so this hypothesis is the same as Conjecture 2.3.1.

Conjecture 2.3.2 is open for each prime $p$. In characteristic 0 the same statement is true, because the global algorithm of Hironaka gives the resolution. But no proof of the patching step in dimension 4 by the method of Zariski is known in characteristic 0 either. Piltant gives an axiomatic form of Zariski's patching theorem in [Pil]. Thus the route of valuations needs two new theorems in dimension 4, not one.

The results that hold in all dimensions are these. A valuation is an *Abhyankar valuation* if the Abhyankar inequality is an equality for it. Volume 3, Chapter 2, proves the inequality and studies the case of equality.

**Theorem 2.3.3 (Knaf-Kuhlmann).** Each Abhyankar valuation of a function field has local uniformization.

Node: SG0000001E · Lean: `Singularity.localUniformization_abhyankar` (the statement only)

Knaf and Kuhlmann prove this with a separable extension of the residue fields [KK05], and Cutkosky removes this condition [Cut20]. The valuations that are not Abhyankar valuations are the hard case. They can have defect (Section 2.2).

**Theorem 2.3.4 (Temkin).** Let $v$ be a valuation of a function field $K$, and let $S$ be a finite subset of $\mathcal{O}_v$. Then there is a finite purely inseparable extension $L$ of $K$, which depends on $S$, such that the extension of $v$ to $L$ has a regular center on an affine model of $L$ that contains $S$.

Node: SG0000001G · Lean: `Singularity.localUniformization_inseparable` (the statement only)

Temkin proves this in [Tem13]. He also reduces local uniformization to valuations of height one [Tem23]. Herrera Govantes, Olalla Acosta, Spivakovsky and Teissier prove that valuations have tight extensions to the completion [HOST26]. This was a conjecture of Teissier, and it is a step in his program for local uniformization.

### Characteristic polyhedra

Let $f = z^m + \sum_{k < m} a_k(x) z^k$ in $K[[x, z]]$. Volume 7, Section 1.2, defines the projected polyhedron of $f$ and the characteristic polyhedron, which is the intersection of the projected polyhedra over all choices of $z$ [Hir67]. The characteristic polyhedron does not depend on the choice of $z$. Cossart, Jannsen and Schober prove that it is intrinsic [CJSch19], and Cossart and Schober build from it an invariant that drops in dimension 2 without completion [CSch21].

Node: SG00000014 · Lean: `Singularity.charPolyhedron` (the definition, invariance under $z \mapsto z + \psi$, and one direction of the vertex criterion) and Volume 7, Proposition 1.2.7, for $z^q + F$ with $F$ clean

The polyhedron exists in each dimension, and the first invariants of [CJS20] (the Hilbert-Samuel function and the directrix) do not go up in each dimension. The missing step is an invariant of the polyhedron that drops for $z^p + g(x_1, \dots, x_4)$. In dimension 3, Cossart and Piltant control the polyhedron by projections to two variables [CP08]. No such control is known for a polyhedron in the space of four variables.

### Rees algebras and idealistic filtrations

The school of Villamayor replaces an ideal by a Rees algebra that is closed under Hasse-Schmidt derivations. Then the elimination algebra replaces the hypersurface of maximal contact [BV10, BenV13]. Benito and Villamayor use a new invariant from elimination algebras to give embedded resolution of surfaces [BenV13]. Kawanoue and Matsuki use idealistic filtrations and a leading generator system in [Kaw07] and [KM16]. Benito, Bravo and Encinas define the Samuel slope of a local ring [BBE24].

**Theorem 2.3.5 (Benito-Bravo-Encinas).** A Noetherian local ring is regular if and only if its Samuel slope is infinite.

Node: SG00000019 · Lean: `Singularity.samuelSlope_eq_top_iff` (planned, no Lean statement yet)

This is [BBE25]. In each of these programs the invariants are defined in all dimensions. The missing step is to prove that they drop. In characteristic $p$ the elimination algebra loses information, and the final case of the induction is not a monomial case as in characteristic 0.

### Weighted blowups

In characteristic 0, Abramovich, Temkin and Włodarczyk [ATW24], and McQuillan [McQ20], resolve singularities by weighted blowups. The invariant is simpler than that of Hironaka, and it drops at each step. Temkin gives an axiomatic frame for this method in [TemD1, TemD2]. In this frame the method needs only enough derivations, and this is exactly what characteristic $p$ lacks.

**Conjecture 2.3.6.** There is an invariant of a singular point in characteristic $p$, of the form of the weighted invariant, that drops under a weighted blowup of a fourfold.

Node: SG0000001R · Lean: `Singularity.WeightedInvariantCharP` (planned, no Lean statement yet)

Section 2.2 gives the obstructions for this route. The natural analogue of the invariant fails in characteristic 2 [Abr25], and weighted blowups cannot keep the normal crossings locus of a pinch point. Conjecture 2.3.6 is vague, because it does not fix the form of the invariant. The map uses it as a research target, not as a precise statement.

### The purely inseparable equations

The hypersurfaces $z^q + F(x_1, \dots, x_n)$ with $q = p^e$ are the core case [Hau10]. Volume 7, Chapter 1, studies them. In two variables $x$, Hauser and Wagner study $z^p + g(x, y)$ with a correction term for the residual order [HW14]. Hauser and Perlega give embedded resolution of these surfaces in 3-space with a modified residual order [HP24]. The modification pays for the increases at the kangaroo points.

**Conjecture 2.3.7.** Let $k$ be a field of characteristic $p$ and let $g \in k[x_1, \dots, x_n]$. If the hypersurface $z^p + g = 0$ is reduced, then it has a resolution.

Node: SG00000009 · Lean: `Singularity.PurelyInseparableHypersurfaceResolution`

For $n \le 3$ the hypersurface has dimension at most 3, and Theorem 2.1.4 gives the resolution. For $n = 4$ it is the first open case, and Theorem 1.5.5 shows that it is a special case of Conjecture 2.1.1. The missing step is a correction term for the residual order in four variables. The cycles of [HP19a] are the first test for each candidate. A candidate must not go to infinity along a cycle.

### Alterations

An *alteration* of a variety $X$ is a proper, surjective and generically finite morphism $X' \to X$ from a variety of the same dimension. A resolution is an alteration of degree 1. In all dimensions and in each characteristic, regular alterations exist.

**Theorem 2.3.8 (de Jong).** Each variety over a field has a regular alteration.

Node: SG0000001K · Lean: `Singularity.exists_regular_alteration` (planned, no Lean statement yet)

**Theorem 2.3.9 (Gabber).** Let $\ell \ne p$ be a prime. Each variety over a field of characteristic $p$ has a regular alteration of degree prime to $\ell$.

Node: SG0000001M · Lean: `Singularity.exists_regular_alteration_coprime` (planned, no Lean statement yet)

**Theorem 2.3.10 (Temkin).** Each variety over a perfect field of characteristic $p$ has a regular alteration whose degree is a power of $p$.

Node: SG0000001N · Lean: `Singularity.exists_regular_p_alteration` (planned, no Lean statement yet)

These are [dJ96], [ILO14] and [Tem17]. The degree of an alteration is the degree of the extension of the function fields. By Theorems 2.3.9 and 2.3.10, the degree can avoid each prime $\ell \ne p$, and it can be a power of $p$. It cannot be 1 by these methods. A route through alterations must descend a resolution of $X'$ to $X$. Assume that the extension of the function fields is Galois with group $G$. Then $X$ is birational to the quotient $X'/G$. When the degree is a power of $p$, the group $G$ is a $p$-group, and its action in characteristic $p$ is wild. Theorem 2.3.10 does not give a Galois extension, so this case is only a model of the difficulty. Volume 8, Chapter 3 gives the precise statements. Nobody knows how to resolve such quotients in dimension 4 in general.

### Notes and references

The routes are in the order of the map. The weights that the project gives them, and their first nodes, are in the document of the routes in tamnd/singularity. Other methods exist. Teissier's program uses overweight deformations of toric varieties, and other programs use jet schemes and Berkovich spaces. The project records these methods on the map, and this handbook will describe them when the project has results on them.
