import matplotlib.pyplot as plt
import numpy as np
from _preamble_and_funcs import *
from scipy.integrate import simpson
from plot_style import apply_style, save_svg, set_figure_title

def I5(hw, T):
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    g_F = eDOS(E_F)
    integrand = (g_F**2) * F_T(E_GRID, hw, T)
    return  simpson(integrand, E_GRID, axis=-1)

def I4(hw, T):
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    g_E = eDOS(E_GRID)
    integrand = eDOS(E_GRID) * eDOS(E_GRID + hw) * F_T(E_GRID, hw, T)
    return simpson(integrand, E_GRID, axis=-1)

def heatmap(*, save_name: str | None = "auto") -> None:
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]
    
    rel = relative_error(I5(hw, T), I4(hw, T))

    fig, ax = plt.subplots(figsize=(8.5, 6.0))
    m = ax.pcolormesh(E_EM_VALUES, T_VALUES, rel, shading="auto", cmap="coolwarm", vmin=-8, vmax=0)
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$T$ [K]")
    secax = ax.secondary_yaxis("right", functions=(lambda t: k_B * t, lambda e: e / k_B))
    secax.set_ylabel(r"$k_B T$ [eV]")
    fig.colorbar(m, ax=ax, pad=0.12, label=r"$\log_{10}|\delta_{rel}|$")

    dE = float(E_GRID[1] - E_GRID[0]) if E_GRID.size > 1 else float("nan")
    title = (
        "Stage 3 — Constant eDOS approximation (Eq. 5 vs Eq. 4)\n"
        f"Simpson integration over $E\\in[{E_GRID[0]:.2f},{E_GRID[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV (N={E_GRID.size}); "
        f"$\\hbar\\omega\\in[{E_EM_VALUES[0]:.2f},{E_EM_VALUES[-1]:.2f}]$ eV (N={E_EM_VALUES.size}); "
        f"$T\\in[{T_VALUES[0]:.0f},{T_VALUES[-1]:.0f}]$ K (N={T_VALUES.size})"
    )
    set_figure_title(fig, title)
    if save_name is not None:
        filename = "stage_3_edos_vs_const_edos_heatmap.png" if save_name == "auto" else save_name
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
        "Stage 3 — Constant eDOS approximation (Eq. 5 vs Eq. 4)\n"
        f"$T$={T:.0f} K; Simpson integration over $E\\in[{E_GRID[0]:.2f},{E_GRID[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV (N={E_GRID.size})"
    )
    set_figure_title(fig, title)
    if save_name is not None:
        filename = f"stage_3_rel_error_T{int(round(T))}K.png" if save_name == "auto" else save_name
        save_svg(fig, filename)
    plt.show()

if __name__ == "__main__":
    apply_style()
    heatmap()
    rel_T(300.0)
