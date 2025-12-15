"""
Stage 2 - Numeric Convergence (energy space)
Derived from docs/notes/2 - Numeric Convergence.md.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import sys
from pathlib import Path

# Allow importing shared plotting style from ../plot_style.py when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _preamble_and_funcs import *
from plot_style import *


def make_energy_grid_simpson(
    dE_max: float, *, E_min: float = E_MIN, E_max: float = E_MAX
) -> tuple[np.ndarray, float]:
    """Return a uniform grid suitable for Simpson integration.

    Uses an even number of intervals (odd number of points) and guarantees
    the effective step is <= dE_max.
    """

    if not np.isfinite(dE_max) or dE_max <= 0.0:
        raise ValueError(f"dE_max must be a positive finite float, got {dE_max!r}")

    n_intervals = int(np.ceil((E_max - E_min) / float(dE_max)))
    if n_intervals % 2 == 1:
        n_intervals += 1  # Simpson prefers an even number of intervals

    E_grid = np.linspace(E_min, E_max, n_intervals + 1, dtype=float)
    dE_eff = float(E_grid[1] - E_grid[0])
    return E_grid, dE_eff


def I_numeric_const_eDOS_sweep(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    E_grid: np.ndarray | None = None,
    batch_size: int = 256,
) -> np.ndarray:
    """Numeric Eq. (4) with constant eDOS = g(E_F)^2 using a log-stable integrand."""

    hw_values = np.asarray(hw_values, dtype=float)
    E = E_GRID if E_grid is None else np.asarray(E_grid, dtype=float)
    n_E = int(E.size)
    max_points = 3_000_000  # controls peak temporary allocations (~O(n_E * batch_size))
    batch_size_eff = int(min(batch_size, max(1, max_points // max(1, n_E))))

    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)
    g_F = density_of_states(E_F)

    a = beta * (E - mu)
    log_denom_a = np.logaddexp(0.0, a)

    out = np.empty_like(hw_values)
    for start in range(0, hw_values.size, batch_size_eff):
        hw = hw_values[start : start + batch_size_eff]
        b = a[:, None] + beta * hw[None, :]
        log_val = a[:, None] - log_denom_a[:, None] - np.logaddexp(0.0, b)
        integrand = np.exp(log_val)
        out[start : start + hw.size] = g_F**2 * simpson(integrand, x=E, axis=0)

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


def rel_error_numeric_vs_exact(
    hw_values: np.ndarray, T: float, E_F: float, *, E_grid: np.ndarray | None = None
) -> np.ndarray:
    I_num = I_numeric_const_eDOS_sweep(hw_values, T, E_F, E_grid=E_grid)
    I_exact = I_analytic_const_eDOS_exact(hw_values, T, E_F)
    return relative_error(I_num, I_exact)


REL_ERROR_CASES = [
    {"T": 300.0, "E_F": 5.0, "title": "T = 300 K, E_F = 5 eV"},
    {"T": 300.0, "E_F": 3.0, "title": "T = 300 K, E_F = 3 eV"},
    {"T": 700.0, "E_F": 3.0, "title": "T = 700 K, E_F = 3 eV"},
    {"T": 1000.0, "E_F": 3.0, "title": "T = 1000 K, E_F = 3 eV"},
]


def mean_abs_rel_error_numeric_vs_exact(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    E_grid: np.ndarray,
    reference_floor_ratio: float = 1e-12,
) -> float:
    """Mean |δ_rel| over the hw range (ignoring vanishing reference values)."""

    I_num = I_numeric_const_eDOS_sweep(hw_values, T, E_F, E_grid=E_grid)
    I_exact = I_analytic_const_eDOS_exact(hw_values, T, E_F)

    ref_scale = float(np.max(np.abs(I_exact)))
    if ref_scale == 0.0:
        return 0.0

    floor = reference_floor_ratio * ref_scale
    mask = np.abs(I_exact) >= floor
    if not np.any(mask):
        return float("nan")

    rel = relative_error(I_num, I_exact)
    return float(np.mean(rel[mask]))


def show_convergence_mean_rel_error_vs_dE(
    *,
    hw_values: np.ndarray | None = None,
    candidate_dE: np.ndarray | None = None,
    reference_floor_ratio: float = 1e-12,
) -> None:
    """Plot ⟨|δ_rel|⟩_{hw} vs integration step ΔE."""

    if hw_values is None:
        # Subsample for speed while still covering the full hw range.
        hw_values = E_EM_VALUES[::5]
    else:
        hw_values = np.asarray(hw_values, dtype=float)

    if candidate_dE is None:
        candidate_dE = np.linspace(5e-3, 1e-1, 20)[::-1]
    else:
        candidate_dE = np.asarray(candidate_dE, dtype=float)
    candidate_dE = np.sort(candidate_dE)[::-1]

    dE_eff_values = np.empty_like(candidate_dE, dtype=float)
    mean_err_by_case = np.empty((candidate_dE.size, len(REL_ERROR_CASES)), dtype=float)

    for i, dE in enumerate(candidate_dE):
        E_grid, dE_eff = make_energy_grid_simpson(float(dE))
        dE_eff_values[i] = dE_eff
        for j, case in enumerate(REL_ERROR_CASES):
            T = float(case["T"])
            E_F = float(case["E_F"])
            mean_err_by_case[i, j] = mean_abs_rel_error_numeric_vs_exact(
                hw_values,
                T,
                E_F,
                E_grid=E_grid,
                reference_floor_ratio=reference_floor_ratio,
            )

    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    for j, case in enumerate(REL_ERROR_CASES):
        ax.loglog(
            dE_eff_values,
            mean_err_by_case[:, j],
            marker="o",
            markersize=4,
            label=str(case["title"]),
        )

    worst = np.nanmax(mean_err_by_case, axis=1)
    ax.loglog(dE_eff_values, worst, color="k", linewidth=2.0, label="max over cases")

    ax.set_xlabel(r"$\Delta \mathcal{E}$ [eV]")
    ax.set_ylabel(r"$\langle |\delta_{rel}| \rangle_{\hbar\omega}$")
    ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)
    ax.set_xlim(float(np.max(dE_eff_values)), float(np.min(dE_eff_values)))
    ax.set_ylim(1e-20, 1.0)
    ax.legend()

    title = r"Integration-step convergence: $\langle |\delta_{rel}| \rangle_{\hbar\omega}$ vs $\Delta\mathcal{E}$"
    set_figure_title(fig, title)
    save_svg(fig, "stage_2_convergence_mean_rel_error_vs_dE.svg")
    plt.show()


def show_rel_error_grid() -> None:
    dE_used = float(E_GRID[1] - E_GRID[0])
    fig, axes = plt.subplots(2, 2, figsize=(11, 5), sharex=True, sharey=True)
    for ax, case in zip(axes.flat, REL_ERROR_CASES):
        T = float(case["T"])
        E_F = float(case["E_F"])
        rel = rel_error_numeric_vs_exact(E_EM_VALUES, T, E_F)

        ax.semilogy(E_EM_VALUES, np.clip(rel, 1e-20, None), color="C0")
        ax.set_title(str(case["title"]))
        ax.set_xlim(float(E_EM_VALUES[0]), float(E_EM_VALUES[-1]))
        ax.set_ylim(1e-16, 1e-10)
        ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)

    axes[1, 0].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[1, 1].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[0, 0].set_ylabel(r"$|\delta_{rel}|$")
    axes[1, 0].set_ylabel(r"$|\delta_{rel}|$")

    title = f"Const eDOS: relative error (numeric integral vs analytic exact), ΔE≈{dE_used:.2e} eV"
    set_figure_title(fig, title)
    save_svg(fig, "stage_2_rel_error_grid.svg")
    plt.show()


if __name__ == "__main__":
    apply_style()
    show_convergence_mean_rel_error_vs_dE()
    show_rel_error_grid()
