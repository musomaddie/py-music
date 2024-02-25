""" Tests related to the time signature! """
from io import BytesIO

from lxml import etree

from pymusic.rhythm.time_signature import TimeSignatureBuilder

N_DIVISIONS = "256"
N_BEATS = "4"
N_TYPE = "4"

DIVISION_ELEMENT = etree.parse(
    BytesIO(
        f"""
        <divisions>{N_DIVISIONS}</divisions>
        """.encode()
    )
).getroot()

TIME_ELEMENT = etree.parse(
    BytesIO(
        f"""
        <time color="#000000">
            <beats>{N_BEATS}</beats>
            <beat-type>{N_TYPE}</beat-type>
        </time>
        """.encode()
    )
).getroot()


def test_builder():
    time_sig = TimeSignatureBuilder.create_from_xml(DIVISION_ELEMENT, TIME_ELEMENT)
    assert time_sig.divisions == int(N_DIVISIONS)
    assert time_sig.numerator == int(N_BEATS)
    assert time_sig.denominator == int(N_TYPE)
