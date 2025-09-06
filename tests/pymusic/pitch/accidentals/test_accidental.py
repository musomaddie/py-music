""" tests for the accidental package. """
from pymusic.pitch.accidental import create_accidental_from_element, Accidental
from tests import create_xml


class TestCorrespondingAccidental:
    """ Tests for corresponding accidental method. """

    def test_natural(self):
        assert create_accidental_from_element(None) == Accidental.NATURAL
        assert Accidental.from_int(0) == Accidental.NATURAL
        assert Accidental.from_str("") == Accidental.NATURAL
        assert Accidental.from_str("♮") == Accidental.NATURAL

    def test_flat(self):
        flat_txt = create_xml(
            "<root-alter>-1</root-alter>")
        assert create_accidental_from_element(flat_txt) == Accidental.FLAT
        assert Accidental.from_int(-1) == Accidental.FLAT
        assert Accidental.from_str("♭") == Accidental.FLAT

    def test_sharp(self):
        sharp_txt = create_xml("<root-alter>1</root-alter>")
        assert create_accidental_from_element(sharp_txt) == Accidental.SHARP
        assert Accidental.from_int(1) == Accidental.SHARP
        assert Accidental.from_str("♯") == Accidental.SHARP
