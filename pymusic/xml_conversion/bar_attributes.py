from dataclasses import dataclass
from typing import Optional

from lxml.etree import Element

from pymusic.xml_conversion.key import KeyBuilder, create_key_builder
from pymusic.xml_conversion.time_signature import TimeSignatureBuilder, create_time_signature_builder


@dataclass
class BarAttributesBuilder:
    """ Represents attributes connected to a bar, as defined by musicXML.


    (Plan) of what happens with its children.
        - divisions: delegates to a time builder (is important to determine relative note lengths).
        - key: delegates to key builder
        - time: delegates to time builder (if present)
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
    # If the time signature is absent we default to using the one from the bar before.
    time_signature_builder: Optional[TimeSignatureBuilder] = None
    key_builder: Optional[KeyBuilder] = None


def create_bar_attributes_builder(attributes_element: Element) -> BarAttributesBuilder:
    builder = BarAttributesBuilder()

    # TODO -> handle the time sig being absent.
    builder.time_signature_builder = create_time_signature_builder(attributes_element)
    builder.key_builder = create_key_builder(attributes_element.find("key"))

    # TODO -> handle the key being absent

    return builder
