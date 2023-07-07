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
    _title: str = ""
    _additional_info: dict[str, str] = field(default_factory=dict)

    def _find_title(self):
        """ Finds and adds the title from the xml."""
        root = self._og_xml.getroot()
        # find work
        for parent_element in root.iter("work"):
            for child_element in root.iter("work-title"):
                self._title = child_element.text

    def _process_children(self):
        root = self._og_xml.getroot()
        for child in root:
            print(child)

    @staticmethod
    def create_from_musicxml_file(filename):
        builder = ScoreBuilder(etree.parse(filename))
        builder._find_title()
        print(builder)
        builder._process_children()
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
