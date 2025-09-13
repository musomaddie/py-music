""" stacks notes to form chords."""
from dataclasses import dataclass, field

from pymusic.key.mode.mode import Mode
from pymusic.piano_util.note_finder import find_note_from_n_semitones
from pymusic.pitch.accidental import Accidental
from pymusic.pitch.chord_type import ChordType
from pymusic.pitch.interval import Interval
from pymusic.pitch.pitchnote import PitchNote
from pymusic.xml_conversion.key import KeyBuilder


def _map_interval_to_idx(interval: Interval) -> int:
    """ Maps an interval to an index in the octave list. """
    match interval:
        case Interval.UNI:
            return 0
        case Interval.MIN_2 | Interval.MAJ_2 | Interval.MAJ_9:
            return 1
        case Interval.MIN_3 | Interval.MAJ_3 | Interval.AUG_9:
            return 2
        case Interval.PERF_4 | Interval.PERF_11:
            return 3
        case Interval.PERF_5:
            return 4
        case Interval.MIN_6 | Interval.MAJ_6 | Interval.MAJ_13:
            return 5
        case Interval.MIN_7 | Interval.MAJ_7:
            return 6

        case _:
            raise ValueError(f"Could not find index for {interval}")


_chord_type_to_mode_map = {
    ChordType.MAJ: Mode.MAJOR,
    ChordType.MIN: Mode.MINOR,
    ChordType.DIM: Mode.MINOR,
    ChordType.AUG: Mode.MAJOR,
    ChordType.SUS_4: Mode.MAJOR,
    ChordType.SUS_2: Mode.MAJOR,
    ChordType.ITALIAN: Mode.MIXOLYDIAN,
    ChordType.FRENCH: Mode.MIXOLYDIAN,
    ChordType.MAJ_6: Mode.MAJOR,
    ChordType.MIN_6: Mode.MINOR,
    ChordType.NEAPOLITAN: Mode.LOCRIAN,
    ChordType.AUG_7: Mode.MIXOLYDIAN,
    ChordType.DIM_7: Mode.MINOR,
    ChordType.DOM: Mode.MIXOLYDIAN,
    ChordType.HALF_DIM: Mode.MINOR,
    ChordType.MIN_MAJ: Mode.HARMONIC_MINOR,
    ChordType.MAJ_7: Mode.MAJOR,
    ChordType.MIN_7: Mode.MINOR,
    ChordType.DOM_9: Mode.MIXOLYDIAN,
    ChordType.MAJ_9: Mode.MAJOR,
    ChordType.MIN_9: Mode.MINOR,
    ChordType.DOM_11: Mode.MIXOLYDIAN,
    ChordType.MAJ_11: Mode.MAJOR,
    ChordType.MIN_11: Mode.MINOR,
    ChordType.DOM_13: Mode.MIXOLYDIAN,
    ChordType.MAJ_13: Mode.MAJOR,
    ChordType.MIN_13: Mode.MINOR,
    ChordType.PEDAL: Mode.MAJOR,
    ChordType.POWER: Mode.MAJOR,
    ChordType.TRISTAN: Mode.MINOR,
}


@dataclass
class ChordNoteModifiers:
    interval_to_change: Interval
    interval_to_use: Interval
    accidental_to_use: Accidental


def _get_extra_modifiers(chord_type: ChordType) -> list[ChordNoteModifiers]:
    """ Returns a list of extra modifiers to use for a chord type. """
    flat_fifth = ChordNoteModifiers(Interval.TRI, Interval.PERF_5, Accidental.FLAT)
    sharp_fifth = ChordNoteModifiers(Interval.MIN_6, Interval.PERF_5, Accidental.SHARP)
    match chord_type:
        case ChordType.DIM:
            return [flat_fifth]
        case ChordType.AUG:
            return [sharp_fifth]
        case ChordType.FRENCH:
            return [flat_fifth]
        case ChordType.AUG_7:
            return [sharp_fifth]
        case ChordType.DIM_7:
            return [flat_fifth, ChordNoteModifiers(Interval.MAJ_6, Interval.MIN_7, Accidental.FLAT)]
        case ChordType.HALF_DIM:
            return [flat_fifth]
        case ChordType.MIN_13:
            return [ChordNoteModifiers(Interval.MAJ_13, Interval.MAJ_6, Accidental.SHARP)]
        case ChordType.TRISTAN:
            return [flat_fifth]
        case _:
            return []


@dataclass
class ChordNoteStackerHelper:
    chord_type: ChordType
    mode: Mode
    extra_modifiers: list[ChordNoteModifiers]
    octave_notes: list[PitchNote] = field(init=False)

    def _find_modified_interval(self, interval: Interval) -> Interval:
        for modifier in self.extra_modifiers:
            if modifier.interval_to_change == interval:
                return modifier.interval_to_use
        return interval

    def _adjust_note(self, note: PitchNote, interval: Interval):
        for modifier in self.extra_modifiers:
            if modifier.interval_to_change == interval:
                return find_note_from_n_semitones(
                    note, modifier.accidental_to_use.n_semitones).get_note_from_name(
                    note.note_name
                )
        return note

    def _find_corresponding_idx(self, interval: Interval) -> int:
        return _map_interval_to_idx(self._find_modified_interval(interval))

    def _find_note(self, interval: Interval) -> PitchNote:
        base_note = self.octave_notes[self._find_corresponding_idx(interval)]
        return self._adjust_note(base_note, interval)

    def stack_notes(self, root_note: PitchNote) -> list[PitchNote]:
        """ Stacks notes to form a chord. """
        self.octave_notes = KeyBuilder(self.mode, root_note).octave
        return [
            self._find_note(interval) for interval in self.chord_type.intervals
        ]

    @staticmethod
    def from_chord_type(chord_type: ChordType) -> 'ChordNoteStackerHelper':
        return ChordNoteStackerHelper(
            chord_type,
            _chord_type_to_mode_map[chord_type],
            _get_extra_modifiers(chord_type)
        )


def construct_chord_notes(
        root_note: PitchNote,
        chord_type: ChordType
) -> list[PitchNote]:
    """

    :param root_note:
    :param chord_type:
    :return:
    """
    return ChordNoteStackerHelper.from_chord_type(chord_type).stack_notes(root_note)
