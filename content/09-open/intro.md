# Introduction

This volume is the research report of the project. It is released at each milestone, and it grows with the project. It states each result that the project has proved in Lean, gives a complete proof in the language of algebraic geometry, and then explains how the Lean proof follows that argument.

The reader we have in mind is a graduate student who knows the first chapters of a book on schemes, such as Hartshorne [Har] or Liu [Liu], and the commutative algebra of Atiyah and Macdonald [AM69]. We do not assume that the reader knows Lean. The Lean parts of each section are short, and the reader can skip them.

Each result has a `Node:` line. The line gives the tag of the result on the map of the project and the name of its Lean declaration. The site gives the current status of each node. A result that depends on a hypothesis that is not yet proved says so in its statement, and the map gives it the status "proved-mod". We never write that a result is proved when its proof uses a hypothesis.

The open problem of this volume is $\mathrm{Res}(p, 4)$: each variety of dimension 4 over a field of characteristic $p > 0$ has a resolution. It is not proved. Chapter 1 gives the cases that the project has proved so far, and the reductions that connect them to the open problem. Chapter 2 gives the cases that mathematicians have proved in dimension at most 3, the reasons why the proofs of characteristic 0 fail in characteristic $p$, and the main routes to dimension 4.
