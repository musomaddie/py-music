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

from pymusic.attributes import Attributes
from pymusic.pitch import ChordSymbol

log = logging.getLogger("measure")


@dataclass
class Measure:
    """
    (also known as bar)
    https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/measure-partwise/
    """
    measure_id: str
    og_xml: etree.Element
    _additional_info: list = field(default_factory=list)

    @staticmethod
    def from_xml(measure_xml: etree.Element) -> 'Measure':
        return _MeasureBuilder(measure_xml).build()


class _MeasureBuilder:

    def __init__(self, og_xml):
        self.og_xml = og_xml
        self._find_id()
        log.warning(f"Starting to build measure {self._id}")
        self._process_children()

    def _process_children(self):
        # TODO -> figure out what to do with print. (should this just go into additional info?,
        #  or a specialised layout place??), and at the very least document it.
        # TODO -> measure-layout -> either document or decide what to do with.

        # TODO -> some of this information should not be buried in the part but also extracted to an external place
        #  to make it easy  to get info about the piece (i.e. the key (and any key changes)..
        for child in self.og_xml:
            if child.tag == "attributes":
                # TODO - save result.
                attributes = Attributes.from_xml(child)
                # TODO -> save attributes!
            elif child.tag == "print":
                continue  # Display only, not helpful
            elif child.tag == "harmony":
                chord = ChordSymbol.create_from_xml(child)
            else:
                log.warning(f"Unhandled attribute {child}")
        # TODO - figure out how to store attributes in _additional_info. (or if I need to).

    def _find_id(self):
        self._id = self.og_xml.attrib["number"]

    def build(self) -> Measure:
        return Measure(self._id, self.og_xml)
