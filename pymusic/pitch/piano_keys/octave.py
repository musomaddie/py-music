from pymusic.pitch.note import Note
from pymusic.pitch.piano_keys.key_notes import WhiteKey, BlackKey, KeyNote

octave = [
    WhiteKey(Note.A, Note.G_SHARP_2, Note.B_FLAT_2),
    BlackKey(Note.A_SHARP, Note.B_FLAT),
    WhiteKey(Note.B, Note.A_SHARP_2, Note.C_FLAT),
    WhiteKey(Note.C, Note.B_SHARP, Note.D_FLAT_2),
    BlackKey(Note.C_SHARP, Note.D_FLAT),
    WhiteKey(Note.D, Note.C_SHARP_2, Note.E_FLAT_2),
    BlackKey(Note.D_SHARP, Note.E_FLAT),
    WhiteKey(Note.E, Note.D_SHARP_2, Note.F_FLAT),
    WhiteKey(Note.F, Note.E_SHARP, Note.G_FLAT_2),
    BlackKey(Note.F_SHARP, Note.G_FLAT),
    WhiteKey(Note.G, Note.F_SHARP_2, Note.A_FLAT_2),
    BlackKey(Note.G_SHARP, Note.A_FLAT)
]


def _note_idx(it, condition, default=-1):
    return next((i for i, elem in enumerate(it) if condition(elem)), default)


def get_note(desired_idx: int) -> KeyNote:
    """ Returns the note at the given index in this octave. """
    return octave[desired_idx % len(octave)]


def find_index(searching_note: Note) -> int:
    """ Returns the index of the note passed. """
    return _note_idx(octave, lambda note: note.matches(searching_note))


def find_key_note(note: Note) -> KeyNote:
    """ Finds the keynote corresponding to the given note.
    Not 100% sure how useful this will be outside of tests though :(
    """
    return next((elem for elem in octave if elem.matches(note)), -1)
