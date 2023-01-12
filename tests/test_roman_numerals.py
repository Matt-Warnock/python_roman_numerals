from python_roman_numerals.roman_numerals import RomanNumerals


class TestRomanNumerals:
    def test_converts_one_to_i(self):
        number = 1
        assert RomanNumerals().convert(number) == "I"

    def test_converts_two_to_ii(self):
        number = 2
        assert RomanNumerals().convert(number) == "II"

    def test_converts_two_to_iii(self):
        number = 3
        assert RomanNumerals().convert(number) == "III"

    def test_converts_five_to_v(self):
        number = 5
        assert RomanNumerals().convert(number) == "V"