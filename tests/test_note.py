from unittest import TestCase

from bs4 import BeautifulSoup

from pymusic.note import NoteBuilder
from pymusic.note_length import NoteLength
from pymusic.note_name import NoteName
from pymusic.octave import Octave
from pymusic.pitch import Pitch
from pymusic.vertical_direction import VerticalDirection


class TestNoteBuilder(TestCase):
    # self.assertEqual(expected, actual)
    def setUp(self) -> None:
        self.note_builder = NoteBuilder()
        self.example_note_xml = """ <note color="#000000" default-x="75" default-y="-15"> 
        <pitch> <step>C</step> <octave>4</octave> </pitch> <duration>512</duration> <instrument 
        id="P1-I1"/> <voice>1</voice> <type>half</type> <stem>up</stem> <staff>1</staff> </note> """
        self.note_soup = BeautifulSoup(self.example_note_xml, "xml")


class TestAddDisplayInfo(TestNoteBuilder):
    def test_add_display_info(self):
        self.note_builder.add_display_info("attr_name", "attr_value")
        self.assertEqual(1, len(self.note_builder.display_info))
        self.assertTrue("attr_name" in self.note_builder.display_info)
        self.assertEqual("attr_value", self.note_builder.display_info["attr_name"])


class TestAddDuration(TestNoteBuilder):
    def test_add_duration(self):
        self.note_builder.add_duration(self.note_soup.find("duration"))
        self.assertEqual(512, self.note_builder.duration)


class TestAddInstrument(TestNoteBuilder):
    # TODO: update this test as this should be the parent instrument to the whole thing
    def test_add_instrument(self):
        self.note_builder.add_instrument(self.note_soup.find("instrument"))
        self.assertEqual("P1-I1", self.note_builder.instrument)


class TestAddMeasure(TestNoteBuilder):
    def test_add_measure(self):
        # TODO: update the passed variable
        expected_measure = "This is a measure"
        self.note_builder.add_measure(expected_measure)
        self.assertEqual(expected_measure, self.note_builder.measure)


class TestAddNoteLength(TestNoteBuilder):
    def test_add_note_length(self):
        self.note_builder.add_note_length(self.note_soup.find("type"))
        self.assertEqual(NoteLength("half"), self.note_builder.note_length)


class TestAddPitch(TestNoteBuilder):
    def test_add_pitch(self):
        self.note_builder.add_pitch(self.note_soup.find("pitch"))
        self.assertEqual(NoteName.C, self.note_builder.pitch.step)
        self.assertEqual(4, self.note_builder.pitch.octave.value)


class TestAddVoice(TestNoteBuilder):
    def test_add_voice(self):
        # TODO: update this type to voice once it's added.
        self.note_builder.add_voice(self.note_soup.find("voice"))
        self.assertEqual("1", self.note_builder.voice)


class TestBuild(TestNoteBuilder):
    def test_empty(self):
        note = self.note_builder.build()
        self.assertEqual(0, len(note.display_info))
        self.assertIsNone(note.pitch)
        self.assertIsNone(note.measure)
        self.assertIsNone(note.duration)
        self.assertIsNone(note.instrument)
        self.assertIsNone(note.voice)
        self.assertIsNone(note.note_length)

    def test_all_values(self):
        # TODO: update to correct types.
        self.note_builder.add_display_info("info name", "info val")
        self.note_builder.add_duration(self.note_soup.find("duration"))
        self.note_builder.add_instrument(self.note_soup.find("instrument"))
        self.note_builder.add_measure("measure")
        self.note_builder.add_note_length(self.note_soup.find("type"))
        self.note_builder.add_pitch(self.note_soup.find("pitch"))
        self.note_builder.add_voice(self.note_soup.find("voice"))
        note = self.note_builder.build()

        self.assertEqual(Pitch(NoteName.C, Octave(4)), note.pitch)
        self.assertEqual(NoteLength("half"), note.note_length)
        self.assertEqual(512, note.duration)
        self.assertEqual("measure", note.measure)
        self.assertEqual("P1-I1", note.instrument)
        self.assertEqual("1", note.voice)
        self.assertEqual({"info name": "info val"}, note.display_info)


class TestCreateNoteFromSoup(TestNoteBuilder):
    def test_basic(self):
        resulting_note = NoteBuilder.create_note_from_soup(self.note_soup.find("note"))

        self.assertEqual(
            {"color": "#000000", "default-x": 75, "default-y": -15, "staff": 1, "stem": VerticalDirection.UP},
            resulting_note.display_info)
        self.assertEqual(Pitch(NoteName.C, Octave(4)), resulting_note.pitch)
        self.assertEqual(512, resulting_note.duration)
        self.assertEqual("P1-I1", resulting_note.instrument)
        self.assertEqual("1", resulting_note.voice)
        self.assertEqual(NoteLength("half"), resulting_note.note_length)
