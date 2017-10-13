import pytest

from memo_fibonacci import fibonacci


def test_base_cases():
    """Test base cases of fibonacci function."""

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

# 0, 1, 1, 2, 3, 5, 8, 13, 21

test_data = {(2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21)}

@pytest.mark.parametrize('n, expected', test_data)
def test_fibonacci(n, expected):
    """Test fibonacci function for any n > 1."""

    assert fibonacci(n) == expected
