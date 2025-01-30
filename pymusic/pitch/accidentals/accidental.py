from enum import Enum

from lxml import etree


class Accidental(Enum):
    """ Enum representation of an accidental. """

    def __init__(self, symbol: str, interval: int):
        self.symbol = symbol
        self.interval = interval

    SHARP = "♯", 1
    FLAT = "♭", -1
    NATURAL = "♮", 0

    # TODO -> the following accidentals are not yet supported by 'from' methods.
    SHARP_2 = "♯♯", 2
    FLAT_2 = "♭♭", -2

    def glance(self):
        """ Returns a short easily readable string for this accidental."""
        if self == Accidental.NATURAL:
            return ""
        return self.symbol

    def inversion(self):
        match self:
            case Accidental.NATURAL:
                return Accidental.NATURAL
            case Accidental.SHARP:
                return Accidental.FLAT
            case Accidental.FLAT:
                return Accidental.SHARP
            case Accidental.FLAT_2:
                return Accidental.SHARP_2
            case Accidental.SHARP_2:
                return Accidental.FLAT_2

    @staticmethod
    def from_xml(alter_xml: etree.Element) -> 'Accidental':
        """ Returns the accidental string from this alter bit."""
        if alter_xml is None:
            return Accidental.NATURAL

        number = alter_xml.text
        if number == "1":
            return Accidental.SHARP
        elif number == "-1":
            return Accidental.FLAT

        raise ValueError(f"Can't handle alter text of {alter_xml}")

    @staticmethod
    def from_int(i: int) -> 'Accidental':
        """ Returns the accidental corresponding to the given number. (negative numbers = flat)"""
        if i == 0:
            return Accidental.NATURAL
        elif i > 0:
            return Accidental.SHARP
        return Accidental.FLAT

    @staticmethod
    def from_str(accidental_str: str) -> 'Accidental':
        if accidental_str == "♭":
            return Accidental.FLAT
        if accidental_str == "♯":
            return Accidental.SHARP
        else:
            return Accidental.NATURAL
