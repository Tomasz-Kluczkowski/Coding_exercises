import pytest

from nth_smallest_element import nth_smallest, nth_smallest_order_n

test_data = [([14, 12, 46, 34, 334], 3, 34),
             ([45, -10, 4, 5, 4], 4, 45),
             ([1, 3, 4, 5], 7, None),
             ([4, 3, 4, 5], 4, None)]


@pytest.mark.parametrize('arr, n, expected', test_data)
def test_nth_smallest(arr, n, expected):
    assert nth_smallest(arr, n) == expected


@pytest.mark.parametrize('arr, n, expected', test_data)
def test_nth_smallest_order_n(arr, n, expected):
    assert nth_smallest(arr, n) == expected
