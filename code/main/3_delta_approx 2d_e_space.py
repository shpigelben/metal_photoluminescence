import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson
from plot_style import apply_style, save_svg, set_figure_title
from _preamble_and_funcs import *

# --- Definitions ---
def gaussian_delta(x, sigma):
    return (1.0 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (x / sigma) ** 2)

def I4(E, hw, T):
    hw = np.asanyarray(hw)[..., None]
    T = np.asanyarray(T)[..., None]
    integrand = F_T(E + hw, E, T) * eDOS(E + hw) * eDOS(E)
    return simpson(integrand, E, axis=-1)


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



if __name__ == "__main__":
    apply_style()
    rel_err_plot(1e-5, 0.1)
    # plot_sigma_convergence(hw=1.5, T=300.0)
    # plot_spectral_comparison(hw=1.5, T=300.0, sigma_factor=6.0)
    # plot_heatmap(sigma_factor=6.0) # Uncomment to run full map
