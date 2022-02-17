from rdflib import OWL, RDFS, Namespace, Literal
from rdflib.extras import infixowl
from xsd_to_rdf.entity.entity import Entity
from config import config


# TODO: no global
RESTRICTION_USAGE = config.get('data_property').get('restriction_usage')
MIN_CARD_TAG = config.get('common').get('min_card_tag')
MAX_CARD_TAG = config.get('common').get('max_card_tag')
EXCLUDED_STRING = config.get('data_property').get('excluded_string')
MINUSCULE = config.get('data_property').get('minuscule')
ACCRONYM_CASE = config.get('data_property').get('accronym_case')


class DataProperty(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.domain = kwargs.get('domain')
        self.xsd_type = kwargs.get('xsd_type')
        self.min = kwargs.get('min_value') if RESTRICTION_USAGE else None
        self.max = kwargs.get('max_value') if RESTRICTION_USAGE else None
        self.type = OWL.DatatypeProperty

    def convert_to_rdf(self):
        super().convert_to_rdf()
        self.set_type()
        self.set_range()
        self.set_domain()
        self.set_restriction()
        self.set_cardinalities()

    def set_domain(self):
        self.graph.add_triplet((self.uri, RDFS.domain, self.domain.uri))

    def set_range(self):
            xsd_type_ns = self.xsd_type[:self.xsd_type.index(':')]
            xsd_type = self.xsd_type[self.xsd_type.index(':') + 1:]
            namespace = next((
                value for (key, value) in self.domain.node.nsmap.items()
                if key == xsd_type_ns))
            ns = Namespace(namespace + '#')
            self.graph.add_triplet((self.uri, RDFS.range, ns[xsd_type]))

    def set_name_with_convention(self):
        self.name = self.name.lower()

    def set_restriction(self):
        SDO = Namespace('https://schema.org/')
        self.graph.bind_namespace('schema', SDO)
        if self.min and self.max:
            self.graph.add_triplet((
                self.uri,
                SDO.minValue,
                Literal(self.min, datatype = self.xsd_type))
            )
            self.graph.add_triplet((
                self.uri,
                SDO.maxValue,
                Literal(self.max, datatype = self.xsd_type))
            )

    def set_cardinalities(self):
        if MIN_CARD_TAG in self.node.attrib:
            infixowl.Restriction(
                self.uri,
                graph = self.graph.get_graph,
                minCardinality = Literal(self.node.attrib.get(MIN_CARD_TAG)),
                identifier = self.namespace[self.name] + 'MinCardinality')
        if MAX_CARD_TAG in self.node.attrib:
            infixowl.Restriction(
                self.uri,
                graph = self.graph.get_graph,
                maxCardinality = Literal(self.node.attrib.get(MAX_CARD_TAG)),
                identifier = self.namespace[self.name] + 'MaxCardinality')
