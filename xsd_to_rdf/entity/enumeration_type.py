from rdflib import OWL, RDF, RDFS, Literal
from xsd_to_rdf.entity.entity import Entity
from xsd_to_rdf.entity.thing_class import ThingClass
from xsd_to_rdf.entity.individual import Individual
from xsd_to_rdf.settings import settings

# TODO: no global 
SUPER_CLASSES = settings.get('ontology').get('super_classes')
ENUM_TAG = settings.get('xsd_nodes').get('enumeration_type').get('enum_tag')


class EnumerationType(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = OWL.Class

    def convert_to_rdf(self):
        super().convert_to_rdf()
        self.set_type()
        self.set_super_element()
        for child in self.node:
            enumerations = list(filter(
                lambda element: ENUM_TAG in element.tag, child))
            for enum in enumerations:
                individual = Individual(
                    graph = self.graph,
                    name = enum.attrib.get('value'),
                    namespace = self.namespace,
                    node = enum,
                    instance_of = self)
                individual.convert_to_rdf()
                self.sub_elements.append(individual)

    def set_super_element(self):
        default_super_class = next((
            cls for cls in SUPER_CLASSES
            if cls.get('super_class_of') == __class__.__name__),
            None)
        if default_super_class is None: return
        self.super_entity = ThingClass(
            name = default_super_class.get('label'),
            namespace = default_super_class.get('namespace'))
        super_class_uri = self.super_entity.namespace[self.super_entity.get_name]
        self.graph.add_triplet((self.uri, RDFS.subClassOf, super_class_uri))
        self.graph.add_triplet((
            super_class_uri,
            RDFS.label,
            Literal(self.super_entity.get_name))
        )
        self.graph.bind_namespace(
            self.super_entity.get_prefix, self.super_entity.get_namespace)
