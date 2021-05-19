from django import template
from helpers import env_helper

register = template.Library()


def is_debug_mode_on(value):
    """
    Check if DEBUG-Mode is on True in Environment-Variables.
    :return: boolean
    """
    return env_helper.is_debug_mode_on()


register.filter(is_debug_mode_on)
