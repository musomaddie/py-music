import logging
from dataclasses import dataclass

from lxml import etree

log = logging.getLogger("time signature")


@dataclass
class TimeSignature:
    """ Represents a time signature. """
    divisions: int
    numerator: int
    denominator: int

    def glance(self) -> str:
        """ Returns a string representing this time signature at a glance."""
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def from_xml(divisions_xml: etree.Element, time_xml: etree.Element) -> 'TimeSignature':
        time_sig = TimeSignature(
            int(divisions_xml.text),
            int(time_xml.find("beats").text),
            int(time_xml.find("beat-type").text)
        )
        log.debug(time_sig)
        log.info(f"In {time_sig.glance()} time")
        return time_sig
