""" Test EVERYTHING in piano keys - thoroughly. """
import pytest

from pymusic.original.pitch import PitchNote
from pymusic.original.pitch.accidentals import Accidental
from pymusic.original.pitch.piano_keys import octave
from pymusic.original.pitch.piano_keys.piano import find_note_with_accidental, find_note_from_number_of_semitones


@pytest.mark.parametrize(
    ("keynote", "accidental", "expected_note"),
    [
        (octave.find_key_note(PitchNote.A), Accidental.NATURAL, PitchNote.A),
        (octave.find_key_note(PitchNote.B), Accidental.NATURAL, PitchNote.B),
        (octave.find_key_note(PitchNote.B), Accidental.FLAT, PitchNote.C_FLAT),
        (octave.find_key_note(PitchNote.C), Accidental.NATURAL, PitchNote.C),
        (octave.find_key_note(PitchNote.C), Accidental.SHARP, PitchNote.B_SHARP),
        (octave.find_key_note(PitchNote.D), Accidental.NATURAL, PitchNote.D),
        (octave.find_key_note(PitchNote.E), Accidental.NATURAL, PitchNote.E),
        (octave.find_key_note(PitchNote.E), Accidental.FLAT, PitchNote.F_FLAT),
        (octave.find_key_note(PitchNote.F), Accidental.NATURAL, PitchNote.F),
        (octave.find_key_note(PitchNote.F), Accidental.SHARP, PitchNote.E_SHARP),
        (octave.find_key_note(PitchNote.G), Accidental.NATURAL, PitchNote.G)
    ]
)
def test_white_note_get_note(keynote, accidental, expected_note):
    assert keynote.get_note(accidental) == expected_note


@pytest.mark.parametrize(
    ("keynote", "accidental", "expected_note"),
    [
        (octave.find_key_note(PitchNote.A_SHARP), Accidental.SHARP, PitchNote.A_SHARP),
        (octave.find_key_note(PitchNote.A_SHARP), Accidental.FLAT, PitchNote.B_FLAT),
        (octave.find_key_note(PitchNote.B_FLAT), Accidental.NATURAL, PitchNote.A_SHARP)
        # I'm less worried about this misbehaving for hte black notes so only testing this.
    ],
)
def test_black_note_get_note(keynote, accidental, expected_note):
    assert keynote.get_note(accidental) == expected_note


@pytest.mark.parametrize(
    ("semitones", "expected_note"),
    [
        (0, octave.find_key_note(PitchNote.C)),
        (1, octave.find_key_note(PitchNote.C_SHARP)),
        (2, octave.find_key_note(PitchNote.D)),
        (3, octave.find_key_note(PitchNote.D_SHARP)),
        (4, octave.find_key_note(PitchNote.E)),
        (5, octave.find_key_note(PitchNote.F)),
        (6, octave.find_key_note(PitchNote.F_SHARP)),
        (7, octave.find_key_note(PitchNote.G)),
        (8, octave.find_key_note(PitchNote.G_SHARP)),
        (9, octave.find_key_note(PitchNote.A)),
        (10, octave.find_key_note(PitchNote.A_SHARP)),
        (11, octave.find_key_note(PitchNote.B)),
        (12, octave.find_key_note(PitchNote.C)),
        (24, octave.find_key_note(PitchNote.C)),
        (-1, octave.find_key_note(PitchNote.B)),
        (-2, octave.find_key_note(PitchNote.B_FLAT)),
        (-3, octave.find_key_note(PitchNote.A))
    ]
)
def test_find_note_from_number_of_semitones(semitones, expected_note):
    assert find_note_from_number_of_semitones(PitchNote.C, semitones) == expected_note


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
