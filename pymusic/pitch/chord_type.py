from dataclasses import field, dataclass
from enum import Enum

from lxml.etree import Element

from pymusic.pitch.interval import Interval as I, Interval

intervals_dict = {
    "": ([I.UNI, I.MAJ_3, I.PERF_5], [I.UNI, I.MAJ_3, I.MIN_3]),
    "m": ([I.UNI, I.MIN_3, I.PERF_5], [I.UNI, I.MIN_3, I.MAJ_3]),
    "dim": ([I.UNI, I.MIN_3, I.TRI], [I.UNI, I.MIN_3, I.MIN_3]),
    "+": ([I.UNI, I.MAJ_3, I.MIN_6], [I.UNI, I.MAJ_3, I.MAJ_3]),
    "sus": ([I.UNI, I.PERF_4, I.PERF_5], [I.UNI, I.PERF_4, I.MAJ_2]),
    "sus2": ([I.UNI, I.MAJ_2, I.PERF_5], [I.UNI, I.MAJ_2, I.PERF_4]),
    "It+6": ([I.UNI, I.MAJ_3, I.MIN_7], [I.UNI, I.MAJ_3, I.TRI]),
    "Fr+6": ([I.UNI, I.MAJ_3, I.TRI, I.MIN_7], [I.UNI, I.MAJ_3, I.MAJ_2, I.MAJ_3]),
    "Gr+6": ([I.UNI, I.MAJ_3, I.PERF_5, I.MIN_7], [I.UNI, I.MAJ_3, I.MIN_3, I.MIN_3]),
    "N6": ([I.UNI, I.MIN_3, I.MIN_6], [I.UNI, I.MIN_3, I.PERF_4]),
    "none": ([], []),
    "pedal": ([I.UNI], [I.UNI]),
    "power": ([I.UNI, I.PERF_5], [I.UNI, I.PERF_5]),
    "Tristan": ([I.UNI, I.TRI, I.MIN_7, I.AUG_9], [I.UNI, I.TRI, I.MAJ_3, I.PERF_4]),
}

intervals_dict["6"] = (intervals_dict[""][0] + [I.MAJ_6], intervals_dict[""][1] + [I.MAJ_2])
intervals_dict["m6"] = (intervals_dict["m"][0] + [I.MIN_6], intervals_dict["m"][1] + [I.MIN_2])
intervals_dict["+7"] = (intervals_dict["+"][0] + [I.MIN_7], intervals_dict["+"][1] + [I.MIN_2])
intervals_dict["dim7"] = (intervals_dict["dim"][0] + [I.MAJ_6], intervals_dict["dim"][1] + [I.MIN_3])
intervals_dict["7"] = (intervals_dict[""][0] + [I.MIN_7], intervals_dict[""][1] + [I.MIN_2])
intervals_dict["7(♭5)"] = (intervals_dict["dim"][0] + [I.MIN_7], intervals_dict["dim"][1] + [I.MAJ_3])
intervals_dict["m(M7)"] = (intervals_dict["m"][0] + [I.MAJ_7], intervals_dict["m"][1] + [I.MAJ_3])
intervals_dict["maj7"] = (intervals_dict[""][0] + [I.MAJ_7], intervals_dict[""][1] + [I.MAJ_3])
intervals_dict["m7"] = (intervals_dict["m"][0] + [I.MIN_7], intervals_dict["m"][1] + [I.MIN_3])
intervals_dict["9"] = (intervals_dict["7"][0] + [I.MAJ_9], intervals_dict["7"][1] + [I.MAJ_3])
intervals_dict["maj9"] = (intervals_dict["maj7"][0] + [I.MAJ_9], intervals_dict["maj7"][1] + [I.MIN_3])
intervals_dict["m9"] = (intervals_dict["m7"][0] + [I.MAJ_9], intervals_dict["m7"][1] + [I.MAJ_3])
intervals_dict["11"] = (intervals_dict["9"][0] + [I.PERF_11], intervals_dict["9"][1] + [I.MAJ_3])
intervals_dict["maj11"] = (intervals_dict["maj9"][0] + [I.PERF_11], intervals_dict["maj9"][1] + [I.MIN_3])
intervals_dict["m11"] = (intervals_dict["m9"][0] + [I.PERF_11], intervals_dict["m9"][1] + [I.MIN_3])
intervals_dict["13"] = (intervals_dict["11"][0] + [I.MAJ_13], intervals_dict["11"][1] + [I.MAJ_3])
intervals_dict["maj13"] = (intervals_dict["maj11"][0] + [I.MAJ_13], intervals_dict["maj11"][1] + [I.MAJ_3])
intervals_dict["m13"] = (intervals_dict["m11"][0] + [I.MAJ_13], intervals_dict["m11"][1] + [I.MAJ_3])


def _get_data(abbrev: str) -> tuple:
    return abbrev, intervals_dict[abbrev][0], intervals_dict[abbrev][1]


@dataclass()
class ChordTypeDataMixin:
    desc: str
    shorthand: str
    intervals: list[Interval] = field(init=False)
    relative_intervals: list[Interval] = field(init=False)

    def __post_init__(self):
        self.intervals = intervals_dict[self.shorthand][0]
        self.relative_intervals = intervals_dict[self.shorthand][1]

    def __hash__(self):
        return hash(self.desc)


class ChordType(ChordTypeDataMixin, Enum):
    """ Represents a type of chord. """

    def glance(self):
        return self.shorthand

    # Triads
    MAJ = "major", ""
    MIN = "minor", "m"
    DIM = "diminished", "dim"
    AUG = "augmented", "+"
    SUS_4 = "suspended-fourth", "sus"
    SUS_2 = "suspended-second", "sus2"

    # Sixths
    ITALIAN = "Italian", "It+6"
    FRENCH = "French", "Fr+6"
    GERMAN = "German", "Gr+6"
    MAJ_6 = "major-sixth", "6"
    MIN_6 = "minor-sixth", "m6"
    NEAPOLITAN = "Neapolitan", "N6"

    # Sevenths
    AUG_7 = "augmented-seventh", "+7"
    DIM_7 = "diminished-seventh", "dim7"
    DOM = "dominant", "7"
    HALF_DIM = "half-diminished", "7(♭5)"
    MIN_MAJ = "minor-major", "m(M7)"
    MAJ_7 = "major-seventh", "maj7"
    MIN_7 = "minor-seventh", "m7"

    # Ninths
    DOM_9 = "dominant-ninth", "9"
    MAJ_9 = "major-ninth", "maj9"
    MIN_9 = "minor-ninth", "m9"

    # Elevenths
    DOM_11 = "dominant-11th", "11"
    MAJ_11 = "major-11th", "maj11"
    MIN_11 = "minor-11th", "m11"

    # Thirteenth
    DOM_13 = "dominant-13th", "13"
    MAJ_13 = "major-13th", "maj13"
    MIN_13 = "minor-13th", "m13"

    # Extras
    NO_CHORD = "none", "none"
    PEDAL = "pedal", "pedal"
    POWER = "power", "power"
    TRISTAN = "Tristan", "Tristan"

    @staticmethod
    def from_element(element: Element) -> 'ChordType':
        return ChordType.from_text(element.find("kind").text)

    @staticmethod
    def from_text(kind_text: str) -> 'ChordType':
        """ Returns the chord type corresponding to the given kind text """
        for c_type in ChordType:
            if c_type.desc == kind_text:
                return c_type

        raise ValueError(f"Unrecognised chord type {kind_text}")
