import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from plot_style import save_svg

############### PREAMBLE ###############

# Physical constants (energy in eV)
k_B = 8.617333262145e-5  # eV/K
hbar = 6.582119569e-16
m_e = 5.485e-4

# INTEGRATION PARAMETERS
E_F = 5.0
E_MIN = 0.0
E_MAX = 10.0
D_E = 5e-4
E_GRID = np.arange(E_MIN, E_MAX + D_E, D_E)

# EMISSION ENERGY VALUES
EMISSION_ENERGY_MIN = 0.01
EMISSION_ENERGY_MAX = 8.0
N_EMISSION = 100
E_EM_VALUES = np.linspace(EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, N_EMISSION)

# TEMPERATURE VALUES
T_MIN = 1.0
T_MAX = 2000.0
N_T = 100
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

# BOSE-EINSTEIN DISTRIBUTION
def n_B(hw, T):
    beta_T = beta(T)
    with np.errstate(over="ignore"):
        exp_arg = beta_T * hw
        return 1.0 / (np.expm1(exp_arg))

# (STABLE) THERMAL FACTOR
def F_T(E, hw, T):
    mu = chemical_potential(T)
    beta_T = beta(T)
    a = beta_T * (E - mu)
    b = a + beta_T * hw
    return np.exp(a - np.logaddexp(0.0, a) - np.logaddexp(0.0, b))

# (CLIPPED) LOGARITHMIC RELATIVE ERROR
def relative_error(candidate: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """Elementwise |(candidate-reference)/reference|, with 0/0 -> 0."""

    # candidate = np.asarray(candidate, dtype=float)
    # reference = np.asarray(reference, dtype=float)
    # with np.errstate(divide="ignore", invalid="ignore"):
    rel = np.abs(candidate - reference) / np.abs(reference)

    # rel = np.where(reference == 0.0, np.where(candidate == 0.0, 0.0, np.inf), rel)
    rel = np.clip(rel, 1e-16, 1.0)
    return np.log10(rel)
    # rel = np.abs((candidate - reference) / reference)
    # rel = np.log10(np.clip(rel, 1e-16, 1.0))
    # return rel


def plot_distributions(hw, T, *, save_name: str | None = None):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.5), sharex=True)
    fig.subplots_adjust(bottom=0.18, hspace=0.08)

    x_offset = 0.02 * (E_MAX - E_MIN)
    logF = lambda hw_val, T_val: np.log10(np.clip(F_T(E_GRID, hw_val, T_val), 1e-300, None))

    # Occupation panel
    (line_e,) = ax1.plot(E_GRID, f_T(E_GRID + hw, T=T), label="f(E + ℏω)", linewidth=2.2)
    (line_h,) = ax1.plot(E_GRID, 1 - f_T(E_GRID, T=T), label="1 - f(E)", linewidth=2.2)
    v_EF = ax1.axvline(E_F, color="k", linestyle="--", alpha=0.25)
    v_EF_hw = ax1.axvline(E_F - hw, color="k", linestyle=":", alpha=0.25)
    label_EF = ax1.text(E_F + x_offset, 0.95, r"$E_F$", transform=ax1.get_xaxis_transform(), va="top", ha="left", alpha=0.55)
    label_EF_hw = ax1.text((E_F - hw) + x_offset, 0.95, r"$E_F-\hbar\omega$", transform=ax1.get_xaxis_transform(), va="top", ha="left", alpha=0.55)
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
    s_hw = Slider(ax_hw, "ℏω [eV]", EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, valinit=float(hw), valstep=0.01)

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


def plot_edos_relative_error(hw, *, save_name: str | None = None):
    """Plot log10 relative error of g(E)g(E+hw) vs g(E_F)^2 with a hw slider."""

    fig, ax = plt.subplots(figsize=(10, 4.8))
    fig.subplots_adjust(bottom=0.18)

    def _relerr(hw_val):
        g_ref = eDOS(E_F) ** 2
        g_var = eDOS(E_GRID) * eDOS(E_GRID + hw_val)
        return relative_error(g_var, g_ref)

    y0 = _relerr(hw)
    (line,) = ax.plot(E_GRID, y0, linewidth=2.0, label=r"$g(E)g(E+\hbar\omega)$ vs $g(E_F)^2$")
    ax.set_xlabel("E [eV]")
    ax.set_ylabel(r"$\log_{10}|\delta_{rel}|$")
    ax.set(xlim=(E_MIN, E_MAX), ylim=(-16, 0.5))
    ax.legend(loc="best")

    ax_hw = fig.add_axes([0.12, 0.05, 0.78, 0.03])
    s_hw = Slider(ax_hw, "ℏω [eV]", EMISSION_ENERGY_MIN, EMISSION_ENERGY_MAX, valinit=float(hw), valstep=0.01)

    def _update(_val):
        y = _relerr(float(s_hw.val))
        line.set_ydata(y)
        fig.canvas.draw_idle()

    s_hw.on_changed(_update)

    def _save_without_sliders(filename: str) -> None:
        slider_axes = [ax_hw]
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

if __name__ == "__main__":
    plot_distributions(2.0, 300.0, save_name="thermal_factor_distributions_default.svg")
    plot_edos_relative_error(2.0, save_name="edos_relative_error_default.svg")
