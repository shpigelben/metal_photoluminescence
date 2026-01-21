# LaTeX project (Overleaf-ready)

- Entry point: `main.tex`
- Sections: `sections/` (each section in its own folder)
- Figures: `figures/` (`\graphicspath{{figures/}}` is set)
- Bibliography: `references.bib` (BibTeX)

## Local build

- `make pdf`

## Clean

- `make clean`

## Minimal Overleaf ZIP

- `make overleaf` (creates/overwrites `overleaf_upload.zip` with only the source + figures)
