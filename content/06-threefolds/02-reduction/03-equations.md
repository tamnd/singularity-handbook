---
title: The equations z^p + g(x, y, w)
nodes: [SG00000009, SG0000001X, SG0000001D, SG00000018]
sources: [CP19, Jac, Hau10, HP19a, Nar83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The equations z^p + g(x, y, w)

Case 1 of Theorem 1.2.6 is a hypersurface $z^p + g = 0$ over a regular base of dimension 3. In this section we look at the simplest form of these equations, the hypersurfaces
$$X_g = V(z^p + g) \subseteq \mathbb{A}^4_k, \qquad g \in k[x, y, w],$$
over a field $k$ of characteristic $p$. They are the case $n = 3$ of the problem P1 of Volume 9, Section 1.5. We prove the basic facts on their singular points, and we give a test for condition (E). Here $R = k[x, y, w]$, and $h = z^p + g \in R[z]$.

*Motivation.* The equations $z^p + g$ are the simplest equations of degree $p$ for which the method of maximal contact fails. The derivative $\partial h/\partial z = p z^{p-1}$ is $0$, so the proof of Proposition 1.2.5 gives nothing. All the information lies in $g$, a function of three variables. The points of multiplicity $p$ are the points where $g$, after a translation and the addition of a constant $c^p$, has order at least $p$ (Lemma 2.3.2). So the equations are a test case for each method in characteristic $p$: they are explicit, and their singular locus can be computed by hand. They also come from the reduction: a purely inseparable step of Section 2.2 over a regular local ring of dimension 3 gives an equation $X^p - x$ of this kind, with $x$ a power series in place of the polynomial $-g$.

### Reducedness

**Lemma 2.3.1.** The following are equivalent: (a) $X_g$ is reduced; (b) $h$ is irreducible in $R[z]$; (c) $g \notin R^p$, where $R^p = \{ a^p : a \in R \}$.

Lean: `Singularity.X_pow_add_C_tfae_threefold` (for $R = k[x, y, w]$, also with "$R[z]/(h)$ is a domain"), `Singularity.X_pow_add_C_tfae` (for each integrally closed domain $R$ of characteristic $p$)

*Proof.* If $g = a^p$ with $a \in R$, then $h = (z + a)^p$, and $z + a$ is a nonzero nilpotent element of $R[z]/(h)$. So (a) implies (c). Let $K = k(x, y, w)$. If $g = b^p$ with $b \in K$, then $b$ is a root of the monic polynomial $T^p - g \in R[T]$, so $b$ is integral over $R$. Since $R$ is a unique factorization domain, it is integrally closed, and $b \in R$. So (c) gives $g \notin K^p$, and also $-g \notin K^p$, since $-1 = (-1)^p$. By Lemma 2.1.1, $h = z^p - (-g)$ is irreducible in $K[z]$. Since $h$ is monic, Gauss's lemma shows that $h$ is irreducible in $R[z]$. So (c) implies (b). Finally, $R[z]$ is a unique factorization domain, so an irreducible element generates a prime ideal, and $R[z]/(h)$ is a domain. So (b) implies (a). $\square$

Over a perfect field, $R^p = k[x^p, y^p, w^p]$, so $g \notin R^p$ means that some monomial of $g$ has an exponent that is not divisible by $p$. Over an imperfect field, $g$ can be a constant $t \notin k^p$, and then $X_g$ is reduced, and even regular, but not smooth (Volume 9, Section 1.5).

When $X_g$ is reduced, it is a variety of dimension 3. By Theorem 1.1.2 and Theorem 1.5.5 of Volume 9, it has a resolution. So the problem P1 is solved for $n \le 3$, by the theorem of Cossart and Piltant.

Node: SG0000001X · Lean: `Singularity.purelyInseparableHypersurfaceResolution_of_resolutionInDim`

Node: SG00000009 · Lean: `Singularity.PurelyInseparableHypersurfaceResolution`

The Lean theorem `Singularity.purelyInseparableHypersurfaceResolution_of_resolutionInDim` is the implication of Theorem 1.5.5 of Volume 9. The case $n \le 3$ also needs $\mathrm{Res}(p, 3)$, and the library has only the statement of it, under the node SG0000001D. For $n = 4$ the problem is open.

### Singular points and multiplicity

**Lemma 2.3.2.** Let $k$ be perfect, and let $X_g$ be reduced. Then a point of $X_g$ is singular if and only if it lies in $V(\partial g/\partial x, \partial g/\partial y, \partial g/\partial w)$. Let $a = (c, a_1, a_2, a_3)$ be a rational point of $X_g$. Then the multiplicity of $X_g$ at $a$ is at most $p$, and it equals $p$ if and only if $g(x + a_1, y + a_2, w + a_3) + c^p$ has order at least $p$.

Lean: `Singularity.PurelyInseparableEquation.pderiv_X_pow_add_self`, `Singularity.PurelyInseparableEquation.shift_X_pow_add`, `Singularity.PurelyInseparableEquation.ord_shift_X_pow_add`, `Singularity.PurelyInseparableEquation.ord_shift_X_pow_add_eq_iff` (the derivatives, the translation and the order at a point). Lean does not prove that the order is the multiplicity, and it does not prove the first claim, which needs the Jacobian criterion.

*Proof.* We have $\partial h/\partial z = p z^{p-1} = 0$, and the other partial derivatives of $h$ are those of $g$. Over a perfect field a variety is regular at a point if and only if it is smooth there, and the Jacobian criterion [Jac] says that the hypersurface $V(h)$ is smooth at a point if and only if some partial derivative of $h$ does not vanish at it. This gives the first claim. For the second, translate $a$ to the origin. Since $(z + c)^p = z^p + c^p$, the equation becomes
$$h(z + c, x + a_1, y + a_2, w + a_3) = z^p + \bigl(g(x + a_1, y + a_2, w + a_3) + c^p\bigr).$$
The monomial $z^p$ does not occur in the second summand, which does not contain $z$. So the order of $h$ at $a$ is the minimum of $p$ and the order of the second summand. By Section 1.2, this order is the multiplicity. $\square$

*Remark (why $k$ is perfect).* Lemma 2.3.2 needs a perfect field twice. First, the Jacobian criterion tests smoothness, and smoothness agrees with regularity only over a perfect field. Second, the translation by $c$ uses a point with coordinates in $k$. Over an imperfect field the lemma fails. Let $k = \mathbb{F}_p(t)$ and $g = x^p - t$. Then all the partial derivatives of $g$ vanish, but $X_g = V(z^p + x^p - t)$ is regular at the closed point $z = 0$, $x^p = t$, $y = w = 0$. Indeed, the ideal of this point in $k[z, x, y, w]$ is $(z, x^p - t, y, w)$, and modulo $h$ it is generated by $z$, $y$ and $w$, since $x^p - t = -z^p$ there. So the maximal ideal of the local ring of $X_g$ at this point is generated by three elements, and the local ring has dimension 3. Lemma 2.3.3 assumes a perfect field for a related reason: over an imperfect residue field one needs more derivations than the $\partial/\partial u_i$, as Section 3.2 explains.

So the points of multiplicity $p$ are the worst points, and they are the points of Theorem 1.2.6. The projection $(z, x, y, w) \mapsto (x, y, w)$ is a bijection from $X_g(\bar k)$ to $\bar k^3$, because $z^p = -g$ has exactly one solution $z$ in $\bar k$. Thus the singular locus is the zero set of three equations in three variables, and it can be a curve, as in Example 2.3.4.

### A test for condition (E)

In the setting of Section 2.2, let $S = k[[u_1, \dots, u_n]]$ with $k$ perfect, let $h = X^p - f$ with $f \in S$, and let $\eta \colon X = \operatorname{Spec} S[X]/(h) \to \operatorname{Spec} S$ be the projection. The partial derivatives $\partial/\partial u_i$ are derivations of $S$, and we extend them to $S[X]$ by $\partial X/\partial u_i = 0$.

**Lemma 2.3.3.** Let $y \in X$ be a point of multiplicity $p$, and let $s = \eta(y)$. Then $\partial f/\partial u_i \in s$ for each $i$. In particular, if $V(\partial f/\partial u_1, \dots, \partial f/\partial u_n) \subseteq E$, then $(S, h, E)$ satisfies condition (E).

Lean: `Singularity.derivation_mem_of_algebraMap_mem_pow`, `Singularity.mem_comap_of_derivation_eq_neg` (the algebraic part, for a derivation of a ring $T$ and a prime $M$). Lean does not prove the step from a point of multiplicity $p$ to the prime $M$, or the second claim on the condition (E).

*Proof.* Let $M \subset S[X]$ be the prime ideal of $y$. Multiplicity $p$ means $h \in M^p S[X]_M$, by the definition of Section 1.2. Lemma 1.2.4, applied to the local ring $S[X]_M$ and the derivation $\partial/\partial u_i$, gives $\partial h/\partial u_i \in M^{p-1} S[X]_M \subseteq M S[X]_M$, because $p \ge 2$. Here $\partial h/\partial u_i = -\partial f/\partial u_i$ lies in $S$. So $\partial f/\partial u_i \in M S[X]_M \cap S = M \cap S = s$. The second claim follows, since $\eta(\operatorname{Sing}_p X)$ is then contained in $V(\partial f/\partial u_1, \dots, \partial f/\partial u_n)$. $\square$

### Two examples

**Example 2.3.4.** Let $k$ be algebraically closed and $g = x y w$. Then $g \notin R^p$, so $X_g$ is reduced. The partial derivatives are $y w$, $x w$ and $x y$. They vanish together exactly when two of $x, y, w$ are $0$, and then $z^p = -x y w = 0$. So $\operatorname{Sing} X_g$ is the union of the three lines in the hyperplane $z = 0$ over the coordinate axes of $\mathbb{A}^3$. At the origin the multiplicity is $\min(p, 3)$, the order of $z^p + x y w$. At a point $(0, a, 0, 0)$ with $a \ne 0$, Lemma 2.3.2 gives the order of $(x + a) y w = a y w + x y w$, which is 2, so the multiplicity is 2. The same holds on the other two lines. So the locus of multiplicity $p$ is the union of the three lines for $p = 2$, the origin for $p = 3$, and empty for $p \ge 5$. In all cases its image lies in $E = \operatorname{div}(x y w)$, and condition (E) holds for this $E$.

Lean: `Singularity.Examples.eval_pderiv_xyw_eq_zero_iff`, `Singularity.Examples.pow_ne_xyw`, `Singularity.Examples.pow_ne_X_mul_X_mul_X`, `Singularity.Examples.ord_X_pow_add_xyw`, `Singularity.Examples.ord_X_add_C_mul_xyw`

The example is a binomial hypersurface, so it can also be resolved by combinatorial methods (Volume 9, Section 2.4). Section 3.2 shows that its invariant $\omega$ is $0$ at the origin for $p = 3$ and $E = \operatorname{div}(x y w)$.

**Example 2.3.5 (Narasimhan).** Let $p = 2$. The hypersurface of Example 2.2.1 of Volume 9 is
$$x^2 + y z^3 + z w^3 + y^7 w = 0,$$
an equation $X_g$ with the variable $x$ in the role of $z$ and $g = y z^3 + z w^3 + y^7 w$. Over a perfect field, Lemma 2.3.2 shows that its points of multiplicity 2 are the points where $\partial g/\partial y$, $\partial g/\partial z$ and $\partial g/\partial w$ vanish. Volume 9 shows that they contain a curve through the origin of embedding dimension 4, so no regular hypersurface contains them. Narasimhan proved this in [Nar83], and his paper is the source of the example.

Node: SG00000018 · Lean: `Singularity.Examples.narasimhan`

*Example.* Let $p = 3$, let $k$ be algebraically closed of characteristic 3, and let $g = x y^2 + w^4$. Then $g \notin R^3$, so $X_g$ is reduced. The partial derivatives of $g$ are $y^2$, $2 x y = -x y$ and $4 w^3 = w^3$. They vanish together exactly when $y = w = 0$, and then $z^3 = -g = 0$. So $\operatorname{Sing} X_g$ is the line $z = y = w = 0$. At a point $(0, a, 0, 0)$ of this line, Lemma 2.3.2 gives the order of $g(x + a, y, w) = a y^2 + x y^2 + w^4$. For $a \ne 0$ this order is 2, so the multiplicity is 2. At the origin the order of $g$ is 3, so the multiplicity is 3. So the locus of multiplicity $p$ is the origin, while the singular locus is a line. Let $E = \operatorname{div}(y)$. The common zero set of the derivatives is the line $V(y, w) \subseteq E$, so condition (E) holds by Lemma 2.3.3. Now let $E = \operatorname{div}(x)$ instead. The locus of multiplicity 3 is the origin, which lies in $V(x)$, so condition (E) holds. But the line $V(y, w)$ does not lie in $V(x)$, so the test of Lemma 2.3.3 does not apply. The test is sufficient, and it is not necessary.

We compute the invariants of Section 3.2 at the origin for $E = \operatorname{div}(y)$. Put $u_1 = y$, $u_2 = x$, $u_3 = w$ and $f = g$. The exponents $(1, 2, 0)$ and $(0, 0, 4)$ of $f$ are not in $3 \mathbb{N}^3$, so $f$ is clean, and $(u; Z)$ is well adapted by Proposition 3.2.4. So $\delta(x) = \operatorname{ord} f / 3 = 1$. The coordinate $u_1 = y$ does not divide $f$, so $r_1 = 0$ and $\epsilon(x) = 3$. The initial form is $F = U_1^2 U_2$, and $\partial F/\partial U_2 = U_1^2 \ne 0$ with $U_2$ not in $E$. So $\omega(x) = \epsilon(x) - 1 = 2$. We checked the derivatives and the orders by computer.

The two examples show the two faces of the equations $z^p + g$. The first one has a divisor $E$ that controls everything, and Chapter 3 shows that its invariant is small. The second one has no hypersurface of maximal contact. In the second case there is still the characteristic polyhedron, and this is the subject of Chapter 3.

### Notes and references

Hauser explains why the equations $z^p + g$ are the core of the problem in characteristic $p$ [Hau10]. Hauser and Perlega study them in all dimensions with the residual order [HP19a], and Volume 7 follows their approach. Lemma 2.3.3 is an elementary sufficient condition for condition (E). It is not taken from [CP19].
