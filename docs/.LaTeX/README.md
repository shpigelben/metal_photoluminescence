# LaTeX build notes

- Entry point: `new - main.tex` (loads all `new - section_*.tex` and figures from `new - figs/`).
- Figures: `new - figs/` (logo + comparison plots). `\graphicspath` is set, so relative includes work.
- Quick build: run `make pdf` in this directory (runs `pdflatex` twice). Or manually: `pdflatex -interaction=nonstopmode -halt-on-error "new - main.tex"` twice.
- Cleanup: `make clean` removes auxiliary files.

If the folder is hidden (e.g., `.LaTeX`), open it by path in VS Code or enable hidden folders. The Makefile and paths work regardless of visibility.*** End Patch**"}github/actions-temporary-commentary id="note-readme"/>
