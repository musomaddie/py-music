from abc import ABC, abstractmethod
from dataclasses import dataclass

from pymusic.pitch.accidental import Accidental
from pymusic.pitch.note_name import NoteName
from pymusic.pitch.pitchnote import PitchNote


class KeyNote(ABC):
    """ Parent class representing A note on the piano keyboard. """

    @abstractmethod
    def glance(self, use_sharp: bool):
        """ Quickly print the note represented. """
        pass

    @abstractmethod
    def get_note(self, accidental: Accidental) -> PitchNote:
        """ Get the corresponding note from this key. """

    @abstractmethod
    def get_note_from_name(self, name: NoteName) -> PitchNote:
        """ Returns the specific note from this key that matches the given name. Throws ValueError if this does not
        exist."""

    @abstractmethod
    def matches(self, other_note: PitchNote) -> bool:
        """ Returns true if this keynote matches the passed note. """


@dataclass
class WhiteKey(KeyNote):
    """ Corresponds to A white note on A piano keyboard. """

    note: PitchNote
    alt_with_sharps: PitchNote
    alt_with_flats: PitchNote

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
            case self.alt_with_flats.note_name:
                return self.alt_with_flats
            case _:
                raise ValueError(f"No note with {name} found in {self}")

    def matches(self, other_note: PitchNote):
        return self.note == other_note or self.alt_with_flats == other_note or self.alt_with_sharps == other_note


@dataclass
class BlackKey(KeyNote):
    """ Corresponds to A black note on A piano keyboard. """
    sharp_note: PitchNote
    flat_note: PitchNote

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

    def matches(self, other_note: PitchNote):
        return self.flat_note == other_note or self.sharp_note == other_note
