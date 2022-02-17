### Install dependencies ###
install:
	py -m pip install -r requirements.txt

install_setup:
	py ./setup.py install --user

### Generation ###
run:
	py ./main.py

### Generation ###
# main => call cise_generator functionalities
#cise:
#	tar -xf ./input/cise_xsd.zip
#	py ./main.py cise ./input/cise_xsd
#	rm -r ./input/cise_xsd

# main => call ecise_generator + merge functionalities
#ecise:
#	tar -xf ./input/ecise_xsd.zip
#	py ./main.py ecise ./input/ecise_xsd ./pdf/andromeda.pdf
#	rm -r ./input/ecise_xsd

### Package ###
build:
	py ./setup.py build
