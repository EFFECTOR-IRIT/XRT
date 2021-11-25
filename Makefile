cise:
	python cise_generator.py cise cise_xsd

ecise:
	python ecise_generator.py ecise ecise_xsd andromeda.pdf
	python merge_ttl.py ecise_xsd

# install:
# 	pip install -r requirements.txt