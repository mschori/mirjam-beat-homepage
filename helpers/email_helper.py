from users.models import User
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from users.tokens import email_confirm_token, reset_password_token
from baby_wishlist.models import Contribution
import os


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
    from_mail = f'Schori-Liem <{os.environ.get("SCHORI_LIEM_EMAIL")}>'
    email = EmailMessage(
        _('Verify your Email'),
        message,
        from_mail,
        to=[user.email]
    )
    email.send()


def send_admin_info_for_signup(user: User):
    """
    Send Signup-Info to admin.
    :param user: user-object
    """
    messages = render_to_string('emails/signup_admin_info.html', {
        'user': user
    })
    from_mail = f'Schori-Liem <{os.environ.get("SCHORI_LIEM_EMAIL")}>'
    email = EmailMessage(
        'New user registered',
        messages,
        from_mail,
        to=[os.environ.get('ADMIN_EMAIL_RECEIVER')]
    )
    email.send()


def send_babywishlist_thank_you_mail(user: User, domain: str, contribution: Contribution):
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
    from_mail = f'Babywishlist Schori-Liem <{os.environ.get("BABYWISHLIST_EMAIL")}>'
    email = EmailMessage(
        _('Thank you!'),
        message,
        from_mail,
        to=[user.email]
    )
    email.content_subtype = 'html'
    email.send()


def send_admin_info_for_babywishlist_contribution(contribution: Contribution):
    """
    Send contribution-info to admin.
    :param contribution: contribution-object
    """
    message = render_to_string('emails/babywishlist_contribution_admin_info.html', {
        'contribution': contribution
    })
    from_mail = f'Babywishlist Schori-Liem <{os.environ.get("BABYWISHLIST_EMAIL")}>'
    email = EmailMessage(
        'New Contribution on schori-liem.ch',
        message,
        from_mail,
        to=[os.environ.get('ADMIN_EMAIL_RECEIVER')]
    )
    email.send()


def send_admin_info_for_babywishlist_contribution_delete(contribution: Contribution):
    """
    Send contribution-info to admin when contribution is deleted.
    :param contribution: contribution-object
    """
    message = render_to_string('emails/babywishlist_contribution_delete_admin_info.html', {
        'contribution': contribution
    })
    from_mail = f'Babywishlist Schori-Liem <{os.environ.get("BABYWISHLIST_EMAIL")}>'
    email = EmailMessage(
        'Contribution deleted!',
        message,
        from_mail,
        to=[os.environ.get('ADMIN_EMAIL_RECEIVER')]
    )
    email.send()


def send_reset_password_mail(user: User, domain: str):
    """
    Send reset-password-mail.
    :param user: user-object
    :param domain: domain from request
    """
    message = render_to_string('emails/reset_password.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': reset_password_token.make_token(user)
    })
    from_mail = f'Schori-Liem <{os.environ.get("SCHORI_LIEM_EMAIL")}>'
    email = EmailMessage(
        _('Reset your password.'),
        message,
        from_mail,
        to=[user.email]
    )
    email.send()
