from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext as _
from users.tokens import email_confirm_token
from django.contrib.auth import get_user
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from helpers import email_helper
from .forms import UserRegistrationForm
from .models import User
from .tokens import reset_password_token


def signup(request):
    """
    View for signup a new user.
    :param request: request from user
    :return: rendered signup-form
    """
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
    """
    Resend confirm-email.
    :param request: request from user
    :return: redirect to home
    """
    user = get_user(request)
    if user.email_confirmed:
        messages.warning(request, _('Your email is already confirmed.'))
    else:
        domain = get_current_site(request).domain
        email_helper.send_signup_mail(user, domain)
        messages.success(request, _('We have send you an email to confirm your email-address.'))
    return redirect('home')


def confirm_email(request, uidb64, token):
    """
    Confirm email-address.
    :param request: request from user
    :param uidb64: id as uidb64
    :param token: email-token
    :return: return to home
    """
    try:
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and email_confirm_token.check_token(user, token):
        user.email_confirmed = True
        user.save()
        messages.success(request, _('Your email is now confirmed. Thank you!'))
    else:
        messages.error(request, _('Your link is invalid or expired.'))
    return redirect('home')


def reset_password(request):
    """
    View for reset_password.
    If POST:
        Send email to user with reset-token.
    :param request:
    :return: render or redirect to reset_password (self)
    """
    if request.method == 'POST':
        email = request.POST.get('email', None)
        try:
            user = User.objects.get(email=email)
            domain = get_current_site(request).domain
            email_helper.send_reset_password_mail(user, domain)
            messages.success(request, _('Yout got an email from us. Please check you spam-folder if needed.'))
            return redirect('reset_password')
        except User.DoesNotExist:
            messages.error(request, _('There is no account registered with this email.'))
            return redirect('reset_password')
    else:
        form = PasswordResetForm()
    return render(request, 'users/reset_password.html', {'form': form})


def reset_password_confirm(request, uidb64, token):
    """
    View for confirm password reset.
    :param request: request from user
    :param uidb64: user-id as uidb64
    :param token: generated user-token from email
    :return: If token is valid:
                rendered view to confrim password reset
             else:
                redirect to home
    """
    try:
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=user_id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and reset_password_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, _('Your password is successfully changed.'))
                return redirect('login')
            else:
                messages.error(request, _('Please check your inputs. The password is not valid.'))
        form = SetPasswordForm(user)
        return render(request, 'users/reset_password_confirm.html', {'form': form})
    else:
        messages.warning(request, _('Your link is invalid or expired.'))
        return redirect('reset_password')
