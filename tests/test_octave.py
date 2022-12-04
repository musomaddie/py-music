from unittest import TestCase

from pymusic.octave import Octave


class TestOctaveConstruction(TestCase):

    def test_valid(self):
        for i in range(1, 10):
            octave = Octave(i)
            self.assertEqual(i, octave.value)

    def test_zero(self):
        self.assertRaises(ValueError, Octave, 0)

    def test_ten(self):
        self.assertRaises(ValueError, Octave, 10)
