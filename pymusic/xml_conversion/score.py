import logging
from dataclasses import dataclass, field

from lxml import etree
from lxml.etree import Element

from pymusic.xml_conversion.musicxml_identifiers import WORK_INFO, TITLE, PARTS
from pymusic.xml_conversion.parts import PartsBuilder, create_parts_builder

# Logging isn't working because we're not loading from any other packages. In the other version this works when we
# import from parts builder.
log = logging.getLogger("score")


@dataclass
class ScoreBuilder:
    title: str = ""
    parts: PartsBuilder = field(default_factory=PartsBuilder)


def get_title(score_element: Element) -> str:
    title = score_element.find(WORK_INFO).find(TITLE).text
    log.debug(f"Title: {title}")
    return title


def create_score_builder(score_element: Element):
    builder = ScoreBuilder()
    builder.title = get_title(score_element)
    builder.parts = create_parts_builder(score_element.find(PARTS))


def create_from_musicxml_file(filename: str):
    # TODO -> figure out logging!
    log.debug(f"creating from %s", filename)
    create_score_builder(etree.parse(filename))


if __name__ == "__main__":
    create_from_musicxml_file("tests/realexamples/lavender haze.musicxml")
