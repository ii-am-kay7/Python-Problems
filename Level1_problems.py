def old_macdonalds(name):

    if len(name) >= 4:
        modified_name = name[:1].capitalize() + name[1:3] + name[3].capitalize() + name[4:]
        return modified_name
    else:
        return "Name is too short"


def master_yoda(text):
    wordlist = text.split()
    return ' '.join(wordlist[::-1])

