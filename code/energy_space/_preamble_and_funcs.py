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
    rel = np.abs((candidate - reference) / reference)

    # rel = np.where(reference == 0.0, np.where(candidate == 0.0, 0.0, np.inf), rel)
    rel = np.clip(rel, 1e-16, 1.0)
    return np.log10(rel)
    # rel = np.abs((candidate - reference) / reference)
    # rel = np.log10(np.clip(rel, 1e-16, 1.0))
    # return rel


def plot_distributions(hw, T, *, is_eDOS = 'const',save_name: str | None = None):
    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.subplots_adjust(bottom=0.27, hspace=0.05)

    e = f_T(E_GRID + hw, T=T)
    h = 1 - f_T(E_GRID, T=T)
    (line_e,) = ax1.plot(E_GRID, e, label="f(E + ℏω)", linewidth=2.2)
    (line_h,) = ax1.plot(E_GRID, h, label="1 - f(E)", linewidth=2.2)
    v_EF = ax1.axvline(E_F, color="k", linestyle="--", alpha=0.25)
    v_EF_hw = ax1.axvline(E_F - hw, color="k", linestyle=":", alpha=0.25)
    x_offset = 0.02 * (E_MAX - E_MIN)
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


    F = np.log10(np.clip(F_T(E_GRID, hw, T), 1e-300, None))
    if is_eDOS == 'const':
        print("Using constant eDOS")
        FF = eDOS(E_F)**2 * F
    elif is_eDOS == 'var':
        print("Using variable eDOS")
        FF = eDOS(E_GRID) * eDOS(E_GRID + hw) * F
    else:
        raise ValueError("eDOS must be 'const' or 'var'")

    (line_F,) = ax2.plot(E_GRID, FF, label="log(F(E, ℏω))", linewidth=2.2)
    
    ax2.set_xlabel("E [eV]")
    ax2.set_ylabel("thermal factor")
    ax2.set_ylim(-80, 0)
    ax2.legend(loc="best")

    

    cutoff0 = -10.0
    line_cut = ax2.axhline(cutoff0, color="k", alpha=0.35, linewidth=1.0)
    y_bottom = float(ax2.get_ylim()[0])
    width_text = ax2.text(
        0.02,
        0.96,
        "",
        transform=ax2.transAxes,
        va="top",
        ha="left",
        fontsize=11,
        bbox={"facecolor": "white", "alpha": 0.55, "edgecolor": "none", "pad": 2},
    )

    blue_fill = None
    red_fill = None

    def _update_fills(y, cutoff):
        nonlocal blue_fill, red_fill
        if blue_fill is not None:
            blue_fill.remove()
        if red_fill is not None:
            red_fill.remove()

        blue_fill = ax2.fill_between(
            E_GRID,
            y,
            cutoff,
            where=y >= cutoff,
            color="lightskyblue",
            alpha=0.30,
        )
        red_fill = ax2.fill_between(
            E_GRID,
            np.minimum(y, cutoff),
            y_bottom,
            color="lightcoral",
            alpha=0.30,
        )

        mask = y >= cutoff
        width = float(E_GRID[mask].max() - E_GRID[mask].min()) if np.any(mask) else 0.0
        width_text.set_text(f"cut={cutoff:.1f}, w={width:.3f} eV")

    ax_cut = fig.add_axes([0.12, 0.15, 0.78, 0.03])
    ax_T = fig.add_axes([0.12, 0.10, 0.78, 0.03])
    ax_hw = fig.add_axes([0.12, 0.05, 0.78, 0.03])
    s_cut = Slider(ax_cut, "cutoff", y_bottom, 0.0, valinit=cutoff0, valstep=1.0)
    s_T = Slider(ax_T, "T [K]", T_MIN, T_MAX, valinit=float(T), valstep=1.0)
    s_hw = Slider(
        ax_hw,
        "ħω [eV]",
        EMISSION_ENERGY_MIN,
        EMISSION_ENERGY_MAX,
        valinit=float(hw),
        valstep=0.01,
    )

    def _update(_val):
        T_val = float(s_T.val)
        hw_val = float(s_hw.val)
        cutoff = float(s_cut.val)
        line_e.set_ydata(f_T(E_GRID + hw_val, T=T_val))
        line_h.set_ydata(1 - f_T(E_GRID, T=T_val))
        x_EF_hw = E_F - hw_val
        v_EF_hw.set_xdata([x_EF_hw, x_EF_hw])
        label_EF_hw.set_x(x_EF_hw + x_offset)
        y = np.log10(np.clip(F_T(E_GRID, hw_val, T_val), 1e-300, None))
        line_F.set_ydata(y)
        line_cut.set_ydata([cutoff, cutoff])
        _update_fills(y, cutoff)
        fig.canvas.draw_idle()

    s_T.on_changed(_update)
    s_hw.on_changed(_update)
    s_cut.on_changed(_update)

    _update_fills(F, cutoff0)
    def _save_without_sliders(filename: str) -> None:
        slider_axes = [ax_cut, ax_T, ax_hw]
        slider_visibility = [ax.get_visible() for ax in slider_axes]
        for ax in slider_axes:
            ax.set_visible(False)
        fig.canvas.draw_idle()
        save_svg(fig, filename)
        for ax, visible in zip(slider_axes, slider_visibility):
            ax.set_visible(visible)
        fig.canvas.draw_idle()

    if save_name is not None:
        _save_without_sliders(save_name)
    plt.show()


if __name__ == "__main__":
    plot_distributions(2.0, 300.0,is_eDOS='var', save_name="thermal_factor_distributions_default.svg")
