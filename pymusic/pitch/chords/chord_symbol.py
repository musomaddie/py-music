"""
Handles a chord symbol (i.e. name / guitar chart above the main system).
Corresponds to harmony music xml element.
"""
import logging
from dataclasses import dataclass, field

from lxml import etree

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.chords.chord_type import ChordType
from pymusic.pitch.interval import Interval
from pymusic.pitch.note import Note
from pymusic.pitch.piano_keys.piano import find_note_from_interval, find_note_from_number_of_semitones

logger = logging.getLogger("chord_symbol")


def _generate_all_notes(root_note: Note, chord_type: ChordType) -> list[Note]:
    def get_next_note(interval: Interval) -> Note:
        if interval == Interval.UNI:
            return root_note
        naturalised_key_note = find_note_from_interval(
            # Get the natural version of the note passed. Since the inversion of a natural is a natural this will
            # always work.
            find_note_from_number_of_semitones(
                root_note, root_note.accidental.inversion().interval
            ).get_note(Accidental.NATURAL),
            interval).get_note(Accidental.NATURAL)

        return find_note_from_interval(root_note, interval).get_note_from_name(naturalised_key_note.note_name)

    return [get_next_note(itl) for itl in chord_type.intervals]


@dataclass
class ChordSymbol:
    """ Represents a chord symbol. """
    root_note: Note
    chord_type: ChordType
    all_notes: list[Note] = field(init=False)

    def __post_init__(self):
        self.all_notes = _generate_all_notes(self.root_note, self.chord_type)

    def glance(self):
        """ Returns an easy-to-read string representation of this chord symbol. """
        return f"{self.root_note.glance()} {self.chord_type.desc}"

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
