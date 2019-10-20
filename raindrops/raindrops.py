FACTORS = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

def convert(number):
    result = [FACTORS[n] for n in FACTORS if number % n == 0]
    return ''.join(result) or str(number)
