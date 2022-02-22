from setuptools import setup, find_packages

setup(
    name='xsd_to_rdf',
    version='1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Generate CISE & eCISE ontologies from XSD files',
    long_description=open('README.md').read(),
    install_requires=[
        "rdflib",
        "PyPDF2",
        "requests",
        "lxml",
    ],
    url='https://gitlab.irit.fr/effector/xsd_to_owl',
    author='Antoine DUPUY',
    author_email='antoine.dupuy@irit.fr',
)
