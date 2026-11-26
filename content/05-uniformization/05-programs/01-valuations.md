---
title: Programs of valuation theory
nodes: [SG0000001E, SG0000001G, SG00000010, SG0000001H, SG0000001J, SG0000000X]
sources: [Zar40, Zar44, Zar44b, Pil, KK05, KK09, Kuh10, Kuh10b, Kuh16, Kuh25, KR23, CKR25, Kuh-book, Kuh00, San17, Cut99, CP04, Cut24, Cut15, Cut20, Cut21, CM17, Tem13, Tem23, NS14, HMOS22, Nov24, Mac36, Vaq07, Tei03, Tei14, Tev14, HOST26, Abh56s, Abh66]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Programs of valuation theory

The programs of this section work with one valuation at a time. They try to prove local uniformization in transcendence degree 4, Conjecture 2.3.1 of Volume 9, and then to patch the local solutions. We describe the plan of Zariski, the known cases (Abhyankar valuations, local uniformization in a finite extension, inseparable local uniformization), the defect, which is the obstruction that all these programs meet, and the tools that try to control it: the classification of defect extensions, key polynomials and tight extensions. We end with the counterexamples of Cutkosky, which show that a stronger relative statement fails in characteristic $p$.

### The plan of Zariski

Zariski proved local uniformization for each valuation of a function field of characteristic 0 [Zar40], and he deduced resolution of varieties of dimension at most 3 in characteristic 0 by patching [Zar44]. Volume 3, Section 4.1, and Section 1.4 of this volume state these results. The plan has two parts. The first part is local uniformization of one valuation. The second part uses the quasi-compactness of the Zariski-Riemann space [Zar44b] to reduce to finitely many valuations and then glues the local solutions.

In characteristic $p$ the second part is known in dimension at most 3. Abhyankar did it for threefolds with $p > 5$ [Abh66], and Cossart and Piltant use a version of it in their proof for threefolds [CP08, CP09]. Piltant gives an account of the patching step in a form that is close to a formal proof [Pil]. In dimension 4 the patching is open. It is Conjecture 2.3.2 of Volume 9. So a proof of Conjecture 2.3.1 alone would not give resolution of fourfolds.

The first part of the plan of Zariski reduces the multiplicity of a hypersurface along the valuation. In characteristic 0 the main tool is the Tschirnhausen transformation, which removes the term of degree $d - 1$ of a monic polynomial of degree $d$. It divides by $d$. In characteristic $p$ this fails when $p$ divides $d$, and the case $d = p$ is the core case. Cutkosky and Mourtada show that the plan of Zariski still works in characteristic $p$ when a finite linear projection of the hypersurface is defectless along the valuation [CM17]. In this sense the defect is the only obstruction to the reduction of the multiplicity by this method. The rest of this section is about the defect.

### Abhyankar valuations

Let $K$ be a function field over a field $k$, and let $v$ be a valuation of $K$ that is trivial on $k$, with value group $\Gamma$ and residue field $k_v$. The Abhyankar inequality is
$$\operatorname{rat.rk} \Gamma + \operatorname{trdeg}_k k_v \le \operatorname{trdeg}_k K.$$
The valuation is an *Abhyankar valuation* if equality holds. Chapter 2 proves local uniformization for these valuations when the residue field is separable over $k$. This is the theorem of Knaf and Kuhlmann [KK05], Theorem 2.2.1. The proof uses the generalized stability theorem of Kuhlmann [Kuh10], which says that the defect does not occur for Abhyankar valuations. Cutkosky removed the condition on the residue field.

**Theorem 5.1.1 (Cutkosky).** Let $K$ be an algebraic function field over a field $k$, and let $v$ be an Abhyankar valuation of $K$ that is trivial on $k$. Then $v$ has local uniformization.

Lean: none yet

This is the main result of [Cut20]. The proof follows the method of Zariski and Abhyankar and not the method of [KK05]. Cutkosky remarks that the absence of a defect does not appear explicitly in his proof [Cut20]. The theorem holds in each characteristic and in each dimension. So the open part of Conjecture 2.3.1 of Volume 9 is about the valuations with strict inequality in the Abhyankar inequality.

### Local uniformization in a finite extension

Knaf and Kuhlmann also proved a weak form of local uniformization for all valuations.

**Theorem 5.1.2 (Knaf-Kuhlmann).** Let $F$ be an algebraic function field over a field $K$, and let $P$ be a place of $F$ that is trivial on $K$. Then there is a finite extension $E$ of $F$ and an extension of $P$ to $E$ that has local uniformization. One can choose $E/F$ to be Galois if one first replaces $K$ by a finite purely inseparable extension. One can also choose $E$ so that the residue field extension of $E/F$ is purely inseparable and so that each element of the value group of $E$ has a multiple by a power of the characteristic exponent in the value group of $F$.

Lean: none yet

This is the main result of [KK09]. The proof uses only valuation theory. Knaf and Kuhlmann also show that no extension is needed if $F$ lies in the completion of an Abhyankar place [KK09]. The theorem does not give local uniformization of $P$ itself. To descend from $E$ to $F$ one needs a statement of the form of Theorem 1.3.4, and Proposition 3.1.4 shows that this needs an extension with no defect, no ramification index and a separable residue extension.

*Remark.* Temkin proved inseparable local uniformization, Theorem 4.1.1: the extension can be chosen purely inseparable, but it depends on the finite set of elements that one wants to make regular [Tem13]. Chapter 4 treats this theorem. Temkin reduces the remaining problem to the equations $t^p = f$ [Tem13, Remark 1.3.5]. So the theorem of Knaf and Kuhlmann with a Galois extension and the theorem of Temkin with a purely inseparable extension isolate two different parts of the problem. Neither of them gives local uniformization of the valuation itself, and we know no method that combines them.

### Reduction to rank one

Zariski already observed that the core of local uniformization is the case of valuations of rank 1. Two later results make this precise. Novacoski and Spivakovsky prove that, in each class of local rings that they consider, local uniformization for all valuations follows from local uniformization for the valuations of rank 1 [NS14]. Temkin proves a height reduction theorem: local uniformization of varieties, and of non-archimedean analytic spaces, follows from the case of valuations of height 1 [Tem23]. Both results are theorems. They reduce Conjecture 2.3.1 of Volume 9 to valuations of rank 1. They do not reduce the dimension.

### The defect

Let $(K, v)$ be a valued field, let $L/K$ be a finite extension, and assume that $v$ has a unique extension to $L$. The *defect* of $L/K$ is
$$d(L/K, v) = \frac{[L : K]}{e \, f},$$
where $e$ is the ramification index and $f$ is the degree of the residue field extension. By the lemma of Ostrowski, $d$ is a power of the characteristic exponent of the residue field [Kuh-book]. Volume 3, Definition 3.2.1, gives the definition in general, with the henselization. So $d = 1$ in residue characteristic 0, and the defect is a phenomenon of characteristic $p$. Section 3.2 shows how a defect extension blocks the lifting of regular charts (Example 3.2.3).

The basic defect extension is of Artin-Schreier type. We compute one example in full.

*Worked example.* Let $K$ be the perfect hull of $\mathbb{F}_p((t))$, with the $t$-adic valuation $v$, normalized by $v(t) = 1$. The value group of $K$ is $\mathbb{Z}[1/p]$, the residue field is $\mathbb{F}_p$, and $K$ is henselian, because it is an algebraic extension of the complete field $\mathbb{F}_p((t))$. Let $\vartheta$ be a root of $X^p - X - t^{-1}$, and let $L = K(\vartheta)$. For $n \ge 1$ let
$$c_n = \sum_{i = 1}^{n} t^{-1/p^i} \in K.$$
In characteristic $p$, $c_n^p = \sum_{i=1}^{n} t^{-1/p^{i-1}} = t^{-1} + \sum_{i=1}^{n-1} t^{-1/p^i}$. So $c_n^p - c_n = t^{-1} - t^{-1/p^n}$, and $\eta_n = \vartheta - c_n$ is a root of
$$X^p - X - t^{-1/p^n}.$$
The value of $t^{-1/p^n}$ is negative, so $v(\eta_n^p) = v(t^{-1/p^n})$ and $v(\eta_n) = -1/p^{n+1}$. Thus $v(\vartheta - c_n)$ increases with $n$ and tends to $0$, and it never reaches $0$. Volume 3, Proposition 3.2.5, proves the remaining facts: $[L : K] = p$, the value group of $L$ is $\mathbb{Z}[1/p]$, the residue field of $L$ is $\mathbb{F}_p$, and the set of the values $v(\vartheta - c)$ with $c \in K$ has no largest element. So $e = f = 1$, and the defect is $p$. Volume 9, Example 2.2.3, uses the same example. The same polynomial over $\mathbb{F}_p((t))$ gives an extension with $e = p$ and no defect (Volume 3, Example 3.2.6). The defect appears only after we adjoin all the $p$-power roots of $t$.

The example shows the mechanism. The element $\vartheta$ is a limit of elements of $K$ in the sense of the value, but it does not lie in $K$. A regular system of parameters cannot see the extension: the value group and the residue field do not change. A method that reads local uniformization from the value group and the residue field, as in Chapter 2, has nothing to work with.

### Dependent and independent defect

Kuhlmann divides the Artin-Schreier defect extensions into two classes, the *dependent* ones and the *independent* ones [Kuh10b]. The definition uses the distance of a generator $\vartheta$ from $K$, that is, the cut in the value group that the values $v(\vartheta - c)$, $c \in K$, define. Roughly, a dependent extension comes from a purely inseparable defect extension by a deformation, and an independent extension does not. Kuhlmann argues that the dependent defect is the harder case, both for local uniformization and for the model theory of valued fields in characteristic $p$.

Three later results develop this classification. Kuhlmann and Rzepka extend the classification to mixed characteristic, and they prove that deeply ramified fields admit only independent defect extensions of prime degree [KR23]. Cutkosky, Kuhlmann and Rzepka prove that a Galois defect extension of prime degree is independent if and only if its module of relative Kähler differentials of the valuation rings is zero [CKR25]. Kuhlmann studies the higher ramification groups of these extensions in [Kuh25]. These are theorems of valuation theory. They give a precise language for the obstruction. They do not yet give a method to remove a defect by blowups.

*Remark.* The tame fields of Kuhlmann are defectless, and their model theory is well understood [Kuh16]. Kuhlmann proposed to prove local uniformization by reduction to a tame situation, and he described this program in [Kuh00]. The program explains why the theorem of Knaf and Kuhlmann needs a finite extension: the extension makes the field closer to a tame field. To remove the extension one has to control the defect extensions that occur on the way down. This step is open.

### Key polynomials

The second tool is the theory of key polynomials. Let $(K, v)$ be a valued field and let $\mu$ be an extension of $v$ to $K(x)$. MacLane constructs $\mu$ from $v$ by a sequence of augmentations along key polynomials when $v$ is discrete of rank 1 [Mac36], and Vaquié extends the theory to each valuation, with limit augmentations [Vaq07]. Volume 3, Theorem 3.3.5, states the theorem of MacLane and Vaquié, Theorem 3.3.51 gives the criterion for a finite chain, and Example 3.3.14 gives an infinite chain. Herrera Govantes, Mahboub, Olalla Acosta and Spivakovsky give an equivalent theory of key polynomials for simple extensions of valued fields [HMOS22].

Key polynomials measure the defect. For a simple extension, the defect is a product of the degrees of the limit steps in a complete set of key polynomials. San Saturnino proved this [San17], and he deduces a form of local uniformization for valuations of rank 1 under inductive assumptions of no defect. Novacoski proves that sequences of key polynomials give generators of an extension of valuation rings when the initial index equals the ramification index, and he deduces the conjecture of Knaf in the case of pure extensions [Nov24].

*Remark.* The program of Spivakovsky uses key polynomials to construct the local uniformization of a valuation of rank 1 step by step. Each key polynomial is a candidate for a new regular parameter after a blowup. The limit key polynomials are the places where the defect enters: in the worked example above, the polynomials $X - c_n$ form an infinite sequence with no limit in $K$. A proof of Conjecture 2.3.1 of Volume 9 along these lines would need to control the limit key polynomials in four variables. This is open.

### Tight extensions and the program of Teissier

Teissier proposes to prove local uniformization by embedded resolution of a toric variety [Tei03]. Let $R$ be a local domain, and let $v$ be a valuation of its fraction field centered at $R$. The graded algebra $\operatorname{gr}_v R$ of $v$ is, when the residue field of $v$ is the residue field of $R$ and is algebraically closed, the algebra of a semigroup, and $R$ is a deformation of it in a precise sense. Teissier develops the theory of *overweight deformations* in [Tei14]. Since the semigroup need not be finitely generated, the toric geometry is in infinitely many variables, and one has to reduce to finitely many. Tevelev treats one case of a question of Teissier on this reduction [Tev14].

The program needs to pass from $R$ to its completion $\hat{R}$ without a change of the value group. Teissier conjectured in 2003 that each valuation of an excellent local domain has such a *tight* extension to $\hat{R}$. Herrera Govantes, Olalla Acosta, Spivakovsky and Teissier prove this conjecture in a preprint of 2026 [HOST26]. The authors present it as a tool for the recent approaches to local uniformization in characteristic $p$. This is a theorem in a recent preprint. We do not know of a published review of it. The toric part of the program in characteristic $p$ and transcendence degree 4 is open.

### Local monomialization and its failure

The relative form of local uniformization is *local monomialization*. Let $k$ be a field, let $K \subseteq L$ be algebraic function fields over $k$ with $L/K$ finite, let $v$ be a valuation of $L$ that is trivial on $k$, and let $R \subseteq S$ be regular local rings, essentially of finite type over $k$, with fraction fields $K$ and $L$, such that $S$ dominates $R$ and $v$ dominates $S$. A *local monomialization* of $R \to S$ along $v$ is a pair of sequences of blowups in regular centers along $v$, $R \to R'$ and $S \to S'$, such that $S'$ dominates $R'$, and there are regular parameters $u_1, \dots, u_n$ of $R'$ and $x_1, \dots, x_n$ of $S'$, units $\gamma_i$ of $S'$ and a matrix $(a_{ij})$ of natural numbers with nonzero determinant such that
$$u_i = \gamma_i \prod_{j = 1}^{n} x_j^{a_{ij}} \quad \text{for } 1 \le i \le n.$$
Cutkosky proved that local monomialization exists in characteristic 0 [Cut99]. In characteristic $p$ it fails.

**Theorem 5.1.3 (Cutkosky).** Let $k$ be a field of characteristic $p > 0$ with at least 3 elements, and let $n \ge 2$. There are algebraic function fields $K \subseteq L$ of transcendence degree $n$ over $k$, with $L/K$ finite, a valuation $v$ of $L$ that is trivial on $k$, and regular local rings $R \subseteq S$ as above, such that $R \to S$ has no local monomialization along $v$. The same example has no weak local monomialization.

Lean: none yet

This is the main result of [Cut15]. The examples come from defect extensions. Cutkosky and Piltant had earlier shown that the stronger form of monomialization, *strong local monomialization*, which asks that the matrix be of a special triangular form, fails for a tower of two Artin-Schreier defect extensions of function fields of surfaces [CP04]. In that paper they also prove strong local monomialization for defectless extensions of function fields of dimension 2. Cutkosky later gave an example in a tower of two independent defect extensions [Cut24]. Cutkosky also shows that in dimension 2 there are stable monomial forms along suitable sequences of blowups, but that they can change in an erratic way under further blowups, with examples from towers of Artin-Schreier defect extensions [Cut21].

*Remark.* Theorem 5.1.3 is not a counterexample to local uniformization. Local uniformization concerns one field, and local monomialization concerns a map between two fields. But the theorem shows that the relative method, which in characteristic 0 passes from a subfield $K_0$ to $K$, cannot be used in characteristic $p$ without control of the defect. This agrees with Proposition 3.1.4 and Example 3.2.3.

### Status

These are theorems: local uniformization of Abhyankar valuations in each characteristic [KK05, Cut20], local uniformization in a finite extension [KK09], inseparable local uniformization [Tem13], the reduction to rank 1 [NS14, Tem23], the reduction of the multiplicity when a projection is defectless [CM17], the classification of Artin-Schreier defect extensions [Kuh10b, KR23, CKR25], and the failure of local monomialization in characteristic $p$ [Cut15]. The existence of tight extensions is a theorem in a recent preprint [HOST26]. Local uniformization of valuations of rank 1 with a defect in transcendence degree 4 is open, and so is the patching in dimension 4.

### Notes and references

Volume 3, Chapters 3 and 4, give the valuation theory that this section uses. For the defect see [Kuh-book]. For the program of Kuhlmann see [Kuh00]. For local monomialization and its failure see [Cut99, CP04, Cut15, Cut24]. For key polynomials and the defect see [San17].
