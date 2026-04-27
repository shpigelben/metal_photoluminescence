from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np

# hbar^2 / (2 m_e) in eV*Angstrom^2
HBAR2_OVER_2ME_EV_A2 = 3.80998212

# FCC high-symmetry points in reciprocal lattice units (2*pi/a).
FCC_POINTS_RLU: dict[str, np.ndarray] = {
    "G": np.array([0.0, 0.0, 0.0]),
    "X": np.array([1.0, 0.0, 0.0]),
    "W": np.array([1.0, 0.5, 0.0]),
    "L": np.array([0.5, 0.5, 0.5]),
    "K": np.array([0.75, 0.75, 0.0]),
    "U": np.array([1.0, 0.25, 0.25]),
}

L_STAR_RLU = np.array(
    [[sx * 0.5, sy * 0.5, sz * 0.5] for sx in (-1.0, 1.0) for sy in (-1.0, 1.0) for sz in (-1.0, 1.0)],
    dtype=float,
)

X_STAR_RLU = np.array(
    [
        [1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, -1.0],
    ],
    dtype=float,
)

X_STAR_AXES = X_STAR_RLU / np.linalg.norm(X_STAR_RLU, axis=1, keepdims=True)


def _canonical_label(label: str) -> str:
    clean = label.strip().upper()
    if clean in {"GAMMA", "G"}:
        return "G"
    if clean not in FCC_POINTS_RLU:
        raise KeyError(f"Unknown high-symmetry label '{label}'.")
    return clean


@dataclass(frozen=True)
class PathSample:
    labels: tuple[str, ...]
    tick_labels: tuple[str, ...]
    tick_indices: np.ndarray
    tick_s_invA: np.ndarray
    k_red: np.ndarray
    k_invA: np.ndarray
    s_invA: np.ndarray


@dataclass(frozen=True)
class QuadraticFit:
    label: str
    occurrence: int
    point_index: int
    a_evA2: float
    b_evA: float
    c_ev: float
    m_eff_over_me: float
    s0_invA: float
    s_fit_invA: np.ndarray
    e_fit_ev: np.ndarray
    s_data_invA: np.ndarray
    e_data_ev: np.ndarray


@dataclass(frozen=True)
class Quadratic1DFit:
    a_evA2: float
    b_evA: float
    c_ev: float
    m_eff_over_me: float
    x_fit_invA: np.ndarray
    e_fit_ev: np.ndarray
    x_data_invA: np.ndarray
    e_data_ev: np.ndarray


@dataclass(frozen=True)
class IsoSurfaceMesh:
    level_ev: float
    kmin: float
    kmax: float
    verts: np.ndarray
    faces: np.ndarray
    delta_min_ev: float
    delta_max_ev: float


@dataclass
class RoseiLikeGoldModel:
    """
    Minimal phenomenological Au model in FCC reciprocal coordinates (rlu = 2*pi/a).

    Bands:
    - 'v': effective valence envelope
    - 'c': effective conduction envelope
    """

    a_ang: float = 4.0782
    eg_l_ev: float = 2.45
    eg_x_ev: float = 1.94
    alpha_c_l: float = 6.0
    alpha_v_l: float = 2.5
    alpha_cx_perp: float = 5.5
    alpha_cx_para: float = 1.3
    alpha_cx_q4: float = 2.0
    alpha_vx_perp: float = 2.8
    alpha_vx_para: float = 2.0

    def energy(self, band: str, k_red: np.ndarray) -> np.ndarray:
        k = np.asarray(k_red, dtype=float)
        if k.shape[-1] != 3:
            raise ValueError("k_red must have shape (..., 3).")
        return self.energy_components(band, k[..., 0], k[..., 1], k[..., 2])

    def energy_components(self, band: str, kx: np.ndarray, ky: np.ndarray, kz: np.ndarray) -> np.ndarray:
        band_key = band.strip().lower()
        if band_key not in {"c", "v"}:
            raise ValueError(f"Unknown band '{band}'. Use 'c' or 'v'.")

        kx, ky, kz = np.broadcast_arrays(np.asarray(kx, dtype=float), np.asarray(ky, dtype=float), np.asarray(kz, dtype=float))

        ec_l = np.full_like(kx, np.inf, dtype=float)
        ev_l = np.full_like(kx, -np.inf, dtype=float)

        for x0, y0, z0 in L_STAR_RLU:
            d2 = (kx - x0) ** 2 + (ky - y0) ** 2 + (kz - z0) ** 2
            ec_l = np.minimum(ec_l, self.eg_l_ev + self.alpha_c_l * d2)
            ev_l = np.maximum(ev_l, -self.alpha_v_l * d2)

        ec_x = np.full_like(kx, np.inf, dtype=float)
        ev_x = np.full_like(kx, -np.inf, dtype=float)

        for (x0, y0, z0), (nx, ny, nz) in zip(X_STAR_RLU, X_STAR_AXES, strict=False):
            qx = kx - x0
            qy = ky - y0
            qz = kz - z0
            q_para = qx * nx + qy * ny + qz * nz
            q2 = qx * qx + qy * qy + qz * qz
            q_perp2 = np.maximum(q2 - q_para * q_para, 0.0)

            ec_i = (
                self.eg_x_ev
                + self.alpha_cx_perp * q_perp2
                - self.alpha_cx_para * q_para * q_para
                + self.alpha_cx_q4 * q_para**4
            )
            ev_i = -self.alpha_vx_perp * q_perp2 - self.alpha_vx_para * q_para * q_para

            ec_x = np.minimum(ec_x, ec_i)
            ev_x = np.maximum(ev_x, ev_i)

        ec = np.minimum(ec_l, ec_x)
        ev = np.maximum(ev_l, ev_x)
        return ec if band_key == "c" else ev

    def delta(self, upper_band: str, lower_band: str, k_red: np.ndarray) -> np.ndarray:
        return self.energy(upper_band, k_red) - self.energy(lower_band, k_red)

    def delta_components(
        self,
        upper_band: str,
        lower_band: str,
        kx: np.ndarray,
        ky: np.ndarray,
        kz: np.ndarray,
    ) -> np.ndarray:
        return self.energy_components(upper_band, kx, ky, kz) - self.energy_components(lower_band, kx, ky, kz)


def build_fcc_path(
    labels: Sequence[str] = ("G", "X", "W", "L", "G"),
    points_per_segment: int = 80,
    a_ang: float = 4.0782,
) -> PathSample:
    if len(labels) < 2:
        raise ValueError("labels must contain at least two points.")
    if points_per_segment < 2:
        raise ValueError("points_per_segment must be >= 2.")

    canon = tuple(_canonical_label(x) for x in labels)
    k_points = [FCC_POINTS_RLU[canon[0]].copy()]
    tick_labels = [canon[0]]
    tick_indices = [0]

    for i in range(len(canon) - 1):
        p0 = FCC_POINTS_RLU[canon[i]]
        p1 = FCC_POINTS_RLU[canon[i + 1]]
        t = np.linspace(0.0, 1.0, points_per_segment + 1, endpoint=True)[1:]
        seg = p0[None, :] + (p1 - p0)[None, :] * t[:, None]
        k_points.extend(seg)
        tick_labels.append(canon[i + 1])
        tick_indices.append(len(k_points) - 1)

    k_red = np.asarray(k_points, dtype=float)
    k_invA = (2.0 * np.pi / a_ang) * k_red

    ds = np.linalg.norm(np.diff(k_invA, axis=0), axis=1)
    s_invA = np.zeros(k_invA.shape[0], dtype=float)
    s_invA[1:] = np.cumsum(ds)
    tick_indices_arr = np.asarray(tick_indices, dtype=int)

    return PathSample(
        labels=canon,
        tick_labels=tuple(tick_labels),
        tick_indices=tick_indices_arr,
        tick_s_invA=s_invA[tick_indices_arr],
        k_red=k_red,
        k_invA=k_invA,
        s_invA=s_invA,
    )


def fit_quadratic_at_label(
    path: PathSample,
    energies_ev: np.ndarray,
    label: str,
    *,
    occurrence: int = 0,
    window_points: int = 15,
) -> QuadraticFit:
    if window_points < 5:
        raise ValueError("window_points must be >= 5.")
    if window_points % 2 == 0:
        raise ValueError("window_points must be odd.")

    y = np.asarray(energies_ev, dtype=float)
    if y.shape != path.s_invA.shape:
        raise ValueError("energies_ev must match the path length.")

    canon = _canonical_label(label)
    matches = [i for i, lbl in enumerate(path.tick_labels) if lbl == canon]
    if not matches:
        raise ValueError(f"Label '{label}' not found on path.")
    if occurrence < 0 or occurrence >= len(matches):
        raise ValueError(f"Occurrence {occurrence} out of range for label '{label}' ({len(matches)} found).")

    tick_idx = matches[occurrence]
    idx0 = int(path.tick_indices[tick_idx])
    half = window_points // 2
    lo = max(0, idx0 - half)
    hi = min(path.s_invA.size, idx0 + half + 1)
    if hi - lo < 5:
        raise ValueError("Not enough points around target for a stable quadratic fit.")

    x_data = path.s_invA[lo:hi] - path.s_invA[idx0]
    y_data = y[lo:hi]
    fit = fit_quadratic_1d(x_data, y_data)

    return QuadraticFit(
        label=canon,
        occurrence=occurrence,
        point_index=idx0,
        a_evA2=float(fit.a_evA2),
        b_evA=float(fit.b_evA),
        c_ev=float(fit.c_ev),
        m_eff_over_me=float(fit.m_eff_over_me),
        s0_invA=float(path.s_invA[idx0]),
        s_fit_invA=fit.x_fit_invA + path.s_invA[idx0],
        e_fit_ev=fit.e_fit_ev,
        s_data_invA=path.s_invA[lo:hi],
        e_data_ev=y_data,
    )


def fit_quadratic_1d(x_invA: np.ndarray, energies_ev: np.ndarray) -> Quadratic1DFit:
    x = np.asarray(x_invA, dtype=float)
    y = np.asarray(energies_ev, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or x.size != y.size:
        raise ValueError("x_invA and energies_ev must be 1D arrays of equal length.")
    if x.size < 5:
        raise ValueError("At least 5 points are required for a stable quadratic fit.")

    a, b, c = np.polyfit(x, y, deg=2)
    y_fit = a * x * x + b * x + c
    m_eff = np.inf if np.isclose(a, 0.0, atol=1e-12) else HBAR2_OVER_2ME_EV_A2 / a

    return Quadratic1DFit(
        a_evA2=float(a),
        b_evA=float(b),
        c_ev=float(c),
        m_eff_over_me=float(m_eff),
        x_fit_invA=x,
        e_fit_ev=y_fit,
        x_data_invA=x,
        e_data_ev=y,
    )


def sample_symmetry_line(
    model: RoseiLikeGoldModel,
    *,
    band: str,
    center_label: str,
    direction_to_label: str,
    qmax_invA: float = 0.20,
    num_points: int = 121,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Sample a 1D line k(q) = k0 + q * u through a symmetry point.

    q is returned in 1/Angstrom, energies in eV, and k-line points in rlu.
    """

    if num_points < 11:
        raise ValueError("num_points must be >= 11.")
    if qmax_invA <= 0:
        raise ValueError("qmax_invA must be positive.")

    center = FCC_POINTS_RLU[_canonical_label(center_label)]
    target = FCC_POINTS_RLU[_canonical_label(direction_to_label)]
    direction = target - center
    norm = float(np.linalg.norm(direction))
    if np.isclose(norm, 0.0):
        raise ValueError("center_label and direction_to_label must be different points.")

    u_hat = direction / norm
    q_invA = np.linspace(-qmax_invA, qmax_invA, num_points, dtype=float)
    q_to_rlu = model.a_ang / (2.0 * np.pi)
    k_line = center[None, :] + (q_invA * q_to_rlu)[:, None] * u_hat[None, :]
    e_line = model.energy(band, k_line)
    return q_invA, e_line, k_line


def sample_path_bands(
    model: RoseiLikeGoldModel,
    path: PathSample,
    bands: Iterable[str] = ("v", "c"),
) -> dict[str, np.ndarray]:
    out: dict[str, np.ndarray] = {}
    for band in bands:
        out[band] = model.energy(band, path.k_red)
    return out


def plot_path_dispersion(
    path: PathSample,
    band_energies_ev: dict[str, np.ndarray],
    *,
    fits: Sequence[QuadraticFit] = (),
    title: str = "Au band dispersion along FCC high-symmetry path",
):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10.0, 5.2))

    for band_name, y in band_energies_ev.items():
        ax.plot(path.s_invA, y, label=f"Band {band_name}")

    for fit in fits:
        ax.plot(fit.s_fit_invA, fit.e_fit_ev, "--", linewidth=2.0, label=f"{fit.label} fit (m*={fit.m_eff_over_me:.3g} me)")

    for s_tick in path.tick_s_invA:
        ax.axvline(s_tick, color="0.85", linewidth=0.8, zorder=0)

    ax.set_xticks(path.tick_s_invA, path.tick_labels)
    ax.set_xlabel(r"Path coordinate $|k|$ [1/Angstrom]")
    ax.set_ylabel("Energy [eV]")
    ax.set_title(title)
    ax.grid(alpha=0.25)
    ax.legend(loc="best")
    fig.tight_layout()
    return fig, ax


def compute_ceds_isosurface(
    model: RoseiLikeGoldModel,
    *,
    upper_band: str,
    lower_band: str,
    hbar_omega_ev: float,
    kmin: float = -1.2,
    kmax: float = 1.2,
    grid_size: int = 70,
) -> IsoSurfaceMesh:
    try:
        from skimage import measure
    except ImportError as exc:
        raise ImportError("scikit-image is required. Install with: pip install scikit-image") from exc

    if grid_size < 20:
        raise ValueError("grid_size must be >= 20.")
    if not (kmax > kmin):
        raise ValueError("kmax must be larger than kmin.")

    k = np.linspace(kmin, kmax, grid_size, dtype=float)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    delta = model.delta_components(upper_band, lower_band, kx, ky, kz)
    delta_min = float(np.min(delta))
    delta_max = float(np.max(delta))
    if hbar_omega_ev < delta_min or hbar_omega_ev > delta_max:
        raise ValueError(
            f"hbar_omega_ev={hbar_omega_ev:.3f} eV is outside delta range [{delta_min:.3f}, {delta_max:.3f}] eV."
        )

    dk = float(k[1] - k[0])
    verts, faces, _normals, _values = measure.marching_cubes(delta, level=hbar_omega_ev, spacing=(dk, dk, dk))
    verts += np.array([kmin, kmin, kmin], dtype=float)

    return IsoSurfaceMesh(
        level_ev=float(hbar_omega_ev),
        kmin=float(kmin),
        kmax=float(kmax),
        verts=verts,
        faces=faces,
        delta_min_ev=delta_min,
        delta_max_ev=delta_max,
    )


def plot_ceds_plotly(
    mesh: IsoSurfaceMesh,
    *,
    marker_labels: Sequence[str] = ("L", "X"),
    marker_size: int = 4,
):
    try:
        import plotly.graph_objects as go
    except ImportError as exc:
        raise ImportError("plotly is required. Install with: pip install plotly") from exc

    fig = go.Figure(
        data=[
            go.Mesh3d(
                x=mesh.verts[:, 0],
                y=mesh.verts[:, 1],
                z=mesh.verts[:, 2],
                i=mesh.faces[:, 0],
                j=mesh.faces[:, 1],
                k=mesh.faces[:, 2],
                opacity=0.45,
                color="gold",
                flatshading=True,
                name=f"CEDS {mesh.level_ev:.2f} eV",
            )
        ]
    )

    colors = {"L": "red", "X": "blue", "G": "black"}
    for raw_label in marker_labels:
        label = raw_label.strip().upper()
        if label in {"L", "L*"}:
            pts = L_STAR_RLU
            name = "L star"
        elif label in {"X", "X*"}:
            pts = X_STAR_RLU
            name = "X star"
        else:
            canon = _canonical_label(label)
            pts = FCC_POINTS_RLU[canon][None, :]
            name = canon

        fig.add_trace(
            go.Scatter3d(
                x=pts[:, 0],
                y=pts[:, 1],
                z=pts[:, 2],
                mode="markers",
                marker=dict(size=marker_size, color=colors.get(label[0], "black")),
                name=name,
            )
        )

    fig.update_layout(
        title=f"CEDS for DeltaE = {mesh.level_ev:.2f} eV",
        scene=dict(
            xaxis_title="kx [rlu]",
            yaxis_title="ky [rlu]",
            zaxis_title="kz [rlu]",
            aspectmode="cube",
        ),
    )
    return fig
