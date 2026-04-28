"""
Data Cleaner GUI — select and remove scatter points from digitised data.
========================================================================
Loads all four data files (X, L, X+L, X+L+Drude).  Click points to
toggle selection (highlighted in red), then press "Remove Selected" to
delete them.  "Save" writes the cleaned data back to disk.  "Undo"
restores the last removal.

Run:  python data_cleaner_gui.py
"""

from __future__ import annotations

import os
import sys
import shutil
import numpy as np

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QPushButton, QLabel, QSizePolicy, QStatusBar, QMessageBox,
)

import matplotlib
matplotlib.use("QtAgg")
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# ═══════════════════════════════════════════════════════════════════════════
#  Data files
# ═══════════════════════════════════════════════════════════════════════════

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "X  (a_e2_X.txt)":           "a_e2_X.txt",
    "L  (b_e2_L.txt)":           "b_e2_L.txt",
    "X+L  (c_e2_X_L.txt)":      "c_e2_X_L.txt",
    "X+L+Drude  (d_e2_X_L_Drude.txt)": "d_e2_X_L_Drude.txt",
}


def _load(fn: str) -> np.ndarray:
    arr = np.loadtxt(os.path.join(DATA_DIR, fn), delimiter=",", skiprows=1)
    return arr[arr[:, 0].argsort()]


# ═══════════════════════════════════════════════════════════════════════════
#  Main window
# ═══════════════════════════════════════════════════════════════════════════

class CleanerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Cleaner")
        self._data: dict[str, np.ndarray] = {}      # label -> array
        self._selected: set[int] = set()             # indices of selected points
        self._undo_stack: list[np.ndarray] = []      # previous states
        self._current_label: str = ""

        # Load all datasets
        for label, fn in FILES.items():
            self._data[label] = _load(fn)

        self._build_ui()
        self._switch_dataset(list(FILES.keys())[3])  # default to X+L+Drude

    # ── UI ──────────────────────────────────────────────────────────────

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(6, 6, 6, 6)

        # Dataset selector
        top_row = QHBoxLayout()
        top_row.addWidget(QLabel("Dataset:"))
        self.combo = QComboBox()
        self.combo.addItems(FILES.keys())
        self.combo.setCurrentText(list(FILES.keys())[3])
        self.combo.currentTextChanged.connect(self._switch_dataset)
        top_row.addWidget(self.combo, stretch=1)
        root.addLayout(top_row)

        # Plot
        self.fig = Figure(figsize=(10, 6), dpi=100)
        self.fig.subplots_adjust(left=0.10, right=0.97, top=0.95, bottom=0.10)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Expanding)
        self.ax = self.fig.add_subplot(111)
        root.addWidget(self.canvas, stretch=1)

        # Connect mouse click
        self.canvas.mpl_connect("button_press_event", self._on_click)

        # Buttons
        btn_row = QHBoxLayout()
        self.btn_remove = QPushButton("Remove Selected")
        self.btn_remove.clicked.connect(self._on_remove)
        self.btn_undo = QPushButton("Undo")
        self.btn_undo.clicked.connect(self._on_undo)
        self.btn_undo.setEnabled(False)
        self.btn_clear = QPushButton("Clear Selection")
        self.btn_clear.clicked.connect(self._on_clear_sel)
        self.btn_save = QPushButton("Save")
        self.btn_save.clicked.connect(self._on_save)
        btn_row.addStretch()
        btn_row.addWidget(self.btn_clear)
        btn_row.addWidget(self.btn_remove)
        btn_row.addWidget(self.btn_undo)
        btn_row.addWidget(self.btn_save)
        btn_row.addStretch()
        root.addLayout(btn_row)

        self.statusBar().showMessage("Click points to select, then Remove.")
        self.resize(1000, 650)

    # ── Dataset switching ───────────────────────────────────────────────

    def _switch_dataset(self, label: str):
        self._current_label = label
        self._selected.clear()
        self._undo_stack.clear()
        self.btn_undo.setEnabled(False)
        self._redraw()

    # ── Drawing ─────────────────────────────────────────────────────────

    def _redraw(self):
        ax = self.ax
        ax.clear()
        d = self._data[self._current_label]
        n = len(d)

        # Unselected points
        mask_unsel = np.array([i not in self._selected for i in range(n)])
        if mask_unsel.any():
            ax.plot(d[mask_unsel, 0], d[mask_unsel, 1], "ko", ms=5,
                    alpha=0.6, picker=True, pickradius=8)

        # Selected points (red)
        mask_sel = ~mask_unsel
        if mask_sel.any():
            ax.plot(d[mask_sel, 0], d[mask_sel, 1], "ro", ms=7, alpha=0.9)

        ax.set_xlabel("\u210f\u03c9 (eV)", fontsize=12)
        ax.set_ylabel("\u03b5\u2082", fontsize=12)
        ax.set_title(self._current_label, fontsize=13)
        ax.grid(alpha=0.25)
        self.canvas.draw_idle()
        self.statusBar().showMessage(
            f"{n} points | {len(self._selected)} selected")

    # ── Click handler ───────────────────────────────────────────────────

    def _on_click(self, event):
        if event.inaxes is not self.ax or event.button != 1:
            return
        d = self._data[self._current_label]
        if len(d) == 0:
            return

        # Find nearest point in data coords
        x_click, y_click = event.xdata, event.ydata

        # Normalise distances by axis range for sensible picking
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        sx = xlim[1] - xlim[0] if xlim[1] != xlim[0] else 1.0
        sy = ylim[1] - ylim[0] if ylim[1] != ylim[0] else 1.0
        dist = ((d[:, 0] - x_click) / sx) ** 2 + ((d[:, 1] - y_click) / sy) ** 2
        idx = int(np.argmin(dist))

        # Only pick if close enough (within ~3% of axis span)
        if np.sqrt(dist[idx]) > 0.03:
            return

        # Toggle selection
        if idx in self._selected:
            self._selected.discard(idx)
        else:
            self._selected.add(idx)
        self._redraw()

    # ── Actions ─────────────────────────────────────────────────────────

    def _on_clear_sel(self):
        self._selected.clear()
        self._redraw()

    def _on_remove(self):
        if not self._selected:
            return
        d = self._data[self._current_label]
        self._undo_stack.append(d.copy())
        self.btn_undo.setEnabled(True)
        keep = np.array([i not in self._selected for i in range(len(d))])
        removed = len(d) - keep.sum()
        self._data[self._current_label] = d[keep]
        self._selected.clear()
        self._redraw()
        self.statusBar().showMessage(f"Removed {removed} points.")

    def _on_undo(self):
        if not self._undo_stack:
            return
        self._data[self._current_label] = self._undo_stack.pop()
        self._selected.clear()
        self.btn_undo.setEnabled(bool(self._undo_stack))
        self._redraw()
        self.statusBar().showMessage("Undo: restored previous state.")

    def _on_save(self):
        label = self._current_label
        fn = FILES[label]
        path = os.path.join(DATA_DIR, fn)

        # Backup
        bak = path + ".bak"
        if not os.path.exists(bak):
            shutil.copy2(path, bak)

        d = self._data[label]
        with open(path, "w") as f:
            f.write("hw, e2\n")
            for row in d:
                f.write(f"{row[0]:.4e},{row[1]:.4e}\n")

        self.statusBar().showMessage(
            f"Saved {len(d)} points to {fn}  (backup: {fn}.bak)")


# ═══════════════════════════════════════════════════════════════════════════
#  Entry point
# ═══════════════════════════════════════════════════════════════════════════

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        * { font-size: 13pt; }
        QPushButton { font-size: 13pt; padding: 6px 18px; }
        QComboBox { font-size: 13pt; }
        QStatusBar { font-size: 12pt; }
    """)
    window = CleanerApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
