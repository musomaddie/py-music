import logging
from dataclasses import dataclass, field

from lxml import etree

from pymusic import update_prefix, globalvars

log = logging.getLogger("part-group")


@dataclass
class PartGroupBuilder:
    """
    Builds a part group instance.
    """
    group_id: str
    og_xml: etree.Element
    parts: list = field(default_factory=list)

    @staticmethod
    def create_from_xml(part_group_xml: etree.Element):
        update_prefix(":", "-> PartGroupBuilder:")
        # log.info(f"{globalvars.prefix} [{builder.group_id}]")
