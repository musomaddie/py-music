import logging
from dataclasses import dataclass, field

import lxml.etree
from lxml import etree

from pymusic import globalvars
from pymusic.measure import MeasureBuilder

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

    def __repr__(self):
        return f"{self._part_name} [{self.part_id}]"

    def build(self) -> Part:
        log.debug(f"{globalvars.prefix} {self} built.")
        return Part(self.part_id, self._part_name, self._part_abbr)

    def glance(self) -> str:
        """ Returns a string representing this part at a glance. """
        return f"{self._part_name} ({self.part_id})"

    @staticmethod
    def create_from_part_list_xml(part_list_xml: lxml.etree.Element) -> 'PartBuilder':
        builder = PartBuilder(part_list_xml.attrib["id"], part_list_xml)
        log.debug(f"starting to build {builder.part_id}")
        builder.process_children()

        log.info(f"Built information for {builder.glance()}")

        return builder

    def process_children(self):
        for child in self.og_xml:
            if child.tag == "part-name":
                self._part_name = child.text
            elif child.tag == "part-abbreviation":
                self._part_abbr = child.text
            else:
                self._additional_info.append(child)

    def add_measures(self, part_with_measures_xml: etree.Element):
        log.debug(f"Adding measures to {self}")
        for child in part_with_measures_xml:
            if child.tag == "measure":
                # TODO - actually add the measure, not just make it.
                MeasureBuilder.create_from_measure_xml(child)
                break
