class RomanNumerals:
    def convert(self, number: int) -> str:
        numeral = ''
        tuples = ((100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'))

        for tup in tuples:
            while number >= tup[0]:
                numeral += tup[1]
                number -= tup[0]

        return numeral + 'I' * number
