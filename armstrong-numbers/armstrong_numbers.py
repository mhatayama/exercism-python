def is_armstrong_number(number):
    pow = len(str(number))
    return number == sum([int(n) ** pow for n in list(str(number))])
