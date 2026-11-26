---
title: Runs that follow no curve
nodes: []
sources: [CP19, CJS20, Chr79]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs that follow no curve

This section reports the fifteenth research result of the milestone S7, from the milestone S7.18. It proves the hypothesis H4 of Section 3.14 in two variables, and it proves its second half in each dimension. Then it shows that the first half is false in three variables, and it gives the example of Cossart and Piltant, where the curve of the run is transcendental. So the hypothesis must allow a subvariety of positive dimension, and the centers of a resolution with this invariant can be surfaces. Last, it shows that this form H4' is false too, by a run that takes the corners for ever. Volume 7, Section 3.13, gives the same result with all the details.

### The problem

Section 3.14 states the hypothesis H4: each infinite run where $\rho$ stays follows a formal curve along which the order of $G$ is at least $\rho$. The hypothesis has two halves: the run follows a formal curve, and the order of $G$ along the curve is at least $\rho$. The question of this section is which half is true, and in which dimension.

### The result

We use the setting of Volume 7, Sections 3.8 to 3.13. Let $Z$ be a regular formal subvariety through the point. The order of $G$ along $Z$ is $\nu^G_Z = \bar\nu_Z(g) - \sum r_i$, where $\bar\nu_Z(g)$ is the largest order along $Z$ of $g + h^p$ for a series $h$, and the sum is over the components of the divisor that contain $Z$. This order does not depend on the coordinates (Volume 7, Lemma 3.13.1). The order of the given $G$ along a curve depends on the coordinates of the cleaning, and an example for $p = 3$ shows this (Volume 7, Remark 3.13.3). A step of a run is a *corner step* if the new point is on the strict transform of the exceptional divisor of the step before.

**Theorem 3.15.1.** An infinite run follows a formal curve if and only if it has only a finite number of corner steps. If an infinite run follows a regular formal curve $\gamma$, then $\nu^G_\gamma \in \{\rho, \rho + 1\}$, and this number does not change along the run.

**Theorem 3.15.2.** Let $n = 2$, and let a run with $\rho \ge 1$ be infinite. Then the run has no corner step after its first step. So it follows a regular formal curve $\gamma$ that is not a component of the divisor, and $\nu^G_\gamma \in \{\rho, \rho + 1\}$. Thus H4 holds for $n = 2$.

**Example 3.15.3.** Let $n = 3$, let $p$ be a prime, $\Delta = \{y, z\}$ and $g = x^p y z$. The run that takes the $y$-chart and the $z$-chart at the origin in turn has $\rho = p$ and $\tau_\rho = 1$ at each point, it is in the first case, and it has a corner step at each step. So it follows no formal curve, and H4 is false for $n = 3$ and each $p$. The run lies on the surface $V(x)$, and the order of $G$ along this surface is $p = \rho$.

**Example 3.15.4.** Let $n = 4$, $\Delta = \{1, 2\}$ and $g = x_2^p x_3^p x_4 + x_1^p x_3$. This is Example 3.18 of [CP19]. Along each formal curve $x_1 = x_3 = 0$, $x_4 = \varphi(x_2)$ with the translations of Volume 7, Example 3.13.11, the triple $(\rho, d, \tau_\rho)$ is $(p, p + 1, 1)$ at each point. The curve can be transcendental, and then its Zariski closure is the plane $W = V(x_1, x_3)$. The locus where the order of $G$ is at least $\rho$ is the union of the planes $V(x_1, x_2)$ and $W$, and the residual order is $p$ at the generic point of $W$.

**Hypothesis 3.15.5 (H4').** Each infinite run with $\rho \ge 1$ lies, from some point on, on the strict transforms of a regular formal subvariety $Z$ of positive dimension with $\nu^G_Z \ge \rho$.

**Lemma 3.15.6.** For each regular formal subvariety $Z$ at the point, $\nu^G_Z \le \operatorname{ord}_Z(\widetilde\Theta(G)) + 1$.

**Example 3.15.7.** Let $n = 3$, let $p$ be a prime, $\Delta = \{y, z\}$ and $g = x^p y z + y^{p+2} z^{p+1}$. Each sequence of the $y$-chart and the $z$-chart at the origin that uses each chart an infinite number of times is an infinite run in the first case, with $\rho = d = \sigma = p$ and $\tau_\rho = 1$ at each point. For each regular formal subvariety $Z$ of positive dimension that the run follows from a point $P_N$, we have $\nu^G_Z(P_N) < \rho$. So H4' is false, for each $p$ and each $n \ge 3$. The curves $V(x, y)$ and $V(x, z)$ in the divisor have $\nu^G = \rho$, but the run follows neither of them.

### The proof in short

For Theorem 3.15.1, a run without corner steps is a sequence of charts of one variable $u$ with translations $t^{(k)}$, and the series $\sum t^{(k)} u^{k+1}$ gives the curve. Conversely, the strict transform of a regular curve meets the exceptional divisor transversally, so it leaves each component that does not contain it. For the order, the chart at the point of the curve keeps the degree of each monomial in the normal variables, and it keeps the classes modulo $p$. So the clean order along the curve does not change. In coordinates adapted to the curve, the order of $G$ at the point converges to the order of $G$ along the curve, and the order at the point is $\rho$ or $\rho + 1$ by Volume 7, Theorem 3.1.4.

For Theorem 3.15.2, the restriction of $\widetilde\Theta(G)$ to the exceptional curve has the order $\rho$, by Volume 7, Theorem 3.7.1. A corner step restricts the ideal to the strict transform of the old exceptional curve, and the order goes down by at least $\sigma \ge \rho$, from at most $\rho + 1$. So a corner step that keeps $\rho$ needs $\rho = 1$. A direct computation shows that in this case the new ideal has two independent linear forms, so $\rho$ goes down at each point of the next blowup, and the run is finite.

For Example 3.15.3, the charts send $x^p y^a z^b$ to $x^p y^{a+b} z^b$ and to $x^p y^a z^{a+b}$. The condition $\gcd(a, b) = 1$ stays, so the point stays clean, and $\widetilde\Theta(G) = (x^p)$ at each point. For Example 3.15.4, the chart $x_2$ multiplies $g$ by $x_2$, and a translation at a step where $p$ divides the exponent of $x_2$ adds a $p$-th power that the cleaning removes. At the generic point of $W$ the residue field $K(x_2, x_4)$ is not perfect, and the term $x_2^p x_4 x_3^p$ cannot be cleaned.

For Lemma 3.15.6, a derivation lowers the order along $Z$ by at most $1$, and it kills the $p$-th powers. For Example 3.15.7, write $g = y^a z^b (x^p + y^m z^l)$. The charts act on $(m - p, l - p)$ by the two elementary matrices, and they keep $a l - b m \equiv -1 \pmod p$. So the point stays clean, and $\widetilde\Theta(G) = (x^p, y^m z^l)$ at each point. By Lemma 3.15.6 a subvariety $Z$ with $\nu^G_Z \ge \rho$ has $x$ and $y^m z^l$ in its prime ideal, so it is in the plane $y = 0$ or $z = 0$. The strict transform of the plane $y = 0$ does not meet the origin of the $y$-chart, so the run leaves it, and the same holds for $z$.

### The test data

1. A tree test for $n = 2$ and $p \in \{2, 3, 5\}$ explored the full trees over $\mathbb{F}_p$ from $2259$ random clean starts with $\rho \ge 1$, to the depth $9$. In $681$ branches that reached the depth $9$, no corner step at $k \ge 1$ kept $\rho$. As a control, the counter found $100$, $166$ and $238$ corner steps on a run with $\rho = 0$, for $p = 2, 3, 5$.
2. The run of Example 3.15.3 was checked for $16$ steps with $p = 2, 3, 5$. At the last point the exponents are $1597$ and $2584$.
3. The run of Example 3.15.4 was checked for $30$ steps with $p = 2, 3, 5$. At the $\mathbb{F}_p$-points of $\mathbb{A}^4$, the pair $(\rho, d)$ is $(p, p + 1)$ exactly at the $2 p^2 - p$ points of the two planes.
4. The data of Example 3.15.7 were checked for $p = 2, 3, 5, 7$, along the sequence that takes the charts in turn and along the Fibonacci sequence for $40$ steps, along $200$ random sequences of length $30$, and for $n = 4$ with a free variable.
5. In Example 3.15.4, the blowup of the line where the two planes meet does not stop the run: after $20$ more point blowups $\rho$ is still $p$, for $p = 2, 3$. The blowup of $V(x_1, x_2)$ and then of the strict transform of $W$ gives $\rho \le 1$ at each $\mathbb{F}_p$-point over the origin.

### What the result means

The second half of H4 is a theorem, and the first half is false for $n \ge 3$. A run can take the corners of the divisor for ever, and then it follows no curve. Also a run that follows a curve need not give an algebraic center, since the curve can be transcendental. In both examples the run lies on a surface along which the order of $G$ is $\rho$. So a resolution with this invariant must take the components of the locus of the order of $G$ as centers, in each dimension, and it cannot use the residual order $d$ to choose them, since $d$ is not upper semicontinuous at the points that are not closed.

Example 3.15.7 shows that also a subvariety is not sufficient. The run sees only the initial form $x^p$ of $G$, as in Example 3.15.3, because the order of the other term goes to infinity along the run. But the order along a subvariety needs the whole ideal. So a study of one run at a time cannot give the centers. The open step is Volume 7, Question 3.13.18: does each run with an infinite number of corner steps meet, at some point, a regular curve in the divisor along which the order of $G$ is at least $\rho$? A sketch in the research notes gives a positive answer for $n = 3$ when only two charts at the origin occur. A computer test found that the blowups of the two corner curves of Example 3.15.7 make $\rho$ go down at each point over the origin.

### Status

The map has the node SG0000005K for Hypothesis 3.15.5, and the nodes SG0000005H and SG0000005J for the two examples of Section 3.14, with Lean proofs. Theorems 3.15.1 and 3.15.2 and Examples 3.15.3 and 3.15.4 have proofs in the text and no Lean proof yet. Example 3.15.7 shows that the hypothesis is false, and the map will record this with a counterexample node. Lemma 3.15.6 and Example 3.15.7 have proofs in the text and no Lean proof yet. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

Example 3.15.4 is Example 3.18 of [CP19]. The transcendence of the curve uses the theorem of Christol [Chr79]. The use of the history of the divisor is from [CJS20]. Example 3.15.7 is from note 24 of the research notes. The other results of this section are a result of the milestone S7.18 of this project (tamnd/singularity#245).
