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

    # Save to file instead of blocking with show()
    filename = f"delta_convergence_{INTEGRAND}.png"
    print(f"Saving figure to {filename}...", flush=True)
    plt.savefig(filename, dpi=300, transparent=True)
    # plt.show()
    print("Done.", flush=True)

