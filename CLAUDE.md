# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

```bash
source .venv/bin/activate
pip install -r code/requirements.txt
```

The `.venv` already exists in the repo root. Python 3.13, dependencies: numpy, scipy, matplotlib, PyQt6.

## Running Code

Notebooks in `code/main/` are the primary artifacts. Run them with Jupyter or marimo (both available in `.venv`):

```bash
jupyter notebook code/main/1_YonatanAnalysis.ipynb
jupyter notebook code/main/2_RoseiAnalysis.ipynb
```

Standalone scripts in `code/main/` (e.g., `rosei_fit_gui.py`, `data_cleaner_gui.py`) use PyQt6 and are run directly:

```bash
python code/main/rosei_fit_gui.py
```

## Architecture

This is a computational physics MSc project. The goal is computing the photoluminescence (PL) spectrum of gold from first principles, separating intraband and interband transition contributions under non-equilibrium conditions.

**Physics model** (see `OVERVIEW.md` for full status and `code/main/rosei_model_formulas.md` for formulas):
- Start from Fermi's Golden Rule for emission rates
- Factored into photonic (LDOS) × electronic (JDOS × occupation) parts
- Gold band structure modeled via Rosei's parabolic approximation at two critical points:
  - **X point** (saddle/$M_1$): gap $\mathcal{E}_g^X = 1.94$ eV, singularity at upper integration limit
  - **L point** (ellipsoid/$M_0$): gap $\mathcal{E}_g^L = 2.45$ eV, singularity at lower integration limit
- Non-equilibrium electron distributions $f^S$ (CW) and $f^P$ (pulsed) replace the equilibrium Fermi-Dirac

**Code layout:**
- `code/main/` — production notebooks and scripts; numbered = thesis chapters/sections
- `code/misc/` — exploratory scripts and prototypes (not authoritative)
- `code/retired/` — superseded code (ignore unless debugging regressions)
- `docs/notes/concepts/` — Obsidian vault with thesis chapter drafts (`A1`–`A9` = appendices, numbered `2–3` = thesis chapters)
- `docs/notes/log/` and `docs/notes/temp/` — working notes, not authoritative

**Key data files in `code/main/`:**
- `a_e2_X.txt`, `b_e2_L.txt`, `c_e2_X_L.txt`, `d_e2_X_L_Drude.txt` — tabulated $\varepsilon_2$ outputs at various stages of model assembly
- `rosei_presets.json` — saved parameter presets for the GUI fitters

## Canvas Workflow (`canvas reply`)

When asked to run `canvas reply`: read `docs/notes/Outline & Questions/DeepDive.canvas` as JSON, find the active (leaf) question node, trace ancestor context, synthesize a math-first answer, then write a new node + edge back to the canvas. Placement must be collision-free (check all bounding boxes). Never move existing nodes.

Response style for canvas answers: math-first (Golden Rule, Kubo–Greenwood, matrix elements), state assumptions explicitly, cite primary literature (Rosei 1975, Christensen & Seraphin 1971, Johnson & Christy 1972) before internal vault notes.
