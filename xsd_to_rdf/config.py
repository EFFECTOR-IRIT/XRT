ontology = dict(
    author = 'IRIT',
    version = '1.3',
    name = 'ecise',
    default_comment = 'No description provided.',
    namespaces = {
        'owl': 'http://www.w3.org/2002/07/owl#',
        'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
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

config = dict(
    input_dir = './input/',
    output_dir = './output/',
    output_filename = 'ecise-ontology-1.3.ttl',
    output_format = 'turtle', # xml, json-ld, turtle
    node_regex = r'.*Type',
    common = dict(
        parent_tag = 'extension',
        comment_tag = 'annotation',
        sequence_tag = 'sequence',
        element_tag = 'element',
        restriction_tag = 'restriction',
        min_value_tag = 'minInclusive',
        max_value_tag = 'maxInclusive',
        min_card_tag = 'minOccurs',
        max_card_tag = 'maxOccurs'
    ),
    thing_class = dict(
        excluded_parents = [
            'rel:Relationship' # do not touch
        ],
        excluded_string = []
    ),
    enumeration_type = dict(
        enum_tag = 'enumeration',
        excluded_string = []
    ),
    relationship_class = dict(
        excluded_string = []
    ),
    data_property = dict(
        excluded_string = [],
        restriction_usage = True
    ),
    object_property = dict(
        prefix = 'has',
        excluded_string = [
            'Involved',
            'Implied',
            'Rel'
        ]
    )
)

xsd_types = dict(
    any_uri = 'xs:anyURI',
    string = 'xs:string',
    int = 'xs:int',
    long = 'xs:long',
    float = 'xs:float',
    boolean = 'xs:boolean',
    double = 'xs:double',
    duration = 'xs:duration',
    time = 'xs:time',
    date = 'xs:date',
    datetime = 'xs:dateTime',
    base64Binary = 'xs:base64Binary',
    hexBinary = 'xs:hexBinary'
)
