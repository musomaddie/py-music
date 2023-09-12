import pytest

from pymusic.key import MAJOR, MINOR, HARMONIC_MINOR, IONIAN, DORIAN, LYDIAN, PHRYGIAN, MIXOLYDIAN, AEOLIAN, LOCRIAN


@pytest.mark.parametrize(
    "mode",
    (MAJOR, MINOR, HARMONIC_MINOR, IONIAN, DORIAN, PHRYGIAN, LYDIAN, MIXOLYDIAN, AEOLIAN, LOCRIAN))
def testCreatedMode(mode):
    # Should have 8 intervals and 7 relative intervals.
    assert len(mode.intervals) == 8
    assert len(mode.intervals_relative) == 7

    current_relative_distance = 0
    for i in range(6):
        current_relative_distance += mode.intervals_relative[i].distance
        assert current_relative_distance == mode.intervals[i + 1].distance
