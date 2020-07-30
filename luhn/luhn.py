import re

VALID_PATTERN = re.compile(r'^[0-9 ]+$')


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if not VALID_PATTERN.match(self.card_num):
            return False

        digits = [int(digit) for digit in self.card_num if digit.isnumeric()]
        digits.reverse()  # read right to left

        if len(digits) < 2:
            return False

        checksum = sum([self.__calc(index, digit)
                        for index, digit in enumerate(digits)])
        return checksum % 10 == 0

    def __calc(self, index, digit):
        if index % 2 == 0:
            return digit
        else:
            return (digit * 2 - 9) if digit * 2 > 9 else digit * 2
