import matplotlib.pyplot as plt
import numpy as np
from plot_style import apply_style, save_svg
from scipy.integrate import simpson, trapezoid
from _preamble_and_funcs import *


def I6(hw, T):
    mu = chemical_potential(T)
    beta_T = beta(T)
    log1pa = np.logaddexp(0.0, -beta_T * mu)
    log1pb = np.logaddexp(0.0, beta_T * (hw - mu))
    return n_B(hw, T) * (hw + (k_B * T) * (log1pa - log1pb))


def I5(hw, T, int: "str"):
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    if int == "trapz":
        return trapezoid(F_T(E_GRID + hw, E_GRID, T), E_GRID, axis=-1)
    elif int == "simpson":
        return simpson(F_T(E_GRID + hw, E_GRID, T), E_GRID, axis=-1)


############## PLOTS ################


def plot_heatmap(*, save_name: str | None = "auto"):
    hw = E_EM_VALUES[None, :]
    T = T_VALUES[:, None]

    I6_2d = I6(hw, T)
    I5_2d_trap = I5(hw, T, int="trapz")
    I5_2d_simp = I5(hw, T, int="simpson")

    rel_trap = relative_error(I5_2d_trap, I6_2d)
    rel_simp = relative_error(I5_2d_simp, I6_2d)

    fig, [ax1, ax2] = plt.subplots(
        1, 2, figsize=(13.5, 6.0), sharex=True, sharey=True, layout="constrained"
    )

    # trapezoid heatmap
    ax1.set_title("Trapezoid")
    m1 = ax1.pcolormesh(
        E_EM_VALUES,
        T_VALUES,
        rel_trap,
        shading="auto",
        cmap="coolwarm",
        vmin=-16,
        vmax=0,
    )

    # simpson heatmap
    ax2.set_title("Simpson")
    m2 = ax2.pcolormesh(
        E_EM_VALUES,
        T_VALUES,
        rel_simp,
        shading="auto",
        cmap="coolwarm",
        vmin=-16,
        vmax=0,
    )

    for ax in [ax1, ax2]:
        ax.set_xlabel(r"$\hbar\omega$ [eV]")
    ax1.set_ylabel(r"$T$ [K]")
    secax = ax2.secondary_yaxis(
        "right", functions=(lambda t: k_B * t, lambda e: e / k_B)
    )
    secax.set_ylabel(r"$k_B T$ [eV]")

    dE = float(E_GRID[1] - E_GRID[0]) if E_GRID.size > 1 else float("nan")
    title = (
        "Numerical integration (Eq. 5 vs Eq. 6)\n"
        f"Integration over $E\\in[{E_GRID[0]:.2f},{E_GRID[-1]:.2f}]$ eV with "
        f"$\\Delta E$={dE:.1e} eV"
    )
    # secondary y-axis for T in K
    # for ax in [ax1, ax2]:
    #     secax = ax.secondary_yaxis("right",functions=(lambda y: y / k_B, lambda T: T * k_B))
    #     secax.set_ylabel(r"$T$ [K]")
    #     kbt_ticks = ax.get_yticks()
    #     secax.set_yticks(kbt_ticks / k_B)
    #     # secax.yaxis.set_major_formatter(FuncFormatter(lambda t, _pos: f"{t:.0f}"))

    fig.colorbar(m1, ax=[ax1, ax2], label=r"$\log_{10}|\delta_{rel}|$", pad=0.10)
    fig.suptitle(title, y=1.12)
    if save_name is not None:
        filename = "stage_2_rel_error_grid.png" if save_name == "auto" else save_name
        save_svg(fig, filename)
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
        I6_ref = I6(hw_vals, T_val)
        integrand = F_T(E_grid[None, :] + hw_vals[:, None], E_grid[None, :], T_val)
        I5_vals = simpson(integrand, E_grid, axis=-1)
        rel[i] = relative_error(I5_vals, I6_ref)

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
    ax.set(xlabel=r"$\hbar\omega$ [eV]", ylabel=r"$T$ [K]")
    secax = ax.secondary_yaxis(
        "right", functions=(lambda t: k_B * t, lambda e: e / k_B)
    )
    secax.set_ylabel(r"$k_B T$ [eV]")
    fig.colorbar(m, ax=ax, pad=0.10, label=r"$\log_{10}|\delta_{rel}|$")

    title = (
        "Relative error heatmap (Simpson, Eq. 5 vs Eq. 6)\n"
        f"$E\\in[{E_min:.2f},{E_max:.2f}]$ eV; $\\Delta E$={dE:.1e} eV"
    )
    ax.set_title(title)

    if save_name is not None:
        filename = (
            "stage_2_rel_error_grid_50x50.png" if save_name == "auto" else save_name
        )
        save_svg(fig, filename)
    plt.show()


def plot_step_convergence(T: float = 300.0, *, save_name: str | None = "auto"):
    hw_values = np.linspace(3, 7, 500)
    I6_ref = I6(hw_values, T)

    fig, axes = plt.subplots(4, 1, figsize=(8.0, 6.0), sharex=True, sharey=True)
    global E_GRID
    E_grid_original = E_GRID
    try:
        for i, dE in enumerate([4e-3, 1e-3, 4e-4, 1e-4]):
            E_GRID = np.arange(E_MIN, E_MAX + dE, dE)
            I5_simp = I5(hw_values, T, int="simpson")
            rel = relative_error(I5_simp, I6_ref)
            axes[i].plot(hw_values, rel, label=rf"$\Delta E$={dE:.0e} eV", alpha=0.8)
            axes[i].legend(loc="right")
    finally:
        E_GRID = E_grid_original

    fig.supylabel(r"$\log_{10}|\delta_{rel}|$")
    fig.supxlabel(r"$\hbar\omega$ [eV]")
    title = (
        "Step-size convergence (Simpson, Eq. 5 vs Eq. 6)\n"
        f"$T$={T:.0f} K; integration over $E\\in[{E_MIN:.2f},{E_MAX:.2f}]$ eV with varying $\\Delta E$"
    )
    axes[-1].set_ylim(-17, -9)
    axes[-1].set_xlim(hw_values[0], hw_values[-1])
    fig.suptitle(title)
    if save_name is not None:
        filename = (
            f"stage_2_step_convergence_T{int(round(T))}K.png"
            if save_name == "auto"
            else save_name
        )
        save_svg(fig, filename)
    plt.show()


def plot_length_convergence(T: float = 300.0, *, save_name: str | None = "auto"):
    hw_values = np.linspace(4, 6, 500)
    I6_ref = I6(hw_values, T)

    fig, axes = plt.subplots(4, 1, figsize=(8.0, 6.0), sharex=True, sharey=True)
    global E_GRID
    E_grid_original = E_GRID
    try:
        for i, L in enumerate([5.5, 5.6, 5.7, 5.8]):
            E_GRID = np.arange(0, L, D_E)
            I5_simp = I5(hw_values, T, int="simpson")
            rel = relative_error(I5_simp, I6_ref)
            axes[i].plot(hw_values, rel, label=rf"$E\in[0,{L}]$ eV", alpha=0.8)
            axes[i].legend(loc="right")
    finally:
        E_GRID = E_grid_original

    # for ax in axes:
    #     ax.set(ylabel=r"$\log_{10}|\delta_{rel}|$")
    # axes[-1].set_xlabel(r"$\hbar\omega$ [eV]")

    fig.supylabel(r"$\log_{10}|\delta_{rel}|$")
    fig.supxlabel(r"$\hbar\omega$ [eV]")

    title = (
        "Integration-interval convergence (Simpson, Eq. 5 vs Eq. 6)\n"
        f"$T$={T:.0f} K; $\\Delta E$={D_E:.1e} eV; integration interval varies"
    )
    axes[-1].set_ylim(-17, -10)
    axes[-1].set_xlim(hw_values[0], hw_values[-1])
    fig.suptitle(title)
    if save_name is not None:
        filename = (
            f"stage_2_length_convergence_T{int(round(T))}K.png"
            if save_name == "auto"
            else save_name
        )
        save_svg(fig, filename)
    plt.show()


if __name__ == "__main__":
    apply_style()
    plot_heatmap()
    # plot_heatmap_50x50()
    # plot_step_convergence(300.0)
    # plot_length_convergence(300.0)
