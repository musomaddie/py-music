import pytest

from pymusic.rhythm.time_signature import TimeSignature
from tests import create_xml

N_DIVISIONS = "256"
N_BEATS = "4"
N_TYPE = "4"


def division_xml(n_divisions: int = 256):
    return create_xml(f""" <divisions>{n_divisions}</divisions> """)


def create_time_xml(beats: int = 4, beat_type: int = 4):
    return create_xml(
        f"""
            <time>
                <beats>{beats}</beats>
                <beat-type>{beat_type}</beat-type>
            </time>
        """
    )


@pytest.mark.parametrize(
    ("time_xml", "expected_numerator", "expected_denominator"),
    [
        (create_time_xml(beats=2), 2, 4),
        (create_time_xml(2, 2), 2, 2),
        (create_time_xml(3, 2), 3, 2),
        (create_time_xml(3), 3, 4),
        (create_time_xml(3, 8), 3, 8),
        (create_time_xml(), 4, 4),
        (create_time_xml(5), 5, 4),
        (create_time_xml(5, 8), 5, 8),
        (create_time_xml(6), 6, 4),
        (create_time_xml(6, 8), 6, 8),
        (create_time_xml(7, 8), 7, 8)
    ]
)
def test_from_xml(time_xml, expected_numerator, expected_denominator):
    time_sig = TimeSignature.from_xml(division_xml(), time_xml)
    assert time_sig.divisions == int(N_DIVISIONS)
    assert time_sig.numerator == int(expected_numerator)
    assert time_sig.denominator == int(expected_denominator)
