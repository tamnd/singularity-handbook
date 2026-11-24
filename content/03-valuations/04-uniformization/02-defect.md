---
title: Results in all dimensions and the defect
nodes: [SG0000001E, SG0000001G]
sources: [KK05, Cut20, Tem13, Kuh-book, Kuh16, CM17, Hau10]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Results in all dimensions and the defect

Two results on local uniformization hold in all dimensions and in each characteristic. The first one is for a special class of valuations, and the second one allows a purely inseparable extension of the function field. In this section we state them, and we explain why the general case is hard. The proofs are not in this volume.

### Abhyankar valuations

**Theorem 4.2.1 (Knaf and Kuhlmann).** Let $K/k$ be a function field over a field $k$ of any characteristic. Each Abhyankar valuation of $K/k$ has local uniformization.

Node: SG0000001E · Lean: `Singularity.localUniformization_abhyankar` (planned, no Lean statement yet)

Knaf and Kuhlmann prove this when $Kv/k$ is separable [KK05], and Cutkosky removes this condition [Cut20]. Abhyankar valuations are defined in Definition 2.2.3. By Corollary 2.2.4 the value group of such a valuation is $\mathbb{Z}^r$, and the residue field is finitely generated over $k$. By Lemma 2.2.1, the field $K$ is a finite extension of a subfield $K_0 = k(x_1, \dots, x_r, y_1, \dots, y_s)$ on which $v$ is a monomial valuation, as in Example 2.4.1. For $K_0$ the problem is easy, because the affine space with the coordinates $x_i$ and $y_j$ is a regular model of $K_0$. The difficulty is the finite extension $K/K_0$. The proof of [KK05] uses the generalized stability theorem of Kuhlmann (Section 2.2): $(K, v)$ is a defectless field. So the finite extension has no defect, and the value group and the residue field control it.

### Purely inseparable extensions

**Theorem 4.2.2 (Temkin).** Let $K/k$ be a function field and let $v$ be a valuation of $K/k$. Then there is a finite purely inseparable extension $L/K$ such that the extension of $v$ to $L$ has local uniformization.

Node: SG0000001G · Lean: `Singularity.localUniformization_inseparable` (planned, no Lean statement yet)

This is the main theorem of [Tem13]. The extension of $v$ to $L$ is unique, because $L/K$ is purely inseparable: if $z^{p^n} \in K$, then $w(z) = v(z^{p^n})/p^n$ for each extension $w$. The paper [Tem13] gives the precise form of the statement. Temkin works with relative forms of the Zariski-Riemann space (Section 1.5). In characteristic 0 the theorem is Theorem 4.1.3, because then $L = K$.

The theorem does not say that a purely inseparable extension removes the defect. In Proposition 3.2.5 the field $K$ is perfect, so it has no purely inseparable extension, and $L/K$ still has defect $p$.

### Why defect is the obstruction

The proofs of local uniformization in low dimension follow a common pattern. One writes $K$ as a finite extension of a subfield $K_0 = K'(x)$, where $K'$ has smaller transcendence degree, and one uses induction on the transcendence degree. The extension $K/K_0$ is given by an equation $f(z) = 0$. Then one changes the coordinate $z$ to $z - a$ with $a \in K_0$ such that the value $v(z - a)$ is as large as possible, and one reads the new value or the new residue. After a pass to the henselization, the degree of the extension is $d \cdot e \cdot f$ (Section 3.2). The factor $e$ is seen by the value group and the factor $f$ by the residue field. The factor $d$ is seen by neither.

The best approximation exists when there is no defect.

**Corollary 4.2.3.** Let $(K, v)$ be a henselian valued field with $\operatorname{char} Kv = 0$, let $L/K$ be a finite extension, and let $w$ be the extension of $v$ to $L$. Then for each $z \in L \setminus K$ the set $w(z - K)$ has a largest element.

Lean: none yet

*Proof.* By Corollary 3.2.2, $d(L/K) = 1$, so $ef = [L : K]$. Proposition 3.2.3 gives the largest element. $\square$

In residue characteristic $p$ this fails. In Proposition 3.2.5 the values $w(\vartheta - s_m)$ increase with $m$, and no $a \in K$ gives the largest value. A change of coordinates cannot reach a best position, and the induction gets stuck. This is the main reason why local uniformization is known in characteristic 0 in all dimensions, but in characteristic $p$ only in dimension at most 3 and in the cases of Theorems 4.2.1 and 4.2.2. In dimension at most 3, Abhyankar, and Cossart and Piltant, treat the defect by a detailed analysis of the equations.

Several results make this precise. The *tame* valued fields are defectless, and Kuhlmann studies their algebra and model theory [Kuh16]. His book draft gives the theory of defect extensions [Kuh-book]. Cutkosky and Mourtada show that, in their setting, the defect of the extensions that come from projections is the only obstruction to the method of projections [CM17]. The survey [Hau10] explains how the invariants of characteristic 0 fail in characteristic $p$.

### Where to go next

This volume proves no theorem of local uniformization. Volume 5 is planned for the proofs of local uniformization in the known cases: Zariski in characteristic 0, Abhyankar for surfaces, and the theorem of Knaf and Kuhlmann. Volume 9, Section 2.2, gives the failure of the methods of characteristic 0, with the Artin-Schreier example of Section 3.2. Volume 9, Section 2.3, gives the two open steps of the route of valuations in dimension 4: local uniformization (Conjecture 2.3.1) and patching (Conjecture 2.3.2).
