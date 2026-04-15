---
section: project
---
# Tasks

- [x] Improve abstract
- [x] Add a more quantitative view of the constant eDOS mismatch
- [ ] Find effective masses for X & L points
	- [ ] understand the Drude subtraction thing
	- [ ] find reliable sources
	- [ ] extract fit params
- [ ] Understand CEDs topologies
	- [ ] Rederive absorption integrals based on CEDs
- [ ] Calculate absorption & compare to Rosei
- [ ] Once absorption matches Rosei's calculate interband emission
	- [ ] equilibrium
	- [ ] non-equilibrium

# Log

## Progress
- Reviewed relevant publications and studied the theoretical and mathematical foundations, including the advisor's previous works.
- Recreated past emission results for intraband emission in both equilibrium (blackbody) and non-equilibrium settings in energy space.
- Settled on a convergent numerical scheme for calculating emission integrals. ([3.1](3.1%20-%20Numeric%20Convergence.md))
- Established the approximate nature of the analytic expressions for intraband emission (thermal and non-equilibrium). ([3.2](3.2%20-%20Analytic%20Approximations.md))
	- Outlined their regions of validity.
	- Found an exact analytic expression for thermal intraband with constant eDOS.
- Quantified the discrepancy between constant eDOS and energy-dependent eDOS. ([3.3](3.3%20-%20Constant%20eDOS%20Approximation.md))
- Understood the new challenges involved in interband transitions compared to intraband (anisotropy requiring k-space treatment).
- Performed k-space calculations and compared with energy-space results.
- Recognized the difficulty and inefficiency of working in k-space and approximating the delta function numerically. ([A5](A5%20-%20Numeric%20Delta%20Approximation.md))
- Found the proper transformations to energy space, valid even for non-isotropic dispersion relations. ([A7](A7%20-%20Intraband%20Transitions%20(Rosei).md), [A8](A8%20-%20Interband%20Transitions%20(Rosei).md))

## Misconceptions
- Thought anisotropy necessarily requires k-space treatment. In practice, for a quadratic band approximation, a careful variable change into 1D energy space is feasible.

## Lingering Questions
- Absorption and emission occur only at the skin depth, but the statistical treatment counting emitters over the particle's entire volume is used to go from a single emitter to the continuum. Isn't it more appropriate to calculate specific emission?
- Are we calculating electronic transitions in bulk metals (where phonon-electron interaction is needed for momentum conservation), or in nanoparticles (where wave-function confinement and momentum spreading open a first-order transition — Landau damping)?
- When testing theoretical predictions against experiment, how should the photonic DOS (generally not that of vacuum in experimental settings) be accounted for, both qualitatively and quantitatively?
- **For Yonatan:** Moving to interband transitions, are we still assuming that any energy-conserving transition is allowed — i.e., are $k_i$ and $k_f$ permitted to differ when an electron recombines into the valence band?


# Review and add to Tasks if relevant

- [ ] Fully realize the criteria for the delta-function approximation in k-space calculations.
- [ ] Compare Novotny's and Farhan's derivations of transition rates and create a cohesive, comprehensive derivation.
	- Novotny's advantage — spontaneous decay, but two-level.
	- Farhan's advantage — Bloch electrons (continuous metal), but stimulated.
- [ ] Compare energy (const eDOS), energy (varying eDOS), and momentum-space cases for intraband transitions that do not conserve momentum.
- [ ] Try to simplify band anisotropy with a change of variables (COV).
	- [ ] Begin with intraband transitions (as per Rosei) for anisotropic band via COV, transitioning to energy space.
	- [ ] Once results are consistent with the isotropic case, proceed to interband transitions.
- [ ] Compute the 1D case of two isotropic bands (semiconductor-like, with Fermi energy inside the conduction band).
- [ ] Focus on lower emission energies.
- [ ] Reproduce Rosei's **absorption** calculation.
- [ ] Calculate **intraband emission** using Rosei's bands and compare to the free electron (parabolic band) approximation.
- [ ] Calculate **interband emission** using Rosei's bands and compare to absorption — in thermal equilibrium, emission = absorption × Planck (Kirchhoff).
- [ ] Extend both interband and intraband calculations to non-equilibrium electronic distributions (steady-states & pulsed).
- [ ] At every step, compare against experimental results where available.


# Points for Consideration

- In Yonatan's paper, the density of states is taken as constant even in energy space: $\rho(\mathcal{E}) \to \rho(\mathcal{E}_\text{F})$. This approximation holds only near the Fermi energy and is used to obtain an analytic solution.
- The most drastic assumption is momentum non-conservation (every transition equally probable). Without it, intraband emission is forbidden and a two-step process involving phonons must be considered. For interband transitions this is more tractable, since direct transitions are one-step processes.
- In numeric calculations, remember to include the photonic contribution for the full emission spectrum.
- **Conservation of crystal momentum:** Does it matter when integrating over the first Brillouin Zone?