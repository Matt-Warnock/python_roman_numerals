import pytest


class TestRomanNumerals:
    tests = [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (10, 'X')
    ]

    test_names = [
        'Converts 1 to I',
        'Converts 2 to II',
        'Converts 3 to III',
        'Converts 5 to V',
        'Converts 6 to VI',
        'Converts 7 to VII',
        'Converts 10 to X'
    ]

    @pytest.mark.parametrize('number, numeral', tests, ids=test_names)
    def test_all_numbers_to_numerals(self, number, numeral, roman_numeral):
        assert roman_numeral.convert(number) == numeral

