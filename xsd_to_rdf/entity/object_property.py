from rdflib import OWL, RDFS, Namespace, Literal
from rdflib.extras import infixowl
from xsd_to_rdf.entity.entity import Entity
from xsd_to_rdf.settings import settings

# TODO: no global 
PREFIX = settings.get('xsd_nodes').get('object_property').get('prefix')
MIN_CARD_TAG = settings.get('xsd_nodes').get('common').get('min_card_tag')
MAX_CARD_TAG = settings.get('xsd_nodes').get('common').get('max_card_tag')
EXCLUDED_STRING = settings.get('xsd_nodes').get('object_property').get('excluded_string')


class ObjectProperty(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = OWL.ObjectProperty
        self.domain = kwargs.get('domain')
        self.range = kwargs.get('range')

    def convert_to_rdf(self):
        super().convert_to_rdf()
        self.set_type()
        self.set_domain()
        self.set_range()
        self.set_cardinalities()

    def set_domain(self):
        self.graph.add_triplet((self.uri, RDFS.domain, self.domain.uri))

    def set_range(self):
        range_ns = self.range[:self.range.index(':')]
        range_entity = self.range[self.range.index(':') + 1:]
        namespace = Namespace(next((
            value for (key, value) in self.node.nsmap.items()
            if key == range_ns)))
        
        range_uri = namespace[range_entity]
        self.graph.add_triplet((self.uri, RDFS.range, range_uri))

    def set_name_with_convention(self):
        for word in EXCLUDED_STRING:
            self.name = self.name.replace(word, '')
        self.name = PREFIX + self.domain.get_name + self.name

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
