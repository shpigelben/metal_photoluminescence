import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

from _preamble_and_funcs import E_F, E_GRID, F_T, eDOS, f_neq, k_B, relative_error
from plot_style import apply_style, save_svg, set_figure_title

DEFAULT_HW_L = 2.0
DEFAULT_DELTA_E = 1e-2
E_EM_VALUES = np.linspace(0.1, 8.0, 200)
T_VALUES = np.linspace(100.0, 2000.0, 100)


def _use_grid(E_grid: np.ndarray | None) -> np.ndarray:
    E_grid = E_GRID if E_grid is None else np.asarray(E_grid)
    if E_grid.size < 2:
        raise ValueError("E_grid must contain at least two points.")
    return E_grid


def _grid_stats(E_grid: np.ndarray) -> tuple[float, float, float]:
    dE = float(E_grid[1] - E_grid[0]) if E_grid.size > 1 else float("nan")
    return float(E_grid[0]), float(E_grid[-1]), dE


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


def _emission(
    hw,
    T,
    *,
    const_edos: bool,
    nonthermal: bool = False,
    hw_L: float | None = None,
    delta_E: float | None = None,
    E_grid: np.ndarray | None = None,
) -> np.ndarray:
    E_grid = _use_grid(E_grid)
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]

    if nonthermal:
        if hw_L is None or delta_E is None:
            raise ValueError("hw_L and delta_E are required for nonthermal emission.")
        f1 = f_neq(E_grid + hw, T, hw_L=hw_L, delta_E=delta_E)
        f2 = f_neq(E_grid, T, hw_L=hw_L, delta_E=delta_E)
        factor = f1 * (1 - f2)
    else:
        factor = F_T(E_grid + hw, E_grid, T)

    if const_edos:
        g1 = g2 = eDOS(E_F)
    else:
        g1 = eDOS(E_grid)
        g2 = eDOS(E_grid + hw)

    return simpson(g1 * g2 * factor, E_grid, axis=-1)


def I5(hw, T, *, E_grid: np.ndarray | None = None) -> np.ndarray:
    return _emission(hw, T, const_edos=True, E_grid=E_grid)


def I4(hw, T, *, E_grid: np.ndarray | None = None) -> np.ndarray:
    return _emission(hw, T, const_edos=False, E_grid=E_grid)


def I5_nonthermal(
    hw,
    T,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
) -> np.ndarray:
    return _emission(
        hw,
        T,
        const_edos=True,
        nonthermal=True,
        hw_L=hw_L,
        delta_E=delta_E,
        E_grid=E_grid,
    )


def I4_nonthermal(
    hw,
    T,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
) -> np.ndarray:
    return _emission(
        hw,
        T,
        const_edos=False,
        nonthermal=True,
        hw_L=hw_L,
        delta_E=delta_E,
        E_grid=E_grid,
    )


def heatmap(*, save_name: str | None = "auto") -> None:
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]
    rel = relative_error(I5(hw, T), I4(hw, T))

    fig, ax = plt.subplots(figsize=(8.5, 6.0))
    m = ax.pcolormesh(
        E_EM_VALUES, T_VALUES, rel, shading="auto", cmap="coolwarm", vmin=-8, vmax=0
    )
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$T$ [K]")
    _add_kbt_axis(ax)
    fig.colorbar(m, ax=ax, pad=0.12, label=r"$\log_{10}|\delta_{rel}|$")

    E_grid = _use_grid(None)
    e_min, e_max, dE = _grid_stats(E_grid)
    title = (
        "Constant eDOS approximation (Eq. 5 vs Eq. 4)\n"
        f"Simpson integration over $E\\in[{e_min:.2f},{e_max:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    ax.set_title(title)
    _save(fig, save_name, "stage_3_edos_vs_const_edos_heatmap.png")
    plt.show()


def rel_T(T: float, *, save_name: str | None = "auto") -> None:
    rel = relative_error(I5(E_EM_VALUES, T), I4(E_EM_VALUES, T))

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(E_EM_VALUES, rel)
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$\log_{10}|\delta_{rel}|$")
    ax.set_xlim(E_EM_VALUES[0], E_EM_VALUES[-1])

    E_grid = _use_grid(None)
    e_min, e_max, dE = _grid_stats(E_grid)
    title = (
        "Constant eDOS approximation (Eq. 5 vs Eq. 4)\n"
        f"$T$={T:.0f} K; Simpson integration over $E\\in[{e_min:.2f},{e_max:.2f}]$ eV "
        f"with $\\Delta E$={dE:.1e} eV"
    )
    ax.set_title(title)
    _save(fig, save_name, f"stage_3_rel_error_T{int(round(T))}K.png")
    plt.show()


def heatmap_nonthermal(
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
    save_name: str | None = "auto",
) -> None:
    E_grid = _use_grid(E_grid)
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]
    rel = relative_error(
        I5_nonthermal(hw, T, hw_L=hw_L, delta_E=delta_E, E_grid=E_grid),
        I4_nonthermal(hw, T, hw_L=hw_L, delta_E=delta_E, E_grid=E_grid),
    )

    fig, ax = plt.subplots(figsize=(8.5, 6.0))
    m = ax.pcolormesh(
        E_EM_VALUES, T_VALUES, rel, shading="auto", cmap="coolwarm", vmin=-8, vmax=0
    )
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$T$ [K]")
    _add_kbt_axis(ax)
    fig.colorbar(m, ax=ax, pad=0.12, label=r"$\log_{10}|\delta_{rel}|$")

    e_min, e_max, dE = _grid_stats(E_grid)
    title = (
        "Constant eDOS approximation (non-equilibrium, Eq. 5 vs Eq. 4)\n"
        f"hw_L={hw_L:.2f} eV; delta_E={delta_E:.2e}; "
        f"Simpson integration over $E\\in[{e_min:.2f},{e_max:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    ax.set_title(title)
    _save(fig, save_name, "stage_3_rel_error_nonthermal_heatmap.png")
    plt.show()


def rel_T_nonthermal(
    T: float,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
    save_name: str | None = "auto",
) -> None:
    E_grid = _use_grid(E_grid)
    rel = relative_error(
        I5_nonthermal(E_EM_VALUES, T, hw_L=hw_L, delta_E=delta_E, E_grid=E_grid),
        I4_nonthermal(E_EM_VALUES, T, hw_L=hw_L, delta_E=delta_E, E_grid=E_grid),
    )

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(E_EM_VALUES, rel)
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$\log_{10}|\delta_{rel}|$")
    ax.set_xlim(E_EM_VALUES[0], E_EM_VALUES[-1])

    e_min, e_max, dE = _grid_stats(E_grid)
    title = (
        "Constant eDOS approximation (non-equilibrium, Eq. 5 vs Eq. 4)\n"
        f"$T$={T:.0f} K; hw_L={hw_L:.2f} eV; delta_E={delta_E:.2e}; "
        f"Simpson integration over $E\\in[{e_min:.2f},{e_max:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    ax.set_title(title)
    _save(fig, save_name, f"stage_3_rel_error_nonthermal_T{int(round(T))}K.png")
    plt.show()


def plot_emission_log(
    T: float,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
    save_name: str | None = "auto",
) -> None:
    E_grid = _use_grid(E_grid)
    thermal = I4(E_EM_VALUES, T, E_grid=E_grid)
    non_eq = I4_nonthermal(
        E_EM_VALUES, T, hw_L=hw_L, delta_E=delta_E, E_grid=E_grid
    )
    log_thermal = np.log10(np.clip(np.abs(thermal), 1e-300, None))
    log_non_eq = np.log10(np.clip(np.abs(non_eq), 1e-300, None))

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(12.5, 5.0), sharex=True, sharey=True
    )
    ax1.plot(E_EM_VALUES, log_thermal)
    ax2.plot(E_EM_VALUES, log_non_eq)
    ax1.set_title("Thermal (Eq. 4)")
    ax2.set_title("Non-equilibrium (Eq. 4)")
    for ax in (ax1, ax2):
        ax.set_xlabel(r"$\hbar\omega$ [eV]")
        ax.set_xlim(E_EM_VALUES[0], E_EM_VALUES[-1])
    ax1.set_ylabel(r"$\log_{10} I(\hbar\omega)$")

    e_min, e_max, dE = _grid_stats(E_grid)
    title = (
        "Emission vs photon energy\n"
        f"$T$={T:.0f} K; hw_L={hw_L:.2f} eV; delta_E={delta_E:.2e}; "
        f"$E\\in[{e_min:.2f},{e_max:.2f}]$ eV; $\\Delta E$={dE:.1e} eV"
    )
    set_figure_title(fig, title)
    _save(fig, save_name, f"stage_3_emission_log_T{int(round(T))}K.png")
    plt.show()


if __name__ == "__main__":
    apply_style()
    heatmap()
    rel_T(300.0)
    heatmap_nonthermal(hw_L=DEFAULT_HW_L, delta_E=DEFAULT_DELTA_E)
    rel_T_nonthermal(300.0, hw_L=DEFAULT_HW_L, delta_E=DEFAULT_DELTA_E)
    plot_emission_log(300.0, hw_L=DEFAULT_HW_L, delta_E=DEFAULT_DELTA_E)
