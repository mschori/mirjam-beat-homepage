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


email_confirm_token = EmailConfirmTokenGenerator()
