init:
	pip install --user -r requirements.txt

style:
	autopep8 --in-place fantacalcio-randomizer/fantacalcio_randomizer.py fantacalcio-randomizer/gui.py

run:
	python fantacalcio-randomizer/gui.py

clean:
	rm Squadra*

exec: style run
