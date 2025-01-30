""" Test EVERYTHING in piano keys - thoroughly. """
import pytest

from pymusic.pitch import Note
from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.piano_keys import octave, find_note_from_number_of_semitones


@pytest.mark.parametrize(
    ("keynote", "accidental", "expected_note"),
    [
        (octave.find_key_note(Note.A), Accidental.NATURAL, Note.A),
        (octave.find_key_note(Note.B), Accidental.NATURAL, Note.B),
        (octave.find_key_note(Note.B), Accidental.FLAT, Note.C_FLAT),
        (octave.find_key_note(Note.C), Accidental.NATURAL, Note.C),
        (octave.find_key_note(Note.C), Accidental.SHARP, Note.B_SHARP),
        (octave.find_key_note(Note.D), Accidental.NATURAL, Note.D),
        (octave.find_key_note(Note.E), Accidental.NATURAL, Note.E),
        (octave.find_key_note(Note.E), Accidental.FLAT, Note.F_FLAT),
        (octave.find_key_note(Note.F), Accidental.NATURAL, Note.F),
        (octave.find_key_note(Note.F), Accidental.SHARP, Note.E_SHARP),
        (octave.find_key_note(Note.G), Accidental.NATURAL, Note.G)
    ]
)
def test_white_note_get_note(keynote, accidental, expected_note):
    assert keynote.get_note(accidental) == expected_note


@pytest.mark.parametrize(
    ("keynote", "accidental", "expected_note"),
    [
        (octave.find_key_note(Note.A_SHARP), Accidental.SHARP, Note.A_SHARP),
        (octave.find_key_note(Note.A_SHARP), Accidental.FLAT, Note.B_FLAT),
        (octave.find_key_note(Note.B_FLAT), Accidental.NATURAL, Note.A_SHARP)
        # I'm less worried about this misbehaving for hte black notes so only testing this.
    ],
)
def test_black_note_get_note(keynote, accidental, expected_note):
    assert keynote.get_note(accidental) == expected_note


@pytest.mark.parametrize(
    ("semitones", "expected_note"),
    [
        (0, octave.find_key_note(Note.C)),
        (1, octave.find_key_note(Note.C_SHARP)),
        (2, octave.find_key_note(Note.D)),
        (3, octave.find_key_note(Note.D_SHARP)),
        (4, octave.find_key_note(Note.E)),
        (5, octave.find_key_note(Note.F)),
        (6, octave.find_key_note(Note.F_SHARP)),
        (7, octave.find_key_note(Note.G)),
        (8, octave.find_key_note(Note.G_SHARP)),
        (9, octave.find_key_note(Note.A)),
        (10, octave.find_key_note(Note.A_SHARP)),
        (11, octave.find_key_note(Note.B)),
        (12, octave.find_key_note(Note.C)),
        (24, octave.find_key_note(Note.C)),
        (-1, octave.find_key_note(Note.B)),
        (-2, octave.find_key_note(Note.B_FLAT)),
        (-3, octave.find_key_note(Note.A))
    ]
)
def test_find_note_from_number_of_semitones(semitones, expected_note):
    assert find_note_from_number_of_semitones(Note.C, semitones) == expected_note
