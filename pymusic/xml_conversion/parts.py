import logging
from dataclasses import dataclass, field

from lxml.etree import Element

from pymusic.xml_conversion.musicxml_identifiers import PART_ID
from pymusic.xml_conversion.part import create_part_builder, PartBuilder

log = logging.getLogger("parts")


@dataclass
class PartsBuilder:
    all_part_builders: list = field(default_factory=list)

    def glance(self) -> str:
        return "[" + ", ".join([
            part.name for part in self.all_part_builders
        ]) + "]"


def add_all_parts(score_parts_elements: list[Element]) -> list[PartBuilder]:
    return [
        create_part_builder(part_element) for part_element in score_parts_elements
    ]


def create_parts_builder(part_list_element: Element) -> PartsBuilder:
    builder = PartsBuilder()
    builder.all_part_builders = add_all_parts(part_list_element.findall(PART_ID))
    log.debug(f"created parts builder with: {builder.glance()}")
    return builder
