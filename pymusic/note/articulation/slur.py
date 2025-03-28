from enum import Enum
from typing import Optional

from lxml import etree


class Slur(Enum):
    START = "start slur"
    MIDDLE = "mid slur"
    END = "end slur"

    @staticmethod
    def from_xml(notations_xml: Optional[etree.Element]) -> Optional['Slur']:
        # TODO -> handle notes in the middle of a slur!! (or rename method to indicate it only includes start / end).
        if notations_xml is None:
            return None
        # Attempt to find it.
        slur_xml = notations_xml.find("slur")
        if slur_xml is None:
            return None

        type_str = slur_xml.attrib.get("type")
        if type_str is None:
            return None

        if type_str == "start":
            return Slur.START
        elif type_str == "stop":
            return Slur.END
