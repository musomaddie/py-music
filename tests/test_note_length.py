from unittest import TestCase

from pymusic.note_length import NoteLength


class TestNoteLength(TestCase):
    def test_basic(self):
        result = NoteLength("quarter")
        self.assertEqual("crochet", result.length_name)
        self.assertEqual(256, result.amount)
