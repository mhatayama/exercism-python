SCORES = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}


score_by_letters = {letter: score for (letter, score)
                    in SCORES.items() for letter in letter}


def score(word):
    chars = [x.upper() for x in word if x.isalpha()]
    return sum(map(lambda x: score_by_letters[x], chars))
