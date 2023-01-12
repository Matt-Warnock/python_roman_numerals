class RomanNumerals:
    def convert(self, number: int) -> str:

        if number == 5:
            return 'V'

        return 'I' * number
