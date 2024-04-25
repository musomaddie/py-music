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
        """ Creates a measure builder from the given xml. """
        builder = MeasureBuilder(measure_xml.attrib["number"], measure_xml)
        log.warning(f"Starting to build {builder}")

        # TODO -> figure out what to do with print. (should this just go into additional info?,
        #  or a specialised layout place??), and at the very least document it.
        # TODO -> measure-layout -> either document or decide what to do with.

        for child in measure_xml:
            if child.tag == "attributes":
                # TODO - save result.
                attributes = AttributesBuilder.create_from_attribute_xml(child)
            elif child.tag == "print":
                continue  # Display only, not helpful
            else:
                log.error(f"\tUnhandled attribute {child}")
        # TODO - figure out how to store attributes in _additional_info. (or if I need to).

        return builder
