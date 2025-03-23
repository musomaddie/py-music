import pytest

from pymusic.rhythm.note_duration import Duration


@pytest.mark.parametrize(
    ("divisions", "duration", "type_str", "expected_name"),
    [
        (256, 512, "half", "minim"),
        (256, 1024, "whole", "semibreve"),
        (256, 64, "16th", "semiquaver"),
        (256, 128, "eighth", "quaver"),
        (256, 256, "quarter", "crochet"),
        (256, 192, "eighth", "dotted quaver"),
        (256, 512, None, "minim"),
        (256, 512, None, "minim"),
        (256, 1024, None, "semibreve"),
        (256, 64, None, "semiquaver"),
        (256, 128, None, "quaver"),
        (256, 256, None, "crochet"),
        (256, 192, None, "dotted quaver"),
    ]
)
def test_create(divisions, duration, type_str, expected_name):
    duration = Duration.create(divisions, duration, type_str)
    assert duration.desc == expected_name
