""" Logic regarding notes using the piano keyboard. """
from abc import ABC, abstractmethod
from dataclasses import dataclass

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.interval import Interval
from pymusic.pitch.note import Note


class KeyNote(ABC):
    """ Parent class representing a note on the piano keyboard. """

    @abstractmethod
    def glance(self, use_sharp: bool):
        """ Quickly print the note represented. """
        pass

    @abstractmethod
    def get_note(self, accidental: Accidental):
        """ Get the corresponding note from this key. """

    @abstractmethod
    def matches(self, other_note: Note):
        """ Returns true if this keynote matches the passed note. """


@dataclass
class WhiteKey(KeyNote):
    """ Corresponds to a white note on a piano keyboard. """
    note: Note
    alt_with_sharps: Note
    alt_with_flats: Note

    def glance(self, use_sharp: bool):
        return self.note.glance()

    def get_note(self, accidental: Accidental):
        if accidental != self.note.accidental:
            if accidental == Accidental.SHARP:
                return self.alt_with_sharps
            else:
                return self.alt_with_flats

        return self.note

    def matches(self, other_note: Note):
        return self.note == other_note


@dataclass
class BlackKey(KeyNote):
    """ Corresponds to a black note on a piano keyboard. """
    sharp_note: Note
    flat_note: Note

    def glance(self, use_sharp: bool):
        if use_sharp:
            return self.sharp_note.glance()
        return self.flat_note.glance()

    def get_note(self, accidental: Accidental):
        if accidental == Accidental.FLAT:
            return self.flat_note
        return self.sharp_note

    def matches(self, other_note: Note):
        return self.flat_note == other_note or self.sharp_note == other_note


# TODO -> can octave go in its own package somewhere?
octave = [
    WhiteKey(Note.A, Note.G_SHARP_2, Note.B_FLAT_2),
    BlackKey(Note.A_SHARP, Note.B_FLAT),
    WhiteKey(Note.B, Note.A_SHARP_2, Note.C_FLAT),
    WhiteKey(Note.C, Note.B_SHARP, Note.D_FLAT_2),
    BlackKey(Note.C_SHARP, Note.D_FLAT),
    WhiteKey(Note.D, Note.C_SHARP_2, Note.E_FLAT_2),
    BlackKey(Note.D_SHARP, Note.E_FLAT),
    WhiteKey(Note.E, Note.D_SHARP_2, Note.F_FLAT),
    WhiteKey(Note.F, Note.E_SHARP, Note.G_FLAT_2),
    BlackKey(Note.F_SHARP, Note.G_FLAT),
    WhiteKey(Note.G, Note.F_SHARP_2, Note.A_FLAT_2),
    BlackKey(Note.G_SHARP, Note.A_FLAT)
]


def _from_octave(desired_idx: int) -> KeyNote:
    return octave[desired_idx % len(octave)]


def _find_starting_idx(starting_note: Note):
    octave_name_sharps = [note.glance(True) for note in octave]
    octave_name_flats = [note.glance(False) for note in octave]

    try:
        idx = octave_name_sharps.index(starting_note.glance())
    except ValueError:
        # This will raise another ValueError for any double sharp / flat notes or B#/Cb or E#/Fb.
        idx = octave_name_flats.index(starting_note.glance())
    return idx


def _note_idx(it, condition, default=-1):
    return next((i for i, elem in enumerate(it) if condition(elem)), default)


def _find_note_idx(searching_note: Note) -> int:
    return _note_idx(octave, lambda note: note.matches(searching_note))


def find_note_from_number_of_semitones(starting_note: Note, semitones: int) -> KeyNote:
    """ Returns the note the number of given number of semitones away from the starting note. """
    starting_idx = _find_note_idx(starting_note)
    return _from_octave(starting_idx + semitones)


def adjust_accidental(note: Note, desired_accidental: Accidental) -> Note:
    """ Takes in a note and returns the same note but with the desired accidental. Will return the note as is in the
    case of it already being the desired accidental.  (does not yet support double sharps / flats). """
    if note.accidental == desired_accidental:
        return note
    note_idx = _find_note_idx(note)
    octave_note = _from_octave(note_idx + desired_accidental.interval)
    return octave_note.get_note(desired_accidental)


def find_note_from_interval(starting_note: Note, interval: Interval) -> KeyNote:
    """ Returns the note which is the interval away from the starting note."""
    return find_note_from_number_of_semitones(starting_note, interval.n_semitones)
