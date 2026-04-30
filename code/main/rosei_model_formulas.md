# Rosei Interband Model — Formulas

Reference: Guerrisi, Rosei & Winsemius, *Phys. Rev. B* **12**, 557 (1975).

## Full model

$$
\varepsilon_2(\omega) = \mathrm{Scale} \times \frac{1}{\omega^2}\Big[|P_X|^2\, N_X\, \widetilde{J}_X(\omega) + |P_L|^2\, N_L\, \widetilde{J}_L(\omega)\Big] + \frac{A_D}{\omega^3}
$$

| Symbol | Description | Default |
|--------|-------------|---------|
| Scale | Overall interband amplitude | auto-fitted |
| $N_X = 6$ | Multiplicity of X-point | fixed |
| $N_L = 8$ | Multiplicity of L-point | fixed |
| $\|P_X/P_L\|^2$ | Squared matrix-element ratio | 0.370 |
| $A_D$ | Drude amplitude ($\omega_p^2 \gamma_D$ in eV³) | 6.0 |

## Broadened JDOS

Each critical-point JDOS is broadened independently with a Lorentzian kernel:

$$
\widetilde{J}_P(\omega) = \int J_P(\omega')\,\frac{\Gamma_P / \pi}{(\omega - \omega')^2 + \Gamma_P^2}\,d\omega'
$$

Default broadening: $\Gamma_X = \Gamma_L = 0.07$ eV.

## X-point (saddle, $M_1$ critical point)

Dispersion near X:

$$
E_c^X(\mathbf{k}) = E_{0c} + A_c^X\, u - B_c^X\, v, \qquad
E_v^X(\mathbf{k}) = E_{0v} - A_v^X\, u - B_v^X\, v
$$

where $u = k_\perp^2$, $v = k_\parallel^2$ (saddle point: minus sign in conduction band).

**Derived quantities:**

$$
\bar{A}_X = A_c^X + A_v^X, \qquad
\bar{B}_X = B_v^X - B_c^X, \qquad
D_X = A_c^X B_v^X + A_v^X B_c^X
$$

**Integration limits** (valid for all $\hbar\omega$):

$$
\mathcal{E}_{\max}^X(\omega) = \frac{A_c^X}{\bar{A}_X}(\hbar\omega - \mathcal{E}_g^X)
$$

Because X is an $M_1$ saddle point, sub-gap transitions ($\hbar\omega < \mathcal{E}_g^X$) exist — the CEDS is open. Following Rosei (1975), the lower limit is replaced by a fixed thermal cutoff:

$$
\mathcal{E}_{\min}^X = -20\,k_BT
$$

The Fermi factor $[1-f(\mathcal{E})]$ naturally suppresses deeply occupied final states, making the integral convergent.

**Joint density of states:**

$$
J_X(\omega, T) = \frac{1}{\sqrt{\bar{A}_X\,|D_X|}}
\int_{\mathcal{E}_{\min}^X}^{\mathcal{E}_{\max}^X}
\frac{[1 - f(\mathcal{E}, T)]}{\sqrt{\mathcal{E}_{\max}^X - \mathcal{E}}}
\,d\mathcal{E}
$$

**Default effective masses** (Christensen & Seraphin 1971):

| Parameter | Value |
|-----------|-------|
| $\mathcal{E}_g^X$ | 1.94 eV |
| $m_{c\perp}^X$ | 0.31 $m_e$ |
| $m_{c\parallel}^X$ | 0.40 $m_e$ |
| $m_{v\perp}^X$ | 0.19 $m_e$ |
| $m_{v\parallel}^X$ | 0.15 $m_e$ |

Band parameters from effective masses: $A_c^X = C / m_{c\perp}^X$, $B_c^X = C / m_{c\parallel}^X$, etc., with $C = \hbar^2/(2m_e) = 3.81$ eV·Å².

## L-point (ellipsoid, $M_0$ critical point)

Dispersion near L:

$$
E_c^L(\mathbf{k}) = E_{0c} + A_c^L\, u + B_c^L\, v, \qquad
E_v^L(\mathbf{k}) = E_{0v} - A_v^L\, u - B_v^L\, v
$$

(no saddle — both terms have the same sign).

**Derived quantities:**

$$
\bar{A}_L = A_c^L + A_v^L, \qquad
\bar{B}_L = B_c^L + B_v^L, \qquad
D_L = A_c^L B_v^L - B_c^L A_v^L
$$

**Integration limits** ($\hbar\omega > \mathcal{E}_g^L$):

$$
\mathcal{E}_{\min}^L(\omega) = \frac{A_c^L}{\bar{A}_L}(\hbar\omega - \mathcal{E}_g^L), \qquad
\mathcal{E}_{\max}^L(\omega) = \frac{B_c^L}{\bar{B}_L}(\hbar\omega - \mathcal{E}_g^L)
$$

**Joint density of states:**

$$
J_L(\omega, T) = \frac{1}{\sqrt{\bar{A}_L\,|D_L|}}
\int_{\mathcal{E}_{\min}^L}^{\mathcal{E}_{\max}^L}
\frac{[1 - f(\mathcal{E}, T)]}{\sqrt{\mathcal{E} - \mathcal{E}_{\min}^L}}
\,d\mathcal{E}
$$

**Default effective masses:**

| Parameter | Value |
|-----------|-------|
| $\mathcal{E}_g^L$ | 2.45 eV |
| $m_{c\perp}^L$ | 0.24 $m_e$ |
| $m_{c\parallel}^L$ | 0.12 $m_e$ |
| $m_{v\perp}^L$ | 0.70 $m_e$ |
| $m_{v\parallel}^L$ | 1.03 $m_e$ |

## Drude (intraband)

High-frequency limit of the Drude dielectric function:

$$
\varepsilon_2^{\mathrm{Drude}}(\omega) = \frac{\omega_p^2\,\gamma_D}{\omega(\omega^2 + \gamma_D^2)}
\;\xrightarrow{\omega \gg \gamma_D}\;
\frac{A_D}{\omega^3}
$$

The single parameter $A_D \equiv \omega_p^2 \gamma_D$ absorbs both the plasma frequency and the scattering rate. Not multiplied by the interband Scale factor.

## Thermal factor

$$
f(\mathcal{E}, T) = \frac{1}{1 + e^{\mathcal{E}/k_BT}}
$$

The factor $[1 - f(\mathcal{E}, T)]$ weights empty final states. Default $T_{\mathrm{eff}} = 600$ K.
