class RomanNumerals:
    def convert(self, number: int) -> str:
        numeral = ''

        while number >= 100:
            numeral += 'C'
            number -= 100

        if number >= 50:
            numeral += 'L'
            number -= 50

        while number >= 10:
            numeral += 'X'
            number -= 10

        if number >= 5:
            numeral += 'V'
            number -= 5

        return numeral + 'I' * number
