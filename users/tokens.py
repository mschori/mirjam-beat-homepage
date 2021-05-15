from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User


class EmailConfirmTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return int(user.pk) + int(timestamp) + bool(user.email_confirmed)


email_confirm_token = EmailConfirmTokenGenerator()
