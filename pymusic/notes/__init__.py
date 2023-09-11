from .accidental import Accidental
from .note_name import Note

SHARP = Accidental(alter="1", desc="Sharp", shorthand="#")
FLAT = Accidental(alter="-1", desc="Flat", shorthand="b")
NONE = Accidental(alter="0", desc="", shorthand="")

A = Note("A")
B = Note("B")
C = Note("C")
D = Note("D")
E = Note("E")
F = Note("F")
G = Note("G")
