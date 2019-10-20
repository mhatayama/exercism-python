DICT_TRANS = {
    "Methionine":   ["AUG"],
    "Phenylalanine":["UUU", "UUC"],
    "Leucine":      ["UUA", "UUG"],
    "Serine":       ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine":     ["UAU", "UAC"],
    "Cysteine":     ["UGU", "UGC"],
    "Tryptophan":   ["UGG"]}
STOPPERS = ["UAA", "UAG", "UGA"]

def proteins(strand):
    result = []
    for i in range(0, len(strand), 3):
        nucleotides = strand[i:i+3]
        for k, v in DICT_TRANS.items():
            if nucleotides in v: result.append(k)
        if nucleotides in STOPPERS: break
    return result
