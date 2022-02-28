# XTR

Version 1.2.0

## General

XTR is a python module that aims at generating ontologies from models described in the XSD language. So far, the module has been tested on two different ontologies: CISE (from version 1.5.2 of the CISE data model) and e-CISE (from versions 2.2.1 and 2.4.0).

## Installation

Clone the GIT repository and install the dependencies with the following command:

    make install

The module is ready to use.

## Usage

A configuration file at the root of the module allows the ontology metadata to be filled in. It is also possible to change input and output directories. You can also change the output format (json-ld, turtle or xml for owl file).

    config = dict(
        metadata = dict(
            name = 'ecise',
            author = 'IRIT',
            version = '1.3',
            creation_date = datetime.now(),
            xsd_version = '2.4.0'
        ),
        files = dict(
            input_dir = './input/',
            output_dir = './output/',
            output_filename = 'ecise-ontology-1.3.ttl',
            output_format = 'turtle', # xml, json-ld, turtle
        )
    )

The XSD files containing the data model to be generated in ontological format should be placed in the input folder. Then the following command can be run:

    make run

The generated ontology should be written and saved in the output folder.

## Known Issues

- Global variables should be passed as parameters to the different classes.
- First level properties are considered as RDF classes (will be corrected in the next version)

## Version 1.2.1

- Known issues correction