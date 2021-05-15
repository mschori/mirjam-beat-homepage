from users.models import User
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from users.tokens import email_confirm_token


def send_signup_mail(user: User, domain: str):
    message = render_to_string('emails/signup.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_confirm_token
    })
    email = EmailMessage(
        _('Verify your Email'),
        message,
        f'Schori-Liem <michael.schori@gmx.ch>',
        to=[user.email]
    )
    email.send()
