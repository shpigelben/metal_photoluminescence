## 1. The Fundamental Distinction: Reflection vs. Photoluminescence

Before constructing the PL model, we must mathematically distinguish it from Reflection (Scattering). While both result in photons leaving the material, they are governed by distinct quantum mechanical orders and coherence properties.

### 1.1 Reflection (Coherent Scattering)

Reflection is a **Second-Order Virtual Process**. The electron interacts with the photon but never populates a real excited eigenstate. It remains in a superposition (virtual state) forbidden by energy conservation, forcing immediate re-radiation.

**The Microscopic Law:** Kramers-Heisenberg Dispersion.

The polarizability $\alpha(\omega)$ of an electron in ground state $|g\rangle$ is a sum over all intermediate states $|k\rangle$:

$$\alpha(\omega) = \frac{e^2}{\hbar} \sum_{k} \left( \frac{|\langle k | \hat{\mathbf{r}} | g \rangle|^2}{\omega_{kg} - \omega - i\gamma} + \frac{|\langle k | \hat{\mathbf{r}} | g \rangle|^2}{\omega_{kg} + \omega + i\gamma} \right)$$

- **Virtual Denominator:** The term $(\omega_{kg} - \omega)$ is non-zero (off-resonance). The electron does not satisfy $E_f = E_i + \hbar\omega$.
    
- **Phase:** $\arg(\alpha)$ is fixed relative to the incident field $\mathbf{E}_{in}$. Coherence is preserved.
    
- **Macroscopic Manifestation:** This coherent summation leads to the Drude-Lorentz dielectric function $\varepsilon(\omega)$, governing Reflection $R = |(\sqrt{\varepsilon}-1)/(\sqrt{\varepsilon}+1)|^2$.
    

### 1.2 Photoluminescence (Incoherent Emission)

PL is a **Sequential First-Order Process**. It involves a "break" in the quantum evolution due to thermalization (dephasing).

1. **Step 1: Real Absorption.** The electron satisfies energy conservation and populates a real band state (e.g., $d \to sp$).
    
2. **Step 2: Relaxation (The Memory Loss).** Electron-electron scattering ($\tau_{ee} \approx 10-100$ fs) redistributes energy, creating a Fermi-Dirac distribution at temperature $T_e$. **Phase memory is lost.**
    
3. **Step 3: Spontaneous Emission.** The electron transitions back to a hole state.
    

**The Microscopic Law:** Fermi’s Golden Rule (FGR).

The emission rate $\Gamma$ is calculated _independently_ of the absorption phase:

$$\Gamma_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{H}_{int} | i \rangle|^2 \delta(E_f - E_i - \hbar\omega)$$

- **Real Delta Function:** Energy is strictly conserved in the final step.
    
- **Independence:** The rate depends on the _population_ of state $|i\rangle$, not the phase of the pump laser.
    

---

## 2. Pillar I: The Quantum-Classical Bridge (Non-Equilibrium FDT)

To model PL, we bridge the microscopic transition (FGR) with the macroscopic statistics ($T_e$) using the **Generalized Fluctuation-Dissipation Theorem (FDT)**.

### 2.1 Generalized Kirchhoff's Law

Standard Kirchhoff's law ($E = \alpha B(T)$) fails because $T_{el} \neq T_{latt}$. We derive the generalized form linking emission power $P$ to the **Net Absorption** of the excited state.

$$\frac{dP}{d\Omega} (\omega) = \frac{\hbar\omega^3}{4\pi^2 c^2} \cdot \text{Abs}(\omega, T_e) \cdot \left[ \frac{1}{e^{(\hbar\omega - \Delta\mu)/k_B T_e} - 1} \right]$$

- $\text{Abs}(\omega, T_e)$: Absorption coefficient modified by Pauli blocking at temperature $T_e$.
    
- $\Delta\mu$: Quasi-Fermi level splitting (Chemical potential of the hot electrons).
    

### 2.2 Derivation of the "Planckian" Limit

From the exact emission integral (Electronic Supply):

$$I_{em} = \int_{E_{gap}}^\infty \underbrace{f(E + \hbar\omega, T_e)}_{\text{Hot Electron}} \underbrace{[1 - f(E, T_e)]}_{\text{Available Hole}} \cdot \text{JDOS}(E) \, dE$$

**The "Step Function" Approximation:**

In the limit where the Fermi energy $\mu \gg \hbar\omega \gg k_B T$, the hole probability $[1-f(E)]$ is $\approx 1$ for transitions from the Fermi surface. The electron distribution approximates the Boltzmann tail: $f(E+\hbar\omega) \approx e^{-(E+\hbar\omega-\mu)/k_B T_e}$.

$$I_{em} \approx e^{-\hbar\omega/k_B T_e} \int f(E) \text{JDOS}(E) dE \propto e^{-\hbar\omega/k_B T_e}$$

> [!INFO] Synthesis
> 
> This explains why metallic PL spectra often look exponential (Planckian-like) but correspond to effective temperatures $T_e \approx 1500-3000$ K, far above the lattice temperature.

---

## 3. Pillar II: Electronic Source Modeling ($\mathcal{S}_{el}$)

The **Electronic Supply** $\mathcal{S}_{el}(\omega)$ is the quantum mechanical capacity of the material to emit, independent of the photonic environment.

### 3.1 The Rosei-Guerrisi Interband Model

We model the interband dielectric function $\varepsilon_{ib}''$ (imaginary part) by summing over vertical transitions in the Brillouin Zone (BZ).

$$\varepsilon_{ib}''(\omega) = \frac{\pi e^2}{\epsilon_0 m^2 \omega^2} \sum_{v,c} \int_{BZ} \frac{2}{(2\pi)^3} |\mathbf{M}_{cv}(\mathbf{k})|^2 \delta(E_c(\mathbf{k}) - E_v(\mathbf{k}) - \hbar\omega) d^3\mathbf{k}$$

- **X and L Points:** These symmetry points in Gold generate the characteristic absorption peaks (Van Hove singularities) at ~2.4 eV and ~1.8 eV.
    

### 3.2 Momentum Broadening (Nanoparticle Correction)

In bulk, momentum is conserved ($\mathbf{k}_{initial} = \mathbf{k}_{final}$). In nanoparticles of size $L$, spatial confinement relaxes this rule via Heisenberg uncertainty ($\Delta k \sim 1/L$).

We modify the bulk JDOS by convolving with a momentum relaxation kernel $\Phi(q)$:

$$\text{JDOS}_{NP}(\omega) = \int \text{JDOS}_{Bulk}(\omega') \Phi(\omega - \omega') d\omega'$$

Where $\Phi(q)$ is derived from the Fourier transform of the particle shape (e.g., Sinc function for a box):

$$\Phi(q) \propto \left| \frac{\sin(qL/2)}{qL/2} \right|^2$$

**Physical Consequence:** Sharp onset edges in bulk absorption become "smeared," allowing emission at energies nominally below the interband threshold.

---

## 4. Pillar III: Photonic Environment ($\mathcal{S}_{ph}$)

The **Photonic Demand** describes how the environment extracts energy from the dipole. We formalize this using the **Local Density of Optical States (LDOS)**.

### 4.1 Dyadic Green’s Function Formalism

The spontaneous emission rate enhancement (Purcell Factor) is given by:

$$\frac{\Gamma}{\Gamma_0} = \frac{\pi c}{ \omega} \text{Im} \left\{ \mathbf{n}_d \cdot \mathbf{G}(\mathbf{r}_0, \mathbf{r}_0; \omega) \cdot \mathbf{n}_d \right\}$$

- $\mathbf{G}(\mathbf{r}, \mathbf{r}'; \omega)$: The electric Dyadic Green's tensor satisfying $\nabla \times \nabla \times \mathbf{G} - k^2 \mathbf{G} = \mathbf{I}\delta(\mathbf{r} - \mathbf{r}')$.
    
- $\mathbf{n}_d$: Orientation of the dipole.
    

### 4.2 The "Product Form" Separability

For the unified model, we assert that the total emission intensity is the product of the Material Supply and Environmental Demand:

$$\Phi_{PL}(\omega) \propto \underbrace{\left[ \int f(E, T_e)(1-f) \text{JDOS}(E) dE \right]}_{\mathcal{S}_{el}(\omega)} \times \underbrace{\text{Im}\{\text{Tr}[\mathbf{G}]\}}_{\mathcal{S}_{ph}(\omega)}$$

- **Separation Validity:** This holds in the **Weak Coupling Regime**. If strong coupling (Rabi splitting) occurred, $\mathcal{S}_{el}$ and $\mathcal{S}_{ph}$ would be entangled in a non-linear Polariton Hamiltonian.
    

---

## 5. Friction Points: Transition Dipole Moment (TDM) Scaling

> [!WARNING] Active Debate: Drude vs. Sivan
> 
> A critical controversy exists regarding the frequency scaling of the matrix element $|\mathbf{M}_{cv}|^2$.

### 5.1 The Standard Drude Model

Assumes free-electron-like behavior for intraband transitions.

$$|\mathbf{M}_{cv}|^2 \propto \frac{1}{\omega^4}$$

**Implication:** PL should vanish rapidly in the visible range.

### 5.2 The Sivan Hypothesis (Symmetry Breaking)

Argues that in nanostructures, surface collisions break translational symmetry, enabling momentum mismatch.

$$|\mathbf{M}_{cv}|^2 \approx \text{Constant} \quad (\text{or } \propto \omega^{-2})$$

**Justification:** In the Sivan model, the spectral shape is dominated by the **JDOS** and the **Fermi Cutoff**, not the matrix element. Assuming a constant TDM provides a better fit to experimental linewidths for $L < 20$ nm particles.

---

## 6. Implementation Algorithm

To synthesize the unified spectrum:

1. **Input:**
    
    - $\varepsilon_{exp}(\omega)$ (Johnson & Christy).
        
    - Simulation parameters: $R$ (Radius), $T_e$ (Electron Temp), $\mu$ (Fermi Level).
        
2. **Pre-Processing (Drude Subtraction):**
    
    $$\varepsilon_{ib}(\omega) = \varepsilon_{exp}(\omega) - \left( 1 - \frac{\omega_p^2}{\omega(\omega + i\gamma_{bulk})} \right)$$
    
    _Use $\varepsilon_{ib}$ to fit Rosei parameters for JDOS._
    
3. **Calculate Electronic Supply $\mathcal{S}_{el}$:**
    
    - Compute Bulk JDOS from fitted bands.
        
    - Apply Momentum Broadening (Convolution with Sinc).
        
    - Apply Fermi Factors: $\text{Supply} = \text{JDOS}_{NP} \times f(E, T_e) \times [1-f(E-\hbar\omega, T_e)]$.
        
4. **Calculate Photonic Demand $\mathcal{S}_{ph}$:**
    
    - Solve Mie Theory or FDTD for the specific geometry.
        
    - Extract $\text{LDOS}(\omega) \propto \text{Im}\{\mathbf{G}\}$.
        
5. **Synthesize:**
    
    $$I_{PL}(\omega) = \mathcal{S}_{el}(\omega) \times \mathcal{S}_{ph}(\omega)$$
    
6. **Normalize & Compare:**
    
    - Normalize to the peak of the experimental PL spectrum to solve for the unknown quantum yield constant.
        

---

**See Also:** [[FDT & Kirchhoff]], [[Fermi Golden Rule Deep Dive]], [[Bulk vs NP]]