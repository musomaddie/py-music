from pymusic.xml_conversion.bar_attributes import create_bar_attributes_builder
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
    bar_attr_builder = create_bar_attributes_builder(attribute_xml())
    assert bar_attr_builder.time_signature_builder.glance() == "4/4"
    assert bar_attr_builder.key_builder.glance() == "C major"
    assert bar_attr_builder.clef_builder.glance() == "𝄞"
