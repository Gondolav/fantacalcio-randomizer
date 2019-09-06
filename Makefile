init:
	pip3.6 install --user -r requirements.txt

style:
	autopep8 --in-place fantacalcio-randomizer/fantacalcio_randomizer.py fantacalcio-randomizer/gui.py

run:
	python3.6 fantacalcio-randomizer/gui.py

clean:
	rm Squadra*

exec: style run
