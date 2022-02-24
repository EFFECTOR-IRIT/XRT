import re
from lxml import etree


def read_file(filename):
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


def read_node(node):
    return etree.QName(node).localname
