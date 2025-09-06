from io import BytesIO

from lxml import etree

from pymusic.original.score import ScoreBuilder

TITLE_ONLY_TEXT = BytesIO(
    b""" 
    <score-partwise version="3.0">
        <work> 
            <work-title>I am title</work-title> 
        </work> 
    </score-partwise>""")

BORING_CHILDREN_TEXT = BytesIO(
    b"""
    <score-partwise version="3.0">
        <child_1> adjk;afjdkl;ajg;ikldasj </child_1>
        <child_2> fjfjffjfj </child_2>
    </score-partwise>""")


class TestScoreBuilder:
    def test_find_title(self):
        builder = ScoreBuilder(etree.parse(TITLE_ONLY_TEXT))
        builder.find_title()
        assert builder._title == "I am title"

    def test_process_children_non_interesting(self):
        builder = ScoreBuilder(etree.parse(BORING_CHILDREN_TEXT))
        builder.process_children()
        assert len(builder._additional_info) == 2
