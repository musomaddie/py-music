from dataclasses import dataclass

from lxml import etree


@dataclass
class KeyBuilder:
    """ Represents a key:

    link: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/key/
    """

    @staticmethod
    def create_from_key_xml(og_xml: etree.Element) -> 'KeyBuilder':
        """ Creates a key builder from the given item. """
        pass
