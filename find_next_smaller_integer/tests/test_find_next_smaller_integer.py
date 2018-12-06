import pytest

from find_next_smaller_integer.find_next_smaller_integer import next_smaller


class TestFindSmallerInt:

    def test_too_short_num(self):
        assert next_smaller(5) == -1
        assert next_smaller(10) == -1

    def test_simple_number(self):
        assert next_smaller(21) == 12
        assert next_smaller(315) == 153
        assert next_smaller(2071) == 2017
        assert next_smaller(1207) == 1072


    def test_mid_complexity_numbers(self):
        assert next_smaller(1234567908) == 1234567890
        assert next_smaller(12345679008) == 12345678900
        assert next_smaller(12345679118) == 12345678911

    def test_more_complex_numbers(self):
        assert next_smaller(12345679658) == 12345679568
