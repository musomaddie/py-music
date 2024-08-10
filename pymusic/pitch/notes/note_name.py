""" NoteName stuff. """
from dataclasses import dataclass

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.notes.octave_note_name import OctaveNoteName


@dataclass
class NoteName:
    """ represents a single note. """
    name: OctaveNoteName
    accidental: Accidental

    def glance(self):
        """ Nicely readable thing. """
        return f"{self.name.name}{self.accidental.shorthand}"

    def __str__(self):
        return self.glance()

    def __repr__(self):
        return self.glance()
