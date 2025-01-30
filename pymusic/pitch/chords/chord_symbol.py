"""
Handles a chord symbol (i.e. name / guitar chart above the main system).
Corresponds to harmony music xml element.
"""
import logging
from dataclasses import dataclass

from lxml import etree

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.chords.chord_type import ChordType
from pymusic.pitch.interval import Interval
from pymusic.pitch.note import Note
from pymusic.pitch.piano_keys.piano import KeyNote, find_note_from_interval, find_note_from_number_of_semitones

logger = logging.getLogger("chord_symbol")


@dataclass
class ChordSymbol:
    """ Represents a chord symbol. """
    root_note: Note
    chord_type: ChordType

    # TODO -> determine the notes found in this chord.
    def glance(self):
        """ Returns an easy-to-read string representation of this chord symbol. """
        return f"{self.root_note.glance()} {self.chord_type.desc}"

    def _determine_note_representation_with_context(self, key_note: KeyNote, interval: Interval):
        if key_note.matches(self.root_note):
            return key_note.get_note(self.root_note.accidental)
        if self.root_note.accidental == Accidental.NATURAL:
            return key_note.get_note(self.root_note.accidental)
        # TODO -> consider doing this by default when calculating the note instead of calculating and then checking.

        # We cannot simply return it based on accidentals like we do for the root since we will not give the correct
        # note names (for example Db major -> Db F Ab).
        naturalised_key_note = find_note_from_interval(
            find_note_from_number_of_semitones(
                self.root_note, self.root_note.accidental.inversion().interval
            ).get_note(Accidental.NATURAL),
            interval
        ).get_note(Accidental.NATURAL)

        return key_note.get_note_from_name(naturalised_key_note.note_name)

    def all_notes(self) -> list[Note]:
        """ Returns an (ordered) list of all notes contained in this chord, starting at the root. """

        # TODO -> this is being a pain with C# and Db chords -> I think for determining accidentals if the base note
        #  is an accidental we think on which of the options we want to return.
        notes = []
        for interval in self.chord_type.intervals:
            notes.append(self._determine_note_representation_with_context(
                find_note_from_interval(starting_note=self.root_note, interval=interval), interval))
        return notes

    #

    # note = find_note_from_number_of_semitones(
    #     starting_note=Note.C, semitones=(Interval.PERF_5.n_semitones * fifths)
    # ).get_note(
    #     Accidental.corresponding_accidental_from_int(fifths)
    # )

    @staticmethod
    def from_xml(harmony_xml: etree.Element) -> 'ChordSymbol':
        """ Returns a chord symbol created from the given XML. """

        chord_root_xml = harmony_xml.find("root")
        if chord_root_xml is None:
            # TODO -> add more detailed information to be displayed here.
            raise ValueError("No root element found, unable to process chord.")

        root_note = Note.corresponding_note(
            chord_root_xml.find("root-step").text,
            Accidental.from_xml(chord_root_xml.find("root-alter"))
        )

        kind_text = harmony_xml.find("kind").text
        chord = ChordSymbol(root_note, ChordType.from_text(kind_text))

        logger.info("Chord %s", chord)
        return chord
