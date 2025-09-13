from dataclasses import dataclass
from typing import Optional

from lxml.etree import Element

from pymusic.articulation.slur_marker import SlurMarker


@dataclass
class SlurBuilder:
    slur_marker: SlurMarker


def create_slur_builder(notations_element: Optional[Element]) -> Optional[SlurBuilder]:
    # TODO figure out how to handle notes in the middle of a slur.
    if notations_element is None:
        return None

    slur_xml = notations_element.find("slur")
    if slur_xml is None:
        return None

    match slur_xml.attrib.get("type"):
        case "start":
            return SlurBuilder(SlurMarker.START)
        case "stop":
            return SlurBuilder(SlurMarker.END)
        case _:
            raise ValueError(f"Slur type {slur_xml.attrib.get('type')} is not supported")
