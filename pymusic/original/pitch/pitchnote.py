""" PitchNote class. """
from enum import Enum

from pymusic.original.pitch.accidentals import Accidental


class NoteName(Enum):
    """ Matches the note name (without accidentals). """
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"

    @staticmethod
    def from_str(note: str) -> 'NoteName':
        for nn in NoteName:
            if nn.value == note:
                return nn


class PitchNote(Enum):
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

    # Double sharps and flats (some excluded like C double flat).
    A_SHARP_2 = NoteName.A, Accidental.SHARP_2
    A_FLAT_2 = NoteName.A, Accidental.FLAT_2
    B_FLAT_2 = NoteName.B, Accidental.FLAT_2
    C_SHARP_2 = NoteName.C, Accidental.SHARP_2
    D_FLAT_2 = NoteName.D, Accidental.FLAT_2
    D_SHARP_2 = NoteName.D, Accidental.SHARP_2
    E_FLAT_2 = NoteName.E, Accidental.FLAT_2
    F_SHARP_2 = NoteName.F, Accidental.SHARP_2
    G_FLAT_2 = NoteName.G, Accidental.FLAT_2
    G_SHARP_2 = NoteName.G, Accidental.SHARP_2

    def glance(self):
        """ Returns an easy-to-read string representation of this note."""
        return f"{self.note_name.value}{self.accidental.glance()}"

    @staticmethod
    def corresponding_note(note_name: str, accidental: Accidental):
        """ Returns the note corresponding to the given note name and alter (which reflects the accidental)."""
        for note in PitchNote:
            if note.note_name.value == note_name and note.accidental == accidental:
                return note

        raise ValueError(f"Unrecognised note {note_name} ({accidental})")

    @staticmethod
    def corresponding_note_from_str(note_str: str) -> 'PitchNote':
        if len(note_str) == 1:
            return PitchNote.corresponding_note(note_str, Accidental.NATURAL)
        if len(note_str) == 2:
            return PitchNote.corresponding_note(note_str[0], Accidental.from_str(note_str[1]))

        raise ValueError(f"Unrecognized note {note_str}")
