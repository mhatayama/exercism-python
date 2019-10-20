class Phone(object):
    def __init__(self, phone_number):
        digits = [x for x in phone_number if x.isnumeric()]
        if digits[0] == '1':
            digits = digits[1:]
        if len(digits) != 10 or digits[0] in '01' or digits[3] in '01':
            raise ValueError("Invalid")

        self.number = "".join(digits)
        self.area_code = self.number[:3]

    def pretty(self):
        return "(%s) %s-%s" % (self.area_code, self.number[3:6], self.number[6:])
