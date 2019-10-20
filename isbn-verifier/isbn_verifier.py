def is_valid(isbn):
    isbn = [x for x in isbn if x.isnumeric() or x == 'X']
    if len(isbn) != 10 or 'X' in isbn[:9]:
        return False
    checksum = 10 if isbn[9] == 'X' else isbn[9]
    digits = isbn[:9] + [checksum]
    _sum = sum([int(digits[i]) * (10 - i) for i in range(0, 10)])
    return _sum % 11 == 0
