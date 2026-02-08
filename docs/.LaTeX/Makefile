PDF=main.pdf
TEX=main.tex
BASE=main

.PHONY: pdf clean

pdf:
	pdflatex -interaction=nonstopmode -halt-on-error "$(TEX)"
	bibtex "$(BASE)" || true
	pdflatex -interaction=nonstopmode -halt-on-error "$(TEX)"
	pdflatex -interaction=nonstopmode -halt-on-error "$(TEX)"

clean:
	rm -f *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.toc
