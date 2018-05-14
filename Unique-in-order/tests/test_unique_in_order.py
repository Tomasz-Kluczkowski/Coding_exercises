import pytest

from unique_in_order import unique_in_order

test_data = [('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
             ('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']),
             ([1, 2, 2, 3, 3], [1, 2, 3])]


@pytest.mark.parametrize("input_sequence, expected", test_data)
def test_unique_in_order(input_sequence, expected):
    """Test finding missing item"""

    assert unique_in_order(input_sequence) == expected
