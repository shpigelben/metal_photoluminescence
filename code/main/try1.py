"""
Rosei Interband ε₂ — Standalone Simpson Integration
====================================================
Faithful recreation of the Rosei (1975) interband model for gold,
with correct integration limits, submerged L-point (E0c_L), and
both absorption/emission Fermi factor modes.

Reference: Guerrisi, Rosei & Winsemius, Phys. Rev. B 12, 557 (1975).
"""

import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

# =============================================================================
# 1. Physical Constants
# =============================================================================
kB   = 8.617e-5   # Boltzmann constant [eV/K]
C    = 3.81       # ℏ²/(2mₑ) [eV·Å²]
N_X  = 6          # X-point multiplicity
N_L  = 8          # L-point multiplicity

# =============================================================================
# 2. Numerically Stable Fermi Weights
# =============================================================================
# Using logaddexp to avoid overflow/underflow at extreme T or E.
#
# Absorption:  W_abs = f(E - ħω) · [1 - f(E)]
#   = occupation of valence state × emptiness of conduction state
#
# Emission:    W_ems = f(E) · [1 - f(E - ħω)]
#   = occupation of conduction state × emptiness of valence state
#
# Rosei's simplified form [1 - f(E)] is the limit of W_abs when
# f(E - ħω) → 1 (valence states deep below E_F are fully occupied).

def W_absorption(E, hw, T):
    """f(E - ħω) · [1 - f(E)], numerically stable."""
    if T == 0:
        return np.where(E - hw < 0, 1.0, 0.0) * np.where(E > 0, 1.0, 0.0)
    beta = 1.0 / (kB * T)
    a = beta * E           # argument for conduction state
    b = beta * (E - hw)    # argument for valence state
    # f(b) · [1 - f(a)] = exp(-logaddexp(0,-b) - logaddexp(0,a))
    #                    = exp(-b - logaddexp(0,-b) + b - logaddexp(0,a))
    # Simpler: log[f(b)] = -logaddexp(0,b); log[1-f(a)] = -logaddexp(0,-a) = a - logaddexp(0,a)
    # But the most robust form:
    return np.exp(-np.logaddexp(0, b) - np.logaddexp(0, -a))

def W_emission(E, hw, T):
    """f(E) · [1 - f(E - ħω)], numerically stable."""
    if T == 0:
        return np.where(E < 0, 1.0, 0.0) * np.where(E - hw > 0, 1.0, 0.0)
    beta = 1.0 / (kB * T)
    a = beta * E
    b = beta * (E - hw)
    return np.exp(-np.logaddexp(0, a) - np.logaddexp(0, -b))

# =============================================================================
# 3. Parametrised Integration Functions
# =============================================================================

def calc_eps2_X(hw_array, Eg, E0c, mc_perp, mc_par, mv_perp, mv_par,
                T, mode="absorption", N_pts=2000):
    """X-point (M1 saddle) interband JDOS via Simpson integration.
    
    Integration limits (Rosei 1975):
        E_max = E0c + (Ac / Abar) · (ħω − Eg)     [single expression, all ħω]
        E_min = −20 kB T                             [thermal cutoff]
    
    The saddle-point geometry keeps the CEDS open below the gap;
    the Fermi factor naturally kills the integrand deep in the Fermi sea.
    """
    Ac, Bc = C / mc_perp, C / mc_par
    Av, Bv = C / mv_perp, C / mv_par
    Abar = Ac + Av
    D_X  = Ac * Bv + Av * Bc
    prefactor = 1.0 / np.sqrt(Abar * abs(D_X))
    
    W = W_absorption if mode == "absorption" else W_emission
    eps2 = np.zeros_like(hw_array)
    
    for i, hw in enumerate(hw_array):
        # Single expression for E_max (Rosei 1975, no piecewise switch)
        E_max = E0c + (Ac / Abar) * (hw - Eg)
        E_min = E0c - 20.0 * kB * T if T > 0 else E0c - 0.1
        if E_max <= E_min:
            continue
        
        E = np.linspace(E_min, E_max - 1e-9, N_pts)
        integrand = W(E, hw, T) / np.sqrt(E_max - E)
        eps2[i] = (prefactor / hw**2) * simpson(integrand, x=E)
    
    return eps2

def calc_eps2_L(hw_array, Eg, E0c, mc_perp, mc_par, mv_perp, mv_par,
                T, mode="absorption", N_pts=2000):
    """L-point (M0 minimum) interband JDOS via Simpson integration.
    
    Integration limits:
        E_min = E0c + (Ac / Abar) · (ħω − Eg)
        E_max = E0c + (Bc / Bbar) · (ħω − Eg)
    
    Hard cutoff: no transitions for ħω ≤ Eg.
    E0c shifts both limits when the L-point minimum is submerged below E_F.
    """
    Ac, Bc = C / mc_perp, C / mc_par
    Av, Bv = C / mv_perp, C / mv_par
    Abar = Ac + Av
    Bbar = Bc + Bv
    D_L  = Ac * Bv - Av * Bc
    prefactor = 1.0 / np.sqrt(Abar * abs(D_L))
    
    W = W_absorption if mode == "absorption" else W_emission
    eps2 = np.zeros_like(hw_array)
    
    for i, hw in enumerate(hw_array):
        if hw <= Eg:
            continue
        
        E_min = E0c + (Ac / Abar) * (hw - Eg)
        E_max = E0c + (Bc / Bbar) * (hw - Eg)
        if E_max <= E_min:
            continue
        
        E = np.linspace(E_min + 1e-9, E_max, N_pts)
        integrand = W(E, hw, T) / np.sqrt(E - E_min)
        eps2[i] = (prefactor / hw**2) * simpson(integrand, x=E)
    
    return eps2

# =============================================================================
# 4. Default Band Parameters (Christensen & Seraphin 1971 / Rosei 1975)
# =============================================================================
PARAMS_X = dict(Eg=1.94, E0c=0.0,
                mc_perp=0.31, mc_par=0.40, mv_perp=0.19, mv_par=0.15)
PARAMS_L = dict(Eg=1.70, E0c=-0.75,
                mc_perp=0.24, mc_par=0.12, mv_perp=0.70, mv_par=1.03)
T_DEFAULT    = 600.0
P_RATIO_SQ   = 0.370   # |Px/PL|²

# =============================================================================
# 5. Execution & Plotting
# =============================================================================
if __name__ == "__main__":
    hw = np.linspace(1.0, 3.5, 300)
    T  = T_DEFAULT
    mode = "absorption"
    
    # Raw JDOS (unbroadened, without overall Scale)
    jdos_X = calc_eps2_X(hw, **PARAMS_X, T=T, mode=mode)
    jdos_L = calc_eps2_L(hw, **PARAMS_L, T=T, mode=mode)
    
    # Full model: ε₂(ω) = Scale/ω² [|Px|² N_X J_X + |PL|² N_L J_L]
    # Here we absorb |PL|² into Scale, so the ratio appears only on X.
    e2_X = N_X * P_RATIO_SQ * jdos_X
    e2_L = N_L * jdos_L
    e2_total = e2_X + e2_L
    
    # Arbitrary overall scale for visual comparison
    scale = 100.0
    e2_X     *= scale
    e2_L     *= scale
    e2_total *= scale
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    
    axes[0].plot(hw, e2_X, color='blue', lw=2)
    axes[0].set_title('X-point ($M_1$ Saddle)')
    axes[0].set_ylabel(r'$\varepsilon_2$ (arb. units)')
    
    axes[1].plot(hw, e2_L, color='red', lw=2)
    axes[1].set_title('L-point (Submerged $M_0$)')
    
    axes[2].plot(hw, e2_X, '--', color='blue', alpha=0.5, label='X')
    axes[2].plot(hw, e2_L, '--', color='red',  alpha=0.5, label='L')
    axes[2].plot(hw, e2_total, color='black', lw=2, label='X + L')
    axes[2].set_title('Total Interband')
    axes[2].legend()
    
    for ax in axes:
        ax.set_xlabel(r'$\hbar\omega$ (eV)')
        ax.set_xlim(1.0, 3.5)
        ax.grid(alpha=0.3)
        ax.axhline(0, color='gray', lw=0.5)
    
    fig.suptitle(f'Rosei Interband Model — T = {T:.0f} K, mode = {mode}',
                 fontsize=14, y=1.02)
    fig.tight_layout()
    plt.show()