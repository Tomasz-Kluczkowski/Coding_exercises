import pytest

from rgb_to_hex import rgb

test_data = [(0, 0, 0, "000000"),
             (255, 255, 255, "FFFFFF"),
             (254, 254, 254, "FEFEFE"),
             (16, 16, 32, "101020"),
             (1, 1, 1, "010101"),
             (128, 127, 129, "807F81"),
             (-10, -10, -10, "000000"),
             (300, 3000, 345, "FFFFFF")]


@pytest.mark.parametrize("r, g, b, expected", test_data)
def test_rgb(r, g, b, expected):
    """Tests proper conversion of decimal values to hexadecimal."""

    assert rgb(r, g, b) == expected
