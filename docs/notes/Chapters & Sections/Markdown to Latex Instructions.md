
# Markdown → LaTeX Conversion Spec (Overleaf-ready)

This is the “meta prompt” for converting the markdown notes in `docs/notes/Chapters & Sections/` into a clean LaTeX project that compiles on Overleaf.

## Goal
- Convert all content from the markdown notes into LaTeX.
- Keep the result **Overleaf compatible** (pdfLaTeX + BibTeX by default).
- Preserve a clear, modular structure: one `.tex` file per chapter/section, a single `main.tex` entry point, and a dedicated figures folder.

## Canonical target (default)
Use and extend the existing LaTeX project in `docs/.LaTeX/`:
- Entry point: `docs/.LaTeX/main.tex`
- Sections: `docs/.LaTeX/sections/`
- Figures: `docs/.LaTeX/figures/`
- Bibliography: `docs/.LaTeX/references.bib`

If asked to generate a *new* Overleaf project instead, mirror this same structure in a new folder (e.g. `docs/LaTeX/`) and keep it self-contained.

## Non-negotiables (Overleaf constraints)
- **No absolute paths** (no `/Users/...`, no `C:\...`).
- Prefer packages that work on Overleaf without extra flags. Avoid `minted` unless explicitly requested (it needs `--shell-escape`).
- Keep file names portable: **no spaces**, avoid `&`, `:`, etc. Use `snake_case`.

## Document class + layout (pick one and be consistent)
Your current LaTeX project already defines class/layout in `docs/.LaTeX/main.tex`. Default behavior:
- **Do not change** paper size/margins unless explicitly requested.

If changing layout is requested, fix the conflict that existed in older notes:
- Use **either** `a4paper` everywhere **or** `letterpaper` everywhere (documentclass + geometry must match).

## Structure mapping (markdown → LaTeX)
### Source of truth
- Each folder under `docs/notes/Chapters & Sections/` is treated as a “chapter” in the logical sense.

### Default mapping (for `article`)
Because `article` has no `\\chapter`, map like this:
- Chapter folder → `\\section{...}`
- Files inside the folder → `\\subsection{...}`

### Folder intro rule
- If a folder contains a markdown file with the **same name as the folder**, treat it as the **intro text** that goes immediately after the folder’s `\\section{...}` heading (do **not** wrap it in a `\\subsection`).
- All other markdown files in that folder become `\\subsection`s.

### Abstract + appendices
- Abstract: if there is an `Abstract.md`, convert it into a LaTeX `abstract` environment in `main.tex` (or `sections/abstract.tex` that is `\\input` before the ToC).
- Appendices: the folder `A - Appendices` becomes `\\appendix`, and each file inside becomes a `\\section{...}` (not a subsection).

### Outline with hyperlinks
- Use `\\tableofcontents` + `hyperref` so the outline is clickable.

## Markdown element conversion rules
### Headings
- `#`/`##`/`###` headings in markdown should become LaTeX `\\section`/`\\subsection`/`\\subsubsection` *within the rules above*.
- Keep titles human-readable; don’t include numeric prefixes unless you want them printed.

### Equations and cross-references
- Do **not** rely on hard-coded equation numbers in text.
- Convert display math into proper environments (`equation`, `align`, `gather`) and add labels:
  - `\\label{eq:<slug>}`
  - Reference with `Eq.~\\eqref{eq:<slug>}`
- If you see manual `\\tag{...}` in markdown, remove it unless preserving a historical numbering is explicitly required.
- If the text says “Eq. (4)” but no label exists, create a label and update the reference.

### Figures
- Convert markdown images (`![alt](path)`) into `figure` environments with:
  - `\\includegraphics`
  - `\\caption{...}`
  - `\\label{fig:<slug>}`
- If the markdown has a line like `Figure X.Y: ...`, treat that as the caption for the preceding figure.
- Put all figure assets under `docs/.LaTeX/figures/` and reference them as `figures/<filename>` (or just `<filename>` if `\\graphicspath` includes `figures/`).
- Use professional sizing defaults (e.g. `width=0.7\\textwidth`), not huge full-page images unless justified.

### Callouts / admonitions
- Obsidian callouts (or “Note/Warning” blocks) should be converted to a clean LaTeX alternative:
  - Use `tcolorbox` (add the package once in the preamble).

### Lists, tables, and code
- Lists: markdown lists → `itemize` / `enumerate`.
- Tables: markdown tables → `table` + `tabular` (use `booktabs` if needed).
- Code blocks: prefer `verbatim` or `listings` (avoid `minted` by default).

### Citations and bibliography (PRL-like)
- Use BibTeX with `docs/.LaTeX/references.bib`.
- Use `\\cite{key}` consistently.
- Target a Physical Review Letters–like look (numeric, compressed ranges). Typical setup:
  - `\\usepackage[numbers,sort&compress]{natbib}`
  - `\\bibliographystyle{apsrev4-2}`
- If the project already uses a different bibliography style, only change it when requested; otherwise keep the existing one.

## Quality checklist (definition of “done”)
- Compiles on Overleaf without manual intervention (select `main.tex` as the main document if needed).
- No absolute paths; all figures resolve.
- Every figure has a caption + label and is referenced in text.
- Equations are numbered automatically and referenced via `\\eqref`.
- Any missing information is marked with clear `TODO:` placeholders rather than guessing.

## Keep the LaTeX folder minimal (source-only)
Goal: at any time, `docs/.LaTeX/` contains **only the current, necessary** source files/assets for compilation and Overleaf upload. When regenerating/updating, overwrite or remove redundant outputs instead of accumulating clutter.

### Allowed contents (keep)
- Source: `main.tex`, `references.bib`, `sections/*.tex`
- Assets: `figures/*` (only files actually referenced by `\\includegraphics`)
- Support files only if required: custom `.sty/.cls/.bst` files used by the document
- Optional: `README.md` (instructions) and a minimal `Makefile` (local build convenience)

### Remove (do not keep)
- LaTeX build artifacts: `*.aux`, `*.log`, `*.out`, `*.toc`, `*.bbl`, `*.blg`, `*.fls`, `*.fdb_latexmk`, `*.synctex.gz`
- Locally compiled PDFs (e.g. `main.pdf`) unless explicitly needed as a figure asset (figure PDFs belong in `figures/`)
- OS/editor junk: `.DS_Store`, temp files, “(copy)” duplicates

### Update rules (avoid duplicates)
- Overwrite in place: when a section is regenerated, it **replaces** its prior `.tex` file (no `*_v2.tex`, no “copy of …” files).
- If a section is removed/renamed in the markdown sources, delete the old `sections/<old>.tex` and remove its `\\input{...}` from `main.tex`.
- Keep figures deduplicated: if the same image appears in multiple places, store a single copy in `figures/` and reference it consistently.

### Minimal Overleaf ZIP (create inside `docs/.LaTeX/`)
Create a ZIP that includes **only what Overleaf needs**, not the local build outputs.

1) Clean the folder (recommended):
- Run `make clean` in `docs/.LaTeX/` (or delete the artifact patterns listed above).

2) Create the upload ZIP (allowlist approach):
- From inside `docs/.LaTeX/`, run:
  - `zip -r overleaf_upload.zip main.tex references.bib sections figures`
- If you use any custom `.sty/.cls/.bst` files in `docs/.LaTeX/`, include them too:
  - `zip -r overleaf_upload.zip main.tex references.bib sections figures *.sty *.cls *.bst`

This produces a clean archive with the entry point + bibliography + all included section files and figure assets.
Overwrite `overleaf_upload.zip` each time (or delete it after uploading) to keep the folder minimal.

3) Sanity check:
- `unzip -l overleaf_upload.zip` should show `main.tex`, `references.bib`, `sections/`, and `figures/` at the ZIP root.
