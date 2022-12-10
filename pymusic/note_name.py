from dataclasses import dataclass
from enum import Enum

from pymusic.accidental import Accidental


class NoteName(Enum):
    """
    The names of each note in an octave as defined by `ASPN`_.

    Each octave starts at C, so the value assigned by the enum reflects this. Internal
    implementation of the `step data type`_ defined in Music XML.

    .. _`ASPN`: https://viva.pressbooks.pub/openmusictheory/chapter/aspn/
    .. _`step data type`: https://www.w3.org/2021/06/musicxml40/musicxml-reference/data-types/step/
    """
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    A = 6
    B = 7


def get_note_name_from_string(value: str):
    """
    Given the note name as a string, returns the matching enum.

    Is case-insensitive and will strip white space.

    :param value: the note name to look up
    :type value: str
    :return: The NoteName corresponding to the passed string
    :rtype: NoteName
    :raise ValueError: if the string passed is not a valid note name.
    """
    value = value.lower().strip().replace(" ", "")
    if value == "a":
        return NoteName.A
    elif value == "b":
        return NoteName.B
    elif value == "c":
        return NoteName.C
    elif value == "d":
        return NoteName.D
    elif value == "e":
        return NoteName.E
    elif value == "f":
        return NoteName.F
    elif value == "g":
        return NoteName.G

    raise ValueError(f"{value} is not a valid note name.")


@dataclass
class FullNoteName:
    """ Contains the full note name (including accidentals). """
    # TODO: improve documentation. & test.
    note_name: NoteName
    accidental: Accidental

    def _to_string(self):
        if self.accidental == Accidental.NONE:
            return self.note_name.name
        return f"{self.note_name.name} ({self.accidental.name})"

    def __hash__(self):
        return hash((self.note_name, self.accidental))

    def __eq__(self, other):
        if isinstance(other, FullNoteName):
            return self.note_name == other.note_name and self.accidental == other.accidental
        return False

    def __repr__(self):
        return self._to_string()

    def __str__(self):
        return self._to_string()


ALL_NOTE_NAMES = dict(
    zip([f"{name}{a}" for name in ["A", "B", "C", "D", "E", "F", "G"] for a in ["b", "", "#"]],
        [FullNoteName(n, a)
         for n in [NoteName.A, NoteName.B, NoteName.C, NoteName.D, NoteName.E, NoteName.F, NoteName.G]
         for a in [Accidental.FLAT, Accidental.NONE, Accidental.SHARP]]))

# Shorter variable for readability.
ann = ALL_NOTE_NAMES
keyboard_keys_ordered = [
    [ann["A"]],
    [ann["A#"], ann["Bb"]],
    [ann["B"], ann["Cb"]],
    [ann["C"], ann["B#"]],
    [ann["C#"], ann["Db"]],
    [ann["D"]],
    [ann["D#"], ann["Eb"]],
    [ann["E"], ann["Fb"]],
    [ann["F"], ann["E#"]],
    [ann["F#"], ann["Gb"]],
    [ann["G"]],
    [ann["G#"], ann["Ab"]]
]

all_doubles = [key for key in keyboard_keys_ordered if len(key) == 2]
v1, v2 = zip(*all_doubles)
EQUIVALENCE = dict(all_doubles) | dict(zip(v2, v1))
