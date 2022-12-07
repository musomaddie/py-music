from dataclasses import dataclass

from bs4 import NavigableString, Tag
from pytz import unicode

from pymusic.note_length import NoteLength
from pymusic.pitch import Pitch
from pymusic.vertical_direction import VerticalDirection


@dataclass
class Note:
    """
    Represents a single musical note

    Internal representation of the note_ element within Music XML. This representation is focused
    on musically identifiable / interesting aspects, to aid in comparisons and analysis.

    .. _note: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/note/

    :param pitch: the pitch_soup value of this note
    :type pitch: Pitch
    :param note_length: the notated length
    :type note_length: NoteLength
    :param duration: How long this note sounds for
    :type duration: int
    :param measure: the measure (bar) that contains this note
    :type measure: str
    :param instrument: the instrument which plays this note
    :type instrument: str
    :param voice: the voice which plays this note
    :type voice: str
    :param display_info: all information relating to the display of this note on the score
    :type display_info: dict
    """
    pitch: Pitch
    note_length: NoteLength
    duration: int  # TODO: custom class?
    measure: 'Measure'
    instrument: str  # TODO: link this to the instrument itself once I set that up.
    voice: int  # TODO: this might become more complicated when it gets to multi parts (etc.) ->
    display_info: dict


class NoteBuilder:
    """ A builder to create a Note. See NOTE (link) for parameters """

    def __init__(self) -> None:
        self.display_info = {}
        self.pitch = None
        self.measure = None
        self.duration = None
        self.instrument = None
        self.voice = None
        self.note_length = None
        # The display details are deliberately missing from the command mapping to make handling
        # easier.
        self.command_mapping = {
            "pitch": self.add_pitch,
            "duration": self.add_duration,
            "instrument": self.add_instrument,
            "voice": self.add_voice,
            "type": self.add_note_length,
        }

        self.display_info_processing = {
            "color": lambda value: value,
            "default-x": lambda value: int(value),
            "default-y": lambda value: int(value),
            "stem": lambda stem_soup: VerticalDirection.make_from_string(stem_soup.contents[0]),
            "staff": lambda staff_soup: int(staff_soup.contents[0])
        }

    def build(self) -> Note:
        """
        Creates and returns a valid note which contains the current state of this builder.

        :return: The newly created Note
        :rtype: Note
        """
        # TODO: ensure this is a valid note before constructing it.
        return Note(
            self.pitch, self.note_length, self.duration, self.measure, self.instrument,
            self.voice, self.display_info)

    def add_display_info(self, attr_name: str, attr_value: str):
        """
        Adds the given attribute name and value to the builders dictionary of display values.

        :param attr_name: the name of the attribute to add
        :type attr_name: str
        :param attr_value: the value this attribute has
        :type attr_value: str
        :return: None

        """
        self.display_info[attr_name] = attr_value

    def add_duration(self, duration_soup: Tag):
        """
        Adds the given duration to the builder.

        :param duration_soup: The tag element which contains the duration.
        :type duration_soup: Tag
        :return: None
        """
        self.duration = int(unicode(duration_soup.contents[0]))

    def add_instrument(self, instrument_soup: Tag):
        """
        Adds the given instrument to the builder.

        :param instrument_soup: The tag element which contains the instrument
        :type instrument_soup: Tag
        :return: None
        """
        self.instrument = instrument_soup["id"]

    def add_measure(self, measure: 'Measure'):
        """
        Adds the given measure (bar) to the builder.

        :param measure: the measure to add
        :type measure: Measure
        :return: None
        """
        self.measure = measure

    def add_note_length(self, note_length_soup: Tag):
        """
        Adds the note length found within the given soup to the builder

        :param note_length_soup: the tag containing the note length information
        :type note_length_soup: Tag
        :return: None
        """
        self.note_length = NoteLength.create_from_xml_soup(note_length_soup)

    def add_pitch(self, pitch_soup: Tag):
        """
        Adds the pitch found within the given soup to the builder

        :param pitch_soup: the tag containing the pitch information
        :type pitch_soup: Tag
        :return: None
        """
        self.pitch = Pitch.create_from_xml_soup(pitch_soup)

    def add_voice(self, voice_soup: Tag) -> 'NoteBuilder':
        """
        Adds the given voice to the builder.
        TODO: update this so that the voice is the parent type.

        :param voice_soup: adds the voice information as found in the tag
        :type voice_soup: Tag
        :return: None
        """
        self.voice = unicode(voice_soup.contents[0])
        return self

    @staticmethod
    def create_note_from_soup(note_soup: Tag) -> Note:
        builder = NoteBuilder()
        for att in note_soup.attrs:
            if att in builder.command_mapping:
                builder.command_mapping[att](note_soup.attrs[att])
            else:
                builder.add_display_info(att, builder.display_info_processing[att](note_soup.attrs[att]))

        for child in note_soup.children:
            if isinstance(child, NavigableString) and unicode(child).isspace():
                continue
            if child.name in builder.command_mapping:
                builder.command_mapping[child.name](child)
            else:
                builder.add_display_info(child.name, builder.display_info_processing[child.name](child))
        return builder.build()

    # Having random thoughts:
    # If I manage to represent this by plotting points with notes and durations this becomes
    # a computational geometry problem I can probably reasonably solve (maybe). (in terms of
    # efficiency)  -> might not actually make much difference though - I'm still just searching
    # for similarities over a large area. # Or turn it into a list of simpler objects will make
    # comparisons a bit easier. (depends a LOT on how I end up comparing words I think).
