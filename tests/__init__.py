""" all generic test configs """
from io import BytesIO

from lxml import etree


def create_xml(content: str) -> etree.Element:
    """ Given a string representing the xml, returns it as an etree element."""
    return etree.parse(BytesIO(content.encode())).getroot()
