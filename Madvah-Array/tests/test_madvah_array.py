import pytest

from madvah_array import is_madvah_array

test_data = [([], False), ([1, ], False) , ([1, 2, ], False),
             ([2, 1, 1], True), ([2, 1, 1, 4, -1, -1], True)]



@pytest.mark.parametrize('input_list, expected', test_data)
def test_is_madvah_array(input_list, expected):
    assert is_madvah_array(input_list) == expected
