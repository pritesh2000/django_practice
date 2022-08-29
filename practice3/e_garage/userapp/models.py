from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from generic.models import BaseField


# Create your models here.

class User(AbstractUser, BaseField):
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    class Meta():
        db_table = "User"

class OwnerRegistraion(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="owner")
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be in 10 digit.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, unique=True, max_length=10)

    class Meta():
        db_table = "owner"

class CustomerRegistration(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be in format of : '9999999999'")
    phone_number = models.CharField(validators=[phone_regex] ,max_length=10, blank=True, unique=True)

    class Meta():
        db_table = "customer"
