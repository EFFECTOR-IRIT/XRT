from rdflib import ConjunctiveGraph, URIRef, RDFS, Namespace, OWL
from xsd_to_rdf.serializers.graph_seralizers import ObjectSerializer

class Graph:

    def __init__(self, namespaces):
        self.graph = ConjunctiveGraph()
        for key, value in namespaces.items():
            self.graph.bind(key, value)

    def add_triplet(self, triplet):
        self.graph.add(triplet)

    def bind_namespace(self, prefix, namespace):
        self.graph.bind(prefix, namespace)

    def serialize(self, output, format):
        serializer = ObjectSerializer()
        serializer.serialize(self.graph, output, format)

    @property
    def get_graph(self):
        return self.graph