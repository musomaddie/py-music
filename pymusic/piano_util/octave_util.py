from pymusic.piano_util.key_note import WhiteKey, BlackKey, KeyNote
from pymusic.pitch.pitchnote import PitchNote

TWO_OCTAVE_NOTE_STR = "ABCDEFGABCDEFG"

OCTAVE = [
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


def _note_idx(condition, default=-1):
    return next((i for i, elem in enumerate(OCTAVE) if condition(elem)), default)


def get_note_from_octave_index(desired_idx: int) -> KeyNote:
    """ Returns the note at the given index in the octave. """
    return OCTAVE[desired_idx % len(OCTAVE)]


def get_octave_index_from_note(searching_note: PitchNote) -> int:
    """ Returns the index of the note passed in the octave. Throws an exception if the note is invalid. """
    idx = _note_idx(lambda note: note.matches(searching_note))
    if idx == -1:
        raise ValueError('No note matches {}'.format(searching_note))
    return idx


def pitch_note_to_key_note(pitch_note: PitchNote) -> KeyNote:
    key_note = next((elem for elem in OCTAVE if elem.matches(pitch_note)), -1)
    if key_note == -1:
        raise ValueError('No note matches {}'.format(pitch_note))
    return key_note


def get_all_base_octave_notes(starting_note: PitchNote) -> list[str]:
    starting_note_str_idx = TWO_OCTAVE_NOTE_STR.find(starting_note.note_name.name)
    return list(TWO_OCTAVE_NOTE_STR[starting_note_str_idx + 1: starting_note_str_idx + 7])
