"""
   <attributes>
    <divisions>256</divisions>
    <key color="#000000">
     <fifths>-2</fifths>
     <mode>major</mode>
    </key>
    <time color="#000000">
     <beats>4</beats>
     <beat-type>4</beat-type>
    </time>
    <staves>1</staves>
    <clef number="1" color="#000000">
     <sign>G</sign>
     <line>2</line>
    </clef>
    <staff-details number="1" print-object="yes" />
   </attributes>

   https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/attributes/
"""
import logging
from dataclasses import dataclass, field

import lxml.etree
from lxml import etree

from pymusic.key.key import KeyBuilder
from pymusic.parts.clef import Clef
from pymusic.rhythm.time_signature import TimeSignatureBuilder

log = logging.getLogger("attributes")


# Worry about what exactly to attach this to later, for now let's just the relevant parts processed.

@dataclass
class AttributesBuilder:
    """ A builder for an attributes' element.
    (https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/attributes/).

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
        - directive: TODO - seems deprecated?
        - measure-style: TODO - will need for multi rest, and some other fancy things.
    """
    og_xml: lxml.etree.Element
    _additional_info: list = field(default_factory=list)

    @staticmethod
    def create_from_attribute_xml(attribute_xml: etree.Element) -> 'AttributesBuilder':
        builder = AttributesBuilder(attribute_xml)
        log.warning(f"Building {builder} ...")

        # TODO -> have a better way of representing that it isn't present, and we should use the previous one instead
        # (if it exists). -> possibly just take in  the previous attributes instead, and use references.
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
                time_signature = TimeSignatureBuilder.create_from_xml(
                    attribute_xml.find("divisions"), child)
            elif child.tag == "key":
                key = KeyBuilder.create_from_key_xml(child)
            elif child.tag == "staves":
                # TODO -> handle multiple staves.
                number_of_staves = 1
            elif child.tag == "clef":
                clef = Clef.create_from_xml(child)
            else:
                log.error(f"\tUnhandled attribute {child}")

        return builder
