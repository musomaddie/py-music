import logging
from dataclasses import dataclass

from lxml.etree import Element

log = logging.getLogger("time_signature")


@dataclass
class TimeSignatureBuilder:
    """ Represents a time signature. """
    numerator: int
    denominator: int
    # TODO -> not 100% sure if this is the best place for this. it's used to determine how long
    # notes are (in conjunction with the time sig to be fair). It's also optional so we should determine a sensible
    # default.
    # https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/divisions/
    divisions: int = 256

    def glance(self) -> str:
        return f"{self.numerator}/{self.denominator}"


def create_time_signature_builder(attributes_element: Element) -> TimeSignatureBuilder:
    time_element = attributes_element.find("time")
    builder = TimeSignatureBuilder(time_element.find("beats").text, time_element.find("beat-type").text)
    builder.divisions = attributes_element.find("divisions").text

    log.debug(f"In {builder.glance()} time")
    return builder
