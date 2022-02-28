from rdflib import ConjunctiveGraph, DC, Literal, RDF, OWL
from xsd_to_rdf.serializers.graph_seralizers import ObjectSerializer
from rdflib.extras.infixowl import Ontology


class Graph:

    def __init__(self, config):
        self.graph = ConjunctiveGraph()
        self.metadata = config.get('metadata')
        ns = config.get('options').get('namespaces')
        for key, value in ns.items():
            self.graph.bind(key, value)

    def add_triplet(self, triplet):
        self.graph.add(triplet)

    def bind_namespace(self, prefix, namespace):
        self.graph.bind(prefix, namespace)

    def set_metadata(self):
        self.graph.bind('dc', DC)
        self.graph.add((self.graph.identifier, RDF.type, OWL.Ontology))
        self.graph.add((self.graph.identifier, OWL.versionInfo, Literal(self.metadata.get('version'))))
        self.graph.add((self.graph.identifier, DC.title, Literal(self.metadata.get('title'))))
        self.graph.add((self.graph.identifier, DC.creator, Literal(self.metadata.get('creator'))))
        self.graph.add((self.graph.identifier, DC.date, Literal(self.metadata.get('date'))))
        self.graph.add((self.graph.identifier, DC.source, Literal(self.metadata.get('source'))))
        self.graph.add((self.graph.identifier, DC.language, Literal(self.metadata.get('language'))))

    def serialize(self, output, format):
        serializer = ObjectSerializer()
        serializer.serialize(self.graph, output, format)

    @property
    def get_graph(self):
        return self.graph
