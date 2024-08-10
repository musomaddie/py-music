""" Interval enum """
from dataclasses import dataclass
from enum import Enum


class Interval(Enum):
    @dataclass
    class Data:
        """ The data used for the interval enum. """
        names: list[str]
        n_semitones: int

    UNI = Data(["unison", "root"], 0)
    MIN_2 = Data(["minor 2nd"], 1)
    MAJ_2 = Data(["major 2nd", "diminished 3rd"], 2)
    MIN_3 = Data(["minor 3rd"], 3)
    MAJ_3 = Data(["major 3rd"], 4)
    PERF_4 = Data(["perfect 4th"], 5)
    TRI = Data(["augmented 4th", "tritone", "diminished 5th"], 6)
    PERF_5 = Data(["perfect 5th"], 7)
    MIN_6 = Data(["minor 6th, augmented 5th"], 8)
    MAJ_6 = Data(["major 6th", "diminished 7th"], 9)
    MIN_7 = Data(["minor 7th", "augmented 6th"], 10)
    MAJ_7 = Data(["major 7th"], 11)
    OCT = Data(["Octave"], 12)
    MAJ_9 = Data(["major 9th"], 14)
    AUG_9 = Data(["augmented 9th"], 15)
    PERF_11 = Data(["perfect 11th"], 17)
    MAJ_13 = Data(["major 13th"], 21)
    TONE = Data(["tone"], 2)
    SEMITONE = Data(["semitone"], 1)

    @property
    def names(self):
        return self.value.names

    @property
    def n_semitones(self):
        return self.value.n_semitones
