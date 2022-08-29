from .models import User, Owner, Customer

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
                        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_no=self.cleaned_data.get('phone_no')
        customer.save()
        return user

        # what wil be returned here is doubtfull


class OwnerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # phone_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_owner = True
        user.save()
        owner = Owner.objects.create(user=user)
        # owner.phone_no=self.cleaned_data.get('phone_no')  # not neccesarry because we didn't take it in models.py
        owner.save()
        return owner