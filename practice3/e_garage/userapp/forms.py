
from django.db import transaction
from django import forms
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserCreationForm

class OwnerRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = '__all__'


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner = True
        user.save()
        return user

class CustomerRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = '__all__'

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user
