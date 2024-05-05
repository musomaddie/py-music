""" Tests for anything in pitch/__init__.py"""

import pytest

from pymusic.pitch import (NATURAL, FLAT, SHARP, corresponding_accidental, A, B, C, D, E, F, G, corresponding_note,
    A_FLAT, A_SHARP, B_FLAT, C_SHARP, B_SHARP, D_SHARP, D_FLAT, C_FLAT, E_FLAT, F_SHARP, F_FLAT, E_SHARP, G_FLAT,
    G_SHARP)
from tests import create_xml


def _make_root_alter_item(number: str):
    return create_xml(
        f""" <root-alter>{number}</root-alter> """)


@pytest.mark.parametrize(
    ("alter_xml", "expected_accidental"),
    [
        (None, NATURAL),
        (_make_root_alter_item("-1"), FLAT),
        (_make_root_alter_item("1"), SHARP)
    ]
)
def test_corresponding_accidental(alter_xml, expected_accidental):
    assert expected_accidental == corresponding_accidental(alter_xml)


@pytest.mark.parametrize(
    ("note_name", "accidental_mod", "expected_note"),
    [
        ("A", NATURAL, A), ("A", FLAT, A_FLAT), ("A", SHARP, A_SHARP),
        ("B", NATURAL, B), ("B", SHARP, B_SHARP), ("B", FLAT, B_FLAT),
        ("C", NATURAL, C), ("C", SHARP, C_SHARP), ("C", FLAT, C_FLAT),
        ("D", NATURAL, D), ("D", SHARP, D_SHARP), ("D", FLAT, D_FLAT),
        ("E", NATURAL, E), ("E", SHARP, E_SHARP), ("E", FLAT, E_FLAT),
        ("F", NATURAL, F), ("F", SHARP, F_SHARP), ("F", FLAT, F_FLAT),
        ("G", NATURAL, G), ("G", SHARP, G_SHARP), ("G", FLAT, G_FLAT)]
)
def test_corresponding_note_naturals(note_name, accidental_mod, expected_note):
    assert expected_note == corresponding_note(note_name, accidental_mod)
