#!/usr/bin/env python3
"""XML serialization and deserialization module."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML and save to file.

    Args:
        dictionary: Python dictionary to serialize
        filename: The filename to save XML data to
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML data from file to Python dictionary.

    Args:
        filename: The filename to read XML data from

    Returns:
        Python dictionary with deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
