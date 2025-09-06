"""
Handles a chord symbol (i.e. name / guitar chart above the main system).
Corresponds to harmony music xml element.
"""
import logging
from dataclasses import dataclass, field

from lxml import etree

from pymusic.original.key import Mode, Key
from pymusic.original.pitch.accidentals import Accidental
from pymusic.original.pitch.chords.chord_type import ChordType
from pymusic.original.pitch.interval import Interval
from pymusic.original.pitch.piano_keys.piano import (find_note_from_number_of_semitones)
from pymusic.original.pitch.pitchnote import PitchNote

logger = logging.getLogger("chord_symbol")


# TODO -> can the note generator stuff live in its own file??

@dataclass
class FurtherAlt:
    interval_to_change: Interval
    interval_idx_lookup: Interval
    accidental: Accidental


@dataclass
class ChordTypeConverterNode:
    chord_type: ChordType
    mode: Mode
    further_alts: list[FurtherAlt] = field(default_factory=list)

    def has_alt_for(self, interval: Interval):
        for alt in self.further_alts:
            if alt.interval_to_change == interval:
                return True
        return False

    def find_corresponding_alt(self, interval: Interval):
        for alt in self.further_alts:
            if alt.interval_to_change == interval:
                return alt

    def find_corresponding_idx(self, interval: Interval):
        if self.has_alt_for(interval):
            return self.find_corresponding_idx(self.find_corresponding_alt(interval).interval_idx_lookup)

        for key, value in interval_to_idx.items():
            if interval in key:
                return value

        raise ValueError(f"Could not find index for {interval}")

    def adjust_note(self, note: PitchNote, interval: Interval):
        if not self.has_alt_for(interval):
            return note
        return find_note_from_number_of_semitones(
            note, self.find_corresponding_alt(interval).accidental.interval).get_note_from_name(note.note_name)

    def make_notes(self, root_note: PitchNote) -> list[PitchNote]:
        octave_notes = Key(self.mode, root_note).octave
        return [
            self.adjust_note(octave_notes[self.find_corresponding_idx(interval)], interval)
            for interval in self.chord_type.intervals
        ]


flat_5th_alt = FurtherAlt(Interval.TRI, Interval.PERF_5, Accidental.FLAT)
sharp_5th_alt = FurtherAlt(Interval.MIN_6, Interval.PERF_5, Accidental.SHARP)
all_nodes = [
    ChordTypeConverterNode(ChordType.MAJ, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.MIN, Mode.MINOR),
    ChordTypeConverterNode(ChordType.DIM, Mode.MINOR, [flat_5th_alt]),
    ChordTypeConverterNode(ChordType.AUG, Mode.MAJOR, [sharp_5th_alt]),
    ChordTypeConverterNode(ChordType.SUS_4, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.SUS_2, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.ITALIAN, Mode.MIXOLYDIAN),
    ChordTypeConverterNode(ChordType.FRENCH, Mode.MIXOLYDIAN, [flat_5th_alt]),
    ChordTypeConverterNode(ChordType.MAJ_6, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.MIN_6, Mode.MINOR),
    ChordTypeConverterNode(ChordType.NEAPOLITAN, Mode.LOCRIAN),
    ChordTypeConverterNode(ChordType.AUG_7, Mode.MIXOLYDIAN, [sharp_5th_alt]),
    ChordTypeConverterNode(
        ChordType.DIM_7, Mode.MINOR, [flat_5th_alt, FurtherAlt(Interval.MAJ_6, Interval.MIN_7, Accidental.FLAT)]),
    ChordTypeConverterNode(ChordType.DOM, Mode.MIXOLYDIAN),
    ChordTypeConverterNode(ChordType.HALF_DIM, Mode.MINOR, [flat_5th_alt]),
    ChordTypeConverterNode(ChordType.MIN_MAJ, Mode.HARMONIC_MINOR),
    ChordTypeConverterNode(ChordType.MAJ_7, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.MIN_7, Mode.MINOR),
    ChordTypeConverterNode(ChordType.DOM_9, Mode.MIXOLYDIAN),
    ChordTypeConverterNode(ChordType.MAJ_9, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.MIN_9, Mode.MINOR),
    ChordTypeConverterNode(ChordType.DOM_11, Mode.MIXOLYDIAN),
    ChordTypeConverterNode(ChordType.MAJ_11, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.MIN_11, Mode.MINOR),
    ChordTypeConverterNode(ChordType.DOM_13, Mode.MIXOLYDIAN),
    ChordTypeConverterNode(ChordType.MAJ_13, Mode.MAJOR),
    ChordTypeConverterNode(
        ChordType.MIN_13, Mode.MINOR, [FurtherAlt(Interval.MAJ_13, Interval.MAJ_6, Accidental.SHARP)]),
    ChordTypeConverterNode(ChordType.PEDAL, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.POWER, Mode.MAJOR),
    ChordTypeConverterNode(ChordType.TRISTAN, Mode.MINOR, [flat_5th_alt])
]

interval_to_idx = {
    (Interval.UNI,): 0,
    (Interval.MIN_2, Interval.MAJ_2): 1,
    (Interval.MAJ_3, Interval.MIN_3): 2,
    (Interval.PERF_4,): 3,
    (Interval.PERF_5,): 4,
    (Interval.MIN_6, Interval.MAJ_6): 5,
    (Interval.MIN_7, Interval.MAJ_7): 6,
    (Interval.MAJ_9,): 1,
    (Interval.AUG_9,): 2,
    (Interval.PERF_11,): 3,
    (Interval.MAJ_13,): 5
}


def _generate_all_notes(root_note: PitchNote, chord_type: ChordType) -> list[PitchNote]:
    def find_converter_node() -> ChordTypeConverterNode:
        for node in all_nodes:
            if node.chord_type == chord_type:
                return node
        raise ValueError(f"Could not convert {chord_type}")

    return find_converter_node().make_notes(root_note)


@dataclass
class ChordSymbol:
    """ Represents a chord symbol.
    # TODO handle slash chords (including with a bass alter)
    # TODO -> consider handling "frames" (guitar chord diagrams).
    """
    root_note: PitchNote
    chord_type: ChordType
    all_notes: list[PitchNote] = field(init=False)

    def __post_init__(self):
        self.all_notes = _generate_all_notes(self.root_note, self.chord_type)

    def glance(self):
        """ Returns an easy-to-read string representation of this chord symbol. """
        root_note_desc = f"{self.root_note.glance()}{self.chord_type.shorthand}"
        all_notes = " ".join([note.glance() for note in self.all_notes])
        return f"{root_note_desc} ({all_notes})"

    @staticmethod
    def from_xml(harmony_xml: etree.Element) -> 'ChordSymbol':
        """ Returns a chord symbol created from the given XML. """

        chord_root_xml = harmony_xml.find("root")
        if chord_root_xml is None:
            # TODO -> add more detailed information to be displayed here.
            raise ValueError("No root element found, unable to process chord.")

        root_note = PitchNote.corresponding_note(
            chord_root_xml.find("root-step").text,
            Accidental.from_xml(chord_root_xml.find("root-alter"))
        )

        kind_text = harmony_xml.find("kind").text
        chord = ChordSymbol(root_note, ChordType.from_text(kind_text))

        logger.info(chord.glance())

        return chord
