---
title: The global step and Zariski's fundamental theorem in dimension four
nodes: [SG000000BQ, SG000000BR, SG000000BS, SG000000BT, SG000000BV, SG000000BW, SG000000BX, SG000000BY, SG000000BZ, SG000000C0, SG000000C1, SG000000C2, SG000000C3, SG000000C4, SG000000C5, SG000000C6, SG000000C7, SG000000C8, SG000000C9]
sources: [Zar44, Abh56, Cut09, CP19, Tem13, Kar03, Ful93, ZS2, Har, Hir64, Pil]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The global step and Zariski's fundamental theorem in dimension four

This section reports the twenty-fourth research result, from the track FP (tamnd/singularity#320), the patching of models. It asks what is missing between local uniformization of 4-folds and resolution of 4-folds. The answer has three parts. First, resolution of 4-folds by projective morphisms is equivalent to two statements: a purely inseparable step of local uniformization, $\mathrm{PILU}_4$, and Zariski's fundamental theorem in dimension 4, $\mathrm{Fund}_4$. This uses the theorem of Temkin on inseparable local uniformization. Second, the proof of Cutkosky for 3-folds reduces $\mathrm{Fund}_4$ to principalization of ideals on regular 4-folds and to a factorization statement for 3-dimensional regular local rings. Third, this factorization statement is false, also in its weakest form, and a toric pair of 4-folds shows exactly where the proof breaks. The global step $\mathrm{Fund}_4$ stays open.

We work over an algebraically closed field $k$ of characteristic $p > 0$. A variety is an integral separated scheme of finite type over $k$. A function field is a finitely generated field extension $K/k$, and its dimension is its transcendence degree. A model of $K$ is a variety with function field $K$. A valuation of $K/k$ is a valuation ring $\mathcal{O}_v$ of $K$ that contains $k$. Its center on a model $X$ is the point $x$ with $\mathcal{O}_{X,x} \subseteq \mathcal{O}_v$ and $\mathfrak{m}_v \cap \mathcal{O}_{X,x} = \mathfrak{m}_x$ (Volume 3, Definition 1.4.1). It is unique because $X$ is separated, and it exists if $X$ is proper. The Zariski-Riemann space $\mathrm{ZR}(K)$ is the set of valuations of $K/k$, and it is quasi-compact (Volume 3, Theorem 1.5.3). For a model $X$ the center map $\mathrm{ZR}(K) \to X$ is continuous, so for an open set $U \subseteq X$ the valuations with center in $U$ form an open set.

### Motivation and history

Zariski proved resolution of 3-folds in characteristic 0 in two steps [Zar44]. The first step is local: each valuation has local uniformization, that is, a model on which its center is regular. The second step is global. Quasi-compactness of $\mathrm{ZR}(K)$ gives finitely many models such that each valuation has a regular center on one of them (Volume 3, Proposition 4.1.2). Then two models are patched at a time. The tool for this is Zariski's fundamental theorem: given two models, there is a third model that dominates both and keeps the regular centers of both. Zariski proved it for 3-folds with a factorization theorem for 2-dimensional regular local rings. In dimension 2 a regular local ring that birationally dominates another one is reached from it by a finite sequence of blowups of closed points. Abhyankar proved this in general [Abh56] (Volume 5, Theorem 1.2.6).

Abhyankar used the same plan for 3-folds in characteristic $p > 5$. Cutkosky gave a shorter proof [Cut09]. His Theorem 15.1 is the fundamental theorem for 3-folds in each characteristic, and his Theorems 16.1 and 16.2 deduce resolution from it. Cossart and Piltant proved resolution of all quasi-excellent schemes of dimension 3 [CP19]. Their Section 4.1 also patches local solutions, with principalization of ideals in dimension 3 (their Proposition 4.4) and Abhyankar's theorem (their Proposition 4.2). Volume 6, Section 1.2 explains the plan of these proofs.

In dimension 4 the local step is open. Temkin proved a weaker form for each dimension: local uniformization holds after a finite purely inseparable extension of the function field [Tem13, Theorem 1.3.2] (Volume 5, Theorem 4.1.1). Temkin also writes that it is not known whether global resolution reduces to local uniformization above dimension 3 [Tem13, Section 1.2(ii)]. In characteristic 0 the fundamental theorem holds in each dimension, because Hironaka's theorem [Hir64] resolves the graph of two models. But no proof by patching is known in dimension 4, also in characteristic 0. This section explains why the method of Zariski and Cutkosky stops in dimension 4.

### The named statements

**Definition 3.24.1 (local uniformization in dimension 4).** $\mathrm{LU}_4^-$ is the statement: for each function field $K$ of dimension 4 and each valuation $v$ of $K/k$, there is a regular local ring $A \subset K$, essentially of finite type over $k$, with fraction field $K$, dominated by $\mathcal{O}_v$. $\mathrm{LU}_4$ is the stronger statement in which, in addition, $A$ contains a given finite subset $S \subset \mathcal{O}_v$.

Node: SG000000BS · Lean: none yet

$\mathrm{LU}_4$ is the affine form of local uniformization of Volume 3, Proposition 4.1.6, and $\mathrm{LU}_4^-$ is the premise of Conjecture 3.21.8. Clearly $\mathrm{LU}_4$ implies $\mathrm{LU}_4^-$.

**Conjecture 3.24.2 ($\mathrm{PILU}_4$).** Let $A$ be a regular local ring, essentially of finite type over $k$, whose fraction field $L$ has dimension 4. Let $a \in A$ with $b = a^{1/p} \notin L$, and let $v$ be a valuation of $L(b)/k$ that dominates $A$. Then there is a regular local ring $A' \subset L(b)$, essentially of finite type over $k$, with fraction field $L(b)$, dominated by $\mathcal{O}_v$, such that $A[b] \subseteq A'$.

Node: SG000000BR · Lean: none yet

This is the degree $p$ step of local uniformization: it uniformizes one purely inseparable cover of degree $p$ along a valuation. Temkin reduces local uniformization to equations $t^p = f$ [Tem13, Remark 1.3.5], and $\mathrm{PILU}_4$ is this reduction in dimension 4.

**Conjecture 3.24.3 ($\mathrm{Fund}_4$, Zariski's fundamental theorem in dimension 4).** Let $K$ be a function field of dimension 4, let $V_0$ and $V_1$ be normal projective models of $K$, and let $N$ be the set of valuations of $K/k$ whose center on $V_0$ or on $V_1$ is a regular point. Then there is a normal projective model $W$ of $K$, with birational morphisms $W \to V_0$ and $W \to V_1$, such that each $v \in N$ has a regular center on $W$.

Node: SG000000BQ · Lean: none yet

In dimension 3 this is [Cut09, Theorem 15.1], where $N$ is restricted to valuations with residue field $k$, and the patching step of [CP19, Section 4.1, Step 3]. The restriction on the residue field does not matter for the applications below. If $\mathcal{O}_v$ is a localization of a valuation ring $\mathcal{O}_{v^*}$ of dimension 0, then the center of $v$ on a model is a generization of the center of $v^*$, and a localization of a regular local ring is regular. Cutkosky uses this argument in his proof of Theorem 16.1.

### Resolution is local uniformization plus the fundamental theorem

Let $\mathrm{Res}_4^{\rm pr}$ be the statement: each variety $X$ of dimension 4 has a projective birational morphism $X' \to X$ with $X'$ regular. Let $\mathrm{Reg}_4$ be the statement: each function field of dimension 4 has a regular projective model.

**Theorem 3.24.4.** $\mathrm{LU}_4^-$ and $\mathrm{Fund}_4$ imply $\mathrm{Res}_4^{\rm pr}$. Conversely, $\mathrm{Res}_4^{\rm pr}$ implies $\mathrm{LU}_4$ and $\mathrm{Fund}_4$.

Node: SG000000BS · Lean: none yet

*Proof.* Assume $\mathrm{LU}_4^-$ and $\mathrm{Fund}_4$, and let $K$ be a function field of dimension 4.

Step 1 (a model for each valuation). Let $v \in \mathrm{ZR}(K)$. By $\mathrm{LU}_4^-$ there is a regular local ring $A \subset K$, essentially of finite type over $k$, with fraction field $K$, dominated by $\mathcal{O}_v$. Write $A = B_{\mathfrak{q}}$, where $B$ is a finitely generated $k$-algebra with fraction field $K$. Embed $\operatorname{Spec} B$ in an affine space, let $\bar X$ be its closure in the projective space, and let $W_v$ be the normalization of $\bar X$. Then $W_v$ is a normal projective model of $K$. Since $B \subseteq A \subseteq \mathcal{O}_v$ and $\mathfrak{m}_v \cap B = \mathfrak{q}$, the center of $v$ on $\bar X$ is $\mathfrak{q}$, with local ring $A$. The ring $A$ is regular, so it is normal, and the normalization is an isomorphism over a neighborhood of $\mathfrak{q}$. So the center of $v$ on $W_v$ is a regular point.

Step 2 (finitely many models). For each $v$ let $O_v \subseteq \mathrm{ZR}(K)$ be the set of valuations whose center on $W_v$ is in $\mathrm{Reg}\, W_v$. The variety $W_v$ is excellent, so $\mathrm{Reg}\, W_v$ is open, and $O_v$ is open. Also $v \in O_v$. Since $\mathrm{ZR}(K)$ is quasi-compact, finitely many sets $O_{v_1}, \dots, O_{v_n}$ cover it. Put $W_i = W_{v_i}$. Then each valuation has a regular center on some $W_i$.

Step 3 ($\mathrm{Reg}_4$). Apply $\mathrm{Fund}_4$ to $(W_1, W_2)$. It gives a normal projective model $W_{12}$ on which each valuation with a regular center on $W_1$ or on $W_2$ has a regular center. Apply $\mathrm{Fund}_4$ to $(W_{12}, W_3)$, and continue. After $n - 1$ steps there is a normal projective model $W$ on which each valuation of $K/k$ has a regular center. Each point $w \in W$ is the center of a valuation, because a local domain is dominated by a valuation ring of its fraction field [ZS2, Chapter VI, Section 4, Theorem 5]. So $W$ is regular. This proves $\mathrm{Reg}_4$.

Step 4 (resolution of a given variety). Let $X$ be a variety of dimension 4 with function field $K$. By Chow's lemma there is a projective birational morphism $X' \to X$ with $X'$ quasi-projective. Let $\bar X'$ be a projective closure of $X'$ and $V_0$ the normalization of $\bar X'$, so $V_0 \to \bar X'$ is finite. Let $V_1$ be a regular projective model of $K$, from Step 3. Apply $\mathrm{Fund}_4$ to $(V_0, V_1)$. Since $V_1$ is regular, $N = \mathrm{ZR}(K)$, so there is a normal projective $W$ that dominates $V_0$ and on which each valuation has a regular center. As in Step 3, $W$ is regular. The morphism $W \to V_0 \to \bar X'$ is projective, because it is a morphism of projective varieties. Over $X'$ it gives a projective birational morphism $W' \to X'$ with $W'$ regular, and $W' \to X' \to X$ is projective and birational.

Conversely, assume $\mathrm{Res}_4^{\rm pr}$. For $\mathrm{Fund}_4$, let $\Gamma$ be the normalization of the closure of the graph of $V_0 \dashrightarrow V_1$ in $V_0 \times V_1$. It is normal and projective. A projective resolution $W \to \Gamma$ gives a regular projective $W$ that dominates $V_0$ and $V_1$, and each center on $W$ is regular. For $\mathrm{LU}_4$, let $v$ be a valuation and $S \subset \mathcal{O}_v$ finite. Choose generators of $K$ over $k$ and replace a generator $a$ by $a^{-1}$ if $v(a) < 0$. This gives a finite set $S_0 \subset \mathcal{O}_v$ that generates $K$. Put $B = k[S \cup S_0]$. Then $B \subseteq \mathcal{O}_v$, so $v$ has a center $x$ on $\operatorname{Spec} B$ and on each projective closure $\bar X$ of $\operatorname{Spec} B$. Let $W \to \bar X$ be a projective resolution and $w$ the center of $v$ on $W$. Then $w$ maps to $x$, so $\mathcal{O}_{W,w} \supseteq \mathcal{O}_{\bar X,x} \supseteq B \supseteq S$, and $\mathcal{O}_{W,w}$ is regular, essentially of finite type, with fraction field $K$, and dominated by $\mathcal{O}_v$. $\square$

Steps 1 to 3 are Cutkosky's proof of [Cut09, Theorem 16.1], and Step 4 is his Theorem 16.2 with $\mathrm{Fund}_4$ in place of principalization of the graph. In Step 4 principalization is not necessary, because $\mathrm{Fund}_4$ with $V_1$ regular already eliminates the indeterminacy.

**Theorem 3.24.5.** $\mathrm{Res}_4^{\rm pr}$ holds if and only if $\mathrm{PILU}_4$ and $\mathrm{Fund}_4$ hold.

Node: SG000000BT · Lean: none yet

*Proof.* Suppose that $\mathrm{PILU}_4$ and $\mathrm{Fund}_4$ hold. By the theorem of Temkin [Tem13, Theorem 1.3.2] local uniformization with a finite set holds after a finite purely inseparable extension $K'/K$. This extension is a tower of extensions of degree $p$, each obtained by adjoining a $p$-th root. Research note 02, Theorem 2.6, descends one degree $p$ step at a time with $\mathrm{PILU}_4$, and controls the finite set through its $p^m$-th powers and normality. This gives $\mathrm{LU}_4$, hence $\mathrm{LU}_4^-$, and Theorem 3.24.4 gives $\mathrm{Res}_4^{\rm pr}$.

Conversely, suppose that $\mathrm{Res}_4^{\rm pr}$ holds. Theorem 3.24.4 gives $\mathrm{Fund}_4$ and $\mathrm{LU}_4$. Let $A$, $b$ and $v$ be as in Conjecture 3.24.2. Write $A = (B_0)_{\mathfrak{q}_0}$ with $B_0$ a finitely generated $k$-algebra, and apply $\mathrm{LU}_4$ to $L(b)$, $v$ and the finite set $S$ that consists of $b$ and of generators of $B_0$. The resulting regular local ring $A'$ contains $B_0$ and $b$. An element of $B_0 \setminus \mathfrak{q}_0$ is a unit of $A$, so it is a unit of $\mathcal{O}_v$, because $v$ dominates $A$. So it is not in $\mathfrak{m}_v \cap A' = \mathfrak{m}_{A'}$, and it is a unit of $A'$. Hence $A \subseteq A'$, and $A[b] \subseteq A'$. $\square$

Theorems 3.24.4 and 3.24.5 are equivalences, so they hide nothing that is harder than resolution. For the same reason they are a reformulation and not a reduction. Their content is that the step from local uniformization to resolution of 4-folds is exactly $\mathrm{Fund}_4$. This agrees with the remark of Temkin, since $\mathrm{Fund}_4$ is open.

**Corollary 3.24.6.** $\mathrm{Fund}_4$ implies Conjecture 3.21.8.

Node: SG000000BS · Lean: none yet

*Proof.* The premise of Conjecture 3.21.8 is $\mathrm{LU}_4^-$, and Theorem 3.24.4 applies. $\square$

### Two lemmas on ideals

The proof of Cutkosky uses principalization of ideals. In dimension 4 this is an open statement.

**Conjecture 3.24.7 ($\mathrm{Princ}_4$).** Let $U$ be a regular quasi-projective variety of dimension 4 and $I \subseteq \mathcal{O}_U$ a nonzero coherent ideal. Then there is a sequence $U_r \to \dots \to U_0 = U$ of blowups along regular centers $C_i$, with $C_i$ contained in the locus where $I \mathcal{O}_{U_i}$ is not invertible, such that $I \mathcal{O}_{U_r}$ is invertible.

Node: SG000000BV · Lean: none yet

In dimension 3 this is [Cut09, Theorem 1.3] and [CP19, Proposition 4.4]. Cutkosky derives it from order reduction for weak transforms of ideals [Cut09, Theorem 5.6]. In dimension 4 that method contains the problem of multiplicity drop for hypersurfaces of 4-folds. Note that $\mathrm{Princ}_4$ is not known to follow from $\mathrm{Res}_4^{\rm pr}$: it is a statement of embedded type. So a route to $\mathrm{Fund}_4$ through $\mathrm{Princ}_4$ can use a hypothesis that is stronger than the goal.

**Lemma 3.24.8.** Let $X$ be a regular quasi-projective variety, let $G \subset X$ be closed of codimension at least 2, and let $f \colon X' \to X$ be a projective birational morphism that is an isomorphism over $X \setminus G$. Then $X' \cong \mathrm{Bl}_J X$ over $X$ for a coherent ideal $J$ with $V(J) \subseteq G$.

Node: SG000000BW · Lean: none yet

*Proof.* By [Har, Theorem II.7.17] there is a coherent ideal $J_0$ with $X' \cong \mathrm{Bl}_{J_0} X$. Over $U = X \setminus G$ the blowup is an isomorphism, so $J_0|_U$ is invertible, because its pullback to the blowup is invertible. So $J_0|_U = \mathcal{O}_U(-D)$ for an effective Cartier divisor $D$ on $U$. Let $\bar D$ be its closure in $X$. It is a Weil divisor, and it is Cartier because $X$ is regular. Put $J = J_0 \cdot \mathcal{O}_X(\bar D)$, a coherent fractional ideal with $J|_U = \mathcal{O}_U$. A local section of $J$ over an open set $V$ is a rational function that is regular on $V \setminus G$. Since $X$ is normal and $G$ has codimension at least 2, it is regular on $V$. So $J \subseteq \mathcal{O}_X$ and $V(J) \subseteq G$. A twist by an invertible sheaf does not change the blowup [Har, Lemma II.7.9 and its proof], so $\mathrm{Bl}_J X \cong \mathrm{Bl}_{J_0} X$. $\square$

**Lemma 3.24.9.** Let $V$ be a Noetherian scheme, $j \colon \tilde U \to V$ an open immersion, $G$ a closed subset of $\tilde U$, $\bar G$ its closure in $V$ with ideal $I_{\bar G}$, and $H \subseteq \mathcal{O}_{\tilde U}$ a coherent ideal with $V(H) \subseteq G$. For $n$ large, the ideal $H' = (\mathcal{O}_V \cap j_* H) + I_{\bar G}^n$ is coherent, $H'|_{\tilde U} = H$, and $H' = \mathcal{O}_V$ on $V \setminus \bar G$.

Node: SG000000BX · Lean: none yet

*Proof.* The sheaf $\mathcal{O}_V \cap j_* H$ is a quasi-coherent subsheaf of $\mathcal{O}_V$, so it is coherent, and its restriction to $\tilde U$ is $H$. Since $V(H) \subseteq G$, the radical of $H$ contains the ideal $I_G$ of $G$ in $\tilde U$, and $I_G^n \subseteq H$ for $n$ large, because $\tilde U$ is Noetherian. So $H'|_{\tilde U} = H + I_G^n = H$. Off $\bar G$ we have $I_{\bar G} = \mathcal{O}_V$. $\square$

**Definition 3.24.10 (fundamental locus).** Let $\phi \colon V \dashrightarrow V'$ be a rational map from a normal variety to a projective variety. The *fundamental locus* of $\phi$ is the complement of the largest open set on which $\phi$ is a morphism.

Node: SG000000C1 · Lean: none yet

The fundamental locus is closed, and it has codimension at least 2. A normal variety is regular in codimension 1, its local rings at points of codimension 1 are discrete valuation rings, and the valuative criterion of properness extends $\phi$ over these points.

### Faithfulness in codimension two

**Lemma 3.24.11.** Let $U$ be a regular variety of dimension 4, $K \subseteq \mathcal{O}_U$ a nonzero ideal, $\alpha \colon Z \to U$ the normalized blowup of $K$, and $\sigma \colon W \to U$ a principalization of $K$ by blowups along regular centers in the locus where $K$ is not invertible. Since $K \mathcal{O}_W$ is invertible and $W$ is normal, $\sigma$ factors through a morphism $\tau \colon W \to Z$. Let $\zeta \in Z$ such that $S = \mathcal{O}_{Z,\zeta}$ is regular of dimension 2 and $R = \mathcal{O}_{U,\alpha(\zeta)}$ has dimension 2. Then $\tau$ is a local isomorphism over $\zeta$.

Node: SG000000BY · Lean: none yet

*Proof.* Make the base change to $\operatorname{Spec} R$. It is flat, so it commutes with blowups. Each center $C_i$ becomes a regular closed subscheme of a regular scheme of dimension 2. It is empty, or a Cartier divisor, whose blowup is an isomorphism, or a finite set of closed points. So over $\operatorname{Spec} R$ the morphism $\sigma$ is a sequence of blowups of closed points of regular 2-dimensional schemes, each in the locus where $K$ is not invertible.

The ring $S$ dominates $R$, because $\zeta$ lies over the closed point of $\operatorname{Spec} R$. Both rings are regular of dimension 2 with the same fraction field. By the theorem of Abhyankar [Abh56, Theorem 3], in the form of [CP19, Proposition 4.2], there is a sequence $R = S_0 \subset S_1 \subset \dots \subset S_m = S$ in which $S_{j+1}$ is the local ring of the blowup of $\operatorname{Spec} S_j$ at its closed point that $S$ dominates.

The ideal $K S_j$ is not invertible for $j < m$. Suppose that $K S_j$ is invertible. Then $\operatorname{Spec} S_j \to \operatorname{Spec} R$ lifts to the blowup of $K$, and to its normalization $Z$, because $S_j$ is normal. The closed point goes to a point $z$ such that $S_j$ dominates $\mathcal{O}_{Z,z}$. Choose a valuation $\nu$ of the fraction field that dominates $S$ [ZS2, Chapter VI, Section 4, Theorem 5]. Then $\nu$ dominates $\mathcal{O}_{Z,z}$ and $\mathcal{O}_{Z,\zeta}$. Since $Z$ is separated, $z = \zeta$, and $S_j \supseteq S \supseteq S_j$, so $S_j = S$. But for $j < m$ the ideal $\mathfrak{m}_{S_j} S_{j+1}$ is principal and $\mathfrak{m}_{S_j}$ is not, so $S_j \ne S_{j+1} \subseteq S$. This is a contradiction.

Now follow the center of $\nu$ through $\sigma$ over $\operatorname{Spec} R$. Suppose that the local ring at the center is $S_j$ with $j < m$. Then $K$ is not invertible there. The center cannot stay to the end, because $K$ is invertible on $W$, and a blowup at another point does not change the local ring at the center. So at some step the center is blown up, and the new local ring is the quadratic transform of $S_j$ that $\nu$ dominates, which is $S_{j+1}$. When the local ring is $S_m = S$, the ideal $K$ is invertible there, and the center is never blown up again. So $W$ has a point $w$ with $\mathcal{O}_{W,w} = S$, and $\tau(w) = \zeta$.

The morphism $\tau$ induces an isomorphism $\mathcal{O}_{Z,\zeta} \to \mathcal{O}_{W,w}$ of local rings of varieties, so it is an isomorphism from a neighborhood of $w$ onto a neighborhood of $\zeta$. So $w$ is isolated in $\tau^{-1}(\zeta)$. The morphism $\tau$ is proper and birational and $Z$ is normal, so the fibre is connected by Zariski's Main Theorem, and $\tau^{-1}(\zeta) = \{w\}$. Then $\tau$ is quasi-finite, hence finite, over a neighborhood of $\zeta$. A finite birational morphism onto a normal scheme is an isomorphism. $\square$

### The route of Cutkosky

The next definition isolates the one place where the proof of Cutkosky needs more than principalization in dimension 4.

**Definition 3.24.12 ($\mathrm{Fac}_3$ and $\mathrm{Fac}_3^L$).** Let $U$, $K$, $\alpha \colon Z \to U$ and $\tau$ be as in Lemma 3.24.11, with $U$ quasi-projective. $\mathrm{Fac}_3$ is the statement: for each such $(U, K)$ there is a principalization $\sigma \colon W \to U$ of $K$ such that $\tau$ is a local isomorphism over each $\zeta \in \mathrm{Reg}\, Z$ with $\dim \overline{\alpha(\zeta)} = 1$ and $\dim \mathcal{O}_{Z,\zeta} \ge 2$. For a triple $(V_0, V_1, N)$ as in Conjecture 3.24.3, let $K$, $Z$, $U_1$ and $L$ be as in Steps 2 to 4 of the proof of Theorem 3.24.13 below. $\mathrm{Fac}_3^L$ for $(V_0, V_1, N)$ is the statement: there is a principalization $W_1 \to U_1$ of $K|_{U_1}$ such that $\tau$ is a local isomorphism over each $\zeta$ as above with, in addition, $\overline{\{\zeta\}} \cap L \ne \emptyset$.

Node: SG000000BZ · Lean: none yet

Clearly $\mathrm{Fac}_3$ implies $\mathrm{Princ}_4$, and $\mathrm{Fac}_3$ implies $\mathrm{Fac}_3^L$ for each triple. Lemma 3.24.11 is the part of $\mathrm{Fac}_3$ at the points $\zeta$ with $\dim \mathcal{O}_{U,\alpha(\zeta)} = 2$, and it holds for each principalization.

**Theorem 3.24.13.** Assume $\mathrm{Princ}_4$. Let $(V_0, V_1, N)$ be as in Conjecture 3.24.3, and assume $\mathrm{Fac}_3^L$ for $(V_0, V_1, N)$. Then the conclusion of $\mathrm{Fund}_4$ holds for $(V_0, V_1, N)$. In particular, $\mathrm{Fac}_3$ implies $\mathrm{Fund}_4$.

Node: SG000000C1 · Lean: none yet

*Proof.* This is the proof of [Cut09, Theorem 15.1], written for dimension 4. Put $U_i = \mathrm{Reg}\, V_i$.

Step 1. Let $\Gamma \subseteq V_0 \times V_1$ be the closure of the graph of $V_0 \dashrightarrow V_1$. The projection $\Gamma \to V_0$ is projective and birational, so $\Gamma \cong \mathrm{Bl}_I V_0$ for a coherent ideal $I$ [Har, Theorem II.7.17].

Step 2. By $\mathrm{Princ}_4$ there is a principalization $W_0 \to U_0$ of $I|_{U_0}$. It is projective and birational, so $W_0 = \mathrm{Bl}_J U_0$ for a coherent ideal $J$. Extend $J$ to $V_0$ by Lemma 3.24.9, with $G = V(J)$, and blow it up. This gives $X_1 \to V_0$ with $X_1|_{U_0} \cong W_0$. Let $V_2$ be the normalization of the blowup of $I \mathcal{O}_{X_1}$. Over $U_0$ the ideal $I \mathcal{O}_{W_0}$ is invertible and $W_0$ is regular, so the preimage of $U_0$ in $V_2$ is $W_0$, and it is regular. The ideal $I \mathcal{O}_{V_2}$ is invertible, so by the universal property of the blowup $V_2 \to V_0$ factors through $\Gamma$. Let $\alpha \colon V_2 \to \Gamma \to V_1$ be the composite, and put $U_2 = \mathrm{Reg}\, V_2$.

Step 3. The morphism $\alpha$ is projective and birational, and $V_2$ is normal, so $V_2 = \mathrm{Bl}_K V_1$ for a coherent ideal $K$, and $Z = \alpha^{-1}(U_1)$ is the normalized blowup of $K|_{U_1}$. By $\mathrm{Fac}_3^L$ there is a principalization $W_1 \to U_1$ of $K|_{U_1}$ with the property of Definition 3.24.12. Write $W_1 = \mathrm{Bl}_H U_1$, extend $H$ to an ideal $H'$ on $V_1$ with $H'|_{U_1} = H$ by Lemma 3.24.9 (only the first summand is necessary), and let $\beta \colon V_3 \to V_1$ be the normalization of $\mathrm{Bl}_{H'} V_1$. Then $\beta^{-1}(U_1) \cong W_1$, because $W_1$ is regular, and on $\beta^{-1}(U_1)$ the birational map $\gamma \colon V_3 \dashrightarrow V_2$ is the morphism $\tau$.

Step 4. Let $L \subseteq V_2$ be the set of the centers on $V_2$ of the valuations $v \in N$ whose center on $V_1$ is singular. Such a $v$ has a regular center $p_0 \in U_0$ on $V_0$, so its center on $V_2$ is in the preimage of $U_0$, which is regular. So $L \subseteq U_2$. Let $\Phi \subseteq V_2$ be the fundamental locus of $\gamma^{-1} \colon V_2 \dashrightarrow V_3$.

*Claim A.* Each irreducible component $\Gamma_2$ of $\Phi$ that meets $L$ is contained in $\alpha^{-1}(\mathrm{Sing}\, V_1)$.

*Proof of Claim A.* Let $\eta_2$ be the generic point of $\Gamma_2$ and let $p_2 \in \Gamma_2 \cap L$. Then $\eta_2$ is a generization of $p_2 \in U_2$, and $U_2$ is open, so $\eta_2 \in U_2$. Put $\eta_1 = \alpha(\eta_2)$ and $d = \dim \overline{\{\eta_1\}}$. Since $\Phi$ has codimension at least 2, $\dim \Gamma_2 \le 2$, so $d \le 2$ and $\dim \mathcal{O}_{V_2, \eta_2} \ge 2$. There are four cases.

- If $\eta_1 \in \mathrm{Sing}\, V_1$, then $\Gamma_2 \subseteq \alpha^{-1}(\overline{\{\eta_1\}}) \subseteq \alpha^{-1}(\mathrm{Sing}\, V_1)$, because $\mathrm{Sing}\, V_1$ is closed.
- If $d = 0$, then $\alpha(\Gamma_2)$ is the closed point $\eta_1 = \alpha(p_2)$. This is the center of a valuation in $N$ on $V_1$ with $p_2 \in L$, so it is singular, and the first case applies.
- If $d = 1$ and $\eta_1 \in U_1$, then $\eta_2 \in \mathrm{Reg}\, Z$, $\dim \overline{\alpha(\eta_2)} = 1$, $\dim \mathcal{O}_{Z,\eta_2} \ge 2$ and $p_2 \in \overline{\{\eta_2\}} \cap L$. By $\mathrm{Fac}_3^L$, $\tau$ is a local isomorphism over $\eta_2$, so $\gamma^{-1}$ is a morphism near $\eta_2$. This contradicts $\eta_2 \in \Phi$.
- If $d = 2$ and $\eta_1 \in U_1$, then $\dim \mathcal{O}_{V_1,\eta_1} = 2$ and $\dim \mathcal{O}_{V_2,\eta_2} = 2$. By Lemma 3.24.11, $\tau$ is a local isomorphism over $\eta_2$ for each principalization. This is a contradiction as before.

So only the first case occurs. This proves Claim A.

Step 5. Let $\tilde U_2$ be $U_2$ minus the union of the components of $\Phi$ that do not meet $L$. It is open and contains $L$. Let $G = \Phi \cap \tilde U_2$. It is closed in $\tilde U_2$, of codimension at least 2, and by Claim A its closure $\bar G$ in $V_2$ is contained in $\alpha^{-1}(\mathrm{Sing}\, V_1)$. The closure $Z_2$ of the graph of $\tilde U_2 \dashrightarrow V_3$ is projective and birational over $\tilde U_2$ and an isomorphism over $\tilde U_2 \setminus G$. By Lemma 3.24.8, $Z_2 = \mathrm{Bl}_{J_2} \tilde U_2$ with $V(J_2) \subseteq G$. By $\mathrm{Princ}_4$ there is a principalization $W_2 \to \tilde U_2$ of $J_2$. Its centers are in the locus where $J_2$ is not invertible, which lies over $G$. So $W_2 \to \tilde U_2$ is an isomorphism over $\tilde U_2 \setminus G$, $W_2$ is regular, and $W_2 \to Z_2 \to V_3$ is a morphism. By Lemma 3.24.8 again, $W_2 = \mathrm{Bl}_{H_2} \tilde U_2$ with $V(H_2) \subseteq G$. Extend $H_2$ to an ideal $J'$ on $V_2$ by Lemma 3.24.9, and let $\delta \colon V_4 \to V_2$ be the normalization of $\mathrm{Bl}_{J'} V_2$. Then $\delta^{-1}(\tilde U_2) \cong W_2$, and $\delta$ is an isomorphism over $V_2 \setminus \bar G$.

Step 6. Let $V_5$ be the normalization of the closure of the graph of $V_4 \dashrightarrow V_3$. It is normal and projective, and it dominates $V_4$, $V_2$, $V_0$ and $V_1$. Let $v \in N$, with centers $p_1, \dots, p_5$ on $V_1, \dots, V_5$.

- Suppose that $p_1 \in U_1$. Then $p_3 \in \beta^{-1}(U_1) \cong W_1$ is regular, and $\gamma$ is a morphism near $p_3$ with $\gamma(p_3) = p_2$. Since $\alpha(p_2) = p_1$ is regular and $\bar G \subseteq \alpha^{-1}(\mathrm{Sing}\, V_1)$, the point $p_2$ is not in $\bar G$, and $\delta$ is an isomorphism near $p_4$. So $V_3 \dashrightarrow V_4$ is a morphism near $p_3$, the graph is isomorphic to $V_3$ near $p_3$, and $\mathcal{O}_{V_5,p_5} \cong \mathcal{O}_{V_3,p_3}$ is regular.
- Suppose that $p_1 \in \mathrm{Sing}\, V_1$. Then $p_2 \in L \subseteq \tilde U_2$, so $p_4 \in \delta^{-1}(\tilde U_2) \cong W_2$ is regular, and $V_4 \to V_3$ is a morphism near $p_4$. So $\mathcal{O}_{V_5,p_5} \cong \mathcal{O}_{V_4,p_4}$ is regular.

So $W = V_5$ has the property of $\mathrm{Fund}_4$. $\square$

If $V_1$ is regular, then $L$ is empty, Claim A has no content, $G$ is empty, and the proof uses only $\mathrm{Princ}_4$. In this case $\mathrm{Fund}_4$ is easy for other reasons too.

**Remark (on the text of Cutkosky).** In his proof of Theorem 15.1 Cutkosky applies the factorization theorem of Abhyankar to $\mathcal{O}_{V_1,\eta_1}$, and this needs $\eta_1$ to be regular. When the curve $\overline{\{\eta_1\}}$ lies in $\mathrm{Sing}\, V_1$, his conclusion $\alpha(\Gamma_2) = p_1$ does not follow. The form of Claim A above is the repair: it is all that the rest of the proof uses, and it is trivial when $\eta_1$ is singular. His final case analysis has three cases, and the two cases of Step 6 cover them, because the only property of $G$ that Step 6 uses is $\bar G \subseteq \alpha^{-1}(\mathrm{Sing}\, V_1)$. In dimension 3 the component $\Gamma_2$ has dimension at most 1. So $d = 1$ means that a curve maps onto a curve, both local rings have dimension 2, and Abhyankar's theorem gives Claim A. The case $d = 2$ does not occur. In dimension 4 the case $d = 2$ is Lemma 3.24.11, which is Abhyankar's theorem again, and the case $d = 1$ needs a statement about regular local rings of dimension 3. The rest of this section shows that this statement is false.

### Factorization of regular local rings of dimension three

**Definition 3.24.14 (factorization).** Let $R \subseteq S$ be regular local rings of the same dimension with a common fraction field, with $S$ dominating $R$, and let $\nu$ be a valuation that dominates $S$. A *monoidal transform* of $R$ is a localization $R_1$ of the blowup of $\operatorname{Spec} R$ along a prime $P$ with $R/P$ regular, such that $R_1$ dominates $R$. The pair $(R, S)$ has *direct factorization* if $S$ is an iterated monoidal transform of $R$. It has *local strong factorization* along $\nu$ if there is a regular local ring $T$, dominated by $\nu$, that is an iterated monoidal transform of both $R$ and $S$. It has *local weak factorization* if $R$ and $S$ are joined by a finite chain of monoidal transforms and their inverses, all dominated by $\nu$.

Node: SG000000C0 · Lean: none yet

Direct factorization implies local strong factorization, with $T = S$, and local strong factorization implies local weak factorization. In dimension 2 all three hold, by Abhyankar. Karu calls the toric form of direct factorization "directly factorizable" [Kar03, Section 1].

**Lemma 3.24.15.** Suppose that $\mathrm{Fac}_3$ holds for $(U, K)$. Then each regular local ring $S = \mathcal{O}_{Z,\zeta}$, with $\zeta$ as in $\mathrm{Fac}_3$, is an iterated monoidal transform of $R = \mathcal{O}_{U,\alpha(\zeta)}$. Conversely, each regular local ring $S$, essentially of finite type over $R$, that birationally dominates $R$ is $\mathcal{O}_{Z,\zeta}$ for some ideal $K$ on $U$ and some $\zeta \in \mathrm{Reg}\, Z$.

Node: SG000000C0 · Lean: none yet

*Proof.* If $\tau$ is a local isomorphism over $\zeta$, then $S = \mathcal{O}_{W,w}$ for a point $w$ of $W$. Follow the center of a valuation that dominates $S$ through the blowups of $\sigma$, localized at $\alpha(\zeta)$. A blowup whose center does not contain the current center of the valuation does not change the local ring, and the other blowups are monoidal transforms. This gives the chain. For the converse, write $S = B_{\mathfrak{q}}$ with $B = R[f_1/f_0, \dots, f_n/f_0]$. Then $\operatorname{Spec} B$ is an affine chart of the blowup of $(f_0, \dots, f_n)$ on $\operatorname{Spec} R$, and its normalization $\tilde B$ satisfies $B \subseteq \tilde B \subseteq S$, because $S$ is normal. So $S$ is the local ring of the normalized blowup at the prime $\mathfrak{m}_S \cap \tilde B$. Spread $(f_0, \dots, f_n)$ out to an ideal on a neighborhood of $\alpha(\zeta)$ in $U$, and extend it to $U$ by Lemma 3.24.9. $\square$

So $\mathrm{Fac}_3$ is a form of direct factorization, and not of strong factorization. Direct factorization is the form that is known to fail in dimension 3. Sally and Shannon found regular local rings $R \subset S$ of dimension 3, with $S$ birationally dominating $R$, such that $S$ is not an iterated monoidal transform of $R$ (Cutkosky quotes these results in the introduction of his paper on local factorization, arXiv math/9803078). The toric example below is explicit, and it works for arbitrary regular centers.

Let $F$ be a field and $R = F[x,y,z]_{(x,y,z)}$. A regular cone $\sigma \subseteq \mathbb{R}^3_{\ge 0}$ gives a regular local ring $S_\sigma$: the local ring of $F[\sigma^\vee \cap \mathbb{Z}^3]$ at its maximal monomial ideal. It birationally dominates $R$ if $\sigma$ meets the interior of the octant.

**Proposition 3.24.16.** Let $\sigma_0 \subset \mathbb{R}^3_{\ge 0}$ be the cone spanned by $g_1 = (0,1,3)$, $g_2 = (1,1,1)$ and $g_3 = (2,1,0)$, and put $S_0 = S_{\sigma_0}$. Then:

1. $\sigma_0$ is regular, and $S_0$ is a regular local ring of dimension 3 that birationally dominates $R$;
2. for each of the torus-invariant regular primes $(x,y)$, $(x,z)$, $(y,z)$ and $(x,y,z)$ of $R$, the ideal $P S_0$ is not principal. So $S_0$ is not an iterated monoidal transform of $R$ with torus-invariant centers.

Node: SG000000C2 · Lean: none yet

*Proof.* (1) The determinant is $0 \cdot (0 - 1) - 1 \cdot (0 - 2) + 3 \cdot (1 - 2) = -1$. Each point in the relative interior of $\sigma_0$ has a positive coefficient on $g_2$, so all its coordinates are positive. So the monomial valuations of weight $w$ in the interior of $\sigma_0$ are positive on $x$, $y$ and $z$, and $x, y, z \in \mathfrak{m}_{S_0}$.

(2) First, a monomial $x^u$ is in $S_0$ if and only if $u \in \sigma_0^\vee$. Indeed, if $x^u = f/h$ with $h$ a unit, that is, with a nonzero constant term, then $x^u h = f \in F[\sigma_0^\vee \cap \mathbb{Z}^3]$, and $u$ is in the support of $f$. Next, by Nakayama's lemma a finitely generated ideal of a local ring is principal if and only if one element of a given set of generators generates it. So for $P = (x^{u_1}, \dots, x^{u_r})$, the ideal $P S_0$ is principal if and only if there is an $i$ with $u_j - u_i \in \sigma_0^\vee$ for all $j$, that is, $\langle g, u_i \rangle \le \langle g, u_j \rangle$ for $g = g_1, g_2, g_3$ and all $j$. For $(x,y)$: $x$ fails at $g_3$, since $2 > 1$, and $y$ fails at $g_1$, since $1 > 0$. For $(x,z)$: $x$ fails at $g_3$ and $z$ fails at $g_1$. For $(y,z)$: $y$ fails at $g_3$, since $1 > 0$, and $z$ fails at $g_1$, since $3 > 1$. For $(x,y,z)$: $x$ fails at $g_3$, and $y$ and $z$ fail at $g_1$. Finally, if $S_0$ dominates a monoidal transform $R_1$ of $R$ along $P$, then a generator of the invertible ideal $P R_1$ generates $P S_0$. $\square$

**Computation.** The research notes enumerate all regular cones in the octant whose generators have entries at most $B$, and test whether a sequence of torus-invariant smooth star subdivisions, at a 2-face or at the whole cone, reaches them. For $B = 2$ all 337 regular cones are reached. For $B = 3$, 144 of the 2515 regular cones are not reached, and for $B = 4$, 900 of the 8860 are not reached. The referee report in note 82 confirmed these numbers with independent code. So 3 is the smallest bound for an unreached cone, and $\sigma_0$ is one of them.

**Theorem 3.24.17.** Let $F$ be a field. There is no prime $P \subseteq \mathfrak{m}_R$ of height at least 2 with $R/P$ regular such that $P S_0$ is principal. Hence $S_0$ is not an iterated monoidal transform of $R$ for any choice of regular centers, and $\mathfrak{m}_R S_0$ is not principal.

Node: SG000000C3 · Lean: none yet

*Proof.* The dual basis of $(g_1, g_2, g_3)$ is $u_1 = (1,-2,1)$, $u_2 = (-3,6,-2)$ and $u_3 = (2,-3,1)$. So $S_0 = F[X_1, X_2, X_3]_{(X_1, X_2, X_3)}$ with $X_1 = x y^{-2} z$, $X_2 = x^{-3} y^6 z^{-2}$ and $X_3 = x^2 y^{-3} z$, and
$$x = X_2 X_3^2, \qquad y = X_1 X_2 X_3, \qquad z = X_1^3 X_2.$$

Step 1 (the divisor $X_2 = 0$ gives the order). Let $\nu$ be the order along $X_2 = 0$. The monomial $x^a y^b z^c$ maps to a monomial in $X_1, X_2, X_3$ whose exponent of $X_2$ is $a + b + c$. The monomial map is injective on exponents, because its matrix is invertible. So distinct monomials of $R$ go to distinct monomials, and no cancellation occurs. Hence $\nu(f) = \mathrm{ord}_{\mathfrak{m}_R}(f)$ for each $f \in R$, and each $f \in \mathfrak{m}_R$ is divisible by $X_2$ in $S_0$.

Step 2 (height 3). The only prime of height 3 is $\mathfrak{m}_R = (x,y,z)$. If $\mathfrak{m}_R S_0$ were principal, then one of $x$, $y$, $z$ would generate it, by Nakayama's lemma. Proposition 3.24.16 shows that none does.

Step 3 (height 2). Let $P$ be a prime of height 2 with $R/P$ regular. Then $P = (u, v)$ with $u, v$ part of a regular system of parameters of $R$. So $u$ and $v$ have order 1, and their initial forms $l_1$ and $l_2$ are linearly independent linear forms in $x, y, z$. By Step 1, $u = X_2 u'$ and $v = X_2 v'$ in $S_0$. So $P S_0 = X_2 \cdot (u', v') S_0$, and $P S_0$ is principal if and only if $(u', v') S_0$ is principal. Reduce modulo $X_2$, with $S_0 / X_2 S_0 = F[X_1, X_3]_{(X_1, X_3)} = T$. A term of order at least 2 of $u$ keeps a factor $X_2$ after division by $X_2$. So, up to units of $R$, which reduce to nonzero constants, $u' \equiv l_1(X_3^2, X_1 X_3, X_1^3)$ and $v' \equiv l_2(X_3^2, X_1 X_3, X_1^3)$. It is sufficient to show that the ideal $I = (f_1, f_2)$ of $T$ is not principal when $f_1$ and $f_2$ are linearly independent elements of
$$W = \mathrm{span}_F \{X_3^2,\ X_1 X_3,\ X_1^3\}.$$
Suppose that $I$ is principal. By Nakayama's lemma one of $f_1$, $f_2$ generates $I$. Call it $f$, call the other one $g$, and write $g = q f$ with $q \in T$. The elements of $W$ have order 2, except the nonzero multiples of $X_1^3$, which have order 3.

- If $f$ has order 3, then $f = c X_1^3$, and $X_1^3$ divides $g = a X_3^2 + b X_1 X_3 + c' X_1^3$. Divisibility by $X_1$ gives $a = 0$, and then divisibility by $X_1^2$ gives $b = 0$. So $g$ is a multiple of $f$, which contradicts the independence.
- If $f$ has order 2 and $g$ has order 3, then $g = c' X_1^3$, so $f$ divides $X_1^3$ in the factorial ring $T$, and $f$ is a unit times $X_1^2$. Then each monomial of $f$ is divisible by $X_1^2$, so the coefficients of $X_3^2$ and $X_1 X_3$ in $f$ are $0$, and $f$ has order 3. This is a contradiction.
- If $f$ and $g$ both have order 2, then $q$ is a unit. The element $h = g - q(0) f = (q - q(0)) f$ is in $W$ and has order at least 3, so $h = c X_1^3$. If $c \ne 0$, then $f$ divides $X_1^3$, and the second case gives a contradiction. If $c = 0$, then $g = q(0) f$, which contradicts the independence.

So $P S_0$ is never principal. Finally, take a chain $R = T_0 \subset T_1 \subset \dots \subset T_r = S_0$ of monoidal transforms. A step whose center has height 1 is the identity, because a prime of height 1 of a regular local ring is principal. So we can assume that the first center $P$ has height at least 2. It is contained in $\mathfrak{m}_R$, because $S_0$ dominates $R$, and $P T_1$ is principal, so $P S_0$ is principal. This contradicts Steps 2 and 3. $\square$

The theorem covers the centers $(x + a y, z + b x)$ with $a, b \in F$, $(x - y^2, z)$ and $(y - x^2, z - x^3)$, which research note 77 proposed as test cases.

**Corollary 3.24.18.** $\mathrm{Fac}_3$ is false, over each field and in each characteristic.

Node: SG000000C4 · Lean: none yet

*Proof.* Let $U = \mathbb{A}^4$ with coordinates $(t, x, y, z)$, and let
$$K = (x^3 y^3 z^2,\ x^4 y z^3,\ y^9,\ x^5 z^3).$$
The exponents of $K$ are $u_0 = (3,3,2)$ and $u_0 + u_1 = (4,1,3)$, $u_0 + u_2 = (0,9,0)$, $u_0 + u_3 = (5,0,3)$. The normal cone at the vertex $u_0$ of their convex hull is $\{w : \langle w, u_j \rangle \ge 0,\ j = 1, 2, 3\} = \sigma_0$. So the normalized blowup $Z$ of $K$ has the chart $\operatorname{Spec} k[t] \otimes k[\sigma_0^\vee \cap \mathbb{Z}^3]$. Let $\zeta$ be the generic point of the line $\{t\text{-axis}\} \times \{\text{fixed point}\}$ of this chart. Then $\mathcal{O}_{Z,\zeta}$ is $S_0$ over $F = k(t)$, so $\zeta \in \mathrm{Reg}\, Z$, $\dim \overline{\alpha(\zeta)} = 1$ and $\dim \mathcal{O}_{Z,\zeta} = 3$, and $\mathcal{O}_{U,\alpha(\zeta)} = R$. If $\mathrm{Fac}_3$ held for $(U, K)$, then $S_0$ would be an iterated monoidal transform of $R$ by Lemma 3.24.15. This contradicts Theorem 3.24.17. $\square$

The referee report in note 82 uses the vertex $(3,3,3)$ and the ideal $(x^3 y^3 z^3, x^4 y z^4, y^9 z, x^5 z^4)$, which works equally well. In this example $V_1 = \mathbb{A}^4$ is regular, so it does not refute $\mathrm{Fac}_3^L$, which is vacuous there. The next construction puts the same local ring over a singular point.

### A toric pair of 4-folds where the route breaks

Let $N = \mathbb{Z}^4$ with coordinates $(t, x, y, z)$, and let $t, x, y, z$ also denote the characters of the dual basis. We use the toric geometry of [Ful93] (Volume 0 and Section 3.22 use the same conventions). The scripts of research note 83 check each number in the construction with exact integer arithmetic.

**Construction 3.24.19.** The construction has four parts.

*The model $V_1$.* Put $f = (2,1,1,1)$, let $e_x, e_y, e_z$ be the unit vectors of the last three coordinates, and put $v_5 = (-1,-1,-1,-1)$. Then
$$f + e_x + e_y + e_z + 2 v_5 = 0,$$
so the cones over the proper subsets of $\{f, e_x, e_y, e_z, v_5\}$ form a complete simplicial fan $\Sigma_1$. Its toric variety $V_1$ is a fake weighted projective space. It is normal and projective. Four of its five maximal cones have determinant $\pm 1$. The fifth cone, $C = \langle f, e_x, e_y, e_z \rangle$, has determinant 2, and each proper face of $C$ is regular. So $\mathrm{Sing}\, V_1 = \{p_1\}$, where $p_1$ is the fixed point of $U_C$. Let $\tau_1 = \langle e_x, e_y, e_z \rangle$ and $C' = \langle e_x, e_y, e_z, v_5 \rangle$. Then $\tau_1 = C \cap C'$, because $f$ and $v_5$ lie on the two sides of the hyperplane $w_t = 0$. The curve $C_1 = V(\tau_1)$ joins $p_1$ to the fixed point $p_1'$ of $U_{C'}$, which is regular. Its generic point $\eta_1$ is regular, with $\mathcal{O}_{V_1, \eta_1} = k(t)[x,y,z]_{(x,y,z)} = R$ over $F = k(t)$, since $U_{\tau_1} = \operatorname{Spec} k[t^{\pm 1}, x, y, z]$.

*The model $V_0$.* Let $P_K \subset \mathbb{R}^3$ be the convex hull of the four exponents of $K$ in the proof of Corollary 3.24.18, let $\Sigma_K$ be its normal fan, and let $\pi(t, x, y, z) = (x, y, z)$. Let $\Sigma'$ be the common refinement of $\Sigma_1$ and of the cones $\pi^{-1}(\rho)$, $\rho \in \Sigma_K$. It is the normal fan of a Minkowski sum of polytopes, so its toric variety is projective. The normal cone $N_{P_K}(u_0)$ at the vertex $u_0$ is $\sigma_0$. So $\tau_1 \cap \pi^{-1}(\sigma_0) = \{0\} \times \sigma_0$ is a cone of $\Sigma'$. It is a common face of the two cones $D_0 = C \cap \pi^{-1}(\sigma_0)$ and $D_0' = C' \cap \pi^{-1}(\sigma_0)$, which lie on the two sides of $w_t = 0$. Let $\Sigma_0$ be obtained from $\Sigma'$ by the star subdivisions at
$$r = (1,1,1,1) \quad\text{and}\quad r' = (-2,1,1,1).$$
Both have $\pi(r) = \pi(r') = (1,1,1) = g_2 \in \sigma_0$. In the basis $(f, e_x, e_y, e_z)$ of $C$ the vector $r$ has the coordinates $(\frac12, \frac12, \frac12, \frac12)$, and in the basis $(e_x, e_y, e_z, v_5)$ of $C'$ the vector $r'$ has the coordinates $(3,3,3,2)$. So $r \in D_0$ and $r' \in D_0'$, and each is in the interior of its cone of $\Sigma_1$. A star subdivision keeps projectivity. In $\Sigma_0$ the 3-dimensional cone $\{0\} \times \sigma_0$, which we write $\sigma_0$ again, is a face of exactly two 4-dimensional cones,
$$D = \langle \sigma_0, r \rangle, \quad \det D = 1, \qquad D' = \langle \sigma_0, r' \rangle, \quad \det D' = -2.$$
Let $V_0 = X(\Sigma_0)$. It is a normal projective toric variety with a toric birational morphism $V_0 \to V_1$.

*The points.* Let $\Gamma = V(\sigma_0) \subseteq V_0$, a curve, with generic point $\eta_2$, and let $p_2$ and $z$ be the fixed points of $U_D$ and $U_{D'}$, the two ends of $\Gamma$. The cone $\sigma_0$ spans the hyperplane $w_t = 0$, so the character $t$ is a unit at $\eta_2$, and
$$\mathcal{O}_{V_0, \eta_2} = k(t)[a, b, c]_{(a, b, c)}, \qquad x = b c^2, \quad y = a b c, \quad z = a^3 b.$$
This is $S_0$ over $F = k(t)$, with $a = X_1$, $b = X_2$, $c = X_3$. The relative interior of $\sigma_0$ lies in the relative interior of $\tau_1$, so $\eta_2$ maps to $\eta_1$. The cone $D$ lies in $C$, so $p_2$ maps to the singular point $p_1$, and $D'$ lies in $C'$, so $z$ maps to the regular point $p_1'$. Since $\det D = 1$ the point $p_2$ is regular on $V_0$, and since $\det D' = -2$ the point $z$ is singular.

*The valuations.* Let $v$ be the monomial valuation of weight
$$w = (1,4,4,5) = (0,0,1,3) + (0,1,1,1) + (0,2,1,0) + (1,1,1,1),$$
the sum of the generators of $D$. It is a divisorial valuation, and $w$ is in the interior of $D$. In the basis of $C$ it has the coordinates $(\frac12, \frac72, \frac72, \frac92)$, so it is in the interior of $C$. So the center of $v$ is $p_2$ on $V_0$, which is regular, and $p_1$ on $V_1$, which is singular, and $v \in N$. Similarly, $w' = (-2,4,4,5) = g_1 + g_2 + g_3 + r'$ is in the interior of $D'$, and in the basis of $C'$ it has the coordinates $(6,6,7,2)$. It gives a valuation $v' \in N$ with center $z$ on $V_0$ and $p_1'$ on $V_1$, which is regular.

Node: SG000000C5 · Lean: none yet

**Theorem 3.24.20.** Run the proof of Theorem 3.24.13 on the triple $(V_0, V_1, N)$ of Construction 3.24.19, with any principalization $W_1$ in Step 3. Then:

1. $\eta_2$ is in the fundamental locus $\Phi$ of $\gamma^{-1} \colon V_2 \dashrightarrow V_3$. The component of $\Phi$ through $\eta_2$ meets $L$ at $p_2$, and it is not contained in $\alpha^{-1}(\mathrm{Sing}\, V_1)$. So Claim A fails, through its case $d = 1$, and $\mathrm{Fac}_3^L$ is false for this triple, over each field and in each characteristic.
2. For each open set $\tilde U_2$ with $L \subseteq \tilde U_2 \subseteq U_2$, the closure of $\Phi \cap \tilde U_2$ contains the point $z$, which is in $\alpha^{-1}(\mathrm{Reg}\, V_1) \setminus U_2$.
3. $\mathrm{Fund}_4$ holds for $(V_0, V_1)$.

Node: SG000000C5 · Lean: none yet

*Proof.* Step 1 of the proof: $V_0$ dominates $V_1$, so $\Gamma \cong V_0$ and $I = \mathcal{O}_{V_0}$. Step 2: a principalization of the unit ideal has its centers in the empty locus, so $W_0 = U_0$, $J = \mathcal{O}$, $X_1 = V_0$ and $V_2 = V_0$, with $\alpha$ the toric morphism. Step 4: $p_2 \in L$, because it is the center of $v$. Since $\sigma_0 \subseteq D$, we have $p_2 \in \overline{\{\eta_2\}}$.

(1) Suppose that $\gamma^{-1}$ is a morphism near $\eta_2$, and put $q = \gamma^{-1}(\eta_2)$. Then $\beta(q) = \alpha(\eta_2) = \eta_1 \in U_1$, so $q \in \beta^{-1}(U_1) \cong W_1$, where $\gamma = \tau$ is a morphism. The morphism $\gamma \circ \gamma^{-1}$ is the identity on a dense open set, and $V_2$ is separated, so $\tau(q) = \eta_2$. The local homomorphisms $\mathcal{O}_{Z,\eta_2} \to \mathcal{O}_{W_1,q} \to \mathcal{O}_{Z,\eta_2}$ are inclusions in the function field with the identity as composite, so $\mathcal{O}_{W_1,q} = S_0$. The base change of $W_1 \to U_1$ to $\operatorname{Spec} R$ is flat and keeps the centers regular. So $\mathcal{O}_{W_1,q}$ is an iterated monoidal transform of $R$: centers that do not pass through the image of $q$ do not change the local ring, and centers of height 1 there give isomorphisms. This contradicts Theorem 3.24.17 with $F = k(t)$. So $\eta_2 \in \Phi$. Let $\Gamma_2$ be a component of $\Phi$ that contains $\eta_2$. Then $p_2 \in \Gamma_2 \cap L$, while $\alpha(\eta_2) = \eta_1 \in U_1$. In Definition 3.24.12 the point $\eta_2$ satisfies all the conditions: $\eta_2 \in \mathrm{Reg}\, Z$, $\dim \overline{\alpha(\eta_2)} = 1$, $\dim \mathcal{O}_{Z,\eta_2} = 3$ and $p_2 \in \overline{\{\eta_2\}} \cap L$. The argument above shows that $\tau$ is never a local isomorphism over $\eta_2$.

(2) The set $\tilde U_2$ is open and contains $p_2$, so it contains its generization $\eta_2$. Hence $\eta_2 \in \Phi \cap \tilde U_2$, and $z \in \overline{\{\eta_2\}}$. Also $\alpha(z) = p_1'$ is regular, and $z$ is singular on $V_2 = V_0$.

(3) A toric resolution by star subdivisions [Ful93] (Cox, Little and Schenck, Theorem 11.1.9) gives a regular projective $W \to V_0 \to V_1$. $\square$

Part (3) shows that the construction is not a counterexample to $\mathrm{Fund}_4$. It is a counterexample to the method. The next result gives the weakest form of Claim A that Step 6 of the proof needs, and part (2) shows that this form fails too.

**Proposition 3.24.21.** In the proof of Theorem 3.24.13, replace Claim A by the condition

(A$^{\rm w}$) there is an open set $\tilde U_2$ with $L \subseteq \tilde U_2 \subseteq U_2$ such that $\overline{\Phi \cap \tilde U_2} \cap \alpha^{-1}(U_1) \subseteq \tilde U_2$.

Then Steps 5 and 6 go through with this $\tilde U_2$ and $G = \Phi \cap \tilde U_2$. So $\mathrm{Princ}_4$ and (A$^{\rm w}$), for some choice of $W_1$, give the conclusion of $\mathrm{Fund}_4$ for $(V_0, V_1, N)$. Claim A implies (A$^{\rm w}$), with the $\tilde U_2$ of Step 5.

Node: SG000000C6 · Lean: none yet

*Proof.* Step 5 uses only that $\tilde U_2$ is open and regular and contains $L$. In Step 6, if $p_1 \in \mathrm{Sing}\, V_1$, then $p_2 \in L \subseteq \tilde U_2$, and the argument is the same as before. Let $p_1 \in U_1$. If $p_2 \in \tilde U_2$, then $p_4 \in \delta^{-1}(\tilde U_2) \cong W_2$ is regular and $W_2 \to V_3$ is a morphism, so $\mathcal{O}_{V_5,p_5} \cong \mathcal{O}_{V_4,p_4}$ is regular. If $p_2 \notin \tilde U_2$, then $p_2 \in \alpha^{-1}(U_1) \setminus \tilde U_2$, so $p_2 \notin \bar G$ by (A$^{\rm w}$). Then $\delta$ is an isomorphism near $p_2$, and the argument of Step 6 applies at $p_3$. Under Claim A, $\bar G \subseteq \alpha^{-1}(\mathrm{Sing}\, V_1)$, which does not meet $\alpha^{-1}(U_1)$. $\square$

Replace $V_0$ in Construction 3.24.19 by a toric resolution by star subdivisions that keeps the regular cones $D$ and $\sigma_0$. Then $V_2 = V_0$ is regular, (A$^{\rm w}$) holds with $\tilde U_2 = U_2 = V_2$, and Claim A still fails by Theorem 3.24.20(1). So Claim A is strictly stronger than what the proof needs. But (A$^{\rm w}$) holds whenever $V_0$ is regular, and then $\mathrm{Fund}_4$ is easy: principalize $I$ on $V_0$. Theorem 3.24.20(2) shows that (A$^{\rm w}$) fails in general, also for toric pairs. So no hypothesis on $W_1$ alone, and no choice of $\tilde U_2$, makes Steps 5 and 6 of the proof of Cutkosky work in dimension 4.

The mechanism is a curve $\Gamma$ in $\Phi$ that maps onto a curve of $V_1$ through a singular point. Its generic local ring does not have direct factorization, and it joins a point of $L$ over $\mathrm{Sing}\, V_1$ to a singular point of $V_2$ over $\mathrm{Reg}\, V_1$. Blowups along regular centers in $U_2$ that remove $\Gamma$ from $\Phi$ near $p_2$ change $V_2$ along all of $\Gamma$, up to $z$. There the valuation $v'$ needs the model $W_1$, and these blowups do not dominate $W_1$. The construction works over each field, and it does not depend on the characteristic. Each of the other 143 cones with entries at most 3 that toric subdivisions do not reach gives the same construction, if the corresponding form of Theorem 3.24.17 holds for it.

### Why dimension four breaks the step of Abhyankar

**Proposition 3.24.22.** In dimension 3, at the generic point $\xi$ of a curve in the fundamental locus that maps onto a curve, the proofs of Cutkosky and of Cossart and Piltant need one of two statements about regular local rings $R \subseteq S$ of the same dimension with $S$ birationally dominating $R$: that $S$ is an iterated monoidal transform of $R$ (Cutkosky), or that $\mathfrak{m}_R S$ is principal when $S \ne R$ (Cossart and Piltant). In dimension 3 these rings have dimension 2, and both statements hold. In dimension 4 the rings have dimension 3 over the field $\kappa(\xi)$, which is not perfect, and both statements fail for $R = k(t)[x,y,z]_{(x,y,z)}$ and $S = S_0$ over $k(t)$.

Node: SG000000C7 · Lean: none yet

*Proof.* In dimension 3 the rings have dimension 2. Abhyankar's theorem gives an iterated quadratic transform, and the first step of the sequence makes $\mathfrak{m}_R S$ principal. In dimension 4, Theorem 3.24.17 shows that $S_0$ is not an iterated monoidal transform of $R$ and that $\mathfrak{m}_R S_0$ is not principal. The field $k(t)$ is not perfect, since $t$ has no $p$-th root. $\square$

For Cutkosky the step is the case $d = 1$ of Claim A, and Theorem 3.24.20 shows that it fails in a global configuration, not only locally. For Cossart and Piltant the step is in Step 2 of the proof of their Proposition 4.6 [CP19]. When a center $Z_i$ of their Lemma 4.5 is a curve whose image is a curve with generic point $\xi_i$, they need the ideal of $Z_i$ to become invertible above $\xi_i$, and they get this from their Proposition 4.2, which is Abhyankar's theorem. This keeps a preliminary principalization an isomorphism away from finitely many closed points, which is their condition (4.7), and this gives the gluing. In dimension 4 the corresponding statement at the generic point of a curve fails. Toric data put the failure over a singular locus: take a singular 3-dimensional cone $\rho$ in $\mathbb{Z}^4$, a resolution that contains a regular 3-dimensional cone $\tau \subseteq \rho$, and a second resolution that contains $\sigma_0$, written in the basis of $\tau$. Then the preliminary principalization can change a model over a whole curve, and (4.7) has to be replaced by a statement about curves. This reading of the proof of Cossart and Piltant is from research note 83, and it is not a theorem.

What does hold locally is strong factorization.

**Theorem 3.24.23 (Karu).** Let $\sigma$ be a regular cone in $\mathbb{R}^n_{\ge 0}$ and let $\nu$ be a valuation vector in the interior of $\sigma$ with rationally independent coordinates. Then there is a regular cone that contains $\nu$ and is obtained from both $\sigma$ and $\mathbb{R}^n_{\ge 0}$ by smooth star subdivisions [Kar03, Theorem 0.2]. In characteristic 0, each pair $R \subseteq S$ of regular local rings, essentially of finite type, with $S$ birationally dominating $R$, has local strong factorization along each valuation [Kar03, Theorem 0.1].

Node: SG000000C7 · Lean: none yet

The toric statement is combinatorial, so it holds in each characteristic. Karu extends an argument of Christensen in dimension 3, and his proof in characteristic 0 uses the monomialization theorem of Cutkosky. In characteristic $p$, local strong factorization of regular local rings of dimension 3 is open. Global strong factorization, and the strong factorization conjecture of Oda for toric varieties, are open even in dimension 3. Resolution of quasi-excellent schemes of dimension 3 is known in each characteristic [CP19, Theorem 1.1]. It resolves graphs over $\operatorname{Spec} \mathcal{O}_{V_1,\eta_1}$, but only at the generic point of the curve.

### What is open

1. $\mathrm{Fund}_4$ (Conjecture 3.24.3). By Theorem 3.24.5 it is, together with $\mathrm{PILU}_4$, exactly what resolution of 4-folds by projective morphisms needs. No reduction of it to simpler statements is known.
2. $\mathrm{Princ}_4$ (Conjecture 3.24.7). It is not known to follow from $\mathrm{Res}_4^{\rm pr}$.
3. Regular reachability of toric rings.

**Conjecture 3.24.24.** Let $\sigma \subseteq \mathbb{R}^3_{\ge 0}$ be a regular cone. If $S_\sigma$ is an iterated monoidal transform of $R = F[x,y,z]_{(x,y,z)}$ with arbitrary regular centers, then $\sigma$ is reached from $\mathbb{R}^3_{\ge 0}$ by smooth star subdivisions at 2-faces or at the whole cone.

Node: SG000000C8 · Lean: none yet

The converse is clear. Research note 83 checks a sufficient condition for the conjecture cone by cone. For entries at most 3 all 144 unreached cones satisfy it, and for entries at most 4, 768 of the 900 unreached cones satisfy it. The 132 cones that are left fall into 22 classes, and they are open. An example is $\langle (0,1,3), (1,2,2), (3,4,1) \rangle$. Here the center $(x, y + z^3)$ is allowed, and in $S_\sigma$ one has $y + z^3 = a b^2 c^3 (c + a^8 b^4)$, so after this blowup $S_\sigma$ is no longer a toric ring over the new ring in the coordinates that the method uses.

4. Patching along curves.

**Conjecture 3.24.25 (patching along curves).** Let $\alpha \colon V_2 \to V_1$ and $\beta \colon V_3 \to V_1$ be projective birational morphisms of normal 4-folds, with $\beta^{-1}(\mathrm{Reg}\, V_1)$ regular, and let $\Gamma \subseteq V_2$ be an irreducible curve in the fundamental locus of $V_2 \dashrightarrow V_3$ such that $\alpha(\Gamma)$ is a curve that meets $\mathrm{Sing}\, V_1$. Then there are projective birational morphisms $V_2' \to V_2$, a composite of blowups along regular centers over $\mathrm{Reg}\, V_2$ near $\alpha^{-1}(\mathrm{Sing}\, V_1)$, and $V_3' \to V_3$, a composite of blowups along regular centers over $\beta^{-1}(\mathrm{Reg}\, V_1)$, both isomorphisms off a neighborhood of $\Gamma$, such that $V_2' \dashrightarrow V_3'$ is a morphism near the generic point of $\Gamma$.

Node: SG000000C9 · Lean: none yet

A positive answer removes $\Gamma$ from the fundamental locus, and the centers of the valuations in $N$ stay regular, because a blowup along a regular center keeps regular points regular. Whether finitely many such steps, together with $\mathrm{Princ}_4$, reach the condition (A$^{\rm w}$) of Proposition 3.24.21 is part of the problem. The local input at the generic point of $\Gamma$ is local strong factorization in dimension 3 over $\kappa(\Gamma)$, which is open in characteristic $p$. The new global difficulty is the termination of the alternating blowups along $\Gamma$ near its points over $\mathrm{Sing}\, V_1$. For Construction 3.24.19, $\mathrm{Fund}_4$ holds by toric resolution, but it is not known whether it holds in the form of Conjecture 3.24.25.

5. Local strong factorization of regular local rings of dimension 3 over imperfect fields of characteristic $p$, beyond the toric case of Theorem 3.24.23.
6. $\mathrm{PILU}_4$ (Conjecture 3.24.2), the local half.

### Exercises

1. Check that $u_1 = (1,-2,1)$, $u_2 = (-3,6,-2)$ and $u_3 = (2,-3,1)$ is the dual basis of $(g_1, g_2, g_3)$ in Proposition 3.24.16, and derive the formulas $x = X_2 X_3^2$, $y = X_1 X_2 X_3$ and $z = X_1^3 X_2$.
2. Show directly from the formulas of Exercise 1 that $(x + a y, z + b x) S_0$ is not principal for $a, b \in F$. Which case of Step 3 of the proof of Theorem 3.24.17 applies?
3. Show that each regular cone in $\mathbb{R}^2_{\ge 0}$ is reached from the quadrant by smooth star subdivisions. Hint: use the Euclidean algorithm on the generators. This is the toric case of Abhyankar's theorem.
4. Find a sequence of smooth star subdivisions of $\mathbb{R}^3_{\ge 0}$ that reaches the cone $\langle (1,0,0), (1,1,0), (1,1,1) \rangle$, and describe the corresponding monoidal transforms of $R$.
5. In Lemma 3.24.8, give an example that shows that the hypothesis on the codimension of $G$ is necessary for $V(J) \subseteq G$. Hint: blow up a Cartier divisor.
6. Prove that $\mathrm{Fac}_3$ implies $\mathrm{Princ}_4$, and that $\mathrm{Fac}_3^L$ has no content for a triple with $V_1$ regular.
7. In Construction 3.24.19, check that $f + e_x + e_y + e_z + 2 v_5 = 0$, that $\det C = 2$, and that each proper face of $C$ is regular. Compute the coordinates of $r$ and $w$ in the basis of $C$, and of $r'$ and $w'$ in the basis of $C'$.
8. In Construction 3.24.19, compute $\det D$ and $\det D'$, and show that $w$ is in the interior of $D$ and $w'$ is in the interior of $D'$.
9. Show that the valuation $v'$ of Construction 3.24.19 is in $N$, and explain why the model $W_1$ is necessary for $v'$ in Step 6 of the proof of Theorem 3.24.13.
10. Show that a regular local ring of dimension 2 that birationally dominates another one $R \ne S$ makes $\mathfrak{m}_R S$ principal. Hint: use Abhyankar's theorem and the first quadratic transform.

### Status

The results are the nodes SG000000BQ to SG000000C9 of the map. Theorems 3.24.4 and 3.24.5, Lemmas 3.24.8, 3.24.9, 3.24.11 and 3.24.15, Proposition 3.24.16, Theorem 3.24.17 and Corollary 3.24.18 are from research note 77 and the referee report in note 82, which checked them. Theorem 3.24.13 is Theorem 77.8 of note 77, in the form that note 82 asks for and that note 83 states as Proposition 83.11. Construction 3.24.19, Theorem 3.24.20, Propositions 3.24.21 and 3.24.22 and Conjectures 3.24.24 and 3.24.25 are new in note 83, and a second referee has not read them yet. Theorem 3.24.23 is quoted from [Kar03]. None of the nodes has a Lean proof. An outside expert has not yet read the result.

### Notes and references

The results are in research note 77, with the corrections of note 82, which is a referee report on note 77, and in research note 83. Note 82 answered Problem 77.P1 of note 77 with Theorem 3.24.17, found that $\mathrm{Fac}_3$ is false, and corrected the citation of the remark of Temkin to [Tem13, Section 1.2(ii)]. Note 83 corrected the remark after Lemma 3.24.15 in note 77: $\mathrm{Fac}_3$ is a direct factorization statement, not a strong factorization statement. The patching method is in [Zar44] and in [Pil] in axiomatic form. The proof of Theorem 3.24.13 follows [Cut09, Theorem 15.1], and Theorem 3.24.4 follows [Cut09, Theorems 16.1 and 16.2]. Abhyankar's theorem is [Abh56], and [CP19, Proposition 4.2] states it in the form used here. The theorem of Temkin is [Tem13, Theorem 1.3.2]. For toric varieties see [Ful93]. For factorization in dimension 3 see [Kar03], and the results of Sally (Trans. Amer. Math. Soc. 171, 1972) and Shannon (Amer. J. Math. 95, 1973), which Cutkosky quotes in arXiv math/9803078. Volume 3, Chapter 4 and Volume 9, Section 3.21 treat the other parts of route R2.
