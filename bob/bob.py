def response(hey_bob):
    stripped = hey_bob.strip()
    if stripped == '':
        return "Fine. Be that way!"
    elif stripped.isupper():
        if stripped.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif stripped.endswith('?'):
        return "Sure."
    else:
        return "Whatever."
