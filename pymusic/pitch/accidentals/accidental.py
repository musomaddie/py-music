from enum import Enum

from lxml import etree


class Accidental(Enum):
    """ Enum representation of an accidental. """
    SHARP = "♯"
    FLAT = "♭"
    NATURAL = "♮"

    @staticmethod
    def corresponding_accidental(alter_xml: etree.Element) -> 'Accidental':
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
    def accidental_hint(number: int) -> str:
        """ Generates a string 'accidental hint' from the given number."""
        accidental = Accidental.NATURAL
        if number > 0:
            accidental = Accidental.SHARP
        elif number < 0:
            accidental = accidental.FLAT
        return accidental.value
