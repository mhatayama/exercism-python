def find_anagrams(word, candidates):
    return [x for x in candidates if is_anagram(word, x)]


def is_anagram(word, candidate):
    return (sorted(word.lower()) == sorted(candidate.lower())
            and word.lower() != candidate.lower())
