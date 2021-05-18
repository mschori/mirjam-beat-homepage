from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from helpers import validation_helper
from django import forms
from .models import User


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
    firstname = forms.CharField(max_length=50, required=True, label='')
    lastname = forms.CharField(max_length=50, required=True, label='')
    email = forms.EmailField(max_length=150, required=True, label='')
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput, label='')
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput, label='')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Email already exist.'), code='invalid')
        return email

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
