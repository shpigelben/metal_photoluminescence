# Extraction of Effective Masses for Gold (Au) from Literature

To calculate the photoluminescence and absorption of gold using the Rosei model, we require precise parameters for the electronic bands near the **X** and **L** symmetry points. This document outlines how these parameters are extracted from the foundational literature.

## 1. Primary Sources
The parameters are derived from two core papers:
1.  **Christensen and Seraphin (1971)** (*Phys. Rev. B* 4, 3321): Provides the first-principles **relativistic band structure** and energy gaps.
2.  **Guerrisi, Rosei, and Winsemius (1975)** (*Phys. Rev. B* 12, 557): Provides the **analytic model** (parabolic band approximation) and the specific fit parameters used to match the experimental dielectric function of gold.

## 2. Locating the Data
### Energy Gaps ($E_g$)
In **Christensen and Seraphin (1971)**, **Table III (page 3332)** lists the energy separations at critical points. 
- **L-point transition ($L_3 \to L_2'$)**: The calculated value is **2.10 eV** (experimental fit is **2.45 eV**).
- **X-point transition ($X_5 \to X_4'$)**: The calculated value is **2.58 eV** (experimental fit is **1.94 eV**).

*Note: The Rosei model uses the experimental thresholds (1.94 eV and 2.45 eV) as these account for the Fermi level position and the complex thermomodulation peaks.*

### Effective Masses ($m^*$)
The effective masses are extracted by calculating the **curvature** of the bands in the **Relativistic Band Structure (Figure 5, page 3330)** of C&S (1971). 

![Figure 5: Relativistic Band Structure (Christensen & Seraphin 1971)](../../4 Misc/Attachments/CS1971_Figure5.png)

The curvature is highly anisotropic at both points. While simplified 1D models often collapse these into single "effective" masses, the physically accurate 3D model requires both Longitudinal ($\parallel$) and Transverse ($\perp$) components.

## 3. Calculation Methodology
To transform the 3D band structure into the 1D energy-space integral used in the appendices, we use the following relationship for a parabolic band:
$$\mathcal{E}(k) = \mathcal{E}_0 + \frac{\hbar^2 k^2}{2m^*} = \mathcal{E}_0 + \alpha k^2$$
Where $\alpha$ (in $eV \cdot \text{\AA}^2$) is:
$$\alpha = \frac{\hbar^2}{2m_e} \frac{m_e}{m^*} \approx \frac{3.81}{m^*/m_e}$$

## 4. Parameter Table (The "Full Relativistic" Set)
The following table summarizes the exact anisotropic parameters from **Christensen and Seraphin (1971)**. These should be used for the derivations in Appendix **A8**.

| Critical Point | Band | Direction | $m^*/m_e$ | Curvature Coefficient ($\alpha$) |
| :--- | :--- | :--- | :--- | :--- |
| **L Point** | Conduction ($sp$) | Longitudinal ($\parallel$) | **0.12** | 8.33 |
| | Conduction ($sp$) | Transverse ($\perp$) | **0.24** | 4.17 |
| | Valence ($d$) | Longitudinal ($\parallel$) | **-1.03** | -0.97 |
| | Valence ($d$) | Transverse ($\perp$) | **-0.70** | -1.43 |
| **X Point** | Conduction ($sp$) | Longitudinal ($\parallel$) | **-0.40** (Saddle) | -2.50 |
| | Conduction ($sp$) | Transverse ($\perp$) | **0.31** | 3.23 |
| | Valence ($d$) | Longitudinal ($\parallel$) | **-0.15** | -6.67 |
| | Valence ($d$) | Transverse ($\perp$) | **-0.19** | -5.26 |

*Note: Dimensionless coefficients used in scripts (relative to energy scale $C \approx 9.03$ eV) are equal to $1 / (m^*/m_e)$.*

## 5. Why use Theoretical C&S Values over Experimental J&C?
Experimental data like **Johnson & Christy (1972)** provide the *total* dielectric function $\epsilon(\omega)$. However, they lack **k-space resolution**.

1.  **Symmetry Specificity:** To isolate the L-point and X-point contributions (which have different topological effects on the Joint Density of States), you **must** use masses that exist at those specific coordinates.
2.  **Mechanism Identification:** C&S (1971) identifies the specific sub-bands ($L_6^+, X_7^-$, etc.) responsible for the optical features. J&C only shows that *something* happens at 2.45 eV; C&S explains *what* and *where* it is.
3.  **Anisotropy:** Optical experiments cannot easily distinguish between longitudinal and transverse curvatures. Only the relativistic theory (or ARPES) provides the directional parameters needed for your 3D-to-1D transformations.
