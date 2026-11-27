---
title: Jung's method for fourfolds in large characteristic
nodes: [SG0000007W, SG0000007X, SG0000007Y, SG0000007Z, SG00000080, SG00000081, SG00000082, SG00000083, SG00000084, SG00000085, SG00000086, SG00000087, SG00000088]
sources: [Cut09, Abh66, Zar44, KKMS, Kat94, Niz06, Tem08, EGA4, Hir64, Kol07, KM10, BenV13, Nar83]
status: drafted
drafted_by: writer
reviewed_by: []
---
## Jung's method for fourfolds in large characteristic

This section reports the twenty-first research result, from the track TT (tamnd/singularity#297). It asks how far the proof of Abhyankar and Cutkosky for threefolds in characteristic $p > 5$ goes in dimension 4. The target, called Target T in the research notes, is resolution of 4-folds in characteristic $p > 24 = 4!$. The answer is that the local half of the method goes through, under one hypothesis on divisors in $\mathbb{P}^4$, and that the global half needs a patching theorem that nobody can prove, also in characteristic 0. The section also corrects a claim of the research notes: a global projection of small local degree does not come from the bound of Albanese, and the Hermitian 4-fold shows why.

### The problem

Volume 6, Section 1.2, gives the plan of [Cut09]. Theorem 1.2.1 of that section, due to Albanese and Abhyankar, gives a normal projective model of a function field of dimension $d$ whose points have multiplicity at most $d!$. For $d = 3$ and $p > 6$, each point has multiplicity less than $p$, and in small multiplicity the method of Jung works: project to a regular 3-fold, resolve the discriminant of the projection, and use that a tame cover of a regular scheme branched along a divisor with normal crossings is toroidal. This gives local uniformization. Patching (Volume 3, Chapter 4) then gives a resolution.

For $d = 4$ the same plan needs $p > 24$ and two theorems in dimension 4: embedded resolution of the discriminant, a divisor in a regular 4-fold, and patching of local uniformizations of 4-folds. An earlier version of the research notes claimed that embedded resolution of 3-folds and $p > 24$ give resolution of 4-folds at once, by one global generic projection. This section shows what is true.

We work over an algebraically closed field $k$ of characteristic $p > 0$. A variety is an integral separated scheme of finite type over $k$. For a noetherian local ring $R$ we write $e(R)$ for its multiplicity, $R^*$ for its completion and $M(R)$ for its maximal ideal. A local blowup of a regular local ring $R$ along a valuation ring $V$ that dominates $R$ is a ring $R[P/x]_{\mathfrak{m}}$, where $P$ is a prime of $R$ with $R/P$ regular, $x \in P$ with $P/x \subseteq V$, and $\mathfrak{m}$ is the center of $V$.

### The hypotheses

**Definition 3.21.1 (embedded resolution of divisors in $\mathbb{P}^4$).** The statement $\mathrm{Emb}(\mathbb{P}^4)$ says: for each reduced divisor $D \subset \mathbb{P}^4_k$ there is a finite sequence of blowups $W_r \to \dots \to W_0 = \mathbb{P}^4_k$ in regular centers such that $W_r$ is regular and the total transform of $D$ in $W_r$ is a divisor with simple normal crossings.

Node: SG0000007W · Lean: none yet

This is open for each $p$. It follows from embedded resolution of reduced 3-folds in regular 4-folds. The analogue for $\mathbb{P}^3$ is the theorem of Abhyankar on embedded resolution of surfaces [Cut09], Volume 6, Theorem 1.2.2. The method below uses it only in a local form.

**Lemma 3.21.2.** Assume $\mathrm{Emb}(\mathbb{P}^4)$. Let $R$ be the local ring of $\mathbb{P}^4_k$ at a closed point, let $0 \ne f \in R$, and let $V$ be a valuation ring of the fraction field of $R$ with residue field $k$ that dominates $R$. Then there is a finite sequence of local blowups $R \to R_0$ along $V$ such that $f = \epsilon y_1^{c_1} \cdots y_4^{c_4}$ with $y_1, \dots, y_4$ a regular system of parameters of $R_0$ and $\epsilon$ a unit of $R_0$.

Node: SG0000007W · Lean: none yet

*Proof.* Write $f = g/h$ with polynomials $g, h$ in affine coordinates and $h$ a unit of $R$. Let $D$ be the closure of $V(g)$ together with the hyperplane at infinity, and take $W_r \to \dots \to W_0$ as in Definition 3.21.1. Let $R_i$ be the local ring of $W_i$ at the center of $V$. If this center lies on the center $Z_i$ of $W_{i+1} \to W_i$, then $R_i \to R_{i+1}$ is the local blowup along $V$ at the prime of $Z_i$, and otherwise $R_{i+1} = R_i$. The total transform of $D$ has simple normal crossings at the center of $V$ on $W_r$, so $g$ is a unit times a monomial in a regular system of parameters of $R_r$. The residue field of $V$ is $k$, so this center is a closed point. $\square$

The cited inputs are stated as hypotheses on the map, because they are published theorems that the project has not proved in Lean.

**Hypothesis 3.21.3 (Albanese).** For each function field $K/k$ of transcendence degree $d$ there is a normal projective variety with function field $K$ whose points all have multiplicity at most $d!$.

Node: SG0000007Y · Lean: none yet

This is [Cut09, Theorem 1.4], Volume 6, Theorem 1.2.1. [Cut09] states it for each $d$.

**Hypothesis 3.21.4 (Abhyankar's lemma).** Let $R = k[[y_1, \dots, y_d]]$ with fraction field $K$, and let $L/K$ be a finite extension that is unramified outside $V(y_1 \cdots y_d)$ and tamely ramified at each prime $(y_i)$. Then there is an integer $N$ with $p \nmid N$ such that $L \subseteq K(y_1^{1/N}, \dots, y_d^{1/N})$. The integral closure of $R$ in $L$ is $k[[z_1, \dots, z_d]]^G$ with $z_i^N = y_i$ and $G \subseteq \mu_N^d$ acting diagonally, and it is generated over $R$ by elements $s_j$ such that $s_j^N$ is a monomial in the $y_i$.

Node: SG0000007Z · Lean: none yet

This is [Cut09, Theorem 14.1 and Corollary 14.2], see also [Abh66].

**Hypothesis 3.21.5 (resolution of log regular schemes).** A log regular scheme $X$ in the sense of Kato has a projective log blowup $Y \to X$ with $Y$ regular that is an isomorphism over the open set where the log structure is trivial.

Node: SG00000080 · Lean: none yet

This is [Kat94, Section 10] and [Niz06, Theorem 5.7]. It is the toroidal resolution of [KKMS] in the language of log geometry, and it holds in each characteristic.

### Local uniformization

The first fact is a standard lemma. It makes explicit a point that the proof of [Cut09, Theorem 14.4] uses without a statement: the discriminant in that proof is nonzero only if the extension is separable.

**Lemma 3.21.6.** Let $R$ be a normal local domain, essentially of finite type over $k$, with fraction field $K$, and let $K^*$ be the fraction field of $R^*$. Let $L/K$ be a finite extension, $T$ the integral closure of $R$ in $L$, $S$ the localization of $T$ at a maximal ideal, and $L^*$ the fraction field of $S^*$. If $[L^* : K^*] < p$, then $L/K$ is separable.

Node: SG00000081 · Lean: none yet

*Proof.* The ring $R$ is excellent, so $T$ is finite over $R$ and $T \otimes_R R^*$ is the product of the completions $T_{\mathfrak{n}}^*$ over the maximal ideals $\mathfrak{n}$ of $T$. Each $T_{\mathfrak{n}}^*$ is a normal domain, since $T_{\mathfrak{n}}$ is normal and excellent. Inverting the nonzero elements of $R$ gives $L \otimes_K K^* \cong \prod_{\mathfrak{n}} L_{\mathfrak{n}}^*$, a product of fields, and $L^*$ is one of them. Let $L_s$ be the separable closure of $K$ in $L$ and $p^a = [L : L_s]$. Then $L_s \otimes_K K^*$ is a product of fields $F_i$, and $L \otimes_K K^* \cong \prod_i L \otimes_{L_s} F_i$. Each $A_i = L \otimes_{L_s} F_i$ has dimension $p^a$ over $F_i$, and $x^{p^a} \in F_i$ for each $x \in A_i$, because $L^{p^a} \subseteq L_s$. So each element of $A_i$ is a unit or nilpotent, and $A_i$ is local. It is reduced, as a factor of a reduced ring, so it is a field of degree $p^a$ over $F_i$. Hence each field $L_{\mathfrak{n}}^*$ has degree divisible by $p^a$ over $K^*$, and $[L^* : K^*] < p$ gives $a = 0$. $\square$

**Theorem 3.21.7.** Assume $\mathrm{Emb}(\mathbb{P}^4)$, and let $p > 24$. Let $L$ be a function field of transcendence degree 4 over $k$ and $V$ a valuation ring of $L$ that contains $k$. Then there is a regular local ring $A$, essentially of finite type over $k$, with fraction field $L$ and dominated by $V$.

Node: SG00000082 · Lean: none yet

This is [Cut09, Theorem 14.4] in dimension 4. It is not a new theorem: the proof of Cutkosky uses dimension 3 only through embedded resolution of surfaces and the bound $3! < p$, and here Lemma 3.21.2 and the bound $4! < p$ take their place. We give the proof so that each input is visible.

*Proof.* If the residue field of $V$ is not $k$, then $V$ is a localization of a valuation ring $V'$ of $L$ with residue field $k$, and a regular local ring dominated by $V'$ has a localization that is dominated by $V$. So we can assume that $V$ has residue field $k$. By Hypothesis 3.21.3 there is a normal projective model of $L$ with all multiplicities at most $24$. Let $S$ be its local ring at the center of $V$. Then $e(S) \le 24 < p$. We use induction on $e(S)$, over the normal local rings $S$ of $L$, essentially of finite type over $k$ and dominated by $V$, with $e(S) < p$. If $e(S) = 1$, then $S$ is regular and we take $A = S$.

*Step 1, a projection at the point.* Choose a system of parameters $x_1, \dots, x_4$ of $S$ with $e((x)S) = e(S)$ [Cut09, Theorem 4.1]. Put $K = k(x_1, \dots, x_4)$ and $R = k[x_1, \dots, x_4]_{(x)}$, the local ring of $\mathbb{P}^4$ at a closed point. Then $S$ dominates $R$, $L/K$ is finite, and $S$ is a localization of the integral closure of $R$ in $L$. Let $K^*$ and $L^*$ be the fraction fields of $R^*$ and $S^*$. Then $[L^* : K^*] = e((x)S^*) = e(S) < p$, so $L/K$ is separable by Lemma 3.21.6. Choose generators $r_j \in S$ of $L/K$ that are integral over $R$, with separable minimal polynomials $f_j$, and put $f = \prod_j \delta(f_j) \ne 0$, where $\delta$ is the discriminant.

*Step 2, the discriminant.* The valuation ring $V \cap K$ dominates $R$ and has residue field $k$. By Lemma 3.21.2 there is a sequence of local blowups $R \to R_0$ along $V$ with $f = \epsilon y_1^{c_1} \cdots y_4^{c_4}$. Let $S_0$ be the local ring of the integral closure of $R_0$ in $L$ at the center of $V$.

*Step 3, the multiplicity does not go up.* Let $K_0^*$ and $L_0^*$ be the fraction fields of $R_0^*$ and $S_0^*$. The completions embed compatibly, $K^* \subseteq K_0^*$ and $L_0^* = K_0^*(L^*)$, so $$e(S_0) \le e(M(R_0) S_0) = [L_0^* : K_0^*] \le [L^* : K^*] = e(S).$$

*Step 4, the cover is tame.* Away from $V(y_1 \cdots y_4)$ the discriminants are units, so $L_0^*$ is unramified there. At $(y_i)$, the fundamental inequality $\sum_l e_l f_l \le [L_0^* : K_0^*] < p$ shows that each ramification index is prime to $p$ and each residue extension is separable. So Hypothesis 3.21.4 applies. If $L_0^* = K_0^*$, then $S_0^* = R_0^*$ and $S_0$ is regular. Otherwise there are a prime $q \ne p$ and $s \in L_0^*$ whose minimal polynomial over $K_0^*$ is $Z^q - y_1^{a_1} \cdots y_4^{a_4}$ [Cut09, p. 46], and $[L_0^* : K_0^*(s)] \le e(S)/q$.

*Step 5, monomial blowups.* By [Cut09, Lemma 14.3] there is a sequence of local blowups $R_0 \to R_1$ along $V$ and a regular system of parameters $z_1, \dots, z_4$ of $R_1$ with $y_1^{a_1} \cdots y_4^{a_4} = \epsilon^* (z_1^{m_1} \cdots z_4^{m_4})^q z_1^{b_1} \cdots z_4^{b_4}$, $\epsilon^*$ a unit, and $b_1 + \dots + b_4 < q$. Let $S_1$ be the next local ring of $L$ over $R_1$. With $x = s (z_1^{m_1} \cdots z_4^{m_4})^{-1}$ we have $x^q = \epsilon^* z_1^{b_1} \cdots z_4^{b_4}$. Let $F$ be the local ring of the integral closure of $R_1^*$ in $K_1^*(x)$ under $S_1^*$. Then $e(F) \le \max(1, b_1 + \dots + b_4) < q$, and $$e(S_1) \le e(F) \, [L_1^* : K_1^*(x)] \le \frac{e(F)}{q} \, e(S) < e(S).$$ By induction there is a regular $A$ dominated by $V$. $\square$

The conclusion is local uniformization without a finite set: the regular ring $A$ need not contain given elements of $V$. The rings $S \subseteq S_0 \subseteq S_1 \subseteq \cdots$ of the proof increase, so a finite set inside the first $S$ stays inside $A$. But the model of Albanese need not contain a given finite set. So the affine form of local uniformization of Volume 9, Conjecture 2.3.1, with its finite set, does not follow.

### From local uniformization to resolution

**Conjecture 3.21.8 (patching in the form of Zariski).** If for each function field $L$ of transcendence degree 4 over $k$, each valuation ring of $L$ that contains $k$ dominates a regular local ring, essentially of finite type over $k$, with fraction field $L$, then each variety of dimension 4 over $k$ has a resolution.

Node: SG0000007X · Lean: none yet

This is the form of the patching step in [Zar44] and in [Cut09, Section 16]. Its premise has no finite set, so it is weaker than the premise of Volume 9, Conjecture 2.3.2. Thus Conjecture 3.21.8 implies Conjecture 2.3.2 for 4-folds, and it is a priori a stronger assumption. In characteristic 0 its conclusion is true by the theorem of Hironaka, but no proof by patching is known for 4-folds, also in characteristic 0. For 3-folds, [Cut09, Theorems 15.1, 16.1 and 16.2] prove the analogue from the quasi-compactness of the Zariski-Riemann space and principalization of ideals on regular 3-folds.

**Corollary 3.21.9.** Assume $\mathrm{Emb}(\mathbb{P}^4)$ and Conjecture 3.21.8, and let $p > 24$. Then each variety of dimension 4 over $k$ has a resolution.

Node: SG00000083 · Lean: none yet

*Proof.* Theorem 3.21.7 gives the premise of Conjecture 3.21.8. $\square$

This is the correct form of the claim that embedded resolution of 3-folds and $p > 24$ give resolution of 4-folds. Of its two hypotheses, the second is the harder one. It is also open in characteristic 0 as a theorem about the method of Zariski.

### One global projection

The claim corrected above came from a sketch with one global projection: replace $X$ by the model of Albanese, project it generically to $\mathbb{P}^4$, bound the local degrees by the multiplicities, and resolve the branch divisor. The step that fails is the third one. The local degree of a finite map at a point equals the multiplicity of the point only when the center of projection is transversal to the tangent cone there. A generic projection is transversal at a general point, not at each point. Abhyankar and Cutkosky avoid this by a choice of the parameters at each point, as in Step 1 of Theorem 3.21.7, and this is why their method is local. The next example shows that the failure is not a matter of a better choice of the projection.

**Example 3.21.10 (the Hermitian 4-fold).** Let $q = p^m$ with $m \ge 1$, and let $X = V(F) \subset \mathbb{P}^5_k$ with $F = \sum_{i=0}^{5} x_i^{q+1}$. Then $X$ is smooth, so each of its points has multiplicity 1. For each point $P \notin X$, the linear projection $\pi_P \colon X \to \mathbb{P}^4$ from $P$ is finite and flat of degree $q + 1$, and its local degree is at least $q$ at each point of the 3-fold $R_P = X \cap V(\sum_i P_i x_i^q)$. There are two cases:

1. If $P$ is projectively $\mathbb{F}_{q^2}$-rational, then the local degree is $q + 1$ at each point of $R_P$, and $\pi_P$ is tamely ramified along $R_P$ with ramification index $q + 1$.
2. Otherwise the local degree is $q$ at the generic point of each component of $R_P$, and $\pi_P$ is wildly ramified along $R_P$.

Node: SG00000084 · Lean: none yet

*Proof.* The partial derivatives of $F$ are $(q+1) x_i^q = x_i^q$, and they have no common zero in $\mathbb{P}^5$, so $X$ is smooth. For vectors $x, u$ and a scalar $t$, $$F(x + t u) = \sum_i (x_i^q + t^q u_i^q)(x_i + t u_i) = F(x) + t \sum_i x_i^q u_i + t^q \sum_i u_i^q x_i + t^{q+1} F(u).$$ Since $P \notin X$, the projection $\pi_P$ is finite, and it is flat because $X$ is Cohen-Macaulay and $\mathbb{P}^4$ is regular. So the local degree at $x \in X$ is the intersection multiplicity at $x$ of $X$ with the line through $x$ and $P$. Put $\ell(x) = \sum_i P_i^q x_i$. For $x \in R_P$ the formula with $u = P$ gives $F(x + tP) = t^q (\ell(x) + t F(P))$ with $F(P) \ne 0$. So the local degree at $x$ is $q$ if $\ell(x) \ne 0$ and $q + 1$ if $\ell(x) = 0$.

Since $k$ is perfect, $\sum_i P_i x_i^q = (\sum_i P_i^{1/q} x_i)^q$, so as a set $R_P = X \cap H'$ with $H' = V(\sum_i P_i^{1/q} x_i)$, a 3-fold. The hyperplanes $H'$ and $V(\ell)$ are equal if and only if $(P_i^q)$ is proportional to $(P_i^{1/q})$, that is, $P^{(q^2)} = \lambda P$, that is, $P$ is projectively $\mathbb{F}_{q^2}$-rational. In this case $\ell = 0$ on $R_P$. If the hyperplanes are different, a component of $R_P$ in $V(\ell)$ is the 3-plane $H' \cap V(\ell)$. A smooth hypersurface in $\mathbb{P}^5$ contains no 3-plane: if $V(x_4, x_5) \subseteq X$, then $F = x_4 G_4 + x_5 G_5$, and $X$ is singular on the nonempty set $V(x_4, x_5, G_4, G_5)$. So in this case the local degree is $q$ at the generic point of each component of $R_P$.

For the ramification, two points of $R_P$ on one line through $P$ would give a total length of at least $2q > q + 1$. So $R_P \to \pi_P(R_P)$ is injective on points, and at the generic point $\eta$ of a component the residue field extension is purely inseparable of some degree $f_\eta = p^a$. Over the generic point of the branch divisor, $\mathcal{O}_X$ is finite and free over a discrete valuation ring, so $e_\eta f_\eta$ is the local degree at $\eta$. In case 2, $e_\eta f_\eta = q$, so the residue extension is inseparable or $p$ divides $e_\eta$, and the ramification is wild. In case 1, $e_\eta f_\eta = q + 1$ is prime to $p$, so $f_\eta = 1$ and $e_\eta = q + 1$, and the ramification is tame. $\square$

For $P = (0, \dots, 0, 1)$ the projection is the Kummer cover $x_5^{q+1} = -\sum_{i < 5} x_i^{q+1}$. So the Hermitian 4-fold has tame projections, but each of its linear projections has local degree at least $q \ge p$ along a 3-fold, at points of multiplicity 1. The bound on the multiplicities from Hypothesis 3.21.3 says nothing about the local degrees. The dichotomy matches the outer Galois points of Hermitian curves, studied by Homma and by Fukasawa. The research notes checked the formula for the local degrees by computer over $\mathbb{F}_{3^6}$, $\mathbb{F}_{5^4}$ and $\mathbb{F}_{3^8}$.

### Jung's method for one variety

When a global projection of small local degree does exist, the toroidal argument of Jung works for one variety.

**Theorem 3.21.11.** Let $X$ be a normal projective 4-fold over $k$. Assume:

1. (TP) there is a finite surjective morphism $\pi \colon X \to W$ onto a regular projective 4-fold $W$ such that at each point $x \in X$, the local degree $[L_x^* : K_{\pi(x)}^*]$ is less than $p$, where $L_x^*$ and $K_w^*$ are the fraction fields of $\mathcal{O}_{X,x}^*$ and $\mathcal{O}_{W,w}^*$;
2. the branch divisor $B$ of $\pi$ has an embedded resolution $W' \to W$ by blowups in regular centers whose total transform $E$ has simple normal crossings.

Then $X$ has a resolution $Y \to X$, projective and birational, with $Y$ regular.

Node: SG00000085 · Lean: none yet

*Proof.* Let $K = k(W)$ and $L = k(X)$. Since $X$ is normal and $\pi$ is finite, each local ring of $X$ is a localization of the integral closure of a local ring of $W$ in $L$. So (TP) and Lemma 3.21.6 show that $L/K$ is separable. By purity of the branch locus, the set over which $\pi$ ramifies is a divisor $B$. Let $X'$ be the normalization of $W'$ in $L$. It is a normal projective variety with a finite morphism $\pi' \colon X' \to W'$ and a projective birational morphism $X' \to X$. For $x' \in X'$ over $x \in X$ and $w' = \pi'(x')$ over $w = \pi(x)$, we have $K_w^* \subseteq K_{w'}^*$ and $L_{x'}^* = K_{w'}^*(L_x^*)$, so the local degrees of $\pi'$ are at most those of $\pi$, and they are less than $p$.

Over $W' \setminus E$ the map $\pi'$ is étale, since there it is the base change of the étale part of $\pi$, and an étale cover of a normal scheme is normal. At a point $w' \in E$, with regular parameters $y_1, \dots, y_4$ and $E = V(y_1 \cdots y_s)$ near $w'$, the fundamental inequality and the bound on the local degree show, as in Step 4 of Theorem 3.21.7, that the primes $(y_i)$ with $i \le s$ are tamely ramified in each factor $L_{x'}^*$, and the primes $(y_i)$ with $i > s$ are unramified. By Hypothesis 3.21.4, $\mathcal{O}_{X',x'}^* \cong k[[z_1, \dots, z_4]]^G$ for a group $G \subseteq \mu_N^4$ acting diagonally, with $p \nmid N$. So $X'$ with the log structure of $\pi'^{-1}(E)$ is log regular: log regularity can be tested on the completions [Kat94], and a quotient of a regular formal scheme by a diagonal group of order prime to $p$ is toric. Hypothesis 3.21.5 gives a resolution $Y \to X'$, and $Y \to X' \to X$ is the required resolution. $\square$

Hypothesis (TP) holds for a normal Galois cover of degree less than $p$ of a regular 4-fold, and for $X = V(z^m - h)$ with $m < p$. For $X = V(z^2 - h)$ the theorem reduces resolution of $X$ to embedded resolution of $V(h)$ in a regular 4-fold. Example 3.21.10 shows that (TP) can fail for each linear projection of a smooth 4-fold, while some of these projections are tame. Tameness is what the toroidal step needs, and (TP) is used only to keep tameness after the base change to $W'$. Whether (TP) can be replaced by tameness of $\pi$ along $B$ is open.

### Hypersurfaces of bounded degree

There is one unconditional statement in the direction of Target T. It is folklore, and the project found no written reference.

**Theorem 3.21.12.** For all $n, d \ge 1$ there is a number $N(n, d)$ such that, if $k$ is algebraically closed of characteristic $p > N(n, d)$, each integral hypersurface $X \subset \mathbb{P}^{n+1}_k$ of degree at most $d$ has a projective birational morphism $Y \to X$ with $Y$ regular.

Node: SG00000086 · Lean: none yet

*Proof.* Fix a degree $e \le d$. Let $H = \mathbb{P}^M_{\mathbb{Z}}$ be the space of nonzero forms of degree $e$ in $n + 2$ variables, and $\mathcal{X} \subset \mathbb{P}^{n+1}_H$ the universal hypersurface. The set $H^{\rm int}$ of points of $H$ with a geometrically integral fiber is constructible [EGA4, 9.7.7].

First, a spreading lemma. Let $Z$ be an integral subscheme of $H$ whose generic point $\zeta$ has characteristic 0 and lies in $H^{\rm int}$. By the theorem of Hironaka [Hir64], in the form of [Tem08], the fiber $\mathcal{X}_\zeta$ has a projective birational morphism $Y_\zeta \to \mathcal{X}_\zeta$ with $Y_\zeta$ regular, so smooth over the field $\kappa(\zeta)$ of characteristic 0, and an isomorphism over a dense open set. This morphism, the smoothness, and the open set spread out over a dense open set $U \subseteq Z$ [EGA4, 8.8.2, 8.10.5 and 17.7.8]. After shrinking $U$, all fibers of $\mathcal{X}_U$ and $\mathcal{Y}_U$ are geometrically integral [EGA4, 9.7.7], and the complement of the open set has fibers of dimension less than $n$ [EGA4, 9.5.5]. Then for each $s \in U$ and each algebraically closed field $\Omega \supseteq \kappa(s)$, the morphism $\mathcal{Y}_\Omega \to \mathcal{X}_\Omega$ is projective and birational with a regular source.

Second, noetherian induction on the closed subsets of $H$ shows that finitely many such sets $U_1, \dots, U_r$ cover $H^{\rm int} \cap H_{\mathbb{Q}}$. At a component of a closed set $Z$ whose generic point is in $H_{\mathbb{Q}}$ but not in $H^{\rm int}$, replace the component by the closure of its intersection with $H^{\rm int}$, which is smaller. At a component whose generic point is in $H_{\mathbb{Q}} \cap H^{\rm int}$, take $U$ from the lemma, open in $Z$, and continue with $Z \setminus U$. A component whose generic point has positive characteristic contains no point of $H_{\mathbb{Q}}$.

Then $C = H^{\rm int} \setminus (U_1 \cup \dots \cup U_r)$ is constructible and has no point of characteristic 0. By the theorem of Chevalley [EGA4, 1.8.4] its image in $\operatorname{Spec} \mathbb{Z}$ is a finite set of primes. Let $N_e$ be the largest of them, and $N(n, d) = \max_{e \le d} N_e$. An integral hypersurface of degree $e$ over $k$ with $p > N(n, d)$ gives a point $s \in H^{\rm int} \setminus C$, so $s \in U_i$ for some $i$, and the lemma gives its resolution. $\square$

The bound $N(n, d)$ is not effective, and the resolution need not be an isomorphism over the regular locus. The same proof works for each bounded family, since the Hilbert scheme is of finite type over $\mathbb{Z}$. The bound depends on the degree, so the theorem does not give Target T.

### Maximal contact in low degree

The algorithm in characteristic 0, in the form of [Kol07, Chapter 3], descends in dimension by a hypersurface of maximal contact. It takes an element of order 1 in $\Delta^{e-1}(I)$, where $I$ has order $e$, and passes to the coefficient ideal on it. In characteristic $p$ one can take Hasse derivatives: $\Delta^j(I)$ is generated by the $D^{(\alpha)} F$ with $F \in I$ and $|\alpha| \le j$, where $D^{(\alpha)} x^\beta = \binom{\beta}{\alpha} x^{\beta - \alpha}$. The research notes asked how early this definition fails for germs of degree less than $p$.

**Lemma 3.21.13.** Let $I \subseteq k[[x_1, \dots, x_n]]$ have order $e \ge 1$, and let $\mathrm{in}_e(I)$ be the span of the parts of degree $e$ of the elements of $I$. Then $\Delta^{e-1}(I)$ contains an element of order 1 if and only if $\mathrm{in}_e(I) \not\subseteq k[x_1^p, \dots, x_n^p]$. In particular this holds if $p \nmid e$.

Node: SG00000087 · Lean: none yet

*Proof.* For $|\alpha| < e - 1$ the series $D^{(\alpha)} F$ has order at least 2. So the linear parts of the elements of $\Delta^{e-1}(I)$ are the combinations of the linear parts of $D^{(\alpha)} F$ with $|\alpha| = e - 1$. If $F_e = \sum_\beta c_\beta x^\beta$ is the part of degree $e$ of $F$, this linear part is $\sum_j (\alpha_j + 1) c_{\alpha + e_j} x_j$. All of them vanish if and only if $c_\beta \ne 0$ implies that each nonzero $\beta_j$ is divisible by $p$, that is, $F_e \in k[x^p]$. If $p \nmid e$, each monomial of degree $e$ has an exponent prime to $p$. $\square$

The criterion depends only on $\mathrm{in}_e(I)$, so it does not change under completion or an extension of $k$. Thus at the first level a germ of order less than $p$ always has an element of order 1. The next example fails at the second level, before any blowup. It looks like a germ of low degree, but it is $z^2 - x^p$ in disguise.

**Example 3.21.14.** Let $p \ge 5$, $1 \le r \le (p - 1)/2$, and $f = z^2 + 2 z (x^r + x^{p-r}) + x^{2r} \in k[[x, y, w, v, z]]$.

1. $f$ has order 2 and degree $\max(2r, p - r + 1)$, and $f$ is a unit times $z''^2 - x^p$ for a regular parameter $z''$.
2. For each hypersurface $H$ whose equation is an element of order 1 of $\Delta^1(f)$, the coefficient ideal of Kollár on $H$ is $C = (x^p)$. So $\Delta^{p-1}(C) = C$ has no element of order 1, also formally and after an extension of $k$.
3. The hypersurface $V(x) \subset H$ has maximal contact with $(C, p)$ in the sense of Hironaka, and the marked ideal $(C, p)$ is equivalent to $(x, 1)$.

Node: SG00000088 · Lean: none yet

*Proof.* Put $B = x^r + x^{p-r}$ and $z' = z + B$. Then $f = z'^2 - G$ with $G = B^2 - x^{2r} = 2 x^p + x^{2p-2r} = u x^p$, where $u = 2 + x^{p-2r}$. Since $p$ is odd and $u(0) = 2 \ne 0$, $u = v^2$ for a unit $v$, and $f = v^2 ((z'/v)^2 - x^p)$. This is part 1 with $z'' = z'/v$.

For part 2, $\Delta^1(f)$ is generated by $f$ and its first derivatives, so $\Delta^1(f) = (z', G, \partial G / \partial x) = (z', x^p)$, because $\partial(2x^p)/\partial x = 0$ and $2p - 2r - 1 \ge p$. So $H = V(z' - \psi)$ with $\psi \in (x^p)$. On $H$, $f|_H = \psi^2 - u x^p$ is $x^p$ times a unit, and $(\Delta^1(f)|_H)^2 = (x^{2p})$. So $C = (f|_H) + (\Delta^1(f)|_H)^2 = (x^p)$. For $|\alpha| < p$ the Leibniz rule gives $D^{(\alpha)}(x^p g) = x^p D^{(\alpha)} g$, so $\Delta^{p-1}(C) = C$, and Lemma 3.21.13 gives the rest.

For part 3, the points of $H$ where $C$ has order at least $p$ are the points of $V(x)$. After a blowup with center in $V(x)$, in a chart $x = x' t$ with $t$ the exceptional equation, the controlled transform is $(x'^p)$, and its locus of order $p$ is the strict transform of $V(x)$. In the chart where $x$ is the exceptional equation, the transform is a unit. So $V(x)$ keeps maximal contact. The controlled transform of $(x^p)$ is the $p$-th power of the controlled transform of $(x)$, and smooth pullback commutes with $p$-th powers, so $(x^p, p)$ and $(x, 1)$ are equivalent. $\square$

So the algorithm, run on $(x, 1)$, blows up the curve $V(x, z' - \psi)$, which is the right first center for $z''^2 - x^p$. The failure is a failure of the definition of maximal contact by an element of order 1 of $\Delta^{e-1}$, not of maximal contact in the sense of Hironaka. The leading generator systems of Kawanoue and Matsuki [KM10] and the elimination algebras of Benito and Villamayor [BenV13] treat such germs. It is not a genuine failure as in the example of Narasimhan in characteristic 2 [Nar83]. The degree of $f$ also depends on the coordinates: after $z' = z + B$ it is $2p - 2r > p$. So the example answers the question of the research notes only in its literal form.

### What is open

1. $\mathrm{Emb}(\mathbb{P}^4)$, for each $p$. Theorem 3.21.7 needs it only in the local form of Lemma 3.21.2.
2. Conjecture 3.21.8, patching of local uniformizations without a finite set in dimension 4. No proof by patching is known, also in characteristic 0. With it and $\mathrm{Emb}(\mathbb{P}^4)$, Corollary 3.21.9 gives Target T.
3. Whether (TP) in Theorem 3.21.11 can be replaced by tameness of $\pi$ along the branch divisor.
4. An effective bound $N(4, d)$ in Theorem 3.21.12 for small $d$.
5. A first genuine failure of maximal contact, in the sense of Narasimhan, for germs of order less than $p$ after blowups. Example 3.21.14 is not one.

### Status

The results are the nodes SG0000007W to SG00000088 of the map. Theorem 3.21.7 is [Cut09, Theorem 14.4] in dimension 4, and Corollary 3.21.9 depends on two open hypotheses. Lemma 3.21.6 and Lemma 3.21.13 are standard lemmas, and Theorem 3.21.12 is folklore. Example 3.21.10 with its dichotomy and the corrected Example 3.21.14 were checked in the research notes, with computer tests. The cited theorems of Albanese, Abhyankar and Kato are hypotheses on the map, and none of the nodes has a Lean proof yet. An outside expert has not yet read the result.

### Notes and references

The results are in research note 56, with the corrections of note 62, which is a referee report on note 56. Note 62 found the dichotomy of Example 3.21.10, the stronger form of the patching hypothesis in Corollary 3.21.9, and the error in the first form of Example 3.21.14. The corrections are also recorded in the research notes 02, 09, 10 and 12, where the earlier claim on Theorem 2.12 appeared. The method of Jung, in the form used here, is in [Abh66] and [Cut09, Sections 4 and 14]. The patching in dimension 3 is [Zar44] and [Cut09, Sections 15 and 16]. The toroidal resolution is [KKMS], and its log form is [Kat94] and [Niz06].
