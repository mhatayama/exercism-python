def distance(strand_a, strand_b):
    """Gets the differences between two strands of DNA

    Args:
        strand_a (str): The string of the first strand
        strand_b (str): The string of the second strand

    Returns:
        int: A number of the differences between two strands

    Raises:
        ValueError: An error occurred two strands have different lengths.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Two strands have different lengths.")
    diffs = [x for x in range(0, len(strand_a)) if strand_a[x] != strand_b[x]]
    return len(diffs)
