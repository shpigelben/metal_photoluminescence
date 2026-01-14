import matplotlib.pyplot as plt
import numpy as np
from _preamble_and_funcs import *
from scipy.integrate import simpson
from plot_style import apply_style, save_svg, set_figure_title


CONVERGED_D_E = 1e-4
CONVERGED_E_MADEFAULT_HW_L = 2.0
DEFAULT_DELTA_E = 1e-2


def converged_energy_grid(
    *, E_min: float = E_MIN, E_max: float = CONVERGED_E_MAX, dE: float = CONVERGED_D_E
) -> np.ndarray:
    E_grid = np.arange(E_min, E_max + dE, dE)
    if E_grid.size < 2:
        raise ValueError("E_min/E_max/dE must define at least two grid points.")
    return E_grid


def I5(hw, T, *, E_grid: np.ndarray | None = None):
    if E_grid is None:
        E_grid = E_GRID
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    g_F = eDOS(E_F)
    integrand = (g_F**2) * F_T(E_grid + hw, E_grid, T)
    return simpson(integrand, E_grid, axis=-1)


def I4(hw, T, *, E_grid: np.ndarray | None = None):
    if E_grid is None:
        E_grid = E_GRID
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    integrand = eDOS(E_grid) * eDOS(E_grid + hw) * F_T(E_grid + hw, E_grid, T)
    return simpson(integrand, E_grid, axis=-1)


def I5_nonthermal(
    hw,
    T,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
):
    if E_grid is None:
        E_grid = converged_energy_grid()
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    g_F = eDOS(E_F)
    f1 = f_neq(E_grid + hw, T, hw_L=hw_L, delta_E=delta_E)
    f2 = f_neq(E_grid, T, hw_L=hw_L, delta_E=delta_E)
    integrand = (g_F**2) * f1 * (1 - f2)
    return simpson(integrand, E_grid, axis=-1)


def I4_nonthermal(
    hw,
    T,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
):
    if E_grid is None:
        E_grid = converged_energy_grid()
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    f1 = f_neq(E_grid + hw, T, hw_L=hw_L, delta_E=delta_E)
    f2 = f_neq(E_grid, T, hw_L=hw_L, delta_E=delta_E)
    integrand = eDOS(E_grid) * eDOS(E_grid + hw) * f1 * (1 - f2)
    return simpson(integrand, E_grid, axis=-1)


def heatmap(*, save_name: str | None = "auto") -> None:
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]

    rel = relative_error(I5(hw, T), I4(hw, T))

    fig, ax = plt.subplots(figsize=(8.5, 6.0))
    m = ax.pcolormesh(
        E_EM_VALUES, T_VALUES, rel, shading="auto", cmap="coolwarm", vmin=-8, vmax=0
    )
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$T$ [K]")
    secax = ax.secondary_yaxis(
        "right", functions=(lambda t: k_B * t, lambda e: e / k_B)
    )
    secax.set_ylabel(r"$k_B T$ [eV]")
    fig.colorbar(m, ax=ax, pad=0.12, label=r"$\log_{10}|\delta_{rel}|$")

    dE = float(E_GRID[1] - E_GRID[0]) if E_GRID.size > 1 else float("nan")
    title = (
        "Constant eDOS approximation (Eq. 5 vs Eq. 4)\n"
        f"Simpson integration over $E\\in[{E_GRID[0]:.2f},{E_GRID[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    plt.title(title)
    if save_name is not None:
        filename = (
            "stage_3_edos_vs_const_edos_heatmap.png"
            if save_name == "auto"
            else save_name
        )
        save_svg(fig, filename)
    plt.show()


def rel_T(T: float, *, save_name: str | None = "auto") -> None:
    rel = relative_error(I5(E_EM_VALUES, T), I4(E_EM_VALUES, T))

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(E_EM_VALUES, rel)
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$\log_{10}|\delta_{rel}|$")
    ax.set_xlim(E_EM_VALUES[0], E_EM_VALUES[-1])

    dE = float(E_GRID[1] - E_GRID[0]) if E_GRID.size > 1 else float("nan")
    title = (
        "Constant eDOS approximation (Eq. 5 vs Eq. 4)\n"
        f"$T$={T:.0f} K; Simpson integration over $E\\in[{E_GRID[0]:.2f},{E_GRID[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    plt.title(title)
    if save_name is not None:
        filename = (
            f"stage_3_rel_error_T{int(round(T))}K.png"
            if save_name == "auto"
            else save_name
        )
        save_svg(fig, filename)
    plt.show()


def heatmap_nonthermal(
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
    save_name: str | None = "auto",
) -> None:
    if E_grid is None:
        E_grid = converged_energy_grid()
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
    secax = ax.secondary_yaxis(
        "right", functions=(lambda t: k_B * t, lambda e: e / k_B)
    )
    secax.set_ylabel(r"$k_B T$ [eV]")
    fig.colorbar(m, ax=ax, pad=0.12, label=r"$\log_{10}|\delta_{rel}|$")

    dE = float(E_grid[1] - E_grid[0]) if E_grid.size > 1 else float("nan")
    title = (
        "Constant eDOS approximation (non-equilibrium, Eq. 5 vs Eq. 4)\n"
        f"hw_L={hw_L:.2f} eV; delta_E={delta_E:.2e}; "
        f"Simpson integration over $E\\in[{E_grid[0]:.2f},{E_grid[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    plt.title(title)
    if save_name is not None:
        filename = (
            "stage_3_rel_error_nonthermal_heatmap.png"
            if save_name == "auto"
            else save_name
        )
        save_svg(fig, filename)
    plt.show()


def rel_T_nonthermal(
    T: float,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
    save_name: str | None = "auto",
) -> None:
    if E_grid is None:
        E_grid = converged_energy_grid()
    rel = relative_error(
        I5_nonthermal(E_EM_VALUES, T, hw_L=hw_L, delta_E=delta_E, E_grid=E_grid),
        I4_nonthermal(E_EM_VALUES, T, hw_L=hw_L, delta_E=delta_E, E_grid=E_grid),
    )

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.plot(E_EM_VALUES, rel)
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$\log_{10}|\delta_{rel}|$")
    ax.set_xlim(E_EM_VALUES[0], E_EM_VALUES[-1])

    dE = float(E_grid[1] - E_grid[0]) if E_grid.size > 1 else float("nan")
    title = (
        "Constant eDOS approximation (non-equilibrium, Eq. 5 vs Eq. 4)\n"
        f"$T$={T:.0f} K; hw_L={hw_L:.2f} eV; delta_E={delta_E:.2e}; "
        f"Simpson integration over $E\\in[{E_grid[0]:.2f},{E_grid[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    plt.title(title)
    if save_name is not None:
        filename = (
            f"stage_3_rel_error_nonthermal_T{int(round(T))}K.png"
            if save_name == "auto"
            else save_name
        )
        save_svg(fig, filename)
    plt.show()


def plot_emission_log(
    T: float,
    *,
    hw_L: float,
    delta_E: float,
    E_grid: np.ndarray | None = None,
    save_name: str | None = "auto",
) -> None:
    if E_grid is None:
        E_grid = converged_energy_grid()

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

    dE = float(E_grid[1] - E_grid[0]) if E_grid.size > 1 else float("nan")
    titl    title = (
"Emission vs photon energy\n"
        f"$T$={T:.0f} K; hw_L={hw_L:.2f} eV; delta_E={delta_E:.2e}; "
        f"$E\\in[{E_grid[0]:.2f},{E_grid[-1]:.2f}]$ eV; $\\Delta E$={dE:.1e} eV"
    )
    set_figure_title(fig, title)
    if save_name is not None:
        filename = (
            f"stage_3_emission_log_T{int(round(T))}K.png"
            if save_name == "auto"
            else save_name
        )
        save_svg(fig, filename)
    plt.show()


if __name__ == "__main__":
    apply_style()
    heatmap()
    rel_T(300.0)
    heatmap_nonthermal(hw_L=DEFAULT_HW_L, delta_E=DEFAULT_DELTA_E)
    rel_T_nonthermal(300.0, hw_L=DEFAULT_HW_L, delta_E=DEFAULT_DELTA_E)
    plot_emission_log(300.0, hw_L=DEFAULT_HW_L, delta_E=DEFAULT_DELTA_E)

        save_svg(fig, filename)
    plt.show()


if __name__ == "__main__":
    apply_style()
    heatmap()
    rel_T(300.0)
 save_svg(fig, filename)
    plt.show()


if __name__ == "__main__":
    apply_style()
    heatmap()
    rel_T(300.0)
