from rdflib import OWL, RDF
from xsd_to_rdf.entity.entity import Entity


class Individual(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instance_of = kwargs.get('instance_of')
        self.type = OWL.NamedIndividual

    def convert_to_rdf(self):
        super().convert_to_rdf()
        self.set_type()
        self.set_individual()

    def set_individual(self):
        self.graph.add_triplet((self.uri, RDF.type, self.instance_of.uri))
