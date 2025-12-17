"""
Stage 3 - Constant eDOS Approximation (energy space)

Compares the constant-eDOS approximation (Eq. 5) against the varying-eDOS
reference (Eq. 4) from `docs/notes/0 - Work Plan.md`.
"""

import matplotlib.pyplot as plt
import numpy as np

from _preamble_and_funcs import (
    E_EM_VALUES,
    E_F_DEFAULT,
    E_GRID,
    E_MAX,
    E_MIN,
    chemical_potential,
    density_of_states,
    integral_const_edos_numeric,
    integral_var_edos_numeric,
    relative_error,
)
from plot_style import apply_style, save_svg, set_figure_title


def rel_error_const_edos_vs_var(hw_values: np.ndarray, T: float, E_F: float) -> np.ndarray:
    """Relative error of Eq. (5) approximation using Eq. (4) as reference."""

    I_const = integral_const_edos_numeric(hw_values, T, E_F)
    I_var = integral_var_edos_numeric(hw_values, T, E_F)
    return relative_error(I_const, I_var)


def rel_error_edos_vs_const_edos(
    E_values: np.ndarray,
    hw_values: np.ndarray,
    *,
    E_F: float,
) -> np.ndarray:
    """Pointwise relative error of the eDOS product vs constant-eDOS.

    Computes |(ρ(E+ħω)ρ(E) - ρ(E_F)^2) / (ρ(E+ħω)ρ(E))| on a (ħω, E) grid.
    The returned array has shape (len(hw_values), len(E_values)).
    """

    E_values = np.asarray(E_values, dtype=float)
    hw_values = np.asarray(hw_values, dtype=float)

    E = E_values[None, :]  # (1, n_E)
    hw = hw_values[:, None]  # (n_hw, 1)

    rho_E = density_of_states(E)
    rho_Ep = density_of_states(E + hw)
    product = rho_E * rho_Ep
    rho_F2 = float(density_of_states(float(E_F)) ** 2)

    with np.errstate(divide="ignore", invalid="ignore"):
        delta = np.abs((product - rho_F2) / product)
    return np.where(product == 0.0, np.nan, delta)


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


def show_edos_vs_const_edos_heatmap(
    *,
    E_F: float = E_F_DEFAULT,
    n_E: int = 500,
    n_hw: int = 500,
    E_min: float | None = None,
    E_max: float | None = None,
    hw_min: float | None = None,
    hw_max: float | None = None,
) -> None:
    """Heatmap of δ_rel(E, ħω) for ρ(E)ρ(E+ħω) vs ρ(E_F)^2."""

    E_lo = float(E_MIN) if E_min is None else float(E_min)
    E_hi = float(E_MAX) if E_max is None else float(E_max)
    if E_lo < 0.0:
        raise ValueError(f"E_min must be >= 0, got {E_lo}")

    hw_lo = float(E_EM_VALUES[0]) if hw_min is None else float(hw_min)
    hw_hi = float(E_EM_VALUES[-1]) if hw_max is None else float(hw_max)

    # Avoid the E=0 singularity (rho(E)=0) by nudging the lower limit.
    if E_lo == 0.0:
        E_lo = float(E_GRID[1])

    E_values = np.linspace(E_lo, E_hi, int(n_E))
    hw_values = np.linspace(hw_lo, hw_hi, int(n_hw))

    delta = rel_error_edos_vs_const_edos(E_values, hw_values, E_F=E_F)
    delta_masked = np.ma.array(delta, mask=~np.isfinite(delta))
    log_delta = np.ma.log10(np.ma.clip(delta_masked, 1e-20, None))

    log_vals = log_delta.compressed()
    if log_vals.size == 0:
        raise RuntimeError("No finite δ_rel values to plot (all points masked).")

    vmin = float(np.floor(np.min(log_vals)))
    vmax = float(np.ceil(np.max(log_vals)))
    if vmin == vmax:
        vmin -= 1.0
        vmax += 1.0

    span = vmax - vmin
    if span <= 6:
        tick_step = 1.0
    elif span <= 12:
        tick_step = 2.0
    elif span <= 24:
        tick_step = 4.0
    else:
        tick_step = 8.0
    ticks = np.arange(vmin, vmax + 0.5 * tick_step, tick_step)

    fig, ax = plt.subplots(figsize=(10.8, 5.6))
    im = ax.imshow(
        log_delta,
        origin="lower",
        aspect="auto",
        extent=(E_values[0], E_values[-1], hw_values[0], hw_values[-1]),
        cmap="RdYlGn_r",
        vmin=vmin,
        vmax=vmax,
        interpolation="nearest",
    )
    fig.colorbar(im, ax=ax, pad=0.12, ticks=ticks, label=r"$\log_{10}|\delta_{rel}|$")

    ax.set_xlabel(r"$\mathcal{E}$ [eV]")
    ax.set_ylabel(r"$\hbar\omega$ [eV]")
    ax.set_xlim(E_values[0], E_values[-1])
    ax.set_ylim(hw_values[0], hw_values[-1])
    ax.grid(False)

    title = rf"$|\delta_{{rel}}(\mathcal{{E}},\hbar\omega)|$ for $\rho(\mathcal{{E}})\rho(\mathcal{{E}}+\hbar\omega)$ vs $\rho^2(\mathcal{{E}}_F)$ (E_F={E_F:.2f} eV)"
    set_figure_title(fig, title)
    save_svg(fig, "stage_3_edos_vs_const_edos_heatmap.svg")
    plt.show()


if __name__ == "__main__":
    apply_style()
    show_rel_error_grid()
    show_edos_vs_const_edos_heatmap()
