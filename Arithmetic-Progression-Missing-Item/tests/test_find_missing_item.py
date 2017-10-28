import pytest

from find_missing_item import find_missing

test_data = [([1, 2, 3, 5], 4),
             ([1, 3, 7, 9], 5),
             ([1, 3], 2)]


@pytest.mark.parametrize("ar_prog, expected", test_data)
def test_find_missing_item(ar_prog, expected):
    """Test finding missing item"""

    assert find_missing(ar_prog) == expected
