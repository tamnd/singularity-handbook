---
title: The characteristic polyhedron and the threefold proofs
nodes: [SG00000014, SG0000001F, SG0000001C, SG0000001V, SG0000001D, SG0000001B, SG0000001H, SG0000001J]
sources: [Hir67, Hir67b, Hir70, Cos87, Cos92, Sch, CP08, CP09, CP14, CP15, CP19, CJS20, CJSch19, CSch21, CGO, Abh66, Cut09, Moh14, Benn70]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The characteristic polyhedron and the threefold proofs

The proofs of resolution and local uniformization in dimension 3 in characteristic $p$ use the characteristic polyhedron of Hironaka. In this section we recall the polyhedron, compute a small example, state what is proved with it, and explain where the method stops. Volume 6 gives the proof of Cossart and Piltant in detail. Here we only collect what matters for dimension 4.

### The polyhedron of Hironaka

Let $S$ be a regular local ring of dimension $n$ with a regular system of parameters $u = (u_1, \dots, u_n)$, and let
$$h = Z^m + f_1 Z^{m-1} + \dots + f_m \in S[Z]$$
be monic, with $f_i \in S$. Assume for simplicity that $S$ is complete, so that each $f_i$ is a power series $\sum_\alpha c_{i, \alpha} u^\alpha$. The polyhedron of $h$ in the coordinates $(u; Z)$ is the convex hull
$$\Delta(h; u; Z) = \operatorname{conv} \Bigl( \bigcup_{i, \alpha \,:\, c_{i, \alpha} \ne 0} \bigl( \tfrac{\alpha}{i} + \mathbb{R}_{\ge 0}^n \bigr) \Bigr) \subseteq \mathbb{R}_{\ge 0}^n.$$
This is Definition 3.1.1 of Volume 6, after [Hir67]. A vertex $y$ of the polyhedron is *solvable* if the initial form of $h$ at $y$ is $(Z - \lambda U^y)^m$ for some $\lambda$ in the residue field. Then $y$ has integral coordinates, and the change $Z \mapsto Z - \lambda u^y$ removes the vertex (Volume 6, Lemma 3.1.4). Hironaka proves that a sequence of such changes, possibly infinite and convergent in the completion, reaches a polyhedron with no solvable vertex, and that this polyhedron is the intersection of the polyhedra $\Delta(h; u; Z')$ over all choices of $Z'$ (Volume 6, Theorem 3.1.5). This intersection is the *characteristic polyhedron* $\Delta(h; u)$. It depends on $u$ and not on $Z$.

In characteristic 0, or when $m$ is a unit in $S$, the Tschirnhausen change $Z \mapsto Z + f_1/m$ reaches the characteristic polyhedron in one step (Volume 6, Corollary 3.1.6). In characteristic $p$ with $m = p$ there is no such formula, and the vertex preparation can need infinitely many steps (Volume 6, Example 3.1.8). The notion of a solvable vertex itself depends on the characteristic, as the example below shows.

### A worked example

Let $k$ be a field of characteristic 2, let $S = k[[x, y]]$, and let
$$h = Z^2 + x^2 + x^3 y.$$
This is a surface $X = V(h)$ in $\mathbb{A}^3$, of the form $z^p + g$. The monomials of $f_2 = x^2 + x^3 y$ give the points $(2, 0)/2 = (1, 0)$ and $(3, 1)/2 = (3/2, 1/2)$. So $\Delta(h; x, y; Z) = \operatorname{conv}\{(1, 0), (3/2, 1/2)\} + \mathbb{R}_{\ge 0}^2$. The point $(3/2, 1/2)$ lies in $(1, 0) + \mathbb{R}^2_{\ge 0}$, so the polyhedron is $(1, 0) + \mathbb{R}_{\ge 0}^2$ with the single vertex $(1, 0)$. The initial form at this vertex is $Z^2 + X^2$. In characteristic 2 this is $(Z + X)^2$, so the vertex is solvable. The change $Z \mapsto Z + x$ gives
$$h = (Z + x)^2 + x^2 + x^3 y = Z^2 + x^3 y,$$
with the polyhedron $(3/2, 1/2) + \mathbb{R}_{\ge 0}^2$. Its vertex is not integral, so it is not solvable, and this is the characteristic polyhedron. In characteristic different from 2, the form $Z^2 + X^2$ is not a square of a linear form, the vertex $(1, 0)$ is not solvable, and the polyhedron $(1, 0) + \mathbb{R}^2_{\ge 0}$ is already characteristic. So the same equation has different characteristic polyhedra in different characteristics.

The smallest sum of the coordinates of a point of $\Delta(h; x, y)$ is $\delta = 2$ in characteristic 2. In characteristic 2 the multiplicity of $X$ at the origin is 2, since $\operatorname{ord}(x^3 y) = 4 \ge 2$. We now resolve $X$ in characteristic 2. With $h = Z^2 + x^3 y$, the partial derivatives are $\partial h / \partial Z = 0$, $\partial h / \partial x = x^2 y$ and $\partial h / \partial y = x^3$. So the singular locus of $X$ is the line $C = V(Z, x)$, and $X$ has multiplicity 2 along $C$. The curve $C$ is regular, and $X$ is normally flat along it, so $C$ is a permissible center. Its blowup has one chart that meets the strict transform, $Z = x Z'$, and there
$$x^{-2} h = Z'^2 + x y.$$
The polyhedron is $(1/2, 1/2) + \mathbb{R}^2_{\ge 0}$, with $\delta = 1$. Its vertex is not integral, so it is the characteristic polyhedron. The singular locus of $V(Z'^2 + xy)$ is the origin. Blow up the origin. In the $x$-chart, $y = x y'$ and $Z' = x Z''$ give $Z''^2 + y'$, which is regular. The $y$-chart is the same with $x$ and $y$ exchanged. In the $Z'$-chart, $x = Z' x_1$ and $y = Z' y_1$ give $1 + x_1 y_1$, which is regular. So two blowups resolve $X$, and the invariant $\delta$ goes from 2 to 1 and then the multiplicity drops.

The example shows two points. First, in characteristic $p$ the coordinate $Z$ must be prepared by changes that are not given by a formula. Second, the right center can be a curve. If we blow up the origin first, which is also permissible, then in the $y$-chart, with $x = y x'$ and $Z = y Z'$, we get $Z'^2 + x'^3 y^2$ with the vertex $(3/2, 1)$ and $\delta = 5/2 > 2$. So $\delta$ alone does not drop under permissible blowups. The invariants of Cossart and Piltant correct for the exceptional divisor (Volume 6, Section 3.2).

### What is proved with the polyhedron

These are theorems.

1. *Excellent surfaces.* Hironaka proved resolution of excellent surfaces with the polyhedron and a numerical invariant for an algorithm of Levi type [Hir67b]. Cossart, Giraud and Orbanz treat the excellent case in detail [CGO]. Lipman proved resolution of excellent surfaces by another method (Volume 9, Theorem 2.1.2).
2. *Embedded surfaces.* Cossart, Jannsen and Saito prove canonical embedded resolution of a reduced closed subscheme of dimension at most 2 of a regular excellent scheme, by permissible blowups (Volume 9, Theorem 2.1.3) [CJS20]. The proof uses the Hilbert-Samuel function, which does not go up under permissible blowups [Benn70], the directrix and the ridge [Hir70], and the characteristic polyhedron.
3. *Threefolds.* Cossart and Piltant prove resolution of reduced quasi-excellent Noetherian schemes of dimension at most 3 (Volume 9, Theorem 2.1.4, and Volume 6, Theorem 1.1.3) [CP08, CP09, CP19], and local uniformization of each valuation of a function field of transcendence degree 3 over a field of characteristic $p$ (Volume 3, Theorem 4.1.5, and Volume 6, Theorem 1.1.6). Earlier, Abhyankar had proved resolution of threefolds over algebraically closed fields of characteristic $p > 5$ [Abh66], and Cutkosky gave a shorter account of this proof [Cut09]. Cossart made the resolution of a threefold an isomorphism over the regular locus [Cos92].
4. *The polyhedron without completion.* Cossart and Piltant prove that the characteristic polyhedron can be reached without passing to the completion [CP15]. Cossart, Jannsen and Schober prove that the polyhedron is intrinsic [CJSch19]. Cossart and Schober build an invariant from the polyhedron that drops strictly for surfaces, also without completion [CSch21]. Schober studies polyhedra and invariants in general [Sch].

The proof of Cossart and Piltant has two parts (Volume 6, Chapters 2 and 3). The first part reduces local uniformization to the equations of degree $p$ of Artin-Schreier type and to the purely inseparable equations $Z^p + f$, by the ramification theory of valuations and by projections (Volume 6, Chapter 2). The second part proves local uniformization for these equations with the invariants $\delta$, $\epsilon$, $\omega$ and $\iota$ of the characteristic polyhedron, which do not increase under Hironaka-permissible blowups (Volume 6, Chapter 3). The decrease of $\iota$ is the Projection Theorem of [CP19], whose proof fills most of the paper.

### Why the method does not extend directly

Volume 6, Chapter 4, lists in detail the places where [CP19] uses dimension 3. We summarize them here.

1. *The reduction uses the lower dimensions.* The reduction to degree $p$ uses embedded resolution of surfaces in a regular scheme of dimension 3 [CJS20], principalization of ideals in dimension 3, and a theorem of Abhyankar on regular local rings of dimension 2. In dimension 4 the reduction would need embedded resolution of threefolds in a regular scheme of dimension 4. This is open in characteristic $p$.
2. *The invariants do not increase, but nobody knows why they decrease.* The definitions of $\delta$, $\epsilon$, $\omega$ and $\iota$, and the theorem that $\iota$ does not increase, hold in each dimension (Volume 6, Section 4.1). The decrease is the problem. For $n = 3$, Cossart and Piltant project the polyhedron in $\mathbb{R}^3$ to a polygon in $\mathbb{R}^2$ and read new invariants from the polygon. For $n = 4$ there is no known projection of a polyhedron in $\mathbb{R}^4$ that plays this role. There is no hypersurface of maximal contact, which would be the natural object to project to (Section 5.3).
3. *Case analysis.* The proof of the Projection Theorem splits into cases by an invariant $\kappa \in \{1, 2, 3, 4\}$, and some blowups increase $\iota$ before it decreases. Cossart and Piltant write that an extension of these case analyses to higher dimensions seems out of reach [CP19, Section 1].
4. *The directrix.* Hironaka proved that the directrix and the closed Hilbert-Samuel stratum of a cone are equal when the residue field is perfect or when the cone lies in a space of dimension at most $p + 1$ [CP19, Proposition 2.55]. For $n = 4$ the cone lies in a space of dimension 5. So for $p = 2$ and $p = 3$ and an imperfect residue field the equality can fail.
5. *Formal arcs.* Cossart and Piltant give an example in dimension 4 in which the closure of a formal arc in the locus of multiplicity $p$ does not become permissible under the point blowups along the arc [CP19, Example 3.18]. Volume 6, Example 4.1.1, computes it. In dimension 3 this phenomenon occurs only in an easy case.

So the polyhedron and its non-increasing invariants exist in each dimension, but the proof of the decrease and the reduction to degree $p$ are tied to dimension 3. Cossart and Piltant describe some results of [CP19, Section 3.3] as a guideline for $n \ge 4$ [CP19, Remark 1.7], but they do not give a plan for the decrease in dimension 4. The status in the literature is that this route needs new ideas. Volume 9, Section 2.3, lists it as the route of characteristic polyhedra.

*Remark.* The purely inseparable equations $Z^{p^e} + f$ are the core case of all routes (Volume 9, Conjecture 2.3.7). Moh studied these equations with the polyhedron [Moh14]. In the worked example above, the surface is of this form, and the right first center was a curve, not a point. In dimension 4 the locus of multiplicity $p$ of such an equation can have components of dimension up to 3, and the choice of the center is part of the problem.

### Notes and references

Volume 6 proves the theorems of Cossart and Piltant up to the Projection Theorem and gives the references to [CP19] in detail. For the polyhedron in practice see [Cos87]. For the routes in dimension 4 see Volume 9, Section 2.3.
