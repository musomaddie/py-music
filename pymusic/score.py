from dataclasses import dataclass, field

import lxml
from lxml import etree


@dataclass
class Score:
    """
    Contains the overall score object. Acts as the top part of the tree, with all other objects extending from here.
    """
    title: str


@dataclass
class ScoreBuilder:
    _og_xml: lxml.etree._ElementTree
    _additional_info: list = field(default_factory=list)
    _title: str = ""

    def _find_title(self):
        """ Finds and adds the title from the xml."""
        root = self._og_xml.getroot()
        # find work
        for parent_element in root.iter("work"):
            for child_element in parent_element.iter("work-title"):
                self._title = child_element.text

    def _process_children(self):
        root = self._og_xml.getroot()
        interesting_children = ["part-list", "part"]
        for child in root:
            if child.tag not in interesting_children:
                self._additional_info.append(child)

    @staticmethod
    def create_from_musicxml_file(filename):
        builder = ScoreBuilder(etree.parse(filename))
        builder._find_title()
        builder._process_children()
        print(builder)
        # root = etree.parse(filename).getroot()
        #
        # for child in root:
        #     print(child.tag)
        #     print(type(child))
        # print(score_title.name)
        # print(score_title.attrs)
        # print(score_title.children)


if __name__ == '__main__':
    ScoreBuilder.create_from_musicxml_file("../tests/realexamples/lavender haze.musicxml")
