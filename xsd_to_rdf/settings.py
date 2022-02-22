settings = dict(
    xsd_nodes = dict(
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
                'rel:Relationship'
            ]
        ),
        enumeration_type = dict(
            enum_tag = 'enumeration'
        ),
        relationship_class = dict(
        ),
        data_property = dict(
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
    ),
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
    ),
    ontology = dict(
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
)