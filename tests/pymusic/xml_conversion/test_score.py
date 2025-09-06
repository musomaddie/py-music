from pymusic.xml_conversion.score import get_title
from tests import create_xml

TITLE = "I am A title"

TITLE_ONLY_CONTENT = create_xml(
    f"""
    <score-partwise version="3.0">
        <work> 
            <work-title>{TITLE}</work-title> 
        </work> 
    </score-partwise>
    """)


def test_title():
    assert TITLE == get_title(TITLE_ONLY_CONTENT)
