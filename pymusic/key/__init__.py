from .mode import Mode
from ..pitch import (
    TONE, UNISON, MAJOR_2nd, MAJOR_3rd, PERFECT_4th, OCTAVE, PERFECT_5th, MAJOR_6th, MAJOR_7th,
    SEMITONE, MINOR_3rd, MINOR_6th, MINOR_7th)

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

IONIAN = MAJOR
# DORIAN  from D
# PHRYGIAN  from E
# LYDIAN  from F
# MIXOLYDIAN from G
# Aeolian from A
# Locrian from B.
