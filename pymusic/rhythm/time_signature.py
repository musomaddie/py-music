import logging
from dataclasses import dataclass

from lxml import etree

log = logging.getLogger("time signature")


@dataclass
class TimeSignature:
    divisions: int
    numerator: int
    denominator: int


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
        log.info(time_sig)
        return time_sig
