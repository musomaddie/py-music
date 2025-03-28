""" Tests for the slur file."""
import pytest

from pymusic.note.articulation.slur import Slur
from tests import create_xml


@pytest.mark.parametrize(
    ("notations_xml", "expected_result"),
    [
        (None, None),
        (create_xml(
            """ <notations> 
                </notations>"""), None),
        (create_xml(
            """ <notations>
                <slur />
                </notations>
            """), None),
        (create_xml(
            """ <notations>
                <slur type="start" />
                </notations>
            """), Slur.START),
        (create_xml(
            """ <notations>
                <slur type="stop" />
                </notations>
            """), Slur.END
        )
    ]
)
def test_from_xml(notations_xml, expected_result):
    assert Slur.from_xml(notations_xml) == expected_result
