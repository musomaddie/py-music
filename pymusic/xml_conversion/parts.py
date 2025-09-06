import logging
from dataclasses import dataclass, field

from lxml.etree import Element

from pymusic.xml_conversion.musicxml_identifiers import PART_ID
from pymusic.xml_conversion.part import create_part_builder, PartBuilder

log = logging.getLogger("parts")


@dataclass
class PartsBuilder:
    all_part_builders: list[PartBuilder] = field(default_factory=list)

    def glance(self) -> str:
        return "[" + ", ".join([
            part.name for part in self.all_part_builders
        ]) + "]"

    def find_corresponding_part(self, required_id: str) -> PartBuilder:
        for builder in self.all_part_builders:
            if builder.id == required_id:
                return builder
        raise Exception(f"Could not find a part builder with the ID: {required_id}")

    def add_bars_for_all_parts(self, parts_elements: Element):
        for part_element in parts_elements:
            # Find the corresponding part and add to its bars.
            corresponding_part_builder = self.find_corresponding_part(part_element.attrib["id"])
            corresponding_part_builder.add_all_bars(part_element.findall("measure"))

            # TODO -> repeat for all instruments
            break


def add_all_parts(score_parts_elements: list[Element]) -> list[PartBuilder]:
    return [
        create_part_builder(part_element) for part_element in score_parts_elements
    ]


def create_parts_builder(part_list_element: Element) -> PartsBuilder:
    builder = PartsBuilder()
    builder.all_part_builders = add_all_parts(part_list_element.findall(PART_ID))
    log.debug(f"created parts builder with: {builder.glance()}")
    return builder
