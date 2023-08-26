from dataclasses import dataclass

import lxml.etree


@dataclass
class Part:
    """
    Links to bars with notes for this instrument only.
    """
    pass


@dataclass
class PartBuilder:
    """
    Builds a part instance.
    """

    @staticmethod
    def create_from_part_list(part_list_xml: lxml.etree.Element):
        pass
