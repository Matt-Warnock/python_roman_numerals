import pytest

from python_roman_numerals.roman_numerals import RomanNumerals


@pytest.fixture()
def roman_numeral() -> RomanNumerals:
    return RomanNumerals()
