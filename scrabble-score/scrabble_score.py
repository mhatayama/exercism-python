DICT_SCORES = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10}


def score(word):
    chars = [x.upper() for x in word if x.isalpha()]
    return sum(map(lambda x: _score_by_letter(x), chars))


def _score_by_letter(letter):
    for letters, score in DICT_SCORES.items():
        if letter in letters:
            return score
