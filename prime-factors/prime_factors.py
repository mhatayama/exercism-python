def factors(value):
    factors = []
    if value < 2:
        return factors

    dividend = value
    divider = 2
    while dividend != 1:
        if dividend % divider == 0:
            factors.append(divider)
            dividend /= divider
        else:
            divider += 1
    return factors
