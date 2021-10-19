cise:
	python cise_generator.py cise cise_xsd

ecise:
	python ecise_generator.py ecise ecise_xsd
	python merge_ttl.py

install:
	pip install -r requirements.txt