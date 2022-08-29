from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

    class Meta():
        db_table = 'owner'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_no = models.CharField(max_length=256)
    
    def __str__(self):
        return self.user.username

    class Meta():
        db_table = 'customer'
