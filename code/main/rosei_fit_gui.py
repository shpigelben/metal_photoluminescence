"""
Rosei ε₂ Interactive Fitting Tool — PyQt6 Application
======================================================
Four-panel comparison of the Rosei interband model against digitised data
from Figure 8 of Guerrisi, Rosei & Winsemius (1975).

Subplots:
  (1) X-point only       (2) L-point only
  (3) X + L combined     (4) X + L + Drude intraband

Run:  python rosei_fit_gui.py
"""

from __future__ import annotations

import os
import sys
import json
import numpy as np
from dataclasses import dataclass
from scipy.integrate import quad
from scipy.signal import fftconvolve
from scipy.optimize import minimize

from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QFormLayout, QDoubleSpinBox, QSlider,
    QPushButton, QLabel, QSizePolicy, QStatusBar, QDialog,
    QInputDialog, QComboBox,
)
import threading

import matplotlib
matplotlib.use("QtAgg")
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# ═══════════════════════════════════════════════════════════════════════════
#  Physical constants & band-parameter dataclasses
# ═══════════════════════════════════════════════════════════════════════════

kB = 8.617e-5   # eV / K
C  = 3.81       # ℏ² / (2 mₑ)  [eV·Å²]
N_X, N_L = 6, 8


def fermi(E: float, T: float) -> float:
    if T == 0:
        return 1.0 if E < 0 else (0.5 if E == 0 else 0.0)
    return 1.0 / (1.0 + np.exp(np.clip(E / (kB * T), -500, 500)))


@dataclass
class XPointParams:
    Ac: float; Bc: float; Av: float; Bv: float
    Eg: float; E0c: float = 0.0

    def __post_init__(self):
        self.Abar = self.Ac + self.Av
        self.Bbar = self.Bv - self.Bc
        self.D    = self.Ac * self.Bv + self.Av * self.Bc

    def E_max(self, hw): return self.E0c + (self.Ac / self.Abar) * (hw - self.Eg)
    def E_min(self, hw): return self.E0c - (self.Bc / self.Bbar) * (hw - self.Eg)
    def prefactor(self):  return 1.0 / np.sqrt(self.Abar * abs(self.D))


@dataclass
class LPointParams:
    Ac: float; Bc: float; Av: float; Bv: float
    Eg: float; E0c: float = 0.0

    def __post_init__(self):
        self.Abar = self.Ac + self.Av
        self.Bbar = self.Bc + self.Bv
        self.D    = self.Ac * self.Bv - self.Bc * self.Av

    def E_min(self, hw): return self.E0c + (self.Ac / self.Abar) * (hw - self.Eg)
    def E_max(self, hw): return self.E0c + (self.Bc / self.Bbar) * (hw - self.Eg)
    def prefactor(self):  return 1.0 / np.sqrt(self.Abar * abs(self.D))


# ═══════════════════════════════════════════════════════════════════════════
#  Core physics functions
# ═══════════════════════════════════════════════════════════════════════════

def _F_rosei(E, hw, T):
    return 1.0 - fermi(E, T)


def _interband_integral(hw, T, p, is_L=False):
    if hw <= p.Eg:
        return 0.0
    e_min, e_max = p.E_min(hw), p.E_max(hw)
    if e_max <= e_min:
        return 0.0
    t_max = np.sqrt(e_max - e_min)
    if is_L:
        integrand = lambda t: 2.0 * _F_rosei(e_min + t**2, hw, T)
    else:
        integrand = lambda t: 2.0 * _F_rosei(e_max - t**2, hw, T)
    result, _ = quad(integrand, 0, t_max)
    return p.prefactor() * result


def _broaden(y, x, gamma):
    if gamma < 1e-4:
        return y.copy()
    dx = x[1] - x[0]
    x_k = x - x[len(x) // 2]
    kernel = (gamma / np.pi) / (x_k**2 + gamma**2) * dx
    return fftconvolve(y, kernel, mode="same")


def _r_squared(d_hw, d_e2, m_hw, m_e2):
    mi = np.interp(d_hw, m_hw, m_e2)
    ss_res = np.sum((d_e2 - mi) ** 2)
    ss_tot = np.sum((d_e2 - np.mean(d_e2)) ** 2)
    return 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else 0.0


# ── Extended energy grid (broadening padding) ───────────────────────────

HW_EXT = np.linspace(0.5, 4.0, 400)
HW_LO, HW_HI = 1.0, 3.2
DISP_MASK = (HW_EXT >= HW_LO) & (HW_EXT <= HW_HI)
HW_DISP = HW_EXT[DISP_MASK]


def compute_interband(params: dict):
    """Return (total, X, L) on HW_DISP after broadening.
    X and L are broadened independently with Gamma_X and Gamma_L."""
    xp = XPointParams(Ac=C / params["mc_perp_X"], Bc=C / params["mc_par_X"],
                      Av=C / params["mv_perp_X"], Bv=C / params["mv_par_X"],
                      Eg=params["Eg_X"])
    lp = LPointParams(Ac=C / params["mc_perp_L"], Bc=C / params["mc_par_L"],
                      Av=C / params["mv_perp_L"], Bv=C / params["mv_par_L"],
                      Eg=params["Eg_L"])
    T = params["T_val"]
    P2 = params["P_ratio_sq"]
    raw_x = np.empty(len(HW_EXT))
    raw_l = np.empty_like(raw_x)
    for i, hw in enumerate(HW_EXT):
        raw_x[i] = N_X * P2 * _interband_integral(hw, T, xp) / hw**2
        raw_l[i] = N_L      * _interband_integral(hw, T, lp, is_L=True) / hw**2
    bx = _broaden(raw_x, HW_EXT, params["Gamma_X"])[DISP_MASK]
    bl = _broaden(raw_l, HW_EXT, params["Gamma_L"])[DISP_MASK]
    return (bx + bl, bx, bl)


def compute_drude(hw, params: dict):
    """Drude ε₂ (high-frequency limit): ε₂ = ωp²γ_D / ω³ ≡ A_drude / ω³.

    A_drude is in absolute ε₂·eV³ units (not scaled by the interband Scale factor).
    For gold: ωp ≈ 9 eV, γ_D ≈ 0.07 eV → A_drude ≈ 5.7.
    """
    A_D = params["A_drude"]
    return A_D / hw**3


# ═══════════════════════════════════════════════════════════════════════════
#  Default parameters  (Christensen & Seraphin 1971 / Rosei 1975)
# ═══════════════════════════════════════════════════════════════════════════

DEFAULTS = dict(
    Eg_X=1.94, Eg_L=2.45,
    mc_perp_X=0.31, mc_par_X=0.40, mv_perp_X=0.19, mv_par_X=0.15,
    mc_perp_L=0.24, mc_par_L=0.12, mv_perp_L=0.70, mv_par_L=1.03,
    P_ratio_sq=0.370, T_val=600.0, Gamma_X=0.07, Gamma_L=0.07,
    A_drude=6.0, Scale=1.0,
)

# Slider specifications: (key, label, min, max, default, step, decimals)
SLIDER_X = [
    ("Eg_X",      "Eg_X (eV)",  1.70, 2.10, DEFAULTS["Eg_X"],      0.01, 2),
    ("mc_perp_X", "mc⊥ X",      0.15, 0.60, DEFAULTS["mc_perp_X"], 0.01, 2),
    ("mc_par_X",  "mc∥ X",      0.15, 0.60, DEFAULTS["mc_par_X"],  0.01, 2),
    ("mv_perp_X", "mv⊥ X",      0.10, 0.50, DEFAULTS["mv_perp_X"], 0.01, 2),
    ("mv_par_X",  "mv∥ X",      0.05, 0.40, DEFAULTS["mv_par_X"],  0.01, 2),
    ("Gamma_X",   "\u0393_X (eV)",  0.00, 0.30, DEFAULTS["Gamma_X"],   0.005, 3),
]
SLIDER_L = [
    ("Eg_L",      "Eg_L (eV)",  2.20, 2.60, DEFAULTS["Eg_L"],      0.01, 2),
    ("mc_perp_L", "mc\u22a5 L",      0.10, 0.50, DEFAULTS["mc_perp_L"], 0.01, 2),
    ("mc_par_L",  "mc\u2225 L",      0.05, 0.30, DEFAULTS["mc_par_L"],  0.01, 2),
    ("mv_perp_L", "mv\u22a5 L",      0.30, 1.50, DEFAULTS["mv_perp_L"], 0.01, 2),
    ("mv_par_L",  "mv\u2225 L",      0.50, 2.50, DEFAULTS["mv_par_L"],  0.01, 2),
    ("Gamma_L",   "\u0393_L (eV)",  0.00, 0.30, DEFAULTS["Gamma_L"],   0.005, 3),
]
SLIDER_SHARED = [
    ("P_ratio_sq", "|Px/PL|²",  0.10, 1.00, DEFAULTS["P_ratio_sq"], 0.01, 2),

    ("T_val",      "T_eff (K)", 10.0, 1000.0, DEFAULTS["T_val"],    10.0, 0),
    ("A_drude",    "A_drude",   0.00, 30.0, DEFAULTS["A_drude"],    0.1,  1),
    ("Scale",      "Scale",     10.0, 2000.0, DEFAULTS["Scale"],    1.0,  1),
]


# ═══════════════════════════════════════════════════════════════════════════
#  Data loading
# ═══════════════════════════════════════════════════════════════════════════

def load_data():
    d = os.path.dirname(os.path.abspath(__file__))
    def _load(fn):
        arr = np.loadtxt(os.path.join(d, fn), delimiter=",", skiprows=1)
        return arr[arr[:, 0].argsort()]
    return dict(
        X   = _load("a_e2_X.txt"),
        L   = _load("b_e2_L.txt"),
        XL  = _load("c_e2_X_L.txt"),
        XLD = _load("d_e2_X_L_Drude.txt"),
    )


# ═══════════════════════════════════════════════════════════════════════════
#  Optimiser (runs in a daemon thread)
# ═══════════════════════════════════════════════════════════════════════════

class _AbortOptimization(Exception):
    pass


def _run_optimize(x0, fit_keys, bounds, data, vis_flags, base_params,
                  abort_event: threading.Event, signal, fixed_scale=None):
    """Run Nelder-Mead in a daemon thread; emit result via signal.
    
    If fixed_scale is given, use it instead of computing an analytic optimal
    scale (used for X-only / L-only fits where Scale stays at its slider value).
    """
    base = dict(base_params)

    def cost(x):
        p = dict(base)
        for k, v, (lo, hi) in zip(fit_keys, x, bounds):
            p[k] = float(np.clip(v, lo, hi))
        try:
            tot, cx, cl = compute_interband(p)
        except Exception:
            return 1e10
        parts = []
        if vis_flags.get("X"):  parts.append((data["X"], cx))
        if vis_flags.get("L"):  parts.append((data["L"], cl))
        if vis_flags.get("XL"): parts.append((data["XL"], tot))
        if not parts:
            parts = [(data["XL"], tot)]

        if fixed_scale is not None:
            scale = fixed_scale
        else:
            num = den = 0.0
            for d, m in parts:
                mi = np.interp(d[:, 0], HW_DISP, m)
                num += np.dot(d[:, 1], mi)
                den += np.dot(mi, mi)
            scale = num / den if den > 1e-30 else 1.0

        return sum(np.sum((d[:, 1] - scale * np.interp(d[:, 0], HW_DISP, m))**2)
                   for d, m in parts)

    def check_abort(xk):
        if abort_event.is_set():
            raise _AbortOptimization()

    try:
        res = minimize(cost, x0, method="Nelder-Mead",
                       callback=check_abort,
                       options={"maxiter": 5000, "xatol": 1e-5,
                                "fatol": 1e-10, "adaptive": True})
    except _AbortOptimization:
        res = None
    signal.emit(res)


# ═══════════════════════════════════════════════════════════════════════════
#  Main window
# ═══════════════════════════════════════════════════════════════════════════

class RoseiApp(QMainWindow):
    _opt_finished = pyqtSignal(object)   # emitted from worker thread

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rosei \u03b5\u2082 \u2014 Guerrisi, Rosei & Winsemius (1975)")
        self.data = load_data()
        self.spins: dict[str, QDoubleSpinBox] = {}
        self._opt_thread: threading.Thread | None = None
        self._abort_event = threading.Event()
        self._opt_finished.connect(self._on_optimize_done)

        # Auto-scale from initial interband fit
        tot0, cx0, cl0 = compute_interband(DEFAULTS)
        mi = np.interp(self.data["XL"][:, 0], HW_DISP, tot0)
        mk = mi > 1e-12
        auto_scale = float(np.dot(self.data["XL"][mk, 1], mi[mk]) /
                           np.dot(mi[mk], mi[mk]))
        DEFAULTS["Scale"] = round(auto_scale, 1)
        # Update Scale slider range
        for spec in SLIDER_SHARED:
            if spec[0] == "Scale":
                idx = SLIDER_SHARED.index(spec)
                SLIDER_SHARED[idx] = ("Scale", "Scale",
                                      round(0.1 * auto_scale, 1),
                                      round(5.0 * auto_scale, 1),
                                      round(auto_scale, 1), 1.0, 1)
                break

        self._build_ui()
        self._update()

    # ── Build UI ────────────────────────────────────────────────────────

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(4, 4, 4, 4)

        # ── 2×2 plot grid ───────────────────────────────────────────────
        plot_grid = QGridLayout()
        plot_grid.setVerticalSpacing(18)
        self.figures = {}
        self.canvases = {}
        self.axes = {}
        self.lines = {}
        self.scats = {}
        self.r2 = {}

        titles = {
            "X":  "X-point",
            "L":  "L-point",
            "XL": "X + L",
            "XLD": "X + L + Drude",
        }
        positions = {"X": (0, 0), "L": (0, 1), "XL": (1, 0), "XLD": (1, 1)}

        for key, (row, col) in positions.items():
            fig = Figure(figsize=(5, 3.5), dpi=100)
            fig.patch.set_alpha(0.0)
            fig.subplots_adjust(left=0.12, right=0.97, top=0.92, bottom=0.18)
            canvas = FigureCanvas(fig)
            canvas.setStyleSheet("background: transparent;")
            canvas.setSizePolicy(QSizePolicy.Policy.Expanding,
                                 QSizePolicy.Policy.Expanding)
            ax = fig.add_subplot(111)
            ax.set_xlabel("ℏω (eV)")
            ax.set_ylabel("ε₂")
            ax.set_xlim(HW_LO, HW_HI)
            ax.set_title(titles[key])
            ax.grid(alpha=0.25)

            d = self.data[key]
            scat = ax.plot(d[:, 0], d[:, 1], "o", color="0.45", ms=4,
                           alpha=0.6, markeredgewidth=0, label="Data")[0]
            line = ax.plot(HW_DISP, np.zeros_like(HW_DISP), "-",
                           color="#1f3d73", lw=1.8, label="Model")[0]
            ax.legend(loc="upper left", fontsize=8, framealpha=0.9)

            # Double-click to enlarge
            canvas.mpl_connect("button_press_event",
                               lambda evt, k=key: self._on_dblclick(evt, k))

            self.figures[key] = fig
            self.canvases[key] = canvas
            self.axes[key] = ax
            self.lines[key] = line
            self.scats[key] = scat
            self.r2[key] = 0.0

            # Stack canvas in panel
            panel = QWidget()
            panel_layout = QVBoxLayout(panel)
            panel_layout.setContentsMargins(0, 0, 0, 0)
            panel_layout.setSpacing(0)
            panel_layout.addWidget(canvas, stretch=1)
            plot_grid.addWidget(panel, row, col)

        root.addLayout(plot_grid, stretch=3)
        root.addSpacing(10)

        # ── Slider panel ────────────────────────────────────────────────
        slider_row = QHBoxLayout()

        slider_row.addWidget(self._make_slider_group("X-point", SLIDER_X))
        slider_row.addWidget(self._make_slider_group("L-point", SLIDER_L))

        # Shared group + preset/reset controls stacked vertically
        shared_col = QVBoxLayout()
        shared_col.addWidget(self._make_slider_group("Shared", SLIDER_SHARED))

        preset_row = QHBoxLayout()
        self.preset_combo = QComboBox()
        self.preset_combo.setMinimumWidth(160)
        self._refresh_preset_combo()
        self.preset_combo.currentTextChanged.connect(self._on_preset_selected)
        self.btn_save_preset = QPushButton("Save")
        self.btn_save_preset.clicked.connect(self._on_save_preset)
        self.btn_del_preset = QPushButton("Delete")
        self.btn_del_preset.clicked.connect(self._on_delete_preset)
        self.btn_rst = QPushButton("Reset")
        self.btn_rst.clicked.connect(self._on_reset)
        preset_row.addWidget(self.preset_combo)
        preset_row.addWidget(self.btn_save_preset)
        preset_row.addWidget(self.btn_del_preset)
        preset_row.addWidget(self.btn_rst)
        shared_col.addLayout(preset_row)

        slider_row.addLayout(shared_col)

        root.addLayout(slider_row, stretch=0)

        self.statusBar().showMessage("Ready")
        self.resize(1200, 950)

    def _make_slider_group(self, title: str, specs) -> QGroupBox:
        group = QGroupBox(title)
        form = QFormLayout()
        form.setContentsMargins(4, 2, 4, 2)
        form.setSpacing(3)
        for key, label, lo, hi, default, step, decimals in specs:
            spin = QDoubleSpinBox()
            spin.setRange(lo, hi)
            spin.setDecimals(decimals)
            spin.setSingleStep(step)
            spin.setValue(default)
            spin.setFixedWidth(120)
            spin.valueChanged.connect(self._on_param_changed)
            self.spins[key] = spin
            # Label shows default in parentheses as reference
            ref = f"{label}  [{default}]"
            form.addRow(ref, spin)
        group.setLayout(form)
        return group

    # ── Enlarge subplot on double-click ─────────────────────────────────

    def _on_dblclick(self, event, key):
        if event.dblclick and event.button == 1:
            self._show_enlarged(key)

    def _show_enlarged(self, key):
        """Open a resizable dialog with a live copy of the subplot."""
        titles = {"X": "X-point", "L": "L-point",
                  "XL": "X + L", "XLD": "X + L + Drude"}

        dlg = QDialog(self)
        dlg.setWindowTitle(titles.get(key, key))
        dlg.resize(900, 600)
        layout = QVBoxLayout(dlg)
        layout.setContentsMargins(4, 4, 4, 4)

        fig = Figure(figsize=(9, 6), dpi=100)
        fig.subplots_adjust(left=0.10, right=0.97, top=0.94, bottom=0.10)
        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Policy.Expanding,
                             QSizePolicy.Policy.Expanding)
        toolbar = NavigationToolbar(canvas, dlg)
        layout.addWidget(toolbar)
        layout.addWidget(canvas, stretch=1)

        ax = fig.add_subplot(111)
        d = self.data[key]
        ax.plot(d[:, 0], d[:, 1], "o", color="0.45", ms=5, alpha=0.6,
                markeredgewidth=0, label="Data")
        y = self.lines[key].get_ydata()
        ax.plot(HW_DISP, y, "-", color="#1f3d73", lw=2,
                label=f"Model  R²={self.r2[key]:.4f}")
        ax.set_xlabel("ℏω (eV)", fontsize=13)
        ax.set_ylabel("ε₂", fontsize=13)
        ax.set_title(titles.get(key, key), fontsize=14)
        ax.set_xlim(HW_LO, HW_HI)
        ymax = max(np.max(d[:, 1]), np.max(y)) * 1.15 if len(y) else 10
        ax.set_ylim(0, max(ymax, 0.5))
        ax.legend(fontsize=11, framealpha=0.9)
        ax.grid(alpha=0.25)
        canvas.draw()

        dlg.exec()

    # ── Callbacks ───────────────────────────────────────────────────────

    def _get_params(self) -> dict:
        return {k: spin.value() for k, spin in self.spins.items()}

    def _on_param_changed(self, _=None):
        self._update()

    def _update(self):
        p = self._get_params()
        scale = p["Scale"]
        tot, cx, cl = compute_interband(p)
        drude = compute_drude(HW_DISP, p)   # absolute ε₂ units, not scaled

        # Drude is NOT multiplied by Scale (it's already in ε₂ units)
        curves = {"X": scale * cx, "L": scale * cl,
                  "XL": scale * tot, "XLD": scale * tot + drude}

        for key in ("X", "L", "XL", "XLD"):
            y = curves[key]
            self.lines[key].set_ydata(y)
            d = self.data[key]
            r2 = _r_squared(d[:, 0], d[:, 1], HW_DISP, y)
            self.r2[key] = r2
            ax = self.axes[key]
            ax.legend([self.scats[key], self.lines[key]],
                      ["Data", f"Model  R²={r2:.4f}"],
                      loc="upper left", fontsize=8, framealpha=0.9)
            ymax = max(np.max(d[:, 1]), np.max(y)) * 1.15 if len(y) else 10
            ax.set_ylim(0, max(ymax, 0.5))
            self.canvases[key].draw_idle()

        self.statusBar().showMessage(
            f"R²  X={self.r2['X']:.4f}  L={self.r2['L']:.4f}  "
            f"XL={self.r2['XL']:.4f}  XLD={self.r2['XLD']:.4f}")

    def _on_reset(self):
        for key, spin in self.spins.items():
            spin.blockSignals(True)
            spin.setValue(DEFAULTS[key])
            spin.blockSignals(False)
        self._update()

    # ── Presets ─────────────────────────────────────────────────────────

    @staticmethod
    def _preset_path():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "rosei_presets.json")

    def _load_presets_file(self) -> dict:
        path = self._preset_path()
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save_presets_file(self, presets: dict):
        with open(self._preset_path(), "w", encoding="utf-8") as f:
            json.dump(presets, f, indent=2)

    def _refresh_preset_combo(self):
        self.preset_combo.blockSignals(True)
        self.preset_combo.clear()
        presets = self._load_presets_file()
        for name in sorted(presets.keys()):
            self.preset_combo.addItem(name)
        self.preset_combo.blockSignals(False)

    def _on_save_preset(self):
        name, ok = QInputDialog.getText(self, "Save Preset", "Preset name:")
        if not ok or not name.strip():
            return
        name = name.strip()
        presets = self._load_presets_file()
        p = self._get_params()
        # Store R² alongside parameters
        p["_r2"] = dict(self.r2)
        presets[name] = p
        self._save_presets_file(presets)
        self._refresh_preset_combo()
        self.preset_combo.blockSignals(True)
        self.preset_combo.setCurrentText(name)
        self.preset_combo.blockSignals(False)
        self.statusBar().showMessage(f"Saved preset '{name}'")

    def _on_preset_selected(self, name: str):
        if not name:
            return
        presets = self._load_presets_file()
        if name not in presets:
            return
        p = presets[name]
        for spin in self.spins.values():
            spin.blockSignals(True)
        for k, spin in self.spins.items():
            if k in p:
                spin.setValue(float(p[k]))
        for spin in self.spins.values():
            spin.blockSignals(False)
        self._update()
        self.statusBar().showMessage(f"Loaded preset '{name}'")

    def _on_delete_preset(self):
        name = self.preset_combo.currentText()
        if not name:
            return
        presets = self._load_presets_file()
        if name in presets:
            del presets[name]
            self._save_presets_file(presets)
        self._refresh_preset_combo()
        self.statusBar().showMessage(f"Deleted preset '{name}'")

    # ── Optimization (threaded) ─────────────────────────────────────────

    def _on_optimize(self, scope="ALL"):
        if self._opt_thread is not None and self._opt_thread.is_alive():
            return

        # Select which parameters and datasets to optimise against
        if scope == "X":
            specs = SLIDER_X
            vis = {"X": True}
        elif scope == "L":
            specs = SLIDER_L
            vis = {"L": True}
        else:  # ALL — fit against X and L data only
            specs = SLIDER_X + SLIDER_L + SLIDER_SHARED
            vis = {"X": True, "L": True}

        fit_keys = [s[0] for s in specs if s[0] != "Scale"]
        bounds   = [(s[2], s[3]) for s in specs if s[0] != "Scale"]
        x0 = np.array([self.spins[k].value() for k in fit_keys])

        self._opt_scope = scope
        self._abort_event.clear()

        self.statusBar().showMessage(f"Running Nelder-Mead ({scope})…")

        # For X/L-only: freeze the current Scale value.
        # For ALL: let the optimizer find the best scale analytically.
        fixed_scale = self.spins["Scale"].value() if scope != "ALL" else None

        self._opt_thread = threading.Thread(
            target=_run_optimize,
            args=(x0, fit_keys, bounds, self.data, vis,
                  self._get_params(), self._abort_event, self._opt_finished,
                  fixed_scale),
            daemon=True,
        )
        self._opt_thread.start()

    def _on_optimize_done(self, res):
        if res is None:
            # Aborted
            self.statusBar().showMessage("Optimisation cancelled.")
            self._opt_thread = None
            return

        scope = getattr(self, "_opt_scope", "ALL")
        if scope == "X":
            specs = SLIDER_X
        elif scope == "L":
            specs = SLIDER_L
        else:
            specs = SLIDER_X + SLIDER_L + SLIDER_SHARED

        fit_keys = [s[0] for s in specs if s[0] != "Scale"]
        bounds   = [(s[2], s[3]) for s in specs if s[0] != "Scale"]

        # Block signals while setting many sliders
        for spin in self.spins.values():
            spin.blockSignals(True)

        for k, v, (lo, hi) in zip(fit_keys, res.x, bounds):
            self.spins[k].setValue(float(np.clip(v, lo, hi)))

        # Compute optimal scale (for ALL scope)
        if scope == "ALL":
            p = self._get_params()
            tot, cx, cl = compute_interband(p)
            drude = compute_drude(HW_DISP, p)
            parts = [
                (self.data["XL"], tot),
                (self.data["X"], cx),
                (self.data["L"], cl),
            ]
            num = den = 0.0
            for d, m in parts:
                mi = np.interp(d[:, 0], HW_DISP, m)
                num += np.dot(d[:, 1], mi)
                den += np.dot(mi, mi)
            opt_scale = num / den if den > 1e-30 else DEFAULTS["Scale"]
            self.spins["Scale"].setValue(round(opt_scale, 1))

        for spin in self.spins.values():
            spin.blockSignals(False)

        self._update()
        self.statusBar().showMessage(
            f"Optimisation done ({scope}): {res.message} ({res.nfev} evals)")
        self._opt_thread = None

    def closeEvent(self, event):
        self._abort_event.set()
        event.accept()


# ═══════════════════════════════════════════════════════════════════════════
#  Entry point
# ═══════════════════════════════════════════════════════════════════════════

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        * { font-size: 13pt; }
        QGroupBox { font-size: 14pt; font-weight: bold; }
        QPushButton { font-size: 13pt; padding: 6px 18px; }
        QDoubleSpinBox { font-size: 13pt; }
        QStatusBar { font-size: 12pt; }
    """)
    window = RoseiApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
