---
title: The known cases
nodes: [SG0000001W, SG0000000D, SG0000001A, SG0000001B, SG0000001D, SG0000001K]
sources: [Hir64, Abh56s, Lip78, Abh66, CP08, CP09, CP19, dJ96]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The known cases

The table gives the known cases of $\mathrm{Res}(p, n)$. The column "Node" gives the node of the map. The page of the node on the site gives its status in Lean.

| Case | Result | Node |
|---|---|---|
| each $p$, $n = 0$ | elementary, proved below | SG0000001W |
| $p = 0$, each $n$ | Hironaka, 1964 | SG0000000D |
| each $p$, $n = 1$ | normalization | SG0000001A |
| each $p$, $n = 2$ | Abhyankar, 1956; Lipman, 1978 for excellent surfaces | SG0000001B |
| $p > 5$, $n = 3$ | Abhyankar, 1966 | SG0000001D |
| each $p$, $n = 3$ | Cossart and Piltant, 2008, 2009 and 2019 | SG0000001D |

The case of dimension 0 is elementary, and it is the first theorem that the project proves in Lean. We give the proof, because it shows how the definitions of the last two sections work together.

**Theorem 2.3.1 (dimension 0).** Let $p \ge 0$. Then $\mathrm{Res}(p, 0)$ holds. More exactly, a reduced scheme $X$ of dimension at most 0 is regular, so the identity of $X$ is a resolution of $X$.

Node: SG0000001W · Lean: `Singularity.resolutionInDim_dim_zero`

*Proof.* Let $x \in X$. The dimension of the local ring $\mathcal{O}_{X,x}$ is the length of the longest chain of points $x = x_0 \rightsquigarrow \dots$ that generalize $x$, that is, the coheight of $x$ in the specialization order. A chain of points of $X$ gives a chain of irreducible closed subsets of the same length, so this length is at most $\dim X \le 0$. Thus $\dim \mathcal{O}_{X,x} = 0$.

The ring $\mathcal{O}_{X,x}$ is reduced because $X$ is reduced. In a local ring of dimension 0 the maximal ideal is the only prime ideal, so it is equal to the nilradical. The nilradical of a reduced ring is $0$. Thus the maximal ideal is $0$, and $\mathcal{O}_{X,x}$ is a field.

A field $K$ is a regular local ring: its maximal ideal is $0$, so $\dim_K \mathfrak{m}/\mathfrak{m}^2 = 0 = \dim K$. Thus each local ring of $X$ is regular, and $X$ is regular. By Proposition 2.5.1, the identity of a regular scheme is a resolution. $\square$

The proof does not use that $X$ is of finite type over a field, and it does not use the characteristic. The Lean proof follows the same three steps, and it uses the Mathlib lemmas `ringKrullDim_stalk_eq_coheight` and `Ring.KrullDimLE.isField_of_isReduced`.

**Theorem 2.3.2 (de Jong).** Let $X$ be a variety over a field $k$. There is a regular variety $Y$ and a proper, surjective and generically finite morphism $Y \to X$.

Node: SG0000001K · Lean: `Singularity.exists_regular_alteration`

Such a morphism is an *alteration*. An alteration is weaker than a resolution, because it can have a degree greater than 1 over the generic point. For many questions of cohomology an alteration is sufficient, but it does not answer the problem of this handbook. Proposition 2.5.2 shows that the statement of the project does not accept an alteration as a resolution.
