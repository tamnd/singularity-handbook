---
title: The bridge to formal-conjectures
nodes: [SG0000000E, SG00000020]
sources: [FC, Hir64, Har, Liu, HirLean]
status: drafted
drafted_by: writer
reviewed_by: []
---
## The bridge to formal-conjectures

The repository google-deepmind/formal-conjectures [FC] has a Lean statement of resolution of singularities. It was written independently of this project, with different choices. If two independent statements of the same problem agree where they meet, a reader can trust each of them more. This section proves that our notion of resolution implies the notion of formal-conjectures for integral varieties over perfect fields. As a consequence, Hironaka's theorem in the form of formal-conjectures is a theorem of the project, with no hypothesis.

### The statement of formal-conjectures

Let $k$ be a field and let $X$ be a scheme over $k$. A morphism $f : Y \to X$ is *birational over* $X$ when there are dense open sets $V \subseteq Y$ and $U \subseteq X$ such that $f$ restricts to an isomorphism $V \to U$. In the statement of formal-conjectures, $X$ *has a resolution* when there are an integral scheme $Y$ and a morphism $f : Y \to X$ such that

1. $f$ is proper;
2. $Y$ is smooth over $k$;
3. $f$ is birational over $X$.

The statement asks this for each integral scheme $X$ that is separated and of finite type over a perfect field $k$. We copied the definition into the project under its licence, in the file `Singularity/Bridge/FormalConjectures.lean`. The copy changes only the namespace.

The two notions differ in three places. Ours asks for a regular $Y$, and theirs asks for a smooth $Y$. Ours asks that $f$ is an isomorphism over the whole regular locus, and theirs asks for an isomorphism over some dense open set. Ours applies to reduced varieties over any field, and theirs to integral schemes over perfect fields.

### The comparison

**Proposition 1.4.1.** Let $k$ be a perfect field, let $X$ be an integral variety over $k$, and let $\pi : Y \to X$ be a resolution of $X$. Then $Y$ is integral and smooth over $k$, and $\pi$ is proper and birational over $X$. Thus $X$ has a resolution in the sense of formal-conjectures.

Node: SG0000000E · Lean: `Singularity.Base.hasResolution_of_isResolution`

*Proof.* Let $U = \operatorname{Reg}(X)$. It is open, because $\pi$ is a resolution.

*$U$ is dense.* Let $\eta$ be the generic point of $X$. Its local ring $\mathcal{O}_{X,\eta}$ is the function field of $X$, because $X$ is integral. A field is a regular local ring (Lemma 1.1.4), so $\eta \in U$. An open set that contains the generic point of an irreducible space is dense.

*$\pi^{-1}(U)$ is dense in $Y$ and isomorphic to $U$.* The first statement is condition 4 of a resolution, and the second is condition 3.

*$Y$ is integral.* The open subscheme $U$ of the integral scheme $X$ is nonempty, so it is integral. Thus $\pi^{-1}(U) \cong U$ is irreducible. The closure of an irreducible set is irreducible, and the closure of $\pi^{-1}(U)$ is $Y$. Thus $Y$ is irreducible. The scheme $Y$ is regular, and a regular local ring is a domain (Theorem 1.3.2), so each local ring of $Y$ is reduced, and $Y$ is reduced. A scheme that is irreducible and reduced is integral [Har, Proposition II.3.1].

*$Y$ is smooth over $k$.* The morphism $\pi$ is proper, so it is of finite type, and $Y$ is locally of finite type over $k$. Over a perfect field, a scheme that is locally of finite type is smooth if and only if it is regular [Liu, Section 4.3]. The scheme $Y$ is regular.

*$\pi$ is proper and birational over $X$.* It is proper because it is a resolution. The dense open sets $\pi^{-1}(U) \subseteq Y$ and $U \subseteq X$ and the isomorphism $\pi^{-1}(U) \to U$ show that $\pi$ is birational over $X$. $\square$

**Corollary 1.4.2 (Hironaka's theorem in the form of formal-conjectures).** Let $k$ be a field of characteristic 0 and let $X$ be an integral scheme that is separated and of finite type over $k$. Then $X$ has a resolution in the sense of formal-conjectures.

Node: SG00000020 · Lean: `Singularity.Base.fcResolutionCharZero`

*Proof.* A field of characteristic 0 is perfect. The scheme $X$ is integral, so it is reduced, and it is a variety in our sense. By Theorem 1.2.5 it has a resolution, and by Proposition 1.4.1 it has a resolution in the sense of formal-conjectures. $\square$

The corollary does not use Hypothesis 1.3.1, because the statement of formal-conjectures is about integral schemes only. Its status on the map is "proved".

### The converse is false

The converse of Proposition 1.4.1 does not hold. A resolution in the sense of formal-conjectures can change the variety over its regular locus.

**Example 1.4.3.** Let $k$ be a field, let $X = \mathbb{A}^2_k$, and let $\pi : Y = \operatorname{Bl}_O \mathbb{A}^2_k \to X$ be the blowup of the origin $O$. Then $Y$ is integral and smooth, $\pi$ is proper, and $\pi$ is an isomorphism over the dense open set $X \setminus \{O\}$. Thus $\pi$ is a resolution of $X$ in the sense of formal-conjectures. But $X$ is regular, so $\operatorname{Reg}(X) = X$, and $\pi$ is not an isomorphism over $X$: its fibre over $O$ is a projective line. Thus $\pi$ is not a resolution in our sense.

Our definition is the stronger one on purpose. A resolution should not change the regular part of $X$. Hironaka's theorem gives this property, and so does Theorem 1.2.5.

The statement of formal-conjectures also needs the perfect field. Let $k$ and $X = \operatorname{Spec} K$ be as in Example 1.1.7. Then $X$ is an integral variety over the imperfect field $k$. Let $f : Y \to X$ be proper and birational over $X$, with $Y$ integral. The function field of $Y$ is $K$, and $Y$ is proper over $K$, so $\dim Y = 0$ and $Y = \operatorname{Spec} K$. This is not smooth over $k$. Thus $X$ has no resolution in the sense of formal-conjectures, but $\mathrm{id}_X$ is a resolution in our sense. This is why formal-conjectures states the problem over perfect fields, and why our statement can use any field.

### The Lean proof

The Lean proof is in the file `base/SingularityBase/Bridge.lean`. It needs the base for one fact: over a perfect field, a scheme locally of finite type is smooth if and only if it is regular. The base proves this as `Scheme.smooth_iff_isRegular`.

```lean
lemma genericPoint_mem_regularLocus (X : Scheme.{u}) [IsIntegral X] :
    genericPoint X ∈ regularLocus X

lemma isReduced_of_isRegularScheme {Y : Scheme.{u}} (h : IsRegularScheme Y) : IsReduced Y

theorem hasResolution_of_isResolution {k : Type u} [Field k] [PerfectField k] {X Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) [IsIntegral X] [LocallyOfFiniteType sX] (π : Y ⟶ X)
    (h : IsResolution π) : Bridge.HasResolution sX

theorem fcResolutionCharZero : Bridge.FCResolutionCharZero
```

The first lemma is the first step of the proof. Mathlib knows that the stalk at the generic point of an integral scheme is a field (`isField_stalk_of_closure_mem_irreducibleComponents`), and the lemma `isRegularLocalRing_of_isField` of Section 1.1 does the rest.

The second lemma is the step "regular implies reduced". It uses the instance of the base that a regular local ring is a domain.

The theorem is Proposition 1.4.1. Mathlib states "birational over $X$" with a structure `Scheme.PartialIso`: a dense open set of the source, a dense open set of the target, and an isomorphism between them. The proof builds this structure from $\pi^{-1}(U)$, $U$ and the restriction of $\pi$, and checks that it is compatible with the maps to $X$ with `morphismRestrict_ι`. For irreducibility, it uses that the image of the irreducible space $\pi^{-1}(U)$ in $Y$ is irreducible and that its closure is $Y$.

The last theorem is Corollary 1.4.2. It applies Theorem 1.2.5 and the bridge, and it uses no hypothesis. Its axioms are the three standard axioms.

### Notes and references

The statement of formal-conjectures is in the file `FormalConjectures/Wikipedia/ResolutionOfSingularities.lean` of [FC]. It is in the part of [FC] whose statements come from articles of Wikipedia. For the equivalence of regular and smooth over a perfect field, see [Liu, Sections 4.2 and 4.3]. Example 1.4.3 is the standard example of a blowup with a regular centre, see [Har, Section I.4 and Section II.7].
