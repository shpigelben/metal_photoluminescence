# Master Guide: Metal Photoluminescence (MSc Thesis)

**Objective:** Compute the photoluminescence (PL) spectrum of Gold (Au) accounting for both **intraband** and **interband** transitions under **non-equilibrium** electron distributions. The inclusion of interband transitions within the non-equilibrium framework is the primary novel contribution.

---

## 1. Project Roadmap

### Phase 1: Intraband Transitions (Equilibrium) ✅
*Focus: Validation of numerical methods against analytic approximations in the low-energy limit.*
- [x] **Analytic Approximation:** Derivation and validity checking (Stage 1).
- [x] **Numeric Integration (Energy Space):** Convergence testing and constant eDOS approximation (Stages 2-4).
- [x] **Numeric Integration (Momentum Space):** 2D/4D delta approximations (Stages 5-6).
- [ ] **Final Verification:** Ensure `intra_momentum.ipynb` matches energy-space results perfectly.

### Phase 2: Intraband Transitions (Non-Equilibrium) 🚧
*Focus: Implementing the "hot" electron distribution.*
- [x] **Distribution Implementation:** Coded the non-equilibrium distribution $f(\mathcal{E}; \omega_L)$ in `_preamble_and_funcs.py`.
- [ ] **Theory Note:** Written [A6](A6%20-%20Non-Equilibrium%20Electron%20Distribution.md) detailing the perturbation model.
- [ ] **Integration:** Adapt energy-space and momentum-space integrators to accept arbitrary $f(\mathbf{k})$.
- [ ] **Validation:** Reproduce literature results (or demonstrate corrections) for intraband non-eq PL.

### Phase 3: Interband Transitions (Equilibrium) 🚧
*Focus: Adding the band structure of Gold.*
- [ ] **Theory Note:** Written [A2](A2%20-%20Interband%20Transitions%20and%20Joint%20Density%20of%20States.md) for JDOS and k-selection.
- [ ] **Isotropic Model:** Implement interband transitions assuming isotropic parabolic bands (Conduction $\leftrightarrow$ Valence).
- [ ] **Anisotropic Model:** Implement X and L symmetry point transitions for Au.
- [ ] **Integration:** Numerical integration over the Brillouin Zone (BZ) for interband terms.

### Phase 4: The Novel Contribution (Non-Eq Interband) 🔮
*Focus: The Thesis Core.*
- [ ] **Synthesis:** Combine Phase 2 (Non-Eq $f(\mathbf{k})$) with Phase 3 (Interband Matrix Elements).
- [ ] **Computation:** Calculate $I_{inter}(\hbar\omega)$ driven by the hot-electron distribution.
- [ ] **Analysis:** Compare the magnitude and spectral shape of Non-Eq Interband vs Intraband.

---

## 2. Technical Architecture

### Code Organization
*   `code/core/`: Shared physics functions (distributions, DOS, constants).
*   `code/intraband/`: Scripts/Notebooks specific to intraband.
*   `code/interband/`: Scripts/Notebooks specific to interband (Au models).
*   `code/paper_plots/`: Scripts generating final thesis figures.

### Key Theoretical Expressions
**General Emission Integral:**
$$ I(\hbar\omega) \propto \iint_{\text{BZ}} f(\mathbf{k}_{1})[1-f(\mathbf{k}_{2})] \left| M_{1\to 2} \right|^2 \delta(\mathcal{E}_1 - \mathcal{E}_2 + \hbar\omega) d^3k_1 d^3k_2 $$

**Distributions:**
*   $f^T$: Equilibrium Fermi-Dirac.
*   $f_{neq}$: Non-equilibrium (Perturbed by pump $\omega_L$).

---

## 3. Immediate To-Do List

1.  **Housekeeping:** Refactor `code/` to separate "scratchpad" notebooks from "production" modules.
2.  **Phase 2 Step:** Implement the `NonEquilibriumDistribution` class in `_preamble_and_funcs.py` (or a new module).
3.  **Phase 3 Step:** Complete the anisotropic interband notebook (`[5] inter_momentum...`).

---

*Last Updated: December 22, 2025*
