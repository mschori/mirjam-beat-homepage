from django.shortcuts import render, redirect
from helpers import env_helper


def home(request):
    """
    View for home.
    :param request: request from user
    :return: rendered home-view
    """
    return render(request, 'home.html')


def email_visual_test(request):
    """
    View for testing email visuals.
    Will not be used in live-mode.
    :param request: request from user
    :return: rendered email
    """
    if env_helper.is_debug_mode_on():
        return render(request, 'emails/babywishlist_thankyou_2.html')
    return redirect('home')
