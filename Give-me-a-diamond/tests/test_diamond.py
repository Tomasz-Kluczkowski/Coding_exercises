import pytest

import diamond

test_invalid_input_data = {(-1, None), (0, None), (2, None)}

@pytest.mark.parametrize('n, expected', test_invalid_input_data)
def test_diamond_invalid_input(n):
    """Check if function diamond returns None on an invalid input."""

    assert diamond
