import pytest

from chars_equal_frequency.chars_equal_frequency import solve


def test_simple_inputs():
    assert solve('abc')
