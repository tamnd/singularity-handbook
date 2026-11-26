# The proof of de Jong

This chapter explains the proof of Theorem 1.2.1. The proof is an induction on the dimension. A variety of dimension $d$ is fibred, after a modification, over a variety of dimension $d - 1$ with fibres of dimension 1. The family of curves is made stable over a dense open subset of the base. The moduli of stable pointed curves then extend the family to a stable curve over an alteration of the base. The induction hypothesis makes the base regular and the discriminant a divisor with strict normal crossings. At the end, the total space is a semistable curve over a regular base, and explicit blowups make it regular.

Section 2.1 studies semistable curves and proves the local computations of the blowups. Section 2.2 states the theorems on stable curves and their moduli that the proof uses, and it proves the extension of a family of curves after an alteration of the base from a named hypothesis on the moduli. Section 2.3 gives the reductions and the fibration in curves. Section 2.4 gives the extension of the family, the induction, and the last blowups. We follow [dJ96, Sections 3 and 4] and use its numbering in the references.

### The structure of the proof

The table lists the steps of the proof in order. The column "Here" says whether the step is proved in this volume or cited, and from where. A step marked "Proved" may use the standard results of algebraic geometry that Section 2.4 lists at the end. The degrees of the alterations are in the table of Section 2.3.

| Step | Content | Here |
|---|---|---|
| 1 | An alteration of $X$ is enough: Lemma 2.3.1, and $Z$ may be enlarged: Lemma 2.3.2 | Proved: Lemmas 2.3.1 and 2.3.2 |
| 2 | Reductions: $k$ algebraically closed, $X$ projective, $Z$ a divisor, $X$ normal | Proved: Steps 1 to 4 of Section 2.3, with the limit theorems of [EGA4] and Chow's lemma |
| 3 | A fibration $X \to \mathbb{P}^{d-1}_k$ in curves after a blowup of points | Proved modulo the general position facts (A) and (B): Lemma 2.3.3, from [dJ96, Lemma 4.11] |
| 4 | Connected fibres by the Stein factorization | Proved: Section 2.3, which de Jong cites in [dJ96, 4.12] |
| 5 | Three marked smooth points on each component of each fibre | Cited: Lemma 2.3.4, from [dJ96, Lemma 4.13] |
| 6 | Base change by alterations of the base keeps the properties | Proved: Lemma 2.3.5 |
| 7 | Sections after a Galois base change | Proved: Step 5 of Section 2.3 |
| 8 | The moduli of stable pointed curves with level structure | Cited: Hypothesis 2.2.4, from [DM69, Knu83] as in [dJ96, 2.24] |
| 9 | A stable model after an alteration of the base | Proved from Step 8: Proposition 2.2.6 and Lemma 2.2.9 |
| 10 | Flattening of $X$ and $T$ over a modification of the base | Cited: [dJ96, 2.19], from Raynaud-Gruson |
| 11 | The components of the fibres of $T$ | Cited with a sketch: Lemma 2.4.1, from [dJ96, Lemma 4.20] |
| 12 | The stable model is normal, and it dominates $X$ | Proved: Proposition 2.4.2, with [dJ96, 4.21] |
| 13 | The base becomes regular and the discriminant a divisor with strict normal crossings | The induction hypothesis: Theorem 1.2.1 in dimension $d - 1$ |
| 14 | The local form of a semistable curve | Proved in part: Proposition 2.1.2; the change of coordinates is cited from [dJ96, 2.23] |
| 15 | The local blowups of the model singularities | Proved: Lemma 2.1.3, Propositions 2.1.5 and 2.4.3 |
| 16 | The reduction to singular loci of codimension at least 3 | Cited: [dJ96, Lemma 3.2] and [dJ96, 3.5] |
| 17 | The global blowups that make $X$ regular | Proved locally, cited globally: Proposition 2.4.4, from [dJ96] |
| 18 | Normal crossings to strict normal crossings | Cited: [dJ96, 2.4 and 4.28] |

*The reductions: Steps 1 to 7.* These steps are in Section 2.3. They change $X$ by modifications and by alterations of a kind that the induction can absorb. Only Steps 1 and 7 can change the degree: the field extension of Step 1 and the Galois cover of Step 7. Steps 3 and 5 contain the arguments of general position that we do not prove in full.

*The moduli: Steps 8 and 9.* This is the only input from outside resolution theory. Section 2.2 isolates it as Hypothesis 2.2.4, and Proposition 2.2.6 deduces the form that the proof uses. The degree of this step is the degree of a cover of the base that trivializes the level structure, and Lemma 2.2.9 bounds it by the order of $\mathrm{GL}_{2g}(\mathbb{F}_\ell)$. This factor is the reason why the theorem gives no control of the degree. Example 2.2.10 shows Step 9 for a family of elliptic curves.

*The extension and the induction: Steps 10 to 13.* These steps replace $X$ by the stable model. The induction hypothesis is applied to the base and to the discriminant, which have dimension $d - 1$. So the induction is on the dimension of $X$, and each step of the induction adds an alteration of the base.

*The last blowups: Steps 14 to 18.* These steps are explicit. The total space of a semistable curve over a regular base, smooth over the complement of a divisor with strict normal crossings, has toroidal singularities $uv = t_1 \cdots t_\mu$, and blowups of their singular loci make it regular. In dimension 2 these are the blowups of Example 2.1.6.

The proof gives a regular alteration, not a resolution. Steps 7, 9 and 13 have degree greater than 1 in general, and nothing in the proof removes this degree. In particular the proof does not give resolution of singularities in characteristic $p$ in any dimension, and resolution in dimension at least 4 in characteristic $p$ is still open.
