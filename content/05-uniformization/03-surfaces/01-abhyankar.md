---
title: The theorem of Abhyankar
nodes: [SG0000001B, SG00000010, SG0000001F]
sources: [Abh56s, Abh59, Lip78, Kuh-book, Cut04]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem of Abhyankar

Chapter 1 proves local uniformization for surfaces in characteristic 0 for every valuation with a finitely generated value group, and it leaves a gap. It also shows where characteristic $p$ enters: the projection of a surface to a plane can be inseparable, it can be wildly ramified, and it can have a defect. Abhyankar closed the case of surfaces over an algebraically closed field of characteristic $p$ by a long and direct analysis. Today the shortest route is global: resolve the surface, and read off the center of each valuation. This section states the theorem of Abhyankar, proves it from the resolution of excellent surfaces, and then returns to the local method. The local method is still useful. It is the method that has a chance in higher dimension, and its failure modes are the ones that we must understand there. So we prove the exact criterion for the lift of Section 1.3, and we test it on Artin-Schreier extensions.

**Theorem 3.1.1 (Abhyankar).** Let $k$ be an algebraically closed field of characteristic $p > 0$, and let $K/k$ be a function field of transcendence degree 2. Then each valuation of $K/k$ has local uniformization.

Lean: none yet

This is [Abh56s], and it is Volume 3, Theorem 4.1.4. Abhyankar also developed the ramification theory of such extensions [Abh59]. We do not reproduce his proof. Abhyankar used the theorem to prove the resolution of surfaces in characteristic $p$. Later Lipman proved the resolution of all excellent surfaces by a direct method [Lip78], and this is the route of Volume 4. With the resolution in hand, local uniformization of surfaces follows at once, over each ground field.

### Local uniformization from the resolution

**Proposition 3.1.2.** Let $k$ be a field of any characteristic, and let $K/k$ be a function field of transcendence degree 2. Then each valuation of $K/k$ has local uniformization.

Lean: none yet

*Proof.* Let $X$ be a model of $K/k$. It is an integral variety of dimension 2 over $k$, so it is a reduced excellent Noetherian scheme of dimension 2. By Volume 4, Theorem 2.2.1, it has a resolution. Proposition 1.4.5 gives the claim. $\square$

The theorem of Lipman is node SG0000001B of the map, with the Lean statement `Singularity.ResolutionInDim` (the statement only). Proposition 3.1.2 contains Theorem 3.1.1, since a function field over an algebraically closed field is a special case. For surfaces it also contains Corollary 1.2.8 and Volume 3, Proposition 4.1.8, which have short direct proofs.

**Corollary 3.1.3.** Let $k$ be a field of any characteristic, let $K/k$ be a function field of transcendence degree $n$, and let $v$ be a valuation of $K/k$ with $\operatorname{trdeg}_k \kappa_v \ge n - 2$. Then $v$ has local uniformization.

Lean: none yet

*Proof.* If $\operatorname{trdeg}_k \kappa_v \ge n - 1$, this is Volume 3, Proposition 4.1.8. Let $\operatorname{trdeg}_k \kappa_v = n - 2$. Choose $y_1, \dots, y_{n-2} \in \mathcal{O}_v$ whose residues form a transcendence basis of $\kappa_v$ over $k$, and let $k' = k(y_1, \dots, y_{n-2})$. By Lemma 1.4.2, $v$ is a valuation of the function field $K/k'$ of transcendence degree 2. By Proposition 3.1.2 over $k'$ it has local uniformization, and by Lemma 1.4.2 so has $v$ over $k$. $\square$

For $n = 3$ the corollary covers each valuation of a threefold whose residue field is not algebraic over $k$. This is part of the theorem of Cossart-Piltant (Volume 3, Theorem 4.1.5), node SG0000001F, stated in Lean as `Singularity.localUniformization_three`. The zero-dimensional valuations are the hard part of that theorem.

*Remark (the hypotheses, and dimension 4).* Theorem 3.1.1 assumes that $k$ is algebraically closed, because Abhyankar worked in that setting. Proposition 3.1.2 removes the assumption, but only by the global theorem of Lipman. This is why Corollary 3.1.3 holds over each field: the reduction of Lemma 1.4.2 replaces $k$ by a field $k'$ of transcendence degree $n - 2$ over $k$, and such a field is never algebraically closed when $n \ge 3$, so Theorem 3.1.1 alone would not suffice. For $n = 4$ the same reduction, with Volume 3, Theorem 4.1.5, in place of Proposition 3.1.2, gives local uniformization of each valuation of a function field of transcendence degree 4 whose residue field is not algebraic over $k$: choose $y \in \mathcal{O}_v$ with a transcendental residue, apply the theorem of Cossart and Piltant over $k(y)$, and use Lemma 1.4.2. The Abhyankar valuations are covered by [Cut20]. What remains in transcendence degree 4 is the case of valuations that are zero-dimensional and not Abhyankar. In characteristic $p$ this case is open, and nothing in this chapter changes that.

### The converse of the lifting lemma

We return to the setting of Section 1.3: $K_0 \subseteq K$ with $[K : K_0]$ finite, $v_0$ the restriction of $v$, and $e$, $f$ and $d$ the ramification index, the residue degree and the defect.

**Proposition 3.1.4.** If $K/K_0$ has an étale generator at $v$, then $e = 1$, the residue extension $Kv/K_0v_0$ is separable, and $d = 1$.

Lean: none yet

*Proof.* Let $z$ be the étale generator, with minimal polynomial $P$ over $K_0$. Over $K_0^h$ write $P = P_1Q$, where $P_1$ is the minimal polynomial of $z$ over $K_0^h$, with $z$ seen in $K^h$. As in the proof of Lemma 1.3.3, $\deg P_1 = [K^h : K_0^h] = def$, and $P_1$ and $Q$ have coefficients in the valuation ring of $K_0^h$. In $K^h$ we have $P'(z) = P_1'(z)Q(z)$. Both factors lie in the valuation ring of $K^h$, and their product is a unit, so $P_1'(z)$ is a unit.

Let $\bar{z}$ be the residue of $z$, and let $\mu$ be its minimal polynomial over $K_0v_0$. Let $z_1, \dots, z_m$ be the roots of $P_1$ in an algebraic closure of $K_0^h$, with $z_1 = z$. The valuation of $K_0^h$ has a unique extension to the algebraic closure. So each $K_0^h$-embedding $\sigma$ of $K^h$ with $\sigma(z) = z_i$ preserves the valuation, and it induces a $K_0v_0$-embedding of residue fields that maps $\bar{z}$ to $\bar{z}_i$. Thus each $\bar{z}_i$ is a root of $\mu$. Since $\bar{P}_1 = \prod (Z - \bar{z}_i)$ and $\mu$ is irreducible, $\bar{P}_1 = \mu^a$ for some $a \ge 1$. Now $\bar{P}_1'(\bar{z}) \ne 0$, because $P_1'(z)$ is a unit. So $\bar{z}$ is a simple root of $\bar{P}_1$. Hence $a = 1$, and $\mu$ is separable of degree $\deg P_1 = def$. Then
$$f = [Kv : K_0v_0] \ge [K_0v_0(\bar{z}) : K_0v_0] = def.$$
So $de \le 1$, that is, $d = e = 1$, and $Kv = K_0v_0(\bar{z})$ is separable over $K_0v_0$. $\square$

**Theorem 3.1.5.** Let $k$ be a field of any characteristic, let $K/k$ be a function field of transcendence degree 2, let $v$ be a valuation of $K/k$, and let $x, y \in K$ be algebraically independent over $k$, with $K_0 = k(x, y)$ and $v_0$ the restriction of $v$. Then $K/K_0$ has an étale generator at $v$ if and only if $v$ is not trivial and $e = 1$, $Kv/K_0v_0$ is separable and $d = 1$, or $v$ is trivial and $K/K_0$ is separable. In this case $v$ has local uniformization, and the proof does not use the theorem of Lipman.

Lean: none yet

*Proof.* For a nontrivial $v$, the equivalence is Lemma 1.3.3 and Proposition 3.1.4. For a trivial $v$, the valuation ring is $K$, and an étale generator is a primitive element $z$ of $K/K_0$, whose derivative $P'(z)$ is not 0. Such an element exists if and only if $K/K_0$ is separable. Local uniformization follows from Corollary 1.2.8 for $v_0$ and Theorem 1.3.4. $\square$

In characteristic 0 we have $d = 1$ and the residue extension is separable, so only the condition $e = 1$ remains. In characteristic $p$ they can fail for a given choice of $x, y$. For example, if $K/k(x, y)$ is purely inseparable for one choice, then each extension of $v_0$ to $K$ is unique, but there is no étale generator over this subfield. Section 3.2 studies the defect.

The criterion of Theorem 3.1.5 depends on the subfield $K_0$. The next example shows two Artin-Schreier extensions in characteristic $p$. In the first one the criterion holds for $K_0 = k(x, y)$. In the second one it fails for $k(x, y)$, but it holds trivially for another subfield, because $K$ is again a field of rational functions.

**Example 3.1.6 (Artin-Schreier extensions).** Let $k$ be a field of characteristic $p > 0$, let $K_0 = k(x, y)$, and let $v_0$ be the monomial valuation with $v_0(x) = 1$ and $v_0(y) = \sqrt{2}$. For $a \in K_0$ let $K_a = K_0(z)$ with $z^p - z = a$. Let $\operatorname{ord}_x$ be the order of vanishing along the line $x = 0$. If $\operatorname{ord}_x(a) = -1$, then $Z^p - Z - a$ is irreducible over $K_0$. Indeed, an Artin-Schreier polynomial with no root in $K_0$ is irreducible, by the argument in the proof of Volume 3, Proposition 3.2.5. For $b \in K_0$, if $\operatorname{ord}_x(b) \ge 0$, then $\operatorname{ord}_x(b^p - b) \ge 0$, and if $\operatorname{ord}_x(b) < 0$, then $\operatorname{ord}_x(b^p - b) = p\operatorname{ord}_x(b)$. In both cases $b^p - b \ne a$. So $[K_a : K_0] = p$ in the two cases below.

1. Let $a = y/x$, with $v_0(a) = \sqrt{2} - 1 > 0$. Let $v$ be an extension of $v_0$ to $K_a$. If $v(z) < 0$, then $v(z^p - z) = p\,v(z) < 0$, which is false. So $z \in \mathcal{O}_v$. The minimal polynomial $P = Z^p - Z - a$ has coefficients in $\mathcal{O}_{v_0}$, and $P'(z) = -1$ is a unit. So $z$ is an étale generator at each extension of $v_0$. By Corollary 1.2.8 and Theorem 1.3.4, each extension has local uniformization, without the theorem of Lipman. The reduction $Z^p - Z$ has the $p$ simple roots $c \in \mathbb{F}_p$, so $P$ splits into linear factors over $K_0^h$ by Hensel's lemma. Thus $v_0$ has $p$ extensions, one with $v(z - c) > 0$ for each $c \in \mathbb{F}_p$.
2. Let $a = 1/x$, with $v_0(a) = -1$. Let $w$ be an extension of $v_0$ to $K_a$. If $w(z) \ge 0$, then $w(z^p - z) \ge 0$, which is false. So $w(z) < 0$, $w(z^p - z) = p\,w(z)$, and $w(z) = -1/p$. Thus $e \ge p$, and the fundamental inequality gives $e = p$, $f = 1$, and $w$ is the only extension of $v_0$. By Proposition 3.1.4 there is no étale generator of $K_a/K_0$ at $w$. Now $x = 1/(z^p - z)$, so $K_a = k(y, z)$, and $y, z$ are algebraically independent. Let $u = 1/z$. Then $x = u^p/(1 - u^{p-1})$. Let $w'$ be the monomial valuation of $k(u, y)$ with $w'(u) = 1/p$ and $w'(y) = \sqrt{2}$. Then $w'(1 - u^{p-1}) = 0$, so $w'(x) = 1$, and $w'(x^iy^j) = i + j\sqrt{2}$. Distinct monomials $x^iy^j$ have distinct values. So $w'(\sum c_{ij}x^iy^j)$ is the least value of a term, and $w'$ restricts to $v_0$ on $K_0$. By uniqueness $w = w'$. So $w$ is a monomial valuation of the field of rational functions $k(u, y)$, and it has local uniformization by Corollary 1.2.8, or by Theorem 2.1.5.

In part 2 the subfield $k(u, y)$ is a good choice and $k(x, y)$ is a bad one, as in Example 2.2.4. The extension has $e = p$, so it is wild, but it has no defect. Section 3.2 gives an extension where no choice of the subfield removes the problem in the naive way.

*Remark (the condition on the order of $a$).* In Example 3.1.6 the hypothesis $\operatorname{ord}_x(a) = -1$ is a normalization. The argument works whenever $\operatorname{ord}_x(a) = -m$ with $p \nmid m$, because $p\operatorname{ord}_x(b)$ is then never equal to $-m$. If $p$ divides $m$, the polynomial can still be irreducible, but one must first change $z$ by an element $b$ of $K_0$ to reduce the pole: $z' = z - b$ satisfies $z'^p - z' = a - (b^p - b)$. This reduction of an Artin-Schreier equation is the basic operation of the ramification theory of [Kuh-book], and in the defect case it never ends, as Section 3.2 shows. In part 1 the residue characteristic is used only through the derivative $P'(z) = -1$, which is a unit in each characteristic. In part 2 the value $-1/p$ of $z$ comes from $p\,w(z) = -1$, and it is the source of the wild ramification.

### Notes and references

The theorem of Abhyankar is [Abh56s]. The book [Cut04] gives an account of the resolution of surfaces in characteristic $p$. The resolution of excellent surfaces is [Lip78]. Volume 4 gives the structure of its proof and cites the hard steps. Proposition 3.1.4 is a standard fact of ramification theory [Kuh-book]. None of the results of this section is in the Lean library.
