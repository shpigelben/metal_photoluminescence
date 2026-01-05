import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson
from plot_style import apply_style, save_svg, set_figure_title
from _preamble_and_funcs import *

# --- Definitions ---

def gaussian_delta(x, sigma):
    """Normalized Gaussian approximation of Dirac Delta."""
    return (1.0 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (x / sigma) ** 2)

def I4(E, hw, T):
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    integrand = F_T(E + hw, E, T) * eDOS(E + hw) * eDOS(E)
    return simpson(integrand, E, axis=-1)


# def I3(E, hw, T, sigma, s):
#     E = np.arange(E[0], E[-1], sigma * s)
#     hw = np.asarray(hw)
#     T = np.asarray(T)
#     if hw.size != 1 or T.size != 1:
#         raise ValueError("I3 expects scalar hw and T; loop externally for arrays.")
#     hw = float(hw)
#     T = float(T)

#     if E.size < 2:
#         return np.nan

#     cutoff = 5.0 * sigma
#     dE = float(E[1] - E[0])
#     profile = np.zeros_like(E)

#     for i, E1 in enumerate(E):
#         center = E1 - hw
#         idx_center = int((center - E[0]) / dE)
#         idx_span = int(cutoff / dE) + 2

#         idx_start = max(0, idx_center - idx_span)
#         idx_end = min(len(E), idx_center + idx_span)
#         if idx_start >= idx_end:
#             continue

#         E2 = E[idx_start:idx_end]
#         delta_arg = E1 - E2 - hw
#         delta_val = gaussian_delta(delta_arg, sigma)

#         therm = F_T(E1, E2, T)
#         dos_prod = eDOS(E1) * eDOS(E2)
#         integrand = therm * dos_prod * delta_val
#         profile[i] = simpson(integrand, E2)

#     return simpson(profile, E)

import numpy as np
from scipy.integrate import simpson

def gaussian_delta(x, sigma):
    return (1.0 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (x / sigma) ** 2)

def I3(E_input, hw, T, sigma, points_per_sigma=5.0, max_memory_mb=500):
    """
    Computes I3 using a fine grid for accuracy, but processes in chunks
    to prevent memory crashes.
    """
    hw = np.asarray(hw)
    T = np.asarray(T)
    if hw.size != 1 or T.size != 1:
        raise ValueError("I3 expects scalar hw and T; loop externally for arrays.")
    hw = float(hw)
    T = float(T)
    # 1. UPSAMPLING (Essential for convergence)
    dE_input = E_input[1] - E_input[0]
    target_dE = sigma / points_per_sigma
    
    if dE_input > target_dE:
        num_points = int((E_input[-1] - E_input[0]) / target_dE)
        E_fine = np.linspace(E_input[0], E_input[-1], num_points)
    else:
        E_fine = E_input

    N = len(E_fine)
    
    # 2. DETERMINE BATCH SIZE
    # We create matrices of size (Batch_Size, N). 
    # Each float64 takes 8 bytes. We estimate 4 arrays are active at once.
    # 4 arrays * 8 bytes * N * Batch = Memory_Limit_Bytes
    bytes_per_row = N * 8 * 4 
    memory_limit_bytes = max_memory_mb * 1024 * 1024
    batch_size = int(memory_limit_bytes / bytes_per_row)
    
    # Ensure at least one row is processed
    batch_size = max(1, batch_size) 
    
    # Pre-calculate E2 dependent terms (calculated once, reused)
    # This assumes eDOS is cheap. If expensive, pre-calculate it.
    dos2 = eDOS(E_fine)[None, :]  # Shape (1, N)
    
    total_integral = 0.0
    
    # 3. CHUNKED PROCESSING
    # We iterate over the outer integral variable (E1) in chunks
    for start_idx in range(0, N, batch_size):
        end_idx = min(start_idx + batch_size, N)
        
        # Current chunk of E1
        E1_chunk = E_fine[start_idx:end_idx] # Shape (B,)
        E1_col = E1_chunk[:, None]           # Shape (B, 1)
        
        # Vectorized computation for this chunk only
        # Matrix shape is (Batch_Size, N) - manageable!
        delta_term = gaussian_delta(E1_col - E_fine - hw, sigma)
        
        therm = F_T(E1_col, E_fine, T)
        dos1 = eDOS(E1_chunk)[:, None]
        
        # Integrand for this slice of E1
        integrand_chunk = therm * (dos1 * dos2) * delta_term
        
        # Integrate over inner variable E2 (axis 1)
        # Result is array of values for the current E1 chunk
        inner_results = simpson(integrand_chunk, E_fine, axis=1)
        
        # Now we need to integrate these results over the current E1 chunk.
        # However, Simpson's rule needs context from neighbors for the edges.
        # To keep it simple and accurate, we sum using the Trapezoidal rule 
        # for the outer accumulation, or just store the values to Simpson at the end.
        
        # Better approach for exactness: Store the 1D profile and Simpson at the very end
        # (This is memory cheap: storing N floats is tiny compared to N*N)
        if start_idx == 0:
            full_profile = inner_results
        else:
            full_profile = np.concatenate((full_profile, inner_results))

    # 4. FINAL INTEGRATION
    # Integrate the profile over E1
    return simpson(full_profile, E_fine)



def rel_err_plot(sigma, s):
    hw = np.linspace(0.01, 8.0, 20)
    E = np.arange(0.0, 10.0, 1e-4)
    I_4 = I4(E, hw, 300)
    I_3 = np.array([I3(E, h, 300, sigma, s) for h in hw])
    rel = relative_error(I_3, I_4)
    # return rel
    fig, ax = plt.subplots(figsize=(8.5, 6.0))
    ax.plot(hw, rel, label=f"sigma={sigma:.1e}, s={s}")
    ax.set_xlabel(r"$\hbar\omega$ [eV]")
    ax.set_ylabel(r"$\log_{10}|\delta_{rel}|$")
    ax.set_title("Relative Error between I3 and I4")
    ax.legend()
    plt.show()


# # Candidate: Eq 3* (2D Profile - Low Memory Version)
# def I3_star_profile_low_mem(E_vals, hw, T, sigma):
#     """
#     Computes Eq (3*) for an array of initial energies E_vals using
#     a sliding window to avoid O(N^2) memory usage.
#     """
#     E_vals = np.atleast_1d(E_vals)
#     results = np.zeros_like(E_vals)

#     # Pre-compute constants
#     cutoff = 5.0 * sigma
#     dE = float(E_GRID[1] - E_GRID[0])

#     # We iterate over the requested E_init values (E_vals)
#     # For each E_init, we integrate over E_prime (final state)
#     # Conservation: E_prime - E_init = hw  =>  E_prime approx E_init + hw

#     for i, e_init in enumerate(E_vals):
#         # 1. Determine integration window for E_prime
#         # We need: |E_prime - e_init - hw| < cutoff
#         center_E = e_init + hw

#         # Find indices in E_GRID corresponding to [center - cutoff, center + cutoff]
#         # Since E_GRID is uniform, we can calculate indices directly
#         idx_center = int((center_E - E_GRID[0]) / dE)
#         idx_span = int(cutoff / dE) + 2 # +2 for safety

#         idx_start = max(0, idx_center - idx_span)
#         idx_end = min(len(E_GRID), idx_center + idx_span)

#         if idx_start >= idx_end:
#             results[i] = 0.0
#             continue

#         # 2. Extract slice
#         E_prime_window = E_GRID[idx_start:idx_end]

#         # 3. Compute Integrand on this slice
#         # Argument for delta: E_prime - e_init - hw
#         delta_arg = E_prime_window - e_init - hw

#         # Gaussian
#         delta_val = gaussian_delta(delta_arg, sigma)

#         # Physics Factors: f(E_init)[1-f(E_prime)] * rho(E_init)rho(E_prime)
#         # Stability: Use F_T(e_init, E_prime, T)
#         therm = F_T(e_init, E_prime_window, T)

#         dos_prod = eDOS(E_prime_window) * eDOS(e_init)

#         integrand_slice = therm * dos_prod * delta_val

#         # 4. Integrate slice
#         results[i] = simpson(integrand_slice, E_prime_window)

#     return results

# # --- Total Integrals for Convergence ---

# def I3_total_low_mem(hw, T, sigma):
#     # Integrate profile over E (initial state)
#     # We compute the profile for all E_GRID points
#     y_vals = I3_star_profile_low_mem(E_GRID, hw, T, sigma)
#     return simpson(y_vals, E_GRID)

# def I4_total(hw, T):
#     y_vals = I4_star_profile(E_GRID, hw, T)
#     return simpson(y_vals, E_GRID)


# # --- Plotting Functions ---

# def plot_sigma_convergence(hw=2.0, T=300.0, *, save_name="auto"):
#     """
#     Sweep sigma to find optimal range for TOTAL integral.
#     """
#     print(f"Running sigma convergence for hw={hw}eV, T={T}K...")
#     ref = I4_total(hw, T)
#     dE = float(E_GRID[1] - E_GRID[0])

#     # Sweep from 0.5*dE to 50*dE (Log spacing)
#     # Note: Very small sigmas (< dE) will look noisy
#     factors = np.logspace(np.log10(0.5), np.log10(50.0), 30)
#     sigmas = factors * dE

#     errors = []
#     for i, s in enumerate(sigmas):
#         # Progress indicator
#         if i % 5 == 0: print(f"  Step {i}/{len(sigmas)}: sigma={s:.1e} eV")

#         val = I3_total_low_mem(hw, T, s)
#         errors.append(relative_error(np.array([val]), np.array([ref]))[0])

#     fig, ax = plt.subplots(figsize=(8.5, 5.0))
#     ax.plot(factors, errors, 'o-', markersize=4)

#     # Mark dE
#     ax.axvline(1.0, color='r', linestyle='--', label=r"$\sigma = \Delta E$")

#     # Annotate regions
#     ax.text(0.6, -1.0, "Undersampling", color='r', ha='right', rotation=90)
#     ax.text(5.0, np.min(errors), " Validity Region", color='g', ha='left', va='bottom')

#     ax.set_xscale("log")
#     ax.set_xlabel(r"Broadening Factor ($\sigma / \Delta E$)")
#     ax.set_ylabel(r"$\log_{10}|\delta_{rel}|$ (Total Integral)")
#     ax.legend(loc='best')

#     # Fix SyntaxWarning using raw string r"..."
#     title = rf"Stage 4 — Convergence of Total Integral vs $\sigma$ ($T={T}$ K)"
#     set_figure_title(fig, title)

#     if save_name is not None:
#         fname = "stage_4_sigma_convergence.png" if save_name == "auto" else save_name
#         save_svg(fig, fname)
#     plt.show()

# def plot_spectral_comparison(hw=1.5, T=300.0, sigma_factor=6.0, save_name="auto"):
#     """
#     Compares the shape of (3*) vs (4*) as a function of Energy.
#     """
#     dE = float(E_GRID[1] - E_GRID[0])
#     sigma = sigma_factor * dE
#     print(f"Running spectral check for sigma={sigma:.1e} eV...")

#     # Compute profiles
#     y_ref = I4_star_profile(E_GRID, hw, T)
#     y_approx = I3_star_profile_low_mem(E_GRID, hw, T, sigma)

#     # Compute relative error profile (avoiding div/0)
#     with np.errstate(divide='ignore', invalid='ignore'):
#         rel_err = np.abs(y_approx - y_ref) / np.abs(y_ref)
#         # Mask where value is negligible to clean up plot noise
#         rel_err[y_ref < 1e-5 * np.max(y_ref)] = np.nan

#     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 7.0), sharex=True, height_ratios=[3, 1])

#     # Top: Profiles
#     ax1.plot(E_GRID, y_ref, 'k-', lw=1.5, label=r"Exact (Eq. 4*)")
#     # Fix SyntaxWarning using raw string r"..." and double backslash
#     ax1.plot(E_GRID, y_approx, 'r--', lw=2.0, label=rf"Approx (Eq. 3*, $\sigma={sigma_factor}\Delta E$)")
#     ax1.set_ylabel("Transition Density [arb.]")
#     ax1.set_title(f"Spectral Profile Check ($T={T}$ K, $\hbar\omega={hw}$ eV)")
#     ax1.legend()
#     ax1.grid(True, alpha=0.3)

#     # Bottom: Relative Error
#     ax2.plot(E_GRID, rel_err * 100, 'k-', lw=1)
#     ax2.axhline(0, color='r', alpha=0.5)
#     ax2.set_ylabel("Error [%]")
#     ax2.set_xlabel(r"Initial Energy $\mathcal{E}$ [eV]")
#     ax2.set_ylim(-10, 10)
#     ax2.grid(True, alpha=0.3)

#     # Fermi Level Markers
#     for ax in [ax1, ax2]:
#         ax.axvline(E_F, color='k', linestyle=':', alpha=0.3)
#         ax.axvline(E_F - hw, color='k', linestyle=':', alpha=0.3)

#     if save_name is not None:
#         fname = "stage_4_spectral_profile.png" if save_name == "auto" else save_name
#         save_svg(fig, fname)
#     plt.show()

# def plot_heatmap(sigma_factor=6.0, *, save_name="auto"):
#     dE = float(E_GRID[1] - E_GRID[0])
#     sigma = sigma_factor * dE

#     # Downsample for speed (heatmap is expensive)
#     hw_vals = np.linspace(EMISSION_ENERGY_MIN, 4.0, 30)
#     T_vals = np.linspace(100, 2000, 30)

#     hw_grid, T_grid = np.meshgrid(hw_vals, T_vals, indexing='xy')

#     # Reference
#     I4_grid = I4_total(hw_grid, T_grid)

#     # Candidate (Loop)
#     I3_grid = np.zeros_like(I4_grid)
#     print(f"Computing heatmap ({I3_grid.size} points)...")

#     # This loop is still slow-ish, but memory safe
#     for i in range(T_vals.size):
#         for j in range(hw_vals.size):
#             I3_grid[i,j] = I3_total_low_mem(hw_vals[j], T_vals[i], sigma)

#     rel = relative_error(I3_grid, I4_grid)

#     fig, ax = plt.subplots(figsize=(8.5, 6.0))
#     m = ax.pcolormesh(hw_vals, T_vals, rel, shading='auto', cmap='coolwarm', vmin=-5, vmax=0)

#     ax.set_xlabel(r"$\hbar\omega$ [eV]")
#     ax.set_ylabel(r"$T$ [K]")
#     fig.colorbar(m, ax=ax, label=r"$\log_{10}|\delta_{rel}|$")

#     # Fix SyntaxWarning
#     title = rf"Stage 4 — Error Heatmap ($\sigma = {sigma_factor}\Delta E$)"
#     set_figure_title(fig, title)

#     if save_name is not None:
#         fname = f"stage_4_heatmap_sigma_{sigma_factor}.png" if save_name == "auto" else save_name
#         save_svg(fig, fname)
#     plt.show()

if __name__ == "__main__":
    apply_style()
    rel_err_plot(1e-5, 0.1)
    # plot_sigma_convergence(hw=1.5, T=300.0)
    # plot_spectral_comparison(hw=1.5, T=300.0, sigma_factor=6.0)
    # plot_heatmap(sigma_factor=6.0) # Uncomment to run full map
