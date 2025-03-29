""" Tests for the grace note xml item. """
import pytest


@pytest.mark.parametrize(
    ("slash", "slur", "expected_glance"),
    [
        ("no", "no", "𝆔 G(3) 𝅘𝅥𝅮"),
        ("no", "yes", "𝆔 (start slur) G(3) 𝅘𝅥"),
        ("yes", "no", "𝆔 G(3) 𝅘𝅥𝅮"),
        ("yes", "yes", "𝆔 (start slur) G(3) 𝅘𝅥𝅮")
    ]
)
def test_single_grace_note(slash, slur, expected_glance):
    print(expected_glance)
