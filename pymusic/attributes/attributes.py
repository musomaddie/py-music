""" https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/attributes/ """
import logging
from dataclasses import dataclass

from lxml import etree

from pymusic.key.key import Key
from pymusic.parts.clef import Clef
from pymusic.rhythm.time_signature import TimeSignature

log = logging.getLogger("attributes")


# Worry about what exactly to attach this to later, for now let's just the relevant parts processed.

@dataclass
class Attributes:
    """ Represents attributes connected to a bar, as defined by musicXML.


    (Plan) of what happens with its children.
        - divisions: delegates to a time builder (is important to determine relative note lengths).
        - key: delegates to key builder
        - time: delegates to time builder
        - staves: delegates to staves builder - if absent we create a builder which is a list of one (?)
        - part-symbol: additional info (but connected to staves)
        - instruments: (additional info) -> maybe reconsider.
        - clef: additional info
        - staff details: additional info
        - transpose: TODO, but additional info for now.
        - for part: TODO
        - directive: TODO - seems deprecated? (from Sibelius stores the tempo text stuff)
        - measure-style: TODO - will need for multi rest, and some other fancy things.
    """
    time_signature: TimeSignature
    key: Key
    clef: Clef

    def glance(self):
        """ Returns a string representing this attribute at a glance."""
        return f"{self.clef.glance()} clef, {self.key.glance()} in {self.time_signature.glance()} time"

    @staticmethod
    def from_xml(attribute_xml: etree.Element) -> 'Attributes':
        time_signature = None
        key = None
        number_of_staves = 1  # default if absent, according to musicxml documentation.
        clef = None  # TODO -> better default here.
        for child in attribute_xml:
            if child.tag == "divisions":
                # Divisions are only used in combination with time signature, but I want to explicitly mark them as
                # handled for my own peace of mind.
                pass
            elif child.tag == "time":
                # TODO -> divisions are optional!!!
                time_signature = TimeSignature.from_xml(attribute_xml.find("divisions"), child)
            elif child.tag == "key":
                key = Key.from_xml(child)
            elif child.tag == "staves":
                # TODO -> handle multiple staves.
                number_of_staves = 1
            elif child.tag == "clef":
                clef = Clef.from_xml(child)
            else:
                log.warning(f"\tUnhandled attribute {child}")

        attributes = Attributes(time_signature, key, clef)
        log.debug(attributes)
        log.info(attributes.glance())

        return attributes
