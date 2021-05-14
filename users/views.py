from django.shortcuts import render
from .forms import UserRegistrationForm


def signup(request):
    form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})
