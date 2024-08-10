""" key class """
import logging
from dataclasses import dataclass

from lxml import etree

from pymusic.key.mode import Mode
from pymusic.pitch import Note, Interval
from pymusic.pitch.note import CN
from pymusic.pitch.piano_keys import find_note_from_number_of_semitones

log = logging.getLogger("key")


@dataclass
class Key:
    """ Represents a musical key. """
    mode: Mode
    note: Note

    def glance(self) -> str:
        """ Returns a string representing this key at a glance. """
        return f"{self.note.glance()} {self.mode.mode_name}"


@dataclass
class KeyBuilder:
    """ Represents a key:
    link: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/key/
    """

    # TODO -> the simpler builders like this can be directly attached to their data class.
    @staticmethod
    def create_from_key_xml(og_xml: etree.Element) -> Key:
        """ Creates a Key from the given xml. """
        mode_xml = og_xml.find("mode")
        mode = Mode.find_mode_from_text(mode_xml.text)

        fifths_xml = og_xml.find("fifths")
        fifths = int(fifths_xml.text)
        note = find_note_from_number_of_semitones(
            starting_note=CN, semitones=(Interval.PERF_5.n_semitones * fifths)
        )
        key = Key(mode, note)
        log.debug(key)
        log.info(f"In {key.glance()}")
        return key
