DICT_SCORES = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10}


def score(word):
    sum = 0
    word = word.upper()
    for i in range(len(word)):
        for letters, score in DICT_SCORES.items():
            if word[i] in letters:
                sum = sum + score
                break
    return sum
