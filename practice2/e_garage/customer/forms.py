from .models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)

    class Meta():
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)

    class Meta():
        model = User
        fields = ['username', 'email', 'phone_number', 'password', 'is_superuser', 'is_staff', 'is_active']
        