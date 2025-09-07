import logging
from dataclasses import dataclass, field

from lxml.etree import Element

from pymusic.key.mode.mode import Mode
from pymusic.piano_util.note_finder import find_note_from_interval, find_note_from_n_semitones
from pymusic.piano_util.octave_util import get_all_base_octave_notes
from pymusic.pitch.accidental import Accidental
from pymusic.pitch.interval import Interval
from pymusic.pitch.note_name import NoteName
from pymusic.pitch.pitchnote import PitchNote

logger = logging.getLogger("key")


@dataclass
class KeyBuilder:
    """ Represents a musical key.

    link: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/key/
    """
    # TODO -> correct types!
    mode: Mode = None
    note: PitchNote = None
    octave: list[PitchNote] = field(default_factory=list)

    def glance(self):
        """ Returns a string representing this key at an easy glance. """
        return f"{self.note.glance()} {self.mode.mode_name}"

    def create_octave_scale(self):
        if self.mode is None or self.note is None:
            raise ValueError("Cannot create an octave scale for a key with no mode or note")

        all_octave_notes = get_all_base_octave_notes(self.note)

        prev_note = self.note
        cur_idx = 0
        processed_octave = [self.note]

        while True:
            if len(all_octave_notes) == 0:
                break
            next_note = find_note_from_interval(
                prev_note, self.mode.relative_intervals[cur_idx]
            ).get_note_from_name(NoteName.from_str(all_octave_notes.pop(0)))

            processed_octave.append(next_note)
            cur_idx += 1
            prev_note = next_note

        self.octave = processed_octave


def create_key_builder(key_element: Element) -> KeyBuilder:
    builder = KeyBuilder()
    builder.mode = Mode.find_mode_from_text(key_element.find("mode").text)
    fifths = int(key_element.find("fifths").text)
    builder.note = find_note_from_n_semitones(
        starting_note=PitchNote.C,
        n_semitones=Interval.PERF_5.n_semitones * fifths).get_note(
        Accidental.from_fifths(fifths)
    )

    builder.create_octave_scale()
    logger.debug(f"In {builder.glance()}")

    return builder
