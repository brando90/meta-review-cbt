.PHONY: paper screen test clean

# Draft 3 manuscript (latex/)
paper:
	cd latex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Evidence-screen companion (evidence-screen/)
screen:
	$(MAKE) -C evidence-screen paper

test:
	$(MAKE) -C evidence-screen test

clean:
	cd latex && latexmk -C main.tex
	$(MAKE) -C evidence-screen clean
