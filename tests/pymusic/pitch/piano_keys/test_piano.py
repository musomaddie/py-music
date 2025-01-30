""" Test EVERYTHING in piano keys - thoroughly. """
import pytest

from pymusic.pitch import Note
from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.piano_keys import octave


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
