import logging
from enum import Enum

from pymusic.pitch.interval.interval import Interval as i, Interval

logger = logging.getLogger("chord_type")


class ChordType(Enum):
    """ Represents a type of chord. """

    def __init__(self, desc: str, intervals: list[Interval], relative_intervals: list[Interval], shorthand: str):
        self.desc = desc
        self.intervals = intervals
        self.relative_intervals = relative_intervals
        self.shorthand = shorthand

    # Triads
    MAJ = "major", [i.UNI, i.MAJ_3, i.PERF_5], [i.UNI, i.MAJ_3, i.MIN_3], ""
    MIN = "minor", [i.UNI, i.MIN_3, i.PERF_5], [i.UNI, i.MIN_3, i.MAJ_3], "m"
    DIM = "diminished", [i.UNI, i.MIN_3, i.TRI], [i.UNI, i.MIN_3, i.MIN_3], "dim"
    AUG = "augmented", [i.UNI, i.MAJ_3, i.MIN_6], [i.UNI, i.MAJ_3, i.MAJ_3], "+"
    SUS_4 = "suspended-fourth", [i.UNI, i.PERF_4, i.PERF_5], [i.UNI, i.PERF_4, i.MAJ_2], "sus"
    SUS_2 = "suspended-second", [i.UNI, i.MAJ_2, i.PERF_5], [i.UNI, i.MAJ_2, i.PERF_4], "sus4"

    # Sixths
    ITALIAN = "Italian", [i.UNI, i.MAJ_3, i.MIN_7], [i.UNI, i.MAJ_3, i.TRI], "It+6"
    FRENCH = "French", [i.UNI, i.MAJ_3, i.TRI, i.MIN_7], [i.UNI, i.MAJ_3, i.MAJ_2, i.MAJ_3], "Fr+6"
    GERMAN = "German", [i.UNI, i.MAJ_3, i.PERF_5, i.MIN_7], [i.UNI, i.MAJ_3, i.MIN_3, i.MIN_3], "Gr+6"
    MAJ_6 = "major-sixth", MAJ[1] + [i.MAJ_6], MAJ[2] + [i.MAJ_2], "6"
    MIN_6 = "minor-sixth", MIN[1] + [i.MIN_6], MIN[2] + [i.MIN_2], "m6"
    NEAPOLITAN = "Neapolitan", [i.UNI, i.MIN_3, i.MIN_6], [i.UNI, i.MIN_3, i.PERF_4], "N6"

    # Sevenths
    AUG_7 = "augmented-seventh", AUG[1] + [i.MIN_7], AUG[2] + [i.MIN_2], "+7"
    DIM_7 = "diminished-seventh", DIM[1] + [i.MAJ_6], DIM[2] + [i.MIN_3], "dim7"
    DOM = "dominant", MAJ[1] + [i.MIN_7], MAJ[2] + [i.MIN_3], "7"
    HALF_DIM = "half-diminished", DIM[1] + [i.MIN_7], DIM[2] + [i.MAJ_3], "7(♭5)"
    MIN_MAJ = "minor-major", MIN[1] + [i.MAJ_7], MIN[2] + [i.MAJ_3], "m(M7)"
    MAJ_7 = "major-seventh", MAJ[1] + [i.MAJ_7], MAJ[2] + [i.MAJ_3], "maj7"
    MIN_7 = "minor-seventh", MIN[1] + [i.MIN_7], MIN[2] + [i.MIN_3], "m7"

    # Ninths
    DOM_9 = "dominant-ninth", DOM[1] + [i.MAJ_9], DOM[2] + [i.MAJ_3], "9"
    MAJ_9 = "major-ninth", MAJ_7[1] + [i.MAJ_9], MAJ_7[2] + [i.MIN_3], "maj9"
    MIN_9 = "minor-ninth", MIN_7[1] + [i.MAJ_9], MAJ_9[2] + [i.MAJ_3], "m9"

    # Elevenths
    DOM_11 = "dominant-11th", DOM_9[1] + [i.PERF_11], DOM_9[2] + [i.MAJ_3], "11"
    MAJ_11 = "major-11th", MAJ_9[1] + [i.PERF_11], MAJ_9[2] + [i.MIN_3], "maj11"
    MIN_11 = "minor-11th", MIN_9[1] + [i.PERF_11], MIN_9[2] + [i.MIN_3], "m11"

    # Thirteenth
    DOM_13 = "dominant-13th", DOM_11[1] + [i.MAJ_13], DOM_11[2] + [i.MAJ_3], "13",
    MAJ_13 = "major-13th", MAJ_11[1] + [i.MAJ_13], MAJ_11[2] + [i.MAJ_3], "maj13"
    MIN_13 = "minor-13th", MIN_11[1] + [i.MAJ_13], MIN_11[2] + [i.MAJ_3], "m13"

    # Extras
    NO_CHORD = "none", [], [], "none"
    PEDAL = "pedal", [i.UNI], [i.UNI], "pedal"
    POWER = "power", [i.UNI, i.PERF_5], [i.UNI, i.PERF_5], "power"
    TRISTAN = "Tristan", [i.UNI, i.TRI, i.MIN_7, i.AUG_9], [i.UNI, i.TRI, i.MAJ_3, i.PERF_4], "Tristan"

    @staticmethod
    def from_text(kind_text: str) -> 'ChordType':
        """ Returns the chord type corresponding to the given kind text """
        for c_type in ChordType:
            if c_type.desc == kind_text:
                return c_type

        raise ValueError(f"Unrecognised chord type {kind_text}")
