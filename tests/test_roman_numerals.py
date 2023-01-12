from python_roman_numerals.roman_numerals import RomanNumerals


class TestRomanNumerals:
    def test_converts_one_to_i(self):
        number = 1
        assert RomanNumerals().convert(number) == "I"


    def test_converts_two_to_ii(self):
        number = 2
        assert RomanNumerals().convert(number) == "II"