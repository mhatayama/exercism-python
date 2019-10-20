def classify(number):
    if number <= 0:
        raise ValueError("invalid number")

    factors = [x for x in range(1, int(number / 2) + 1) if number % x == 0]
    aliquotSum = sum(factors)
    if aliquotSum == number:
        return 'perfect'
    elif aliquotSum > number:
        return 'abundant'
    else:
        return 'deficient'
