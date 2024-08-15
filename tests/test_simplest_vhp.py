import pytest

def test_simplest():
    import yaml
    import logging

    import pandas as pd
    import biocypher

    import ontoweaver

    logging.debug("Load ontology...")

    bc = biocypher.BioCypher(
        biocypher_config_path = "tests/vhp/biocypher_config.yaml",
        schema_config_path = "tests/vhp/schema_config_vhp.yaml"
    )
    # bc.show_ontology_structure()

    logging.debug("Load data...")
    table = pd.read_csv("tests/vhp/data_vhp.csv")

    logging.debug("Load mapping...")
    with open("tests/vhp/mapping_vhp.yaml") as fd:
        mapping = yaml.full_load(fd)

    logging.debug("Run the adapter...")
    adapter = ontoweaver.tabular.extract_all(table, mapping)
    assert(adapter)

    logging.debug("Write nodes...")
    assert(adapter.nodes)
    bc.write_nodes( adapter.nodes )

    logging.debug("Write edges...")
    assert(adapter.edges)
    bc.write_edges( adapter.edges )

    logging.debug("Write import script...")
    bc.write_import_call()

    # Future versions of Biocypher will allow:
    # import_file = bc.write_import_call()
    # logging.debug("Import script is in:")
    # print(import_file)
    # assert(import_file)

if __name__ == "__main__":
    test_simplest()
