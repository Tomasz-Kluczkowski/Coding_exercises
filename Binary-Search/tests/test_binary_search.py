import pytest

from binary_search import binary_search, binary_search_recursive

test_data = [([1, 2, 3, 4], 4, 3),
             ([1, 3, 7, 9], 3, 1),
             ([1, 3], 2, None),
             ([x for x in range(100000)], 50099, 50099)]


@pytest.mark.parametrize("input_list, item, expected", test_data)
def test_binary_search(input_list, item, expected):
    """Test binary search"""

    assert binary_search(input_list, item) == expected


@pytest.mark.parametrize("input_list, item, expected", test_data)
def test_binary_search_recursive(input_list, item, expected):
    """Test binary search recursive"""

    assert binary_search_recursive(input_list, item) == expected
