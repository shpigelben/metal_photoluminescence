The emission of electromagnetic radiation from a material body is governed by the intricate coupling between the body's optical environment and its intrinsic material properties. In this work we calculate the emission from metallic structures and under weak relatively weak illumination. Emission rate is therefore calculated using Fermi's golden rule which allows us to decouple the photonic and electronic contributions
$$
\Gamma(\hbar\omega) = \frac{2\pi}{\hbar}   \mu
$$
$$\begin{align} \Gamma(\hbar\omega) &= \Gamma_{\text{ph}}(\hbar\omega)\cdot \Gamma_{\text{e}}(\hbar\omega) \end{align}$$

The photonic part is characterized by the Local Density of States (LDOS), which encapsulates the geometry and antenna properties of the structure. The electronic contribution, which is the focus of this study, describes the material's intrinsic response.

## Electronic Transitions in Metals
The electronic rate $\Gamma(\hbar\omega)$, measured in transitions per second ($s^{-1}$), arises from spontaneous decay processes where an electron transitions from a high-energy state to a lower one. In metals like gold, these transitions are categorized into two distinct types:

1. **Intraband transitions ($\Gamma_{\text{cc}}$):** Occurring within the conduction band, necessarily assisted by phonons or defects.
2. **Interband transitions ($\Gamma_{\text{cv}}$):** Occurring between distinct bands, typically from the conduction band down to the valence band.
    

Thus, the total electronic rate is:
$$\Gamma_{\text{e}} = \Gamma_{e}^{\text{cc}} + \Gamma_{e}^{\text{cv}}$$

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

$$\boxed{ \rho_q(\mathcal{E}) = \left( \frac{4\pi m_{c\perp} \sqrt{2m_{c\parallel}}}{\hbar^3} \right) \Bigg[ \sqrt{\mathcal{E}_{\perp}^{max} - \mathcal{E}} \; - \; \sqrt{\max(0, \mathcal{E}) - \mathcal{E}} \Bigg] }$$