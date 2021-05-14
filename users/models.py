from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model User.
    Stores all informations about a user.
    Custom User-Model / Backend.
    """
    email = models.EmailField(_('email address'), unique=True)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    phone_mobile = PhoneNumberField(null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    email_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.firstname + ' ' + self.lastname
