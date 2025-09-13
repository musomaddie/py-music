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
    "N6": ([I.UNI, I.MIN_3, I.MIN_6], [I.UNI, I.MIN_3, I.PERF_4])
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


class ChordType(Enum):
    """ Represents a type of chord. """

    def __init__(self, desc: str, shorthand: str, intervals: list[Interval], relative_intervals: list[Interval]):
        self.desc = desc
        self.shorthand = shorthand
        self.intervals = intervals
        self.relative_intervals = relative_intervals

    def glance(self):
        return self.shorthand

    # Triads
    MAJ = "major", *_get_data(""),
    MIN = "minor", *_get_data("m")
    DIM = "diminished", *_get_data("dim")
    AUG = "augmented", *_get_data("+")
    SUS_4 = "suspended-fourth", *_get_data("sus")
    SUS_2 = "suspended-second", *_get_data("sus2")

    # Sixths
    ITALIAN = "Italian", *_get_data("It+6")
    FRENCH = "French", *_get_data("Fr+6")
    GERMAN = "German", *_get_data("Gr+6")
    MAJ_6 = "major-sixth", *_get_data("6")
    MIN_6 = "minor-sixth", *_get_data("m6")
    NEAPOLITAN = "Neapolitan", *_get_data("N6")

    # Sevenths
    AUG_7 = "augmented-seventh", *_get_data("+7")
    DIM_7 = "diminished-seventh", *_get_data("dim7")
    DOM = "dominant", *_get_data("7")
    HALF_DIM = "half-diminished", *_get_data("7(♭5)")
    MIN_MAJ = "minor-major", *_get_data("m(M7)")
    MAJ_7 = "major-seventh", *_get_data("maj7")
    MIN_7 = "minor-seventh", *_get_data("m7")

    # Ninths
    DOM_9 = "dominant-ninth", *_get_data("9")
    MAJ_9 = "major-ninth", *_get_data("maj9")
    MIN_9 = "minor-ninth", *_get_data("m9")

    # Elevenths
    DOM_11 = "dominant-11th", *_get_data("11")
    MAJ_11 = "major-11th", *_get_data("maj11")
    MIN_11 = "minor-11th", *_get_data("m11")

    # Thirteenth
    DOM_13 = "dominant-13th", *_get_data("13")
    MAJ_13 = "major-13th", *_get_data("maj13")
    MIN_13 = "minor-13th", *_get_data("m13")

    # Extras
    NO_CHORD = "none", "none", [], []
    PEDAL = "pedal", "pedal", [I.UNI], [I.UNI]
    POWER = "power", "power", [I.UNI, I.PERF_5], [I.UNI, I.PERF_5]
    TRISTAN = "Tristan", "Tristan", [I.UNI, I.TRI, I.MIN_7, I.AUG_9], [I.UNI, I.TRI, I.MAJ_3, I.PERF_4]

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
