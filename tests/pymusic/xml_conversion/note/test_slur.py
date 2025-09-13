import pytest

from pymusic.articulation.slur_marker import SlurMarker
from pymusic.xml_conversion.note.slur import SlurBuilder, create_slur_builder
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
                <slur type="start" />
                </notations>
            """), SlurBuilder(SlurMarker.START)),
        (create_xml(
            """ <notations>
                <slur type="stop" />
                </notations>
            """), SlurBuilder(SlurMarker.END)
        )
    ]
)
def test_create_slur_builder(notations_xml, expected_result):
    assert create_slur_builder(notations_xml) == expected_result


@pytest.mark.parametrize(
    "type_str", ["", """type="unknown" """]
)
def test_create_slur_builder_raises_exception_on_unknown_slur_type(type_str):
    with pytest.raises(ValueError):
        create_slur_builder(create_xml(
            f""" <notations>
                <slur  {type_str} />
                </notations>
            """))
