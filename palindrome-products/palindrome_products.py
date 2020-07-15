def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid")

    value = -1
    factors = []
    for x in range(min_factor, max_factor + 1):
        for y in range(x, max_factor + 1):
            num = x * y
            if value > num:
                continue
            if is_palindrome(num):
                if value < num:
                    value = num
                    factors = []
                factors.append([x, y])

    return None if len(factors) == 0 else value, factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Invalid")

    value = max_factor * max_factor + 1
    factors = []
    for x in range(min_factor, max_factor + 1):
        for y in range(x, max_factor + 1):
            num = x * y
            if value < num:
                continue
            if is_palindrome(num):
                if value > num:
                    value = num
                    factors = []
                factors.append([x, y])

    return None if len(factors) == 0 else value, factors


def is_palindrome(number):
    return str(number) == str(number)[::-1]
