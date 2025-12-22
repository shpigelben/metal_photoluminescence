"""
Stage 4 - Delta (2D) Approximation, Energy Space
Derived from docs/notes/4 - Delta (2D) Approximation E-Space.md.
"""

from __future__ import annotations

NOTES: list[str] = [
    "POC: show convergence requirements for int x delta(x - mu) dx = mu when the delta is approximated by a Gaussian.",
    "POC: show convergence requirements for int_{-1}^{1} int_{-1}^{1} x*y*delta(x - y - mu) dx dy = int_{-1}^{1} (y + mu)*y dy using a Gaussian delta.",
    "After identifying convergence parameters, enforce them when comparing the resolved Eq. (4) and unresolved Eq. (3) expressions.",
]


def todo() -> list[str]:
    return NOTES.copy()


if __name__ == "__main__":
    for item in todo():
        print(f"- [ ] {item}")
