from dataclasses import dataclass, field
from enum import Enum

from pymusic.pitch.interval import Interval as Mi


def _make_relative_intervals(intervals: list[Mi]) -> list[Mi]:
    n_semis = [
        i2.n_semitones - i1.n_semitones for i1, i2 in zip(intervals, intervals[1:])
    ]

    relative_intervals = []
    for num in n_semis:
        if num == 1:
            relative_intervals.append(Mi.SEMITONE)
        elif num == 2:
            relative_intervals.append(Mi.TONE)
        else:
            relative_intervals.append(Mi.MIN_3)
    return relative_intervals


maj_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MAJ_3, Mi.PERF_4, Mi.PERF_5, Mi.MAJ_6, Mi.MAJ_7, Mi.OCT]
min_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MIN_3, Mi.PERF_4, Mi.PERF_5, Mi.MIN_6, Mi.MIN_7, Mi.OCT]
harm_min_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MIN_3, Mi.PERF_4, Mi.PERF_5, Mi.MIN_6, Mi.MAJ_7, Mi.OCT]
ion_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MAJ_3, Mi.PERF_4, Mi.PERF_5, Mi.MAJ_6, Mi.MAJ_7, Mi.OCT]
dor_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MIN_3, Mi.PERF_4, Mi.PERF_5, Mi.MAJ_6, Mi.MIN_7, Mi.OCT]
phry_intervals = [Mi.UNI, Mi.MIN_2, Mi.MIN_3, Mi.PERF_4, Mi.PERF_5, Mi.MIN_6, Mi.MIN_7, Mi.OCT]
lyd_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MAJ_3, Mi.TRI, Mi.PERF_5, Mi.MAJ_6, Mi.MAJ_7, Mi.OCT]
mixo_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MAJ_3, Mi.PERF_4, Mi.PERF_5, Mi.MAJ_6, Mi.MIN_7, Mi.OCT]
aeo_intervals = [Mi.UNI, Mi.MAJ_2, Mi.MIN_3, Mi.PERF_4, Mi.PERF_5, Mi.MIN_6, Mi.MIN_7, Mi.OCT]
loc_intervals = [Mi.UNI, Mi.MIN_2, Mi.MIN_3, Mi.PERF_4, Mi.TRI, Mi.MIN_6, Mi.MIN_7, Mi.OCT]


@dataclass
class ModeDataMixin:
    mode_name: str
    root_intervals: list[Mi]
    relative_intervals: list[Mi] = field(init=False)

    def __post_init__(self):
        self.relative_intervals = _make_relative_intervals(self.root_intervals)

    def __hash__(self):
        return hash(self.mode_name)


class Mode(ModeDataMixin, Enum):
    """ Represents a scale. """

    MAJOR = "major", maj_intervals
    MINOR = "minor", min_intervals
    HARMONIC_MINOR = "harmonic minor", harm_min_intervals
    IONIAN = "ionian", ion_intervals
    DORIAN = "dorian", dor_intervals
    PHRYGIAN = "phrygian", phry_intervals
    LYDIAN = "lydian", lyd_intervals
    MIXOLYDIAN = "mixolydian", mixo_intervals
    AEOLIAN = "aeolian", aeo_intervals
    LOCRIAN = "locrian", loc_intervals

    @staticmethod
    def find_mode_from_text(text: str) -> 'Mode':
        """ Given text returns the corresponding mode. """
        for mode in Mode:
            if mode.mode_name == text:
                return mode

        raise ValueError(f"Unrecognized mode {text}")
