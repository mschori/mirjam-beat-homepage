from django.shortcuts import render, redirect
from helpers import env_helper
from wishlist.models import Contribution
import os


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
    print('hey')
    if env_helper.is_debug_mode_on():
        bankname = os.environ.get('BANK_NAME')
        iban = os.environ.get('BANK_IBAN')
        to = os.environ.get('BANK_TO')
        contribution = Contribution.objects.first()
        return render(request, 'wishlist/thanks_you.html',
                      {'contribution': contribution, 'bankname': bankname, 'iban': iban, 'to': to})
    return redirect('home')
