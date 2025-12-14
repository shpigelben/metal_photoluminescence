# LaTeX build notes

- Entry point: `ai - main.tex` (loads all `ai - section_*.tex` and figures from `ai - figs/`).
- Figures: `ai - figs/` (logo + comparison plots). `\graphicspath` is set, so relative includes work.
- Quick build: run `make pdf` in this directory (runs `pdflatex`, `bibtex`, then `pdflatex` twice). Or manually: `pdflatex -interaction=nonstopmode -halt-on-error "ai - main.tex"`, `bibtex "ai - main"`, then `pdflatex` twice.
- Cleanup: `make clean` removes auxiliary files.

If the folder is hidden (e.g., `.LaTeX`), open it by path in VS Code or enable hidden folders. The Makefile and paths work regardless of visibility.*** End Patch**"}github/actions-temporary-commentary id="note-readme"/>
