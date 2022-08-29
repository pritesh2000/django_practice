from django.db import models
from django.contrib.auth.models import AbstractUser

from generic.models import BaseField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser, BaseField):

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(_('email'), max_length=128, unique=True)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    password = models.CharField(max_length=264)

    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message='Phone number must be in 10 digit and starts with 7,8 or 9.')
    phone_number = models.CharField(validators=[phone_regex], max_length=10, unique=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    class Meta():
        db_table = 'User'

    def __str__(self):
        return self.username
    

