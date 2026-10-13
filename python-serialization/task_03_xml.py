#!/usr/bin/env python3
"""Module for converting to xml"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """take a dictionary and dump"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    with open(filename, "wb") as f:
        f.write(ET.tostring(root))


def deserialize_from_xml(filename):
    """converting the xml to dictionary"""
    d = {}
    with open(filename) as file:
        xml_tree = ET.parse(file)
        root = xml_tree.getroot()
        for element in root:
            d[element.tag] = element.text
        return d
