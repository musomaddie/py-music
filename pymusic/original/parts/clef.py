""" Clef: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/clef/

Clefs are only useful when it comes to the display (we can extract note information regardless so, while I'm still
going to save it, I'm not going to even think about doing something special with it.
"""
import logging
from dataclasses import dataclass
from enum import Enum

from lxml import etree

log = logging.getLogger("clef")


class ClefSymbol(Enum):
    """ Corresponds to clef sign in music xml. """
    # TODO -> can I get some unicode or nerd font symbol here to help.
    TREBLE = 1
    BASS = 2
    ALTO = 3
    PERCUSSION = 4
    TAB = 5
    JIANPU = 6

    @staticmethod
    def get_symbol_from_string(s: str) -> 'ClefSymbol':
        """ Returns the clef symbol corresponding to the given string. Throws an exception if none found. """
        if s == "G":
            return ClefSymbol.TREBLE
        if s == "F":
            return ClefSymbol.BASS
        if s == "C":
            return ClefSymbol.ALTO
        if s == "percussion":
            return ClefSymbol.PERCUSSION
        if s == "tab":
            return ClefSymbol.TAB
        if s == "jianpu":
            return ClefSymbol.JIANPU
        raise KeyError(f"{s} is not a valid clef symbol.")


@dataclass
class Clef:
    """ Represents a musical clef."""
    symbol: ClefSymbol
    line: int

    def glance(self) -> str:
        """ Returns a string representing the clef at a glance. """
        return self.symbol.name

    @staticmethod
    def from_xml(clef_xml: etree.Element) -> 'Clef':
        """ Creates a clef from some given xml. """
        clef = Clef(
            symbol=ClefSymbol.get_symbol_from_string(clef_xml.find("sign").text),
            line=clef_xml.find("line").text)

        log.debug(clef)
        log.info(f"{clef.glance()} clef")
        return clef
