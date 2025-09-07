from enum import Enum

from pymusic.pitch.interval.interval import Interval as Mi


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


class Mode(Enum):
    """ Represents a scale. """

    def __init__(
            self,
            mode_name: str,
            root_intervals: list[Mi],
            relative_intervals: list[Mi]
    ):
        self.mode_name = mode_name
        self.root_intervals = root_intervals
        self.relative_intervals = relative_intervals

    MAJOR = "major", maj_intervals, _make_relative_intervals(maj_intervals)
    MINOR = "minor", min_intervals, _make_relative_intervals(min_intervals)
    HARMONIC_MINOR = "harmonic minor", harm_min_intervals, _make_relative_intervals(harm_min_intervals)
    IONIAN = "ionian", ion_intervals, _make_relative_intervals(ion_intervals)
    DORIAN = "dorian", dor_intervals, _make_relative_intervals(dor_intervals)
    PHRYGIAN = "phrygian", phry_intervals, _make_relative_intervals(phry_intervals)
    LYDIAN = "lydian", lyd_intervals, _make_relative_intervals(lyd_intervals)
    MIXOLYDIAN = "mixolydian", mixo_intervals, _make_relative_intervals(mixo_intervals)
    AEOLIAN = "aeolian", aeo_intervals, _make_relative_intervals(aeo_intervals)
    LOCRIAN = "locrian", loc_intervals, _make_relative_intervals(loc_intervals)

    @staticmethod
    def find_mode_from_text(text: str) -> 'Mode':
        """ Given text returns the corresponding mode. """
        for mode in Mode:
            if mode.mode_name == text:
                return mode

        raise ValueError(f"Unrecognized mode {text}")
