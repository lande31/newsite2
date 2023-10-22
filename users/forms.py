from django import forms
from .models import Customer
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.db import models






class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    phone = forms.CharField(min_length=12)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email','phone', 'password1', 'password2')

