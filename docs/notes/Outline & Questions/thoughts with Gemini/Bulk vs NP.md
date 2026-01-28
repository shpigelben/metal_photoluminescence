## 1. EXECUTIVE SUMMARY: THE CORE THESIS

**Objective:**

To develop a computationally rigorous model for the photoluminescence (PL) of Gold (Au) nanostructures under continuous-wave (CW) laser excitation. The model must explicitly decouple the quantum mechanical material response (Electronic) from the electrodynamic environment (Photonic).

**The Central Problem:**

Standard thermal emission models rely on Kirchhoff’s Law ($\text{Emission} = \text{Absorptivity} \times \text{Blackbody}$), which presumes thermodynamic equilibrium ($T_{\text{electron}} = T_{\text{lattice}} = T_{\text{photon}}$).

Under laser excitation, the electron distribution becomes **Non-Thermal** ($f(E) \neq f_{\text{Fermi}}(T)$). Consequently, standard macroscopic models (Drude-Lorentz) fail to predict:

1. The specific spectral features of interband transitions (X and L points).
    
2. The quantum efficiency of emission in the absence of thermal equilibrium.
    

**The Solution Architecture:**

We adopt a **Hybrid Semi-Classical Formalism** operating in the **Weak Coupling Regime**:

$$\Gamma(\omega) = \underbrace{\mathcal{I}_{\text{electronic}}(\omega)}_{\text{Material}} \times \underbrace{\mathcal{I}_{\text{photonic}}(\omega)}_{\text{Environment}}$$

This allows us to compute the electronic band-to-band transitions using Fermi’s Golden Rule (FGR) and multiply them by the local density of states (LDOS) derived from classical Green’s tensors.

---

## 2. THE TECHNICAL STACK & MATHEMATICAL FORMALISM

### 2.1 The Electronic Module (Material Physics)

**Model:** **Rosei-Guerrisi Interband Model** (extended to Non-Equilibrium).

**Primary Equation:** Fermi’s Golden Rule for the Transition Rate $\Gamma_{i \to f}$.

The transition rate per unit volume for photon emission at energy $\hbar\omega$ is:

$$R_{em}(\hbar\omega) = \frac{2\pi}{\hbar} \sum_{i,f} |\mathcal{M}_{fi}|^2 \cdot \eta(E_i, E_f) \cdot \delta(E_i - E_f - \hbar\omega)$$

**Components:**

1. **Matrix Element ($|\mathcal{M}_{fi}|^2$):** Represents the dipole transition strength.
    
    - **Interband:** Derived from Rosei model (d-band to sp-band). Assumed constant near symmetry points X and L.
        
    - **Intraband:** Approximated via Drude scaling or Surface-Assisted Landau Damping (see Section 4).
        
2. **Population Factor ($\eta$):** The critical non-equilibrium term.
    
    - $$\eta = f_{c}(E)[1 - f_{v}(E-\hbar\omega)]$$
        
    - _Note:_ We explicitly neglect Stimulated Emission ($f_c f_v$) as $\hbar\omega \gg k_B T$ (Boltzmann Limit).
        
3. **Joint Density of States (JDOS):** The summation over $k$-space is converted to an integral over energy:
    
    - $$\text{JDOS}(\hbar\omega) = \frac{1}{(2\pi)^3} \int_{\text{BZ}} \frac{dS_k}{|\nabla_k (E_c - E_v)|}$$
        

### 2.2 The Photonic Module (Electrodynamics)

**Model:** **Macroscopic QED** (Novotny & Hecht, Ch. 8).

**Primary Equation:** Spontaneous Emission Rate in an Arbitrary Environment.

The vacuum density of states $\rho_{vac}$ is replaced by the partial local density of states (LDOS), calculated via the **Green’s Dyadic** $\mathbf{G}(\mathbf{r}, \mathbf{r}; \omega)$:

$$\frac{\Gamma}{\Gamma_0} = \frac{\text{Power}}{\text{Power}_0} = \frac{6\pi c}{\omega} \text{Im} \left\{ \hat{\mathbf{n}} \cdot \mathbf{G}(\mathbf{r}_0, \mathbf{r}_0; \omega) \cdot \hat{\mathbf{n}} \right\}$$

- **$\mathbf{G}$:** The classical electromagnetic Green's function, solved via FDTD or analytical Mie theory.
    
- **$\hat{\mathbf{n}}$:** The orientation of the dipole (averaged for polycrystalline gold).
    

### 2.3 The "Product Form" (Separability)

The final master equation for the simulated signal:

$$S(\omega) \propto \underbrace{\left( \omega \cdot |\mu|^2 \cdot \text{JDOS} \cdot f_{neq} \right)}_{\text{Electronic Source}} \times \underbrace{\left( \omega^2 \cdot \text{Im}\{\mathbf{G}\} \right)}_{\text{Photonic Enhancement}}$$

_(Note: The $\omega$ powers aggregate to $\omega^3$ in free space)._

---

## 3. SETTLED SCIENCE (Validated Decisions)

The following principles are considered **axiomatic** for this project. No further debate is required.

**3.1 Regime Validity (Weak Coupling)**

- **Fact:** The electron dephasing time in Gold is $\tau \approx 10-20 \text{ fs}$ ($\gamma \approx 10^{14} \text{ Hz}$).
    
- **Implication:** The Rabi frequency $\Omega_R$ for any realistic CW laser intensity is $\Omega_R \ll \gamma$.
    
- **Decision:** We formally reject the **Optical Bloch Equations** and **Jaynes-Cummings Model**. The system has no phase memory; FGR is mathematically sufficient.
    

**3.2 Microscopic Reversibility**

- **Fact:** The transition dipole moment is Hermitian: $|\langle f | \hat{\mu} | i \rangle| = |\langle i | \hat{\mu} | f \rangle|$.
    
- **Implication:** The spectral "fingerprint" (peak locations) of Absorption and Emission are identical.
    
- **Nuance:** The emission spectrum is "blue-tilted" relative to absorption due to the $\omega^3$ phase-space factor (Einstein $A/B$ ratio).
    

**3.3 The Intraband Drude Scaling**

- **Fact:** Direct intraband transitions in bulk are forbidden by momentum conservation ($\mathbf{q}_{photon} \approx 0$). They require phonon assistance (2nd Order).
    
- **Decision:** For the **bulk** contribution, we model the intraband matrix element scaling as:
    
    $$|\mathcal{M}_{intra}|^2 \propto \frac{1}{\omega^4}$$
    
    This aligns with the Drude macroscopic dielectric function $\epsilon_2(\omega) \propto \omega^{-3}$.
    

**3.4 Neglect of Stimulated Emission**

- **Fact:** At 2.0 eV (visible), $\hbar\omega \approx 80 \times k_B T_{room}$.
    
- **Calculation:** The Bose-Einstein factor $(e^{\hbar\omega/kT} - 1)^{-1} \approx e^{-\hbar\omega/kT}$.
    
- **Decision:** The error from neglecting stimulated emission is $\sim 10^{-30}$. We assume pure spontaneous emission.
    

---

## 4. ADDENDUM: MATHEMATICAL PROOF OF MOMENTUM BROADENING

_(Use this section to defend the "First-Order Intraband" hypothesis against critique regarding momentum conservation)._

**Objective:** Prove mathematically that confining a particle to a box of size $L$ broadens its momentum distribution $\Phi(k)$ significantly enough to allow "forbidden" transitions.

**1. The Spatial Wavefunction (Confinement)**

Consider an electron confined in a 1D box of length $L$ (representing the nanoparticle diameter). The ground state wavefunction is:

$$\psi(x) = \begin{cases} \sqrt{\frac{2}{L}} \cos\left(\frac{\pi x}{L}\right) & \text{if } |x| \le L/2 \\ 0 & \text{otherwise} \end{cases}$$

_(Note: Using cosine for the ground state centered at 0)._

**2. The Momentum Space Wavefunction**

To find the probability of measuring momentum $k$, we take the Fourier Transform:

$$\Phi(k) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \psi(x) e^{-ikx} dx = \frac{1}{\sqrt{\pi L}} \int_{-L/2}^{L/2} \cos\left(\frac{\pi x}{L}\right) e^{-ikx} dx$$

**3. The Result (The Sinc Function)**

Evaluating this integral yields:

$$\Phi(k) = \sqrt{\frac{L}{4\pi}} \left[ \text{sinc}\left(\frac{(k - \pi/L)L}{2}\right) + \text{sinc}\left(\frac{(k + \pi/L)L}{2}\right) \right]$$

where $\text{sinc}(u) = \frac{\sin(u)}{u}$.

**4. The Uncertainty Width ($\Delta k$)**

The primary peak of the $\text{sinc}(u)$ function occurs when $u=0$, or $k = \pm \pi/L$.

The first zero of the function occurs when the argument is $\pi$.

$$\frac{\Delta k \cdot L}{2} = \pi \implies \Delta k = \frac{2\pi}{L}$$

**5. Physical Consequence (The Transition)**

In the bulk limit ($L \to \infty$), $\Delta k \to 0$, and $\Phi(k)$ becomes a Dirac Delta function $\delta(k-k_0)$. Transitions are strictly forbidden unless $\Delta k_{exact}$ is met.

In the nanoparticle limit ($L \to 0$):

- **The Width Grows:** $\Delta k$ becomes large.
    
- **The Tails Overlap:** The wavefunction $\Phi_i(k)$ contains significant amplitude components at momenta far from its center.
    
- **Transition Probability:**
    
    $$M_{fi} \propto \int \Phi_f^*(k) \Phi_i(k-q) dk$$
    
    Even if the centers of $\Phi_i$ and $\Phi_f$ are separated by a "forbidden" gap, the broadened tails of the Sinc functions overlap, making the integral non-zero. This is the **First-Order Surface-Assisted Transition**.
    

---

## 5. FRICTION POINTS & RESOLUTION STRATEGIES

### 5.1 The "Constant TDM" Controversy (Sivan vs. Standard Model)

**The Conflict:** Standard Solid State theory predicts $|M|^2 \propto \omega^{-4}$. Advisor (Sivan) argues for an effectively constant TDM in nanoparticles.

**The Physics:** Relying on the derivation in Section 4, the surface breaks translational symmetry ($\nabla F \neq 0$), relaxing selection rules.

**The Resolution:**

We acknowledge that for small NPs ($< 20$ nm), the $1/\omega^4$ scaling is relaxed.

- **Method:** We will treat "Constant TDM" as an **upper-bound limit** for error analysis.
    
- **Defense:** "While we adopt the standard Drude scaling for the bulk baseline, we acknowledge that surface momentum transfer (demonstrated by the Sinc function broadening) introduces a 'white noise' floor to the matrix element, which we parametrize separately."
    

### 5.2 Validity of Bulk Bands in Nanoparticles

**The Conflict:** Can we use the Rosei (bulk) band structure for a 20nm particle?

**The Resolution:** **Yes, via the Envelope Function Approximation (EFA).**

- **Logic:** The discretization energy $\Delta E \approx \hbar^2 \pi^2 / (2m L^2)$ is negligible compared to thermal broadening ($k_B T$) and scattering broadening ($\hbar \gamma$) for $L > 5$ nm.
    
- **Status:** We treat the density of states as a continuum (Rosei model) but apply the momentum relaxation factor from 5.1.
    

---

## 6. CONTEXTUAL NUANCE & HOUSE RULES

### 6.1 Notation Standards

- **Energy:** Electron Volts (eV).
    
- **Frequencies:** Angular frequency $\omega$ (rad/s) for theory; Wavelength $\lambda$ (nm) for spectral plots.
    
- **Green's Tensor:** Denoted as $\mathbf{G}$. Must always specify arguments: $\mathbf{G}(\mathbf{r}, \mathbf{r}')$ vs. $\mathbf{G}(\mathbf{r}, \mathbf{r})$.
    
- **Dielectric Function:** $\epsilon(\omega) = \epsilon_1 + i\epsilon_2$.
    
    - $\epsilon_2$ is strictly proportional to **Absorption**.
        
    - $\text{Im}\{\mathbf{G}\}$ is strictly proportional to **LDOS**.
        

### 6.2 Implementation Constraints

1. **Drude Subtraction:** Experimental absorption data must be pre-processed:
    
    $$\epsilon_{interband} = \epsilon_{exp} - \epsilon_{Drude}(\omega_p, \gamma)$$
    
    Only $\epsilon_{interband}$ is to be fitted to the Rosei model.
    
2. **Simulation Flow:**
    
    - **Step 1:** Calculate/Load Bulk JDOS (Rosei).
        
    - **Step 2:** Apply Non-Eq Fermi Factors (User defined $T_e, \mu_{chem}$).
        
    - **Step 3:** Compute electronic spectrum $I_e(\omega)$.
        
    - **Step 4:** Compute Photonic LDOS via Mie/FDTD $I_{ph}(\omega)$.
        
    - **Step 5:** Multiply: $I_{total} = I_e \times I_{ph}$.
        

### 6.3 Sensitivity Policy (Sensitive Data)

- Standard prohibition on using PII/Sensitive data applies.
    
- Use of generic terms like "Leading Defense Company" for employment context is strictly enforced in all external communications.
    

---

## 7. ACTIONABLE NEXT STEPS

1. **Code Validation:** Verify the Python script integrating the Rosei JDOS with the $\omega^3$ pre-factor. Ensure the units of the Green's tensor (inverse volume/length) cancel correctly with the dipole moment to yield a Rate ($s^{-1}$).
    
2. **Sivan Defense Prep:** Prepare the specific "Momentum Overlap Integral" derivation (Section 4) to justify the first-order intraband transition mechanism during reviews.
    
3. **Data Generation:** Run the FGR model for Electron Temperatures $T_e = [300K, \dots, 2000K]$ to generate the theoretical emission map.