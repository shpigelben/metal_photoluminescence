# Progress Report
 - Settled on a convergent numerical scheme for the calculation of the emission integral. ([3.1](../3%20-%20Intraband%20Transitions/3.1%20-%20Numeric%20Convergence.md)) 
 - Established approximate nature of the analytic expressions for intraband emission (thermal and non-equilibrium). ([3.2](../3%20-%20Intraband%20Transitions/3.2%20-%20Analytic%20Approximations.md))
	 - Outlined its region of validity. 
	 - Found an exact analytic expression for thermal intraband with constant eDOS.
 - Quantified the discrepancy between constant eDOS and energy-dependent eDOS. ([3.3](../../../figures/constant_eDOS_approximation.png))
 - Recognized the difficulty and inefficiency of working in k-space and having to approximate the delta function numerically ([A5](../A%20-%20Appendices/A5%20-%20Numeric%20Delta%20Approximation.md))
 - Found the proper transformations that take us to energy space, even with non-isotropic dispersion relations ([A7](../A%20-%20Appendices/A7%20-%20Quadratic%20Intraband%20Transitions.md), [A8](../A%20-%20Appendices/A8%20-%20Quadratic%20Interband%20Transitions.md))

# Tasks

- [x]  Improve abstract
- [x] add a more quantitative view of the constant eDOS mismatch
- [ ] Focus on lower emission energies.
- [ ] Reproduce Rossei's absorption calculation
- [ ] Calculate intraband emission using Rossei's bands and compare the free electron approximation (parabolic band)
- [ ] Calculate interband emission using Rossei's bands and compare to absorption - in thermal eq emission = absorption\* plank (Kirchhoff).
- [ ] ?



# Questions
- Absorption and emission happen only at skin-depth. The statistical transition from a single emitter to continuum includes counting emitters in the particle's entire volume. Isn't it more appropriate to calculate specific emission?
- We're either calculating electronic transitions in bulk metals in which case we have to account for phonon-electron interaction for momentum conservation to hold.
- Or we're calculating electronic transitions in nano-particles in which a first order transition is opened due to the confinement of the wave-function in space and the spreading of momentum. (Landau damping)
- In testing theoretical predictions against experimental evidence, shouldn't the photonic DOS 
- In experimental settings I imagine LDOPS (which are generally not that of vacuum?) affect the emission spectrum both qualitatively and quantitatively - how do we address this when drawing comparisons?
