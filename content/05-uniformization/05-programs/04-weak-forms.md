---
title: Weak forms and the status of the programs
nodes: [SG0000001K, SG0000001M, SG0000001N, SG0000001G, SG0000001H, SG0000001J, SG00000007]
sources: [dJ96, dJ97, AdJ97, ILO14, Tem17, Tem13, Tem23, KK05, KK09, Cut15, Cut20, CM17, Kuh10b, KR23, CKR25, Nov24, NS14, HOST26, Zar44, Abh66, CP08, CP09, CP19, CJS20, BV10, BenV13, BBE25, KM16, ATW24, McQ20, AQS24, AQS25, AT26, HP24, HW14, Hau10, Cut99, Hir17]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Weak forms and the status of the programs

Some theorems give a weak form of resolution or of local uniformization in each dimension and in each characteristic. They replace the birational map by a generically finite one, or they make the function field larger. Volume 8 treats them in detail. In this section we recall what they give for local uniformization and what they do not give. We end with a table of the status of the programs of this chapter.

### Alterations

An *alteration* of a variety $X$ is a proper, surjective and generically finite morphism $X' \to X$ from a variety of the same dimension. Its degree is the degree of the extension of the function fields. A resolution is an alteration of degree 1. These are theorems.

1. *de Jong.* Each variety over a field has a regular alteration, and one can ask that the inverse image of a given proper closed subset is a divisor with strict normal crossings [dJ96]. Volume 8, Theorem 1.2.1, and Volume 9, Theorem 2.3.8, state the theorem. de Jong also proves a form for families of curves and a Galois form [dJ97], and Abramovich and de Jong treat smoothness, semistability and toroidal geometry [AdJ97].
2. *Gabber.* Let $\ell$ be a prime different from the characteristic. Each variety has a regular alteration of degree prime to $\ell$, and each Noetherian quasi-excellent scheme on which $\ell$ is invertible has local uniformization for the topology of $\ell'$-alterations [ILO14]. Volume 8, Theorems 3.2.4 and 3.2.8, and Volume 9, Theorem 2.3.9, state these results.
3. *Temkin.* Each variety over a perfect field of characteristic $p$ has a regular alteration whose degree is a power of $p$ [Tem17]. Volume 8, Theorem 3.3.2, states the general form for schemes of finite type over a quasi-excellent base of dimension at most 3, and Volume 9, Theorem 2.3.10, states the case of varieties.

So the degree of a regular alteration can avoid each prime $\ell \ne p$, and it can be a power of $p$. The two results together suggest that only the prime $p$ is a problem. They do not give degree 1.

### What the weak forms give for local uniformization

Let $K$ be a function field over $k$ and let $v$ be a valuation of $K$ that is trivial on $k$. A regular alteration $X' \to X$ of a model $X$ of $K$ gives a finite extension $K'$ of $K$, an extension $v'$ of $v$ to $K'$, and a regular center of $v'$ on $X'$. So each of the three theorems gives local uniformization of $v$ after a finite extension of $K$. This is the conclusion of the theorem of Knaf and Kuhlmann, Theorem 5.1.2, which they prove by valuation theory only [KK09]. The theorem of Temkin on $p$-alterations controls the degree, and inseparable local uniformization controls the type of the extension: it can be purely inseparable [Tem13] (Theorem 4.1.1).

To pass from $K'$ back to $K$ one has to descend. If $K'/K$ is Galois with group $G$, then $X$ is birational to the quotient $X'/G$, and one has to resolve the quotient singularities of $X'/G$. When the degree is a power of $p$, the group $G$ is a $p$-group, and its action in characteristic $p$ is wild. A resolution of wild quotient singularities is not known in dimension 4. When $K'/K$ is purely inseparable, Proposition 4.2.1 and Example 4.2.2 show that regularity does not descend. In both cases the descent meets the defect of Section 5.1: the extension $K'/K$ along $v$ can have a defect, and then Proposition 3.1.4 shows that the lifting method of Chapter 1 does not apply.

*Remark.* The weak forms are enough for many applications, for example for the finiteness of étale cohomology [ILO14] and for questions where a finite extension of the function field does not matter. They are not a route to Conjecture 2.3.1 or Conjecture 2.1.1 of Volume 9 unless a new descent theorem is found. Volume 9, Section 2.3, describes the route of alterations in these terms.

### The status of the programs

The table lists the programs of this chapter. The column "proved" gives the strongest theorems that the program has produced. The column "where it stops" gives the step that is open in dimension 4 in characteristic $p$. Each entry of the first column is a theorem of the literature, except where the table says "announcement".

| Program | Proved | Where it stops |
|---|---|---|
| Zariski, patching | resolution from local uniformization in dimension at most 3 [Zar44, Abh66, CP08, CP09] | patching in dimension 4 (Volume 9, Conjecture 2.3.2) |
| Abhyankar valuations | local uniformization in each dimension [KK05, Cut20] | the valuations that are not Abhyankar |
| Finite extensions | local uniformization in a finite extension [KK09] | the descent along a defect extension |
| Inseparable local uniformization | local uniformization after a purely inseparable extension [Tem13], height reduction [Tem23] | regularity does not descend (Section 4.2) |
| Defect theory | classification of Artin-Schreier defect [Kuh10b, KR23, CKR25], the defect as the obstruction to the projection method [CM17] | no method that removes a dependent defect by blowups |
| Key polynomials, tight extensions | generators of extensions [Nov24], reduction to rank 1 [NS14], tight extensions in a recent preprint [HOST26] | control of limit key polynomials in transcendence degree 4 |
| Local monomialization | true in characteristic 0 [Cut99] | false in characteristic $p$ [Cut15] |
| Characteristic polyhedron | embedded surfaces [CJS20], threefolds [CP08, CP09, CP19] | the reduction to degree $p$ and the Projection Theorem in dimension 4 |
| Rees algebras, elimination | stratification [BV10], strong monomial case [BenV13], Samuel slope [BBE25] | a decreasing invariant outside the monomial case |
| Idealistic filtrations | an algorithm in dimension 3 [KM16] | the program in dimension at least 4 |
| Hironaka, infinitely near points | announcement [Hir17] | not checked by the community |
| Weighted blowups | resolution in characteristic 0 [ATW24, McQ20], plane curves in characteristic $p$ [AQS24, AQS25] | the tangent space can grow [AQS24], pinch points in characteristic 2 [AT26], an invariant that drops in dimension 4 (Volume 9, Conjecture 2.3.6) |
| Purely inseparable equations | embedded surfaces in dimension 3 [HP24], $z^p + g(x, y)$ [HW14] | $z^p + g(x_1, \dots, x_4)$ (Volume 9, Conjecture 2.3.7) |
| Alterations | regular alterations of degree prime to $\ell$ or a power of $p$ [dJ96, ILO14, Tem17] | degree 1, the descent along wild or inseparable extensions |

Local uniformization in transcendence degree 4 and resolution of fourfolds in characteristic $p$ are open. No program in this table claims a proof, except the announcement of Hironaka, which the literature does not accept as a proof at the time of writing. Hauser describes the problem in the same way in his survey [Hau10], and the later papers that we cite treat it as open.

### Notes and references

Volume 8 proves the theorem of de Jong and states the refinements of Gabber and Temkin. Volume 9, Chapter 2, states the open problems and the routes. For local monomialization in characteristic 0 see [Cut99].
