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


@dataclass
class TimeSignatureBuilder:
    """ A builder for the time signature element. """

    divisions_og_xml: etree.Element
    time_og_xml: etree.Element
    _divisions: int
    _numerator: int
    _denominator: int

    def build(self) -> TimeSignature:
        """ Returns a time signature built from the provided builder values. """
        return TimeSignature(self._divisions, self._numerator, self._denominator)

    @staticmethod
    def create_from_xml(
            divisions_xml: etree.Element,
            time_xml: etree.Element,
    ) -> TimeSignature:
        """ A builder for the time signature, taking into account divisions. """
        time_sig = TimeSignatureBuilder(
            divisions_xml,
            time_xml,
            int(divisions_xml.text),
            int(time_xml.find("beats").text),
            int(time_xml.find("beat-type").text)
        ).build()
        log.debug(time_sig)
        log.info(f"In {time_sig.glance()} time")
        return time_sig
