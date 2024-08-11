""" Note class. """
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

    def __init__(self, note_name: NoteName, accidental: Accidental):
        self.note_name = note_name
        self.accidental = accidental

    A = NoteName.A, Accidental.NATURAL
    A_FLAT = NoteName.A, Accidental.FLAT
    A_SHARP = NoteName.A, Accidental.SHARP
    B = NoteName.B, Accidental.NATURAL
    B_FLAT = NoteName.B, Accidental.FLAT
    B_SHARP = NoteName.B, Accidental.SHARP
    C = NoteName.C, Accidental.NATURAL
    C_FLAT = NoteName.C, Accidental.FLAT
    C_SHARP = NoteName.C, Accidental.SHARP
    D = NoteName.D, Accidental.NATURAL
    D_FLAT = NoteName.D, Accidental.FLAT
    D_SHARP = NoteName.D, Accidental.SHARP
    E = NoteName.E, Accidental.NATURAL
    E_FLAT = NoteName.E, Accidental.FLAT
    E_SHARP = NoteName.E, Accidental.SHARP
    F = NoteName.F, Accidental.NATURAL
    F_FLAT = NoteName.F, Accidental.FLAT
    F_SHARP = NoteName.F, Accidental.SHARP
    G = NoteName.G, Accidental.NATURAL
    G_FLAT = NoteName.G, Accidental.FLAT
    G_SHARP = NoteName.G, Accidental.SHARP

    def glance(self):
        """ Returns an easy-to-read string representation of this note."""
        return f"{self.note_name.value}{self.accidental.value}"

    @staticmethod
    def corresponding_note(note_name: str, accidental: Accidental):
        """ Returns the note corresponding to the given note name and alter (which reflects the accidental)."""
        for note in Note:
            if note.note_name.value == note_name and note.accidental == accidental:
                return note

        raise ValueError(f"Unrecognised note {note_name} ({accidental})")
