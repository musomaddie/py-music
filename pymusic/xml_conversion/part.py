import logging
from dataclasses import dataclass, field

from lxml.etree import Element

from pymusic.xml_conversion.bar import BarBuilder, create_bar_builder
from pymusic.xml_conversion.musicxml_identifiers import INSTRUMENT_NAME, PART_ABBR

log = logging.getLogger("part")


@dataclass
class PartBuilder:
    id: str
    name: str = ""
    abbr: str = ""
    bars: list[BarBuilder] = field(default_factory=list)

    def glance(self) -> str:
        return f"{self.name} ({self.id})"

    def add_all_bars(self, measure_elements: list[Element]):
        log.debug(f"Adding bars to: {self.glance()}")
        for bar_element in measure_elements:
            bar_builder = create_bar_builder(bar_element)

            # TODO -> save the bar and save all bars.
            break


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
