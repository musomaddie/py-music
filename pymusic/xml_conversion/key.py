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


def _create_octave_scale(mode: Mode, starting_note: PitchNote) -> list[PitchNote]:
    all_octave_notes = get_all_base_octave_notes(starting_note)

    prev_note = starting_note
    cur_idx = 0
    processed_octave = [starting_note]

    while True:
        if len(all_octave_notes) == 0:
            break
        next_note = find_note_from_interval(
            prev_note, mode.relative_intervals[cur_idx]
        ).get_note_from_name(NoteName.from_str(all_octave_notes.pop(0)))

        processed_octave.append(next_note)
        cur_idx += 1
        prev_note = next_note

    return processed_octave


@dataclass
class KeyBuilder:
    """ Represents a musical key.

    link: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/key/
    """
    # TODO -> correct types!
    mode: Mode
    note: PitchNote
    octave: list[PitchNote] = field(init=False)

    def glance(self):
        """ Returns a string representing this key at an easy glance. """
        return f"{self.note.glance()} {self.mode.mode_name}"

    def __post_init__(self):
        self.octave = _create_octave_scale(self.mode, self.note)


def _find_mode(key_element: Element) -> Mode:
    return Mode.find_mode_from_text(key_element.find("mode").text)


def _find_note(key_element: Element) -> PitchNote:
    fifths = int(key_element.find("fifths").text)
    return find_note_from_n_semitones(
        starting_note=PitchNote.C,
        n_semitones=Interval.PERF_5.n_semitones * fifths).get_note(
        Accidental.from_fifths(fifths)
    )


def create_key_builder(key_element: Element) -> KeyBuilder:
    builder = KeyBuilder(_find_mode(key_element), _find_note(key_element))

    logger.debug(f"In {builder.glance()}")

    return builder
