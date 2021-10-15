from os import X_OK
from django.contrib.auth import forms
from django.contrib.auth import models
from django.core.exceptions import ImproperlyConfigured
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import Textarea
from .models import Contact_Forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Contact Form



class FormContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Forms
        fields = ["first_name", "last_name", "email", "phone", "address", "message"]