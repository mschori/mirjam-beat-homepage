import re


def is_password_valid(password: str):
    """
    Check if password is valid.
    Password must contain at least:
    - 8 characters
    - 1 lower case character
    - 1 upper case character
    - 1 numeric character
    :param password: password to check
    :return: boolean
    """
    if len(password) < 8 or \
            re.search('[A-Z]', password) is None or \
            re.search('[a-z]', password) is None or \
            re.search('[0-9]', password) is None:
        return False
    return True
