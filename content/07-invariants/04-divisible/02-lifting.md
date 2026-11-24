---
title: Lifting a blowup of the base
nodes: [SG0000003K]
sources: [Cos87, Pos24, Hir64, CP08]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Lifting a blowup of the base

Let $q = p^e$ and let $f = z^q + g$ with $g \in R$. Some proofs in dimension $3$ do not blow up the hypersurface $X = V(f)$ directly. Cossart blows up the base $\operatorname{Spec} R$ to improve $g$, and he reads the effect on $X$ afterwards [Cos87]. Posva gives a modern account of this method for the quotients by foliations [Pos24, Appendix A]. A blowup of the base along a center $C$ comes from a blowup of $X$ only if $X$ contains a center over $C$ along which it is equimultiple. This section gives the exact test.

Let $I \subseteq R$ be the ideal of $C$. A center of $\operatorname{Spec} R[z]$ that maps isomorphically to $C$ has the ideal
$$J = (z - h) + I R[z]$$
for some $h \in R$. Indeed, $R[z]/J \cong R/I$, by the map that sends $z$ to $h$.

**Proposition 4.2.1.** Let $I$ be an ideal of $R$, let $g, h \in R$, and let $J = (z - h) + I R[z]$. Then
$$z^q + g \in J^q \iff g + h^q \in I^q.$$

Node: SG0000003K · Lean: `Singularity.X_pow_add_C_mem_pow_iff`

*Proof.* Assume that $g + h^q \in I^q$. In characteristic $p$, the Frobenius of $R[z]$ gives $(z - h)^q = z^q - h^q$. So
$$z^q + g = (z - h)^q + (g + h^q).$$
The first term lies in $J^q$, because $z - h \in J$. The second term lies in $I^q R[z] \subseteq J^q$.

Conversely, assume that $z^q + g \in J^q$. Let $\varphi \colon R[z] \to R$ be the homomorphism of $R$-algebras with $\varphi(z) = h$. Then $\varphi(z - h) = 0$ and $\varphi(a) = a$ for $a \in I$. So $\varphi(J) \subseteq I$, and thus $\varphi(J^q) \subseteq I^q$. Since $\varphi(z^q + g) = h^q + g$, we get $g + h^q \in I^q$. $\square$

Now let $R$ be a regular local ring and let $C$ be regular, so that $R/I$ is a regular local ring. Then $R[z]/J \cong R/I$, and $C' = V(J)$ is a regular center of $\operatorname{Spec} R[z]$.

**Corollary 4.2.2.** In this situation, $C' \subseteq X$ and $X$ has order $q$ along $C'$ if and only if $g + h^q \in I^q$. In that case, write $I = (x_1, \dots, x_c)$, where $x_1, \dots, x_c$ is a part of a regular system of parameters of $R$. In the $x_1$-chart of the blowup of $\operatorname{Spec} R[z]$ along $C'$, put $x_i = x_1 x_i'$ for $2 \le i \le c$ and $z - h = x_1 z'$. Then the strict transform of $X$ is
$$z'^q + x_1^{-q} \pi^*(g + h^q) = 0,$$
where $\pi$ is the blowup of the base along $C$.

*Proof.* Translate $z = z_1 + h$. Then $f = z_1^q + (g + h^q)$ and $J = (z_1) + I R[z_1]$. By Proposition 4.2.1, $f \in J^q$ if and only if $g + h^q \in I^q$. Assume this holds. The associated graded ring of $R[z_1]$ for $J$ is $\operatorname{gr}_I(R)[Z_1]$, and the initial form of $z_1^q$ is $Z_1^q \ne 0$. The initial form of $g + h^q$ has degree at least $q$ and does not contain $Z_1$. So the two forms cannot cancel, and the order of $f$ along $C'$ is exactly $q$. In the chart, $\pi^*(g + h^q) = x_1^q g'$ for some $g'$, because $g + h^q \in I^q$. Then $f = x_1^q (z'^q + g')$, and $z'^q + g'$ is the strict transform. $\square$

At a point of $C'$, the order of $f$ is at most $q$, because $f$ is monic of degree $q$ in $z$. So under the condition of the corollary, $X$ is equimultiple along $C'$. For a hypersurface, this is the condition of Hironaka for a permissible center [Hir64]. Thus the base blowup along $C$ lifts to a permissible blowup of $X$, and the strict transform is again of the form $z^q + g'$.

### When the test fails

The condition asks for an element $h$ of $R$. Over a point of $C$, a solution modulo $I^q$ may need a $q$-th root of an element of the residue field of $C$. At the generic point of a curve $C$, the residue field is a function field of transcendence degree $1$, and it is not perfect. So the test can fail even when the order of $X$ is $q$ at each closed point of $C$. Where it fails, the base blowup is still a birational step for $X$, but it is not a permissible blowup of $X$. For the resolution of $X$ alone this can be acceptable. For the embedded problem, it means that the process must use other methods near such centers. The project checks the test on the centers of the algorithm of Cossart in dimension $3$, and Volume 9 reports the results.

### Notes and references

Proposition 4.2.1 is elementary. The reduction of the problem in dimension $3$ to equations $z^p + g$ and the blowups of the base are in [Cos87] and [CP08]. The modern form of the base blowups for foliations is in [Pos24, Appendix A]. Permissible centers and normal flatness are in [Hir64].
