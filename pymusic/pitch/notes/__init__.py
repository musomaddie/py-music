from pymusic.pitch.accidentals import NATURAL, FLAT, SHARP
from pymusic.pitch.notes.note_name import NoteName
from pymusic.pitch.notes.octave_note_name import OctaveNoteName

A_FLAT = NoteName(OctaveNoteName.A, FLAT)
A = NoteName(OctaveNoteName.A, NATURAL)
A_SHARP = NoteName(OctaveNoteName.A, SHARP)

B_FLAT = NoteName(OctaveNoteName.B, FLAT)
B = NoteName(OctaveNoteName.B, NATURAL)

C = NoteName(OctaveNoteName.C, NATURAL)
C_SHARP = NoteName(OctaveNoteName.C, SHARP)

D_FLAT = NoteName(OctaveNoteName.D, FLAT)
D = NoteName(OctaveNoteName.D, NATURAL)
D_SHARP = NoteName(OctaveNoteName.D, SHARP)

E_FLAT = NoteName(OctaveNoteName.E, FLAT)
E = NoteName(OctaveNoteName.E, NATURAL)

F = NoteName(OctaveNoteName.F, NATURAL)
F_SHARP = NoteName(OctaveNoteName.F, SHARP)

G_FLAT = NoteName(OctaveNoteName.G, FLAT)
G = NoteName(OctaveNoteName.G, NATURAL)
G_SHARP = NoteName(OctaveNoteName.G, SHARP)
