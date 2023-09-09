import logging
from dataclasses import dataclass, field

import lxml.etree

from pymusic import globalvars, update_prefix

log = logging.getLogger("part")


@dataclass
class Part:
    """
    Links to bars with notes for this instrument only.
    """
    part_id: str
    part_name: str
    part_abbr: str


@dataclass
class PartBuilder:
    """
    Builds a part instance.
    """
    part_id: str
    og_xml: lxml.etree.Element
    _part_name: str = ""
    _part_abbr: str = ""
    _additional_info: list = field(default_factory=list)
    _interesting_children = [
        "part-name",
        "part-abbreviation"]

    def __str__(self):
        return f"{self._part_name} ({self._part_abbr}) [{self.part_id}]"

    @staticmethod
    def create_from_part_list_xml(part_list_xml: lxml.etree.Element) -> Part:
        update_prefix(":", "-> Part Builder:", unless_contains="Part Builder")
        builder = PartBuilder(part_list_xml.attrib["id"], part_list_xml)
        log.info(f"{globalvars.prefix} [{builder.part_id}]")

        builder.process_children()
        return builder.build()

    def build(self) -> Part:
        log.info(f"{globalvars.prefix} {self} built.")
        return Part(self.part_id, self._part_name, self._part_abbr)

    def process_children(self):
        for child in self.og_xml:
            if child.tag == "part-name":
                self._part_name = child.text
            elif child.tag == "part-abbreviation":
                self._part_abbr = child.text
            else:
                self._additional_info.append(child)

        log.debug(f"{globalvars.prefix} additional info: {self._additional_info}")
