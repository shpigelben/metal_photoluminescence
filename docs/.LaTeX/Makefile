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
	rm -rf overleaf_upload
	mkdir -p overleaf_upload
	cp -p main.tex references.bib overleaf_upload/
	cp -R sections figures overleaf_upload/
	rm -f overleaf_upload.zip

clean:
	rm -f *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.toc
