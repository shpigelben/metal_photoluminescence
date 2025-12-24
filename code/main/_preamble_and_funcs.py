import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from plot_style import apply_style, save_svg

############### PREAMBLE ###############

# Physical constants (energy in eV)
k_B = 8.617333262145e-5  # eV/K
hbar = 6.582119569e-16
m_e = 5.485e-4

# INTEGRATION PARAMETERS
E_F = 5.0
E_MIN = 0.0
E_MAX = 10.0
D_E = 1e-4
E_GRID = np.arange(E_MIN, E_MAX + D_E, D_E)

# EMISSION ENERGY VALUES
EMISSION_ENERGY_MIN = 0.01
EMISSION_ENERGY_MAX = 8.0
N_EMISSION = 50
E_EM_VALUES = np.linspace(EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, N_EMISSION)

# TEMPERATURE VALUES
T_MIN = 1.0
T_MAX = 2000.0
N_T = 50
T_VALUES = np.linspace(T_MIN, T_MAX, N_T)

############### FUNCTIONS ###############


# INVERSE THERMAL ENERGY
def beta(T):
    return 1.0 / (k_B * T)


# CHEMICAL POTENTIAL
def chemical_potential(T: float | np.ndarray) -> float | np.ndarray:
    T_F = E_F / k_B
    return E_F * (1 - (np.pi**2 / 12) * ((T / T_F) ** 2))


# ELECTRON DENSITY OF STATES
def eDOS(E: float | np.ndarray) -> float | np.ndarray:
    return ((m_e**1.5) / (np.pi**2 * hbar**3)) * np.sqrt(2 * E)


# FERMI-DIRAC DISTRIBUTION
def f_T(E, T):
    mu = chemical_potential(T)
    beta_T = beta(T)
    exp_E = np.exp(beta_T * (E - mu))
    return 1.0 / (exp_E + 1)


# NON-EQUILIBRIUM ("HOT") DISTRIBUTION
def f_neq(E, T, hw_L, delta_E):
    """
    Non-equilibrium distribution perturbed by laser hw_L.
    f = f_T + delta_E * [f_T(E-hw_L)(1-f_T(E)) - f_T(E)(1-f_T(E+hw_L))]
    """
    ft = f_T(E, T)
    ft_minus = f_T(E - hw_L, T)
    ft_plus = f_T(E + hw_L, T)
    B = ft_minus * (1 - ft) - ft * (1 - ft_plus)
    return ft + delta_E * B


# BOSE-EINSTEIN DISTRIBUTION
def n_B(hw, T):
    beta_T = beta(T)
    with np.errstate(over="ignore"):
        exp_arg = beta_T * hw
        return 1.0 / (np.expm1(exp_arg))


# (STABLE) THERMAL FACTOR
def F_T(E1, E2, T):
    """Stable thermal factor f(E1)[1-f(E2)]"""
    beta_T = beta(T)
    mu = chemical_potential(T)
    a1 = beta_T * (E1 - mu)
    a2 = beta_T * (E2 - mu)
    return np.exp(a2 - np.logaddexp(0.0, a2) - np.logaddexp(0.0, a1))


# (CLIPPED) LOGARITHMIC RELATIVE ERROR
def relative_error(candidate: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """Elementwise |(candidate-reference)/reference|, with 0/0 -> 0."""

    rel = np.abs(candidate - reference) / np.abs(reference)
    rel = np.clip(rel, 1e-16, 1.0)
    return np.log10(rel)


def plot_distributions(hw, T, *, save_name: str | None = None):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.5), sharex=True)
    fig.subplots_adjust(bottom=0.18, hspace=0.08)

    x_offset = 0.02 * (E_MAX - E_MIN)
    logF = lambda hw_val, T_val: np.log10(
        np.clip(F_T(E_GRID + hw_val, E_GRID, T_val), 1e-300, None)
    )

    # Occupation panel
    (line_e,) = ax1.plot(
        E_GRID, f_T(E_GRID + hw, T=T), label="f(E + ℏω)", linewidth=2.2
    )
    (line_h,) = ax1.plot(E_GRID, 1 - f_T(E_GRID, T=T), label="1 - f(E)", linewidth=2.2)
    v_EF = ax1.axvline(E_F, color="k", linestyle="--", alpha=0.25)
    v_EF_hw = ax1.axvline(E_F - hw, color="k", linestyle=":", alpha=0.25)
    label_EF = ax1.text(
        E_F + x_offset,
        0.95,
        r"$E_F$",
        transform=ax1.get_xaxis_transform(),
        va="top",
        ha="left",
        alpha=0.55,
    )
    label_EF_hw = ax1.text(
        (E_F - hw) + x_offset,
        0.95,
        r"$E_F-\hbar\omega$",
        transform=ax1.get_xaxis_transform(),
        va="top",
        ha="left",
        alpha=0.55,
    )
    ax1.set_ylabel("Occupation")
    ax1.set_xlim(E_MIN, E_MAX)
    ax1.legend(loc="best")

    # Thermal factor panel (no cutoff slider)
    F0 = logF(hw, T)
    (line_F,) = ax2.plot(E_GRID, F0, label="log(F(E, ℏω))", linewidth=2.2)
    fill_F = ax2.fill_between(E_GRID, F0, np.min(F0), color="lightskyblue", alpha=0.30)
    ax2.set(xlabel="E [eV]", ylabel="thermal factor")
    ax2.set_ylim(-80, 0)
    ax2.legend(loc="best")

    ax_T = fig.add_axes([0.12, 0.10, 0.78, 0.03])
    ax_hw = fig.add_axes([0.12, 0.05, 0.78, 0.03])
    s_T = Slider(ax_T, "T [K]", T_MIN, T_MAX, valinit=float(T), valstep=1.0)
    s_hw = Slider(
        ax_hw,
        "ℏω [eV]",
        EMISSION_ENERGY_MIN,
        EMISSION_ENERGY_MAX,
        valinit=float(hw),
        valstep=0.01,
    )

    def _update(_val):
        nonlocal fill_F
        T_val = float(s_T.val)
        hw_val = float(s_hw.val)
        line_e.set_ydata(f_T(E_GRID + hw_val, T=T_val))
        line_h.set_ydata(1 - f_T(E_GRID, T=T_val))
        x_EF_hw = E_F - hw_val
        v_EF_hw.set_xdata([x_EF_hw, x_EF_hw])
        label_EF_hw.set_x(x_EF_hw + x_offset)
        y = logF(hw_val, T_val)
        line_F.set_ydata(y)
        if fill_F is not None:
            fill_F.remove()

        fill_F = ax2.fill_between(E_GRID, y, -80, color="lightskyblue", alpha=0.30)

        fig.canvas.draw_idle()

    s_T.on_changed(_update)
    s_hw.on_changed(_update)

    def _save_without_sliders(filename: str) -> None:
        slider_axes = [ax_T, ax_hw]
        vis = [ax.get_visible() for ax in slider_axes]
        for ax in slider_axes:
            ax.set_visible(False)
        fig.canvas.draw_idle()
        save_svg(fig, filename)
        for ax, v in zip(slider_axes, vis):
            ax.set_visible(v)
        fig.canvas.draw_idle()

    if save_name is not None:
        _save_without_sliders(save_name)
    plt.show()


def plot_edos_relative_error(
    hw: float | None = None,
    *,
    hw_values: np.ndarray | None = None,
    E_values: np.ndarray | None = None,
    save_name: str | None = None,
):
    """Plot heatmap of log10 relative error of g(E)g(E+hw) vs g(E_F)^2 over (E, hw)."""

    if hw_values is None:
        hw_values = E_EM_VALUES
    hw_values = np.asanyarray(hw_values, dtype=float)
    if hw_values.ndim != 1:
        raise ValueError("hw_values must be a 1D array")

    if E_values is None:
        E_values = np.linspace(E_MIN, E_MAX, 100)
    E_values = np.asanyarray(E_values, dtype=float)
    if E_values.ndim != 1:
        raise ValueError("E_values must be a 1D array")

    g_ref = eDOS(E_F) ** 2
    g_E = eDOS(E_values)
    g_E_plus_hw = eDOS(E_values[None, :] + hw_values[:, None])
    rel = relative_error(g_E[None, :] * g_E_plus_hw, g_ref)

    fig, ax = plt.subplots(figsize=(8.5, 6.0))
    m = ax.pcolormesh(
        E_values,
        hw_values,
        rel,
        shading="auto",
        cmap="coolwarm",
        vmin=-16,
        vmax=0,
    )

    ax.set(
        xlabel="E [eV]", ylabel=r"$\hbar\omega$ [eV]", xlim=(E_values[0], E_values[-1])
    )
    ax.axvline(E_F, color="k", linestyle="--", alpha=0.25)
    if hw is not None:
        ax.axhline(float(hw), color="k", linestyle=":", alpha=0.25)

    fig.colorbar(m, ax=ax, pad=0.10, label=r"$\log_{10}|\delta_{rel}|$")

    if save_name is not None:
        save_svg(fig, save_name)
    plt.show()


if __name__ == "__main__":
    apply_style()
    plot_distributions(2.0, 300.0, save_name="thermal_factor_distributions_default.png")
    plot_edos_relative_error(save_name="edos_relative_error_default.png")
