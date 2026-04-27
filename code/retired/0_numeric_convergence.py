import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson, trapezoid

from _preamble_and_funcs import *
from code.misc.plot_style import apply_style, save_svg

_INTEGRATORS = {"simpson": simpson, "trapz": trapezoid}


def _save(fig, save_name: str | None, default_name: str) -> None:
    if save_name is None:
        return
    save_svg(fig, default_name if save_name == "auto" else save_name)


def _add_kbt_axis(ax):
    secax = ax.secondary_yaxis(
        "right", functions=(lambda t: k_B * t, lambda e: e / k_B)
    )
    secax.set_ylabel(r"$k_B T$ [eV]")
    return secax


def I6(hw, T):
    mu = chemical_potential(T)
    beta_T = beta(T)
    log1pa = np.logaddexp(0.0, -beta_T * mu)
    log1pb = np.logaddexp(0.0, beta_T * (hw - mu))
    return n_B(hw, T) * (hw + (k_B * T) * (log1pa - log1pb))


def I5(
    hw, T, method: str = "simpson", *, E_grid: np.ndarray | None = None
) -> np.ndarray:
    if E_grid is None:
        E_grid = E_GRID
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    integrator = _INTEGRATORS.get(method)
    if integrator is None:
        raise ValueError(f"Unknown integrator '{method}'.")
    return integrator(F_T(E_grid + hw, E_grid, T), E_grid, axis=-1)


def plot_heatmap(*, save_name: str | None = "auto"):
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]

    I6_2d = I6(hw, T)

    fig, axes = plt.subplots(
        1, 2, figsize=(13.5, 6.0), sharex=True, sharey=True, layout="constrained"
    )
    mappable = None
    for ax, method, title in zip(
        axes, ("trapz", "simpson"), ("Trapezoid", "Simpson")
    ):
        rel = relative_error(I5(hw, T, method=method), I6_2d)
        mappable = ax.pcolormesh(
            E_EM_VALUES,
            T_VALUES,
            rel,
            shading="auto",
            cmap="coolwarm",
            vmin=-16,
            vmax=0,
        )
        ax.set_title(title)
        ax.set_xlabel(r"$\hbar\omega$ [eV]")

    axes[0].set_ylabel(r"$T$ [K]")
    _add_kbt_axis(axes[1])

    dE = float(E_GRID[1] - E_GRID[0]) if E_GRID.size > 1 else float("nan")
    fig.colorbar(
        mappable, ax=axes, label=r"$\log_{10}|\delta_{rel}|$", pad=0.10
    )
    fig.suptitle(
        "Numerical integration (Eq. 5 vs Eq. 6)\n"
        f"Integration over $E\\in[{E_GRID[0]:.2f},{E_GRID[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV",
        y=1.12,
    )
    _save(fig, save_name, "stage_2_rel_error_grid.png")
    plt.show()
 

def plot_heatmap_50x50(
    *,
    E_min: float = E_MIN,
    E_max: float = E_MAX,
    dE: float = 1e-4,
    save_name: str | None = "auto",
):
    hw_vals = np.linspace(EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, 50)
    T_vals = np.linspace(T_MIN, T_MAX, 50)
    E_grid = np.arange(E_min, E_max + dE, dE)
    if E_grid.size < 2:
        raise ValueError("E_min/E_max/dE must define at least two grid points.")

    rel = np.empty((T_vals.size, hw_vals.size), dtype=float)
    for i, T_val in enumerate(T_vals):
        rel[i] = relative_error(
            I5(hw_vals, T_val, E_grid=E_grid), I6(hw_vals, T_val)
        )

    fig, ax = plt.subplots(figsize=(8.5, 6.0))
    m = ax.pcolormesh(
        hw_vals,
        T_vals,
        rel,
        shading="auto",
        cmap="coolwarm",
        vmin=-16,
        vmax=0,
    )
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$T_e$ [K]")
    _add_kbt_axis(ax)
    fig.colorbar(m, ax=ax, pad=0.10, label=r"$\log_{10}|\delta_{rel}|$")

    title = (
        "Relative error heatmap (Simpson, Eq. 5 vs Eq. 6)\n"
        f"$E\\in[{E_min:.2f},{E_max:.2f}]$ eV; $\\Delta E$={dE:.1e} eV"
    )
    ax.set_title(title)

    _save(fig, save_name, "stage_2_rel_error_grid_50x50.png")
    plt.show()


def _plot_convergence(
    hw_values: np.ndarray,
    T: float,
    grids: list[np.ndarray],
    labels: list[str],
    *,
    title: str,
    ylim: tuple[float, float],
    save_name: str | None,
    default_name: str,
) -> None:
    I6_ref = I6(hw_values, T)

    fig, axes = plt.subplots(
        len(grids), 1, figsize=(8.0, 6.0), sharex=True, sharey=True
    )
    for ax, grid, label in zip(axes, grids, labels):
        rel = relative_error(I5(hw_values, T, E_grid=grid), I6_ref)
        ax.plot(hw_values, rel, label=label, alpha=0.8)
        ax.legend(loc="right")

    fig.supylabel(r"$\log_{10}|\delta_{rel}|$")
    fig.supxlabel(r"$\hbar\omega$ [eV]")
    axes[-1].set_ylim(*ylim)
    axes[-1].set_xlim(hw_values[0], hw_values[-1])
    fig.suptitle(title)
    _save(fig, save_name, default_name)
    plt.show()


def plot_step_convergence(T: float = 300.0, *, save_name: str | None = "auto"):
    hw_values = np.linspace(3, 7, 500)
    steps = [4e-3, 1e-3, 4e-4, 1e-4]
    grids = [np.arange(E_MIN, E_MAX + dE, dE) for dE in steps]
    labels = [rf"$\Delta E$={dE:.0e} eV" for dE in steps]
    title = (
        "Step-size convergence (Simpson, Eq. 5 vs Eq. 6)\n"
        f"$T$={T:.0f} K; integration over $E\\in[{E_MIN:.2f},{E_MAX:.2f}]$ eV "
        "with varying $\\Delta E$"
    )
    _plot_convergence(
        hw_values,
        T,
        grids,
        labels,
        title=title,
        ylim=(-17, -9),
        save_name=save_name,
        default_name=f"stage_2_step_convergence_T{int(round(T))}K.png",
    )


def plot_length_convergence(T: float = 300.0, *, save_name: str | None = "auto"):
    hw_values = np.linspace(4, 6, 500)
    lengths = [5.5, 5.6, 5.7, 5.8]
    grids = [np.arange(0, L, D_E) for L in lengths]
    labels = [rf"$E\in[0,{L}]$ eV" for L in lengths]

    title = (
        "Integration-interval convergence (Simpson, Eq. 5 vs Eq. 6)\n"
        f"$T$={T:.0f} K; $\\Delta E$={D_E:.1e} eV; integration interval varies"
    )
    _plot_convergence(
        hw_values,
        T,
        grids,
        labels,
        title=title,
        ylim=(-17, -10),
        save_name=save_name,
        default_name=f"stage_2_length_convergence_T{int(round(T))}K.png",
    )


if __name__ == "__main__":
    apply_style()
    plot_heatmap()
    plot_heatmap_50x50()
    plot_step_convergence(300.0)
    plot_length_convergence(300.0)
