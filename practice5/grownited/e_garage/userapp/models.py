from django.db import models
from django.contrib.auth.models import AbstractUser
from generic.models import BaseField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.

class User(AbstractUser, BaseField):
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    profile_pic = models.ImageField()

    phone_regex = RegexValidator(regex=r'^[6-9]{1}\d{9}', message='Phone number must be in 10 digit')
    phone_number = models.CharField(validators=[phone_regex], max_length=10, unique=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta():
        db_table = "User"

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    garage_name = models.CharField(max_length=128)
    garage_email = models.EmailField(max_length=128, unique=True)
    

    class Meta():
        db_table = "owner"

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta():
        db_table = "customer"

    def __str__(self):
        return self.user.username
    