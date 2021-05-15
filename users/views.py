from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext as _
from users.tokens import email_confirm_token
from django.contrib.auth import get_user
from django.contrib import messages
from helpers import email_helper
from .forms import UserRegistrationForm
from .models import User


def signup(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                is_active=True
            )
            user.save()
            domain = get_current_site(request).domain
            email_helper.send_signup_mail(user, domain)
            messages.success(request, _('We have send you an email to confirm your registration.'))
            return redirect('login')
        else:
            messages.error(request, _('Form is not valid. Please check your inputs.'))
    return render(request, 'registration/signup.html', {'form': form})


def resend_confirm_email(request):
    user = get_user(request)
    if user.email_confirmed:
        messages.warning(request, _('Your email is already confirmed.'))
    else:
        domain = get_current_site(request).domain
        email_helper.send_signup_mail(user, domain)
        messages.success(request, _('We have send you an email to confirm your email-address.'))
    return redirect('home')


def confirm_email(request, uidb64, token):
    user = None
    try:
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.warning(request, _('Your link is invalid or expired.'))
    if email_confirm_token.check_token(user, token):
        user.email_confirmed = True
        user.save()
        messages.success(request, _('Your email is now confirmed. Thank you!'))
    return redirect('home')
