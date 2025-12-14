import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from matplotlib.ticker import FuncFormatter

from plot_style import apply_style, save_svg, set_figure_title

# Constants (energy in eV)
k_B = 8.617333262145e-5
hbar = 6.582119569e-16
m_e = 5.485e-4
E_F_DEFAULT = 3.0

# Energy integration grid for Eq. (4)
E_min = 0.0
E_max = 10.0
dE = 1e-3
E_grid = np.arange(E_min, E_max + dE, dE)

# Emission energy sweep (hbar*omega)
E_em_values = np.linspace(0.01, 8.0, 2000)

def chemical_potential(E_F: float, T: float) -> float:
    T_F = E_F / k_B
    return E_F * (1 - (np.pi**2 / 12) * ((T / T_F) ** 2))

def density_of_states(E: float | np.ndarray) -> float | np.ndarray:
    return ((m_e ** 1.5) / (np.pi ** 2 * hbar ** 3)) * np.sqrt(2 * E)

def relative_error(candidate: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """Elementwise |(candidate-reference)/reference|, with 0/0 -> 0."""

    candidate = np.asarray(candidate, dtype=float)
    reference = np.asarray(reference, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.abs((candidate - reference) / reference)
    return np.where(reference == 0.0, np.where(candidate == 0.0, 0.0, np.inf), rel)


def I_numeric_const_eDOS_sweep(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    batch_size: int = 256,
) -> np.ndarray:
    """Numeric Eq. (4) with constant eDOS = g(E_F)^2 using a log-stable integrand."""

    hw_values = np.asarray(hw_values, dtype=float)

    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)
    g_F = density_of_states(E_F)

    a = beta * (E_grid - mu)
    log_denom_a = np.logaddexp(0.0, a)

    out = np.empty_like(hw_values)
    for start in range(0, hw_values.size, batch_size):
        hw = hw_values[start : start + batch_size]
        b = a[:, None] + beta * hw[None, :]
        log_val = a[:, None] - log_denom_a[:, None] - np.logaddexp(0.0, b)
        integrand = np.exp(log_val)
        out[start : start + hw.size] = g_F**2 * simpson(integrand, x=E_grid, axis=0)

    return out


def I_analytic_const_eDOS_exact(hw: np.ndarray, T: float, E_F: float) -> np.ndarray:
    """Analytic constant-eDOS result (no μ ≫ k_B T approximation)."""

    hw = np.asarray(hw, dtype=float)
    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)
    g_F = density_of_states(E_F)

    x = beta * hw
    bracket = x + np.logaddexp(0.0, -beta * mu) - np.logaddexp(0.0, beta * (hw - mu))
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        denom = np.expm1(x)
        f0 = 1.0 / (np.exp(-beta * mu) + 1.0)
        ratio = np.where(x == 0.0, f0, bracket / denom)
    return g_F**2 * k_B * T * ratio


def I_analytic_const_eDOS_approx(hw: np.ndarray, T: float, E_F: float) -> np.ndarray:
    """Analytic constant-eDOS result with μ ≫ k_B T approximation."""

    hw = np.asarray(hw, dtype=float)
    beta = 1.0 / (k_B * T)
    g_F = density_of_states(E_F)

    x = beta * hw
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        denom = np.expm1(x)
        ratio = np.where(x == 0.0, k_B * T, hw / denom)
    return g_F**2 * ratio


def rel_error_numeric_vs_exact(hw_values: np.ndarray, T: float, E_F: float) -> np.ndarray:
    I_num = I_numeric_const_eDOS_sweep(hw_values, T, E_F)
    I_exact = I_analytic_const_eDOS_exact(hw_values, T, E_F)
    return relative_error(I_num, I_exact)


def rel_error_approx_vs_exact(hw_values: np.ndarray, T: float, E_F: float) -> np.ndarray:
    I_approx = I_analytic_const_eDOS_approx(hw_values, T, E_F)
    I_exact = I_analytic_const_eDOS_exact(hw_values, T, E_F)
    return relative_error(I_approx, I_exact)


REL_ERROR_CASES = [
    {"T": 300.0, "E_F": 5.0, "title": "T = 300 K, E_F = 5 eV"},
    {"T": 300.0, "E_F": 3.0, "title": "T = 300 K, E_F = 3 eV"},
    {"T": 700.0, "E_F": 3.0, "title": "T = 700 K, E_F = 3 eV"},
    {"T": 1000.0, "E_F": 3.0, "title": "T = 1000 K, E_F = 3 eV"},
]

def show_rel_error_grid() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True, sharey=True)
    for ax, case in zip(axes.flat, REL_ERROR_CASES):
        T = float(case["T"])
        E_F = float(case["E_F"])
        rel = rel_error_numeric_vs_exact(E_em_values, T, E_F)

        ax.semilogy(E_em_values, np.clip(rel, 1e-20, None), color="C0")
        ax.set_title(str(case["title"]))
        ax.set_xlim(0.0, float(E_em_values[-1]))
        ax.set_ylim(1e-20, 1.0)
        ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)

    axes[1, 0].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[1, 1].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[0, 0].set_ylabel(r"$|\delta_{rel}|$")
    axes[1, 0].set_ylabel(r"$|\delta_{rel}|$")

    title = "Const eDOS: relative error (numeric integral vs analytic exact)"
    set_figure_title(fig, title)
    save_svg(fig, "stage_1_rel_error_grid.svg")
    plt.show()


def show_rel_error_heatmap_exact_vs_approx(
    *,
    E_F: float = E_F_DEFAULT,
    hw_min: float = 0.01,
    hw_max: float = 5.0,
    n_hw: int = 2000,
    T_min: float = 0.0,
    T_max: float = 5000.0,
    n_T: int = 1200,
) -> None:
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
    show_rel_error_grid()
    show_rel_error_heatmap_exact_vs_approx(E_F=E_F_DEFAULT)
