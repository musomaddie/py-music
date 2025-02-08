""" This is really just testing the key builder but that's fine. """
import pytest

from pymusic.key import Mode
from pymusic.key.key import Key
from pymusic.pitch import Note
from tests import create_xml
from tests.pymusic import convert_into_note_list

# Test the Bb example because that's what is the current problem.
# TODO -> test more thoroughly

BB_KEY_ELEMENT = create_xml(
    f"""
    <key color="#000000">
        <fifths>-2</fifths>
        <mode>major</mode>
    </key>
    """
)


def test_bb():
    result = Key.from_xml(BB_KEY_ELEMENT)
    assert result.mode == Mode.MAJOR
    assert result.note == Note.B_FLAT


@pytest.mark.parametrize(
    ("mode", "expected_scale"),
    [
        ("major", "CDEFGAB")
    ]
)
def test_c_all_modes(mode, expected_scale):
    c_key_element = create_xml(
        f"""
        <key>
            <fifths>0</fifths>
            <mode>{mode}</mode>
        </key>
        """
    )
    assert Key.from_xml(c_key_element).octave == convert_into_note_list(expected_scale)
