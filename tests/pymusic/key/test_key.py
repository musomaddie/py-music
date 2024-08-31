""" This is really just testing the key builder but that's fine. """
from pymusic.key import Mode
from pymusic.key.key import KeyBuilder
from pymusic.pitch import Note
from tests import create_xml

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


# < key
# color = "#000000" >
# < fifths > -2 < / fifths >
# < mode > major < / mode >
# < / key >


def test_bb():
    result = KeyBuilder.create_from_key_xml(BB_KEY_ELEMENT)
    assert result.mode == Mode.MAJOR
    assert result.note == Note.B_FLAT
