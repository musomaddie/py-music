import logging
from dataclasses import dataclass

from lxml import etree

log = logging.getLogger("time signature")


@dataclass
class TimeSignature:
    """ Represents a time signature. """
    divisions: int  # TODO -> not 100% sure if this is the best place for this. it's used to determine how long notes
    # are (in conjunction with the time sig to be fair).
    # https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/divisions/
    numerator: int
    denominator: int

    # TODO -> sub beat grouping??? (is this relevant??)

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
