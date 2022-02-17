from xsd_to_rdf.entity.thing_class import ThingClass
from xsd_to_rdf.entity.enumeration_type import EnumerationType
# from xsd_to_rdf.entity.data_property import DataProperty


class EntityPicker:

    def get_entity(self, node_type):
        """
        Get rdfentity by node type
        """
        entity = factory.get_entity_class(node_type)
        return entity


class EntityFactory:

    def __init__(self):
        self._entities = {}

    def register_entity(self, node_type, rdfentity):
        """
        Register rdfentity with associated node type
        """
        self._entities[node_type] = rdfentity

    def get_entity_class(self, node_type):
        """
        Get rdfentity by node type
        """
        rdfentity = self._entities.get(node_type)
        if not rdfentity:
            raise ValueError(node_type)
        return rdfentity


factory = EntityFactory()
factory.register_entity('simpleType', EnumerationType)
factory.register_entity('complexType', ThingClass)
