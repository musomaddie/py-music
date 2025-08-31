import logging
from dataclasses import dataclass

from lxml.etree import Element

from pymusic.xml_conversion.musicxml_identifiers import INSTRUMENT_NAME, PART_ABBR

log = logging.getLogger("part")


@dataclass
class PartBuilder:
    id: str
    name: str = ""
    abbr: str = ""

    def glance(self) -> str:
        return f"{self.name} ({self.id})"


def get_name(part_element: Element) -> str:
    return part_element.find(INSTRUMENT_NAME).text


def get_abbr(part_element: Element) -> str:
    # TODO -> handle the case where the abbreviation doesn't exist (use name instead)
    return part_element.find(PART_ABBR).text


def create_part_builder(part_element: Element) -> PartBuilder:
    builder = PartBuilder(part_element.attrib["id"])
    builder.name = get_name(part_element)
    builder.abbr = get_abbr(part_element)

    log.debug(f"created part builder for {builder.glance()}")
    return builder
