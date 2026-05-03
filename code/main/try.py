import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

# --- Physical Constants & Global Parameters ---
kB = 8.617e-5    # Boltzmann constant [eV/K]
T  = 600.0       # Effective temperature [K]
C  = 3.81        # hbar^2 / 2m_e [eV*Angstrom^2]

# --- X-Point Parameters (M1 Saddle Point) ---
Eg_X  = 1.94     # Nominal geometric gap
E0c_X = 0.0      # Empty minimum (at or above Fermi level)
mc_perp_X, mc_par_X = 0.31, 0.40
mv_perp_X, mv_par_X = 0.19, 0.15

Ac_X, Bc_X = C / mc_perp_X, C / mc_par_X
Av_X, Bv_X = C / mv_perp_X, C / mv_par_X
Abar_X = Ac_X + Av_X
Bbar_X = Bv_X - Bc_X  # Notice the subtraction for saddle point

# --- L-Point Parameters (M0 Minimum - SUBMERGED) ---
Eg_L  = 1.70     # Geometric gap (pushed down)
E0c_L = -0.75    # Submerged minimum (below Fermi level)
mc_perp_L, mc_par_L = 0.24, 0.12
mv_perp_L, mv_par_L = 0.70, 1.03

Ac_L, Bc_L = C / mc_perp_L, C / mc_par_L
Av_L, Bv_L = C / mv_perp_L, C / mv_par_L
Abar_L = Ac_L + Av_L
Bbar_L = Bc_L + Bv_L

# --- Core Physics Functions ---
def fermi(E, T):
    """Fermi-Dirac distribution. E=0 is the Fermi level."""
    if T == 0: return np.where(E < 0, 1.0, 0.0)
    return 1.0 / (1.0 + np.exp(np.clip(E / (kB * T), -500, 500)))

def calc_eps2_X(hw_array, N_pts=2000):
    """Integrates the X-point transitions."""
    eps2_X = np.zeros_like(hw_array)
    prefactor = 1.0 / np.sqrt(Abar_X * abs(Ac_X * Bv_X + Av_X * Bc_X))
    
    for i, hw in enumerate(hw_array):
        # Piecewise upper bound due to M1 topology
        if hw >= Eg_X:
            E_max = E0c_X + (Ac_X / Abar_X) * (hw - Eg_X)
        else:
            E_max = E0c_X + (Bc_X / Bbar_X) * (hw - Eg_X)
            
        E_min = E0c_X - 20.0 * kB * T  # Rosei's deep Fermi sea cutoff
        if E_max <= E_min: continue
        
        # Add epsilon offset to avoid 1/sqrt(0) singularity at E_max
        E = np.linspace(E_min, E_max - 1e-9, N_pts)
        
        # W_abs = f(initial) * [1 - f(final)]
        weights = fermi(E - hw, T) * (1.0 - fermi(E, T))
        integrand = weights / np.sqrt(E_max - E)
        
        eps2_X[i] = (prefactor / hw**2) * simpson(integrand, x=E)
        
    return eps2_X

def calc_eps2_L(hw_array, N_pts=2000):
    """Integrates the submerged L-point transitions."""
    eps2_L = np.zeros_like(hw_array)
    prefactor = 1.0 / np.sqrt(Abar_L * abs(Ac_L * Bv_L - Av_L * Bc_L))
    
    for i, hw in enumerate(hw_array):
        if hw <= Eg_L: continue # Absolute geometric block
        
        # Linear bounds for M0 minimum
        E_min = E0c_L + (Ac_L / Abar_L) * (hw - Eg_L)
        E_max = E0c_L + (Bc_L / Bbar_L) * (hw - Eg_L)
        if E_max <= E_min: continue
        
        # Add epsilon offset to avoid 1/sqrt(0) singularity at E_min
        E = np.linspace(E_min + 1e-9, E_max, N_pts)
        
        weights = fermi(E - hw, T) * (1.0 - fermi(E, T))
        integrand = weights / np.sqrt(E - E_min)
        
        eps2_L[i] = (prefactor / hw**2) * simpson(integrand, x=E)
        
    return eps2_L

# --- Execution & Plotting ---
if __name__ == "__main__":
    hw = np.linspace(1.0, 3.5, 300)
    
    # Calculate unbroadened integrals
    e2_X = calc_eps2_X(hw)
    e2_L = calc_eps2_L(hw)
    
    # Arbitrary scaling to match relative visual weights in Rosei's figures
    e2_X *= 50.0  
    e2_L *= 80.0  
    
    plt.figure(figsize=(9, 6))
    plt.plot(hw, e2_X, label='X-point ($M_1$ Saddle)', ls='--', color='blue')
    plt.plot(hw, e2_L, label='L-point (Submerged Minimum)', ls='-.', color='red')
    plt.plot(hw, e2_X + e2_L, label='Total Interband', color='black', lw=2)
    
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.xlabel(r'Photon Energy $\hbar\omega$ (eV)', fontsize=12)
    plt.ylabel(r'$\epsilon_2$ (Arbitrary Units)', fontsize=12)
    plt.title('Theoretical Absorption Onset (600K) via Simpson Integration', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(alpha=0.3)
    plt.xlim(1.0, 3.5)
    plt.ylim(0, max(np.max(e2_X + e2_L)*1.1, 0.1))
    
    plt.tight_layout()
    plt.show()