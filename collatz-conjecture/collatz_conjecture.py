def steps(number, cnt=0):
    if number < 1:
        raise ValueError("invalid")
    elif number == 1:
        return cnt
    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return steps(number, cnt + 1)
