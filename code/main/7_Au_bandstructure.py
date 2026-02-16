from __future__ import annotations

import os
import sys
from dataclasses import dataclass

import numpy as np
from matplotlib import colormaps
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import PathCollection
from PyQt6.QtCore import QObject, Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSlider,
    QSpinBox,
    QSplitter,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QAbstractItemView,
)

try:
    from plot_style import apply_style
except Exception:
    apply_style = lambda: None  # noqa: E731


@dataclass
class BandData:
    material_id: str
    bandstructure: object
    spin_channel: object
    energies: np.ndarray
    distance: np.ndarray
    nbands: int
    label_positions: dict[str, list[float]]
    label_order: list[str]
    tick_label_map: dict[float, str]
    xmin: float
    xmax: float


@dataclass(frozen=True)
class TransitionCandidate:
    v: int
    c: int
    onset_ev: float
    k_index: int
    ev_at_onset: float
    ec_at_onset: float

    @property
    def key(self) -> tuple[int, int]:
        return (self.v, self.c)


def _clean_label(label: str) -> str:
    return label.replace(r"\Gamma", "G").replace("GAMMA", "G")


def _merge_label_at_x(tick_map: dict[float, str], x: float, label: str, tol: float = 1e-10) -> None:
    for x0 in list(tick_map):
        if abs(x - x0) <= tol:
            parts = tick_map[x0].split("|")
            if label not in parts:
                tick_map[x0] = f"{tick_map[x0]}|{label}"
            return
    tick_map[x] = label


def parse_band_data(material_id: str, bandstructure: object) -> BandData:
    spin_channel = next(iter(bandstructure.bands))
    energies = np.asarray(bandstructure.bands[spin_channel], dtype=float) - float(bandstructure.efermi)
    distance = np.asarray(bandstructure.distance, dtype=float)
    nbands, _ = energies.shape

    label_positions: dict[str, list[float]] = {}
    label_order: list[str] = []
    for i, kp in enumerate(bandstructure.kpoints):
        label = getattr(kp, "label", None)
        if not label:
            continue
        clean = _clean_label(str(label))
        x = float(distance[i])
        if clean not in label_positions:
            label_positions[clean] = []
            label_order.append(clean)
        if all(abs(x - x0) > 1e-10 for x0 in label_positions[clean]):
            label_positions[clean].append(x)

    for lbl in label_positions:
        label_positions[lbl].sort()

    tick_label_map: dict[float, str] = {}
    for lbl, xs in label_positions.items():
        for x in xs:
            _merge_label_at_x(tick_label_map, x, lbl)

    return BandData(
        material_id=material_id,
        bandstructure=bandstructure,
        spin_channel=spin_channel,
        energies=energies,
        distance=distance,
        nbands=nbands,
        label_positions=label_positions,
        label_order=label_order,
        tick_label_map=tick_label_map,
        xmin=float(distance.min()),
        xmax=float(distance.max()),
    )


class MPFetchWorker(QObject):
    finished = pyqtSignal(object, str)
    error = pyqtSignal(str)

    def __init__(self, api_key: str, material_id: str) -> None:
        super().__init__()
        self.api_key = api_key
        self.material_id = material_id

    def run(self) -> None:
        try:
            from mp_api.client import MPRester

            with MPRester(self.api_key) as mpr:
                try:
                    bandstructure = mpr.get_bandstructure_by_material_id(
                        material_id=self.material_id, line_mode=True
                    )
                except TypeError:
                    bandstructure = mpr.get_bandstructure_by_material_id(self.material_id)
            self.finished.emit(bandstructure, self.material_id)
        except Exception as exc:
            self.error.emit(str(exc))


class AuBandGUI(QMainWindow):
    HW_SCALE = 1000

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Au Band Structure Explorer (Materials Project)")
        self.resize(1500, 900)

        self.band_data: BandData | None = None
        self.fetch_thread: QThread | None = None
        self.fetch_worker: MPFetchWorker | None = None
        self._updating_controls = False
        self.transition_candidates: list[TransitionCandidate] = []
        self.transition_candidate_map: dict[tuple[int, int], TransitionCandidate] = {}
        self.selected_transition_keys: list[tuple[int, int]] = []
        self.transition_pick_keys: list[tuple[int, int]] = []
        self.transition_scatter: PathCollection | None = None

        self._build_ui()
        self._connect_signals()
        self._draw_placeholder(self.figure, self.canvas, "Load a material band structure to begin.")
        self._draw_placeholder(
            self.figure_transition,
            self.canvas_transition,
            "Load a material band structure to populate transition picks.",
        )

    def _build_ui(self) -> None:
        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)
        layout.setContentsMargins(6, 6, 6, 6)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)

        controls_scroll = QScrollArea()
        controls_scroll.setWidgetResizable(True)
        controls_scroll.setMinimumWidth(370)
        controls_panel = QWidget()
        controls_scroll.setWidget(controls_panel)
        controls_layout = QVBoxLayout(controls_panel)
        controls_layout.setContentsMargins(8, 8, 8, 8)
        controls_layout.setSpacing(10)

        source_group = QGroupBox("Data Source")
        source_form = QFormLayout(source_group)
        self.api_key_edit = QLineEdit(os.getenv("MP_API_KEY", ""))
        self.api_key_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.api_key_edit.setPlaceholderText("Materials Project API key")
        self.material_id_edit = QLineEdit("mp-81")
        self.load_button = QPushButton("Load Band Structure")
        self.status_label = QLabel("Idle")
        self.status_label.setWordWrap(True)
        source_form.addRow("API key", self.api_key_edit)
        source_form.addRow("Material ID", self.material_id_edit)
        source_form.addRow(self.load_button)
        source_form.addRow("Status", self.status_label)
        controls_layout.addWidget(source_group)

        band_group = QGroupBox("Band Selection")
        band_layout = QVBoxLayout(band_group)
        self.band_list = QListWidget()
        self.band_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.band_list.setMinimumHeight(260)
        self.select_all_button = QPushButton("Select All")
        self.select_near_ef_button = QPushButton("Select Near EF")
        self.clear_bands_button = QPushButton("Clear")
        band_button_row = QHBoxLayout()
        band_button_row.addWidget(self.select_all_button)
        band_button_row.addWidget(self.select_near_ef_button)
        band_button_row.addWidget(self.clear_bands_button)
        band_layout.addWidget(self.band_list)
        band_layout.addLayout(band_button_row)
        controls_layout.addWidget(band_group)

        view_group = QGroupBox("View Controls")
        view_form = QFormLayout(view_group)
        self.view_mode_combo = QComboBox()
        self.view_mode_combo.addItems(["Around point", "Full path"])
        self.center_point_combo = QComboBox()
        self.occurrence_combo = QComboBox()
        self.half_window_spin = QDoubleSpinBox()
        self.half_window_spin.setDecimals(3)
        self.half_window_spin.setSingleStep(0.01)
        self.half_window_spin.setMinimum(0.01)
        self.half_window_spin.setSuffix(" 1/A")
        self.shade_below_ef_checkbox = QCheckBox("Shade E < EF")
        self.shade_below_ef_checkbox.setChecked(True)
        self.show_legend_checkbox = QCheckBox("Show legends")
        self.show_legend_checkbox.setChecked(True)
        view_form.addRow("View", self.view_mode_combo)
        view_form.addRow("Center", self.center_point_combo)
        view_form.addRow("Occurrence", self.occurrence_combo)
        view_form.addRow("Delta k / 2", self.half_window_spin)
        view_form.addRow(self.shade_below_ef_checkbox)
        view_form.addRow(self.show_legend_checkbox)
        controls_layout.addWidget(view_group)

        diff_group = QGroupBox("Branch Difference")
        diff_form = QFormLayout(diff_group)
        self.branch_a_combo = QComboBox()
        self.branch_b_combo = QComboBox()
        self.hbar_slider = QSlider(Qt.Orientation.Horizontal)
        self.hbar_slider.setTracking(True)
        self.hbar_spin = QDoubleSpinBox()
        self.hbar_spin.setDecimals(3)
        self.hbar_spin.setSingleStep(0.01)
        self.hbar_spin.setMinimum(0.0)
        self.hbar_spin.setSuffix(" eV")
        self.shade_diff_checkbox = QCheckBox("Shade region where |dE| <= hbar omega")
        self.shade_diff_checkbox.setChecked(True)
        diff_form.addRow("Branch A", self.branch_a_combo)
        diff_form.addRow("Branch B", self.branch_b_combo)
        diff_form.addRow("hbar omega", self.hbar_slider)
        diff_form.addRow("hbar omega (exact)", self.hbar_spin)
        diff_form.addRow(self.shade_diff_checkbox)
        controls_layout.addWidget(diff_group)

        transition_group = QGroupBox("Transition Picker")
        transition_form = QFormLayout(transition_group)
        self.transition_use_window_checkbox = QCheckBox("Use current k-window")
        self.transition_use_window_checkbox.setChecked(True)
        self.transition_max_pairs_spin = QSpinBox()
        self.transition_max_pairs_spin.setRange(8, 600)
        self.transition_max_pairs_spin.setSingleStep(8)
        self.transition_max_pairs_spin.setValue(120)
        self.transition_clear_button = QPushButton("Clear Picked Transitions")
        transition_form.addRow(self.transition_use_window_checkbox)
        transition_form.addRow("Visible onset points", self.transition_max_pairs_spin)
        transition_form.addRow(self.transition_clear_button)
        controls_layout.addWidget(transition_group)
        controls_layout.addStretch(1)

        splitter.addWidget(controls_scroll)

        plot_panel = QWidget()
        plot_layout = QVBoxLayout(plot_panel)
        plot_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_tabs = QTabWidget()
        self.figure = Figure(figsize=(9.0, 7.0))
        self.canvas = FigureCanvas(self.figure)
        self.figure_transition = Figure(figsize=(9.0, 7.0))
        self.canvas_transition = FigureCanvas(self.figure_transition)
        self.plot_tabs.addTab(self.canvas, "Band Explorer")
        self.plot_tabs.addTab(self.canvas_transition, "Transition Picker")
        plot_layout.addWidget(self.plot_tabs)
        splitter.addWidget(plot_panel)
        splitter.setSizes([380, 1120])
        splitter.setStretchFactor(1, 1)

        self.setStyleSheet(
            """
            QGroupBox {
                font-weight: 600;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 8px;
                padding: 0 4px;
            }
            QListWidget {
                background: #fafafa;
            }
            """
        )

    def _connect_signals(self) -> None:
        self.load_button.clicked.connect(self.load_bandstructure)

        self.select_all_button.clicked.connect(self.select_all_bands)
        self.select_near_ef_button.clicked.connect(self.select_near_ef_bands)
        self.clear_bands_button.clicked.connect(self.clear_band_selection)

        self.band_list.itemSelectionChanged.connect(self.redraw)
        self.view_mode_combo.currentIndexChanged.connect(self.on_view_mode_changed)
        self.center_point_combo.currentIndexChanged.connect(self.on_center_changed)
        self.occurrence_combo.currentIndexChanged.connect(self.redraw)
        self.half_window_spin.valueChanged.connect(self.redraw)
        self.shade_below_ef_checkbox.toggled.connect(self.redraw)
        self.show_legend_checkbox.toggled.connect(self.redraw)

        self.branch_a_combo.currentIndexChanged.connect(self.on_diff_branches_changed)
        self.branch_b_combo.currentIndexChanged.connect(self.on_diff_branches_changed)
        self.hbar_slider.valueChanged.connect(self.on_hbar_slider_changed)
        self.hbar_spin.valueChanged.connect(self.on_hbar_spin_changed)
        self.shade_diff_checkbox.toggled.connect(self.redraw)
        self.transition_use_window_checkbox.toggled.connect(self.redraw)
        self.transition_max_pairs_spin.valueChanged.connect(self.redraw)
        self.transition_clear_button.clicked.connect(self.on_clear_transition_selection)
        self.canvas_transition.mpl_connect("pick_event", self.on_transition_pick)

    def load_bandstructure(self) -> None:
        if self.fetch_thread is not None:
            return

        api_key = self.api_key_edit.text().strip() or os.getenv("MP_API_KEY", "").strip()
        material_id = self.material_id_edit.text().strip()

        if not api_key:
            self._show_error("API key missing. Enter a Materials Project key.")
            return
        if not material_id:
            self._show_error("Material ID is empty.")
            return

        self.status_label.setText(f"Loading {material_id}...")
        self.load_button.setEnabled(False)

        self.fetch_thread = QThread(self)
        self.fetch_worker = MPFetchWorker(api_key, material_id)
        self.fetch_worker.moveToThread(self.fetch_thread)

        self.fetch_thread.started.connect(self.fetch_worker.run)
        self.fetch_worker.finished.connect(self.on_load_success)
        self.fetch_worker.error.connect(self.on_load_error)
        self.fetch_worker.finished.connect(self.fetch_thread.quit)
        self.fetch_worker.error.connect(self.fetch_thread.quit)
        self.fetch_thread.finished.connect(self._on_worker_finished)
        self.fetch_thread.start()

    def on_load_success(self, bandstructure: object, material_id: str) -> None:
        try:
            self.band_data = parse_band_data(material_id, bandstructure)
            if not self.band_data.label_order:
                self._show_error("No labeled high-symmetry points found in this band structure.")
                return
            self.populate_controls_after_load()
            self.status_label.setText(
                f"Loaded {material_id} | bands: {self.band_data.nbands} | spin: {self.band_data.spin_channel}"
            )
            self.redraw()
        except Exception as exc:
            self._show_error(f"Failed to parse data: {exc}")

    def on_load_error(self, message: str) -> None:
        self._show_error(f"Failed to load band structure: {message}")

    def _on_worker_finished(self) -> None:
        self.load_button.setEnabled(True)
        if self.fetch_worker is not None:
            self.fetch_worker.deleteLater()
        if self.fetch_thread is not None:
            self.fetch_thread.deleteLater()
        self.fetch_worker = None
        self.fetch_thread = None

    def populate_controls_after_load(self) -> None:
        if self.band_data is None:
            return

        d = self.band_data
        self._updating_controls = True
        try:
            self.band_list.clear()
            for i in range(d.nbands):
                item = QListWidgetItem(f"band {i}")
                item.setData(Qt.ItemDataRole.UserRole, i)
                self.band_list.addItem(item)

            self.branch_a_combo.clear()
            self.branch_b_combo.clear()
            for i in range(d.nbands):
                self.branch_a_combo.addItem(f"band {i}", i)
                self.branch_b_combo.addItem(f"band {i}", i)

            near_ef = np.argsort(np.min(np.abs(d.energies), axis=1))[: min(6, d.nbands)]
            for idx in near_ef:
                self.band_list.item(int(idx)).setSelected(True)

            self.center_point_combo.clear()
            self.center_point_combo.addItems(d.label_order)
            if "X" in d.label_positions:
                self.center_point_combo.setCurrentText("X")
            elif "L" in d.label_positions:
                self.center_point_combo.setCurrentText("L")

            half_window = min(0.35, max(0.05, (d.xmax - d.xmin) / 4))
            self.half_window_spin.setValue(float(half_window))
            self.update_occurrence_combo()

            if d.nbands > 1:
                self.branch_b_combo.setCurrentIndex(1)
            self.update_hbar_range()
            self.update_focus_enabled_state()
            self.selected_transition_keys.clear()
            self.transition_candidates = []
            self.transition_candidate_map = {}
            self.transition_pick_keys = []
            self.transition_scatter = None
        finally:
            self._updating_controls = False

    def update_occurrence_combo(self) -> None:
        if self.band_data is None:
            return
        center = self.center_point_combo.currentText().strip()
        xs = self.band_data.label_positions.get(center, [])

        self.occurrence_combo.blockSignals(True)
        self.occurrence_combo.clear()
        for i, x in enumerate(xs):
            self.occurrence_combo.addItem(f"#{i + 1} @ {x:.3f}", i)
        if xs:
            self.occurrence_combo.setCurrentIndex(0)
        self.occurrence_combo.blockSignals(False)

    def update_focus_enabled_state(self) -> None:
        focus = self.view_mode_combo.currentText() == "Around point"
        self.center_point_combo.setEnabled(focus)
        self.occurrence_combo.setEnabled(focus)
        self.half_window_spin.setEnabled(focus)

    def update_hbar_range(self) -> None:
        if self.band_data is None:
            return
        a = int(self.branch_a_combo.currentData() or 0)
        b = int(self.branch_b_combo.currentData() or 0)
        ea = self.band_data.energies[a, :]
        eb = self.band_data.energies[b, :]
        cross = ((ea < 0.0) & (eb > 0.0)) | ((ea > 0.0) & (eb < 0.0))
        diff_curve = np.abs(ea - eb) * cross.astype(float)
        hmax = max(0.05, float(np.max(diff_curve)) * 1.05)

        current = self.hbar_spin.value()
        if current <= 1e-12:
            current = 0.4 * hmax
        value = min(current, hmax)
        self.hbar_spin.blockSignals(True)
        self.hbar_slider.blockSignals(True)
        self.hbar_spin.setMaximum(hmax)
        self.hbar_spin.setValue(value)
        self.hbar_slider.setMinimum(0)
        self.hbar_slider.setMaximum(max(1, int(round(hmax * self.HW_SCALE))))
        self.hbar_slider.setValue(int(round(value * self.HW_SCALE)))
        self.hbar_slider.blockSignals(False)
        self.hbar_spin.blockSignals(False)

    def select_all_bands(self) -> None:
        self._set_band_selection(range(self.band_list.count()))

    def clear_band_selection(self) -> None:
        self._set_band_selection([])

    def select_near_ef_bands(self) -> None:
        if self.band_data is None:
            return
        near_ef = np.argsort(np.min(np.abs(self.band_data.energies), axis=1))[: min(6, self.band_data.nbands)]
        self._set_band_selection([int(i) for i in near_ef])

    def _set_band_selection(self, indices: list[int] | range) -> None:
        index_set = set(int(i) for i in indices)
        self.band_list.blockSignals(True)
        for row in range(self.band_list.count()):
            self.band_list.item(row).setSelected(row in index_set)
        self.band_list.blockSignals(False)
        self.redraw()

    def selected_bands(self) -> list[int]:
        out: list[int] = []
        for item in self.band_list.selectedItems():
            idx = item.data(Qt.ItemDataRole.UserRole)
            if idx is not None:
                out.append(int(idx))
        return sorted(set(out))

    def on_view_mode_changed(self) -> None:
        if self._updating_controls:
            return
        self.update_focus_enabled_state()
        self.redraw()

    def on_center_changed(self) -> None:
        if self._updating_controls:
            return
        self.update_occurrence_combo()
        self.redraw()

    def on_diff_branches_changed(self) -> None:
        if self._updating_controls:
            return
        self.update_hbar_range()
        self.redraw()

    def on_hbar_slider_changed(self, value: int) -> None:
        if self._updating_controls:
            return
        evalue = float(value) / self.HW_SCALE
        self.hbar_spin.blockSignals(True)
        self.hbar_spin.setValue(evalue)
        self.hbar_spin.blockSignals(False)
        self.redraw()

    def on_hbar_spin_changed(self, value: float) -> None:
        if self._updating_controls:
            return
        sval = int(round(float(value) * self.HW_SCALE))
        self.hbar_slider.blockSignals(True)
        self.hbar_slider.setValue(sval)
        self.hbar_slider.blockSignals(False)
        self.redraw()

    def on_clear_transition_selection(self) -> None:
        self.selected_transition_keys.clear()
        self.redraw()

    def on_transition_pick(self, event) -> None:
        if self.band_data is None:
            return
        if self.transition_scatter is None:
            return
        if event.artist is not self.transition_scatter:
            return
        inds = getattr(event, "ind", None)
        if inds is None or len(inds) == 0:
            return

        pick_i = int(inds[0])
        if pick_i < 0 or pick_i >= len(self.transition_pick_keys):
            return
        key = self.transition_pick_keys[pick_i]
        if key in self.selected_transition_keys:
            self.selected_transition_keys = [k for k in self.selected_transition_keys if k != key]
        else:
            self.selected_transition_keys.append(key)
            if len(self.selected_transition_keys) > 12:
                self.selected_transition_keys = self.selected_transition_keys[-12:]
        self._draw_transition_picker()

    def _current_x_window(self) -> tuple[float, float, float | None]:
        assert self.band_data is not None
        d = self.band_data
        mode = self.view_mode_combo.currentText()
        if mode == "Around point":
            center = self.center_point_combo.currentText().strip()
            xs = d.label_positions.get(center, [])
            if xs:
                occ = int(self.occurrence_combo.currentData() or 0)
                occ = max(0, min(occ, len(xs) - 1))
                x0 = float(xs[occ])
                dk = float(self.half_window_spin.value())
                return max(d.xmin, x0 - dk), min(d.xmax, x0 + dk), x0
        return d.xmin, d.xmax, None

    def _x_window_mask(self) -> tuple[float, float, float | None, np.ndarray]:
        assert self.band_data is not None
        d = self.band_data
        xlo, xhi, x0 = self._current_x_window()
        mask = (d.distance >= xlo - 1e-12) & (d.distance <= xhi + 1e-12)
        if not np.any(mask):
            mask = np.ones_like(d.distance, dtype=bool)
        return xlo, xhi, x0, mask

    def _build_tick_labels(
        self, xlo: float, xhi: float, x0: float | None
    ) -> tuple[list[float], dict[float, str]]:
        assert self.band_data is not None
        d = self.band_data
        tick_label_map = dict(d.tick_label_map)
        tick_x = [x for x in sorted(tick_label_map) if (x >= xlo - 1e-12 and x <= xhi + 1e-12)]
        if x0 is not None and all(abs(x - x0) > 1e-10 for x in tick_x):
            center = self.center_point_combo.currentText().strip()
            tick_x.append(x0)
            tick_x.sort()
            _merge_label_at_x(tick_label_map, x0, center)
        return tick_x, tick_label_map

    def _compute_transition_candidates(self, mask: np.ndarray) -> list[TransitionCandidate]:
        assert self.band_data is not None
        d = self.band_data
        global_idx = np.where(mask)[0]
        energies = d.energies[:, global_idx]
        valence = np.where(np.any(energies < 0.0, axis=1))[0]
        conduction = np.where(np.any(energies > 0.0, axis=1))[0]

        out: list[TransitionCandidate] = []
        for v in valence:
            ev = energies[v, :]
            for c in conduction:
                if c == v:
                    continue
                ec = energies[c, :]
                cross = (ev < 0.0) & (ec > 0.0)
                if not np.any(cross):
                    continue
                local_cross = np.where(cross)[0]
                delta = ec[cross] - ev[cross]
                j = int(np.argmin(delta))
                k_local = int(local_cross[j])
                k_global = int(global_idx[k_local])
                out.append(
                    TransitionCandidate(
                        v=v,
                        c=c,
                        onset_ev=float(delta[j]),
                        k_index=k_global,
                        ev_at_onset=float(d.energies[v, k_global]),
                        ec_at_onset=float(d.energies[c, k_global]),
                    )
                )
        out.sort(key=lambda t: (t.onset_ev, t.v, t.c))
        return out

    def redraw(self) -> None:
        if self._updating_controls:
            return
        if self.band_data is None:
            self._draw_placeholder(self.figure, self.canvas, "Load a material band structure to begin.")
            self._draw_placeholder(
                self.figure_transition,
                self.canvas_transition,
                "Load a material band structure to populate transition picks.",
            )
            return
        self._draw_band_explorer()
        self._draw_transition_picker()

    def _draw_band_explorer(self) -> None:
        assert self.band_data is not None
        d = self.band_data
        selected = self.selected_bands()
        xlo, xhi, x0, mask = self._x_window_mask()

        self.figure.clear()
        gs = self.figure.add_gridspec(2, 1, height_ratios=[3.3, 1.7], hspace=0.08)
        ax_band = self.figure.add_subplot(gs[0, 0])
        ax_diff = self.figure.add_subplot(gs[1, 0], sharex=ax_band)

        if selected:
            cmap = colormaps.get_cmap("tab10")
            for j, band_idx in enumerate(selected):
                color = cmap(j % 10)
                first_segment = True
                for branch in d.bandstructure.branches:
                    i0 = int(branch["start_index"])
                    i1 = int(branch["end_index"]) + 1
                    ax_band.plot(
                        d.distance[i0:i1],
                        d.energies[band_idx, i0:i1],
                        color=color,
                        lw=1.35,
                        label=f"band {band_idx}" if first_segment else None,
                    )
                    first_segment = False

            selected_energy = d.energies[selected, :][:, mask]
            emin = float(np.min(selected_energy))
            emax = float(np.max(selected_energy))
            pad = max(0.2, 0.08 * (emax - emin if emax > emin else 1.0))
            ax_band.set_ylim(emin - pad, emax + pad)

            if self.shade_below_ef_checkbox.isChecked():
                ymin, _ = ax_band.get_ylim()
                if ymin < 0.0:
                    ax_band.axhspan(ymin, 0.0, color="0.88", alpha=0.3, zorder=-2)

            if self.show_legend_checkbox.isChecked() and len(selected) <= 12:
                ax_band.legend(frameon=False, ncol=2, fontsize=9, loc="best")
        else:
            ax_band.text(
                0.5,
                0.5,
                "Select at least one band.",
                ha="center",
                va="center",
                transform=ax_band.transAxes,
            )

        tick_x, tick_label_map = self._build_tick_labels(xlo, xhi, x0)
        for xt in tick_x:
            ax_band.axvline(xt, color="0.85", lw=0.8, zorder=0)
            ax_diff.axvline(xt, color="0.85", lw=0.8, zorder=0)

        ax_band.set_xlim(xlo, xhi)
        ax_band.axhline(0.0, color="black", lw=0.95, ls="--", alpha=0.8)
        ax_band.set_ylabel(r"$E - E_F$ (eV)")
        ax_band.set_title(f"{d.material_id}: band structure")
        ax_band.tick_params(axis="x", labelbottom=False)

        a = int(self.branch_a_combo.currentData() or 0)
        b = int(self.branch_b_combo.currentData() or 0)
        ea = d.energies[a, :]
        eb = d.energies[b, :]
        cross_factor = ((ea < 0.0) & (eb > 0.0)) | ((ea > 0.0) & (eb < 0.0))
        diff_curve = np.abs(ea - eb) * cross_factor.astype(float)

        x_vis = d.distance[mask]
        diff_vis = diff_curve[mask]
        cross_vis = cross_factor[mask]

        ax_diff.plot(
            x_vis,
            diff_vis,
            color="tab:red",
            lw=1.5,
            label=f"|band {a} - band {b}| * I(opposite EF side)",
        )
        ax_diff.fill_between(x_vis, 0.0, diff_vis, color="0.92", alpha=0.8, zorder=-3)

        hw = float(self.hbar_spin.value())
        if self.shade_diff_checkbox.isChecked():
            region_mask = cross_vis & (diff_vis <= hw)
            ax_diff.fill_between(
                x_vis,
                0.0,
                diff_vis,
                where=region_mask,
                interpolate=True,
                color="tab:orange",
                alpha=0.45,
                label="region: |dE| <= hbar omega",
                zorder=-2,
            )

        ax_diff.axhline(hw, color="black", lw=0.95, ls=":", alpha=0.85, label=f"hbar omega = {hw:.3f} eV")
        ytop = max(float(np.max(diff_vis)), hw)
        ypad = max(0.05, 0.12 * (ytop if ytop > 0 else 1.0))
        ax_diff.set_ylim(0.0, ytop + ypad)
        ax_diff.set_ylabel(r"$|\Delta E|$ (eV)")
        ax_diff.set_xlabel("High-symmetry k-path")
        ax_diff.set_xticks(tick_x)
        ax_diff.set_xticklabels([tick_label_map[x] for x in tick_x])

        if self.show_legend_checkbox.isChecked():
            ax_diff.legend(frameon=False, fontsize=8, loc="upper right")

        self.canvas.draw_idle()

    def _draw_transition_picker(self) -> None:
        assert self.band_data is not None
        d = self.band_data

        if self.transition_use_window_checkbox.isChecked():
            xlo, xhi, x0, mask = self._x_window_mask()
            window_text = f"window [{xlo:.3f}, {xhi:.3f}] 1/A"
        else:
            xlo, xhi, x0 = d.xmin, d.xmax, None
            mask = np.ones_like(d.distance, dtype=bool)
            window_text = "full path"

        candidates = self._compute_transition_candidates(mask)
        self.transition_candidates = candidates
        self.transition_candidate_map = {t.key: t for t in candidates}
        self.selected_transition_keys = [k for k in self.selected_transition_keys if k in self.transition_candidate_map]

        self.figure_transition.clear()
        if not candidates:
            self.transition_pick_keys = []
            self.transition_scatter = None
            self._draw_placeholder(
                self.figure_transition,
                self.canvas_transition,
                "No interband onset transitions found in current selection/window.",
            )
            return

        max_pairs = int(self.transition_max_pairs_spin.value())
        visible = candidates[: max_pairs]
        self.transition_pick_keys = [t.key for t in visible]

        gs = self.figure_transition.add_gridspec(2, 1, height_ratios=[1.35, 2.2], hspace=0.18)
        ax_onset = self.figure_transition.add_subplot(gs[0, 0])
        ax_pick = self.figure_transition.add_subplot(gs[1, 0])

        x = np.array([t.onset_ev for t in visible], dtype=float)
        y = np.arange(len(visible), dtype=float)
        self.transition_scatter = ax_onset.scatter(
            x,
            y,
            c=x,
            cmap="viridis",
            s=52,
            alpha=0.95,
            picker=True,
            edgecolors="none",
        )
        selected_set = set(self.selected_transition_keys)
        selected_vis = [i for i, t in enumerate(visible) if t.key in selected_set]
        if selected_vis:
            ax_onset.scatter(
                x[selected_vis],
                y[selected_vis],
                facecolors="none",
                edgecolors="black",
                linewidths=1.2,
                s=110,
                zorder=4,
            )
        cbar = self.figure_transition.colorbar(self.transition_scatter, ax=ax_onset, pad=0.01)
        cbar.set_label("Onset hbar omega (eV)", fontsize=8)

        ax_onset.set_yticks(y)
        ax_onset.set_yticklabels([f"v{t.v}->c{t.c}" for t in visible], fontsize=8)
        ax_onset.invert_yaxis()
        ax_onset.grid(axis="x", alpha=0.25)
        ax_onset.set_xlabel("Onset hbar omega (eV)")
        ax_onset.set_title("Clickable onset map (click points to toggle transitions)")

        for band_idx in range(d.nbands):
            ax_pick.plot(d.distance, d.energies[band_idx, :], color="0.86", lw=0.8, zorder=0)

        color_cycle = colormaps.get_cmap("tab10")
        selected_candidates = [self.transition_candidate_map[k] for k in self.selected_transition_keys if k in self.transition_candidate_map]
        nsel = len(selected_candidates)
        xspan = d.xmax - d.xmin
        for i, t in enumerate(selected_candidates):
            color = color_cycle(i % 10)
            ax_pick.plot(d.distance, d.energies[t.v, :], color=color, lw=1.7, ls="--", alpha=0.9, label=f"T{i + 1}: v{t.v}->c{t.c}")
            ax_pick.plot(d.distance, d.energies[t.c, :], color=color, lw=1.7, ls="-", alpha=0.9)

            base_x = float(d.distance[t.k_index])
            dx = ((i - 0.5 * (nsel - 1)) * 0.01 * xspan) if nsel > 1 else 0.0
            x_arrow = np.clip(base_x + dx, d.xmin, d.xmax)
            y1 = float(d.energies[t.v, t.k_index])
            y2 = float(d.energies[t.c, t.k_index])
            ax_pick.annotate(
                "",
                xy=(x_arrow, y2),
                xytext=(x_arrow, y1),
                arrowprops=dict(arrowstyle="<->", color=color, lw=1.9, alpha=0.95),
                zorder=5,
            )
            ymid = 0.5 * (y1 + y2)
            ax_pick.text(
                x_arrow + 0.004 * xspan,
                ymid,
                f"T{i + 1}",
                color=color,
                fontsize=8,
                va="center",
                ha="left",
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=color, alpha=0.75),
                zorder=6,
            )

        tick_x, tick_label_map = self._build_tick_labels(xlo, xhi, x0)
        for xt in tick_x:
            ax_pick.axvline(xt, color="0.9", lw=0.8, zorder=0)
        ax_pick.axhline(0.0, color="black", lw=0.9, ls="--", alpha=0.75, zorder=1)
        ax_pick.set_xlim(xlo, xhi)
        ax_pick.set_ylabel(r"$E - E_F$ (eV)")
        ax_pick.set_xlabel("High-symmetry k-path")
        ax_pick.set_title(
            f"Selected transition branches and arrows ({window_text})\n"
            "Dashed=valence, solid=conduction; arrows at onset-k"
        )
        ax_pick.set_xticks(tick_x)
        ax_pick.set_xticklabels([tick_label_map[xi] for xi in tick_x])
        if self.show_legend_checkbox.isChecked() and selected_candidates:
            ax_pick.legend(frameon=False, fontsize=8, ncol=2, loc="best")

        self.canvas_transition.draw_idle()

    def _draw_placeholder(self, figure: Figure, canvas: FigureCanvas, text: str) -> None:
        figure.clear()
        ax = figure.add_subplot(1, 1, 1)
        ax.text(0.5, 0.5, text, ha="center", va="center", transform=ax.transAxes)
        ax.set_axis_off()
        canvas.draw_idle()

    def _show_error(self, message: str) -> None:
        self.status_label.setText("Error")
        QMessageBox.critical(self, "Error", message)


def main() -> int:
    apply_style()
    app = QApplication(sys.argv)
    window = AuBandGUI()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
