---
title: The road to dimension four
nodes: [SG00000007, SG0000009E, SG00000096, SG0000007W, SG0000007X, SG00000082, SG0000001H, SG0000001J]
sources: [Cos87, Pos24, CP08, CP09, CJS20, Moh87, HP19a, Nar83, Hau10, Cut09, Tem13, Zar44, KK09, CM17, Kuh10b, Abr25]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The road to dimension four

This section is a guide for a student who wants to work on resolution of singularities of fourfolds in characteristic $p$. It says how a proof is expected to go, which parts of it are proved, and which parts are open. It does not give a proof of $\mathrm{Res}(p, 4)$, and none is known. The rest of this chapter and Chapter 3 contain the details. Here we put them in one order.

Each claim in this section has one of three marks. A claim that is *proved in the handbook* has a statement with a number and a node of the map, and we give both. A claim that is *cited* is proved in a published source or in a research note of the project, and it is not yet a statement of the handbook. We give the source, and for a research note we say if a referee report has checked it. A claim that is *open* has no proof. Some open claims are conjectures that the project expects to be true, and some are questions with no expected answer. We say which.

The project keeps its research notes in the repository of the map. A reference such as "note 45" is to the research note with this number. A result of a note is a cited result in the sense above, and it is not part of the handbook until a section of the handbook proves it.

### The statement

We recall the definitions of Section 1. A *variety* over a field $k$ is a reduced scheme that is separated and of finite type over $k$. A *resolution* of a scheme $X$ is a proper morphism $\pi \colon Y \to X$ with $Y$ regular, such that the regular locus $\operatorname{Reg}(X)$ is open, $\pi$ is an isomorphism over it, and $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$.

**Definition 2.5.1.** Let $p$ be a prime and let $n \ge 0$.

1. $\mathrm{Res}(p, n)$ is the statement: each variety of dimension at most $n$ over a field of characteristic $p$ has a resolution. When $p$ is fixed we write $\mathrm{Res}_n$.
2. $\mathrm{Emb}_m$ is the statement: each reduced hypersurface $D$ in a regular variety $W$ of dimension $m + 1$ over a field of characteristic $p$ has an embedded resolution. That is, there is a finite sequence of blowups $W_r \to \dots \to W_0 = W$ in regular centers such that the total transform of $D$ in $W_r$ is a divisor with simple normal crossings.
3. $\mathrm{LU}_n$ is local uniformization in dimension $n$: for each function field $K$ of transcendence degree $n$ over $k$, each valuation $v$ of $K$ trivial on $k$ and each finite set $S$ in the valuation ring $\mathcal{O}_v$, there is a regular local ring $A \subset K$, essentially of finite type over $k$, with fraction field $K$, dominated by $\mathcal{O}_v$ and with $S \subset A$.
4. $\mathrm{Patch}_n$ is the statement: $\mathrm{LU}_n$ implies $\mathrm{Res}_n$. This is the patching problem of Zariski [Zar44].

The problem of this volume is $\mathrm{Res}(p, 4)$. It is Conjecture 2.1.1, with the node SG00000007 and the Lean statement `Singularity.ResolutionDimFourCharP`. Status: open for each prime $p$.

The known cases are these. $\mathrm{Res}(p, n)$ holds for $n \le 3$ and each $p$, by the work of Cossart and Piltant [CP08, CP09] (cited; Theorems 2.1.4 and 2.1.5, nodes SG0000001V and SG0000001F, which the handbook states and does not prove). Cossart, Jannsen and Saito give a canonical embedded resolution of each reduced closed subscheme of dimension at most 2 of a regular excellent scheme [CJS20] (cited; Theorem 2.1.3, node SG0000001C). Note 02 uses their Corollary 0.4 for $\mathrm{Emb}_2$. $\mathrm{Emb}_3$ is open for each $p$. $\mathrm{LU}_4$ is Conjecture 2.3.1 (node SG0000001H), and it is open. A form of $\mathrm{Patch}_4$ is Conjecture 2.3.2 (node SG0000001J), and it is open. In characteristic 0 the statement $\mathrm{Patch}_n$ is true, because $\mathrm{Res}_n$ is true there, but no proof of it by the method of patching is known for $n \ge 4$.

### Why dimension four in characteristic p is hard

The proofs of characteristic 0 use an induction on the dimension. At a point of maximal order $d$ of a hypersurface they choose a regular hypersurface $V$ of *maximal contact*: $V$ contains all the nearby points of order $d$, and it keeps this property after each permissible blowup. The problem then goes down to $V$. Section 2.2 explains why each step of this method fails in characteristic $p$. Three failures matter most in dimension 4.

*No maximal contact.* Narasimhan gave a hypersurface in $\mathbb{A}^4$ in characteristic 2 whose points of order 2 near the origin lie on no regular hypersurface germ, also not on a formal one [Nar83]. This is Example 2.2.1 (proved in the handbook, node SG00000018, with a Lean proof `Singularity.Examples.narasimhan`). The curve of points of order 2 in that example has embedding dimension 4, so no induction on a hypersurface sees all of it. Section 3.21 gives a related question for germs of order less than $p$ (item 5 of its list of open problems).

*The residual order goes up.* For an equation $f = z^q + F(x_1, \dots, x_n)$ with $q = p^e$, Volume 7, Section 1.3, defines the residual order $d$: write the clean part of $F$ as $x^r G$ with a monomial $x^r$ in the components of the divisor, and put $d = \operatorname{ord} G$. In characteristic 0 the analogue of $d$ does not go up at points where the order stays. In characteristic $p$ it can go up. Moh's bound, Volume 7, Theorem 1.4.1 (proved in the handbook for point blowups, node SG00000015), says that $d' \le d + p^{e-1}$ after a point blowup [Moh87]. Volume 7, Example 1.4.2 (node SG00000016) is a point blowup with $p = 2$ and $q = 4$ where $d$ goes from 5 to 7, so the bound is sharp there. A point after a blowup where the order stays and the residual order goes up is a *kangaroo point*, in the terms of Hauser [Hau10]. For $q = p$, Volume 7, Corollary 3.2.5 gives $d' \le d + 1$, and Volume 7, Section 3.2, describes the kangaroo points with the log-Jacobian ideal.

*Unbounded growth.* Hauser and Perlega found an equation $z^{p^3} + F$ in four variables for $p \ge 3$, and in five variables for $p = 2$, with an infinite sequence of point blowups along which the order stays $p^3$ and the residual order tends to infinity [HP19a]. This is Volume 7, Theorem 1.4.3 (cited, node SG00000017). Volume 7, Example 1.4.5 (node SG00000039) certifies one cycle of it in Lean. The examples do not refute resolution, because larger centers are permissible at some steps (Volume 7, Remark 1.4.4). But they show that point blowups and the pair (order, residual order) are not enough. A proof must choose the centers well, or it must add an invariant that pays for the increases.

Two more failures are in Section 2.2: over an imperfect field a regular variety need not be smooth (Example 2.2.2, node SG0000000C), and a valuation can have defect (Example 2.2.3). The second one is the subject of the track VD below.

### The two local cores

A proof of $\mathrm{Res}_4$ by any known route meets one of two local problems. Both are about purely inseparable equations.

**Definition 2.5.2.** Let $e \ge 1$. The statement $\mathrm{Core}_3(e)$ says: for each regular local ring $R$ of dimension 3, essentially of finite type over a perfect field $k$ of characteristic $p$, each divisor $E$ with simple normal crossings on $\operatorname{Spec} R$, and each $g \in R$, the hypersurface $z^{p^e} + g = 0$ in $\operatorname{Spec} R[z]$ has an embedded resolution by blowups in regular centers that is compatible with $E$.

The first core is $\mathrm{Emb}_3$, and inside it the statements $\mathrm{Core}_3(e)$. At a point where the multiplicity is prime to $p$, the Tschirnhausen transformation gives a hypersurface of maximal contact, as in characteristic 0. At a point where the multiplicity is $p^e$, the local equation can be put in the form $z^{p^e} + g$, and this is $\mathrm{Core}_3(e)$. At a point where the multiplicity is $p^e m_0$ with $e \ge 1$ and $p \nmid m_0 > 1$, the two cases mix. Status: the expectation that the standard reductions reduce $\mathrm{Emb}_3$ to $\mathrm{Core}_3(e)$ for all $e$ and to the mixed case is a heuristic of note 02, and it is not proved. Each $\mathrm{Core}_3(e)$ is open. Three routes need $\mathrm{Emb}_3$: the patching route uses it in the charts, the method of Jung uses it for the discriminant (Section 3.21), and the condition (E) of Cossart and Piltant has an embedded form in dimension 3.

The second core is a theorem of Cossart, one dimension higher. Let $Y$ be a regular variety of dimension $n$ over a perfect field $k$ of characteristic $p$, with a divisor $E$ with simple normal crossings, and let $g \in \mathcal{O}_Y$. Locally, with coordinates $x_1, \dots, x_n$ and $E = V(\prod_{i \in \Delta} x_i)$, Volume 7, Definition 3.1.1 (node SG0000003E) defines the log-Jacobian ideal $\Theta(g)$, the ideal generated by $x_i \partial_i g$ for $i \in \Delta$ and by $\partial_j g$ for $j \notin \Delta$. It does not change when we add a $p$-th power to $g$. For a clean $g = x^r G$ it is $x^r \widetilde\Theta(G)$, and Volume 7, Definition 3.1.3 (node SG0000003F) defines $\rho = \operatorname{ord} \widetilde\Theta(G)$. Volume 7, Section 3.4, gives two conditions (H1) and (H2) on a regular center $C$: (H1) says that $\widetilde\Theta(G)$ is equimultiple along $C$, and (H2) says the same for a second ideal $\widetilde\Theta_C(G)$ in one case.

**Conjecture 2.5.3 (Cossart's theorem on a base of dimension 4).** Let $Y$ be a regular variety of dimension 4 over a perfect field of characteristic $p$, let $E$ be a divisor on $Y$ with simple normal crossings, and let $g \in \mathcal{O}_Y$ be locally not a $p$-th power. Then there is a finite sequence of blowups of $Y$ in regular centers that satisfy (H1) and (H2), with $E$ replaced at each step by its total transform, such that at the end $\rho = 0$ at each point of the locus where $z^p + g$ has multiplicity $p$.

Status: open. For $\dim Y = 3$ the statement is the theorem of Cossart's thesis [Cos87], and Posva gives a global form of it [Pos24] (cited). This is the problem that Volume 7, Chapter 3, works on. The following parts of the proof in dimension 3 hold in each dimension, and so in dimension 4 (proved in the handbook):

1. the dichotomy $d - 1 \le \rho \le d$, Volume 7, Theorem 3.1.4 (node SG0000003F);
2. the law of transformation under a point blowup, Volume 7, Theorem 3.2.3 (node SG0000003M), and the fact that $\rho$ does not go up, Theorem 3.2.4 (node SG0000003N);
3. the same for a regular center with (H1) and (H2), Volume 7, Theorem 3.4.5 (node SG0000004Q), and Example 3.4.6 (node SG0000004R) shows that (H2) is necessary;
4. the end case: at a point with $\rho = 0$ the equation is binomial, $z^p + x^r$ or $z^p + x^r x_j$, Volume 7, Theorem 3.5.3 (node SG0000004S);
5. the equality of $\rho$ with the invariant $\omega$ of Cossart and Piltant, Volume 7, Proposition 3.6.1 (node SG0000004T).

What does not carry over is the case analysis of Cossart in dimension 3. It uses a secondary invariant with a finite number of values and treats each value by hand. In dimension 4 the runs of blowups where $\rho$ stays are much richer, and Volume 7, Sections 3.7 to 3.18, studies them. Note 02 calls Conjecture 2.5.3 the common local core of two global problems: the problem $\mathrm{PILU}_4$ below, and the problem of resolving the normalization of a regular 4-fold $Y$ in $k(Y)(b^{1/p})$. Both have the local equation $z^p + g(x_1, \dots, x_4)$. Status of this claim: a heuristic of note 02. In particular, a proof of Conjecture 2.5.3 does not give $\mathrm{PILU}_4$ at once. One also needs the blowups of the base to lift to permissible blowups of the hypersurface (Volume 7, Section 4.3, and Section 3.20), and a resolution of the binomial end cases.

### The global reductions

Three reductions connect the local cores to $\mathrm{Res}_4$. None of them is a statement of the handbook yet.

1. Let $\mathrm{PILU}_n$ be local uniformization for the extensions $L(a^{1/p})$ of the fraction field $L$ of a regular local ring $A$ of dimension $n$, with $a \in A$ and $a^{1/p} \notin L$. Note 02, Theorem 2.6, proves that the inseparable local uniformization of Temkin [Tem13] and $\mathrm{PILU}_n$ give $\mathrm{LU}_n$ (cited, research note). So for local uniformization, the degree $p$ purely inseparable case is the whole problem.
2. Let $\mathrm{AO}_n$ be the conjecture of Abramovich and Oort: for each variety $X$ of dimension $n$ there are a regular variety $Y$ and a proper surjective morphism $Y \to X$ with $k(Y)/k(X)$ finite and purely inseparable. Let $\mathrm{FQ}_n$ be the statement: for each regular variety $Y$ of dimension $n$ and each saturated $p$-closed foliation $\mathcal{F}$ on $Y$ (see the track FO below), the quotient $Y/\mathcal{F}$ has a resolution. Note 02, Theorem 2.9, proves that $\mathrm{AO}_n$ and $\mathrm{FQ}_n$ give $\mathrm{Res}_n$ (cited, research note). $\mathrm{AO}_n$ is open for $n \ge 4$. Note 02, Corollary 2.10, also claims that $\mathrm{AO}_n$ and the resolution of the normalizations $z^p = g$ over regular $n$-folds give $\mathrm{Res}_n$. Note 58 found a gap in its proof: for a foliation of rank one on an $n$-fold the quotient is a cover of degree $p^{n-1}$ of the Frobenius twist, not of degree $p$, so the quotient is locally $z^p = g$ only for a foliation of corank one. Status of Corollary 2.10: not proved.
3. The method of Jung. Note 02, Theorem 2.12, claimed that $\mathrm{Emb}_3$ and $p > 24$ give $\mathrm{Res}_4$. Notes 56 and 62 corrected it, and Section 3.21 gives the correct form: $\mathrm{Emb}(\mathbb{P}^4)$ and $p > 24$ give local uniformization (Theorem 3.21.7), and a resolution needs a patching theorem in addition (Corollary 3.21.9). See the track TT below.

### The tracks

The project works on seven tracks at the same time. Each one attacks one piece of the problem. The names are the names of the issues of the project. For each track we give the main statement, what is proved, and the first case that is open.

#### Track C4: corner runs in four variables

The track C4 (tamnd/singularity#286) works on Conjecture 2.5.3 through the runs of point blowups where $\rho$ stays. The worst runs are at the corners of the divisor.

**Definition 2.5.4.** Let $R = K[[x, y, z, w]]$ with the divisor $E = V(yz)$, and let $g \in R$ be clean. A *corner run in four variables* is an infinite sequence of point blowups $P_N, P_{N+1}, \dots$ such that each $P_{m+1}$ lies in the $y$-chart or in the $z$-chart at the corner $y_{m+1} = z_{m+1} = 0$, each of the two charts occurs an infinite number of times, and $\rho(P_m) \ge 1$ is the same for all $m$. The point $P_{m+1}$ is given by a translation vector $(a_m, b_m) \in K^2$ in the free coordinates $(x, w)$. The run is *linear* if the vectors $(a_m, b_m)$ for $m$ large lie on one line through the origin, and *planar* if not.

This is the setting of Volume 7, Section 3.17, and the linear runs are those of Volume 7, Definition 3.17.5. Conjecture L (Volume 7, Conjecture 3.17.18, node SG0000006Z) asks for a free coordinate whose translations are 0 from some point on. Conjecture L° (Volume 7, Conjecture 3.17.24, node SG00000075) asks in addition that the corner curves have the order of $G$ at least $\rho$, so that a resolution can blow them up. Hypothesis H1 is Volume 7, Hypothesis 3.17.32 (node SG0000007D).

*Main conjecture of the track.* Volume 7, Conjecture 3.18.39 (P), node SG00000096: a clean $g \in K[[y, z]][x, w]$ has no planar corner run. By Volume 7, Theorem 3.18.19 (node SG0000008N), a corner run is planar if and only if Conjecture L fails for it.

*What is proved in the handbook.*

1. Volume 7, Corollary 3.18.18 (node SG0000008M): for $\deg_{x, w} g < p$, each corner run is linear, and H1, L and L° hold.
2. Volume 7, Corollary 3.18.36 (node SG00000093): Conjecture L holds if $\deg_{x, w} g \le p$, or if $g$ satisfies a condition (C) on its derivatives of order $p^e$, or if $g \in K[[y, z]][x^p, w^p]$.
3. Volume 7, Theorem 3.18.37 (node SG00000094) describes the runs for $g \in K[[y, z]][x^p, w^p]$, and Corollary 3.18.38 (node SG00000095) gives L° for $g = B_1 x^p + B_2 w^p + B_0$.
4. In three variables, Volume 7, Theorem 3.16.14 (node SG0000006H) proves that a corner run with free translations has only a finite number of nonzero translations.
5. Volume 7, Corollary 3.17.12 (node SG0000006T) shows that in four variables the translations need not be finite, so the four variable case is different.

*What is cited.* Note 69 proves Conjecture P for $p = 2$ and $\deg_{x, w} g = 3$, and note 71, a referee report on note 69, confirms this. Note 71 also gives a proof of Conjecture P for each $p$ and each degree. It asks for a second referee before the result goes into the handbook. Status: cited, not yet checked by a second referee.

*What is open.* The first open case is Conjecture 4.4 of note 69: for $p = 2$ and $\deg_{x, w} g = 3$, Hypothesis H1 and Conjecture L° for the linear runs with an infinite number of nonzero translations. More generally, H1 and L° for the linear runs with $\deg_{x, w} g \ge p$ and $g \notin K[[y, z]][x^p, w^p]$ are open. Also open are the runs that leave a component of the divisor an infinite number of times, the conjecture V of Volume 7, Section 3.15, the case $g \in K[[x, y, z]]$ with more than two divisor components at the corner, and a rule for the centers that has been tested on long runs. Two warnings: Volume 7, Hypothesis 3.13.12 (H4', node SG0000005K) is false by Example 3.13.15 (node SG0000005M), and Volume 7, Conjecture 3.11.3 (node SG0000005D) on kangaroo paths is false by Example 3.11.6 (node SG0000005G). Proposition 3.11.5 (node SG0000005F) proves it when $\tau_\rho \le 1$ at the start. Question 3.13.18 of Volume 7 is the corrected question.

#### Track M2: mixed multiplicities

The track M2 (tamnd/singularity#287) works on the mixed case of $\mathrm{Emb}_3$, Problem 10.2 of note 10, for the multiplicity $m = p^e m_0$ with $e \ge 1$, $p \nmid m_0$ and $m_0 > 1$. Write the equation as $f = z^m + a_1 z^{m-1} + \dots + a_m$ over a regular local ring $R$.

*What is proved in the handbook.* Volume 7, Theorem 4.1.3 (nodes SG0000003J and SG0000007G): a translation $z \mapsto z + c$ does not change $a_1$, and if $a_1 = \dots = a_{i-1} = 0$ with $i < p^e$, it does not change $a_i$. This is the rigid layer. Volume 7, Proposition 4.1.4 (nodes SG0000003J and SG0000007F): the coefficient $a_{p^e}$ changes by $m_0 c^{p^e}$ plus terms in the lower coefficients. Both have Lean proofs. For the purely inseparable case $m = p$, Volume 7, Theorem 4.3.6 (node SG0000007N) proves that a blowup of the base along a regular center lifts to a permissible blowup if and only if the hypersurface has multiplicity $p$ at the generic point of the center, and Corollary 4.3.8 (node SG0000007P) and Examples 4.3.14 and 4.3.16 (nodes SG0000007T and SG0000007V) complete the picture. Section 3.20 reports this result.

*The first case.* Let $p$ be odd, $m = 2p$, and $R = k[[x_0, x_1, x_2]]$ with a divisor $E$ given by a set of the coordinates. For a weight $w \in \mathbb{R}^3_{\ge 0}$ let $v_w$ be the monomial valuation with $v_w(x_i) = w_i$. For a coordinate $z$ put $\delta_z(w) = \min_{i \ge 1} v_w(a_i)/i$, and let $\delta(w)$ be the supremum of $\delta_{z'}(w)$ over all coordinates $z'$. Put $\delta = \delta(1, 1, 1)$, let $\mu_k = \delta(e_k)$ for the unit vector $e_k$, and put
$$\omega = \delta - \sum_{k \in E} \mu_k .$$
This is the residual slope of note 61. Note 61 also defines a rule, Rule 61.9', that chooses the center at each point: first a center in the divisor, then a monomial center when $\omega = 0$, and then the main center. We do not repeat the rule here.

**Conjecture 2.5.5 (termination for $m = 2p$).** Let $p$ be odd and $m = 2p$. For each germ $(f, E)$ as above, each choice of the coordinates and of the tie breaks of Rule 61.9', and each sequence of closed points of multiplicity $m$, each over the center chosen at the point before, the sequence of blowups of Rule 61.9' is finite.

This is Conjecture 65.2 of note 65. Status: open. What is cited: note 61 proves that $\omega$ does not depend on the choice of $z$ and of the coordinates that keep $E$. Note 65 (a referee report on note 61, Theorem 65.1) and note 66 (Theorem 66.3) show that $\omega$ can go up under Rule 61.9', in note 66 by $1/p$, so $\omega$ alone does not prove termination. Note 66, Theorem 66.6, proves Conjecture 2.5.5 when $\omega = 0$ at the first point: then $\omega$ stays 0, and $\delta$ drops by at least $1/B$ at each step, with $B = \operatorname{lcm}(1, \dots, 2p)$. No referee report on note 66 exists yet. The first open case is $\omega > 0$ at the first point. Computer runs of note 66 found no cycle.

#### Track NW: Newton polyhedra and Frobenius

The track NW (tamnd/singularity#296) asks if a change of coordinates and weighted blowups can make $z^p + g$ Newton nondegenerate. Volume 7, Section 3.3, defines the Newton polyhedron of $f$ and its initial forms. The equation is *Newton nondegenerate* if no initial form for a compact face has a critical point in the torus.

*What is proved in the handbook.* Volume 7, Theorem 3.3.13 (node SG0000008P, with a Lean proof `Singularity.newtonNondegenerate_purelyInseparable_iff`): over a perfect field, $z^p + g$ is Newton nondegenerate if and only if no initial form $\operatorname{in}_w g$ with $w \in \mathbb{Z}^n_{>0}$ has a critical point in the torus. Example 3.3.14 (node SG0000008Q) shows that the field must be perfect. Theorems 3.3.16 and 3.3.17 (nodes SG0000008R and SG0000008S) give an obstruction. Let $C$ be the projective critical set of the lowest form $h$ of $g$, of degree $D$. If $C$ is not in the union of $n$ hyperplanes with independent equations, then no change $x \mapsto \varphi(x)$, $z \mapsto z + q$ makes the equation Newton nondegenerate, and for $D > p$ no change of all the coordinates does. Proposition 3.3.20 (node SG0000008T) decides when a change that keeps one coordinate removes the torus critical points, and Theorem 3.3.22 (node SG0000008Y) gives the obstruction of the Fano plane for $p = 2$. Conjecture 3.3.24 (node SG0000008Z) is the case $D = p$. Theorem 3.3.26 (node SG0000008W) resolves a Newton nondegenerate germ by a toric morphism, Proposition 3.3.27 (node SG0000008V) finds the singular points of the strict transform, and Theorem 3.3.29 (node SG0000008X) treats a binary form $h$ with $p \mid D$ by one weighted blowup.

*What is cited.* The map has the nodes SG00000097 to SG0000009E from notes 68 and 70, and the handbook does not yet prove them. SG00000097 and SG00000099 extend the obstruction to $D = p$ under conditions. SG0000009A is a form of degree 5 in three variables for $p = 5$ that no change of coordinates prepares. SG0000009D says that one weighted blowup with the weights $(1, \dots, 1, \nu/p)$ lowers the residual order $\nu$ when $p \mid \nu$, outside some exceptional points. Here $\nu$ is the order of the part of $g$ without monomials that are $p$-th powers.

**Conjecture 2.5.6.** Let $k$ be an algebraically closed field of characteristic $p > 0$, let $n \ge 3$, and let $f = z^p + g$ with $g \in k[[x_1, \dots, x_n]]$ and residual order $\nu \ge 2$. Then there is a finite sequence of weighted blowups such that at each step the largest residual order at the points of the strict transform over the origin drops. In particular, after a finite number of steps the strict transform is smooth at each point over the origin.

Node: SG0000009E · Lean: none yet

Status: open, and the project does not know if it is true. The first open cases are the case $p \nmid \nu$, the exceptional points of SG0000009D, and the termination. The decision of notes 55 and 68 was negative for the original aim: the three test cases of the track C4 in note 55 resist every change of all the coordinates (note 68, Corollary 3.2, checked by the referee report in note 70). So Newton nondegeneracy alone does not give Conjecture 2.5.3.

#### Track TT: the method of Jung for large p

The track TT (tamnd/singularity#297) is Section 3.21. It asks how far the proof of Abhyankar and Cutkosky for threefolds with $p > 5$ goes in dimension 4.

*Main statement.* Corollary 3.21.9 (node SG00000083): $\mathrm{Emb}(\mathbb{P}^4)$, Conjecture 3.21.8 and $p > 24$ give $\mathrm{Res}(p, 4)$ over an algebraically closed field. Here $\mathrm{Emb}(\mathbb{P}^4)$ is Definition 3.21.1 (node SG0000007W), embedded resolution of reduced divisors in $\mathbb{P}^4$, which follows from $\mathrm{Emb}_3$. Conjecture 3.21.8 (node SG0000007X) is patching in the form of Zariski in dimension 4.

*What is proved in the handbook.* Theorem 3.21.7 (node SG00000082): $\mathrm{Emb}(\mathbb{P}^4)$ and $p > 24$ give local uniformization in dimension 4. This is [Cut09, Theorem 14.4] in dimension 4, and it uses three cited theorems, Hypotheses 3.21.3 to 3.21.5 (nodes SG0000007Y, SG0000007Z and SG00000080). Example 3.21.10 (node SG00000084) shows that for the Hermitian 4-fold each linear projection to $\mathbb{P}^4$ has local degree at least $q$ along a 3-fold, so one global projection is not enough. Theorem 3.21.11 (node SG00000085) gives a resolution of one 4-fold with a tame projection whose branch divisor has an embedded resolution. Theorem 3.21.12 (node SG00000086) resolves hypersurfaces of bounded degree for $p$ large. Example 3.21.14 (node SG00000088) is a germ of order less than $p$ with maximal contact.

*What is open.* $\mathrm{Emb}(\mathbb{P}^4)$ for each $p$; Conjecture 3.21.8, for which no proof by patching is known even in characteristic 0; and the question if the hypothesis (TP) of Theorem 3.21.11 can be weakened to tameness along the branch divisor. The first open case is $\mathrm{Emb}(\mathbb{P}^4)$ in the local form of Lemma 3.21.2. So the track TT moves the problem to $\mathrm{Emb}_3$ and to patching. It does not avoid them.

#### Track HS: Hasse-Schmidt digits for e at least 2

The track HS (tamnd/singularity#288) works on $\mathrm{Core}_3(e)$ for $e \ge 2$, where the examples of Hauser and Perlega live. For $q = p^e$ the derivations of order one kill all $p$-th powers, but the cleaning only removes $q$-th powers. So the log-Jacobian ideal does not see enough of $g$, and a finer object is needed.

**Definition 2.5.7.** Let $R = K[[x_1, \dots, x_n]]$, let $E = V(\prod_{i \in \Delta} x_i)$, and let $F$ be the complement of $\Delta$. For $g \in R$ and $1 \le m < q$, let $\Theta^{\le m}_E(g)$ be the ideal of $R$ generated by the coefficients of the monomials $s^\alpha$ with $1 \le |\alpha| \le m$ in the expansion of $g\bigl(x_i (1 + s_i) \ (i \in \Delta), \ x_j + s_j \ (j \in F)\bigr)$ in new variables $s_1, \dots, s_n$. The *digit levels* are $m = p^j$ with $0 \le j \le e - 1$. Let $\rho_m$ be the order of the residual factor of $\Theta^{\le m}_E(g)$ after the monomial factor is removed.

For $m = 1$ the ideal $\Theta^{\le 1}_E(g)$ is the log-Jacobian ideal $\Theta(g)$ of Volume 7, Section 3.1. Note 45 defines these ideals, and note 48 is its referee report.

*What is cited.* Note 45 proves: the ideal $\Theta^{\le m}_E(g)$ does not change when we add $h^{p^j}$ with $p^j > m$, so the top level $m = p^{e-1}$ sees $g$ up to $q$-th powers; the dichotomy $d - m \le \rho_m \le d - s_m$ for $m \ge p^{e-1}$, with a number $s_m$ that comes from the digits of the initial form (Theorem 3.1); an exact law of transformation under point blowups (Theorem 4.1); the bound $\rho'_m \le \rho_m$ at the points that note 45 calls balanced (Theorem 5.2); and $d' \le d + \max(0, P - T)$ with $P = p^{e-1}$ and a digit number $T$ (Corollary 5.4), which refines Moh's bound. For $m = 1$ each point is balanced, so $\rho_1$ never goes up (Corollary 5.5). Example 5.6 of note 45 is an increase of $\rho_4$ at a point that is not balanced, for $p = 2$ and $e = 3$. On the cycles of Hauser and Perlega, $\rho_{p^{e-1}}$ drops at some step of each pass that note 45 computed (five passes of one cycle and four of the other), but it grows without bound along the iterated cycles (Proposition 7.1 of note 45). The handbook has the parts for $m = 1$: Volume 7, Proposition 1.1.4 (node SG0000004M), Theorem 3.1.4 and Example 3.1.7, and the examples Theorem 1.4.3 and Example 1.4.5.

*What is open.* The first open problem is (O1) of note 45: a rule that chooses a permissible center, for example a curve or a surface, through each point that is not balanced, such that $\rho_{p^{e-1}}$, or the pair $(d, \rho_{p^{e-1}})$ in the lexicographic order, does not go up. This needs a law of transformation for centers of positive dimension, which Theorem 4.1 of note 45 does not give. Whether the property of being balanced depends on the coordinates is also open.

#### Track VD: valuations and defect

The track VD (tamnd/singularity#298) works on $\mathrm{LU}_4$ directly, through the defect of Section 2.2. Let $k$ be algebraically closed of characteristic $p$, let $F$ be a function field of transcendence degree 4 over $k$, and let $\nu$ be a valuation of $F$ of rank one, trivial on $k$, with residue field $k$.

**Definition 2.5.8.** A *projection* of $F$ is a subfield $K = k(y_1, \dots, y_4)$ with $F/K$ finite and separable. It has *zero defect* if the defect of $(F/K, \nu)$ in the sense of Section 2.2 is 1. The valuation $\nu$ is of *CA type* if its value group is $\mathbb{Z}^r$, there are $x_1, \dots, x_r \in F$ whose values form a basis of it, and $F$ lies in the completion of $k(x_1, \dots, x_r)$ for $\nu$.

**Conjecture 2.5.9 (V7).** Let $\nu$ be as above. If $F$ has a projection with zero defect for $\nu$, then $\nu$ has local uniformization.

Status: open in general. What is cited: note 57 proves Conjecture 2.5.9 for the valuations of CA type, and note 59, its referee report, finds that this case is a theorem of Knaf and Kuhlmann [KK09, Theorem 1.5]. Note 57 also corrects a count of dimensions: the theorem of Cutkosky and Mourtada on zero defect [CM17, Theorem 7.1], for a function field of dimension 4, needs embedded local uniformization in dimension 4, not in dimension 3. So Conjecture 2.5.9 is not a consequence of the work in dimension 3. Note 57 gives examples in dimension 4 with dependent Artin-Schreier defect (its Examples 4.4 and 4.5) and a tower with independent defect (its Example 4.7), in the classes of Kuhlmann [Kuh10b]. The handbook has the background: Example 2.2.3 (defect, node SG00000010), Theorem 2.3.3 (Knaf and Kuhlmann for Abhyankar valuations, node SG0000001E), Theorem 2.3.4 (Temkin, node SG0000001G), and Conjectures 2.3.1 and 2.3.2.

*What is open.* The first open case is the valuations of rank one with value group $\mathbb{Z}^2$ of $k(x_1, \dots, x_4)$ that are not of CA type. The conjecture V4 of note 06, local uniformization when each defect extension in a tower is independent, is also open.

#### Track FO: foliations and their quotients

The track FO (tamnd/singularity#299) works on $\mathrm{FQ}_4$ of the reduction above. Let $Y$ be a regular variety of dimension $n$ over a perfect field $k$ of characteristic $p$, with tangent sheaf $T_Y$.

**Definition 2.5.10.** A *$p$-closed foliation* on $Y$ is a saturated subsheaf $\mathcal{F} \subseteq T_Y$ that is closed under the Lie bracket and under $D \mapsto D^p$. Its rank is its rank as a sheaf, and its corank is $n$ minus the rank. Its *quotient* $Y/\mathcal{F}$ is the normal variety with the structure sheaf of the local sections $f$ of $\mathcal{O}_Y$ with $D(f) = 0$ for all local sections $D$ of $\mathcal{F}$. A foliation of rank one is *multiplicative* at a point if near the point it is generated by $\sum_i c_i x_i \partial_i$ with $c_i \in \mathbb{F}_p$ in some coordinates.

By the correspondence of Jacobson and Ekedahl, the quotients $Y/\mathcal{F}$ are the normal varieties $Z$ with $k(Y)^p \subseteq k(Z) \subseteq k(Y)$. Posva proves for 1-foliations on surfaces, and in corank one on threefolds, that blowups make the singularities multiplicative [Pos24] (cited).

**Conjecture 2.5.11 (multiplicative reduction in dimension 4).** Let $\mathcal{F}$ be a $p$-closed foliation of rank one on a regular variety of dimension 4. Then there is a proper birational morphism $Y' \to Y$, a composite of blowups, such that the transform of $\mathcal{F}$ on $Y'$ has only multiplicative singularities.

This is Problem 4.9 of note 04. Status: open. What is cited (note 58, no referee report yet): for the maximal torus $\mathbb{G}_m^4$ acting diagonally, the invariant $p$-closed foliations of each rank are classified by the subspaces $V \subseteq \mathbb{F}_p^4$ (Theorem 2.3); a finite sequence of weighted blowups with weights in $\{1, \dots, p - 1\}$ makes each of them regular on a tame toric stack, and on a regular toric variety for $p = 2$ (Theorem 3.4); and the quotients are toric (Corollary 3.6). For tori of rank 1, 2 or 3 the toric method fails: Examples 5.1 and 5.3 of note 58 have no toric resolution in any coordinates. For the torus $\mathbb{G}_m$, note 58 reduces Conjecture 2.5.11 near the exceptional divisor to Problem 6.4 of note 58, the twisted pair problem on a threefold.

*What is open.* The first open case is Problem 6.4 of note 58. Also open are Problem 4.10 of note 04, the foliations with a torus symmetry of smaller rank, and $\mathrm{AO}_4$. Note 58 also points out that the route through $z^p = g$ needs corank one, while Conjecture 2.5.11 is about rank one, and in dimension 4 these are different problems.

### How the pieces fit

The table lists the tracks, the statement each one aims at, and the place of that statement in the proof.

| Track | Aim | Feeds | Status of the aim | First open case |
|---|---|---|---|---|
| C4 | Conjecture 3.18.39 (P), then L° and H1 | Conjecture 2.5.3 | P cited for all $p$ (note 71, one referee); L° open for $\deg_{x,w} g \ge p$ | Conjecture 4.4 of note 69 |
| M2 | Conjecture 2.5.5 | $\mathrm{Emb}_3$, mixed case | proved when $\omega = 0$ (note 66) | $\omega > 0$ at the first point |
| NW | Conjecture 2.5.6 | Conjecture 2.5.3 | one step proved for $p \mid \nu$ (SG0000009D) | $p \nmid \nu$; exceptional points |
| TT | Corollary 3.21.9 | $\mathrm{Res}_4$ for $p > 24$ | proved under $\mathrm{Emb}(\mathbb{P}^4)$ and Conjecture 3.21.8 | $\mathrm{Emb}(\mathbb{P}^4)$, Lemma 3.21.2 |
| HS | an invariant for $\mathrm{Core}_3(e)$, $e \ge 2$ | $\mathrm{Emb}_3$ | law and dichotomy cited (notes 45, 48) | (O1) of note 45 |
| VD | Conjecture 2.5.9 | $\mathrm{LU}_4$ | CA type known [KK09] | non CA type, value group $\mathbb{Z}^2$ |
| FO | Conjecture 2.5.11 | $\mathrm{FQ}_4$ | maximal torus cited (note 58) | Problem 6.4 of note 58 |

The diagram shows the implications. An arrow $A \to B$ means that $A$ is used in a proof of $B$, or in the expected proof. A mark [P] means proved in the handbook, [C] cited, and [O] open.

```
 C4, NW --> Conj 2.5.3 [O] --> PILU_4 [O] --(Temkin, note 02 [C])--> LU_4 [O]
 HS --> Core_3(e), e >= 2 [O] --+
 C4, NW --> Core_3(1) [O] ------+--> Emb_3 [O] --> Emb(P^4) [O]
 M2 --> mixed case [O] ---------+
 Emb(P^4) + (p > 24) --(Thm 3.21.7 [P])--> LU_4
 VD --> LU_4 for zero defect projections [O] --> LU_4
 LU_4 + Conj 3.21.8 [O] --> Res(p,4)      (Cor 3.21.9 [P], for p > 24 with Emb(P^4))
 LU_4 + Patch_4 [O] --> Res(p,4)          (definition of Patch_4)
 AO_4 [O] + FQ_4 [O] --(note 02, Thm 2.9 [C])--> Res(p,4)
 FO --> Conj 2.5.11 [O] --> FQ_4 (rank one steps; corank gap, note 58)
```

**Remark 2.5.12.** The diagram is not a proof, and it is not a precise statement of how the pieces assemble. Some arrows are heuristics of note 02, as we said above. A precise statement of the assembly, with the exact hypotheses of each arrow, is in preparation in the research notes. Until it exists, a student should treat each arrow that is not marked [P] or [C] as a research problem in its own right.

### Exercises

The exercises go from the proved results to the open ones. The last part of each exercise points to an open problem.

1. Let $q = p^e$ and $1 \le m < q$, and let $p^j$ be the least power of $p$ with $p^j > m$. Prove that $\Theta^{\le m}_E(g + h^{p^j}) = \Theta^{\le m}_E(g)$ for each $h \in R$. Show by the example $g = 0$, $h = x_1$ with $1 \notin \Delta$ and $m = p$ that $\Theta^{\le p}_E(h^p)$ can be the unit ideal. Then read Theorem 5.2 of note 45 and say why the condition of balance is needed; compare with problem (O1).
2. Let $m = 2p$ with $p$ odd. Use the theorem of Lucas to prove that $\binom{2p}{i} \equiv 0 \pmod p$ for $0 < i < p$ and $\binom{2p}{p} \equiv 2 \pmod p$. Deduce Volume 7, Proposition 4.1.4, for $e = 1$ and $m_0 = 2$ in the case $a_1 = \dots = a_{p-1} = 0$: then $a'_p = a_p + 2 c^p$. Then let $f = z^{2p} + x_0^{a} x_1^{b}$ with $a + b \ge 2p$, with $a$ and $b$ not both divisible by $2p$, and with $E = \{1\}$. Use Lemma 61.2 of note 61, which says that the supremum in the definition of $\delta(w)$ may be taken over the translations $z \mapsto z + c$, to prove that $\delta = (a + b)/(2p)$ and $\mu_1 = b/(2p)$. So $\omega = a/(2p)$, and $\omega = 0$ if and only if $a = 0$. The case $\omega = 0$ is the case of Theorem 66.6 of note 66, and the case $\omega > 0$ is the open part of Conjecture 2.5.5.
3. Let $(x, w) \mapsto (x, w) A$ be a change of the free coordinates by a matrix $A \in \mathrm{GL}_2(K)$ at the point $P_N$ of a corner run in four variables. Show that it commutes with the corner charts, and that it maps the translation vectors $(a_m, b_m)$ by the same matrix. Deduce that being linear in the sense of Definition 2.5.4 does not depend on linear free coordinates. Volume 7, Theorem 3.18.19, proves this for all free coordinates. Then read Conjecture 4.4 of note 69 and list the monomials of $g$ that its proof must still treat.
4. Let $h \in k[x_1, \dots, x_n]$ be a form of degree $D$. Prove the identity of Euler, $\sum_i x_i \partial_i h = D h$, in each characteristic. Deduce that if $p \nmid D$, each critical point of $h$ lies on $h = 0$. For $p = 2$, show that $h = x^3 y + x^2 y^2 + x y^3$ has the critical point $(1, 1)$ with $h(1, 1) \ne 0$, and that after the cleaning, which removes the square $x^2 y^2$, this critical point lies on the zero set. Then explain why the weights $(1, \dots, 1, \nu/p)$ of the node SG0000009D are not available when $p \nmid \nu$. This is one reason why the case $p \nmid \nu$ of Conjecture 2.5.6 is open.
5. Let $X = V(F) \subset \mathbb{P}^5$ with $F = \sum_{i=0}^{5} x_i^{q+1}$ and $q = p^m$, and let $P \notin X$. Show that the projection from $P$ has local degree at least $q$ at each point of $X \cap V(\sum_i P_i x_i^q)$. This is part of Example 3.21.10. Explain why this does not contradict Theorem 3.21.7, and why it shows that Conjecture 3.21.8, and not one projection, carries the global part of the method of Jung.
6. Let $\nu$ be a valuation of CA type with value group $\mathbb{Z}^2$ and adapted basis $x_1, x_2$. Let $F/K$ be a projection with $K \supseteq k(x_1, x_2)$. Show that $F$ lies in the henselization $K^h$ of $K$, and deduce that $F/K$ has zero defect. Use that $F$ lies in the completion of $k(x_1, x_2)$, and that for a valuation of rank one the henselization is separably closed in the completion. Then explain why this argument says nothing about a valuation that is not of CA type, which is the first open case of Conjecture 2.5.9.
7. Let $Y$ be a regular variety of dimension $n$ and $\mathcal{F}$ a $p$-closed foliation of rank $r$ on $Y$, with $Z = Y/\mathcal{F}$. Prove that $[k(Y) : k(Z)] = p^r$ and $[k(Z) : k(Y)^p] = p^{n-r}$. Deduce that $Z$ is locally a cover $z^p = g$ of the Frobenius twist of $Y$ only when $r = n - 1$. This is the gap that note 58 found in Corollary 2.10 of note 02.
8. Let $V \subseteq \mathbb{F}_3^2$ be the line spanned by $(1, 2)$, and let $\mathcal{F}_V$ be the foliation on $\mathbb{A}^2$ generated by $x_1 \partial_1 + 2 x_2 \partial_2$. Find the weighted blowup with weights in $\{1, 2\}$ that makes it regular, as in Theorem 3.4 of note 58, and describe the quotient as a toric surface. Then read Example 5.1 of note 58 and explain why the same method fails for a torus of rank 1 in dimension 4, which leads to Problem 6.4 of note 58.

### Notes and references

This section collects the tracks of tamnd/singularity#290. The known cases are those of Section 2.1, with the works of Cossart and Piltant [CP08, CP09] and of Cossart, Jannsen and Saito [CJS20]. The failures are those of Section 2.2, with Narasimhan [Nar83], Moh [Moh87], Hauser [Hau10] and Hauser and Perlega [HP19a]. Abramovich discusses replacements of maximal contact in [Abr25]. The theorem of Cossart in dimension 3 is in his thesis [Cos87], and Posva gives a modern account and a global form [Pos24], which is also the source for foliations. Local uniformization and patching are in Zariski [Zar44], Temkin [Tem13], Knaf and Kuhlmann [KK09] and Cutkosky and Mourtada [CM17], and the classes of defect are in Kuhlmann [Kuh10b]. The method of Jung in dimension 4 follows Cutkosky [Cut09]. The research notes cited here are notes 02, 04, 06, 10, 45, 48, 55 to 59, 61, 62 and 64 to 71 of the project. The results of the notes that are not yet in the handbook are marked as cited, and they have no node of the map unless the text gives one.
