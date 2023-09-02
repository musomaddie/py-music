from io import BytesIO

from lxml import etree

from pymusic.parts.part import PartBuilder

PART_ID = "P1"
PART_NAME = "Test Part"
PART_ABBR = "T.Part."

PART_ELEMENT = etree.parse(
    BytesIO(
        f"""
        <score-part id="{PART_ID}">
            <part-name>{PART_NAME}</part-name>
            <part-name-display>
                <display-text>Display Text</display-text>
            </part-name-display>
            <part-abbreviation>{PART_ABBR}</part-abbreviation>
        </score-part>
        """.encode()
    )
).getroot()


class TestPartBuilder:
    def test_part_id(self):
        builder = PartBuilder.create_from_part_list(PART_ELEMENT)
        assert builder.part_id == "P1"

    def test_part_name(self):
        builder = PartBuilder.create_from_part_list(PART_ELEMENT)
        assert builder._part_name == PART_NAME

    def test_part_abbr(self):
        builder = PartBuilder.create_from_part_list(PART_ELEMENT)
        assert builder._part_abbr == PART_ABBR
