from python_roman_numerals.roman_numerals import RomanNumerals

class TestRomanNumerals:
    def test_all_numbers_to_numerals(self):
        numbers = [1,2,3,5,6,7]
        numerals = ['I','II','III','V','VI','VII']

        for i in range(len(numbers)):
            assert RomanNumerals().convert(numbers[i]) == numerals[i]
