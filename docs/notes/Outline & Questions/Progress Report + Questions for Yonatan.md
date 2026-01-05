## Things accomplished in the project

- learning the theory, math involved and reviewing relevant publications (including advisor's previous works).
- understanding the new challenges involved in calculating interband transitions as opposed to intraband transitions (namely - working in k-space due to anisotropy of the bands).
- recreating past emission results for intraband emission both in equilibrium (BB) and in non-equilibrium settings in energy space.
- performing similar calculations, now in k - space and comparing results.
- realizing error in approach and understanding the need to make an approximation for the delta function (energy conservation).
- understanding when both numerical and analytical approximations converge to desired relative error.
# Things to be accomplished in the project

- need to fully realize the criteria for the conversion of delta-function approximation when performing k-space calculations.
- when the above is met, continue to performing the desired interband calculations - these, under non-equilibrium conditions will be constitute new (and hopefully interesting) contributions.

# Questions for Yonatan

As I work on updating the shared Overleaf file I would appreciate a clarification regarding the conservation of momentum in electronic transitions. I've relentlessly asked you about the lack of momentum conservation in the FGR calculation for intraband transitions. As far as I can recall we have not reached a mutual understanding, but established that the results of this calculations go hand in hand with experimental data. Moving to interband transition, are we still going to assume that any energy conserving transition is allowed? Namely, are $k_{i}$ and $k_{f}$ allowed to be different when an electron recombines into the valence band?


## Queue

- [ ] Compare Novotny's and Farhan's derivations of transition rates
	- [ ] create a cohesive and comprehensive derivation that fits the bill.
		- Novotny's advantage - spontaneous decay, but two level.
		- Farhan's advantage - Bloch electrons (continuous metal), but stimulated. 
- [ ] Comparing energy (const eDOS), energy (varying eDOS) and momentum cases for intraband transitions that do not conserve momentum.
- [ ] Trying to compute the 1D case of two isotropic bands (like in semiconductors, but with the Fermi energy "sitting inside" the conduction band).
- [ ] Try to simplify anisotropy with a change of variables (COV).
	- [ ] Maybe begin with intraband transitions (as per Rosei) for anisotropic band going through COV and transitioning to energy space.
	- [ ] Once the calculation establishes number close to isotropic band, proceed to computing interband transitions.

## Points for Consideration

- In Yonatan's paper they consider the density of states to be a constant of integration even in energy space, namely $\rho(\mathcal{E})\to \rho(\mathcal{E}_{\text{F}})$. This is an approximation that holds only for energies close to Fermi energy and is used to achieve an analytic solution.
- The worst assumption, of course is that of momentum not being conserved which leads to every transition being equally probable. Without this assumption though, intraband emission is impossible and a two step process (involving phonons) has to be considered.
	- For interband transitions this is more easily resolved since direct transitions can occur as a one step process.
- In numeric calculations - remember to add the photonic contribution for the full emission spectrum.
- **Conservation of Crystal momentum!** Does it matter when integrating over the first Brilluin Zone?

