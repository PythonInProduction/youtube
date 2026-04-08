import pytest
from launch import can_launch


@pytest.mark.parametrize(
    "is_armed, safety_key_inserted, expected",
    [
        (True, True, True),
        (False, True, False),
        (True, False, False),
    ],
)
def test_can_launch(is_armed, safety_key_inserted, expected):
    assert can_launch(is_armed, safety_key_inserted) is expected
