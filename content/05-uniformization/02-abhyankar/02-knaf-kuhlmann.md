---
title: The theorem of Knaf-Kuhlmann
nodes: [SG0000001E, SG0000000Y, SG00000010]
sources: [KK05, Kuh10, Kuh-book, Cut20, Tem13]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The theorem of Knaf-Kuhlmann

A finitely generated field extension $F/k$ is *separable* if it has a separating transcendence basis, that is, a transcendence basis $\bar{y}_1, \dots, \bar{y}_t$ such that $F/k(\bar{y})$ is finite and separable. If $k$ is perfect, each finitely generated extension of $k$ is separable.

**Theorem 2.2.1 (Knaf-Kuhlmann).** Let $k$ be a field of any characteristic, let $K/k$ be a function field, and let $v$ be an Abhyankar valuation of $K/k$ such that $Kv/k$ is separable. Then $v$ has local uniformization.

Node: SG0000001E · Lean: `Singularity.localUniformization_abhyankar` (the statement only)

This is [KK05]. The Lean statement has the same hypothesis on the residue field, and it asks for a regular center. The proof below uses the inputs of [KK05], the monomial case and the generalized stability theorem [Kuh10], in the form of the lifting theorem of Section 1.3. We do not claim that it follows the steps of [KK05]. It is complete up to two cited facts: the theorem of Kuhlmann, which we state next, and the facts on the henselization that Section 1.3 uses.

### Defectless fields

A valued field $(K_0, v_0)$ is *defectless* if each finite extension of its henselization $K_0^h$ has defect 1 in the sense of Volume 3, Definition 3.2.1 [Kuh-book]. A trivially valued field is defectless: it is henselian, the valuation extends to a finite extension $L$ in a unique way, as the trivial valuation, and then $e = 1$ and $f = [L : K_0]$. Each valued field with residue field of characteristic 0 is defectless, by Volume 3, Corollary 3.2.2.

A *valued function field* is a function field $F/K_0$ with a valuation of $F$. It is *without transcendence defect* if the Abhyankar inequality for $F/K_0$ is an equality, that is,
$$\operatorname{rr}(\Gamma_F/\Gamma_{K_0}) + \operatorname{trdeg}(Fv/K_0v) = \operatorname{trdeg}(F/K_0).$$
For a trivially valued $K_0 = k$ this says that the valuation of $F/k$ is an Abhyankar valuation.

**Theorem 2.2.2 (generalized stability theorem).** Let $(F/K_0, v)$ be a valued function field without transcendence defect. If $(K_0, v)$ is defectless, then $(F, v)$ is defectless.

Lean: none yet

This is the main theorem of [Kuh10]. We use it only for a trivially valued ground field $k$. Then it says: each Abhyankar valuation of a function field over $k$ gives a defectless valued field. Its proof is long, and it uses the ramification theory of [Kuh-book]. The defect is node SG00000010 of the map, with the planned Lean name `Singularity.Valuation.defect` (no Lean statement yet).

### The proof of Theorem 2.2.1

*Proof of Theorem 2.2.1.* If $v$ is trivial, then $\mathcal{O}_v = K$, and for each finite $S \subseteq K$ an affine model $A \supseteq S$ has the center $0$ and the local ring $K$, which is regular. Assume that $v$ is not trivial.

Choice of the subfield. Let $r = \operatorname{rr}\Gamma_v$ and $t = \operatorname{trdeg}_k Kv$, so $r + t = \operatorname{trdeg}_k K$. By Volume 3, Corollary 2.2.4, $\Gamma_v \cong \mathbb{Z}^r$ and $Kv$ is finitely generated over $k$. Choose $x_1, \dots, x_r \in K$ such that $v(x_1), \dots, v(x_r)$ is a basis of $\Gamma_v$. Choose a separating transcendence basis $\bar{y}_1, \dots, \bar{y}_t$ of $Kv/k$, and lift it to $y_1, \dots, y_t \in \mathcal{O}_v$. Let $K_0 = k(x_1, \dots, x_r, y_1, \dots, y_t)$, and let $v_0$ be the restriction of $v$.

The valuation $v_0$. Apply Volume 3, Lemma 2.2.1, to the trivially valued field $k$. The $r + t$ elements are algebraically independent over $k$, and
$$\Gamma_{v_0} = \bigoplus_i \mathbb{Z}v(x_i) = \Gamma_v, \qquad K_0v_0 = k(\bar{y}_1, \dots, \bar{y}_t).$$
The proof of that lemma shows more. A nonzero polynomial $p$ in $y$ has $v(p) = 0$, so $v_0$ is trivial on $k(y)$. A polynomial $\sum_a x^ap_a$, with $p_a \in k[y]$, has value $\min_a a \cdot v(x)$. So $v_0$ is the monomial valuation of $K_0 = k(y)(x_1, \dots, x_r)$ over $k(y)$ with weights $v(x_1), \dots, v(x_r)$. By Corollary 2.1.6, $v_0$ has local uniformization.

The extension $K/K_0$. Since $r + t = \operatorname{trdeg}_k K$, the extension $K/K_0$ is algebraic, and it is finite because $K$ is finitely generated over $k$. Its ramification index is $e = 1$, because $\Gamma_{v_0} = \Gamma_v$. Its residue extension $Kv/k(\bar{y})$ is finite and separable, by the choice of $\bar{y}$. The valued field $(K_0, v_0)$ is a valued function field over the trivially valued field $k$ without transcendence defect, because $v_0$ is an Abhyankar valuation of $K_0/k$ (Lemma 2.1.2 over $k(y)$, or the count $r + t$). By Theorem 2.2.2, $(K_0, v_0)$ is defectless. The henselization $K^h = K \cdot K_0^h$ is a finite extension of $K_0^h$, so the defect $d$ of $v$ over $v_0$ is 1.

The end. By Lemma 1.3.3 there is an étale generator of $K/K_0$ at $v$. By Theorem 1.3.4, $v$ has local uniformization. $\square$

The proof applies Theorem 2.2.2 to $K_0$, which is a field of rational functions with a monomial valuation. For such a field one may hope for a direct proof that it is defectless, but we do not know a short one, and we do not give one.

**Corollary 2.2.3.** Let $k$ be a perfect field. Then each Abhyankar valuation of a function field $K/k$ has local uniformization.

Lean: none yet

*Proof.* By Volume 3, Corollary 2.2.4, $Kv$ is finitely generated over $k$, so it is separable over $k$. Theorem 2.2.1 applies. $\square$

### Examples

**Example 2.2.4 (a ramified extension that is monomial).** Let $k$ be a field of any characteristic, let $v_0$ be the monomial valuation of $k(x, y)$ with $v_0(x) = 1$ and $v_0(y) = \sqrt{2}$, and let $K = k(x, y, z)$ with $z^2 = x + y$. Then $K = k(z, y)$, since $x = z^2 - y$, and $z, y$ are algebraically independent. Let $w$ be the monomial valuation of $k(z, y)$ with weights $w(z) = 1/2$ and $w(y) = \sqrt{2}$. The initial form of $x^iy^j = (z^2 - y)^iy^j$ for $w$ is $z^{2i}y^j$, because $w(z^2) = 1 < w(y)$. Distinct monomials $x^iy^j$ give distinct initial forms, so there is no cancellation, and $w(\sum c_{ij}x^iy^j) = \min\{i + j\sqrt{2} : c_{ij} \ne 0\}$. So $w$ extends $v_0$. Its ramification index over $k(x, y)$ is 2, which is the degree $[K : k(x, y)]$, so $w$ is the only extension of $v_0$ to $K$. In the proof of Theorem 2.2.1, a basis of $\Gamma_w = \frac{1}{2}\mathbb{Z} + \mathbb{Z}\sqrt{2}$ is $w(z), w(y)$, so $K_0 = K$, and Theorem 2.1.5 gives local uniformization directly. The subfield $k(x, y)$ is a bad choice, because $e = 2$ there.

**Example 2.2.5 (an étale generator with two extensions).** Let $k$ have characteristic different from 2, let $v_0$ be as in Example 2.2.4, and let $K = k(x, y, z)$ with $z^2 = 1 + x + y$. The residue of $1 + x + y$ is $1$, a square. Over $k(x, y)^h$, Hensel's lemma gives a root of $Z^2 - (1 + x + y)$ with residue $1$, and the polynomial splits. So $v_0$ has two extensions $v_+$ and $v_-$ to $K$, with $v_\pm(z \mp 1) > 0$. For each of them $e = f = d = 1$. The element $z$ is an étale generator at both: its minimal polynomial is $Z^2 - (1 + x + y)$, and $P'(z) = 2z$ has residue $\pm 2 \ne 0$. By Theorem 1.3.4 both extensions have local uniformization.

**Example 2.2.6 (an inseparable residue field).** Let $k = \mathbb{F}_p(t)$, let $K = k(x, y)$, and let $v$ be the order of vanishing along the irreducible polynomial $\pi = y^p - t$ of $k[x, y]$. Its value group is $\mathbb{Z}$ and its residue field is $k(t^{1/p})(\bar{x})$, of transcendence degree 1. So $v$ is a divisorial valuation and it has local uniformization by Volume 3, Proposition 4.1.8. But $Kv/k$ is not separable, because $Kv$ contains $t^{1/p}$, which is purely inseparable over $k$ and not in $k$. The proof of Theorem 2.2.1 does not apply. For example, the subfield $K_0 = k(\pi, x) = k(y^p, x)$ has the same value group, and $K/K_0$ is purely inseparable of degree $p$. So $K/K_0$ has no étale generator.

### Without separability

Cutkosky proved local uniformization of Abhyankar valuations without the hypothesis that $Kv/k$ is separable [Cut20]. This is the full form of Volume 3, Theorem 4.2.1. The Lean statement `Singularity.localUniformization_abhyankar` has the hypothesis of Theorem 2.2.1, so it does not express the general form. Temkin gives another proof of the separable case as a step of his proof of inseparable local uniformization [Tem13]. Section 4.1 explains where it enters.

### Notes and references

Theorem 2.2.1 is the main theorem of [KK05]. Their theorem gives a smooth center, and the Lean statement asks only for a regular center. Theorem 2.2.2 is the main theorem of [Kuh10]. The general case without separability is [Cut20]. Lemma 1.3.3, Theorem 1.3.4 and Theorem 2.2.2 are not in the Lean library, so the proof above is not checked in Lean. A Lean proof along these lines needs the henselization, the defect, and the generalized stability theorem.
