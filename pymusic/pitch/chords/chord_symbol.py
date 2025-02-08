"""
Handles a chord symbol (i.e. name / guitar chart above the main system).
Corresponds to harmony music xml element.
"""
import logging
from dataclasses import dataclass, field

from lxml import etree

from pymusic.key import Mode, Key
from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.chords.chord_type import ChordType
from pymusic.pitch.interval import Interval
from pymusic.pitch.note import Note
from pymusic.pitch.piano_keys import find_note_from_number_of_semitones

logger = logging.getLogger("chord_symbol")
INTERVAL_TO_IDX = {
    "unison": 0,
    "2nd": 1,
    "3rd": 2,
    "4th": 3,
    "5th": 4,
    "6th": 5,
    "7th": 6
}


def _generate_all_notes(root_note: Note, chord_type: ChordType) -> list[Note]:
    # Create the major version of the scale and use the intervals from the chord with the note list somehow?
    octave_note_list = Key(Mode.MAJOR, root_note).octave

    def find_corresponding_idx(interval: Interval) -> int:
        for key, value in INTERVAL_TO_IDX.items():
            if key in " ".join(interval.names):
                return value

        raise ValueError(f"Cannot find the corresponding index for {interval.names}.")

    def find_note_from_octave(interval: Interval, major_interval: Interval) -> Note:
        major_note = octave_note_list[find_corresponding_idx(interval)]
        if interval == major_interval:
            return major_note

        # Otherwise get the difference between the two.
        diff_semitones = interval.n_semitones - major_interval.n_semitones
        return find_note_from_number_of_semitones(major_note, diff_semitones).get_note_from_name(major_note.note_name)

    notes = []
    for itl, maj_itl in zip(chord_type.intervals, ChordType.MAJ.intervals):
        notes.append(find_note_from_octave(itl, maj_itl))
    return notes


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
