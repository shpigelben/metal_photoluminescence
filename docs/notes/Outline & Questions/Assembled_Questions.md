# Assembled Questions (for supervisor meeting)

**Goal:** walk out with clear, defensible modeling assumptions + the next concrete steps for the thesis.

## 1) Terminology + “what exactly are we calculating?”
- [ ] **[PL vs thermal radiation](<Non-equilibrium Emission in Metals.md>)**: should I call the equilibrium (Planck-like) emission from metals “photoluminescence”, or reserve “PL” for optically excited (non-equilibrium) emission? What phrasing do you prefer for the thesis/abstract?
- [ ] **[Photonic vs electronic factorization](<Introduction.md>)**: in which regimes is it legitimate to separate the spectrum into a “photonic” factor and an “electronic” factor (e.g., something like `I(ω) = I_ph(ω) · I_e(ω)`)? Is it actually multiplicative or should it be presented differently?
- [ ] **[Spontaneous vs stimulated](<../Chapters & Sections/A - Appendices/A1 - Derivation of the General Emission Integral.md>)**: in the FGR-based derivation, are we computing spontaneous emission, stimulated emission, or both? Where should the `(n_B(ω)+1)` factor enter so that the equilibrium limit is consistent?

## 2) Momentum conservation / selection rules (my biggest confusion)
- [ ] **[Intraband emission](<Progress Report + Questions for Yonatan.md>)**: my current intraband integral effectively allows any `k_i → k_f` transition as long as energy is conserved (no explicit momentum delta). What is the clean physical justification you’re comfortable with (phonons, impurities, surfaces/finite size, Umklapp)?
- [ ] **[Photon momentum “paradox”](<Electronic Transitions.md>)**: for a parabolic band, a photon has negligible momentum (`q≈0`)—so can an intraband transition conserve energy *and* crystal momentum without scattering assistance? If not, what is the most correct way to describe the process we’re modeling (and what quantity is conserved)?
- [ ] **[“Two-step” nature](<../Chapters & Sections/A - Appendices/A1 - Derivation of the General Emission Integral.md>)**: if intraband emission in a perfect crystal requires scattering assistance (phonons/defects), do we need to explicitly treat a phonon Hamiltonian / second-order perturbation, or is an effective momentum-relaxing matrix element the standard/acceptable approach here?
- [ ] **[Weighting by phonons](<../Chapters & Sections/A - Appendices/A2 - Derivation of Analytic Approximation.md>)**: even if phonons enable momentum relaxation, is it reasonable to treat all energy-conserving transitions as equally probable, or should the rate be weighted by phonon DOS/coupling? What is the minimal correction that matters for this project?
- [ ] **[Interband transitions](<Progress Report + Questions for Yonatan.md>)**: for `c ↔ v` transitions near X/L in Au, do we enforce crystal momentum conservation (direct transitions, `k_i = k_f + G`) or allow `k_i ≠ k_f` (indirect)? If indirect is allowed, what scattering mechanism should dominate and how would we incorporate it?
- [ ] **[BZ integration](<Progress Report + Questions for Yonatan.md>)**: when integrating over the full first BZ, does enforcing crystal-momentum conservation materially change the outcome (and dimensionality), or can it be absorbed into an effective matrix element?

## 3) Which processes dominate “metal optics”?
- [ ] **[Reflection/absorption intuition](<Photon Absorption by Conduction Electrons.md>)**: when connecting to the classical Drude picture (“conduction electrons oscillate and re-radiate”), which quantum process is the best match—**intraband** transitions, **interband** transitions, or something else (collective plasmons / screening)?
- [ ] **[Au in the visible](<Photon Absorption by Conduction Electrons.md>)**: roughly where (in photon energy) do interband transitions start to dominate Au’s optical response, and how should I describe that boundary in the thesis?

## 4) Approximations I need you to bless (or kill)
- [ ] **[Constant dipole matrix element](<Non-equilibrium Emission in Metals.md>)**: under what conditions is it reasonable to treat the TDM as constant for intraband? For interband near X/L, can we also approximate it as constant, or is the `k`/polarization dependence essential?
- [ ] **[Constant eDOS + analytic expressions](<0 - Work Plan.md>)**: my notes suggest the constant-eDOS approximation can be poor away from a narrow window around `E_F`. For the thesis, should I treat the analytic forms mainly as benchmarks, and rely on energy-dependent DOS numerics as the “real” result?
- [ ] **[Missing steady-state analytic form](<Comparisons New.md>)**: I still have a gap: what is the correct analytic approximation for the steady-state/non-equilibrium case (the `I^S_analytic approx` placeholder in my notes)?

## 5) k-space modeling near X/L: integration limits and “valley” approximations
- [ ] **[Cutoffs](<Integration Limits of X & L Points vs the Center of BZ.md>)**: for Rosei-like parabolic/quadratic expansions around X/L, how should I choose the k-space cutoff so I stay within the validity region but still capture the dominant contribution?
- [ ] **[Geometry of the BZ](<Integration Limits of X & L Points vs the Center of BZ.md>)**: is it acceptable to replace the true BZ boundary (truncated octahedron) by a simplified region (sphere/cylinder/infinite limits) after shifting coordinates to an X/L-centered frame? What is the best justification and when does it break?
- [ ] **[Fair comparisons](<0 - Work Plan.md>)**: if I compare a parabolic model vs a saddle/non-parabolic model, how do I ensure I’m integrating over the *same* physical region of k-space?

## 6) Delta function / linewidth: physics vs numerics
- [ ] **[Gaussian vs Lorentzian](<../Chapters & Sections/3 - Intraband Transitions/3.4 - Delta Approximation.md>)**: when approximating energy conservation `δ(ΔE ± ħω)`, should I use a Gaussian purely for numerics, or a Lorentzian with a physical linewidth (finite lifetime)? What should set the linewidth (electron scattering rate / Drude damping / something else)?
- [ ] **[Choosing σ and grid](<../Chapters & Sections/A - Appendices/A5 - Numeric Delta Approximation.md>)**: is there a standard rule-of-thumb for selecting the δ-approximation width vs the integration step so that total error (approximation + quadrature) is controlled?

## 7) Non-equilibrium distribution under pumping (extending to interband)
- [ ] **[Correct form of `f^S`](<Non-equilibrium Emission in Metals.md>)**: I encountered a published steady-state distribution that can produce `f>1` (unphysical). What is the correct expression we should use, and how should I justify it in writing?
- [ ] **[Band distinction](<Non-equilibrium Emission in Metals.md>)**: for interband emission under pumping, should the non-equilibrium distribution explicitly distinguish conduction vs valence (separate distributions / quasi-Fermi levels), or is a single corrected `f(E)` acceptable?
- [ ] **[What goes into `ε''`](<Non-equilibrium Emission in Metals.md>)**: in the non-equilibrium correction `δE`, should `ε''(ω_L)` come from Drude only, or include Lorentz/interband contributions when the pump is in the visible? How do we implement this consistently?
- [ ] **[Strong pump / pulsed](<../Chapters & Sections/A - Appendices/A1 - Derivation of the General Emission Integral.md>)**: at what point do we need to worry about nonlinear response or time dependence (pulsed illumination), versus a simple steady-state Boltzmann picture?

## 8) Thesis-facing: references + “canonical” derivations
- [ ] **[Key citations needed](<../Chapters & Sections/1 - Introduction/Abstract.md>)**: what are the best references for (a) intraband equilibrium emission giving Planck-like behavior, (b) interband emission being negligible in thermal equilibrium for Au, and (c) the standard hot-PL non-equilibrium distribution under CW/pulsed excitation?
- [ ] **[Which derivation to follow](<Progress Report + Questions for Yonatan.md>)**: between Novotny-style quantized-field derivations and metal/Bloch-electron treatments (e.g., Farhan-style), which route do you recommend as the most defensible backbone for my thesis?
- [ ] **[Gauge choice](<../Chapters & Sections/A - Appendices/A1 - Derivation of the General Emission Integral.md>)**: in the derivation of light–matter interaction, is it safe to assume Coulomb gauge throughout, and what do I need to state to make that assumption legitimate?
