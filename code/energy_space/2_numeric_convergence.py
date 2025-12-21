import matplotlib.pyplot as plt
import numpy as np
from plot_style import apply_style, save_svg
from _preamble_and_funcs import *
from scipy.integrate import quad, simpson, trapezoid

def I6(hw, T):
    mu = chemical_potential(T)
    log1pa = np.logaddexp(0.0, -beta(T) * mu)
    log1pb = np.logaddexp(0.0, beta(T) * (hw - mu))
    return n_B(hw, T) * (hw + (1.0 / beta(T)) * (log1pa - log1pb))

def I5(hw, T, int: "str"):
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    if int == "trapz":
        return trapezoid(F_T(E_GRID, hw, T), E_GRID, axis=-1)
    elif int == "simpson":
        return simpson(F_T(E_GRID, hw, T), E_GRID, axis=-1)

############## PLOTS ################

def plot_heatmap():
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]

    I6_2d = I6(hw, T)
    I5_2d_trap = I5(hw, T, int='trapz')
    I5_2d_simp = I5(hw, T, int='simpson')

    rel_trap = relative_error(I5_2d_trap, I6_2d)
    rel_simp = relative_error(I5_2d_simp, I6_2d)

    fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(13.5, 5.0), sharex=True, sharey=True)
    
    # trapezoid heatmap
    ax1.set_title("Trapezoid")
    m1 = ax1.pcolormesh(E_EM_VALUES, T_VALUES, rel_trap,
        shading="auto",
        cmap="coolwarm",
        vmin=-16,
        vmax=0)


    # simpson heatmap
    ax2.set_title("Simpson")
    m2 = ax2.pcolormesh(E_EM_VALUES, T_VALUES, rel_simp,
        shading="auto",
        cmap="coolwarm",
        vmin=-16,
        vmax=0)

    for ax in [ax1, ax2]:
        ax.set_xlabel(r"$\hbar\omega$ [eV]")
    ax1.set_ylabel(r"$T$ [K]")

    plt.suptitle(f"Relative Error - Eq. 6 vs Eq. 5", fontsize=16)
    # secondary y-axis for T in K
    # for ax in [ax1, ax2]:
    #     secax = ax.secondary_yaxis("right",functions=(lambda y: y / k_B, lambda T: T * k_B))
    #     secax.set_ylabel(r"$T$ [K]")
    #     kbt_ticks = ax.get_yticks()
    #     secax.set_yticks(kbt_ticks / k_B)
    #     # secax.yaxis.set_major_formatter(FuncFormatter(lambda t, _pos: f"{t:.0f}"))

    fig.colorbar(m1, ax=[ax1, ax2], label=r"$\log_{10}|\delta_{rel}|$", pad=0.02)
    # fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.0), sharex=True, sharey=True)
    # m = _add_heatmap(axes[0], E_EM_VALUES, T_use, log10_rel_trap, "Trapezoid")
    # _add_heatmap(axes[1], E_EM_VALUES, T_use, log10_rel_simp, "Simpson")
    # _add_heatmap(axes[2], E_EM_VALUES, T_use, log10_rel_quad, "Quadrature")
    # fig.colorbar(m1, ax=axes, label=r"$\log_{10}|\delta_{rel}|$", pad=0.02)
    # plt.tight_layout()
    plt.show()

def plot_step_convergence(T = 300.0):
    E_EM_VALUES = np.linspace(3,7,100)
    I6_simp = I6(E_EM_VALUES, T)
    for D_E in [1e-3, 4e-4, 1e-4]:
        global E_GRID
        E_GRID = np.arange(E_MIN, E_MAX + D_E, D_E)
        I5_simp = I5(E_EM_VALUES, T, int='simpson')
        rel = relative_error(I5_simp, I6_simp)
        plt.plot(E_EM_VALUES, rel, label=f"$\Delta E$={D_E:.0e}")

    
    plt.xlabel(r"$\hbar\omega$ [eV]")
    plt.ylabel(r"$\log_{10}|\delta_{rel}|$")
    plt.title(f"Relative Error at T={T} K - Eq. 6 vs Eq. 5")
    plt.ylim(-17, -9)
    plt.legend()
    plt.show()

def plot_length_convergence(T = 300.0):
    E_EM_VALUES = np.linspace(3,7,100)
    I6_simp = I6(E_EM_VALUES, T)
    for L in [1,2,3,4,5,6]:
        global E_GRID
        E_GRID = np.arange(E_F - L, E_F + L, D_E)
        I5_simp = I5(E_EM_VALUES, T, int='simpson')
        rel = relative_error(I5_simp, I6_simp)
        plt.plot(E_EM_VALUES, rel, label=f"$range = {2*L}")
    
    plt.xlabel(r"$\hbar\omega$ [eV]")
    plt.ylabel(r"$\log_{10}|\delta_{rel}|$")
    plt.title(f"Relative Error at T={T} K - Eq. 6 vs Eq. 5")
    plt.ylim(-17, -2)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    apply_style()
    plot_heatmap()
    # plot_int_convergence(300.0)
    # plot_length_convergence(300.0)
