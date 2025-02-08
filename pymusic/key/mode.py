from enum import Enum

from pymusic.pitch import Interval as i, Interval


class Mode(Enum):

    def __init__(self, mode_name: str, intervals: list[Interval]):
        """ Represents a scale. """
        self.mode_name = mode_name
        self.intervals = intervals
        self.intervals_relative = self._make_relative(self.intervals)

    @staticmethod
    def _make_relative(intervals: list[Interval]):
        """ Converts the list of intervals to a relative list. """
        n_semis = []
        relative = []

        for i1, i2 in zip(intervals, intervals[1:]):
            n_semis.append(i2.n_semitones - i1.n_semitones)

        for num in n_semis:
            if num == 1:
                relative.append(Interval.SEMITONE)
            elif num == 2:
                relative.append(Interval.TONE)
            else:
                relative.append(Interval.MIN_3)

        return relative

    """ Represents a scale (via an enum)"""
    MAJOR = "major", [i.UNI, i.MAJ_2, i.MAJ_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MAJ_7, i.OCT]
    MINOR = "minor", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MIN_7, i.OCT]
    HARMONIC_MINOR = "harmonic minor", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MAJ_7, i.OCT]
    IONIAN = "ionian", [i.UNI, i.MAJ_2, i.MAJ_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MAJ_7, i.OCT]
    DORIAN = "dorian", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MIN_7, i.OCT]
    PHRYGIAN = "phrygian", [i.UNI, i.MIN_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MIN_7, i.OCT]
    LYDIAN = "lydian", [i.UNI, i.MAJ_2, i.MAJ_3, i.TRI, i.PERF_5, i.MAJ_6, i.MAJ_7, i.OCT]
    MIXOLYDIAN = "mixolydian", [i.UNI, i.MAJ_2, i.MAJ_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MIN_7, i.OCT]
    AEOLIAN = "aeolian", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MIN_7, i.OCT]
    LOCRIAN = "locrian", [i.UNI, i.MIN_2, i.MIN_3, i.PERF_4, i.TRI, i.MIN_6, i.MIN_7, i.OCT]

    @staticmethod
    def find_mode_from_text(text: str) -> 'Mode':
        """ Given text returns the corresponding mode. """
        for mode in Mode:
            if mode.mode_name == text:
                return mode

        raise ValueError(f"Unrecognized mode {text}")
