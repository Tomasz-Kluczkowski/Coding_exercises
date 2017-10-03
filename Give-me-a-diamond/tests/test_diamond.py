import pytest

from diamond import diamond

invalid_input_data = {(-11, None), (-1, None), (0, None),
                           (2, None), (4, None)}

@pytest.mark.parametrize('n, expected', invalid_input_data)
def test_diamond_invalid_input(n, expected):
    """Check if function diamond returns None on an invalid input."""

    assert diamond(n) == expected


def test_basic_shape():
    """Test diamond production for n = 3."""

    assert diamond(3) == ' *\n***\n *\n'


def test_highher_n_value():
    """Test for n = 9."""

    assert diamond(9) == '    *\n   ***\n  *****\n *******\n*********\n' \
                         ' *******\n  *****\n   ***\n    *\n'
