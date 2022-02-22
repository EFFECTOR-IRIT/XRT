### Install dependencies ###
install:
	py -m pip install -r requirements.txt

install_setup:
	py ./setup.py install --user

### Generation ###
run:
	py ./main.py

### Package ###
build:
	py ./setup.py build
