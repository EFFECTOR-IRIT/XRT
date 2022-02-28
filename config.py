from datetime import datetime


config = dict(
    metadata = dict(
        title = 'ecise',
        creator = 'IRIT',
        version = '1.3',
        date = datetime.now(),
        source = '2.4.0',
        language = 'en'
    ),
    files = dict(
        input_dir = './input/',
        output_dir = './output/',
        output_filename = 'ecise-ontology-1.3.ttl',
        output_format = 'turtle', # xml, json-ld, turtle
    ),
    options = dict(
        base_uri = 'http://www.ecise.eu/datamodel/v1/',
        default_comment = 'No description provided.',
        namespaces = {
            'owl': 'http://www.w3.org/2002/07/owl#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
        },
        super_classes = [
            {
                'label': 'EnumerationType',
                'namespace': 'http://www.ecise.eu/datamodel/v1/enum/',
                'super_class_of': 'EnumerationType'
            },
            {
                'label': 'Relationship',
                'namespace': 'http://www.ecise.eu/datamodel/v1/relationship/',
                'super_class_of': 'RelationshipClass'
            }
        ]
    )
)
