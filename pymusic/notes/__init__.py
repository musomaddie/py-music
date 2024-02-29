from .accidental import Accidental
from .black_note import BlackNote
from .note import Note
from .note_names import NoteName

SHARP = Accidental(alter="1", desc="Sharp", shorthand="#")
FLAT = Accidental(alter="-1", desc="Flat", shorthand="b")
NONE = Accidental(alter="0", desc="", shorthand="")

A = Note(NoteName.A)
B = Note(NoteName.B)
C = Note(NoteName.C)
D = Note(NoteName.D)
E = Note(NoteName.E)
F = Note(NoteName.F)
G = Note(NoteName.G)

AB = BlackNote(NoteName.A, NoteName.B)
CD = BlackNote(NoteName.C, NoteName.D)
DE = BlackNote(NoteName.D, NoteName.E)
FG = BlackNote(NoteName.F, NoteName.G)
GA = BlackNote(NoteName.G, NoteName.A)

KEYBOARD_OCTAVE = [C, CD, D, DE, E, F, FG, G, GA, A, AB, B]
