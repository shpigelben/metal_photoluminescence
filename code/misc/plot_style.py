from pathlib import Path
import matplotlib as mpl

PROJECT_ROOT = Path(__file__).resolve().parents[2]
FIGURES_DIR = PROJECT_ROOT / "docs" / "4 Misc" / "Attachments"


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "figure.dpi": 200,
            "savefig.dpi": 200,
            "savefig.format": "png",
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.02,
            "savefig.transparent": True,
            "figure.facecolor": "none",
            "axes.facecolor": "none",
            "font.size": 13,
            "axes.labelsize": 13,
            "axes.titlesize": 13,
            "axes.titlepad": 4.0,
            "figure.titlesize": 15,
            "legend.fontsize": 12,
            "legend.frameon": False,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "axes.linewidth": 0.8,
            "lines.linewidth": 1.6,
            "lines.solid_capstyle": "round",
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "xtick.major.size": 4,
            "ytick.major.size": 4,
            "xtick.minor.size": 2,
            "ytick.minor.size": 2,
            "xtick.major.width": 0.8,
            "ytick.major.width": 0.8,
            "xtick.minor.width": 0.6,
            "ytick.minor.width": 0.6,
            "xtick.minor.visible": True,
            "ytick.minor.visible": True,
            "axes.unicode_minus": False,
            "mathtext.fontset": "stix",
            "font.family": "serif",
            "svg.fonttype": "none",
        }
    )


def save_svg(fig, filename: str, *, figures_dir: Path = FIGURES_DIR) -> Path:
    figures_dir.mkdir(parents=True, exist_ok=True)
    path = figures_dir / filename
    fmt = path.suffix.lstrip(".") or "png"
    fig.savefig(path, format=fmt, dpi=200, transparent=True)
    return path


def tight_layout_below_text(fig, text, *, pad: float = 0.01) -> None:
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bbox = text.get_window_extent(renderer).transformed(fig.transFigure.inverted())
    top = max(0.0, bbox.y0 - pad)
    fig.tight_layout(rect=(0.0, 0.0, 1.0, top))


def set_figure_title(fig, title: str, *, fontsize: float | None = None, pad: float = 0.01):
    text = fig.suptitle(title, y=0.99, fontsize=fontsize)
    tight_layout_below_text(fig, text, pad=pad)
    return text
