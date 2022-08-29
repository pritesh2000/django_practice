from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from userapp.models import Customer, Owner, User


class OwnerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=10)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    profile_pic = forms.ImageField(required=False)

    garage_name = forms.CharField(required=True)
    garage_email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User

        # this is not working for removing help text
        """
        fields = ('username', 'password1', 'password2')
        # exclude = ("username.help_text", 'password.help_text', 'password2.help_text')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
        """
    # working perfectly with init function for removing help text
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text=None
        self.fields['password1'].help_text=None    
        self.fields['password2'].help_text=None
    
    # print(UserCreationForm())

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner= True
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.profile_pic = self.cleaned_data.get('profile_pic')
        user.save()
        
        owner = Owner.objects.create(user=user)
        owner.garage_name=self.cleaned_data.get('garage_name')
        owner.garage_email=self.cleaned_data.get('garage_email')
        owner.save()
        return owner

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=10)
    first_name = forms.CharField(required=False)
    last_name= forms.CharField(required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer=True
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.profile_pic = self.cleaned_data.get('profile_pic')
        user.save()

        customer = Customer.objects.create(user=user)        
        return user
