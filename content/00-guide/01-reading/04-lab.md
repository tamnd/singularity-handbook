---
title: How to rerun a computation
nodes: []
sources: [HP19a]
status: drafted
drafted_by: writer
reviewed_by: []
---
## How to rerun a computation

Some results of the handbook and of the research notes of the project come from computations. A computation gives examples and checks of examples. It does not prove a general statement. The directory `lab` of the map repository tamnd/singularity has the tools and the scripts of these computations. This section tells what the lab simulator computes, how it checks a certificate, and how a reader can run the computation of a research note again.

### The simulator

The simulator `lab/sim` is a small package in Python. It uses only the standard library of Python 3. It computes with polynomials over $\mathbb{F}_p$ and over $\mathbb{F}_{p^k}$, with exact arithmetic.

Its object is a point of a purely inseparable equation (Volume 7, Section 1.3). The data are a prime $p$, a power $q = p^e$, a polynomial $F$ in the variables $x_1, \dots, x_n$ and a set $E$ of indices, the divisor. The equation is $f = z^q + F$. The simulator computes these objects.

1. *The cleaning.* It removes from $F$ the monomials whose exponents are in $q\mathbb{N}^n$ (Volume 7, Definition 1.3.1). These monomials form $h^q$ for a polynomial $h$, and the change $z \mapsto z + h$ takes $z^q + F$ to $z^q + F^{\mathrm{cl}}$. The simulator gives $h$.
2. *The residual order.* It writes $F = \prod_{i \in E} x_i^{r_i} \cdot G$ with each $r_i$ as large as possible, and gives $r$, $G$ and $d = \operatorname{ord} G$ (Volume 7, Definition 1.3.3).
3. *A chart.* A point chart is the $x_j$-chart of the blowup of the origin, followed by translations $x_i \mapsto x_i + t_i$ with $t_i$ in the field and by the cleaning. A coordinate chart does the same for the blowup of a coordinate centre $V(z, x_i : i \in \Gamma)$. The new divisor is $\{j\}$ together with the $i \in E$ whose component passes through the new point. The simulator also tells whether the order of $f$ stays $q$.
4. *The invariants of the log-Jacobian ideal.* For $q = p$ it gives $\rho$ (Volume 7, Definition 3.1.3), the type $\tau = d - \rho$ (Definition 3.1.5), the order $\nu^G_Z$ along a coordinate stratum $Z$ (Definition 3.13.2), and the hypotheses (H1) and (H2) of research note 03. It can also change the free coordinate to $X = x + \lambda w + \gamma$ and clean in the new coordinates.
5. *Random walks.* From a seed it makes sequences of point charts with random translations. At each step it checks Theorems 3.7 and 3.12 and Corollaries 3.13 and 3.14 of research note 03, that is, $\rho \in \{d - 1, d\}$, $\rho$ does not go up, $d' \le d + 1$, and a kangaroo point is a change of type.

The invariant $\rho$ uses first derivatives, so it is the invariant of Volume 7 only for $q = p$. For $q = p^e$ with $e > 1$ the simulator gives $d$ and the charts. A walk uses only point centres and only the points that are rational over the field of the ring. So a walk is a sample of a family. It is not a search of the family.

The simulator has a test bank. Each test computes an example of the handbook or of a research note and compares the numbers with the text. Examples are the kangaroo point of Hauser, the cycle of Hauser and Perlega [HP19a], and Examples 3.13.21, 3.14.9 and 3.15.18 of Volume 7. The workflow `lab` of the map repository runs the test bank at each change of the lab.

### How a certificate is checked

A certificate is a file in JSON that records a finite sequence of charts. It has $p$, $k$, $q$, the names of the variables, the start polynomial $F_0$ and the start divisor $E_0$. For each step $m = 1, 2, \dots$ it records the chart (point or coordinate, the index $j$, the translations $t$ and, for a coordinate chart, the centre), the cleaning $h_m$, the result $F_m$, the divisor $E_m$, the residual order $d_m$ and a witness: the exponent $\alpha_m$ of a monomial of $G_m$ with $|\alpha_m| = d_m$.

The checker reads the certificate and computes each step again from $F_{m-1}$ and $E_{m-1}$. It accepts the certificate if and only if at each step these conditions hold.

1. The computed cleaning is $h_m$, and the computed transform is $F_m$.
2. The computed divisor is $E_m$.
3. The order of the transform of $f$ is still $q$.
4. The computed residual order is $d_m$.
5. The monomial $x^{\alpha_m}$ has a nonzero coefficient in $G_m$, and $|\alpha_m| = d_m$.

All arithmetic is exact, so the check is a finite computation. Condition 5 lets a reader see the bound $\operatorname{ord} G_m \le d_m$ from a single monomial. Condition 4 gives the equality. The map repository has two certificates: the kangaroo point of Hauser for $p = 2$, and the first six steps of the cycle of Hauser and Perlega for $p = 2$ and $q = 8$.

```sh
cd lab/sim
python3 -m labsim check certificates/kangaroo-p2.json
python3 -m labsim step -p 2 -vars x,y -f "x^3*y + x*y^3" -divisor x,y -chart x -t y=1
```

The first command prints `ok`. The second command prints the invariants before and after the chart. For $F = x^3 y + x y^3$ and $E = \{x, y\}$ it gives $d = 2$ and $\rho = 2$. After the $x$-chart with $t_y = 1$ the cleaning is $h = xy$, the new polynomial is $x^2 y^3$, the new divisor is $\{x\}$, and $d' = 3$, $\rho' = 2$. The residual order goes up from $2$ to $3$, so this is a kangaroo point, and the type goes from $0$ to $1$.

### The scripts of the research notes

The research notes mark each result with a tag. The tag [C] means numerical evidence only. A claim with this tag rests on a computation, and the scripts of that computation are in `lab/notes/NN/` of the map repository, where NN is the number of the note. Each folder has a file `README.md`. It names the claims of the note that the scripts support, gives the commands, the expected output and the run time, and lists the dependencies. Most scripts use only the standard library of Python 3. A few use sympy or galois, and the file `README.md` of the folder says so.

To rerun the computation of a note, do these steps.

1. Clone tamnd/singularity and read `lab/notes/NN/README.md`.
2. Run the command of the claim from the root of the clone, for example `python3 lab/notes/NN/<script>.py`. The scripts find their data and their helper modules by paths relative to their own file, so the current directory does not matter.
3. Compare the output with the section "Expected output" of the file `README.md` and with the numbers of the note. A random search has a fixed seed, in its command or in its code, so a run with the same seed gives the same output.

The workflow `lab` also runs the scripts that take less than 30 seconds, and it compares their output with the expected lines. The long searches are not in the workflow. Their file `README.md` gives the run time on one machine and, where possible, a short form of the command for a quick check.

A computation over a finite field, along finite words and with a budget, can find a counterexample, but it cannot prove that there is none. So a [C] claim stays a claim of the note. It enters the map only as a node of kind example, counterexample or conjecture.
