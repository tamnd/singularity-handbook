---
title: Runs along a curve
nodes: []
sources: [Hir64, CJS20, Nar83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Runs along a curve

This section reports the fourteenth research result of the milestone S7, from the milestone S7.18 so far. It asks whether each run of point blowups where $\rho$ stays is finite. It gives an infinite run that follows a curve, and an infinite run that starts at an isolated point of the locus of $\rho$. The second run refutes the first form of the hypothesis H4. The section states the corrected form, with the order of $G$ in place of the order of $\widetilde\Theta(G)$, and it gives the computer tests. Volume 7, Section 3.12, gives the same result with all the details.

### The problem

By Section 3.13, the triple $(\rho, d, \tau_\rho)$ can get worse along a kangaroo path, and the full form $\widetilde\tau$ does not repair it. An invariant that gets worse at some steps can still give a resolution if each sequence of point blowups where $\rho$ stays is finite. So the question of this section is: is each such sequence finite? If the answer is no, a reader can ask which sequences are infinite, and which centers a resolution must take for them.

### The result

We use the setting of Volume 7, Sections 3.8 to 3.12. So $g = x^r G$ is clean for the divisor $\Delta$, $d = \operatorname{ord} G$, and $\rho = \rho(g)$. A *run* is a finite or infinite sequence of points $P_0, P_1, \dots$, where each $P_{i+1}$ is a point of a chart of the blowup of $P_i$ at the origin, after the cleaning, with $\rho(P_{i+1}) = \rho(P_i)$. A run *follows* a formal curve $\gamma$, with the prime ideal $I_\gamma$ of $K[[x]]$ and $K[[x]] / I_\gamma \cong K[[s]]$, if each $P_{i+1}$ is the point of the strict transform of $\gamma$ over $P_i$.

**Example 3.14.1.** Let $p = 2$, $\Delta = \{y\}$ and $g_k = x^4 y^{2k+1} + x^2 y^{3k+1} z^3$ for $k \ge 0$, as in Volume 7, Example 3.12.2. Then each $g_k$ is clean, with $(\rho, d, \tau_\rho) = (4, 4, 1)$, and the origin of the $y$-chart of the blowup of $g_k$ is $g_k$ with $k + 1$ in place of $k$. So the run does not end. It follows the $y$-axis $C$, and $\widetilde\Theta(G_k) \subseteq I_C^4$ and $\rho = 4$ at each point of $C$. The blowup of $C$ makes $\rho$ go down at each point over the origin.

**Example 3.14.2.** Let $p = 2$, $\Delta = \{x, z\}$ and $g_k = x^{5 + 3k} y^2 z^3 + x^{10 + 3k} y^3 z^2$ for $k \ge 0$, as in Volume 7, Example 3.12.4. Then each $g_k$ is clean, with $r = (5 + 3k, 0, 2)$ and the same $G = y^2 z + x^5 y^3$. The ideal $\widetilde\Theta(G)$ is $(y^2 z, x^5 y^2)$, so $\rho = d = 3$. The origin of the $x$-chart of the blowup of $g_k$ is $g_{k+1}$, so the run does not end, and it follows the $x$-axis $\gamma$. At each point of $K^3$ other than the origin, $\rho \le 2$, and $\rho = 2$ at the other points of $\gamma$. So the run starts at an isolated point of the locus where $\rho \ge 3$. Here $G \in I_\gamma^3$, but $\widetilde\Theta(G) \not\subseteq I_\gamma^3$.

**Hypothesis 3.14.3 (H4).** Let $P_0, P_1, P_2, \dots$ be an infinite run, and let $g = x^r G$ and $\rho$ be the data of $P_0$. Then the run follows a formal curve $\gamma$ through $P_0$, and $G \in I_\gamma^\rho$.

The first form of H4, in the first text of Volume 7, Section 3.12, asked for $\widetilde\Theta(G) \subseteq I_\gamma^\rho$. Example 3.14.2 shows that this form is false: no formal curve $\gamma'$ through the origin has $\widetilde\Theta(G) \subseteq I_{\gamma'}^3$ (Volume 7, Remark 3.12.6).

### The proof in short

In both examples the point is a monomial times $G$, and the chart at the origin multiplies the monomial part by a power of the chart variable and keeps a term of $G$ of degree $d$. In Example 3.14.1 this term is $x^4$. In Example 3.14.2 the chart $x$ sends the two monomials of $g_k$ to the two monomials of $g_{k+1}$, and $G$ does not change. In each case the cleanness is clear, since each monomial has an odd exponent.

In Example 3.14.2 the generators of $\widetilde\Theta(G)$ are $e_x = (k + 1) y^2 z + k x^5 y^3$, $e_z = y^2 z$ and $\partial_y G = x^5 y^2$, with the coefficients modulo $2$. For the value of $\rho$ at a point $Q \ne 0$, the proof uses that the log-Jacobian ideal at $Q$ is $\Theta(g_0) = x^5 y^2 z^2 (z, x^5)$ in the local ring of $Q$, since $x_i \partial_i$ and $\partial_i$ generate the same ideal where $x_i$ is a unit. By Volume 7, Theorem 3.1.4, $\rho(Q)$ is the order of this ideal after the division by its largest monomial factor in the components of $\Delta$ through $Q$. At a point $Q = (a, 0, 0)$ with $a \ne 0$, this is the ideal $(y^2)$. So the free derivative $\partial_y G = x^5 y^2$ has the order $7$ at the origin but the order $2$ along $\gamma$, and $\rho$ does not see the curve. The series $G = y^2 (z + x^5 y)$ is in $I_\gamma^3$, so the order of $G$ sees it.

### The test data

Tree tests with $(p, n) = (2, 3)$ explored all the charts and all the translations over $\mathbb{F}_p$ to a depth limit, from points of the first case with $p \mid |r| + d$ and $\tau_\rho \ge 2$.

1. The script `inv38` used the depth limit $10$ on $600$ starts. At $446$ starts all the branches ended, $153$ starts reached the depth limit, and $1$ start reached the time limit. The script `inv38b` used the depth limit $12$ on $800$ starts, with the results $621$, $178$ and $1$. The maximal depth of a start where all the branches end was $11$.
2. The script `inv38b` extended each deep branch along the same chart at the origin for $40$ more steps. Of the deep nodes, $238$ were axis tails. For $236$ of them $\rho$ stayed for the $40$ extra steps, and for $2$ of them $\rho$ went from $4$ to $2$. A chain of this test shows the mechanism of Example 3.14.1.
3. The script `inv39` computed the formal curve of each deep branch, and it checked the two forms of H4. For the $238$ axis tails of $(2, 3)$, the first form held for $216$ and failed for $22$, and the form of Hypothesis 3.14.3 held for $234$ and failed for $4$. The $4$ failures are artifacts of the test, at the starts $738$ and $788$. There are $18$ distinct starts of $(2, 3)$ that contradict the first form, and the start $49$ is Example 3.14.2. No start contradicts Hypothesis 3.14.3. For $(3, 3)$, the form of Hypothesis 3.14.3 held for all the $30$ axis tails, and the first form held for $28$.
4. A tree test where each center is an isolated point of the locus of the order of $\widetilde\Theta(G)$ ended at $780$ of $800$ starts of $(2, 3)$ and at $398$ of $400$ starts of $(3, 3)$. With the locus of the order of $G$ it ended at $799$ of $800$ starts of $(2, 3)$, at all $400$ starts of $(3, 3)$, and at $298$ of $300$ starts of $(2, 4)$.

The test checks that a center is isolated only against the lines and the quadrics over $\mathbb{F}_p$. The start $788$ of $(2, 3)$ passes this check, but it follows the cubic $x = 0$, $y = z + z^3$ of the locus, and the start $112$ of $(2, 4)$ follows a curve of higher degree too. The cleaning at the generic point of the curve, where the residue field is not perfect, is not tested.

### What the result means

The answer to the question of this section is no, but for a reason that each resolution must handle: a point blowup at a point of a curve in the locus of the invariant does not separate the curve from the locus. Example 3.14.2 shows that the locus must be the locus of the order of $G$, that is, the locus where the multiplicity of $G$ is at least $\rho$, and not the locus of $\rho$. The function $\rho$ is $3$ at the origin and $2$ at the generic point of the curve that the run follows. A choice of centers needs the value at the point also at the generic point of this curve. So a resolution with this invariant must take its centers in the locus of the order of $G$, with $\rho$ as a second entry, or it must use a form of $\rho$ that sees the curve.

If Hypothesis 3.14.3 holds, then a run that starts at an isolated point of the locus where the order of $G$ is at least $\rho$ is finite, and a run that does not end gives a formal curve of this locus. The blowup of this curve is a step of a different type. Volume 7, Theorem 3.4.5, controls $\rho$ at such a step under its condition (H1), and (H1) asks for the order $\rho$ of $\widetilde\Theta(G)$ along the curve. Example 3.14.2 shows that (H1) can fail on the curves of Hypothesis 3.14.3, although in this example $\rho$ goes down at each point over the origin. So the next work needs a form of Theorem 3.4.5 with a condition on $G$. In characteristic $0$ a hypersurface of maximal contact gives the analogue of H4. In characteristic $p$ it need not exist [Nar83], so the hypothesis is the point to prove.

### Status

The map has no node for this result yet, and the Lean library has no statement of it. The examples are checked by hand, and the start $49$ of the test is Example 3.14.2. The hypothesis is open. An outside expert has not yet read the result, and the milestone S7 asks for this.

### Notes and references

The use of the history of the components of the divisor is from [CJS20]. Maximal contact is from [Hir64], and its failure in characteristic $2$ is [Nar83]. Examples 3.14.1 and 3.14.2 and Hypothesis 3.14.3 are a result of the milestone S7.18 of this project (tamnd/singularity#245).
