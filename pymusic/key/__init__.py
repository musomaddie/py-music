""" Mode things :) """

from .mode import Mode
from ..pitch import (
    TONE, UNISON, MAJOR_2, MAJOR_3, PERFECT_4, OCTAVE, PERFECT_5, MAJOR_6, MAJOR_7,
    SEMITONE, MINOR_3, MINOR_6, MINOR_7, MINOR_2, TRITONE)

MAJOR = Mode(
    name="Major",
    intervals=[UNISON, MAJOR_2, MAJOR_3, PERFECT_4, PERFECT_5, MAJOR_6, MAJOR_7, OCTAVE],
    intervals_relative=[TONE, TONE, SEMITONE, TONE, TONE, TONE, SEMITONE])

MINOR = Mode(
    name="Minor",
    intervals=[UNISON, MAJOR_2, MINOR_3, PERFECT_4, PERFECT_5, MINOR_6, MINOR_7, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, SEMITONE, TONE, TONE]
)

HARMONIC_MINOR = Mode(
    name="Harmonic Minor",
    intervals=[UNISON, MAJOR_2, MINOR_3, PERFECT_4, PERFECT_5, MINOR_6, MAJOR_7, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, SEMITONE, MINOR_3, SEMITONE]
)

IONIAN = Mode(
    name="Ionian",
    intervals=MAJOR.intervals,
    intervals_relative=MAJOR.intervals_relative)
DORIAN = Mode(
    name="Dorian",
    intervals=[UNISON, MAJOR_2, MINOR_3, PERFECT_4, PERFECT_5, MAJOR_6, MINOR_7, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, TONE, SEMITONE, TONE])
PHRYGIAN = Mode(
    name="Pyrygian",
    intervals=[UNISON, MINOR_2, MINOR_3, PERFECT_4, PERFECT_5, MINOR_6, MINOR_7, OCTAVE],
    intervals_relative=[SEMITONE, TONE, TONE, TONE, SEMITONE, TONE, TONE]
)
LYDIAN = Mode(
    name="Lydian",
    intervals=[UNISON, MAJOR_2, MAJOR_3, TRITONE, PERFECT_5, MAJOR_6, MAJOR_7, OCTAVE],
    intervals_relative=[TONE, TONE, TONE, SEMITONE, TONE, TONE, SEMITONE]
)
MIXOLYDIAN = Mode(
    name="Mixolydian",
    intervals=[UNISON, MAJOR_2, MAJOR_3, PERFECT_4, PERFECT_5, MAJOR_6, MINOR_7, OCTAVE],
    intervals_relative=[TONE, TONE, SEMITONE, TONE, TONE, SEMITONE, TONE]
)
AEOLIAN = Mode(
    name="Aeolian",
    intervals=[UNISON, MAJOR_2, MINOR_3, PERFECT_4, PERFECT_5, MINOR_6, MINOR_7, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, SEMITONE, TONE, TONE]
)
LOCRIAN = Mode(
    name="Locrian",
    intervals=[UNISON, MINOR_2, MINOR_3, PERFECT_4, TRITONE, MINOR_6, MINOR_7, OCTAVE],
    intervals_relative=[SEMITONE, TONE, TONE, SEMITONE, TONE, TONE, TONE]
)


def find_mode_from_text(text: str) -> Mode:
    """ Given text returns the corresponding mode. """
    if text == "major":
        return MAJOR
