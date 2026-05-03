import numpy as np
from scipy.integrate import simpson
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import os

# =============================================================================
# 1. Physical Constants
# =============================================================================
kB = 8.617e-5    # Boltzmann constant [eV/K]
T  = 600.0       # Effective temperature [K]
C  = 3.81        # hbar^2 / 2m_e [eV*Angstrom^2]

def fermi(E, T):
    """Fermi-Dirac distribution. E=0 is the Fermi level."""
    return 1.0 / (1.0 + np.exp(np.clip(E / (kB * T), -500, 500)))

# =============================================================================
# 2. Integration Models
# =============================================================================
def calc_eps2_X(hw_array, Eg_X, mc_perp, mc_par, mv_perp, mv_par, scale, N_pts=300):
    """Computes X-point (M1 Saddle) transitions for an array of energies."""
    eps2 = np.zeros_like(hw_array)
    E0c_X = 0.0 # Conduction band saddle at Fermi level
    
    Ac, Bc = C / mc_perp, C / mc_par
    Av, Bv = C / mv_perp, C / mv_par
    Abar = Ac + Av
    Bbar = Bv - Bc
    D_X  = Ac * Bv + Av * Bc
    
    prefactor = scale / np.sqrt(Abar * (abs(D_X) + 1e-12))
    
    for i, hw in enumerate(hw_array):
        # Piecewise upper bound due to M1 geometry
        if hw >= Eg_X: E_max = E0c_X + (Ac / Abar) * (hw - Eg_X)
        else:          E_max = E0c_X + (Bc / Bbar) * (hw - Eg_X)
            
        E_min = E0c_X - 20.0 * kB * T  # Deep Fermi sea cutoff
        if E_max <= E_min: continue
        
        # Grid with epsilon offset to prevent 1/sqrt(0)
        E = np.linspace(E_min, E_max - 1e-9, N_pts)
        weights = fermi(E - hw, T) * (1.0 - fermi(E, T))
        integrand = weights / np.sqrt(E_max - E)
        
        eps2[i] = (prefactor / hw**2) * simpson(integrand, x=E)
    return eps2

def calc_eps2_L(hw_array, Eg_L, E0c_L, mc_perp, mc_par, mv_perp, mv_par, scale, N_pts=300):
    """Computes L-point (Submerged M0 Minimum) transitions."""
    eps2 = np.zeros_like(hw_array)
    
    Ac, Bc = C / mc_perp, C / mc_par
    Av, Bv = C / mv_perp, C / mv_par
    Abar = Ac + Av
    Bbar = Bc + Bv
    D_L  = Ac * Bv - Av * Bc
    
    prefactor = scale / np.sqrt(Abar * (abs(D_L) + 1e-12))
    
    for i, hw in enumerate(hw_array):
        if hw <= Eg_L: continue # Absolute geometric cutoff
        
        E_min = E0c_L + (Ac / Abar) * (hw - Eg_L)
        E_max = E0c_L + (Bc / Bbar) * (hw - Eg_L)
        if E_max <= E_min: continue
        
        E = np.linspace(E_min + 1e-9, E_max, N_pts)
        weights = fermi(E - hw, T) * (1.0 - fermi(E, T))
        integrand = weights / np.sqrt(E - E_min)
        
        eps2[i] = (prefactor / hw**2) * simpson(integrand, x=E)
    return eps2

# =============================================================================
# 3. Optimization Setup
# =============================================================================
def load_data(filename):
    # Get the absolute path of the directory where this script lives
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the text file
    filepath = os.path.join(script_dir, filename)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Could not find {filepath}")
    
    data = np.loadtxt(filepath, delimiter=",", skiprows=1)
    return data[:, 0], data[:, 1]

def optimize_X(hw_data, e2_data):
    print("\n--- Optimizing X-Point ---")
    # Params: [Eg_X, mc_perp, mc_par, mv_perp, mv_par, scale]
    p0 = [1.94, 0.31, 0.40, 0.19, 0.15, 100.0] 
    bounds = [(1.7, 2.2), (0.1, 1.5), (0.1, 1.5), (0.05, 1.0), (0.05, 1.0), (1.0, 5000.0)]
    
    def cost(p):
        model_e2 = calc_eps2_X(hw_data, *p)
        ssr = np.sum((e2_data - model_e2)**2)
        return ssr

    res = minimize(cost, p0, method='L-BFGS-B', bounds=bounds, options={'disp': False})
    print(f"Success: {res.success}, SSR: {res.fun:.4f}")
    print(f"Fitted Eg_X: {res.x[0]:.3f} eV | Scale: {res.x[5]:.1f}")
    print(f"Masses - mc_perp: {res.x[1]:.3f}, mc_par: {res.x[2]:.3f}, mv_perp: {res.x[3]:.3f}, mv_par: {res.x[4]:.3f}")
    return res.x

def optimize_L(hw_data, e2_data):
    print("\n--- Optimizing L-Point ---")
    # Params: [Eg_L, E0c_L, mc_perp, mc_par, mv_perp, mv_par, scale]
    p0 = [1.70, -0.75, 0.24, 0.12, 0.70, 1.03, 100.0]
    bounds = [(1.0, 2.5), (-2.0, 0.0), (0.05, 1.5), (0.05, 1.5), (0.3, 2.5), (0.5, 3.0), (1.0, 5000.0)]
    
    def cost(p):
        model_e2 = calc_eps2_L(hw_data, *p)
        ssr = np.sum((e2_data - model_e2)**2)
        return ssr

    res = minimize(cost, p0, method='L-BFGS-B', bounds=bounds, options={'disp': False})
    print(f"Success: {res.success}, SSR: {res.fun:.4f}")
    print(f"Fitted Eg_L: {res.x[0]:.3f} eV | E0c_L: {res.x[1]:.3f} eV | Scale: {res.x[6]:.1f}")
    print(f"Masses - mc_perp: {res.x[2]:.3f}, mc_par: {res.x[3]:.3f}, mv_perp: {res.x[4]:.3f}, mv_par: {res.x[5]:.3f}")
    return res.x

# =============================================================================
# 4. Execution & Plotting
# =============================================================================
if __name__ == "__main__":
    try:
        hw_X, e2_X_data = load_data("a_e2_X.txt")
        hw_L, e2_L_data = load_data("b_e2_L.txt")
    except FileNotFoundError as e:
        print(e)
        print("Please ensure 'a_e2_X.txt' and 'b_e2_L.txt' are in the same directory.")
        exit()

    # Run Regressions
    opt_p_X = optimize_X(hw_X, e2_X_data)
    opt_p_L = optimize_L(hw_L, e2_L_data)
    
    # Generate smooth curves for plotting based on optimized parameters
    hw_smooth = np.linspace(1.5, 3.5, 200)
    e2_X_fit = calc_eps2_X(hw_smooth, *opt_p_X)
    e2_L_fit = calc_eps2_L(hw_smooth, *opt_p_L)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.plot(hw_X, e2_X_data, 'ko', alpha=0.5, label='Digitized Data (X)')
    ax1.plot(hw_smooth, e2_X_fit, 'b-', lw=2, label='Fitted Model (X)')
    ax1.set_title(f"X-Point Fit ($E_g$ = {opt_p_X[0]:.2f} eV)")
    ax1.set_xlabel(r"Photon Energy $\hbar\omega$ (eV)")
    ax1.set_ylabel(r"$\epsilon_2$")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(hw_L, e2_L_data, 'ko', alpha=0.5, label='Digitized Data (L)')
    ax2.plot(hw_smooth, e2_L_fit, 'r-', lw=2, label='Fitted Model (L)')
    ax2.set_title(f"L-Point Fit ($E_g$ = {opt_p_L[0]:.2f} eV, $E_{{0c}}$ = {opt_p_L[1]:.2f} eV)")
    ax2.set_xlabel(r"Photon Energy $\hbar\omega$ (eV)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
