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

def heatmap():
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]
    
    rel = relative_error(I5(hw, T), I4(hw, T))

    fig, ax = plt.subplots(figsize=(8.0, 6.0))
    m = ax.pcolormesh(E_EM_VALUES, T_VALUES, rel, cmap="coolwarm", vmin=-8, vmax=0)
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$k_B T$ [eV]")
    fig.colorbar(m, ax=ax, pad=0.13, label=r"$\log_{10}|\delta_{rel}|$")
    set_figure_title(fig, "Heatmap: $\\log_{10}(|\\delta_{rel}(\\hbar\\omega, k_B T)|)$ (const eDOS)")
    plt.show()

def rel_T(T:float) -> None:
    rel = relative_error(I4(E_EM_VALUES, T), I5(E_EM_VALUES, T))
    plt.plot(E_EM_VALUES, rel)
    plt.xlabel(r"$\hbar\omega$ [eV]")
    plt.ylabel(r"$\log_{10}|\delta_{rel}|$")
    plt.xlim(E_EM_VALUES[0], E_EM_VALUES[-1])
    plt.title(f"Relative error at T = {T} K")
    plt.show()

if __name__ == "__main__":
    apply_style()
    heatmap()
    rel_T(300.0)
