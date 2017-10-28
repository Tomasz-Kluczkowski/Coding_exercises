import pytest

from is_merge import is_merge


test_data = [('codewars', 'code', 'wars', True),
             ('codewars', 'cdw', 'oears', True),
             ('codewars', 'cod', 'wars', False),
             ('aadbcdef', 'adbc', 'adef', True),
             ('bananas', 'bas', 'anan', True),
             ('bananas from bahamas', 'bfbs', 'ananas rom ahama', True),
             ('bananas from bahamas', 'nas', 'bana from bahamas', True),
             ('bananas from bahamas', 'bhm', 'ananas from baaas', True)]

@pytest.mark.parametrize("complete, part1, part2, expected", test_data)
def test_is_merge(complete, part1, part2, expected):
    """Test if part1 and part2 can be merged into complete maintaining order."""

    assert is_merge(complete, part1, part2) == expected


