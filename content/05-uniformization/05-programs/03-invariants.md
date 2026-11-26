---
title: Programs with invariants that drop
nodes: [SG00000018, SG00000015, SG00000016, SG00000017, SG00000019, SG0000001R, SG00000009]
sources: [Hau03, Hau08, Hau10, Hau14, HSch12, Vil89, EV98, EH02, BM97, Wlo05, Kol07, Nar83, Gir75, Moh87, Moh96, HP19a, HP19b, HP24, HW14, Vil07, Vil08, BV10, BenV13, BBE24, BBE25, BEP, Kaw07, KM10, KM16, ATW24, ATW20, McQ20, Quek22, AQ24, ABQTW25, Wlo-cob, TemD1, TemD2, AQS24, AQS25, AT26, Abr25, Hir77, Hir03, Hir05, Hir17]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Programs with invariants that drop

The proof of resolution in characteristic 0 attaches to each point an invariant with values in a well ordered set. The algorithm blows up the locus where the invariant is maximal, and the invariant drops. The programs of this section try to build such an invariant in characteristic $p$. We first recall the proof of characteristic 0 and list what fails in characteristic $p$, with the counterexamples. Then we describe the programs of Villamayor and his school, of Kawanoue and Matsuki, of Hironaka, and of Abramovich, Temkin and Włodarczyk.

### The proof of characteristic 0 and what fails

Let $f$ be a function of order $d$ at a point $a$ of a smooth variety $W$ over a field of characteristic 0. Three facts drive the induction [Hau03, Vil89, EV98, BM97, EH02, Wlo05, Kol07].

1. *Maximal contact.* A derivative of order $d - 1$ of $f$ has order 1 at $a$, so it defines a smooth hypersurface $V$ through $a$. The hypersurface $V$ contains the points of order $d$ near $a$, and its strict transforms keep this property under permissible blowups.
2. *The coefficient ideal.* The restriction of the coefficients of $f$ to $V$ defines an ideal on $V$, the coefficient ideal. Its order is the second entry of the invariant, and the induction runs on $V$, which has smaller dimension.
3. *The monomial case.* At the end of the induction the coefficient ideal is a monomial in the exceptional divisors, and a combinatorial step finishes the proof.

In characteristic $p$ each of the three facts fails. We give the counterexamples. They are all theorems.

*Maximal contact fails.* Let $K$ be a field of characteristic 2 and let $f = x^2 + y z^3 + z w^3 + y^7 w$. The first derivatives are $0$, $z^3 + y^6 w$, $y z^2 + w^3$ and $z w^2 + y^7$, and they all have order at least 3 at the origin. So no derivative of order $d - 1 = 1$ of $f$ has order 1. More is true. Narasimhan proved that the points of order 2 of $X = V(f)$ near the origin lie in no smooth hypersurface germ, also not in a formal one [Nar83]. Volume 9, Example 2.2.1, proves this with the curve $t \mapsto (t^{32}, t^7, t^{19}, t^{15})$ in the locus of order 2. Giraud studies what remains of maximal contact in characteristic $p$ [Gir75]. The basic reason is visible already for $x^p$: the derivative of order $p - 1$ of $x^p$ is $p! \, x = 0$, and the Hasse derivatives $D^{(j)} x^p = \binom{p}{j} x^{p - j}$ vanish for $0 < j < p$.

*The residual order can increase.* For the purely inseparable equations $f = z^q + F(x_1, \dots, x_n)$ with $q = p^e$, the natural analogue of the order of the coefficient ideal is the residual order. Moh proved that under a point blowup it increases by at most $p^{e-1}$ [Moh87] (Volume 7, Theorem 1.4.1). Volume 7, Example 1.4.2, shows an increase from 5 to 7 for $p = 2$ and $q = 4$ in one blowup. In characteristic 0 the order of the coefficient ideal does not increase under such a blowup. Moh also showed that the weighted order can increase in characteristic $p$ [Moh96].

*The increase can be unbounded.* Moh claimed that the residual order stays bounded along each sequence of blowups with constant order $q$. Hauser and Perlega disproved this claim for $e \ge 3$: there is an equation $z^{p^3} + F$ and an infinite sequence of point blowups along which the residual order tends to infinity [HP19a] (Volume 7, Theorem 1.4.3). For $e = 1$ the bounded form holds [HP19a, Section 3]. Hauser and Perlega characterize the increase of the residual order [HP19b]. Hauser calls the points where the increase happens *kangaroo points*, and he describes the polynomials that produce them [Hau08]. These sequences do not contradict resolution: at some steps a larger center is permissible (Volume 7, Remark 1.4.4). But they show that the residual order is not an invariant that drops.

*The invariant need not be upper semicontinuous.* Perlega notes that the invariant of characteristic 0 is not upper semicontinuous in characteristic $p$ [HP24]. So the locus where it is maximal need not be closed, and it cannot be the center of the next blowup. Perlega constructs another invariant, which is upper semicontinuous and drops at each blowup, and with it he gives a new proof of embedded resolution of surfaces in a smooth space of dimension 3 over an algebraically closed field of any characteristic [HP24]. In place of maximal contact the proof uses coefficient ideals on regular hypersurfaces that are chosen by cleaning, a form of the Tschirnhausen change that works in each characteristic.

Hauser explains these failures in his survey [Hau10]. He argues that the equations $z^p + g$ are the core of the problem in all dimensions, which is Conjecture 2.3.7 of Volume 9. Volume 7 studies the residual order of these equations in detail. Hauser and Schicho give a combinatorial game that models the monomial step [HSch12], and Hauser gives a text on blowups with examples in characteristic $p$ [Hau14].

### Rees algebras and elimination

Villamayor and his school replace an ideal by a Rees algebra that is closed under the Hasse-Schmidt derivations [Vil07]. In characteristic 0 such an algebra has a hypersurface of maximal contact. In characteristic $p$ Villamayor replaces the restriction to a hypersurface by an *elimination algebra*, which lives on a smooth space of smaller dimension and is defined by a projection [Vil08]. The elimination algebra exists in each characteristic, and it gives invariants in each dimension.

These are theorems. Bravo and Villamayor define an upper semicontinuous function on the locus of highest multiplicity of a hypersurface over a perfect field, in each characteristic, and they show that blowups along its maximal stratum reduce the singularities to a monomial form [BV10]. Benito and Villamayor define invariants that give an analogue of the monomial case, the *strong monomial case*, and they show that for hypersurfaces in this case the resolution is combinatorial [BenV13]. Benito and Villamayor also use the invariant from elimination algebras to obtain embedded resolution of surfaces [BenV13], which was known before. Bravo, Encinas and Pascual-Escudero relate the invariants to the sequence of Nash multiplicities of arcs [BEP].

Benito, Bravo and Encinas define the *Samuel slope* of a local ring from the asymptotic Samuel function [BBE24]. For an excellent local ring $R$, the Samuel slope is infinite if and only if $R_{\mathrm{red}}$ is regular [BBE25]. This is Theorem 2.3.5 of Volume 9. The Samuel slope is a candidate for an invariant that is defined intrinsically, without a choice of an embedding.

*Remark.* In all these works the invariants are defined in each dimension. The missing step is a proof that they drop in dimension at least 3 for the general case, not only in the monomial case. In characteristic $p$ the elimination algebra loses information about the original algebra, and the step from the strong monomial case to the general case is not known. The literature presents this as a program, not as a proof of resolution in dimension 4.

### Idealistic filtrations

Kawanoue introduced the *idealistic filtration program* [Kaw07]. An idealistic filtration is a filtration of ideals that is stable under differential operators, in the sense of Hasse-Schmidt, and under integral closure. In place of a hypersurface of maximal contact it uses a *leading generator system*, a finite set of elements of the filtration whose leading terms, in suitable coordinates, are powers of the form $x_i^{p^{e_i}}$. Kawanoue and Matsuki define the basic invariants of the program and prove their main properties [KM10].

In dimension 3 Kawanoue and Matsuki give a local algorithm with an invariant that drops strictly after each blowup, and they use the method of Benito and Villamayor in it [KM16]. The global form gives embedded resolution of surfaces in a smooth space of dimension 3, which was known before. The new point is the invariant: it drops even though the residual order can increase, and the algorithm treats the kangaroo points of Hauser [KM16]. This is a theorem in dimension 3. The program in higher dimension is not complete, and its authors do not claim resolution in dimension 4.

### The announced program of Hironaka

Hironaka introduced idealistic exponents [Hir77]. Later he developed a theory of infinitely near singular points, with differential operators, aimed at characteristic $p$ [Hir03, Hir05]. In 2017 Hironaka posted on his web page a manuscript, "Resolution of singularities in positive characteristics" [Hir17], which claims embedded resolution of singularities of algebraic schemes in characteristic $p$ in each dimension.

This is an announcement. As far as we know, the manuscript has not been published in a refereed journal, and no independent account confirms the proof. The literature after 2017, for example the surveys and the papers of the other programs in this section, treats resolution in dimension at least 4 in characteristic $p$ as open. This handbook does the same. Volume 9, Conjecture 2.1.1, states the open problem.

### Weighted and logarithmic methods

In characteristic 0 a new proof of resolution uses weighted blowups.

**Theorem 5.3.1 (Abramovich-Temkin-Włodarczyk; McQuillan).** Let $X$ be a reduced closed subscheme of a smooth variety $Y$ over a field of characteristic 0. There is a canonical sequence of weighted blowups of smooth Deligne-Mumford stacks $Y_N \to \dots \to Y_0 = Y$ such that the strict transform of $X$ in $Y_N$ is smooth. The sequence is functorial for smooth morphisms. Each blowup is the weighted blowup of the center where an invariant of $X$ is maximal, and the invariant drops at each step.

Lean: none yet

This is the main result of [ATW24]. McQuillan obtained a result of the same kind independently [McQ20]. The invariant is a finite sequence of rational numbers, and it is much simpler than the invariant of Hironaka. There are logarithmic versions: Abramovich, Temkin and Włodarczyk treat toroidal orbifolds and logarithmic principalization [ATW20], Quek gives logarithmic weighted blowups [Quek22], and Abramovich and Quek use multi-weighted blowups [AQ24]. Further work treats the relative and foliated cases [ABQTW25], and Włodarczyk gives a construction by cobordant blowups [Wlo-cob]. Temkin gives an axiomatic frame, the *dream resolution*, for regular schemes with enough derivations and for excellent schemes of characteristic 0 [TemD1, TemD2]. All these results are in characteristic 0. The notes [Abr25] explain the method for a general reader.

The weighted method still uses maximal contact in a weak form: the invariant is computed from a sequence of maximal contact elements. In characteristic $p$ this fails for the reasons above. Two recent results make the obstruction precise. Abramovich, Quek and Schober show that in characteristic $p$ a weighted blowup can increase the dimension of the tangent space of the resulting stack, even when the maximal order drops, and this breaks the induction of characteristic 0. They resolve plane curves over a perfect field with multi-weighted blowups [AQS24], and they study torus actions over fields that are not perfect [AQS25]. Abramovich and Temkin classify the pinch points in characteristic 2 and show that weighted blowups cannot give a resolution of them that keeps the normal crossings locus. Each pinch point is still the coarse moduli space of a normal crossings stack [AT26]. These are theorems about characteristic $p$, and they are negative for the naive extension of the method.

*Worked example.* Let $f = x^2 + y^3$, the cusp, in the plane over a field $k$. In characteristic 0 the weighted invariant is $(2, 3)$, and the weighted blowup with the weights $w(x) = 3$ and $w(y) = 2$ resolves the curve in one step. The blowup has two charts. In the $x$-chart, $x = u^3$ and $y = u^2 y_1$, with a quotient by $\mu_3$, and $f = u^6 (1 + y_1^3)$. In the $y$-chart, $y = u^2$ and $x = u^3 x_1$, with a quotient by $\mu_2$, and $f = u^6 (x_1^2 + 1)$. In characteristic 0 the strict transforms $V(1 + y_1^3)$ and $V(x_1^2 + 1)$ are smooth and meet the exceptional divisor $V(u)$ transversally. In characteristic 2 the strict transform $V(x_1^2 + 1) = V((x_1 + 1)^2)$ in the $y$-chart is not reduced. In characteristic 3 the same happens in the $x$-chart, with $1 + y_1^3 = (1 + y_1)^3$. The reason is that the chart is a quotient by the group scheme $\mu_p$, which is not reduced in characteristic $p$, and the map $u \mapsto u^p$ is purely inseparable. So in characteristic $p$ one cannot use the weights of characteristic 0 when $p$ divides a weight, and the strict transform has to be computed on the stack with more care. This is one of the phenomena that [AQS24] studies.

*Remark.* Volume 9, Conjecture 2.3.6, asks for an invariant of the weighted form that drops under a weighted blowup of a fourfold in characteristic $p$. The conjecture does not fix the form of the invariant, and the results above show that the natural candidate fails at least in characteristic 2. This route is open.

### Status

These are theorems: the failure of maximal contact [Nar83], Moh's bound [Moh87], the unbounded increase of the residual order [HP19a], the stratification of Bravo and Villamayor [BV10], the strong monomial case [BenV13], the characterization of regularity by the Samuel slope [BBE25], the algorithm of Kawanoue and Matsuki in dimension 3 [KM16], the weighted resolution in characteristic 0 [ATW24, McQ20], and the negative results on weighted blowups in characteristic $p$ [AQS24, AT26]. The manuscript of Hironaka [Hir17] is an announcement. An invariant that drops in dimension 4 in characteristic $p$ is not known, and resolution of fourfolds by any of these programs is open.

### Notes and references

Volume 7 studies the residual order and its increase, and Volume 9, Section 2.3, lists these programs as routes. For the program of Hironaka see [Hir77, Hir03, Hir05, Hir17].
