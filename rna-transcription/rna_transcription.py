MAP = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand):
    return ''.join([MAP[x] for x in list(dna_strand)])
