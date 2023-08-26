import logging
from dataclasses import dataclass

from lxml import etree

from pymusic import globalvars

log = logging.getLogger("parts")


@dataclass
class PartsBuilder:
    """
    Builds a list of parts.
    """

    @staticmethod
    def create_from_part_list_xml(part_list_xml: etree.Element):
        globalvars.prefix = globalvars.prefix.replace(":", "-> PartsBuilder:")
        log.info(f"{globalvars.prefix}starting building")
        print("\twithin parts file.")
        print(part_list_xml)

# TODOS:
# 2 - add logging .
