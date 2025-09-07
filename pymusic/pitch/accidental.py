from enum import Enum
from typing import Optional

from lxml.etree import Element


class Accidental(Enum):
    """ Enum representation of an accidental. """

    def __init__(self, symbol: str, n_semitones: int):
        self.symbol = symbol
        self.n_semitones = n_semitones

    SHARP = "♯", 1
    FLAT = "♭", -1
    NATURAL = "♮", 0
    SHARP_2 = "𝄪", 2
    FLAT_2 = "𝄫", -2

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
    def from_int(i: int) -> 'Accidental':
        for accidental in Accidental:
            if i == accidental.n_semitones:
                return accidental
        raise ValueError(f"Unrecognized accidental by {i} semitones")

    @staticmethod
    def from_fifths(n_fifths: int) -> 'Accidental':
        if n_fifths > 0:
            return Accidental.SHARP
        if n_fifths < 0:
            return Accidental.FLAT
        return Accidental.NATURAL

    @staticmethod
    def from_str(s: str) -> 'Accidental':
        # Special case for natural
        if s == "":
            return Accidental.NATURAL
        for accidental in Accidental:
            if s == accidental.symbol:
                return accidental
        raise ValueError(f"Unrecognized accidental with string: {s}")


def create_accidental_from_element(element: Optional[Element]) -> Accidental:
    if element is None:
        return Accidental.NATURAL
    return Accidental.from_int(int(element.text))
