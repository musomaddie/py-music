from dataclasses import dataclass, field
from enum import Enum

from pymusic.pitch import Interval as i, Interval


class Mode(Enum):

    @dataclass
    class Data:

        """ Represents a scale. """
        mode_name: str
        intervals: list[Interval]  # From base.
        intervals_relative: list[Interval] = field(init=False)

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

        def __post_init__(self):
            self.intervals_relative = self._make_relative(self.intervals)

    """ Represents a scale (via an enum)"""
    MAJOR = Data("major", [i.UNI, i.MAJ_2, i.MAJ_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MAJ_7, i.OCT])
    MINOR = Data("minor", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MIN_7, i.OCT])
    HARMONIC_MINOR = Data("harmonic minor", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MAJ_7, i.OCT])
    IONIAN = Data("ionian", [i.UNI, i.MAJ_2, i.MAJ_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MAJ_7, i.OCT])
    DORIAN = Data("dorian", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MIN_7, i.OCT])
    PHRYGIAN = Data("phrygian", [i.UNI, i.MIN_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MIN_7, i.OCT])
    LYDIAN = Data("lydian", [i.UNI, i.MAJ_2, i.MAJ_3, i.TRI, i.PERF_5, i.MAJ_6, i.MAJ_7, i.OCT])
    MIXOLYDIAN = Data("mixolydian", [i.UNI, i.MAJ_2, i.MAJ_3, i.PERF_4, i.PERF_5, i.MAJ_6, i.MIN_7, i.OCT])
    AEOLIAN = Data("aeolian", [i.UNI, i.MAJ_2, i.MIN_3, i.PERF_4, i.PERF_5, i.MIN_6, i.MIN_7, i.OCT])
    LOCRIAN = Data("locrian", [i.UNI, i.MIN_2, i.MIN_3, i.PERF_4, i.TRI, i.MIN_6, i.MIN_7, i.OCT])

    @property
    def mode_name(self):
        return self.value.mode_name

    @property
    def intervals(self):
        return self.value.intervals

    @property
    def intervals_relative(self):
        return self.intervals_relative

    @staticmethod
    def find_mode_from_text(text: str) -> 'Mode':
        """ Given text returns the corresponding mode. """
        # TODO -> generalise this
        if text == "major":
            return Mode.MAJOR
