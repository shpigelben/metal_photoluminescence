"""
Stage 3 - Constant eDOS Approximation (energy space)

Compares Eq. (4) ↔ Eq. (5) from `docs/notes/0 - Work Plan.md`:

  Eq. (4): I_var(hw)   = ∫ f(E+hw)[1-f(E)] g(E+hw) g(E) dE
  Eq. (5): I_const(hw) = g(E_F)^2 ∫ f(E+hw)[1-f(E)] dE

The constant-eDOS approximation is expected to work when the contributing energies
stay close to μ (roughly: max(hw, kBT) << E_F), and to degrade as hw approaches μ,
because the T→0 support expands from [μ-hw, μ] and samples far below E_F.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

# Allow importing shared plotting style from ../plot_style.py when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _preamble_and_funcs import (  # noqa: E402
    E_EM_VALUES,
    E_F_DEFAULT,
    E_GRID,
    chemical_potential,
    density_of_states,
    k_B,
    relative_error,
)
from plot_style import apply_style, save_svg, set_figure_title  # noqa: E402


def I_numeric_const_eDOS_sweep(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    batch_size: int = 256,
) -> np.ndarray:
    """Numeric Eq. (5): constant eDOS = g(E_F)^2 using a log-stable integrand."""

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


def I_numeric_var_eDOS_sweep(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    batch_size: int = 128,
) -> np.ndarray:
    """Numeric Eq. (4): varying eDOS g(E) g(E+hw) using a log-stable thermal factor."""

    hw_values = np.asarray(hw_values, dtype=float)
    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)

    a = beta * (E_GRID - mu)
    log_denom_a = np.logaddexp(0.0, a)
    g_E = density_of_states(E_GRID).astype(float, copy=False)

    out = np.empty_like(hw_values)
    for start in range(0, hw_values.size, batch_size):
        hw = hw_values[start : start + batch_size]
        b = a[:, None] + beta * hw[None, :]
        log_val = a[:, None] - log_denom_a[:, None] - np.logaddexp(0.0, b)
        thermal = np.exp(log_val)
        g_Ep = density_of_states(E_GRID[:, None] + hw[None, :])
        integrand = thermal * g_E[:, None] * g_Ep
        out[start : start + hw.size] = simpson(integrand, x=E_GRID, axis=0)

    return out


def rel_error_const_edos_vs_var(hw_values: np.ndarray, T: float, E_F: float) -> np.ndarray:
    """Relative error of Eq. (5) approximation using Eq. (4) as reference."""

    I_const = I_numeric_const_eDOS_sweep(hw_values, T, E_F)
    I_var = I_numeric_var_eDOS_sweep(hw_values, T, E_F)
    return relative_error(I_const, I_var)


REL_ERROR_CASES = [
    {"T": 300.0, "E_F": 5.0, "title": "T = 300 K, E_F = 5 eV"},
    {"T": 300.0, "E_F": 3.0, "title": "T = 300 K, E_F = 3 eV"},
    {"T": 700.0, "E_F": 3.0, "title": "T = 700 K, E_F = 3 eV"},
    {"T": 1000.0, "E_F": 3.0, "title": "T = 1000 K, E_F = 3 eV"},
]


def show_rel_error_grid(*, hw_values: np.ndarray = E_EM_VALUES) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True, sharey=True)
    for ax, case in zip(axes.flat, REL_ERROR_CASES):
        T = float(case["T"])
        E_F = float(case["E_F"])
        mu = chemical_potential(E_F, T)

        rel = rel_error_const_edos_vs_var(hw_values, T, E_F)

        ax.semilogy(hw_values, np.clip(rel, 1e-20, None), color="C0")
        ax.axvline(mu, color="k", linestyle="--", alpha=0.4, linewidth=1.0, label=r"$\mu$")
        ax.set_title(str(case["title"]))
        ax.set_xlim(float(hw_values[0]), float(hw_values[-1]))
        ax.set_ylim(1e-20, 1.0)
        ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)

    axes[1, 0].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[1, 1].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[0, 0].set_ylabel(r"$|\delta_{rel}|$")
    axes[1, 0].set_ylabel(r"$|\delta_{rel}|$")

    title = "Constant eDOS approximation: relative error (Eq. (5) vs Eq. (4))"
    set_figure_title(fig, title)
    save_svg(fig, "stage_3_rel_error_grid.svg")
    plt.show()


if __name__ == "__main__":
    apply_style()
    show_rel_error_grid()
