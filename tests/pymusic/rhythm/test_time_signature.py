""" Tests related to the time signature! """
from pymusic.rhythm.time_signature import TimeSignature
from tests import create_xml

N_DIVISIONS = "256"
N_BEATS = "4"
N_TYPE = "4"

DIVISION_ELEMENT = create_xml(
    f""" <divisions>{N_DIVISIONS}</divisions> """)

TIME_ELEMENT = create_xml(
    f""" <time color="#000000">
            <beats>{N_BEATS}</beats>
            <beat-type>{N_TYPE}</beat-type>
        </time> """)


def test_builder():
    time_sig = TimeSignature.from_xml(DIVISION_ELEMENT, TIME_ELEMENT)
    assert time_sig.divisions == int(N_DIVISIONS)
    assert time_sig.numerator == int(N_BEATS)
    assert time_sig.denominator == int(N_TYPE)
