import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from _preamble_and_funcs import *
from plot_style import apply_style, save_svg

# exact integtral solution (Eq. 6)
def I6(hw, T, E_F):
    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)

    log1pa = np.logaddexp(0.0, -beta * mu)                 # log(1 + e^{-βμ})
    log1pb = np.logaddexp(0.0, beta * (hw - mu))           # log(1 + e^{β(hw-μ)})
    return  hw + (1.0 / beta) * (log1pa - log1pb)


# approximate integral solution (Eq. 7)
def I7(hw):
    return hw

# plot heatmap of relative error (Eq. 6 vs Eq. 7)
def plot_rel():
    hw_1D = np.linspace(0.01, 8.0, 100)
    T_1D = np.linspace(1.0, 5000.0, 100)
    kBT_1D = k_B * T_1D
    hw, T = np.meshgrid(hw_1D, T_1D, indexing="xy")

    I6_grid = I6(hw, T, E_F_DEFAULT)
    I7_grid = I7(hw)
    
    rel = relative_error(I7_grid, I6_grid)
    log10_err = np.log10(np.clip(rel, 1e-20, 1))

    fig, ax = plt.subplots(figsize=(11, 6.0))
    pc = ax.pcolormesh(hw_1D, kBT_1D, log10_err, cmap="coolwarm", vmin=-16, vmax=0)
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$k_B T$ [eV]")

    # secondary y-axis for T in K
    secax = ax.secondary_yaxis("right",functions=(lambda y: y / k_B, lambda T: T * k_B))
    secax.set_ylabel(r"$T$ [K]")
    kbt_ticks = ax.get_yticks()
    secax.set_yticks(kbt_ticks / k_B)
    secax.yaxis.set_major_formatter(FuncFormatter(lambda t, _pos: f"{t:.0f}"))

    cbar = fig.colorbar(pc, ax=ax, pad=0.13)
    cbar.set_label(r"$\log_{10}|\delta_{rel}|$")

    ax.set_title(f"Low Energy Approximation (Eq. 7 vs Eq. 6), E_F = {E_F_DEFAULT:.2f} eV")
    save_svg(fig, f"stage_1_analytic_approx_rel_error.svg")
    plt.show()

if __name__ == "__main__":
    apply_style()
    plot_rel()
