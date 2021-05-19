import os


def is_debug_mode_on():
    """
    Check if DEBUG-Mode is on True in Environment-Variables.
    :return:
    """
    return os.environ.get('DEBUG') == '1' or os.environ.get('DEBUG') == 'True'
