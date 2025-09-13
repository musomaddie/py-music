import logging
from dataclasses import dataclass, field

from lxml.etree import Element

from pymusic.piano_util.chord_note_stacker import construct_chord_notes
from pymusic.pitch.accidental import create_accidental_from_element
from pymusic.pitch.chord_type import ChordType
from pymusic.pitch.pitchnote import PitchNote

log = logging.getLogger("chord_symbol")


@dataclass
class ChordSymbolBuilder:
    # TODO -> handle slash chords (including with an altered bass)

    root_note: PitchNote
    chord_type: ChordType
    all_notes: list[PitchNote] = field(init=False)

    def __post_init__(self):
        self.all_notes = construct_chord_notes(self.root_note, self.chord_type)

    def glance(self):
        name = f"{self.root_note.glance()}{self.chord_type.shorthand}"
        notes = " ".join([note.glance() for note in self.all_notes])
        return f"{name} ({notes})"


def get_root_note(root_note_element: Element) -> PitchNote:
    if root_note_element is None:
        raise ValueError("No root note element found, unable to process chord.")

    return PitchNote.corresponding_note(
        root_note_element.find("root-step").text,
        create_accidental_from_element(root_note_element.find("root-alter"))
    )


def create_chord_symbol_builder(harmony_element: Element) -> ChordSymbolBuilder:
    builder = ChordSymbolBuilder(
        get_root_note(harmony_element.find("root")),
        ChordType.from_element(harmony_element)
    )

    log.debug(f"Chord: {builder.glance()}")

    return builder
