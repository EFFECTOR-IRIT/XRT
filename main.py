import os
import sys
import glob
from reader.xsd_reader import read_file, read_node
from xsd_to_rdf.graph.graph import Graph
from xsd_to_rdf.entity_picker.entity_picker import EntityPicker
from config import config


# TODO: no global 
INPUT_DIR = config.get('files').get('input_dir')
OUTPUT_DIR = config.get('files').get('output_dir')
OUTPUT_FILE = config.get('files').get('output_filename')
OUPUT_FORMAT = config.get('files').get('output_format')
METADATA = config.get('metadata')
OPTIONS = config.get('options')

class MainProcess:

    def run(self):
        # 1 - Initialize graph
        graph = Graph(config)
        graph.set_metadata()
        # 2 - Get files from input
        files = glob.glob(
            INPUT_DIR + '**/*.xsd',
            recursive=True)
        if len(files) == 0: raise FileNotFoundError(INPUT_DIR)
        # 3 - extract nodes and sub-elements
        for filename in files:
            namespace, nodes = read_file(filename)
            # 4 - build entities from nodes (TODO: data property first level)
            for node in nodes:
                node_type = read_node(node)
                entity = EntityPicker().get_entity(node_type)(
                    graph = graph,
                    name = node.attrib['name'],
                    namespace = namespace,
                    node = node,
                    options = OPTIONS)
                entity.convert_to_rdf()
        # 6 - serialize graph in chosen format (config)
        output = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        graph.serialize(output, OUPUT_FORMAT)


if __name__ == "__main__":
    process = MainProcess()
    process.run()
    sys.exit(0)
