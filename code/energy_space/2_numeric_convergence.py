"""
Stage 2 - Numeric Convergence (energy space)
Derived from docs/notes/2 - Numeric Convergence.md.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import sys
from pathlib import Path

# Allow importing shared plotting style from ../plot_style.py when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _preamble_and_funcs import *
from plot_style import *

def I_numeric_const_eDOS_sweep(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    batch_size: int = 256,
) -> np.ndarray:
    """Numeric Eq. (4) with constant eDOS = g(E_F)^2 using a log-stable integrand."""

    hw_values = np.asarray(hw_values, dtype=float)

    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)
    g_F = density_of_states(E_F)

    a = beta * (E_GRID - mu)
    log_denom_a = np.logaddexp(0.0, a)

    out = np.empty_like(hw_values)
    for start in range(0, hw_values.size, batch_size):
        hw = hw_values[start : start + batch_size]
        b = a[:, None] + beta * hw[None, :]
        log_val = a[:, None] - log_denom_a[:, None] - np.logaddexp(0.0, b)
        integrand = np.exp(log_val)
        out[start : start + hw.size] = g_F**2 * simpson(integrand, x=E_GRID, axis=0)

    return out


def I_analytic_const_eDOS_exact(hw: np.ndarray, T: float, E_F: float) -> np.ndarray:
    """Analytic constant-eDOS result (exact, no k_B T approximation)."""

    hw = np.asarray(hw, dtype=float)
    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)
    g_F = density_of_states(E_F)

    x = beta * hw
    bracket = x + np.logaddexp(0.0, -beta * mu) - np.logaddexp(0.0, beta * (hw - mu))
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        denom = np.expm1(x)
        f0 = 1.0 / (np.exp(-beta * mu) + 1.0)
        ratio = np.where(x == 0.0, f0, bracket / denom)
    return g_F**2 * k_B * T * ratio


def rel_error_numeric_vs_exact(hw_values: np.ndarray, T: float, E_F: float) -> np.ndarray:
    I_num = I_numeric_const_eDOS_sweep(hw_values, T, E_F)
    I_exact = I_analytic_const_eDOS_exact(hw_values, T, E_F)
    return relative_error(I_num, I_exact)


REL_ERROR_CASES = [
    {"T": 300.0, "E_F": 5.0, "title": "T = 300 K, E_F = 5 eV"},
    {"T": 300.0, "E_F": 3.0, "title": "T = 300 K, E_F = 3 eV"},
    {"T": 700.0, "E_F": 3.0, "title": "T = 700 K, E_F = 3 eV"},
    {"T": 1000.0, "E_F": 3.0, "title": "T = 1000 K, E_F = 3 eV"},
]

def show_rel_error_grid() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True, sharey=True)
    for ax, case in zip(axes.flat, REL_ERROR_CASES):
        T = float(case["T"])
        E_F = float(case["E_F"])
        rel = rel_error_numeric_vs_exact(E_EM_VALUES, T, E_F)

        ax.semilogy(E_EM_VALUES, np.clip(rel, 1e-20, None), color="C0")
        ax.set_title(str(case["title"]))
        ax.set_xlim(0.0, float(E_EM_VALUES[-1]))
        ax.set_ylim(1e-20, 1.0)
        ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)

    axes[1, 0].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[1, 1].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[0, 0].set_ylabel(r"$|\delta_{rel}|$")
    axes[1, 0].set_ylabel(r"$|\delta_{rel}|$")

    title = "Const eDOS: relative error (numeric integral vs analytic exact)"
    set_figure_title(fig, title)
    save_svg(fig, "stage_2_rel_error_grid.svg")
    plt.show()


if __name__ == "__main__":
    apply_style()
    show_rel_error_grid()
