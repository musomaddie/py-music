"""
Handles a chord symbol (i.e. name / guitar chart above the main system).
Corresponds to harmony music xml element.
"""
import logging
from dataclasses import dataclass

from lxml import etree

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.chords.chord_type import ChordType
from pymusic.pitch.note import Note
from pymusic.pitch.piano_keys import find_note_from_number_of_semitones

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

    def all_notes(self) -> list[Note]:
        """ Returns an (ordered) list of all notes contained in this chord, starting at the root. """
        # TODO -> add a dictionary of notes so we don't have to recalculate this??? -> not sure if its worth it.
        notes = []
        for interval in self.chord_type.intervals:
            new_note = find_note_from_number_of_semitones(
                starting_note=self.root_note, semitones=interval.n_semitones
                # TODO -> determine how to do this when the starting note isn't an accidental. (i.e. G major, F major).
            ).get_note(self.root_note.accidental)
            notes.append(new_note)
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
