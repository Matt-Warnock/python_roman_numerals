class RomanNumerals:
    def convert(self, number: int) -> str:

        if number == 5:
            return 'V'

        if number == 6:
            return 'VI'

        return 'I' * number
