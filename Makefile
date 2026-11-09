.PHONY: paper screen test clean

# Draft 4.1 feedback manuscript (latex/)
paper:
	cd latex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Evidence-screen companion (evidence-screen/)
screen:
	$(MAKE) -C evidence-screen paper

test:
	$(MAKE) -C evidence-screen test
	python3 experiments/01_1st_principles_evolutionary_argument_against_cbt/scripts/test_verification_receipts.py
	python3 experiments/01_1st_principles_evolutionary_argument_against_cbt/scripts/check_revision.py

clean:
	cd latex && latexmk -C main.tex
	$(MAKE) -C evidence-screen clean
