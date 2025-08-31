from pymusic.xml_conversion.part import get_name, get_abbr, PartBuilder, create_part_builder
from tests import create_xml

PART_ID = "P1"
PART_NAME = "Test Part"
PART_ABBR = "T.Part."

PART_ELEMENT = create_xml(
    f"""
        <score-part id="{PART_ID}">
            <part-name>{PART_NAME}</part-name>
            <part-name-display>
                <display-text>Display Text</display-text>
            </part-name-display>
            <part-abbreviation>{PART_ABBR}</part-abbreviation>
        </score-part>
        """
)


def test_get_name():
    assert PART_NAME == get_name(PART_ELEMENT)


def test_get_abbreviation():
    assert PART_ABBR == get_abbr(PART_ELEMENT)


def test_create_part_builder():
    expected_part_builder = PartBuilder(
        id=PART_ID, name=PART_NAME, abbr=PART_ABBR
    )
    assert expected_part_builder == create_part_builder(PART_ELEMENT)
