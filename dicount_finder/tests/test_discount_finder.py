"""

input
"15 20 60 75 80 100"
"9 9 12 12 12 15 16 20"

output
"15 60 75"
"9 9 12 15"
def find_discounted(prices):
    #your code here

"""
import pytest
from dicount_finder.discount_finder import find_discounted

data = [
    ("15 20 60 75 80 100", "15 60 75"),
    ("9 9 12 12 12 15 16 20", "9 9 12 15")
]


@pytest.mark.parametrize('input, expected', data)
def test_dicount_finder(input, expected):
    assert find_discounted(input) == expected
