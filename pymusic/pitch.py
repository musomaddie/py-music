from dataclasses import dataclass

from bs4 import Tag
from lxml.builder import unicode

from pymusic.note_name import NoteName, get_note_name_from_string
from pymusic.octave import Octave


@dataclass
class Pitch:
    """
    Identifies each note through their pitch_soup which generated through the step (note name)
    and the
    octave.

    Internal representation of the pitch_ element in MusicXML.

    .. _step: https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/pitch/

    :param step: the diatonic step value of this note
    :type step: NoteName
    :param octave: the octave of this note
    :type octave: Octave
    """
    step: NoteName
    octave: Octave

    @staticmethod
    def create_from_xml_soup(pitch_soup: Tag) -> 'Pitch':
        """
        Creates a Pitch instance from the provided MusicXML.

        The provided XML must contain both an <octave> and <step> element which must contain the
        octave number and string note name respectively. The following example creates a Pitch
        corresponding to middle C.

        .. code-block:: xml
            :emphasize-lines: 2,3

            <pitch_soup>
                <octave>4</octave>
                <step>C</step>
            </pitch_soup>

        :param pitch_soup: the XML containing this pitch_soup and passed through BeautifulSoup.
        :type pitch_soup: bs4.Tag
        :return: the created pitch_soup.
        :rtype: Pitch
        :raise ValueError: If the XML is cannot be parsed correctly to form a pitch_soup.

        TODO: display beautiful soup tag better!!
        """
        found_octave = pitch_soup.find("octave")
        found_step = pitch_soup.find("step")

        # TODO: add more useful information to these error messages - namely the bar and part.
        if found_octave is None:
            raise ValueError(f"The pitch_soup {pitch_soup} is missing an octave.")
        elif len(found_octave.contents) == 0:
            raise ValueError(f"The octave '{found_octave}' is missing content.")
        if found_step is None:
            raise ValueError(f"The pitch_soup {pitch_soup} is missing a step.")
        elif len(found_step.contents) == 0:
            raise ValueError(f"The step '{found_step}' is missing content")

        return Pitch(
            get_note_name_from_string(unicode(found_step.contents[0])),
            Octave(int(unicode(found_octave.contents[0])))
        )
