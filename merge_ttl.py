from rdflib import Graph
import sys
import os
import fnmatch



def merge(dir):
    final_graph = Graph()
    for path, dirs, files in os.walk(dir):
        for f in fnmatch.filter(files,'*.ttl'):
            fullname = os.path.abspath(os.path.join(path,f))
            print("Adding file:", fullname)
            graph = Graph()
            graph.parse(fullname, format="turtle")
            final_graph = final_graph + graph
    final_graph.serialize("ontology_merged", format='turtle')




if __name__ == "__main__":
    merge(sys.argv[1] )