import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import simpson

from plot_style import apply_style, save_svg, set_figure_title

# Physical constants (energy in eV)
k_B = 8.617333262145e-5  # eV/K
hbar = 6.582119569e-16
m_e = 5.485e-4

# Global parameters
E_F = 5.0
T = 300.0
EMISSION_ENERGY_MIN = 0.01
EMISSION_ENERGY_MAX = 8.0
N_EMISSION = 150
HW_VALUES = np.linspace(EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, N_EMISSION)
E_MIN = 0.0
E_MAX = 10.0
T_MIN = 1.0
T_MAX = 2000.0


def beta(T_val: float) -> float:
    return 1.0 / (k_B * T_val)


def chemical_potential(T_val: float) -> float:
    T_F = E_F / k_B
    return E_F * (1 - (np.pi**2 / 12) * ((T_val / T_F) ** 2))


def n_B(hw, T_val: float):
    beta_T = beta(T_val)
    with np.errstate(over="ignore"):
        exp_arg = beta_T * hw
        return 1.0 / np.expm1(exp_arg)


def F_T(E, hw, T_val: float):
    mu = chemical_potential(T_val)
    beta_T = beta(T_val)
    a = beta_T * (E - mu)
    b = a + beta_T * hw
    return np.exp(a - np.logaddexp(0.0, a) - np.logaddexp(0.0, b))


def relative_error(candidate: np.ndarray, reference: np.ndarray) -> np.ndarray:
    rel = np.abs(candidate - reference) / np.abs(reference)
    rel = np.clip(rel, 1e-16, 1.0)
    return np.log10(rel)


def I6(hw, T_val: float):
    mu = chemical_potential(T_val)
    beta_T = beta(T_val)
    log1pa = np.logaddexp(0.0, -beta_T * mu)
    log1pb = np.logaddexp(0.0, beta_T * (hw - mu))
    return n_B(hw, T_val) * (hw + (1.0 / beta_T) * (log1pa - log1pb))


def I5(hw, E_min: float, E_max: float, dE: float, T_val: float):
    if dE <= 0.0 or E_max <= E_min:
        return np.full_like(hw, np.nan, dtype=float)
    E_grid = np.arange(E_min, E_max + dE, dE)
    if E_grid.size < 2:
        return np.full_like(hw, np.nan, dtype=float)
    integrand = F_T(E_grid[None, :], hw[:, None], T_val)
    return simpson(integrand, E_grid, axis=-1)


def plot_length_convergence(E_min: float, E_max: float, dE: float):
    I6_ref = I6(HW_VALUES, T)

    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    fig.subplots_adjust(bottom=0.26)

    rel0 = relative_error(I5(HW_VALUES, E_min, E_max, dE, T), I6_ref)
    (line,) = ax.plot(HW_VALUES, rel0, linewidth=2.0)

    ax.set(
        xlabel=r"$\hbar\omega$ [eV]",
        ylabel=r"$\log_{10}|\delta_{rel}|$",
        xlim=(HW_VALUES[0], HW_VALUES[-1]),
        ylim=(-17, 0.5),
    )
    ax.set_title("Relative error: Eq. 5 (numeric) vs Eq. 6 (analytic)")

    ax_Emin = fig.add_axes([0.12, 0.16, 0.78, 0.03])
    ax_Emax = fig.add_axes([0.12, 0.11, 0.78, 0.03])
    ax_dE = fig.add_axes([0.12, 0.06, 0.78, 0.03])

    s_Emin = Slider(ax_Emin, "E_min [eV]", 0.0, 9.0, valinit=float(E_min), valstep=0.1)
    s_Emax = Slider(ax_Emax, "E_max [eV]", 1.0, 10.0, valinit=float(E_max), valstep=0.1)
    s_dE = Slider(ax_dE, "dE [eV]", 1e-4, 1e-3, valinit=float(dE), valstep=1e-4)

    def _update(_val):
        rel = relative_error(
            I5(HW_VALUES, s_Emin.val, s_Emax.val, s_dE.val, T),
            I6_ref,
        )
        line.set_ydata(rel)
        fig.canvas.draw_idle()

    s_Emin.on_changed(_update)
    s_Emax.on_changed(_update)
    s_dE.on_changed(_update)

    plt.show()


if __name__ == "__main__":
    print(I5(7.0, 0.0, 10.0, 1e-4, 30.0))
    print(I6(7.0, 50.0))
    # plot_length_convergence(E_min=0.0, E_max=10.0, dE=1e-3)
