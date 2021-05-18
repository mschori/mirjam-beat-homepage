from django import template
from helpers import string_helper

register = template.Library()


def cut_string_end(string: str, max_length: int):
    """
    Template-Tag to cut a given string.
    Cutting on end of string.
    :param string: string to cut
    :param max_length: allowed max-length for string
    :return: cutted string
    """
    return string_helper.cust_string_end(string, max_length)


def cut_string_end_wiht_ellipsis(string: str, max_length: int):
    """
    Template-Tag to cut a given string and add ellipsis.
    Cutting on end of string.
    :param string: string to cut
    :param max_length: allowed max-length for string
    :return: cutted string
    """
    return string_helper.cust_string_end(string, max_length, True)


def cut_string_start(string: str, max_length: int):
    """
    Template-Tag to cut a given string.
    Cutting on start of string.
    :param string: string to cut
    :param max_length: allowed max-length for string
    :return: cutted string
    """
    return string_helper.cut_string_start(string, max_length)


def cut_string_start_with_ellipsis(string: str, max_length: int):
    """
    Template-Tag to cut a given String and add ellipsis.
    Cutting on start of string.
    :param string: string to cut
    :param max_length: allowed max-length for string
    :return: cutted string
    """
    return string_helper.cut_string_start(string, max_length, True)


register.filter(cut_string_end)
register.filter(cut_string_end_wiht_ellipsis)
register.filter(cut_string_start)
register.filter(cut_string_start_with_ellipsis)
