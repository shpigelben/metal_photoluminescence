- Total emission
	- usage of FGR and the valid field strengths.
	- photonic & electronic parts (when are they separable?).
	- ==focusing on bulk metals (photonic DOS is that of free space WHY? maybe electrons are free, photons inside metals will immediately get absorbed and reemitted)==
		- photonic modes propagate outside the metal, so the approximation holds but this leads to a different issue - absorption and emission happen only in skin-depth. When counting states in the transition from a single localized emitter to a bulk continuous metal we are summing over all of the metal's size. This shouldn't be the case. Instead we should compute an intrinsic specific emission (per unit volume).
		- Does the fact this happen only near the metal surface somehow modify the Bloch states due to surface effects?
___
### Introduction
The emission of electromagnetic radiation from a material body is governed by the intricate coupling between the body's optical environment and its intrinsic material properties. 


As described by Novotny, this interaction allows us to conceptually and mathematically decouple the emission spectrum into separate photonic and electronic contributions:

$$\begin{align} I(\hbar\omega) &= I_{\text{ph}}(\hbar\omega)\cdot I_{\text{e}}(\hbar\omega) \end{align}$$

The photonic part is characterized by the Local Density of States (LDOS), which encapsulates the geometry and antenna properties of the structure. The electronic contribution, which is the focus of this study, describes the intrinsic response of the material itself. This separability is rigorously justified in the weak coupling regime by Fermi's Golden Rule, which treats the electronic transition probability and the photonic mode density as independent factors. Consequently, the spectral intensity of emission $I(\hbar\omega)$—physically representing the power radiated per unit energy interval (typically measured in $\text{W}\cdot\text{eV}^{-1}$)—is directly proportional to the product of the photon energy $\hbar\omega$ and the total electronic transition rate $\Gamma(\hbar\omega)$.

**Electronic Transitions in Metals**

The electronic rate $\Gamma(\hbar\omega)$, measured in transitions per second ($s^{-1}$), arises from spontaneous decay processes where an electron transitions from a high-energy state to a lower one. In metals like gold, these transitions are categorized into two distinct types:

1. **Intraband transitions ($\Gamma_{\text{cc}}$):** Occurring within the conduction band, necessarily assisted by phonons or defects.
    
2. **Interband transitions ($\Gamma_{\text{cv}}$):** Occurring between distinct bands, typically from the conduction band down to the valence band.
    

Thus, the total electronic rate is:

$$\Gamma_{\text{e}} = \Gamma_{\text{cc}} + \Gamma_{\text{cv}}$$

In a state of thermal equilibrium, the emission spectrum of gold is overwhelmingly dominated by intraband transitions. This is because the valence band is fully occupied, effectively blocking interband decay paths and rendering their contribution negligible.

**The Non-Equilibrium Hypothesis**
This equilibrium assumption, however, breaks down under external illumination. In non-equilibrium scenarios—such as a metal driven to a steady state by monochromatic radiation—incoming photons can excite electrons out of the valence band. We posit that this process generates a significant population of holes in the valence band, opening new channels for radiative decay. This non-equilibrium hole population allows interband transitions ($\Gamma_{\text{cv}}$) to become a prominent feature of the emission spectrum, potentially rivaling or exceeding the thermal intraband background.

### Methodology: The Rotational Saddle-Point Approximation
Modeling this contribution presents a specific methodological challenge regarding the band structure. Previous derivations of non-equilibrium electronic distributions [Sivan & Dubi](../../../resources/1%20-%20theory-of-hot-photoluminescence-from-drude-metals.pdf) focused on intraband transitions, exploiting the approximate isotropy of the conduction band to simplify calculations in energy space. The valence band, in contrast, is highly anisotropic, meaning simple isotropic approximations fail to capture the physics of interband transitions.

To address this without resorting to computationally prohibitive full-band integration, we adopt the **Rotational Saddle-Point Approximation**, based on the model developed by Guerrisi, Rosei, and Winsemius. We focus on the high-symmetry **X** and **L** points in the Brillouin zone, which account for the majority of the interband density of states.

For transitions near the X point (specifically band 5 to band 6), we model the dispersion relations not as simple parabolas, but as rotational quadratic surfaces. The upper band is treated geometrically as a hyperbolic paraboloid (a saddle shape) while the lower band is modeled as an elliptic paraboloid . This specific topology is critical because it yields a step-like singularity in the Joint Density of States (JDOS), a physical feature distinct from the inverse square-root singularity predicted by isotropic models. This approach allows us to accurately calculate the spectral transition rate $\Gamma(\hbar\omega)$ in energy space while retaining the necessary rigor regarding the band structure's anisotropy.

**Research Objectives**

Our goal is to provide a comprehensive emission spectrum that accounts for these previously neglected contributions. We approximate the total interband contribution by summing the transitions from these high-symmetry valleys, weighted by their multiplicity in the first Brillouin zone (6 for X, 8 for L).

The overall electronic contribution to the emission is therefore modeled as:

$$\Gamma = \Gamma_{\text{cc}} + 6\Gamma_{\text{cv}}^{\text{X}} + 8\Gamma_{\text{cv}}^{\text{L}}$$



