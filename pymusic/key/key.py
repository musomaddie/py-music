""" key class """
import logging
from dataclasses import dataclass, field

from lxml import etree

from pymusic.key.mode import Mode
from pymusic.pitch import PitchNote, Interval
from pymusic.pitch.accidentals import Accidental
from pymusic.pitch.piano_keys import find_note_from_number_of_semitones, find_note_from_interval
from pymusic.pitch.pitchnote import NoteName

log = logging.getLogger("key")


def _create_octave_scale(mode: Mode, starting_note: PitchNote) -> list[PitchNote]:
    all_notes_str = "ABCDEFGABCDEF"
    all_notes = list(all_notes_str[all_notes_str.find(starting_note.note_name.name) + 1:all_notes_str.find(
        starting_note.note_name.name) + 7])

    prev_note = starting_note
    cur_idx = 0
    octave = [starting_note]

    while True:
        if len(all_notes) == 0:
            break

        next_note = find_note_from_interval(
            prev_note, mode.intervals_relative[cur_idx]
        ).get_note_from_name(NoteName.from_str(all_notes.pop(0)))

        octave.append(next_note)
        cur_idx += 1
        prev_note = next_note

    return octave


@dataclass
class Key:
    """ Represents a musical key.

    link: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/key/
    """
    mode: Mode
    note: PitchNote
    octave: list[PitchNote] = field(init=False)

    def __post_init__(self):
        self.octave = _create_octave_scale(self.mode, self.note)

    def glance(self) -> str:
        """ Returns a string representing this key at a glance. """
        return f"{self.note.glance()} {self.mode.mode_name}"

    @staticmethod
    def from_xml(og_xml: etree.Element) -> 'Key':
        """ Creates a Key from the given xml. """
        mode_xml = og_xml.find("mode")
        mode = Mode.find_mode_from_text(mode_xml.text)

        fifths_xml = og_xml.find("fifths")
        fifths = int(fifths_xml.text)
        note = find_note_from_number_of_semitones(
            starting_note=PitchNote.C, semitones=(Interval.PERF_5.n_semitones * fifths)
        ).get_note(
            Accidental.from_int(fifths)
        )
        key = Key(mode, note)
        log.debug(key)
        log.info(f"In {key.glance()}")
        return key
