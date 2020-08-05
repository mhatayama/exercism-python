class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if not self.card_num.isnumeric():
            return False

        digits = [int(digit) for digit in self.card_num]
        digits.reverse()  # read right to left

        if len(digits) < 2:
            return False

        checksum = sum([digit if index % 2 == 0 else
                        (digit * 2 - 9 if digit * 2 > 9 else digit * 2)
                        for index, digit in enumerate(digits)])
        return checksum % 10 == 0
