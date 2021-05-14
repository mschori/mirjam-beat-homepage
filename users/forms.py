from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from helpers import validation_helper
from django import forms
from .models import User
import re


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('firstname', 'lastname', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email')


class UserRegistrationForm(forms.Form):
    """
    Class for user-registration-form.
    Fields: firstname, lastname, email, password1, password2, license_plate.
    Can be used for views.
    """
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=150, required=True)
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    phone_mobile = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Email already exist.'), code='invalid')
        return email

    def clean_phone_mobile(self):
        phone_mobile = self.cleaned_data['phone_mobile']
        if not re.match('^\+\d{9,15}$', phone_mobile):
            raise ValidationError(_('Phone number is not valid.'), code='invalid')
        return phone_mobile

    def clean(self):
        form_data = self.cleaned_data
        message_password1 = _('Password is not valid.')
        message_password2 = _('Passwords are not equal.')
        if not validation_helper.is_password_valid(form_data['password1']):
            self._errors['password1'] = self.error_class([message_password1])
            raise ValidationError(message_password1, code='invalid')
        if form_data['password1'] != form_data['password2']:
            self._errors['password2'] = self.error_class([message_password2])
            raise ValidationError(message_password2, code='invalid')
        return form_data
