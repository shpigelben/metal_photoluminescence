import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../main")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from plot_style import apply_style, save_svg
import matplotlib.ticker as ticker

INTEGRAND = "cos"  # Options: "poly" (x^2), "cos" (cos(x))

def gaussian(x, mu, sigma):
    # Vectorized Gaussian: works if x and sigma are broadcastable
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


def calculate_error_grid(mu, L, sigma_vals, frac_vals):
    """
    Calculates error grid where dy (y-axis) is a fraction of sigma/2.
    dx = frac * (sigma / 2)

    Vectorized over sigma values (inner loop) for performance.
    """
    error_grid = np.zeros((len(frac_vals), len(sigma_vals)))

    # Pre-broadcast sigma for vectorization
    # shape: (N_sigma, 1)
    sigma_col = sigma_vals[:, np.newaxis]
    
    if INTEGRAND == "poly":
        ref = mu**2
    elif INTEGRAND == "cos":
        # Limit sigma -> 0 of integral is cos(mu)
        ref = np.cos(mu)

    for i, frac in enumerate(frac_vals):
        # Determine number of points needed to cover [-L*sigma, L*sigma]
        # n_points is constant for a given fraction
        n_points = int(np.ceil(4 * L / frac)) + 1

        if n_points < 4:
            # Insufficient points for reliable integration
            error_grid[i, :] = 0.0  # log10(1.0) = 0
            continue

        # Normalized grid t from -L to L
        # shape: (1, n_points)
        t = np.linspace(-L, L, n_points)[np.newaxis, :]

        # Vectorized calculation over all sigmas for this fraction
        # X shape: (N_sigma, n_points)
        X = mu + sigma_col * t

        # Y shape: (N_sigma, n_points)
        if INTEGRAND == "poly":
            Y = (X**2) * gaussian(X, mu, sigma_col)
        elif INTEGRAND == "cos":
            Y = np.cos(X) * gaussian(X, mu, sigma_col)

        # Integrate along the spatial axis (axis 1)
        # Result shape: (N_sigma,)
        integrals = simpson(Y, x=X, axis=1)

        if ref == 0:
            errs = np.abs(integrals)
        else:
            errs = np.abs((integrals - ref) / ref)

        # Clip and log
        error_grid[i, :] = np.log10(np.maximum(errs, 1e-16))

    return error_grid


def main():
    apply_style()

    mu = 2.0
    L_values = [4, 7, 10]

    # Parameter Ranges
    sigma_vals = np.logspace(-10, -1, 30)
    frac_vals = np.logspace(-5, 0.3, 30)

    # Pre-calculate all grids
    results = []
    global_min = float("inf")
    global_max = float("-inf")
    Z_L10 = None
                 
    print("Calculating error grids...")
    for L in L_values:
        print(f"  Processing L={L}...")
        Z = calculate_error_grid(mu, L, sigma_vals, frac_vals)

        current_min = np.nanmin(Z)
        current_max = np.nanmax(Z)
        if current_min < global_min:
            global_min = current_min
        if current_max > global_max:
            global_max = current_max

        if L == 10:
            Z_L10 = Z

        results.append((L, Z))

    # Use constrained_layout to help with spacing automatically
    fig, axes = plt.subplots(
        1, 3, figsize=(15, 6), sharey=True, sharex=True, constrained_layout=True
    )

    SIGMA, FRAC = np.meshgrid(sigma_vals, frac_vals)
    # Calculate physical dx at every point for contours
    DX_GRID = FRAC * (SIGMA / 2.0)

    last_mesh = None
    for ax, (L, Z) in zip(axes, results):
        # Set scales FIRST to avoid artifacts with contours
        ax.set_xscale("log")
        ax.set_yscale("log")

        last_mesh = ax.pcolormesh(
            SIGMA,
            FRAC,
            Z,
            shading="auto",
            cmap="viridis",
            vmin=global_min,
            vmax=global_max,
        )

        n_points_vals = (np.ceil(4 * L / frac_vals) + 1).astype(int)
        n_min = int(n_points_vals.min())
        n_max = int(n_points_vals.max())

        # Add contours for constant dx
        # Automatically generate levels across the range of the grid
        # Avoid extreme float precision issues by clamping min level
        dx_min, dx_max = np.nanmin(DX_GRID), np.nanmax(DX_GRID)

        # Ensure we don't go below reasonable float precision for plotting
        safe_min = max(dx_min, 1e-15)

        # Create log-spaced levels
        levels = np.logspace(np.ceil(np.log10(safe_min)), np.floor(np.log10(dx_max)), 7)

        CS = ax.contour(
            SIGMA,
            FRAC,
            DX_GRID,
            levels=levels,
            colors="white",
            linewidths=0.8,
            alpha=0.7,
        )
        ax.clabel(
            CS,
            inline=True,
            fontsize=8,
            fmt=lambda x: f"$dx=10^{{{int(np.round(np.log10(x)))}}}$",
        )

        ax.set_title(f"L = {L}")
        ax.set_xlabel(r"$\sigma \ [x]$")
        if ax == axes[0]:
            ax.set_ylabel(r"$s = \Delta x \  / \  2\sigma \ \text{[a.u]}$")

        ax.text(
            0.02,
            0.98,
            f"grid points n: {n_min:,} to {n_max:,}\n"
            r"$n=\lceil 4L/s \rceil + 1$",
            transform=ax.transAxes,
            va="top",
            ha="left",
            fontsize=9,
            color="white",
            bbox=dict(
                facecolor="black",
                alpha=0.35,
                edgecolor="none",
                boxstyle="round,pad=0.2",
            ),
        )

    fig.colorbar(
        last_mesh,
        ax=axes.ravel().tolist(),
        label=r"$\log_{10}(\epsilon_{rel})$",
        # pad=0.08  # constrained_layout handles padding better usually
    )

    # Move suptitle up slightly to avoid overlap
    if INTEGRAND == "poly":
        title_str = r"$\int x^2 G_\sigma(x-\mu) dx \approx \mu^2$"
    else:
        title_str = r"$\int \cos(x) G_\sigma(x-\mu) dx \approx \cos(\mu)$"

    plt.suptitle(
        f"1D Delta Convergence: {title_str}\n(Contours show physical $dx$)",
        fontsize=16,
        y=1.05,
    )

    # Save to figures folder instead of blocking with show()
    filename = f"delta_convergence_{INTEGRAND}.png"
    path = save_svg(fig, filename)
    print(f"Saving figure to {path}...", flush=True)

    # Fine grid figure for L=10 with target rel error ~1e-14.
    L_fine = 10
    target_log = -14.0
    fine_points = 70

    if Z_L10 is None:
        Z_L10 = calculate_error_grid(mu, L_fine, sigma_vals, frac_vals)

    reach_mask = Z_L10 <= target_log
    if np.any(reach_mask):
        sigma_hit = sigma_vals[reach_mask.any(axis=0)]
        frac_hit = frac_vals[reach_mask.any(axis=1)]

        pad_decades = 0.35
        sigma_min = max(
            sigma_vals.min(), 10 ** (np.log10(sigma_hit.min()) - pad_decades)
        )
        sigma_max = min(
            sigma_vals.max(), 10 ** (np.log10(sigma_hit.max()) + pad_decades)
        )
        frac_min = max(
            frac_vals.min(), 10 ** (np.log10(frac_hit.min()) - pad_decades)
        )
        frac_max = min(
            frac_vals.max(), 10 ** (np.log10(frac_hit.max()) + pad_decades)
        )
    else:
        sigma_min, sigma_max = sigma_vals.min(), sigma_vals.max()
        frac_min, frac_max = frac_vals.min(), frac_vals.max()

    n_min = int(np.ceil(4 * L_fine / frac_max)) + 1
    n_max = int(np.ceil(4 * L_fine / frac_min)) + 1
    n_min = max(n_min, 4)
    n_max = max(n_max, n_min)

    if n_max == n_min:
        n_vals_fine = np.array([n_min], dtype=int)
    else:
        n_vals_fine = np.unique(
            np.round(
                np.logspace(np.log10(n_min), np.log10(n_max), fine_points)
            ).astype(int)
        )
        if n_vals_fine.size < 2:
            n_vals_fine = np.array(sorted({n_min, n_max}), dtype=int)

    sigma_vals_fine = np.logspace(np.log10(sigma_min), np.log10(sigma_max), fine_points)
    frac_vals_fine = 4 * L_fine / (n_vals_fine - 1)

    print("Calculating fine grid for L=10...", flush=True)
    Z_fine = calculate_error_grid(mu, L_fine, sigma_vals_fine, frac_vals_fine)

    SIGMA_FINE, _ = np.meshgrid(sigma_vals_fine, frac_vals_fine)
    N_FINE = np.broadcast_to(n_vals_fine[:, np.newaxis], SIGMA_FINE.shape)
    fig_fine, ax_fine = plt.subplots(figsize=(7.2, 6.0), constrained_layout=True)
    ax_fine.set_xscale("log")
    ax_fine.set_yscale("log")

    fine_mesh = ax_fine.pcolormesh(
        SIGMA_FINE,
        N_FINE,
        Z_fine,
        shading="auto",
        cmap="viridis",
    )
    fig_fine.colorbar(
        fine_mesh,
        ax=ax_fine,
        label=r"$\log_{10}(\epsilon_{rel})$",
    )

    target_contour = ax_fine.contour(
        SIGMA_FINE,
        N_FINE,
        Z_fine,
        levels=[target_log],
        colors="white",
        linewidths=1.2,
        linestyles="--",
    )
    ax_fine.clabel(
        target_contour,
        inline=True,
        fontsize=8,
        fmt=lambda _: r"$10^{-14}$",
    )

    max_n = 500
    combined_mask = (Z_fine <= target_log) & (N_FINE < max_n)

    if np.any(combined_mask):
        ax_fine.contourf(
            SIGMA_FINE,
            N_FINE,
            combined_mask.astype(float),
            levels=[0.5, 1.5],
            colors=["#ffb000"],
            alpha=0.35,
        )
        ax_fine.contour(
            SIGMA_FINE,
            N_FINE,
            combined_mask.astype(float),
            levels=[0.5],
            colors="#ffb000",
            linewidths=1.4,
        )

        ax_fine.text(
            0.02,
            0.02,
            "shaded: rel err <= 1e-14 and n < 500",
            transform=ax_fine.transAxes,
            ha="left",
            va="bottom",
            fontsize=9,
            color="white",
            bbox=dict(
                facecolor="black",
                alpha=0.35,
                edgecolor="none",
                boxstyle="round,pad=0.2",
            ),
        )
    else:
        ax_fine.text(
            0.02,
            0.02,
            "No points with rel err <= 1e-14 and n < 500",
            transform=ax_fine.transAxes,
            ha="left",
            va="bottom",
            fontsize=9,
            color="white",
            bbox=dict(
                facecolor="black",
                alpha=0.35,
                edgecolor="none",
                boxstyle="round,pad=0.2",
            ),
        )

    ax_fine.set_title("L = 10 (fine grid)")
    ax_fine.set_xlabel(r"$\sigma \ [x]$")
    ax_fine.set_ylabel(r"$n = \lceil 4L/s \rceil + 1$")

    fine_filename = f"delta_convergence_{INTEGRAND}_L10_fine.png"
    fine_path = save_svg(fig_fine, fine_filename)
    print(f"Saving fine figure to {fine_path}...", flush=True)
    plt.show()
    print("Done.", flush=True)

if __name__ == "__main__":
    main()
