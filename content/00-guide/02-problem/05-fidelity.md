---
title: The fidelity checks
nodes: [SG0000000A, SG0000000B, SG0000001X, SG0000000C]
sources: []
status: drafted
drafted_by: writer
reviewed_by: []
---
## The fidelity checks

A Lean proof of a wrong statement is of no use. Before the project trusts a statement of the problem, the statement must pass seven checks.

| Check | Content |
|---|---|
| F1 | The file builds with the pinned toolchain, and the statements use no axiom. |
| F2 | Lean proofs of the statement in known cases. |
| F3 | Lean proofs that weaker or wrong forms of the statement are false, or accept wrong maps. |
| F4 | A strong prover gets a budget to prove the statement in a trivial way. A success is a failure of the check. |
| F5 | An independent model translates the Lean statement to English, and a person compares the result with the text. |
| F6 | Two algebraic geometers sign that the Lean statement means the text. |
| F7 | The hash of the statement file is pinned, and each proof is compared with the pinned statement. |

This section gives the first instances of F2 and F3.

**Proposition 2.5.1 (F2).** Let $X$ be a regular scheme. Then the identity $X \to X$ is a resolution of $X$.

Node: SG0000000A · Lean: `Singularity.Fidelity.isResolution_id`

*Proof.* $X$ is regular. The identity is proper. Since $X$ is regular, $\operatorname{Reg}(X) = X$, so we can take $U = X$, and the restriction of the identity to $U$ is an isomorphism. The inverse image of $\operatorname{Reg}(X) = X$ is $X$, which is dense in $X$. $\square$

**Proposition 2.5.2 (F3).** Let $X$ be a scheme with a point $x \in \operatorname{Reg}(X)$, and let $\nabla : X \sqcup X \to X$ be the codiagonal, the identity on each copy of $X$. Then $\nabla$ is not a resolution of $X$.

Node: SG0000000B · Lean: `Singularity.Fidelity.not_isResolution_codiag`

*Proof.* Assume that $\nabla$ is a resolution, and let $U = \operatorname{Reg}(X)$ be the open set of condition 3. Then the restriction $\nabla^{-1}(U) \to U$ is an isomorphism, so its map of topological spaces is injective. Let $x_1$ and $x_2$ be the images of $x$ in the first and in the second copy of $X$. The two copies have disjoint images in $X \sqcup X$, so $x_1 \neq x_2$. But $\nabla(x_1) = x = \nabla(x_2)$, and $x \in U$, so $x_1$ and $x_2$ are two different points of $\nabla^{-1}(U)$ with the same image. This is a contradiction. $\square$

If $X$ is regular and nonempty, then $X \sqcup X$ is regular, $\nabla$ is finite and so proper, and the inverse image of $\operatorname{Reg}(X)$ is all of $X \sqcup X$. So $\nabla$ satisfies conditions 1, 2 and 4, and only condition 3 fails. Without condition 3, a map of degree 2 would count as a resolution, and so would each alteration of de Jong's theorem. The proposition shows that condition 3 is necessary.

The core problem P1 of Section 2.2 must be a special case of the main statement. Else a proof of P1 tells us nothing about $\mathrm{Res}(p, n)$. The next proposition is this check.

**Proposition 2.5.3 (P1 is a special case).** Let $p \neq 0$ and let $n \ge 0$. If $\mathrm{Res}(p, n)$ holds, then each reduced hypersurface $X_g : z^p + g(x_1, \dots, x_n) = 0$ over a field of characteristic $p$ has a resolution.

Node: SG0000001X · Lean: `Singularity.purelyInseparableHypersurfaceResolution_of_resolutionInDim`

*Proof.* Let $A = k[x_1, \dots, x_n, z]$ and $f = z^p + g$. The coefficient of $f$ at the monomial $z^p$ is 1, because $p \neq 0$ and $g$ does not contain $z$. So $f \neq 0$, and $f$ is a nonzerodivisor of the domain $A$. For a nonzerodivisor $f$ of a Noetherian ring $A$ we have $\dim A/(f) + 1 \le \dim A$, and $\dim A = n + 1$. Thus $\dim X_g = \dim A/(f) \le n$.

The scheme $X_g = \operatorname{Spec} A/(f)$ is affine and of finite type over $k$. A morphism of affine schemes is separated and quasi-compact. Thus $X_g$ is a variety when it is reduced, and $\mathrm{Res}(p, n)$ gives a resolution of $X_g$. $\square$

In particular, a proof of the open case $\mathrm{Res}(p, 4)$ gives P1 for $n = 4$. The converse is not known: a proof of P1 is a test of a method, not a proof of the open case.

The statement with "smooth" in place of "regular" is false over an imperfect field (Section 2.4). The Lean proof of this third instance is planned.

Node: SG0000000C · Lean: `Singularity.exists_regular_not_smooth`
