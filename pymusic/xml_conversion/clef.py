import logging
from dataclasses import dataclass

from lxml.etree import Element

from pymusic.pitch.clef_symbol import ClefSymbol

logger = logging.getLogger("clef")


@dataclass
class ClefBuilder:
    symbol: ClefSymbol = None
    line: int = 0

    def glance(self) -> str:
        """ Returns a string representation of the clef at an easy glance."""
        return self.symbol.symbol


def create_clef_builder(element: Element) -> ClefBuilder:
    builder = ClefBuilder()

    builder.symbol = ClefSymbol.from_str(element.find("sign").text)
    builder.line = int(element.find("line").text)
    logger.debug(f"Clef: {builder.glance()}")

    return builder
