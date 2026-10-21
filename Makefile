.PHONY: paper test clean

paper:
	latexmk -pdf -outdir=_build -interaction=nonstopmode -halt-on-error main.tex
	cp _build/main.pdf main.pdf

test:
	python3 -m unittest discover -s tests -v
	python3 scripts/check_project.py

clean:
	latexmk -C -outdir=_build main.tex
