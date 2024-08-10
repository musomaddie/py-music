""" Note class. """
from dataclasses import dataclass
from enum import Enum

from pymusic.pitch.accidentals import Accidental


class NoteName(Enum):
    """ Matches the note name (without accidentals). """
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"


@dataclass
class Note:
    """ Stores information relating to a single note (in notation). i.e. Eb and D# will be a different note,
    despite being the same pitch."""
    name: NoteName
    accidental: Accidental

    def glance(self):
        """ Returns an easy-to-read string representation of this note."""
        return f"{self.name.value}{self.accidental.value}"
