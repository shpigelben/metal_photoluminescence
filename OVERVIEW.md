htig

# Project Overview — Metal Photoluminescence

## Research Objective

This MSc project computes the **photoluminescence (PL) spectrum of gold** from first principles, with the goal of quantifying the contribution of **interband transitions** (valence → conduction) under non-equilibrium conditions. Previous work established that intraband (conduction-band-only) transitions at thermal equilibrium are consistent with Kirchhoff's law. The question is: when gold is driven out of equilibrium by CW or pulsed illumination, how much do interband channels contribute to the total emission?

The approach is:

1. Use Fermi's Golden Rule for electronic transition rates.
2. Separate photonic (LDOS) and electronic contributions.
3. Model gold's band structure near the **X** (saddle) and **L** (ellipsoidal minimum) critical points using Rosei's parabolic approximation.
4. Reduce the 3D Brillouin-zone integrals to 1D energy-space integrals via a chain of coordinate transformations.
5. Validate by reproducing known absorption spectra (Rosei's $\varepsilon_2$), then extend to non-equilibrium emission.

---

## Current Status

### What Has Been Done

#### Theory & Derivations (docs/notes/)

| Deliverable                                                    | Status | Location                     |
| :------------------------------------------------------------- | :----: | :--------------------------- |
| General emission integral (FGR → 6D → factored form)         |   ✅   | A1, §2.1                    |
| Thermal factor identity ($f \cdot \bar{f}$ → Bose-Einstein) |   ✅   | A2, A3                       |
| Free-electron eDOS                                             |   ✅   | A4                           |
| Numeric delta-function approximation                           |   ✅   | A5                           |
| Boltzmann equation & non-equilibrium distribution              |   ✅   | A6                           |
| Intraband transitions (Rosei saddle band, eDOS derivation)     |   ✅   | A7                           |
| Interband transitions at X point (saddle topology)             |   ✅   | A8                           |
| Interband transitions at L point (ellipsoidal topology)        |   ✅   | A8.L                         |
| Kirchhoff's law consistency proof                              |   ✅   | A9                           |
| Effective mass extraction from C&S 1971                        |   ✅   | Effective Mass Extraction.md |
| Intraband emission: numeric convergence                        |   ✅   | §3.1                        |
| Intraband emission: analytic approximation accuracy            |   ✅   | §3.2                        |
| Intraband emission: constant eDOS error quantification         |   ✅   | §3.3                        |

#### Code (code/main/)

| Notebook                    | What it computes                                                                                             | Status |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------- | :----: |
| `1_YonatanAnalysis.ipynb` | Intraband emission: convergence, analytic approx, eDOS error                                                 |   ✅   |
| `2_RoseiAnalysis.ipynb`   | Interband$\varepsilon_2$: X + L integrals, temperature dependence, emission vs absorption, Kirchhoff check |   ✅   |

#### Key Results Established

- The constant-eDOS approximation introduces 10–30% error in intraband emission at optical frequencies — it is **not** a negligible approximation.
- Gold's equilibrium emission is **selective** (frequency-dependent emissivity), not blackbody. The microscopic calculation is consistent with Kirchhoff's law ($\text{emission}/\text{absorption} = e^{-\beta\hbar\omega}$) but does not produce Planckian emission.
- The X-point and L-point interband integrals have the same $\sqrt{\hbar\omega - \mathcal{E}_g}$ JDOS onset (both $M_0$), but different integrand structures: singularity at the upper limit (X) vs lower limit (L).

---

### What Remains

#### High Priority — Core Thesis Work

| Task                                                                                                                       | Chapter | Depends On                            |
| :------------------------------------------------------------------------------------------------------------------------- | :------: | :------------------------------------ |
| **Interband emission** (not just absorption): compute $\Gamma_e^{cv}(\hbar\omega)$ for X and L at equilibrium      |   §4   | A8, A8.L — done                      |
| **Non-equilibrium interband emission**: replace $f^T$ with $f^S$ (CW) and $f^P$ (pulsed)                       | §4, §5 | A6 distribution + interband integrals |
| **Intraband with Rosei bands**: compute intraband emission using the anisotropic conduction band (not free-electron) |  §3.5  | A7 — done                            |
| **Total emission spectrum**: combine intraband + interband, equilibrium + non-equilibrium, compare                   |   §5   | All above                             |
| **Comparison to experiment**: overlay computed $\varepsilon_2$ with Johnson & Christy (1972) data                  | §4, §5 | Interband$\varepsilon_2$ — done    |

#### Medium Priority — Thesis Writing

| Task                                               | Notes                                                           |
| :------------------------------------------------- | :-------------------------------------------------------------- |
| Expand**Introduction** (§1)                 | Currently ~30 lines; needs literature review, problem statement |
| Expand**Theoretical Framework** (§2)        | Currently ~30 lines; needs full narrative                       |
| Write**Interband Transitions** chapter (§4) | Empty — results exist in notebook, need prose                  |
| Write**Results & Discussion** (§5)          | Not started                                                     |
| Write**Conclusion** (§6)                    | Not started                                                     |

#### Open Questions for Advisor

- Constant eDOS approximation error (~10–30%): is this acceptable or should the full $\rho(\mathcal{E})$ always be kept?
- Bulk vs nanoparticle: first-order (Landau) vs second-order (phonon-mediated) TDM — which regime is the thesis targeting?
- Skin-depth issue: should we compute specific emission (per unit volume)?
- Should the non-vacuum photonic DOS be included when comparing to experiment?

---

## Project Structure

```
metal_photoluminescence/
├── AGENTS.md                    # Codex agent protocols
├── OVERVIEW.md                  # ← This file
├── README.md
├── code/
│   ├── requirements.txt
│   ├── main/                    # Production notebooks
│   │   ├── 1_YonatanAnalysis.ipynb    # Intraband emission analysis
│   │   └── 2_RoseiAnalysis.ipynb      # Interband absorption/emission (Rosei)
│   ├── misc/                    # Exploratory scripts & prototypes
│   └── retired/                 # Superseded scripts
├── docs/
│   ├── notes/                   # Obsidian vault — thesis chapters + appendices
│   │   ├── 0 - Outline.md      # Master thesis outline
│   │   ├── 1..4 - *.md         # Thesis chapters
│   │   ├── A1..A9 - *.md       # Appendices (derivations)
│   │   ├── A8.L - *.md         # L-point interband derivation
│   │   └── *.md                 # Working notes, references
│   └── references/              # Literature notes
└── figures/                     # Generated plots
```

## Key References

1. **Guerrisi, Rosei & Winsemius (1975)** — Phys. Rev. B 12, 557: Parabolic band model for gold, X/L parameters, $|P_X/P_L|^2 = 0.37$.
2. **Christensen & Seraphin (1971)** — Phys. Rev. B 4, 3321: Relativistic band structure, anisotropic effective masses at X and L.
3. **Johnson & Christy (1972)** — Phys. Rev. B 6, 4370: Experimental $\varepsilon(\omega)$ for gold.
4. **Sivan & Dubi** — Non-equilibrium electron distribution, steady-state PL theory.
