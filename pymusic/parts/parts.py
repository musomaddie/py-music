import logging
from dataclasses import dataclass, field

from lxml import etree

from pymusic import globalvars, update_prefix
from .part import PartBuilder

log = logging.getLogger("parts")


@dataclass
class PartsBuilder:
    """
    Builds a list of parts.
    """

    # _additional_info: list = field(default_factory=list)
    # _title: str = ""
    # # _interesting_children_map = {
    # #     "part-list": PartsBuilder.create_from_part_list_xml
    # # }

    @staticmethod
    def create_from_part_list_xml(part_list_xml: etree.Element):
        update_prefix(":", "-> PartsBuilder:")
        log.info(f"{globalvars.prefix} building")

        # I don't think I have to care that much about part groups -> :).
        # TODO - handle part grouping.

        for item in part_list_xml.iter("score-part"):
            PartBuilder.create_from_part_list(item)
