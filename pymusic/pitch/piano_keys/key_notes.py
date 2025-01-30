from abc import ABC, abstractmethod
from dataclasses import dataclass

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.note import Note, NoteName


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
    def get_note_from_name(self, name: NoteName):
        """ Returns the specific note from this key that matches the given name. Throws ValueError if this does not
        exist."""

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
        if accidental == self.note.accidental or accidental == Accidental.NATURAL:
            return self.note

        if accidental == Accidental.SHARP:
            return self.alt_with_sharps
        if accidental == Accidental.FLAT:
            return self.alt_with_flats
        raise ValueError(f"Don't know how to handle {accidental.glance()}")

    def get_note_from_name(self, name: NoteName):
        match name:
            case self.note.note_name:
                return self.note
            case self.alt_with_sharps.note_name:
                return self.alt_with_sharps
            case self.alt_with_flats:
                return self.alt_with_flats
            case _:
                ValueError(f"No note with {name} found in {self}")

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

    def get_note_from_name(self, name: NoteName):
        match name:
            case self.sharp_note.note_name:
                return self.sharp_note
            case self.flat_note.note_name:
                return self.flat_note
            case _:
                ValueError(f"No note with {name} found in {self}")

    def matches(self, other_note: Note):
        return self.flat_note == other_note or self.sharp_note == other_note
