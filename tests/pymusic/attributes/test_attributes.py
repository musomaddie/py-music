from pymusic.attributes.attributes import Attributes
from tests import create_xml


def attribute_xml(
        key_fifths: int = 0,
        key_mode: str = "major",
        beats: int = 4,
        beat_type: int = 4,
        staves: int = 1,
        clef_sign: str = "G",
        clef_line: int = 2):
    return create_xml(
        f"""
            <attributes>
                <divisions>256</divisions>
                <key>
                    <fifths>{key_fifths}</fifths>
                    <mode>{key_mode}</mode>
                </key>
                <time>
                    <beats>{beats}</beats>
                    <beat-type>{beat_type}</beat-type>
                </time>
                <staves>{staves}</staves>
                <clef number="1">
                    <sign>{clef_sign}</sign>
                    <line>{clef_line}</line>
                </clef>
                </attributes>
        """
    )


def test_attribute():
    attributes = Attributes.from_xml(attribute_xml())
    assert attributes.time_signature.glance() == "4/4"
