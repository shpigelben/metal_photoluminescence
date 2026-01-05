# A2 - Interband Transitions and Joint Density of States

For interband transitions, the general emission integral derived in [A0](A0%20-%20Derivation%20of%20the%20General%20Emission%20Integral.md) can be significantly simplified by invoking the **k-selection rule** (momentum conservation).

## 1. Momentum Conservation (k-selection)

In a direct transition between a valence band ($v$) and a conduction band ($c$), the momentum of the involved photon $\mathbf{q}$ is negligible compared to the electron wave-vector $\mathbf{k}$ ($\mathbf{q} \approx 0$). This imposes a vertical transition requirement in the Brillouin Zone:
$$ \mathbf{k}_c = \mathbf{k}_v \equiv \mathbf{k} $$
The transition dipole moment $\mu^{cv}$ thus becomes diagonal in k-space, represented by a delta function $\delta(\mathbf{k}_1 - \mathbf{k}_2)$. Inserting this into the general expression:
$$ \Gamma(\hbar\omega) \propto \iint\limits_{\text{BZ}} |\mu^{cv}(\mathbf{k}_1, \mathbf{k}_2)|^2 f_c(\mathbf{k}_1)\overline{f_v(\mathbf{k}_2)} \delta(\mathcal{E}_c(\mathbf{k}_1) - \mathcal{E}_v(\mathbf{k}_2) - \hbar\omega) \delta(\mathbf{k}_1 - \mathbf{k}_2) d^3k_1 d^3k_2 $$
Resolving the $d^3k_2$ integral yields:
$$ \Gamma(\hbar\omega) = \frac{2\pi}{\hbar} \left( \frac{2V}{(2\pi)^3} \right) \int\limits_{\text{BZ}} |\mu^{cv}(\mathbf{k})|^2 f_c(\mathbf{k})\overline{f_v(\mathbf{k})} \delta(\mathcal{E}_c(\mathbf{k}) - \mathcal{E}_v(\mathbf{k}) - \hbar\omega) d^3k $$

## 2. Joint Density of States (JDOS)

The term $\mathcal{E}_{cv}(\mathbf{k}) = \mathcal{E}_c(\mathbf{k}) - \mathcal{E}_v(\mathbf{k})$ defines the **interband transition energy**. To convert the k-space integral into an energy-space integral, we introduce the Joint Density of States, $\rho_J(\mathcal{E})$:
$$ \rho_J(\mathcal{E}) = \frac{2}{(2\pi)^3} \int\limits_{\text{BZ}} \delta(\mathcal{E}_{cv}(\mathbf{k}) - \mathcal{E}) d^3k $$
In the case where the matrix element $|\mu^{cv}|^2$ and the occupations $f$ vary slowly compared to the delta function, we can express the emission rate as:
$$ \Gamma(\hbar\omega) \propto |\mu^{cv}|^2 \cdot \text{Occupancy Factor} \cdot \rho_J(\hbar\omega) $$

### 2.1 Analytic JDOS for Parabolic Bands
Assuming isotropic parabolic bands:
$$ \mathcal{E}_c(\mathbf{k}) = \mathcal{E}_g + \frac{\hbar^2k^2}{2m_c}, \quad \mathcal{E}_v(\mathbf{k}) = -\frac{\hbar^2k^2}{2m_v} $$
The transition energy is:
$$ \mathcal{E}_{cv}(\mathbf{k}) = \mathcal{E}_g + \frac{\hbar^2k^2}{2\mu_r} $$
where $\mu_r = (m_c^{-1} + m_v^{-1})^{-1}$ is the reduced mass. The JDOS then takes the familiar square-root form:
$$ \rho_J(\mathcal{E}) = \frac{1}{2\pi^2} \left( \frac{2\mu_r}{\hbar^2} \right)^{3/2} \sqrt{\mathcal{E} - \mathcal{E}_g} $$

## 3. The Van Roosbroeck-Shockley Relation

In equilibrium, the emission rate $R(\hbar\omega)$ and the absorption coefficient $\alpha(\hbar\omega)$ are related by the principle of detailed balance. For a semiconductor (or interband transitions in metals), this is the Van Roosbroeck-Shockley relation:
$$ R(\hbar\omega) = \frac{n^2 (\hbar\omega)^2}{\pi^2 c^2 \hbar^3} \alpha(\hbar\omega) \frac{1}{\exp(\hbar\omega/k_BT) - 1} $$
This provides a critical consistency check for our numerical interband model: the equilibrium emission spectrum must match the product of the absorption spectrum and the blackbody photon density.

## 4. Application to Gold

For Gold, the interband transitions are primarily around the **L** and **X** points of the Brillouin Zone. Unlike the isotropic model above, these require:
1.  **Anisotropic Masses:** Using longitudinal and transverse effective masses ($m_\parallel, m_\perp$).
2.  **Band Offsets:** Correctly placing the $d$-bands relative to the Fermi level.
3.  **Non-Equilibrium:** Using $f_{neq}(\mathbf{k})$ instead of $f^T(\mathcal{E})$ inside the integral, which breaks the simple JDOS proportionality if the distribution is highly non-spherical.
