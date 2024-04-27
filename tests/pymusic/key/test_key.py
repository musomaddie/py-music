""" Tests related to the key! """
from io import BytesIO

import pytest
from lxml import etree

from pymusic.key import MAJOR
from pymusic.key.key import KeyBuilder, Key
from pymusic.pitch import (C, G, D, A, E, B, F, B_FLAT, E_FLAT, A_FLAT, D_FLAT, G_FLAT, C_FLAT)


def make_major_key(number):
    """ Returns an etree element representing the major key with the given number of sharps or flats. """
    return etree.parse(BytesIO(
        f"""
        <key color="#000000">
            <fifths>{number}</fifths>
            <mode>major</mode>
            </key>
        """.encode()
    )).getroot()


class TestBuilder:

    @pytest.mark.parametrize(
        ("accidental_number", "note", "as_text"),
        [
            (0, C, "C major"),
            (1, G, "G major"),
            (2, D, "D major"),
            (3, A, "A major"),
            (4, E, "E major"),
            (5, B, "B major"),
            (-1, F, "F major"),
            (-2, B_FLAT, "Bb major"),
            (-3, E_FLAT, "Eb major"),
            (-4, A_FLAT, "Ab major"),
            (-5, D_FLAT, "Db major"),
            (-6, G_FLAT, "Gb major"),
            (-7, C_FLAT, "Cb major")
        ]
    )
    def test_major_key(self, accidental_number, note, as_text):
        key = KeyBuilder.create_from_key_xml(make_major_key(accidental_number))
        expected_key = Key(MAJOR, note)
        assert expected_key == key
        assert as_text == key.glance()
