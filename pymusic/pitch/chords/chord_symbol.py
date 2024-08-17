"""
Handles a chord symbol (i.e. name / guitar chart above the main system).
Corresponds to harmony music xml element.
"""
import logging
from dataclasses import dataclass
from enum import Enum

from lxml import etree

from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.interval import Interval as i, Interval
from pymusic.pitch.note import Note

logger = logging.getLogger("chord_symbol")


# TODO -> it might be worth moving this into its own location separate from pitch so I can get nice imports in the
#  init without running into circles lol.

class ChordType(Enum):
    """ Represents a type of chord. """

    def __init__(self, desc: str, intervals: list[Interval], relative_intervals: list[Interval]):
        self.desc = desc
        self.intervals = intervals
        self.relative_intervals = relative_intervals

    # Triads
    MAJ = "major", [i.UNI, i.MAJ_3, i.PERF_5], [i.UNI, i.MAJ_3, i.MIN_3]
    MIN = "minor", [i.UNI, i.MIN_3, i.PERF_5], [i.UNI, i.MIN_3, i.MAJ_3]
    DIM = "diminished", [i.UNI, i.MIN_3, i.TRI], [i.UNI, i.MIN_3, i.MIN_3]
    AUG = "augmented", [i.UNI, i.MAJ_3, i.MIN_6], [i.UNI, i.MAJ_3, i.MAJ_3]
    SUS_4 = "suspended-fourth", [i.UNI, i.PERF_4, i.PERF_5], [i.UNI, i.PERF_4, i.MAJ_2]
    SUS_2 = "suspended-second", [i.UNI, i.MAJ_2, i.PERF_5], [i.UNI, i.MAJ_2, i.PERF_4]

    # Sixths
    ITALIAN = "Italian", [i.UNI, i.MAJ_3, i.MIN_7], [i.UNI, i.MAJ_3, i.TRI]
    FRENCH = "French", [i.UNI, i.MAJ_3, i.TRI, i.MIN_7], [i.UNI, i.MAJ_3, i.MAJ_2, i.MAJ_3]
    GERMAN = "German", [i.UNI, i.MAJ_3, i.PERF_5, i.MIN_7], [i.UNI, i.MAJ_3, i.MIN_3, i.MIN_3]
    MAJ_6 = "major-sixth", MAJ[1] + [i.MAJ_6], MAJ[2] + [i.MAJ_2]
    MIN_6 = "minor-sixth", MIN[1] + [i.MIN_6], MIN[2] + [i.MIN_2]
    NEAPOLITAN = "Neapolitan", [i.UNI, i.MIN_3, i.MIN_6], [i.UNI, i.MIN_3, i.PERF_4]

    # Sevenths
    AUG_7 = "augmented-seventh", AUG[1] + [i.MIN_7], AUG[2] + [i.MIN_2]
    DIM_7 = "diminished-seventh", DIM[1] + [i.MAJ_6], DIM[2] + [i.MIN_3]
    DOM = "dominant", MAJ[1] + [i.MIN_7], MAJ[2] + [i.MIN_3]
    HALF_DIM = "half-diminished", DIM[1] + [i.MIN_7], DIM[2] + [i.MAJ_3]
    MAJ_MIN = "major-minor", MIN[1] + [i.MAJ_7], MIN[2] + [i.MAJ_3]
    MAJ_7 = "major-seventh", MAJ[1] + [i.MAJ_7], MAJ[2] + [i.MAJ_3]
    MIN_7 = "minor-seventh", MIN[1] + [i.MIN_7], MIN[2] + [i.MIN_3]

    # Ninths
    DOM_9 = "dominant-ninth", DOM[1] + [i.MAJ_9], DOM[2] + [i.MAJ_3]
    MAJ_9 = "major-ninth", MAJ_7[1] + [i.MAJ_9], MAJ_7[2] + [i.MIN_3]
    MIN_9 = "minor-ninth", MIN_7[1] + [i.MAJ_9], MAJ_9[2] + [i.MAJ_3]

    # Elevenths
    DOM_11 = "dominant-11th", DOM_9[1] + [i.PERF_11], DOM_9[2] + [i.MAJ_3]
    MAJ_11 = "major-11th", MAJ_9[1] + [i.PERF_11], MAJ_9[2] + [i.MIN_3]
    MIN_11 = "minor-11th", MIN_9[1] + [i.PERF_11], MIN_9[2] + [i.MIN_3]

    # Thirteenth
    DOM_13 = "dominant-13th", DOM_11[1] + [i.MAJ_13], DOM_11[2] + [i.MAJ_3]
    MAJ_13 = "major-13th", MAJ_11[1] + [i.MAJ_13], MAJ_11[2] + [i.MAJ_3]
    MIN_13 = "minor-13th", MIN_11[1] + [i.MAJ_13], MIN_11[2] + [i.MAJ_3]

    # Extras
    NO_CHORD = "none", [], []
    PEDAL = "pedal", [i.UNI], [i.UNI]
    POWER = "power", [i.UNI, i.PERF_5], [i.UNI, i.PERF_5]
    TRISTAN = "Tristan", [i.UNI, i.TRI, i.MIN_7, i.AUG_9], [i.UNI, i.TRI, i.MAJ_3, i.PERF_4]

    @staticmethod
    def find_corresponding(kind_text: str) -> 'ChordType':
        """ Returns the chord type corresponding to the given kind text """
        for c_type in ChordType:
            if c_type.desc == kind_text:
                return c_type

        raise ValueError(f"Unrecognised chord type {kind_text}")


@dataclass
class ChordSymbol:
    """ Represents a chord symbol. """
    root_note: Note
    chord_type: ChordType

    # TODO -> determine the notes found in this chord.
    def glance(self):
        """ Returns an easy-to-read string representation of this chord symbol. """
        return f"{self.root_note.glance()} {self.chord_type.desc}"

    @staticmethod
    def create_from_xml(harmony_xml: etree.Element) -> 'ChordSymbol':
        """ Returns a chord symbol created from the given XML. """
        logger.error("Creating chord with %s", harmony_xml)

        chord_root_xml = harmony_xml.find("root")
        if chord_root_xml is None:
            # TODO -> add more detailed information to be displayed here.
            raise ValueError("No root element found, unable to process chord.")
        root_note = Note.corresponding_note(
            chord_root_xml.find("root-step").text,
            Accidental.corresponding_accidental(chord_root_xml.find("root-alter"))
        )
        kind_text = harmony_xml.find("kind").text
        return ChordSymbol(root_note, ChordType.find_corresponding(kind_text))
