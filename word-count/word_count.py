import re

def count_words(sentence):
    counter = dict()
    for word in re.split(r'[\s\,\:\!\&\@\$\%\^\.\_]', sentence.lower()):
        word = word.strip("'")
        if len(word) > 0:
            counter[word] = counter.get(word, 0) + 1
    return counter
