from __future__ import annotations

import os
import sys
from dataclasses import dataclass

import numpy as np
from matplotlib import colormaps
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import PathCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
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
    from code.misc.plot_style import apply_style
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


@dataclass
class UniformBandData:
    material_id: str
    bandstructure: object
    spin_channel: object
    energies: np.ndarray
    k_frac_folded: np.ndarray
    k_cart_folded: np.ndarray
    k_cart_plot: np.ndarray
    energies_plot: np.ndarray
    nbands: int
    nkpoints: int
    nkpoints_plot: int
    k_unit_label: str
    expanded_by_symmetry: bool


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


def parse_uniform_band_data(material_id: str, bandstructure: object) -> UniformBandData:
    branches = getattr(bandstructure, "branches", None)
    if branches:
        # Guard against APIs that silently return line-mode path data.
        raise ValueError("Uniform-k request returned line-mode band structure.")

    spin_channel = next(iter(bandstructure.bands))
    energies = np.asarray(bandstructure.bands[spin_channel], dtype=float) - float(bandstructure.efermi)
    k_frac = np.asarray([np.asarray(kp.frac_coords, dtype=float) for kp in bandstructure.kpoints], dtype=float)

    if energies.ndim != 2:
        raise ValueError("Uniform-k band energies are not 2D.")
    if k_frac.ndim != 2 or k_frac.shape[1] != 3:
        raise ValueError("Uniform-k coordinates are not Nx3.")

    nbands, nk = energies.shape
    if nk != k_frac.shape[0]:
        # Robust fallback for unexpected transposed arrays.
        if energies.shape[0] == k_frac.shape[0]:
            energies = energies.T
            nbands, nk = energies.shape
        else:
            raise ValueError("Uniform-k energies and k-point arrays have incompatible shapes.")

    # Fold to centered reciprocal-cell coordinates.
    k_frac_folded = ((k_frac + 0.5) % 1.0) - 0.5

    rec_lattice = getattr(bandstructure, "lattice_rec", None)
    if rec_lattice is not None and hasattr(rec_lattice, "matrix"):
        rec_mat = np.asarray(rec_lattice.matrix, dtype=float)
        k_cart_folded = k_frac_folded @ rec_mat
        k_unit_label = "1/Angstrom"
    else:
        rec_mat = np.eye(3, dtype=float)
        k_cart_folded = k_frac_folded.copy()
        k_unit_label = "r.l.u."

    k_cart_plot, energies_plot, expanded = _expand_kmesh_by_symmetry(
        bandstructure=bandstructure,
        rec_mat=rec_mat,
        k_cart_folded=k_cart_folded,
        energies=energies,
    )

    return UniformBandData(
        material_id=material_id,
        bandstructure=bandstructure,
        spin_channel=spin_channel,
        energies=energies,
        k_frac_folded=k_frac_folded,
        k_cart_folded=k_cart_folded,
        k_cart_plot=k_cart_plot,
        energies_plot=energies_plot,
        nbands=nbands,
        nkpoints=nk,
        nkpoints_plot=int(k_cart_plot.shape[0]),
        k_unit_label=k_unit_label,
        expanded_by_symmetry=expanded,
    )


def _fold_cart_points_to_centered_cell(k_cart: np.ndarray, rec_mat: np.ndarray) -> np.ndarray:
    inv_rec = np.linalg.inv(rec_mat)
    frac = np.asarray(k_cart, dtype=float) @ inv_rec
    frac_fold = ((frac + 0.5) % 1.0) - 0.5
    return frac_fold @ rec_mat


def _expand_kmesh_by_symmetry(
    bandstructure: object,
    rec_mat: np.ndarray,
    k_cart_folded: np.ndarray,
    energies: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, bool]:
    """Expand irreducible k-mesh to full BZ using point-group rotations when available."""
    k0 = np.asarray(k_cart_folded, dtype=float)
    e0 = np.asarray(energies, dtype=float)
    if k0.ndim != 2 or k0.shape[1] != 3 or e0.ndim != 2:
        return k0, e0, False

    ops_mats: list[np.ndarray] = []
    try:
        from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

        structure = getattr(bandstructure, "structure", None)
        if structure is not None:
            sga = SpacegroupAnalyzer(structure, symprec=1e-3)
            ops = sga.get_point_group_operations(cartesian=True)
            for op in ops:
                rot = np.asarray(op.rotation_matrix, dtype=float)
                if rot.shape == (3, 3):
                    ops_mats.append(rot)
    except Exception:
        ops_mats = []

    if not ops_mats:
        return k0, e0, False

    # Add time-reversal partner if inversion is absent in the point group list.
    has_inversion = any(np.allclose(rot, -np.eye(3), atol=1e-8) for rot in ops_mats)
    if not has_inversion:
        ops_mats.append(-np.eye(3, dtype=float))

    nops = len(ops_mats)
    all_k = np.vstack([k0 @ rot.T for rot in ops_mats])
    all_e = np.tile(e0, (1, nops))
    all_k = _fold_cart_points_to_centered_cell(all_k, rec_mat)

    scale = max(1.0, float(np.max(np.linalg.norm(all_k, axis=1))))
    tol = 1e-6 * scale
    key = np.round(all_k / tol).astype(np.int64)
    _, unique_idx = np.unique(key, axis=0, return_index=True)
    unique_idx = np.sort(unique_idx)

    k_unique = all_k[unique_idx]
    e_unique = all_e[:, unique_idx]
    expanded = int(k_unique.shape[0]) > int(k0.shape[0]) + 4
    return k_unique, e_unique, expanded


def _wigner_seitz_polyhedron(rec_mat: np.ndarray) -> tuple[np.ndarray, list[np.ndarray]]:
    """Return vertices/faces for the reciprocal Wigner-Seitz cell via half-space intersection."""
    coeffs = np.array(
        [(i, j, k) for i in range(-2, 3) for j in range(-2, 3) for k in range(-2, 3) if (i, j, k) != (0, 0, 0)],
        dtype=float,
    )
    gvecs = coeffs @ rec_mat
    norms = np.linalg.norm(gvecs, axis=1)
    if norms.size == 0:
        return np.zeros((0, 3), dtype=float), []

    min_norm = float(np.min(norms))
    keep = norms <= (2.2 * min_norm + 1e-12)
    gvecs = gvecs[keep]
    norms = norms[keep]
    if gvecs.shape[0] > 60:
        idx = np.argsort(norms)[:60]
        gvecs = gvecs[idx]

    d = 0.5 * np.sum(gvecs * gvecs, axis=1)
    scale = max(1.0, float(np.max(np.linalg.norm(gvecs, axis=1))))
    tol_plane = 1e-7 * scale
    tol_vertex = 1e-6 * scale

    m = gvecs.shape[0]
    verts: list[np.ndarray] = []
    for i in range(m - 2):
        n1 = gvecs[i]
        for j in range(i + 1, m - 1):
            n2 = gvecs[j]
            for k in range(j + 1, m):
                n3 = gvecs[k]
                A = np.vstack((n1, n2, n3))
                if abs(float(np.linalg.det(A))) < 1e-10:
                    continue
                x = np.linalg.solve(A, np.array([d[i], d[j], d[k]], dtype=float))
                if not np.all(gvecs @ x <= d + tol_plane):
                    continue
                if not verts:
                    verts.append(x)
                    continue
                dv = np.linalg.norm(np.asarray(verts) - x[None, :], axis=1)
                if float(np.min(dv)) > tol_vertex:
                    verts.append(x)

    if not verts:
        return np.zeros((0, 3), dtype=float), []

    vertices = np.asarray(verts, dtype=float)
    face_tol = 2e-6 * scale
    used: set[tuple[int, ...]] = set()
    faces: list[np.ndarray] = []
    for i in range(m):
        dist = gvecs[i] @ vertices.T - d[i]
        idx = np.where(np.abs(dist) <= face_tol)[0]
        if idx.size < 3:
            continue
        key = tuple(sorted(int(ii) for ii in idx.tolist()))
        if key in used:
            continue
        pts = vertices[idx]
        n = gvecs[i]
        n_norm = float(np.linalg.norm(n))
        if n_norm < 1e-12:
            continue
        n = n / n_norm
        ref = np.array([1.0, 0.0, 0.0]) if abs(n[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
        u = np.cross(n, ref)
        u_norm = float(np.linalg.norm(u))
        if u_norm < 1e-12:
            ref = np.array([0.0, 0.0, 1.0])
            u = np.cross(n, ref)
            u_norm = float(np.linalg.norm(u))
            if u_norm < 1e-12:
                continue
        u = u / u_norm
        v = np.cross(n, u)
        c = np.mean(pts, axis=0)
        ang = np.arctan2((pts - c) @ v, (pts - c) @ u)
        poly = pts[np.argsort(ang)]
        if poly.shape[0] >= 3:
            faces.append(poly)
            used.add(key)

    return vertices, faces


def _extract_symmetry_points_cart(line_bandstructure: object, rec_mat: np.ndarray) -> dict[str, np.ndarray]:
    """Extract unique labeled symmetry points from the line-mode band path."""
    points: dict[str, np.ndarray] = {}
    for kp in getattr(line_bandstructure, "kpoints", []):
        label = getattr(kp, "label", None)
        if not label:
            continue
        clean = _clean_label(str(label))
        frac = np.asarray(getattr(kp, "frac_coords", None), dtype=float)
        if frac.shape != (3,):
            continue
        frac_fold = ((frac + 0.5) % 1.0) - 0.5
        frac_fold = np.where(np.isclose(frac_fold, -0.5, atol=1e-10), 0.5, frac_fold)
        cart = frac_fold @ rec_mat
        if clean not in points:
            points[clean] = cart
            continue
        # Prefer farther-from-origin representative so face/edge points are visible.
        if float(np.linalg.norm(cart)) > float(np.linalg.norm(points[clean])) + 1e-9:
            points[clean] = cart
    return points


def _reduce_points_to_wigner_seitz(
    points_cart: np.ndarray,
    rec_mat: np.ndarray,
    *,
    search_radius: int = 2,
    block_size: int = 2048,
) -> np.ndarray:
    """Map cartesian reciprocal points into the first Wigner-Seitz cell."""
    pts_in = np.asarray(points_cart, dtype=float)
    squeeze = False
    if pts_in.ndim == 1:
        if pts_in.shape[0] != 3:
            raise ValueError("Single k-point must have shape (3,).")
        pts = pts_in.reshape(1, 3)
        squeeze = True
    elif pts_in.ndim == 2 and pts_in.shape[1] == 3:
        pts = pts_in
    else:
        raise ValueError("k-points must have shape (N, 3) or (3,).")

    coeffs = np.array(
        [
            (i, j, k)
            for i in range(-search_radius, search_radius + 1)
            for j in range(-search_radius, search_radius + 1)
            for k in range(-search_radius, search_radius + 1)
        ],
        dtype=float,
    )
    shifts = coeffs @ np.asarray(rec_mat, dtype=float)

    out = np.empty_like(pts)
    npts = int(pts.shape[0])
    for i0 in range(0, npts, max(1, int(block_size))):
        block = pts[i0 : i0 + int(block_size)]
        candidates = block[:, None, :] - shifts[None, :, :]
        dist2 = np.einsum("bij,bij->bi", candidates, candidates)
        best = np.argmin(dist2, axis=1)
        out[i0 : i0 + block.shape[0]] = candidates[np.arange(block.shape[0]), best]

    if squeeze:
        return out[0]
    return out


def _reference_index_in_window(distance: np.ndarray, xlo: float, xhi: float) -> int:
    """Pick a deterministic index near the center of the visible x-window."""
    xmid = 0.5 * (float(xlo) + float(xhi))
    visible = np.where((distance >= xlo - 1e-12) & (distance <= xhi + 1e-12))[0]
    if visible.size:
        return int(visible[np.argmin(np.abs(distance[visible] - xmid))])
    return int(np.argmin(np.abs(distance - xmid)))


def build_cv_label_map(
    band_indices: list[int],
    energies: np.ndarray,
    distance: np.ndarray,
    xlo: float,
    xhi: float,
    *,
    explicit_base_map: dict[int, str] | None = None,
) -> dict[int, str]:
    """Build labels like v3/c5 for the active window.

    Classification rule (metal-friendly):
    - `vN`: band is strictly below EF across the visible window.
    - `cN`: band touches/crosses/exists above EF anywhere in the visible window.

    This avoids tagging EF-crossing bands as valence just because a single
    reference k-point happened to be below EF.
    """
    labels: dict[int, str] = {}
    if explicit_base_map:
        for k, v in explicit_base_map.items():
            labels[int(k)] = str(v)

    unresolved = [int(b) for b in band_indices if int(b) not in labels]
    if not unresolved:
        return labels

    visible = np.where((distance >= xlo - 1e-12) & (distance <= xhi + 1e-12))[0]
    if visible.size == 0:
        visible = np.arange(distance.size, dtype=int)

    iref = _reference_index_in_window(distance, xlo, xhi)
    e_ref = {b: float(energies[b, iref]) for b in unresolved}
    e_win = {b: np.asarray(energies[b, visible], dtype=float) for b in unresolved}

    # Valence-only bands stay below EF everywhere in the visible window.
    valence = sorted(
        [b for b in unresolved if np.any(e_win[b] < 0.0) and not np.any(e_win[b] >= 0.0)],
        key=lambda b: float(np.max(e_win[b][e_win[b] < 0.0])) if np.any(e_win[b] < 0.0) else e_ref[b],
        reverse=True,
    )

    # Conduction includes bands touching/crossing/above EF in the visible window.
    conduction = sorted(
        [b for b in unresolved if b not in valence],
        key=lambda b: float(np.min(e_win[b][e_win[b] >= 0.0])) if np.any(e_win[b] >= 0.0) else e_ref[b],
    )

    for i, b in enumerate(valence, start=1):
        labels[b] = f"v{i}"
    for i, b in enumerate(conduction, start=1):
        labels[b] = f"c{i}"
    return labels


class MPFetchWorker(QObject):
    finished = pyqtSignal(object, object, str)
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
                    line_bandstructure = mpr.get_bandstructure_by_material_id(
                        material_id=self.material_id, line_mode=True
                    )
                except TypeError:
                    line_bandstructure = mpr.get_bandstructure_by_material_id(self.material_id)

                # Uniform-k data for 3D BZ plotting is optional. Keep line-mode flow alive even if this fails.
                uniform_bandstructure = None
                try:
                    uniform_bandstructure = mpr.get_bandstructure_by_material_id(
                        material_id=self.material_id, line_mode=False
                    )
                except Exception:
                    uniform_bandstructure = None

            self.finished.emit(line_bandstructure, uniform_bandstructure, self.material_id)
        except Exception as exc:
            self.error.emit(str(exc))


class AuBandGUI(QMainWindow):
    HW_SCALE = 1000

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Au Band Structure Explorer (Materials Project)")
        self.resize(1500, 900)

        self.band_data: BandData | None = None
        self.uniform_band_data: UniformBandData | None = None
        self.fetch_thread: QThread | None = None
        self.fetch_worker: MPFetchWorker | None = None
        self._updating_controls = False
        # Optional manual overrides:
        # - base c/v notation (e.g. {12: "v3", 15: "c5"})
        # - selector-only orbital notation text (e.g. {12: "d", 15: "sp"})
        self.cv_label_overrides: dict[int, str] = {}
        self.selector_orbital_overrides: dict[int, str] = {}
        # Backward-compatible alias for older experiments/scripts.
        self.rosei_label_overrides = self.selector_orbital_overrides
        self.transition_candidates: list[TransitionCandidate] = []
        self.transition_visible_candidates: list[TransitionCandidate] = []
        self.transition_candidate_map: dict[tuple[int, int], TransitionCandidate] = {}
        self.selected_transition_keys: list[tuple[int, int]] = []
        self.transition_cv_map: dict[int, str] = {}
        self.transition_pick_keys: list[tuple[int, int]] = []
        self.transition_scatter: PathCollection | None = None
        self._updating_transition_choice = False
        self.main_diff_bands: list[int] = []
        self.main_line_to_band: dict[int, int] = {}
        self.aggregate_diff_curve: np.ndarray | None = None
        self.aggregate_active_pairs: int = 0
        self._bz_axis = None
        self._bz_needs_refresh = True
        self._bz_ws_vertices = np.zeros((0, 3), dtype=float)
        self._bz_ws_faces: list[np.ndarray] = []
        self._bz_k_cart_ws = np.zeros((0, 3), dtype=float)
        self._bz_rec_mat = np.eye(3, dtype=float)
        self._bz_sym_points: dict[str, np.ndarray] = {}
        self._ceds_pair_cache: dict[tuple[int, int], tuple[np.ndarray, np.ndarray]] = {}

        self._build_ui()
        self._connect_signals()
        self._draw_placeholder(self.figure, self.canvas, "Load a material band structure to begin.")
        self._draw_placeholder(
            self.figure_transition,
            self.canvas_transition,
            "Load a material band structure to populate transition picks.",
        )
        self._draw_placeholder(
            self.figure_bz,
            self.canvas_bz,
            "Load a material band structure to populate 3D CEDS.",
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
        self.diff_pair_label = QLabel("DeltaE source: click 2 bands on plot (or select exactly 2 in list)")
        self.diff_pair_label.setWordWrap(True)
        self.hbar_slider = QSlider(Qt.Orientation.Horizontal)
        self.hbar_slider.setTracking(True)
        self.hbar_spin = QDoubleSpinBox()
        self.hbar_spin.setDecimals(3)
        self.hbar_spin.setSingleStep(0.01)
        self.hbar_spin.setMinimum(0.0)
        self.hbar_spin.setSuffix(" eV")
        self.ceds_tol_spin = QDoubleSpinBox()
        self.ceds_tol_spin.setDecimals(3)
        self.ceds_tol_spin.setSingleStep(0.005)
        self.ceds_tol_spin.setMinimum(0.0)
        self.ceds_tol_spin.setMaximum(1.0)
        self.ceds_tol_spin.setValue(0.03)
        self.ceds_tol_spin.setSuffix(" eV")
        self.ceds_points_spin = QSpinBox()
        self.ceds_points_spin.setRange(50, 50000)
        self.ceds_points_spin.setSingleStep(250)
        self.ceds_points_spin.setValue(2000)
        self.ceds_surface_checkbox = QCheckBox("Approximate surface mesh (slow)")
        self.ceds_surface_checkbox.setChecked(False)
        self.shade_diff_checkbox = QCheckBox("Shade region where |dE| <= hbar omega")
        self.shade_diff_checkbox.setChecked(True)
        diff_form.addRow("DeltaE pair", self.diff_pair_label)
        diff_form.addRow("hbar omega", self.hbar_slider)
        diff_form.addRow("hbar omega (exact)", self.hbar_spin)
        diff_form.addRow("CEDS tolerance", self.ceds_tol_spin)
        diff_form.addRow("CEDS max points", self.ceds_points_spin)
        diff_form.addRow(self.ceds_surface_checkbox)
        diff_form.addRow(self.shade_diff_checkbox)
        controls_layout.addWidget(diff_group)

        transition_group = QGroupBox("Transition Picker")
        transition_form = QFormLayout(transition_group)
        self.transition_max_pairs_slider = QSlider(Qt.Orientation.Horizontal)
        self.transition_max_pairs_slider.setRange(1, 10)
        self.transition_max_pairs_slider.setSingleStep(1)
        self.transition_max_pairs_slider.setPageStep(1)
        self.transition_max_pairs_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.transition_max_pairs_slider.setTickInterval(1)
        self.transition_max_pairs_slider.setValue(10)
        self.transition_max_pairs_value_label = QLabel("10")
        self.transition_max_pairs_value_label.setMinimumWidth(24)
        self.transition_max_pairs_value_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        transition_max_pairs_row = QWidget()
        transition_max_pairs_layout = QHBoxLayout(transition_max_pairs_row)
        transition_max_pairs_layout.setContentsMargins(0, 0, 0, 0)
        transition_max_pairs_layout.addWidget(self.transition_max_pairs_slider, 1)
        transition_max_pairs_layout.addWidget(self.transition_max_pairs_value_label)
        self.ceds_transition_combo = QComboBox()
        self.ceds_transition_combo.setSizeAdjustPolicy(
            QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon
        )
        transition_form.addRow("Visible onset points", transition_max_pairs_row)
        transition_form.addRow("CEDS transition", self.ceds_transition_combo)
        controls_layout.addWidget(transition_group)
        controls_layout.addStretch(1)

        splitter.addWidget(controls_scroll)

        plot_panel = QWidget()
        plot_layout = QVBoxLayout(plot_panel)
        plot_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_tabs = QTabWidget()
        self.figure = Figure(figsize=(9.0, 7.0))
        self.canvas = FigureCanvas(self.figure)
        # Use constrained layout for transition tabs so titles/labels adapt to the tab size.
        self.figure_transition = Figure(figsize=(9.0, 7.0), layout="constrained")
        self.canvas_transition = FigureCanvas(self.figure_transition)
        self.figure_bz = Figure(figsize=(9.0, 7.0), layout="constrained")
        self.canvas_bz = FigureCanvas(self.figure_bz)
        self.plot_tabs.addTab(self.canvas, "Band Explorer")
        self.plot_tabs.addTab(self.canvas_transition, "Transition Picker")
        self.plot_tabs.addTab(self.canvas_bz, "3D CEDS")
        plot_layout.addWidget(self.plot_tabs, 1)

        view_row = QWidget()
        view_row_layout = QHBoxLayout(view_row)
        view_row_layout.setContentsMargins(2, 0, 2, 0)
        view_row_layout.addWidget(QLabel("3D Elevation"))
        self.bz_elev_slider = QSlider(Qt.Orientation.Horizontal)
        self.bz_elev_slider.setRange(-90, 90)
        self.bz_elev_slider.setValue(22)
        self.bz_elev_value = QLabel("22 deg")
        self.bz_elev_value.setMinimumWidth(40)
        self.bz_elev_value.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        view_row_layout.addWidget(self.bz_elev_slider, 1)
        view_row_layout.addWidget(self.bz_elev_value)
        view_row_layout.addSpacing(12)
        view_row_layout.addWidget(QLabel("Azimuth"))
        self.bz_azim_slider = QSlider(Qt.Orientation.Horizontal)
        self.bz_azim_slider.setRange(-180, 180)
        self.bz_azim_slider.setValue(35)
        self.bz_azim_value = QLabel("35 deg")
        self.bz_azim_value.setMinimumWidth(44)
        self.bz_azim_value.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        view_row_layout.addWidget(self.bz_azim_slider, 1)
        view_row_layout.addWidget(self.bz_azim_value)
        plot_layout.addWidget(view_row)
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

        self.hbar_slider.valueChanged.connect(self.on_hbar_slider_changed)
        self.hbar_spin.valueChanged.connect(self.on_hbar_spin_changed)
        self.ceds_tol_spin.valueChanged.connect(self.redraw)
        self.ceds_points_spin.valueChanged.connect(self.redraw)
        self.ceds_surface_checkbox.toggled.connect(self.redraw)
        self.shade_diff_checkbox.toggled.connect(self.redraw)
        self.transition_max_pairs_slider.valueChanged.connect(self.on_transition_max_pairs_changed)
        self.ceds_transition_combo.currentIndexChanged.connect(self.on_ceds_transition_choice_changed)
        self.bz_elev_slider.valueChanged.connect(self.on_bz_view_changed)
        self.bz_azim_slider.valueChanged.connect(self.on_bz_view_changed)
        self.plot_tabs.currentChanged.connect(self.on_plot_tab_changed)
        self.canvas.mpl_connect("pick_event", self.on_main_band_pick)
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

    def on_load_success(
        self, line_bandstructure: object, uniform_bandstructure: object | None, material_id: str
    ) -> None:
        try:
            self.band_data = parse_band_data(material_id, line_bandstructure)
            self.uniform_band_data = None
            uniform_note = " | 3D BZ: unavailable"
            if uniform_bandstructure is not None:
                try:
                    self.uniform_band_data = parse_uniform_band_data(material_id, uniform_bandstructure)
                    uniform_note = f" | 3D k-mesh: {self.uniform_band_data.nkpoints} points"
                except Exception:
                    self.uniform_band_data = None
                    uniform_note = " | 3D BZ: parse failed"
            self._prepare_bz_geometry_cache()
            if not self.band_data.label_order:
                self._show_error("No labeled high-symmetry points found in this band structure.")
                return
            self.populate_controls_after_load()
            self.status_label.setText(
                f"Loaded {material_id} | bands: {self.band_data.nbands} | spin: {self.band_data.spin_channel}"
                f"{uniform_note}"
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

            self.main_diff_bands = []
            self.main_line_to_band = {}
            self.aggregate_diff_curve = None
            self.aggregate_active_pairs = 0
            self._rebuild_aggregate_cache()
            self.update_hbar_range()
            self.update_focus_enabled_state()
            self.selected_transition_keys.clear()
            self.transition_candidates = []
            self.transition_visible_candidates = []
            self.transition_candidate_map = {}
            self.transition_cv_map = {}
            self.transition_pick_keys = []
            self.transition_scatter = None
            self.ceds_transition_combo.clear()
            self._ceds_pair_cache = {}
            self._bz_axis = None
            self._bz_needs_refresh = True
            self._bz_k_cart_ws = np.zeros((0, 3), dtype=float)
            self._bz_rec_mat = np.eye(3, dtype=float)
            self._refresh_band_choice_labels()
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

    def selected_diff_pair(self) -> tuple[int, int] | None:
        """Return active DeltaE pair: preferred from main-plot picks, fallback to list."""
        self._prune_main_diff_bands()
        if len(self.main_diff_bands) == 2:
            return int(self.main_diff_bands[0]), int(self.main_diff_bands[1])
        sel = self.selected_bands()
        if len(sel) != 2:
            return None
        return int(sel[0]), int(sel[1])

    def _prune_main_diff_bands(self, selected: list[int] | None = None) -> None:
        """Keep at most two unique picked bands that are still selected in the list."""
        if selected is None:
            selected = self.selected_bands()
        selected_set = {int(i) for i in selected}

        keep: list[int] = []
        seen: set[int] = set()
        for b in self.main_diff_bands:
            bi = int(b)
            if bi in selected_set and bi not in seen:
                keep.append(bi)
                seen.add(bi)
        self.main_diff_bands = keep[-2:]

    def _pair_diff_curve(self, a: int, b: int) -> np.ndarray:
        assert self.band_data is not None
        ea = self.band_data.energies[int(a), :]
        eb = self.band_data.energies[int(b), :]
        cross = ((ea < 0.0) & (eb > 0.0)) | ((ea > 0.0) & (eb < 0.0))
        return np.abs(ea - eb) * cross.astype(float)

    def update_hbar_range(self) -> None:
        if self.band_data is None:
            return
        pair_hmax = 0.05
        pair = self.selected_diff_pair()
        if pair is not None:
            diff_curve = self._pair_diff_curve(*pair)
            pair_hmax = max(0.05, float(np.max(diff_curve)))
        hmax = pair_hmax * 1.05

        current = self.hbar_spin.value()
        if current <= 1e-12:
            # Keep initial value close to single-pair scale while allowing a larger max.
            current = 0.4 * pair_hmax
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

    def on_transition_max_pairs_changed(self, value: int) -> None:
        self.transition_max_pairs_value_label.setText(str(int(value)))
        if self._updating_controls:
            return
        self.redraw()

    def on_ceds_transition_choice_changed(self) -> None:
        if self._updating_controls or self._updating_transition_choice:
            return
        data = self.ceds_transition_combo.currentData()
        key: tuple[int, int] | None = None
        if data is not None:
            try:
                key = (int(data[0]), int(data[1]))
            except Exception:
                key = None
        self.selected_transition_keys = [key] if key is not None else []
        self.redraw()

    def on_bz_view_changed(self) -> None:
        self.bz_elev_value.setText(f"{int(self.bz_elev_slider.value())} deg")
        self.bz_azim_value.setText(f"{int(self.bz_azim_slider.value())} deg")
        if self._updating_controls:
            return
        if self._bz_axis is not None and self._bz_axis in self.figure_bz.axes:
            self._bz_axis.view_init(
                elev=float(self.bz_elev_slider.value()),
                azim=float(self.bz_azim_slider.value()),
            )
            self.canvas_bz.draw_idle()
            return
        if self.band_data is not None and self.plot_tabs.currentWidget() is self.canvas_bz:
            self._draw_bz_3d()

    def on_plot_tab_changed(self, _: int) -> None:
        if self.plot_tabs.currentWidget() is not self.canvas_bz:
            return
        if self.band_data is None:
            return
        if self._bz_axis is None or self._bz_needs_refresh:
            self._draw_bz_3d()
            return
        self.on_bz_view_changed()

    def on_main_band_pick(self, event) -> None:
        if self.band_data is None:
            return
        artist = getattr(event, "artist", None)
        if artist is None:
            return
        band_idx = self.main_line_to_band.get(id(artist))
        if band_idx is None:
            return
        bi = int(band_idx)
        if bi in self.main_diff_bands:
            self.main_diff_bands = [b for b in self.main_diff_bands if int(b) != bi]
        else:
            self.main_diff_bands.append(bi)
            if len(self.main_diff_bands) > 2:
                self.main_diff_bands = self.main_diff_bands[-2:]
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
            self.selected_transition_keys = []
        else:
            self.selected_transition_keys = [key]
        self.redraw()

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

    def _band_label_context(self, xlo: float, xhi: float, x0: float | None) -> dict[int, str]:
        """Build cN/vN labels for the active k-window."""
        assert self.band_data is not None
        d = self.band_data
        cv_map = build_cv_label_map(
            list(range(int(d.nbands))),
            d.energies,
            d.distance,
            xlo,
            xhi,
            explicit_base_map=self.cv_label_overrides,
        )
        return cv_map

    def _dual_band_label(self, band_idx: int, *, cv_map: dict[int, str], selector_label: bool = False) -> str:
        base_label = cv_map.get(int(band_idx), f"b{int(band_idx)}")
        if not selector_label:
            return base_label

        extra = self.selector_orbital_overrides.get(int(band_idx))
        if extra is None:
            return base_label
        extra_clean = str(extra).strip()
        if not extra_clean:
            return base_label
        return f"{base_label} | {extra_clean}"

    def _refresh_band_choice_labels(self) -> None:
        """Update list labels and DeltaE pair status text."""
        if self.band_data is None:
            return

        d = self.band_data
        xlo, xhi, x0 = self._current_x_window()
        cv_map = self._band_label_context(xlo, xhi, x0)

        self.band_list.blockSignals(True)
        try:
            for i in range(d.nbands):
                dual = self._dual_band_label(i, cv_map=cv_map, selector_label=True)
                ui_text = f"band {i} : {dual}"
                if i < self.band_list.count():
                    self.band_list.item(i).setText(ui_text)
        finally:
            self.band_list.blockSignals(False)

        self._prune_main_diff_bands()
        if len(self.main_diff_bands) == 2:
            a, b = int(self.main_diff_bands[0]), int(self.main_diff_bands[1])
            a_text = self._dual_band_label(a, cv_map=cv_map, selector_label=True)
            b_text = self._dual_band_label(b, cv_map=cv_map, selector_label=True)
            self.diff_pair_label.setText(f"DeltaE source: plot picks {a_text} vs {b_text}")
        elif len(self.main_diff_bands) == 1:
            a = int(self.main_diff_bands[0])
            a_text = self._dual_band_label(a, cv_map=cv_map, selector_label=True)
            self.diff_pair_label.setText(f"DeltaE source: picked {a_text}; click one more band on plot")
        else:
            pair = self.selected_diff_pair()
            if pair is None:
                self.diff_pair_label.setText("DeltaE source: click 2 bands on plot (or select exactly 2 in list)")
            else:
                a, b = pair
                a_text = self._dual_band_label(a, cv_map=cv_map, selector_label=True)
                b_text = self._dual_band_label(b, cv_map=cv_map, selector_label=True)
                self.diff_pair_label.setText(f"DeltaE source: {a_text} vs {b_text}")

    def _set_combo_to_data(self, combo: QComboBox, data: tuple[int, int] | None) -> None:
        if data is None:
            combo.setCurrentIndex(0)
            return
        for i in range(combo.count()):
            if combo.itemData(i) == data:
                combo.setCurrentIndex(i)
                return
        combo.setCurrentIndex(0)

    def _refresh_ceds_transition_combos(
        self, visible: list[TransitionCandidate], transition_cv_map: dict[int, str]
    ) -> None:
        if self.band_data is None:
            return
        self.transition_cv_map = dict(transition_cv_map)
        d = self.band_data
        visible_keys = [t.key for t in visible]
        self.selected_transition_keys = [k for k in self.selected_transition_keys if k in visible_keys][:1]
        if not self.selected_transition_keys and visible:
            self.selected_transition_keys = [visible[0].key]

        selected = self.selected_transition_keys[0] if self.selected_transition_keys else None

        self._updating_transition_choice = True
        try:
            self.ceds_transition_combo.blockSignals(True)
            self.ceds_transition_combo.clear()
            self.ceds_transition_combo.addItem("None", None)

            for t in visible:
                kx = float(d.distance[int(t.k_index)])
                v_lbl = transition_cv_map.get(int(t.v), f"b{int(t.v)}")
                c_lbl = transition_cv_map.get(int(t.c), f"b{int(t.c)}")
                text = f"{t.onset_ev:.3f} eV | {v_lbl}->{c_lbl} | k={kx:.3f}"
                key = (int(t.v), int(t.c))
                self.ceds_transition_combo.addItem(text, key)

            self._set_combo_to_data(self.ceds_transition_combo, selected)
            data = self.ceds_transition_combo.currentData()
            if data is None:
                self.selected_transition_keys = []
            else:
                self.selected_transition_keys = [(int(data[0]), int(data[1]))]
        finally:
            self.ceds_transition_combo.blockSignals(False)
            self._updating_transition_choice = False

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

    def _rebuild_aggregate_cache(self) -> None:
        """Cache sum_k curve for all band pairs weighted by opposite-EF occupancy."""
        if self.band_data is None:
            self.aggregate_diff_curve = None
            self.aggregate_active_pairs = 0
            return

        d = self.band_data
        energies = d.energies
        nbands, nk = energies.shape
        agg = np.zeros(nk, dtype=float)
        active_pairs = 0
        for i in range(max(0, nbands - 1)):
            ei = energies[i, :]
            for j in range(i + 1, nbands):
                ej = energies[j, :]
                cross = ((ei < 0.0) & (ej > 0.0)) | ((ei > 0.0) & (ej < 0.0))
                if not np.any(cross):
                    continue
                active_pairs += 1
                agg += np.abs(ei - ej) * cross.astype(float)

        self.aggregate_diff_curve = agg
        self.aggregate_active_pairs = active_pairs

    def _aggregate_curve(self) -> np.ndarray:
        if self.aggregate_diff_curve is None:
            self._rebuild_aggregate_cache()
        if self.aggregate_diff_curve is None:
            return np.zeros(0, dtype=float)
        return self.aggregate_diff_curve

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
            self._draw_placeholder(
                self.figure_bz,
                self.canvas_bz,
                "Load a material band structure to populate 3D CEDS.",
            )
            self._bz_axis = None
            self._bz_needs_refresh = True
            return
        self._refresh_band_choice_labels()
        self.update_hbar_range()
        self._draw_band_explorer()
        self._draw_transition_picker()
        self._bz_needs_refresh = True
        if self.plot_tabs.currentWidget() is self.canvas_bz:
            self._draw_bz_3d()

    def _draw_band_explorer(self) -> None:
        assert self.band_data is not None
        d = self.band_data
        selected = self.selected_bands()
        self.main_line_to_band = {}
        self._prune_main_diff_bands(selected)
        picked_set = {int(b) for b in self.main_diff_bands}
        xlo, xhi, x0, mask = self._x_window_mask()

        self.figure.clear()
        gs = self.figure.add_gridspec(2, 1, height_ratios=[3.3, 1.7], hspace=0.08)
        ax_band = self.figure.add_subplot(gs[0, 0])
        ax_diff = self.figure.add_subplot(gs[1, 0], sharex=ax_band)

        if selected:
            cmap = colormaps.get_cmap("tab10")
            cv_label_map = self._band_label_context(xlo, xhi, x0)
            for j, band_idx in enumerate(selected):
                color = cmap(j % 10)
                dual_label = self._dual_band_label(int(band_idx), cv_map=cv_label_map)
                is_highlight = int(band_idx) in picked_set
                if not picked_set:
                    line_alpha = 0.92
                    line_lw = 1.35
                else:
                    line_alpha = 0.98 if is_highlight else 0.30
                    line_lw = 2.9 if is_highlight else 1.0
                first_segment = True
                for branch in d.bandstructure.branches:
                    i0 = int(branch["start_index"])
                    i1 = int(branch["end_index"]) + 1
                    show_label = first_segment and (not picked_set or is_highlight)
                    (line,) = ax_band.plot(
                        d.distance[i0:i1],
                        d.energies[band_idx, i0:i1],
                        color=color,
                        lw=line_lw,
                        alpha=line_alpha,
                        zorder=4 if is_highlight else 2,
                        label=dual_label if show_label else None,
                        picker=5,
                    )
                    self.main_line_to_band[id(line)] = int(band_idx)
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

            show_band_legend = self.show_legend_checkbox.isChecked() and (
                bool(picked_set) or len(selected) <= 12
            )
            if show_band_legend:
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

        hw = float(self.hbar_spin.value())
        pair = self.selected_diff_pair()
        pair_map = self._band_label_context(xlo, xhi, x0)
        x_vis = d.distance[mask]

        if pair is None:
            ax_diff.text(
                0.5,
                0.5,
                "Click 2 selected bands on the plot (or select exactly 2 in Band Selection).",
                ha="center",
                va="center",
                transform=ax_diff.transAxes,
            )
            ax_diff.axhline(hw, color="black", lw=0.95, ls=":", alpha=0.85, label=f"hbar omega = {hw:.3f} eV")
            ytop = max(0.05, hw)
        else:
            a, b = pair
            diff_curve = self._pair_diff_curve(a, b)
            diff_vis = diff_curve[mask]
            a_dual = self._dual_band_label(a, cv_map=pair_map)
            b_dual = self._dual_band_label(b, cv_map=pair_map)

            ax_diff.plot(
                x_vis,
                diff_vis,
                color="tab:red",
                lw=1.5,
                label=f"|{a_dual} - {b_dual}| * I(opposite EF side)",
            )
            ax_diff.fill_between(x_vis, 0.0, diff_vis, color="0.92", alpha=0.8, zorder=-3)

            if self.shade_diff_checkbox.isChecked():
                region_mask = diff_vis <= hw
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

        xlo, xhi, x0 = d.xmin, d.xmax, None
        mask = np.ones_like(d.distance, dtype=bool)

        candidates = self._compute_transition_candidates(mask)
        self.transition_candidates = candidates
        self.transition_visible_candidates = []
        self.transition_candidate_map = {t.key: t for t in candidates}
        self.selected_transition_keys = [k for k in self.selected_transition_keys if k in self.transition_candidate_map][
            :1
        ]

        self.figure_transition.clear()
        if not candidates:
            self.transition_pick_keys = []
            self.transition_scatter = None
            self.transition_cv_map = {}
            self._draw_placeholder(
                self.figure_transition,
                self.canvas_transition,
                "No interband onset transitions found on the full k-path.",
            )
            self._refresh_ceds_transition_combos([], {})
            return

        max_pairs = int(self.transition_max_pairs_slider.value())
        visible = candidates[: max_pairs]
        self.transition_visible_candidates = visible
        visible_key_set = {t.key for t in visible}
        # Keep selected transition markers aligned with visible onset points.
        self.selected_transition_keys = [k for k in self.selected_transition_keys if k in visible_key_set][:1]
        self.transition_pick_keys = [t.key for t in visible]

        # Build a stable cN/vN naming map for bands participating in visible transitions.
        transition_cv_map = build_cv_label_map(
            list(range(int(d.nbands))),
            d.energies,
            d.distance,
            xlo,
            xhi,
            explicit_base_map=self.cv_label_overrides,
        )
        self.transition_cv_map = transition_cv_map

        def _transition_dual_label(band_idx: int, x_for_point: float) -> str:
            _ = x_for_point  # kept for signature compatibility with existing calls
            return transition_cv_map.get(int(band_idx), f"b{band_idx}")

        self._refresh_ceds_transition_combos(visible, transition_cv_map)

        gs = self.figure_transition.add_gridspec(2, 1, height_ratios=[1.25, 2.25])
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
        onset_tick_labels = [
            f"{_transition_dual_label(t.v, d.distance[t.k_index])} -> {_transition_dual_label(t.c, d.distance[t.k_index])}"
            for t in visible
        ]
        ax_onset.set_yticklabels(onset_tick_labels, fontsize=8)
        ax_onset.invert_yaxis()
        ax_onset.grid(axis="x", alpha=0.25)
        ax_onset.set_xlabel("Onset hbar omega (eV)")
        ax_onset.set_title(
            "Clickable onset map (click one point to choose CEDS transition)",
            fontsize=10,
            pad=8,
        )

        visible_bands = sorted({int(t.v) for t in visible} | {int(t.c) for t in visible})
        for band_idx in visible_bands:
            ax_pick.plot(d.distance, d.energies[band_idx, :], color="0.86", lw=0.8, zorder=0)

        color_cycle = colormaps.get_cmap("tab10")
        selected_candidates = [t for t in visible if t.key in selected_set]
        nsel = len(selected_candidates)
        xspan = d.xmax - d.xmin
        for i, t in enumerate(selected_candidates):
            color = color_cycle(i % 10)
            t_v = _transition_dual_label(t.v, d.distance[t.k_index])
            t_c = _transition_dual_label(t.c, d.distance[t.k_index])
            ax_pick.plot(
                d.distance,
                d.energies[t.v, :],
                color=color,
                lw=1.7,
                ls="--",
                alpha=0.9,
                label=f"T{i + 1}: {t_v} -> {t_c}",
            )
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
            "Selected transition branches and arrows (visible-onset bands only)\n"
            "Dashed=valence, solid=conduction; arrows at onset-k",
            fontsize=10,
            pad=8,
        )
        ax_pick.set_xticks(tick_x)
        ax_pick.set_xticklabels([tick_label_map[xi] for xi in tick_x])
        if self.show_legend_checkbox.isChecked() and selected_candidates:
            ax_pick.legend(frameon=False, fontsize=8, ncol=2, loc="best")

        self.canvas_transition.draw_idle()

    def _prepare_bz_geometry_cache(self) -> None:
        self._bz_ws_vertices = np.zeros((0, 3), dtype=float)
        self._bz_ws_faces = []
        self._bz_k_cart_ws = np.zeros((0, 3), dtype=float)
        self._bz_rec_mat = np.eye(3, dtype=float)
        self._bz_sym_points = {}
        self._ceds_pair_cache = {}

        if self.uniform_band_data is None or self.band_data is None:
            return

        d3 = self.uniform_band_data
        rec_lattice = getattr(d3.bandstructure, "lattice_rec", None)
        rec_mat = (
            np.asarray(rec_lattice.matrix, dtype=float)
            if (rec_lattice is not None and hasattr(rec_lattice, "matrix"))
            else np.eye(3, dtype=float)
        )
        self._bz_rec_mat = rec_mat
        self._bz_ws_vertices, self._bz_ws_faces = _wigner_seitz_polyhedron(rec_mat)
        self._bz_k_cart_ws = _reduce_points_to_wigner_seitz(np.asarray(d3.k_cart_plot, dtype=float), rec_mat)

        sym_raw = _extract_symmetry_points_cart(self.band_data.bandstructure, rec_mat)
        if sym_raw:
            labels = list(sym_raw.keys())
            pts = np.asarray([sym_raw[lbl] for lbl in labels], dtype=float)
            pts_ws = _reduce_points_to_wigner_seitz(pts, rec_mat)
            self._bz_sym_points = {lbl: pts_ws[i] for i, lbl in enumerate(labels)}

    def _get_ceds_pair_arrays(self, a: int, b: int) -> tuple[np.ndarray, np.ndarray]:
        assert self.uniform_band_data is not None
        key = (int(a), int(b))
        cached = self._ceds_pair_cache.get(key)
        if cached is not None:
            return cached

        ea = self.uniform_band_data.energies_plot[int(a), :]
        eb = self.uniform_band_data.energies_plot[int(b), :]
        inter_mask = ((ea < 0.0) & (eb > 0.0)) | ((ea > 0.0) & (eb < 0.0))
        delta_e = np.abs(ea - eb)
        self._ceds_pair_cache[key] = (delta_e, inter_mask)
        return delta_e, inter_mask

    def _draw_bz_3d(self) -> None:
        if self.uniform_band_data is None:
            self._draw_placeholder(
                self.figure_bz,
                self.canvas_bz,
                "Uniform-k data unavailable for this material.\n"
                "3D BZ view requires MP band structure with line_mode=False.",
            )
            return
        if self.band_data is None:
            self._draw_placeholder(self.figure_bz, self.canvas_bz, "Load a material band structure to begin.")
            return

        d3 = self.uniform_band_data
        if not self.transition_visible_candidates:
            self._draw_placeholder(
                self.figure_bz,
                self.canvas_bz,
                "No onset entries available.\n"
                "Increase Visible onset points in Transition Picker.",
            )
            return

        if not self.transition_cv_map:
            self.transition_cv_map = build_cv_label_map(
                list(range(int(self.band_data.nbands))),
                self.band_data.energies,
                self.band_data.distance,
                self.band_data.xmin,
                self.band_data.xmax,
                explicit_base_map=self.cv_label_overrides,
            )

        visible_map = {t.key: t for t in self.transition_visible_candidates}
        selected_keys = [k for k in self.selected_transition_keys if k in visible_map][:1]
        if not selected_keys:
            selected_keys = [self.transition_visible_candidates[0].key]
            self.selected_transition_keys = selected_keys[:]
            self._refresh_ceds_transition_combos(self.transition_visible_candidates, self.transition_cv_map)

        if not selected_keys or selected_keys[0] not in visible_map:
            self._draw_placeholder(
                self.figure_bz,
                self.canvas_bz,
                "Choose one transition from the onset list for 3D CEDS.",
            )
            return
        t = visible_map[selected_keys[0]]

        if (not self._bz_ws_faces) and (not self._bz_sym_points):
            self._prepare_bz_geometry_cache()
        kxyz = np.asarray(self._bz_k_cart_ws, dtype=float)
        if kxyz.ndim != 2 or kxyz.shape[1] != 3 or kxyz.shape[0] == 0:
            # Fallback if cache was not prepared for any reason.
            kxyz = _reduce_points_to_wigner_seitz(np.asarray(d3.k_cart_plot, dtype=float), self._bz_rec_mat)
        if kxyz.ndim != 2 or kxyz.shape[1] != 3 or kxyz.shape[0] == 0:
            self._draw_placeholder(self.figure_bz, self.canvas_bz, "Invalid 3D k-mesh data.")
            return

        ws_vertices = self._bz_ws_vertices
        ws_faces = self._bz_ws_faces
        sym_points = self._bz_sym_points

        self.figure_bz.clear()
        ax = self.figure_bz.add_subplot(1, 1, 1, projection="3d")
        self._bz_axis = ax

        hw = float(self.hbar_spin.value())
        tol_user = float(self.ceds_tol_spin.value())
        max_points = int(self.ceds_points_spin.value())
        use_surface = self.ceds_surface_checkbox.isChecked()

        a = int(t.v)
        b = int(t.c)
        delta_e, inter_mask = self._get_ceds_pair_arrays(a, b)
        mismatch = np.abs(delta_e - hw)
        idx_valid = np.where(inter_mask)[0]
        idx = np.zeros(0, dtype=int)

        if idx_valid.size > 0:
            if tol_user > 0.0:
                keep = inter_mask & (mismatch <= tol_user)
                idx = np.where(keep)[0]
            else:
                # Exact isosurface condition. On a discrete mesh this is typically empty.
                idx = np.where(inter_mask & np.isclose(mismatch, 0.0, atol=1e-12))[0]

            if idx.size > max_points:
                local = np.argpartition(mismatch[idx], max_points - 1)[:max_points]
                idx = idx[local]

        a_lbl = self.transition_cv_map.get(a, f"b{a}")
        b_lbl = self.transition_cv_map.get(b, f"b{b}")
        if idx.size > 0:
            color = "tab:orange"
            ax.scatter(
                kxyz[idx, 0],
                kxyz[idx, 1],
                kxyz[idx, 2],
                c=color,
                s=8,
                alpha=0.62,
                linewidths=0.0,
                depthshade=False,
                label=f"{a_lbl}->{b_lbl} (onset {float(t.onset_ev):.3f} eV)",
            )
            if use_surface and idx.size >= 120:
                try:
                    ax.plot_trisurf(
                        kxyz[idx, 0],
                        kxyz[idx, 1],
                        kxyz[idx, 2],
                        color=color,
                        alpha=0.12,
                        linewidth=0.05,
                        antialiased=True,
                        shade=False,
                    )
                except Exception:
                    pass

        onset_pt = None
        try:
            kp = self.band_data.bandstructure.kpoints[int(t.k_index)]
            frac = np.asarray(getattr(kp, "frac_coords", None), dtype=float)
            if frac.shape == (3,):
                onset_cart = frac @ self._bz_rec_mat
                onset_pt = _reduce_points_to_wigner_seitz(onset_cart, self._bz_rec_mat)
        except Exception:
            onset_pt = None
        if onset_pt is not None:
            ax.scatter(
                [float(onset_pt[0])],
                [float(onset_pt[1])],
                [float(onset_pt[2])],
                c="crimson",
                marker="*",
                s=105,
                depthshade=False,
                zorder=8,
                label="Onset k (path)",
            )

        if ws_faces:
            ws_poly = Poly3DCollection(
                ws_faces,
                facecolors=(0.62, 0.70, 0.86, 0.08),
                edgecolors=(0.23, 0.31, 0.49, 0.78),
                linewidths=1.0,
                zorder=2,
            )
            ax.add_collection3d(ws_poly)

        if sym_points:
            preferred = ["G", "X", "L", "W", "K", "U"]
            labels = preferred + sorted([k for k in sym_points if k not in preferred])
            for lbl in labels:
                if lbl not in sym_points:
                    continue
                pt = np.asarray(sym_points[lbl], dtype=float)
                ax.scatter(
                    [pt[0]],
                    [pt[1]],
                    [pt[2]],
                    c="black",
                    s=28,
                    marker="o",
                    depthshade=False,
                    zorder=6,
                )

        cloud = [kxyz]
        if ws_vertices.size:
            cloud.append(ws_vertices)
        if sym_points:
            cloud.append(np.asarray(list(sym_points.values()), dtype=float))
        all_pts = np.vstack(cloud)
        mins = np.min(all_pts, axis=0)
        maxs = np.max(all_pts, axis=0)
        center = 0.5 * (mins + maxs)
        half = 0.5 * float(np.max(maxs - mins)) * 1.06
        half = max(half, 1e-6)
        ax.set_xlim(center[0] - half, center[0] + half)
        ax.set_ylim(center[1] - half, center[1] + half)
        ax.set_zlim(center[2] - half, center[2] + half)
        ax.set_box_aspect((1, 1, 1))

        ax.set_xlabel(fr"$k_x$ ({d3.k_unit_label})")
        ax.set_ylabel(fr"$k_y$ ({d3.k_unit_label})")
        ax.set_zlabel(fr"$k_z$ ({d3.k_unit_label})")
        triad = 0.18 * half
        ax.quiver(0.0, 0.0, 0.0, triad, 0.0, 0.0, color="tab:red", arrow_length_ratio=0.12, linewidth=1.1)
        ax.quiver(0.0, 0.0, 0.0, 0.0, triad, 0.0, color="tab:green", arrow_length_ratio=0.12, linewidth=1.1)
        ax.quiver(0.0, 0.0, 0.0, 0.0, 0.0, triad, color="tab:blue", arrow_length_ratio=0.12, linewidth=1.1)
        ax.text(triad, 0.0, 0.0, "x", color="tab:red", fontsize=8)
        ax.text(0.0, triad, 0.0, "y", color="tab:green", fontsize=8)
        ax.text(0.0, 0.0, triad, "z", color="tab:blue", fontsize=8)

        if sym_points:
            text_shift = 0.028 * half
            preferred = ["G", "X", "L", "W", "K", "U"]
            labels = preferred + sorted([k for k in sym_points if k not in preferred])
            for lbl in labels:
                if lbl not in sym_points:
                    continue
                pt = np.asarray(sym_points[lbl], dtype=float)
                ax.text(
                    pt[0] + text_shift,
                    pt[1] + text_shift,
                    pt[2] + text_shift,
                    lbl,
                    color="black",
                    fontsize=8,
                    zorder=7,
                )

        if idx.size == 0:
            tol_text = "no hits"
        elif tol_user > 0.0:
            tol_text = f"tol={tol_user:.3f} eV"
        else:
            tol_text = "tol=0 (exact)"
        surface_text = "trisurf approx" if use_surface else "scatter only"
        title = (
            f"{d3.material_id}: CEDS in 3D BZ | hbar omega={hw:.3f} eV | "
            f"transition={a_lbl}->{b_lbl} | points={int(idx.size)} | max points={max_points} | "
            f"condition: |E_a-E_b-hbar omega|<=tol | {tol_text} | surface={surface_text}"
        )
        if d3.expanded_by_symmetry:
            title += " | symmetry-expanded"
        else:
            title += " | raw mesh"
        ax.set_title(title, fontsize=10, pad=10)
        ax.view_init(elev=float(self.bz_elev_slider.value()), azim=float(self.bz_azim_slider.value()))

        if idx.size == 0:
            ax.text2D(
                0.02,
                0.98,
                "No CEDS hits for selected transition at current hbar omega.\n"
                "Increase tolerance (or change hbar omega).",
                transform=ax.transAxes,
                ha="left",
                va="top",
                fontsize=9,
                color="black",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.7", alpha=0.75),
            )

        if self.show_legend_checkbox.isChecked() and idx.size > 0:
            ax.legend(frameon=False, fontsize=8, loc="upper left")

        self._bz_needs_refresh = False
        self.canvas_bz.draw_idle()

    def _draw_placeholder(self, figure: Figure, canvas: FigureCanvas, text: str) -> None:
        figure.clear()
        ax = figure.add_subplot(1, 1, 1)
        ax.text(0.5, 0.5, text, ha="center", va="center", transform=ax.transAxes)
        ax.set_axis_off()
        if figure is self.figure_bz:
            self._bz_axis = None
            self._bz_needs_refresh = False
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
