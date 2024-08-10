""" package corresponding to a single note."""
from .note import Note, NoteName
from ..accidentals import Accidental

AF = Note(NoteName.A, Accidental.FLAT)
AN = Note(NoteName.A, Accidental.NATURAL)
AS = Note(NoteName.A, Accidental.SHARP)

BF = Note(NoteName.B, Accidental.FLAT)
BN = Note(NoteName.B, Accidental.NATURAL)
BS = Note(NoteName.B, Accidental.SHARP)

CF = Note(NoteName.C, Accidental.FLAT)
CN = Note(NoteName.C, Accidental.NATURAL)
CS = Note(NoteName.C, Accidental.SHARP)

DF = Note(NoteName.D, Accidental.FLAT)
DN = Note(NoteName.D, Accidental.NATURAL)
DS = Note(NoteName.D, Accidental.SHARP)

EF = Note(NoteName.E, Accidental.FLAT)
EN = Note(NoteName.E, Accidental.NATURAL)
ES = Note(NoteName.E, Accidental.SHARP)

FF = Note(NoteName.F, Accidental.FLAT)
FN = Note(NoteName.F, Accidental.NATURAL)
FS = Note(NoteName.F, Accidental.SHARP)

GF = Note(NoteName.G, Accidental.FLAT)
GN = Note(NoteName.G, Accidental.NATURAL)
GS = Note(NoteName.G, Accidental.SHARP)
