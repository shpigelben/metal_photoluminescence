# Q&A Log

## Question 1
**Q:** What is a modern approach to calculating intraband and interband transitions properly?

**A:**
### Modern Framework

1.  **Electronic Structure (DFT)**
    *   **Method:** Density Functional Theory (e.g., VASP, Quantum ESPRESSO).
    *   **Key for Au:** Must include **Spin-Orbit Coupling (SOC)** to correctly split the $d$-bands.

2.  **Interband Transitions**
    *   **Formula:** Fermi's Golden Rule.
    $$
    W_{i \to f} \propto \int_{BZ} |\mathbf{p}_{if}|^2 \delta(E_f - E_i - \hbar\omega) d\mathbf{k}
    $$
    *   **Technique:** Numerical integration over the Brillouin Zone using the **Tetrahedron method** or Gaussian broadening.

3.  **Intraband Transitions**
    *   **Mechanism:** Indirect transitions requiring momentum conservation via phonons or defects.
    *   **Model:** **Drude-Lorentz** model, parameterized by scattering rates ($\gamma$) derived from electron-phonon coupling calculations.

### Answer 1.2 (Computational Branch)
**Focus: Implementation in `code/main/`**

While the theoretical framework uses DFT, your current codebase implements a **semi-empirical** variation suitable for rapid parameter space exploration:

1.  **Band Structure ($E_k$):**
    *   Instead of full DFT, you appear to be using **analytic approximations** (Parabolic/Cosine bands) in `1_analytic_approximation.py` and `3_delta_approx 2d_e_space.py`.
    *   *Upgrade path:* Import $E(k)$ grids from VASP into `_preamble_and_funcs.py`.

2.  **Integration ($W_{if}$):**
    *   You are tackling the $\delta$-function integration in `0_numeric_convergence.py`.
    *   **Current Method:** Gaussian Broadening (`delta_approx`).
    *   **Verification:** The `numeric_convergence` plots in `figures/` track the error of this broadening vs. grid density ($N_k$).

3.  **Momentum Matrix Elements ($M_{if}$):**
    *   Currently likely treated as constant or simple $k$-dependent functions in `2_constant_edos_approx.py`.
    *   *Modern Standard:* Extract $M_{if}(k)$ from Wannier90 or DFT output to capture selection rules properly.
