import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Allow importing shared plotting style from ../plot_style.py when run as a script.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from plot_style import apply_style, save_svg

# Constants (energy in eV)
k_B = 8.617333262145e-5  # eV/K

E_MIN = 0.0
E_MAX = 10.0


def chemical_potential(E_F: float, T: float) -> float:
    T_F = E_F / k_B
    return E_F * (1 - (np.pi**2 / 12) * ((T / T_F) ** 2))


def fermi_occupation_mu_beta(E: np.ndarray, mu: float, beta: float) -> np.ndarray:
    """Stable f(E) = 1/(exp(beta(E-mu)) + 1)."""

    a = beta * (np.asarray(E, dtype=float) - mu)
    return np.exp(-np.logaddexp(0.0, a))


def fermi_hole_mu_beta(E: np.ndarray, mu: float, beta: float) -> np.ndarray:
    """Stable 1 - f(E)."""

    a = beta * (np.asarray(E, dtype=float) - mu)
    return np.exp(a - np.logaddexp(0.0, a))


def fermi_product_mu_beta(E: np.ndarray, hw: float, mu: float, beta: float) -> np.ndarray:
    """Stable f(E+hw)[1-f(E)] (log-form)."""

    E = np.asarray(E, dtype=float)
    a = beta * (E - mu)
    b = a + beta * hw
    log_val = a - np.logaddexp(0.0, a) - np.logaddexp(0.0, b)
    return np.exp(log_val)


def show_fermi_product_interactive() -> None:
    E_plot = np.linspace(E_MIN, E_MAX, 2500)
    E_F0 = 5.0
    T0 = 300.0
    hw0 = 1.0
    y_floor = 1e-20

    fig, ax = plt.subplots(figsize=(10, 5.2))
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.32, top=0.90)

    mu0 = chemical_potential(E_F0, T0)
    beta0 = 1.0 / (k_B * T0)

    y = fermi_product_mu_beta(E_plot, hw0, mu0, beta0)
    (line_prod,) = ax.semilogy(
        E_plot,
        np.clip(y, 1e-300, None),
        color="C0",
        label=r"$f(\mathcal{E}+\hbar\omega)\,[1-f(\mathcal{E})]$",
    )
    fill = [
        ax.fill_between(
            E_plot,
            y_floor,
            np.clip(y, y_floor, None),
            color=line_prod.get_color(),
            alpha=0.18,
            zorder=line_prod.get_zorder() - 1,
        )
    ]

    f_plus = fermi_occupation_mu_beta(E_plot + hw0, mu0, beta0)
    (line_fplus,) = ax.semilogy(
        E_plot,
        np.clip(f_plus, 1e-300, None),
        color="C1",
        alpha=0.35,
        label=r"$f(\mathcal{E}+\hbar\omega)$",
    )

    hole = fermi_hole_mu_beta(E_plot, mu0, beta0)
    (line_hole,) = ax.semilogy(
        E_plot,
        np.clip(hole, 1e-300, None),
        color="C2",
        alpha=0.35,
        label=r"$1-f(\mathcal{E})$",
    )

    v_mu = ax.axvline(mu0, color="k", linestyle="--", alpha=0.7, label=r"$\mu$")
    v_muhw = ax.axvline(mu0 - hw0, color="k", linestyle=":", alpha=0.5, label=r"$\mu-\hbar\omega$")

    ax.set_xlabel(r"$\mathcal{E}$ [eV]")
    ax.set_ylabel(r"Occupation / product")
    ax.set_title("Thermal factor: f(E+ħω)[1−f(E)]")
    ax.set_xlim(E_MIN, E_MAX)
    ax.set_ylim(y_floor, 1.0)
    ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)
    ax.legend(loc="upper right")

    info = ax.text(0.02, 0.96, "", transform=ax.transAxes, va="top")

    ax_EF = fig.add_axes([0.10, 0.21, 0.82, 0.03])
    ax_T = fig.add_axes([0.10, 0.16, 0.82, 0.03])
    ax_hw = fig.add_axes([0.10, 0.11, 0.82, 0.03])

    s_EF = Slider(ax_EF, r"$\mathcal{E}_F$ [eV]", 1.0, 7.0, valinit=E_F0, valstep=0.1)
    s_T = Slider(ax_T, r"$T$ [K]", 50.0, 5000.0, valinit=T0, valstep=10.0)
    s_hw = Slider(ax_hw, r"$\hbar\omega$ [eV]", 0.0, 8.0, valinit=hw0, valstep=0.01)

    def _update(_val: float) -> None:
        E_F = float(s_EF.val)
        T = float(s_T.val)
        hw = float(s_hw.val)

        mu = chemical_potential(E_F, T)
        beta = 1.0 / (k_B * T)

        y_new = fermi_product_mu_beta(E_plot, hw, mu, beta)
        line_prod.set_ydata(np.clip(y_new, 1e-300, None))
        line_fplus.set_ydata(np.clip(fermi_occupation_mu_beta(E_plot + hw, mu, beta), 1e-300, None))
        line_hole.set_ydata(np.clip(fermi_hole_mu_beta(E_plot, mu, beta), 1e-300, None))

        fill[0].remove()
        fill[0] = ax.fill_between(
            E_plot,
            y_floor,
            np.clip(y_new, y_floor, None),
            color=line_prod.get_color(),
            alpha=0.18,
            zorder=line_prod.get_zorder() - 1,
        )

        v_mu.set_xdata([mu, mu])
        v_muhw.set_xdata([mu - hw, mu - hw])

        info.set_text(f"mu={mu:.3f} eV, kBT={k_B*T:.4f} eV")
        fig.canvas.draw_idle()

    s_EF.on_changed(_update)
    s_T.on_changed(_update)
    s_hw.on_changed(_update)

    _update(0.0)
    save_svg(fig, "fermi_product_interactive_default.svg")

    def _on_key(event) -> None:
        if event.key == "s":
            save_svg(fig, "fermi_product_interactive.svg")

    fig.canvas.mpl_connect("key_press_event", _on_key)
    plt.show()


if __name__ == "__main__":
    apply_style()
    show_fermi_product_interactive()
