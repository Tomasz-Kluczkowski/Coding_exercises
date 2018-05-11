import pytest

from form_largest_num import max_number

test_data = [(213, 321),
             (7389, 9873)]


@pytest.mark.parametrize('input_num, expected', test_data)
def test_maxNumber(input_num, expected):
    assert max_number(input_num) == expected
