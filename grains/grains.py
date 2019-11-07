def square(number):
    if number < 1 or number > 64:
        raise ValueError("invalid")
    return 2 ** (number - 1)


def total():
    return sum([square(n) for n in range(1, 65)])  # 2 ** 64 - 1
