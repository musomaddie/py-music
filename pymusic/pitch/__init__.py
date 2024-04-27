from .accidental import Accidental
from .black_note import BlackNote
from .interval import Interval
from .note import (Note, A, A_FLAT, A_SHARP, B, B_FLAT, B_SHARP, C, C_SHARP, C_FLAT, D, D_SHARP, D_FLAT, E, E_FLAT,
    E_SHARP, F, F_SHARP, F_FLAT, G, G_SHARP, G_FLAT)

SEMITONE = Interval(text="semitone", distance=1)
TONE = Interval(text="tone", distance=2)

UNISON = Interval(text="unison", distance=0)
MINOR_2nd = Interval(text="minor 2nd", distance=1)
MAJOR_2nd = Interval(text="major 2nd", distance=2)
MINOR_3rd = Interval(text="minor 3rd", distance=3)
MAJOR_3rd = Interval(text="major 3rd", distance=4)
PERFECT_4th = Interval(text="perfect 4th", distance=5)
TRITONE = Interval(text="tritone", distance=6)
PERFECT_5th = Interval(text="perfect 5th", distance=7)
MINOR_6th = Interval(text="minor 6th", distance=8)
MAJOR_6th = Interval(text="major 6th", distance=9)
MINOR_7th = Interval(text="minor 7th", distance=10)
MAJOR_7th = Interval(text="major 7th", distance=11)
OCTAVE = Interval(text="Octave", distance=12)

SHARP = Accidental(alter="1", desc="Sharp", shorthand="#")
FLAT = Accidental(alter="-1", desc="Flat", shorthand="b")
NONE = Accidental(alter="0", desc="", shorthand="")

KEYBOARD_OCTAVE_SHARPS = [C, C_SHARP, D, D_SHARP, E, F, F_SHARP, G, G_SHARP, A, A_SHARP, B]
KEYBOARD_OCTAVE_FLATS = [C, D_FLAT, D, E_FLAT, E, F, G_FLAT, G, A_FLAT, A, B_FLAT, B]
