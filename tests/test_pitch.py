from unittest import TestCase

from bs4 import BeautifulSoup

from pymusic.note_name import NoteName
from pymusic.octave import Octave
from pymusic.pitch import Pitch


class TestCreateFromXmlSoup(TestCase):
    def test_basic(self):
        xml_soup = """ <pitch> <step>C</step> <octave>4</octave> </pitch> """
        result = Pitch.create_from_xml_soup(BeautifulSoup(xml_soup, "xml").find("pitch"))
        self.assertEqual(NoteName.C, result.step)
        self.assertEqual(Octave(4), result.octave)

    def test_missing_octave(self):
        xml_soup = """ <pitch> <step> C </step> </pitch> """
        self.assertRaises(ValueError, Pitch.create_from_xml_soup, BeautifulSoup(xml_soup, "xml"))

    def test_missing_step(self):
        xml_soup = """ <pitch> <octave>4</octave> </pitch>"""
        self.assertRaises(ValueError, Pitch.create_from_xml_soup, BeautifulSoup(xml_soup, "xml"))

    def test_with_spaces(self):
        xml_soup = """ <pitch> <octave> 4 </octave> <step> C </step> </pitch> """
        result = Pitch.create_from_xml_soup(BeautifulSoup(xml_soup, "xml").find("pitch"))
        self.assertEqual(NoteName.C, result.step)
        self.assertEqual(Octave(4), result.octave)

    def test_with_missing_octave_number(self):
        xml_soup = """ <pitch> <octave></octave> <step> C </step> </pitch>"""
        self.assertRaises(ValueError, Pitch.create_from_xml_soup, BeautifulSoup(xml_soup, "xml"))

    def test_missing_note_name(self):
        xml_soup = """ <pitch> <octave>4</octave> <step>H</step> </pitch>"""
        self.assertRaises(ValueError, Pitch.create_from_xml_soup, BeautifulSoup(xml_soup, "xml"))
