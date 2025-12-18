"""
Shared constants and utility functions for energy-space scripts.
"""

import numpy as np

# Physical constants (energy in eV)
k_B = 8.617333262145e-5  # eV/K
hbar = 6.582119569e-16
m_e = 5.485e-4

# Default simulation parameters
E_F_DEFAULT = 5.0
E_MIN = 0.0
E_MAX = 10.0
D_E = 1e-2
E_GRID = np.arange(E_MIN, E_MAX + D_E, D_E)

EMISSION_ENERGY_MIN = 0.01
EMISSION_ENERGY_MAX = 8.0
N_EMISSION = 2000
E_EM_VALUES = np.linspace(EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, N_EMISSION)


def chemical_potential(E_F: float, T: float | np.ndarray) -> float | np.ndarray:
    T_F = E_F / k_B
    return E_F * (1 - (np.pi**2 / 12) * ((T / T_F) ** 2))


def eDOS(E: float | np.ndarray) -> float | np.ndarray:
    return ((m_e ** 1.5) / (np.pi ** 2 * hbar ** 3)) * np.sqrt(2 * E)


def relative_error(candidate: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """Elementwise |(candidate-reference)/reference|, with 0/0 -> 0."""

    candidate = np.asarray(candidate, dtype=float)
    reference = np.asarray(reference, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.abs((candidate - reference) / reference)
    return np.where(reference == 0.0, np.where(candidate == 0.0, 0.0, np.inf), rel)
    rel = np.abs((candidate - reference) / reference)
    return rel


# def fermi_occupation_mu_beta(E: np.ndarray, mu: float, beta: float) -> np.ndarray:
#     """Stable f(E) = 1/(exp(beta(E-mu)) + 1)."""

#     a = beta * (np.asarray(E, dtype=float) - mu)
#     return np.exp(-np.logaddexp(0.0, a))


# def fermi_hole_mu_beta(E: np.ndarray, mu: float, beta: float) -> np.ndarray:
#     """Stable 1 - f(E)."""

#     a = beta * (np.asarray(E, dtype=float) - mu)
#     return np.exp(a - np.logaddexp(0.0, a))


# def fermi_product_mu_beta(E: np.ndarray, hw: float, mu: float, beta: float) -> np.ndarray:
#     """Stable f(E+hw)[1-f(E)] (log-form)."""

#     E = np.asarray(E, dtype=float)
#     a = beta * (E - mu)
#     b = a + beta * hw
#     log_val = a - np.logaddexp(0.0, a) - np.logaddexp(0.0, b)
#     return np.exp(log_val)

# Fermi-Dirac occupation number
def f_T(E, T):
    mu = chemical_potential(T)
    beta = 1.0 / (k_B * T)
    exp_E = np.exp(beta * (E - mu))
    return 1.0 / (exp_E + 1)

# Bose-Einstein occupation number
def n_B(hw, T):
    beta = 1.0 / (k_B * T)
    with np.errstate(over="ignore"):
        exp_arg = beta * hw
        return 1.0 / (np.expm1(exp_arg))


def F_T(E, hw, T, E_F):
    # Explicitly compute f(E+hw)[1-f(E)] without subtracting from 1:
    #   f(E + hw)[1 - f(E)] = exp(beta*(E-mu)) / ((exp(beta*(E-mu)) + 1)(exp(beta*(E+hw-mu)) + 1))
    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)
    exp_E = np.exp(beta * (E - mu))
    exp_hw = np.exp(beta * hw)
    return exp_E / ((exp_E + 1) * (exp_E * exp_hw + 1))





# def make_energy_grid_simpson(
#     dE_max: float,
#     *,
#     E_min: float = E_MIN,
#     E_max: float = E_MAX,
# ) -> tuple[np.ndarray, float]:
#     """Return a uniform grid suitable for composite Simpson integration.

#     Picks an even number of intervals (odd number of points) and ensures the
#     resulting effective step size satisfies ΔE_eff <= dE_max.
#     """

#     if not np.isfinite(dE_max) or dE_max <= 0.0:
#         raise ValueError(f"dE_max must be a positive finite float, got {dE_max!r}")

#     n_intervals = int(np.ceil((E_max - E_min) / float(dE_max)))
#     if n_intervals % 2 == 1:
#         n_intervals += 1

#     E_grid = np.linspace(float(E_min), float(E_max), n_intervals + 1, dtype=float)
#     dE_eff = float(E_grid[1] - E_grid[0])
#     return E_grid, dE_eff


def mean_abs_relative_error(
    candidate: np.ndarray,
    reference: np.ndarray,
    *,
    reference_floor_ratio: float = 1e-12,
) -> float:
    """Mean |(candidate-reference)/reference|, excluding tiny reference values."""

    candidate = np.asarray(candidate, dtype=float)
    reference = np.asarray(reference, dtype=float)

    ref_scale = float(np.max(np.abs(reference)))
    if ref_scale == 0.0:
        return 0.0

    floor = float(reference_floor_ratio) * ref_scale
    mask = np.abs(reference) >= floor
    if not np.any(mask):
        return float("nan")

    rel = relative_error(candidate, reference)
    return float(np.mean(rel[mask]))


def integral_const_edos_exact(hw: np.ndarray, T: float, E_F: float) -> np.ndarray:
    """Analytic constant-eDOS result (exact, no k_B T approximation)."""

    hw = np.asarray(hw, dtype=float)
    mu = float(chemical_potential(float(E_F), float(T)))
    beta = 1.0 / (k_B * float(T))
    g_F = float(density_of_states(float(E_F)))

    x = beta * hw
    beta_mu = beta * mu
    term_mu = np.logaddexp(0.0, -beta_mu)
    term_hw_minus_mu = np.logaddexp(beta_mu, x) - beta_mu
    bracket = x + term_mu - term_hw_minus_mu
    # with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
    #     denom = np.expm1(x)
    #     f0 = 1.0 / (np.exp(-beta * mu) + 1.0)
    #     ratio = np.where(x == 0.0, f0, bracket / denom)
    return g_F**2 * k_B * float(T) * ratio


def integral_const_edos_approx(hw: np.ndarray, T: float, E_F: float) -> np.ndarray:
    """Low-(ħω,kBT) approximation of the constant-eDOS result."""

    hw = np.asarray(hw, dtype=float)
    beta = 1.0 / (k_B * float(T))
    g_F = float(density_of_states(float(E_F)))

    x = beta * hw
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        denom = np.expm1(x)
        ratio = np.where(x == 0.0, k_B * float(T), hw / denom)
    return g_F**2 * ratio


def _effective_batch_size(batch_size: int, n_E: int, *, max_points: int) -> int:
    if batch_size <= 0:
        raise ValueError(f"batch_size must be positive, got {batch_size}")
    n_E = int(n_E)
    max_points = int(max_points)
    return int(min(batch_size, max(1, max_points // max(1, n_E))))


def integral_const_edos_numeric(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    E_grid: np.ndarray | None = None,
    batch_size: int = 256,
    max_points: int = 3_000_000,
) -> np.ndarray:
    """Numeric constant-eDOS integral (Eq. 5) using a log-stable thermal factor."""

    hw_values = np.asarray(hw_values, dtype=float)
    E = E_GRID if E_grid is None else np.asarray(E_grid, dtype=float)
    batch_size_eff = _effective_batch_size(batch_size, E.size, max_points=max_points)

    mu = float(chemical_potential(float(E_F), float(T)))
    beta = 1.0 / (k_B * float(T))
    g_F = float(density_of_states(float(E_F)))

    a = beta * (E - mu)
    log_denom_a = np.logaddexp(0.0, a)

    out = np.empty_like(hw_values)

    # Local import keeps stage-0/1 usable without SciPy installed.
    from scipy.integrate import simpson  # type: ignore

    for start in range(0, hw_values.size, batch_size_eff):
        hw = hw_values[start : start + batch_size_eff]
        b = a[:, None] + beta * hw[None, :]
        log_val = a[:, None] - log_denom_a[:, None] - np.logaddexp(0.0, b)
        integrand = np.exp(log_val)
        out[start : start + hw.size] = g_F**2 * simpson(integrand, x=E, axis=0)

    return out


def integral_var_edos_numeric(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    E_grid: np.ndarray | None = None,
    batch_size: int = 128,
    max_points: int = 1_500_000,
) -> np.ndarray:
    """Numeric varying-eDOS integral (Eq. 4) using a log-stable thermal factor."""

    hw_values = np.asarray(hw_values, dtype=float)
    E = E_GRID if E_grid is None else np.asarray(E_grid, dtype=float)
    batch_size_eff = _effective_batch_size(batch_size, E.size, max_points=max_points)

    mu = float(chemical_potential(float(E_F), float(T)))
    beta = 1.0 / (k_B * float(T))

    a = beta * (E - mu)
    log_denom_a = np.logaddexp(0.0, a)
    g_E = density_of_states(E).astype(float, copy=False)

    out = np.empty_like(hw_values)

    from scipy.integrate import simpson  # type: ignore

    for start in range(0, hw_values.size, batch_size_eff):
        hw = hw_values[start : start + batch_size_eff]
        b = a[:, None] + beta * hw[None, :]
        log_val = a[:, None] - log_denom_a[:, None] - np.logaddexp(0.0, b)
        thermal = np.exp(log_val)
        g_Ep = density_of_states(E[:, None] + hw[None, :])
        integrand = thermal * g_E[:, None] * g_Ep
        out[start : start + hw.size] = simpson(integrand, x=E, axis=0)

    return out
