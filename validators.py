# Separator validator function. Separator must be ':' or '-'.
def separatorValidate(txt):
    if ':' in txt and '-' in txt:
        return False
    elif '-' in txt:
        return (True, '-')
    elif ':' in txt:
        return (True, ':')
    else:
        return False