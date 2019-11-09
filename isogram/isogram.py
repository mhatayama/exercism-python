import re

# Matches any alphanumeric character that appears multiple times
duplicate_characters = re.compile(r'(\w).*\1', re.IGNORECASE)


def is_isogram(string):
    """Checks if a string is an isogram, which is a word or phrase without
    a repeating letter."""
    return duplicate_characters.search(string) == None
