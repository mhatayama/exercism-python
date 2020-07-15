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

    return None if value == -1 else value, factors


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

    return None if value == max_factor * max_factor + 1 else value, factors


def is_palindrome(number):
    number_str = str(number)
    for i in range(int(len(number_str) / 2)):
        if number_str[i] != number_str[len(number_str) - i - 1]:
            return False
    return True
