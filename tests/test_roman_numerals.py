from python_roman_numerals.roman_numerals import RomanNumerals


class TestRomanNumerals:
    def test_foo(self):
        number = 1
        assert RomanNumerals().convert(number) == "I"
