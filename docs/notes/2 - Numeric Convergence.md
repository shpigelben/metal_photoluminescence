# Stage 2 — Numeric Convergence (energy space)

This note documents what is implemented in `code/energy_space/2_numeric_convergence.py`.

## Goal

Numerically evaluate the constant-eDOS emission integral and verify convergence with respect to the **energy-integration step** $\Delta\mathcal{E}$ by comparing against a closed-form analytic expression.

## Definitions

- Fermi–Dirac occupation:
  $$
  f(\mathcal{E})=\frac{1}{e^{\beta(\mathcal{E}-\mu)}+1},\qquad \beta=\frac{1}{k_B T}.
  $$
- Chemical potential approximation (implemented in `_preamble_and_funcs.py`):
  $$
  \mu(\mathcal{E}_F,T)\approx \mathcal{E}_F\left(1-\frac{\pi^2}{12}\left(\frac{T}{T_F}\right)^2\right),
  \qquad T_F=\frac{\mathcal{E}_F}{k_B}.
  $$
- Free-electron density of states (implemented in `_preamble_and_funcs.py`):
  $$
  \rho(\mathcal{E}) = \frac{m_e^{3/2}}{\pi^2\hbar^3}\sqrt{2\mathcal{E}},
  \qquad \rho_F=\rho(\mathcal{E}_F).
  $$

## Numeric integral (constant eDOS)

The script computes, for each emission energy $\hbar\omega$,
$$
I_{\mathrm{num}}(\hbar\omega;T,\mathcal{E}_F)
  = \rho_F^2\int_{\mathcal{E}_{\min}}^{\mathcal{E}_{\max}}
  f(\mathcal{E}+\hbar\omega)\,[1-f(\mathcal{E})]\;d\mathcal{E}.
  \tag{S2.1}
$$

### Log-stable thermal factor

To avoid overflow/underflow in the thermal factor, the integrand is built in log form.
Let
$$
a=\beta(\mathcal{E}-\mu),\qquad b=a+\beta\hbar\omega.
$$
Then
$$
f(\mathcal{E}+\hbar\omega)\,[1-f(\mathcal{E})]
=\frac{e^{a}}{\left(1+e^{a}\right)\left(1+e^{b}\right)}.
$$
Equivalently,
$$
\log\!\Big(f(\mathcal{E}+\hbar\omega)\,[1-f(\mathcal{E})]\Big)
= a-\log(1+e^{a})-\log(1+e^{b}).
\tag{S2.2}
$$
In code this uses $\log(1+e^x)=\mathrm{logaddexp}(0,x)$, and then exponentiates once:
$$
\texttt{integrand}=\exp(\texttt{log\_val}).
$$

### Quadrature

The integral in (S2.1) is evaluated with composite Simpson’s rule:
$$
I_{\mathrm{num}}(\hbar\omega) = \rho_F^2\;\mathrm{Simpson}\!\left(\texttt{integrand}(\mathcal{E});\,\mathcal{E}\in \mathcal{E}_{\text{grid}}\right).
$$

To keep memory bounded, the code batches the $\hbar\omega$ sweep and also caps the effective batch size so that the largest temporary array is $\mathcal{O}(N_\mathcal{E}\times N_{\hbar\omega,\text{batch}})$.

## Analytic reference (exact for constant eDOS)

The script compares against an analytic “exact” constant-eDOS result:
$$
I_{\mathrm{exact}}(\hbar\omega;T,\mathcal{E}_F)=\rho_F^2\,k_B T\,R(\hbar\omega),
\tag{S2.3}
$$
where $x=\beta\hbar\omega$ and
$$
R(\hbar\omega)=
\begin{cases}
\dfrac{x+\ln\!\left(1+e^{-\beta\mu}\right)-\ln\!\left(1+e^{\beta(\hbar\omega-\mu)}\right)}{e^{x}-1}, & x\neq 0,\\
\dfrac{1}{1+e^{-\beta\mu}}, & x=0.
\end{cases}
\tag{S2.4}
$$
Numerically, $e^x-1$ is evaluated using $\mathrm{expm1}(x)$ for stability.

## Relative error definition

For each $\hbar\omega$ point:
$$
\delta_{\mathrm{rel}}(\hbar\omega)=\left|\frac{I_{\mathrm{num}}(\hbar\omega)-I_{\mathrm{exact}}(\hbar\omega)}{I_{\mathrm{exact}}(\hbar\omega)}\right|.
\tag{S2.5}
$$
The helper `relative_error(...)` in `_preamble_and_funcs.py` also enforces $0/0\to 0$ elementwise.

## What is plotted

### 1) Convergence vs $\Delta\mathcal{E}$ (mean error over $\hbar\omega$)

The script generates a convergence plot of the **mean** error over a $\hbar\omega$ range:
$$
\left\langle |\delta_{\mathrm{rel}}| \right\rangle_{\hbar\omega}
=\frac{1}{N}\sum_{\hbar\omega\in\mathcal{W}} |\delta_{\mathrm{rel}}(\hbar\omega)|.
\tag{S2.6}
$$

- The tested steps are $\Delta\mathcal{E}\in\{10^{-1},10^{-2},10^{-3},10^{-4}\}\,\mathrm{eV}$.
- For each requested $\Delta\mathcal{E}$, a Simpson-friendly uniform grid is built by choosing an **even** number of intervals $N$ and setting
  $$
  \mathcal{E}_{\text{grid}}=\mathrm{linspace}(\mathcal{E}_{\min},\mathcal{E}_{\max},N+1),\qquad
  \Delta\mathcal{E}_{\mathrm{eff}}=\frac{\mathcal{E}_{\max}-\mathcal{E}_{\min}}{N}\le \Delta\mathcal{E}.
  \tag{S2.7}
  $$
- The averaging set $\mathcal{W}$ is a subsample of the emission-energy axis: `E_EM_VALUES[::5]`.
- Points where $|I_{\mathrm{exact}}|$ is extremely small are excluded from the mean (to avoid ill-conditioned relative errors). Concretely, the mean uses only $\hbar\omega$ values satisfying
  $$
  |I_{\mathrm{exact}}(\hbar\omega)| \ge r\;\max_{\hbar\omega\in\mathcal{W}}|I_{\mathrm{exact}}(\hbar\omega)|,
  \qquad r=10^{-12}.
  \tag{S2.8}
  $$

The figure is saved as `docs/figures/stage_2_convergence_mean_rel_error_vs_dE.svg`.

### 2) $\delta_{\mathrm{rel}}(\hbar\omega)$ curves on the default grid

The script also produces the 2×2 grid plot of $\delta_{\mathrm{rel}}(\hbar\omega)$ for:
$$
(T,\mathcal{E}_F)\in\{(300,5),(300,3),(700,3),(1000,3)\}.
$$
This plot uses the default `E_GRID` (from `_preamble_and_funcs.py`) rather than the swept grids, and is saved as `docs/figures/stage_2_rel_error_grid.svg`.

## Why we do not reach “machine precision”

Even though Simpson’s quadrature error decreases rapidly for smooth integrands, the plotted relative error is not expected to go all the way to $\sim10^{-16}$ (double precision machine epsilon), because:

1. **Relative error becomes ill-conditioned when the reference is tiny.**  
   For large $\hbar\omega$, $I_{\mathrm{exact}}(\hbar\omega)$ becomes extremely small, so dividing by it amplifies any floating-point noise; this is why the convergence average masks small-$I_{\mathrm{exact}}$ points via (S2.8).
2. **Floating-point roundoff/summation noise eventually dominates.**  
   Making $\Delta\mathcal{E}$ smaller increases the number of samples in the composite rule; beyond a point, the discretization error is below the accumulated rounding error, so refinement no longer improves (and can appear to worsen) $\langle|\delta_{\mathrm{rel}}|\rangle_{\hbar\omega}$.
3. **The analytic “exact” expression is still evaluated in floating point.**  
   $I_{\mathrm{exact}}$ uses `\logaddexp` and $\mathrm{expm1}$ for stability, but it is not an exact real-number oracle; it carries its own finite-precision error.
4. **Finite integration limits and exponent underflow.**  
   The numeric integral is performed on $[\mathcal{E}_{\min},\mathcal{E}_{\max}]$ and evaluates $\exp(\text{log-integrand})$; far from the thermal peak this can underflow to zero. These effects are typically negligible physically, but they set practical accuracy floors in $\delta_{\mathrm{rel}}$.

As a result, “smaller $\Delta\mathcal{E}$ $\Rightarrow$ smaller plotted error” is not guaranteed to be strictly monotone across all regimes and metrics, especially when the relative error is averaged over a $\hbar\omega$ range that includes very small reference values.

## TODO (from the original work plan)

- [ ] show that the calculated $f(\mathcal{E}+\hbar\omega)\,[1-f(\mathcal{E})]$ is more numerically stable than the explicit form.
- [ ] show that when using the numerically stable version, the two forms converge to machine precision away from the Fermi energy.
- [ ] using the trapezoid method, find the integration step necessary for convergence (to avoid unnecessary overhead).
- [ ] explain the deviation around the Fermi energy and suggest a solution if possible.
- [ ] show the multiple plots that illustrate how Fermi energy and temperature affect the relative error.
