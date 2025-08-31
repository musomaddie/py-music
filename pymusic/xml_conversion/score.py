import logging
from dataclasses import dataclass

from lxml import etree
from lxml.etree import Element

# Logging isn't working because we're not loading from any other packages. In the other version this works when we
# import from parts builder.
log = logging.getLogger(__name__)


@dataclass
class ScoreBuilder:
    title: str = ""
    # TODO -> parts ....


def get_title(score_element: Element) -> str:
    title = score_element.find("work").find("work-title").text
    log.debug(f"Title: {title}")
    return title


def build_score(score_element: Element):
    builder = ScoreBuilder()
    builder.title = get_title(score_element)

    print(builder)


def create_from_musicxml_file(filename: str):
    # TODO -> figure out logging!
    log.debug(f"creating from %s", filename)
    build_score(etree.parse(filename))


if __name__ == "__main__":
    create_from_musicxml_file("tests/realexamples/lavender haze.musicxml")
