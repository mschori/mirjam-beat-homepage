from django.shortcuts import render


def home(request):
    """
    View for home.
    :param request: request from user
    :return: rendered home-view
    """
    return render(request, 'home.html')
