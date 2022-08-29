from django.db import models
from django.contrib.auth.models import AbstractUser

from generic.models import BaseField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from django.db.models.signals import pre_save, post_save, pre_delete

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
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta():
        db_table = 'User'

    def __str__(self):
        return self.username
    

class OneField(models.Model):
    title=models.CharField(max_length=30)

    class Meta():
        db_table="one"

class Student(models.Model):
    name = models.CharField(max_length=10)
    city = models.IntegerField()
    roll = models.CharField(max_length=100)
    
    class Meta():
        db_table = 'student'

class Customer(models.Model):
    name = models.CharField(max_length=10)
    serial_no = models.IntegerField()
    site = models.CharField(max_length=10)

    class Meta():
        db_table = 'customer'

def onefield_pre(sender, instance, *args, **kwargs):
    print("Pre is working")

def onefield_post(sender, instance, *args, **kwargs):
    print('Post is working')

def onefield_delete(sender, instance, *args, **kwargs):
    print("Deleted")

post_save.connect(onefield_post, sender=OneField)

pre_save.connect(onefield_pre, sender=OneField)

pre_delete.connect(onefield_delete, sender=OneField)