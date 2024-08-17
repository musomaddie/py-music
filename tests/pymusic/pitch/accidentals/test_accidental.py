""" tests for the accidental package. """
from pymusic.pitch.accidentals import Accidental
from tests import create_xml


class TestCorrespondingAccidental:
    """ Tests for corresponding accidental method. """

    def test_natural(self):
        assert Accidental.corresponding_accidental(None) == Accidental.NATURAL

    def test_flat(self):
        flat_txt = create_xml(
            "<root-alter>-1</root-alter>")
        assert Accidental.corresponding_accidental(flat_txt) == Accidental.FLAT

    def test_sharp(self):
        sharp_txt = create_xml("<root-alter>1</root-alter>")
        assert Accidental.corresponding_accidental(sharp_txt) == Accidental.SHARP
