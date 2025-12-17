import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

from _preamble_and_funcs import *
from plot_style import apply_style, save_svg


# exact integtral solution (Eq. 6)
def I6(hw, T, E_F):
    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)
    g_F = eDOS(E_F)

    log1pa = np.logaddexp(0.0, -beta * mu)                 # log(1 + e^{-βμ})
    log1pb = np.logaddexp(0.0, beta * (hw - mu))           # log(1 + e^{β(hw-μ)})
    bracket = hw + (1.0 / beta) * (log1pa - log1pb)

    return (g_F**2)  * bracket


# approximate integral solution (Eq. 7)
def I7(hw, T, E_F):
    g_F = eDOS(E_F)
    return (g_F**2)  * hw

# plot heatmap of relative error (Eq. 6 vs Eq. 7)
def plot_rel():
    hw_1D = np.linspace(0.01, 8.0, 1000)
    T_1D = np.linspace(1.0, 5000.0, 1000)
    hw, T = np.meshgrid(hw_1D, T_1D, indexing="xy")

    I6_grid = I6(hw, T, E_F_DEFAULT)
    I7_grid = I7(hw, T, E_F_DEFAULT)
    rel = relative_error(I7_grid, I6_grid)

    min_clip = 1e-20
    max_clip = 1
    log10_err = np.log10(np.clip(rel, min_clip, max_clip))


    fig, ax = plt.subplots(figsize=(11, 6.0))

    ax.pcolormesh(hw_1D, T_1D, log10_err, vmin = -16, vmax = 0)
    ax.set_ylabel(r"$T$ [K]")
    ax.set_xlabel(r"$\hbar\omega$ [eV]")
    plt.show()
 

def show_rel_error_heatmap_exact_vs_approx(
    *,
    E_F: float = E_F_DEFAULT,
    hw_min: float = 0.01,
    hw_max: float = 8.0,
    n_hw: int = 2000,
    T_min: float = 0.0,
    T_max: float = 5000.0,
    n_T: int = 1200,
) -> None:
    """Show log10|δ_rel| for Eq. (7) vs Eq. (6) over (ħω, kBT)."""

    hw_values = np.linspace(hw_min, hw_max, n_hw)
    T_min_eff = max(float(T_min), 1.0e-6)
    T_values = np.linspace(T_min_eff, T_max, n_T)
    kBT_values = k_B * T_values

    # Vectorized relative error (approx vs exact) without expm1:
    # I_exact ∝ [hw + kBT*(ln(1+e^{-βμ}) - ln(1+e^{β(hw-μ)}))]
    # I_approx ∝ hw
    mu = chemical_potential(float(E_F), T_values)
    beta = 1.0 / (k_B * T_values)

    term1 = np.logaddexp(0.0, -beta * mu)  # log(1 + e^{-βμ})   shape (n_T,)
    arg2 = beta[:, None] * (hw_values[None, :] - mu[:, None])
    log_terms = term1[:, None] - np.logaddexp(0.0, arg2)

    denom = hw_values[None, :] + (k_B * T_values)[:, None] * log_terms

    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.abs(1.0 - (hw_values[None, :] / denom))
    rel = np.nan_to_num(rel, nan=0.0, posinf=1e6, neginf=1e6)
    log10_err = np.log10(np.clip(rel, 1e-20, 1e6))

    fig, ax = plt.subplots(figsize=(11, 6.0))
    y0 = 0.0 if T_min <= 0 else float(k_B * T_min)
    im = ax.imshow(
        log10_err,
        origin="lower",
        aspect="auto",
        extent=(hw_values[0], hw_values[-1], y0, kBT_values[-1]),
        cmap="RdYlGn_r",
        vmin=-16.0,
        vmax=0.0,
        interpolation="nearest",
    )

    cbar = fig.colorbar(im, ax=ax, pad=0.14, ticks=np.arange(-16, 0.1, 2.0))
    cbar.set_label(r"$\log_{10}|\delta_{rel}|$")
    cbar.ax.tick_params(length=3)

    ax.set_xlabel(r"$\hbar\omega$ [eV]")
    ax.set_ylabel(r"$k_B T$ [eV]")

    secax = ax.secondary_yaxis(
        "right",
        functions=(lambda y: y / k_B, lambda T: T * k_B),
    )
    secax.set_ylabel(r"$T$ [K]")
    kbt_ticks = ax.get_yticks()
    secax.set_yticks(kbt_ticks / k_B)
    secax.yaxis.set_major_formatter(FuncFormatter(lambda t, _pos: f"{t:.0f}"))

    title = f"Analytic approximation error map (approx vs exact), E_F = {E_F:.2f} eV"
    ax.set_title(title)
    fig.tight_layout()
    ef_tag = f"{E_F:.2f}".replace(".", "p")
    save_svg(fig, f"stage_1_heatmap_exact_vs_approx_EF{ef_tag}eV.svg")
    plt.show()


if __name__ == "__main__":
    apply_style()
    plot_rel()
#     show_rel_error_heatmap_exact_vs_approx(E_F=E_F_DEFAULT)
