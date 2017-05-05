def camelize(needsCamelizing):
    if isinstance(needsCamelizing, dict):
        return cameldict(needsCamelizing)
    elif isinstance(needsCamelizing, list):
        return [camelize(el) for el in needsCamelizing]
    elif isinstance(needsCamelizing, str):
        return camelcase(needsCamelizing)
    else:
        return None


def camelcase(snake_str, upper=True):
    """
    Format a string from snake case to upper or lower camelCase
    """
    # UpperCamelCase
    if upper:
        return snake_str.title().replace('_', '')

    # lowerCamelCase requires splitting the string into 2 parts
    head, *body = snake_str.split('_', maxsplit=1)

    # Make the first word lower, then capitalize all other words
    return ''.join([
        head.lower(),
        body.title().replace('_', '') if len(body) else body
    ])


def cameldict(snake_dict, upper=True):
    return {camelcase(key): camelize(value)
            for key, value
            in snake_dict.items()}
