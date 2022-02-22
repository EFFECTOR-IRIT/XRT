import os
import sys
import glob
import re
from lxml import etree
from xsd_to_rdf.graph.graph import Graph
from xsd_to_rdf.entity_picker.entity_picker import EntityPicker
from config import config


# TODO: no global 
INPUT_DIR = config.get('files').get('input_dir')
OUTPUT_DIR = config.get('files').get('output_dir')
OUTPUT_FILE = config.get('files').get('output_filename')
OUPUT_FORMAT = config.get('files').get('output_format')


class MainProcess:

    def run(self):
        # 1 - Initialize graph
        graph = Graph()
        # 2 - Get files from input
        files = glob.glob(
            INPUT_DIR + '**/*.xsd',
            recursive=True)
        if len(files) == 0: raise FileNotFoundError(INPUT_DIR)
        # 3 - extract nodes and sub-elements
        for filename in files:
            namespace, nodes = self.extract_sources_from_filename(filename)
            # 4 - build entities from nodes (TODO: data property first level)
            for node in nodes:
                node_type = etree.QName(node).localname
                entity = EntityPicker().get_entity(node_type)(
                    graph = graph,
                    name = node.attrib['name'],
                    namespace = namespace,
                    node = node)
                entity.convert_to_rdf()
        # 6 - serialize graph in chosen format (config)
        output = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        graph.serialize(output, OUPUT_FORMAT)

    # TODO: move this function
    def extract_sources_from_filename(self, filename):
        """
        Extract nodes from XSD file
        """
        parser = etree.XMLParser(remove_comments=True)
        node_regex = re.compile(r'.*Type')
        with open(filename, encoding='utf8') as f:
            root = etree.parse(f, parser).getroot()
        # retrieve class and sub-elements
        children = root.getchildren()
        namespace = root.attrib.get('targetNamespace')
        return namespace, list(filter(
            lambda child : re.match(node_regex, child.tag),
            children))


if __name__ == "__main__":
    process = MainProcess()
    process.run()
    sys.exit(0)
