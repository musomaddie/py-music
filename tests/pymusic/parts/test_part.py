from pymusic.parts.part import _PartBuilder
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


class TestPartBuilder:
    def test_part_id(self):
        builder = _PartBuilder(PART_ELEMENT)
        assert builder.part_id == "P1"

    def test_part_name(self):
        builder = _PartBuilder(PART_ELEMENT)
        assert builder.part_name == PART_NAME

    def test_part_abbr(self):
        builder = _PartBuilder(PART_ELEMENT)
        assert builder.part_abbr == PART_ABBR
