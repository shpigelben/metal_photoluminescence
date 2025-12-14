"""
Stage 5 - Delta (2D) Approximation, K Space
Derived from docs/notes/5 - Delta (2D) Approximation K-Space.md.
"""

from __future__ import annotations

NOTES: list[str] = [
    "Find convergence conditions for a simple 1D function where the delta argument traces a hyperbola in k-space.",
    "Find convergence conditions for a simple 2D function with the same geometry.",
    "Clarify and complete the unfinished 'When ...' bullet from the original notes before coding the last experiment.",
]


def todo() -> list[str]:
    return NOTES.copy()


if __name__ == "__main__":
    for item in todo():
        print(f"- [ ] {item}")
