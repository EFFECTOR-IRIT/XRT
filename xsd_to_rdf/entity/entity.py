from rdflib import RDFS, Literal, Namespace, RDF
from xsd_to_rdf.settings import settings


# TODO: no global
COMMENT_TAG = settings.get('xsd_nodes').get('common').get('comment_tag')


class Entity:

    def __init__(self, **kwargs):
        self.graph = kwargs.get('graph')
        self.name = (kwargs.get('name')
            .replace(' ', '')
            .replace('/', '_')
            .replace('(', '_')
            .replace(')', ''))
        self.namespace = Namespace(kwargs.get('namespace'))
        self.node = kwargs.get('node')
        self.options = kwargs.get('options')
        self.prefix = kwargs.get('namespace').rstrip('/').split('/').pop()
        self.type = None
        self.sub_elements = []
        self.super_entity = None

    def convert_to_rdf(self):
        self.set_name_with_convention()
        self.uri = self.namespace[self.name]
        self.graph.bind_namespace(self.prefix, self.namespace)
        self.set_label()
        self.set_comment()

    def set_type(self):
        self.graph.add_triplet((self.uri, RDF.type, self.type))

    def set_comment(self):
        if self.node is not None:
            text = ""
            annotation_tags = list(filter(
                lambda child: COMMENT_TAG in child.tag, list(self.node)))
            if len(annotation_tags) == 0:
                text = self.options.get('default_comment')
            else:
                if len(annotation_tags) > 1: raise ValueError(self.name)
                [annotation_tag] = annotation_tags
                if len(annotation_tag) > 1: raise ValueError(self.name)
                if len(annotation_tag) == 0:
                    text = self.options.get('default_comment')
                else:
                    [comment_tag] = annotation_tag
                    text = comment_tag.text if comment_tag.text else self.options.get('default_comment')
                self.graph.add_triplet((
                    self.uri,
                    RDFS.comment,
                    Literal(text)
                ))

    def set_label(self):
        self.graph.add_triplet((self.uri, RDFS.label, Literal(self.name)))

    def set_name_with_convention(self):
        ...

    @property
    def get_graph(self):
        return self.graph

    @property
    def get_name(self):
        return self.name

    @property
    def get_namespace(self):
        return self.namespace

    @property
    def get_node(self):
        return self.node

    @property
    def get_prefix(self):
        return self.prefix

    @property
    def get_type(self):
        return self.type

    @property
    def get_sub_elements(self):
        return self.sub_elements

    @property
    def get_super_entity(self):
        return self.super_entity
