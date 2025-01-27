from enum import Enum

from lxml import etree


class Accidental(Enum):
    """ Enum representation of an accidental. """
    SHARP = "♯"
    FLAT = "♭"
    NATURAL = "♮"

    def glance(self):
        """ Returns a short easily readable string for this accidental."""
        if self == Accidental.NATURAL:
            return ""
        return self.value

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
