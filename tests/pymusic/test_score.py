from io import BytesIO

from lxml import etree

from pymusic.score import ScoreBuilder

TITLE_ONLY_TEXT = BytesIO(
    b""" 
    <score-partwise version="3.0">
        <work> 
            <work-title>I am title</work-title> 
        </work> 
    </score-partwise>""")


class TestScoreBuilder:
    def test_find_title(self):
        builder = ScoreBuilder(etree.parse(TITLE_ONLY_TEXT))
        builder._find_title()
        assert builder._title == "I am title"
