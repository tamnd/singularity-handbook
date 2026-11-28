# Inseparable local uniformization

Temkin proved that each valuation of a function field has local uniformization after a finite purely inseparable extension of the function field [Tem13]. The theorem holds in each characteristic and in each dimension. In characteristic 0 it is the theorem of Zariski. In characteristic $p$ it is the strongest known result on local uniformization in dimension at least 4, and it is the starting point of route R2 of Volume 9, Chapter 2.

Section 4.1 states the theorem in the form of [Tem13], shows that it implies the Lean statement `Singularity.localUniformization_inseparable`, and describes the structure of the proof. Section 4.2 explains why the theorem does not give local uniformization of the valuation itself, with an example from Volume 4, and it connects the remaining problem with the conjectures of Volume 9, Section 2.3. Section 4.3 proves, over a perfect ground field, that the theorem of Temkin reduces local uniformization to one purely inseparable step of degree $p$. It proves this step when the equation of the step is monomial modulo $p$-th powers, and it states the missing input, weak log monomialization along a valuation, as a hypothesis that it does not prove.

We do not prove the theorem of Temkin. The proofs in this chapter deduce consequences from it.
