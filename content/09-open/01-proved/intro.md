# The proved cases and the reductions

This chapter has the first results of the project. Section 1.1 proves resolution in dimension 0, in each characteristic. Section 1.2 proves resolution of integral varieties in characteristic 0, from the Lean proof of Hironaka's Main Theorem I. Section 1.3 gives the step from integral varieties to reduced varieties, which is still a named hypothesis in Lean. Section 1.4 compares our statement with the statement of formal-conjectures. Section 1.5 shows that the core problem P1 is a special case of the main statement.

The definitions are those of Volume 0, Chapter 2. We recall the most important one. Let $X$ be a scheme. A morphism $\pi : Y \to X$ is a *resolution* of $X$ when these four conditions hold:

1. $Y$ is regular;
2. $\pi$ is proper;
3. the regular locus $\operatorname{Reg}(X)$ is open in $X$, and $\pi^{-1}(\operatorname{Reg}(X)) \to \operatorname{Reg}(X)$ is an isomorphism;
4. $\pi^{-1}(\operatorname{Reg}(X))$ is dense in $Y$.

For a prime $p$ or $p = 0$ and for $n \ge 0$, $\mathrm{Res}(p, n)$ is the statement that each variety of dimension at most $n$ over a field of characteristic $p$ has a resolution. A *variety* over a field $k$ is a reduced scheme that is separated and of finite type over $k$. It need not be irreducible.
