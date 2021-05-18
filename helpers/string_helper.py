from django.utils.translation import ugettext_lazy


def cust_string_end(string: str, max_length: int, with_ellipsis: bool = False) -> str:
    """
    Cut given string to the given max-lenght.
    Cutting on end of string.
    :param string: string to cut
    :param max_length: max-length of string
    :param with_ellipsis: adding ellipsis
    :return: cutted string
    """
    cutted_string = f'{string[:max_length]}...' if with_ellipsis else f'{string[:max_length]}'
    return cutted_string if len(string) - 3 > max_length else string


def cut_string_start(string: str, max_length: int, with_ellipsis: bool = False) -> str:
    """
    Cut given string to given max-length.
    Cutting on start of string.
    :param string: string to cut
    :param max_length: max-length of string
    :param with_ellipsis: adding ellipsis
    :return: cutted string
    """
    cutted_string = f'{string[max_length:]}...' if with_ellipsis else f'{string[max_length:]}'
    return cutted_string if len(string) - 3 > max_length else string


def translate_lazy_string(string: str) -> str:
    """
    Translate given string with django-lazy-method.
    :param string: string to translate
    :return: translated string
    """
    return ugettext_lazy(string)
