import logging
from dataclasses import dataclass

from lxml import etree

from pymusic.key import find_mode_from_text, Mode, MAJOR
from pymusic.pitch import C, PERFECT_5th, KEYBOARD_OCTAVE_SHARPS, KEYBOARD_OCTAVE_FLATS, Note, C_FLAT

log = logging.getLogger("key")


@dataclass
class Key:
    """ Represents a key."""
    mode: Mode
    note: Note

    def glance(self) -> str:
        """ Returns a string representing this key at a glance. """
        return f"{self.note.name} {self.mode.name.lower()}"


@dataclass
class KeyBuilder:
    """ Represents a key:

    link: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/key/
    """

    # TODO -> the simpler builders like this can be directly attached to their data class.
    @staticmethod
    def create_from_key_xml(og_xml: etree.Element) -> Key:
        """ Creates a key builder from the given item. """

        fifths_xml = og_xml.find("fifths")
        fifths = int(fifths_xml.text)
        mode_xml = og_xml.find("mode")
        mode = find_mode_from_text(mode_xml.text)

        keyboard = KEYBOARD_OCTAVE_SHARPS
        if fifths < 0:
            keyboard = KEYBOARD_OCTAVE_FLATS

        # TODO -> check mode time (right now only major is supported)
        starting_note = C
        starting_note_idx = keyboard.index(starting_note)
        fifths_gap = PERFECT_5th.distance * fifths
        key_note = keyboard[(starting_note_idx + fifths_gap) % len(keyboard)]

        # TODO -> generalise the special case a little more.
        if fifths == -7 and mode == MAJOR:
            key_note = C_FLAT

        key = Key(mode, key_note)
        log.debug(key)
        log.info(f"In {key.glance()}")
        return key
