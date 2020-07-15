def largest(min_factor, max_factor):
    return find_palindromes(min_factor, max_factor, lambda a, b: a < b)


def smallest(min_factor, max_factor):
    return find_palindromes(min_factor, max_factor, lambda a, b: a > b)


def find_palindromes(min_factor, max_factor, op):
    if min_factor > max_factor:
        raise ValueError("Invalid")

    value = None
    factors = []
    for x in range(min_factor, max_factor + 1):
        for y in range(x, max_factor + 1):
            num = x * y
            if is_palindrome(num):
                if value is None or op(value, num):
                    value = num
                    factors = [[x, y]]
                elif value == num:
                    factors.append([x, y])

    return value, factors


def is_palindrome(number):
    return str(number) == str(number)[::-1]
