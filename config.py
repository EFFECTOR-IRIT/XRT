from datetime import datetime


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
