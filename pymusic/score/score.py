import logging
from dataclasses import dataclass, field

import lxml
from lxml import etree

from pymusic import globalvars
from pymusic.parts import PartsBuilder

log = logging.getLogger("score")


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
    _interesting_children_map = {
        "part-list": PartsBuilder.create_from_part_list_xml
    }

    # TODO: add links to parts, and links to bars.
    # This is all gonna be one crazy connected tree / graph thing, but that's ok.

    def find_title(self):
        """ Finds and adds the title from the xml."""
        root = self._og_xml.getroot()
        for parent_element in root.iter("work"):
            for child_element in parent_element.iter("work-title"):
                self._title = child_element.text
                log.debug(f"{globalvars.prefix}title - %s", self._title)

    def process_children(self):
        root = self._og_xml.getroot()
        for child in root:
            if child.tag in self._interesting_children_map:
                self._interesting_children_map[child.tag](child)
            if child.tag not in self._interesting_children_map:
                self._additional_info.append(child)

    @staticmethod
    def create_from_musicxml_file(filename):
        globalvars.prefix = "ScoreBuilder:"
        log.info(f"{globalvars.prefix} creating from %s", filename)
        builder = ScoreBuilder(etree.parse(filename))
        builder.find_title()
        builder.process_children()


if __name__ == '__main__':
    ScoreBuilder.create_from_musicxml_file("tests/realexamples/lavender haze.musicxml")
