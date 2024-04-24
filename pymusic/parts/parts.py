import logging
from dataclasses import dataclass, field

import lxml
from lxml import etree

from .part import PartBuilder, Part

log = logging.getLogger("parts")


@dataclass
class Parts:
    parts: list[Part]


@dataclass
class PartsBuilder:
    """
    Builds a list of parts.
    """
    og_xml: lxml.etree.Element
    _additional_info: list = field(default_factory=list)
    _parts: dict[str, PartBuilder] = field(default_factory=dict)

    def __str__(self):
        return f"{self._parts}"

    def __repr__(self):
        return self._parts

    def glance(self):
        """ Returns a string representing all parts at a glance. """
        return "; ".join([part.glance() for part in self._parts.values()])

    @staticmethod
    def create_from_part_list_xml(part_list_xml: etree.Element) -> 'PartsBuilder':
        builder = PartsBuilder(part_list_xml)
        builder.process_children()
        log.debug(builder)
        log.info(f"Created initial parts: {builder.glance()}")
        return builder

    # def build(self) -> Parts:
    #     log.info(f"{globalvars.prefix} {self} built.")
    #     # return Parts(self._parts)

    def process_children(self):
        for child in self.og_xml:
            if child.tag == "score-part":
                self._parts[child.attrib["id"]] = PartBuilder.create_from_part_list_xml(child)
            else:
                self._additional_info.append(child)

    def add_measures_to_part(self, part_xml: etree.Element):
        self._parts[part_xml.attrib["id"]].add_measures(part_xml)
