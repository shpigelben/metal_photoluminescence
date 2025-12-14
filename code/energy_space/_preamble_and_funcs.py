"""
Shared constants and utility functions for energy-space scripts.
"""

from __future__ import annotations
import numpy as np

# Physical constants (energy in eV)
k_B = 8.617333262145e-5  # eV/K
hbar = 6.582119569e-16
m_e = 5.485e-4

# Default simulation parameters
E_F_DEFAULT = 3.0
E_MIN = 0.0
E_MAX = 10.0
D_E = 1e-3
E_GRID = np.arange(E_MIN, E_MAX + D_E, D_E)

EMISSION_ENERGY_MIN = 0.01
EMISSION_ENERGY_MAX = 8.0
N_EMISSION = 2000
E_EM_VALUES = np.linspace(EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, N_EMISSION)


def chemical_potential(E_F: float, T: float) -> float:
    T_F = E_F / k_B
    return E_F * (1 - (np.pi**2 / 12) * ((T / T_F) ** 2))


def density_of_states(E: float | np.ndarray) -> float | np.ndarray:
    return ((m_e ** 1.5) / (np.pi ** 2 * hbar ** 3)) * np.sqrt(2 * E)


def relative_error(candidate: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """Elementwise |(candidate-reference)/reference|, with 0/0 -> 0."""

    candidate = np.asarray(candidate, dtype=float)
    reference = np.asarray(reference, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.abs((candidate - reference) / reference)
    return np.where(reference == 0.0, np.where(candidate == 0.0, 0.0, np.inf), rel)


def fermi_occupation_mu_beta(E: np.ndarray, mu: float, beta: float) -> np.ndarray:
    """Stable f(E) = 1/(exp(beta(E-mu)) + 1)."""

    a = beta * (np.asarray(E, dtype=float) - mu)
    return np.exp(-np.logaddexp(0.0, a))


def fermi_hole_mu_beta(E: np.ndarray, mu: float, beta: float) -> np.ndarray:
    """Stable 1 - f(E)."""

    a = beta * (np.asarray(E, dtype=float) - mu)
    return np.exp(a - np.logaddexp(0.0, a))


def fermi_product_mu_beta(E: np.ndarray, hw: float, mu: float, beta: float) -> np.ndarray:
    """Stable f(E+hw)[1-f(E)] (log-form)."""

    E = np.asarray(E, dtype=float)
    a = beta * (E - mu)
    b = a + beta * hw
    log_val = a - np.logaddexp(0.0, a) - np.logaddexp(0.0, b)
    return np.exp(log_val)
