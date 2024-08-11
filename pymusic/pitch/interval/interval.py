""" Interval enum """
from enum import Enum


class Interval(Enum):

    def __init__(self, names: list[str], n_semitones: int):
        """ The data used for the interval enum. """
        self.names = names
        self.n_semitones = n_semitones

    UNI = ["unison", "root"], 0
    MIN_2 = ["minor 2nd"], 1
    MAJ_2 = ["major 2nd", "diminished 3rd"], 2
    MIN_3 = ["minor 3rd"], 3
    MAJ_3 = ["major 3rd"], 4
    PERF_4 = ["perfect 4th"], 5
    TRI = ["augmented 4th", "tritone", "diminished 5th"], 6
    PERF_5 = ["perfect 5th"], 7
    MIN_6 = ["minor 6th, augmented 5th"], 8
    MAJ_6 = ["major 6th", "diminished 7th"], 9
    MIN_7 = ["minor 7th", "augmented 6th"], 10
    MAJ_7 = ["major 7th"], 11
    OCT = ["Octave"], 12
    MAJ_9 = ["major 9th"], 14
    AUG_9 = ["augmented 9th"], 15
    PERF_11 = ["perfect 11th"], 17
    MAJ_13 = ["major 13th"], 21
    TONE = ["tone"], 2
    SEMITONE = ["semitone"], 1
