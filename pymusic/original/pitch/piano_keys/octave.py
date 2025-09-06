from pymusic.original.pitch.piano_keys.key_notes import WhiteKey, BlackKey, KeyNote
from pymusic.original.pitch.pitchnote import PitchNote

octave = [
    WhiteKey(PitchNote.A, PitchNote.G_SHARP_2, PitchNote.B_FLAT_2),
    BlackKey(PitchNote.A_SHARP, PitchNote.B_FLAT),
    WhiteKey(PitchNote.B, PitchNote.A_SHARP_2, PitchNote.C_FLAT),
    WhiteKey(PitchNote.C, PitchNote.B_SHARP, PitchNote.D_FLAT_2),
    BlackKey(PitchNote.C_SHARP, PitchNote.D_FLAT),
    WhiteKey(PitchNote.D, PitchNote.C_SHARP_2, PitchNote.E_FLAT_2),
    BlackKey(PitchNote.D_SHARP, PitchNote.E_FLAT),
    WhiteKey(PitchNote.E, PitchNote.D_SHARP_2, PitchNote.F_FLAT),
    WhiteKey(PitchNote.F, PitchNote.E_SHARP, PitchNote.G_FLAT_2),
    BlackKey(PitchNote.F_SHARP, PitchNote.G_FLAT),
    WhiteKey(PitchNote.G, PitchNote.F_SHARP_2, PitchNote.A_FLAT_2),
    BlackKey(PitchNote.G_SHARP, PitchNote.A_FLAT)
]


def _note_idx(it, condition, default=-1):
    return next((i for i, elem in enumerate(it) if condition(elem)), default)


def get_note(desired_idx: int) -> KeyNote:
    """ Returns the note at the given index in this octave. """
    return octave[desired_idx % len(octave)]


def find_index(searching_note: PitchNote) -> int:
    """ Returns the index of the note passed. """
    return _note_idx(octave, lambda note: note.matches(searching_note))


def find_key_note(note: PitchNote) -> KeyNote:
    """ Finds the keynote corresponding to the given note.
    Not 100% sure how useful this will be outside of tests though :(
    """
    return next((elem for elem in octave if elem.matches(note)), -1)
