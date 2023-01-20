class RomanNumerals:
    def convert(self, number: int) -> str:
        numeral = ''

        if number >= 10:
            numeral = 'X'
            number -= 10

        if number >= 5:
            numeral = 'V'
            number -= 5

        return numeral + 'I' * number
