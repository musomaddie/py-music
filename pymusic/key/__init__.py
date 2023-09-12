from .mode import Mode
from ..pitch import (
    TONE, UNISON, MAJOR_2nd, MAJOR_3rd, PERFECT_4th, OCTAVE, PERFECT_5th, MAJOR_6th, MAJOR_7th,
    SEMITONE, MINOR_3rd, MINOR_6th, MINOR_7th, MINOR_2nd, TRITONE)

MAJOR = Mode(
    name="Major",
    intervals=[UNISON, MAJOR_2nd, MAJOR_3rd, PERFECT_4th, PERFECT_5th, MAJOR_6th, MAJOR_7th, OCTAVE],
    intervals_relative=[TONE, TONE, SEMITONE, TONE, TONE, TONE, SEMITONE])

MINOR = Mode(
    name="Minor",
    intervals=[UNISON, MAJOR_2nd, MINOR_3rd, PERFECT_4th, PERFECT_5th, MINOR_6th, MINOR_7th, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, SEMITONE, TONE, TONE]
)

HARMONIC_MINOR = Mode(
    name="Harmonic Minor",
    intervals=[UNISON, MAJOR_2nd, MINOR_3rd, PERFECT_4th, PERFECT_5th, MINOR_6th, MAJOR_7th, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, SEMITONE, MINOR_3rd, SEMITONE]
)

IONIAN = Mode(
    name="Ionian",
    intervals=MAJOR.intervals,
    intervals_relative=MAJOR.intervals_relative)
DORIAN = Mode(
    name="Dorian",
    intervals=[UNISON, MAJOR_2nd, MINOR_3rd, PERFECT_4th, PERFECT_5th, MAJOR_6th, MINOR_7th, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, TONE, SEMITONE, TONE])
PHRYGIAN = Mode(
    name="Pyrygian",
    intervals=[UNISON, MINOR_2nd, MINOR_3rd, PERFECT_4th, PERFECT_5th, MINOR_6th, MINOR_7th, OCTAVE],
    intervals_relative=[SEMITONE, TONE, TONE, TONE, SEMITONE, TONE, TONE]
)
LYDIAN = Mode(
    name="Lydian",
    intervals=[UNISON, MAJOR_2nd, MAJOR_3rd, TRITONE, PERFECT_5th, MAJOR_6th, MAJOR_7th, OCTAVE],
    intervals_relative=[TONE, TONE, TONE, SEMITONE, TONE, TONE, SEMITONE]
)
MIXOLYDIAN = Mode(
    name="Mixolydian",
    intervals=[UNISON, MAJOR_2nd, MAJOR_3rd, PERFECT_4th, PERFECT_5th, MAJOR_6th, MINOR_7th, OCTAVE],
    intervals_relative=[TONE, TONE, SEMITONE, TONE, TONE, SEMITONE, TONE]
)
AEOLIAN = Mode(
    name="Aeolian",
    intervals=[UNISON, MAJOR_2nd, MINOR_3rd, PERFECT_4th, PERFECT_5th, MINOR_6th, MINOR_7th, OCTAVE],
    intervals_relative=[TONE, SEMITONE, TONE, TONE, SEMITONE, TONE, TONE]
)
LOCRIAN = Mode(
    name="Locrian",
    intervals=[UNISON, MINOR_2nd, MINOR_3rd, PERFECT_4th, TRITONE, MINOR_6th, MINOR_7th, OCTAVE],
    intervals_relative=[SEMITONE, TONE, TONE, SEMITONE, TONE, TONE, TONE]
)
