PDF=main.pdf
TEX=main.tex
BASE=main

.PHONY: pdf clean overleaf

pdf:
	pdflatex -interaction=nonstopmode -halt-on-error "$(TEX)"
	bibtex "$(BASE)" || true
	pdflatex -interaction=nonstopmode -halt-on-error "$(TEX)"
	pdflatex -interaction=nonstopmode -halt-on-error "$(TEX)"

overleaf: clean
	rm -f overleaf_upload.zip
	zip -r overleaf_upload.zip main.tex references.bib sections figures

clean:
	rm -f *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.toc
