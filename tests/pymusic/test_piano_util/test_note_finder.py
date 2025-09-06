import pytest

from pymusic.piano_util.note_finder import find_note_with_accidental
from pymusic.pitch.accidental import Accidental
from pymusic.pitch.pitchnote import PitchNote


@pytest.mark.parametrize(
    ("starting_note", "desired_accidental", "expected_note"),
    [
        (PitchNote.corresponding_note_from_str("C"), Accidental.NATURAL, PitchNote.corresponding_note_from_str("C")),
        (PitchNote.corresponding_note_from_str("C"), Accidental.SHARP, PitchNote.corresponding_note_from_str("C♯")),
        (PitchNote.corresponding_note_from_str("C"), Accidental.FLAT, PitchNote.corresponding_note_from_str("C♭")),
        (PitchNote.corresponding_note_from_str("C♯"), Accidental.FLAT, PitchNote.corresponding_note_from_str("C♭")),
        (PitchNote.corresponding_note_from_str("C♯"), Accidental.NATURAL, PitchNote.corresponding_note_from_str("C")),
        (PitchNote.corresponding_note_from_str("C♭"), Accidental.FLAT, PitchNote.corresponding_note_from_str("C♭")),
        (PitchNote.corresponding_note_from_str("C♭"), Accidental.NATURAL, PitchNote.corresponding_note_from_str("C")),
        (PitchNote.corresponding_note_from_str("C♭"), Accidental.SHARP, PitchNote.corresponding_note_from_str("C♯")),
    ]
)
def test_find_note_with_accidental(starting_note, desired_accidental, expected_note):
    assert find_note_with_accidental(starting_note, desired_accidental) == expected_note
