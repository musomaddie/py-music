import logging
from dataclasses import dataclass, field

import lxml
from lxml import etree

from pymusic import globalvars, update_prefix
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
    _parts: list = field(default_factory=list)
    _additional_info: list = field(default_factory=list)
    _interesting_children_map = {
        "score-part": PartBuilder.create_from_part_list_xml
    }

    def __str__(self):
        return f"{self._parts}"

    @staticmethod
    def create_from_part_list_xml(part_list_xml: etree.Element) -> Parts:
        update_prefix(":", "-> PartsBuilder:")
        builder = PartsBuilder(part_list_xml)
        log.info(f"{globalvars.prefix} building")
        builder.process_children()

        return builder.build()

    def build(self) -> Parts:
        log.info(f"{globalvars.prefix} {self} built.")
        return Parts(self._parts)

    def process_children(self):
        for child in self.og_xml:
            if child.tag in self._interesting_children_map:
                self._parts.append(
                    self._interesting_children_map[child.tag](child))
            else:
                self._additional_info.append(child)
