import logging
from dataclasses import dataclass
from typing import Optional

from lxml.etree import Element

from pymusic.xml_conversion.bar_attributes import BarAttributesBuilder, create_bar_attributes_builder

log = logging.getLogger("bar")


@dataclass
class BarBuilder:
    number: int
    attributes_builder: Optional[BarAttributesBuilder] = None


def create_bar_builder(measure_element: Element) -> BarBuilder:
    builder = BarBuilder(measure_element.attrib["number"])
    log.info(f"Creating builder for bar: {builder.number}")

    # TODO -> handle none case.
    builder.attributes_builder = create_bar_attributes_builder(measure_element.find("attributes"))

    return builder
