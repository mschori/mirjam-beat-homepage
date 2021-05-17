from users.models import User
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from users.tokens import email_confirm_token
from baby_wishlist.models import Contribution


def send_signup_mail(user: User, domain: str):
    """
    Send Signup-Mail.
    :param user: user-object
    :param domain: domain from request
    """
    message = render_to_string('emails/signup.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_confirm_token.make_token(user)
    })
    email = EmailMessage(
        _('Verify your Email'),
        message,
        f'Schori-Liem <michael.schori.89@gmail.com>',
        to=[user.email]
    )
    # email.send()


def send_babywish_thank_you_mail(user: User, domain: str, contribution: Contribution):
    """
    Send babywish-thank-you-Mail.
    :param user: user-object
    :param domain: domain from request
    :param contribution: contribution-object
    """
    message = render_to_string('emails/babywishlist_thankyou.html', {
        'user': user,
        'domain': domain,
        'contribution': contribution
    })
    email = EmailMessage(
        _('Thank you!'),
        message,
        f'Schori-Liem <michael.schori.89@gmail.com>',
        to=[user.email]
    )
    # email.send()
