class RomanNumerals:
    def convert(self, number_input: int) -> str:
        numbers_to_numerals = ((100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'))
        result = ''

        for (number, numeral) in numbers_to_numerals:
            while number_input >= number:
                result += numeral
                number_input -= number

        return result + 'I' * number_input
