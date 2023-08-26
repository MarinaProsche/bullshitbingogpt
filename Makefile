example:
	python code_for_examples.py
gen:
	rm -rf buzzwords && mkdir buzzwords && python generator_for_themes.py
flask:
	flask --app app run	