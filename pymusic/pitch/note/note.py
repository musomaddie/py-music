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


class Note(Enum):
    """ Stores information relating to a single note (in notation). i.e. Eb and D# will be a different note,
    despite being the same pitch."""

    @dataclass
    class Data:
        """ note data """
        note_name: NoteName
        accidental: Accidental

    A = Data(NoteName.A, Accidental.NATURAL)
    A_FLAT = Data(NoteName.A, Accidental.FLAT)
    A_SHARP = Data(NoteName.A, Accidental.SHARP)
    B = Data(NoteName.B, Accidental.NATURAL)
    B_FLAT = Data(NoteName.B, Accidental.FLAT)
    B_SHARP = Data(NoteName.B, Accidental.SHARP)
    C = Data(NoteName.C, Accidental.NATURAL)
    C_FLAT = Data(NoteName.C, Accidental.FLAT)
    C_SHARP = Data(NoteName.C, Accidental.SHARP)
    D = Data(NoteName.D, Accidental.NATURAL)
    D_FLAT = Data(NoteName.D, Accidental.FLAT)
    D_SHARP = Data(NoteName.D, Accidental.SHARP)
    E = Data(NoteName.E, Accidental.NATURAL)
    E_FLAT = Data(NoteName.E, Accidental.FLAT)
    E_SHARP = Data(NoteName.E, Accidental.SHARP)
    F = Data(NoteName.F, Accidental.NATURAL)
    F_FLAT = Data(NoteName.F, Accidental.FLAT)
    F_SHARP = Data(NoteName.F, Accidental.SHARP)
    G = Data(NoteName.G, Accidental.NATURAL)
    G_FLAT = Data(NoteName.G, Accidental.FLAT)
    G_SHARP = Data(NoteName.G, Accidental.SHARP)

    @property
    def note_name(self):
        return self.value.note_name

    @property
    def accidental(self):
        return self.value.accidental

    def glance(self):
        """ Returns an easy-to-read string representation of this note."""
        return f"{self.note_name.value}{self.accidental.value}"
