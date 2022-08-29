from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'phone_number', 'password', 'is_superuser', 'is_staff', 'is_active']
        