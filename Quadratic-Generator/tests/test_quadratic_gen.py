import pytest

from quadratic_gen import quadratic_gen



data_set = [
    (1, 0, 0, 10, [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]])
]

@pytest.mark.parametrize('a, b, c, num_of_iterations, expected', data_set)
def test_quadratic_gen(a, b, c, num_of_iterations, expected):
    gen = quadratic_gen(a, b, c)
    assert [next(gen) for _ in range(num_of_iterations)] == expected
