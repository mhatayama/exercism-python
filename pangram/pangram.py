def is_pangram(sentence):
    uniq = [x for x in set(sentence.upper()) if x.isalpha()]
    return len(uniq) == 26
