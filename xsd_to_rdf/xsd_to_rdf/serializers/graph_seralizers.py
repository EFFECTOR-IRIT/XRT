class ObjectSerializer:

    def serialize(self, graph, output, format):
        """
        Serialize object to format
        """
        serializer = factory.get_serializer(format)
        serializer.set_graph(graph)
        return serializer.serialize(output)


class XMLSerializer:

    def __init__(self):
        self.graph = None
    
    def set_graph(self, graph):
        self.graph = graph

    def serialize(self, output):
        """
        Serialize rdf graph to xml format
        """
        self.graph.serialize(output, format='xml')


class TurtleSerializer:

    def __init__(self):
        self.graph = None

    def set_graph(self, graph):
        self.graph = graph

    def serialize(self, output):
        """
        Serialize rdf graph to turtle format
        """
        self.graph.serialize(output, format='turtle')


class JSONLDSerializer:

    def __init__(self):
        self.graph = None

    def set_graph(self, graph):
        self.graph = graph

    def serialize(self, output):
        """
        Serialize rdf graph to jsonld format
        """
        self.graph.serialize(output, format='json-ld')


class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        """
        Register format serializer
        """
        self._creators[format] = creator

    def get_serializer(self, format):
        """
        Get serializer by format
        """
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('xml', XMLSerializer)
factory.register_format('turtle', TurtleSerializer)
factory.register_format('json-ld', JSONLDSerializer)
