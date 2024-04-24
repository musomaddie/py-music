import logging
from dataclasses import dataclass

from lxml import etree

from pymusic.key import find_mode_from_text, Mode
from pymusic.pitch import C, KEYBOARD_OCTAVE, PERFECT_5th, BlackNote, Note

log = logging.getLogger("key")


@dataclass
class Key:
    """ Represents a key."""
    mode: Mode
    note: Note | BlackNote
    human_readable: str

    def glance(self) -> str:
        """ Returns a string representing this key at a glance. """
        return self.human_readable


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

        # TODO -> check mode time (right now only major is supported)
        starting_note = C
        starting_note_idx = KEYBOARD_OCTAVE.index(starting_note)
        fifths_gap = PERFECT_5th.distance * fifths
        key_note = KEYBOARD_OCTAVE[(starting_note_idx + fifths_gap) % len(KEYBOARD_OCTAVE)]

        # Let's make the human-readable string.
        if isinstance(key_note, Note):
            note_str = key_note.name.name
        else:
            if fifths < 0:
                note_str = f"{key_note.note_above.name.name}b"
            else:
                note_str = f"{key_note.note_below.name.name}#"

        key = Key(mode, key_note, f"{note_str} {mode.name.lower()}")
        log.debug(key)
        log.info(f"In {key.glance()}")
        return key
