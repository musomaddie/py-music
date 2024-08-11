""" Logic regarding notes using the piano keyboard. """
from abc import ABC, abstractmethod
from dataclasses import dataclass

from pymusic.pitch.interval import Interval
from pymusic.pitch.note import Note


class KeyNote(ABC):
    """ Parent class representing a note on the piano keyboard. """

    @abstractmethod
    def glance(self, use_sharp: bool):
        """ Quickly print the note represented. """
        pass

    @abstractmethod
    def get_note(self, accidental_hint: str):
        """ Get the corresponding note from this key. """


@dataclass
class WhiteKey(KeyNote):
    """ Corresponds to a white note on a piano keyboard. """
    note: Note

    def glance(self, use_sharp: bool):
        return self.note.glance()

    def get_note(self, accidental_hint: str):
        return self.note


@dataclass
class BlackKey(KeyNote):
    """ Corresponds to a black note on a piano keyboard. """
    sharp_note: Note
    flat_note: Note

    def glance(self, use_sharp: bool):
        if use_sharp:
            return self.sharp_note.glance()
        return self.flat_note.glance()

    def get_note(self, accidental_hint: str):
        if accidental_hint == "♭":
            return self.flat_note
        return self.sharp_note


octave = [
    WhiteKey(Note.A),
    BlackKey(Note.A_SHARP, Note.B_FLAT),
    WhiteKey(Note.B),
    WhiteKey(Note.C),
    BlackKey(Note.C_SHARP, Note.D_FLAT),
    WhiteKey(Note.D),
    BlackKey(Note.D_SHARP, Note.E_FLAT),
    WhiteKey(Note.E),
    WhiteKey(Note.F),
    BlackKey(Note.F_SHARP, Note.G_FLAT),
    WhiteKey(Note.G),
    BlackKey(Note.G_SHARP, Note.A_FLAT)
]


def _find_starting_idx(starting_note: Note):
    octave_name_sharps = [note.glance(True) for note in octave]
    octave_name_flats = [note.glance(False) for note in octave]

    try:
        idx = octave_name_sharps.index(starting_note.glance())
    except ValueError:
        # This will raise another ValueError for any double sharp / flat notes or B#/Cb or E#/Fb.
        idx = octave_name_flats.index(starting_note.glance())
    return idx


def find_note_from_number_of_semitones(starting_note: Note, semitones: int):
    """ Returns the note the number of given number of semitones away from the starting note. """
    starting_idx = _find_starting_idx(starting_note)
    keynote = octave[(starting_idx + semitones) % len(octave)]
    return keynote.get_note(starting_note.accidental.value)


def find_note_from_interval(starting_note: Note, interval: Interval):
    """ Returns the note which is the interval away from the starting note."""
    return find_note_from_number_of_semitones(starting_note, interval.n_semitones)
