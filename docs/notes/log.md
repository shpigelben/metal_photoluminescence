# Log

Last updated: 2025-12-14

## What’s implemented (energy-space “stages”)

- **Shared constants + utilities**: `code/energy_space/_preamble_and_funcs.py`
  - Energy grids (`E_GRID`, `E_EM_VALUES`), constants (`k_B`, `hbar`, `m_e`), `chemical_potential()`, `density_of_states()`, `relative_error()`.
- **Stage 0 (sanity/intuition plots)**: `code/energy_space/0_electon_occupation.py`
  - Interactive plot of the thermal factor `f(E+ℏω)[1-f(E)]` + its components.
- **Stage 1 (analytic approximation validity)**: `code/energy_space/1_analytic_approximation.py`
  - Implements the **exact constant-eDOS analytic** form (Eq. (6) in `docs/notes/0 - Work Plan.md`) and the **approximate** low-`k_BT`/“large energy” form (Eq. (7)).
  - Produces error visualizations (e.g. heatmap) for “approx vs exact”.
- **Stage 2 (numeric convergence under constant eDOS)**: `code/energy_space/2_numeric_convergence.py`
  - Numeric evaluation of Eq. (5) via Simpson integration of a log-stable integrand, compared against the analytic exact Eq. (6).

## “Stable” Fermi-Dirac usage (what it means here)

Implemented in `code/energy_space/_preamble_and_funcs.py`:

- `fermi_occupation_mu_beta(E, mu, beta)` computes `f(E)=1/(exp(β(E-μ))+1)` in a way that avoids `exp(...)` overflow using `logaddexp`.
- `fermi_hole_mu_beta(E, mu, beta)` computes `1-f(E)` *without* subtracting from 1 (avoids catastrophic cancellation when `f≈1`).
- `fermi_product_mu_beta(E, hw, mu, beta)` computes `f(E+hw)[1-f(E)]` in **log-form** (adds logs, then `exp` once), preserving dynamic range.

These changes fix pointwise numerical issues (overflow/cancellation) in the thermal factors, especially at large `|β(E-μ)|`.

## Insights from the comparisons (what the “instability” usually is)

- **Stability of the Fermi factors is necessary but not sufficient**: even with a log-stable integrand, the *comparison* can look unstable due to how the analytic forms and error metrics behave in certain regimes.
- **Approximation breakdown near the Fermi scale**: the Eq. (6) → (7) approximation assumes `μ` and `μ-ℏω` are large compared to `k_BT`. When `ℏω ≈ μ ≈ E_F`, this assumption fails and deviations from numeric evaluation increase (not a floating-point bug).
- **Relative-error spikes can be an artifact**: when the “exact/analytic” value is exponentially small (large `βℏω`), tiny absolute differences (quadrature error, truncation, underflow-to-0) can produce large relative error. In those regimes, absolute error or log-error is often more informative than `|(num-ana)/ana|`.
- **Analytic evaluation also needs stable primitives**: the “exact” closed form should avoid `log1p(exp(x))` with large positive `x` and avoid `exp(x)-1` for small `x` (use `logaddexp` / `expm1`-style forms as in `code/energy_space/1_analytic_approximation.py`).

## Open items / next steps

- **Stage 3**: validate the constant eDOS approximation (Eq. (4) ↔ (5)) and identify where it fails.
- **Stage 4+**: validate delta-function approximation in energy-space and then k-space (Eq. (3) ↔ (4), etc.).
- **Explain/mitigate the “deviation around the Fermi energy”** with targeted diagnostics:
  - separate *physics approximation error* (Eq. (6) vs (7), constant eDOS, delta approximation) from *numerical error* (grid truncation, step size, integration method),
  - consider plotting absolute error alongside relative error in low-signal regimes.

