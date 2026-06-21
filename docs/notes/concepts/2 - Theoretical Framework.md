---
section: thesis
---
In certain (which?) cases we can represent emission and absorption of light by a substance as having a decoupled photonic and electronic contribution 
$$
\begin{align} \Gamma(\hbar\omega) &= \Gamma_{\text{ph}}(\hbar\omega)\cdot \Gamma_{\text{e}}(\hbar\omega) \end{align}
$$
which roughly relate to its geometric (extrinsic) and material (intrinsic) characteristic respectively. [^3] The electronic contribution can be further divided into intraband and interband contributions
$$
\Gamma_{e}(\hbar \omega) = \Gamma_{e}^{\text{cc}}(\hbar \omega) + \Gamma_{e}^{\text{cv}}(\hbar \omega)
$$
The latter can once again be shown as consisting (in the specific case of gold) of two distinct contributions from different regions of the Brillouin zone

$$
\Gamma_{e}(\hbar\omega) = 6\Gamma_{e}^{X}(\hbar\omega)+8\Gamma_{e}^{L}(\hbar\omega)
$$
___


The emission of electromagnetic radiation from a material body is governed by the intricate coupling between the body's optical environment and its intrinsic material properties. We are using Fermi's golden rule to calculate transition rates (and consequently the emission[^1]) enables us to decouple the photonic aspect of emission from the electronic part roughly as follows

$$\begin{align} \Gamma(\hbar\omega) &= \Gamma_{\text{ph}}(\hbar\omega)\cdot \Gamma_{\text{e}}(\hbar\omega) \end{align}$$

The photonic part is characterized by the Local Density of States (LDOS), which encapsulates the geometry and antenna properties of the structure. The electronic contribution, which is the focus of this study, describes the material's intrinsic response.

The electronic transitions of interest are the intraband transitions inside the conduction band $\Gamma_{\text{cc}}$ and the interband transition between the valence and the conduction band $\Gamma_{\text{cv}}$. Their sum represent their shared contribution to the electronic aspect of emission

$$
\Gamma_{e}(\hbar \omega) = \Gamma_{e}^{\text{cc}}(\hbar \omega) + \Gamma_{e}^{\text{cv}}(\hbar \omega)
$$

Our material of choice for this work is gold for which an approximate dispersion relation exists for both bands [Rosei](../../../resources/main/7%20-%20Rosei.pdf). Those approximations hold near the X and L points in Gold's Brillouin zone which has 6 and 8 such facets respectively. So a total account of the electronic part should be

$$
\Gamma_{e}(\hbar\omega) = 6\Gamma_{e}^{X}(\hbar\omega)+8\Gamma_{e}^{L}(\hbar\omega)
$$

==We focus on the high-symmetry **X** and **L** points in the Brillouin zone, which account for the majority of the interband density of states (why is that statement true).==

[^1]: A more rigorous treatment (other than FGR) would be required for unusually strong field strengths since we're dealing with metals which have very short coherence times.

[^2]: 

[^3]: The photonic part is characterized by the Local Density of States (LDOS), which encapsulates the geometry and antenna properties of the structure. The electronic contribution, which is the focus of this study, describes the material's intrinsic response.
