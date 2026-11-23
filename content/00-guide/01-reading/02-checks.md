---
title: How to check a claim
nodes: []
sources: []
status: drafted
drafted_by: writer
reviewed_by: []
---
## How to check a claim

Each theorem of the handbook has a line under its statement, of this form.

```text
Node: SG0000000A · Lean: Singularity.Fidelity.isResolution_id (status: proved)
```

The node is an entry of the map of the project. The map is in the repository tamnd/singularity, and each node has a page on singularity.tamnd.com. The Lean name is the declaration in tamnd/singularity-lean that states or proves the result. The status comes from the Lean build at the date of the edition. A person does not write it.

The status has one of these values.

| Status | Meaning |
|---|---|
| planned | the Lean statement does not exist yet |
| stated | the Lean statement builds, and there is no complete proof |
| defined | a definition that builds |
| proved | the Lean proof builds with the standard axioms only, and each node that it uses is proved |
| proved-mod | the Lean proof takes other nodes as hypotheses |
| open | an open problem |
| refuted | the negation is proved in Lean |

A Lean proof shows that the Lean statement is true. It does not show that the Lean statement means what the text says. For the statements of the problem, the project runs a set of fidelity checks, and Chapter 2 describes them. For the other results, the reader must compare the Lean statement with the text. The site shows the Lean statement on the page of each node.

A chapter has the mark "draft" until a person with the right background has read it. The text of a draft can have errors. Please report them as issues of tamnd/singularity-handbook.
