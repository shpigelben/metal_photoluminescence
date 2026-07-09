# Derivations — Consolidated Absorption/Rosei Materials

This folder gathers **every absorption-derivation artifact** in the project into one place,
identifies its provenance, and distills the *correct* content into a single master document:

> **`master/rosei_grw.tex` (→ `rosei_grw.pdf`) — THE master document.** Self-contained
> rederivation from FGR in k-space, written **in Rosei's own symbols** so that GRW's
> Eqs. (1)–(10) are recreated one by one — with the printed defects of (4), (6) and (8)
> corrected and the corrected forms used. Includes the L point (which GRW delegate),
> the photonic density of states, and the emission spectrum, all closed by the exact
> van Roosbroeck–Shockley check.
>
> **`master/rosei_master.tex` (→ `rosei_master.pdf`)** — SI-units companion: the
> convention-general σ_c formulation, the X-branch fork side by side, the cross-repo
> conventions dictionary, and the full quantization details.

**New finding recorded in `rosei_grw.tex` (beyond the known (6)/(8) issues):** GRW's
printed Eq. (4), D = (8π²ħ²)⁻¹𝓕/k∥, is dimensionally inconsistent with their Eq. (9)
under any standard |P|² convention. The FGR-exact form is
**D = (16π²𝒟k∥)⁻¹ = 𝓕²/(4π²ħ⁴k∥)** (with |P|² = |⟨u|∇|l⟩|², spin carried in (9)'s 8π²,
N counted as half-neighborhoods 6/8). The discrepancy 2𝓕/ħ² is constant per critical
point and is absorbed into the fitted strength S = 𝓕|P|² — invisible to fits, but it
matters for the physical meaning of the extracted |P|².

## Manifest

### `sources/mine/` — Ben's derivation chain (the "my attempt" path)

| File | Role | Status |
|---|---|---|
| `A1 - Derivation of the General Emission Integral.md` | FGR + minimal coupling → 6D emission integral. The k-space starting point. | ✅ Sound (one intermediate line drops the ½ in (e/2m)(A·p+p·A); final result correct) |
| `A2 - Derivation of Analytic Approximation.md`, `A3 - Thermal Factor Energy Space.md` | Thermal-factor identity f·(1−f′) → Bose factor (Kirchhoff machinery) | ✅ |
| `A8 - Interband Transitions (Rosei).md` | Ben's u–v linearization method at X (emission form) | ✅ Method correct; its 𝓔_min denominator (B_v+B_c) applies only to the σ_c=+1 case — see master doc App. B |
| `A8.L - Interband Transitions at L (Rosei).md` | L-point counterpart (Claude-drafted, commit d382653) | ⚠️ Calls the L conduction band a saddle (−B_c) — contradicts C&S masses (m_c∥ = +0.12) and the verified X/L note. Superseded by master doc §L |
| `Absorption Integral (Using Rosei's Notations).md` | First translation of the absorption integral into Rosei notation | ✅ but unfinished (Jacobian section fragmentary) |
| `Interband Absorption at X and L (Rosei's Notation).md` | The polished X+L absorption note | ✅ **Most reliable single note**; documents GRW eqs (6)/(8) transcription issues |
| `Equivalence of My Absorption Integral and Rosei's.md` | Jacobian ↔ Rosei-D bridge, |det J| = 4k⊥k∥𝒟, 𝒟=(ħ²/2)²𝓕⁻² | ✅ Independently re-verified 2026-07-02 |
| `Effective Mass Extraction.md` | Signed effective masses from C&S 1971 Fig. 5 | ✅ Extraction documented; **X ∥-mass assignment (c: −0.40, v: −0.15) is opposite to what GRW's own model requires — see master doc §X-fork** |
| `rosei_model_formulas.md` | Formulas as implemented in the fit GUI | ⚠️ Chimera at X: uses the B̄_X>0 (closed-window) masses **and** GRW's open-CEDS narrative (−20k_BT floor, "M₁ saddle, sub-gap transitions exist"). L section fully consistent. |
| `X & L Dispersion Relations.md`, `Integration Limits of X & L Points vs the Center of BZ.md`, `First Order TDM.md` | Supporting notes | Copied for completeness (not re-audited in this pass) |

### `sources/recreations/` — attempts at recreating Rosei's derivation (AI-drafted)

| File | Provenance | Status |
|---|---|---|
| `interband_derivation.tex/.pdf` (v1) | Copilot (commit c20d45d) | ❌ Do not trust — see memory/repo audit |
| `interband_derivation_v2.tex/.pdf` | AI-drafted | ❌ Internally inconsistent: asserts B̄ = B_v−B_c > 0 *and* a geometric sub-gap tail (requires B̄<0); labels L as M₁ |
| `rosei_equivalence_derivation.tex/.pdf` | Latest LaTeX comparison (commit a95685f) | ◐ Best of the three; its eq-(8) diagnosis ("⊥ masses required") holds only on the B̄_X>0 branch — the master doc gives the branch-resolved correction |
| `4_interband_transitions.tex`, `appendix_a8_quadratic_interband_transitions.tex` | Thesis-skeleton drafts (docs/.LaTeX) | ◐ Skeletons; inherit A8/A8.L conventions |

### `sources/reference/`

| File | Notes |
|---|---|
| `7 - Rosei.pdf` / `7 - Rosei.tex` | Guerrisi, Rosei & Winsemius, PRB **12**, 557 (1975). The Mathpix TeX has OCR artifacts: eq (6) dimensionally garbled, eq (8) subscript-inconsistent with eqs (1)–(3). Corrected forms derived in master doc App. A. |

## Key reconciliation (full detail in the master document)

With the C&S-signed masses as extracted (X: m_c = (0.31, **−0.40**), m_v = (−0.19, −0.15); L: m_c = (0.24, +0.12), m_v = (−0.70, −1.03)):

- At **both** X and L the transition-energy surface Ω(k) = E_c−E_v has a **closed** constant-Ω
  window above 𝓔_g (√(ħω−𝓔_g) JDOS onset at both) — even though the X conduction *band* is
  a genuine saddle. The X/L difference lives in **where the 1/√ edge singularity sits**:
  sign(𝒟) puts it at the **upper** window edge at X (𝒟_X>0) and the **lower** edge at L (𝒟_L<0).
- GRW's *operational* model instead has B̄_X<0 (open CEDS, real sub-gap tail, −20k_BT floor,
  step-like onset at ≈1.83 eV). That requires the **opposite** X ∥-mass assignment
  (m_u∥ = 0.15 < m_l∥ = 0.40 — physically favored: flat d-bands are heavy). **Action item:
  re-inspect C&S Fig. 5 slopes along Δ.**
- The fitted ε₂ *shape* cannot distinguish the two assignments above the gap (the ∥ masses
  enter only via 𝓕_X, which is absorbed into the fitted strength S_X = 𝓕_X|P_X|²); the
  physics differs below the gap (geometric tail vs broadening-only tail).
