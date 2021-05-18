from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User


class EmailConfirmTokenGenerator(PasswordResetTokenGenerator):
    """
    TokenGenerator for email-confirmation.
    """

    def _make_hash_value(self, user: User, timestamp: int):
        """
        Create token for email confirmation.
        :param user: user-object
        :param timestamp: timestamp for token
        :return: genertaed token
        """
        return (
                int(user.pk) + int(timestamp) + bool(user.email_confirmed)
        )


class ResetPasswordTokenGenerator(PasswordResetTokenGenerator):
    """
    TokenGenerator for reset-password.
    """

    def _make_hash_value(self, user, timestamp):
        """
        Create token for reset_password.
        :param user: user-object
        :param timestamp: timestamp for token
        :return: generated token
        """
        return str(int(user.pk) + int(timestamp)) + str(user.last_login)


email_confirm_token = EmailConfirmTokenGenerator()
reset_password_token = ResetPasswordTokenGenerator()
