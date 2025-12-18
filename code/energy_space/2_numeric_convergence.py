import matplotlib.pyplot as plt
import numpy as np
import plot_style
import _preamble_and_funcs import chemical_potential, k_B, E_EM_VALUES, E_GRID, F_T, integral_const_edos_exact, make_energy_grid_simpson, mean_abs_relative_error, relative_error
from scipy.integrate import trapezoid

def I6(hw, T, E_F):
    mu = chemical_potential(E_F, T)
    beta = 1.0 / (k_B * T)

    log1pa = np.logaddexp(0.0, -beta * mu)                 # log(1 + e^{-βμ})
    log1pb = np.logaddexp(0.0, beta * (hw - mu))           # log(1 + e^{β(hw-μ)})
    return  hw + (1.0 / beta) * (log1pa - log1pb)

def I5(hw, T, E_F):
    mu = chemical_potential(E_F, T)
    F = F_T(hw, mu, T)
    return trapezoid(F, E_EM_VALUES)

def rel_error_numeric_vs_exact(
    hw_values: np.ndarray, T: float, E_F: float, *, E_grid: np.ndarray | None = None
) -> np.ndarray:
    I_num = integral_const_edos_numeric(hw_values, T, E_F, E_grid=E_grid)
    I_exact = integral_const_edos_exact(hw_values, T, E_F)
    return relative_error(I_num, I_exact)


REL_ERROR_CASES = [
    {"T": 300.0, "E_F": 5.0, "title": "T = 300 K, E_F = 5 eV"},
    {"T": 300.0, "E_F": 3.0, "title": "T = 300 K, E_F = 3 eV"},
    {"T": 700.0, "E_F": 3.0, "title": "T = 700 K, E_F = 3 eV"},
    {"T": 1000.0, "E_F": 3.0, "title": "T = 1000 K, E_F = 3 eV"},
]


def mean_abs_rel_error_numeric_vs_exact(
    hw_values: np.ndarray,
    T: float,
    E_F: float,
    *,
    E_grid: np.ndarray,
    reference_floor_ratio: float = 1e-12,
) -> float:
    """Mean |δ_rel| over the hw range (ignoring tiny reference values)."""

    I_num = integral_const_edos_numeric(hw_values, T, E_F, E_grid=E_grid)
    I_exact = integral_const_edos_exact(hw_values, T, E_F)
    return mean_abs_relative_error(
        I_num, I_exact, reference_floor_ratio=reference_floor_ratio
    )


def show_convergence_mean_rel_error_vs_dE(
    *,
    hw_values: np.ndarray | None = None,
    candidate_dE: np.ndarray | None = None,
    reference_floor_ratio: float = 1e-12,
) -> None:
    """Plot ⟨|δ_rel|⟩_{hw} vs integration step ΔE."""

    if hw_values is None:
        # Subsample for speed while still covering the full hw range.
        hw_values = E_EM_VALUES[::5]
    else:
        hw_values = np.asarray(hw_values, dtype=float)

    if candidate_dE is None:
        candidate_dE = np.array([1e-1, 1e-2, 1e-3, 1e-4], dtype=float)
    else:
        candidate_dE = np.asarray(candidate_dE, dtype=float)
    candidate_dE = np.sort(candidate_dE)[::-1]

    dE_eff_values = np.empty_like(candidate_dE, dtype=float)
    mean_err_by_case = np.empty((candidate_dE.size, len(REL_ERROR_CASES)), dtype=float)

    for i, dE in enumerate(candidate_dE):
        E_grid, dE_eff = make_energy_grid_simpson(float(dE))
        dE_eff_values[i] = dE_eff
        for j, case in enumerate(REL_ERROR_CASES):
            T = float(case["T"])
            E_F = float(case["E_F"])
            mean_err_by_case[i, j] = mean_abs_rel_error_numeric_vs_exact(
                hw_values,
                T,
                E_F,
                E_grid=E_grid,
                reference_floor_ratio=reference_floor_ratio,
            )

    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    for j, case in enumerate(REL_ERROR_CASES):
        ax.loglog(
            dE_eff_values,
            mean_err_by_case[:, j],
            marker="o",
            markersize=4,
            label=str(case["title"]),
        )

    worst = np.nanmax(mean_err_by_case, axis=1)
    ax.loglog(dE_eff_values, worst, color="k", linewidth=2.0, label="max over cases")

    ax.set_xlabel(r"$\Delta \mathcal{E}$ [eV]")
    ax.set_ylabel(r"$\langle |\delta_{rel}| \rangle_{\hbar\omega}$")
    ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)
    ax.set_xlim(float(np.max(dE_eff_values)), float(np.min(dE_eff_values)))
    ax.set_ylim(1e-20, 1.0)
    ax.legend()

    title = r"Integration-step convergence: $\langle |\delta_{rel}| \rangle_{\hbar\omega}$ vs $\Delta\mathcal{E}$"
    set_figure_title(fig, title)
    save_svg(fig, "stage_2_convergence_mean_rel_error_vs_dE.svg")
    plt.show()


def show_rel_error_grid() -> None:
    dE_used = float(E_GRID[1] - E_GRID[0])
    fig, axes = plt.subplots(2, 2, figsize=(11, 5), sharex=True, sharey=True)
    for ax, case in zip(axes.flat, REL_ERROR_CASES):
        T = float(case["T"])
        E_F = float(case["E_F"])
        rel = rel_error_numeric_vs_exact(E_EM_VALUES, T, E_F)

        ax.semilogy(E_EM_VALUES, np.clip(rel, 1e-20, None), color="C0")
        ax.set_title(str(case["title"]))
        ax.set_xlim(float(E_EM_VALUES[0]), float(E_EM_VALUES[-1]))
        ax.set_ylim(1e-16, 1e-10)
        ax.grid(True, which="both", linestyle=":", linewidth=0.6, alpha=0.5)

    axes[1, 0].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[1, 1].set_xlabel(r"$\hbar\omega$ [eV]")
    axes[0, 0].set_ylabel(r"$|\delta_{rel}|$")
    axes[1, 0].set_ylabel(r"$|\delta_{rel}|$")

    title = f"Const eDOS: relative error (numeric integral vs analytic exact), ΔE≈{dE_used:.2e} eV"
    set_figure_title(fig, title)
    save_svg(fig, "stage_2_rel_error_grid.svg")
    plt.show()


if __name__ == "__main__":
    apply_style()
    show_convergence_mean_rel_error_vs_dE()
    show_rel_error_grid()
