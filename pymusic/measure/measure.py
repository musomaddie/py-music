"""
Bar (children)
- attrib (in line)
    - number
    - width
- print info things
- attributes
    - divisions
    - key
        - fifths
        - mode
    - time
        -beats
        -beat type
    - staves
    - clef (number, color)
        - sign, line
    - staff details
- harmony (color)
    - root
        - step, alter
    - kind
    - frame
        - strings, frets, note, staff
- direction
    - type, (words)
    - voice, staff
- direction (directive)
- note


"""
import logging
from dataclasses import dataclass, field

from lxml import etree

from pymusic.attributes import AttributesBuilder

log = logging.getLogger("measure")


@dataclass
class MeasureBuilder:
    """
    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/measure-partwise/
    """
    measure_id: str
    og_xml: etree.Element
    _additional_info: list = field(default_factory=list)

    @staticmethod
    def create_from_measure_xml(measure_xml: etree.Element) -> 'MeasureBuilder':
        builder = MeasureBuilder(measure_xml.attrib["number"], measure_xml)
        log.warning(f"Starting to build {builder}")

        for child in measure_xml:
            if child.tag == "attributes":
                AttributesBuilder.create_from_attribute_xml(child)
            else:
                builder._additional_info.append(child)

        # TODO - figure out how to store attributes in _additional_info. (or if I need to).

        return builder
