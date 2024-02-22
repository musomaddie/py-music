import logging
from dataclasses import dataclass

from lxml import etree

log = logging.getLogger("time signature")


@dataclass
class TimeSignatureBuilder:
    """ A builder for the time signature element. """

    divisions_og_xml: etree.Element
    time_og_xml: etree.Element
    divisions: int
    numerator: int
    denominator: int

    @staticmethod
    def create_from_xml(
            divisions_xml: etree.Element,
            time_xml: etree.Element,
    ) -> 'TimeSignatureBuilder':
        """ A builder for the time signature, taking into account divisions. """
        return TimeSignatureBuilder(
            divisions_xml,
            time_xml,
            int(divisions_xml.text),
            int(time_xml.find("beats").text),
            int(time_xml.find("beat-type").text)
        )
