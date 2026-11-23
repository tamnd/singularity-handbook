---
title: The fidelity checks
nodes: [SG0000000A, SG0000000B, SG0000000C]
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

The statement with "smooth" in place of "regular" is false over an imperfect field (Section 2.4). The Lean proof of this third instance is planned.

Node: SG0000000C · Lean: `Singularity.exists_regular_not_smooth`
