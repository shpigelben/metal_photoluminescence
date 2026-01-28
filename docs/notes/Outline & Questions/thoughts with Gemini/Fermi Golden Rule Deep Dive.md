## 1. EXECUTIVE SUMMARY & CORE THESIS

- **The Specific Problem:** The canonical "Energy Space" formulation of Fermi's Golden Rule ($W \propto |M|^2 \rho(E)$) is fundamentally insufficient for interband transitions in metals. It relies on isotropic approximations that collapse the angular dependence of the transition dipole moment $\mathbf{p}_{cv}(\mathbf{k})$. Furthermore, standard solid-state solvers assume a vacuum environment, neglecting the local photonic density of states (LDOS) modifications critical in nanophotonics (Purcell Effect).
    
- **The Proposed Solution:** A "Composite Phase Space" approach. The transition rate is derived as a **spectral convolution** of the Electronic Supply (momentum-resolved Joint Density of States) and the Photonic Demand (Green's Function-derived LDOS).
    
- **The "Why":** This formalism preserves the microscopic selection rules of the anisotropic Fermi surface (via $\mathbf{k}$-space integration) while simultaneously capturing the macroscopic electromagnetic boundary conditions (via $\text{Im}\{\mathbb{G}\}$). It bridges the gap between Condensed Matter Physics (electronic bands) and Macroscopic QED (Novotny formalism).
    

## 2. TECHNICAL STACK & MATHEMATICAL FORMALISM

- **Mathematical Models:**
    
    - **Basis:** Momentum Space ($\mathbf{k}$-space) is the fundamental basis; Energy space is a derived projection.
        
    - **Perturbation:** First-Order Time-Dependent Perturbation Theory (Dipole Approximation).
        
    - **Field Quantization:** Canonical quantization of the electromagnetic field expanded in generalized normal modes $\mathbf{u}_{\mathbf{q}\lambda}(\mathbf{r})$.
        
- **Key Equations (The Master Formulation):**
    
    The total transition rate $\Gamma(\mathbf{r})$ is the frequency integration of the **Spectral Overlap**:
    
    $$\Gamma(\mathbf{r}) = \frac{\pi e^2}{\epsilon_0 m^2} \int_{0}^{\infty} \frac{d(\hbar\omega)}{\omega} \cdot \underbrace{\mathcal{S}_{el}(\omega)}_{\text{Electronic Supply}} \cdot \underbrace{\mathcal{S}_{ph}(\mathbf{r}, \omega)}_{\text{Photonic Demand}}$$
    
    **I. The Electronic Supply (Weighted JDOS):**
    
    Defined by integrating over the Brillouin Zone (BZ) to rigorously capture band anisotropy:
    
    $$\mathcal{S}_{el}(\omega) = \frac{1}{(2\pi)^3} \int_{\text{BZ}} d^3k \, |\hat{\epsilon} \cdot \mathbf{p}_{cv}(\mathbf{k})|^2 \cdot \mathcal{F}_{stat}(\mathbf{k}, T_e) \cdot \delta(E_c(\mathbf{k}) - E_v(\mathbf{k}) - \hbar\omega)$$
    
    **II. The Photonic Demand (Projected LDOS):** Defined via the imaginary part of the Dyadic Green's Function:
    
    $$\mathcal{S}_{ph}(\mathbf{r}, \omega) = \frac{6\omega}{\pi c^2} \left[ \mathbf{n}_\mu \cdot \text{Im} \{ \mathbb{G}(\mathbf{r}, \mathbf{r}; \omega) \} \cdot \mathbf{n}_\mu \right] \cdot [1 + n_B(\omega, T_{ph})]$$
    
- **Statistical Weights ($\mathcal{F}_{stat}$):**
    
    To account for Pauli blocking and thermal population in non-equilibrium conditions:
    
    $$\mathcal{F}_{stat}(\mathbf{k}) = f_{FD}(E_c, \mu_c, T_e) \times [1 - f_{FD}(E_v, \mu_v, T_e)]$$
    

## 3. "SETTLED SCIENCE" (Axioms)

- **Decision:** **Momentum Space is the Fundamental Generator.**
    
    - **Rationale:** Energy is a degenerate scalar eigenvalue. The transition matrix element $\mathbf{p}_{cv}(\mathbf{k})$ is a vector field that varies significantly across the iso-energy surface.
        
    - **Mathematical Justification:** The transformation to energy space requires the Jacobian determinant (group velocity):
        
        $$\int d^3k \to \int dE \int_{S_E} \frac{dS_k}{|\nabla_\mathbf{k} E(\mathbf{k})|}$$
        
        Pre-averaging over $S_E$ (the DOS approximation) destroys the directional information of $\mathbf{p}_{cv}(\mathbf{k})$ necessary for anisotropic media.
        
- **Decision:** **Equivalence of DOS Definitions (The "Rosetta Stone").**
    
    - **Rationale:** The three common definitions of Density of States are mathematically isomorphic.
        
    - **The Mapping:**
        
        1. **Phase Space Counting:** $\rho(E) = \int \frac{d^3k}{(2\pi)^3} \delta(E - E_k)$
            
        2. **Jacobian Form:** $\rho(E) = \frac{1}{(2\pi)^3} \frac{dS_E}{|\nabla E|}$
            
        3. **Green's Function Form:** $\rho(E) = -\frac{1}{\pi} \text{Im}\{\text{Tr}[\mathbb{G}]\}$
            
    - **Verification:** Applying the Green's Function trace to the vacuum $\mathbb{G}_0$ yields the exact vacuum mode density $\rho_0 = \omega^2/(\pi^2 c^3)$.
        
- **Decision:** **Novotny's Green's Function formalism is compatible with Continuum Mechanics.**
    
    - **Rationale:** While Novotny derives $\Gamma \propto \text{Im}\{\mathbb{G}\}$ for a single atom ($\delta$-function in electronic energy), the linearity of Quantum Mechanics allows this result to be used as the **kernel** for the continuum integration over the metal bands.
        

## 4. "FRICTION POINTS" (ACTIVE DEBATES & RESOLUTIONS)

- **Conflict 1: The "Single Delta" Paradox.**
    
    - **The Issue:** The Master Equation contains _one_ energy conservation delta $\delta(E_f - E_i)$. The final formula utilizes _two_ density functions (JDOS and LDOS), each defined by its own delta. Where did the second delta come from?
        
    - **Resolution:** The **Convolution Identity**. We mathematically split the single conservation constraint into an integral over all possible exchange energies $\hbar\omega$.
        
    - **Mathematical Defense:**
        
        $$\delta(E_{el} - E_{ph}) \equiv \int_{-\infty}^{\infty} d(\hbar\omega) \, \delta(E_{el} - \hbar\omega) \cdot \delta(\hbar\omega - E_{ph})$$
        
        This operation rigorously decouples the electronic summation ($\sum_\mathbf{k}$) from the photonic summation ($\sum_\mathbf{q}$).
        
- **Conflict 2: Direct vs. Indirect Transitions (Counting Densities).**
    
    - **The Issue:** Does the calculation require two densities or three?
        
    - **Resolution:** It depends on momentum conservation constraints.
        
        - **Case A: Direct (Vertical) Transitions:** $\mathbf{k}_f = \mathbf{k}_i$. The initial and final electron states are locked. **Result:** Convolve 2 Densities (JDOS $\times$ LDOS).
            
        - **Case B: Indirect (Phonon-Assisted) Transitions:** $\mathbf{k}_f = \mathbf{k}_i \pm \mathbf{q}_{ph}$. The lock is broken; initial and final states are statistically independent. **Result:** Convolve 3 Densities ($\rho_{valence} \times \rho_{conduction} \times \text{LDOS}$).
            

## 5. CONTEXTUAL NUANCE & HOUSE RULES

- **Computational Scope:**
    
    - **Interband (Gold Color):** Treat as **Direct**. Use JDOS.
        
    - **Intraband (Drude Heating):** Treat as **Indirect**. Use product of $\rho_{init} \times \rho_{final}$.
        
- **Approximations:**
    
    - **Dipole Approximation:** Valid since $\lambda_{light} \gg a_{lattice}$.
        
    - **Weak Coupling:** Assumes no Rabi flopping (Markovian limit).
        
- **Variable Definitions:**
    
    - $\mathbf{p}_{cv} = \langle c | \hat{\mathbf{p}} | v \rangle$: Momentum matrix element.
        
    - $\mathbf{u}_{\mathbf{q}\lambda}(\mathbf{r})$: Normalized electromagnetic mode function.
        

## 6. ADDENDUM: CRITICAL DERIVATIONS

**Derivation:** **The Emergence of Dual Densities from the Composite Master Equation**

**Objective:** Prove that $W_{i\to f} \propto \int \text{JDOS} \times \text{LDOS} \, d\omega$.

**Step 1: The Composite Hilbert Space Summation**

The rate $\Gamma$ is the sum over all final composite states $|F\rangle = |\mathbf{k}_v, 1_{\mathbf{q}\lambda}\rangle$.

$$\Gamma = \frac{2\pi}{\hbar} \sum_{\mathbf{k}_v} \sum_{\mathbf{q}\lambda} |\langle \mathbf{k}_v, 1_{\mathbf{q}\lambda} | H_{int} | \mathbf{k}_c, 0 \rangle|^2 \delta(E_c - E_v - \hbar\omega_{\mathbf{q}})$$

**Step 2: Factorization of the Interaction Hamiltonian**

Using $H_{int} \propto \hat{\mathbf{p}} \cdot \hat{\mathbf{A}}$ and expanding $\hat{\mathbf{A}}$ in modes $\mathbf{u}_{\mathbf{q}\lambda}$:

$$|\mathcal{M}_{if}|^2 = \left( \frac{\pi e^2 \hbar}{\epsilon_0 m^2 \omega_{\mathbf{q}}} \right) |\mathbf{p}_{cv} \cdot \mathbf{u}_{\mathbf{q}\lambda}^*(\mathbf{r})|^2$$

**Step 3: Introduction of the Convolution Kernel**

Insert the identity $\int d(\hbar\omega) \delta(E_{cv} - \hbar\omega) \delta(\hbar\omega - \hbar\omega_{\mathbf{q}}) = \delta(E_{cv} - \hbar\omega_{\mathbf{q}})$.

$$\Gamma = \frac{\pi e^2}{\epsilon_0 m^2} \int \frac{d(\hbar\omega)}{\omega} \left[ \sum_{\mathbf{k}_v} \dots \delta(E_{cv} - \hbar\omega) \right] \left[ \sum_{\mathbf{q}\lambda} \dots \delta(\hbar\omega - \hbar\omega_{\mathbf{q}}) \right]$$

**Step 4: Identification of the Densities**

- **Electronic Term:** The sum over $\mathbf{k}$ constrained by $\delta(E_{cv} - \hbar\omega)$ is the **Joint Density of States (JDOS)**.
    
- **Photonic Term:** The sum over $\mathbf{q}$ constrained by $\delta(\hbar\omega - \hbar\omega_{\mathbf{q}})$ is the definition of **Local Density of Optical States (LDOS)**.
    
    - _Note:_ Via Novotny Eq. (8.117), $\sum_\mathbf{q} |\mathbf{u}_\mathbf{q}|^2 \delta(\dots) \equiv \frac{2\omega}{\pi c^2} \text{Im}\{\text{Tr}[\mathbb{G}]\}$.
        

**Final Result:**

The transition rate is the frequency-wise product of the material's ability to emit ($\mathcal{S}_{el}$) and the environment's ability to accept ($\mathcal{S}_{ph}$).
